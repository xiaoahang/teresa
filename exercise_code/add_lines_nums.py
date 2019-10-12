import sys # this is must!!!


# file input & output
# f = open('./blabla/filepath', 'r')  # read only
# f = open('./blabla/filepath', 'w')  # write only
# f = open('./blabla/filepath', 'a')  # append only
#
# f.readline() # read line from file
# f.read() # careful : may swallow big file in one
# f.write(s) # write string s to file
# f.close() # close file

# elegant / sfficient approach for many text applications
f = open('foo.txt', 'r')
for line in f:
    print(line, end=' ')
# copy a text file, but adding line numbers
infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')
num = 0

for line in infile:
    num += 1
    print(num, line, end=' ', file=outfile)

infile.close()
outfile.close()

# script invoked as 'python add_line_nums.py foo.txt foo1.txt'

# filestreams often handled using with ... as ... construct
# executes open command and assigns to var
# filestram automatically closes when lab_code block exits

with open(sys.argv[1], 'r') as infile:
    num = 0
    for line in infile:
        num += 1
        print(num, line, end=' ',file=outfile)
# to standard input , output nd error systems are avaliable from the sys module as
# sys.stdin, sys.stdout, and sys.stderr
# must import sys
# stream has similar methods to file objects ; eg. sys.stderr.write(s)
# to consle
print('Hello World!', file=sys.stderr)
# to a file
f = open('lab/foo.txt','w')
print('Hello World!', file=f)
