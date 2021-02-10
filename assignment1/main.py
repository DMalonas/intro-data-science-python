# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from RegexPractice import names, grades, logs


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("****Ex 1****\n")
    names()
    print("\n\n****Ex 2****\n")
    print("person: " + str(grades()))
    print("\n\n****Ex 3****\n")
    print(len(logs()))

