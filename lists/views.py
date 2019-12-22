from django.shortcuts import redirect,render
from django.contrib.auth import get_user_model
from lists.models import Item,List
from lists.forms import ExistingListItemForm, ItemForm, NewListForm
User = get_user_model()


def home_page(request):
    return render(request, 'home.html',
    {
        'form':ItemForm()
    })

def finish_task(request, item_id):
    item_updated = Item.objects.get(id=item_id)
    item_updated.is_finish = True
    item_updated.save()
    list_ = List.objects.get(item=item_updated)
    return redirect(list_)

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
    	'list': list_, "form": form
    })


def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})
