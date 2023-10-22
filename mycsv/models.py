from django.db import models

# Create your models here.

# I need the model to import the csv file in the ORM 
# I call it "Company"
# I'm adding upload_at field as a dateTimeField,
# it is useful to get the last updated rows date
class Company(models.Model):
    
    Index = models.CharField(max_length=50,primary_key=True)
    OrganizationId = models.CharField(max_length=50,blank=True,null=True)
    Name = models.CharField(max_length=50,blank=True,null=True)
    Website = models.URLField(max_length=50,blank=True,null=True)
    Country = models.CharField(max_length=50,blank=True,null=True)
    Description = models.CharField(max_length=50,blank=True,null=True)
    Founded = models.CharField(max_length=50,blank=True,null=True)
    Industry = models.CharField(max_length=50,blank=True,null=True)
    Numberofemployees = models.CharField(max_length=50,blank=True,null=True)
    upload_at = models.DateTimeField(blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'COMPANY'