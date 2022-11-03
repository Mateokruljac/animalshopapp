from django.urls import path 
from . import views 

urlpatterns = [
    #core url 
    path("",views.store,name = "store"),
    path("cart", views.cart,name = "cart"),
    path("checkout", views.checkout, name = "checkout"),
    
    #animal based urls
    path("animal-create",views.create_animal,name = "animal-create"),
    path("animal-update/<animalID>",views.update_animal, name = "animal-update"),
    path("animal-detail/<animalID>",views.detail_animal,name = "animal-detail"),
    path("animal-about/<animalID>",views.about_animal, name = "animal-about"),
    path("animal-delete/<animalID>",views.delete_animal, name = "animal-delete"),
    
    #category based urls
    path("category-list",views.category_list,name = "category_list"),
    path("category-create",views.category_create,name = "category_create"),
    path("category-update/<categoryID>",views.category_update, name = "category_update"),
    path("category-delete/<categoryID>",views.category_delete,name = "category_delete"),
    path("animals-by-category/<categoryID>",views.animals_by_category,name = "animals_by_category"),
   
    #tag based urls
    path("tag-list",views.tag_list,name = "tag_list"),
    path("tag-create",views.tag_create,name = "tag_create"),
    path("tag-update/<tagID>",views.tag_update, name = "tag_update"),
    path("tag-delete/<tagID>",views.tag_delete,name = "tag_delete"),
    path("animals-by-tag/<tagID>",views.animals_by_tag,name = "animals_by_tag"),
    
    #comment based urls
    path("create-comment/<product_id>",views.create_comment,name = "create_comment"),
    path("update-comment/<product_id>/<comment_id>",views.update_comment,name = "update_comment"),
    path("delete-comment/<product_id>/<comment_id>",views.delete_comment,name = "delete_comment"),
    
    
    #search
    path("search",views.search,name = "search"),
    
    #likes
    path("likes/<animalID>",views.likes,name = "likes")
    
]
