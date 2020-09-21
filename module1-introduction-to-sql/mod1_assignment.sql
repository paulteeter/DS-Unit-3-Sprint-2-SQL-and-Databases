-- Question 1:

SELECT
  COUNT(*)
FROM charactercreator_character

-- The answer is: 302


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

-- Question 3:
SELECT
	COUNT(*) as items
FROM armory_item

-- The answer is 174

-- Question 4:
SELECT
	COUNT(*) as weapons
FROM armory_weapon

-- The answer is 37 weapons

SELECT 174 - 37

-- The answer is 137 items are NOT weapons

-- Question 5:

SELECT
	COUNT(item_id) as TotalItems,
	character_id
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;

-- Question 6:

SELECT COUNT(cci.item_id) as Weapons,
	cci.character_id,
	weap.item_ptr_id
FROM charactercreator_character_inventory as cci
JOIN armory_weapon as weap
ON cci.item_id = weap.item_ptr_id
GROUP BY cci.character_id
LIMIT 20;

-- Question 7:

SELECT
	AVG(item_id)as AvgItems,
	character_id
FROM charactercreator_character_inventory
GROUP BY character_id

