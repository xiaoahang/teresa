# basic array
x = ['what', 'can', 'I', 'put', 'in', 'my', 'list']
print(x[3])  # accessing value at index 3
print(x[-2])  # negative position counts in from end
print(x[1:3])  # taking a slice
print(x[:3])  # missing value defaults to list start
print(x[3:])  # missing value defaults to list end
x[1:3] = ['I', 'CHANGED', 'IT']  # assign to slice
print(x)
print(x[1:6])
print(x[1:6:2])  # slice with step=2
print(x[6:1:-2])  # slice with negative step=2

print(x[::-1])  # does what? - reverses list!

# list append & add
a = ['what']
b = ['why']
a.append('and')
print(a)
print(a + b)

mark = int(input("please input a INTEGER mark : "))
if mark > 40:
    print("result : pass")
else:
    print('result : fail')

if mark >= 70:
    print('result : first')
elif mark >= 40:
    print('result : pass')
else:
    print('result : fail')

# while loops
# continue: continue with next iteration of loop
# break: exit loop
score = 1
while score > 0:
    score = int(input('please input score : '))
    print('score was ', score)
    continue
# for loop & range function
# when feasible , prefer to use for loop
# generally gives more elegant solution
# also supports break , continue
myString = 'this and that'
for i in myString:
    print(i, end='')
# range(5) creates and returns an iterator from 0,4
# range(5) 0-4
# range(3,7) 3,4,5,6
# range(0,10,2) 0,2,4,6,8
# range(10,0,-2) 10,8,6,4,2
for i in range(5):
    print(i)

# prefer use simple for loop if just need to access elements in turn
scores = [5, 12, 7, 15]
for value in scores:
    if value > 10:
        print(value)

# but to change list elements, must address them buy index
# use range - len  construction
scores = [5, 12, 7, 15]
for i in range(len(scores)):
    scores[i] = scores[i] + 2
    print('new score', scores[i])

# basic printing
# default: print expressions on one line, with a space between, and outputs a final newline
# can override defaults, with keyword arg
print('this', 'that', sep='\n', end='\n\n')

# interpolation
# all python built-in types have printable representations
# can create formatted strings by interpolation 插值
# the formatting , or interpolation, operator: '%'
# left-hand arg : q string containing conversation specs
# right-hand arg: a tuple of values for insertion into format string ( or single non-tuple value if only one required)
# returns result after conversation specs are replaced with values
myPi = 3.141592
form = 'The value of %s (to 3 decimal places) is %.3f'
form % ('PI', myPi)
print(form % ('PI', myPi))
print('%s = %.3f (3 decimal places)' % ('PI', myPi))

print("sad")
