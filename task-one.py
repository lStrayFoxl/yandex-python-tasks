def maximizing_a(a: str, b: str) -> str:
    arr_a = list(a)
    arr_b = list(b)

    arr_b.sort(reverse=True)

    count = 0
    result = ''
    for element in arr_a:
        if (element < arr_b[count]):
            element = arr_b[count]
            count += 1

        result += element

    return result

a = '00000'
b = '11111'
print(maximizing_a(a, b))