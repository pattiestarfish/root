Databases: set of data stored in computer, structured for easy access
Relational databases: structures allowing us to identify and access data in relation to another piece of data within database
Records: data stored within tables in rows and columns
Columns: labeled with descriptive name, and each column has a specific data type

Relational database management system(RDBMS): program that allows user to create, update, and administer relational database
Popular RDBMS:
1. SQLite is database engine, software allowing users to interact with relational database
- within SQLite, database stored as single file (distinguishing trait), allowing for greater accessibility than before (ie. can email single file)
- popular choice for databases in cellphones, PDAs, MP3, electronic gadgets
- however, single file portability limits write permisions (only 1 user may edit at a time)
- SQLite does not offer data validation: allows entry of any data type (does not enforce user-defined schemas)
*access via git bash command: sqlite3 ____.sqlite

2. MySQL: most popular open source SQL database, often accessed using PHP (owned by Oracle)
- disadvantages include poor performance when scaling, not the most comprehensive but easy to use

3. PostgreSQL: Not controlled by any coorporation, typically used for web app dev
- many similarities with MySQL
- much slower in performance than other databases like MySQL

4. OracleDB: Privately owned NOT open source
- useful for large applications like banking industry, many pre-integrated business applications

5. SQL Server: Microsoft's own SQL server
- free entry level version known as Express