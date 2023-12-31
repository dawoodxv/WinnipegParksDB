import csv
import random

# Read the park CSV and create a mapping from parkName to parkID
park_mapping = {}
with open('parks.csv', newline='', encoding='utf-8-sig') as park_file:
    park_reader = csv.DictReader(park_file)
    for row in park_reader:
        park_mapping[row['parkName']] = row['parkID']

# Read the species CSV and create a mapping from botanicalName to speciesID
species_mapping = {}
with open('specie.csv', newline='', encoding='utf-8-sig') as species_file:
    species_reader = csv.DictReader(species_file)
    for row in species_reader:
        species_mapping[row['biotonicalName']] = row['specieID']

# Read the neighborhood CSV and create a mapping from neighborhoodName to neighborhoodID
neighborhood_mapping = {}
with open('neighborhood.csv', newline='', encoding='utf-8-sig') as neighborhood_file:
    neighborhood_reader = csv.DictReader(neighborhood_file)
    for row in neighborhood_reader:
        neighborhood_mapping[row['neighborhoodName']] = row['neighborhoodID']

# Create a list to store the mapped tree data
mapped_tree_data = []

# Read the main tree data CSV and perform the mappings
with open('trees.csv', newline='', encoding='utf-8-sig') as tree_file:
    tree_reader = csv.DictReader(tree_file)
    for row in tree_reader:
        tree_id = row['Tree ID']
        diameter = row['Diameter at Breast Height']
        park_name = row['Park']
        botanical_name = row['Botanical Name']
        neighborhood = row['Neighbourhood']

        # Map park name to parkID, or assign a random parkID if "Not In Park"
        park_id = park_mapping.get(park_name, str(random.randint(10000, 99999)))

        # Map botanical name to specieID
        specie_id = species_mapping.get(botanical_name, '')

        # Map neighborhood to neighborhoodID, or assign a random neighborhoodID if not found
        neighborhood_id = neighborhood_mapping.get(neighborhood, str(random.randint(1, 999)))

        mapped_tree_data.append({
            'treeID': tree_id,
            'diameter': diameter,
            'parkID': park_id,
            'specieID': specie_id,
            'neighborhoodID': neighborhood_id
        })

# Write the mapped tree data into a new CSV file
with open('mapped_tree_data.csv', 'w', newline='', encoding='utf-8-sig') as mapped_file:
    fieldnames = ['treeID', 'diameter', 'parkID', 'specieID', 'neighborhoodID']
    writer = csv.DictWriter(mapped_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(mapped_tree_data)

print("Mapped tree data has been saved to mapped_tree_data.csv")
