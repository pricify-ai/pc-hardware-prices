# PC hardware prices: weekly open data

Weekly prices and stock of the most popular PC components at US retailers, from the [Pricify](https://pricify.ai) price trackers: graphics cards, processors, SSDs, hard drives, memory and power supplies. One release every week, in Excel and JSON, free to use with credit.

**Latest: 2026-W42** (2026-10-12 to 2026-10-18, US Eastern) · [Excel](latest/pricify-latest.xlsx) · [JSON](latest/json/) · [all weeks](data/)

## This week

| Site | Tracks | Products | Biggest drop vs last week | Biggest rise | In stock at the most stores |
|---|---|---:|---|---|---|
| [rtx.live](https://rtx.live) | NVIDIA RTX cards | 100 | Zotac GeForce RTX 5060 GAMING AMP COR...: $389.99 (-17.0%) | PNY GeForce RTX 5080 Slim Overclocked...: $1,699.99 (+13.3%) | Gigabyte GeForce RTX 5060 WINDFORCE O...: 7 retailers, 21 shops |
| [vga.live](https://vga.live) | Graphics cards | 100 | Zotac GeForce RTX 5060 GAMING AMP COR...: $389.99 (-17.0%) | PNY GeForce RTX 5080 Slim Overclocked...: $1,699.99 (+13.3%) | Gigabyte GeForce RTX 5060 WINDFORCE O...: 7 retailers, 21 shops |
| [cpu.live](https://cpu.live) | Processors | 100 | Intel Core Ultra 5 225: $159.99 (-10.4%) | AMD Ryzen 9 9900X3D: $529.99 (+10.4%) | AMD Ryzen 7 9850X3D: 7 retailers, 35 shops |
| [ssd.live](https://ssd.live) | SSDs | 100 | Lexar Professional Workflow 4TB Porta...: $649.99 (-20.7%) | Lexar JumpDrive D500 512GB Portable SSD: $121.00 (+21.0%) | Samsung T7 1TB Portable SSD Gray: 8 retailers, 34 shops |
| [hdd.live](https://hdd.live) | Hard drives | 100 | Western Digital WD My Passport 2TB Ex...: $132.10 (-22.3%) | Western Digital WD Red Pro 24TB 3.5"...: $1,311.83 (+23.8%) | Western Digital WD Red Plus 8TB 3.5"...: 9 retailers, 30 shops |
| [rams.live](https://rams.live) | Memory kits | 100 | Patriot Viper Steel 16GB (2x8GB) DDR4...: $129.99 (-18.8%) | TEAMGROUP T-Create Master 128GB (8x16...: $5,039.99 (+24.8%) | Corsair Vengeance LPX 32GB (2x16GB) D...: 6 retailers, 24 shops |
| [psu.live](https://psu.live) | Power supplies | 100 | SilverStone 550W 80+ Bronze Fully Mod...: $67.71 (-24.2%) | Corsair RM850e 850W 80+ Gold Fully Mo...: $123.99 (+24.0%) | Corsair RMx 1000W 80+ Gold Fully Modu...: 7 retailers, 35 shops |

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
