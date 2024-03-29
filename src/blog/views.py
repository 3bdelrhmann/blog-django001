from django.shortcuts import render,get_object_or_404
from .models import *
from .forms import *
def home(request):

	context = {
		'title' : 'الصفحة الرئيسية',
		'posts' : Post.objects.all()
	}
	return render(request,'blog/index.html',context)

def about(request):
	return render(request,'blog/about.html',{'title' : 'من انا'})


def post_detail(request,post_id):
	post = get_object_or_404(Post,pk = post_id)
	comments = post.comments.filter(active=True)

	if request.method == 'POST':
		comment_form = Newcomment(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
			comment_form = Newcomment()
	else:
		comment_form = Newcomment()

	context = {
		'title' : post.title,
		'post'  : post,
		'comments' : comments,
		'comment_form' : comment_form,
	}

	return render(request,'blog/detail.html',context)