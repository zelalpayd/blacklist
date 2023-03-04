import gzip
import csv
import json
import os
from __init__ import files, BASE_DIR


# take all informations from one species' bed file, make it dictionary and return
def list_creation(file):
    bed_dict = {}
    with gzip.open(file, 'rt') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            chrom = row[0]
            start = int(row[1])
            end = int(row[2])
            if chrom not in bed_dict:
                bed_dict[chrom] = []
            bed_dict[chrom].append([start, end])
    return bed_dict



blacklist_species_dict = {}
for file in files:
    species = file.split("-")[0]
    blacklist_dict = list_creation(os.path.join(BASE_DIR,'blacklist_files',file))
    blacklist_species_dict[species] = blacklist_dict


with open("blacklist.json","w") as output:
    json.dump(blacklist_species_dict, output, indent=1)