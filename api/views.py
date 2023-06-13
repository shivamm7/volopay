from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.http import JsonResponse


from api.models import Api
import json


def total_items(request):
    data = json.loads(request.body.decode('utf-8'))

    dept = data["department"]
    start = data["start_date"]
    end = data["end_date"]
    
    db_connection = connection.cursor()
    query = f"SELECT COUNT(*) FROM api_api WHERE department = '{dept}' AND (date BETWEEN '{start}' AND '{end}')"
    
    db_connection.execute(query)
    rows = db_connection.fetchall()

    db_connection.close()

    result = {"result" : rows[0][0]}
    
    return JsonResponse(result)

def nth_most_total_item(request):
    data = json.loads(request.body.decode('utf-8'))

    item = data["item_by"]
    start = data["start_date"]
    end = data["end_date"]
    n = data["n"]

    db_connection = connection.cursor()

    if item == 'quantity':
        query = f"SELECT software, SUM(seats) as seats FROM api_api WHERE date BETWEEN '{start}' AND '{end}' GROUP BY software ORDER BY seats DESC"
    elif item == 'price':
        query = f"SELECT software, SUM(amount) as seats FROM api_api WHERE date BETWEEN '{start}' AND '{end}' GROUP BY software ORDER BY seats DESC"
        
    
    db_connection.execute(query)
    rows = db_connection.fetchall()
    print(rows)
    result = {"result" : rows[n][0]}
    
    return JsonResponse(result)

def percentage_of_department_wise_sold_items(request):
    data = json.loads(request.body.decode('utf-8'))

    start = data["start_date"]
    end = data["end_date"]

    db_connection = connection.cursor()

    query = f"SELECT department, SUM(seats) as seats FROM api_api WHERE date BETWEEN '{start}' AND '{end}' GROUP BY department"
    db_connection.execute(query)
    departments = db_connection.fetchall()

    query = f"SELECT SUM(seats) as seats FROM api_api WHERE date BETWEEN '{start}' AND '{end}'"
    db_connection.execute(query)
    total_seats = db_connection.fetchall()

    result = {}

    for department in departments:
        print(department[1], total_seats[0])

        percentage = department[1] / total_seats[0][0] * 100

        result[department[0]] = percentage

    return JsonResponse(result)

def monthly_sales(request):
    data = json.loads(request.body.decode('utf-8'))

    product = data["product"]
    year = data["year"]

    db_connection = connection.cursor()

    query = f"SELECT SUM(seats) as seats FROM api_api"
    db_connection.execute(query)
    sales = db_connection.fetchall()

    print(sales)

    return HttpResponse("result")
