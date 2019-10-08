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

def add_item(request,list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect(f'/lists/{list_.id}/')

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'],list=list_)
	return redirect('/lists/{list_.id}/')

def view_list(request,list_id):
	list_ = List.objects.get(id=list_id)
	return render(request, 'list.html', {'list': list_	})
