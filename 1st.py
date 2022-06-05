from Booking import Booking
def Menu():
    print("""
    1. Display all records
    2. Sort record by Customer Name using Bubble sort
    3. Sort record by Package Name using Selection sort
    4. Sort record by Package Cost using Insertion sort
    5. Search record by Customer Name using Linear Search and update record
    6. Search record by Package Name using Binary Search and update record
    7. List records range from $X to $Y. e.g $100-200
    0. Exit Application
    """)

record = {1: {"PackageName": "The Fullerton Hotel Glamping Under the Stars","CustomerName": "Kevin", "NoOfPax" : 3, "PackageCostPerPax" : 300},
          2: {"PackageName": "Play Line Friends Themed Staycation","CustomerName": "Yuki", "NoOfPax" : 4, "PackageCostPerPax" : 400},
          3: {"PackageName": "Shangri-La Rasa All-Inclusive Datecation","CustomerName": "Sebastian", "NoOfPax" : 10, "PackageCostPerPax" : 500},
          4: {"PackageName": "Raffles Hotel Reflections of Raffles Staycation","CustomerName": "Lewis", "NoOfPax" : 6, "PackageCostPerPax" : 200},
          5: {"PackageName": "Marina Bay Sands Sandsational Staycation Package","CustomerName": "Charles", "NoOfPax" : 22, "PackageCostPerPax" : 100},
          6: {"PackageName": "The Clan Uncovers: Craft and Cook Staycation Package","CustomerName": "Pierre", "NoOfPax" : 33, "PackageCostPerPax" : 550},
          7: {"PackageName": "Fairmont Singapore Mancation","CustomerName": "Mick", "NoOfPax" : 2, "PackageCostPerPax" : 900},
          8: {"PackageName": "The Barracks Hotel Sea Breeze & Champagne Package","CustomerName": "Daniel", "NoOfPax" : 17, "PackageCostPerPax" : 400},
          9: {"PackageName": "Marina Bay Sands experience","CustomerName": "Lando", "NoOfPax" : 5, "PackageCostPerPax" : 300},
          10: {"PackageName": "Duxton Reserve Resort","CustomerName": "Alex", "NoOfPax" : 9, "PackageCostPerPax" : 300},
         }

Record = [
        Booking("The Fullerton Hotel Glamping Under the Stars","Kevin", 3, 300),
        Booking("Play Line Friends Themed Staycation","Yuki", 4, 400),
        Booking("Shangri-La Rasa All-Inclusive Datecation","Sebastian", 10, 500),
        Booking("Raffles Hotel Reflections of Raffles Staycation","Lewis", 6, 200),
        Booking("Marina Bay Sands Sandsational Staycation Package","Charles", 22, 100),
        Booking("The Clan Uncovers: Craft and Cook Staycation Package","Pierre", 33, 550),
        Booking("Fairmont Singapore Mancation","Mick", 2, 900),
        Booking("The Barracks Hotel Sea Breeze & Champagne Package","Lando", 17, 400),
        Booking("Marina Bay Sands Experience","Daniel", 5, 300),
        Booking("Duxton Reserve Resort","Alex", 9, 300),
]

def DisplayAllRecords():
    index = 1
    while True:
        if index <= 10:
            print("--------------------------------------------------------------------")
            print(f"Package Name: {record[index]['PackageName']}")
            print(f"Customer Name: {record[index]['CustomerName']}")
            print(f"Number of Pax: {record[index]['NoOfPax']}")
            print(f"Package Cost per Pax: {record[index]['PackageCostPerPax']}")
            print("--------------------------------------------------------------------")
            index += 1
        elif index > 10:
            return False
    # for i in range(len(Record)):
    #     print(
    #         f"-------------------------------{i+1}------------------------------------")
    #     print(f"Package Name: {Record[i].get_package_name()}")
    #     print(f"Customer Name: {Record[i].get_customer_name()}")
    #     print(f"Number of Pax: {Record[i].get_no_of_pax()}")
    #     print(f"Package Cost per Pax: {Record[i].get_cost_per_pax()}")
    #     print("--------------------------------------------------------------------")

def CustomerNameBubbleSort():
    namelist = []
    index = 1
    for name in record:
        name = record[index]['CustomerName']
        namelist.append(name)
        index += 1
    print(namelist)

    length = len(namelist) - 1
    unsorted = True

    while unsorted:
        unsorted = False
        for element in range(0,length):
            if namelist[element] > namelist[element + 1]:
                hold = namelist[element + 1]
                namelist[element + 1] = namelist[element]
                namelist[element] = hold
                # print(namelist)
                unsorted = True
    print(namelist)
    for i in range(1, 11):
        for name in namelist:
            if record[i]['CustomerName'] == name:
                print("--------------------------------------------------------------------")
                print(f"Package Name: {record[i]['PackageName']}")
                print(f"Customer Name: {record[i]['CustomerName']}")
                print(f"Number of Pax: {record[i]['NoOfPax']}")
                print(f"Package Cost per Pax: {record[i]['PackageCostPerPax']}")
                print("--------------------------------------------------------------------")

def PackageNamebySelectionSort():
    namelist = []
    index = 1
    for name in record:
        name = record[index]['PackageName']
        namelist.append(name)
        index += 1
    print(namelist)

    i = 0
    while i<len(namelist):
        smallest = min(namelist[i:])
        index_of_smallest = namelist.index(smallest)
        namelist[i],namelist[index_of_smallest] = namelist[index_of_smallest],namelist[i]
        i=i+1
    print(namelist)

def PackageCostbyInsertionSort():
    costlist = []
    index = 1
    for name in record:
        name = record[index]['PackageCostPerPax']
        costlist.append(name)
        index += 1
    print(costlist)

    for i in range(1, len(costlist)): 
        val = costlist[i]
        j = i-1
        while j >=0 and val < costlist[j] : 
            costlist[j+1] = costlist[j] 
            j -= 1
        costlist[j+1] = val
    print (costlist)

