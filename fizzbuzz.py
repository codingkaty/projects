#fizzbuzz project 

i = 1

while i < 100:
    if i%3==0 and i%5==0:
        print("this is fizzbuzz {}".format(i))
    elif i%3 == 0:
        print("this is fizz {}".format(i))
    elif i%5 == 0:
        print(i)
        print("this is buzz {}".format(i))
    else:
        print(i)
    i += 1
