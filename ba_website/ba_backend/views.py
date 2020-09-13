import sys
import math
import time
import random
import string
import json
import os

# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import *


def index(request):
    if not request.method == "GET":
        response = HttpResponse()
        response.status_code = 404
        return response
    return JsonResponse({"Test": "works"})

def version(request):
    if not request.method == "GET":
        response = HttpResponse()
        response.status_code = 404
        return response
    return JsonResponse({"version": "0.1"})

@csrf_exempt
def factorial(request, number):
    if not request.method == "GET":
        response = HttpResponse()
        response.status_code = 404
        return response
    own_print("started 'calc_factorial'")

    start = time.time()
    result = math.factorial(number)
    end = time.time()
    duration = end - start
    result_size = sys.getsizeof(result) / 1048576

    response = JsonResponse(
        {
            "Number_to_factorize": number,
            "Result_size_in_mb": result_size,
            "duration": duration,
        }
    )
    own_print(response.content)
    return response


@csrf_exempt
def save_random_integer(request, seed=1, used_as_subfunction=False):
    if not request.method == "POST":
        response = HttpResponse()
        response.status_code = 404
        return response

    start = time.time()

    integer = 0

    if not used_as_subfunction:
        seed = int(json.loads(request.body)["seed"])
        random.seed(seed)

    integer = int(round(random.random() * 100000, 0))

    end_creating = time.time()

    int_obj = Integer_Object()
    int_obj.int_value = integer
    int_obj.save()
    int_obj_id = int_obj.pk

    end = time.time()
    duration_creating = end_creating - start
    duration_saving = end - end_creating
    duration = end - start
    response = JsonResponse(
        {
            "integer": integer,
            "id": int_obj_id,
            "duration_of_creating": duration_creating,
            "duration_of_saving": duration_saving,
            "duration": duration,
        }
    )
    if not used_as_subfunction:
        own_print(response.content)
    return response


@csrf_exempt
def save_multiple_random_integers(request):
    if not request.method == "POST":
        response = HttpResponse()
        response.status_code = 404
        return response
    own_print("started 'save_multiple_random_integers'")

    integer_ids = []

    number_of_integers = int(json.loads(request.body)["number_of_integers"])
    seed = int(json.loads(request.body)["seed"])

    start = time.time()

    random.seed(seed)
    for _ in range(0, number_of_integers):
        integer_ids.append(json.loads(save_random_integer(request, used_as_subfunction=True).content)["id"])

    end = time.time()
    duration = end - start

    response = JsonResponse(
        {"requested_number_of_integers": number_of_integers, "duration": duration, "ids": integer_ids}
    )
    own_print("Saved multiple integers!")
    return response


def get_integer_from_db(request, integer_id):
    if not request.method == "GET":
        response = HttpResponse()
        response.status_code = 404
        return response
    start = time.time()

    int_object = Integer_Object.objects.get(pk=integer_id)
    integer = int_object.int_value
    end_getting = time.time()
    end = time.time()

    integer_size = sys.getsizeof(integer) / 1048576
    duration_loading = end_getting - start
    duration = end - start
    response = JsonResponse(
        {
            "size_of_integer_in_mb": integer_size,
            "duration_of_loading": duration_loading,
            "duration": duration,
            "integer": integer,
        }
    )
    own_print(response.content)
    return response


@csrf_exempt
def delete_integer_from_db(request, integer_id):
    if not request.method == "DELETE":
        response = HttpResponse()
        response.status_code = 404
        return response
    start = time.time()

    int_object = Integer_Object.objects.get(pk=integer_id)
    end_getting = time.time()
    int_object.delete()
    end = time.time()

    duration_loading = end_getting - start
    duration_deleting = end - end_getting
    duration = end - start
    response = JsonResponse(
        {
            "duration_of_loading": duration_loading,
            "duration_of_deleting": duration_deleting,
            "duration": duration,
        }
    )
    own_print(response.content)
    return response


@csrf_exempt
def delete_all_integers_from_db(request):
    if not request.method == "DELETE":
        response = HttpResponse()
        response.status_code = 404
        return response
    start = time.time()

    int_objects = Integer_Object.objects.all()
    end_getting = time.time()

    for int_object in int_objects:
        int_object.delete()

    end = time.time()

    duration_loading = end_getting - start
    duration_deleting = end - end_getting
    duration = end - start
    response = JsonResponse(
        {
            "duration_of_loading": duration_loading,
            "duration_of_deleting": duration_deleting,
            "duration": duration,
        }
    )
    own_print(response.content)
    return response


