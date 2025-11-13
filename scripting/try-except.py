# #!/usr/bin/env python3
import subprocess

# try:
#     open("/no/such/file")
# except FileNotFoundError as e:
#     print(f"Ooops: {e}")


def home_usage():
    try:
        cmd = ["du", "-sh", "/tmp/secret_folder_that_does_not_exist"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"du failed: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"


print("=== HOME USAGE ===")
print(home_usage())
