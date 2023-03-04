import json

def in_region_or_not(argument):
    if argument:
        return "Your region is in the blacklist region"
    if not argument:
        return "Your region is not in the blacklist region"

def checking(species, chromosome, start, stop):
    with open('blacklist.json') as json_file:
        file_content = json_file.read()
        species_dict = json.loads(file_content)
    specie_list = species_dict[species]

    in_region = False
    for region in specie_list[chromosome]:
        if region[0] <= start and region[1] >= stop:
            in_region = True

    return in_region_or_not(in_region)
