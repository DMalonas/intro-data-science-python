# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Q1_PoE import *
from Q2_AvgInfluenzaDoses import *
from Q3_ChickenpoxBySex import *
from Q4_CorrChickepox import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Q1----> : " + str(proportion_of_education()) + "\n")

    print("Q2----> : " + str(average_influenza_doses()) + "\n")

    print("Q3----> : " + str(chickenpox_by_sex()) + "\n")

    print("Q4----> : " + str(corr_chickenpox()) + "\n")
