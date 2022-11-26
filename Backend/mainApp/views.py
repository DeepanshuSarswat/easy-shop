from rest_framework.response import Response
from rest_framework.views import APIView
from .repository import DukanCreationUtils

# Create your views here.


class CreateOrGetDukaanAPI(APIView):

    def get(self,request,*args,**kwargs):
        print(request.user)
        print(request.user.is_authenticated)
        try:
            if request.user.is_authenticated:
                return DukanCreationUtils().list_dukaan(request)
            return Response({'status':403,'message':'Please Authenticate Yourself to list dukaans.'})
        except Exception as e:
            return Response({'status':500,'message':str(e)})

    def post(self,request,*args,**kwargs):
        try:
            if request.user.is_authenticated:
                return DukanCreationUtils().create_dukaan(request)
            return Response({'status':403,'message':'Please Authenticate Yourself to create dukaan.'})
        except Exception as e:
            return Response({'status':500,'message':str(e)})



class ProductAPI(APIView):
    # list product for shop
    def get(self,request,*args,**kwargs):
        pass

    # create product for shop
    def post(self,request,*args,**kwargs):
        pass