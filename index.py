# def calcSum(a, b):
#     return a + b
# print(calcSum(1, 2))

# sumLambda = lambda a, b: a + b
# print(sumLambda(2, 3))

# def calcSquares(list):
#     newList = []
#     for num in list:
#         newList.append(num * num)
#     return newList
# print(calcSquares([1, 2, 3, 4, 5]))

# calcSquare = lambda list: [num * num for num in list]
# print(calcSquare([1, 2, 3, 4, 5]))

# sum = lambda num1: lambda num2: num1 + num2
# print(sum(2)(3))

# def upper(txt):
#     return txt.upper()
# def lower(txt):
#     return txt.lower()
# print(upper('Hello'))
# print(lower('PHP'))


# HIGHER ORDER FUNCTION. 3 FUNCTIONS
# def upper(txt):
#     return txt.upper()

# def lower(txt):
#     return txt.lower()

# def say_hello(func):
#     greeting= func('Hello. I am Abdulkhakim')
#     print(greeting)
# say_hello(upper)
# say_hello(lower)
# HIGHER ORDER FUNCTION.

# def sayHello(type, txt):
#     if type == 'upper':
#         print(txt.upper())
#     else: print(txt.lower())
# sayHello('lower', 'Abdulkhakim')
# sayHello('upper', 'Abdulkhakim')
# sayHello('sdjzhfgkuy', 'Abdulkhakim')

# #IMPERATIVE STYLE(HOW TO DO IT) 
# string = 'Hello. I am Abdulkhakim'
# urlFriendly = []
# for char in string:
#     if char == ' ':
#         urlFriendly.append('_')
#     else: urlFriendly.append(char)
# urlFriendly = ''.join(urlFriendly)
# print(urlFriendly)

# #DECLARATIVE STYLE(WHAT TO DO) 
# string2 = 'Hello I am Abdulkhakim'
# urlFriendly2 = string2.replace(' ', '_')
# print(urlFriendly2)

# def calcloan(credit, period, interest):
#     yearInterestMoney = (credit * interest) / 100
#     periodInterestMoney = yearInterestMoney * period
#     allMoney = credit + periodInterestMoney
#     monthlyPayment = allMoney / (period * 12)
#     monthlyInSums = monthlyPayment * 10800
#     return (f'You have to pay {int(monthlyInSums)} sums per month.')
# print(calcloan(1000, 3, 26))

print(abs(5 - 6))

