from django.http import HttpResponsePermanentRedirect

class LowercaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lowercase_path = request.path_info.lower()
        
        if request.path_info != lowercase_path:
            return HttpResponsePermanentRedirect(lowercase_path)

        return self.get_response(request)
