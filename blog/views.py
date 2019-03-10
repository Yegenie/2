from django.shortcuts import render, redirect , get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost

# Create your views here.

def home(request):
    blogs = Blog.objects #쿼리셋 #메소드 #기능을표시
    blog_list = Blog.objects.all() #블로그 모든 글을 대상으로
    paginator = Paginator(blog_list, 3) # 세글을 한페이지에보기
    page = request.GET.get('page') #request된 페이지가 뭔지 알아내고 (즉,변수에담아내고)
    posts = paginator.get_page(page)#request된 페이지를 얻어온 뒤 return 해준다
    return render(request, 'home.html' , {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def post(request):
    return render(request, 'post.html')

def create(request): #입력받은 내용을 데베에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) # redirect: 위에 사항 모두를 처리한 뒤 다음 주소로 이동

def blogpost(request):
    # 1. 입력된 내용을 처리 
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=Flase)
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog') 
    # 2. 빈 페이지를 띄워줌
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})