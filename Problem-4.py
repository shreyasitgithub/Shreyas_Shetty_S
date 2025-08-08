def count_multiples(numbers):
    result = {}

    for i in range(1, 10):
        count = 0
        for num in numbers:
            if num % i == 0:
                count += 1

        result[i] = count

    return result

input = [1,2,8,9,12,17,22,10,15,20,30]

output = count_multiples(input)

print(output)