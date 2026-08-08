import subprocess
import time
import requests
import os
import signal

def test_api():
    # Start the server
    process = subprocess.Popen(["python", "main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Starting server...")