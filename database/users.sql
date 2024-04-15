CREATE TABLE users (
	username varchar(30) NOT NULL,
	password VARCHAR(30) NOT NULL,
	phone_number DECIMAL(10, 0) NOT NULL,
	pan VARCHAR(10) NOT NULL,
	aadhar_number DECIMAL(12, 0) NOT NULL,
	name VARCHAR(30) NOT NULL,
	dob DATE NOT NULL,
	gender ENUM('M','F') NOT NULL,
	CONSTRAINT users_pk PRIMARY KEY (username),
	CONSTRAINT users_unique UNIQUE KEY (pan),
	CONSTRAINT users_unique_1 UNIQUE KEY (aadhar_number)
)

