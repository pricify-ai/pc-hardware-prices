# Pricify price indices

Daily indices of US retail prices for PC components, from 2026-10-01. Live at https://pricify.ai/indices.

A store's own price for a new unit in stock, at the end of each day, US Eastern time. Marketplace sellers, used, open-box and refurbished units, and prices not confirmed are left out.

Chained: 100 on the first day, then moved each day by the geometric mean of the same products' price changes, so a product coming into or going out of stock moves nothing. A one-day move of more than half, up or down, is left out of the chain.

| Index | Name | Unit of `level` | What it covers |
|---|---|---|---|
| `gpu` | Pricify GPU Index | none (chained value only) | Consumer graphics cards (GeForce, Radeon, Arc), every board partner. |
| `gpu-launch` | Graphics cards over launch price | % over launch price | The middle current model's lowest price against its launch price, models released in the last two years. |
| `cpu` | Pricify CPU Index | none (chained value only) | Consumer desktop processors (Ryzen, Core, Core Ultra). |
| `ddr5` | DDR5 memory | $/GB | DDR5 memory kits and modules for desktops and laptops, without ECC. |
| `ddr4` | DDR4 memory | $/GB | DDR4 memory kits and modules for desktops and laptops, without ECC. |
| `nvme` | NVMe SSDs | $/TB | Consumer NVMe solid-state drives. |
| `hdd` | Hard drives (desktop and NAS) | $/TB | Desktop and NAS hard drives. |

`pricify-indices.csv`: one row per index and day. `value` is the chained index (100 on its first day; empty for an index with a level only), `level` the day's middle figure in its unit, `measured` the products (or, for `gpu-launch`, models) it was read from. A published day is not revised; a restatement, if one is ever needed, is listed in CHANGELOG.md.
