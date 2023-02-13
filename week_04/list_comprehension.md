List = [i for i in [1, 2, 3]]
print(List)


list = [i for i in range(11) if i % 2 == 0]
print(list)


matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)


# for loop
List = []

for i in 'Hello':
    List.append(i)

print(List)


List = [i for i in 'Hello']
print(List)


matrix = []

for i in range(3):

    matrix.append([])

    for j in range(5):
        matrix[i].append(j)

print(matrix)



matrix = [[j for j in range(5)] for i in range(3)]

print(matrix)


# if else
lis = ["Even" if i % 2 == 0
	else "Odd" for i in range(8)]
print(lis)


lis = [num for num in range(100)
	if num % 5 == 0 if num % 10 == 0]
print(lis)


twoDMatrix = [[10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]]

trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))]

print(trans)
