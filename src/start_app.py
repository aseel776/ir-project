from app import createApp
from core.ports import APP_PORT

if __name__ == '__main__':
    app = createApp()
    app.run(debug=True, host = '127.0.0.1', port= APP_PORT)