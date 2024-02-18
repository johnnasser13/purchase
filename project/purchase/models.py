
from django.db import models

# Company -- Department -- User -- PurchaseRequest -- PurchaseItem --Item -- ApproverRequest -- Approver -- AC -- Type -- Urgency

class Company(models.Model):
    cmpID = models.IntegerField(primary_key = True)
    cmpName = models.CharField(max_length=20)

  
class Department(models.Model):
    DpID = models.IntegerField(primary_key = True)
    DpName = models.CharField(max_length=20)
    cmpID = models.ForeignKey(Company, related_name='department', on_delete=models.CASCADE)




class User(models.Model):
    userID = models.IntegerField(primary_key = True)
    DpID = models.ForeignKey(Department, related_name='user', on_delete=models.CASCADE)
    userName = models.CharField(max_length=20)



class Type(models.Model):
    typeID = models.IntegerField(primary_key = True)
    typeStatus = models.CharField(max_length=20)



class Urgency(models.Model):
    urgencyID = models.IntegerField(primary_key = True)
    urgencyLevel = models.CharField(max_length=20)




class PurchaseRequest(models.Model):
    reqID = models.IntegerField(primary_key = True)
    DpID = models.ForeignKey(Department, related_name='purreq', on_delete=models.CASCADE)
    userID = models.ForeignKey(User, related_name='purreq', on_delete=models.CASCADE)
    typeID = models.ForeignKey(Type, related_name='purreq', on_delete=models.CASCADE)
    urgencyID = models.ForeignKey(Urgency, related_name='purreq', on_delete=models.CASCADE)




class Item(models.Model):
    itemID = models.IntegerField(primary_key = True)
    itemName = models.CharField(max_length=20)




class PurchaseItem(models.Model):
    purID = models.IntegerField(primary_key = True)
    itemID = models.ForeignKey(Item, related_name='purit', on_delete=models.CASCADE)
    reqID = models.ForeignKey(PurchaseRequest, related_name='purit', on_delete=models.CASCADE)
    price = models.IntegerField



class AC(models.Model):
    ACID = models.IntegerField(primary_key = True)
    DpID = models.ForeignKey(Department, related_name='ac', on_delete=models.CASCADE)
    typeID = models.ForeignKey(Type, related_name='ac', on_delete=models.CASCADE)
    urgencyID = models.ForeignKey(Urgency, related_name='ac', on_delete=models.CASCADE)




class Approver(models.Model):
    AppID = models.IntegerField(primary_key = True)
    ACID = models.ForeignKey(AC, related_name='approver', on_delete=models.CASCADE)
    userID = models.ForeignKey(User, related_name='approver', on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    order = models.IntegerField



class ApproverRequest(models.Model):
    AppReq = models.IntegerField(primary_key = True)
    AppID = models.ForeignKey(Approver, related_name='appreq', on_delete=models.CASCADE)
    reqID = models.ForeignKey(PurchaseRequest, related_name='appreq', on_delete=models.CASCADE)
    status = models.CharField(max_length=40)
    ApproverDate = models.DateField()


    



