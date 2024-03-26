from django.shortcuts import render

# Create your views here.
#def is't a function called post_list that takes request and will return 
# the value it gests from calling another function render that will render 
# (put toguether) our template blogs/post_list.html

def post_list(request):
    return render(request, 'blog/post_list.html', {})