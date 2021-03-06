
from indepfunc import id_valid
import uxfunc


class employee():
    def __init__(self):
        self.data = {}
        ##self.first_name = employee.string_gen("First Name")
        self.last_name = employee.string_gen("Last Name")
        ##self.birth_year = employee.date_check("year")
        ##self.birth_month = employee.date_check("month")
        ##self.birth_day = employee.date_check("day")
        ##self.position = employee.string_gen("position")
        ##self.uni_status = employee.get_uni_status()
        self.employee_id = None


    def string_gen(type):
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
        em_id = input(f"What is the employee ID of the employee {type}?: ")
        if em_id.isdigit():
            return em_id
        else:
            print()
            print("Not a Valid employee ID")
            return False


    def update():
        update_id = employee.id_valid("data you want to update")
        print(worker.data)
        if update_id == False:
                print()
            
        elif All_employees_dict.get(update_id) is not None:
            while True:

                poss_opt = ("UPDATE MENU", "------------------------", "What key do you want to update?: ","1 - Employee ID", "2 - First Name", "3 - Last Name", "4 - Year of Birth", "5 - Month of Birth", "6 - Day of Birth", "7 - Position", "8 - University Status", "9 - Exit Update menu: ")
                change = uxfunc.scroll_menu(poss_opt)
                if change == "1":
                    while True:
                        new_id = id_valid("add")
                        if new_id in All_employees_dict.keys():
                                print("This ID is taken")
                                continue
                        else:
                            old_object_name = worker.last_name + str(worker.data["Employee ID"])

                            worker.data["Employee ID"] = new_id

                            new_object_name = worker.last_name + str(new_id)

                            employee_objects_list.append(new_object_name)
                            employee_objects_list.remove(old_object_name)

                
                            employee_objects_dict[new_object_name] = worker.data
                            del employee_objects_dict[old_object_name]
                            break
                    print("Returning to Main Menu")
                    break


                        
                elif change == "2":
                    new_first_name = employee.string_gen("first name")
                    worker.data["First Name"] = new_first_name
                    

                elif change == "3":
                    print(worker.data)
                    print("______________________")      
                    old_object_name = worker.data["Last Name"] + str(worker.data["Employee ID"])

                    new_last_name = employee.string_gen("last name")
                    worker.data["Last Name"] = new_last_name

                    
                    new_object_name = new_last_name + str(worker.data["Employee ID"])
                
                    employee_objects_list.remove(old_object_name)
                    employee_objects_list.append(new_object_name)

                
                    employee_objects_dict[new_object_name] = worker.data
                    print("______________________")      
                    del employee_objects_dict[old_object_name]
                    print(employee_objects_dict)
                    print("______________________")
                    print("Returning to Main Menu")
                    break
                        
                    
                elif change == "4":
                    new_year_ob = employee.date_check("year")
                    worker.data["Birth Year"] = new_year_ob
                        
                    
                elif change == "5":
                    new_month_ob = employee.date_check("month")
                    worker.data["Birth Month"] = new_month_ob
                        
                    
                elif change == "6":
                    new_day_ob = employee.data_check("day")
                    worker.data["Birth Day"] = new_day_ob
                        
                    
                elif change == "7":
                    new_position = employee.string_gen("posiiton")
                    worker.data["Position"] = new_position
                        
                    
                elif change == "8":
                    new_uni = employee.get_uni_status()
                    worker.data["Graduated Uni"] = new_uni

                elif change == "9":
                    break

                else:
                    uxfunc.usage()

        else:
                print()
                print("There is no employee with this ID")
                print()


if __name__ == '__main__':
    employee_objects_dict = {}
    employee_objects_list = []
    All_employees_dict = {}
    temp = None

    while True:
        opt = ("------------------------ ", "MAIN MENU","------------------------ ", "Do you want to: ", "1 - Add an Employee", "2 - Remove an Employee", "3 - Get total number of employees", "4 - get a list of Employees" , "5 - Retrieve the data of an employee (By ID)" ,"6 - Update employee's data","7 - Print list of employee objects", "8 - print dictionary of objects", "9 - Exit program")
        option = uxfunc.scroll_menu(opt)
        if option == "1":
            while True:

                
                worker = employee()
               ## worker.data["First Name"] = worker.first_name
                worker.data["Last Name"] = worker.last_name
              ##  worker.data["Birth Year"] = worker.birth_year
               ## worker.data["Birth Month"] = worker.birth_month
               ## worker.data["Birth Day"] = worker.birth_day
               ## worker.data["Position"] = worker.position
               ## worker.data["Graduated Uni"] = worker.uni_status

                
                while True:
                    id_verif = employee.id_valid("you want to add")
                    if id_verif in All_employees_dict:
                        print("This ID is taken")
                        break
                    elif id_verif == False:
                        print()
                        break
                    else:
                        worker.employee_id = id_verif
                        print(worker.employee_id)
                        worker.data["Employee ID"] = worker.employee_id
                        All_employees_dict[id_verif] = worker.data


                        object_name = worker.last_name + str(worker.employee_id)
                        employee_objects_list.append(object_name)
                        employee_objects_dict[object_name] = worker.data




                        print(worker)
                        print("___________")


                        print(worker.data)
                        print("___________")

                        print(All_employees_dict)
                        print("___________")

                        print(object_name)

                        object_name = worker
                        print("___________")

                        print(object_name)

                        print(employee_objects_list)
                        print(employee_objects_dict)



                        
                        
                        break
                    
               
               ## print("___________")            
                ##print(object_name)
               ## print("___________")
               ## print(employee_objects_list)
               ## print("___________")
               ## print(employee_objects_dict)

                break
                


        elif option == "2":
            delete_id = employee.id_valid("you want to delete")
            print()
            if delete_id == False:
                print()
            elif delete_id in All_employees_dict:
                verification = input("Enter [xBCD] to confirm deletion (case sensitive): ")
                if verification == "BBCD":
                    del All_employees_dict[delete_id]
                    print()
                    print("Employee Data deleted")
                else:
                    print()
                    print("Verification failed")
            else:
                print()
                print("NO Employee with that ID")


        elif option == "3":
            employee_counter = 0 
            for employee_dict in All_employees_dict:
                employee_counter += 1 
            print()
            print(f"The total number of employees is {employee_counter}")


        elif option == "4":
            print()
            if All_employees_dict:
                for dict in All_employees_dict:
                    print(All_employees_dict[dict])
            else:
                print("No employee data present")


        elif option == "5":
            show_id = employee.id_valid("data you want to show")
            if show_id == False:
                print()
          
            elif All_employees_dict.get(show_id) is not None:
                print()
                print(All_employees_dict[show_id])
                print()
            else:
                print()
                print("There is no employee with this ID")
                print()


        elif option == "6":
            employee.update()

        elif option == "7":
            print(All_employees_dict)


        elif option == "8":
            print(employee_objects_dict)


        elif option == "9":
            exit()

        
        else:
            uxfunc.usage()