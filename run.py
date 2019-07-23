import sys
sys.path.append('API/model')
sys.path.append('API')
from app import create_app
server = create_app()
server.run()