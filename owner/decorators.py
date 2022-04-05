from django.shortcuts import redirect


def admin_sign_in_required(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return view(request, *args, **kwargs)
        else:
            return redirect("signin")
    return wrapper
