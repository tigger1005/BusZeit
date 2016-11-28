__author__ = 'ebrecht'

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Tigger5', 'EbrechtTeci1000')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

if __name__ == "__main__":
    do_connect()
