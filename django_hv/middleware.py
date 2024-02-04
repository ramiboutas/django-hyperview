from django.http import HttpRequest
from django.utils.functional import cached_property


class HyperviewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.hv = HyperviewDetails(request)
        return self.get_response(request)


class HyperviewDetails:
    def __init__(self, request: HttpRequest) -> None:
        self.request = request

    def __bool__(self):
        return self.is_hv

    @cached_property
    def is_hv(self):
        return "X-Hyperview-Version" in self.request.headers
