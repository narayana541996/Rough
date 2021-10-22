'''def calculate_tax(salary):#takes salary as parameter
    s, r, a = 300001, 0.32, 60400
    return (salary - s)*r + a'''

def calculate_tax():#takes in salary as a user input.
    s, r, a = 300001, 0.32, 60400
    try:
        return (int(input('Enter salary: ')) - s)*r + a
    except:
        return 'Error, try using a different input.'

print(calculate_tax())