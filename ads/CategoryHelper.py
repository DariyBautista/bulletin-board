# Переносимо CATEGORY_TO_SUBCATEGORIES в окремий клас
from .models import Ad

class CategoryHelper:
    CATEGORY_TO_SUBCATEGORIES = {
        Ad.Category.HOUSEHOLD: [
            Ad.Subcategory.FRIDGES,
            Ad.Subcategory.WASHING_MACHINES,
            Ad.Subcategory.BOILERS,
            Ad.Subcategory.OVENS,
            Ad.Subcategory.HOODS,
            Ad.Subcategory.MICROWAVES,
        ],
        Ad.Category.COMPUTER: [
            Ad.Subcategory.PC,
            Ad.Subcategory.LAPTOPS,
            Ad.Subcategory.MONITORS,
            Ad.Subcategory.PRINTERS,
            Ad.Subcategory.SCANNERS,
        ],
        Ad.Category.SMARTPHONES: [
            Ad.Subcategory.ANDROID,
            Ad.Subcategory.IOS,
        ],
        Ad.Category.OTHER: [
            Ad.Subcategory.CLOTHES,
            Ad.Subcategory.SHOES,
            Ad.Subcategory.ACCESSORIES,
            Ad.Subcategory.SPORT,
            Ad.Subcategory.TOYS,
        ]
    }

    @classmethod
    def get_subcategories_for_category(cls, category):
        if category in cls.CATEGORY_TO_SUBCATEGORIES:
            return cls.CATEGORY_TO_SUBCATEGORIES[category]
        return []

    @classmethod
    def get_subcategory_choices(cls, category):
        allowed_subs = cls.get_subcategories_for_category(category)
        return [(key, label) for key, label in Ad.Subcategory.choices if key in allowed_subs]
