# LISTS
x = [1,2,3]
p = ['onias', 144, False, [1,2,3]]
print(p)
print(len(p))
o = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(o[-4])
print(o[2])
print(o[2:])
print(o[2:])
l[0] = 'onias'
print(l)
l.append('israel')
print(l)
l.append(['x', 'y', 'z'])
print(l)
l.extend(['x', 'y', 'z'])
print(l)
z = l.pop()
print(l)
print(z)
print(l.pop(4))
n = [8,12,-3]
b = ['x','y','z']
n.reverse()
b.reverse()
print(n)
l.reverse()
print(l)
n.sort()
print(n)

list = [1,2,['x','y','z']]
print(list[2])
print(list[2][1])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][2])
print(matrix[1][1])
print(matrix[2][0])

# list comprehension
col = [row[0] for row in matrix]
print(col)