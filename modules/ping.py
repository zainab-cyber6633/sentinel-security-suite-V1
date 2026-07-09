import subprocess


def ping_host(target):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", target],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return f"[+] {target} is reachable"
        else:
            return f"[-] {target} is not reachable"

    except Exception as error:
        return f"Error: {error}"