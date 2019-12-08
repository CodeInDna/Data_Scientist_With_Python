/*REFERENCE a table with a FOREIGN KEY
In your database, you want the professors table to reference the universities table. You can do that by specifying a column in professors table that references a column in the universities table.
As just shown in the video, the syntax for that looks like this:
ALTER TABLE a 
ADD CONSTRAINT a_fkey FOREIGN KEY (b_id) REFERENCES b (id);
Table a should now refer to table b, via b_id, which points to id. a_fkey is, as usual, a constraint name you can choose on your own.
Pay attention to the naming convention employed here: Usually, a foreign key referencing another primary key with name id is named x_id, where x is the name of the referencing table in the singular form.
*/
-- Rename the university_shortname column
ALTER TABLE professors
RENAME COLUMN university_shortname TO university_id;

-- Add a foreign key on professors referencing universities
ALTER TABLE professors
ADD CONSTRAINT professors_fkey FOREIGN KEY (university_id) REFERENCES universities(id);

/*Explore foreign key constraints
Foreign key constraints help you to keep order in your database mini-world. In your database, for instance, only professors belonging to Swiss universities should be allowed, as only Swiss universities are part of the universities table.
The foreign key on professors referencing universities you just created thus makes sure that only existing universities can be specified when inserting new data. Let's test this!*/
-- Try to insert a new professor
INSERT INTO professors (firstname, lastname, university_id)
VALUES ('Albert', 'Einstein', 'UZH');
/*As you can see, inserting a professor with non-existing university IDs violates the foreign key constraint you've just added. This also makes sure that all universities are spelled equally – adding to data consistency.*/

/*JOIN tables linked by a foreign key
Let's join these two tables to analyze the data further!
You might already know how SQL joins work from the Intro to SQL for Data Science course (last exercise) or from Joining Data in PostgreSQL.
While foreign keys and primary keys are not strictly necessary for join queries, they greatly help by telling you what to expect. For instance, you can be sure that records referenced from table A will always be present in table B – so a join from table A will always find something in table B. If not, the foreign key constraint would be violated.
*/
-- Select all professors working for universities in the city of Zurich
SELECT professors.lastname, universities.id, universities.university_city
FROM professors
JOIN universities
ON professors.university_id = universities.id
WHERE universities.university_city = 'Zurich';

/*How to implement N:M-relationships
Create a table
Add foreign keys for every connected table
Add additional attributes
 
CREATE TABLE affiliations (
 professor_id integer REFERENCES professors (id),
 organization_id varchar(256) REFERENCES organization (id),
 function varchar(256)
 
No primary key!
Possible PK = {professor_id, organization_id, function}
);*/

/*Add foreign keys to the "affiliations" table
At the moment, the affiliations table has the structure {firstname, lastname, function, organization}, as you can see in the preview at the bottom right. In the next three exercises, you're going to turn this table into the form {professor_id, organization_id, function}, with professor_id and organization_id being foreign keys that point to the respective tables.
You're going to transform the affiliations table in-place, i.e., without creating a temporary table to cache your intermediate results.*/

-- Add a professor_id column
ALTER TABLE affiliations
ADD COLUMN professor_id integer REFERENCES professors (id);

-- Rename the organization column to organization_id
ALTER TABLE affiliations
RENAME organization TO organization_id;

-- Add a foreign key on organization_id
ALTER TABLE affiliations
ADD CONSTRAINT affiliations_organization_fkey FOREIGN KEY (organization_id) REFERENCES organizations (id);

/*Populate the "professor_id" column
Now it's time to also populate professors_id. You'll take the ID directly from professors.
Here's a way to update columns of a table based on values in another table:
UPDATE table_a
SET column_to_update = table_b.column_to_update_from
FROM table_b
WHERE condition1 AND condition2 AND ...;
This query does the following:
For each row in table_a, find the corresponding row in table_b where condition1, condition2, etc., are met.
Set the value of column_to_update to the value of column_to_update_from (from that corresponding row).
The conditions usually compare other columns of both tables, e.g. table_a.some_column = table_b.some_column. Of course, this query only makes sense if there is only one matching row in table_b*/
-- Update professor_id to professors.id where firstname, lastname correspond to rows in professors
UPDATE affiliations
SET professor_id = professors.id
FROM professors
WHERE affiliations.firstname = professors.firstname AND affiliations.lastname = professors.lastname;

-- Have a look at the 10 first rows of affiliations again
SELECT * FROM affiliations LIMIT 10;

