"""
http://ncse.ie/wp-content/uploads/2016/05/NCSE-Allocation-of-RT-to-Primary-Schools-September-2016.pdf
"""

import csv, sys

wr = csv.writer(sys.stdout)

wr.writerow(('County', 'RollNumber', 'Name', 'hours_201610', 'hours_201609'))

wr.writerows(csv.reader(sys.stdin))
