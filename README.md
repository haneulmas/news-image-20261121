[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/haneulmas/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/haneulmas/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Built for the [make.fun bounty](https://make.fun/bounty/news-image-20261121).

# The World in One Day: Saturday 21 November 2026

One image that sums up Saturday 21 November 2026. The centre is a
globe drawn as a clock, its continents folded like pages of
newsprint, with seven region dots riding an orbit ring around it.
Beside the globe are the five stories that led the day. Below it,
eight more stories are drawn as cards. Underneath, a dated ledger
lists all 35 stories reported that day, numbered 01 to 35, with a
markets strip at the foot. The globe is the whole composition: one
planet, one day, one clock. Nothing else on the page is decoration.
The stars are the only marks without a story behind them, and there
are four of them.

## What the image shows

The five leading stories: COP31 talks in Antalya running past their
deadline with no deal, Russian missiles landing in Poland, the Saudi
coalition intercepting three Houthi missiles aimed at Riyadh, Wall
Street entering correction with the Nasdaq down 5.28%, and a
magnitude 6.7 earthquake near Carhuamayo in Peru.

The eight drawn cards: the ICJ ruling that Myanmar committed
genocide against the Rohingya, BepiColombo reaching Mercury after
eight years, Cyclone Akvan making landfall in Odisha, Estonia
shutting its Russia border, the UK and EU signing three deals,
strikes on Kryvyi Rih, the FBI and US Agriculture Department being
hacked, and Indonesia's 2026 forest fires.

The ledger adds the rest of the day, from the Bayer Roundup
settlement in Missouri and the Anthropic IPO to the Basra power
plant fire, the Hormuz tanker attacks, the Air Niugini jet that made
an emergency landing at Davao, the displacement of around 700,000
people around Moyale in Ethiopia, the IRGC claim of a downed US
MQ-9 drone over the Strait of Hormuz, and the coalition's
announcement that it destroyed six Houthi workshops in Sana'a.
Every figure in the picture comes from reports published on 21
November 2026: the Horizon daily briefing, One Turn News, AP,
Nature, the USGS, the Civil Aviation Authority of the Philippines,
Islamic Relief, and ANI. The drone claim is worded as a claim
because the United States has not confirmed it. Closing prices in
the markets strip are the closes reported that day.

## How to run

```sh
python3 main.py
```

The script copies `entry.png`, the finished 1024 by 1024 picture,
into `$MAKEFUN_OUTPUT_DIR` (or `/output` when the variable is not
set). It runs on Python 3.13, uses only the standard library,
touches no network, and refuses to run if the picture is over the
1 MiB limit.

## Determinism

The output is a byte-for-byte copy of the bundled picture, so every
run writes identical bytes. Two runs were checked by comparing
SHA-256 hashes.

## Files

- `main.py`: the copy script described above.
- `entry.png`: the finished picture.
- `README.md`: this file.
- `LICENSE`: MIT license.
