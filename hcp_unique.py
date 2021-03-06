import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('outfile')
args = parser.parse_args()

HuffmanCodedPos = np.dtype([
    ('hcp', np.uint8, 32),
    ])

data = np.fromfile(args.file, dtype=HuffmanCodedPos)
print(len(data))

data_unique = np.unique(data)
print(len(data_unique))

data_unique.tofile(args.outfile)
