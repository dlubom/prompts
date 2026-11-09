# Kontrola SPELEOOPIS

Scenariusze są syntetyczne. Sprawdzają decyzje i zachowanie zakresu zadania,
nie zgodność odpowiedzi ze sztywnym wzorcem stylistycznym.

## Przeprowadzenie próby

1. Użyj jednej wersji skilla, modelu i ustawień dla całej serii. Zapisz commit
   lub kopię plików skilla, model, ustawienia, datę i dostępne narzędzia.
2. Każdy przypadek z [cases.json](cases.json) uruchom w osobnym, czystym kontekście.
   Udostępnij modelowi badany skill z jego instrukcją oraz wyłącznie pole `request`
   wybranego przypadku. Wywołaj skill przez `$speleoopis`.
3. Kryteria z tego pliku zachowaj dla oceniającego. Oceniany model nie powinien
   czytać tego pliku, innych przypadków ani wyników wcześniejszych prób.
4. Zachowaj pełną odpowiedź i istotne wywołania narzędzi. Oceń każde kryterium
   jako spełnione, niespełnione lub niesprawdzone, wskazując fragment odpowiedzi.
5. Przypadek zalicz tylko przy spełnieniu wszystkich jego kryteriów. Przed oceną
   stabilności powtórz serię co najmniej trzy razy; pojedyncza próba jest kontrolą
   wstępną. Porównując wersje, zachowaj te same wejścia i warunki.

Zapis wyników powinien zawierać identyfikator przypadku, numer powtórzenia,
oceny kryteriów i ścieżkę do pełnej odpowiedzi. Brak wykonanej próby oznacza
„niesprawdzone”, a nie zaliczenie. Udane obliczenia nie potwierdzają zachowania
modelu przy redakcji, doborze źródeł ani interpretacji planu.

## Kryteria oceny

We wszystkich przypadkach, w których odpowiedź zawiera znaczniki, ich typ i prefiks
muszą odpowiadać wzorcom z instrukcji: BRAK–Q, SPRZECZNOŚĆ–K, WERYFIKACJA–W,
NAZWA–N, HIPOTEZA–H. Ten sam problem powinien mieć ten sam identyfikator w tekście
i w pytaniach.

### S01 — sama redakcja

- Poprawia zgodę gramatyczną: korytarz „zakręca”, dwa okna „są widoczne”.
- Zachowuje Salę Mokrą, szerokość 2 m, odległość 5 m, kierunek północny,
  rumosz, dwa okna i zakończenie zawaliskiem.
- Oddaje poprawiony akapit bez żądania planu, pomiarów, daty czy identyfikatora.
- Nie tworzy grafu, rejestru obiektów ani dodatkowych faktów o jaskini.
- Nie deklaruje sprawdzenia zgodności z pomiarami lub planem.

### S02 — niepełne dowiązanie

- Przygotowuje lokalny opis udokumentowanych partii, zachowując roboczy status
  związku z Salą Łącznikową; nie utożsamia numeru 0 z otworem ani dawną stacją.
- Wyznacza sumę długości podanych odcinków 20 m i różnicę wysokości 0 → 2 = −5 m.
  Wartości dotyczą tylko nowego ciągu; nie stają się przyrostem parametrów systemu.
- Nie przypisuje kierunków geograficznych, globalnych współrzędnych ani rzędnej
  względem starego otworu.
- Oznacza punkt 2 jako koniec pomiaru przy widocznej kontynuacji.
- Pyta o identyfikację miejsca dowiązania, odniesienie wysokości i orientację;
  brak tych odpowiedzi nie blokuje lokalnego opisu.

### S03 — wielkości wymagające porównania

- Rozdziela deklarowane 10 m głębokości od 8,7 m różnicy wysokości stacji.
- Używa `WERYFIKACJA:W…`, ponieważ zgodność granic nie została ustalona;
  nie oznacza samej różnicy liczb jako `SPRZECZNOŚĆ:K…`.
- Pyta o położenie A.12 i A.15 względem krawędzi i dna.
- Nie koryguje głębokości na 8,7 m ani nie uśrednia wartości.
- Nie przedstawia hipotetycznego przesunięcia stacji jako ustalonego faktu.

### S04 — rzeczywisty konflikt źródeł

- Rozpoznaje konflikt pomiarów tej samej wielkości, granic i daty; różnica 1,3 m
  przekracza deklarowane niepewności.
- Używa `SPRZECZNOŚĆ:K…` i wskazuje N1 oraz P1 z ich wartościami.
- Pozostawia wynik publikacyjny nierozstrzygnięty; nie wybiera źródła tylko
  dlatego, że zawiera współrzędne, i nie uśrednia liczb do 9,35 m.
- Proponuje sprawdzenie źródeł lub ponowny pomiar, zachowując oba ustalenia.

### S05 — udokumentowane rozstrzygnięcie

- Wyznacza rzędną dna −10,0 m i głębokość 10,0 m.
- Wyjaśnia zgodność N1 i P1 potwierdzonym przesunięciem z T1.
- Podaje głębokość w opisie bez pozostawiania rozstrzygniętej sprzeczności
  lub zbędnego pytania o znane już granice.
- Nie wyznacza długości liny z obliczonej głębokości.
