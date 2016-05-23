from itertools import groupby

f = open('salesdata', 'r')
prev_month, category, sales = f.readline().strip().split('|')
saleslist = [float(sales)]
done = False
while not done:
    line = f.readline()
    if line:
        month, category, sales = line.strip().split('|')
    else:
        done = True
    if not done and month == prev_month:
        saleslist.append(float(sales))
    else:
        total = sum(saleslist)
        average = total / len(saleslist)
        print(prev_month, total, average)
        saleslist = [float(sales)]
        prev_month = month


with open('salesdata', 'r') as f:
    mylist = [(line.strip().split('|')) for line in f]
    #sorted([(line.strip().split('|')) for line in f], key=lambda x: x[1])

print(mylist)
groups = groupby(mylist, key=lambda x: x[1])
for month, group in groups:
    saleslist = [float(x[2]) for x in group]
    total = sum(saleslist)
    average = total / len(saleslist)
    print(month, total, average)




