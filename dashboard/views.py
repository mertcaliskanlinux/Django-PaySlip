from django.shortcuts import render
from .models import Staff
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def index(request):
    staff = Staff.objects.all()
    context = {'staff':staff,}

    return render(request,'dashboard/index.html',context)


def payslip(request,pk):
    staff = Staff.objects.get(id=pk)
    template_path = 'dashboard/staff_payslip.html'
    context = {'staff':staff,}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


