# install java 8, SchemaSpy, Graphviz, sqlite3, sqlite driver
path 
# it should have java, schemaspy-6.1.0.jar, sqlite3, graphviz, sqlite-jdbc-3.23.1.jar

# Create TutorialSampleDB.sql
sqlite3 TutorialsSampleDB.db < TutorialsSampleDB.sql

# Create sqlite.properties
description=SQLite
driver=org.sqlite.JDBC
driverPath=sqlite-jdbc-3.23.1.jar
connectionSpec=jdbc:sqlite:<db>
db=TutorialsSampleDB.db

java -jar schemaspy-6.1.0.jar -t sqlite  -db TutorialsSampleDB.db -cat TutorialsSampleDB -s TutorialsSampleDB -vizjs -o . -sso
