from django.shortcuts import render,redirect
from . models import*
from . forms import *
from django.views.generic import ListView,UpdateView,CreateView,DetailView,DeleteView
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def home(req):
    ha=ProductModel.objects.filter(category='Home Apliences')
    phone=ProductModel.objects.filter(category='Mobiles')
    sports=ProductModel.objects.filter(category='Sports')
    grocery=ProductModel.objects.filter(category='Grocery')
    furnishing=ProductModel.objects.filter(category='Furnishing')
    books=ProductModel.objects.filter(category='Books')
    beauty=ProductModel.objects.filter(category='Beauty')
    product_stock=InventoryModel.objects.all()
    b=''
    ser=req.GET.get('searchpro')
    print(ser)
    if ser:
        pro=ProductModel.objects.filter(name__icontains=ser)
        return render(req,'search_result.html',{'pro':pro})
    return render(req,'home-products.html',{'ha':ha,'phone':phone,'sports':sports,'grocery':grocery,'fur':furnishing,'books':books,'beauty':beauty})

def viewall(req):
    all=ProductModel.objects.filter(category='Home Apliences')
    return render(req,'viewall.html',{'all':all})

def AddProduct(req):
    if req.method=='POST':
        form=ProductForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect(AddProduct)
    else:
        form=ProductForm()
    return render(req,'add_product.html',{'form':form})

def AddCategory(req):
    if req.method=='POST':
        form=CategoryForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect('/app1/home')
    else:
        form=CategoryForm()
    return render(req,'add_category.html',{'form':form})

def AdminPage(req):
    return render(req,'admin_page.html')

def AllProducts(req):
    all=ProductModel.objects.all()
    return render(req,'all_products.html',{'all':all})


class EditProduct(UpdateView):
    model=ProductModel
    context_object_name='edit'
    template_name='edit_product.html'
    fields='__all__'
    success_url='/app1/home'


class DeleteProduct(DeleteView):
    model=ProductModel
    success_url='/app1/adminpage'
    template_name='delete_product.html'
    context_object_name='form'

def details(req,id):
    det=ProductModel.objects.get(id=id)
    off=AvailableOffers.objects.all()
    return render(req,'detail_page.html',{'det':det,'off':off})

def reg(req):
    if req.method=='POST':
        form=Regform(req.POST)
        a=form.data['username']
        if form.is_valid():
            form.save()
            return redirect(loginuser)
    else:
        form=Regform()
    return render(req,'registration.html',{'form':form})

def loginuser(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        user=authenticate(req,username=username,password=password)
        if user:
            login(req,user)
            return redirect(home)
    else: 
        print('login failed')
        redirect(reg)
    return render(req,'signup.html')
    
def logoutuser(req):
    logout(req)
    return redirect('/app1/login')

def UserProfile(req,id):
    a=ProfileModel.objects.get(id=id)
    return render(req,'profile.html',{'a':a})

# all_instances = ProfileModel.objects.all()
# for instance in all_instances:
#     print(instance.id)


class EditProfile(UpdateView):
    model=ProfileModel
    context_object_name='edit'
    template_name='edit-profile.html'
    fields='__all__'
    success_url='/app1/home'

class UserListView(ListView):
    model=User
    template_name='users-list.html'
    context_object_name='users'

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users-create.html'
    success_url='/app1/users'

# views.py

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users-delete.html'
    success_url = '/app1/users'

def kart(req,id):
    addr=ProfileModel.objects.get(id=id)
    total_price=0
    q_total=0
    kart_item=CartItem.objects.filter(user=req.user)
    
    for i in kart_item:
        total_price=total_price+i.price
    
    return render(req,'kart_page.html',{'addr':addr,'kart':kart_item,'total':total_price})

def add_to_cart(req,id,price,name,rating,offer):
    quantity=1
    product=CartItem.objects.create(user=req.user,price=price,name=name,rating=rating,offer=offer,quantity=quantity)
    product.save()
    return redirect('/app1/home')

def remove_from_cart(req,id):
    cart_item = CartItem.objects.get(pk=id)
    cart_item.delete()
    return redirect('/app1/home')


def AddInventory(req):
    if req.method=='POST':
        form=InventoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form=InventoryForm()
    return render(req,'add-inventory.html',{'form':form})

class InventoryListView(ListView):
    model=InventoryModel
    template_name='all-inventory.html'
    context_object_name='item'
    
from django.shortcuts import render, redirect
from .models import CartItem, InventoryModel

def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    for cart_item in cart_items:
        if cart_item.name is not None:
            cart_item_name = cart_item.name
            print(cart_item_name)

            try:
                inventory_item = InventoryModel.objects.get(product__name=cart_item_name)
                if inventory_item.quantity > 0:
                    inventory_item.quantity -= 1
                    inventory_item.save()
                    # order=OrdersModel(
                    #     name=name,
                    #     quantity=quantity,
                    #     price=price)
                    # order.save()
                    print('done')
                    c_item=CartItem.objects.all()
                    for x in c_item:
                        x.delete()


                else:
                    print(cart_item_name ,'not in stock')
            except InventoryModel.DoesNotExist:
                print(f'Inventory entry not found for item "{cart_item_name}"')
                messages.error(request, 'Selected item not in stock')
        else:
            print('CartItem has no associated product.')

    return redirect(home)
            
def DeliveryBoy(req):
    return render(req,'delivery-boy.html')

def DeliveryBoyList(req):
    deliver_boys=User.objects.all()
    return render(req,'delivery-boy-list.html',{'boys':deliver_boys})