"""
Source of this data:

'Find a school' and save response to GetSchoolsMap request.
"""

import json, csv, sys

with open('schools-list.json', 'rt') as f_in:
    data_0 = json.load(f_in)

raw_schools = json.loads(data_0['d'])

def float_or_zero(s):
    try:
        return float(s)
    except:
        return 0.0

col_descrs = [(str, 'Address1'),
              (str, 'Address2'),
              (str, 'Address3'),
              (str, 'Address4'),
              (str, 'County'),
              (str.strip, 'Email'),
              (int, 'Enrol_female'),
              (int, 'Enrol_male'),
              (int, 'Enrol_total'),
              (str, 'Ethos'),
              (str, 'Gender'),
              (int, 'ID'),
              (str, 'Lang'),
              (float_or_zero, 'Lat'),
              (float_or_zero, 'Long'),
              (str, 'Name'),
              (str, 'Phone'),
              (str, 'Principal'),
              (str, 'RollNumber'),
              (str, 'Website')]

def school_as_tuple(s):
    return tuple([f(s[c]) for f, c in col_descrs])

schools = [school_as_tuple(s) for s in raw_schools]

wr = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
wr.writerow(tuple(d[1] for d in col_descrs))
wr.writerows(schools)

"""
python schools_data.py >| schools.csv
"""
