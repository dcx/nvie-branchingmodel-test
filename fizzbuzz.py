
def fizzbuzz(num):
    print "Fizzbuzz test starts"
    for i in range(1,num+1):
        if (i%3==0 and i%5==0): print "FizzBuzz"
        elif i % 3 == 0: print "Fizz"
        elif i % 5 == 0: print "Buzz"
        else: print i


def buzzfizz(num):
    print "Buzzfizz test starts"
    for i in range(1,num+1):
        if (i%2==0 and i%7==0): print "BuzzFizz"
        elif i % 2 == 0: print "Buzz"
        elif i % 7 == 0: print "Fizz"
        else: print i

if __name__ == '__main__':
    fizzbuzz(15)
    print ""
    buzzfizz(15)

    
