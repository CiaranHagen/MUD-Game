#!/bin/bash
wmctrl -r :ACTIVE: -b add,fullscreen

cd $(locate '*/MUDGame')
python3 main.py

wmctrl -r :ACTIVE: -b remove,fullscreen


