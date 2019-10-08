from django.shortcuts import redirect,render
from lists.models import Item,List

# Create your views here.

def personal_comment(items):
	personal_comment = ''

	if len(items) == 0: 
		personal_comment = 'yey, waktunya berlibur'
	elif len(items) < 5:	
		personal_comment = 'sibuk tapi santai'
	else:
		personal_comment = 'oh tidak'

	return personal_comment	

def home_page(request):
	return render(request, 'home.html')

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'],list=list_)
	return redirect('/lists/the-only-list-in-the-world')

def view_list(request):
	items = Item.objects.all()
	return render(request, 'home.html', {'items': items	})
