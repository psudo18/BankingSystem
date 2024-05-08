CREATE TRIGGER `deposit_trigger`
AFTER UPDATE ON quantum_bank.accounts
FOR EACH ROW BEGIN
	DECLARE acc_no decimal(16);

	SET acc_no = NEW.account_no;

	IF NEW.balance > OLD.balance AND @DISABLE_TRIGGER IS NOT true THEN
        INSERT INTO quantum_bank.transactions (acc_no, amount, transaction_type)
        VALUES (acc_no, NEW.balance - OLD.balance, 'DEPOSIT');
    END IF;
END;