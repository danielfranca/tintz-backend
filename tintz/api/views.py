from rest_framework_drilldown import DrillDownAPIView
from rest_framework import mixins
from rest_framework import serializers
from django.shortcuts import get_object_or_404


def SerializerFactory(the_model):
    class Serializer(serializers.ModelSerializer):
        class Meta:
            model = the_model

    return Serializer


# Create your views here.
class BaseApiView(DrillDownAPIView, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    MAX_RESULTS = 5000

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get_base_query(self, *args, **kwargs):
        if 'pk' in kwargs:
            return self.model.objects.filter(pk=kwargs['pk']).all()
        else:
            return self.model.objects.all()

    def get_object(self):
        queryset = self.get_base_query()
        filter = {}
        self.multiple_lookup_fields = ['pk']
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj