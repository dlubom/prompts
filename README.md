# Prompty

Repozytorium promptów i skilli do Codexa.

## SPELEOOPIS

[SPELEOOPIS](.agents/skills/speleoopis/SKILL.md) pomaga opracowywać opisy morfologiczne i inwentarzowe jaskiń. Łączy redakcję tekstu ze sprawdzaniem pomiarów, planów, przekrojów i wcześniejszej dokumentacji. Instrukcja skilla i prompt są napisane po polsku.

[Oryginalny prompt v1.0](.agents/skills/speleoopis/references/SPELEOOPIS_prompt_v1_0.txt) można też wykorzystać samodzielnie.

## Użycie w Codexie

```sh
git clone https://github.com/dlubom/prompts.git
cd prompts
codex
```

Po uruchomieniu Codexa możesz użyć poniższego polecenia.

> $speleoopis Opracuj roboczy opis nowych partii jaskini na podstawie załączonych pomiarów, planu, przekroju i notatek.

W aplikacji Codex otwórz sklonowany katalog jako projekt. Aby używać skilla w innym repozytorium, skopiuj cały katalog `.agents/skills/speleoopis` do `.agents/skills/` w katalogu głównym tego repozytorium.
