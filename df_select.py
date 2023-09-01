#!/usr/bin/env python

import sys
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="Script to select columns in a dataframe.")

parser.add_argument("df_file", type=str, help="left dataframe (TSV file)")
parser.add_argument("col_names", type=str, nargs="+", help="column name")
parser.add_argument("-d", "--delimiter", type=str, default="\t", help="delimiter (default, \\t)")

args = parser.parse_args()

df = pd.read_table(args.df_file, sep=args.delimiter)
df = df[args.col_names]
df.to_csv(sys.stdout, sep=args.delimiter, index=None)
