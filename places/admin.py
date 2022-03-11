from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInLine(SortableInlineAdminMixin, admin.TabularInline):
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
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["__str__", "order", 'image', 'get_preview']
    fields = ["order", 'image', 'get_preview']
    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" width="200" />'
        )