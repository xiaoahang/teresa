"""\
------------------------------------------------------------
USE: python <PROGNAME> (options) file1...fileN
OPTIONS:
    -h : print this help message
    -b : use BINARY weights (default: count weighting)
    -s FILE : use stoplist file FILE
    -I PATT : identify input files using pattern PATT, 
              (otherwise uses files listed on command line)
------------------------------------------------------------
"""

import sys, re, getopt, glob

opts, args = getopt.getopt(sys.argv[1:], 'hs:bI:')
opts = dict(opts)
filenames = args

##############################
# HELP option

if '-h' in opts:
    progname = sys.argv[0]
    progname = progname.split('/')[-1]  # strip out extended path
    help = __doc__.replace('<PROGNAME>', progname, 1)
    print(help, file=sys.stderr)
    sys.exit()

##############################
# Identify input files, when "-I" option used

if '-I' in opts:
    filenames = glob.glob(opts['-I'])

print('INPUT-FILES:', ' '.join(filenames))

##############################
# STOPLIST option

stops = set()
if '-s' in opts:
    with open(opts['-s'], 'r') as stop_fs:
        for line in stop_fs:
            stops.add(line.strip())

##############################

if '-b' in opts:
    # sensitive of not
    print(opts)


# findall convert to lowercase
# and then tran save to another files
def txt_to_lower_case(filenames):
    for name in filenames:
        print(name)
        with open(name, 'r') as fileinput:
            for line in fileinput:
                line = line.lower()
                print(line)


def count_words():
    return 0


def count_overlap():
    return 0


def count_overlap_sensitive():
    return 0


txt_to_lower_case(filenames)
# compare.py -s stop_list.txt NEWS/news01.txt NEWS/news02.txt