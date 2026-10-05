def countdown(numbers):
    if numbers>6:
        return
    print(numbers)
    countdown(numbers+1)
countdown(1)
#......___-----------
def reverse_countdown(numbers):
    if numbers<1:
        return
    print(numbers)
    reverse_countdown(numbers-1)
reverse_countdown(10)
#   .............
def rev_countdown(n):
    if n == 0:
        return
    print(n)
    rev_countdown(n-1)
rev_countdown(10)