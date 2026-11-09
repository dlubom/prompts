# Prompty

Repozytorium promptów i skilli do Codexa.

## SPELEOOPIS

[SPELEOOPIS](.agents/skills/speleoopis/SKILL.md) pomaga opracowywać opisy morfologiczne i inwentarzowe jaskiń. Łączy redakcję tekstu ze sprawdzaniem pomiarów, planów, przekrojów i wcześniejszej dokumentacji. Instrukcje są napisane po polsku.

[Pełną instrukcję SPELEOOPIS](.agents/skills/speleoopis/references/speleoopis.md) można też wykorzystać samodzielnie.

Zakres zadania może obejmować samą redakcję językową, analizę dokumentacji lub pełne opracowanie opisu. Do zwykłej korekty językowej wystarczy tekst; analiza geometrii wymaga odpowiednich materiałów źródłowych.

## Użycie w Codexie

Wymagany jest zainstalowany i skonfigurowany Codex CLI albo aplikacja Codex. Klonowanie repozytorium wymaga Gita.

```sh
git clone https://github.com/dlubom/prompts.git
cd prompts
codex
```

Po uruchomieniu Codex CLI wpisz w rozmowie:

> $speleoopis Opracuj roboczy opis nowych partii jaskini na podstawie załączonych pomiarów, planu, przekroju i notatek.

Przykład samej redakcji:

> $speleoopis Popraw wyłącznie język poniższego opisu. Zachowaj fakty, liczby i nazwy: …

W aplikacji Codex otwórz sklonowany katalog jako projekt. Aby używać skilla w innym repozytorium, skopiuj cały katalog `.agents/skills/speleoopis` do `.agents/skills/` w katalogu głównym tego repozytorium.

Skill ma standardowy plik `SKILL.md` z polami `name` i `description` oraz instrukcję w `references/`. Jest dostępny dla projektu; może być wybrany jawnie lub automatycznie na podstawie opisu zadania. Szczegóły wykrywania i formatu opisuje [oficjalna dokumentacja skilli](https://learn.chatgpt.com/docs/build-skills). Jeśli skill nie pojawia się po skopiowaniu, uruchom Codexa ponownie.

## Kontrola zmian

[Scenariusze i kryteria oceny](tests/speleoopis/README.md) pozwalają sprawdzić redakcję, niepełne dowiązanie oraz rozbieżności między źródłami. Dane wejściowe są syntetyczne i oddzielone od kryteriów oceny.

Wzory zapisane w instrukcji można sprawdzić lokalnie, używając Pythona 3 bez dodatkowych bibliotek:

```sh
python3 -B -m unittest discover -s tests -v
```

Testy liczbowe sprawdzają wzory; ocenę zachowania modelu przeprowadza się osobno według scenariuszy.
