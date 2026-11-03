# PC hardware prices: weekly open data

Weekly prices and stock of the most popular PC components at US retailers, from the [Pricify](https://pricify.ai) price trackers: graphics cards, processors, SSDs, hard drives, memory and power supplies. One release every week, in Excel and JSON, free to use with credit.

**Latest: 2026-W44** (2026-10-26 to 2026-11-01, US Eastern) · [Excel](latest/pricify-latest.xlsx) · [JSON](latest/json/) · [all weeks](data/)

## This week

| Site | Tracks | Products | Biggest drop vs last week | Biggest rise | In stock at the most stores |
|---|---|---:|---|---|---|
| [rtx.live](https://rtx.live) | NVIDIA RTX cards | 100 | PNY RTX Pro 6000 Blackwell Max-Q Work...: $13,999.99 (-12.5%) | MSI GeForce RTX 5070 Ti 16GB GAMING T...: $1,549.99 (+24.0%) | ASUS GeForce RTX 5060 Ti Prime Triple...: 6 retailers, 35 shops |
| [vga.live](https://vga.live) | Graphics cards | 100 | Gigabyte AMD Radeon RX 9070 Gaming Ov...: $809.99 (-14.7%) | MSI GeForce RTX 5070 Ti 16GB GAMING T...: $1,549.99 (+24.0%) | ASUS GeForce RTX 5060 Ti Prime Triple...: 6 retailers, 35 shops |
| [cpu.live](https://cpu.live) | Processors | 100 | AMD Ryzen 5 5600XT: $149.99 (-20.6%) | AMD Ryzen 7 9700X: $319.99 (+10.3%) | AMD Ryzen 7 9850X3D: 6 retailers, 35 shops |
| [ssd.live](https://ssd.live) | SSDs | 100 | Apricorn Aegis Fortress L3 16TB Porta...: $9,807.95 (-24.3%) | Corsair MP600 ELITE 1TB M.2 2280 NVMe...: $304.00 (+21.6%) | SanDisk Portable Drive 1TB SSD: 8 retailers, 35 shops |
| [hdd.live](https://hdd.live) | Hard drives | 100 | Western Digital My Passport 4TB Exter...: $189.77 (-24.1%) | Western Digital My Book 16TB External...: $659.99 (+20.0%) | Western Digital WD Red Plus 8TB 3.5"...: 8 retailers, 32 shops |
| [rams.live](https://rams.live) | Memory kits | 100 | Corsair Vengeance 16GB DDR4-3200 CL22...: $119.99 (-24.1%) | Patriot 32GB DDR5-5600 CL46 SO-DIMM (...: $619.99 (+24.0%) | Corsair Vengeance LPX 32GB (2x16GB) D...: 5 retailers, 30 shops |
| [psu.live](https://psu.live) | Power supplies | 100 | Thermaltake Toughpower GF A3 ATX 1200...: $119.99 (-20.0%) | ASUS TUF 1000W 80+ Gold Fully Modular: $226.99 (+15.7%) | Corsair HX1000i 1000W 80+ Platinum Fu...: 6 retailers, 35 shops |

Prices are the ones stores ask themselves for new products; marketplace sellers are never counted. Each site also has a table of every model (graphics cards, processors) or size class (drives, memory, power supplies).

## What's inside

| Path | What |
|---|---|
| `latest/pricify-latest.xlsx` | The newest week: a tab per site, a tab of its models or sizes, a Daily tab |
| `latest/json/<site>.json` | The newest week, one JSON document per site |
| `data/<year>/<week>/` | Every week, kept as released |
| [`indices/`](indices/) | The Pricify price indices, every day since 2026-10-01 |
| [`forecasts/`](forecasts/) | The forecast record: each day's sealed forecasts, their scores, a script that checks the seals |
| [SCHEMA.md](SCHEMA.md) | Every field, with units |
| [METHODOLOGY.md](METHODOLOGY.md) | What counts as a price and how a week is computed |
| [CHANGELOG.md](CHANGELOG.md) | One line per release, and any correction |

## Indices and forecast record

Seven daily indices of US retail prices (graphics cards, graphics cards against launch price, processors, DDR5 and DDR4 memory, NVMe SSDs, hard drives), chained from the stores' own prices, in [indices/](indices/). Every day Pricify also seals a forecast of each index and of graphics card and processor prices, 7, 30 and 90 days ahead: each day's forecasts carry a SHA-256 fingerprint chained to the day before, so none can be changed after the fact. They are here as they were sealed, with their scores as they come due, in [forecasts/](forecasts/); `python forecasts/verify_forecasts.py` checks every seal. Live at [pricify.ai/indices](https://pricify.ai/indices) and [pricify.ai/forecasts](https://pricify.ai/forecasts).

## Use it

```python
import pandas as pd

gpus = pd.read_excel("latest/pricify-latest.xlsx", sheet_name="rtx.live")
models = pd.read_excel("latest/pricify-latest.xlsx", sheet_name="rtx.live models")

import requests
doc = requests.get("https://raw.githubusercontent.com/pricify-ai/pc-hardware-prices/main/latest/json/cpu.live.json").json()
cpus = pd.json_normalize(doc["products"])
```

Each product carries a stable `product_id`, its part number and UPC, so weeks join to each other and to your own data.

## License and credit

[CC BY 4.0](LICENSE): use it for anything, including commercial work and model training, as long as you credit "Pricify (pricify.ai)" with a link. GitHub's "Cite this repository" button gives the citation ([CITATION.cff](CITATION.cff)).

The full catalog, daily and per-store detail and live data are available from [pricify.ai](https://pricify.ai).
