USE northwind;

/*
Write a query to find the price of the cheapest item that Northwind sells. Then write a
second query to find the name of the product that has that price.
*/
-- Cheapest Item that Northwind sells
SELECT MIN(UnitPrice) 
FROM products;
-- Name of the cheapest product that Northwind sells
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);

-- Write a query to find the average price of all items that Northwind sells.
SELECT ROUND(AVG(UnitPrice), 2) AS 'Average'
FROM products;

/*
Write a query to find the price of the most expensive item that Northwind sells. Then
write a second query to find the name of the product with that price, plus the name of
the supplier for that product.
*/
-- Most expensive Item Northwind sells
SELECT MAX(UnitPrice)
FROM products;

-- Product name of the most expensive Item that Northwind sells
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM products);

-- Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries)
SELECT SUM(Salary)
FROM employees;

/*
Write a query to identify the highest salary and the lowest salary amounts which any
employee makes. (Just the amounts, not the specific employees!)
*/
SELECT MAX(Salary), MIN(Salary)
FROM employees;

/*
Write a query to find the name and supplier ID of each supplier and the number of
items they supply. 
*/
SELECT suppliers.SupplierID, suppliers.CompanyName, COUNT(products.ProductID) AS ItemCount
FROM suppliers
JOIN products
ON suppliers.supplierID = products.SupplierID
GROUP BY suppliers.CompanyName, suppliers.SupplierID;

/*
Write a query to find the list of all category names and the average price for items in
each category
*/
SELECT categories.CategoryName, ROUND(AVG(products.UnitPrice), 2)
FROM categories
JOIN products
ON categories.CategoryID = products.CategoryID
GROUP BY categories.CategoryID, categories.CategoryName;

/*
Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
is the name of each supplier and the number of items they supply.
*/
SELECT suppliers.CompanyName, COUNT(products.ProductID) AS ItemCount
FROM suppliers
JOIN products
ON suppliers.SupplierID = products.SupplierID
GROUP BY suppliers.SupplierID, suppliers.CompanyName
HAVING COUNT(products.ProductID) >= 5;

/*
Write a query to list products currently in inventory by the product id, product name,
and inventory value (calculated by multiplying unit price by the number of units on
hand). Sort the results in descending order by value. If two or more have the same
value, order by product name. If a product is not in stock, leave it off the list.
*/
SELECT ProductID, ProductName, UnitPrice * UnitsInStock AS InventoryValue
FROM products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName ASC;