/*Drop "firstname" and "lastname"
The firstname and lastname columns of affiliations were used to establish a link to the professors table in the last exercise – so the appropriate professor IDs could be copied over. This only worked because there is exactly one corresponding professor for each row in affiliations. In other words: {firstname, lastname} is a candidate key of professors – a unique combination of columns.
It isn't one in affiliations though, because, as said in the video, professors can have more than one affiliation.
Because professors are referenced by professor_id now, the firstname and lastname columns are no longer needed, so it's time to drop them. After all, one of the goals of a database is to reduce redundancy where possible.*/
-- Drop the firstname column
ALTER TABLE affiliations
DROP COLUMN firstname;

-- Drop the lastname column
ALTER TABLE affiliations
DROP COLUMN lastname;

# Referential integrity
/*Referential integrity violations
Referential integrity from table A to table B is violated...
...if a record in table B that is referenced from a record in table A is deleted.
...if a record in table A referencing a non-existing record from table B is inserted.
Foreign keys prevent violations!*/

# Dealing with violations
CREATE TABLE a (
 id integer PRIMARY KEY,
 column_a varchar(64), 
 ...,
 b_id integer REFERENCES b (id) ON DELETE NO ACTION
);
 
CREATE TABLE a (
 id integer PRIMARY KEY,
 column_a varchar(64), 
 ...,
 b_id integer REFERENCES b (id) ON DELETE CASCADE
);

/*Dealing with violations, contd.
ON DELETE...
...NO ACTION: Throw an error
...CASCADE: Delete all referencing records
...RESTRICT: Throw an error
...SET NULL: Set the referencing column to NULL
...SET DEFAULT: Set the referencing column to its default value*/

/*Change the referential integrity behavior of a key
So far, you implemented three foreign key constraints:
professors.university_id to universities.id
affiliations.organization_id to organizations.id
affiliations.professor_id to professors.id
These foreign keys currently have the behavior ON DELETE NO ACTION. Here, you're going to change that behavior for the column referencing organizations from affiliations. If an organization is deleted, all its affiliations (by any professor) should also be deleted.
Altering a key constraint doesn't work with ALTER COLUMN. Instead, you have to delete the key constraint and then add a new one with a different ON DELETE behavior.
For deleting constraints, though, you need to know their name. This information is also stored in information_schema.*/
-- Identify the correct constraint name
SELECT constraint_name, table_name, constraint_type
FROM information_schema.table_constraints
WHERE constraint_type = 'FOREIGN KEY';

-- Drop the right foreign key constraint
ALTER TABLE affiliations
DROP CONSTRAINT affiliations_organization_id_fkey;

-- Add a new foreign key constraint from affiliations to organizations which cascades deletion
ALTER TABLE affiliations
ADD CONSTRAINT affiliations_organization_id_fkey FOREIGN KEY (organization_id) REFERENCES organizations (id) ON DELETE CASCADE;

-- Delete an organization 
DELETE FROM organizations 
WHERE id = 'CUREM';

-- Check that no more affiliations with this organization exist
SELECT * FROM organizations
WHERE id = 'CUREM';

/*As you can see, whenever an organization referenced by an affiliation is deleted, the affiliations also gets deleted. It is your job as database designer to judge whether this is a sensible configuration. Sometimes, setting values to NULL or to restrict deletion altogether might make more sense!*/

/*Count affiliations per university
Now that your data is ready for analysis, let's run some exemplary SQL queries on the database. You'll now use already known concepts such as grouping by columns and joining tables.
In this exercise, you will find out which university has the most affiliations (through its professors). For that, you need both affiliations and professors tables, as the latter also holds the university_id.
As a quick repetition, remember that joins have the following structure:
SELECT table_a.column1, table_a.column2, table_b.column1, ... 
FROM table_a
JOIN table_b 
ON table_a.column = table_b.column
This results in a combination of table_a and table_b, but only with rows where table_a.column is equal to table_b.column.
*/
-- Count the total number of affiliations per university
SELECT COUNT(*), professors.university_id 
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
GROUP BY professors.university_id
ORDER BY count DESC;

/*Join all the tables together
In this last exercise, you will find the university city of the professor with the most affiliations in the sector "Media & communication".
For this, you need to join all the tables, group by a column, and then use selection criteria to get only the rows in the correct sector.*/
-- Filter the table and sort it
SELECT COUNT(*), organizations.organization_sector, 
professors.id, universities.university_city
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id
WHERE organizations.organization_sector = 'Media & communication'
GROUP BY organizations.organization_sector, 
professors.id, universities.university_city
ORDER BY count DESC;

# The professor with id 538 has the most affiliations in the "Media & communication" sector, and he or she lives in the city of Lausanne. Thanks to your database design, you can be sure that the data you've just queried is consistent. Of course, you could also put university_city and organization_sector in their own tables, making the data model even more formal. However, in database design, you have to strike a balance between modeling overhead, desired data consistency, and usability for queries like the one you've just wrote. Congratulations, you made it to the end!