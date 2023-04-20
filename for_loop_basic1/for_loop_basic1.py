# Print  Print all integers from 0 to 150.
for i in range(151):
    print(i)

# Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1005, 5):
    print(i)

# Print integers 1 to 100. Divisible by 5, print "Coding". Divisible by 10, print "Coding Dojo".
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Add odd integers from 0 to 500,000, and print the final sum.
x = 0
for i in range(0, 500002):
    if i % 2 == 0:
        x = x + i
print(x)

# Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    print(i)

# Print only the integers that are a multiple of mult.
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)