headset.connect()
print "Connecting..."

while headset.status != 'connected':
	time.sleep(1)
	if headset.status == 'standby':
		headset.connect()
		print "Retrying connect..."
print "Connected."