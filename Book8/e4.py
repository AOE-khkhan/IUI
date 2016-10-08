from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


l1 = [['::'], ['::1'], ['0.0.0.0'], ['0.0.0.0'], ['100BaseTX'], ['10Base2'], ['10Base5'], ['10BaseT'], ['127.0.0.1'], ['255.255.255.255'], ['802.11', 'frame', 'format'], ['802.5', 'data', 'frame'], ['802.5', 'token', 'frame'], ['abrupt', 'connection', 'release'], ['abrupt', 'connection', 'release'], ['Additive', 'Increase', 'Multiplicative', 'Decrease', '(AIMD)'], ['address'], ['address', 'learning'], ['Address', 'Resolution', 'Protocol'], ['adhoc', 'network'], ['AF_INET'], ['AF_INET6'], ['AF_UNSPEC'], ['AIMD'], ['ALG'], ['ALOHA'], ['Alternating', 'Bit', 'Protocol'], ['anycast'], ['API'], ['Application', 'layer'], ['Application', 'Level', 'Gateway'], ['ARP'], ['ARP'], ['ARP', 'cache'], ['ARPANET'], ['ascii'], ['ASN.1'], ['ATM'], ['Base64', 'encoding'], ['Basic', 'Service', 'Set', '(BSS)'], ['beacon', 'frame', '(802.11)'], ['BGP'], ['BGP'], ['BGP', 'Adj-RIB-In'], ['BGP', 'Adj-RIB-Out'], ['BGP', 'decision', 'process'], ['BGP', 'KEEPALIVE'], ['BGP', 'local-preference'], ['BGP', 'nexthop'], ['BGP', 'NOTIFICATION'], ['BGP', 'OPEN'], ['BGP', 'peer'], ['BGP', 'RIB'], ['BGP', 'UPDATE'], ['binary', 'exponential', 'back-off', '(CSMA/CD)'], ['bit', 'stuf\xef\xac\x81ng'], ['BNF'], ['Border', 'Gateway', 'Protocol'], ['bridge'], ['broadcast'], ['BSS'], ['Carrier', 'Sense', 'Multiple', 'Access'], ['ance'], ['tion'], ['character', 'stuf\xef\xac\x81ng'], ['Checksum', 'computation'], ['CIDR'], ['Class', 'A', 'IPv4', 'address'], ['Class', 'B', 'IPv4', 'address'], ['Class', 'C', 'IPv4', 'address'], ['Classless', 'Interdomain', 'Routing'], ['Clear', 'To', 'Send'], ['Cold', 'potato', 'routing'], ['collision'], ['collision', 'detection'], ['collision', 'domain'], ['con\xef\xac\x81rmed', 'connectionless', 'service'], ['congestion', 'collapse'], ['connection', 'establishment'], ['connection-oriented', 'service'], ['Connectionless', 'service'], ['connectionless', 'service'], ['count', 'to', 'in\xef\xac\x81nity'], ['CSMA'], ['CSMA', '(non-persistent)'], ['CSMA', '(persistent)'], ['CSMA/CA'], ['CSMA/CD'], ['CTS'], ['CTS', 'frame', '(802.11)'], ['cumulative', 'acknowledgements'], ['customer-provider', 'peering', 'relationship'], ['datagram'], ['Datalink', 'layer'], ['delayed', 'acknowledgements'], ['Denial', 'of', 'Service'], ['DHCP'], ['DHCPv6'], ['dial-up', 'line'], ['DIFS'], ['Distance', 'vector'], ['DNS'], ['DNS', 'message', 'format'], ['Dynamic', 'Host', 'Con\xef\xac\x81guration', 'Protocol'], ['EAP'], ['eBGP'], ['eBGP'], ['EGP'], ['EIFS'], ['EIGRP'], ['electrical', 'cable'], ['email', 'message', 'format'], ['Ending', 'Delimiter', '(Token', 'Ring)'], ['Ethernet', 'bridge'], ['Ethernet', 'DIX', 'frame', 'format'], ['Ethernet', 'hub'], ['Ethernet', 'switch'], ['Ethernet', 'Type', '\xef\xac\x81eld'], ['EtherType'], ['exponential', 'backoff'], ['export', 'policy'], ['Extended', 'Inter', 'Frame', 'Space'], ['Extensible', 'Authentication', 'Protocol'], ['Fairness'], ['Fast', 'Ethernet'], ['FDM'], ['\xef\xac\x81rewall'], ['Five', 'layers', 'reference', 'model'], ['frame'], ['frame'], ['Frame-Relay'], ['framing'], ['Frequency', 'Division', 'Multiplexing'], ['FTP'], ['ftp'], ['getaddrinfo'], ['go-back-n'], ['graceful', 'connection', 'release'], ['graceful', 'connection', 'release'], ['Hello', 'message'], ['hidden', 'station', 'problem'], ['hop-by-hop', 'forwarding'], ['hosts.txt'], ['hosts.txt'], ['Hot', 'potato', 'routing'], ['HTML'], ['HTTP'], ['hub'], ['IANA'], ['iBGP'], ['iBGP'], ['ICANN'], ['ICMP'], ['IETF'], ['IGP'], ['IGRP'], ['IMAP'], ['import', 'policy'], ['independent', 'network'], ['infrastructure', 'network'], ['interdomain', 'routing', 'policy'], ['Internet'], ['internet'], ['Internet', 'Control', 'Message', 'Protocol'], ['inverse', 'query'], ['IP'], ['IP', 'options'], ['IP', 'pre\xef\xac\x81x'], ['IP', 'subnet'], ['IPv4'], ['IPv4', 'fragmentation', 'and', 'reassembly'], ['IPv6'], ['IPv6', 'fragmentation'], ['IS-IS'], ['ISN'], ['ISO'], ['ISO-3166'], ['ISP'], ['ITU'], ['IXP'], ['jamming'], ['jumbogram'], ['label'], ['LAN'], ['large', 'window'], ['leased', 'line'], ['Link', 'Local', 'address'], ['link', 'local', 'IPv4', 'addresses'], ['link-state', 'routing'], ['LLC'], ['Logical', 'Link', 'Control', '(LLC)'], ['loopback', 'interface'], ['MAC', 'address', 'learning'], ['MAC', 'address', 'table', '(Ethernet', 'switch)'], ['MAN'], ['man-in-the-middle', 'attack'], ['Manchester', 'encoding'], ['max-min', 'fairness'], ['Maximum', 'Segment', 'Lifetime', '(MSL)'], ['maximum', 'segment', 'lifetime', '(MSL)'], ['Maximum', 'Segment', 'Size'], ['Maximum', 'Transmission', 'Unit'], ['Maximum', 'Transmission', 'Unit', '(MTU)'], ['message-mode', 'data', 'transfer'], ['Middlebox'], ['MIME'], ['MIME', 'document'], ['minicomputer'], ['modem'], ['Monitor', 'station'], ['monomode', 'optical', '\xef\xac\x81ber'], ['MSS'], ['MSS'], ['MTU'], ['Multi-Exit', 'Discriminator', '(MED)'], ['multicast'], ['multihomed', 'host'], ['multihomed', 'network'], ['multimode', 'optical', '\xef\xac\x81ber'], ['Nagle', 'algorithm'], ['nameserver'], ['NAT'], ['NAT'], ['NAT66'], ['NBMA'], ['NBMA'], ['Neighbour', 'Discovery', 'Protocol'], ['Network', 'Address', 'Translation'], ['Network', 'Information', 'Center'], ['Network', 'layer'], ['network-byte', 'order'], ['NFS'], ['Non-Broadcast', 'Multi-Access', 'Networks'], ['non-persistent', 'CSMA'], ['NTP'], ['Open', 'Shortest', 'Path', 'First'], ['optical', '\xef\xac\x81ber'], ['ordering', 'of', 'SDUs'], ['Organisation', 'Unique', 'Identi\xef\xac\x81er'], ['OSI'], ['OSI', 'reference', 'model'], ['OSPF'], ['OSPF'], ['OSPF', 'area'], ['OSPF', 'Designated', 'Router'], ['OUI'], ['packet'], ['packet'], ['packet', 'radio'], ['packet', 'size', 'distribution'], ['Path', 'MTU', 'discovery'], ['PBL'], ['peer-to-peer'], ['persistence', 'timer'], ['persistent', 'CSMA'], ['Physical', 'layer'], ['piggybacking'], ['ping'], ['ping6'], ['Point-to-Point', 'Protocol'], ['POP'], ['Post', 'Of\xef\xac\x81ce', 'Protocol'], ['PPP'], ['private', 'IPv4', 'addresses'], ['Provider', 'Aggregatable', 'address'], ['Provider', 'Independent', 'address'], ['provision', 'of', 'a', 'byte', 'stream', 'service'], ['Reference', 'models'], ['reliable', 'connectionless', 'service'], ['Request', 'To', 'Send'], ['resolver'], ['RFC', '1032'], ['RFC', '1032'], ['RFC', '1035'], ['RFC', '1035'], ['RFC', '1035'], ['RFC', '1035'], ['RFC', '1042'], ['RFC', '1042'], ['RFC', '1055'], ['RFC', '1055'], ['RFC', '1071'], ['RFC', '1071'], ['RFC', '1071'], ['RFC', '1094'], ['RFC', '1122'], ['RFC', '1122'], ['RFC', '1122'], ['RFC', '1122'], ['RFC', '1122'], ['RFC', '1122'], ['RFC', '1122'], ['RFC', '1144'], ['RFC', '1144'], ['RFC', '1149'], ['RFC', '1149'], ['RFC', '1169'], ['RFC', '1169'], ['RFC', '1191'], ['RFC', '1191'], ['RFC', '1195'], ['RFC', '1195'], ['RFC', '1258'], ['RFC', '1258'], ['RFC', '1305'], ['RFC', '1321'], ['RFC', '1321'], ['RFC', '1323'], ['RFC', '1323'], ['RFC', '1323'], ['RFC', '1323'], ['RFC', '1323'], ['RFC', '1347'], ['RFC', '1347'], ['RFC', '1350'], ['RFC', '1518'], ['RFC', '1518'], ['RFC', '1518'], ['RFC', '1519'], ['RFC', '1519'], ['RFC', '1519'], ['RFC', '1542'], ['RFC', '1542'], ['RFC', '1548'], ['RFC', '1548'], ['RFC', '1550'], ['RFC', '1550'], ['RFC', '1561'], ['RFC', '1561'], ['RFC', '1621'], ['RFC', '1621'], ['RFC', '1624'], ['RFC', '1624'], ['RFC', '1631'], ['RFC', '1631'], ['RFC', '1661'], ['RFC', '1661'], ['RFC', '1661'], ['RFC', '1662'], ['RFC', '1662'], ['RFC', '1710'], ['RFC', '1710'], ['RFC', '1710'], ['RFC', '1738'], ['RFC', '1738'], ['RFC', '1738'], ['RFC', '1752'], ['RFC', '1752'], ['RFC', '1752'], ['RFC', '1812'], ['RFC', '1812'], ['RFC', '1812'], ['RFC', '1819'], ['RFC', '1819'], ['RFC', '1889'], ['RFC', '1896'], ['RFC', '1896'], ['RFC', '1918'], ['RFC', '1918'], ['RFC', '1918'], ['RFC', '1918'], ['RFC', '1918'], ['RFC', '1939'], ['RFC', '1939'], ['RFC', '1939'], ['RFC', '1939'], ['RFC', '1939'], ['RFC', '1945'], ['RFC', '1945'], ['RFC', '1945'], ['RFC', '1945'], ['RFC', '1948'], ['RFC', '1948'], ['RFC', '1951'], ['RFC', '1951'], ['RFC', '1981'], ['RFC', '1981'], ['RFC', '20'], ['RFC', '20'], ['RFC', '20'], ['RFC', '2001'], ['RFC', '2003'], ['RFC', '2003'], ['RFC', '2018'], ['RFC', '2018'], ['RFC', '2045'], ['RFC', '2045'], ['RFC', '2045'], ['RFC', '2045'], ['RFC', '2046'], ['RFC', '2046'], ['RFC', '2046'], ['RFC', '2050'], ['RFC', '2050'], ['RFC', '2080'], ['RFC', '2080'], ['RFC', '2080'], ['RFC', '2082'], ['RFC', '2082'], ['RFC', '2131'], ['RFC', '2131'], ['RFC', '2140'], ['RFC', '2140'], ['RFC', '2140'], ['RFC', '2225'], ['RFC', '2225'], ['RFC', '2328'], ['RFC', '2328'], ['RFC', '2328'], ['RFC', '2328'], ['RFC', '2332'], ['RFC', '2332'], ['RFC', '2364'], ['RFC', '2364'], ['RFC', '2368'], ['RFC', '2453'], ['RFC', '2453'], ['RFC', '2453'], ['RFC', '2460'], ['RFC', '2460'], ['RFC', '2460'], ['RFC', '2464'], ['RFC', '2464'], ['RFC', '2507'], ['RFC', '2507'], ['RFC', '2516'], ['RFC', '2516'], ['RFC', '2581'], ['RFC', '2581'], ['RFC', '2616'], ['RFC', '2616'], ['RFC', '2616'], ['RFC', '2616'], ['RFC', '2616'], ['RFC', '2616'], ['RFC', '2617'], ['RFC', '2617'], ['RFC', '2622'], ['RFC', '2622'], ['RFC', '2675'], ['RFC', '2711'], ['RFC', '2766'], ['RFC', '2766'], ['RFC', '2821'], ['RFC', '2854'], ['RFC', '2854'], ['RFC', '2920'], ['RFC', '2965'], ['RFC', '2988'], ['RFC', '2988'], ['RFC', '2988'], ['RFC', '2988'], ['RFC', '2991'], ['RFC', '3021'], ['RFC', '3021'], ['RFC', '3022'], ['RFC', '3022'], ['RFC', '3031'], ['RFC', '3031'], ['RFC', '3168'], ['RFC', '3168'], ['RFC', '3168'], ['RFC', '3168'], ['RFC', '3187'], ['RFC', '3234'], ['RFC', '3234'], ['RFC', '3235'], ['RFC', '3235'], ['RFC', '3309'], ['RFC', '3309'], ['RFC', '3309'], ['RFC', '3315'], ['RFC', '3315'], ['RFC', '3330'], ['RFC', '3360'], ['RFC', '3360'], ['RFC', '3390'], ['RFC', '3390'], ['RFC', '3390'], ['RFC', '3490'], ['RFC', '3501'], ['RFC', '3501'], ['RFC', '3501'], ['RFC', '3513'], ['RFC', '3513'], ['RFC', '3596'], ['RFC', '3596'], ['RFC', '3748'], ['RFC', '3748'], ['RFC', '3782'], ['RFC', '3782'], ['RFC', '3819'], ['RFC', '3819'], ['RFC', '3828'], ['RFC', '3927'], ['RFC', '3927'], ['RFC', '3927'], ['RFC', '3931'], ['RFC', '3931'], ['RFC', '3971'], ['RFC', '3971'], ['RFC', '3972'], ['RFC', '3972'], ['RFC', '3986'], ['RFC', '3986'], ['RFC', '3986'], ['RFC', '4033'], ['RFC', '4033'], ['RFC', '4151'], ['RFC', '4193'], ['RFC', '4193'], ['RFC', '4251'], ['RFC', '4251'], ['RFC', '4253'], ['RFC', '4264'], ['RFC', '4264'], ['RFC', '4271'], ['RFC', '4271'], ['RFC', '4271'], ['RFC', '4287'], ['RFC', '4291'], ['RFC', '4291'], ['RFC', '4301'], ['RFC', '4301'], ['RFC', '4302'], ['RFC', '4302'], ['RFC', '4303'], ['RFC', '4303'], ['RFC', '4340'], ['RFC', '4443'], ['RFC', '4443'], ['RFC', '4443'], ['RFC', '4451'], ['RFC', '4451'], ['RFC', '4456'], ['RFC', '4456'], ['RFC', '4614'], ['RFC', '4614'], ['RFC', '4632'], ['RFC', '4634'], ['RFC', '4648'], ['RFC', '4648'], ['RFC', '4648'], ['RFC', '4822'], ['RFC', '4822'], ['RFC', '4838'], ['RFC', '4838'], ['RFC', '4861'], ['RFC', '4861'], ['RFC', '4862'], ['RFC', '4862'], ['RFC', '4870'], ['RFC', '4870'], ['RFC', '4871'], ['RFC', '4871'], ['RFC', '4941'], ['RFC', '4941'], ['RFC', '4944'], ['RFC', '4944'], ['RFC', '4944'], ['RFC', '4952'], ['RFC', '4952'], ['RFC', '4953'], ['RFC', '4953'], ['RFC', '4954'], ['RFC', '4954'], ['RFC', '4954'], ['RFC', '4963'], ['RFC', '4963'], ['RFC', '4963'], ['RFC', '4966'], ['RFC', '4966'], ['RFC', '4987'], ['RFC', '4987'], ['RFC', '5004'], ['RFC', '5004'], ['RFC', '5065'], ['RFC', '5065'], ['RFC', '5068'], ['RFC', '5068'], ['RFC', '5072'], ['RFC', '5072'], ['RFC', '5095'], ['RFC', '5095'], ['RFC', '5227'], ['RFC', '5227'], ['RFC', '5234'], ['RFC', '5234'], ['RFC', '5234'], ['RFC', '5246'], ['RFC', '5321'], ['RFC', '5321'], ['RFC', '5321'], ['RFC', '5321'], ['RFC', '5322'], ['RFC', '5322'], ['RFC', '5322'], ['RFC', '5322'], ['RFC', '5340'], ['RFC', '5340'], ['RFC', '5340'], ['RFC', '5531'], ['RFC', '5598'], ['RFC', '5598'], ['RFC', '5646'], ['RFC', '5646'], ['RFC', '5681'], ['RFC', '5681'], ['RFC', '5681'], ['RFC', '5681'], ['RFC', '5735'], ['RFC', '5735'], ['RFC', '5795'], ['RFC', '5795'], ['RFC', '5880'], ['RFC', '5890'], ['RFC', '5890'], ['RFC', '6068'], ['RFC', '6068'], ['RFC', '6144'], ['RFC', '6144'], ['RFC', '6265'], ['RFC', '6265'], ['RFC', '6274'], ['RFC', '6274'], ['RFC', '768'], ['RFC', '768'], ['RFC', '789'], ['RFC', '789'], ['RFC', '791'], ['RFC', '791'], ['RFC', '791'], ['RFC', '791'], ['RFC', '791'], ['RFC', '791'], ['RFC', '791'], ['RFC', '791'], ['RFC', '791'], ['150'], ['150'], ['RFC', '792'], ['RFC', '792'], ['RFC', '793'], ['RFC', '793'], ['RFC', '793'], ['RFC', '793'], ['RFC', '793'], ['RFC', '793'], ['RFC', '793'], ['RFC', '793'], ['RFC', '793'], ['RFC', '793'], ['RIP'], ['RIP'], ['RIR'], ['Robustness', 'principle'], ['root', 'nameserver'], ['round-trip-time'], ['router'], ['Routing', 'Information', 'Protocol'], ['RPC'], ['RTS'], ['RTS', 'frame', '(802.11)'], ['SDU'], ['SDU', '(Service', 'Data', 'Unit)'], ['segment'], ['segment'], ['selective', 'acknowledgements'], ['RFC', '813'], ['RFC', '813'], ['RFC', '819'], ['RFC', '819'], ['RFC', '821'], ['RFC', '821'], ['RFC', '821'], ['RFC', '822'], ['RFC', '826'], ['RFC', '826'], ['RFC', '826'], ['RFC', '854'], ['RFC', '879'], ['RFC', '879'], ['RFC', '893'], ['RFC', '893'], ['RFC', '894'], ['RFC', '894'], ['RFC', '894'], ['RFC', '896'], ['RFC', '896'], ['RFC', '896'], ['RFC', '952'], ['RFC', '952'], ['RFC', '959'], ['RFC', '959'], ['RFC', '959'], ['RFC', '959'], ['RFC', '959'], ['RFC', '974'], ['RFC', '974'], ['selective', 'repeat'], ['sendto'], ['sequence', 'number'], ['Serial', 'Line', 'IP'], ['service', 'access', 'point'], ['Service', 'Data', 'Unit'], ['service', 'primitives'], ['Service', 'Set', 'Identity', '(SSID)'], ['shared-cost', 'peering', 'relationship'], ['Short', 'Inter', 'Frame', 'Spacing'], ['sibling', 'peering', 'relationship'], ['SIFS'], ['SLAC'], ['slot', 'time', '(Ethernet)'], ['slotted', 'ALOHA'], ['slotTime', '(CSMA/CA)'], ['SMTP'], ['SNMP'], ['SOCK_DGRAM'], ['SOCK_STREAM'], ['socket'], ['socket'], ['socket.bind'], ['socket.close'], ['socket.connect'], ['socket.recv'], ['socket.recvfrom'], ['socket.send'], ['socket.shutdown'], ['source', 'routing'], ['speed', 'of', 'light'], ['split', 'horizon'], ['split', 'horizon', 'with', 'poison', 'reverse'], ['spoofed', 'packet'], ['SSH'], ['SSID'], ['standard', 'query'], ['Starting', 'Delimiter', '(Token', 'Ring)'], ['Stateless', 'Address', 'Con\xef\xac\x81guration'], ['stream-mode', 'data', 'transfer'], ['stub', 'domain'], ['stuf\xef\xac\x81ng', '(bit)'], ['stuf\xef\xac\x81ng', '(character)'], ['subnet', 'mask'], ['switch'], ['switch'], ['SYN', 'cookie'], ['SYN', 'cookies'], ['TCB'], ['TCP'], ['TCP'], ['TCP', 'Connection', 'establishment'], ['TCP', 'connection', 'release'], ['TCP', 'fast', 'retransmit'], ['TCP', 'header'], ['TCP', 'Initial', 'Sequence', 'Number'], ['TCP', 'MSS'], ['TCP', 'Options'], ['TCP', 'RST'], ['TCP', 'SACK'], ['TCP', 'selective', 'acknowledgements'], ['TCP', 'self', 'clocking'], ['TCP', 'SYN'], ['TCP', 'SYN+ACK'], ['TCP/IP'], ['TCP/IP', 'reference', 'model'], ['telnet'], ['Tier-1', 'ISP'], ['Time', 'Division', 'Multiplexing'], ['Time', 'To', 'Live', '(IP)'], ['time-sequence', 'diagram'], ['TLD'], ['TLS'], ['Token', 'Holding', 'Time'], ['Token', 'Ring', 'data', 'frame'], ['Token', 'Ring', 'Monitor'], ['Token', 'Ring', 'token', 'frame'], ['traceroute'], ['traceroute6'], ['transit', 'domain'], ['Transmission', 'Control', 'Block'], ['transport', 'clock'], ['Transport', 'layer'], ['two-way', 'connectivity'], ['UDP'], ['UDP'], ['UDP', 'Checksum'], ['UDP', 'segment'], ['unicast'], ['Unique', 'Local', 'Unicast', 'IPv6'], ['unreliable', 'connectionless', 'service'], ['virtual', 'circuit'], ['Virtual', 'LAN'], ['VLAN'], ['vnc'], ['W3C'], ['WAN'], ['Wavelength', 'Division', 'Multiplexing'], ['WDM'], ['WiFi'], ['X.25'], ['X11'], ['XML']]
l2 = [' 160', ' 160', ' 146', ' 155', ' 234', ' 233', ' 233', ' 233', ' 146', ' 155', ' 242', ' 227', ' 227', ' 18', ' 86', ' 109', ' 11', ' 235', ' 154', ' 242', ' 56', ' 56', ' 56', ' 249', ' 169', ' 216', ' 72', ' 249', ' 249', ' 23', ' 169', ' 154', ' 249', ' 154', ' 249', ' 249', ' 249', ' 249', ' 41', ' 242', ' 245', ' 178', ' 249', ' 181', ' 181', ' 187', ' 180', ' 187', ' 183', ' 180', ' 180', ' 179', ' 181', ' 180', ' 221', ' 212', ' 249', ' 178', ' 234', ' 249', ' 242', ' 217', ' 222', ' 218', ' 213', ' 88', ' 249', ' 142', ' 142', ' 142', ' 144', ' 225', ' 191', ' 215', ' 219', ' 233', ' 13', ' 107', ' 16', ' 16', ' 12', ' 13', ' 135', ' 217', ' 218', ' 217', ' 222', ' 218', ' 225', ' 244', ' 76', ' 177', ' 129', ' 22', ' 102', ' 93', ' 155', ' 166', ' 249', ' 222', ' 133', ' 249', ' 34', ' 155', ' 229', ' 185', ' 250', ' 250', ' 222', ' 250', ' 20', ' 38', ' 227', ' 234', ' 231', ' 233', ' 234', ' 230', ' 230', ' 102', ' 178', ' 222', ' 229', ' 107', ' 234', ' 215', ' 166', ' 20', ' 22', ' 250', ' 250', ' 212', ' 215', ' 250', ' 250', ' 56', ' 75', ' 19', ' 86', ' 137', ' 225', ' 129', ' 32', ' 250', ' 190', ' 250', ' 250', ' 250', ' 250', ' 185', ' 250', ' 250', ' 150', ' 250', ' 250', ' 250', ' 250', ' 178', ' 242', ' 242', ' 178', ' 250', ' 250', ' 150', ' 250', ' 250', ' 150', ' 142', ' 142', ' 250', ' 149', ' 251', ' 163', ' 251', ' 251', ' 251', ' 251', ' 251', ' 251', ' 251', ' 219', ' 162', ' 131', ' 251', ' 99', ' 251', ' 160', ' 146', ' 137', ' 232', ' 232', ' 185', ' 235', ' 235', ' 251', ' 155', ' 212', ' 107', ' 83', ' 79', ' 94', ' 148', ' 149', ' 17', ' 166', ' 251', ' 251', ' 251', ' 251', ' 228', ' 20', ' 94', ' 251', ' 148', ' 191', ' 251', ' 142', ' 145', ' 20', ' 98', ' 251', ' 168', ' 251', ' 169', ' 128', ' 251', ' 166', ' 168', ' 32', ' 22', ' 251', ' 252', ' 128', ' 218', ' 252', ' 172', ' 20', ' 13', ' 230', ' 252', ' 23', ' 172', ' 252', ' 172', ' 173', ' 230', ' 22', ' 252', ' 216', ' 99', ' 153', ' 252', ' 30', ' 79', ' 217', ' 22', ' 81', ' 152', ' 165', ' 228', ' 252', ' 45', ' 228', ' 146', ' 159', ' 159', ' 81', ' 20', ' 13', ' 225', ' 252', ' 32', ' 264', ' 33', '35', ' 249', ' 264', ' 245', ' 264', ' 229', ' 265', ' 88', ' 114', ' 265', ' 252', ' 23', ' 90', ' 91', ' 95', ' 103', ' 231', ' 265', ' 229', ' 265', ' 81', ' 265', ' 5', ' 265', ' 153', ' 265', ' 172', ' 265', ' 92', ' 265', ' 252', ' 114', ' 265', ' 95', ' 99', '101', ' 105', ' 265', ' 158', ' 265', ' 116', ' 144', ' 249', ' 265', ' 143', ' 145', ' 265', ' 11', ' 265', ' 229', ' 265', ' 158', ' 265', ' 158', ' 265', ' 158', ' 265', ' 157', ' 265', ' 158', ' 265', ' 127', ' 154', ' 265', ' 229', ' 265', ' 158', ' 161', ' 265', ' 48', ' 54', ' 265', ' 157', ' 158', ' 265', ' 110', ' 143', ' 265', ' 158', ' 265', ' 265', ' 41', ' 265', ' 147', ' 160', ' 168', ' 183', ' 265', ' 45', ' 46', ' 64', ' 252', ' 266', ' 50', ' 51', ' 64', ' 266', ' 92', ' 266', ' 162', ' 266', ' 165', ' 266', ' 28', ' 41', ' 264', ' 117', ' 187', ' 266', ' 104', ' 266', ' 40', ' 41', ' 251', ' 266', ' 40', ' 41', ' 266', ' 144', ' 266', ' 171', ' 172', ' 266', ' 171', ' 266', ' 156', ' 266', ' 97', ' 101', ' 266', ' 156', ' 266', ' 172', ' 175', ' 252', ' 266', ' 156', ' 266', ' 230', ' 266', ' 266', ' 171', ' 252', ' 266', ' 161', '163', ' 266', ' 232', ' 266', ' 162', ' 266', ' 230', ' 266', ' 104', ' 266', ' 44', ' 50', '53', ' 65', ' 250', ' 266', ' 54', ' 266', ' 178', ' 266', ' 162', ' 163', ' 169', ' 266', ' 43', ' 41', ' 266', ' 114', ' 266', ' 94', ' 100', '102', ' 267', ' 267', ' 143', ' 267', ' 168', ' 267', ' 186', ' 267', ' 90', ' 110', ' 118', ' 267', ' 48', ' 166', ' 267', ' 169', ' 267', ' 71', ' 114', ' 267', ' 166', ' 267', ' 267', ' 95', ' 267', ' 112', ' 117', ' 267', ' 267', ' 45', ' 250', ' 267', ' 158', ' 267', ' 36', ' 267', ' 229', ' 267', ' 113', ' 125', ' 127', ' 267', ' 267', ' 147', ' 160', ' 267', ' 186', ' 267', ' 166', ' 267', ' 166', ' 267', ' 48', ' 54', ' 267', ' 35', ' 267', ' 48', ' 160', ' 268', ' 47', ' 268', ' 252', ' 192', ' 268', ' 178', ' 180', ' 268', ' 48', ' 160', ' 268', ' 164', ' 268', ' 164', ' 268', ' 164', ' 268', ' 268', ' 164', ' 165', ' 268', ' 191', ' 268', ' 185', ' 268', ' 89', ' 268', ' 249', ' 114', ' 41', ' 42', ' 268', ' 171', ' 268', ' 6', ' 268', ' 166', ' 268', ' 166', ' 268', ' 45', ' 268', ' 45', ' 268', ' 166', ' 268', ' 148', ' 162', ' 268', ' 41', ' 268', ' 95', ' 268', ' 43', ' 45', ' 268', ' 153', ' 157', ' 268', ' 169', ' 268', ' 94', ' 268', ' 191', ' 268', ' 185', ' 269', ' 45', ' 269', ' 229', ' 269', ' 163', ' 269', ' 155', ' 269', ' 29', ' 249', ' 269', ' 253', ' 43', ' 44', ' 63', ' 269', ' 38', ' 39', ' 43', ' 269', ' 172', ' 252', ' 269', ' 252', ' 38', ' 269', ' 65', ' 269', ' 110', ' 111', ' 125', ' 269', ' 146', ' 269', ' 229', ' 269', ' 262', ' 33', ' 41', ' 48', ' 269', ' 169', ' 269', ' 55', ' 269', ' 150', ' 269', ' 87', ' 264', ' 138', ' 264', ' 29', ' 91', ' 107', ' 141', ' 142', ' 144', ' 147', ' 148', '', ' 156', ' 264', ' 151', ' 264', ' 81', ' 89', '91', ' 95', ' 97', '99', ' 101', ' 102', ' 124', '', ' 170', ' 252', ' 252', ' 96', ' 252', ' 252', ' 252', ' 170', ' 252', ' 225', ' 244', ' 12', ' 252', ' 23', ' 252', ' 78', ' 103', ' 264', ' 32', ' 264', ' 63', ' 252', ' 264', ' 40', ' 154', ' 249', ' 264', ' 253', ' 94', ' 264', ' 231', ' 264', ' 232', ' 245', ' 264', ' 98', ' 107', ' 264', ' 32', ' 264', ' 44', ' 46', ' 169', ' 250', ' 264', ' 62', ' 264', ' 77', ' 56', ' 72', ' 228', ' 11', ' 12', ' 12', ' 245', ' 178', ' 222', ' 178', ' 222', ' 166', ' 221', ' 217', ' 223', ' 252', ' 252', ' 56', ' 56', ' 56', ' 252', ' 59', ' 57', ' 57', ' 57', ' 59', ' 57', ' 57', ' 131', ' 218', ' 136', ' 136', ' 252', ' 252', ' 245', ' 252', ' 227', ' 166', ' 17', ' 175', ' 212', ' 213', ' 142', ' 234', ' 252', ' 252', ' 93', ' 252', ' 89', ' 252', ' 90', ' 95', ' 103', ' 89', ' 91', ' 94', ' 94', ' 92', ' 104', ' 104', ' 105', ' 90', ' 90', ' 252', ' 23', ' 253', ' 194', ' 216', ' 147', ' 12', ' 253', ' 253', ' 228', ' 227', ' 227', ' 227', ' 153', ' 165', ' 175', ' 97', ' 83', ' 23', ' 140', ' 86', ' 253', ' 88', ' 87', ' 253', ' 160', ' 13', ' 129', ' 240', ' 240', ' 253', ' 253', ' 253', ' 215', ' 215', ' 241', ' 253', ' 253', ' 253']
print len(l1)
print len(l2)
for faf in range(len(l2)):
    tex = l1[faf]
    tex2 = l2[faf]
    if any(c.isalpha() for c in tex2) or len(tex2)>4 or tex2=='':
        continue
    print tex
    m = convert('CN5.pdf', pages=[int(tex2)+10])

    m = m.split('\n\n')
    f2 = open("xxCN5.txt",'a')
    f3 = open("yyCN5.txt",'a')
    for k in m:
        if len(k)>150:
            s = ""
            k = list(k)
            chick = []
            mac = 0
            while mac<len(k):
            #print k[mac]
                if k[mac]=='\n':
                #k[m] = " "
                    chick.append(' ')

                elif k[mac]=='-':
                    temp = mac+1
                #print "True"
                    if temp!=len(k) and k[temp]=='\n':
                    #print "True"
                        mac = mac+1
                    else:
                        chick.append(k[mac].lower())
                else:
                    chick.append(k[mac].lower())
                mac = mac+1
            k = chick

            
        
            print "".join(k).strip()
            temp = "".join(k)

            temp.strip()
            f2.write(temp)
            f2.write("\n")

            temp = temp.split(' ')
            l = []
            for cha in temp:
                #if "isymmetric" in cha: #or "pproxmia" in cha:
                #    l.append(1)
                check = 0
                for vv in tex:
                    if vv.lower() in cha and vv!='':
                        print cha
                        l.append(1)
                        check=1
                        break
                if check==0:
                    l.append(0)
            print len(temp)
            print len(l)
            lll = ",".join(str(x) for x in l)
            f3.write(lll)
            f3.write("\n")
            print "\n"
            print l
            print "\n"
    f2.close()
    f3.close()
