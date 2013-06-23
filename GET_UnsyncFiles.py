##  SeeNonSyncFilesandFolders_Dropbox_Application
## bin/bash

#Import Dropbox Python Module
from dropbox import client, rest, session
#Import standard library modules.
import webbrowser, os, math, sys, urllib, getpass

# Get username of logged in account.
username1 = getpass.getuser()
# Path to dropbox file
baseFile = r"/Users/"+username1+r"/Dropbox"
# Get current working directory
workingDIR = os.getcwd()
#print "Your current working directory is: \r %s" %(workingDIR)
baseURL = r"www.dropbox.com/home"

# App information from Dropbox.com
APP_NAME = "NoSyncFilesandFolders"
APP_KEY = "6mxj9n8b08otsi2"
APP_SECRET = "8nbtuksilxhbmoy"
ACCESS_TYPE = "dropbox"

# Dropbox application login.
sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
request_token = sess.obtain_request_token()
url = sess.build_authorize_url(request_token)

# Make the user sign in and authorize this token
webbrowser.open_new(url)
print "\r **** Please visit this website and press the 'Allow' button, then hit 'Enter' here. ***"
raw_input()

# This will fail if the user didn't visit the above URL and hit 'Allow'
access_token = sess.obtain_access_token(request_token)
client = client.DropboxClient(sess)

# Get folder contents of each path passed into it.
def GetFolderContents(FolderID):
    try:
        folderMetadata = client.metadata(FolderID)
        folderContents = folderMetadata['contents']
        return folderContents
    except:
        return []

# Get contents of the root folder.
user_metadata = GetFolderContents('/')
filesList = []
totalFiles = 0
# Get contents of each directory in the root folder.
for i in user_metadata:
    filesProcessed = 0
    print "Hard at work... Processing [%s] file" %(i['path'][1:])
    first = i['path']
    filesList.append(first)
    filesProcessed += 1
    # Get contents of each second level folder
    for j in GetFolderContents(first):
        second = j['path']
        filesList.append(second)
        filesProcessed += 1
        # Get contents of each third level folder.
        for k in GetFolderContents(second):
            third = k['path']
            filesList.append(third)
            filesProcessed += 1
            # Get contents of each fourth level folder.
            for l in GetFolderContents(third):
                fourth = l['path']
                filesList.append(fourth)
                filesProcessed += 1
                # Get contents of each fifth level folder.
                for j in GetFolderContents(fourth):
                    fifth = j['path']
                    filesList.append(fifth)
                    filesProcessed += 1
    totalFiles += filesProcessed
    print "\t - Processed %s files in %s folder \r" %(filesProcessed, first[1:])
print "%s files processed from www.Dropbox.com in %s seconds... pretty good, eh? :)" %(totalFiles, "30")

# Breaking up the
for i in range(10):
    print (2**i)*"."+"\r"

## List of all files storable on Dropbox [https://www.dropbox.com/help/6/en]
acceptableExtensionsList = ['jpg', 'jpeg', 'png', 'tiff', 'tif', 'gif', 'bmp', 'ai', 'psd', '3gp',
    '3gpp', '3gpp2', 'avi', 'mov', 'mwv', 'm4v', 'mpg', 'mkv', 'mpeg', 'vob', 'flv', 'mts',
    'm2t', 'ts','dv']

# Processing files
for files in filesList:
    # Check for a file extension of each file.
    if len(files.split(".")[-1]) < 5:
        if files.split(".")[-1].lower() in acceptableExtensionsList:
            # if object is file then process accordingly
            if os.path.isfile(baseFile + files) is False:
                fileName  = os.path.split(files)[-1]
                fileLoc = baseFile+str(os.path.split(files.encode('utf-8'))[:-1][0])
                scriptLoc = str(workingDIR)+r"/creatingInternetLocation.scpt"
                builtURL =  urllib.quote(baseURL+os.path.join(os.path.split(files)[:-1])[0])
                inputString = ('osascript  "%s" "%s" "%s" "%s"') %(scriptLoc, builtURL, fileName, fileLoc)
                os.system(inputString)
                print "make a file with attributes"
            else:
                print "File not Folder already exists"
        elif os.path.isdir(baseFile + files):
            print "Folder alredy exists"
        else:
            try:
                os.mkdir(baseFile+files.replace(".","_"))
            except:
                print "Dummy file already exists"
    elif os.path.isdir(str(baseFile)+files.replace(".","_")):
        print "[%s] already exists" %(baseFile + files)
    elif os.path.isdir(str(baseFile)+files.replace(".","_")):
        print "[%s] already exists" %(baseFile + files)
    else:
        print str(baseFile), files.replace(".", "_")
        os.mkdir(str(baseFile)+files.replace(".","_"))
print "FINISHED!  You have saved soooo much space on your machine"



