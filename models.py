"""
SQLAlchemy models for the Book E-Commerce application.
"""

from sqlalchemy import Column, Integer, String, Float, Text
from database import Base


class Book(Base):
    """Represents a book available in the store."""

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(50), nullable=False, index=True)
    cover_image = Column(String(300), nullable=False)
    description = Column(Text, nullable=True)

    def to_dict(self):
        """Serialize book to dictionary for JSON responses."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "category": self.category,
            "cover_image": self.cover_image,
            "description": self.description,
        }
