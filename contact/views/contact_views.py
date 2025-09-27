from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[:10]

    context = {
        'contacts': contacts,
        'site_title': 'Contatos -'
    }
    

    return render(
        request,
        'contact/index.html',
        context,
    )

# https://docs.djangoproject.com/en/5.2/ref/models/querysets/#field-lookups

def search(request):
    serach_value = request.GET.get('q','').strip()
    
    if serach_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(frist_name__icontains=serach_value) |
            Q(last_name__icontains=serach_value) |
            Q(id__icontains=serach_value) |
            Q(phone__icontains=serach_value) |
            Q(email__icontains=serach_value) 
            )\
        .order_by('-id')
    # print(contacts.query)
    
    context = {
        'contacts': contacts,
        'site_title': 'Search -'
    }
    

    return render(
        request,
        'contact/index.html',
        context,
    )


def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact.objects, pk=contact_id, show=True)

    site_title = f'{single_contact.frist_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }
    

    return render(
        request,
        'contact/single_contact.html',
        context,
    )