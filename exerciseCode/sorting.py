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

