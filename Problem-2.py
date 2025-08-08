def get_odd_numbers(n):
    result = []
    num = 1
    for i in range(n):
        result.append(num)
        num +=2
    return result

a = int(input("Enter a number: "))
output = get_odd_numbers(a)
for val in output:
    print(val, end=", ")