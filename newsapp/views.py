import json
import random

from html_sanitizer import Sanitizer
from django.utils.datastructures import MultiValueDictKeyError
sanitizer = Sanitizer()

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *
from accounts.models import CustomUser


# Create your views here.
class HomeView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'all_article_list'


def home(request):
    all_articles = Article.objects.all()
    try:
        keyword = request.GET['s']
    except MultiValueDictKeyError:
        keyword = ''
    # print('Keyword:', keyword)
    if keyword:
        # countries = Country.objects.filter(name__icontains=keyword)
        # all_articles = Article.objects.filter(country__in=countries)
        all_articles = Article.objects.filter(title__icontains=keyword)
    context = {'all_article_list': all_articles}
    return render(request, 'index.html', context)


def post(request, slug):
    user = request.user
    article = get_object_or_404(Article, slug=slug)
    all_awards = Award.objects.all()
    in_featured = Article.objects.filter(country=article.country.id).exclude(slug=article.slug).order_by('-id')[:3]
    featured = Article.objects.exclude(country=article.country.id).order_by('-id')[:3-len(in_featured)]

    # Code to display user article choices on page
    articleVoteItems = article.get_votes
    article.selectYV = ''
    article.selectNV = ''

    for vi in articleVoteItems:
        if user.username == vi.voter.username:
            if vi.choice == 'yes':
                article.selectYV = 'selected'
            elif vi.choice == 'no':
                article.selectNV = 'selected'

    comments = article.comment.all()
    for comment in comments:
        contentbox = str(comment.content).split('\n')
        awards = comment.awards
        for awarditem in awards:
            pass

    # AI Voter
    difficulty = 1  # lowest at 0
    complexity = [1] + [0] * difficulty
    if random.choice(complexity):
        article.yes_vote += random.randint(0, 4)
        article.no_vote += random.randint(0, 4)
        article.save()

        for comment in comments:
            # print('Data:', comment.time_ago_data)
            comment.yes_vote += random.randint(0, 3)
            comment.no_vote += random.randint(0, 2)
            comment.save()
            replies = comment.reply.all()
            for reply in replies:
                reply.yes_vote += random.randint(0, 3)
                reply.no_vote += random.randint(0, 2)
                reply.save()

    context = {'article': article, 'all_awards': all_awards, 'featured': featured, 'in_featured': in_featured}
    return render(request, 'post_single.html', context)


@csrf_exempt
def updateArticleVote(request):
    user = request.user
    data = json.loads(request.body)
    slug = data['Slug']
    poll = data['Poll']

    article = Article.objects.get(slug=slug)

    def response():
        return JsonResponse('ArticleVote was updated!!', safe=False)
        # return JsonResponse({'y': article.yes_vote, 'n': article.no_vote})

    # if user is guest:
    if not user.is_authenticated:
        return JsonResponse('User is guest', safe=False)

    vote, created = VoteItem.objects.get_or_create(voter=user, parent='a', parent_id=article.id, article=article)

    # Add code to allow only one vote per user
    if created or vote.choice == '':

        if poll == 'yes':
            article.yes_vote += 1
            vote.choice = 'yes'
        elif poll == 'no':
            article.no_vote += 1
            vote.choice = 'no'

        article.save()
        vote.save()

        return response()

    else:
        if poll == vote.choice:

            # Remove Vote
            if poll == 'no':
                article.no_vote -= 1
                vote.choice = ''
            else:
                article.yes_vote -= 1
                vote.choice = ''

            article.save()
            vote.save()

            return response()

        elif poll == 'no':
            article.no_vote += 1
            article.yes_vote -= 1
            vote.choice = 'no'

        elif poll == 'yes':
            article.no_vote -= 1
            article.yes_vote += 1
            vote.choice = 'yes'

        article.save()
        vote.save()

        return response()


@csrf_exempt
def updateCommentVote(request):
    user = request.user
    data = json.loads(request.body)
    slug = data['Slug']
    poll = data['Poll']
    id = data['ID']

    article = get_object_or_404(Article, slug=slug)
    comment = get_object_or_404(article.comments, anon_id=id)

    # Handle guest users:
    if not user.is_authenticated:
        return JsonResponse('User is guest', safe=False)

    vote, created = VoteItem.objects.get_or_create(voter=user, parent='c', parent_id=comment.id, comment=comment)
    print(vote.choice)

    if created or vote.choice == '':
        if poll == 'yes':
            comment.yes_vote += 1
            vote.choice = 'yes'
        elif poll == 'no':
            comment.no_vote += 1
            vote.choice = 'no'

        comment.save()
        vote.save()
        return JsonResponse('CommentVote was updated!', safe=False)

    else:
        if poll == vote.choice:

            # Remove Vote
            if poll == 'no':
                comment.no_vote -= 1
                vote.choice = ''
            else:
                comment.yes_vote -= 1
                vote.choice = ''

            comment.save()
            vote.save()
            return JsonResponse('CommentVote is removed', safe=False)

        elif poll == 'no':
            comment.no_vote += 1
            comment.yes_vote -= 1
            vote.choice = 'no'

        elif poll == 'yes':
            comment.no_vote -= 1
            comment.yes_vote += 1
            vote.choice = 'yes'

        comment.save()
        vote.save()
        return JsonResponse(f'CommentVote was updated', safe=False)


