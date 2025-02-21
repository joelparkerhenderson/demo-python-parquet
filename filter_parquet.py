#!/usr/bin/env python

import pyarrow.parquet as pq

# To extract entries from a Parquet file where the Ship column exactly matches `USS Enterprise-D`
# without loading the entire file into memory, you can use the filters argument in PyArrow's `read_table`
# function to apply "predicate pushdown".  This method allows you to specify conditions that are used to
# filter data during the read operation, which can significantly reduce memory usage by only loading the
# relevant subset of data.  This is useful when dealing with Common Crawl's indexes, because they're huge!

# Define filters to apply predicate pushdown
# Here we specify that we only want rows where the 'Ship' column is 'USS Enterprise-D'
filters = [('Ship', '=', 'USS Enterprise-D')]

# Read the Parquet file with the filters applied to avoid loading a monstrously large file into memory
table = pq.read_table('example.parquet', filters=filters)

# Convert to Pandas DataFrame for easier viewing/manipulation (optional)
filtered_df = table.to_pandas()

print(filtered_df)

# Output:
#            Captain            Actor              Ship         Quote
# 0  Jean-Luc Picard  Patrick Stewart  USS Enterprise-D   Make it so.
# 1   Edward Jellico        Ronny Cox  USS Enterprise-D  Get it done.
