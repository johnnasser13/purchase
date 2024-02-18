from urllib import response
from django.shortcuts import get_object_or_404, render
from django.http.response import JsonResponse 
from ..models import Company , Department , User , PurchaseRequest , PurchaseItem ,Item , ApproverRequest , Approver , AC , Type , Urgency
from rest_framework.decorators import api_view
from .serializers import CompanySerializer , DepartmentSerializer , UserSerializer , PurchaseRequestSerializer , PurchaseItemSerializer , ItemSerializer , ApproverRequestSerializer, ApproverSerializer , ACSerializer, TypeSerializer ,UrgencySerializer
from rest_framework import status , serializers
from rest_framework.response import Response




#company api
@api_view(['GET'])
def get_cmp(request):
    if request.query_params:
        companies = Company.objects.filter(**request.query_params.dict())
    else:
        companies = Company.objects.all()

    if companies:
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_cmp(request):
    company = CompanySerializer(data=request.data)
 
    # validating for already existing data
    if Company.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if company.is_valid():
        company.save()
        return Response(company.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_cmp(request, pk):
    company = Company.objects.get(pk=pk)
    data = CompanySerializer(instance=company, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_cmp(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    return Response(status=status.HTTP_202_ACCEPTED)











#department api
@api_view(['GET'])
def get_dp(request):
    if request.query_params:
        departments = Department.objects.filter(**request.query_params.dict())
    else:
        departments = Department.objects.all()

    if departments:
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_dp(request):
    department = DepartmentSerializer(data=request.data)
 
    # validating for already existing data
    if Department.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if department.is_valid():
        department.save()
        return Response(department.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_dp(request, pk):
    department = Department.objects.get(pk=pk)
    data = DepartmentSerializer(instance=department, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_dp(request, pk):
    departments = get_object_or_404(Department, pk=pk)
    departments.delete()
    return Response(status=status.HTTP_202_ACCEPTED)











#user api
@api_view(['GET'])
def get_user(request):
    if request.query_params:
        users = User.objects.filter(**request.query_params.dict())
    else:
        users = User.objects.all()

    if users:
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_user(request):
    users = UserSerializer(data=request.data)
 
    # validating for already existing data
    if User.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if users.is_valid():
        users.save()
        return Response(users.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_user(request, pk):
    users = User.objects.get(pk=pk)
    data = UserSerializer(instance=users, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_user(request, pk):
    users = get_object_or_404(User, pk=pk)
    users.delete()
    return Response(status=status.HTTP_202_ACCEPTED)






#PurchaseRequest api
@api_view(['GET'])
def get_purchasereq(request):
    if request.query_params:
        purreq = PurchaseRequest.objects.filter(**request.query_params.dict())
    else:
        purreq = PurchaseRequest.objects.all()

    if purreq:
        serializer = PurchaseRequestSerializer(purreq, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_purchasereq(request):
    purreq = PurchaseRequestSerializer(data=request.data)
 
    # validating for already existing data
    if PurchaseRequest.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if purreq.is_valid():
        purreq.save()
        return Response(purreq.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_purchasereq(request, pk):
    purreq = PurchaseRequest.objects.get(pk=pk)
    data = PurchaseRequestSerializer(instance=purreq, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_purchasereq(request, pk):
    purreq = get_object_or_404(PurchaseRequest, pk=pk)
    purreq.delete()
    return Response(status=status.HTTP_202_ACCEPTED)







#PurchaseItem
@api_view(['GET'])
def get_purchaseitem(request):
    if request.query_params:
        puritem = PurchaseItem.objects.filter(**request.query_params.dict())
    else:
        puritem = PurchaseItem.objects.all()

    if puritem:
        serializer = PurchaseItemSerializer(puritem, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_purchaseitem(request):
    puritem = PurchaseItemSerializer(data=request.data)
 
    # validating for already existing data
    if PurchaseItem.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if puritem.is_valid():
        puritem.save()
        return Response(puritem.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_purchaseitem(request, pk):
    puritem = PurchaseItem.objects.get(pk=pk)
    data = PurchaseItemSerializer(instance=puritem, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_purchaseitem(request, pk):
    puritem = get_object_or_404(PurchaseItem, pk=pk)
    puritem.delete()
    return Response(status=status.HTTP_202_ACCEPTED)






#Item
@api_view(['GET'])
def get_item(request):
    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()

    if items:
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_item(request):
    items = ItemSerializer(data=request.data)
 
    # validating for already existing data
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if items.is_valid():
        items.save()
        return Response(items.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_item(request, pk):
    items = Item.objects.get(pk=pk)
    data = ItemSerializer(instance=items, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_item(request, pk):
    items = get_object_or_404(Department, pk=pk)
    items.delete()
    return Response(status=status.HTTP_202_ACCEPTED)






#ApproverRequest
@api_view(['GET'])
def get_appreq(request):
    if request.query_params:
        appreq = ApproverRequest.objects.filter(**request.query_params.dict())
    else:
        appreq = ApproverRequest.objects.all()

    if appreq:
        serializer = ApproverRequestSerializer(appreq, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_appreq(request):
    appreq = ApproverRequestSerializer(data=request.data)
 
    # validating for already existing data
    if ApproverRequest.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if appreq.is_valid():
        appreq.save()
        return Response(appreq.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_appreq(request, pk):
    appreq = ApproverRequest.objects.get(pk=pk)
    data = ApproverRequestSerializer(instance=appreq, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_appreq(request, pk):
    appreq = get_object_or_404(ApproverRequest, pk=pk)
    appreq.delete()
    return Response(status=status.HTTP_202_ACCEPTED)







#Approver
@api_view(['GET'])
def get_approver(request):
    if request.query_params:
        approver = Approver.objects.filter(**request.query_params.dict())
    else:
        approver = Approver.objects.all()

    if approver:
        serializer = ApproverSerializer(approver, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_approver(request):
    approver = ApproverSerializer(data=request.data)
 
    # validating for already existing data
    if Approver.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if approver.is_valid():
        approver.save()
        return Response(approver.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_approver(request, pk):
    approver = Approver.objects.get(pk=pk)
    data = ApproverSerializer(instance=approver, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_approver(request, pk):
    approver = get_object_or_404(Approver, pk=pk)
    approver.delete()
    return Response(status=status.HTTP_202_ACCEPTED)






#AC
@api_view(['GET'])
def get_ac(request):
    if request.query_params:
        ac = AC.objects.filter(**request.query_params.dict())
    else:
        ac = AC.objects.all()

    if ac:
        serializer = ACSerializer(ac, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_ac(request):
    ac = ACSerializer(data=request.data)
 
    # validating for already existing data
    if AC.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if ac.is_valid():
        ac.save()
        return Response(ac.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_ac(request, pk):
    ac = AC.objects.get(pk=pk)
    data = ACSerializer(instance=ac, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_ac(request, pk):
    ac = get_object_or_404(AC, pk=pk)
    ac.delete()
    return Response(status=status.HTTP_202_ACCEPTED)






#Type
@api_view(['GET'])
def get_type(request):
    if request.query_params:
        type = Type.objects.filter(**request.query_params.dict())
    else:
        type = Type.objects.all()

    if type:
        serializer = TypeSerializer(type, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_type(request):
    type = TypeSerializer(data=request.data)
 
    # validating for already existing data
    if Type.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if type.is_valid():
        type.save()
        return Response(type.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_type(request, pk):
    type = Type.objects.get(pk=pk)
    data = TypeSerializer(instance=type, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_type(request, pk):
    type = get_object_or_404(Type, pk=pk)
    type.delete()
    return Response(status=status.HTTP_202_ACCEPTED)






#urgency api
@api_view(['GET'])
def get_urgency(request):
    if request.query_params:
        urgency = Urgency.objects.filter(**request.query_params.dict())
    else:
        urgency = Urgency.objects.all()

    if urgency:
        serializer = UrgencySerializer(urgency, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_urgency(request):
    urgency = UrgencySerializer(data=request.data)
 
    # validating for already existing data
    if Urgency.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if urgency.is_valid():
        urgency.save()
        return Response(urgency.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_urgency(request, pk):
    urgency = Urgency.objects.get(pk=pk)
    data = UrgencySerializer(instance=urgency, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_urgency(request, pk):
    urgency = get_object_or_404(Urgency, pk=pk)
    urgency.delete()
    return Response(status=status.HTTP_202_ACCEPTED)






























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


#@api_view()
#def


#def List(request):
  # data = Company.objects.all()
  # Response = {
  #     'companies': list(data.values('cmpID','cmpName'))
  # }
    
#   companies = [
#       {
#
#       'cmpID': 1 ,
#       "cmpName" : "DELL"
#
#       },
#
#       {
#       'cmpID': 2 , 
#       "cmpName" : "HP"
#       }
#
#   ]
#   return JsonResponse(companies, safe=False)
#
#
#
#
