import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

cursor = conn.cursor()

query1 = """
-- Question 1:

SELECT
  COUNT(*)
FROM charactercreator_character

-- The answer is: 302
"""
result1 = cursor.execute(query1).fetchall()
print(result1)

query2 = """
-- Question 2

SELECT
	COUNT(*) as fighters
FROM charactercreator_fighter;

-- The answer is 68

SELECT
	COUNT(*) as clerics
FROM charactercreator_cleric;

-- The answer is 75

SELECT
	COUNT(*) as mages
FROM charactercreator_mage;

-- The answer is 108

SELECT
	COUNT(*) as necromancers
FROM charactercreator_necromancer;

-- The Answer is 11

SELECT
	COUNT(*)
FROM charactercreator_thief;

-- The Answer is 51
"""

# result2 = cursor.execute(query2).fetchall()
# print(result2)

query3 = """
-- Question 3:
SELECT
	COUNT(*) as items
FROM armory_item

-- The answer is 174
"""

result3 = cursor.execute(query3).fetchall()
print(result3)

query4 = """
-- Question 4:
SELECT
	COUNT(*) as weapons
FROM armory_weapon

-- The answer is 37 weapons

SELECT 174 - 37

-- The answer is 137 items are NOT weapons
"""

# result4 = cursor.execute(query4).fetchall()
# print(result4)

query5 = """
-- Question 5:

SELECT
	COUNT(item_id) as TotalItems,
	character_id
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
"""

result5 = cursor.execute(query5).fetchall()
print(result5)

query6 = """
-- Question 6:

SELECT COUNT(cci.item_id) as Weapons,
	cci.character_id,
	weap.item_ptr_id
FROM charactercreator_character_inventory as cci
JOIN armory_weapon as weap
ON cci.item_id = weap.item_ptr_id
GROUP BY cci.character_id
LIMIT 20;
"""

result6 = cursor.execute(query6).fetchall()
print(result6)

query7 = """
-- Question 7:

SELECT
	AVG(item_id)as AvgItems,
	character_id
FROM charactercreator_character_inventory
GROUP BY character_id
"""
# result7 = cursor.execute(query7).fetchall()
# print(result7)
