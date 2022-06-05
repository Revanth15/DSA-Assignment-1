from tabulate import tabulate
from Booking import Booking
import time
from colorama import Fore, Style


def Menu():
    print("""
    1. Display all records
    2. Sort record by Customer Name using Bubble sort
    3. Sort record by Package Name using Selection sort
    4. Sort record by Package Cost using Insertion sort
    5. Sort record by Number of Pax using Shell sort
    6. Search record by Customer Name using Linear Search and update record
    7. Search record by Package Name using Binary Search and update record
    8. List records range from $X to $Y. e.g $100-200
    0. Exit Application
    """)

def printC(value,color):
    if color. upper() == "Y": 
        print(Fore.YELLOW + value + Style.RESET_ALL)
    elif color.upper() == "R": 
        print(Fore.RED + value + Style.RESET_ALL)
    elif color.upper() == "G": 
        print(Fore.GREEN + value + Style.RESET_ALL)
    else:
        print(value)

def UpdateRecord(Record, i):
    name = input("Enter Updated Customer Name: ")
    package_name = input("Enter Updated Package Name: ")
    pax = input("Enter Updated number of pax: ")
    cost_per_pax = input("Enter Updated cost per pax: ")
    oldcname = Record[i].get_customer_name()
    oldpname = Record[i].get_package_name()
    oldpax = Record[i].get_no_of_pax()
    oldcost = Record[i].get_cost_per_pax()
    
    if name != '':
        if name.isalpha() == True:
            Record[i].set_customer_name(str(name).title())
        else:
            printC("Please only enter letters only for customer name", "Y")
    if package_name != '':
        if package_name.isalpha() == True:
            Record[i].set_package_name(str(package_name).title())
        else:
            printC("Please only enter letters only for package name", "Y")
    if pax != '':
        if pax.isdigit() == True and int(pax) > 0:
            Record[i].set_no_of_pax(int(pax))
        else:
            printC("Please only enter numbers for pax", "Y")
    if cost_per_pax != '':
        if cost_per_pax.isdigit() == True and int(cost_per_pax) > 0:
            Record[i].set_cost_per_pax(int(cost_per_pax))
        else:
            printC("Please only enter numbers for cost", "Y")
    print(f"""
    ******************************************************************************
    Package Name: {oldpname if oldpname == Record[i].get_package_name() else Fore.BLUE + f"{oldpname} ---> {Record[i].get_package_name()}"+ Style.RESET_ALL}
    Customer Name: {oldcname if oldcname == Record[i].get_customer_name() else Fore.BLUE + str(oldcname) + " ---> " + str(Record[i].get_customer_name())+ Style.RESET_ALL}
    Number of Pax: {oldpax if oldpax == Record[i].get_no_of_pax() else Fore.BLUE + str(oldpax) + " ---> " + str(Record[i].get_no_of_pax())+ Style.RESET_ALL}
    Cost per Pax: {oldcost if oldcost == Record[i].get_cost_per_pax() else Fore.BLUE + str(oldcost) + " ---> " + str(Record[i].get_cost_per_pax())+ Style.RESET_ALL}
    """)
    printC("Record has successfully been updated!","G")


def DisplayAllRecords(Record):
    table = []

    for i in range(len(Record)):
        table.append([Record[i].get_package_name(), Record[i].get_customer_name(), Record[i].get_no_of_pax(), Record[i].get_cost_per_pax()])

    print(tabulate(table, headers=["Package Name", "Customer Name", "Pax number", "Cost per pax"],tablefmt="psql"))
    print("************************************************End of records**********************************************")


def CustomerNameBubbleSort(Record):
    n = len(Record)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if Record[j].get_customer_name() > Record[j + 1].get_customer_name():
                Record[j], Record[j + 1] = Record[j + 1], Record[j]
    DisplayAllRecords(Record)


def PackageNamebySelectionSort(Record):
    for i in range(len(Record)):
        min_idx = i
        for j in range(i+1, len(Record)):
            if Record[min_idx].get_package_name() > Record[j].get_package_name():
                min_idx = j
        Record[i], Record[min_idx] = Record[min_idx], Record[i]


def PackageCostbyInsertionSort(Record):
    for i in range(1, len(Record)):
        val = Record[i]
        j = i
        while j > 0 and val.get_cost_per_pax() < Record[j - 1].get_cost_per_pax():
            Record[j] = Record[j - 1]
            j -= 1
        Record[j] = val


def NoofPaxbyShellSort(Record):
    n = len(Record)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = Record[i]
            j = i
            while j >= gap and Record[j-gap].get_no_of_pax() > Record[i].get_no_of_pax():
                Record[j] = Record[j-gap]
                j -= gap
            Record[j] = temp
        gap //= 2


