CREATE DATABASE IF NOT EXISTS products_db;

USE products_db;

CREATE TABLE IF NOT EXISTS products (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  price DECIMAL(5,2) NOT NULL,
  description VARCHAR(200) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO products (id, name, price, description) VALUES
  (1,	'Pure Wool Yarn',	5, '100% pure wool, worsted weight yarn, 50 gram ball'),
  (2,	'4mm Knitting Needles',	7.5,	'High quality metal needles'),
  (3,	'4mm Crochet Hook',	6,	'Suitable for use with DK and aran weight yarn'),
  (4,	'Crafting Scissors',	12.5,	'For trimming and snipping sturdy metal design'),
  (5,	'Knitting Bag',	25,	'Perfect to hold all your crafting supplies, durable cotton design');
