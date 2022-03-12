import uxfunc


class employee():
    def __init__(self):
        self.first_name = employee.string_gen("First Name")
        self.last_name = employee.string_gen("Last Name")
        ##self.birth_year = employee.date_check("year")
        ##self.birth_month = employee.date_check("month")
        ##self.birth_day = employee.date_check("day")
        ##self.position = employee.string_gen("position")
        ##self.uni_status = employee.get_uni_status()
        self.employee_id = None
        self.object_instance = None

    def ID_input():
        while True:
                number_str = input(f"What is the employee ID: ")
                try:
                    x = int(number_str)
                    if x <=0:
                        print("Must be positive integer greater than 0: ")
                        continue
                    if str(x) in dict_pointers_id.keys():
                        print("ID is taken")
                        continue
                    return x
                except ValueError:
                    print("You must enter a number")


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
            return "a"


    def update(pointer):

        while True:

            poss_opt = ("UPDATE MENU", "------------------------", "What key do you want to update?: ","1 - Employee ID", "2 - First Name", "3 - Last Name", "4 - Year of Birth", "5 - Month of Birth", "6 - Day of Birth", "7 - Position", "8 - University Status", "9 - Exit Update menu: ")
            change = uxfunc.scroll_menu(poss_opt)
            if change == "1":
                print("coming")
                '''
                while True:
                    new_id = employee.ID_input()
                    if new_id in employees_dict_of_dict.keys():
                            print("This ID is taken")
                            continue
                    else:
                        old_object_name = worker.last_name + str(employee_dict["Employee ID"])

                        employee_dict["Employee ID"] = new_id

                        new_object_name = worker.last_name + str(new_id)

                    ##   employee_objects_list.append(new_object_name)
                    ##   employee_objects_list.remove(old_object_name)

            
                    ##   employee_objects_dict[new_object_name] = employee_dict
                    ###   del employee_objects_dict[old_object_name]
                        break
                print("Returning to Main Menu")
                break

                '''
                    
            elif change == "2":
                new_first_name = employee.string_gen("first name")
                pointer.first_name = new_first_name
                

            elif change == "3":
                object_new_name = []
                new_last_name = employee.string_gen("last name")
                pointer.last_name = new_last_name
                pointer.object_instance = pointer.last_name + str(pointer.employee_id)
                object_new_name.append(pointer.object_instance)
                

                    
                
            elif change == "4":
                new_year_ob = employee.date_check("year")
                pointer.birth_year = new_year_ob
                    
                
            elif change == "5":
                new_month_ob = employee.date_check("month")
                pointer.birth_month = new_month_ob
                    
                
            elif change == "6":
                new_day_ob = employee.date_check("day")
                pointer.birth_day = new_day_ob
                    
                
            elif change == "7":
                new_position = employee.string_gen("posiiton")
                pointer.position = new_position
                    
                
            elif change == "8":
                new_uni = employee.get_uni_status()
                pointer.uni_status = new_uni

            elif change == "9":
                break

            else:
                uxfunc.usage()

      


    def check(pointer):
        print(pointer.__dict__)                  


if __name__ == '__main__':
    dict_pointers_id = {}

    while True:

        ## Drop-down choices ##
        opt = ("MAIN MENU","------------------------ ", "Do you want to: ", "1 - Add an Employee", "2 - Remove an Employee", "3 - Get total number of employees", "4 - get a list of Employees" , "5 - Retrieve the data of an employee (By ID)" ,"6 - Update employee's data","7 - Exit program",)
        option = uxfunc.scroll_menu(opt)


        ## Option 1 creates new data entry ## ##WORKING WITH POINTER PASS TO FUNC ##
        if option == "1":
            employee_dict = {}
            object_name = []
            worker = employee()
            
            while True:
                new_id = employee.ID_input()
                id_str = str(new_id)
                if not employee_dict:
                    employee_dict["Employee ID"] = id_str
                    worker.employee_id = id_str
                    worker.object_instance = worker.last_name + str(worker.employee_id)
                    object_name.append(worker.object_instance)
                    break
                else:
                    if id_str in employee_dict["Employee ID"]:
                        print("This ID is taken")
                    else:
                        employee_dict["Employee ID"] = id_str
                        worker.employee_id = id_str
                        worker.object_instance = worker.last_name + str(worker.employee_id)
                        object_name.append(worker.object_instance)
                        break

                employee_dict["First Name"] = worker.first_name
                employee_dict["Last Name"] = worker.last_name
                ##employee_dict["Birth Year"] = worker.birth_year
                ##employee_dict["Birth Month"] = worker.birth_month
                ##employee_dict["Birth Day"] = worker.birth_day
                ##employee_dict["Position"] = worker.position
                ##employee_dict["Graduated Uni"] = worker.uni_status
                employee_dict["Employee ID"] = worker.employee_id
                employee_dict["Class Instance Name"] = worker.object_instance


            
            for name in range(len(object_name)):
                object_name[name] = worker
                dict_pointers_id[worker.employee_id] = object_name[name]

            print()

            
           

        ### WORKING WITH POINTER PASS TO FUNC###
        elif option == "2":
            delete_id_int = employee.id_valid("you want to delete")
            delete_id = str(delete_id_int)
          
            if delete_id == "a":
                print()
            elif delete_id in dict_pointers_id.keys():
                verification = input("Enter [xBCD] to confirm deletion (case sensitive): ")
                if verification == "xBCD":
                    del dict_pointers_id[delete_id]
                    print()
                    print("Employee Data deleted")
                    print()
                else:
                    print()
                    print("Verification failed")
                    print()
            else:
                print()
                print("NO Employee with that ID")
                print()

        ### WORKING ###
        elif option == "3":
            employee_counter = 0 
            for dict in dict_pointers_id:
                employee_counter += 1 
            print()
            print(f"The total number of employees is {employee_counter}")



        ###WORKING - WITH PASSED POINTER PRINT DONE IN CLASS FUNC ###
        elif option == "4":
            print()
            if dict_pointers_id:
                for dict in dict_pointers_id:
                    employee.check(dict_pointers_id[dict])
            else:
                print("No employee data present")
                print()


        ###WORKING - WITH PASSED POINTER PRINT DONE IN CLASS FUNC ###
        elif option == "5":
            show_id_int = employee.id_valid("data you want to show")
            show_id = str(show_id_int)
            if show_id == "a":
                print()
            elif show_id in dict_pointers_id.keys():
                print()
                employee.check(dict_pointers_id[show_id])
                print()
            else:
                print()
                print("There is no employee with this ID")
                print()


        elif option == "6":
            update_id_int = employee.id_valid("data you want to update")
            update_id = str(update_id_int)
            if update_id == "a":
                print()
            elif update_id in dict_pointers_id.keys():
                print()
                employee.update(dict_pointers_id[update_id])
            else:
                print()
                print("There is no employee with this ID")
                print()
            


        elif option == "7":
            exit()

        else:
            uxfunc.usage()