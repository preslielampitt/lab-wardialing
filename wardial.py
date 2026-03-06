import requests

def is_server_at_hostname(hostname):
    '''
    A hostname is a generic word for either an IP address or a domain name.
    Your function should return True if `requests.get` is successfully able to connect to the input hostname.

    >>> is_server_at_hostname('google.com')
    True
    >>> is_server_at_hostname('www.google.com')
    True
    >>> is_server_at_hostname('GoOgLe.CoM')
    True
    >>> is_server_at_hostname('142.250.68.110')  # IP address for google.com
    True

    >>> is_server_at_hostname('facebook.com')
    True
    >>> is_server_at_hostname('www.facebook.com')
    True
    >>> is_server_at_hostname('FACEBOOK.com')
    True

    # These test cases below use made up hostnames and so should always pass
    # (i.e. your function will always return `False`)
    # even when the internet isn't working.
    >>> is_server_at_hostname('google.commmm')
    False
    >>> is_server_at_hostname('aslkdjlaksjdlaksjdlakj')
    False
    >>> is_server_at_hostname('142.250.68.110.1.3.4.5')
    False
    >>> is_server_at_hostname('8.8.8.8')
    False
    '''
    try:
        url = 'http://' + hostname
        r = requests.get(url, timeout=5.0)
        return True
    except:
        return False


def increment_ip(ip):
    '''
    Return the "next" IPv4 address.

    >>> increment_ip('1.2.3.4')
    '1.2.3.5'
    >>> increment_ip('1.2.3.255')
    '1.2.4.0'
    >>> increment_ip('0.0.0.0')
    '0.0.0.1'
    >>> increment_ip('0.0.0.255')
    '0.0.1.0'
    >>> increment_ip('0.0.255.255')
    '0.1.0.0'
    >>> increment_ip('0.255.255.255')
    '1.0.0.0'
    >>> increment_ip('0.255.5.255')
    '0.255.6.0'
    >>> increment_ip('255.255.255.255')
    '0.0.0.0'
    '''
    parts = ip.split('.')
    nums = [int(x) for x in parts]

    for i in range(3, -1, -1):
        nums[i] += 1
        if nums[i] <= 255:
            break
        else:
            nums[i] = 0
    
    return '.'.join(str(x) for x in nums)


def enumerate_ips(start_ip, n):
    '''
    Return a list containing the next `n` IPs beginning with `start_ip`.

    >>> list(enumerate_ips('192.168.1.0', 2))
    ['192.168.1.0', '192.168.1.1']

    >>> list(enumerate_ips('8.8.8.8', 10))
    ['8.8.8.8', '8.8.8.9', '8.8.8.10', '8.8.8.11', '8.8.8.12', '8.8.8.13', '8.8.8.14', '8.8.8.15', '8.8.8.16', '8.8.8.17']

    # This test ensures that you are properly handling "wrap around"
    #
    >>> list(enumerate_ips('192.168.0.255', 2))
    ['192.168.0.255', '192.168.1.0']

    The following tests ensure that the correct number of ips get returned.

    >>> len(list(enumerate_ips('8.8.8.8', 10)))
    10
    >>> len(list(enumerate_ips('8.8.8.8', 1000)))
    1000
    >>> len(list(enumerate_ips('8.8.8.8', 100000)))
    100000
    '''
    parts = start_ip.split('.')
    nums = [int(x) for x in parts]
    
    next_ips = [start_ip]
    i = 1
    while i < n:
        for j in range(3, -1, -1):
            nums[j] += 1
            if nums[j] <= 255:
                break
            else:
                nums[j] = 0
        next_ip = '.'.join(str(x) for x in nums)
        next_ips.append(next_ip)
        i += 1
    
    return next_ips

# ensures the code only gets run when the file is run as a script
# the code will not be run when the file is run as doctests
if __name__ == '__main__':
    dprk_ips = enumerate_ips('175.45.176.0', 1024)

    dprk_ips_with_servers = []
    for ip in dprk_ips:
        print("Processing ip address:" + ip)
        connected = is_server_at_hostname(ip)
        print("Does the ip address have a web server? " + str(connected))
        if connected == True:
            dprk_ips_with_servers += [ip]


    print('dprk_ips_with_servers=', dprk_ips_with_servers)
