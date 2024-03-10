CREATE TABLE product_category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    desc TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    modified_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP
);

CREATE TABLE product_inventory (
    id SERIAL PRIMARY KEY,
    SKU VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    category_id INT REFERENCES product_category(id),
    created_at TIMESTAMP DEFAULT NOW(),
    inventory_id INT,
    modified_at TIMESTAMP DEFAULT NOW(),
    price DECIMAL(10, 2),
    deleted_at TIMESTAMP,
    discount_id INT REFERENCES discount(id),
    created_at_discount TIMESTAMP,
    modified_at_discount TIMESTAMP
);

CREATE TABLE discount (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    desc TEXT,
    discount_percent DECIMAL(5, 2) NOT NULL,
    active BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    modified_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP
);

CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    modified_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    category_id INT REFERENCES product_category(id)
);