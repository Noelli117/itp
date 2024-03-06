Had some issues when setting up the loop function for printing hashes, so I asked GPT then I got this line of codes:

for i in range(1, variables + 1):
        spaces = ' ' * (variables - i)
        hashes = '#' * i
        print(spaces + hashes)
