from django.shortcuts import render, redirect,get_object_or_404, redirect
from .forms import SigninForm, LoginForm, ExpenseForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

#- Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm


from django.utils import timezone
# Create your views here.
from .models import Expense, Profile


def homepage(request):
	return render(request, 'acc/index.html')

def register(request):
	form = SigninForm()
	if request.method == "POST":
		form = SigninForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("my login")
	else:
		form = SigninForm()

	context = {'registerform':form}
	return render(request, 'acc/register.html', context=context)

def my_login(request):
	form = LoginForm()
	
	if request.method == 'POST':
		form = LoginForm(request, data=request.POST)
		
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			
			if user is not None:
				auth.login(request, user)
				return redirect("expense_list", status='draft')

	context = {'loginform':form}
	return render(request, 'acc/my-login.html', context=context)

@login_required(login_url="my login")
def profile(request):

	return render(request, 'acc/profile.html')

@login_required(login_url="my login")
def profile_update(request):
	if request.method=='POST':
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
		if user_form.is_valid and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect("profile")
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)

		
	context = {
			'user_form':user_form,
			'profile_form':profile_form,
	}

	return render(request, 'acc/profile_update.html', context)

@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update the session to prevent the user from being logged out
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')  # Redirect to the profile or any other desired page
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        # Perform account deletion logic
        user = request.user
        user.delete()
        messages.success(request, 'Account deleted successfully!')
        return redirect('user-logout')  # Redirect to the logout view after deletion
    return render(request, 'delete_account.html')

@login_required(login_url="my login")
def dashboard(request):
	user_expenses = Expense.objects.filter(user=request.user)
	return render(request, 'acc/dashboard.html', {'user_expenses': user_expenses})

def user_logout(request):
	auth.logout(request)
	return redirect("")


#expense views

@login_required(login_url="my login")
def expense_list(request, status='draft'):
    # Filter expenses based on the logged-in user and the specified status
    expenses = Expense.objects.filter(user=request.user, status=status)
    return render(request, 'acc/expense_list.html', {'expenses': expenses, 'status': status})

@login_required(login_url="my login")
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Set the user to the logged-in user
            expense.save()
            return redirect('expense_list', status='draft')
    else:
        form = ExpenseForm()
    context = {'expenseform': form}
    return render(request, 'acc/add_expense.html', context=context)

@login_required(login_url="my login")
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    
    # Check if the expense belongs to the logged-in user
    if expense.user != request.user:
        return render(request, 'acc/error.html', {'error_message': 'Permission denied'})

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list', status='draft')
    else:
        form = ExpenseForm(instance=expense)
    context = {'expenseform': form}
    return render(request, 'acc/edit_expense.html', context=context)

@login_required(login_url="my login")
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    # Check if the expense belongs to the logged-in user
    if expense.user != request.user:
        return render(request, 'acc/error.html', {'error_message': 'Permission denied'})

    if request.method == 'POST':
        # Instead of deleting, set the status to "trash"
        expense.status = 'trash'
        expense.save()
        messages.success(request, 'Record moved to trash successfully!')
        return redirect('expense_list', status='draft')

    return render(request, 'acc/delete_expense.html', {'expense': expense})

@login_required(login_url="my login")
def restore_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    # Check if the expense belongs to the logged-in user
    if expense.user != request.user:
        return render(request, 'acc/error.html', {'error_message': 'Permission denied'})

    if request.method == 'POST':
        # Restore the expense by setting the status back to "draft"
        expense.status = 'draft'
        expense.save()
        messages.success(request, 'Record restored successfully!')
        return redirect('expense_list', status='trash')

    return render(request, 'acc/restore_expense.html', {'expense': expense})

@login_required(login_url="my login")
def permanently_delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    # Check if the expense belongs to the logged-in user
    if expense.user != request.user:
        return render(request, 'acc/error.html', {'error_message': 'Permission denied'})

    if request.method == 'POST':
        # Permanently delete the expense
        expense.delete()
        messages.success(request, 'Record permanently deleted successfully!')
        return redirect('expense_list', status='draft')

    return render(request, 'acc/permanently_delete_expense.html', {'expense': expense})