from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return HttpResponse('<html><title>Homepage</title><body> <h1>Muhammad Riansyah Tohamba<h1></body></html>')
