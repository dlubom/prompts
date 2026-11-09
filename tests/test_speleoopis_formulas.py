"""Check the actual expressions in the prompt against independent numeric cases."""

import ast
import math
from pathlib import Path
import re
import unittest


PROMPT = (
    Path(__file__).resolve().parents[1]
    / ".agents/skills/speleoopis/references/speleoopis.md"
).read_text(encoding="utf-8")
EXPRESSIONS = re.findall(r"`([^`\n]+)`", PROMPT)
EXPRESSIONS += re.search(r"```text\n(ΔE = .*?)\n```", PROMPT, re.S)[1].splitlines()


def formula(name, **values):
    matches = [
        text.split("=", 1)[1].strip()
        for text in EXPRESSIONS
        if text.split("=", 1)[0].strip() == name and "=" in text
    ]
    if len(matches) != 1:
        raise AssertionError(f"Expected one formula for {name}, found {matches}")
    return calculate(matches[0], **values)


def calculate(expression, **values):
    """Evaluate only arithmetic and the four named math functions, never document code."""
    expression = expression.replace("·", "*").replace("−", "-")
    expression = expression.replace("°", "").replace("modulo", "%")
    expression = re.sub(r"(?<=\d),(?=\d)", ".", expression)
    functions = {
        "sin": lambda degrees: math.sin(math.radians(degrees)),
        "cos": lambda degrees: math.cos(math.radians(degrees)),
        "atan2": math.atan2,
        "degrees": math.degrees,
    }
    tree = ast.parse(expression, mode="eval")
    allowed = (
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Add, ast.Sub, ast.Mult,
        ast.Mod, ast.USub, ast.UAdd, ast.Load, ast.Name, ast.Constant, ast.Call,
    )
    for node in ast.walk(tree):
        if not isinstance(node, allowed):
            raise ValueError(f"Unsupported expression element: {type(node).__name__}")
        if isinstance(node, ast.Call) and (
            not isinstance(node.func, ast.Name)
            or node.func.id not in functions
            or node.keywords
        ):
            raise ValueError("Unsupported function call")
        if isinstance(node, ast.Constant) and type(node.value) not in (int, float):
            raise ValueError("Only numeric constants are allowed")
    return eval(compile(tree, "<prompt formula>", "eval"), {"__builtins__": {}}, functions | values)


class SurveyFormulas(unittest.TestCase):
    def test_cardinal_directions(self):
        for azimuth, expected in (
            (0, (0, 10, 0)), (90, (10, 0, 0)),
            (180, (0, -10, 0)), (270, (-10, 0, 0)),
        ):
            with self.subTest(azimuth=azimuth):
                for name, result in zip(("ΔE", "ΔN", "ΔZ"), expected):
                    self.assertAlmostEqual(formula(name, L=10, A=azimuth, i=0), result)

    def test_inclination_and_horizontal_projection(self):
        for inclination, vertical, horizontal in (
            (-60, -8.660254037844386, 5),
            (30, 5, 8.660254037844386),
            (0, 0, 10), (90, 10, 0), (-90, -10, 0),
        ):
            with self.subTest(inclination=inclination):
                self.assertAlmostEqual(formula("ΔZ", L=10, i=inclination), vertical)
                self.assertAlmostEqual(formula("H", L=10, i=inclination), horizontal)

    def test_reverse_and_vector_length(self):
        for azimuth in (0, 37, 90, 180, 270, 359):
            for inclination in (-80, -30, 0, 35, 80):
                with self.subTest(azimuth=azimuth, inclination=inclination):
                    forward = [formula(n, L=10, A=azimuth, i=inclination)
                               for n in ("ΔE", "ΔN", "ΔZ")]
                    reverse = [formula(n, L=10, A=formula("A_rev", A=azimuth),
                                       i=formula("i_rev", i=inclination))
                               for n in ("ΔE", "ΔN", "ΔZ")]
                    self.assertAlmostEqual(sum(v*v for v in forward), 100)
                    for a, b in zip(forward, reverse):
                        self.assertAlmostEqual(a, -b)
        self.assertAlmostEqual(formula("A_rev", A=270), 90)
        self.assertAlmostEqual(formula("i_rev", i=-30), 30)

    def test_inverse_azimuth_all_quadrants(self):
        # A vertical vector has no defined azimuth and is deliberately excluded.
        for east, north, expected in (
            (0, 1, 0), (1, 1, 45), (1, 0, 90), (1, -1, 135),
            (0, -1, 180), (-1, -1, 225), (-1, 0, 270), (-1, 1, 315),
        ):
            with self.subTest(east=east, north=north):
                self.assertAlmostEqual(formula("A", ΔE=east, ΔN=north), expected)

    def test_declination_sign_and_wrap(self):
        for magnetic, correction, expected in (
            (350, 15, 5), (5, -15, 350), (90, 0, 90), (355, 5, 0),
        ):
            with self.subTest(magnetic=magnetic, correction=correction):
                self.assertAlmostEqual(formula("A_geo", A_mag=magnetic, D=correction), expected)

    def test_angular_units_and_zenith(self):
        for grads, degrees in ((0, 0), (100, 90), (200, 180), (400, 360)):
            with self.subTest(grads=grads):
                self.assertAlmostEqual(formula("kąt_stopnie", kąt_grady=grads), degrees)
        for zenith, inclination in ((0, 90), (90, 0), (150, -60), (180, -90)):
            with self.subTest(zenith=zenith):
                self.assertAlmostEqual(formula("i", z=zenith), inclination)

    def test_vertical_extent(self):
        expression = re.search(r"Deniwelację licz jako `([^`]+)`", PROMPT)[1]
        for elevations, expected in (((0, -8, -5, -12), 12), ((5, -12), 17)):
            with self.subTest(elevations=elevations):
                self.assertAlmostEqual(calculate(expression, Z_max=max(elevations),
                                                 Z_min=min(elevations)), expected)

    def test_scenario_geometry(self):
        # S02: local endpoint, with no claim of a global tie-in.
        self.assertAlmostEqual(formula("ΔE", L=10, A=90, i=0)
                               + formula("ΔE", L=10, A=0, i=-30), 10)
        self.assertAlmostEqual(formula("ΔN", L=10, A=90, i=0)
                               + formula("ΔN", L=10, A=0, i=-30), 8.660254037844386)
        self.assertAlmostEqual(formula("ΔZ", L=10, i=0)
                               + formula("ΔZ", L=10, i=-30), -5)


if __name__ == "__main__":
    unittest.main()
