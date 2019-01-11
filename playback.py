#!/usr/bin/env python3

from irrp_with_class import IRRP3

irrp=IRRP3(gpio=17, filename="codes")
irrp.playback("light:on")
