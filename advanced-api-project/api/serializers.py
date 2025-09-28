#NEW
from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer): # serializer for the book model
    class Meta:
        model = Book
        fields = '__all__' #this serializes all fields without needing to mention them individually
        
        def validate_publication_year(self, data):
            """ensuring the date is not in the future 
            This method is called automatically during serializer validation."""
            current_year = datetime.date.today().year
            if data > current_year:
                raise serializers.ValidationError("Publication year cannot be in the future.")
            return data
        
# Serializer for the Author model.
# It includes:
#   - The author's name.
#   - A nested list of the author's books, serialized using BookSerializer.        
class AuthorSerializer(serializers.ModelSerializer): #serializer for the Author model
    class Meta:
        book = BookSerializer(many=True, read_only=True)
        
        model = Author
        fields = ['name', 'books']  # 'fields' defines the fields that will be included in the serialized output.
        
        """Notes:
    - The `books` field relies on the reverse relationship defined in the Book model.
      Ensure the `Book` model's foreign key to `Author` uses `related_name='books'`
      or leave it as default (Django will use the lowercase name of the model, i.e., 'book').
    """
    # Relationship handling:
# The Author model and Book model have a one-to-many relationship via ForeignKey.
# In AuthorSerializer, the 'books' field uses the related_name from the Book model ('books').
# This allows serialization of all books associated with a given author directly inside the author's serialized data.