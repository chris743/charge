from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import date

def RenderPDF(request, model, template_name):
        template_path = template_name
        Query = model.objects.all()
        today = date.today()
        modelname = model.objects.model._meta.db_table
        context = {'items': Query, 'date': today, 'model': modelname}
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response


