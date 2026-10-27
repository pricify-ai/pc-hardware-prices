"""Check the seals of the Pricify forecast record, with nothing but Python 3:

    python forecasts/verify_forecasts.py            (from the repository's root)

Each day's forecasts are sealed when they are made: the SHA-256 of the day before's digest, a line naming the method
and the day, then one line per forecast, "target|horizon|base|p10|p50|p90" (four decimals), sorted by target and
horizon. Each digest is in the next day's "previous", so changing any forecast after the fact breaks every digest
from that day on. This script recomputes them all from the files and says whether the chain holds.
"""

import hashlib
import json
import sys
from pathlib import Path


def seal(previous, made_on, method, forecasts):
    lines = [previous, f"{method} {made_on}"]
    lines += ["|".join(str(field) for field in row) for row in sorted(forecasts, key=lambda r: (r[0], int(r[1])))]
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def main(folder):
    batches = []
    for path in sorted(Path(folder).rglob("W*.json")):
        batches += json.loads(path.read_text(encoding="utf-8"))["batches"]
    batches.sort(key=lambda b: (b["method"], b["made_on"]))
    previous, broken = {}, 0
    for batch in batches:
        method = batch["method"]
        ok = batch["previous"] == previous.get(method, "") and seal(
            batch["previous"], batch["made_on"], method, batch["forecasts"]) == batch["digest"]
        broken += not ok
        print(f"{batch['made_on']}  {method:8} {len(batch['forecasts']):5} forecasts  {batch['digest'][:16]}  "
              f"{'holds' if ok else 'BROKEN'}")
        previous[method] = batch["digest"]
    print(f"{len(batches)} days checked: " + ("every seal holds" if not broken else f"{broken} BROKEN"))
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent))
