Synopsis

I created a python module that uses the PostSQL database to keep track of players and matches in a game tournament. 
Code Example

Motivation

This project was designed to teach me how to store data and interact programmatically with that data. Now i will be able to develop a database containg fully normalized data within multiple tables and modify it. 

Installation

The project came with three templates: tournament.sql, tournament.py, and tournament_test.py
The tournament.sql contained the database schema in SQL create table commands.
the tournament.py contained the code of the module that had docstrings that instructed each function. 
The tournament_test.py contains unit tests that the functions you wrote in tournament.py

We then logged on through the vagrant virtual machine and we made sure that we had the vagrantfile in our files. 

Once I had logged into Vagrant
1.I typed in PSQL
2.vagrant=> \i tournament.sql
3.vagrant=> \q

Once I did that, I ran the test by putting typing
python tournament_test.py

Once it showed these results, 
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!

I knew i was finished.

I found this readme really helpful in follwing through on this project. Whoever this is a godsend
https://github.com/p00gz/udacity-fullstack-swiss-tournament-P2/blob/master/README.md
