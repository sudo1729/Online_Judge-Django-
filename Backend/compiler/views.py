'''Imports for Api '''

from compiler.models import Compiler
from compiler.serializers import CompilerSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


'''Imports to Run code'''
import subprocess
import os
import sys
from pathlib import Path
import secrets
import string
import json




'''Imports for compilers'''
from compiler.python_compiler import executePythonCode
from compiler.cpp_compiler import executeCppCode




class CompilerList(APIView):
    """
    List all Compilers, or create a new Compiler.
    """
    def get(self, request, format=None):
        Compilers = Compiler.objects.all()
        serializer = CompilerSerializer(Compilers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompilerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            #print(data)
            if(data['language'] == 'Python'):
                result = executePythonCode(data)
                #print(result)
                # ans = json.dumps(result)
            else:
                result = executeCppCode(data)
                #print(result)
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompilerDetail(APIView):
    """
    Retrieve, update or delete a Compiler instance.
    """
    def get_object(self, pk):
        try:
            return Compiler.objects.get(pk=pk)
        except Compiler.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Compiler = self.get_object(pk)
        serializer = CompilerSerializer(Compiler)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Compiler = self.get_object(pk)
        serializer = CompilerSerializer(Compiler, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Compiler = self.get_object(pk)
        Compiler.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)