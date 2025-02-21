#!/usr/bin/env python

import os
import pyarrow.parquet as pq

def describe_parquet(file_path):
    file_size = os.path.getsize(file_path)
    print(f"File Size: {file_size} bytes")

    table   = pq.read_table(file_path)
    columns = table.column_names

    print(f"Number of rows: {table.num_rows}")
    print(f"Number of columns: {len(columns)}")

    print("Columns:")
    for column in columns:
        print(column)

describe_parquet("example.parquet")

# Output:
# File Size: 3557 bytes
# Number of rows: 7
# Number of columns: 4
# Columns:
# Captain
# Actor
# Ship
# Quote
