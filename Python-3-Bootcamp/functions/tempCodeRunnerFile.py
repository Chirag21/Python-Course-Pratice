
mylist1 = [('Billy',400),('Sasha',500),('Eminem',600)]

def employee_check(work_hours):
    current_max=0
    employee_of_month=''
    
    for emp,hrs in work_hours:
        if(hrs>current_max):
            current_max=hrs
            employee_of_month=emp

    return (employee_of_month,current_max)

employee_check(mylist1)