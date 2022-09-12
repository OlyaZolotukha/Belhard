CREATE TABLE  categories(
    id SMALLSERIAL PRIMARY KEY,
    parent_id SMALLINT,
    is_published BOOLEAN DEFAULT(false),
    name VARCHAR(20)
    FOREIGN KEY(parent_id) references categories(id) on delete cascade);

CREATE TABLE products(
    id SMALLSERIAL PRIMARY KEY,
    category_id SMALLINT,
    prise SMALLINT,
    media VARCHAR(255),
    total SMALLINT,
    is_published BOOLEAN DEFAULT(false),
    name VARCHAR(20),
    FOREIGN KEY(category_id) references categories(id));

CREATE TABLE languages(
    id SMALLSERIAL PRIMARY KEY,
    language_code VARCHAR(2));

CREATE TABLE bot_users(
    id VARCHAR(2) PRIMARY KEY,
    is_blocked BOOLEAN DEFAULT(false),
    balance SMALLINT,
    language_id SMALLINT,
    FOREIGN KEY (language_id) references languages(id));

CREATE TABLE statuses(
    id SMALLSERIAL PRIMARY KEY,
    name VARCHAR(20));

CREATE TABLE invoices(
    id VARCHAR(10) PRIMARY KEY,
    bot_user_id VARCHAR(2),
    data_create TIMESTAMP,
    total SMALLINT,
    status_id SMALLINT,
    FOREIGN KEY (bot_user_id) references bot_users (id),
    FOREIGN KEY (status_id) references statuses (id));

CREATE TABLE orders(
    id SMALLSERIAL PRIMARY KEY,
    bot_user_id VARCHAR(2),
    data_create TIMESTAMP,
    status_id SMALLINT,
    invoice_id VARCHAR(10),
    FOREIGN KEY (bot_user_id) references bot_users(id),
    FOREIGN KEY (status_id) references statuses(id),
    FOREIGN KEY (invoice_id) references invoices(id));

CREATE TABLE orders(
    id SMALLSERIAL PRIMARY KEY,
    order_id SMALLINT,
    product_id SMALLINT,
    total SMALLINT,
    FOREIGN KEY (order_id) references orders(id),
    FOREIGN KEY (product_id) references products(id))
