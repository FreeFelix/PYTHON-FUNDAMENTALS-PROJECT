# In the script, write the student's name and code, the class code, and the lecturer's name.S

# Student Name: GASASIRA JEAN FELIX
# Student Code: s3
# Class Code: Level 3
# Lecture Name: Harerimana Dominique
# Unit Name: UNIT RW-University-II 

with open('/var/log/auth.log', 'r') as file:
    data = file.readlines()

print("\t\t\t\t\tLog Parse auth.log from the command usage.")
print("\t\t\t\t\t__________________________________________\n")
print()

def main():
    def show_info():
        """
        Extracts and prints information about command usage events.
        Includes the Timestamp, executing user, and command executed.
        """
        for i in data:
            if 'COMMAND' in i:
                # 1.1. Include the Timestamp
                timestamp = i.split()[0]

                # 1.2. Include the executing user 
                execute_user = i.split()[9]

                # 1.3. Include the command.
                command_usage = i.split()[11]

                print(f"\nTimestamp of the log event: {timestamp} the executing user is: {execute_user} and command executed is: {command_usage}.")
                print()

    # 2. Log Parse auth.log: Monitor user authentication changes.

    def show_useradded():
        """
        Prints details of successful user or group additions.
        """
        for i in data:
            if ('useradd' in i or 'groupadd' in i) and not 'failed' in i:
                print(f"\nSuccessful User/Group Add: {i.strip()}")

    def show_userdel():
        """
        Prints details of deleted users.
        """
        for i in data:
            if 'userdel' in i:
                print(f"\nDeleted User: {i.strip()}")

    def show_changed_password():
        """
        Prints details of password changes.
        """
        for i in data:
            if 'passwd' in i:
                print(f"\nChanged Password: {i.strip()}")

    def show_su():
        """
        Prints details of `su` command usage.
        """
        for i in data:
            if 'su' in i:
                print(f"\nUsed su Command: {i.strip()}")

    def show_sudo():
        """
        Prints details of `sudo` command usage.
        Includes an alert for failed `sudo` attempts.
        """
        for i in data:
            if 'sudo' in i and 'authentication failure' in i:
                print("*************Alert*****************\n")
                print(f"\nALERT! Failed sudo Command: {i.strip()}")
            elif 'sudo' in i:
                print(f"\nUsed sudo Command: {i.strip()}")

    # Call the functions to process the log data
    show_info()
    
    print("\n***************To check all created users****************\n")
    show_useradded()
    print("\n***************To check all deleted users****************\n")
    show_userdel()
    print("\n***************To check all changed password****************\n")
    show_changed_password()
    print("\n****************To check of changing user operation***************\n")
    show_su()
    print("\n****************To check all sudo and alert notifications***************\n")
    show_sudo()
    print("\n*******************************\n")

if __name__ == '__main__':
    main()
