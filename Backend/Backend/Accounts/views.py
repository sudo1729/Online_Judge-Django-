from Accounts.models import User
from Accounts.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# User CRUD operation

class UserList(APIView):

    def get_object(self, userName):
        try:
            return User.objects.get(userName=userName)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, userName,password, format=None):
        user = self.get_object(userName)
        serializer = UserSerializer(user)
        data = serializer.data
        if(data['password'] == password):
            return Response({'detail':"Found"})
        else:
            return Response({"detail":"Not Found"})
        return Response("hello")

    def post(self, request, format=None):
        data = request.data
        # print(data)
        # if('email' not in data or 'userName' not in data or 'password' not in 'data'):
        #     return Response({'detail':"Trying to be smart huh!!!"})
        try:
            user = User.objects.get(userName=str(data['userName']))
            return Response({'detail':"Already Registered"})
        except:
            try:
                user = User.objects.get(email = data['email'])
                return Response({'detail':"Already Registered"})
            except:
                serializer = UserSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    # return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response({'detail':"Successfully created"})
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, userName, format=None):
        user = self.get_object(userName)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 


# userCode
