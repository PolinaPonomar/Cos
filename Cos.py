#import math
#L=[math.cos(x*math.pi/180) for x in range(90)]
#print(L)

def foo():
    for i in range(100):
        if i%4 == 0:
            x = i
            if x%2 == 0:
                y = x*2
            else:
                y = x*(-2)
            L = [x,y]
            yield L

f = foo()
print (f.__next__())
print (f.__next__())
print (f.__next__())
print (f.__next__())
print (f.__next__())
print (f.__next__())
print (f.__next__())
print (f.__next__())
print (f.__next__())

