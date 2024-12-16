from django.shortcuts import render, redirect
from .forms import RobotForm
from .models import Robot

def create_robot(request):
    if request.method == 'POST':
        form = RobotForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new robot to the database
            return redirect('robot_list')  # Redirect to a success page or a list view
    else:
        form = RobotForm()

    return render(request, 'robots/create_robot.html', {'form': form})

def robot_list(request):
    robots = Robot.objects.all()
    return render(request, 'robots/robot_list.html', {'robots': robots})