def get_integers_from_db(request, number_of_integers=None):
    if not request.method == "GET":
        response = HttpResponse()
        response.status_code = 404
        return response
    start = time.time()

    array = []
    int_objects = Integer_Object.objects.all()

    for x, int_obj in enumerate(int_objects):
        if number_of_integers:
            if x >= number_of_integers:
                break
        array.append(int_obj.int_value)


    end_getting = time.time()
    end = time.time()

    array_size = sys.getsizeof(array) / 1048576
    array_length = len(array)
    duration_loading = end_getting - start
    duration = end - start
    response = JsonResponse(
        {
            "size_of_array_in_mb": array_size,
            "array_size_in_units": array_length,
            "duration_of_loading": duration_loading,
            "duration": duration,
            "array": array,
        }
    )
    own_print("Got integers, sending now...")
    return response


def sort_integers_from_db(request):
    if not request.method == "GET":
        response = HttpResponse()
        response.status_code = 404
        return response
    start = time.time()

    array = []
    int_objects = Integer_Object.objects.all()

    for int_obj in int_objects:
        array.append(int_obj.int_value)

    end_getting = time.time()
    array.sort()
    end = time.time()

    array_size = sys.getsizeof(array) / 1048576
    array_length = len(array)
    first_int = array[0]
    last_int = array[-1]
    duration_loading = end_getting - start
    duration_sorting = end - end_getting
    duration = end - start
    response = JsonResponse(
        {
            "size_of_array_in_mb": array_size,
            "array_size_in_units": array_length,
            "duration_of_loading": duration_loading,
            "duration_of_sorting": duration_sorting,
            "duration": duration,
            "first_int": first_int,
            "last_int": last_int,
        }
    )
    own_print(response.content)
    return response


def get_string_from_db(request, string_id):
    if not request.method == "GET":
        response = HttpResponse()
        response.status_code = 404
        return response

    start = time.time()
    str_object = String_Object.objects.get(pk=string_id)
    string_ = str_object.string_value
    end = time.time()

    string_size = sys.getsizeof(string_) / 1048576
    duration = end - start
    response = JsonResponse(
        {
            "size_of_string_in_mb": string_size,
            "duration_of_loading": duration,
            "duration": duration,
            "string": string_,
        }
    )
    own_print(f"Got string with ID {string_id} from db, sending now...")
    return response


def get_strings_from_db(request, number_of_strings=None):
    if not request.method == "GET":
        response = HttpResponse()
        response.status_code = 404
        return response
    start = time.time()

    array = []
    str_objects = String_Object.objects.all()

    for x, str_obj in enumerate(str_objects):
        if number_of_strings:
            if x >= number_of_strings:
                break
        array.append(str_obj.string_value)
        

    end_getting = time.time()
    end = time.time()

    array_size = sys.getsizeof(array) / 1048576
    array_length = len(array)
    duration_loading = end_getting - start
    duration = end - start
    response = JsonResponse(
        {
            "size_of_array_in_mb": array_size,
            "array_size_in_units": array_length,
            "duration_of_loading": duration_loading,
            "duration": duration,
            "array": array,
        }
    )
    own_print("Got strings, sending now...")
    return response


@csrf_exempt
def delete_string_from_db(request, string_id):
    if not request.method == "DELETE":
        response = HttpResponse()
        response.status_code = 404
        return response
    start = time.time()

    str_object = String_Object.objects.get(pk=string_id)
    end_getting = time.time()
    str_object.delete()
    end = time.time()

    duration_loading = end_getting - start
    duration_deleting = end - end_getting
    duration = end - start
    response = JsonResponse(
        {
            "duration_of_loading": duration_loading,
            "duration_of_deleting": duration_deleting,
            "duration": duration,
        }
    )
    own_print(response.content)
    return response


@csrf_exempt
def delete_all_strings_from_db(request):
    if not request.method == "DELETE":
        response = HttpResponse()
        response.status_code = 404
        return response
    start = time.time()

    str_objects = String_Object.objects.all()
    end_getting = time.time()

    for str_object in str_objects:
        str_object.delete()

    end = time.time()

    duration_loading = end_getting - start
    duration_deleting = end - end_getting
    duration = end - start
    response = JsonResponse(
        {
            "duration_of_loading": duration_loading,
            "duration_of_deleting": duration_deleting,
            "duration": duration,
        }
    )
    own_print(response.content)
    return response


