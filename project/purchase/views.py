from urllib import response
from django.shortcuts import render
from django.http.response import JsonResponse 
from .models import Company , Department , User , PurchaseRequest , PurchaseItem ,Item , ApproverRequest , Approver , AC , Type , Urgency
from rest_framework.decorators import api_view
from .serializers import CompanySerializer , DepartmentSerializer , UserSerializer , PurchaseRequestSerializer , PurchaseItemSerializer , ItemSerializer , ApproverRequestSerializer, ApproverSerializer , ACSerializer, TypeSerializer ,UrgencySerializer
from rest_framework import status ,filters 
from rest_framework.response import Response




#@api_view(['GET','POST'])
#def List(request):
#
#    #GET
#    if request.method == 'GET':
#        companies = Company.objects.all()
#        serializer = CompanySerializer(companies, many=True)
#        return Response(serializer.data)
#
#    #POST
#    elif request.method == 'POST':
#        serializer = CompanySerializer(data= request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status= status.HTTP_201_CREATED)    
#        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
#
#

#@api_view()
#def


def List(request):
  # data = Company.objects.all()
  # Response = {
  #     'companies': list(data.values('cmpID','cmpName'))
  # }
    
    companies = [
        {

        'cmpID': 1 ,
        "cmpName" : "DELL"

        },

        {
        'cmpID': 2 , 
        "cmpName" : "HP"
        }

    ]
    return JsonResponse(companies, safe=False)




