# PC hardware prices: weekly open data

Weekly prices and stock of the most popular PC components at US retailers, from the [Pricify](https://pricify.ai) price trackers: graphics cards, processors, SSDs, hard drives, memory and power supplies. One release every week, in Excel and JSON, free to use with credit.

**Latest: 2026-W43** (2026-10-19 to 2026-10-25, US Eastern) · [Excel](latest/pricify-latest.xlsx) · [JSON](latest/json/) · [all weeks](data/)

## This week

| Site | Tracks | Products | Biggest drop vs last week | Biggest rise | In stock at the most stores |
|---|---|---:|---|---|---|
| [rtx.live](https://rtx.live) | NVIDIA RTX cards | 100 | ASUS GeForce RTX 5060 Ti Prime Overcl...: $469.99 (-17.5%) | PNY GeForce RTX 5060 Overclocked Dual...: $449.99 (+21.6%) | ASUS GeForce RTX 5060 Ti Prime Overcl...: 6 retailers, 34 shops |
| [vga.live](https://vga.live) | Graphics cards | 100 | ASUS GeForce RTX 5060 Ti Prime Overcl...: $469.99 (-17.5%) | PNY GeForce RTX 5060 Overclocked Dual...: $449.99 (+21.6%) | ASUS GeForce RTX 5060 Ti Prime Overcl...: 6 retailers, 34 shops |
| [cpu.live](https://cpu.live) | Processors | 100 | AMD Ryzen 5 5600X: $159.00 (-8.7%) | Intel Core i9-14900K: $429.99 (+13.2%) | AMD Ryzen 7 9800X3D: 7 retailers, 35 shops |
| [ssd.live](https://ssd.live) | SSDs | 100 | Samsung 990 PRO 4TB M.2 2280 NVMe PCI...: $799.90 (-15.7%) | SanDisk Optimus GX PRO 8100 1TB M.2 2...: $299.99 (+20.0%) | SanDisk Portable Drive 1TB SSD: 8 retailers, 29 shops |
| [hdd.live](https://hdd.live) | Hard drives | 100 | Western Digital Elements 1TB External...: $119.60 (-14.3%) | Western Digital WD Purple Pro 24TB 3....: $1,319.99 (+14.9%) | Western Digital WD Red Plus 8TB 3.5"...: 8 retailers, 33 shops |
| [rams.live](https://rams.live) | Memory kits | 100 | Kingston FURY Beast 16GB DDR5-5200 CL40: $325.05 (-8.9%) | Synology 16GB DDR4-2666 ECC SO-DIMM (...: $1,054.99 (+22.0%) | Corsair Vengeance LPX 32GB (2x16GB) D...: 5 retailers, 26 shops |
| [psu.live](https://psu.live) | Power supplies | 100 | MSI A850GLS MLG EDITION 850W 80+ Gold...: $79.99 (-21.9%) | MSI MAG A650BE 650W 80+ Bronze Semi-M...: $69.99 (+16.7%) | Corsair RMx 1000W 80+ Gold Fully Modu...: 7 retailers, 35 shops |

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
