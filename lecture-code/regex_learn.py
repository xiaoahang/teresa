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
# {3,12} at least 3 and at most 12 occurrence
# {3,} at least 3
# {,12} between zero and12 occurrences
# {3}  exactly 3 occurrences
reg44 = re.compile('a{5}b{1,4}c{2,}')
reg44.match('aaaaabcc')  # Y
reg44.match('aaaaabc')  # N
reg44.match('aaaaabccccc')  # Y
reg44.match('aaaabccccc')  # N
reg44.match('aaaabbbbbbccccc')  # N

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
'[A-z]'  # valid but != [A-Za-z]
'[a-Z]'  # not valid
# some common char classes have predefined names:
# . matches any char
# \d abbreviates [0-9]
# \w abbreviates [A-Za-z0-9]
# \s abbreviates [\f\t\n\r] i.e. whitespace chars

reg5_1 = re.compile('[a-d][m-z][0-9]*')
# matches any string containing any letter between a and d
# followed by any letter between m and z
# followed by zero or more digits in the range 0 to 9
reg5_1.match('bm3405')
reg5_1.match('dx19')
reg5_1.match('thiscontainsav3440soqualifies')
# 6. ^ carat : to negate a char class, put the ^ at  the start
reg6 = re.compile('[^0-9]')
reg6.match('ddd')
reg6.match('666')
reg6.match('abc6')
reg6.match('6abc6')
'[^abc]'  # matches every thing but abc
'[^\d\s]'  # does not matches digit or whitespace

# 7. some negated char classed are predefined
# \D (not 0-9) \S (not whitespace) \W (not \w)

# 8. anchors tie matching to appearing at certain positions
# # ^ matches the beginning of rhe string
# # $ matches the end of the string
# # \b matches at word boundary (between \W and \w); but see extended ppt slide on raw string before using \b
# # "^author" -- matches strings beginning with 'author'
# # ">>$" -- matches strings end with '>>'
'^author'  # match strings starting with author
'[^0-9]'  # negation
'^[0-9]'  # start anchor (string must begin with digit)
'\bfu(n|nny)'  # matches fun, funny, not refund
# some special chars, such ad \b, present a problem in python
# # normally, in strings, \b means 'backspace'
# # to get python to handle \b correctly in regex, must mark  it as a raw string
# # a raw string is preceded by r
funRE = re.compile(r'\bfu(n|nny)')
# can use \ to 'escape' a metacharacter back to its original meaning
# eg might actually want to look for occurrence of ^ in text, in that case, use
'\^'

# 9. using brackets(groups) in regex to identify portions for return
# # identified numerically - count '('s in from left, starting with 1
'(([a-z]+)(ed|ing))'
'([a-z]+)'
'(ed|ing)'

# 10. a successful regex match returns a match object
# # stores info of matching substrings and their spans
# # access using match object's methods: group, groups, span
sent = 'I have baked a cake!'
m = re.search('(([a-z]+)(ed|ing))', sent)
m.group(1)  # returns substring for group 1
m.span(1)  # return start / end indices for group 1
m.group(2)
m.group(3)
m.span(3)
m.groups()
m.group(4)
# group 1 : (([a-z])+(ed|ing))
# group 2 : ([a-z])+
# group 3 : (ed|ing)

# 11. findall method returns a list of matches for regex
s = 'I like fish, chips and peas!'
word = re.compile('[A-Za-z]+')
# word = re.compile('\w+')
word.findall(s)
# # above regex  has no groups: in this case, list of matching strings  returned
# # in case where regex has groups,
# instead returns a list of n-tuples of group matches(for groups 1+)
str = 'al bill 22 chad 333 dave eric 55'
mm = re.findall('[a-z]+ \d', str)
mmm = re.findall('([a-z]+) (\d)', str)

# 12. Method finditer returns an iterator for a sequence of match objects, one for each match
str1 = 'al bill 22 chad 333 dave eric 55'
mm1 = re.finditer('([a-z]+) (\d+)', str)
# print(mm1)
for m in mm1:
    # print(m.group(1), end=' ')
    print(m.groups(), end=' ')
print()  # bill chad eric

# 13. matching of regex is greedy, for python and perl
# # always takes longest matching string
# # for each quantified sub-pattern, tries to match to longest substring
# # this is not always the behaviour you need
str2 = '<p><b>hello</b></p>'
tag = re.compile('<.*>')
m2 = tag.search(str2)
m2.group()
# doesn't work due to greedy matching behaviour
#
# force non-greedy matching of a quantifier by adding a '?'
# quantifiers *? +? ?? {m,n}? match to shortest string possible for overall match
tag2 = re.compile('<.*?>')
m3 = tag2.search(str2)
m3.group()
tag2.findall(str2)
# or
tag3 = re.compile('<[^>]*>')
m4 = tag3.search(str2)
m4.group()
tag3.findall(str2)
# todo please do reflection of the other solution

# 14. can provide flags that modify how a regex is compiled,
# and thereby its behaviour in matching

# flag(shortname)   meaning
# IGNORECASE        do case-insensitive matching (treats [A-Z] same as [a-z]
# MULTILINE         multiline matching - allows ^, $ to match start / end of lines in multiple string
# DOTALL            allow '.' metachar to match newlines in multiline strings
str = 'This and that. \nAnd the other.'
m = re.search('[a-z]+', str, re.IGNORECASE)
word = re.compile('[a-z]+'.re.I)
firstword = re.compile('^[a-z]+', re.I | re.M)
firstword.findall(str)

# 15. a key operation is is substring replacement or substitution
# # for substitution in python, can use regex object method sub()
# # has agrs for replacement string,  and string being matched against
# # optional keyword arg count = n sets upper limit on count of replacements made
# # # - if absent (or count = 0) all occurrences replaced
# # return strings that results after replacements done

names = re.compile('(Alan|Bill|Chad)')
str = 'Vote for Alan. Bill is clever.'
names.sub('Mark', str)
names.sub('Mark', str, count=1)

# # alternative method subn(), returns (as an n-tuple)  both modified  string and a count of the replacements done
# # corresponding class level function  additionally takes regex as its first arg
# # often want to use substrings from a match in constructing the replacement string -- for this use backreference
# # a backreference has form "\N" for some N >=1
# # refers to the text matched to the Nth group of the regex
# # must use a raw string when backrefs are present

swap = re.compile('(Anne|Abi) (likes|hates) (Bill|Bob)')
str = 'I heard that Anne likes Bill, today.'
swap.sub(r'\3 \2 \1', str)
# backrefs can also be used within a regex
# # indicates that some matched string must appear again
r'\b(\w) \1\b'
# mathces if same word appears twice, as in 'kick the the ball'

# pythons strings are objects with own methods. To join a list of strings, call join() method from instance of delimiter string:
tokens = ['this', 'and', 'that']
'::'.join(tokens)

# some of python string methods are v.useful for text processing
# where they are sufficient for your needs, have advantages
# are simpler to use than regex
# are faster / more efficient than regex
# methods names provides a clear 'semantics' when code is read

