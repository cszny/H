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
  filePath = "api/env/ws/gx"
  fileOpen = open(filePath, 'r')
  fileRead = fileOpen.read()
  return render_template("library.html", fileRead=fileRead)

@app.route("/notify", methods=["GET", "POST"])
def notify():
  filePath = "api/env/ws/px"
  fileOpen = open(filePath, 'r')
  fileRead = fileOpen.read()
  return render_template("notif.html", fileRead=fileRead)