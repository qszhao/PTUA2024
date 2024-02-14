# prints out all odd numbers between 0 and 100
start, end = 0, 100
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end = " ")
