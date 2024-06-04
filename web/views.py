from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.http import Http404

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = form.save()
            return redirect('success_page')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.Book.DoesNotExist:
        raise  Http404("Book Not Found")
    return render(request, "book_detail.html",{"book": book})


def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book Not Found")
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("success_page")
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'form': form})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('success_page')
    else:
        return render(request, 'delete_book_confirm.html', {'book': book} )