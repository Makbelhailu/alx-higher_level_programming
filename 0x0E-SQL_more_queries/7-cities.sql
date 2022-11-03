-- create table with forign key

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE,
	state_id INT NOT NULL FOREIGN KEY (state_id) REFERENCES states(id);
	name VARCHAR(256)) NOT NULL;
