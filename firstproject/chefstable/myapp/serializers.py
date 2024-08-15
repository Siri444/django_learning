from rest_framework import serializers
from .models import employee,student

#validators

'''def start_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('NAme should start with r')'''
    
    
'''class studentserializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=50)
    #field level validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    #object level validation
    def validate(self,value):
        na=value.get('name')
        ct=value.get('city')
        if na.lower()=='shreya' and ct.lower()!='hyderabad':
            raise serializers.ValidationError('City not valid')
        return value
    
    def create(self,validated_data):
        return student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        #print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        #print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance'''
        
    
class employeeserializer(serializers.Serializer):
    emp_name=serializers.CharField(max_length=100)
    emp_id=serializers.IntegerField()
    department=serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return employee.objects.create(**validated_data)
    
#modelserializer

class studentserializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower()!='r':
            raise serializers.ValidationError('NAme should start with r')
    name=serializers.CharField(validators=[start_with_r])
    #name=serializers.CharField(read_only=True)
    class Meta:
        model=student
        fields=['name','roll','city']
        #read_only_fields=['name','city']
        
        #field level validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value
        #object level validation
    def validate(self,value):
        na=value.get('name')
        ct=value.get('city')
        if na.lower()=='sonam' and ct.lower()!='hyderabad':
            raise serializers.ValidationError('City not valid')
        return value
