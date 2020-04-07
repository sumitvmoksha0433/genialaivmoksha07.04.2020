from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm,\
                   UserEditForm,ProfileEditForm,PersonForm
from .models import Profile,Country,State,City,Location,Person
from django.views.generic import ListView,CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
def site_ranking(request):
    return render(request,'account/siteranking.html')

def summary(request):
    data = request.user
    #userdata=User.objects.all(instance=request.user)
    data=User.objects.get(username__exact=data)
    data1=Profile.objects.get(user__exact=data)
    return render(request,
                  'account/summary.html',
                  {'data': data,'data1': data1,})

class LocationListView(ListView):
    model = Person
    context_object_name = 'people'


class LocationCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


class LocationUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')

def load_state1(request):
    country_id = request.GET.get('country')
    state = State.objects.filter(id=country_id).order_by('state')
    return render(request, 'account/states.html', {'state': state})

def load_state(request):
    inputData = request.GET.get('data')
    type = request.GET.get('type')
    responseData = None
    if type == "country" :
         responseData = State.objects.filter(country_id=inputData).order_by('state')
         print("states ", responseData)
         return render(request, 'account/states.html', {'data': responseData})
    elif type == "state" :
         responseData = City.objects.filter(state_id=inputData).order_by('city')
         print("cities ", responseData)
         return render(request, 'account/cities.html', {'data': responseData})
    elif type == "city" :
         responseData = Location.objects.filter(city_id=inputData).order_by('location')
         print("locations " ,  responseData)
         return render(request, 'account/locations.html', {'data': responseData})
    else:
        return render(request, 'account/states.html')


