import sys, re

# penRE = re.compile('pen')
# with open(sys.argv[1], 'r') as infs:
#     for line in infs:
#         # if re.search('pen', line):
#         if penRE.search(line):
#             print('line', end=' ')
# when a regex is to be used for many times, is better (ie. faster) to compile a regex object
# assigning object to a well-named variable gives more-readable code
# eg. having regex for 'word' 'URL' etc

# 1. | vertical bar : to specify that one of several options are permitted in a match, to separate them by a vertical bar
reg1 = re.compile('car|bike|train')
reg1.match('carnation')  # True
reg1.match('motorbike')  # True
reg1.match('detraining')  # True

# 2. () parentheses : can group parts of a pattern, using  parentheses
reg2 = re.compile("(e|i)nquir(e|y|ing)")
reg2.match('enquiry')
reg2.match('inquiring')
reg2.match('enquire')

# 3.quantifiers : specify want some number of (sub) pattern occurrence
#   * zero or more
#   + one or more
#   ? zero or one occurrence ( optional )
# apply to immediately preceding item or group in pattern
reg3 = re.compile("ab*d?e")
reg3.match('abde')
reg3.match('bde')  # None
reg3.match('abd')  # None
reg3.match('aeee')
# e.g. does regex "c(ab)*(de)+" match
#   ghcabdemn True
#   ghcabbdemn False
#   ghcababdemn True
reg4 = re.compile("c(ab)*(de)+")
reg4.match('ghcabdemn')
reg4.match('ghcabbdemn')
reg4.match('ghcabababdemn')

# 4. {} braces : There’s an alternative notation for quantifiers, using braces ({,})
# allows count range for repetitions to be specified (e.g. “3–12”) 允许指定重复的计数范围

# 5. [,] square brackets : Use square brackets ([,]) to indicate a character class
reg5 = re.compile('c[ad]r')
reg5.match('car')
reg5.match('cdr')
reg5.match('cadr')
# Can specify char ranges using a hyphen
'[A-Z]'
'[a-f]'
'[A-Za-z]'
'[0-9]'
# some common char classes have predefined names:
# . matches any char
# \d abbreviates [0-9]
# \w abbreviates [A-Za-z0-9]
# \s abbreviates [\f\t\n\r] i.e. whitespace chars

# 6. ^ carat : to negate a char class, put the ^ at  the start
reg6 = re.compile('[^0-9]')
reg6.match('ddd')
reg6.match('666')
reg6.match('abc6')
reg6.match('6abc6')

# 7. some negated char classed are predefined
# \D (not 0-9) \S (not whitespace) \W (not \w)

# 8. anchors tie matching to appearing at certain positions
# # ^ matches the beginning of rhe string
# # $ matches the end of the string
# # \b matches at word boundary (between \W and \w); but see extended ppt slide on raw string before using \b
# # "^author" -- matches strings beginning with 'author'
# # ">>$" -- matches strings end with '>>'

# 9. using brackets(groups) in regex to identify portions for return
# # identified numerically - count '('s in from left, starting with 1
'(([a-z]+)(ed|ing))'
'([a-z]+)'
'(ed|ing)'

# 10. a successful regex match returns a match object
# # stores info of matching substrings and their spans
# # access using match object's methods: group, groups, span
sent = 'I have baked a cake!'
m = re.search('(([a-z])+(ed|ing))', sent)
m.group(1)  # returns substring for group 1
m.span(1)  # return start / end indices for group 1
m.group(3)
m.span(3)

# 11. findall method returns a list of matches for regex
s = 'I like fish, chips and peas!'
word = re.compile('[A-Za-z]+')
# word = re.compile('\w+')
word.findall(s)
# # above regex  has no groups: in this case, list of matching strings  returned
# # in case where regex has groups, instead returns a list od n-tuples of group matches(for groups 1+)
