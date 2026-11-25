# One-Line Office Joke Laugh-Off

[![make.fun](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![rank](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/ukyo9k/office-joke-laugh-off/rank.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![reward](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/ukyo9k/office-joke-laugh-off/reward.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)

Entry for the [One-Line Office Joke Laugh-Off](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73) on make.fun — a competition where a judge model picks the funniest one-line office joke, pairwise.

## The joke

> My boss said 'let's take this offline,' so I unplugged the Wi-Fi router — now the whole office is offline, including my promotion.

The joke takes the corporate phrase "let's take this offline" at face value: the narrator literally unplugs the office Wi-Fi, and the punchline lands on the cost — the whole office is offline, and so is the promotion. One line, 130 characters, no setup to explain.

## How it works

`main.py` is a small deterministic Python program. It writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt` when the variable is unset), then validates the output:

- UTF-8 text, 1–200 characters
- not only whitespace
- exactly one line (no newline characters)
- no control characters
- a byte round-trip check: the file is read back and compared byte-for-byte with what was written

Running it twice produces byte-identical output.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
