def DoStuff(x, y, z):
    a = []
    for i in range(len(x)):
        if x[i] > 10:
            temp = x[i] * y
        else:
            temp = x[i] + y
        if temp > 20:
            a.append(temp)
        if z == True:
            print("value is:" + str(temp))
    return a


def process_data():
    l = [1, 2, 3, 4, 5, 11, 12, 13]
    result = DoStuff(l, 5, True)
    for i in range(0, len(result)):
        result[i] = result[i] + 10
    return result


print(process_data())
