-- quantum_bank.accounts definition

CREATE TABLE `accounts` (
  `account_no` decimal(16,0) NOT NULL,
  `balance` decimal(10,2) NOT NULL DEFAULT '0.00',
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`account_no`),
  CONSTRAINT `accounts_users_account_no_fk` FOREIGN KEY (`account_no`) REFERENCES quantum_bank.users (`account_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
