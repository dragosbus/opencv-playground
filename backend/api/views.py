from flask import Blueprint, request,make_response,Flask
from .controlers import read_numpy_array
import time
from threading import Thread

views = Blueprint('views', __name__)

class MyThread(Thread):
    def __init__(self, target, args=list()):
        Thread.__init__(self)
        self.target = target
        self.args = args
        
    def run(self):
        self.target(*self.args)

threads = []
killed = False

def long_request():
    print("Staring long request")
    time.sleep(10)
    print('Ended long request')

@views.route('/')
def home():
    print(f"the client request is {request.remote_addr}")
    return '<h1>Test</h1>'

@views.route('/long_request')
def make_long_request():
    t = MyThread(target=long_request)
    threads.append(t)
    
    for t in threads:
        t.start()
        t.join()

    return make_response({
        "data":"Success"
    })
    
@views.route('/kill_long_request')
def kill_long_request():
    for t in threads:
        t.join()
    return make_response({
        "data":"Success"
    })

@views.route("/image")
def get_image():
    try:
        numpy_array = read_numpy_array('static/test.jpg')

        return numpy_array
    except Exception as e:
        print(e)

from flask_socketio import send, emit,SocketIO

socketio = SocketIO(Flask(__name__))

