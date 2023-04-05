#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
# # importing the required libraries
# import requests
# # Enter the api key of openweathermap here
# api_key = "e350eb73ae05d393946e11ea020b13ff"
# # Base url for the open map api
# root_url = "http://api.openweathermap.org/data/2.5/weather?"
# # City name for which we need the weather data
# city_name = "bangalore"
# # Building the final url for the API call
# url = f"{root_url}appid={api_key}&q={city_name}"
# # sending a get request at the url
# r = requests.get(url)
# # displaying the json weather data returned by the api
# print(r.json())
# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("Palindrom")
# else:
#     print("Palindrom emas")
