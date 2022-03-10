def string_input(type):
    while True:
        nam = input(f"Please enter the {type} of the employee: ")
        if len(nam.strip()) > 1 and nam.isalpha():
            return nam
        else:
            print("Name must be a minimum of 2 letters")


def date_check(type):
    if type == "day":
        while True:
            day = input(f"What is the employee's day of birth: ")
            try:
                x = int(day)
                if 1 <= x <= 31:
                    return x
                else:
                    print("Must be an integer between 1 and 31")
            except ValueError:
                print("Must be an integer between 1 and 31")
    if type == "month":
        while True:
            month = input(f"What is the employee's month of birth: ")
            try:
                x = int(month)
                if 1 <= x <= 12:
                    return x
                else:
                    print("Must be an integer between 1 and 12")
            except ValueError:
                print("Must be an integer between 1 and 12")
    if type == "year":           
        while True:
            year = input(f"What is the employee's year of birth: ")
            try:
                x = int(year)
                if 1900 <= x <= 2004:
                    return x
                else:
                    print("Must be an integer between 1900 and 2004")
            except ValueError:
                print("Must be an integer between 1900 and 2004")







def get_uni_status():
    while True:
        uni = input("Has the employee graduated from university?: ")
        if uni.isalpha():
            if uni.upper() == "YES":
                return True
            elif uni.upper() == "NO":
                return False
            else:
                print("Need to input [yes] or [no]")
        else:
            print("Need to input [yes] or [no]")


def id_valid(type):
    em_id = input(f"What is the employee ID of the employee data you want to {type}?: ")
    if em_id.isdigit():
        return em_id
    else:
        print("Not a Valid employee ID")


