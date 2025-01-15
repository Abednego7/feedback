from django import forms
from .models import Review

# Primera forma de crear un formulario:
"""
class ReviewForm(forms.Form):
    # error_messages: pair -> key:value
    # key: nombre del atributo html
    # value: mensaje de error personalizado
    user_name = forms.CharField(
        label="Your name",
        max_length=100,
        error_messages={
            "required": "Your name must not be empty!",
            "max_length": "Please enter a shorter name!",
        },
    )

    review_text = forms.CharField(
        label="Your Feedback", widget=forms.Textarea, max_length=200
    )

    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
"""


# Segunda forma de crear un formulario, basado en mi modelo:
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # Puedes usar solo los campos que deseas, usando una lista:
        # fields = ["user_name", "review_text"]

        # Tambien se podria usar exclude para listar los que no se incluiran:
        # exclude = ["owner_comment"]

        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating",
        }

        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!",
            }
        }
