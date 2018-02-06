How would you improve the following Python snippet? In terms of readability, bug-free, and performance.

import os
from commands import getoutput

BASEDIR = '/home/user/Download'

def find_fn_fp():
    positive_c = 0
    cmd = 'ls testfn*'
    splits = getoutput(cmd).split('\n')
    for item in splits:

        """ command line 'ls testfn*' and BASEDIR absolute path the provided path is missing "testfn*" folders
            "ls testfn*" will get all the files under all testfn* folders under the relative path name and only
            return all files name not include folders name. BASEDIR can not include testfn* order command So
            path = os.path.join(BASEDIR, item) is e.g.path = "/home/user/Download/filename" which is wrong """

        path = os.path.join(BASEDIR, item)

        with open(path,'r') as f:
            for line in f:
                cols = line.split(',')

                """ If the judgment condition "if len(cols) is not 12:"and print result "print 'csv line error, not 11
                    columns'logic does not match. Base on follow-up logic to determine the conditions, I personally think that
                    "Clean" is data label which only appear at the end of the data line close[10], so "if len(cols) is not 12"
                     modify to "if len(cols) is not 11". """

                if len(cols) is not 12:
                    print 'csv line error, not 11 columns'

                """ The following logic to determine the existence of duplication, low efficiency """
                if not cols[1] and not cols[2] and cols[10] != 'Clean':
                    if cols[9] == '0':
                        positive_c += 1
                if cols[1] and cols[2] and not cols[10]:
                    if cols[9] == '0':
                        positive_c += 1
    print('Positive:%d'%positive_c)

find_fn_fp()

########################################################################

Based on the original program improvement:
# Fix bugs
# Object-oriented design to improve re-usability
# Achieve multi-threading, improve efficiency
# Fuzzy check all similar folder name to enhance the use of the scene
# Optimize the logic to improve efficiency, meanWhile program easy add logic to judge the condition
# Modular development is easy to maintain
# Modify coding style and easy to understand
