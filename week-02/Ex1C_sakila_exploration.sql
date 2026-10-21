/*
A.) actord_id, first_name, last_name, last_update
B.) film_id, title, description, release_year, language_id, original_language_id, rental_duration, 
rental_rate, length, replacement_cost, rating, special_features, last_update
C.) film_actor column
D.)  It includes rental_id, rental_date, inventory_id, customer_id, return_date, staff_id and last_update 
in a table format and includes a thousand rows. This is easy to read as it is in a visualized table
format
E.) Inventory includes a table that lists the inventory_id, film_id, store_id and last_update. 
This is also easy to read because it is a visualized table with column headers
F.) The three tables needed are rental, inventory, and film. The rental table contains the date and time each film was rented. The rental table 
is connected to the inventory table through the "inventory_id" column, which identifies the film that was rented using the ID. 
The inventory table is connected to the film table through the "film_id" column. The film table contains the film titles, 
allowing us to identify the names of all films rented on a specific date.
*/

-- Q5: 
SELECT rental_date, inventory_id
FROM rental;

SELECT inventory_id, film_id
FROM inventory;

SELECT film_id, title
FROM film;