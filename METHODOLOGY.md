# Methodology

How each weekly release is made. The same rules decide what the Pricify sites show.

## The week

An ISO week, Monday 00:00 to Sunday 24:00, US Eastern time. A release is named by its week: `2026-W41` is
Monday October 5 to Sunday October 11, 2026.

## Which products

The 100 most popular products on each site that a store sold itself, new and in stock, on at least one day of the
week. "Popular" is our own measure of interest: what people look at, search and set alerts for on the sites, and what
sells at the stores. Refurbished and open-box units are not included.

| Site | Products |
|---|---|
| rtx.live | NVIDIA GeForce RTX graphics cards |
| vga.live | Graphics cards of every maker |
| cpu.live | Processors |
| ssd.live | SSDs |
| hdd.live | Hard drives |
| rams.live | Memory |
| psu.live | Power supplies |

A product can be on two sites (a GeForce card is on rtx.live and vga.live); it keeps the same `product_id` on both.

Each site also has a table of every model (graphics cards, processors: the RTX 5090 across all its cards) or size class
(drives, memory, power supplies: every 2TB NVMe SSD, every 850W Gold power supply), computed the same way across all
of its products.

## Which prices

- **A store's own price only.** A marketplace seller's listing on a store's site is never counted, however cheap.
- **New condition only.**
- **Confirmed.** An offer we could not read again for about three days is treated as not in stock, not as still
  available at its last price.
- **Online and in shops.** An offer is a store's price online, or at one of its physical shops. Shops count toward
  "shops in stock".

## How a week is computed

Every offer's readings are replayed to its state at the end of each day of the week. For each product and day:
the lowest price in stock (`daily[].low`), where it was (`daily[].low_store`), and how many retailers and physical shops
had it in stock.

From the seven days:

| Field | Meaning |
|---|---|
| `week_low`, `week_high` | The lowest and highest of the daily lowest prices |
| `week_open`, `week_close` | The first and the last day's lowest price |
| `typical_price_end` | The median of each retailer's lowest price at the end of the week: what most stores ask |
| `days_in_stock` | Days, of seven, it was in stock at a store selling it itself |
| `change_vs_prev_week_pct` | `week_close` against the previous week's close |

The lowest price and the typical price can tell different stories: when a product sells out at most stores, its
lowest price may hold at one retailer while the typical price climbs.

## Checks before release

Before a week is published, rows that look wrong are held for a second look, never published as they are and never
silently changed:

- a lowest price over three times, or under 40% of, the product's launch price;
- a move of 25% or more against the previous week;
- a week's high over twice its low.

A held product's place in the top 100 goes to the next most popular. Most held rows are real market moves and are
released once confirmed; some are a reading error, corrected at the source first.
A correction to a released week is listed in [CHANGELOG.md](CHANGELOG.md), and the week is re-released with a new
`generated` time; nothing is rewritten silently.

## Not included

No product photos, no text written by stores or makers, and no seller or customer information. Prices change within
minutes; always check the store before buying.
