# Schema

Each week has one Excel workbook and one JSON document per site, with the same fields. Prices are in US dollars;
dates are US Eastern.

## JSON document (`json/<site>.json`)

| Field | Type | Example |
|---|---|---|
| `dataset` | string | `Pricify weekly PC hardware prices` |
| `site` | string | `cpu.live` |
| `week` | string, ISO week | `2026-W41` |
| `from`, `to` | date | `2026-10-05`, `2026-10-11` |
| `timezone` | string | `America/New_York` |
| `currency` | string | `USD` |
| `license`, `attribution` | string | `CC BY 4.0`, `Pricify (pricify.ai)` |
| `generated` | timestamp, UTC | `2026-10-18T05:20:00Z` |
| `products` | array of products, most popular first | |

## Product

| Field | Type | Meaning |
|---|---|---|
| `rank` | integer | Its place in the site's top 100 this week (1 = most popular) |
| `product_id` | integer | Stable across weeks and sites |
| `name` | string | Product name |
| `maker` | string | `ASUS`, `AMD`, `Samsung` ... |
| `model` | string or null | The GPU or processor model (`GeForce RTX 5080`, `Ryzen 7 9850X3D`), else the product line |
| `category` | string | `gpu`, `cpu`, `ssd`, `hdd`, `ram`, `psu` |
| `part_number` | string or null | The maker's part number |
| `upc` | string or null | 12-digit UPC (or 13-digit EAN) |
| `launch_price` | number or null | The model's launch price (MSRP); graphics cards and processors |
| `week_low`, `week_high` | number | Lowest and highest of the daily lowest prices |
| `week_open`, `week_close` | number or null | First and last day's lowest price |
| `typical_price_end` | number or null | Median of each retailer's lowest price at the week's end |
| `prev_week_close` | number or null | Last week's `week_close` |
| `change_vs_prev_week_pct` | number or null | `week_close` vs `prev_week_close`, in percent |
| `days_in_stock` | integer, 1 to 7 | Days a store selling it itself had it in stock |
| `retailers_in_stock_end` | integer | Retailers with it in stock at the week's end |
| `shops_in_stock_end` | integer | Physical shops with it on the shelf at the week's end |
| `lowest_store_end` | string or null | Where the lowest price was at the week's end; `(in store)` for a shop |
| `url` | string | The product's page on the site, with every store's current price |
| `daily` | array of 7 days | `date`, `low`, `low_store`, `retailers_in_stock`, `shops_in_stock` |

## Models and sizes

Each JSON document also has `models` (rtx.live, vga.live, cpu.live: every GPU or processor model) or `sizes` (ssd.live,
hdd.live, rams.live, psu.live: size classes such as `2TB NVMe`, `8TB`, `32GB DDR5`, `850W Gold`). A row covers every
product of that model or size the site tracks, whichever store sells it.

| Field | Type | Meaning |
|---|---|---|
| `name` | string | `GeForce RTX 5090`, `Ryzen 7 9800X3D`, `2TB NVMe` ... |
| `launch_price` | number or null | The model's launch price (models only) |
| `products_tracked` | integer | Products of that model or size the site tracks |
| `products_in_stock_end` | integer | Of those, in stock at a store selling it itself at the week's end |
| `week_low` ... `lowest_store_end` | | As for a product, across all of them |

## Excel workbook (`pricify-<week>.xlsx`)

- `README`: the week, the rules, the license.
- One tab per site (`rtx.live`, `vga.live`, `cpu.live`, `ssd.live`, `hdd.live`, `rams.live`, `psu.live`): one row per
  product, the fields above except `daily`.
- One tab per site of its models or sizes (`rtx.live models`, `ssd.live sizes` ...).
- `Daily`: one row per product and day, across all sites.
