#!/usr/bin/env python

import sys
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="Script to sort rows in a dataframe.", formatter_class=argparse.MetavarTypeHelpFormatter)

parser.add_argument("df_file", type=str, help="left dataframe (TSV file)")
parser.add_argument("col_name", type=str, help="column name")
parser.add_argument("-d", "--delimiter", type=str, default="\t", help="delimiter (default, \\t)")
parser.add_argument("-r", "--reverse", action="store_true", help="decending order")

args = parser.parse_args()

df = pd.read_table(args.df_file, sep=args.delimiter, dtype=object)
df = df.sort_values(args.col_name, ascending=(not args.reverse))
df.to_csv(sys.stdout, sep=args.delimiter, index=None)
