def GUGU(n):
    result = []
    i: int = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result


print(GUGU(2))
