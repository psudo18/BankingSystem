create table users
(
    username      varchar(30)     not null
        primary key,
    password      varchar(30)     not null,
    phone_number  decimal         not null,
    pan           varchar(10)     not null,
    aadhar_number decimal(12)     not null,
    name          varchar(30)     not null,
    dob           date            not null,
    gender        enum ('M', 'F') not null,
    account_no    decimal(16)     not null,
    constraint users_pk
        unique (pan),
    constraint users_pk_2
        unique (aadhar_number),
    constraint users_pk_3
        unique (account_no)
);


