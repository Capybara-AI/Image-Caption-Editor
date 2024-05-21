import subprocess

def run():
    subprocess.run(['streamlit', 'run', "image_caption_editor/app.py"], check=True)

if __name__ == "__main__":
    run()
