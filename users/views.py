from rest_framework import viewsets
# from rest_framework import status
# from rest_framework.generics import RetrieveUpdateAPIView
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
from .serializers import (
    UserSerializer
)
from .models import User 

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()



# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserSerializer

#     def retrieve(self, request, *args, **kwargs):
#         # There is nothing to validate or save here. Instead, we just want the
#         # serializer to handle turning our `User` object into something that
#         # can be JSONified and sent to the client.
#         serializer = self.serializer_class(request.user)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         user_data = request.data.get('user', {})

#         serializer_data = {
#             # 'username': user_data.get('username', request.user.username),
#             # 'email': user_data.get('email', request.user.email),

#             'profile': {
#                 'bio': user_data.get('bio', request.user.profile.bio),
#                 'profile_pic': user_data.get('profile_pic', request.user.profile.profile_pic)
#             }
#         }

#         # Here is that serialize, validate, save pattern we talked about
#         # before.
#         serializer = self.serializer_class(
#             request.user, data=serializer_data, partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_200_OK)