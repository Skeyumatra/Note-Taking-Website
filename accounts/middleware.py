from django.shortcuts import redirect

class LogInMidlleware:
    def __init__(self,get_response):
        self.get_response=get_response
        self.exclude_paths=["/accounts/login/","/admin/","/accounts/register/"]
    
    def __call__(self, request):
        if not any(request.path.startswith(path) for path in self.exclude_paths):
            if not request.session.get("user_id"):
              if not request.session.get("user_id"):
                return redirect("/accounts/login/")
        response = self.get_response(request)
        return response