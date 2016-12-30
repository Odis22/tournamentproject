import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def delete_matches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM results")
    db.commit()
    db.close()


def delete_players():

    db = connect()
    c = db.cursor()
    query = ("DELETE FROM players;")
    c.execute(query)
    db.commit()
    db.close()


def count_players():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    query = ("SELECT count(players.player_id) AS player_count FROM players;")
    c.execute(query)
    count = int(c.fetchone()[0])
    db.close()
    return count


def register_player(name):

    db = connect()
    c = db.cursor()
    query = ("INSERT INTO players (name) values (%s);")
    c.execute(query, (name,))
    db.commit()
    db.close()


def player_standings():

    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM standings;")
    matches = c.fetchall()
    db.close()
    return matches


def report_match(winner, loser):
    """Records the outcome of a single match between two players.

 Args:
    winner:  the id number of the player who won
    loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    q = "INSERT INTO results (winner, loser) values (%s, %s);"
    c.execute(q, (int(winner), int(loser)))
    db.commit()
    db.close()


def breakIntoGroups(list, size=2):
    size = max(1, size)
    return [list[i:i + size]for i in range(0, len(list), size)]


def swiss_pairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
    A list of tuples, each of which contains (id1, name1, id2, name2)
    id1: the first player's unique id
    name1: the first player's name
    id2: the second player's unique id
    name2: the second player's name
    """
    standings = player_standings()
    grouped_pool = breakIntoGroups(standings, 2)
    matched_pairs = list()

    for pair in grouped_pool:
        pairing = list()
        for player in pair:
            pairing.append(player[0])
            pairing.append(player[1])
        matched_pairs.append(pairing)

    return matched_pairs
