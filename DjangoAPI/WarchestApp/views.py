from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from WarchestApp.models import WarchestData
from WarchestApp.serializers import WarchestSerializer

from django.core.files.storage import default_storage

import json
# Create your views here.


# def warchestData():
#     jsonData = {
#         "dates": ["7/27/2022", "7/28/2022"],
#         "tables": [{
#             "title": "ABC",
#             "fieldData": [
#                 [10, 20],
#                 [11, 21],
#                 [12, 22],
#                 [13, 23],
#                 [13, 23]
#             ]
#         },
#             {
#             "title": "DEF",
#             "fieldData": [
#                 [10, 20],
#                 [11, 21],
#                 [32, 22],
#                 [13, 23],
#                 [13, 23]
#             ]
#         },
#             {
#             "title": "GIJ",
#             "fieldData": [
#                 [10, 20],
#                 [11, 21],
#                 [42, 22],
#                 [13, 23],
#                 [13, 23]
#             ]
#         },
#             {
#             "title": "KLM",
#             "fieldData": [
#                 [10, 20],
#                 [11, 21],
#                 [52, 22],
#                 [13, 23],
#                 [13, 23]
#             ]
#         },
#         ]
#     }
#     var = json.loads(jsonData)


@csrf_exempt
def warchestApi(request, id=0):

    if request.method == 'GET':
        warchests = WarchestData.objects.all()
        # print(warchests)
        warchests_serializer = WarchestSerializer(warchests, many=True)
        # print(warchests_serializer.data)
        warchest_dict = json.dumps(warchests_serializer.data)

        print(warchest_dict)
        return JsonResponse(warchests_serializer.data, safe=False)

    elif request.method == 'POST':
        print(" post-----")
        warchest_data = JSONParser().parse(request)
        print(warchest_data)
        warchests_serializer = WarchestSerializer(data=warchest_data)
        if warchests_serializer.is_valid():
            warchests_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        print(" put-----")
        warchest_data = JSONParser().parse(request)
        print(warchest_data)
        warchest = WarchestData.objects.get(
            Id=warchest_data['Id'])
        warchests_serializer = WarchestSerializer(warchest, data=warchest_data)
        if warchests_serializer.is_valid():
            warchests_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        print(warchests_serializer.errors)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        warchest = WarchestData.objects.get(Id=id)
        warchest.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    print(" SaveFile-----")
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
