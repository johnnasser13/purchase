from rest_framework import serializers
from ..models import Company , Department , User , PurchaseRequest , PurchaseItem ,Item , ApproverRequest , Approver , AC , Type , Urgency


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PurchaseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequest
        fields = '__all__'

class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ApproverRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApproverRequest
        fields = '__all__'

class ApproverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approver
        fields = '__all__'

class ACSerializer(serializers.ModelSerializer):
    class Meta:
        model = AC
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class UrgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Urgency
        fields = '__all__'