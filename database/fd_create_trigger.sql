CREATE  TRIGGER `fd_create_trigger`
AFTER INSERT ON quantum_bank.fix_deposit
FOR EACH ROW BEGIN

	declare amount decimal(10,2);
	DECLARE acc_no decimal(16);

	set amount = new.amount;
	SET acc_no = NEW.acc_no;

	IF amount > 0 THEN
        INSERT INTO quantum_bank.transactions (acc_no, amount, transaction_type)
        VALUES (acc_no, amount, 'FD_CREATION');
    END IF;
END;
