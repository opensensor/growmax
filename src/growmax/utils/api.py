import machine
import ubinascii
import time

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
            "api_key": config.OPEN_SENSOR_API_KEY,
        }
    except Exception as e:
        print(e)
    return report_data


def add_adafruit_scd4x_data_to_report(report_data, temp, rh, ppm_carbon_dioxide):
    if temp:
        report_data["temp"] = {
            "temp": temp,
            "unit": "C"
        }
    if rh:
        report_data["rh"] = {
            "rh": rh,
        }
    if ppm_carbon_dioxide:
        report_data["co2"] = {
            "ppm": ppm_carbon_dioxide,
        }


def report_environment_data(report_data):
    """ This method requires installing urequests from pypi. """
    try:
        import urequests
        import json
        time.sleep(1.0)
        resp = urequests.post(
            "https://api.opensensor.io/environment/",
            headers=headers,
            data=json.dumps(report_data))
        print(resp.status_code)
        resp.close()
    except Exception as e:
        print(e)
