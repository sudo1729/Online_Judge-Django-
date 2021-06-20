from rest_framework import serializers
from Compiler.models import Compiler


class CompilerSerializer(serializers.ModelSerializer):
    class Meta:
        mode = Compiler
        fields = ['id','slug','code','language','customInput','expectedOuput','output','verdict']
        