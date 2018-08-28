import requests
import datetime
from time import sleep
import math
from config import CONFIG
# from flask import Flask, request, jsonify, render_template
from aiohttp import web
import socketio
import eventlet
import eventlet.wsgi
import subprocess
import pymongo

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

app.router.add_static('/static', 'static')

async def index(request):
	with open('templates/index.html') as f:
		return web.Response(text=f.read(), content_type='text/html')

@sio.on('connect', namespace='/')
def connect(sid, environ):
	print("connect ", sid)
	sio.emit('status', 'collecting', room=sid)
	process = subprocess.Popen(["python3", "worker/worker.py", CONFIG["host"], CONFIG["username"], CONFIG["password"], sid], stdout=subprocess.PIPE, bufsize=1)

@sio.on('progress', namespace='/')
def progress(sid, environ):
	data = db.sessions.find_one({"id": str(sid)})
	sio.emit('progress', data["progress"], room=sid)
	if (data["progress"] >= 1):
		sio.emit('status', 'done', room=sid)

@sio.on('data', namespace='/')
def progress(sid, environ):
	data = db.sessions.find_one({"id": str(sid)})
	sio.emit('result', data, room=sid)

if __name__ == "__main__":
	# app.run(host='whosthehog.home', port=80, ssl_context=sc)
	app.router.add_get('/', index)
	web.run_app(app)
	# app.run(host='0.0.0.0', port=8000)

