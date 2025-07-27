# 31. Environment variables
import os
api_key = os.getenv('API_KEY')

# 32. Docker health check script
import socket
s = socket.create_connection(('localhost', 5432), timeout=5)

# 33. CI/CD: Shell execution
import subprocess
subprocess.run(['pytest', 'tests/'])

# 34. Config reader
import configparser
config = configparser.ConfigParser()
config.read('app.ini')

# 35. Create virtual environment
# python -m venv env

# 36. Dependency freeze
# pip freeze > requirements.txt

# 37. Git automation
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'update'])

# 38. YAML loader
import yaml
with open('config.yaml') as f:
    settings = yaml.safe_load(f)

# 39. Build notifier
# Use Slack API to send notification after build

# 40. Load .env
from dotenv import load_dotenv
load_dotenv()
