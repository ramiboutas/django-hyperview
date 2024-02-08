from typing import Any
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.template.base import Template
from django.template.response import TemplateResponse


def hv_reponde(response: HttpResponse):
    response.headers["content-type"] = "application/vnd.hyperview+xml"
    return response


class HyperviewResponse(TemplateResponse):
    def __init__(
        self,
        request,
        template,
        context=None,
        status=None,
        charset=None,
        using=None,
        headers=None,
    ):
        super().__init__(
            request=request,
            template=template,
            context=context,
            content_type="application/vnd.hyperview+xml",
            status=status,
            charset=charset,
            using=using,
            headers=headers,
        )
