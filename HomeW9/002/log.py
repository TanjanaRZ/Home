import csv
from datetime import datetime

def writeLog(name, request, answer, date):
    f = open('log.csv', 'a')
    writer = csv.writer(f, lineterminator='\r')
    writer.writerow([name, request, answer, datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')])
    f.close()