DopboxApp
=========

Create pointers to the files that you choose not to sync via DropBox API.

Use virtualENV to create a virtual environment in the folder called 'Dropbox.ENV' .
  - https://pypi.python.org/pypi/virtualenv
  
Create a dropbox application:
  - https://www.dropbox.com/developers
Update the application with your information in 'GET_UnsyncFiles.py':
  # App information from Dropbox.com
	APP_NAME = "--Your Application Name--"
	APP_KEY = "--APP Key--"
	APP_SECRET = "--APP Secret Code--"

Reference 'DropboxApp_Requirements.txt' for pip installation modules required.

'Dropbox_Get_Unsync.scpt' is an applescript written for the required commands
to run the program.

  - 'GET_UnsyncFiles.py' contains the python script to create pointers to your
  dropbox files that you have chosen to unsync from your machine.
  	- The scipt will open an instance of your default browser and allow the user
  	to link the app to their dropbox account.
  	 
  - If the user decides to re-sync and files, they will be copied back to their
  local machine and each existing file with the same name "(Selective Sync Conflict)"
  will be added to the filename.  'Remove_ResyncDoubles.py' removes the extra files.
  