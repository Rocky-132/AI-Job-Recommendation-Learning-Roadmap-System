import os
import sys
import subprocess
import venv

def main():
    workspace = os.path.dirname(os.path.abspath(__file__))
    venv_dir = os.path.join(workspace, ".venv")
    
    # 1. Create virtual environment if it doesn't exist
    if not os.path.exists(venv_dir):
        print(f"Creating virtual environment in {venv_dir}...")
        venv.create(venv_dir, with_pip=True)
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")

    # Determine paths to python and pip executables
    if sys.platform == "win32":
        python_exe = os.path.join(venv_dir, "Scripts", "python.exe")
        pip_exe = os.path.join(venv_dir, "Scripts", "pip.exe")
        uvicorn_exe = os.path.join(venv_dir, "Scripts", "uvicorn.exe")
    else:
        python_exe = os.path.join(venv_dir, "bin", "python")
        pip_exe = os.path.join(venv_dir, "bin", "pip")
        uvicorn_exe = os.path.join(venv_dir, "bin", "uvicorn")

    # 2. Install/Upgrade requirements
    requirements_txt = os.path.join(workspace, "requirements.txt")
    if os.path.exists(requirements_txt):
        print("Installing / upgrading requirements...")
        try:
            subprocess.run([pip_exe, "install", "-r", requirements_txt], check=True)
            print("Dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Warning: requirements.txt not found.", file=sys.stderr)

    # 3. Start FastAPI server
    print("Starting FastAPI server using uvicorn...")
    main_module = "backend.main:app"
    
    try:
        # Run uvicorn as a subprocess so we can capture ctrl-c cleanly
        # Use python_exe -m uvicorn to ensure it runs within the virtualenv
        cmd = [python_exe, "-m", "uvicorn", main_module, "--reload", "--host", "127.0.0.1", "--port", "8000"]
        print(f"Running command: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\nFastAPI server stopped by user.")
    except subprocess.CalledProcessError as e:
        print(f"Server crashed or exited with error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
