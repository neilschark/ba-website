from django.urls import path
from . import views

urlpatterns = [
    # GET
    path("", views.index),

    # GET
    path("version", views.version),

    # Get
    path("factorial/<int:number>", views.factorial),

    # POST {"seed": int}
    path("create/random-integer", views.save_random_integer),

    # POST {"number_of_integers": int, "seed": int}
    path("create/random-integers", views.save_multiple_random_integers),

    # GET
    path("get/integer/<int:integer_id>", views.get_integer_from_db),

    # DELETE
    path("delete/integer/<int:integer_id>", views.delete_integer_from_db),

    # GET
    path("get/integers/<int:number_of_integers>", views.get_integers_from_db),

    # DELETE
    path("delete/integers", views.delete_all_integers_from_db),

    # GET
    path("get/integers-sorted", views.sort_integers_from_db),

    # GET
    path("get/string/<int:string_id>", views.get_string_from_db),

    # GET
    path("get/strings/<int:number_of_strings>", views.get_strings_from_db),

    # DELETE
    path("delete/string/<int:string_id>", views.delete_string_from_db),

    # DELETE
    path("delete/strings", views.delete_all_strings_from_db),

    # POST {"max_string_size": int, "seed": int}
    path("create/random-string", views.save_random_string),

    # POST {"max_string_size": int}
    path("create/simple-string", views.save_simple_unsorted_string),

    # POST {"max_string_size": int}
    path("create/zero-string", views.save_zero_string),

    # GET
    path("get/string-sorted/<int:string_id>", views.sort_string),

    # POST {"max_byte_size": int}
    path("create/zero-bytes", views.save_zero_bytes),

    # GET
    path("get/bytes-without-sending/<int:byte_id>", views.get_bytes),

    # GET
    path("get/multiple-bytes-without-sending/<int:number_of_bytes>", views.get_multiple_bytes),

    # DELETE
    path("delete/bytes/<int:byte_id>", views.delete_bytes_from_db),

    # DELETE
    path("delete/bytes", views.delete_all_bytes_from_db),

]
