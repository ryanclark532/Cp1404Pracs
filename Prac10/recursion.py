"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0

    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
"""output will be 3 because the first run 5% 2= 1. next run through 4 %2= 0
next run 3 %2=1. next run 2%2=0. next run 1%2=1 adding up to 3 before n=0 and the function terminates"""
# TODO: 2. use the debugger to step through and see what's actually happening
#print(do_it(5))

def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return 0
    print(n**2)
    do_something(n - 1)

# TODO: 3. write down what you think the output of do_something(4) will be,
" function will cause some sort of error, since there is no exit stratergy"
# TODO: 4. use the debugger to step through and see what's actually happening


# TODO: 5. fix do_something() so that it works according to the docstring
#do_something(4)

def blocks_loop():
    rows=int(input("Rows? "))
    blocks=0
    while rows>0:
        blocks+=rows
        rows-=1
    print(blocks)

def block_recursive(rows):
    if rows <0:
        return 0
    return rows+block_recursive(rows-1)

rows=int(input("rows?"))
print("you need", block_recursive(rows), "blocks for", rows, "rows")
#blocks_loop()