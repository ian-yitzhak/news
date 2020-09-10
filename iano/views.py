from django.shortcuts import render




from . models import Contact ,Post

from django.http import HttpResponse




def home(request):

    posts = Post.objects.all()




    if request.method =="POST":

       
        email = request.POST.get('email')
        
        subject = request.POST.get('subject')
       
        contact.email=email
        
        contact.subject=subject
        contact.save()

        return render( request , 'iano/contact.html')

    return render( request , 'iano/index.html'  , {'posts' : posts})








