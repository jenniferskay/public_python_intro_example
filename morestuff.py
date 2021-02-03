from somefuncs import leap_year_print

print ("in the morestuff file")

def foo():
    print ("Hello in foo")
    print ("all done foo")


print("A")

years = [3000, 3001, 3002, 3003, 3004]

for i in years:
    leap_year_print(i)

print ("B")

foo()

print ("done the morestuff file")


