from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from blog.models import Post
from forms import BlogForm

# Create your views here.
def index(request):
	# get the blog posts that are published
	posts = Post.objects.filter(published=True)
	# now return the rendered template
	return render(request, 'blog/index.html', {'posts': posts})
     
def post(request, slug):
	# get the Post object
	post = get_object_or_404(Post, slug=slug)
	# now return the rendered template
	return render(request, 'blog/post.html', {'post': post})

def new_post(request):
	if request.method == 'POST':
		print request
		# create a form instance and populate it with data from the request
		form = BlogForm(request.POST)
		# check if it is valid
		if form.is_valid():
			# process data and redirect to a new URL
			title = form.cleaned_data['title']
			description = form.cleaned_data['description']
			content = form.cleaned_data['content']
			new = Post(title=title, content=content, description=description,
						published=form['published'], slug=slugify(unicode(title)))
			new.save()
			return HttpResponseRedirect('/blog/')
	# GET or other methods, create a blank form
	else:
		print "GET HERE"
		form = BlogForm()
		print form
	return render(request, 'blog/new.html', {'form': form})