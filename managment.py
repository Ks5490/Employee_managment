import indepfunc
import uxfunc


def ID_input():
    while True:
            number_str = input(f"What is the employee ID: ")
            try:
                x = int(number_str)
                if x <=0:
                    print("Must be positive integer greater than 0: ")
                    continue
                if str(x) in employees_dict_of_dict:
                    print("ID is taken")
                    continue
                return x
            except ValueError:
                print("You must enter a number")


def update():
        em_id = input("What is the employee ID of the employee data you want to update?: ")
        print()
        if em_id.isdigit():
            em_id_str = str(em_id)
            if employees_dict_of_dict.get(em_id) is not None:
                while True:

                    poss_opt = ("UPDATE MENU", "------------------------", "What key do you want to update?: ","1 - Employee ID", "2 - First Name", "3 - Last Name", "4 - Year of Birth", "5 - Month of Birth", "6 - Day of Birth", "7 - Position", "8 - University Status", "9 - Exit Update menu: ")
                    change = uxfunc.scroll_menu(poss_opt)
                    
                    if change == "1":
                        temp = employees_dict_of_dict[em_id_str]
                        updated_id = ID_input()
                        updated_id_str = str(updated_id)
                        employees_dict_of_dict[updated_id_str] = temp
                        employees_dict_of_dict[updated_id_str]["Employee ID"] = updated_id_str
                        del employees_dict_of_dict[em_id_str]
                        print()
                        print("Returning to Main Menu")
                        break
                    elif change == "2":
                        new_first_name = indepfunc.string_input("first name")
                        employees_dict_of_dict[em_id_str]["First Name"] = new_first_name
                    elif change == "3":
                        new_last_name = indepfunc.string_input("last name")
                        employees_dict_of_dict[em_id_str]["Last Name"] = new_last_name
                    elif change == "4":
                        new_year = indepfunc.Birth_yr()
                        employees_dict_of_dict[em_id_str]["Year of Birth"] = new_year
                    elif change == "5":
                        new_month = indepfunc.Birth_month()
                        employees_dict_of_dict[em_id_str]["Month of Birth"] = new_month
                    elif change == "6":
                        new_day = indepfunc.Birth_day()
                        employees_dict_of_dict[em_id_str]["Day of Birth"] = new_day
                    elif change == "7":
                        new_position = indepfunc.string_input("position")
                        employees_dict_of_dict[em_id_str]["Position"] = new_position
                    elif change == "8":
                        new_uni = indepfunc.get_uni_status()
                        employees_dict_of_dict[em_id_str]["University Graduate"] = new_uni
                    elif change == "9":
                        break
                    else:
                        uxfunc.usage()
            else:
                print("There is no employee with this ID")
        else:
            print("Not a Valid employee ID")


if __name__ == '__main__':
    employees_dict_of_dict = {}
    employee_count = 0 

    while True:

        ## Drop-down choices ##
        opt = ("MAIN MENU","------------------------ ", "Do you want to: ", "1 - Add an Employee", "2 - Remove an Employee", "3 - Get total number of employees", "4 - get a list of Employees" , "5 - Retrieve the data of an employee (By ID)" ,"6 - Update employee's data","7 - Exit program",)
        option = uxfunc.scroll_menu(opt)


        ## Option 1 creates new data entry ##
        if option == "1":
            employees_dict = {}
            while True:
                new_id = ID_input()
                id_str = str(new_id)
                if not employees_dict:
                    employees_dict["Employee ID"] = id_str
                    break
                else:
                    if new_id in employees_dict["Employee ID"]:
                        print("This ID is taken")
                    else:
                        employees_dict["Employee ID"] = id_str
                        break
        
            first_name = indepfunc.string_input("first name")
            employees_dict["First Name"] = first_name

            last_name = indepfunc.string_input("last name")
            employees_dict["Last Name"] = last_name
            
            year_OB = indepfunc.Birth_yr()
            employees_dict["Year of Birth"] = year_OB

            month_OB = indepfunc.Birth_month()
            employees_dict["Month of Birth"] = month_OB

            day_OB = indepfunc.Birth_day()
            employees_dict["Day of Birth"] = day_OB

            position = indepfunc.string_input("position")
            employees_dict["Position"] = position

            university = indepfunc.get_uni_status()
            employees_dict["University Graduate"] = university

            employees_dict_of_dict[id_str] = employees_dict

            employee_count += 1 
            print()

        ## Option 2 removes data entry from given Employee ID ##
        elif option == "2":
            print()
            ident_no1 = indepfunc.id_valid("remove")
            if employees_dict_of_dict.get(ident_no1) is not None:
                verification = input("Input [XBXC] to confirm data deletion: ")
                if verification == "XBXC":
                    del employees_dict_of_dict[ident_no1]
                else:
                    print("Faild confirmation")
            else:
                print("There is no employee with this ID")

            employee_count -= 1

        ## Option 3 prints employee count ##
        elif option == "3":
            print()
            print(f"Total number of employees is {employee_count}")
            print()
        
        ## Option 4 prints a list of dicts containing employee data ##
        elif option == "4":
            print()
            if employees_dict_of_dict:
                for dict in employees_dict_of_dict:
                    print(employees_dict_of_dict[dict])
            else:
                print("No Employee Data present")
            print()

        ## Option 5 prints dict of data from given Employee ID ## 
        elif option == "5":
            print()
            show_id = indepfunc.id_valid("show")
            if employees_dict_of_dict.get(show_id) is not None:
                print()
                print(employees_dict_of_dict[show_id])
                print()
            else:
                print()
                print("There is no employee with this ID")
                print()

        ## Option 6 goes into Upddate menu ##    
        elif option == "6":
            print()
            update()
            print()
            
        ## Exit Program ##
        elif option == "7":
            exit()

        else:
            uxfunc.usage()

        

    
