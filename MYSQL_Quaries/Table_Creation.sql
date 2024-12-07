CREATE TABLE IF NOT EXISTS units(
    unit_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    unit_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    unit_id INTEGER REFERENCES units(unit_id),
    product_price FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    total FLOAT NOT NULL,
    order_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS order_detail(
    order_id INTEGER REFERENCES orders(order_id),
    product_id INTEGER REFERENCES products(product_id),
    quantity FLOAT NOT NULL,
    total_price FLOAT NOT NULL
);