def print_graph(n):
    for i in range(-8, 9):
        power = get_power(i, 2)
        print("*" * power)

def get_power(x, n):
    return x ** n

print_graph(2)
