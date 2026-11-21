# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/haneulmas/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/haneulmas/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image that sums up the world's news of Saturday 21 November 2026, for the make.fun bounty `news-image-20261121`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png — a 1024x1024 PNG, under 1 MiB
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=h14gtbhq&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>

## What the image shows

The 1024×1024 image is a newspaper front-page infographic with six
labelled panels. The stories were chosen from news reported on
21 November 2026, i.e. the events that happened, or were first
reported, on 21 November 2026 in the sources below.

1. **Poland — Russian missiles land in Poland.**
   Two Russian missiles and a suspected drone came down in Poland.
   Warsaw called it a deliberate provocation; NATO called it a grave
   violation of its airspace. Sources: One Turn News ("Today's world
   news", 21 Nov 2026), Newsy Today.
2. **New York — Wall Street slides into correction.**
   The S&P 500 and Dow entered correction territory as AI shares
   plunged; the Nasdaq fell 5.28% and Nvidia dropped about 14%.
   Sources: One Turn News, SimpleLife daily news 21 Nov 2026.
3. **The Hague — ICJ: Myanmar committed genocide.**
   The International Court of Justice found that Myanmar's forces
   committed genocide against the Rohingya — the first time a state
   has been found responsible for genocide. Sources: One Turn News,
   Disclosure News burst 21 Nov 2026.
4. **Tallinn — Estonia shuts its Russia border.**
   Estonia closed all border crossings with Russia after suspected
   arson sabotage. Sources: homevo.eu news digest, 21 Nov 2026.
5. **India — Cyclone Akvan strikes the Odisha coast.**
   Cyclonic Storm Akvan crossed the south Odisha and north Andhra
   Pradesh coast with strong winds and heavy rainfall. Source:
   JagranJosh school assembly headlines, 21 Nov 2026.
6. **Brussels — UK and EU sign three deals.**
   Prime Minister Burnham signed agreements on food trade, carbon
   markets and youth mobility at a Brussels summit. Source:
   One Turn News, 21 Nov 2026.

No facts were invented for the image; panel sub-text is a short summary
of the verified headlines above. The image was drawn programmatically
with PIL (vector pictograms and typeset text), so no text is garbled
and no figure is cut off.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` to `/output/entry.png`, creating `/output` if needed.
It is deterministic: both runs write the same bytes.

## Files

- `main.py` — entrypoint, copies `entry.png` to the output directory
- `entry.png` — the 1024×1024 news-summary image
- `LICENSE` — MIT
- `.makefun/owner.json` — proves the repo belongs to the make.fun
  account whose wallet is named there
