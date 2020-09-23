# NoSQL and Document-oriented databases

NoSQL, no worries? Not exactly, but it's still a powerful approach for some
problems.

## Learning Objectives

- Identify appropriate use cases for document-oriented databases
- Deploy and use a simple MongoDB instance

## Before Lecture

Sign up for an account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas),
the official hosted service of MongoDB with a generous (500mb) free tier. You
can also explore the many [MongoDB tools](http://mongodb-tools.com/) out there,
though none in particular are recommended or required for installation (we're
really just checking out MongoDB as a way to understand document-oriented
databases - it's unlikely to become a core part of your toolkit the way SQLite
and PostgreSQL may).

## Live Lecture Task

Another database, same data? Let's try to store the RPG data in our MongoDB
instance, and learn about the advantages and disadvantages of the NoSQL paradigm
in the process. We will depend on
[PyMongo](https://api.mongodb.com/python/current/) to connect to the database.

Note - the
[JSON](https://github.com/LambdaSchool/Django-RPG/blob/master/testdata.json)
representation of the data is likely to be particularly useful for this purpose.

## Assignment

Reproduce (debugging as needed) the live lecture task of setting up and
inserting the RPG data into a MongoDB instance, and add the code you write to do
so here. Then answer the following question (can be a comment in the top of your
code or in Markdown) - "How was working with MongoDB different from working with
PostgreSQL? What was easier, and what was harder?"

There is no other required tasks to turn in, but it is suggested to then revisit
the first two modules, rework/complete things as needed, and just check out with
fresh eyes the SQL approach. Compare and contrast, and come with questions
tomorrow - the main topic will be database differences and tradeoffs!

# Import into MongoDB collection from JSON file

with open('/Users/macuser/Lambda/Unit 3/DS-Unit-3-Sprint-2-SQL-and-Databases/module3-nosql-and-document-oriented-databases/test_data_json.txt') as json_file:
    rpg_data = json.load(json_file)

# Create a new database
rpg_db = client.rpg_data

# Create a collection inside the database
character_table = rpg_db.characters

# Insert many into collection
character_table.insert_many(rpg_data)
print(character_table.count_documents({}))


<!--       ##############       -->

MongoDB seems to have a much easier workflow, as its structure is not as rigid. 
PostgreSQL and Mongo have equally easy interfaces with Python code, but their layout and implementation on the server side are not the same. MongoDB seems more intuitive and powerful, more flexible.

<!--       ##############       -->






## Resources and Stretch Goals

Put Titanic data in Big Data! That is, try to load `titanic.csv` from yesterday
into your MongoDB cluster.

Push MongoDB - it is flexible and can support fast iteration. Design your own
database to save some key/value pairs for an application you'd like to work on
or data you'd like to analyze, and build it out as much as you can!
