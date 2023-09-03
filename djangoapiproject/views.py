from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Home page request")
    friends=[
        'Raj',
        'Pawan',
        'Rishikesh'
    ]
    return JsonResponse(friends, safe=False)

    