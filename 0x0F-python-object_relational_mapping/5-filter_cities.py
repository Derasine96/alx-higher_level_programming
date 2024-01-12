#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
    Usage: ./0-select_states.py sys.argv[1] sys.argv[2] hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "INNER JOIN states ON states.id=cities.state_id "
        "WHERE cities.name LIKE BINARY %s"
        )
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
