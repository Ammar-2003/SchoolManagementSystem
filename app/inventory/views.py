from django.shortcuts import render
from django.views import View
class InventoryView(View): 
    def get(self,request):
        return render(request, 'inventory.html') 