numbers = [1, -2, 73, 42, 5, 6]

def naoborot(number, n=0):
    if len(number) <= 1:
        return number
    number[n], number[-n - 1] = number[-n - 1], number[n]
    if n + 1 != int(len(number) / 2):
        return naoborot(number, n + 1)
    return number

print(naoborot(numbers))
