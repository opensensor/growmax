import machine
import ubinascii

from growmax.utils import sensors

def read_and_report_adafruit_scd4x(scd4x):
    try:
        import urequests
        import ujson
        data = sensors.read_adafruit_scd4x(scd4x)
        device_id = ubinascii.hexlify(machine.unique_id()).decode()
        report_data = {
            "device_metadata": {
                "device_id": device_id,
                "name": "matt_d_pico_w_test",
            },
            "temp": {
                "temp": data[0],
                "unit": "C"
            },
            "rh": {
                "rh": data[1],
            },
            "CO2": {
                "ppm": data[2],
            }
        }
        resp = urequests.post(
            "https://api.opensensor.io/environment/",
            headers={'content-type': 'application/json'},
            data=ujson.dumps(report_data))
        print(resp.text)
        return data
    except Exception as e:
        print(e)
    return None
