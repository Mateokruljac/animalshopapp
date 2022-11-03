from django.contrib import admin
from pets.models import Animal, Category, Tag, Status, Comments

# Register your models here.
admin.site.register(Animal)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Status)
admin.site.register(Comments)