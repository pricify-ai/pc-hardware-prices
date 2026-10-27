# Pricify forecast record

Every day, after the day has ended, Pricify forecasts each price index and the lowest price of each graphics card and processor model that has a market (in stock at a store's own price at the end of at least 5 of the last 7 days), 7, 30 and 90 days ahead: a middle figure (`p50`) and an 80% range (`p10` to `p90`), from `base`, the figure that day. Live at https://pricify.ai/forecasts.

## Sealed

Each day's forecasts are sealed when they are made: `digest` is the SHA-256 of the day before's digest, a line naming the method and the day, and one line per forecast. The next day carries it as `previous`, so changing any forecast after the fact breaks every digest from that day on. Check them all with

```
python forecasts/verify_forecasts.py
```

`<year>/W<nn>.json` holds a week's days as they were sealed, and is not changed once published. Forecasts are made only for the day that has just ended, never for an earlier one.

## Scored

`scores.csv` adds each forecast's outcome when its day comes: `actual`, and `inside_range` (1 when the outcome fell between `p10` and `p90`; an honest range holds it about 8 times in 10). A model's forecast is scored on a day it is in stock at a store's own price.

## Methods

`naive`, the baseline: the figure stays where it is, with the 80% range from how much such figures have moved day to day. Every later method joins the record beside it and is scored on the same days.

These are forecasts of component prices: not of any company's shares, and not advice to buy or sell anything.
