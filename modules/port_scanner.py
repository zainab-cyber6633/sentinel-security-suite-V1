import socket


def port_scan(target):

    ports = [21, 22, 23, 25, 53, 80, 443, 8080]

    result = f"Port Scan Result for {target}\n\n"


    for port in ports:

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(1)

            status = sock.connect_ex(
                (target, port)
            )


            if status == 0:

                result += f"[OPEN] Port {port}\n"


            else:

                result += f"[CLOSED] Port {port}\n"


            sock.close()


        except Exception as error:

            result += f"Port {port} Error: {error}\n"


    print("\n" + result)

    return result