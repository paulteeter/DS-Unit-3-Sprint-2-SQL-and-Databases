-- select all rows and columns from albumsSELECT *
SELECT *
FROM albums;

SELECT AlbumId, Title
FROM albums
LIMIT 5;

SELECT 
	CustomerId,
	FirstName,
	LastName,
	Country
FROM customers
-- WHERE Country='Brazil'
WHERE Country in ('Brazil', 'USA');

-- How many different countries do our customers come from
SELECT
	COUNT(*),
	COUNT(Country),
	COUNT(DISTINCT Country)
FROM customers;

-- Find average invoice total for each customer
SELECT
	CustomerId,
	AVG(Total)
FROM invoices
GROUP BY CustomerId;

-- Which customers have an average invoice > 6
SELECT
	CustomerId,
	AVG(Total) as AvgTotal
FROM invoices
GROUP BY CustomerId
HAVING AvgTotal >= 6;

-- Introducing JOINS by adding Customer Name to previous
SELECT
	inv.CustomerId,
	cust.FirstName,
	cust.LastName,
	AVG(inv.Total) as AvgTotal
FROM invoices as inv
LEFT JOIN customers as cust
ON inv.CustomerId = cust.CustomerId
GROUP BY inv.CustomerId
HAVING AvgTotal >= 6;

-- Which artist has the most albums?

SELECT
	COUNT(alb.AlbumId) as NumAlbums,
	alb.ArtistId,
	art.Name as ArtistName
FROM albums as alb
JOIN artists as art
ON alb.ArtistId = art.ArtistId
GROUP BY ArtistName
ORDER BY NumAlbums DESC;