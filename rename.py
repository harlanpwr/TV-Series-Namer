from os import rename, listdir
from os.path import isfile, join
import tvdb_api


myPath = "./Season 1/"
tv = tvdb_api.Tvdb()

allFiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]


# Returns the int as a string and if it is under 10 it puts a 0 at the front of it e.g 8 => "08"
def add0(num):
    if num < 10:
        return "0" + str(num)
    else:
        return str(num)

# Collects user unpit to get the Series name, season and file type
series = input("Series Name: ")
#series = "Brooklyn Nine-Nine"

season = input("Season: ")
while not season.isdigit():
    print("Error. Season must be a number")
    season = input("Season: ")
season = int(season)




# All supported types. User can add to this variable at will
# It is a safety measure to make sure it dosn't clear the directory
supported_types = [".mp4",".avi",".mov"]

# Tells the user about filetpyes
print("\n\n Supported file types are: ")
print(supported_types)
print("To add more add them to the 'supported_types' variable in rename.py\n")

fileType = input("File type: ")
while fileType not in supported_types:
    print("\nError not a supported filetype. Please add it or enter a supported type")
    fileType = input("File type: ")







# Remove files that do not have the specified file extention
files = allFiles

for i in allFiles:
    if fileType not in i:
        files.remove(i)
files.sort(reverse=True)
for i in files:
    print(i)

# List of episodes and the amount of them
epList = tv[series][season]
episodeCount = len(epList)

newFiles = []

# This loop iterates through all the episodes and then renames the file to it
for i in range(1, episodeCount + 1):
    epName = epList[i]["episodeName"]
    epNumber = i

    # Fstring deciding the layout of name. Until I add a custom way
    newName  = f"{series} - s{add0(season)}e{add0(epNumber)} - {epName}{fileType}"
    newFiles.append(newName)
    #rename(myPath + files[i-1], myPath + newFiles[i-1])
