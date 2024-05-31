import subprocess
import os

def run():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    app_path = os.path.join(dir_path, 'app.py')
    subprocess.run(['streamlit', 'run', app_path], check=True)
if __name__ == "__main__":
    run()
