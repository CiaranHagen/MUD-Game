#!/bin/bash

cd $(locate '*/MUDGame')
echo -ne "\e[9;1t"

wmctrl -r :ACTIVE: -b add,fullscreen

python3 main.py

wmctrl -r :ACTIVE: -b remove,fullscreen
