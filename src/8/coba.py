import mindwave, time
import keyboard
import csv

headset = mindwave.Headset('COM4', '1425')
time.sleep(2)
a=0
headset.connect()
print "Connecting..."

while headset.status != 'connected':
    time.sleep(0.5)
    if headset.status == 'standby':
        headset.connect()
        print "Retrying connect..."
print "Connected."

while True:
    print "raw_value: %s : %s" % (headset.raw_value, a)
    writer.writerow({'RawValue': headset.raw_value, 'sign': a})
