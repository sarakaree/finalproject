from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Review
from django.views.generic import  DetailView
from cart.forms import CartAddProductForm
from django.contrib import messages

# Create your views here.

def index(request):
    top_five_products = Product.objects.all()[:8]
    # showing only 6 categoires in menu bar 
    categories = Category.objects.all()[:6]
    products = Product.objects.all()
    return render(request,'bookshop/index.html',{'categories':categories,'products':products,'top_five_products':top_five_products})
    


    #total products display function
def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request,'bookshop/products_list.html',{'category':category,
                                                     'categories':categories,
                                                     'products':products})

    #single product vi

def product_detail(request, slug):
    product = get_object_or_404(Product,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    
    #getting product id for showing all review realted to one product
    reviewproduct = Product.objects.filter(slug=slug)
    prid = None
    for product_id in reviewproduct:
        prid = product_id.id

    all_reviews = Review.objects.filter(product=prid)
    
    return render(request,'bookshop/product_detail.html',{'product': product,'cart_product_form': cart_product_form,'all_reviews':all_reviews})

def all_Categories(request):
    categories = Category.objects.all()
    return render(request,'bookshop/all_category_list.html',{'categories':categories})



def contact_us(request):
    return render(request,'bookshop/contact_us.html')


def aboutus(request):
    return render(request,'bookshop/aboutus.html')
    debug_message = 'This is the debug message.'
    context = {'debug_message': debug_message}
    return render(request, 'aboutus.html', context)



from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from bookshop.forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshop/add_book.html', {'form': form})



# def add_book(request):
#     if request.method == 'POST':
#         # Process the submitted form data and save the book
#         # Ensure the user is authenticated and their role is either 'Author' or 'Publishing House'
#         if request.user.role in ['Author', 'Publishing House']:
#             # Process the form data and save the book
#             # Code to handle adding a book goes here
#             return redirect('books_list')  # Redirect to the book list page
#         else:
#             return redirect('unauthorized')  # Redirect to unauthorized access page

#     return render(request, 'add_book.html')
















def search_Result(request):
    if request.method== 'POST':
        searh_query = request.POST['search']
        query_result = Product.objects.filter(name__startswith=searh_query)
        return render(request,'bookshop/search.html',{'query_result':query_result,'searh_query':searh_query})


#review 
def Comment_Review(request,product_id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        rating = request.POST['rating']
        review_comment = request.POST['review']
        product = get_object_or_404(Product,id=product_id)
        comment_review = Review.objects.create(product=product,name=name,email=email,rating=rating,review_comment=review_comment)
        message = messages.success(request,"Your reviews is submitted")
        
        return render(request,'bookshop/product_detail.html')
    
    return render(request,'bookshop/product_detail.html')