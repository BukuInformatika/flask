import mindwave,time

headset = mindwave.Headset('COM4', '1425')
time.sleep(1)

headset.connect()
print "Connecting..."

while headset.status != 'connected':
	time.sleep(1)
	if headset.status == 'standby':
		headset.connect()
		print "Retrying connect..."
print "Connected."

while True:
	print headset.raw_value
	time.sleep(1)