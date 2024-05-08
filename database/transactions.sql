-- quantum_bank.transactions definition

CREATE TABLE `transactions` (
  `transaction_id` bigint NOT NULL AUTO_INCREMENT,
  `acc_no` decimal(16,0) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `transaction_type` enum('DEPOSIT','WITHDRAWAL','FD_CREATION','FD_BREAK','FD_MATURE') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`transaction_id`),
  KEY `transactions_accounts_FK` (`acc_no`),
  CONSTRAINT `transactions_accounts_FK` FOREIGN KEY (`acc_no`) REFERENCES quantum_bank.accounts (`account_no`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
