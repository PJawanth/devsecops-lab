import os

def add(a, b):
    return a + b

def run_command():
    os.system("ls")  # ❌ insecure shell execution

API_KEY = "my-secret-key"  # ❌ hardcoded secret

if __name__ == "__main__":
    print(add(2, 3))
    run_command()
