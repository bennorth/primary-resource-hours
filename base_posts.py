"""
Source of base posts:

http://www.education.ie/en/Circulars-and-Forms/Active-Circulars/cl0007_2016_appendix_C.pdf
"""

import csv, sys

wr = csv.writer(sys.stdout)

wr.writerow(('County', 'RollNumber', 'Name', 'Address',
             'GAM_EAL_full_posts', 'GAM_EAL_hours',
             'padding_0',
             'GAM_EAL_posts_clustered', 'GAM_EAL_clustering_hours',
             'padding_1',
             'Permanent_resource_posts',
             'padding_1',
             'Additional_allocation'))

wr.writerows(csv.reader(sys.stdin))

"""
python base_posts.py < base-posts.csv >| base-posts-headed.csv
"""
