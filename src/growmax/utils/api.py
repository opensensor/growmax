import machine
import ubinascii
import time
from growmax.utils import sensors

import config

headers = {'content-type': 'application/json'}

def read_and_report_adafruit_scd4x(scd4x):
    """This method requires installing urequests and ujson from pypi."""
    try:
        import urequests
        import ujson
        data = sensors.read_adafruit_scd4x(scd4x)
        time.sleep(1.0)
        device_id = ubinascii.hexlify(machine.unique_id()).decode()
        time.sleep(1.0)
        report_data = {
            "device_metadata": {
                "device_id": device_id,
                "name": config.DEVICE_NAME,
            },
            "temp": {
                "temp": data[0],
                "unit": "C"
            },
            "rh": {
                "rh": data[1],
            },
            "co2": {
                "ppm": data[2],
            }
        }
        time.sleep(1.0)
        resp = urequests.post(
            "https://api.opensensor.io/environment/",
            headers=headers,
            data=ujson.dumps(report_data))
        print(resp.status_code)
        resp.close()
        return data
    except Exception as e:
        print(e)
    return None

