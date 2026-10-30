USE northwind;

-- Product Name of the most expensive product
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM products);

-- What is the product name(s) and categories of the least expensive products?
SELECT products.ProductName, products.UnitPrice, categories.CategoryName
FROM products
JOIN categories
ON products.CategoryID = categories.CategoryID
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products)
GROUP BY products.ProductName, products.UnitPrice, categories.CategoryName;

/*
What is the order id, shipping name and shipping address of all orders shipped via
"Federal Shipping"?
*/
-- 1st Attempt at Query
SELECT OrderID, ShipName, ShipAddress, ShipVia
FROM orders
WHERE ShipVia = 3;

-- 2nd Attempt at Query with feedback from ChatGPT
SELECT OrderID, ShipName, ShipAddress
FROM orders
WHERE ShipVia = (SELECT ShipperID FROM shippers WHERE CompanyName = 'Federal Shipping');

/*
What are the order ids of the orders that included "Sasquatch Ale"?
∗ HINT: Find the product id of "Sasquatch Ale" in a subquery and then use that value
to find the matching orders from the `order details` table.
*/
SELECT OrderID
FROM `order details`
WHERE ProductID = (SELECT ProductID FROM products WHERE ProductName = 'Sasquatch Ale'
);

-- What is the name of the employee that sold order 10266?
SELECT employees.FirstName, employees.LastName, orders.OrderID 
FROM employees 
JOIN orders
ON employees.EmployeeID = orders.EmployeeID
WHERE orders.OrderID = 10266;

-- What is the name of the customer that bought order 10266?
SELECT customers.ContactName, customers.CompanyName, orders.OrderID 
FROM customers
JOIN orders
ON customers.CustomerID = orders.CustomerID
WHERE orders.OrderID = 10266;


