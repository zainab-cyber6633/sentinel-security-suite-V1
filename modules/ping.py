import subprocess


def ping_host(target):

    try:

        result = subprocess.run(
            ["ping", "-n", "1", target],
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as error:

        return f"Error: {error}"