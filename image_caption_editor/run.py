import subprocess

def run():
    """Run the Streamlit app using subprocess to invoke the CLI correctly."""
    # Absolute path to your app.py or relative from the current working directory
    subprocess.run(['streamlit', 'run', "image_caption_editor/app.py"], check=True)

if __name__ == "__main__":
    run()
