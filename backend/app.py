from api import create_app
from flask_socketio import SocketIO, emit

app = create_app()
socketio = SocketIO(app, cors_allowed_origins="*", engineio_logger=True)

@socketio.on('connect')
def handle_my_custom_event():
    print('connected')
    emit('test', "fff")
    
@socketio.on('test')
def handle_test():
    print("ff")


if __name__ == '__main__':
    
    app.run(debug=True)
    socketio.run(app, debug=True)