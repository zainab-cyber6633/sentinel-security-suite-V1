import subprocess
import platform


def ping_host(target):

    try:

        if platform.system() == "Windows":
            command = ["ping", "-n", "1", target]
        else:
            command = ["ping", "-c", "1", target]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as error:

        return f"Error: {error}"