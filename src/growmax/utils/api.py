import machine
import ubinascii
import time
from growmax.utils import sensors

import config

headers = {'content-type': 'application/json'}


def get_device_metadata():
    report_data = {}
    try:
        time.sleep(1.0)
        device_id = ubinascii.hexlify(machine.unique_id()).decode()
        time.sleep(1.0)
        report_data["device_metadata"] = {
            "device_id": device_id,
            "name": config.DEVICE_NAME,
        }
    except Exception as e:
        print(e)
    return report_data


def read_adafruit_scd4x_(scd4x, report_data):
    try:
        time.sleep(1.0)
        data = sensors.read_adafruit_scd4x(scd4x)
        time.sleep(1.0)
        report_data["temp"] = {
            "temp": data[0],
            "unit": "C"
        }
        report_data["rh"] = {
            "rh": data[1],
        }
        report_data["co2"] = {
            "ppm": data[2],
        }
    except Exception as e:
        print(e)


def report_environment_data(report_data):
    """This method requires installing urequests and ujson from pypi."""
    try:
        import urequests
        import ujson
        time.sleep(1.0)
        resp = urequests.post(
            "https://api.opensensor.io/environment/",
            headers=headers,
            data=ujson.dumps(report_data))
        print(resp.status_code)
        resp.close()
    except Exception as e:
        print(e)
