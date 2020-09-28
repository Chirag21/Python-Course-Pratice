mylist = [3,5]

def check_even_odd(lst):
    for x in lst:
        if(x%2 == 0):
            return True
        else:
            pass
    return False

print(check_even_odd(mylist))

##########################################################################################

mylist1 = [('Billy',400),('Sasha',1500),('Eminem',600)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    
    for emp,hrs in work_hours:
        if(hrs > current_max):
            current_max = hrs
            employee_of_month = emp
        else:
            pass

    return (employee_of_month,current_max)

name,hours = employee_check((mylist1))
print(f'{name} is the employee of the year. He/She worked for {hours} hours')

###################################################################################################
string1 = 'GameOfThrones'

def myfunc(x):
    out = []
    for i in range(len(x)):
        if i % 2 == 0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)   # IMP


print(myfunc(string1))