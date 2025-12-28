## WAP that reads a Date in MMDDYYYY format and display the date in the format <MonthName> <Day>, <Year>

date=int(input("Enter the date in MMDDYYYY Format"))

#now We need to do some simple calculations to extract month, day and year from the given input

month=date//1000000
day=(date//10000)%100
year=date%10000

month_names=["January","February","March","April","May","June","July","August","September","October","November","December"]

print("The date is %s %d, %d"%(month_names[month-1],day,year))