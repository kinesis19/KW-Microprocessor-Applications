def input_name():
    name = input("Please enter your name: ")
    return name

def print_name(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    user_name = input_name()
    print_name(user_name)