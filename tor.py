import requesocks
import ipaddress


start_ip = ipaddress.IPv4Address('5.5.5.5')
end_ip = ipaddress.IPv4Address('5.5.10.5')
for ip_int in range(int(start_ip), int(end_ip)):
    print(ipaddress.IPv4Address(ip_int))
    print "(+) Sending request with requesocks..."
    session = requesocks.session()
    session.proxies = {'http': 'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    r = session.get(ipaddress.IPv4Address(ip_int))


def main():
    print "Running tests..."


if __name__ == "__main__":
    main()