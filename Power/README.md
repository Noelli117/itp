def print_graph(n):
 def power = get_power(i, 2)
 print("*" * power)
 for i in range(-8, 9):
  print_graph(n)

print_graph(2)

This is the original codes I had, which I could not figure out why it can't be ran.
So I asked GPT, which it pointed out couple of my incorrect indentation: 
1.The for loop should be defined outside the print_graph function, as it's used to call the function.
2.The print("*" * power) statement should be indented inside the for loop to ensure it executes within each iteration.


Therefore I rewrote the codes into this:
def print_graph(n):
 for i in range(-8, 9):
     power = get_power(i, 2)
     print("*" * power)
 

print_graph(2)

And it was still not working, then I realized that I did not define the get_power fuction, so I added it into the codes.Then I got this:

def print_graph(n):
    for i in range(-8, 9):
        power = get_power(i, 2)
        print("*" * power)

def get_power(x, n):
    return x ** n

print_graph(2)

Then it works, horray.