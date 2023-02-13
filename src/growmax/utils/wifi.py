import time
import config


# Global variables
wlan = None

def ensure_wifi_connected():
    # check if the Wi-Fi interface is connected
    if not config.WIFI_ENABLED:
        print("WIFI not enabled; change your config if you want wifi capabilities enabled.")
        return
    print("ensure_wifi_connected")
    time.sleep(1.0)
    import network
    global wlan
    if wlan is None:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.disconnect()
        time.sleep(1.0)
    if not wlan.isconnected():
        print(f"Connecting to Wi-Fi SSID: {config.WIFI_SSID}")
        wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

        # connect to the Wi-Fi network:
        while not wlan.isconnected():
            time.sleep(0.5)

        # sync current time via NTP
        from growmax import ntpclient
        ntpclient.settime()
        print(f"Connected to Wi-Fi SSID: {config.WIFI_SSID}")
        time.sleep(0.5)

