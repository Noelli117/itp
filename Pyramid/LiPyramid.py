def print_pyramid(variables):
    if variables < 1 or variables > 8:
        print("Pyramid's height shoube be between 1 and 8.")
        return
    for i in range(1, variables + 1):
        spaces = ' ' * (variables - i)
        hashes = '#' * i
        print(spaces + hashes)

stacks=int(input("Enter levels of pyramid(1-8):"))
print_pyramid(stacks)
