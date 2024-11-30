from django.shortcuts import render
from .models import EndOfDayReport
from django.utils.dateparse import parse_date

def daily_report_view(request):
    selected_date = request.GET.get('date')
    report = None

    # Tarih geçerli mi diye kontrol ediyoruz
    if selected_date:
        parsed_date = parse_date(selected_date)
        if parsed_date:
            report = EndOfDayReport.objects.filter(date=parsed_date).first()  # Seçilen tarihe ait raporu al
        else:
            report = None  # Geçerli bir tarih girilmezse rapor bulunamadı olarak ayarla

    context = {
        'report': report,
        'selected_date': selected_date,
    }
    return render(request, 'end_of_day/daily_report.html', context)
