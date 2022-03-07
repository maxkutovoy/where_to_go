from django.contrib import admin
from .models import Place, Image


class ImageInLine(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInLine,
    ]


admin.site.register(Image)
