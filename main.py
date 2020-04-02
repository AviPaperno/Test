import upip
import socket
import mylib
import time
import usnmp

mylib.do_connect('room 6','66666666')



def test_time(IP,PORT,COMMUNITY = 'public'):

    oids_pat = ['1.3.6.1.2.1.1.3.0']

	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.settimeout(1)
    greq = usnmp.SnmpPacket(type=usnmp.SNMP_GETNEXTREQUEST, community=agent_community, id=time.ticks_us())
    for oid in oids_pat:
        greq.varbinds[oid] = None

     s.sendto(greq.tobytes(), (agent_ip, agent_port))
     d = s.recvfrom(1024)
        
        #decode the response
     gresp = usnmp.SnmpPacket(d[0])

     print(gresp)

