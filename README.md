# pi

A simple test application that estimates π using the Monte Carlo method.

## Usage

```bash
python3 main.py            # 1,000,000 samples (default)
python3 main.py 10000000   # 10,000,000 samples
```

## How it works

Random points are generated inside a unit square with an inscribed circle.
Since the circle's area (π/4) is the ratio of the square's area (1), the
fraction of points landing inside the circle approximates π/4.
