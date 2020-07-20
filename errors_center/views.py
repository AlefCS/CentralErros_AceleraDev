from django.shortcuts import redirect


def redirect_root2docs(request):
    response = redirect("/api/docs/")

    return response
