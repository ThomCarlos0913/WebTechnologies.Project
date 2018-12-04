from models import *

class DbInitData:
    def fetch_data():
        admin_list = []
        admin_list.append(User(username = "ThomCarlos",
                        password = "thom123",
                        email = "johnthomas.carlos@gmail.com",
                        privelege = 2))
        admin_list.append(User(username = "DexterCuaresma",
                        password = "dexter",
                        email = "cuaresmadexterjames@gmail.com",
                        privelege = 2))
        admin_list.append(User(username = "MarkCaadyang",
                        password = "pogiako123",
                        email = "caadyangmark4599@gmail.com",
                        privelege = 2))
        admin_list.append(User(username = "RalphOrtiz",
                        password = "ralph123",
                        email = "ralphchrstian.ortiz@gmail.com",
                        privelege = 2))

        # Initialize event details
        event_details = []
        event_details.append(Event(i_title = 'Perth St Andrew’s Day Scottish Festival',
                          i_venue = 'King Edward Street, Pert',
                          i_time = '2018-12-02',
                          i_details = 'Celebrate St Andrews Day with live music and a marketplace selling food and drink from Scotland’s natural larder.',
                          i_passed = 1))
        event_details.append(Event(i_title = 'Over 35s to 50s Plus Party for Singles & Couples',
                          i_venue = 'Ashwells Country Club, Brentwood',
                          i_time = '2018-11-30',
                          i_details = 'A chance to meet fellow singles and new friends with a pop soundtrack from the 80s right up to last week. Singles and couples welcome.',
                          i_passed = 1))
        event_details.append(Event(i_title = 'Festive Party',
                          i_venue = 'Edinburgh',
                          i_time = '2019-02-03',
                          i_details = 'Celebrate Christmas in the Ghillie Dhu Auditorium with a three-course festive meal, a live ceilidh band and a DJ.',
                          i_passed = 0))
        event_details.append(Event(i_title = 'New Years Eve Gin and Fizz Party Night',
                          i_venue = 'Best Western Old Mill Hotel & Leisure Club, Bury',
                          i_time = '2018-12-31',
                          i_details = 'See in the New Year with a five course meal, gin, fizz and live music.',
                          i_passed = 0))
        event_details.append(Event(i_title = 'Hogmanay at Harvey Nichols',
                          i_venue = 'Harvey Nichols Forth Floor Restaurant, Brasserie, and Bar, Edinburgh',
                          i_time = '2018-12-09',
                          i_details = 'Arrive to champagne and bagpipes, sit down to a five-course dinner with paired wines, enjoy live music, dancing and a late night buffet, then watch the fireworks over the castle.',
                          i_passed = 0))
        event_details.append(Event(i_title = 'Concert in the Gardens',
                          i_venue = 'Princes Street Gardens, Edinburgh',
                          i_time = '2018-11-21',
                          i_details = 'See in 2019 with headliners Franz Ferdinand, supported by Metronomy and Free Love.',
                          i_passed = 1))
        event_details.append(Event(i_title = 'Aftermath the Game',
                          i_venue = 'The Old Bank of England, London EC4A',
                          i_time = '2018-12-15',
                          i_details = 'Escape game adventures which can either be played as individual, stand-alone experiences or played back-to-back for a more immerse narrative.',
                          i_passed = 0))
        event_details.append(Event(i_title = 'Bath on Ice',
                          i_venue = 'Royal Victoria Park, Bath',
                          i_time = '2018-12-16',
                          i_details = 'Bath gets a festive makeover with ice skating, glow-in-the-dark mini golf, wood-fired pizza and festive drinks aplenty.',
                          i_passed = 0))
        event_details.append(Event(i_title = 'Buddy Hollys Winter Dance Party',
                          i_venue = 'Burnley Mechanics',
                          i_time = '2019-02-06',
                          i_details = 'In the style of Buddy Hollys string of dance parties across the American mid west in 1959, celebrate the music of Ritchie Valens, Big Bopper, Dion & the Belmonts and Buddy Holly.',
                          i_passed = 0))
        event_details.append(Event(i_title = 'Burns Hame Toun',
                          i_venue = 'Burns Cottage, Alloway',
                          i_time = '2019-01-23',
                          i_details = 'Street party celebrating Burns with a strip the willow world record attempt, live music, haggis and whisky festival and much more.',
                          i_passed = 0))
        event_details.append(Event(i_title = 'Christmas Spectacular',
                          i_venue = 'London Palladium, W1F',
                          i_time = '2018-12-26',
                          i_details = "Soprano Claire Rutter, tenor Peter Auty, The Jingle Belle Dancers and ballet principals Ekaterina Bulgutova and Yuri Kudriavtsev join the orchestra for a feast of Christmas fun including Andersons Sleigh Ride, Tchaikovskys The Nutcracker Suite, Winter from Vivald is The Four Seasons and Dukas Sorcerer Apprentice as featured in Disneys antasia. Conducted by John Rigby.",
                          i_passed = 0))
        event_details.append(Event(i_title = 'Dancers Black Tie Dinner & Ball',
                          i_venue = 'Scarborough Spa',
                          i_time = '2019-02-14',
                          i_details = 'Black tie dinner and ball, with a three-course meal and plenty of ballroom, Latin and sequence dancing.',
                          i_passed = 0))
        event_details.append(Event(i_title = 'The Dating Show Live 2019',
                          i_venue = 'NEC, Birmingham',
                          i_time = '2019-03-12',
                          i_details = 'Dating expo with musical performances from the cast of Jersey Boys and Sheila Ferguson.',
                          i_passed = 0))
        event_details.append(Event(i_title = 'Friday Night Social',
                          i_venue = 'Teviot, Edinburgh',
                          i_time = '2018-12-01',
                          i_details = 'An opportunity to meet new people over a drink or two at he end of the week.',
                          i_passed = 1))
        event_details.append(Event(i_title = 'Now Thats What I Call Pop Music',
                          i_venue = 'Caseys Venues, Donnington',
                          i_time = '2018-08-04',
                          i_details = 'Journey through the eras of pop music with a live show and DJ.',
                          i_passed = 1))

        featured_e = Featured(i_title = 'Christmas Spectacular',
                          i_venue = 'London Palladium, W1F',
                          i_time = '2018-12-26',
                          i_details = "Soprano Claire Rutter, tenor Peter Auty, The Jingle Belle Dancers and ballet principals Ekaterina Bulgutova and Yuri Kudriavtsev join the orchestra for a feast of Christmas fun including Andersons Sleigh Ride, Tchaikovskys The Nutcracker Suite, Winter from Vivald is The Four Seasons and Dukas Sorcerer Apprentice as featured in Disneys antasia. Conducted by John Rigby.",
                          i_passed = 0)

        return (admin_list, event_details, featured_e)
