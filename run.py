import os
from app import create_app

if ('FLASK_CONFIG' in os.environ):
    config_name = os.getenv('FLASK_CONFIG') 
else:
    config_name = 'development'

app = create_app(config_name)

if __name__ == '__main__':
    app.run()
