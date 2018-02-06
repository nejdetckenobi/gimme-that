import netifaces as ni


def get_ips():
    interfaces = ni.interfaces()
    ips = []
    for interface in interfaces:
        try:
            if 'broadcast' in ni.ifaddresses(interface)[ni.AF_INET][0]:
                ips.append(ni.ifaddresses(interface)[ni.AF_INET][0]['addr'])
        except KeyError:
            pass
    return ips
