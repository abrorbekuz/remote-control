from django.http import HttpResponse
from controls.models import COMMAND
import pyautogui as pg
import json

def press_key(request, key):
    fkey = COMMAND.objects.filter(link = key)
    success = "no"

    if fkey is not None:
        success = "ok"
        print(fkey.first().k_command)
        pg.press(fkey.first().k_command)

    return HttpResponse(
        json.dumps({ "succes": success}),
        content_type="application/json"
    )
