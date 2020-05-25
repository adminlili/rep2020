#!/usr/bin/pyhon3

import os
import platform

info = {}

platform_details = platform.platform()
info["platform details"] = platform_details

system_name = platform.system()
info["system name"] = system_name

processor_name = platform.processor()
info["processor name"] = processor_name

architecture_details = platform.architecture()
info["architecture details"] = architecture_details



i = 0
while i < 15:
	os.system("/root/scripts/add_15users_sh_py/add_15users.sh")
	i += 1

