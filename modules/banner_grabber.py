import socket


def banner_grab(target, port):

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(5)

        sock.connect((target, port))


        # Send request for HTTP services
        if port == 80:
            sock.send(
                b"HEAD / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n"
            )


        banner = sock.recv(1024).decode(
            errors="ignore"
        )


        result = (
            f"Target : {target}\n"
            f"Port   : {port}\n\n"
            f"Banner:\n{banner}"
        )


        sock.close()

        return result


    except Exception as error:

        return f"Banner Grab Failed: {error}"