#!/usr/bin/env/ python3
import sys

try:
    n = int(sys.argv[1])
    n -= 3500

    if n <= 1500:
        n = n  * 0.03 - 0
    elif n > 1500 and n <= 4500:
        n = n * 0.1 - 105
    elif n > 4500 and n <= 9000:
        n = n * 0.2 - 555
    elif n > 9000 and n <= 35000:
        n = n * 0.25 - 1005
    elif n > 35000 and n <= 55000:
        n = n * 0.3 - 2755
    elif n > 55000 and n <= 80000:
        n = n * 0.35 - 5505
    elif n > 80000:
        n = n *0.45 - 13505
    print(format(n,".2f"))
except ValueError:
    print("parameter Error")