@csrf_exempt
def save_zero_string(request):
    if not request.method == "POST":
        response = HttpResponse()
        response.status_code = 404
        return response
    own_print("Started 'save_zero_string' function!")
    start = time.time()

    max_string_size = int(json.loads(request.body)["max_string_size"])

    max_string_size_byte = max_string_size * 1048576
    big_str = ""

    own_print("Generating string... This could take a loong time...")
    with open("/dev/zero", "rb") as file:
        read_bytes = file.read(max_string_size_byte)

    own_print("Got zeros, convert them now...")
    array = []
    for _byte in read_bytes:
        array.append(_byte)
        # big_str += str(_byte)
    big_str = "".join(map(str, array))

    own_print("String created, starting save...")
    end_creating = time.time()

    str_obj = String_Object()
    str_obj.string_value = big_str
    str_obj.save()
    str_id = str_obj.pk

    end = time.time()
    own_print("String saved!")

    str_size = sys.getsizeof(big_str) / 1048576
    duration_creating = end_creating - start
    duration_saving = end - end_creating
    duration = end - start

    response = JsonResponse(
        {
            "requested_size_of_string_in_mb": max_string_size,
            "actual_size_of_string_in_mb": str_size,
            "id": str_id,
            "duration_of_creating": duration_creating,
            "duration_of_saving": duration_saving,
            "duration": duration,
        }
    )

    own_print(response.content)
    return response


@csrf_exempt
def save_random_string(request):
    if not request.method == "POST":
        response = HttpResponse()
        response.status_code = 404
        return response
    own_print("Started 'save_random_string' function!")
    start = time.time()

    max_string_size = int(json.loads(request.body)["max_string_size"])
    seed = int(json.loads(request.body)["seed"])

    max_array_size_byte = max_string_size * 1048576
    big_str = ""

    random.seed(seed)

    own_print("Generating string... This could take a loong time...")
    while sys.getsizeof(big_str) < max_array_size_byte:
        big_str += random.choice(string.ascii_letters)

    own_print("String created, starting save...")
    end_creating = time.time()

    str_obj = String_Object()
    str_obj.string_value = big_str
    str_obj.save()
    str_id = str_obj.pk

    end = time.time()
    own_print("String saved!")

    str_size = sys.getsizeof(big_str) / 1048576
    duration_creating = end_creating - start
    duration_saving = end - end_creating
    duration = end - start

    response = JsonResponse(
        {
            "requested_size_of_string_in_mb": max_string_size,
            "actual_size_of_string_in_mb": str_size,
            "id": str_id,
            "duration_of_creating": duration_creating,
            "duration_of_saving": duration_saving,
            "duration": duration,
        }
    )

    own_print(response.content)
    return response


@csrf_exempt
def save_simple_unsorted_string(request):
    if not request.method == "POST":
        response = HttpResponse()
        response.status_code = 404
        return response
    own_print("Started 'save_string' function!")
    start = time.time()

    max_string_size = int(json.loads(request.body)["max_string_size"])
    max_array_size_byte = max_string_size * 1048576
    big_str = ""

    own_print("Generating string... This could take some time...")
    while sys.getsizeof(big_str) < max_array_size_byte:
        big_str += string.ascii_letters

    own_print("String created, starting save...")
    end_creating = time.time()

    str_obj = String_Object()
    str_obj.string_value = big_str
    str_obj.save()
    str_id = str_obj.pk

    end = time.time()
    own_print("String saved!")

    str_size = sys.getsizeof(big_str) / 1048576
    duration_creating = end_creating - start
    duration_saving = end - end_creating
    duration = end - start

    response = JsonResponse(
        {
            "requested_size_of_array_in_mb": max_string_size,
            "actual_size_of_array_in_mb": str_size,
            "id": str_id,
            "duration_of_creating": duration_creating,
            "duration_of_saving": duration_saving,
            "duration": duration,
        }
    )

    own_print(response.content)
    return response


