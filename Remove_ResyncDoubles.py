## Delete resync dummies
# Import standard library modules
import os, shutil, getpass
# Get username of currently logged in user.
username1 = getpass.getuser()

# Path to dropbox file.
baseFile = r"/Users/"+username1+r"/Dropbox"

# If file has 'Selective Sync Confilict' its deleted.
for Resync_file in os.listdir(baseFile):
    if "(Selective Sync Conflict)" in Resync_file:
        RM_Path = os.path.join(baseFile, Resync_file)
        shutil.rmtree(RM_Path)
