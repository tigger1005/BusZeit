import servo
import vga
import ntptime2
import timeZone
import time
import gc

__author__ = 'ebrecht'


def settime():
    while not ntptime2.settime():
        print('Keine Zeit bekommen')
        sv.set_to_fail()
        time.sleep(10)
    # Adjust with time zone
    while not timeZone.adjust_time():
        print('Keine Zeitzone bekommen')
        sv.set_to_fail()
        time.sleep(10)

# Connect to WLAN
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('test1234', '12345678')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


# Write data to text window
print('Start BusTimes')

# Initialize all
sv = servo.servo()

# Try to connect to Network
#do_connect()

# Get time from internet
settime()

print('Time is set')
print(time.localtime())
lastUpdate = time.time()

while True:
    # Trigger garbage collector
    gc.collect()

    # Time accurate?
    if time.time() - lastUpdate > 3600:
        lastUpdate = time.time()
        settime()

    # Get bus times from VGA
    timesList = vga.get_times()
    while not timesList:
        print('Keine Abfahrtzeiten bekommen')
        sv.set_to_fail()
        time.sleep(100)
        timesList = vga.get_times()

    # Trigger garbage collector
    gc.collect()

    # is list empty?
    while timesList:
        print(timesList)
        # Use 1. entry

        minutes = 2

        while minutes > 1:
            actualTime = time.localtime()
            # how many minutes left?
            minutes = vga.get_minutes(actualTime, timesList[0])
            # set servo
            sv.minutes(minutes)

        #  delete used time
        del timesList[0]
    pass
