#!/usr/bin/python
# -*- coding: utf8 -*-
# coding:UTF-8
import decimal
import sys

# To import DB Object
from DBconnect import DBConn

country = ""

if len(sys.argv) < 2:
    print("No connect to MySQL")
    sys.exit()
else:
    user = sys.argv[1]
    passwd = sys.argv[2]
    country = sys.argv[3]
try:
    dbuse = DBConn(user, passwd)
    dbuse.dbConnect()
except:
    print("MySQL DB Error")


if country == "Taiwan" or country == "taiwan":
    table = "Criminal_Laws_Taiwan_ce"
else:
    table = "Criminal_Laws_China_ce"
    
def is_chinese(uchar):
    if uchar.isalnum():
        return False
    uchar = uchar.decode('utf8')
    for c in uchar:
        if not u'\u4e00' <= c <= u'\u9fa5':
            return False
    return True

while True:
    try:
        line = raw_input()
        if line and line.find("deleted") == -1 and line.find("( 刪除 )") == -1:
            tmp = line.partition("-")
            text = tmp[0].split()
            data = tmp[2].split()
            chinese = english = ""
            col = 0
            for x in text:
                if is_chinese(x):
                    if chinese != "":
                        chinese += " "
                    chinese += x
                elif x.isalpha():
                    if english == "":
                        col = 1
                    else:
                        english += " "
                    english += x
                elif x.isdigit():
                    if col == 0:
                        chinese += " " + x
                    else:
                        english += " " + x
            if len(data) == 3:
                ce = float(data[0])
                ec = float(data[1])
                number = int(data[2])
            #print (line, tmp, text, data)
            #print (chinese.decode('utf8'), english, ce, ec, number)
            if chinese != "" and english != "" and len(data) == 3:
                sql = "INSERT INTO {0} (Chinese, English, CE, EC, NUMBER) \
VALUES ('{1}', '{2}', {3}, {4}, {5})".format(table, chinese, english , ce, ec, number)
                #print(sql)
                dbuse.RUN(sql)
    except EOFError:
        break
    
dbuse.dbClose()
