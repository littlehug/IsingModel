#!/usr/bin/python
# -*- coding: utf8 -*-
import MySQLdb

class DBConn:
    # Set the info about connection
    def __init__(self, user, passwd):
        self.user = user
        self.host = 'mysql'
        self.passwd = passwd
        self.dbname = user
        
    def dbConnect(self):
        self.db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.dbname, charset='utf8')
        self.cursor = self.db.cursor()
        
    # Build SQL statement query function
    def runQuery(self, sql):
        self.cursor.execute(sql)
        self.results = self.cursor.fetchall()
        
    # SQL Insert, Update, Delete
    def RUN(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
        
    # Close the connection
    def dbClose(self):
        self.db.close()

"""Non-Object design
try:
    db = MySQLdb.connect(host="mysql", user="phoebechang", passwd="...", db="phoebechang")
    sql = "SELECT codeA, code B FROM coding5"

    # execute SQL statement
    cursor = db.cursor()
    cursor.execute(sql)
    
    # fetch multi-data
    results = cursor.fetchall()

    # fetch data with loops
    for record in results:
        col1 = record[0]
        col2 = record[1]
        print "%s, %s" % (col1, col2)
    # stop connection
    db.close()
    
except MySQLdb.Error as e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    
"""
