from django.shortcuts import render, redirect
from .models import Subject, StudyRecord
from datetime import timedelta

def top(request):
    subject_list = Subject.objects.values_list("name", flat=True)
    if request.method == "POST" and "new_subject" in request.POST:
        new_subject = request.POST.get("new_subject", "").strip()
        if new_subject and not Subject.objects.filter(name=new_subject).exists():
            Subject.objects.create(name=new_subject)
        return redirect("top")
    return render(request, "index.html", {"subject_list": subject_list})

def form(request):
    if request.method == "POST":
        content = request.POST["content"]
        selected_subject = request.POST.get("selected_subject", "未選択")
        elapsed_time_str = request.POST.get("elapsed_time", "00:00:00")
        hours, minutes, seconds = map(int, elapsed_time_str.split(':'))
        elapsed_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        StudyRecord.objects.create(
            subject=selected_subject,
            comment=content,
            elapsed_time=elapsed_time
        )
    
    # 新しい順に並べ替え
    records = StudyRecord.objects.all().order_by('-created_at')
    
    return render(request, "record/form.html", {"records": records})
