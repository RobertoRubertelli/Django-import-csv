# Django import csv htmx hyperscript pandas example tutorial
[link to Git-Hub source files](https://github.com/RobertoRubertelli/django-import-csv/tree/master)
####
Import a csv file, choosed by the user, in a Django Model.
The scenario is common, here a tutorial example.  
Django Htmx Hyperscript Bootstrap Pandas 
working together to resolve the scenario.
The code at the hand must be EFFICIENT and SHORT.
I try to keep the code BASIC here.

Htmx is taking care to open the file request in the client browser.
Htmx is sending the Ajax post request to the server   
and send back the partial html to the client.
Hyperscript is giving the import bar status in the DOM.
Hyperscript in the button,when clicked,it is typing in the DOM.
Hyperscript needs Bootstrap for the progress bar.
Pandas is reading the csv.
Iterating the pandas dataframe , I fill the model ORM.
This code is not for BIG DATA.
It is useful for 20.000 up to 50.000 rows upload.


My Tutorial [Django Import CSV](https://www.managepy.it/importcsvtutorial)

My Site [Managepy.it](https://www.managepy.it/)


## Getting started

## Setup

Read the requirements.txt

```bash

# Install requirements.txt in a new virtual environment
pipenv install -r requirements.txt
# activate the shell
pipenv shell

# Clone Git folders
Clone Git
# Setup database.
python manage.py migrate

# Now you can view the project at http://localhost:8000
```
