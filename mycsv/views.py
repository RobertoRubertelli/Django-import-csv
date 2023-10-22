from django.shortcuts import render

# I will use it to manage the error in case
from django.http import HttpResponse

# I need the model
from .models import Company

# I need Pandas
import pandas as pd

# Create your views here.

# I need the home view ready for the htmx
def Home(request):
    
    context = {}

    if request.htmx:
        return render(request,'homepartial.html')
    return render (request,'home.html',context)

# The function for the upload
def Company_Upload(request):
    
    # an empty context    
    context={}            
     
    # I need to check if the user choose a file 
    filepath = request.FILES.get('file', False)
    if filepath == False :
        msg="You have to choose a csv file"
        context={'msg':msg}

        return render (request,'homepartial.html',context)

    # if the user choosed the file go ahead in else
    else:
        # I have just one field name on request.FILES
        # I'm getting the file name choosed by the user
        myuploadfile= request.FILES['file']
        # Now I have the file name
        
        # Pandas is readind the csv file choosed by the user
        df = pd.read_csv(myuploadfile)
        
        # I will not check all the fields, if something will be wrong,
        # using try,in except,I will manage an extra error in case. 
        try:

            # I'm checking some fields before import, just for example
            if 'Organization Id' and 'Industry' and 'Number of employees' in df.columns:
                
                # I delete the rows present before the import
                Company.objects.all().delete()

                # To import I have to iterate the pandas for the ORM.
                # I have to avoid the iteration in case of BIG DATA, 
                # but here it is not the subject.
                row_iter = df.iterrows()

                objs = [

                    # my model
                    Company(
                        # I fill the model fields with the df rows,
                        # thrue the iteration
                        Index = row['Index'],
                        OrganizationId = row['Organization Id'],
                        Name = row['Name'],
                        Website = row['Website'],
                        Country = row['Country'], 
                        Description = row['Description'],
                        Founded = row['Founded'],
                        Industry = row['Industry'],
                        Numberofemployees = row['Number of employees'],

                        )
                    for index, row in row_iter
                    ]
                # bulk_create to safe the rows. 
                Company.objects.bulk_create(objs)
                
                # I want the text of the message alert in django code, 
                # giving it in the context.
                # in the partial html page the condition 
                # and the script, for the message.
                msg = "Imported in the Model." + " CSV File Name:   "+ str(myuploadfile) 
                context={'msg':msg}
                
                # I'm calling POST with HTMX, I'm sure I need just the partial
                return render(request,'homepartial.html',context)    
            
            
            else:
                # there is an error.. in the csv import fields name
                return HttpResponse("<H2>The file is wrong, it doesn't match the database fields.</H2>")
        except:
            # there is an error .. I don't know why. 
            return HttpResponse("<H2>Sorry, something is wrong , the file wasn't imported</H2>")
    

# to delete all rows
def deleterow(request):
            
    Company.objects.all().delete()
    
    msg="Rows Deleted"
    context={'msg':msg}
    
    return render (request,'homepartial.html',context)

# to print the objects rows in the terminal
def printrow(request):
    
    print(Company.objects.all())
    msg="Object Printed in the Terminal"
    context={'msg':msg}
    
    return render (request,'homepartial.html',context)