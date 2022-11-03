from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from pets.models import Animal, Comments, Tag, Category
from api.serializers import AnimalSerializer, CommentSerializer, TagSerializer,CategorySerializer, RegistrationSerializer,LoginSerializer
import datetime 

# Create your views here.

@api_view(["GET","POST"])
def animal_list_or_create(request,format = None):
    """ 
    List all animal, or create a new 
    """
    
    if request.method == "GET":
        animals = Animal.objects.all()
        seraializer = AnimalSerializer(animals, many = True)
        return Response(seraializer.data)
    
    elif request.method == "POST":
        serializer = AnimalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def animal_detail(request,animal_id,format = None):
    """ 
    Retrieve, update or delete animal
    """
    #check if animal at all exists!
    try:
        animal  = Animal.objects.get(id = animal_id)
    except Animal.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = AnimalSerializer(animal,many = False)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = AnimalSerializer(instance = animal,data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else: 
          return Response(status = status.HTTP_400_BAD_REQUEST)
      
    elif request.method == "DELETE":
        animal.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(["GET","POST"])
def comments_list_or_create(request, animal_id, format = None):
    """ 
    List all comments, or create a new 
    """
    if request.method == "GET":
        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)
   
    elif request.method == "POST":
        product = Animal.objects.get(id = animal_id)
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
@api_view(["GET","PUT","DELETE"])
def comment_detail(request, comment_id, format = None):
    """ 
    Retrieve, update or delete comment
    """
    #check if comment at all exists!
    try:
        comment = Comments.objects.get(id = comment_id)
    except Comments.DoesNotExist:
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    if request.method == "GET":
        serializer = CommentSerializer(comment, many = False)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = CommentSerializer(comment,data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        comment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(["GET","POST"])            
def tag_create_or_list (request,format = None):
    """ 
    List all tag, or create a new 
    """
    if request.method == "GET":
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = TagSerializer(data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

     
@api_view(["GET","PUT","DELETE"])
def tag_detail(request,tag_id,format = None):
    """ 
    Retrieve, update or delete tag
    """
    #check if tag at all exists!
    try:
        tag = Tag.objects.get(id = tag_id)
    except Tag.DoesNotExist:
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    if request.method == "GET":
        serailizer = TagSerializer(tag, many = False)
        return Response(serailizer.data, status = status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = TagSerializer(instance = tag, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        tag.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
@api_view(["GET","POST"])    
def category_list_or_create(request,format = None):
    """ 
    List all category, or create a new 
    """
   
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
def category_detail(request,category_id,format = None):
    """ 
    Retrieve, update or delete category
    """
    #check if category at all exists!
    try:
        category = Category.objects.get(id = category_id)
    except Category.DoesNotExist:
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    if request.method == "GET":
        serializer = CategorySerializer(category, many = False)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = CategorySerializer(category, data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    elif request.method == "DELETE":
        category.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def registration_api(request,format = None):
    
    if request.method == "POST":        
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.create()
            data["first_name"] = user.first_name
            data["last_name"] = user.last_name
            data["username"] = user.username
            data["email"] = user.email
            data["password"] = user.password
        else:
            data = serializer.errors
        
        return Response (data)
    

@api_view(["GET","POST"])
def login_api(request, format = None):
    if request.method == "GET":
        content = {"user" : str(request.user),"auth" : str(request.auth)}
        return Response(data = content, status = status.HTTP_200_OK)
    
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]
        
        if not username or not password:
            return Response({"msg":"Please fill all fields"}, status = status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(username = username)
        if not user.exists():
            return Response({"msg":"User does not exists!"},status= status.HTTP_400_BAD_REQUEST)
        
        return Response({"msg":"Successfully"},status= status.HTTP_200_OK)   
        
        
        