# Python dictionary data type:
# 1. corresponds to PERL hashes, a.k.a. associative arrays # 对应于PERL哈希，又名关联数组
# 2. consist of unordered sets of key:value pairs 无序键值对
# 3. keys must be unique (within given dictionary) 键名不能重复

# Example — telephone directory: here prepopulate with some name:number pairs:
tel = {'alf': 111, 'bob': 222, 'cal': 333}
print(tel)
print(tel['bob'])
tel['bob'] = 555
print(tel)
tel['deb'] = 444  # new key - create new entry
print(tel)
del tel['bob']
tel.keys()  # get list of keys
# tel.has_key('cal')  # check keys exists # the has_key has been deleted????
print('cal' in tel)  # also check for key - nicer

for k in tel:  # iterate over keys
    print(k, tel[k])

# May use dictionaries to store numeric values associated with keys
# e.g. the counts of different words in a text corpus
# e.g. density of different metals e.g. share price of companies
# May want to handle dictionary in a manner ordered w.r.t. the values
# e.g. identify the most common words in text corpus
# e.g. sort companies by share price, so can identify “top ten” companies
# Can use lambda function returning key’s value in dictionary, e.g.
counts = {'a': 3, 'c': 1, 'b': 5}
sorted(counts)
sorted(counts, key=lambda v: counts[v])
sorted(counts, key=lambda v: counts[v], reverse=True)
sorted(counts.items(), key=lambda item: item[1])  # 排序后转换为元组

# EXAMPLE: print metals in descending order of density
densities = {'iron': 7.8, 'gold': 19.3, 'zinc': 7.13, 'lead': 11.4}
for m in sorted(densities, key=lambda v: densities[v]):
    print('%8s = %8.3f' % (m, densities[m]))

# A further keyword arg cmp:
# lets you supply a custom two arg function for comparing list items
# should return negative/0/positive value depending on
# whether first arg is considered smaller than/same as/bigger than second


# list , tuples and strings
## group together multiple elements
## these are sequence types # 有序
## but dictionary is NOT an ordered type 字典是无序的
## 字典的key是唯一的
## key value maps
## dictionary is a kind of mapping type


