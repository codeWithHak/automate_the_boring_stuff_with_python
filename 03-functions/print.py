# print("Hello ")
# print("World")
# print("Hello", end=' ')
# print("World")
# print("hi",'bye','tata', sep=', ')


# def divideBy (num):
#     try:
#         return int(42 / num)
#     except :
#         print('Error: Invalid Arguement')

# print(divideBy(11))
# print(divideBy(2))
# print(divideBy(0))


def spam (divideBy):
    return 42/divideBy

try:
    (print(spam(11)))
    (print(spam(10)))
    (print(spam(0)))
    (print(spam(9)))

except ZeroDivisionError:
    print("Error: Invalid Input")

