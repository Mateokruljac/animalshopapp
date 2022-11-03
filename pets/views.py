from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from pets.forms import CommentForm
from pets.forms import CategoryForm,TagForm,AnimalForms,AnimalForms
from pets.models import Animal, Category, Tag, Comments
from members.models import Order
from .utils import cart_total_quantity
# Create your views here.

"""                                                                                   CORE                                                                                                """
def store (request):
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    items = context["items"]
    animals = Animal.objects.all().order_by("name")
    return render (request,"core/store.html",{"animals":animals,"cart_items":cart_items,"items":items})


def cart (request):
    context = cart_total_quantity(request)
    items = context["items"]
    order = context["order"]
    cart_items = context["cart_items"]
    return render (request,"core/cart.html",{"items":items,"order":order,"cart_items":cart_items})

#checkout view 
def checkout (request):
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    items = context["items"]
    order = context["order"]
    
    return render (request,"core/checkout.html",{"items":items,"order":order,"cart_items":cart_items})


########################################################################################################################################################################################################
"""                                                                             Animal CRUD operations                                                                                """

def create_animal(request):
    """ 
    This view enable registered user create a new post, etc. add new animal
    """
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    items = context["items"]
    order = context["order"]
    
    submitted = False
    if request.method == "POST":
        form = AnimalForms(request.POST,request.FILES)
        if form.is_valid():
            pre_save = form.save(commit = False)
            pre_save.owner = request.user
            pre_save.save()
            form.save_m2m()
            return HttpResponseRedirect("/animal-create?submitted=True")
        else:
            messages.info(request,"Something went wrong!Please, try again!")
            return render (request,"animal/animal_create.html",{"form":form,"cart_items":cart_items,"items":items,"order":order})
    else:
        form = AnimalForms()
        if "submitted" in request.GET:
            submitted = True 
        return render (request,"animal/animal_create.html",{"form":form,"submitted":submitted,"cart_items":cart_items})


def update_animal(request,animalID):
    """ 
    This view enable user who has created this post that can update if want 
    """
    updated = False
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    
    if request.method == "POST":
        animal = Animal.objects.get(pk = animalID)
        form = AnimalForms(request.POST or None,instance = animal)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/animal-update/{animalID}?updated=True")
        else:
            messages.info("Something went wrong.Please, try again!")
            return render (request,"animal/animal_create.html",{"form":form,"cart_items":cart_items})
                   
    else:
        animal = Animal.objects.get(pk = animalID)
        form = AnimalForms(instance = animal)
        if "updated" in request.GET:
            updated = True
        
        return render(request,"animal/animal_update.html",{"updated":updated,"form":form,"cart_items":cart_items})


#like animal
def likes (request,animalID):
    like = False
    if request.method == "POST":
        animal = get_object_or_404(Animal,pk = animalID)
        print("Animl",animalID)
        if animal.likes.filter(id = request.user.id).exists():
            animal.likes.remove(request.user)
            like = False
            return HttpResponseRedirect(reverse("animal-detail",args=([str(animalID)])))
        else:
            animal.likes.add(request.user)
            like = True            
        
        return HttpResponseRedirect(reverse("animal-detail",args=([str(animalID)])))
    else:
        return HttpResponseRedirect(reverse("animal-detail",args=([str(animalID)])))


def detail_animal(request,animalID):
    """ 
    This view enable that user can see more about product/animal    
    """
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    animal = Animal.objects.get(pk = animalID)
    
    #list and count comments
    comments = Comments.objects.filter(animal = animal)
    count_comments = 0
    for _ in comments:
        count_comments +=1
    
    return render (request,"animal/animal_detail.html",{"animal":animal,"cart_items":cart_items,"comments":comments,"count_comments":count_comments})

def about_animal(request,animalID):
    animal = Animal.objects.get(id = animalID)
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    return render(request,"animal/animal_about.html",{"animal":animal,"cart_items":cart_items})    

def delete_animal(request,animalID):
    try: 
        animal = Animal.objects.get(pk = animalID)
        animal.delete()
        return redirect ("store")
    except animal.DoesNotExist:
        return redirect ("store")

######################################################################################################################################################################################
"""                                                                           Categories - CRUD operations                                                              """

def category_list(request):
    """ 
    This view returns list of category
    """
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    categories = Category.objects.all()
    return render (request,"category/category_list.html",{"categories":categories,"cart_items":cart_items})


def category_create(request):
    """ 
    This view enable you to create a new category
    """
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    created = False 
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid(): 
            form = form.save(commit = False)
            form.owner = request.user
            form.save()
            return HttpResponseRedirect("category-create?created=True")
        else:
            messages.info(request,"Something went wrong!")
            return render (request,"category/category_create.html",{"form":form,"cart_items":cart_items})
    else:
        form = CategoryForm()
        if "created" in request.GET:
            created = True
        return render (request,"category/category_create.html",{"form":form,"created":created,"cart_items":cart_items})

