from django.core.exceptions import ValidationError
from django.shortcuts import redirect,render
from lists.models import Item,List

# Create your views here.

def personal_comment(items):
	personal_comment = ''

	if len(items) > 0 and len(items) < 5:	
		personal_comment = 'sibuk tapi santai'
	elif len(items) == 0:
		personal_comment = 'yey, waktunya berlibur'
	else:
		personal_comment = 'oh tidak'

	return personal_comment	

def home_page(request):
	return render(request, 'home.html',{'personal_comment' : 'yey, waktunya berlibur'})

def add_item(request,list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect(f'/lists/{list_.id}/')


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {
    	'list': list_, "form": form,'personal_comment': personal_comment(list_.item_set.all())
    	})


def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})


def share_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    list_.shared_with.add(request.POST['sharee'])
    return redirect(list_)

