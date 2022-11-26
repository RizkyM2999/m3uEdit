import os

print ('hello')

#python3 m3u_to_csv.py 'm3u/input.m3u' 'csv/output.csv'
#exec(open("m3u_to_csv.py 'm3u/input.m3u' 'csv/output.csv'").read())

os.system("python3 csv_to_m3u.py 'input.csv' 'output.m3u'")
