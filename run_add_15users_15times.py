#!/usr/bin/pyhon3

import os
import platform

info = {}

platform_details = platform.platform()
info["platform details"] = platform_details



i = 0
while i < 15:
	os.system("/root/scripts/add_15users_sh_py/add_15users.sh")
	i += 1

