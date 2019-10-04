# defining functions
# Use keyword def


# e.g. function to compute Fibonacci series upto n, returned as a list
# (stops when next value would be >= n)
def fib(n):  # compute Fibonacci
    a, b = 0, 1  # seriesupton
    series = []
    while b < n:
        series.append(b)
        a, b = b, a + b
    return series


# return: can use explicit “return <val>” statement, as above
# a return with no argument returns special value “None”
# a function call that completes without a return also returns “None”

# Function arguments can have default values, or be called by keyword (i.e. by name):
# arguments that have a default value can be omitted in function call 有默认值，可以在调用时缺省该参数
# keyword args can be given out of order 参数可乱序
# non-keyword args are identified by position – must come first in call 非关键字参数由位置标识-必须在调用中排在首位


# Example: simplified “range” function:
def myrange(end, start=0, step=1):
    range = []
    if start <= end and step >= 1:
        while start < end:
            range.append(start)
            start = start + step
    return range


myrange(10, 1, 2)
myrange(10, 0, 2)
# Some okay function calls:
myrange(11)
myrange(11, 3, 2)
myrange(11, step=2)
myrange(start=3, end=11, step=2)
myrange(step=2, start=3, end=11)
# Some bad function calls:
# myrange(start=3, 11)  # non-keyword args come 1st
# myrange(11, step=2, end=11)  # multi values for ’end’ arg
# myrange(start=3, step=2)  # ’end’ arg needed:no default
