import datetime
from django.contrib import messages
from django.shortcuts import redirect, render

# local imports
from .models import Leave
from .forms import LeaveForm

# Create your views here.

def get_number_of_days(start, end):
    days = abs((end-start)).days+1

    # fetch all dates between start day and end date
    all_dates = [start + datetime.timedelta(days=x) for x in range(days)]

    # use the datetime weekday() method to determine if the days fall on a weekend 
    weekdays = [date for date in all_dates if not date.weekday() in [5,6]]
    return len(weekdays)


def index(request):
    title = "Welcome to leave Management App"
    ctx = {
        "title": title
        
    }
    return render(request, 'index.html', ctx)

def fetch_all_leaves(request):
    all_leave = Leave.fetch_all_data()
    ctx = {
        "all_leave":all_leave
    }

    return render(request, 'leave.html', ctx)


def fetch_leave_details(request, id):
    leave_details = Leave.fetch_single_data(id)

    ctx = {
        "leave_details": leave_details
    }

    return render(request, 'leave_details.html', ctx)


def requet_new_leave(request):
    # add form funtionality here
    errors = None
    if request.method == 'POST':
        # create form instance and populate with data from htmls forms 
        form = LeaveForm(request.POST)
        # validate the inputs
        if form.is_valid():
            # form.commit(False)
            data = form.save(commit=False)
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            days = get_number_of_days(start_date, end_date)
            data.requested_days = days
            print("90900", data.requested_days)
            data.save()
            return redirect('leaves')

        errors = form.errors

    # instantiate empty form
    form = LeaveForm()
    ctx={
        'form': form,
        'errors': errors
    }
    return render(request, 'request_leave.html', ctx)


def  edit_leave_request(request, id):
    leave = Leave.fetch_single_data(id)
    form = LeaveForm(request.POST or None, instance=leave)
    if form.is_valid():
            data = form.save(commit=False)
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            days = get_number_of_days(start_date, end_date)
            data.requested_days = days
            form.save()
            return redirect('leave-details', leave.id)

    ctx ={
        "form": form,
        "id": id
    }
    return render(request, 'leave_details_edit.html', ctx)

def delete_leave_request(request, id):
    deleted = Leave.delete_single_data(id)
    print('deleted', deleted)
    return redirect('leaves')
