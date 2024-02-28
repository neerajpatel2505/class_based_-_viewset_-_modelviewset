from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.models import User
from .serializers import UserSerializer

# # Basic Class based API-----------------------------------------------------------
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class List(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = User.objects.all()
#         serializer = UserSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class Details(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = UserSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = UserSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# # mixins based API-------------------------------------------------


# from rest_framework import mixins
# from rest_framework import generics

# class List(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class Details(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

## Generic based API----------------------------------------------
# from rest_framework import generics


# class List(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class Details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

## ------------------------ViewSets-----------------------------------
# # During dispatch, the following attributes are available on the ViewSet.
# # basename - the base to use for the URL names that are created.
# # action - the name of the current action (e.g., list, create).
# # detail - boolean indicating if the current action is configured for a list or detail view.
# # suffix - the display suffix for the viewset type - mirrors the detail attribute.
# # name - the display name for the viewset. This argument is mutually exclusive to suffix.
# # description - the display description for the individual view of a viewset.


# from django.shortcuts import render
# from rest_framework.response import Response
# from .serializers import UserSerializer
# from rest_framework import status
# from rest_framework import viewsets


# class StudentViewSet(viewsets.ViewSet):
#     def list(self, request):
#         print("*********List***********")
#         print("Basename:", self.basename)
#         print("Action:", self.action)
#         print("Detail:", self.detail)
#         print("Suffix:", self.suffix)
#         print("Name:", self.name)
#         print("Description:", self.description)
#         stu = User.objects.all()
#         serializer = UserSerializer(stu, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         id = pk
#         if id is not None:
#             stu = User.objects.get(id=id)
#             serializer = UserSerializer(stu)
#             return Response(serializer.data)

#     def create(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self,request, pk):
#         id = pk
#         stu = User.objects.get(pk=id)
#         serializer = UserSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self,request, pk):
#         id = pk
#         stu = User.objects.get(pk=id)
#         serializer = UserSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated'})
#         return Response(serializer.errors)

#     def destroy(self,request, pk):
#         id = pk
#         stu = User.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})

## ModelViewSte------------------------------------------------------    
from rest_framework import viewsets
class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer