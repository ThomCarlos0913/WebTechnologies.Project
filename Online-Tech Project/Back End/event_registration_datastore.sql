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

CREATE TABLE event_details (
    event_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    event_title VARCHAR(70),
    event_date  DATE NOT NULL,
    event_venue TEXT NOT NULL,
    event_description TEXT NOT NULL
);

Insert into event_details(event_title,event_date,event_venue,event_description)
values('Perth St Andrew’s Day Scottish Festival',
			"2018-12-02",
            'King Edward Street, Pert',
            'Celebrate St Andrews Day with live music and a marketplace selling food and drink from Scotland’s natural larder.'
	   ),
       ('Over 35s to 50s Plus Party for Singles & Couples',
			"2018-11-30",
            'ashwells country club, brentwood',
            'A chance to meet fellow singles and new friends with a pop soundtrack from the 80s right up to last week. Singles and couples welcome.'

       ),
       ('Festive Party.',
			"2019-02-03",
            'Edinburgh',
            'Celebrate Christmas in the Ghillie Dhu Auditorium with a three-course festive meal, a live ceilidh band and a DJ.'
       ),
       ('New Years Eve Gin and Fizz Party Night',
			"2018-12-31",
            'Best Western Old Mill Hotel & Leisure Club, Bury',
            'See in the New Year with a five course meal, gin, fizz and live music.'
       ),
       ('Hogmanay at Harvey Nichols',
			"2018-12-09",
            'Harvey Nichols Forth Floor Restaurant, Brasserie, and Bar, Edinburgh',
            'Arrive to champagne and bagpipes, sit down to a five-course dinner with paired wines,
			enjoy live music, dancing and a late night buffet, then watch the fireworks over the castle.'
       ),
       ('Concert in the Gardens',
			"2018-11-21",
            'Princes Street Gardens, Edinburgh',
            'See in 2019 with headliners Franz Ferdinand, supported by Metronomy and Free Love.'
       ),
       ('Aftermath the Game',
			"2018-12-15",
            'The Old Bank of England, London EC4A',
            'Escape game adventures which can either be played as individual, stand-alone experiences or played back-to-back for a more immerse narrative.'
       ),
       ('Bath on Ice',
			"2018-12-16",
            'Royal Victoria Park, Bath',
            'Bath gets a festive makeover with ice skating, glow-in-the-dark mini golf, wood-fired pizza and festive drinks aplenty.'
       ),
       ('Buddy Hollys Winter Dance Party',
			"2019-02-06",
            'Burnley Mechanics',
            'In the style of Buddy Hollys string of dance parties across the American mid west in 1959, celebrate the music of Ritchie Valens,
			 Big Bopper, Dion & the Belmonts and Buddy Holly.'
       ),
       ('Burns Hame Toun',
			"2019-01-23",
            'Burns Cottage, Alloway',
            'Street party celebrating Burns with a strip the willow world record attempt, live music, haggis and whisky festival and much more.'
       ),
       ('Christmas Spectacular',
			"2018-12-26",
            'London Palladium, W1F',
            'Soprano Claire Rutter, tenor Peter Auty, The Jingle Belle Dancers and ballet principals Ekaterina Bulgutova and Yuri Kudriavtsev join
			 the orchestra for a feast of Christmas fun including Andersons Sleigh Ride, Tchaikovskys The Nutcracker Suite, Winter from Vivaldis The
			 Four Seasons and Dukas Sorcerer Apprentice as featured in Disneys antasia. Conducted by John Rigby.'
       ),
       ('Dancers Black Tie Dinner & Ball',
			"2019-02-14",
            'Scarborough Spa',
            'Black tie dinner and ball, with a three-course meal and plenty of ballroom, Latin and sequence dancing.'
       ),
       ('The Dating Show Live 2019',
			"2019-03-12",
            'NEC, Birmingham',
            'Dating expo with musical performances from the cast of Jersey Boys and Sheila Ferguson.'
       ),
       ('Friday Night Social',
			"2018-12-01",
            'Teviot, Edinburgh',
            'An opportunity to meet new people over a drink or two at he end of the week.'
       ),
       ('Now Thats What I Call Pop Music',
			"2019-03-04",
            'Caseys Venues, Donnington',
            'Journey through the eras of pop music with a live show and DJ.'

       );
