
from threading import Thread, Event
from time import sleep
from datetime import datetime

#holds tuples of client invo by UUID
client_list = {}

def disconnect_monitor():
	while True:
		for client in client_list:
			time_since_checkin = (datetime.now() - client_list[client][2]).total_seconds()
			print 'checking client:', client, 'checked in', time_since_checkin, 'ago'
			if time_since_checkin > 60:
				print client, 'lost!'
			else:
				print client, 'checking in!'
		sleep(15)

disconnect_monitor_daemon = Thread(target = disconnect_monitor)
disconnect_monitor_daemon.setDaemon = True
disconnect_monitor_daemon.start()