# Trees Database Project

This project involves a Trees Database that allows users to perform various queries and operations related to parks, neighborhoods, and tree data. The project includes SQL scripts, Java code for the Command Line Interface (CLI), and other relevant files.

# Project Structure

The project includes the following files:

- **DatabaseApp.java**: The Java source code for the command-line interface and queries methods.
- **initialData.sql**: SQL file containing all 'INSERT' commands to populate the database.
- **data.db**: The initial database file populated with all the data.
- **makefile**: A makefile for building and running the project/Command Line Interface.
- **mapping.py**: Sample python script for merging multiple CSV files according to the required mapping.
- **csvToSql.py**: Sample python script for converting CSV files to 'INSERT' SQL commands.

# Setup Instructions

1. **Compile and Run Java Code:**
   ```bash
   make run
   ```
2. **Populate the Database:**
   - The database is initially populated into the data.db file.
   - The database can be cleared by running the `delete` command in the CLI, and populated by running the `init` command. But initializing like this may take a significant amount of time.
   - Alternatively, you can use SQLite3 commands for much faster initialization (populating):
   ```bash
   sqlite3
   .read initialData.sql
   .save <someName>.db
   .exit
   ```

# Usage Instructions

The command-line interface supports various queries and commands. For a list of available commands and their explanations, run the h command within the interface.

## Examples

1. `Delete Tables`: This would drop all the tables in our database if they exist.
   ```bash
   delete
   ```
2. `Initialize the Database`: This would first create our 8 tables and then use the `INSERT` commands in our project.sql file to populate the database. (Initializing like this would take a significant amount of time)
   ```bash
   init
   ```
3. `popParkTrees`: This query can be used to get either the most or the least popular trees in all our parks. To get most popular we can use the `-most` flag and to get the least popular we can use the `-least` flag as our second argument. We will also have to give the number of trees we want to print which is essentialy the length of the result list, this will be given as the third argument `numberOfTrees`.
   ```bash
   popParkTrees <-most/-least> <numberOfTrees>
   ```
4. `diameter`: The query can be used in three different ways by using these three different flags as the second argument:
   - `-range`: By using this flag you can get all the trees which have the diamter in the range you give in the third argument. if using this flag the third argument `diameter` has to be in this format: minRange-maxRange (eg. 5-10)
   - `-greater`: By using this query you can get all the trees which have diameter greater than the diamter you give in the third argument.
   - `-fewer`: By using this query you can get all the trees which have diameter fewer than the diamter you give in the third argument.
   ```bash
   diameter <-range/-greater/-fewer> <diameter>
   ```

- The other queries follow a similar format. Explanation can be retreived by using `h` command which will print a help page.

# Contributors

- Muhammad Dawood Safdar (7926993)
- Muhammad Hassan Nauman (7871016)
