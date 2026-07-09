import whois


def whois_lookup(domain):

    try:

        data = whois.whois(domain)

        result = (
            f"Domain Name : {data.domain_name}\n"
            f"Registrar   : {data.registrar}\n"
            f"Country     : {data.country}\n"
            f"Created     : {data.creation_date}\n"
            f"Expiry      : {data.expiration_date}"
        )

        print("\n" + result)

        return result


    except Exception as error:

        result = f"WHOIS Lookup Failed: {error}"

        print(result)

        return result