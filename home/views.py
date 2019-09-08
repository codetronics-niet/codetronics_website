from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """[summary]
    Simple home page view
    Arguments:
        TemplateView {[type]} -- [description]
    """
    template_name = 'home.html'
