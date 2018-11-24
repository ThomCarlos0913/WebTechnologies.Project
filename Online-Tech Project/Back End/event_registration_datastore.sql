Create Database OnlineTechDataStore;
use OnlineTechDataStore;

CREATE TABLE users_account (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    account_username VARCHAR(50) NOT NULL,
    account_password VARCHAR(255) NOT NULL,
    account_email VARCHAR(50) NOT NULL,
    account_created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    account_privelege INT NOT NULL
);

insert into users_account (account_username, account_password, account_email, account_privelege)
	values ('ThomCarlos', '123asdqw', 'johnthomas.carlos@gmail.com', 2);

insert into users_account (account_username, account_password, account_email, account_privelege)
	values ('DexterCuaresma', 'dexter', 'cuaresmadexterjames@gmail.com', 2);

insert into users_account (account_username, account_password, account_email, account_privelege)
	values ('MarkCaadyang', 'pogiako123', 'caadyangmark4599@gmail.com', 2);

insert into users_account (account_username, account_password, account_email, account_privelege) 
	values ('RalphOrtiz', 'ralph123', 'ralph@gmail.com', 2);
