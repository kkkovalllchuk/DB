from django.core.management import call_command
from django.http import HttpResponse


def fill_data(request):
    try:
        call_command('fill_data')
        return HttpResponse('Data succsesfully filled to ZNO DB table')
    except Exception as e:
        return HttpResponse('Error while filling data into ZNO DB table data', status=500)

def delete_data(request):
    try:
        call_command('delete_data')
        return HttpResponse('All data succsesfully deleted from ZNO DB table')
    except Exception as e:
        return HttpResponse('Error while deleting all data into ZNO DB table data', status=500)