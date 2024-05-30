import subprocess
import os

def main():
    script_path = os.path.join(os.path.dirname(__file__), 'app.py')
    subprocess.run(['streamlit', 'run', script_path])

if __name__ == '__main__':
    main()
