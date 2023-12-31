import csv

# Define the input and output file paths
input_csv_file = 'mapped_tree_data.csv'
output_sql_file = 'insert_queries.sql'

# Open the input CSV file in utf-8-sig encoding
with open(input_csv_file, mode='r', encoding='utf-8-sig') as csv_file:
    # Create a CSV reader
    csv_reader = csv.DictReader(csv_file)
    
    # Open the output SQL file for writing
    with open(output_sql_file, mode='w') as sql_file:
        for row in csv_reader:
            treeID = row['treeID']
            diameter = row['diameter']
            parkID = row['parkID']
            specieID = row['specieID']
            neighborhoodID = row['neighborhoodID']
            
            # Construct the SQL insert query
            sql_query = f"INSERT INTO trees VALUES ({treeID}, {diameter}, {parkID}, {specieID}, {neighborhoodID});\n"
            
            # Write the SQL query to the output file
            sql_file.write(sql_query)

print("SQL insert queries have been generated and saved to", output_sql_file)
