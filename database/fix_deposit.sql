create table fix_deposit
(
    fd_no           bigint auto_increment
        primary key,
    acc_no          decimal(16)    not null,
    amount          decimal(10, 2) not null,
    maturity_amount decimal(10, 2) not null,
    roi             decimal(2, 1)  not null,
    start_date      date           not null,
    maturity_date   date           not null,
    years           int            not null,
    constraint fix_deposit_accounts_account_no_fk
        foreign key (acc_no) references quantum_bank.accounts (account_no)
);


