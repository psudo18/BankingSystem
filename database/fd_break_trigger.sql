CREATE  TRIGGER `fd_break_trigger`
AFTER DELETE ON quantum_bank.fix_deposit
FOR EACH ROW BEGIN

	declare acc_no decimal(16);
	declare amount decimal(10,2);

	set acc_no = old.acc_no;
	set amount = old.amount;

	if curdate() < old.maturity_date then
		INSERT INTO quantum_bank.transactions (acc_no, amount, transaction_type)
    	VALUES (acc_no, amount, 'FD_BREAK');
    end if;
END;
