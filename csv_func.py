# -*- coding: utf-8 -*-
#!/usr/bin/env python2

"""
Example for you to import this function:
    from csv_func import csv_deal
    filename = "example.csv"
    csv_do = csv_deal(filename)
    csv_do.print_row()
    data = [[1, 2 ,3], [4, 5, 6]]
    csv_do.write_row(data)
"""

import csv

class csv_deal:
    def __init__(self, filename):
        self.filename = filename
    def print_row(self):
        f = open(self.filename, 'r')
        for row in csv.reader(f):
            print row
        f.close()
    def write_row(self, data):
        f = open(self.filename, 'w')
        w = csv.writer(f)
        w.writerows(data)
        f.close()


