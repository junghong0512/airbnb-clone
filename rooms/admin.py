from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Defintion """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("room_type", "guest", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {"classes": ("collapse",), "fields": ("amenity", "facility", "house_rule")},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guest",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "name",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "city",
        "room_type",
        "amenity",
        "facility",
        "house_rule",
        "country",
    )

    search_fields = (
        "^city",
        "^host__username",
        "name",
    )

    filter_horizontal = (
        "amenity",
        "facility",
        "house_rule",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
