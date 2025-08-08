def odd_series(n):
    result = []
    num = 1

    if n % 2 == 0:
        count = n - 1
    else: 
        count = n

    for i in range(count):
        result.append(num)
        num += 2

    return result

a = int(input("Enter a number: "))
output = odd_series(a)
for i in output:
    print(i, end= " , ")