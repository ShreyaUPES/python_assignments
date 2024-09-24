#Print statement in python
print("Hello, World!")

#using input function in python
x = int(input('Enter value of x: '))

#using if-else conditions to check if value is greater or lesser than 5
if x > 5:
    print("x is greater than 5.")
else:
    print("x is lesser than 5.")

#seeing how the break statement works, along with while statement
count = int(input("Enter the value of count: "))
while count < 10:
    if count == 5:
        break
    print(count)
    count += 1

#seeing how continue statement works
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)

#using a for loop to see its implementation
for i in range(5):
    print(i, ' ')

#implementing 'in' keyword in for loop in python
for i in range(0, 10):
    print(i, ' ')

