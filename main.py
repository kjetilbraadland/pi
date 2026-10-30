#!/usr/bin/env python3
"""Simple pi estimation app — Monte Carlo method.

Estimates pi by throwing random "darts" at a unit square with an
inscribed circle. The ratio of points inside the circle to total
points approximates pi/4.
"""

import random
import sys


def estimate_pi(n: int = 1_000_000) -> float:
    inside = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return 4 * inside / n


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000
    result = estimate_pi(n)
    print(f"Estimated pi after {n:,} samples: {result:.6f}")
    print(f"Actual pi:                    {3.14159265358979:.6f}")
    print(f"Error: {abs(result - 3.14159265358979):.6f}")


if __name__ == "__main__":
    main()
