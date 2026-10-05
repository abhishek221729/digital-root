def digital_root(number):
    number = abs(number)

    while number >= 10:
        digits = str(number)
        total = 0

        for digit in digits:
            total = total + int(digit)

        number = total

    return number


buckets = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}


start = 1
end = 10

for number in range(start, end + 1):
    root = digital_root(number)
    buckets[root].append(number)

print(buckets)