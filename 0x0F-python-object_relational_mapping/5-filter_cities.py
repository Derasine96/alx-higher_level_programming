#!/usr/bin/python3
"""
    Script that lists all cities of a specific state from the database hbtn_0e_4_usa
    Usage: ./0-select_states.py sys.argv[1] sys.argv[2] hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    cities = list(row[0] for row in rows)
    print(sep=", ", *cities)
    cur.close()
    db.close()
