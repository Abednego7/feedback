from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Para trabajar con clases
from django.views import View

# Para trabajar con un caso especifico de devolver una template como el caso de ThankYou
from django.views.generic.base import TemplateView

# Para trabajar con listas que deben ser renderizadas
from django.views.generic import ListView, DetailView

# Facilita y acorta el uso de respuestas de form como View
from django.views.generic.edit import FormView

# Una especie de FormView mas especializado:
# El cual nos ahorra el guardar datos y inclusive evitar crear forms.py
from django.views.generic.edit import CreateView


from .forms import ReviewForm
from .models import Review


# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # Esta funcion se uso con todo lo de arriba pero, heredando de FormView:
    # Las propiedades de arriba, se usaron mas esta funcion de abajo, menos la propieda de 'model'
    # la propiedad de model se uso con CreateView
    """
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    """

    # Antes se uso View en el class, con el metodo de abajo:
    """
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {"form": form})
    """


"""
def review(request):

    # post: devuelve un diccionario, el cual contien un par clave-valor;
    #        donde la key es el name de input y el value, el valor ingresado.

    if request.method == "POST":

        # Tercer agumento: instance, para actualizar

        # existing_data = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance=existing_data)

        form = ReviewForm(request.POST)

        if form.is_valid():
            # METODO 1: Usando un form personalizado:
            # cleaned_data: diccionario con datos limpiados.

            # review = Review(
            #    user_name=form.cleaned_data["user_name"],
            #    review_text=form.cleaned_data["review_text"],
            #    rating=form.cleaned_data["rating"],
            # )

            # review.save()

            # METODO 2: Usando ModelForm:
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {"form": form})

"""


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # Filter Query
    # def get_queryset(self):
    #    base_query = super().get_queryset()
    #    data = base_query.filter(rating__gt=4)
    #    return data

    # Metodo con TemplateView:
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context
    """


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        # Se hace un cambio de tipo porque favorite_id viene de un input y es tratado como str
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        context["review"] = selected_review
        return context
    """


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # con session que ya viene incluido, se pueden consultar y agregar datos
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
