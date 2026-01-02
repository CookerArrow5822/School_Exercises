#q1

def sum_q1(n):
    if n == 0:
        return 0
    return n + sum_q1(n - 1)

print(sum_q1(6))

#q2
def sum_q2(n):
    n = str(n)
    if len(n) <= 1:
        return n
    return n[-1] + sum_q2(n[:-1])

print(sum_q2(123))

#q3
def sum_q3(n):
    n = str(n)
    if len(n) <= 1:
        return n
    return n[-1] + sum_q2(n[:-1])

print(sum_q3("hello"))

#q4

def sum_q4(n):
    if len(n) <= 1:
        return n
    return [n[-1]] + sum_q4(n[:-1])

n = [1,2,3,4]
print(sum_q4(n))

#q5
def multiply(a, b):
    if b == 0:
        return 0
    if b < 0:
        return -multiply(a, -b)

    return a + multiply(a, b - 1)

print(multiply(10, 2))
print(multiply(-51, -4))
print(multiply(3, 9))

#q6
def is_heteromecic(num):
    n = 0
    while n * (n + 1) <= num:
        if n * (n + 1) == num:
            return True
        n += 1
    return False

print(is_heteromecic(10))
print(is_heteromecic(110))

#q7
def length(n):
    if n == "":
        return 0
    return 1 + length(n[1:])

print(length(""))
print(length("this is 9"))