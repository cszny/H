from flask import Flask, render_template, request, redirect, url_for, g, flash, abort, jsonify, send_file, Response, make_response
import requests
import base64
import hashlib
import time
import socket
import threading
import random
import string
import os
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = "Hikari"

@app.route("/", methods=["GET", "POST"])
def home():
  return "Hello"
  
@app.route("/library", methods=["GET", "POST"])
def library():
  filePath = "env/ws/gx"
  fileOpen = open(filePath, 'r')
  fileRead = fileOpen.read()
  return Response(fileRead, content_type="text/plain")