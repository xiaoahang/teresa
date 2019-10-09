# sorting
# numbers into ascending / descending order
# strings (such as words) into alphabetic order
# sorted general function — returns a sorted copy of list
# .sort() called from list — sorts the list “in place”
x = [7, 11, 3, 9, 2]
print(sorted(x))  # "sorted" returns sorted variant of x
print(x)  # but x itself unchanged
x.sort()  # ".sort()" modifies list ‘in-place’
print(x)  # so x itself now different

# by default, sorting puts
# numbers in ascending order 升序
# strings into standard alphabetic order (upper before lower case)
# Can change default behaviour, using keyword args:
# can reverse standard sort order as follows:
x = [7, 11, 3, 9, 2]
sorted(x)
sorted(x, reverse=True)
# Same keyword args used for function and method sorting approaches
x.sort(reverse=True)
print(x)

# Keyword key allows you to supply a (single arg) function
# function computes some alternate value from item (of list being sorted)
# items of list then sorted on basis of these alternate values
# for ‘one-off’ functions, can use lambda notation
# e.g. lambda x:(x * x) + 1 :
# means give me one input (x) and I’ll give you back result x * x +1
# e.g. lambda i:i[1] : given item i, computes/returns i[1]
# which makes sense if i is a sequence, so i[1] is its 2nd element

# Example: sorting list of pairs (tuples) by second value
# would otherwise sort by first value
x = [('a', 3), ('c', 1), ('b', 5)]
sorted(x)

sorted(x, key=lambda item: item[1])  # mean that you sort the list by the [1] index in one tuple

# modifying sort behaviour
## 自定义排序
# 1. lambda
## keywords 'key' allows you to supply a function
## function conoutes some alternative value from item(of list being sorted)
## items of list then  sorted on basis of these altenative values
## for 'one-off' funtions, can use lambda funtion

# lambda notation, means f(x) = x*x +1,means input x, output x*x+1
lambda x: (x * x) + 1

# give item s, computes/returns s[1]
lambda x: x[1]
# which only makes sense if either
## s is a sequence : so s[1] is its 2nd element
#  or s is a dictionary: so s[1] looks up values for key 1

x = [('a', 3), ('c', 1), ('b', 5)]
sorted(x)

sorted(x, key=lambda item: item[1])  # mean that you sort the list by the [1] index in one tuple
# 2. use keyword arg cmp:
## lets you supply a custom two arg funtion for comparing list items
## should return negative/0/positive value depending on whether fisrt arg id considered smaller than / same as / bigger than second
## this is easy for sort based on the order of keys
tel = {'alf': 111, 'bob': 222, 'cal': 333}
for k in tel:
    print(k, ':', tel[k])

for k in sorted(tel):
    print(k, ':', tel[k])

# eg
counts = {'a': 3, 'c': 1, 'b': 5}
labels = list(counts.keys())
labels.sort(key=lambda v: counts[v])
sorted(counts.items(), key=lambda i: i[1])
# eg2
densities = {
    'iron': 7.8,
    'gold': 19.3,
    'zinc': 7.13,
    'lead': 11.4
}
metals = list(densities.keys())
metals.sort(reverse=True, key=lambda m: densities[m])
for i in metals:
    print('{0:>8} = {1:5.1f}'.format(i, densities[i]))
