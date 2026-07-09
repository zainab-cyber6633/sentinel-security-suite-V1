import socket


def dns_lookup(domain):

    try:

        ip_address = socket.gethostbyname(domain)

        result = (
            f"Domain Name : {domain}\n"
            f"IP Address  : {ip_address}"
        )

        return result


    except Exception as error:

        return f"DNS Lookup Failed: {error}"