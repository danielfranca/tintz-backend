from api.views import BaseApiView, SerializerFactory
from email_marketing.models import Subscriber

# Create your views here.
class SubscriberApi(BaseApiView):
    """
    Endpoint to add subscriber
    """
    model = Subscriber
    serializer_class = SerializerFactory(model)
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
