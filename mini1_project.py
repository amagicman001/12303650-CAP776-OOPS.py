def printmenu():
  print("1. Add Record")
  print("2. Delete a specific record")
  print("3. View all records")
  print("4. view a specific year records")
  print("5. view last 5 year records")
  print("6. Exit from program")

def addRecord(dataset):
  year=int(input("Enter year: "))
  if year in dataset:
    print("Data for specific Year already Present!!")
    return
  elif year % 4 != 0 or (year %100==0 and year%400!=0):
    print(f"Invalid Year!!--Olympic was not held in {year}")
    return
  else:
    total=int(input("Enter total no. of medals won: "))
    gold=int(input("Enter no. of Gold medals won: "))
    silver=int(input("Enter no. of Silver medals won: "))
    bronze=int(input("Enter no. of Bronze medals won:"))
    if total != gold+silver+bronze:
        print("Invalid input")
        return
    else:
         dataset[year]=[total,gold,silver,bronze]
         print(f"Record added successfully for {year}!!")

def deleteRecord(dataset):
  year=int(input("Enter the year of which record is to delete: "))
  if year in dataset:
    del dataset[year]
    print(f"Record deleted successfully for {year}")
  else:
    print(f"Record Not Found for {year}")

def viewAllrecord(dataset):
  print("*******************Olympic Records Year wise*********************")
  print()
  if dataset:
    for year, medal in dataset.items():
        if year in dataset:
            print(f"Year: {year}")
            print(f" Total Medals won: {medal[0]}")
            print(f" Gold Medals won: {medal[1]}")
            print(f" Silver Medals won: {medal[2]}")
            print(f" Bronze Medals won: {medal[3]}")
            print()
        else:
           print("No records found. Empty dataset")

def viewSpecific(dataset):
  year=int(input("Enter the year whose Record you want: "))
  if year in dataset:
   medal=dataset[year]
   print(f"Total Medals won: {medal[0]}")
   print(f"Gold Medals won: {medal[1]}")
   print(f"Silver Medals won: {medal[2]}")
   print(f"Bronze Medals won: {medal[3]}")
  else:
    print(f"Record Not found for {year}")


def viewLast5(dataset):
   print()
   print("Last 5 year Records->")
   last5years = sorted(dataset.keys(), reverse=True)[:5]
   for year in last5years:
    if year in dataset:   
      medal = dataset[year]
      print(f"Year: {year}")
      print(f"  Total Medals won: {medal[0]}")
      print(f"  Gold Medals won: {medal[1]}")
      print(f"  Silver Medals won: {medal[2]}")
      print(f"  Bronze Medals won: {medal[3]}")
      print()
    else:
       print("No Records found")

def main():
  dataset={
      1992: [7,7,0,0],
      1996: [8,4,2,2],
      2000: [6,4,0,2],
      2004: [6,5,2,0],
      2008: [4,0,3,1],
      2012: [5,2,0,3],
      2016: [6,3,0,3],
      2020: [4,2,1,1],
    }
  
  print("___________________Welcome to CUBA's, Boxing records in Olympics______________________")
  while True:
      print("\n")
      printmenu()
      choice=input("Enter your choice: ")
      print()
      if choice=='1':
        addRecord(dataset)
      elif choice=='2':
        deleteRecord(dataset)
      elif choice=='3':
        viewAllrecord(dataset)
      elif choice=="4":
        viewSpecific(dataset)
      elif choice=='5':
         viewLast5(dataset)
      else:
        print("Invalid Choice!!")
        print()
        print("--------------Thanks for using my snippet!!-----------------")
        print()
        return False

if __name__=="__main__":
  main()
