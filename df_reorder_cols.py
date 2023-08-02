#!/usr/bin/env python

import sys
import pandas as pd

if len(sys.argv) <= 2:
    print("usage:", sys.argv[0], "in.tsv col1 col2 ...", file=sys.stderr)
    sys.exit(1)

col_order = sys.argv[2:]
df = pd.read_csv(sys.argv[1], sep="\t")
df = df[col_order]
df.to_csv(sys.stdout, sep="\t", index=None)

