from CountPositiveLines import *

# Please input please enter a valid base path,the end needs "/"
base_dir = '/Users/leonsaber/Desktop/'

# Under the base path of the folder fuzzy query regular expressions
folder_name = 'testfnfp*'

worker = CountPositiveLines()
print('Positive:%d' % worker.count_folder_positive_line(base_dir, folder_name))


