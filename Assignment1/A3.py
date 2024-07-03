def polynomial(coefficients, x):
    v = 0
    x_i = 1
    for i in range(len(coefficients) - 1, -1, -1):
        v += x_i * coefficients[i]
        x_i *= x
    return v

degree = int(input("Enter the degree of the polynomial: "))
coefficients = []

print("Starting from the leading coefficient, list all the coefficients of the polynomial equation:")
for _ in range(degree + 1):
    coefficients.append(int(input("Enter: ")))

lb = int(input("Enter the lower bound: "))
ub = int(input("Enter the upper bound: "))
steps = int(input("Steps in which you want to increment: "))

for i in range(lb, ub + 1, steps):
    temp = polynomial(coefficients, i)
    v = int(temp)
    for j in range(1, v + 1):
        print("*", end=" ")
    print()