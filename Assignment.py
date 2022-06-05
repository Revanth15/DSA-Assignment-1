from Main import *

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
    elif userInput == '4':
        PackageCostbyInsertionSort(Record)
    elif userInput == '5':
        NoofPaxbyShellSort(Record)
    elif userInput == '6':
        SearchRecordbyCustomerName(Record)
    elif userInput == '7':
        SearchRecordbyPackageName(Record)
    elif userInput == '8':
        ListRecordsRange(Record)
    else:
        print("Please enter numbers from 0-7 only.Thank you!")