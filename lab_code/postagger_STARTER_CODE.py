"""
USE: python <PROGNAME> (options) 
OPTIONS:
    -h : print this help message and exit
    -d FILE : use FILE as data to create a new lexicon file
    -l FILE : create OR read lexicon file FILE
    -t FILE : apply lexicon to test data in FILE
"""
################################################################

import sys, re, getopt

################################################################
# Command line options handling, and help

opts, args = getopt.getopt(sys.argv[1:], 'hd:l:t:')
opts = dict(opts)

print(opts)


def printHelp():
    help = __doc__.replace('<PROGNAME>', sys.argv[0], 1)
    print('-' * 60, help, '-' * 60, file=sys.stderr)
    sys.exit()


if '-h' in opts:
    printHelp()

if len(args) > 0:
    print("\n** ERROR: no arg files - only options! **", file=sys.stderr)
    printHelp()

if '-l' not in opts:
    print("\n** ERROR: must specify lexicon file name (opt: -l) **", file=sys.stderr)
    printHelp()

################################################################

# read file
file = opts['-l']
f = open(file, 'r')
lex = re.compile(r'[A-Za-z]+/[A-Za-z]+')
term_postag_count = {}
full_pos_taggs = {}
l_count = 0

for line in f:
    for l in lex.findall(line):
        l_count += 1
        token = l.split('/')[0]
        pos = l.split('/')[1]
        if token in term_postag_count:
            if pos in term_postag_count[token]:
                term_postag_count[token][pos] += 1
            else:
                term_postag_count[token][pos] = 1
        else:
            term_postag_count[token] = {}
            term_postag_count[token][pos] = 1

        if pos in full_pos_taggs:
            full_pos_taggs[pos] += 1
        else:
            full_pos_taggs[pos] = 1

print(sorted(full_pos_taggs.items(), key=lambda item: item[1], reverse=True))
print(l_count)

ambiguous_count = 0
unambiguous_count = 0
for tpc in term_postag_count:
    if len(tpc) > 1:
        ambiguous_count += 1
    else:
        unambiguous_count += 1
print(ambiguous_count, unambiguous_count)

# 7.consider a naive approach to POS tagging which simply assigns to each token its own most common POS tag
common_pos_tag = {}
for tpc in term_postag_count:
    tpc_item = term_postag_count[tpc]
    sort_re = sorted(tpc_item.items(), key=lambda item: item[1], reverse=True)
    common_pos_tag[tpc] = sort_re[0][0]
print(common_pos_tag)

# compute accuracy



