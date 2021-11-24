n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

tongsochan = 0
max = 0
min = 0

for v in array:
    if v % 2 == 0:
        tongsochan += v
    elif v > max:
        max = v
    elif v < min:
        min = v
print(array)
print("số lớn nhất trong mảng là ",max)
print("số nhỏ nhất trong mảng là ",min)
print("tổng số chẵn trong mảng là ",tongsochan)