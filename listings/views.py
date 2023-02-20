from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import price_choices, states_choices, bedroom_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        "listings": paged_listings
    }
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        "listing" : listing
    }
    return render(request, "listings/listing.html", context)

def search(request):
    queryset_list = Listing.objects.order_by("-list_date").filter(is_published=True)
    #keyword
    if 'keywords' in request.GET:
        entered_keywords = request.GET['keywords']
        if entered_keywords:
            queryset_list = queryset_list.filter(description__icontains=entered_keywords)
    #city
    if 'city' in request.GET:
        entered_city = request.GET["city"]
        if entered_city:
            queryset_list = queryset_list.filter(city__iexact=entered_city)
    #state
    if 'state' in request.GET:
        entered_state = request.GET["state"]
        if entered_state:
            queryset_list = queryset_list.filter(state__iexact=entered_state)
    #bedrooms
    if 'bedrooms' in request.GET:
        entered_bedrooms = request.GET["bedrooms"]
        if entered_bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=entered_bedrooms)
    #price
    if 'price' in request.GET:
        entered_price = request.GET['price']
        if entered_price:
            queryset_list = queryset_list.filter(price__lte = entered_price)
    
    context = {
        "listings":queryset_list,
        "state_choices":states_choices,
        "bedroom_choices":bedroom_choices,
        "price_choices":price_choices,
        'values': request.GET
    }
    return render(request, "listings/search.html", context)
