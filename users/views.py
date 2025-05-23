from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads'] = self.request.user.ads.all()
        return context