@csrf_exempt
def updateReplyVote(request):
    user = request.user
    data = json.loads(request.body)
    slug = data['Slug']
    poll = data['Poll']
    comment_id = data['Comment ID']
    id = data['ID']

    article = get_object_or_404(Article, slug=slug)
    comment = get_object_or_404(article.comments, anon_id=comment_id)
    reply = get_object_or_404(comment.replies, anon_id=id)

    # if user is guest:
    if not user.is_authenticated:
        return JsonResponse('User is guest', safe=False)

    vote, created = VoteItem.objects.get_or_create(voter=user, parent='r', parent_id=reply.id, reply=reply)

    if created or vote.choice == '':

        if poll == 'yes':
            reply.yes_vote += 1
            vote.choice = 'yes'
        elif poll == 'no':
            reply.no_vote += 1
            vote.choice = 'no'

        reply.save()
        vote.save()
        return JsonResponse('Reply-Vote was updated!', safe=False)

    else:
        if poll == vote.choice:

            # Remove Vote
            if poll == 'no':
                reply.no_vote -= 1
                vote.choice = ''
            else:
                reply.yes_vote -= 1
                vote.choice = ''

            reply.save()
            vote.save()
            return JsonResponse('ReplyVote is removed', safe=False)

        elif poll == 'no':
            reply.no_vote += 1
            reply.yes_vote -= 1
            vote.choice = 'no'

        elif poll == 'yes':
            reply.no_vote -= 1
            reply.yes_vote += 1
            vote.choice = 'yes'

        reply.save()
        vote.save()
        return JsonResponse('Reply-Vote was updated!', safe=False)


def addComment(request, slug):
    form = CommentForm(request.POST)
    user = request.user

    # if user is guest:
    if not user.is_authenticated:
        return JsonResponse('User is guest', safe=False)
        # return HttpResponse("<script>alerT(e, 'Oops! You have to be logged in to vote', '#C94B0C');</script>")

    if form.is_valid():
        data = form.cleaned_data
        content = sanitizer.sanitize(data['content'])
        article = get_object_or_404(Article, slug=slug)
        comment = Comment(author=user, content=content)
        comment.yes_vote += 1
        comment.save()

        # Add user vote as an upvote
        voteitem = VoteItem(voter=user, parent='c', parent_id=comment.id, comment=comment, choice='yes')
        voteitem.save()
        article.comment.add(comment)
        article.save()

    else:
        print('Form ain\'t valid')
        return JsonResponse('Form ain\'t valid', safe=False)

    # return JsonResponse('Comment Received', safe=False)
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return go_back(request)
    # return HttpResponseRedirect(f'/post/{slug}')
    # return HttpResponse('<script>location.replace(document.referrer);</script>')


def addReply(request):
    form = ReplyForm(request.POST)
    user = request.user

    # if user is guest:
    if not user.is_authenticated:
        return JsonResponse('User is guest', safe=False)

    if form.is_valid():
        data = form.cleaned_data
        print(data)
        content = sanitizer.sanitize(data['content'])
        recipent = data['recipent']
        # verified_img = '<img src="/static/img/verify.png" class="verified text-center">'
        # content = f"<span style='color: #3932be'>@{recipent}</span> {content}"
        comment = data['comment']
        comment = get_object_or_404(Comment, anon_id=comment)
        reply = Reply(author=user, content=content, recipent=recipent)
        reply.yes_vote += 1
        reply.save()
        comment.reply.add(reply)
        comment.save()

        # Add user vote as an upvote
        voteitem = VoteItem(voter=user, parent='r', parent_id=reply.id, reply=reply, choice='yes')
        voteitem.save()
        print('Sub-Reply Added')


    else:
        print('Form ain\'t valid')

    return go_back(request)


def contact(request):
    form = ContactForm
    return render(request, 'contact.html', {'form': form})


def delete(request, type, id):
    user = request.user

    types = {'post': Article, 'comment': Comment, 'reply': Reply}
    in_type = types.get(type)

    if not in_type:
        return JsonResponse('Error with deletion', safe=False)

    i_object = get_object_or_404(in_type, anon_id=id)

    if i_object.author == user:
        if i_object.content == '--deleted--':
            i_object.delete()
        else:
            i_object.content = '--deleted--'
            i_object.save()

        # Pro feature
        # i_object.delete()
        return go_back(request)

    else:
        return JsonResponse('Error with deletion', safe=False)


@csrf_exempt
def gift(request):
    user = request.user
    data = json.loads(request.body)
    print('Data:', data)
    id = data['id']
    owner = data['owner']
    parent = data['parent']
    quantity = data['quantity']
    award_id = data['award']

    if id:
        awarditem = get_object_or_404(AwardItem, anon_id=id)
        if awarditem.quantity == 0:
            awarditem.delete()
        else:
            awarditem.quantity -= 1
            awarditem.save()
    award = get_object_or_404(Award, id=award_id)
    owner = get_object_or_404(CustomUser, username=owner)

    new_award, created = AwardItem.objects.get_or_create(owner=owner, award=award, parent_id=parent)
    print(created)
    new_award.get_anon_id()
    new_award.quantity += quantity
    new_award.save()

    return JsonResponse('Done', safe=False)


@csrf_exempt
def awardTransaction(request):
    user = request.user
    data = json.loads(request.body)
    print('Data:', data)
    status = data['status']
    email = data['email']
    award = data['award']
    price = data['price']

    award = get_object_or_404(Award, name=award)
    award_tf = AwardTransaction(award=award, status=status, email=email, price=price)
    award_tf.save()
    return JsonResponse(
        'Success', safe=False
    )


def country(request):
    countries = Country.objects.all()
    json_file = [""""import json file here"""]

    # for cont in json_file:
    # new_country = Country(name=cont['name'], capital=cont['capital'], code=cont['code'], continent=cont[''])

    # Country.objects.exclude(code="t1").delete()
    context = {'countries': countries, 'count': len(countries), 'choice': random.choice(countries)}
    return render(request, 'manage/country.html', context)


"""START PRODUCTS CATEGORY"""


def products(request):
    context = {}
    return render(request, 'products.html', context)
