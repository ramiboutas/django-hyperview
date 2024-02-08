from django.http import HttpResponse


def hv_repond(response: HttpResponse):
    response.headers["content-type"] = "application/vnd.hyperview+xml"
    return response


hv_reponde = hv_repond  # Calling this func 'hv_reponde' was a Typo. TODO: leave it as 'hv_repond' someday
