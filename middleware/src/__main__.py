import os
from src.app.app import App

FLASK_PORT = os.environ.get('FLASK_PORT')

if __name__ == '__main__':
    App.run(host='0.0.0.0', port=FLASK_PORT, debug=True)

