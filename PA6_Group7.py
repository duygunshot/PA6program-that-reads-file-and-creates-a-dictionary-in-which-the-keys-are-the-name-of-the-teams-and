#Group7
#Dean Tran, Edwin Rodriguez, Elisa Shukuru
#04/23/2023
"""The purpose of this project is to write a program that
reads file and creates a dictionary in which the keys are the
name of the teams, and each keys associated value is the number
of times the team has won the World Series."""
namewondict = dict()
yearnamedict = dict()
myset = set()
mylist = []
myrange = []

with open("WorldSeriesWinners.txt", "rt") as f:#Open the txt file as f
    for i in f:
        myset.add(i.strip())#add name to set so there is no duplicate
        mylist.append(i.strip())#add name to list
        
    for i in myset:
        x = mylist.count(i)#count how many time the team has won
        namewondict.update({i:x})#update the dictionary with name of the team and number of times they have won

    myrange = [i for i in range(1903, 2010) if i != 1904 and i != 1994]#make a range from 1903 to 2010 that exclude the year 1904 and 1994
    for i, j in zip(myrange, mylist):#run two loops at the same time
        yearnamedict.update({i:j})#update the dictionary with the year number and the name of the team

year = int(input("Enter a year number from 1903 to 2009: "))#Ask user to enter year number

while True:#Ask the user to enter again if the number is out of range or is 1904 or 1994
    if year not in range(1903,2010):
        year = int(input("Year out of range, please enter again: "))
    elif year == 1904 or year == 1994:
        year = int(input("World Series was not played in this year. Please enter again: "))
    else:
        break
        
name =yearnamedict[year]#find the name of the team
times = namewondict[name]#find the number of times they have won
print("Team that won World Series: ", name)#display the name
print("They have won: ", times, " time(s)")#display the year