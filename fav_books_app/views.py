from fav_books_app.models import Book
from django.shortcuts import redirect, render
from login.models import User
from django.contrib import messages

# Create your views here.
def book(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        Book.objects.all()
        context={"User_name":User.objects.get(id=request.session.get('user_id')).first_name,
        "logged_user":User.objects.get(id=request.session.get('user_id')),
        "all_books":Book.objects.all()
        }
        return render(request,'success.html',context)

def add_book(request):
    errors = Book.objects.book_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/books')
    else:
        this_user=User.objects.get(id=request.session.get('user_id'))
        this_book=Book.objects.create(title=request.POST['title'],description=request.POST['description'],uploaded_by=this_user)
        this_book.add_to_fav_by.add(this_user)
        return redirect('/books')

def view_books(request,id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context={"User_name":User.objects.get(id=request.session.get('user_id')).first_name,
        "view_book":Book.objects.get(id=id),
        "logged_user":User.objects.get(id=request.session.get('user_id'))}
        return render (request,'book_details.html',context)

def add_to_fav(request,id,_from=0):
    this_user=User.objects.get(id=request.session.get('user_id'))
    this_book=Book.objects.get(id=id)
    this_book.add_to_fav_by.add(this_user)
    if _from==1:
        return redirect(f'/books/{id}')
    else:
        return redirect('/books')

    

def update_delete(request,id):
    
    if request.method== "POST":
        if 'delete_book' in request.POST:
            Book.objects.get(id=id).delete()
            return redirect('/books')
        errors = Book.objects.book_validator(request.POST)
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect(f'/books/{id}')
        else:
            if 'update_book' in request.POST:
                this_book=Book.objects.get(id=id)
                if this_book.title != request.POST['title']:
                    this_book.title = request.POST['title']
                    this_book.save()
                if this_book.description != request.POST['description']:
                    this_book.description = request.POST['description']
                    this_book.save()
                return redirect(f'/books/{id}')

def remove_from_fav(request,id):
    this_user=User.objects.get(id=request.session.get('user_id'))
    this_book=Book.objects.get(id=id)
    this_book.add_to_fav_by.remove(this_user)
    return redirect(f'/books/{id}')

def view_fav(request):
    context={"User_name":User.objects.get(id=request.session.get('user_id')).first_name,
        "logged_user":User.objects.get(id=request.session.get('user_id'))
        }
    return render(request,'all_fav.html',context)
    
    
    


