def show_employee(employeeName,salary=50):
   # we use + so we can see more clear " anything" +
    print("Worker "+employeeName,salary)
# Donna is defolt value salary =50
show_employee("Donna")
show_employee("Bobi"   ,    100)
show_employee("judi"   ,    200)
show_employee("Ben "   ,     300)
# key word arguments Suzi,
show_employee(employeeName="Suzi",salary=400)
# positional arguments,
show_employee(salary=500,employeeName="Joni")
#call function with one positional argument,in my understending Suzi and Bobi took 50 becouse in first row salary=50

show_employee("Suzi")
show_employee("Bobi")
# another positional arguments
show_employee(salary=200,employeeName="judi")

