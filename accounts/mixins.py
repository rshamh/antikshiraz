from django.http import Http404


class SuperUserRequiredMixin():
    """Verify that the current user is Superuser."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404