# Changelog

One line per weekly release, newest first. Corrections to a released week are listed below the releases.

- **2026-W44** (2026-10-26 to 2026-11-01): 7 sites, 700 products, 291 models and size classes.
- **2026-W43** (2026-10-19 to 2026-10-25): 7 sites, 700 products, 291 models and size classes.
- **2026-W42** (2026-10-12 to 2026-10-18): 7 sites, 700 products, 300 models and size classes.
- **2026-W41** (2026-10-05 to 2026-10-11): 7 sites, 700 products, 294 models and size classes.

The indices (`indices/`) and the forecast record (`forecasts/`) are updated with each release from 2026-W43 on.

## Corrections

- **2026-10-24**: W41 and W42 counted some products as in stock after a store had stopped selling them itself. Two kinds of read were not applied when the days were replayed: a read without a price (how a page that stopped showing one is recorded) and a marketplace seller taking over Amazon's own offer. The read before them stood, so a product could stay in stock, at its last store price, for good. Measured on October 23, the replay counted 3,853 products in stock at a store itself where the corrected one counts 3,602. Every read is applied from W43 on. W41 and W42 are kept as released.
- **2026-11-02**: Corsair's own store (Corsair Store) was often read from out-of-date copies of its pages, so some of its prices and stock did not follow the store's. Checked on corsair.com on November 2: the MP600 CORE XT 1TB we had at $74.99 in stock since October 1 was $324.99 on its page, a 64GB DDR5 kit we had at $989.99 was $1,071.99, and a DDR4 kit we had in stock had no price or cart button. Rows of W41 to W43 that name Corsair Store as the lowest store may be wrong; in W43 those include the lowest 32GB DDR5 kit ($229.99) and the lowest 1TB NVMe drive ($74.99). From W44 on, Corsair Store's prices are left out until they are read from the page a shopper sees. W41 to W43 are kept as released.
