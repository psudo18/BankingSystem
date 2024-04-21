CREATE TRIGGER trg_insert_accounts
AFTER INSERT ON quantum_bank.users
FOR EACH ROW
BEGIN
    -- Extract data from the newly inserted row
    DECLARE v_acc_no decimal(16);
    DECLARE v_name varchar(30);

    SET v_acc_no = NEW.account_no;
    SET v_name = NEW.name;

    -- Insert data into the accounts table
    INSERT INTO quantum_bank.accounts (account_no, name)
    VALUES (v_acc_no, v_name);
END;
