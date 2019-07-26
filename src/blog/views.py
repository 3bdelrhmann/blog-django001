from django.shortcuts import render

posts = [
	{
		'title' : 'first blog',
		'content' : 'lorem ipsum lorem ipsum lorem ipsum lorem ipsum ',
		'date':'15-3-2019',
		'author' : 'ahmed'

	},
	{
		'title' : 'second blog',
		'content' : '21 ipsum lorem ipsum lorem ipsum lorem ipsum ',
		'date':'19-3-2019',
		'author' : 'ali'

	},
	{
		'title' : 'thirt blog',
		'content' : '19 lorem ipsum lorem ipsum lorem ipsum lorem ipsum ',
		'date':'18-3-2019',
		'author' : 'mohamed'

	},
	{
		'title' : 'fourth blog',
		'content' : 'iiilorem ipsum lorem ipsum lorem ipsum lorem ipsum ',
		'date':'16-3-2019',
		'author' : 'omar'

	},
]
def home(request):

	context = {
		'title' : 'الصفحة الرئيسية',
		'posts' : posts
	}
	return render(request,'blog/index.html',context)

def about(request):
	return render(request,'blog/about.html',{'title' : 'من انا'})