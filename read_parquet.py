#!/usr/bin/env python

import pandas as pd

# Read the Parquet file into a DataFrame
df = pd.read_parquet('example.parquet')

# Display the contents of the DataFrame
print("Contents of the Parquet file:")
print(df)


# Output:
# Contents of the Parquet file:
#             Captain            Actor              Ship                            Quote
# 0     James T. Kirk  William Shatner    USS Enterprise              Beam me up, Scotty!
# 1   Jean-Luc Picard  Patrick Stewart  USS Enterprise-D                      Make it so.
# 2    Benjamin Sisko     Avery Brooks      Deep Space 9                 It's a faaaaake!
# 3   Kathryn Janeway     Kate Mulgrew       USS Voyager   There's coffee in that nebula.
# 4   Jonathan Archer     Scott Bakula  Enterprise NX-01  We're not out here to play God.
# 5  William T. Riker  Jonathan Frakes         USS Titan         I love surprise parties.
# 6    Edward Jellico        Ronny Cox  USS Enterprise-D                     Get it done.