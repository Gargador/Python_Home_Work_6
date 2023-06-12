# Задача 30:
a1 = int(input())
d = int(input())
n = int(input())

progression = []
for i in range(n):
    current = a1 + i * d
    progression.append(current)

print(progression)


# Задача 32:
def find_indexes(lst, min_range, max_range):
    indices = []
    for i in range(len(lst)):
        if min_range <= lst[i] <= max_range:
            indices.append(i)
    return indices

lst = [2, 7, 3, 8, 4, 9, 6, 12]
min_range = 3
max_range = 8
print(find_indexes(lst, min_range, max_range))