def category_update(request,categoryID):
    """ 
    This view enable you to update a view if you are a creator
    """
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    updated = False 
    if request.method == "POST":
        category = Category.objects.get(pk = categoryID)
        form =CategoryForm(request.POST,instance = category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/category-update/{categoryID}?updated=True")
        else:
            messages.info(request,"Something went wrong!")
            return render (request,"category/category_update.html",{"form":form,"category":category,"cart_items":cart_items})
    
    else:
        category = Category.objects.get(pk = categoryID)
        form = CategoryForm(instance = category)
        if "updated" in request.GET: 
            updated = True 
        return render (request,"category/category_update.html",{"form":form,"updated":updated,"category":category,"cart_items":cart_items})

def category_delete(reqeust,categoryID):
    """ 
    This view enable you to delete deisred category if you are a creator 
    """
    try: 
        category = Category.objects.get(pk = categoryID)
        category.delete()
        return redirect("category_list")
    except category.DoesNotExist:
        return redirect("category_list")

def animals_by_category(request,categoryID):
    category = Category.objects.get(id = categoryID)
    animals = Animal.objects.filter(species = category)
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    return render (request,"category/get_animal.html",{"animals":animals,"category":category,"cart_items":cart_items})    

###############################################################################################################################################################################################################
"""                                                                             Tag - CRUD operations                                                                   """



def tag_list(request):
    """ 
    This view returns list of tags
    """
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    tags = Tag.objects.all()
    return render (request,"tag/tag_list.html",{"tags":tags,"cart_items":cart_items})


def tag_create(request):
    """ 
    This view enable you to create a new tag
    """
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    created = False 
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid(): 
            form = form.save(commit = False)
            form.owner = request.user
            form.save()
            return HttpResponseRedirect("tag-create?created=True")
        else:
            messages.info(request,"Something went wrong!")
            return render (request,"tag/tag_create.html",{"form":form,"cart_items":cart_items})
    else:
        form = TagForm()
        if "created" in request.GET:
            created = True
        return render (request,"tag/tag_create.html",{"form":form,"created":created,"cart_items":cart_items})

def tag_update(request,tagID):
    """ 
    This view enable you to update a view if you are a creator
    """
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    updated = False 
    if request.method == "POST":
        tag = Tag.objects.get(pk = tagID)
        form = TagForm(request.POST,instance = tag)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/tag-update/{tagID}?updated=True")
        else:
            messages.info(request,"Something went wrong!")
            return render (request,"tag/tag_update.html",{"form":form,"tag":tag,"cart_items":cart_items})
    
    else:
        tag = Tag.objects.get(pk = tagID)
        form = TagForm(instance = tag)
        if "updated" in request.GET: 
            updated = True 
        return render (request,"tag/tag_update.html",{"form":form,"updated":updated,"tag":tag,"cart_items":cart_items})

def tag_delete(reqeust,tagID):
    """ 
    This view enable you to delete deisred tag if you are a creator 
    """
    try: 
        tag = Tag.objects.get(pk =  tagID)
        tag.delete()
        return redirect("tag_list")
    except tag.DoesNotExist:
        return redirect("tag_list")
    

def animals_by_tag(request,tagID):
    tag = Tag.objects.get(id = tagID)
    animals = Animal.objects.filter(tag = tag)
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    return render (request,"tag/get_animal.html",{"animals":animals,"tag":tag,"cart_items":cart_items})    
    
#####################################################################################################################################################################################     
"""                                                                                        SEARCH PANEL                                                                        """


def search(request):
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    
    if request.method == "POST":
        searched = request.POST.get("search")
        print(searched)
        animals = Animal.objects.filter(name__contains = searched.title())
        return render (request,"core/search.html",{"animals":animals,"cart_items":cart_items})
    
        
    else:
        return render (request,"core/search.html",{"cart_items":cart_items})
    
    
#################################################################################################################################################################################################
"""                                                                       Comments CRUD                                                                                         """


def create_comment(request,product_id):
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    product = Animal.objects.get(id = product_id)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
           form = form.save(commit = False)
           form.animal = product
           form.owner = request.user
           form.save()
           return HttpResponseRedirect(reverse("animal-detail",args = ([str(product_id)])))   
    else:
        form = CommentForm()
        return render (request,"comment/comment_create.html",{"form":form,"cart_items":cart_items})


def update_comment(request,product_id,comment_id):
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    
    if request.method == "POST":
        comment = Comments.objects.get(id = comment_id)
        form = CommentForm(request.POST,instance = comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("animal-detail",args = ([str(product_id)])))
    else:
        comment = Comments.objects.get(id = comment_id)
        form = CommentForm(instance = comment)
        return render (request,"comment/comment_update.html",{"form":form,"cart_items":cart_items})

def delete_comment(request,product_id,comment_id):
    comment = Comments.objects.get(id = comment_id)
    try:
        comment.delete()
    except comment.DoesNotExist:
        pass
    
    else: 
      return HttpResponseRedirect(reverse("animal-detail",args = ([str(product_id)])))

#######################################################################################################################################################################################