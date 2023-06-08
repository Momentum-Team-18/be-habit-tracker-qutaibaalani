from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitRecord, User
from .forms import HabitForm, HabitRecordForm


# Create your views here.
def homePage(request):
    habits = Habit.objects.all()
    habitRecords = HabitRecord.objects.all()
    context = {"habits": habits, "habitRecords": habitRecords}
    return render(request, "habit_tracker/index.html", context)


def newHabit(request):
    form = HabitForm()
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect("homePage")
    return render(request, "habit_tracker/habit_form.html", {"form": form})


def newRecord(request, pk):
    form = HabitRecordForm()
    # habitRecords = HabitRecord.objects.all()
    habit = get_object_or_404(Habit, id=pk)

    context = {"form": form, "habit": habit}
    if request.method == "POST":
        form = HabitRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()

            return redirect("habitDetails", pk)
    return render(request, "habit_tracker/record_form.html", context)


def editRecord(request, pk):
    record = get_object_or_404(HabitRecord, pk=pk)
    habit_pk = record.habit_id

    if request.method == "POST":
        form = HabitRecordForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect("habitDetails", habit_pk)
    else:
        form = HabitRecordForm(instance=record)
    return render(request, "habit_tracker/record_form.html", {"form": form})


def deleteRecord(request, pk):
    record = get_object_or_404(HabitRecord, pk=pk)
    habit_pk = record.habit_id
    record.delete()
    return redirect("habitDetails", habit_pk)


def habitDetails(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    context = {"habit": habit}

    return render(request, "habit_tracker/habitDetails.html", context)
