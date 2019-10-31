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
all_token_pos = {}

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
# 6.
print(sorted(full_pos_taggs.items(), key=lambda item: item[1], reverse=True))
print(l_count)
# [('NN', 60268), ('IN', 46842), ('DT', 39105), ('NNP', 37595), ('JJ', 29217), ('NNS', 28323), ('RB', 14472), ('VBD', 14122), ('VB', 12613), ('PRP', 12197), ('CC', 10565), ('TO', 10497), ('VBZ', 10338), ('VBN', 9384), ('VBG', 7113), ('VBP', 5952), ('CD', 5003), ('MD', 4688), ('POS', 3884), ('WDT', 2114), ('JJR', 1494), ('WP', 1170), ('NNPS', 1097), ('WRB', 967), ('JJS', 865), ('RP', 857), ('RBR', 784), ('EX', 388), ('PDT', 184), ('RBS', 182), ('FW', 108), ('UH', 33), ('LS', 13), ('SYM', 13)]
# 372447
# 60268 / 372447 = 0.1618

ambiguous_count = 0
unambiguous_count = 0
for tpc in term_postag_count:
    if len(tpc) > 1:
        ambiguous_count += 1
    else:
        unambiguous_count += 1
print('ambiguous_count', ambiguous_count, 'unambiguous_count', unambiguous_count)
# ambiguous_count 23553 unambiguous_count 40

# 7.consider a naive approach to POS tagging which simply assigns to each token its own most common POS tag
# 8. compute accuracy score
common_pos_tag = {}
for tpc in term_postag_count:
    tpc_item = term_postag_count[tpc]
    sort_re = sorted(tpc_item.items(), key=lambda item: item[1], reverse=True)
    common_pos_tag[tpc] = sort_re[0][0]


def compute_accuracy(dic, file_path):
    _file = open(file_path, 'r')
    lex_count = 0
    right_count = 0

    for _line in _file:
        for _l in lex.findall(_line):
            lex_count += 1
            _token = _l.split('/')[0]
            _pos = _l.split('/')[1]
            _predict_pos = 'NN'
            if _token in dic:
                _predict_pos = dic[_token]
            if _predict_pos == _pos:
                right_count += 1
    print(right_count / lex_count)
    return right_count / lex_count


compute_accuracy(common_pos_tag, 'POSTAG_DATA/training_data.txt')  # 0.08333333333333333
compute_accuracy(common_pos_tag, 'POSTAG_DATA/test_data.txt')  # 0.08333333333333333
