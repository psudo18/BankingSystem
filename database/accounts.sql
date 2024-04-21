create table accounts
(
    account_no decimal(16)                 not null,
    balance    decimal(10, 2) default 0.00 not null,
    name       varchar(30)                 not null,
    constraint accounts_users_account_no_fk
        foreign key (account_no) references quantum_bank.users (account_no)
);


