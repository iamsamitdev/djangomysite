from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Import the Post model
from .models import Post

# สร้างฟังก์ชันสำหรับแสดงโพสต์ทั้งหมด
def post_list(request):

    # สร้างตัวแปร posts เก็บโพสต์ทั้งหมดที่มีสถานะเผยแพร่
    posts = Post.published.all() # ใช้โมเดล Post และ Manager published

    # สร้างตัวแปรกำหนดจำนวนโพสต์ที่แสดงต่อหน้า
    per_page = 5
    paginator = Paginator(posts, per_page)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # ส่งค่าตัวแปร posts ไปแสดงผลที่เทมเพลต blog/post/list.html
    return render(request, 'blog/post/list.html', {'posts': posts})


# สร้างฟังก์ชันสำหรับแสดงโพสต์แต่ละโพสต์
def post_detail(request, id):
    # สร้างตัวแปร post เก็บโพสต์ที่มี id ตามที่ระบุ
    post = Post.published.get(id=id) # ใช้โมเดล Post และ Manager published

    # ส่งค่าตัวแปร post ไปแสดงผลที่เทมเพลต blog/post/detail.html
    return render(request, 'blog/post/detail.html', {'post': post})