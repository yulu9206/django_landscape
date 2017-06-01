from django.shortcuts import render, redirect
def index(request):
	return render(request, 'land/index.html')
def show(request, num):
	num = int(num)
	type = ''
	if num < 10:
		type = '/static/land/images/snow.jpg'
	elif num < 20:
		type = '/static/land/images/desert.jpg'
	elif num < 30:
		type = '/static/land/images/forest.jpg'
	elif num < 40:
		type = '/static/land/images/vineyard.jpg'
	elif num < 50:
		type = '/static/land/images/tropical.jpg'
	else:
		return redirect('/')
	context = {
	'type': type
	}
	return render(request, 'land/show.html', context)