USE northwind;

/*
Create a single query to list the product id, product name, unit price and category
name of all products. Order by category name and within that, by product name.
*/
SELECT products.ProductID, products.ProductName, products.UnitPrice, categories.CategoryName
FROM products
INNER JOIN categories
ON products.CategoryID = categories.CategoryID
ORDER BY
categories.CategoryName,
products.ProductName;

/*
Create a single query to list the product id, product name, unit price and supplier
name of all products that cost more than $75. Order by product name
*/
SELECT products.ProductID, products.ProductName, products.UnitPrice, suppliers.CompanyName
FROM products
INNER JOIN suppliers
ON products.SupplierID = suppliers.SupplierID
WHERE products.UnitPrice > 75
ORDER BY
products.ProductName;

/*
Create a single query to list the product id, product name, unit price, category name,
and supplier name of every product. Order by product name.
*/
SELECT products.ProductID, products.ProductName, products.UnitPrice, categories.CategoryName, suppliers.CompanyName
FROM products
INNER JOIN categories
ON products.CategoryID = categories.CategoryID
INNER JOIN suppliers
ON products.SupplierID = suppliers.SupplierID
ORDER BY
products.ProductName;

/*
Create a single query to list the order id, ship name, ship address, and shipping
company name of every order that shipped to Germany. Assign the shipping company
name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
shipped to.
*/
SELECT orders.OrderID, orders.ShipName, orders.ShipAddress, shippers.CompanyName AS Shipper
FROM orders
INNER JOIN shippers
ON orders.ShipVia = shippers.ShipperID
WHERE orders.ShipCountry = 'germany'
ORDER BY
shipper, orders.ShipName;

/*
Start from the same query as above (#4), but omit OrderID and add logic to group by
ship name, with a count of how many orders were shipped for that ship name.
*/
SELECT orders.ShipName, orders.ShipAddress, shippers.CompanyName AS Shipper, COUNT(*) AS OrderCount
FROM orders
INNER JOIN shippers
ON orders.ShipVia = shippers.ShipperID
WHERE orders.ShipCountry = 'Germany'
GROUP BY
orders.ShipName,
orders.ShipAddress,
shippers.CompanyName
ORDER BY
Shipper,
orders.ShipName;

/*
Create a single query to list the order id, order date, ship name, ship address of all
orders that included Sasquatch Ale.
*/
SELECT orders.OrderID, orders.OrderDate, orders.ShipName, orders.ShipAddress
FROM orders
INNER JOIN `Order Details`
ON orders.OrderID = `Order Details`.OrderID
INNER JOIN products
ON `Order Details`.ProductID = products.ProductID
WHERE products.ProductName = 'Sasquatch Ale';