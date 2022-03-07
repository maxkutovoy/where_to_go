from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ("get_preview", )

    def get_preview(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" width="200" />'
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInLine,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'image', 'get_preview']
    fields = ["image_order", 'image', 'get_preview']
    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" width="200" />'
        )