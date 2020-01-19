from foodiedotcom.models import Restaurant, RestaurantExtraInfo
from .serializers import RestaurantSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import requests, csv
from django.db import connection


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@renderer_classes([TemplateHTMLRenderer])
def insert_data_func(request):
    sql_stmt1 = 'INSERT INTO tbl_restaurant_info (restaurant_id, restro_name, cuisines, avg_cost_for_two, currency, has_table_booking, has_online_delivery, rating, rating_color, rating_text, votes) values (%s)'
    sql_stmt2 = 'INSERT INTO tbl_restaurant_extra_info (restaurant_id, country_code, city, address, locality, locality_verbose, x, y) values (%s)'
    file_name1 = '/sattu/project/feed_d_foodie/source/foodiedotcom/restaurantsa9126b3.csv'
    file_name2 = '/sattu/project/feed_d_foodie/source/foodiedotcom/restaurant_addc9a1430.csv'
    cursor = connection.cursor()

    restro_dict = {}
    restro_detail_list = []
    with open(file_name1, 'r') as csvfile1:
        csv_data = csv.reader(csvfile1)
        header = next(csv_data)

        for row in csv_data:
            restro_dict = {header[i]: row[i] for i in range(len(header))}
            restro_detail_list.append(restro_dict)
        
        for val_dict in restro_detail_list:
            val_dict.update({'Restaurant ID': int(val_dict.get('Restaurant ID', ''))})
            val_dict.update({'Average Cost for two': int(val_dict.get('Average Cost for two', ''))})
            val_dict.update({'Votes': int(val_dict.get('Votes', ''))})
            val_dict.update({'Aggregate rating': float(val_dict.get('Aggregate rating', ''))})
            val_dict.update({'Currency': str(val_dict.get('Currency', ''))})
            data_vals = str(list(val_dict.values()))[1:-1]
            # cursor.execute(sql_stmt1 % data_vals)

    restro_extra_dict = {}
    restro_extra_detail_list = []
    with open(file_name2, 'r') as csvfile2:
        csv_data = csv.reader(csvfile2)
        header = next(csv_data)

        for row in csv_data:
            restro_extra_dict = {header[i]: row[i] for i in range(len(header))}
            restro_extra_detail_list.append(restro_extra_dict)

        for val_dict in restro_extra_detail_list:
            val_dict.update({'Restaurant ID': int(val_dict.get('Restaurant ID', ''))})
            val_dict.update({'Country Code': int(val_dict.get('Country Code', ''))})
            val_dict.update({'Longitude': float(val_dict.get('Longitude', ''))})
            val_dict.update({'Latitude': float(val_dict.get('Latitude', ''))})
            data_vals = str(list(val_dict.values()))[1:-1]
            # cursor.execute(sql_stmt2 % data_vals)

    return Response({}, template_name='insert_data_template.html')

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@renderer_classes([TemplateHTMLRenderer])
def get_restaurant_info(request):
    sort_key_map = {'votes': 'Votes', 'rating': 'Rating', 'avg_cost_for_two': 'Average Cost For 2'}
    cuisines = str(request.GET.get('cuisines', ''))
    restro_name = str(request.GET.get('restro_name', ''))
    sort_by = str(request.GET.get('sort_by', ''))
    sort_key_for_orm = ''
    if sort_by:
        if sort_by == 'avg_cost_for_two':
            sort_key_for_orm = sort_by
        else:
            sort_key_for_orm = '-' + sort_by
        if cuisines:
            restro_dataset = Restaurant.objects.filter(cuisines__icontains=cuisines).values().order_by(sort_key_for_orm)
            restro_dataset_count = Restaurant.objects.filter(cuisines__icontains=cuisines).values().count()
        elif restro_name:
            restro_dataset = Restaurant.objects.filter(restro_name__icontains=restro_name).values().order_by(sort_key_for_orm)
            restro_dataset_count = Restaurant.objects.filter(restro_name__icontains=restro_name).values().count()
        else:
            restro_dataset = Restaurant.objects.values().order_by(sort_key_for_orm)
            restro_dataset_count = Restaurant.objects.values().count()
    else:
        if cuisines:
            restro_dataset = Restaurant.objects.filter(cuisines__icontains=cuisines).values()
            restro_dataset_count = Restaurant.objects.filter(cuisines__icontains=cuisines).values().count()
        elif restro_name:
            restro_dataset = Restaurant.objects.filter(restro_name__icontains=restro_name).values()
            restro_dataset_count = Restaurant.objects.filter(restro_name__icontains=restro_name).values().count()
        else:
            restro_dataset = Restaurant.objects.values()
            restro_dataset_count = Restaurant.objects.values().count()

    sort_keys = [
        {'name': 'Rating', 'value': 'rating'},
        {'name': 'Votes', 'value': 'votes'},
        {'name': 'Average Cost For 2', 'value': 'avg_cost_for_two'}        
    ]
    sort_by_key = {'sort_key_list': sort_keys}
    final_dict = {'restro_list': restro_dataset}
    sort_by_name = sort_key_map.get(sort_by, '')
    return render(request, 'restaurant_list_template.html', {'final_dict': final_dict, 'count': restro_dataset_count, 'cuisines': cuisines, 'restro_name': restro_name, 'sort_keys': sort_by_key, 'sort_by': sort_by_name})

