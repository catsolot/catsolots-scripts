#!/usr/bin/env python3

import sys

sep = "&"
line = "\hline"
end = "\\\\"

def gen(n):
    print("\\begin{center}")
    print("\\begin{tabular}{| c | c |}")
    print("\\hline")
    for i in range (65, 65+26):
        alpha = chr(i)
        if i + n <= 90:
            letter = chr(i+n)
        else:
            letter = chr((i + n) - 26)
        print(alpha, sep, letter, end, end = " ")
        print("\hline", end = " ")
    print("\\end{tabular}")
    print("\\end{center}")

if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) <= 1:
        print("Usage: ./gen.py n")
        print("Where n is the caesar cipher key")
        exit()
    key = int(sys.argv[len(sys.argv) - 1])
    gen(key)
