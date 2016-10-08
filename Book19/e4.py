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

l1 = [['accepted', 'traf\xef\xac\x81c'], ['acknowledgment', '\xef\xac\x82it'], ['action', 'dimension'], ['Active', 'Messages', '(AM)'], ['Active', 'Messages', '(AM)'], ['adaptive', 'credits'], ['adaptive', 'routing'], ['adaptive', 'routing'], ['adaptive', 'routing', 'function'], ['adaptivity'], ['all-destination', 'encoding'], ['Alpha', '21364', 'router'], ['applied', 'load'], ['arbitration', 'strategy'], ['Arctic', 'router'], ['Ariadne'], ['asynchronous', 'bus'], ['asynchronous', 'replication'], ['backplane', 'bus'], ['backtracking'], ['backtracking'], ['balanced', 'tree'], ['barrier', 'synchronization'], ['baseline', 'MIN'], ['baseline', 'permutation'], ['bidirectional', 'MIN'], ['bisection', 'bandwidth'], ['bisection', 'width'], ['bit', 'reversal', 'communication', 'pattern'], ['bit', 'reversal', 'permutation'], ['bit', 'string', 'encoding'], ['block', 'fault', 'region'], ['blocking', 'MIN'], ['blocking', 'time'], ['broadcast'], ['broadcast'], ['buffer', 'allocation'], ['buffer', 'management'], ['buffer', 'size'], ['buffered', 'wormhole', 'switching'], ['buffering'], ['buffers'], ['buffers'], ['arbiter'], ['arbitration'], ['asynchronous'], ['master'], ['synchronous'], ['butter\xef\xac\x82y', 'communication', 'pattern'], ['butter\xef\xac\x82y', 'MIN'], ['butter\xef\xac\x82y', 'permutation'], ['canonical', 'deadlocked', 'con\xef\xac\x81guration'], ['Cavallino'], ['centralized', 'arbitration'], ['centralized', 'routing'], ['chain', 'algorithm'], ['channel', 'delay'], ['channel', 'dependency'], ['channel', 'dependency', 'graph'], ['channel', 'dependency', 'graph'], ['channel', 'multiplexing', 'delay'], ['channel', 'status'], ['channel', 'wait-for', 'graph', '(CWG)'], ['channel', 'waiting', 'graph'], ['Chaos', 'router'], ['chaotic', 'routing'], ['chunks'], ['circuit', 'switching'], ['class', 'dependency'], ['class', 'dependency', 'graph'], ['coherent', 'routing', 'function'], ['coherent', 'routing', 'function'], ['collective', 'communication'], ['collective', 'communication'], ['barrier', 'synchronization'], ['broadcast'], ['complete', 'exchange'], ['gather'], ['global', 'combining'], ['gossiping'], ['hardware', 'support'], ['parallel', 'pre\xef\xac\x81x'], ['parallel', 'suf\xef\xac\x81x'], ['personalized', 'broadcast'], ['personalized', 'combining'], ['reduce'], ['reduce', 'and', 'spread'], ['scan'], ['scatter'], ['software', 'support'], ['total', 'exchange'], ['communicator'], ['compatible', 'pair'], ['complementary', 'channel'], ['complete', 'exchange'], ['compressionless', 'routing'], ['compressionless', 'routing'], ['compressionless', 'routing'], ['concentration', 'switch'], ['con\xef\xac\x81guration'], ['connected', 'graph'], ['connected', 'routing', 'algorithm'], ['connected', 'routing', 'function'], ['connected', 'routing', 'function'], ['connection', 'pattern'], ['connectivity'], ['conservative', 'switching'], ['consumption', 'assumption'], ['copying'], ['corresponding', 'channel'], ['Cray', 'T3D'], ['Cray', 'T3E'], ['crossbar'], ['crossbar', 'network'], ['crossbar', 'switch'], ['cube', 'MIN'], ['cube', 'permutation'], ['cube-connected', 'cycles'], ['cycle'], ['data', 'channel'], ['dateline', 'link'], ['de', 'Bruijn', 'network'], ['deactivated', 'node'], ['dead', 'address', '\xef\xac\x82it'], ['deadlock'], ['avoidance'], ['prevention'], ['recovery'], ['deadlock', 'buffer'], ['deadlock', 'buffer'], ['deadlock', 'freedom'], ['deadlock', 'handling'], ['deadlock', 'set'], ['deadlock-free', 'routing', 'function'], ['deadlocked', 'con\xef\xac\x81guration'], ['deadlocked', 'con\xef\xac\x81guration'], ['decreasing', 'network'], ['decreasing', 'probability', 'distribution'], ['de\xef\xac\x82ection', 'routing'], ['demand-slotted', 'round-robin'], ['depth-contention-free'], ['deterministic', 'routing'], ['deterministic', 'routing'], ['diameter'], ['digit', 'reversal', 'permutation'], ['dilated', 'MIN'], ['dimension', 'order'], ['dimension', 'reversal', '(DR)'], ['dimension', 'reversal', '(DR)'], ['dimension-order', 'routing'], ['dimension-ordered', 'chain'], ['direct', 'connect', 'module', '(DCM)'], ['direct', 'cross-dependency'], ['direct', 'cross-dependency'], ['direct', 'cross-multicast', 'dependency'], ['direct', 'dependency'], ['direct', 'dependency'], ['direct', 'multicast', 'dependency'], ['direct', 'network'], ['direct', 'network'], ['adjacent', 'node'], ['diameter'], ['external', 'channels'], ['internal', 'channel'], ['node', 'degree'], ['nodes'], ['port'], ['regular'], ['router'], ['symmetric'], ['direction', 'order', 'routing'], ['Disha'], ['Disha', 'sequential'], ['distance', 'component'], ['distance', 'span'], ['distributed', 'arbitration'], ['distributed', 'routing'], ['multiprocessor', '(DSM)'], ['distributed-memory', 'multiprocessors'], ['distribution', 'of', 'destinations'], ['distribution', 'switch'], ['double-y', 'routing'], ['DP-sft'], ['Duato\xe2\x80\x99s', 'protocol'], ['dynamic', 'fault'], ['dynamic', 'fault'], ['dynamic', 'routing'], ['e-sft'], ['e-sft'], ['eastward', 'virtual', 'network'], ['end-of-header', '\xef\xac\x82it'], ['equivalence', 'class'], ['equivalent', 'channels'], ['escape', 'channel'], ['escape', 'channel'], ['exactly-once', 'injection'], ['exchange', 'permutation'], ['94'], ['extended', 'class', 'dependency', 'graph'], ['graph'], ['external', '\xef\xac\x82ow', 'control'], ['f', '-\xef\xac\x82at', 'router'], ['Fast', 'Messages', '(FM)'], ['fat', 'tree'], ['fault', 'chain'], ['fault', 'diagnosis'], ['fault', 'model'], ['fault', 'region'], ['fault', 'ring'], ['fault', 'tolerance'], ['fault-recoverable', 'routing'], ['fault-tolerant', 'routing'], ['\xef\xac\x81nite-state', 'machine'], ['\xef\xac\x82it'], ['\xef\xac\x82it'], ['\xef\xac\x82it', 'multiplexing', 'delay'], ['\xef\xac\x82it-level', 'recovery'], ['\xef\xac\x82ow', 'control'], ['\xef\xac\x82ow', 'control'], ['forward', '\xef\xac\x82it'], ['frame'], ['frame'], ['fully', 'adaptive', 'minimal', 'routing'], ['fully', 'adaptive', 'routing'], ['fully', 'adaptive', 'routing'], ['gather'], ['generation', 'rate'], ['global', 'arbitration'], ['global', 'combining'], ['GO'], ['gossiping'], ['Hamiltonian', 'path'], ['hierarchical', 'leader-based', '(HL)'], ['high-channel', 'subnetwork'], ['hop', 'algorithms'], ['hot', 'potato', 'routing'], ['hot', 'spot'], ['hybrid', 'networks'], ['hypercube'], ['hypermesh'], ['hypernodes'], ['IBM', 'SP2', 'router'], ['identity', 'permutation'], ['increasing', 'network'], ['incremental', 'expandability'], ['indirect', 'cross-dependency'], ['indirect', 'cross-dependency'], ['indirect', 'dependency'], ['indirect', 'dependency'], ['indirect', 'multicast', 'dependency'], ['indirect', 'network'], ['indirect', 'network'], ['injection', 'limitation'], ['injection', 'rate'], ['injection', 'rate'], ['input', 'frame'], ['input-driven', 'scheduling'], ['Intel', 'Tera\xef\xac\x82ops', 'router'], ['intercommunicators'], ['interconnection', 'network'], ['interdimensional', 'virtual', 'channels'], ['internal', '\xef\xac\x82ow', 'control'], ['interval', 'routing'], ['intracommunicator'], ['inverse', 'perfect', 'shuf\xef\xac\x82e', 'permutation'], ['k-ary', 'n-cube'], ['k-neighborhood'], ['k-reachability'], ['kill', '\xef\xac\x82it'], ['knot'], ['knot', 'cycle', 'density'], ['latency'], ['latency'], ['leader'], ['distribution'], ['legal', 'con\xef\xac\x81guration'], ['legal', 'con\xef\xac\x81guration'], ['level-1', 'leader'], ['level-2', 'leader'], ['link', 'controller', '(LC)'], ['link', 'controller', '(LC)'], ['link', 'failure'], ['livelock'], ['livelock'], ['livelock', 'freedom'], ['local', 'arbitration'], ['logical', 'channel'], ['logical', 'channel'], ['low-channel', 'subnetwork'], ['mad', 'postman', 'switching'], ['mad-y'], ['mapper'], ['pattern'], ['maximally', 'adaptive', 'routing'], ['mesh-route'], ['message'], ['message', 'component'], ['message', 'envelope'], ['message', '\xef\xac\x82ow', 'control'], ['message', '\xef\xac\x82ow', 'model'], ['message', 'length'], ['message', 'pathway'], ['message-level', 'recovery'], ['messaging', 'layer'], ['micropacket'], ['backward', 'connection'], ['baseline'], ['bidirectional'], ['blocking'], ['butter\xef\xac\x82y'], ['cube'], ['dilated'], ['forward', 'connection'], ['nonblocking'], ['Omega'], ['rearrangeable'], ['stages'], ['stages'], ['turnaround', 'connection'], ['turnaround', 'routing'], ['unidirectional'], ['minimal', 'routing'], ['function'], ['misrouting'], ['misrouting'], ['buffered', 'mode'], ['ready', 'mode'], ['standard', 'mode'], ['synchronous', 'mode'], ['multicast'], ['multicast', 'dependency'], ['multicast', 'latency'], ['multicast', 'routing'], ['multicast', 'set'], ['multicast', 'tree'], ['multicomputers'], ['multipath', 'network'], ['multiphase', 'routing'], ['multiphase', 'routing'], ['multiple-region', 'bit', 'string', 'encoding'], ['multiple-region', 'stride', 'encoding'], ['multiplexed', 'transfer'], ['(MIN)'], ['(MIN)'], ['Myrinet'], ['n-dimensional', 'mesh'], ['negative-\xef\xac\x81rst', 'routing'], ['negative-\xef\xac\x81rst', 'routing'], ['negative-hop', 'routing'], ['network', 'capacity'], ['network', 'con\xef\xac\x81guration'], ['network', 'latency'], ['network', 'of', 'workstations', '(NOW)'], ['no-farther', 'paths'], ['no-load', 'message', 'latency'], ['node', 'failure'], ['node', 'size'], ['nonblocking', 'MIN'], ['nonminimal', 'routing'], ['nonmultiplexed', 'transfer'], ['nonuniform', 'memory', 'access', '(NUMA)'], ['normalized', 'bandwidth'], ['north-last', 'routing'], ['oblivious', 'routing'], ['offered', 'traf\xef\xac\x81c'], ['Omega', 'network'], ['opt-y', 'routing'], ['optimal', 'multicast', 'cycle', '(OMC)'], ['optimal', 'multicast', 'path', '(OMP)'], ['optimal', 'multicast', 'tree', '(OMT)'], ['optimistic', 'switching'], ['origin-based', 'routing'], ['output', 'frame'], ['output-driven', 'scheduling'], ['P-cube', 'routing'], ['packaging'], ['packet'], ['packet'], ['packet', 'classes'], ['packet', 'header'], ['packet', 'header'], ['packet', 'size'], ['packet', 'switching'], ['packetization'], ['pad', '\xef\xac\x82it'], ['parallel', 'pre\xef\xac\x81x'], ['parallel', 'suf\xef\xac\x81x'], ['partially', 'adaptive', 'routing'], ['partially', 'adaptive', 'routing'], ['partitionability'], ['path'], ['path-based', 'routing'], ['perfect', 'k-shuf\xef\xac\x82e', 'permutation'], ['permanent', 'fault'], ['baseline'], ['bit', 'reversal'], ['butter\xef\xac\x82y'], ['cube'], ['digit', 'reversal'], ['exchange'], ['identity'], ['inverse', 'perfect', 'shuf\xef\xac\x82e'], ['perfect', 'k-shuf\xef\xac\x82e'], ['permutations'], ['persistent', 'communication'], ['personalized', 'all-to-all', 'broadcast'], ['personalized', 'broadcast'], ['personalized', 'combining'], ['phit'], ['physical', 'channel', '\xef\xac\x82ow', 'control'], ['physical', 'constraints'], ['physical', 'layer'], ['point-to-point', 'network'], ['port'], ['port'], ['port'], ['positive-hop', 'routing'], ['preferred', 'neighbors'], ['probe', 'lead'], ['process', 'group'], ['processor', 'cluster'], ['processor', 'interface'], ['processor', 'interface'], ['pro\xef\xac\x81table', 'routing'], ['pro\xef\xac\x81table', 'routing'], ['progressive', 'deadlock', 'recovery'], ['progressive', 'routing'], ['progressive', 'routing'], ['R2', 'router'], ['reachable', 'con\xef\xac\x81guration'], ['rearrangeable', 'MIN'], ['receiving', 'latency'], ['rectilinear', 'Steiner', 'tree', 'problem'], ['reduce'], ['reduce', 'and', 'spread'], ['redundancy', 'level'], ['redundant', 'channel'], ['region'], ['regressive', 'deadlock', 'recovery'], ['regular', 'network'], ['release', '\xef\xac\x82it'], ['release', '\xef\xac\x82it'], ['reliability'], ['reliability/performance', 'trade-offs'], ['Reliable', 'Router'], ['repairability'], ['reply', 'network'], ['reply', 'packets'], ['reporting', 'phase'], ['request', 'network'], ['request', 'packets'], ['resource', 'set'], ['return-to-sender', 'protocol'], ['reverse', '\xef\xac\x82it'], ['ring'], ['root', 'process'], ['routable', 'con\xef\xac\x81guration'], ['router'], ['arbitration'], ['buffers'], ['buffers'], ['crossbar', 'switch'], ['link', 'controller', '(LC)'], ['link', 'controller', '(LC)'], ['pipelines'], ['processor', 'interface'], ['processor', 'interface'], ['routing', 'and', 'arbitration', 'unit'], ['routing', 'and', 'arbitration', 'unit'], ['switch'], ['adaptive'], ['adaptive'], ['backtracking'], ['backtracking'], ['centralized'], ['de\xef\xac\x82ection'], ['deterministic'], ['deterministic'], ['direction', 'order'], ['distributed'], ['fault-recoverable'], ['fault-tolerant'], ['fully', 'adaptive'], ['fully', 'adaptive'], ['fully', 'adaptive', 'minimal'], ['hot', 'potato'], ['mad-y'], ['maximally', 'adaptive'], ['maximally', 'adaptive', 'double-y'], ['minimal'], ['misrouting'], ['misrouting'], ['multicast'], ['multiphase'], ['multiphase'], ['negative-\xef\xac\x81rst'], ['nonminimal'], ['oblivious'], ['opt-y'], ['origin-based'], ['partially', 'adaptive'], ['partially', 'adaptive'], ['path-based'], ['pro\xef\xac\x81table'], ['pro\xef\xac\x81table'], ['progressive'], ['progressive'], ['source'], ['source'], ['table-lookup'], ['tree-based'], ['true', 'fully', 'adaptive'], ['true', 'fully', 'adaptive'], ['unicast'], ['routing', 'algorithm'], ['routing', 'algorithm'], ['routing', 'and', 'arbitration', 'unit'], ['routing', 'and', 'arbitration', 'unit'], ['routing', 'control', 'unit', 'delay'], ['routing', 'delay'], ['routing', 'function'], ['routing', 'function'], ['routing', 'function'], ['routing', 'layer'], ['routing', 'probe'], ['routing', 'subfunction'], ['routing', 'subfunction'], ['safe', 'node'], ['safety', 'level'], ['scalability'], ['scan'], ['scatter'], ['scouting', 'distance'], ['scouting', 'switching'], ['selection', 'function'], ['selection', 'function'], ['selection', 'function'], ['selection', 'function'], ['selection', 'function'], ['sender-based', 'protocol'], ['sending', 'latency'], ['separate', 'addressing'], ['ServerNet'], ['SGI', 'SPIDER'], ['shared-medium', 'networks'], ['shared-medium', 'networks'], ['shared-memory', 'multiprocessors'], ['simplicity'], ['sink', 'channel'], ['slack', 'buffers'], ['software', 'messaging', 'layer'], ['software-based', 'rerouting'], ['solid', 'fault', 'model'], ['leader', '(SQHL)'], ['source', 'routing'], ['source', 'routing'], ['(SCHL)'], ['source-partitioned', 'U-mesh'], ['spanning', 'binomial', 'tree'], ['spanning-bus', 'hypercube'], ['spare', 'dimension'], ['spare', 'neighbors'], ['spatial', 'locality'], ['sphere', 'of', 'locality'], ['split', 'transaction', 'protocol'], ['split-and-sort', 'function'], ['star', 'graph'], ['start-up', 'latency'], ['starvation'], ['static', 'fault'], ['Steiner', 'tree', 'problem'], ['STOP'], ['store-and-forward', '(SAF)'], ['straight-line', 'selection', 'function'], ['street-sign', 'routing'], ['subtree'], ['switch'], ['switch'], ['switch', 'delay'], ['switch', 'port'], ['switch-based', 'network'], ['switching'], ['switching', 'layer'], ['switching', 'technique'], ['switching', 'technique'], ['switching', 'technique'], ['symmetric', 'network'], ['synchronous', 'bus'], ['synchronous', 'replication'], ['table-lookup', 'routing'], ['temporal', 'locality'], ['throughput'], ['throughput'], ['time-dependent', 'selection', 'function'], ['topology'], ['orthogonal'], ['strictly', 'orthogonal'], ['weakly', 'orthogonal'], ['torus'], ['total', 'exchange'], ['traf\xef\xac\x81c'], ['transient', 'fault'], ['tree'], ['tree'], ['balanced'], ['leaf', 'node'], ['root', 'node'], ['tree-based', 'routing'], ['true', 'cycle'], ['true', 'fully', 'adaptive', 'routing'], ['true', 'fully', 'adaptive', 'routing'], ['U-cube'], ['U-mesh'], ['unicast', 'routing'], ['Unicast-cube'], ['unidirectional', 'MIN'], ['uniform', 'distribution'], ['uniform', 'memory', 'access', '(UMA)'], ['unit', 'of', '\xef\xac\x82ow', 'control'], ['unsafe', 'node'], ['unsafe', 'node'], ['vector', 'routing'], ['virtual', 'channel'], ['virtual', 'channel'], ['virtual', 'channel', 'controller', '(VC)'], ['virtual', 'channel', 'trio'], ['complementary', 'channel'], ['corresponding', 'channel'], ['data', 'channel'], ['virtual', 'circuit', 'caching', '(VCC)'], ['virtual', 'cut-through', 'switching', '(VCT)'], ['virtual', 'lane'], ['virtual', 'network'], ['virtual', 'topologies'], ['wait', 'chain'], ['wait-for', 'graph'], ['waiting', 'channel'], ['wake-up', 'phase'], ['wave', 'pipelining'], ['wave', 'pipelining'], ['wave', 'switching'], ['west-\xef\xac\x81rst', 'routing'], ['westward', 'virtual', 'network'], ['wormhole', 'switching'], ['zenith', 'node']]
l2 = [' 477', ' 67', ' 410', ' 454', ' 457', ' 415', ' 141', ' 144', ' 560', ' 139', ' 220', ' 416', ' 478', ' 9', ' 412', ' 426', ' 11', ' 232', ' 10', ' 141', ' 144', ' 17', ' 212', ' 30', ' 27', ' 30', ' 361', ' 361', ' 481', ' 26', ' 220', ' 293', ' 28', ' 217', ' 9', ' 210', ' 15', ' 43', ' 556', ' 64', ' 447', ' 44', ' 381', ' 12', ' 12', ' 11', ' 11', ' 11', ' 481', ' 31', ' 26', ' 88', ' 394', ' 12', ' 140', ' 272', ' 512', ' 90', ' 94', ' 561', ' 382', ' 560', ' 113', ' 108', ' 409', ' 300', ' 65', ' 49', ' 104', ' 104', ' 88', ' 564', ' 208', ' 465', ' 212', ' 210', ' 211', ' 210', ' 210', ' 211', ' 555', ' 212', ' 212', ' 210', ' 210', ' 210', ' 212', ' 212', ' 210', ' 553', ' 211', ' 460', ' 244', ' 68', ' 211', ' 74', ' 117', ' 342', ' 30', ' 561', ' 217', ' 290', ' 90', ' 561', ' 24', ' 139', ' 75', ' 449', ' 447', ' 67', ' 396', ' 401', ' 21', ' 22', ' 379', ' 31', ' 27', ' 18', ' 217', ' 67', ' 399', ' 18', ' 317', ' 59', ' 83', ' 85', ' 85', ' 85', ' 118', ' 178', ' 139', ' 554', ' 113', ' 562', ' 88', ' 562', ' 151', ' 480', ' 109', ' 196', ' 272', ' 141', ' 144', ' 14', ' 26', ' 30', ' 272', ' 165', ' 328', ' 146', ' 272', ' 423', ' 95', ' 563', ' 244', ' 95', ' 561', ' 244', ' 7', ' 13', ' 13', ' 14', ' 13', ' 13', ' 14', ' 13', ' 13', ' 14', ' 13', ' 14', ' 402', ' 118', ' 121', ' 366', ' 6', ' 12', ' 140', ' 4', ' 3', ' 480', ' 30', ' 170', ' 536', ' 166', ' 294', ' 557', ' 165', ' 323', ' 536', ' 330', ' 220', ' 104', ' 104', ' 93', ' 507', ' 339', ' 27', ' 564', ' 104', ' 244', ' 45', ' 392', ' 457', ' 34', ' 313', ' 296', ' 293', ' 293', ' 313', ' 139', ' 291', ' 290', ' 141', ' 46', ' 55', ' 382', ' 338', ' 15', ' 43', ' 341', ' 403', ' 431', ' 145', ' 141', ' 145', ' 210', ' 478', ' 422', ' 210', ' 435', ' 211', ' 237', ' 253', ' 237', ' 157', ' 109', ' 188', ' 9', ' 16', ' 38', ' 38', ' 431', ' 27', ' 151', ' 5', ' 99', ' 563', ' 99', ' 562', ' 244', ' 7', ' 20', ' 555', ' 478', ' 480', ' 409', ' 198', ' 394', ' 461', ' 560', ' 397', ' 45', ' 143', ' 461', ' 26', ' 16', ' 302', ' 297', ' 341', ' 113', ' 114', ' 5', ' 476', ' 253', ' 481', ' 89', ' 561', ' 253', ' 253', ' 44', ' 380', ' 293', ' 83', ' 122', ' 139', ' 422', ' 62', ' 73', ' 237', ' 58', ' 171', ' 437', ' 481', ' 145', ' 200', ' 14', ' 366', ' 463', ' 46', ' 108', ' 480', ' 73', ' 338', ' 445', ' 406', ' 31', ' 30', ' 30', ' 28', ' 31', ' 31', ' 30', ' 31', ' 29', ' 31', ' 29', ' 23', ' 24', ' 31', ' 31', ' 29', ' 141', ' 195', ' 141', ' 144', ' 464', ' 464', ' 464', ' 464', ' 213', ' 243', ' 217', ' 140', ' 218', ' 268', ' 3', ' 29', ' 140', ' 334', ' 220', ' 220', ' 11', ' 21', ' 23', ' 434', ' 16', ' 153', ' 326', ' 157', ' 477', ' 88', ' 217', ' 4', ' 414', ' 360', ' 293', ' 362', ' 29', ' 141', ' 11', ' 4', ' 477', ' 153', ' 145', ' 478', ' 31', ' 171', ' 218', ' 218', ' 219', ' 75', ' 318', ' 409', ' 198', ' 153', ' 375', ' 14', ' 46', ' 418', ' 14', ' 52', ' 553', ' 52', ' 446', ' 342', ' 212', ' 212', ' 141', ' 145', ' 6', ' 217', ' 236', ' 25', ' 294', ' 27', ' 26', ' 26', ' 27', ' 26', ' 27', ' 27', ' 26', ' 25', ' 25', ' 464', ' 211', ' 210', ' 210', ' 46', ' 46', ' 6', ' 43', ' 13', ' 13', ' 499', ' 553', ' 157', ' 304', ' 70', ' 209', ' 213', ' 44', ' 381', ' 141', ' 144', ' 117', ' 141', ' 144', ' 414', ' 90', ' 29', ' 271', ' 219', ' 210', ' 212', ' 291', ' 290', ' 221', ' 117', ' 14', ' 341', ' 549', ' 6', ' 556', ' 403', ' 6', ' 397', ' 397', ' 258', ' 397', ' 397', ' 113', ' 449', ' 341', ' 16', ' 209', ' 90', ' 13', ' 422', ' 44', ' 381', ' 379', ' 44', ' 380', ' 420', ' 44', ' 381', ' 44', '', ' 44', ' 141', ' 144', ' 141', ' 144', ' 140', ' 109', ' 141', ' 144', ' 402', ' 140', ' 291', ' 290', ' 141', ' 145', ' 145', ' 109', ' 171', ' 145', ' 171', ' 141', ' 141', ' 144', ' 140', ' 140', ' 334', ' 326', ' 141', ' 145', ' 171', ' 318', ' 141', ' 145', ' 236', ' 141', ' 144', ' 141', ' 144', ' 140', ' 398', ' 141', ' 221', ' 145', ' 177', ' 140', ' 14', ' 554', ' 44', ' 380', ' 511', ' 45', ' 87', ' 144', ' 380', ' 43', ' 49', ' 93', ' 562', ' 319', ' 304', ' 5', ' 212', ' 210', ' 70', ' 70', ' 87', ' 144', ' 194', ' 380', '', ' 415', ' 271', ' 268', ' 437', ' 406', ' 7', ' 9', ' 4', ' 6', ' 561', ' 388', ' 553', ' 323', ' 321', ' 255', ' 140', ' 398', ' 256', ' 277', ' 222', ' 38', ' 298', ' 304', ' 480', ' 480', ' 12', ' 244', ' 18', ' 217', ' 84', ' 294', ' 219', ' 435', ' 52', ' 195', ' 141', ' 217', ' 20', ' 44', ' 511', ' 20', ' 20', ' 15', ' 43', ' 43', ' 553', ' 556', ' 14', ' 11', ' 232', ' 141', ' 480', ' 5', ' 477', ' 196', ' 14', ' 15', ' 15', ' 15', ' 16', ' 211', ' 477', ' 294', ' 17', ' 217', ' 17', ' 17', ' 17', ' 221', ' 108', ' 145', ' 177', ' 274', ' 274', ' 140', ' 274', ' 29', ' 480', ' 4', ' 46', ' 302', ' 317', ' 407', ' 62', ' 555', ' 380', ' 68', ' 68', ' 67', ' 67', ' 533', ' 54', ' 63', ' 159', ' 461', ' 288', ' 108', ' 107', ' 258', ' 51', ' 425', ' 425', ' 153', ' 330', ' 55', ' 318']
print len(l1)
print len(l2)
for faf in range(len(l2)):
    tex = l1[faf]
    tex2 = l2[faf]
    if any(c.isalpha() for c in tex2) or len(tex2)>4 or tex2=='':
        continue
    print tex
    m = convert('CN6.pdf', pages=[int(tex2)+24])

    m = m.split('\n\n')
    f2 = open("xxCN6.txt",'a')
    f3 = open("yyCN6.txt",'a')
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
