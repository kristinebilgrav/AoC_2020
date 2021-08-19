import sys

numbers = []
for line in open(sys.argv[1]):
    line=line.strip().split(',')
    for n in line:
       n= int(n)
       numbers.append(n)

end = 2020-len(numbers)
for i in range(4,30000001):
    #print("n",numbers.count(numbers[-1]), numbers[-1])
    if numbers.count(numbers[-1]) > 1:
        where = []
        for t in range(len(numbers)):
            if numbers[t] == numbers[-1]:
                where.append(t)
        lpos = where[-2] + 1
        hpos= where[-1] +1
        n = hpos - lpos
        #print(i, where, n)
        numbers.append(n)
    else:
        #numbers.count(numbers[-1]) == 1:
        numbers.append(0)

print(numbers[29999999])
