#!/usr/bin/env python3

from irrp_with_class import IRRP


irrp = IRRP(gpio=17, filename="codes")
irrp.playback("light:on")
