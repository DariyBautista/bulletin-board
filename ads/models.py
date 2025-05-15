from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Ad(models.Model):
    class Category(models.TextChoices):
        HOUSEHOLD = 'household', 'Побутова техніка'
        COMPUTER = 'computer', 'Комп\'ютерна техніка'
        SMARTPHONES = 'smartphones', 'Смартфони'
        OTHER = 'other', 'Інше'

    class Subcategory(models.TextChoices):
        # Household
        FRIDGES = 'fridges', 'Холодильники'
        WASHING_MACHINES = 'washing_machines', 'Пральні машини'
        BOILERS = 'boilers', 'Бойлери'
        OVENS = 'ovens', 'Печі'
        HOODS = 'hoods', 'Витяжки'
        MICROWAVES = 'microwaves', 'Мікрохвильові печі'

        # Computer
        PC = 'pc', 'ПК'
        LAPTOPS = 'laptops', 'Ноутбуки'
        MONITORS = 'monitors', 'Монітори'
        PRINTERS = 'printers', 'Принтери'
        SCANNERS = 'scanners', 'Сканери'

        # Smartphones
        ANDROID = 'android', 'Android смартфони'
        IOS = 'ios', 'iOS/Apple смартфони'

        # Other
        CLOTHES = 'clothes', 'Одяг'
        SHOES = 'shoes', 'Взуття'
        ACCESSORIES = 'accessories', 'Аксесуари'
        SPORT = 'sport', 'Спортивне обладнання'
        TOYS = 'toys', 'Іграшки'

    class Status(models.TextChoices):
        ACTIVE = 'active', 'Активне'
        INACTIVE = 'inactive', 'Неактивне'

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.CharField(
        max_length=20,
        choices=Category.choices
    )

    subcategory = models.CharField(
        max_length=30,
        choices=Subcategory.choices
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ACTIVE
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')

    def __str__(self):
        return self.title
