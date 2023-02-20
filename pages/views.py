from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, states_choices, bedroom_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3]
    context = {
        "listings": listings,
        "state_choices":states_choices,
        "bedroom_choices":bedroom_choices,
        "price_choices":price_choices,
        }
    return render(request, "pages/index.html", context)

def about(request):
    realtors = Realtor.objects.order_by("-hire_date")
    context = {
        "realtors" : realtors,
    }
    return render(request, template_name="pages/about.html", context=context)