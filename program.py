def greet_user():
    print("Hello, welcome to Python programming!")

def main():
    greet_user()
    user_name = input("What is your name? ")
    print(f"Nice to meet you, {user_name}!")

if __name__ == "__main__":
    main()
