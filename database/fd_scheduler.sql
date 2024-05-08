CREATE EVENT UpdateBalance
ON SCHEDULE EVERY 1 MINUTE

DO BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE _acc_no DECIMAL(16);
    DECLARE _maturity_amount DECIMAL(10, 2);
    DECLARE cur CURSOR FOR SELECT acc_no, maturity_amount FROM quantum_bank.fix_deposit WHERE maturity_date = CURRENT_DATE;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
      FETCH cur INTO _acc_no, _maturity_amount;
      IF done THEN
        LEAVE read_loop;
      END IF;
      SET @DISABLE_TRIGGER = 1;
      UPDATE quantum_bank.accounts SET balance = balance + _maturity_amount WHERE account_no = _acc_no;
      DELETE FROM quantum_bank.fix_deposit WHERE acc_no = _acc_no AND maturity_date = CURRENT_DATE;
      insert into quantum_bank.transactions (acc_no,amount,transaction_type)
      values (_acc_no, _maturity_amount, 'FD_MATURE');
    END LOOP;

    CLOSE cur;
  END
