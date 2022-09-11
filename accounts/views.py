from django.shortcuts import render, get_object_or_404
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Profile
from .forms import ProfileEditForm, SocialsEditForm, AvatarEditForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect


# Account Utils
def go_back(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def get_user_profile(request, username):
    user = Profile.objects.get(username=username)
    form = ProfileEditForm
    social_form = SocialsEditForm
    avatar_form = AvatarEditForm
    return render(request, 'profile.html',
                  {"duser": user, 'form': form, 'social_form': social_form, 'avatar_form': avatar_form})


# For seperate edit profile page
# def get_user_profile_edit(request, username):
#     user = Profile.objects.get(username=username)
#     return render(request, 'edit_profile.html', {"duser":user})


def edit_user_social(request, username):
    form = SocialsEditForm(request.POST)
    req_user = request.user
    user = get_object_or_404(Profile, username=username)

    print('User:', user)
    print('Username:', username)

    if user.user != req_user:
        return JsonResponse('Error! User is not same as account', safe=False)

    # if user is guest:
    if not user.user.is_authenticated:
        return JsonResponse('User is guest', safe=False)
    if form.is_valid():
        data = form.cleaned_data
        for field, value in data.items():
            if value:
                exec(f'user.{field} = "{value}"')
                user.save()

    return go_back(request)


def edit_user_profile(request, username):
    form = ProfileEditForm(request.POST)
    req_user = request.user
    user = get_object_or_404(Profile, username=username)

    if user.user != req_user:
        return JsonResponse('Error! User is not same as account', safe=False)

    # if user is guest:
    if not user.user.is_authenticated:
        return JsonResponse('User is guest', safe=False)
    if form.is_valid():
        data = form.cleaned_data
        print(data)
        for field, value in data.items():
            if value:
                exec(f'user.{field} = "{value}"')
                user.save()

    else:
        print('Form Ain\'t valid')

    return go_back(request)


def edit_user_avatar(request, username):
    form = AvatarEditForm(request.POST, request.FILES)
    req_user = request.user
    user = get_object_or_404(Profile, username=username)

    if user.user != req_user:
        return JsonResponse('Error! User is not same as account', safe=False)

    # if user is guest:
    if not user.user.is_authenticated:
        return JsonResponse('User is guest', safe=False)

    if form.is_valid():
        data = form.cleaned_data
        avatar = data['avatar']

        user.avatar = avatar
        user.save()
        if avatar != 'static_media/user.png':
            typ = str(avatar.name).split('.')[-1]
            avatar.name = (username + '.' + typ).lower()
            # print('Avatar:', str(avatar.name))
            # print('Data Chunk:', avatar.chunks)
        # filename = username
        # with open('.media/avatars/')

    return go_back(request)
