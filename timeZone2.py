__author__ = 'ebrecht'

try:
    import ujson as json
except:
    import json
try:
    import usocket as socket
except:
    import socket



def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

def timeZone(time, longitude = 10.900556, latitude = 48.338056):

    url = 'https://maps.googleapis.com/maps/api/timezone/json'
    url_parameter = 'timestamp={0:f}&location={1:f},{2:f}'.format(time, latitude, longitude)
    full_url = url + '?' + url_parameter
    print (full_url)
    return http_get(full_url)



if __name__ == "__main__":
    # Show window
    print('wait...')
    print (timeZone(1478708042.6730614))
