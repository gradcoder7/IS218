from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Feedback
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    feedbacks = product.feedbacks.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.product = product
            feedback.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = FeedbackForm()
    return render(request, 'products/product_detail.html', {'product': product, 'form': form, 'feedbacks': feedbacks})

@login_required
def feedback_report(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'reports/feedback_report.html', {'feedbacks': feedbacks})

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')
