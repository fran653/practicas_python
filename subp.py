import subprocess
result = subprocess.run(["host", "8.8.8.8"], capture_output=True, text=True)
print(result.returncode)
                         