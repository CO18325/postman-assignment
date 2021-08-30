DROP TABLE IF EXISTS categories;

CREATE TABLE categories(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	category_name TEXT NOT NULL
);

DROP TABLE IF EXISTS PRODUCTS;

create TABLE products(
	prod_id INTEGER PRIMARY KEY AUTOINCREMENT,
	category INTEGER NOT NULL,
	apiName TEXT NOT NULL,
	link TEXT NOT NULL
);

