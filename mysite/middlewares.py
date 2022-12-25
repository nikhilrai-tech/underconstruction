from django.shortcuts import render
class mysitemidd:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("i am midd before view")
        response=render(request,"cons.html")
        print("i am midd after view")
        return response
