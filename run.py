import sys
import os
sys.path.append('API/model')
sys.path.append('API')
from app import create_app
server = create_app()
server.run(host='0.0.0.0', port=os.environ['PORT'])