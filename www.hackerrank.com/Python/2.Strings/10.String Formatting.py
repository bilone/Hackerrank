def print_formatted(number):
    # your code goes here
    k=len(format(number,'b'))
    for i in range(number):
        print(str(i+1).rjust(k),format(i+1,'o').rjust(k),format(i+1,'X').rjust(k),format(i+1,'b').rjust(k))

n = int(input())
print_formatted(n)