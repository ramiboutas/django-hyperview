from django.http import HttpResponse


def hv_reponde(response: HttpResponse):
    response.headers["content-type"] = "application/vnd.hyperview+xml"
    return response
