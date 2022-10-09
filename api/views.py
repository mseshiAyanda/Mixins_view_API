from rest_framework.response import Response
from rest_framework import authentication, generics, mixins, permissions
from .serializers import ArticleSerializers

from .models import Article


class ArticleMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
   ):

   queryset = Article.objects.all()
   serializer_class = ArticleSerializers
   authentication_classes = [authentication.SessionAuthentication]
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   lookup_field = 'pk'

   def get(self, request, *args, **kwargs):
       print(args, kwargs)
       pk = kwargs.get("pk")
       if pk is not None:
            return self.retrieve(request, *args,**kwargs)
       return self.list(request, *args, **kwargs)

   def post(self, request, *args, **kwargs):
           return self.create(request, *args, **kwargs)

article_mixin_view = ArticleMixinView.as_view()