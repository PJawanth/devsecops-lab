import os

def add(a, b):
    return a + b

import subprocess

subprocess.run(["ls"], check=True)


API_KEY = os.getenv("API_KEY")

if __name__ == "__main__":
    print(add(2, 3))
    run_command()
