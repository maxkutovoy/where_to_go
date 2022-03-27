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
            '<img src="{}" width="200" />',
            obj.image.url
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInLine,
    ]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['__str__', 'image', 'place', 'get_preview']
    fields = ['image', 'place', 'get_preview']
    readonly_fields = ('get_preview',)
    raw_id_fields = ('place',)
    autocomplete_fields = ('place', )

    def get_preview(self, obj):
        return format_html(
            '<img src="{}" width="200" />',
            obj.image.url
        )
