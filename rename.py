from os import rename, listdir
from os.path import isfile, join
import tvdb_api

mypath = "./"
tv = tvdb_api.Tvdb()

allfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

series = input("Series Name: ")
season = int(input("Season: "))
supported_types = ["mp4","avi","mov"]
print("\n\n Supported file types are: ")
print(supported_types)
print("To add more add them to the 'supported_types' variable in rename.py\n")

filestype = input("File type")

# Remove files that arenot
files = allfiles
for i in allfiles:
        if i not in series:
                files.remove(i)

print(tv[series][season].data.keys())
