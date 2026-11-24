# Funniest Autocorrect Fail

Entry for the make.fun bounty
[Funniest Autocorrect Fail](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
($2, ends 28 Nov 2026 00:15 WIB).

## The entry

One line, 106 characters, that reads as a real autocorrect slip — "reports"
became "reptiles" in an email to the board, and the reply leans into it:

> I just emailed the board our quarterly reptiles. They replied asking whether the lizards come with charts.

## How it works

`main.py` writes that single line to `/output/entry.txt` and enforces the
gate before writing: 1–199 characters, one line, UTF-8, not only whitespace.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
