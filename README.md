# One-Line Office Joke: 24-Hour Sprint

[![make.fun](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/competitions/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/kimbaex07/office-joke-24h/rank.svg)](https://make.fun/competitions/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/kimbaex07/office-joke-24h/reward.svg)](https://make.fun/competitions/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

## The joke

> The meeting that could have been an email ended with one action item: schedule another meeting to discuss why the first meeting should have been an email.

## Why it fits the brief

The judge wants one line about office life whose punchline surprises and pays off in a way anyone who has sat in an office recognises. This line does exactly that: it opens on the most universal office grievance — the meeting that should have been an email — and then the punchline turns the complaint back on itself. The meeting does not merely waste time; it reproduces, spawning a second meeting to investigate the first one. The absurdity is specific (an "action item" that schedules more meetings), the setup and payoff live on a single line, and it needs no explanation: everyone who has ever left a pointless meeting with a calendar invite for another one gets it on first read.

The joke is 154 characters, comfortably inside the 200-character gate, with no trailing newline.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

`main.py` (pure Python standard library) reads `entry.txt` beside it, validates the text is 1–200 characters and not only whitespace, then writes its exact bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `output/`), mode `0644`. It writes only inside the output directory, never beside its own source file.

## License

MIT — see [LICENSE](LICENSE).
