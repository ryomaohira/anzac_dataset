# from lib.WW1Photographs import WW1Photographs as WW1P
from lib.Person import Person
from lib.PersonManager import PersonManager

def main():
    portraits_csv = './CSV/soldier_portraits_australasian_traveller.csv'
    personManager = PersonManager([portraits_csv])



print("Start ----------------------------------------------")
main()
print("End ------------------------------------------------")




