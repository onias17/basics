# CONTROL FLOW

# Comparison Operators
2 > 1
1 < 2
1 >= 1
1 <= 4
1 != 1
1 == 1
1 == '1'        # false
'hi' == 'bye'   # false

# Logical Operators
(1 > 2) and (2 < 3)
(1 > 2) or (2 < 3)
(1 == 2) or (2 == 3) or (4 == 4)

# If / Else
if 1 < 2:
    print('first block')
    if 2 > 3:
        print('yes')

if 1 > 2:
    print('hello')
elif 3 == 3:
    print('elif ran')
else:
    print('last')

# Loops
# for
seq = [1,2,3,4,5,6]

for item in seq:

    print(item)

d = {'onias': 1, 'naq': 2, 'jair': 3}

for k in d:
    print(k)
    print(d[k])

mypairs = [(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item)

for (tup1,tup2) in mypairs: # or for tup1, tup2 in mypairs
    print(tup2)
    print(tup1)

# while
i = 1

while i < 5:
    print('i is: {}'.format(i))
    i = i + 1

# range
range(5) # range(0, 5)
list(range(0,5)) # [0,1,2,3,4]
list(range(0,21,2)) # [0,2,4,6,8,10,12,14,16,18,20]

for item in range(10):
    print(item)

# List Comprehensions
x = [1,2,3,4]
out = []

for num in x:
    out.append(num**2)

print(out)

out2 = [num**2 for num in x]
print(out2)