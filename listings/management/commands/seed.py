from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **options):
        sample_listings = [
            {
                'title': 'Beachfront Villa',
                'description': 'A beautiful villa with ocean views.',
                'price_per_night': 250.00,
                'location': 'Agadir',
            },
            {
                'title': 'Mountain Cabin',
                'description': 'Cozy cabin surrounded by nature.',
                'price_per_night': 150.00,
                'location': 'Ifrane',
            },
            {
                'title': 'City Apartment',
                'description': 'Modern apartment in the heart of Casablanca.',
                'price_per_night': 180.00,
                'location': 'Casablanca',
            },
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully! 🌱'))
