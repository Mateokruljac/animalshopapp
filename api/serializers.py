from pets.models import Animal, Comments, Tag, Category
from rest_framework import serializers
     
from django.contrib.auth.models import User 
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ["id","name","about","owner","species","likes","img","status","price"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["id","name","body","dateAdded","owner","animal"]
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id","name","owner"]
   

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","title","owner"]

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ["first_name","last_name","username","email","password","password"]
        extra_kwargs = {
            "password1" :{"write_only" : True}
        }
    
    def create(self):
        email = self.validated_data["email"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        username =  self.validated_data["username"]
        password =  self.validated_data["password"]
        confirm_password =  self.validated_data["password"]
        
        if password != confirm_password:
            raise serializers.ValidationError({"password" : "Passwords must matching"})
        
        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError({"username" : "User with that username already exists!"})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({"username" : "User with that username already exists!"})


        user = User(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            password = password)
        
        user.save()
        
        
        return user
    
class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["username","password"]
        
    
    
    
