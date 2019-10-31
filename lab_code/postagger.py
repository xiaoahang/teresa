"""
USE: python <PROGNAME> (options) 
OPTIONS:
    -h : print this help message and exit
    -d FILE : use FILE as data to create a new lexicon file
    -l FILE : create OR read lexicon file FILE
    -r FILE : apply train lexicon to test data in FILE
    -e FILE : apply test lexicon to test data in FILE
"""
################################################################

import sys, re, getopt


class CommandLine:
    def __init__(self):
        opts, args = getopt.getopt(sys.argv[1:], 'hd:l:r:e:')
        opts = dict(opts)
        self.argfiles = [opts['-r'], opts['-e']]

        if '-h' in opts:
            self.printHelp()

        if len(args) > 0:
            print("\n** ERROR: no arg files - only options! **", file=sys.stderr)
            self.printHelp()

        # if '-l' not in opts:
        #     print("\n** ERROR: must specify lexicon file name (opt: -l) **", file=sys.stderr)
        #     self.printHelp()

        if '-r' not in opts:
            print("\n** ERROR: must specify train lexicon file name (opt: -r) **", file=sys.stderr)
            self.printHelp()

        if '-e' not in opts:
            print("\n** ERROR: must specify test lexicon file name (opt: -e) **", file=sys.stderr)
            self.printHelp()

    def printHelp(self):
        help = __doc__.replace('<PROGNAME>', sys.argv[0], 1)
        print('-' * 60, help, '-' * 60, file=sys.stderr)
        sys.exit()


class POSTagging:
    def __init__(self, config):
        self.train_path = config.argfiles[0]
        self.test_path = config.argfiles[1]
        self.default_pos = 'NN'
        self.results = {}
        self.term_postag_count = {}  # term postag count
        self.full_pos_taggs = {}  # postag count
        self.common_pos_tag = {}  # term most_occur_postag
        self.lex = re.compile('r[A-Za-z]+/[A-Za-z]+')

    def train(self):
        f = open(self.train_path, 'r')
        for line in f:
            for l in self.lex.findall(line):
                token = l.split('/')[0]
                pos = l.split('/')[1]
                if token in self.term_postag_count:
                    if pos in self.term_postag_count[token]:
                        self.term_postag_count[token][pos] += 1
                else:
                    self.term_postag_count[token] = {pos: 1}

                if pos in self.full_pos_taggs:
                    self.full_pos_taggs[pos] += 1
                else:
                    self.full_pos_taggs[pos] = 1

        for tpc in self.term_postag_count:
            tpc_item = self.term_postag_count[tpc]
            sort_re = sorted(tpc_item.items(), key=lambda item: item[1], reverse=True)
            self.common_pos_tag[tpc] = sort_re[0][0]
        self.default_pos = sorted(self.full_pos_taggs.items(), key=lambda i: i[1], reverse=True)[0][0]

    def test(self):
        f = open(self.test_path, 'r')
        lex_count = 0
        right_count = 0
        for line in f:
            for l in self.lex.findall(line):
                lex_count += 1
                token = l.split('/')[0]
                pos = l.split('/')[1]
                predict_pos = self.default_pos
                if token in self.common_pos_tag:
                    predict_pos = self.common_pos_tag[token]
                if predict_pos == pos:
                    right_count += 1
        self.result = right_count / lex_count

    def printResults(self):
        print(self.result)


if __name__ == '__main__':
    config = CommandLine()
    postagging = POSTagging(config)
    postagging.train()
    postagging.test()
    postagging.printResults()
