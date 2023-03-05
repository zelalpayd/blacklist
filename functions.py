import json
import requests


def get_sequence(species,chromosome,start,stop):
    sequence = requests.get(
        f"https://api.genome.ucsc.edu/getData/sequence?genome={species};chrom={chromosome};start={start};end={stop}")
    dict_sequence= json.loads(sequence.text)
    dna_sequence = dict_sequence["dna"]
    return dna_sequence


def checking(species, chromosome, start, stop):
    with open('blacklist.json') as json_file:
        file_content = json_file.read()
        species_dict = json.loads(file_content)
    specie_list = species_dict[species]

    in_region = False

    for region in specie_list[chromosome]:
        if region[0] <= start and region[1] >= stop:
            in_region = True
    dna_sequence = get_sequence(species,chromosome,start,stop)
    
    if in_region:
        return f"Your region is in the blacklist region and the sequence is {dna_sequence}"
    if not in_region:
        return "Your region is not in the blacklist region"


