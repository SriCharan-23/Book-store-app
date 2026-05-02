"""
Seed script to populate the database with sample books.
Run this directly or it will be called on FastAPI startup.
"""

from database import engine, SessionLocal, Base
from models import Book


SAMPLE_BOOKS = [
    # ── Self-Help ──
    {
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "price": 14.99,
        "category": "Self-Help",
        "cover_image": "/static/images/self_help_1.webp",
        "description": "A guide to spiritual enlightenment that shows you how to live in the present moment and break free from the pain-body.",
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "price": 16.99,
        "category": "Self-Help",
        "cover_image": "/static/images/self_help_2.webp",
        "description": "Tiny changes, remarkable results. A proven framework for improving every day through the compound effect of small habits.",
    },
    {
        "title": "Mindset: The New Psychology",
        "author": "Carol S. Dweck",
        "price": 13.49,
        "category": "Self-Help",
        "cover_image": "/static/images/self_help_3.webp",
        "description": "Discover how a simple idea about the brain can create a love of learning and a resilience essential for great accomplishment.",
    },
    {
        "title": "The Subtle Art of Not Caring",
        "author": "Mark Manson",
        "price": 15.99,
        "category": "Self-Help",
        "cover_image": "/static/images/self_help_4.webp",
        "description": "A counterintuitive approach to living a good life by choosing what truly matters and letting go of the rest.",
    },
    # ── Devotional ──
    {
        "title": "Jesus Calling",
        "author": "Sarah Young",
        "price": 12.99,
        "category": "Devotional",
        "cover_image": "/static/images/devotional_1.webp",
        "description": "A devotional filled with uniquely personal treasures from heaven that speak to your heart and draw you closer to God.",
    },
    {
        "title": "My Utmost for His Highest",
        "author": "Oswald Chambers",
        "price": 11.49,
        "category": "Devotional",
        "cover_image": "/static/images/devotional_2.webp",
        "description": "Classic daily devotional readings that have inspired millions to a deeper relationship with God for over a century.",
    },
    {
        "title": "The Daily Stoic",
        "author": "Ryan Holiday",
        "price": 14.49,
        "category": "Devotional",
        "cover_image": "/static/images/devotional_3.svg",
        "description": "366 meditations on wisdom, perseverance, and the art of living drawn from the ancient Stoic philosophers.",
    },
    {
        "title": "Streams in the Desert",
        "author": "L.B. Cowman",
        "price": 10.99,
        "category": "Devotional",
        "cover_image": "/static/images/devotional_4.svg",
        "description": "A beloved devotional classic offering daily meditations that bring comfort and spiritual renewal.",
    },
    # ── Business ──
    {
        "title": "Zero to One",
        "author": "Peter Thiel",
        "price": 18.99,
        "category": "Business",
        "cover_image": "/static/images/business_1.svg",
        "description": "Notes on startups, or how to build the future. Every moment in business happens only once.",
    },
    {
        "title": "The Lean Startup",
        "author": "Eric Ries",
        "price": 17.49,
        "category": "Business",
        "cover_image": "/static/images/business_2.svg",
        "description": "A new approach to business that's being adopted around the world, changing the way companies are built.",
    },
    {
        "title": "Good to Great",
        "author": "Jim Collins",
        "price": 19.99,
        "category": "Business",
        "cover_image": "/static/images/business_3.svg",
        "description": "Why some companies make the leap to greatness and others don't — based on a rigorous five-year research project.",
    },
    {
        "title": "Think and Grow Rich",
        "author": "Napoleon Hill",
        "price": 12.99,
        "category": "Business",
        "cover_image": "/static/images/business_4.svg",
        "description": "The timeless classic on turning desire into fortune, based on Andrew Carnegie's secret formula for success.",
    },
    # ── Education ──
    {
        "title": "Sapiens: A Brief History",
        "author": "Yuval Noah Harari",
        "price": 16.99,
        "category": "Education",
        "cover_image": "/static/images/education_1.svg",
        "description": "A groundbreaking narrative of humanity's creation and evolution that explores how biology and history have defined us.",
    },
    {
        "title": "Cosmos",
        "author": "Carl Sagan",
        "price": 15.49,
        "category": "Education",
        "cover_image": "/static/images/education_2.svg",
        "description": "A sweeping exploration of the universe, its origin, and the story of human discovery across the cosmos.",
    },
    {
        "title": "A Short History of Everything",
        "author": "Bill Bryson",
        "price": 14.99,
        "category": "Education",
        "cover_image": "/static/images/education_3.svg",
        "description": "An illuminating, witty journey through science — from the Big Bang to the rise of civilization.",
    },
    {
        "title": "Educated: A Memoir",
        "author": "Tara Westover",
        "price": 13.99,
        "category": "Education",
        "cover_image": "/static/images/education_4.svg",
        "description": "A memoir about the transformative power of education and the struggle to reconcile love for family with self-invention.",
    },
]


def seed_database():
    """Populate the database with sample books if it's empty."""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        existing_count = db.query(Book).count()
        if existing_count == 0:
            for book_data in SAMPLE_BOOKS:
                book = Book(**book_data)
                db.add(book)
            db.commit()
            print(f"[OK] Seeded {len(SAMPLE_BOOKS)} books into the database.")
        else:
            print(f"[INFO] Database already has {existing_count} books. Skipping seed.")
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
