from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Points_purchase
from adminpage.models import PointsStatus
from points.models import PurchaseRequest

# Create your views here.
def points(request):
  user_points_status = PointsStatus.objects.filter(user=request.user).first()
  available_points = user_points_status.total_points - user_points_status.used_points
  print(available_points)
  if request.method == 'POST':
      selected_option = request.POST.get('option_select') #num
      selected_option_info = Points_purchase.objects.filter(num=selected_option).first()
      print(selected_option_info.price)
      if available_points < selected_option_info.price:
        print('if')
        messages.error(request, '포인트가 부족합니다 :(')
        return redirect('points:points-page')
      else:
        PurchaseRequest.objects.create(user=request.user, purchase_option_id=selected_option)
        return redirect('points:points-page')
  else:
    context = dict()
    products = Points_purchase.objects.order_by('num')
    context['products'] = products
    context['available_points'] = available_points

  return render(request, 'points/points.html', context=context)

def points_info(request):
  return render(request, 'points/points_info.html')
