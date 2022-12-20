#
# SPDX-FileCopyrightText: Copyright 2022 Arm Limited and/or its affiliates <open-source-office@arm.com>
# SPDX-License-Identifier: MIT
#
import machine
import socket
import struct
import time


def settime():
    ntp_request = bytearray(48)
    ntp_request[0] = 0x23  # v4, client mode

    addr = socket.getaddrinfo("pool.ntp.org", 123)[0][-1]

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.settimeout(5)
    s.sendto(ntp_request, addr)

    ntp_response = s.recv(48)

    transit_timestamp_seconds = struct.unpack("!I", ntp_response[40:44])[0]

    (year, month, mday, hour, minute, second, weekday, _) = time.gmtime(
        transit_timestamp_seconds - 2208988800
    )  # (date(1970, 1, 1) - date(1900, 1, 1)).days * 24*60*60

    machine.RTC().datetime((year, month, mday, weekday, hour, minute, second, 0))
