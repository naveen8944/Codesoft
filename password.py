import random
import string
def gen_Password(length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digit = string.digits
    symbol = string.punctuation
    total_char = lower_case + upper_case + digit + symbol    
    # Ensure the password contains at least one character from each category
    total_password = [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(digit),
        random.choice(symbol)
    ]  
    # Fill the remaining characters randomly
    for _ in range(length - 4):
        total_password.append(random.choice(total_char))
    
    # Shuffle the list to ensure randomness
    random.shuffle(total_password)
    
    return ''.join(total_password)

def main():
    print("Generate your Password:")
while True:
        try:
            length = int(input("Enter the length of the password (Note: Please enter a minimum of 8 characters): "))
            if length < 8:
                print("Enter a minimum of 8 characters for the length.")
            else:
                break
        except ValueError:
            print("Invalid Number! Please enter a valid number.")
    
total_password = gen_Password(length)
print("\nGenerated password is:")
print(total_password)
print("\nStore your password securely and don't share it with others.")

if _name_ == "_main_":
    main()