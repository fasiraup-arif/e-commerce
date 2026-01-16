import random
from django.core.management.base import BaseCommand
from store.models import Product

class Command(BaseCommand):
    help = "Seed database with 100 products"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()  # optional: clear old products

        product_names = [
            "Wireless Headphones", "Smart Watch", "Bluetooth Speaker",
            "Laptop Bag", "Gaming Mouse", "Mechanical Keyboard",
            "Power Bank", "USB Charger", "LED Monitor",
            "Mobile Phone", "Tablet", "Web Camera",
            "Office Chair", "Running Shoes", "Backpack",
            "Sunglasses", "Fitness Band", "Smart TV",
            "Coffee Maker", "Air Fryer"
        ]

        for i in range(1, 101):
            title = random.choice(product_names) + f" {i}"
            price = random.randint(500, 5000)
            discount_price = None

            if random.choice([True, False]):
                discount_price = price - random.randint(50, 300)

            Product.objects.create(
                title=title,
                description=f"High quality {title} with best performance.",
                price=price,
                discount_price=discount_price,
                image=f"https://picsum.photos/seed/product{i}/600/600",
                stock=random.randint(5, 50),
                is_active=True
            )

        self.stdout.write(self.style.SUCCESS("✅ 100 products created successfully"))
