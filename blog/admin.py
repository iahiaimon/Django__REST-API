from django.contrib import admin
from .models import CustomUser, Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "username", "created_at")
    list_filter = ("username", "created_at")
    search_fields = ("title", "content")
    raw_id_fields = ("username",) 

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = CustomUser.objects.all()
            print("Users in dropdown:", kwargs["queryset"]) 
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