@csrf_exempt
def sort_string(request, string_id):
    if not request.method == "GET":
        response = HttpResponse()
        response.status_code = 404
        return response
    own_print("Started 'sort_string' function!")
    start = time.time()

    own_print("Loading string from db...")
    string_ = String_Object.objects.filter(pk=string_id)[0].string_value
    end_getting = time.time()

    own_print("String loaded from db!")
    own_print("Starting sort of string...")

    string_ = "".join(sorted(string_))

    end = time.time()
    own_print("String sorted!")

    string_size = sys.getsizeof(string_) / 1048576
    duration_loading = end_getting - start
    duration_sorting = end - end_getting
    duration = end - start
    response = JsonResponse(
        {
            "actual_size_of_string_in_mb": string_size,
            "duration_of_loading": duration_loading,
            "duration_of_sorting": duration_sorting,
            "duration": duration,
            "first_char": string_[0],
            "last_char": string_[-1],
        }
    )

    own_print(response.content)
    return response


@csrf_exempt
def save_zero_bytes(request):
    if not request.method == "POST":
        response = HttpResponse()
        response.status_code = 404
        return response
    own_print("Started 'save_zero_bytes' function!")
    start = time.time()

    max_byte_size = int(json.loads(request.body)["max_byte_size"])
    max_byte_size_byte = max_byte_size * 1048576

    own_print("Generating bytes... This could take a loong time...")
    with open("/dev/zero", "rb") as file:
        read_bytes = file.read(max_byte_size_byte)

    end_creating = time.time()
    own_print("Got zeroes, saving them now...")
    byte_obj = Bytes_Object()
    byte_obj.bytes_value = read_bytes
    byte_obj.save()
    byte_id = byte_obj.pk

    end = time.time()
    own_print("Bytes saved!")

    byte_size = sys.getsizeof(read_bytes) / 1048576
    duration_creating = end_creating - start
    duration_saving = end - end_creating
    duration = end - start

    response = JsonResponse(
        {
            "requested_size_of_bytes_in_mb": max_byte_size,
            "actual_size_of_bytes_in_mb": byte_size,
            "id": byte_id,
            "duration_of_creating": duration_creating,
            "duration_of_saving": duration_saving,
            "duration": duration,
        }
    )

    own_print(response.content)
    return response


def get_bytes(request, byte_id):
    if not request.method == "GET":
        response = HttpResponse()
        response.status_code = 404
        return response
    own_print("Started 'get_bytes' function!")

    start = time.time()
    bytes_object = Bytes_Object.objects.get(pk=byte_id)
    bytes_ = bytes_object.bytes_value
    end = time.time()
    
    duration = end - start
    response = JsonResponse(
        {
            "duration_of_loading": duration,
            "duration": duration,
        }
    )
    own_print(f"Got bytes with ID {byte_id} from db, sending metadata now")
    return response

def get_multiple_bytes(request, number_of_bytes=None):
    if not request.method == "GET":
        response = HttpResponse()
        response.status_code = 404
        return response
    start = time.time()

    array = []
    byte_objects = Bytes_Object.objects.all()

    for x, bytes_obj in enumerate(byte_objects):
        if number_of_bytes:
            if x >= number_of_bytes:
                break
        array.append(bytes_obj.bytes_value)
        

    end_getting = time.time()
    end = time.time()

    duration_loading = end_getting - start
    duration = end - start
    response = JsonResponse(
        {
            "duration_of_loading": duration_loading,
            "duration": duration,
        }
    )
    own_print("Got bytes, sending metadata now...")
    return response


@csrf_exempt
def delete_bytes_from_db(request, byte_id):
    if not request.method == "DELETE":
        response = HttpResponse()
        response.status_code = 404
        return response
    start = time.time()

    str_object = Bytes_Object.objects.get(pk=byte_id)
    end_getting = time.time()
    str_object.delete()
    end = time.time()

    duration_loading = end_getting - start
    duration_deleting = end - end_getting
    duration = end - start
    response = JsonResponse(
        {
            "duration_of_loading": duration_loading,
            "duration_of_deleting": duration_deleting,
            "duration": duration,
        }
    )
    own_print(response.content)
    return response


@csrf_exempt
def delete_all_bytes_from_db(request):
    if not request.method == "DELETE":
        response = HttpResponse()
        response.status_code = 404
        return response
    start = time.time()

    byte_objects = Bytes_Object.objects.all()
    end_getting = time.time()

    for byte_object in byte_objects:
        byte_object.delete()

    end = time.time()

    duration_loading = end_getting - start
    duration_deleting = end - end_getting
    duration = end - start
    response = JsonResponse(
        {
            "duration_of_loading": duration_loading,
            "duration_of_deleting": duration_deleting,
            "duration": duration,
        }
    )
    own_print(response.content)
    return response


def own_print(var_to_print):
    if "DEBUG_DEPLOYMENT" in os.environ:
        print(var_to_print)
