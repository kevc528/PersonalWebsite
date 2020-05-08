from django.shortcuts import render


# render the contacts page
def contact(request):
    return render(request, 'contact.html', {})
