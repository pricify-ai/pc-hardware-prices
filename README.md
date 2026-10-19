# PC hardware prices: weekly open data

Weekly prices and stock of the most popular PC components at US retailers, from the [Pricify](https://pricify.ai) price trackers: graphics cards, processors, SSDs, hard drives, memory and power supplies. One release every week, in Excel and JSON, free to use with credit.

**Latest: 2026-W41** (2026-10-05 to 2026-10-11, US Eastern) · [Excel](latest/pricify-latest.xlsx) · [JSON](latest/json/) · [all weeks](data/)

## This week

| Site | Tracks | Products | Biggest drop vs last week | Biggest rise | In stock at the most stores |
|---|---|---:|---|---|---|
| [rtx.live](https://rtx.live) | NVIDIA RTX cards | 100 | NVIDIA RTX Pro 4500 Blackwell Single-...: $4,499.99 (-10.0%) | Gigabyte GeForce RTX 5060 WINDFORCE O...: $429.99 (+16.2%) | Gigabyte GeForce RTX 5060 WINDFORCE O...: 7 retailers, 25 shops |
| [vga.live](https://vga.live) | Graphics cards | 100 | Sparkle Intel Arc Pro B70 Blower Sing...: $1,499.99 (-16.7%) | Gigabyte GeForce RTX 5060 WINDFORCE O...: $429.99 (+16.2%) | Gigabyte GeForce RTX 5060 WINDFORCE O...: 7 retailers, 25 shops |
| [cpu.live](https://cpu.live) | Processors | 100 | Intel Core i7-14700K: $279.99 (-22.2%) | AMD Ryzen Threadripper 9970X: $2,299.99 (+21.1%) | AMD Ryzen 7 9850X3D: 7 retailers, 35 shops |
| [ssd.live](https://ssd.live) | SSDs | 100 | Samsung 990 1TB M.2 2280 NVMe PCIe 4.0: $189.99 (-17.0%) | Lexar SL500 2TB Portable SSD (LSL500M...: $469.99 (+23.7%) | SanDisk 500GB Portable SSD (SDSSDE31-...: 8 retailers, 35 shops |
| [hdd.live](https://hdd.live) | Hard drives | 100 | Western Digital MYPSPT 4TB External H...: $254.99 (-19.0%) | Western Digital My Book 6TB External...: $380.99 (+20.7%) | Western Digital WD Red Plus 8TB 3.5"...: 9 retailers, 33 shops |
| [rams.live](https://rams.live) | Memory kits | 100 | TEAMGROUP T-Create Master 128GB (8x16...: $4,039.99 (-19.8%) | Kingston Fury Renegade RGB 32GB (2x16...: $723.32 (+16.4%) | Corsair Vengeance LPX 32GB (2x16GB) D...: 6 retailers, 27 shops |
| [psu.live](https://psu.live) | Power supplies | 100 | Cooler Master V750 750W 80+ Gold Full...: $124.98 (-23.4%) | ASUS ROG Thor 1000W 80+ Platinum ATX 3.1: $469.99 (+11.9%) | Corsair RMx 1000W 80+ Gold Fully Modu...: 7 retailers, 35 shops |

Prices are the ones stores ask themselves for new products; marketplace sellers are never counted. Each site also has a table of every model (graphics cards, processors) or size class (drives, memory, power supplies).

## What's inside

| Path | What |
|---|---|
| `latest/pricify-latest.xlsx` | The newest week: a tab per site, a tab of its models or sizes, a Daily tab |
| `latest/json/<site>.json` | The newest week, one JSON document per site |
| `data/<year>/<week>/` | Every week, kept as released |
| [SCHEMA.md](SCHEMA.md) | Every field, with units |
| [METHODOLOGY.md](METHODOLOGY.md) | What counts as a price and how a week is computed |
| [CHANGELOG.md](CHANGELOG.md) | One line per release, and any correction |

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
