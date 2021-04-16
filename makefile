# Microservices Project Make File
# author: umer mansoor

VIRTUALENV = $(shell which virtualenv)

clean: shutdown
	rm -fr microservices.egg-info
	rm -fr venv

venv:
	$(VIRTUALvenv) venv

install: clean venv
	source venv/Scripts/activate; python setup.py install
	source venv/Scripts/activate; python setup.py develop

launch: venv shutdown
	source venv/Scripts/activate; python  myfiles/movies.py &
	source venv/Scripts/activate; python  myfiles/showtimes.py &
	source venv/Scripts/activate; python  myfiles/bookings.py &
	source venv/Scripts/activate; python  myfiles/user.py &

shutdown:
	ps -ef | grep "myfiles/movies.py" | grep -v grep | awk '{print $$2}' 
	ps -ef | grep "myfiles/showtimes.py" | grep -v grep | awk '{print $$2}' 
	ps -ef | grep "myfiles/bookings.py" | grep -v grep | awk '{print $$2}' 
	ps -ef | grep "myfiles/user.py" | grep -v grep | awk '{print $$2}' 

