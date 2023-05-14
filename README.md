# Flask_fileDownloader
To set up the file upload and management system with admin panel, follow the instructions below:

Clone or download the repository from GitHub.

Install the required dependencies by running the command pip install flask, pandas in the terminal.
Also need to run thid commands - 
python -m venv venv
venv\Scripts\activate
set FLASK_APP=app.py
flask run

Navigate to the app directory and open the config.py file. Here, you can configure the application settings, such as the upload folder location, admin login credentials, and allowed file types.

Run the application by running the command python app.py in the terminal.

Open a web browser and navigate to http://localhost:5000 to access the application.

To upload a file, click on the "Upload File" button and select a CSV or XLSX file from your local machine. The uploaded files will be saved in the designated upload folder.

To access the admin panel, click on the "Admin Login" button and enter the credentials specified in the config.py file.

In the admin panel, you can view a table record of all the uploaded files. Each file will have two buttons, one to download the file and another to open the file.

Clicking on the "Download" button will download the file to your local machine.

Clicking on the "Open" button will display the contents of the file as a table using the Pandas package or any other suitable package.

That's it! You now have a file upload and management system with an admin panel that allows you to easily view and manipulate uploaded files.
