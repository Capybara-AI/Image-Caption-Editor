import subprocess

def run():
    """Run the Streamlit app using subprocess to invoke the CLI correctly."""
    subprocess.run(['streamlit', 'run', "image_caption_editor/app.py"], check=True)

if __name__ == "__main__":
    run()
