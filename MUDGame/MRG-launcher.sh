#!/bin/bash

cd $(locate '*/MUDGame')

wmctrl -r :ACTIVE: -b add,fullscreen

python3 main.py

wmctrl -r :ACTIVE: -b remove,fullscreen