def SearchRecordbyCustomerName(Record):
    search_value = str(input("Enter Customer Name: ")).title()
    table = []
    for i in range(len(Record)):
        if Record[i].get_customer_name() == search_value:
            table.append([i,Record[i].get_package_name(), Record[i].get_customer_name(), Record[i].get_no_of_pax(), Record[i].get_cost_per_pax()])

    if len(table) == 1:
        UpdateRecord(Record, table[0][0])
    elif len(table) > 1:
        print("Looks like there are more than 1 customer ")
        print(tabulate(table, headers=["ID","Package Name", "Customer Name", "Pax number", "Cost per pax"],tablefmt="psql"))
        chosenID = int(input("Enter the ID of the customer you wish to update: "))
        for i in range(len(table)):
            if chosenID == table[i][0]:
                UpdateRecord(Record, chosenID)
    else:
        printC("Name not found in list", "R")


def SearchRecordbyPackageName(Record):
    PackageNamebySelectionSort(Record)

    n = input("Enter Package Name: ").title()
    low = 0
    high = len(Record) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if Record[mid].get_package_name() < n:
            low = mid + 1
        elif Record[mid].get_package_name() > n:
            high = mid - 1
        else:
            UpdateRecord(Record, mid)
            break


def ListRecordsRange(Record):
    while True:
        rangeInput = input("Enter range: ").replace("$", "")
        if rangeInput == "0":
            printC("0 cannot be entered","Y")
            return None
        rangeInput = rangeInput.split("-")
        if not (rangeInput[0].isdecimal() and rangeInput[1].isdecimal()):
            printC("$X and $Y is not a number!","Y")
            return None
        PackageCostbyInsertionSort(Record)
        if int(rangeInput[0]) < Record[0].get_cost_per_pax():
            printC(f"Range is too low, lowest package cost per pax is ${Record[0].get_cost_per_pax()} and you entered ${rangeInput[0]}", "Y")
            return None
        table = []
        for i in range(len(Record)):
            if Record[i].get_cost_per_pax() in range(int(rangeInput[0]), int(rangeInput[1])+1):
                table.append([i+1,Record[i].get_package_name(), Record[i].get_customer_name(), Record[i].get_no_of_pax(), Record[i].get_cost_per_pax()])

        print(tabulate(table, headers=["ID","Package Name", "Customer Name", "Pax number", "Cost per pax"],tablefmt="psql"))
        print("**************************************************End of records*************************************************")
        break


Record = [
    Booking("The Fullerton Hotel Glamping Under the Stars",
            "Max Verstappen", 3, 300),
    Booking("Play Line Friends Themed Staycation", "Yuki Tsunoda", 4, 400),
    Booking("Shangri-La Rasa All-Inclusive Datecation",
            "Sebastian Vettel", 10, 500),
    Booking("Raffles Hotel Reflections of Raffles Staycation",
            "Lewis Hamilton", 6, 200),
    Booking("Marina Bay Sands Sandsational Staycation Package",
            "Charles Leclerc", 22, 100),
    Booking("The Clan Uncovers: Craft and Cook Staycation Package",
            "Pierre Gasly", 33, 550),
    Booking("Fairmont Singapore Mancation", "Mick Schumacher", 2, 900),
    Booking("The Barracks Hotel Sea Breeze & Champagne Package",
            "Alex Albon", 17, 400),
    Booking("Marina Bay Sands Experience", "Daniel Ricciardo", 5, 300),
    Booking("Duxton Reserve Resort", "Alex Albon", 9, 300)
]


while True:
    Menu()
    userInput = input("Enter (1-7) to begin program, 0 to quit: ")
    if userInput == '0':
        for x in range(0, 4):
            b = "Ending Program" + "." * x
            print(b, end="\r")
            time.sleep(0.5)
        break
    elif userInput == '1':
        DisplayAllRecords(Record)
    elif userInput == '2':
        CustomerNameBubbleSort(Record)
    elif userInput == '3':
        PackageNamebySelectionSort(Record)
        DisplayAllRecords(Record)
    elif userInput == '4':
        PackageCostbyInsertionSort(Record)
        DisplayAllRecords(Record)
    elif userInput == '5':
        NoofPaxbyShellSort(Record)
        NoofPaxbyShellSort(Record)
        DisplayAllRecords(Record)
    elif userInput == '6':
        SearchRecordbyCustomerName(Record)
    elif userInput == '7':
        SearchRecordbyPackageName(Record)
    elif userInput == '8':
        ListRecordsRange(Record)
    else:
        printC("Please enter numbers from 0-7 only.Thank you!","R")
