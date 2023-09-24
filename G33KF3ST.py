import getpass
import random
import string


def generate_password():
    length = 12 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def multi_factor_authentication():
 
    otp = random.randint(100000, 999999)
    return otp

def main():
    print("Welcome to Secure Data Access")
    username = input("Enter your username: ")

 
    stored_password = generate_password()
    print("Your generated password:", stored_password)

   
    entered_password = getpass.getpass("Enter your password: ")


    if entered_password == stored_password:
        print("Password verified.")

        # Simulate MFA
        otp = multi_factor_authentication()
        print(f"Enter the OTP sent to your device: {otp}")
        entered_otp = input("Enter OTP: ")

        # Simulate OTP verification
        if int(entered_otp) == otp:
            print("Multi-Factor Authentication (MFA) successful. Access granted.")
        else:
            print("MFA failed. Access denied.")
    else:
        print("Password incorrect. Access denied.")

if __name__ == "__main__":
    main()
