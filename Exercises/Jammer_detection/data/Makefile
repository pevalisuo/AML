# CONVBIN FLAGS
#  -v	version
#  -od    include doppler frequency in rinex obs [off]
#  -os    include snr in rinex obs [off]
#  -oi    include iono correction in rinex nav header [off]
#  -ot    include time correction in rinex nav header [off]
#  -ol    include leap seconds in rinex nav header [off]

# Use the latest RTKlibExplorer from GITHub
#RTKPATHExp=/home/petri/Projects/Tuleva/RTKLIB_bin
#RTKPATH=/home/petri/Projects/Tuleva/RTKLIB_TTJ/bin
#SERIALPORT=/dev/ttyACM0
#LOGFILE=data_`date +%FT%H%M%S`


.PRECIOUS: %.24o %.obs %.nav %.sbs %.nc %.h5 %.zip %.tgz

%.obs: %.ubx
	convbin -v 3.03 -od -os -oi -ot -ol $<

%.pos: %.24o
	# $< = source
	# $@ = target
	#rnx2rtkp -x 0 -y 2 -k rtklib.conf -o $@ $< data.nav
	rnx2rtkp -x 0 -y 2 -k ../nav/gps_galileo.conf -o $@ $< ../nav/BRD400DLR_S_20242540000_01D_MN.rnx

capture:
	stty -F $(SERIALPORT) raw
	touch $(LOFGILE).ubx
	ln -s $(LOGFILE).ubx current.ubx
	cat $(SERIALPORT) | tee $(LOGFILE).ubx | tai64n > $(LOGFILE).tubx

check: 
	rsync -av jammer@192.168.241.41:petri/*.ubx .
	#tail -n 2000 current.ubx > check.ubx
	cp current.ubx  check.ubx
	$(RTKPATH)/convbin -v 3.03 -od -os -oi -ot -ol check.ubx
	$(RTKPATH)/rnx2rtkp -x 0 -y 2 -k rtklib.conf -o check.pos check.obs check.nav
	tail -n 10 check.pos


	
	
