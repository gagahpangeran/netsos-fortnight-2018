import hashlib


def hash_password(password):
    """Hashes a string with md5 and returns the hex of the hash."""
    hashed = hashlib.md5()
    hashed.update(password.encode())
    return hashed.hexdigest()


def main():
    print("Welcome to Secure System Enterprises!\n")
    print("Running system checks...")
    print("System Info:")
    print("Version Number: 13.3.7")
    print("Last Updated: 31 August 1995\n")
    print("Available Commands:")
    print("CREATEUSER <username>")
    print("LOGIN <username>")
    print("GETFLAG [this command is for admins only]")

    users = {
        'm_delima': {
            'hashed_password': "42b1f9f860e2be044fa45b82a361f235",
            'is_admin': True,
        },
    }
    current_user = None
    while True:
        command = input(">> Enter a command: ").split(" ", 1)
        try:
            if not command:
                print("Please enter a command.")
            elif command[0] == "LOGIN":
                if current_user is not None:
                    print("You are already logged in!")
                    continue
                if len(command) != 2:
                    print("Please specify your username")
                    continue
                password = input("Enter your password: ")
                if command[1] in users and users[command[1]]['hashed_password'] == hash_password(password):
                    current_user = users[command[1]]
                    print("Welcome back", command[1] + "!")
                else:
                    print("Invalid username or password.")
            elif command[0] == "CREATEUSER":
                if len(command) != 2:
                    print("Please specify your username")
                    continue
                if command[1] in users:
                    print("Sorry, this username is already taken.") 
                    continue
                password = input("Enter your password: ")
                users[command[1]] = {
                    'hashed_password': hash_password(password),
                    'is_admin': False,
                }
                print("Your account has successfully been created!")
            elif command[0] == "GETFLAG":
                if current_user and current_user["is_admin"]:
                    with open("flag.txt") as f:
                        print("The flag is", f.read())
                else:
                    print("You are not an admin, begone!")
                    exit()
            else:
                print("Invalid command.")
        except Exception:
            print("Uh-oh, and error occured while trying to process your command :(")


if __name__ == "__main__":
    main()