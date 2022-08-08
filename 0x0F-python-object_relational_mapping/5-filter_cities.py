#!/usr/bin/python3
""" Takes in the name of a state as an argument and
lists all cities of that state,
using the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = db.cursor()
    param = sys.argv[4]
    cur.execute("""
    SELECT cities.name FROM cities
    LEFT JOIN states
    ON states.id=cities.state_id
    WHERE states.name = %s
    ORDER BY cities.id ASC""", (param,))
    query_rows = cur.fetchall()
    print(', '.join(row[0] for row in query_rows))
    cur.close()
    db.close()
