def leap_year(y):
    if y <= 1752:
        return False
    elif y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False
    
    
def leap_year_print(year):
    result = leap_year(year)  
    print ("%d is" %year, end = " ")
    if (not(result)):
        print ("NOT", end = " ")
    print ("a leap year")
    
    
print ("in the somefuncs file")

    
if __name__ == "__main__":
    print ("Enter a year", end = ": ")
    year = input()
    year = int(year)
    leap_year_print(year)
    
    

print ("end of somefuncs file")