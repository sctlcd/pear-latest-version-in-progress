from django.shortcuts import render


# Pearl views
def handler403(request, exception):
    """
        Error Handler 403 - Forbidden access
    """
    return render(request, 'error_403.html', status=403)


def handler404(request, exception):
    """
        Error Handler 404 - Page Not Found
    """
    return render(request, 'error_404.html', status=404)


def handler500(request):
    """
        Error Handler 500 - Internal Server Error
    """
    return render(request, 'error_500.html', status=500)
