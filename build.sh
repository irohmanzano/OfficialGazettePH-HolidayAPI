#!/bin/bash
apt-get update
apt-get install -y wget gnupg ca-certificates
pip install -r requirements.txt
