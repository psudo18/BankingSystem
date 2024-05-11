create table transactions
(
    transaction_id     bigint auto_increment
        primary key,
    acc_no             decimal(16)                                                                                   not null,
    amount             decimal(10, 2)                                                                                not null,
    transaction_type   enum ('DEPOSIT', 'WITHDRAWAL', 'FD_CREATION', 'FD_BREAK', 'FD_MATURE', 'CREDITED', 'DEBITED') not null,
    date               timestamp   default CURRENT_TIMESTAMP                                                         not null,
    transaction_detail varchar(16) default 'SELF'                                                                    not null,
    constraint transactions_accounts_FK
        foreign key (acc_no) references quantum_bank.accounts (account_no)
);


