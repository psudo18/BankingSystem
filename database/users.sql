-- quantum_bank.users definition

CREATE TABLE `users` (
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `phone_number` decimal(10,0) NOT NULL,
  `pan` varchar(10) NOT NULL,
  `aadhar_number` decimal(12,0) NOT NULL,
  `name` varchar(30) NOT NULL,
  `dob` date NOT NULL,
  `gender` enum('M','F') NOT NULL,
  `account_no` decimal(16,0) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `users_pk` (`pan`),
  UNIQUE KEY `users_pk_2` (`aadhar_number`),
  UNIQUE KEY `users_pk_3` (`account_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
