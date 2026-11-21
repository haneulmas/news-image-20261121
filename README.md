[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/haneulmas/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/haneulmas/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Built for the [make.fun bounty](https://make.fun/bounty/news-image-20261121) — referral code `re4yck73`.

# The World Today — Saturday 21 November 2026

A single-page newspaper front page that sums up Saturday 21 November
2026 in six panels. Each panel covers one story that defined the day,
laid out the way a printed front page would be: headline first, image
second, and a short line of context underneath.

## The six stories

- **Poland missiles** — a missile incident involving Poland.
- **Wall Street correction** — a sharp correction on the US markets.
- **ICJ ruling on Myanmar** — the International Court of Justice
  rules in the genocide case against Myanmar.
- **Estonia border shutdown** — Estonia closes its border crossings.
- **Cyclone Akvan** — the day's major storm story.
- **UK–EU deals** — new agreements between Britain and the European
  Union.

## How to run

```sh
python3 main.py
```

The script copies `entry.png`, the finished 1024 by 1024 front page,
into `$MAKEFUN_OUTPUT_DIR` (or `/output` when the variable is not
set). It needs nothing else: only the Python standard library, and it
never touches the network.

## Determinism

The output is a byte-for-byte copy of the bundled picture, so every
run produces an identical file. Repeated runs were checked by comparing
SHA-256 hashes.

## Files

- `main.py` — the copy script described above.
- `entry.png` — the finished front page artwork.
- `README.md` — this file.
- `LICENSE` — MIT license.
