__author__ = 'Maddie Stigler'
import csv
import sqlite3

def load_course_database(db_name, csv_filename):
    """Takes two strings and reads file"""
    with open(csv_filename, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tuple(row,)
            conn = sqlite3.connect(db_name)
            with conn:
                cur = conn.cursor()
                sql_cmd = "insert into coursedata values(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(sql_cmd, (row[0], row[1], row[2],row[3], row[4], row[5], row[6] ))

if __name__ == '__main__':
    load_course_database('course1.db', 'seas-courses-5years.csv')