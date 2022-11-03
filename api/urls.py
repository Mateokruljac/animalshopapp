from importlib.resources import path
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

# from rest_framework import permissions
# from drf_yasg import openapi

# ...

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

# urlpatterns = [
#    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#    ...
# ]
urlpatterns = [
    #animals api
    path("animal-list",views.animal_list_or_create,name = "api-animal-list"),
    path("animal-detail/<animal_id>",views.animal_detail,name = "api-animal-detail"),
    
    #comments api
    path("comment-list/<animal_id>",views.comments_list_or_create, name = "api-comment-list"),
    path("comment-detail/<comment_id>",views.comment_detail,name = "api-comment-detail"),
    
    #tag api 
    path("tag-list",views.tag_create_or_list, name = "api-tag-list"),
    path("tag-detail/<tag_id>",views.tag_detail,name = "api-tag-detail"),
    
    #category api
    path("category-list",views.category_list_or_create,name = "api-category-list"),
    path("category-detail/<category_id>",views.category_detail,name = "api-category-detail"),
    
    #register user
    path("register",views.registration_api,name = "register-api"),
    
    #log in user
    path("login",views.login_api,name = "login-api")
]

urlpatterns = format_suffix_patterns(urlpatterns)