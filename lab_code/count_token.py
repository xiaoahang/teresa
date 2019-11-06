import sys, re
import pylab as p

# read and count
word_re = re.compile(r'[A-Za-z]+')
dic = {}
f = open('mobydick.txt', 'r')
total_word_count = 0
for line in f:
    for l in word_re.findall(line.lower()):
        total_word_count += 1
        if l in dic:
            dic[l] += 1
        else:
            dic[l] = 1

print('dic', dic)
# sort
sort_re = sorted(dic.items(), key=lambda item: item[1], reverse=True)
print('sort_re', sort_re)
print('total_word_count', total_word_count)
# stop-words HIGH FREQUENCY
print(sort_re[0:20])
# plot top 100
x_100 = list(item[0] for item in sort_re[:100])
y_100 = list(item[1] for item in sort_re[:100])
p.plot(x_100, y_100)
p.show()
# plot cumulative count top 100
x_cum_100 = list(item[0] for item in sort_re[:100])
y_cum_100 = list(sum(list(i[1] for i in sort_re[0:index+1])) for index, item in enumerate(sort_re[:100]))
print(y_cum_100)
p.plot(x_cum_100, y_cum_100)
p.show()


# X = [0, 1, 2]
# Y1 = [1.2, 2.2, 1.8]
# Y2 = [1.5, 2.0, 2.6]
# p.subplot(211)  # 2行1列
# p.plot(X, Y1)
# p.subplot(212)
# p.plot(X, Y2)
# p.show()
