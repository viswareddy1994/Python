"""
import  os


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir,"subfolder","file_name")
"""
"""
import os

# Print current working directory
print("Current Working Directory:", os.getcwd())

# Check if .env file exists
env_file_path = os.path.join(os.path.dirname(__file__), '.env')
print(".env file exists:", os.path.isfile(env_file_path))
"""