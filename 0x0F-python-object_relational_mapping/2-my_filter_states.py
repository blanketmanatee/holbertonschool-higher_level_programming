#!/usr/bin/python3

import sys
import mySQLdb

if __name == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT *  from 'states' WHERE BINARY 'name' = '{}'"
                  .format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
