#!/bin/bash

sudo apt update
sudo apt install --yes python3 python3-pip

python3 -m pip install --upgrade twine
python3 -m pip install --upgrade build
