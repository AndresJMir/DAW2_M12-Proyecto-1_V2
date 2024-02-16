CREATE TABLE orders (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	product_id INTEGER NOT NULL,
	buyer_id INTEGER NOT NULL,
	offer DECIMAL(10, 2) NOT NULL,
	created DATETIME NOT NULL DEFAULT (DATETIME('now')),
	CONSTRAINT uc_product_buyer UNIQUE (product_id, buyer_id),
	FOREIGN KEY (product_id) REFERENCES products(id),
	FOREIGN KEY (buyer_id) REFERENCES users(id)
);

CREATE TABLE confirmed_orders (
	order_id INTEGER PRIMARY KEY,
	created DATETIME NOT NULL DEFAULT (DATETIME('now')),
	FOREIGN KEY (order_id) REFERENCES orders(id)
);

-- Inserir dades fictícies a la taula orders
INSERT INTO orders (id, product_id, buyer_id, offer) VALUES
(1, 1, 2, 500.00),
(2, 2, 1, 18.00),
(3, 3, 3, 10.00),
(4, 3, 1, 12.00),
(5, 3, 2, 11.00);
UPDATE SQLITE_SEQUENCE SET seq = 5 WHERE name = 'orders';

-- Inserir dades fictícies a la taula confirmed_orders
INSERT INTO confirmed_orders (order_id) VALUES
(1);
UPDATE SQLITE_SEQUENCE SET seq = 1 WHERE name = 'confirmed_orders';
