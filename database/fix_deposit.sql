-- quantum_bank.fix_deposit definition

CREATE TABLE `fix_deposit` (
  `fd_no` bigint NOT NULL AUTO_INCREMENT,
  `acc_no` decimal(16,0) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `maturity_amount` decimal(10,2) NOT NULL,
  `roi` decimal(3,1) NOT NULL,
  `start_date` date NOT NULL,
  `maturity_date` date NOT NULL,
  `years` int NOT NULL,
  PRIMARY KEY (`fd_no`),
  KEY `fix_deposit_accounts_account_no_fk` (`acc_no`),
  CONSTRAINT `fix_deposit_accounts_account_no_fk` FOREIGN KEY (`acc_no`) REFERENCES quantum_bank.accounts (`account_no`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
