# 高级路由功能

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 6 高级路由功能
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 499 -->
6 高级路由功能
路由是将数据包从一个网络转发到另一个网络中的目的地址的过程。路由器是处在两个网络之间转发数据包
的设备。路由器根据路由表中储存的各种传输路径传输数据包，每一个传输路径即为一个路由条目。
设备具有三层路由功能，通过VRouter，进行路由配置，对不同的数据包进行转发。系统有一个默认
VRouter，即trust-vr，同时系统支持多VRouter（多VR）功能。
设备支持目的路由、ISP路由、源路由（Source-Based Routing，简称SBR）、源接口路由（SourceInterface-Based Routing，简称SIBR）、目的接口路由（Destination-Interface-Based Routing，
简称DIBR）、策略路由（Policy-Based Routing，简称PBR）、动态路由（包括RIP、OSPF、IS-IS和
BGP）、等价多径路由（Equal Cost MultiPath Routing，简称ECMP）、静态组播路由，和协议无关组
播路由（Protocol Independent Multicast，简称PIM）等。
l 配置目的路由：手工定义的路由条目，根据目的地址指定下一跳。
l 配置目的接口路由：根据数据包的目的IP地址和入接口，选择路由，进行转发。
l 配置源路由：根据数据包的源IP地址，选择路由，进行转发。
l 配置源接口路由（SIBR）：根据数据包的源IP地址和入接口，选择路由，进行转发。
l 配置ISP路由：根据不同的ISP确定下一跳。
l 配置策略路由（PBR）：根据数据包的源IP地址、目的IP地址以及服务类型，选择路由，进行转发。
l 域名路由：配置目的域名和下一跳地址，通过DNS Snooping解析来建立并更新目的域名与IP地址的映射关系信
息，生成路由。只支持通过CLI配置，请参阅《StoneOS命令行手册》。
l 动态路由：设备按照动态路由协议（配置RIP、配置OSPF、配置IS-IS或者配置BGP）自动生成的动态路由表项对
数据包进行路由选择并转发。配置IS-IS只支持通过CLI配置，请参阅《StoneOS命令行手册》。
l 等价多径路由（ECMP）：到达相同目的IP地址或网段的数据流量在多条相同管理距离的路径上进行负载均衡。
只支持通过CLI配置，请参阅《StoneOS命令行手册》。
l 静态组播路由：通过手工配置组播路由规则来实现将数据从组播源传送给组播成员。只支持通过CLI配置，请参
阅《StoneOS命令行手册》。
l 配置协议无关组播（PIM/PIMv6）：表示为IP组播提供路由信息的可以是静态路由或任意单播路由协议。组播路
由和所采用的单播路由协议无关，只要是能够通过单播路由协议产生相应的组播路由表项即可。
l BFD：用于快速检测和监控网络链路或IP路由的双向转发连通性。
路由功能支持IPv4和IPv6地址。如接口开启了IPv6功能，用户可根据需要配置IPv6地址的路由条目。

<!-- 来源页 500 -->
注意: 当设备对进入的数据包进行转发时，按照这样的顺序选路：策略路由> 源接口路由> 源路由
> 目的接口路由> 目的路由/ISP路由/动态路由。

<!-- 来源页 501 -->
开启/关闭静态路由查询
对于策略路由、源接口路由和源路由，用户可以单独控制是否需要对它们进行查询（系统要求必须进行目的
路由查询）。默认情况下，策略路由、源接口路由和源路由查询为开启状态。开启/关闭策略路由、源接口路
由和源路由查询，在全局配置模式下，使用以下命令（适用于所有VRouter）：
l
开启：route enable {pbr | sibr | sbr |dibr}
l
关闭：route disable {pbr | sibr | sbr |dibr}
关于开启/关闭静态路由查询的配置举例，请参阅“开启/关闭静态路由查询功能配置举例”。

<!-- 来源页 502 -->
开启/关闭会话重匹配路由
默认情况下，会话重匹配路由的功能是开启的。当用户添加、修改或删除路由时，会话会重新匹配最优路
由。在会话重匹配路由的过程中，系统会根据情况对会话作出如下不同操作：
l
当会话之前匹配的路由被删除时：
l
若会话保留功能（keep-session）关闭，则相匹配的会话将被删除。
l
若会话保留功能（keep-session）开启，则相匹配的会话不会被删除，且会话的路由信息变为无
效。当与会话之前匹配的路由被重新添加后，会话将重匹配路由：
l
若重新匹配的路由的出接口未发生变化，则会话的路由信息变为有效，会话恢复可用状
态。
l
若重新匹配的路由的出接口发生变化，则会话将被删除。
l
当会话之前匹配的路由被修改或有新路由被添加时：
l
若会话之前匹配的路由仍是最优路由，会话保持可用状态。
l
若会话之前匹配的路由不是最优路由，但重新匹配的路由的出接口未发生变化，会话更新路由信
息。
l
若会话之前匹配的路由不是最优路由，且重新匹配的路由的出接口发生变化，会话将被删除。
注意:
l
设备默认开启会话重匹配路由功能（session rematch route enable)，但如果处于HA
Peer模式下，该功能不会生效。对于HA Peer模式下的设备，如果要使用会话重匹配路由功
能，则需要使用命令行（session rematch route enable peer-mode）手动开启。相关配
置参阅开启/关闭HA Peer模式下的会话重匹配路由功能章节。
l
在某些情况下（如添加或删除策略路由的应用类型），会话可能会被大量删除，导致流量异
常。此时，需要关闭会话重匹配路由功能。
会话重匹配路由功能的配置包括：
l
开启/关闭会话重匹配路由功能
l
开启/关闭HA peer模式下的会话重匹配路由功能
l
开启/关闭会话保留功能

<!-- 来源页 503 -->
l
开启/关闭特定场景下的会话保留功能
l
查看会话重匹配路由功能的配置状态
开启/关闭会话重匹配路由功能
默认情况下，会话重匹配路由功能为开启状态。开启/关闭会话重匹配路由功能，在Flow配置模式下，使用
以下命令：
session rematch route {enable | disable}
l
enable – 开启会话重匹配路由功能。
l
disable – 关闭会话重匹配路由功能。若会话保留功能和HA Peer模式下的会话重匹配路由功能是开启
状态，也会被同时关闭。
开启/关闭HA Peer模式下的会话重匹配路由功能
注意: 仅限在不存在非对称路由的环境中开启HA Peer模式下的会话重匹配路由功能，否则将影响
设备的业务运行。
默认情况下，HA Peer模式下的会话重匹配路由功能为关闭状态。开启/关闭HA Peer模式下的会话重匹配
路由功能，在Flow配置模式下，使用以下命令：
l
开启：session rematch route enable peer-mode
l
关闭：no session rematch route enable peer-mode
开启/关闭会话保留功能
默认情况下，会话保留功能为关闭状态。开启/关闭会话保留功能，在Flow配置模式下，使用以下命令：
l
开启：session rematch route enable keep-session
l
关闭：no session rematch route enable keep-session
开启/关闭特定场景下的会话保留功能
特定场景指当添加的明细路由的父路由下一跳是VRouter时，在会话重匹配路由的过程中，系统会将父路由
的会话删除，从而影响业务运行。为了避免这一情况，用户可以开启特定场景下的会话保留功能，在添加的
明细路由的父路由下一跳是VRouter时，不删除相匹配的会话。默认情况下，特定场景下的会话保留功能为
关闭状态。
开启/关闭特定场景下的会话保留功能，在Flow配置模式下，使用以下命令：

<!-- 来源页 504 -->
l
开启特定场景下的会话保留功能：session rematch route enable keep-cross-vr-session
l
关闭特定场景下的会话保留功能：no session rematch route enable keep-cross-vr-session
查看会话重匹配路由功能的配置状态
用户能够查看会话重匹配路由功能的配置状态，包括会话重匹配路由功能和会话保留功能。
查看会话重匹配路由功能的配置状态，在任何模式下，使用以下命令：
show fib change
以下是一个返回结果示例：
hostname# show fib change
Route session rematch:enable（会话重匹配路由功能为开启状态）, keep-session:disable（会话
保留功能为关闭状态）
IPv4 DBR Fib change
=====================================================
Vrid Action Destination Nexthop-Num
-----------------------------------------------------

<!-- 来源页 505 -->
VRouter
虚拟路由器即Virtual Router（VRouter），在系统中简称为VR。VR具有路由器功能，不同VR拥有各自独
立的路由表。系统中有一个默认VR，名为trust-vr，trust-vr不能被删除。默认情况下，所有三层安全域都
将会自动绑定到trust-vr上。
系统支持多VR功能且不同硬件平台支持的最大VR数不同。多VR将设备划分成多个虚拟路由器，每个虚拟路
由器使用和维护各自完全独立的路由表，此时一台设备可以充当多台路由器使用。多VR使设备能够实现不同
路由域的地址隔离与不同VR间的地址重叠，同时能够在一定程度上避免路由泄露，增加网络的路由安全。下
图描述了接口、安全域、VSwitch和VRouter之间的关系：
如上图所示，接口、安全域、VSwitch和VRouter之间的绑定关系如下：
l 接口绑定到安全域。绑定到二层安全域的接口为二层接口，绑定到三层安全域的接口为三层接口。一个接口只能
绑定到一个安全域。主接口与子接口可以分别属于不同的安全域。
l 安全域绑定到VSwitch或者VRouter。二层安全域绑定到VSwitch（预定义二层安全域默认绑定到系统缺省
VSwitch——VSwitch1），三层安全域绑定到VRouter（预定义三层安全域默认绑定到系统缺省VR——trustvr）。由此，也实现了接口与VSwitch或者VR的绑定。一个安全域只能绑定到一个VSwtich或者VR。
配置VRouter
Hillstone设备的所有路由配置都需要在相应的VRouter配置模式下进行。进入VRouter配置模式，在全局
配置模式下使用以下命令：
ip vrouter vrouter-name

<!-- 来源页 506 -->
l
vrouter-name – 指定VRouter的名称。
开启和关闭多VR功能
默认情况下，系统的多VR功能是关闭的，即除缺省VR外，用户不可以创建和使用其它的VR。配置多VR后，
流量的传输最多可跨越3个VR，多于3个VR的流量将会被丢弃。
开启或者关闭系统的多VR功能，在任何模式下使用以下命令：
l
开启：exec vrouter enable
l
关闭：exec vrouter disable
执行以上命令后，需要重启设备才能相应地开启或者关闭多VR功能。设备重启后，部分平台的最大并发连接
数会根据多VR功能的开启或者关闭状态减少或者恢复正常。关于系统最大并发连接数变化的详细信息，请参
阅"调整系统最大并发连接数" 在第894页。
创建VRouter
开启系统的多VR功能并重启设备后，在全局配置模式下使用以下命令创建一个VRouter并且进入VRouter配
置模式：
ip vrouter vrouter-name
l
vrouter-name – 指定将要创建的VRouter的名称。如果指定的名称已存在，则直接进入VRouter配置
模式。
在全局配置模式下，使用该命令no的形式删除指定的VRouter：
no ip vrouter vr-name
显示VRouter信息
在任何模式下，使用以下命令查看VRouter信息：
show ip vrouter [vrouter-name]
l
vrouter-name – 显示指定名称VRouter的信息。如果不指定该参数，系统将显示所有VRouter的信
息。
指定最大路由条目数
指定VRouter允许的最大路由条目数（包含VRouter下的所有直连路由、静态路由和各种动态路由），在
VRouter配置模式下，使用以下命令：
max-routes number

<!-- 来源页 507 -->
l
number – 指定最大路由条目数。范围是1到100000。
在VRouter配置模式下，使用该命令no的形式取消最大路由条目数的指定：
no max-routes
当路由条目数达到最大路由条目数，系统将会发出警告。
引入VRouter路由
用户可以把其它VRouter中的路由条目引入到当前VRouter进行使用。引入VRouter路由，在VRouter配置
模式下使用以下命令：
import vrouter vrouter-name {connected | static | rip | ospf | bgp}
l
vrouter-name – 指定被引入路由所属的VRouter。
l
connected | static | rip | ospf | bgp – 指定被引入路由的类型。
多次配置该命令引入多种类型路由。
注意: 从其它VRouter引入的路由的优先级低于VRouter自身的路由。
取消直连路由优先
直连路由拥有最高路由优先级，在同时配置其他路由时，直连路由会被优先使用，使得其他路由不生效，因
此，用户可以根据需要，取消直连路由优先，使其他路由优先使用。在VRouter配置模式下使用以下命令：
fib-lookup connect-first-disable
在VRouter配置模式下，使用该命令no的形式恢复直连路由优先：
no fib-lookup connect-first-disable

<!-- 来源页 508 -->
目的路由
静态路由是手工定义的路由条目，根据目的地址指定下一跳，因此也称作目的路由。对外连接较少或者内网
连接相对比较稳定的网络通常使用目的路由。用户可以根据需要确定是否添加默认路由条目。
配置目的路由
用户可以添加目的路由条目并且显示目的路由信息。
添加目的路由条目
用户可以为VRouter添加目的路由条目。但是，添加目的路由条目之前，需要进入VRouter配置模式。请在
全局配置模式下使用以下命令：
ip vrouter vrouter-name
l
vrouter-name – 指定VRouter的名称。
进入到VRouter配置模式下后，用户可以添加目的路由条目。在VRouter配置模式下使用以下命令：
ip route {A.B.C.D/M | A.B.C.D A.B.C.D} {A.B.C.D | interface-name [A.B.C.D] | vrouter vroutername} [distance-value] [weight weight-value] [tag tag-value] [description description]
[schedule schedule-name] [track track-name]
l
A.B.C.D/M | A.B.C.D A.B.C.D – 指定目的地址。Hillstone设备支持两种方式，A.B.C.D/M或者
A.B.C.D A.B.C.D，例如1.1.1.0/24或者1.1.1.0 255.255.255.0。
l
A.B.C.D | interface-name [A.B.C.D] | vrouter vrouter-name – 指定下一跳。可以是网关地址
（A.B.C.D）、接口（interface-name）或者VRouter（vrouter vrouter-name）。当下一跳为接
口时，用户可以选择隧道接口名称（当为多隧道接口时，用户必须使用A.B.C.D参数指定IPSec VPN、
GRE或者SCVPN隧道的下一跳IP地址，并且此地址必须和该隧道接口绑定的相应隧道的下一跳IP地址相
同）、Null0接口或者PPPoE接口。
l
distance-value – 指定路由的管理距离大小。该参数设定路由的优先级，取值越小，优先级越高，而
在有多条路由选择的时候，优先级高的路由会被优先使用。取值范围是1到255，默认值为1。当路由距
离为255时，该路由无效。
l
weight weight-value – 指定路由权值的大小。路由权值决定负载均衡中流量转发的比重。范围是1到
255，默认值是1。

<!-- 来源页 509 -->
l
tag tag-value – 指定目的路由的标记值。在OSPF引入路由时，如果此处配置的路由标记值匹配到路由
映射表中的规则，那么将会引入该路由，从而实现对引入路由信息的过滤。取值范围是1到
4294967295。
l
description description – 指定路由的描述信息。范围是1到63个字符。
l
schedule schedule-name – 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配
置多次该命令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的
时间表。
l
track track-name – 指定已创建的监测对象名称。指定后，若针对该监测对象的监测失败，则该路由
无效。
使用多条该命令添加多条目的路由条目。
使用以上命令no的形式删除指定的目的路由条目：
no ip route {A.B.C.D/M | A.B.C.D A.B.C.D} {A.B.C.D | interface-name A.B.C.D | interface-name
[A.B.C.D] | vrouter vrouter-name} [description description] [schedule schedule-name]
显示目的路由信息
用户可以在任何模式下使用以下命令查看目的路由信息：
show ip route static [vrouter vrouter-name]
l
vrouter-name - 显示指定的VRouter的目的路由信息。

<!-- 来源页 510 -->
目的接口路由
目的接口路由（DIBR）根据数据包的目的IP地址和入接口，选择路由，进行转发。
添加目的接口路由条目
目的接口路由的配置也需要在VRouter配置模式下完成。进入VRouter配置模式，在全局配置模式下，使用
以下命令：
ip vrouter vrouter-name
进入到VRouter配置模式下后，用户可以添加目的接口路由条目。在VRouter配置模式下使用以下命令：
ip route in-interface interface-name {A.B.C.D/M | A.B.C.D A.B.C.D} {A.B.C.D | interface-name
[A.B.C.D] | vrouter vrouter-name} [distance-value] [weight weight-value] [description
description] [schedule schedule-name] [track track-name]
l
in-interface interface-name - 指定路由条目的入接口。
l
A.B.C.D/M | A.B.C.D A.B.C.D – 指定目的地址。Hillstone设备支持两种方式，A.B.C.D/M或者
A.B.C.D A.B.C.D，例如1.1.1.0/24或者1.1.1.0 255.255.255.0。
l
A.B.C.D | interface-name [A.B.C.D] | vrouter vrouter-name – 指定下一跳。可以是网关地址
（A.B.C.D）、接口（interface-name）或者VRouter（vrouter vrouter-name）。当下一跳为接
口时，用户可以选择隧道接口名称（当为多隧道接口时，用户必须使用A.B.C.D参数指定IPSec VPN、
GRE或者SCVPN隧道的下一跳IP地址，并且此地址必须和该隧道接口绑定的相应隧道的下一跳IP地址相
同）、Null0接口或者PPPoE接口。
l
distance-value – 指定路由的管理距离大小。该参数设定路由的优先级，取值越小，优先级越高，而
在有多条路由选择的时候，优先级高的路由会被优先使用。取值范围是1到255，默认值为1。当路由距
离为255时，该路由无效。
l
weight weight-value – 指定路由权值的大小。路由权值决定负载均衡中流量转发的比重。范围是1到
255，默认值是1。
l
description description – 指定路由的描述信息。范围是1到63个字符。
l
schedule schedule-name – 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配
置多次该命令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的
时间表。

<!-- 来源页 511 -->
l
track track-name – 指定已创建的监测对象名称。指定后，若针对该监测对象的监测失败，则该路由
无效。
使用多条该命令添加多条目的接口路由条目。
使用以上命令no的形式删除指定的目的接口路由条目：
no ip route in-interface interface-name {A.B.C.D/M | A.B.C.D A.B.C.D} {A.B.C.D | interfacename [A.B.C.D] | vrouter vrouter-name} [description description] [schedule schedule-name]
查看目的接口路由信息
用户可以在任何模式下使用以下命令查看目的接口路由信息：
show ip route in-interface interface-name
l
in-interface interface-name - 显示指定入接口的目的接口路由信息。
查看目的接口路由的FIB信息
用户可以在任何模式下使用以下命令查看目的接口路由的FIB信息：
show [ipv6] fib in-interface interface-name
l
in-interface interface-name - 显示指定入接口的目的接口路由的FIB信息。

<!-- 来源页 512 -->
ISP路由
很多用户通常会申请多条线路进行流量负载均衡。然而，一般的均衡是不会根据流量的流向做均衡的，如果
网通的服务器通过电信访问，网速就会很慢。设备针对该问题，提供ISP路由功能，使不同ISP流量走专有路
由，从而提高网络访问速度。
配置ISP路由，用户首先需要将子网条目添加到一个ISP，然后才可以配置以ISP名称为目的地的ISP路由。用
户可以自定义ISP信息，也可以上传和下载ISP包含不同ISP信息的自定义配置文件。同时系统提供预定义
IPv4 ISP配置文件包含四个ISP，分别是中国电信（China-telecom）、中国联通（China-netcom）、中
国移动（China-mobile）和教育网（CERNET）；预定义IPv6 ISP配置文件包含四个ISP，分别是中国电信
（China-telecom-v6）、中国联通（China-netcom-v6）、中国移动（China-mobile-v6）和教育网
（CERNET-v6）。预定义ISP配置文件可通过ISP信息库实现升级，关于如何更改预定义ISP信息库更新配
置，请参阅“升级特征库”一节。
配置ISP路由
配置ISP路由，用户需要进行的操作如下：
l ISP信息库配置
l 配置ISP信息
l 配置ISP路由
l 上传/保存ISP配置文件
l 查看ISP路由配置信息
ISP信息库配置
默认情况下，系统会每日自动更新ISP信息库，用户可以根据需要更改ISP信息库更新配置。
ISP信息库更新配置包括：
l 配置ISP信息库更新模式
l 配置更新传输协议
l 配置更新服务器
l 指定HTTP代理服务器
l 指定更新时间
l 立即更新
l 导入预定义ISP配置文件

<!-- 来源页 513 -->
l 显示ISP信息库信息
l 显示ISP信息库更新配置信息
配置ISP信息库更新模式
系统支持手动和自动两种更新方式。配置ISP信息库更新方式，在全局配置模式下，使用以下命令：
isp-information update mode {auto | manual}
l
auto – 指定自动更新ISP信息库。该方式为系统的默认更新方式。
l
manual – 指定手动更新ISP信息库。
在全局配置模式下使用该命令no的形式恢复默认更新模式：
no isp-information update mode
配置更新传输协议
系统支持通过HTTP和HTTPS对ISP信息库进行更新，默认为HTTPS。配置ISP信息库更新的传输协议为
HTTP，在全局配置模式下，使用以下命令：
isp-information update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：
no isp-information update protocol HTTP
配置更新服务器
系统提供默认的ISP信息库更新服务器，即update1.hillstonenet.com和update2.hillstonenet.com，
同时用户也可以根据需要配置其它更新服务器下载最新预定义ISP配置文件。最多可配置3个。配置更新服务
器，在全局配置模式下，使用以下命令：
isp-information update {server1 | server2 | server3} {ip-address | domain-name} [vrouter
vrouter-name] [src-interface src-interface-name]
l
server1 | server2 | server3 – 指定将要配置的服务器，服务器支持双栈协议，可配置IPv4地址和IPv6
地址。server1的默认值为update1.hillstonenet.com，server2的默认值为
update2.hillstonenet.com。
l
ip-address | domain-name – 指定更新服务器的名称，可以是IP地址形式（ip-address）也可以是
域名形式（domain-name，例如update1.hillstonenet.com）。
l
vrouter vrouter-name– 指定更新服务器绑定的虚拟路由器。若不指定则默认是trust-vr。

<!-- 来源页 514 -->
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，ISP信息库更新时将通过该源接口对更新服务器发起访问。若不指定，则默认使用管理口作为源接
口。
在全局配置模式下，使用该命令no的形式恢复server1或server2的默认配置，删除server3的配置：
no isp-information update {server1 | server2 | server3}
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保ISP信息库能够正常升级，需要在设备上指定代理服
务器的IP地址和端口号。
为ISP信息库升级指定代理服务器，在全局配置模式下，使用如下命令：
isp-information update proxy-server {main | backup} ip-address port-number
l
main | backup – 使用main参数指定主代理服务器，使用backup指定备份代理服务器。
l
ip-address port-number – 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no isp-information update proxy-server {main | backup}命令。
指定更新时间
默认情况下，系统采用自动模式每日更新ISP信息库，并且为避免服务器流量过大，每日更新时间是随机
的。用户可以根据需要指定ISP信息库更新的频率和时间，在全局配置模式下，使用以下命令：
isp-information update schedule {daily | weekly {mon | tue | wed | thu | fri | sat | sun} |
monthly <1-31>} [HH:MM]
l
daily – 指定频率为每天更新。
l
weekly {mon | tue | wed | thu | fri | sat | sun} – 指定频率为每周更新。mon | tue | wed | thu | fri
| sat | sun用来指定每周更新的日期。
l
monthly <1-31> – 指定频率为每月更新。<1-31>用来指定每月更新的日期。
l
HH:MM – 指定更新的时间，例如09：00。
立即更新
无论更新模式为手动还是自动，用户都可以随时使用以下命令更新ISP信息库。立即更新ISP信息库，在任何
模式下，使用以下命令：
exec isp-information update

<!-- 来源页 515 -->
l
exec isp-information update – 仅对当前ISP信息库与更新服务器最新发布ISP信息库的不同部分进
行更新。
导入预定义ISP配置文件
在某些情况下，用户设备可能无法连接到更新服务器对ISP信息库进行更新，针对这一问题，StoneOS提供
ISP配置文件导入功能。用户可以通过FTP、FTPS、SFTP或者TFTP方式导入预定义ISP配置文件，从而更新
设备的ISP信息库。导入预定义ISP配置文件，在执行模式下，使用以下命令：
import ispfile from {ftp server ip-address [user user-name password password ] | ftps
server ip-address [user user-name password password ] | sftp server ip-address [user username password password ] | tftp server ip-address } [vrouter vr-name] file-name
l
ip-address - 指定FTP/FTPS/SFTP/TFTP服务器的IP地址。
l
user username password password - 指定FTP/FTPS/SFTP服务器的用户名和密码。
l
vrouter vr-name – 指定FTP/FTPS/SFTP/TFTP服务器所属的VRouter。
l
file-name - 指定导入的预定义ISP配置文件的名称。
删除预定义ISP配置文件
系统预定义ISP配置文件为加密形式，设备出厂时系统自带ISP信息库，ISP信息库中包含预定义ISP配置文
件，设备可以通过连接更新服务器更新ISP信息库或通过FTP、FTPS、SFTP或者TFTP方式导入预定义ISP配
置文件，从而更新设备的ISP信息库。ISP信息库中的预定义ISP配置文件支持通过CLI删除。
删除预定义IPv4 ISP配置文件
用户可以在执行模式下，通过使用以下命令将预定义IPv4 ISP配置文件从系统中删除：
exec isp-network clear-predefine
执行该命令后，重启系统，系统将恢复使用原有的预定义IPv4 ISP配置文件（出厂时系统自带的预定义IPv4
ISP配置文件）。
注意: 为保证预定义IPv4 ISP配置文件能够正常删除，请在删除预定义IPv4 ISP配置文件前，先删
除嵌套的IPv4 ISP信息条目。
删除预定义IPv6 ISP配置文件
用户可以在执行模式下，通过使用以下命令将预定义IPv6 ISP配置文件从系统中删除：
exec isp-network clear-predefine ipv6

<!-- 来源页 516 -->
执行该命令后，重启系统，系统将恢复使用原有的预定义IPv6 ISP配置文件（出厂时系统自带的预定义IPv6
ISP配置文件）。
注意: 为保证预定义IPv6 ISP配置文件能够正常删除，请在删除预定义IPv6 ISP配置文件前，先删
除嵌套的IPv6 ISP信息条目。
显示ISP信息库信息
用户可以随时使用相应的show命令查看设备的ISP信息库信息。在任何模式下使用以下命令：
show isp-information info
例如：
hostname(config)# show isp-information info
DB vendor: Hillstone Networks（显示数据库供应商）
Current version: 1.0.220902（显示ISP信息库当前版本）
Release date: 2022/09/02 15:00:02（显示更新服务器上当前版本的发布时间）
显示ISP信息库更新配置信息
用户可以随时使用相应的show命令查看设备上的ISP信息库更新信息，包括更新服务器信息、更新模式、更
新频率及时间以及僵尸网络防御特征库更新状况等。查看ISP信息库更新配置信息，在任何模式下使用以下
命令：
show isp-information update
例如：
hostname(config)# show isp-information update
ISP signature update options:（显示ISP信息库的更新项）
protocol: HTTPS（显示ISP信息库更新的传输协议）
server1: update1.hillstonenet.com, 443, trust-vr（显示ISP信息库更新服务器的信息）
server2: update2.hillstonenet.com, 443, trust-vr（显示ISP信息库更新服务器的信息）
server3: 10.10.10.10, 443, trust-vr（显示ISP信息库更新服务器的信息）
proxy server status: enable（显示代理服务器状态）
main proxy server:（显示主代理服务器的信息）
backup proxy server: ip 10.10.10.10, port 12（显示备份代理服务器的信息）
mode: auto（显示ISP信息库更新的模式）

<!-- 来源页 517 -->
schedule: daily 09:21（显示自动模式下的更新周期）
current status: normal（显示ISP信息库更新/没更新的过程状态，normal即ISP信息库当前处于没更新
的状态）
last update result: Download signature failed; please confirm the servers are reachable
（显示上一次更新ISP信息库的结果）
last update time: Fri Nov 4 09:22:02 2022（显示上一次更新ISP信息库的时间）
配置IPv4 ISP信息
在设备上配置IPv4 ISP信息，首先需要进入IPv4 ISP信息配置模式。在全局配置模式下，使用以下命令，创
建IPv4 ISP名称并且进入IPv4 ISP信息配置模式：
isp-network isp-name
l
isp-name – 指定IPv4 ISP名称，系统最多允许创建26个IPv4 ISP信息。
在全局配置模式下，使用该命令no的形式删除指定名称的IPv4 ISP：
no isp-network isp-name
添加子网条目
为IPv4 ISP添加子网条目，在IPv4 ISP信息配置模式下，使用以下命令：
subnet A.B.C.D/M
l
A.B.C.D/M – 为IPv4 ISP指定子网，格式为IP地址/掩码，例如1.1.1.0/24，系统最多允许添加的子网
条目数根据平台不同而不同，范围是1000-6000个。
在IPv4 ISP信息配置模式下配置多条该命令，为IPv4 ISP添加多个子网。
在IPv4 ISP信息配置模式下使用该命令no的形式删除指定的子网：
no subnet A.B.C.D/M
添加IPv4 ISP信息条目
为IPv4 ISP添加IPv4 ISP信息条目，即添加其他已配置的IPv4 ISP信息（预定义IPv4 ISP信息或自定义IPv4
ISP信息），在IPv4 ISP信息配置模式下，使用以下命令：
member isp-name
l
isp-name – 指定IPv4 ISP名称。系统支持的IPv4 ISP嵌套层数最多为1层，并且不支持回环嵌套，
IPv4 ISP信息不可以再嵌套它所属的IPv4 ISP信息。

<!-- 来源页 518 -->
在IPv4 ISP信息配置模式下配置多条该命令，为ISP添加多个IPv4 ISP信息条目。系统最多允许添加8个IPv4
ISP信息条目。
在IPv4 ISP信息配置模式下使用该命令no的形式删除指定嵌套的IPv4 ISP信息条目：
no member isp-name
注意: IPv4 ISP 信息和IPv6 ISP信息不允许相互嵌套。
配置IPv4 ISP路由
IPv4 ISP路由需要在VRouter配置模式下进行配置。进入VRouter配置模式，在全局配置模式下使用以下命
令：
ip vrouter vrouter-name
l
vrouter-name – 指定VRouter的名称。
在VRouter配置模式，使用以下命令配置ISP路由条目：
ip route isp-name {A.B.C.D | interface-name | vrouter vrouter-name} [distance-value]
[weight weight-value] [description description] [schedule schedule-name]
l
isp-name – 指定系统中已存在的IPv4 IS.;P名称作为路由的目的地址。
l
A.B.C.D | interface-name | vrouter vrouter-name – 指定下一跳。可以是网关地址（A.B.C.D）、
接口（interface-name）或者VRouter（vrouter vrouter-name）。当下一跳为接口时，用户可以
选择隧道接口名称、Null0接口或者PPPoE接口。
l
distance-value – 指定路由的管理距离大小。该参数设定路由的优先级，取值越小，优先级越高，而
在有多条路由选择的时候，优先级高的路由会被优先使用。取值范围是1到255，默认值为10。当路由距
离为255时，该路由无效。
l
weight weight-value – 指定路由权值的大小。路由权值决定负载均衡中流量转发的比重。范围是1到
255，默认值是1。
l
description description – 指定路由的描述信息。范围是1到63个字符。
l
schedule schedule-name – 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配
置多次该命令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的
时间表。
使用多条该命令添加多条IPv4 ISP路由条目。
使用以上命令no的形式删除指定的IPv4 ISP路由条目：

<!-- 来源页 519 -->
no ip route isp-name {A.B.C.D | interface-name | vrouter vrouter-name } [distance-value]
[weight weight-value] [description description] [schedule schedule-name]
查看IPv4 ISP路由配置信息
用户可以通过show命令查看IPv4 ISP路由配置信息。
l
查看预定义IPv4 ISP配置文件信息：
show pre-isp-network {all | isp-name}
l
查看自定义IPv4 ISP配置文件信息：
show isp-network {all | isp-name}
l
查看IPv4 ISP路由条目：
show ip route isp [isp-name | vrouter vrouter-name]
上传/下载自定义IPv4 ISP配置文件
设备支持两种IPv4 ISP配置文件，分别是用户自定义IPv4 ISP配置文件和系统预定义IPv4 ISP配置文件。
l
自定义IPv4 ISP配置文件：请按照下所示实例格式书写用户自定义配置文件，否则，即使文件上传成
功，也不可以在系统中生效。
# Software Version 5.5 SG6000-MX_MAIN-68-V6-r1018.bin 202211040258
!
Version 5.5R10
subVersion 1.0
isp-network test
subnet 1.1.1.1/32
subnet 2.2.2.2/32
member CERNET
exit
上传自定义IPv4 ISP配置文件
用户可以通过FTP/FTPS/SFTP/TFTP服务器上传自定义IPv4 ISP配置文件，在执行模式下，使用以下命令：
import ispfile from {ftp server ip-address [user user-name password password ] | ftps
server ip-address [user user-name password password ] | sftp server ip-address [user username password password ] | tftp server ip-address } [vrouter vr-name] file-name

<!-- 来源页 520 -->
l
ip-address - 指定FTP/FTPS/SFTP/TFTP服务器的IP地址。
l
user username password password - 指定FTP/FTPS/SFTP服务器的用户名和密码。
l
vrouter vr-name – 指定FTP/FTPS/SFTP/TFTP服务器所属的VRouter。
l
file-name - 指定自定义IPv4 ISP配置文件名称。
下载自定义IPv4 ISP信息配置文件
用户仅可通过WebUI方式将在设备上配置的自定义IPv4 ISP信息保存到电脑。保存步骤如下：
1. 选择“网络> 路由> ISP信息”。
2. 选择“IPv4”标签页。
3. 点击“下载”按钮，弹出<下载自定义ISP配置文件>对话框。
4. 在“ISP名称”下拉菜单中选择需要保存的IPv4 ISP的名称。
5. 点击“保存”按钮，保存相应的IPv4 ISP配置文件到电脑的指定位置。
配置IPv6 ISP信息
在设备上配置IPv6 ISP信息，首先需要进入IPv6 ISP信息配置模式。在全局配置模式下，使用以下命令，创
建IPv6 ISP名称并且进入IPv6 ISP信息配置模式：
isp-network isp-name ipv6
l
isp-name – 指定IPv6 ISP名称，系统最多允许创建26个IPv6 ISP信息。
l
ipv6 - 指定ISP信息类型为IPv6。
在全局配置模式下，使用该命令no的形式删除指定名称的IPv6 ISP：
no isp-network isp-name
添加IPv6子网条目
为IPv6 ISP添加子网条目，在IPv6 ISP信息配置模式下，使用以下命令：
subnet ipv6-address/prefix
l
ipv6-address/prefix – 为IPv6 ISP指定子网，格式为IPv6地址/前缀长度，例如1::1/64，系统最多
允许添加的子网条目数根据平台不同而不同，范围是1000-6000个。
在IPv6 ISP信息配置模式下配置多条该命令，为IPv6 ISP添加多个子网。
在IPv6 ISP信息配置模式下使用该命令no的形式删除指定的子网：
no subnet ipv6-address/prefix

<!-- 来源页 521 -->
添加IPv6 ISP信息条目
为IPv6 ISP添加IPv6 ISP信息条目，即添加其他已配置的IPv6 ISP信息（预定义IPv6 ISP信息或自定义IPv6
ISP信息），在IPv6 ISP信息配置模式下，使用以下命令：
member isp-name
l
isp-name – 指定IPv6 ISP名称。系统支持的IPv6 ISP嵌套层数最多为1层，并且不支持回环嵌套，
IPv6 ISP信息不可以再嵌套它所属的ISP信息。
在IPv6 ISP信息配置模式下配置多条该命令，为ISP添加多个IPv6 ISP信息条目。系统最多允许添加8个IPv6
ISP信息条目。
在IPv6 ISP信息配置模式下使用该命令no的形式删除指定嵌套的IPv6 ISP信息条目：
no member isp-name
注意: IPv6 ISP 信息和IPv4 ISP信息不允许相互嵌套。
配置IPv6 ISP路由
IPv6 ISP路由需要在VRouter配置模式下进行配置。进入VRouter配置模式，在全局配置模式下使用以下命
令：
ip vrouter vrouter-name
l
vrouter-name – 指定VRouter的名称。
在VRouter配置模式，使用以下命令配置ISP路由条目：
ipv6 route isp-name {A.B.C.D | interface-name | vrouter vrouter-name} [distance-value]
[weight weight-value] [description description] [schedule schedule-name]
l
isp-name – 指定系统中已存在的IPv6 ISP名称作为路由的目的地址。
l
A.B.C.D | interface-name | vrouter vrouter-name – 指定下一跳。可以是网关地址（A.B.C.D）、
接口（interface-name）或者VRouter（vrouter vrouter-name）。当下一跳为接口时，用户可以
选择隧道接口名称、Null0接口或者PPPoE接口。
l
distance-value – 指定路由的管理距离大小。该参数设定路由的优先级，取值越小，优先级越高，而
在有多条路由选择的时候，优先级高的路由会被优先使用。取值范围是1到255，默认值为10。当路由距
离为255时，该路由无效。

<!-- 来源页 522 -->
l
weight weight-value – 指定路由权值的大小。路由权值决定负载均衡中流量转发的比重。范围是1到
255，默认值是1。
l
description description – 指定路由的描述信息。范围是1到63个字符。
l
schedule schedule-name – 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配
置多次该命令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的
时间表。
使用多条该命令添加多条IPv6 ISP路由条目。
使用以上命令no的形式删除指定的IPv6 ISP路由条目：
no ipv6 route isp-name {A.B.C.D | interface-name | vrouter vrouter-name } [distance-value]
[weight weight-value] [description description] [schedule schedule-name]
查看IPv6 ISP信息
用户可以通过show命令查看IPv6 ISP配置文件信息，在任何模式下，使用以下命令：
l
查看预定义IPv6 ISP配置文件信息：
show ipv6 pre-isp-network {all | isp-name}
l
查看自定义IPv6 ISP配置文件信息：
show ipv6 isp-network {all | isp-name}
上传/下载自定义IPv6 ISP配置文件
设备支持两种IPv6 ISP配置文件，分别是用户自定义IPv6 ISP配置文件和系统预定义IPv6 ISP配置文件。
l
自定义IPv6 ISP配置文件：请按照下所示实例格式书写用户自定义配置文件，否则，即使文件上传成
功，也不可以在系统中生效。
Software Version 5.5 SG6000-MX_MAIN-68-V6-r1018.bin 202211040257
!
Version 5.5R10
subVersion 1.0
isp-network testv6 ipv6
subnet 1::1/128
subnet 2::2/128

<!-- 来源页 523 -->
member CERNET-v6
exit
上传自定义IPv6 ISP配置文件
用户可以通过FTP/FTPS/SFTP/TFTP服务器上传自定义IPv6 ISP配置文件，在执行模式下，使用以下命令：
import ispfile from {ftp server ip-address [user user-name password password ] | ftps
server ip-address [user user-name password password ] | sftp server ip-address [user username password password ] | tftp server ip-address } [vrouter vr-name] file-name
l
ip-address - 指定FTP/FTPS/SFTP/TFTP服务器的IP地址。
l
user username password password - 指定FTP/FTPS/SFTP服务器的用户名和密码。
l
vrouter vr-name – 指定FTP/FTPS/SFTP/TFTP服务器所属的VRouter。
l
file-name - 指定自定义IPv6 ISP配置文件名称。
下载自定义IPv6 ISP信息配置文件
用户仅可通过WebUI方式将在设备上配置的自定义IPv6 ISP信息保存到电脑。保存步骤如下：
1. 选择“网络> 路由> ISP信息”。
2. 选择“IPv6”标签页。
3. 点击“下载”按钮，弹出<下载自定义ISP配置文件>对话框。
4. 在“ISP名称”下拉菜单中选择需要保存的IPv6 ISP的名称。
5. 点击“确定”按钮，保存相应的IPv6 ISP配置文件到电脑的指定位置。

<!-- 来源页 524 -->
配置源路由
源路由的配置需要在VRouter配置模式下完成。进入VRouter配置模式，在全局配置模式下，使用以下命
令：
ip vrouter vrouter-name
添加源路由条目
在VRouter配置模式下，使用以下命令添加一条源路由条目：
ip route source {A.B.C.D/M | A.B.C.D A.B.C.D} {A.B.C.D | interface-name | vrouter vroutername} [distance-value] [weight weight-value] [schedule schedule-name] [track track-name]
l
A.B.C.D/M | A.B.C.D A.B.C.D – 指定源路由条目的网络地址。设备支持两种方式，A.B.C.D/M或者
A.B.C.D A.B.C.D，例如1.1.1.0/24或者1.1.1.0 255.255.255.0。
l
A.B.C.D | interface-name – 指定下一跳。可以是网关地址（A.B.C.D）、接口（interface-name）
或者VRouter（vrouter vrouter-name）。当下一跳为接口时，用户可以选择隧道接口、Null0接口
或者PPPoE接口。
l
distance-value – 指定路由的管理距离大小。该参数设定路由的优先级，取值越小，优先级越高，而
在有多条路由选择的时候，优先级高的路由会被优先使用。取值范围是1到255，默认值为1。当路由距
离为255时，该路由无效。
l
weight weight-value – 指定路由权值的大小。路由权值决定负载均衡中流量转发的权重。范围是1到
255，默认值是1。
l
schedule schedule-name – 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配
置多次该命令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的
时间表。
l
track track-name – 指定已创建的监测对象名称。指定后，若针对该监测对象的监测失败，则该路由
无效。
使用以上命令no的形式删除指定的源路由条目：
no ip route source { A.B.C.D/M | A.B.C.D A.B.C.D} {A.B.C.D | interface-name}
查看源路由条目信息
用户可以在任何模式下通过show命令查看源路由条目信息。在任何模式下，使用以下命令：

<!-- 来源页 525 -->
源路由：show ip route source [vrouter vrouter-name]
l
vrouter-name – 显示指定的VRouter的源路由信息。
配置源接口路由
源接口路由的配置也需要在VRouter配置模式下完成。进入VRouter配置模式，在全局配置模式下，使用以
下命令：
ip vrouter vrouter-name
添加源接口路由条目
在VRouter配置模式下，使用以下命令添加一条源接口路由条目：
ip route source in-interface interface-name { A.B.C.D/M | A.B.C.D A.B.C.D} {A.B.C.D |
interface-name | vrouter vrouter-name} [distance-value] [weight weight-value] [schedule
schedule-name] [track track-name]
l
interface-name – 指定路由条目的入接口。
l
A.B.C.D/M | A.B.C.D A.B.C.D – 指定路由条目的源网络地址。Hillstone设备支持两种方式，
A.B.C.D/M或者A.B.C.D A.B.C.D，例如1.1.1.0/24或者1.1.1.0 255.255.255.0。
l
A.B.C.D | interface-name | vrouter vrouter-name – 指定下一跳。可以是网关地址（A.B.C.D）、
接口（interface-name）或者VRouter（vrouter vrouter-name）。当下一跳为接口时，用户可以
选择隧道接口名称，也可以选择Null0接口（黑洞路由）。
l
distance-value – 指定路由的管理距离大小。该参数设定路由的优先级，取值越小，优先级越高，而
在有多条路由选择的时候，优先级高的路由会被优先使用。取值范围是1到255，默认值为1。当路由距
离为255时，该路由无效。
l
weight weight-value – 指定路由权值的大小。路由权值决定负载均衡中流量转发的权重。范围是1到
255，默认值是1。
l
schedule schedule-name – 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配
置多次该命令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的
时间表。
l
track track-name – 指定已创建的监测对象名称。指定后，若针对该监测对象的监测失败，则该路由
无效。
使用以上命令no的形式删除指定的源接口路由条目：

<!-- 来源页 526 -->
no ip route source in-interface interface-name { A.B.C.D/M | A.B.C.D A.B.C.D} {A.B.C.D |
interface-name | vrouter vrouter-name }
查看源接口路由条目信息
用户可以在任何模式下通过show命令查看源接口路由条目信息。在任何模式下，使用以下命令：
源接口路由：show ip route source in-interface interface-name

<!-- 来源页 527 -->
配置策略路由
配置策略路由（PBR），根据数据包的源地址、源用户、目的地址和服务选择路由并进行转发。
创建PBR策略组
创建PBR策略组，在全局配置模式下使用以下命令：
pbr-policy name
l
name – 指定PBR策略组的名称，名称范围是1到31个字符。如果该策略组已经创建，则直接进入PBR策
略配置模式。
使用no pbr-policy name删除指定的PBR策略组。
创建PBR规则
进入PBR策略配置模式下，用户便可定义自己的PBR规则。在CLI中创建PBR规则的命令如下：
{match | match-v6 } [id rule-id] [name name] [before rule-id | after rule-id | top] src-addr
dst-addr service-name [application-name] nexthop {interface-name | A.B.C.D | vrouter
vrouter-name | vsys vsys-name} [weight value] [track track-object-name]
l
id rule-id – 指定新建策略规则的ID，取值范围为1到255。如果不指定，系统将会为PBR规则自动分配
一个ID。规则ID在该PBR策略中必须是唯一的。
l
name name – 指定新建策略规则的名称，取值范围为1-95个字符。
l
before rule-id | after rule-id | top – 指定PBR规则的位置，可以是某个规则之前（before ruleid）、某个规则之后（after rule-id）或者所有规则的首位（top）。默认情况下，系统会将新创建的
策略规则放到所有规则的末尾。
l
src-addr – 指定源地址，该地址为地址簿条目。
l
dst-addr – 指定目的地址，该地址为地址簿条目。
l
service-name – 指定服务名称。service-name为服务簿中定义的服务。
l
application-name – 指定应用名称。application-name 为应用簿中定义的应用。
l
nexthop {interface-name | A.B.C.D | vrouter vrouter-name | vsys vsys-name} – 指定下一
跳。interface-name为出接口的名称，A.B.C.D为下一跳的IP地址，vrouter vrouter-name为
VRouter，vsys vsys-name为虚拟系统。单条策略路由规则最多支持配置64个下一跳。

<!-- 来源页 528 -->
l
weight value – 指定下一跳的权重，取值范围是1到255，默认值是1。如果一条策略路由匹配多个下
一跳，系统会按照权重值比例分配流量。
l
track track-object-name – 指定下一跳的监测对象。如果监控对象失败，本条策略路由也会失败。关
于如何配置监测对象，请参阅“系统管理“的“配置监测对象”部分。
使用该命令no的形式删除指定ID的规则。在PBR策略配置模式下，执行以下命令：
no {match | match-v6} id rule-id
另外，用户还可以在PBR策略配置模式下使用以下命令，创建一个策略规则ID，并且进入PBR策略规则配置
模式，再进一步配置其它策略规则相关参数：
{match | match-v6} [id rule-id] [name name] [ before rule-id | after rule-id | top]
l
id id – 指定PBR策略规则的ID。如果不指定，系统将会为策略规则自动分配一个ID。规则ID在整个系统
中必须是唯一的。策略规则的ID大小并不表示策略规则的匹配先后顺序。
l
name name –指定新建策略规则的名称，取值范围为1-95个字符。
l
top | before rule-id | after rule-id – 指定策略规则的位置，可以是某个规则ID之前（before
id）、某个规则ID之后（after id）或者所有规则的首位（top）。默认情况下，系统会将新创建的策略
规则放到所有规则的末尾。
注意: 关于如何配置其它策略相关参数，请参考下一节“编辑PBR策略规则”。
编辑PBR策略规则
创建好的PBR策略规则可以通过编辑来修改不合适的参数值，但是修改工作必须在PBR策略规则配置模式下
才可以进行。在CLI中进入PBR策略规则配置模式，请输入以下命令：
l
{match | match-v6} id rule-id（该命令适用于规则ID已存在的情况，并且用该命令no的形式，可以
删除该条规则，即no {match | match-v6} id rule-id）
l
{match | match-v6} name name（该命令适用于规则名称已存在的情况，并且用该命令no的形式，
可以删除该条规则，即no {match | match-v6} name name）
进入PBR策略规则配置模式后，可使用的编辑策略规则的命令如下：
l
添加策略规则名称：name name
l
删除策略规则名称：no name

<!-- 来源页 529 -->
l
添加地址簿条目类型源地址：src-addr src-addr
l
删除地址簿条目类型源地址：no src-addr src-addr
l
添加IP成员类型源地址：src-ip {ip/netmask | ip-address netmask}
l
删除IP成员类型源地址：no src-ip {ip/netmask | ip-address netmask}
l
添加主机成员类型源地址：src-host host-name
l
删除主机成员类型源地址：no src-host host-name
l
添加IP地址范围类型源地址：src-range min-ip max-ip
l
删除IP地址范围类型源地址：no src-range min-ip max-ip
l
添加外部动态列表类型源地址：src-ip-external-dynamic-list name name
l
name - 指定外部动态列表的名称。仅支持指定IP类型的外部动态列表。name非自定义项，为系
统中已配置的IP类型的外部动态列表名称。
l
删除外部动态列表类型源地址：no src-ip-external-dynamic-list name name
l
添加地址簿条目类型目的地址：dst-addr dst-addr
l
删除地址簿条目类型目的地址：no dst-addr dst-addr
l
添加IP成员类型目的地址：dst-ip ip/netmask
l
删除IP成员类型目的地址：no dst-ip ip/netmask
l
添加主机成员类型目的地址：dst-host host-name
l
删除主机成员类型目的地址：no dst-host host-name
l
添加IP地址范围类型目的地址：dst-range min-ip [max-ip]
l
删除IP地址范围类型目的地址：no dst-range min-ip [max-ip]
l
添加外部动态列表类型目的地址：dst-ip-external-dynamic-list name name
l
name - 指定外部动态列表的名称。仅支持指定IP类型的外部动态列表。name非自定义项，为系
统中已配置的IP类型的外部动态列表名称。
l
删除外部动态列表类型目的地址：no dst-ip-external-dynamic-list name name
l
添加角色类型源用户：role role-name
l
删除角色类型源用户：no role role-name
l
添加用户类型源用户：user aaa-server-name user-name
l
删除用户类型源用户：no user aaa-server-name user-name

<!-- 来源页 530 -->
l
添加用户组类型源用户：user-group aaa-server-name user-group-name
l
删除用户组类型源用户：no user-group aaa-server-name user-group-name
l
添加服务类型：service service-name
l
删除服务类型：no service service-name
l
添加应用类型：application application-name
l
删除应用类型：no application application-name
l
添加域名簿：host-book { any | domain-name | predef-domain-geo }
注意:
l
一条策略路由规则仅支持引用一个域名簿。
l
配置了域名簿的策略路由规则只能被HTTP、HTTPS流量命中。
l
删除域名簿：no host-book{ any | domain-name | predef-domain-geo }
l
指定下一跳：nexthop {interface-name | A.B.C.D | vrouter-name | vsys vsys-name}
l
取消下一跳配置：no nexthop
l
绑定多路包复制模板：duplicate-profile profile-name（详细说明请参阅"基于策略路由的多路包复
制" 在第155页。）
l
解除多路包复制模板的绑定：no duplicate-profile
l
配置时间表：schedule schedule-name
l
删除时间表：no schedule
l
添加规则描述：description string
l
删除规则描述：no description
l
开启日志记录功能：log enable
l
关闭日志记录功能：no log enable
配置BFD监测方式
当策略路由的下一跳类型为IP地址或隧道接口时，用户可以指定BFD监测方式，用于快速检测链路连通性。

<!-- 来源页 531 -->
注意:
l
策略路由只支持BFD单跳检测，不支持BFD多跳检测。
l
当下一跳的IP地址和BFD出接口的IP地址不在同一网段时，BFD监测不会生效。
l
当下一跳类型为IP地址时，如果BFD出接口的主IP和二级IP在同一网段，则设备只会使用出接
口的主IP发送BFD消息。
配置BFD监测方式，在PBR策略规则配置模式下，使用以下命令：
nexthop {IP-address | interface-name} bfd BFD-interface BFD-peer-IP
l
IP-address - 指定下一跳类型为IP地址并输入对应的IP地址。
l
interface-name - 指定下一跳类型为接口并选择对应的隧道接口。
l
BFD-interface - 指定BFD出接口。
l
BFD-peer-IP - 指定BFD对端的IP地址。若下一跳类型为隧道接口，则BFD对端IP地址一般设置为对端
隧道接口的IP地址。
取消配置BFD监测方式，在PBR策略规则配置模式下，使用以下命令：
no nexthop {IP-address | interface-name} bfd
启用/禁用PBR策略规则
默认情况下，配置好的PBR策略规则会在系统中立即生效。用户可以通过命令禁用某条策略规则，使其不对
流量进行控制。禁用或者启用某条策略规则，在PBR策略规则配置模式下，使用以下命令：
l
禁用：disable
l
启用：enable
开启/关闭地址反选功能
如果用户要对指定源/目的地址进行排除，不希望某些源/目的地址被匹配，则可以开启地址反选功能。该功
能默认为关闭状态。
例如：开启源地址反选功能，并指定策略路由规则的源地址为1.1.1.1。表示只有源地址为1.1.1.1的流量不
会匹配该条规则，其余源地址都能够匹配。
开启/关闭源地址反选功能，在PBR策略规则配置模式下，使用以下命令：
l
开启：src-reverse enable

<!-- 来源页 532 -->
l
关闭：no src-reverse enable
开启/关闭目的地址反选功能，在PBR策略规则配置模式下，使用以下命令：
l
开启：dst-reverse enable
l
关闭：no dst-reverse enable
修改规则排列顺序
PBR策略中的规则通过ID进行唯一标识。流量进入设备时，设备对PBR策略规则进行顺序查找，然后按照查
找到的相匹配的第一条规则对流量进行处理。但是，PBR策略规则ID的大小顺序并不是规则查找时的匹配顺
序。使用show pbr-policy命令列出的规则顺序才是规则匹配顺序（系统将由上到下进行查找匹配）。用户
在创建PBR策略规则时可以指定该规则的排列位置，也可以在PBR策略配置模式下修改其位置。PBR策略规
则的排列位置可以是绝对位置，即处在首位（Top）或者处在末位（Bottom），也可以是相对位置，即位
于某个ID之前或之后。修改规则排列顺序，在PBR策略配置模式下使用以下命令：
move rule-id {top | bottom | before rule-id | after rule-id}
配置目的路由优先查找
默认情况下，设备对进入的数据包进行转发时，按照这样的顺序选路：策略路由>源接口路由>源路由>目的
路由，在某些情况下，用户需要使匹配PBR策略规则的数据包，转发时优先查找目的路由，即选路的顺序
为：目的路由à策略路由。配置PBR策略规则的目的路由（DBR）优先查找，在PBR策略规则配置模式下，使
用以下命令：
fib-lookup dbr-first
使用以上命令no的形式取消PBR策略规则的目的路由（DBR）优先查找：no fib-lookup dbr-first
应用PBR策略
可以通过绑定PBR策略到接口、安全域或者VRouter来实现PBR策略的应用。在接口配置模式、安全域配置
模式或VRouter配置模式下，使用以下命令：
bind pbr-policy name
l
name – 绑定指定的PBR策略到接口、安全域或者VRouter。
使用以上命令no的形式取消PBR策略在接口、安全域或者VRouter的绑定：
no bind pbr-policy

<!-- 来源页 533 -->
配置PBR策略全局匹配顺序
默认情况下，如果接口和其所在安全域或者VRouter绑定了PBR策略，流量匹配顺序为：接口->安全域-
>VRouter。用户可以根据需要自行配置PBR策略的全局匹配顺序，在全局配置模式下，使用以下命令：
pbr-match order index
l
index –为PBR策略指定全局匹配顺序的排序指数。包括1-6，顺序分别表示如下：
l
1 - 接口->安全域->Vrouter。该排序指数为默认值。
l
2 - 安全域->接口->Vrouter。
l
3 - Vrouter ->安全域->接口。
l
4 - 接口-> Vrouter ->安全域。
l
5 - Vrouter ->接口->安全域。
l
6 - 安全域-> Vrouter->接口。
使用no pbr-match恢复默认匹配顺序配置。
显示PBR策略全局匹配顺序
用户可以在任何模式下，通过show命令查看PBR策略规则的全局匹配顺序信息。具体命令以下：
show pbr-match order
策略路由规则支持配置TTL
用户可以在PBR规则中配置报文的TTL，符合条件的报文将被设备转发到特定的出口链路。配置TTL，请先执
行以下命令进入PBR策略规则配置模式：
l
match [id rule-id] [ before rule-id | after rule-id | top]
l
match id rule-id（该命令适用于规则ID已存在的情况）
在PBR策略规则配置模式下，输入以下命令：
ttl-range min-ttl max-ttl
l
min-ttl max-ttl – 指定策略路由规则中报文的生存时间范围。min-ttl指定生存时间的最小值，取值范
围为1到255；max-ttl指定生存时间的最大值，取值范围为1到255。
在PBR策略规则配置模式下，执行no ttl-range命令取消TTL范围的配置。

<!-- 来源页 534 -->
查看PBR策略规则信息
用户可以在任何模式下，通过show命令查看PBR策略规则的具体信息。具体命令以下：
show pbr-policy [name]
l
name – 显示指定PBR策略的详细信息。如果不指定名称则显示所有PBR策略的详细信息。
DNS重定向
系统支持DNS重定向，即在用户向DNS服务器发出域名请求时，系统将DNS请求重定向到指定的DNS服务器
地址。目前，DNS重定向主要应用于视频引流。通过和PBR策略结合，系统可将Web视频网站的流量引流到
指定的链路上，进而提升用户访问视频的体验。
在全局配置模式下,使用以下命令开启或关闭DNS重定向功能：
app cache dns-redirect {enable | disable}
l
enable – 开启DNS重定向功能。开启后，用户可根据系统提示指定DNS服务器地址，然后系统会将用
户的DNS请求重定向到指定的DNS服务器上。
l
disable – 关闭DNS重定向功能。默认情况下，系统关闭该功能。
在任何模式下，使用show dns-redirect命令查看DNS服务器和接口（该接口为PBR策略绑定的入接口）之
间的绑定关系。
配置案例
l
"例：Web视频引流配置案例" 在第665页
开启/关闭PBR延迟更新功能
当PBR的源地址或目的地址配置了域名簿时，若DNS更新了相关域名，PBR会相应进行更新。默认情况下，
PBR会有1秒的缓冲延迟更新，避免短时间内频繁更新导致系统负担过大。但同时，在这1秒的缓冲延迟更新
期间，会存在新的业务匹配不上PBR的情况，因此系统支持关闭PBR延迟更新，在DNS更新时立即触发PBR
更新。
PBR延迟更新功能默认开启。开启/关闭PBR延迟更新功能，在全局配置模式下，使用以下命令：
l
开启PBR延迟更新：pbr dns-update-delay enable
l
关闭PBR延迟更新：pbr dns-update-delay disable
在策略路由中绑定多路包复制模板
开始之前

<!-- 来源页 535 -->
l 阅读"多路包复制" 在第154页功能介绍。
l 阅读"基于策略路由的多路包复制" 在第155页介绍。
在策略路由中绑定多路包复制模板，需先进入PBR策略规则配置模式。如何进入PBR策略规则配置模式，请
参阅"配置策略路由" 在第525页章节。
绑定多路包复制模板
用户需根据业务规划需求，将多路包复制模板绑定到指定策略路由规则中。1个多路包复制模板最多可以被8
条策略路由（PBR）规则绑定。
绑定多路包复制模板，在PBR策略规则配置模式下，使用以下命令：
duplicate-profile profile-name
l
profile-name - 指定需要绑定的多路包复制模板名称。
在PBR策略规则配置模式下，使用以下命令，解除多路包复制模板的绑定：
no duplicate-profile
示例：
hostname(config)# pbr-policy test vrouter trust-vr （创建PBR策略路由并进入PBR策略配置模
式）
hostname(config-pbr)# match id 1 （创建PBR策略规则ID，并且进入PBR策略规则配置模式）
hostname(config-pbr-match)# src-ip 20.0.0.0/24 （指定源地址）
hostname(config-pbr-match)# dst-ip 40.0.0.0/24 （指定目的地址）
hostname(config-pbr-match)# service "Any" （指定服务）
hostname(config-pbr-match)# nexthop tunnel1 （指定下一跳）
hostname(config-pbr-match)# nexthop tunnel2
hostname(config-pbr-match)# duplicate-profile test （绑定多路包复制模板）
hostname(config-pbr-match)# exit
hostname(config-pbr)# exit
下一步
在策略路由中绑定多路包复制模板后，请根据业务规划需求，逐项核查配置步骤的完成情况。待所有配置完
成后，通过Ping命令检查多路包复制链路的连通性，确保配置无误且链路正常。
示例：

<!-- 来源页 536 -->


<!-- 来源页 537 -->
域名路由
域名路由支持配置目的域名和下一跳地址，通过DNS Snooping主动解析或者被动解析建立并更新目的域名
与IP地址的映射关系信息，生成路由。系统根据目的IP地址查询路由进行数据转发。同时，支持在OSPF中重
分发域名路由。
域名路由仅支持通过CLI配置。
相关链接：
l 关于DNS Snooping主动解析或者被动解析的相关配置，请参阅：命令行手册> DNS Snooping。
l 关于OSPF重分发路由的相关配置，请参阅：命令行手册> 配置OSPF-引入路由。
配置域名路由
用户可以添加域名路由条目并且查看域名路由信息。
添加域名路由条目
域名路由的配置需要在VRoute配置模式下完成。进入VRouter配置模式，请在全局配置模式下使用以下命
令：
ip vrouter vrouter-name
l
vrouter vrouter-name– 指定VRouter的名称。
进入到VRouter配置模式下后，用户可以添加域名路由条目。在VRouter配置模式下使用以下命令：
domain route domain-name {A.B.C.D | interface-name [A.B.C.D] | vrouter vrouter-name}
[distance-value] [weight weight-value] [description description] [schedule schedulename]
l
domain-name– 指定目的域名。仅支持精确域名（如“www.test.com”）。
l
A.B.C.D | interface-name [A.B.C.D] | vrouter vrouter-name– 指定下一跳。可以是网关地址
（A.B.C.D）、接口（interface-name）或者VRouter（vrouter vrouter-name）。当下一跳为接
口时，用户可以选择隧道接口名称（当为多隧道接口时，用户必须使用A.B.C.D参数指定IPSec VPN、
GRE或者SCVPN隧道的下一跳IP地址，并且此地址必须和该隧道接口绑定的相应隧道的下一跳IP地址相
同）、Null0接口或者PPPoE接口。

<!-- 来源页 538 -->
l
distance-value– 指定路由的管理距离大小。该参数设定路由的优先级，取值越小，优先级越高，而
在有多条路由选择的时候，优先级高的路由会被优先使用。取值范围是1到255，默认值为1。当路由距
离为255时，该路由无效。
l
weight weight-value– 指定路由权值的大小。路由权值决定负载均衡中流量转发的比重。范围是1到
255，默认值是1。
l
description description– 指定路由的描述信息。范围是1到63个字符。
l
schedule schedule-name– 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配
置多次该命令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的
时间表。
使用多条该命令添加多条域名路由条目。
使用以上命令no的形式删除指定的域名路由条目：
no domain route domain-name {A.B.C.D | interface-name [A.B.C.D] | vrouter vrouter-name}
[distance-value] [weight weight-value] [description description] [schedule schedulename]
查看域名路由信息
用户可以在任何模式下使用以下命令查看域名路由信息：
show ip route domain-route domain-name [vrouter vrouter-name]
l
domain-name- 查看指定域名的域名路由信息。
l
vrouter-name- 查看指定的VRouter的域名路由信息。
查看域名路由状态
用户可以在任何模式下使用以下命令查看域名路由状态：
show domain-route status [vrouter vrouter-name]
l
vrouter-name- 查看指定的VRouter的域名路由状态。

<!-- 来源页 539 -->
动态路由
动态路由是根据网络系统的运行情况而自动调整的路由。Hillstone设备根据路由协议自动调整动态路由
表。StoneOS支持RIP、OSPF、IS-IS和BGP四种动态路由协议。
l "配置RIP" 在第537页
l "配置OSPF路由协议" 在第543页
l "配置IS-IS" 在第559页
l "配置BGP协议" 在第574页
配置RIP
RIP（Routing Information Protocol）是路由信息协议。它是一种在路由器之间交换路由信息的内部网
关路由协议。目前，RIP有RIP-1和RIP-2两个版本，设备均支持。
对RIP协议的配置包括基本配置、引入路由、被动接口、邻居、网络和距离。另外，RIP参数配置完成后，用
户还需要在不同的接口上配置RIP参数，包括指定接口接收和发送更新的RIP版本号、水平分割以及接口的
RIP认证。
基本配置
RIP协议的基本配置包括指定RIP版本号、指定缺省度量、指定缺省距离、配置缺省信息发布以及配置定时器
（时间间隔、失效时间、保持时间和清除时间）。用户可以为不同的VRouter分别配置RIP协议。对RIP协议
的基本配置需要在RIP路由模式下进行。进入RIP路由模式，请在全局配置模式下，使用以下命令：
ip vrouter vrouter-name （进入VRouter配置模式）
router rip（进入RIP路由模式，同时开启设备的RIP功能）
在VRouter配置模式下，使用no router rip关闭RIP功能。
指定版本号
Hillstone设备支持RIP-1和RIP-2两个版本。RIP-1以广播方式传输报文；而RIP-2使用组播方式。指定RIP
协议版本号，在RIP路由模式使用以下命令：
version version-number
l
version-number – 指定版本号，1（RIP-1）或者2（RIP-2）。默认为2。
使用no version命令恢复默认版本配置。

<!-- 来源页 540 -->
指定缺省度量
RIP协议使用跳数来衡量到达目的网络的距离，称为度量。路由器到与它直接相连网络的度量为1，通过一个
路由器可达的网络的度量为2，依此类推，度量的最大值可以到15，度量大于15的网络为不可达网络。缺省
度量在引入路由时生效。指定RIP的缺省度量，在RIP路由配置模式下使用以下命令：
default-metric value
l
value – 指定缺省度量值。范围是1到15，默认值是1。
使用no default-metric命令恢复缺省度量值。
指定缺省距离
指定RIP路由的缺省距离，在RIP路由配置模式下使用以下命令：
distance distance-value
使用no distance命令恢复缺省距离值。
配置缺省信息发布
用户可以指定是否默认路由发布到其它使用RIP协议的路由器。默认情况下，RIP协议不发送默认路由。配置
缺省信息发布，在RIP路由配置模式下使用以下命令：
发送：default-information originate
不发送：no default-information originate
配置定时器
RIP可配置的定时器分别是时间间隔（Interval）、失效时间（Invalid）、保持时间（Holddown）和清除
时间（Flush）。具体描述如下：
l
时间间隔：每次向所有邻居发送全部RIP路由所间隔的时间。默认是30秒。
l
失效时间：如果一条路由在失效时间内一直没有被更新，该路由的度量就会被标记为16，表示为不可达
路由。默认的失效时间是180秒。
l
保持时间：如果一条更新后的路由的度量变大，例如，从2更新到4，该路由会被赋予一个保持时间，路
由在保持时间内，不接受任何更新。默认的保持时间是180秒。
l
清除时间：度量被标记为16的不可达路由会一直被发布到其它RIP协议路由，直到清除时间结束；如果该
路由仍没有被更新，清除时间结束后，将会被从RIP路由信息数据库中删除。默认的清除时间是240秒。
用户可以修改以上四个定时器的时间值。配置定时器，在RIP路由配置模式下使用以下命令：
timers basic interval-time invalid-time holddown-time flush-time

<!-- 来源页 541 -->
l
interval-time – 指定发送更新的时间间隔，单位为秒。范围是0到16777215秒。默认值是30秒。
l
invalid-time – 指定路由的失效时间，单位为秒。范围是1到16777215秒。默认值是180秒。
l
holddown-time – 指定路由的保持时间，单位为秒。范围是1到16777215秒。默认值是180秒。
l
flush-time – 指定路由的清除时间，单位为秒。范围是1到16777215秒。默认值是240秒。
使用no timers basic命令恢复定时器的默认值。
引入路由
RIP协议允许用户将设备上其它路由协议（BGP、直连、静态、OSPF和IS-IS）的路由信息引入到RIP中，并
向外发布。同时，用户可以设置被引入路由的度量。配置引入路由，在RIP路由配置模式下使用以下命令：
redistribute {bgp | connected | static | ospf | isis } [metric value]
l
bgp | connected | static | ospf | isis – 指定引入路由的类型，可以是BGP（bgp）、直连路由
（connected）、静态路由（static）、OSPF（ospf）或者IS-IS（isis）。
l
metric value – 指定引入路由的度量。范围是1到15。如果不指定该数值，系统会使用RIP的缺省度量
（通过default-metric value配置）。
用户可以配置多条该命令引入不同类型的路由。
使用no redistribute {bgp | connected | static | ospf | isis}命令取消指定类型路由的引入。
配置被动接口
用户可以将一些接口配置为只接收更新但是不发送，这种只接收更新的接口就是被动接口。配置被动接口，
在RIP路由配置模式下使用以下命令：
passive-interface interface-name
l
interface-name – 指定接口的名称作为被动接口。
用户可以配置多条该命令添加多个被动接口。
使用no passive-interface interface-name命令取消被动接口的配置。
配置邻居
用户可以指定一些邻居，使邻居和Hillstone设备之间能够允许点到点（非广播）的RIP信息交换。指定邻
居，在RIP路由配置模式下使用以下命令：
neighbor ip-address
l
ip-address – 指定邻居的IP地址。

<!-- 来源页 542 -->
用户可以配置多条该命令添加多个邻居。
使用no neighbor ip-address命令删除指定的邻居。
配置网络
用户需要配置一些网络，只有在指定网络中的接口才能接收和发送RIP更新。配置网络，在RIP路由配置模式
下使用以下命令：
network ip-address/netmask
l
ip-address/netmask – 指定网络的IP地址，例如10.200.0.0/16。
用户可以配置多条该命令添加多个网络。
使用no network ip-address/netmask命令删除指定的网络。
配置距离
用户可以为从一些指定网络得到的路由指定管理距离。配置距离，在RIP路由配置模式下使用以下命令：
distance distance-value ip-address/netmask
l
distance-value – 指定管理距离。范围是1到255。用该命令指定的距离优先级高于RIP基本配置中的
缺省距离（通过distance distance-value指定）。
l
ip-address/netmask – 指定网络的IP地址，例如10.200.0.0/16。
用户可以配置多条该命令为从不同的网络更新的路由指定距离。
使用no distance ip-address/netmask命令删除指定的管理距离。
RIP数据库
设备运行RIP协议，就拥有一个RIP路由数据库，该数据库中储存了所有可达目的网络的路由条目。路由条目
包含的信息有目的地址、下一跳、度量、来源以及定时器信息。用户可以在任何模式下，通过以下命令，随
时查看RIP数据库的信息：
show ip rip database [A.B.C.D/M] [vrouter vrouter-name]
l
A.B.C.D/M – 显示指定目的IP地址的RIP信息。
l
vrouter vrouter-name– 显示指定VRouter的RIP信息。StoneOS目前只支持trust-vr一个
VRouter。
配置接口的RIP功能
RIP功能在设备接口上的配置包括：认证方式、发送和接收的RIP版本号以及水分割功能。接口的RIP功能配
置需要在接口配置模式下完成。

<!-- 来源页 543 -->
配置RIP报文认证
只有RIP-2支持RIP报文认证。认证方式有两种，分别是明文认证和MD5密文认证。明文认证不能提供安全保
障。未加密的认证字随RIP报文一同传送，所以明文认证不能用于安全性要求较高的情况。默认为明文认
证。用户需要配置RIP报文的认证方式和认证码。在接口配置模式下，使用以下命令：
l
方式：ip rip authentication mode {md5 | text}
l
认证码：ip rip authentication string string
使用以上两个命令no的形式可以取消对认证方式和认证码的指定：
l
no ip rip authentication mode
l
no ip rip authentication string
配置发送和接收的RIP版本号
默认情况下，接口发送RIP-2信息。指定接口发送RIP信息的版本号，在接口配置模式下，使用以下命令：
ip rip send version [1][2]
l
1 – 指定只发送RIP-1的RIP信息。
l
2 – 指定只发送RIP-2的RIP信息。
使用no ip rip send version命令恢复默认版本号。
默认情况下，接口接收RIP-2信息。指定接口接收RIP信息的版本号，在接口配置模式下，使用以下命令：
ip rip receive version [1][2]
l
1 – 指定只发送RIP-1的RIP信息。
l
2 – 指定只发送RIP-2的RIP信息。
使用no ip rip receive version命令恢复默认版本号。
配置水平分割
水平分割是指不从本接口发送从该接口学到的路由。它可以在一定程度上避免产生路由环，保证路由的正确
传播。配置水平分割功能，在接口配置模式下，使用以下命令：
开启水平分割：ip rip split-horizon
关闭水平分割：no ip rip split-horizon
显示系统RIP信息
用户可以通过show命令随时查看系统的RIP信息。查看RIP信息，在任何模式下使用以下命令：

<!-- 来源页 544 -->
show ip rip
配置OSPF
OSPF是开放式最短路径优先协议（Open Shortest Path First）的缩写。它是IETF组织开发的一个基于链
路状态的内部网关协议。当前的OSPF版本为版本2（RFC2328）。OSPF适应各种规模的网络，快速收敛特
性能够在网络拓扑结构发生变化后立即发送更新报文，并且其算法本身决定了不会生成路由环路。OSPF还
具有以下特性：
l 区域划分：将自治系统的网络划分成区域来管理，从而减少了协议对CPU和内存的占用，提高性能。
l 无类路由：无类路由特性允许可变长子网掩码的使用。
l 等价路由：支持等价路由，提高多条路由的利用率。
l 组播发送：支持组播地址发送，减少对非OSPF设备的影响。
l 支持验证：支持基于接口的报文验证以保证路由计算的安全性。
说明：“自治系统”是处于一个管理机构控制之下的路由器和网络群组。一个自治系统中的所有路由器必须
运行相同的路由协议。
OSPF GR
GR（Graceful Restart）即平滑重启，也被称作NSF（Non-Stop Forwarding）。在运行OSPF协议的网
络环境中，OSPF GR可以保证HA主备切换时网络流量不中断。
如上图所示，设备A和设备B组成HA Active-Passive（A/P）模式，进行HA主备切换时，新主设备与相邻
设备Router Y的OSPF邻居关系会断开并重新建立，引起路由震荡和业务中断。配置OSPF GR功能后，进行
HA主备切换时，新主设备进入GR Restarter状态，并向邻居Router Y发送Grace LSA，通告GR周期、GR
原因和接口地址等信息。Router Y收到Grace LSA后，进入GR Helper状态，并会在GR周期内保持与新主
设备的邻居关系，协助新主设备完成GR，保证数据转发不中断。
OSPF GR基础概念：
l GR Restarter：GR重启的设备，即由于HA主备切换导致OSPF路由协议重启的设备。
l GR Helper：GR Restarter的邻居，具有GR能力，协助GR Restarter进行GR的设备。

<!-- 来源页 545 -->
l Grace LSA：Opaque LSA的Type-9 LSA的一种，用于支持OSPF GR功能。Grace LSA在HA主备切换时生成，
向邻居通告GR周期、GR原因和接口地址等信息。
注意:
l
OSPF GR功能支持设备HA Active-Passive（A/P）模式以及双主控HA，不支持HA Peer模
式。
l
以下场景中的设备可以作为GR Restarter，其它场景下的设备只支持作为GR Helper：
l
进行设备HA切换的新主设备;
l
进行双主控（SCM）HA切换的设备（X系列所有型号、K系列K20803/K9180）。
l
如果主备设备间的HA连接断开，则OSPF GR功能不生效。
配置OSPF路由协议
用户可以为不同的VRouter分别配置OSPF协议。OSPF协议配置包括以下各项：
l 配置Router ID
l 配置区域认证
l 配置接口的网络类型
l 配置区域的路由聚合
l 配置区域的缺省花费
l 配置区域的虚拟链路
l 配置stub区域
l 配置NSSA区域
l 配置接口发送OSPF报文的缺省花费
l 配置缺省度量
l 配置缺省信息发布
l 配置缺省距离
l 配置OSPF定时器
l 指定运行OSPF协议的接口网络
l 引入路由

<!-- 来源页 546 -->
l 配置距离
l 配置被动接口
l 配置基于路由访问控制列表的路由过滤
l 配置ABR路由聚合
l 配置ASBR路由聚合
l 配置OSPF GR
开启OSPF功能
OSPF协议的基本配置需要在OSPF路由模式下进行。进入OSPF路由模式，请在VRouter配置模式下，使用
以下命令：
ip vrouter vrouter-name（进入VRouter配置模式）
router ospf [process-id]（进入OSPF路由模式，同时开启Hillstone设备的OSPF功能）
l
process-id – 指定OSPF的进程ID。默认值是1，取值范围是1到65535。每个OSPF进程相互独立，有
各自的链路状态数据库和对应的OSPF路由表信息。每一个VRouter支持最多4个OSPF进程，多个进程共
同维护一个VRouter的路由表。
在指定OSPF进程ID时，注意如下事项：
l
每个OSPF进程中运行OSPF协议的接口网络不能重叠。
l
当多个OSPF进程中存在相同前缀的路由条目时，首先比较比较各个路由条目的管理距离，管理距离低的
将被优先加入到VRouter的路由表中；管理距离相同时，优先发现的的路由条目将被加入到VRouter的
路由表中。
l
当其他路由协议引入OSPF路由时，将默认引入进程ID为1的OSPF路由信息。如果此进程不存在，将无法
引入OSPF路由。
在VRouter配置模式下，使用no router ospf [process-id]关闭OSPF功能。
配置Router ID
每一台运行OSPF协议的路由器都必须拥有一个Router ID。Router ID是每个路由器在整个OSPF域中唯一
标识，使用IP地址的形式表示。为Hillstone设备的OSPF协议配置Router ID，在OSPF路由模式下，使用以
下命令：
router-id A.B.C.D [local]

<!-- 来源页 547 -->
l
A.B.C.D – 指定OSPF协议使用的Router ID，为IP地址形式。
l
local - 指定OSPF协议的Router ID为本地配置，该配置适用于HA A/A工作模式，并且不进行HA配置
同步。默认情况下，Router ID为非本地配置。
配置区域认证
用户可以配置区域的认证方式。默认情况下，区域是没有认证方式的。配置区域的认证方式，在OSPF路由
模式下，使用以下命令：
area {id | A.B.C.D} authentication [message-digest]
l
id | A.B.C.D – 指定区域ID。区域ID用32比特数来表示，可以是数字形式，也可以是IP地址形式。
l
[message-digest] – 指定使用MD5认证方式。如果不使用该关键字，则为明文认证。
用该命令指定的认证类型必须与区域内其它的路由相同。同一网络中通过OSPF协议通信的路由器的认证密
码必须相同。
使用no area {id | A.B.C.D} authentication命令取消对认证方式的指定。
配置接口的网络类型
OSPF协议的接口的网路类型有以下三种：广播、点到点（Point-to-point）以及点到多点（Point-tomultipoint）网络类型。默认情况下，接口的网络类型为广播类型。配置接口的网络类型，在接口配置模式
下，使用以下命令：
ip ospf network {point-to-point | point-to-multipoint}
l
point-to-point – 指定接口网络类型为点到点网络类型。
l
point-to-multipoint -指定接口网络类型为点到多点网络类型。
在隧道接口配置模式下，使用该命令no的形式恢复接口网络类型为广播类型：
no ip ospf network
配置区域的路由聚合
路由聚合是指将具有相同前缀的路由信息通过ABR聚合在一起，只发布一条路由到其它区域。一个区域可以
配置多条聚合网段，这样OSPF可以对多个网段进行聚合。默认情况下，区域的路由聚合功能是关闭的。配
置区域的路由聚合，在OSPF路由模式下，使用以下命令：
area {id | A.B.C.D} range {A.B.C.D/M} [advertise | not-advertise]
l
id | A.B.C.D– 指定需要进行路由聚合的区域ID。区域ID用32比特数来表示，可以是数字形式，也可以
是IP地址形式。

<!-- 来源页 548 -->
l
range {A.B.C.D/M} – 指定被聚合的网段。
l
advertise – 指定将这一网段的路由聚合并通告聚合后的路由。
l
not-advertise – 指定将这一网段的路由聚合且不通告聚合后的路由。
路由聚合功能仅对区域边界路由（连接骨干区域和非骨干区域的路由器，简称为ABR）有效。
使用no area {id | A.B.C.D} range {A.B.C.D/M} [advertise | not-advertise]命令取消路由聚合的配
置。
配置区域的缺省花费
区域的缺省花费是指将报文发送到stub区域的缺省路由花费。指定区域的缺省花费，在OSPF路由模式下，
使用以下命令：
area {id | A.B.C.D} default-cost cost-value
l
id | A.B.C.D – 指定需要指定缺省花费的区域ID。区域ID用32比特数来表示，可以是数字形式，也可以
是IP地址形式。
l
cost-value – 指定花费值。默认值是1。范围是0到16777214。
使用no area {id | A.B.C.D} default-cost命令恢复缺省花费的配置。
注意: 该命令仅对NSSA区域有效。
配置区域的虚拟链路
虚拟链路（Virtual Links）用来连接不连续的骨干区域，使他们能够保持逻辑上的连续性。配置虚拟链路以
及定时器参数，在OSPF路由模式下，使用以下命令：
area {id | A.B.C.D} virtual-link A.B.C.D [hello-interval interval-value] [retransmit-interval
interval-value] [transmit-delay interval-value] [dead-interval interval-value]
l
id | A.B.C.D – 需要做虚拟链路进行连接的区域ID。区域ID用32比特数来表示，可以是数字形式，也可
以是IP地址形式。
l
virtual-link A.B.C.D – 指定作为虚拟链路路由器的Router ID。
l
hello-interval interval-value– 指定接口发送Hello报文的时间间隔，单位为秒，默认值是10秒。范
围是1到65535秒。

<!-- 来源页 549 -->
l
retransmit-interval interval-value – 一台路由器向它的邻居发送一条LSA后需要获得对方的确认报
文。若在指定的时间内没有收到对方的确认报文，就会向邻居重传这条LSA。该参数用来指定邻接路由器
之间重传LSA的时间间隔，单位为秒，默认值是5秒。范围是3到65535秒。
l
transmit-delay interval-value – 指定更新包的延迟时间，单位为秒，默认值是1秒。范围是1到
65536秒。
l
dead-interval interval-value – 如果路由器在一定的时间内都没有收到对方的Hello报文，则认为对
端路由器失效，这个一定的时间就是相邻路由器间的失效时间。该参数指定失效时间值，单位为秒，默
认值是40秒。范围是1到655635秒。
使用no area {id | A.B.C.D} virtual-link A.B.C.D [hello-interval] [retransmit-interval] [transmitdelay] [dead-interval]命令恢复定时器的默认时间值。
用户可以配置虚拟链路的认证方式。在OSPF路由模式下，使用以下命令：
area {id | A.B.C.D} virtual-link A.B.C.D authentication [message-digest] [authentication-key
string] [message-digest-key ID md5 string] [null]
l
id | A.B.C.D – 需要做虚拟链路进行连接的区域ID。区域ID用32比特数来表示，可以是数字形式，也可
以是IP地址形式。
l
virtual-link A.B.C.D– 指定作为虚拟链路路由器的Router ID。
l
message-digest – 指定使用MD5认证。
l
authentication-key string – 指定明文认证的认证密码。
l
message-digest-key ID md5 string – 指定MD5认证的认证ID和密码。
l
null – 不使用认证。
使用no area {id | A.B.C.D} virtual-link A.B.C.D authentication [message-digest]
[authentication-key string] [message-digest-key ID]命令取消认证配置。
配置stub区域
stub区域是不收发Type-5的LSA（AS-external-LSAs）区域。对于产生大量Type-5 LSA的网络，这种处
理方式能够有效减小stub区域内路由器的LSDB规模，并缓解SPF计算对路由器资源的占用。stub区域通常
位于自治系统边界。配置OSPF的stub区域，在OSPF路由模式下，使用以下命令：
area {id | A.B.C.D} stub [no-summary]

<!-- 来源页 550 -->
l
id | A.B.C.D – 指定stub区域的区域ID。区域ID用32比特数来表示，可以是数字形式，也可以是IP地址
形式。
l
no-summary – 阻止ABR向stub区域发送3类或4类汇总LSA。
使用no area {id | A.B.C.D} stub [no-summary]命令取消stub区域的配置。
配置NSSA区域
Stub区域不能引入外部路由，为了在允许将自治系统外部路由通告到OSPF路由域内部的同时，保持其余部
分的Stub区域的特征，网络管理员可以将区域配置为NSSA区域。配置OSPF的NSSA区域，在OSPF路由模
式下，使用以下命令：
area {id | A.B.C.D} nssa [no-summary | no-redistribution | default-information-originate]
l
id | A.B.C.D – 指定NSSA区域的区域ID。区域ID用32比特数来表示，可以是数字形式，也可以是IP地址
形式。
l
no-summary | no-redistribution | default-information-originate – no-summary参数只用于
NSSA区域的ABR，配置后，NSSA ABR只通过Type-3的Summary-LSA向区域内发布一条缺省路由，
不再向区域内发布任何其它Summary-LSAs（这种区域又称为Totally NSSA区域）。noredistribution参数用于禁止将AS外部路由以Type-7 LSA的形式引入到NSSA区域中，这个参数通常只
用在既是NSSA区域的ABR，也是OSPF自治系统的ASBR的路由器上，以保证所有外部路由信息能正确
地进入OSPF路由域。default-information-originate参数只用于NSSA区域的ABR或ASBR，配置
后，对于ABR，不论本地是否存在缺省路由，都将生成一条Type-7 LSA向区域内发布缺省路由；对于
ASBR，只有当本地存在缺省路由时，才产生Type-7 LSA向区域内发布缺省路由。
使用no area {id | A.B.C.D} nssa [no-summary | no-redistribution | default-informationoriginate]命令取消NSSA区域的配置。
配置OSPF的引用带宽
OSPF可以根据接口的带宽计算接口发送OSPF报文的花费。配置OSPF的引用带宽，在OSPF路由模式下，使
用以下命令：
auto-cost reference-bandwidth bandwidth
l
bandwidth – 指定带宽值，单位为Mbps，默认值是100。范围是1到4294967。
使用no auto-cost reference-bandwidth命令使OSPF根据接口的类型计算接口发送OSPF报文的花费。

<!-- 来源页 551 -->
指定缺省度量
此处配置的OSPF协议的缺省度量在引入路由时生效。指定OSPF的缺省度量，在OSPF路由配置模式下使用
以下命令：
default-metric value
l
value – 指定缺省度量值。范围是1到16777214。
使用no default-metric命令恢复缺省度量的默认值。
配置缺省信息发布
用户可以指定是否将默认路由发布到其它使用OSPF协议的路由器。默认情况下，是不发送默认路由的。配
置缺省信息发布，在OSPF路由配置模式下使用以下命令：
default-information originate [always] [type {1｜2}] [metric value]
l
always – OSPF无条件产生并发送默认路由。
l
type {1｜2} – 指定与发送到OSPF路由域的默认路由相关联的外部路由的类型。1指type1外部路由，2
指type2外部路由。
l
metric value – 指定发送默认路由的度量。如果不使用该命令配置度量并且也没有使用defaultmetric value配置默认度量，其默认度量将会是20。范围是0到16777214。
使用no default-information originate命令恢复默认值。
指定缺省距离
指定OSPF路由的缺省距离，在OSPF路由配置模式下使用以下命令：
distance distance-value
l
distance-value – 指定缺省管理距离。范围是1到255，默认值是110。
使用no distance命令恢复缺省距离的默认值。
配置OSPF定时器
用户可以指定以下两个OSPF协议的定时器：OSPF收到更新后在多长时间内进行重新计算以及OSPF两次计
算的时间间隔。配置OSPF定时器，在OSPF路由配置模式下使用以下命令：
timers spf delay1 delay2
l
delay1 – 收到更新后，在该指定时间内进行重新计算，单位为秒。范围是0到65535，默认值是5秒。
l
delay2 – 指定两次计算的时间间隔，单位为秒。范围是0到65535，默认值是10秒。
使用no timers spf命令恢复默认值。

<!-- 来源页 552 -->
指定运行OSPF协议的接口网络
指定运行OSPF协议的接口网络并且将网络配置到指定的区域中，在OSPF路由配置模式下使用以下命令：
network A.B.C.D/M area {id | A.B.C.D}
l
A.B.C.D/M – 指定运行OSPF协议的接口网络。
l
area {id | A.B.C.D} – 指定将网络添加到的区域ID。区域ID用32比特数来表示，可以是数字形式，也可
以是IP地址形式。
使用no network A.B.C.D/M area {id | A.B.C.D}命令取消对网络的指定。
引入路由
OSPF协议允许用户引入其他OSPF进程路由信息以及其它路由协议（BGP、IS-IS、直连、静态、RIP、
VPN、ISP或者域名路由）的路由信息，并向外发布。用户可以设置被引入路由的度量以及外部路由的类
型，还可以引用路由映射表对路由信息进行过滤，仅允许引入或拒绝引入特定的路由信息。配置引入路由，
在OSPF路由配置模式下使用以下命令：
redistribute {bgp | connected | isis | ospf process-id | static | rip | vpn | domain| isp} [type {1 |
2}] [metric value] [route-map name] [tag tag-value]
l
bgp | connected | isis | ospf process-id | static | rip | vpn | domain| isp– 指定引入路由的类
型，可以是BGP（bgp）、ISIS(isis)、指定的OSPF进程（ospf process-id）、直连路由
（connected）、静态路由（static）、RIP（rip）、VPN路由（vpn）、域名路由（domain）或者
ISP路由（isp）。
l
type {1｜2} – 指定外部路由的类型。1指type1外部路由，2指type2外部路由。
l
metric value – 指定引入路由的度量。范围是0到16777214。如果不指定该数值，系统会使用OSPF的
缺省度量（通过default-metric value配置）。
l
route-map name –指定用于过滤引入路由信息的路由映射表。有关路由映射表的更多信息，请参阅"
路由映射表" 在第591页。
l
tag tag-value – 指定引入的路由的标记值。取值范围是1到4294967295。
用户可以配置多条该命令引入不同类型的路由。
使用no redistribute {bgp | connected | isis | ospf process-id | static | rip | vpn | domain | isp}
命令取消指定类型路由的引入。
配置距离
用户可以根据路由类型指定管理距离。配置距离，在OSPF路由配置模式下使用以下命令：

<!-- 来源页 553 -->
distance ospf {intra-area distance-value | inter-area distance-value | external distancevalue}
l
intra-area distance-value – 指定区域内路由的管理距离。默认值是110。范围是1到255。
l
inter-area distance-value – 指定区域间路由的管理距离。默认值是110。范围是1到255。
l
external distance-value – 指定外部type5类型路由的管理距离。默认值是110。范围是1到255。
使用no distance ospf命令恢复距离的默认值。
配置被动接口
用户可以将一些接口配置为只接收更新但是不发送，这种只接收更新的接口就是被动接口。配置被动接口，
在OSPF路由配置模式下使用以下命令：
passive-interface interface-name
l
interface-name – 指定接口的名称作为被动接口。
用户可以配置多条该命令添加多个被动接口。
使用no passive-interface interface-name命令取消被动接口的配置。
配置基于路由访问控制列表的路由过滤
OSPF协议支持通过路由访问控制列表对引入的路由进行过滤。配置基于路由访问控制列表的路由过滤，在
OSPF路由配置模式下，使用以下命令：
distribute-list access-list-name in [interface-name]
l
access-list-name – 指定路由访问控制列表的名称。关于路由访问控制列表的更多信息，请参阅"路由
访问控制列表" 在第596页。
l
in – 指定对引入的路由（in）进行过滤。
l
interface-name – 指定接口名称。指定后，将过滤从指定接口学习到的OSPF路由。如果不指定接口名
称，系统将过滤所有OSPF路由。
如果不指定接口名称，系统将过滤所有OSPF路由。
使用该命令no的形式取消基于路由访问控制列表的路由过滤的配置：
no distribute-list access-list-name in [interface-name]
配置ABR路由聚合
ABR（Area Border Router）即区域边界路由器，用于连接骨干区域和非骨干区域的路由器。ABR路由聚
合指的是ABR向其他区域通告路由信息时，将具有相同前缀的路由信息以网段为单位进行聚合，只通告一条

<!-- 来源页 554 -->
路由到其它区域。一个区域可以配置多条聚合网段，这样OSPF可以对多个网段进行聚合。该功能默认为关
闭状态。
注意: 仅能够在ABR设备上配置和执行ABR路由聚合功能。
配置ABR路由聚合，在OSPF路由模式下，使用以下命令：
area {id | A.B.C.D} range {A.B.C.D/M} [advertise | not-advertise] [cost cost]
l
id | A.B.C.D – 指定需要进行路由聚合的区域ID。区域ID用32比特数来表示，可以是数字形式，也可以
是IP地址形式。
l
range {A.B.C.D/M} – 指定聚合路由的网段地址及掩码。
l
advertise – 通告聚合路由。
l
not-advertise – 不通告聚合路由。
l
cost cost – 指定聚合路由的开销值，取值范围为0-16777214。
说明：到目的地址的开销值=到ABR的开销值+配置的聚合路由开销值。若不配置，则到目的地址的开销
值=到ABR的开销值+所有被聚合路由中最大的开销值。
取消配置ABR聚合路由的开销值，在OSPF路由模式下，使用以下命令：
no area {id | A.B.C.D} range {A.B.C.D/M} cost
删除ABR聚合路由，在OSPF路由模式下，使用以下命令：
no area {id | A.B.C.D} range {A.B.C.D/M}
配置ASBR路由聚合
ASBR（AS Boundary Routers）即自治系统边界路由器，用于和其他自治系统交换路由信息的路由器。只
要一台OSPF路由器引入了外部路由信息，则该路由器就成为ASBR。ASBR路由聚合是OSPF在自治系统边界
对外部路由进行聚合，ASBR能够将引入的多条外部路由聚合成一条，从而减少OSPF网络内部的路由条目，
减轻网络负担，提高路由处理效率。该功能默认为关闭状态。
注意:
l
仅能够在ASBR设备上配置和执行ASBR路由聚合功能。
l
不支持对NSSA区域中的Type-7 LSA以及由Type-7 LSA转换成的Type-5 LSA进行ASBR路由
聚合。
配置ASBR路由聚合，在OSPF路由模式下，使用以下命令：

<!-- 来源页 555 -->
summary-address A.B.C.D/M [not-advertise] [cost cost] [tag tag]
l
A.B.C.D/M – 指定聚合路由的网段地址及掩码。
l
not-advertise – 不通告聚合路由，若不配置则将通告聚合路由。
l
cost cost – 指定聚合的外部路由的开销值，取值范围为0-16777214。
说明：
l
到第一类外部路由的开销值=内部到达ASBR的开销值+配置的外部路由开销值。若不配置，则到第
一类外部路由的开销值=内部到达ASBR的开销值+所有被聚合路由中最大的外部路由开销值。
l
到第二类外部路由的开销值=配置的外部路由开销值。若不配置，则到第二类外部路由的开销值=
所有被聚合路由中最大的外部路由开销值。
l
tag tag – 指定聚合路由的标记，用户可以根据标记过滤路由或限制流量进入特定网络。取值范围为1-
4294967295，若不配置，则功能不生效。
取消配置ASBR聚合路由的不通告聚合路由、开销值、标记，在OSPF路由模式下，使用以下命令：
no summary-address A.B.C.D/M {[not-advertise] [cost cost] [tag tag]}
删除ASBR聚合路由，在OSPF路由模式下，使用以下命令：
no summary-address A.B.C.D/M
配置OSPF GR
配置OSPF GR包含以下内容：
l
启用Opaque LSA发布接收能力
l
启用GR Restarter的GR功能
l
配置GR Restarter的GR周期
l
启用GR Helper功能
l
启用GR Helper严格检查
l
查看OSPF GR信息
启用Opaque LSA发布接收能力
Opaque LSA是用于OSPF的扩展通用机制，它包括Type-9 LSA、Type-10 LSA和Type-11 LSA。
Opaque LSA通过Type-9 LSA中的Grace LSA支持OSPF GR功能。
注意: 使用OSPF GR功能前，需要首先启用Opaque LSA发布接收能力。

<!-- 来源页 556 -->
启用Opaque LSA发布接收能力，在OSPF路由模式下，使用以下命令：
capability opaque
在OSPF路由模式下，使用no capability opaque命令关闭Opaque LSA发布接收能力。
启用GR Restarter的GR功能
启用GR Restarter的GR功能，在OSPF路由模式下，使用以下命令：
graceful-restart ietf enable
在OSPF路由模式下，使用no graceful-restart ietf enable命令关闭GR Restarter的GR功能。
配置GR Restarter的GR周期
GR周期即GR的超时时间，在GR周期内，GR Helper会维持与GR Restarter的邻居关系；超过GR周期后，
无论GR是否完成，GR Helper会退出GR Helper状态。
配置GR Restarter的GR周期，在OSPF路由模式下，使用以下命令：
graceful-restart ietf interval value
l
value - 指定GR Restarter的GR周期，取值范围为1-1800秒。默认值为120秒。当邻居数量较多时，
建议通过该命令调大GR周期。
在OSPF路由模式下，使用no graceful-restart ietf interval命令恢复默认值。
启用GR Helper功能
启用GR Helper功能，在OSPF路由模式下，使用以下命令：
graceful-restart ietf helper enable
在OSPF路由模式下，使用no graceful-restart ietf helper enable命令关闭GR Helper功能。
启用GR Helper严格检查
配置GR Helper严格检查功能后，当GR Helper设备检查到LSA发生变化时，GR Helper设备会退出GR
Helper状态。配置GR Helper严格检查功能，在OSPF路由模式下，使用以下命令：
graceful-restart ietf helper strict-lsa-checking
在OSPF路由模式下，使用no graceful-restart ietf helper strict-lsa-checking命令关闭GR Helper严
格检查功能。
查看OSPF GR信息
查看OSPF GR信息，在任何模式下使用以下命令：
show ip ospf graceful-restart [vrouter vrouter-name]

<!-- 来源页 557 -->
l
vrouter vrouter-name - 显示指定VRouter的OSPF GR信息，如不指定则显示默认VRouter，即
trust-vr的OSPF GR信息。
配置接口的OSPF功能
接口的OSPF功能配置需要在接口配置模式下完成。OSPF协议在Hillstone设备接口上的配置包括：
l 配置接口的OSPF认证
l 指定接口的链路花费
l 配置接口定时器
l 指定接口路由器优先级
l 配置接口的网络类型
配置接口的OSPF认证
接口的OSPF认证优先于区域OSPF认证。Hillstone设备支持明文认证和MD5认证。默认情况下，接口的
OSPF认证是关闭的。开启或者关闭接口的OSPF认证功能，在接口配置模式下使用以下命令：
ip ospf authentication
no ip ospf authentication
配置明文认证的认证密码，在接口配置模式下，使用以下命令：
ip ospf authentication-key string
l
string – 指定认证密码（最多为8个字符）。
使用no ip ospf authentication-key命令取消密码配置。
配置MD5认证ID和密码，在接口配置模式下，使用以下命令：
ip ospf message-digest-key ID md5 string
l
ID – 指定认证ID。
l
string – 指定认证密码。
使用no ip ospf message-digest-key ID命令取消密码配置。
指定接口的链路花费
指定接口的链路花费，在接口配置模式下，使用以下命令：
ip ospf costcost-value [local]

<!-- 来源页 558 -->
l
cost-value – 指定接口的链路花费。取值范围是1到65535。
l
local – 指定接口的链路花费为local。当设备处于HA A/A模式时，配置此参数，该接口的链路花费值
将不会同步到备份设备，从而使两台设备具有不同的链路花费值，避免出现非对称OSPF路由。
使用no ip ospf cost [local]命令取消对所需花费的指定。
配置接口定时器
接口的定时器有以下四个：接口发送Hello包的时间间隔、接口相邻路由器的失效时间、接口重传LSA的时间
间隔以及接口更新包的延迟时间。
指定接口发送Hello包的时间间隔，在接口配置模式下，使用以下命令：
ip ospf hello-interval interval
l
interval – 指定接口发送Hello包的时间间隔，单位为秒。默认值是10秒。范围是1到65535秒。
使用no ip ospf hello-interval恢复默认时间间隔。
如果接口在一定的时间内都没有收到对方的Hello报文，则认为对端路由器失效，这个一定的时间就是相邻
路由器间的失效时间。指定接口的相邻路由失效时间，在接口配置模式下，使用以下命令：
ip ospf dead-interval interval
l
interval – 指定接口的相邻路由失效时间，单位为秒。默认值是40秒（发送Hello包时间间隔的4倍）。
范围是1到65535秒。
使用no ip ospf dead-interval恢复默认失效时间。
指定接口重传LSA的时间间隔，在接口配置模式下，使用以下命令：
ip ospf retransmit-interval interval
l
interval – 指定接口重传LSA的时间间隔，单位为秒。默认值是5秒。范围是3到65535秒。
使用no ip ospf retransmit-interval恢复默认时间间隔。
指定接口更新包的延迟时间，在接口配置模式下，使用以下命令：
ip ospf transmit-delayinterval
l
interval – 指定接口更新包的延迟时间，单位为秒。默认值是1秒。范围是1到65535秒。
使用no ip ospf transmit-delay恢复默认延迟时间。

<!-- 来源页 559 -->
指定接口路由器优先级
路由器的优先级用来决定使用哪个路由器作为指定路由器。指定路由器用来接收网络中所有其它路由器的链
路信息，并将收到的链路信息广播出去。指定接口路由器的优先级，在接口配置模式下，使用以下命令：
ip ospf priority level
l
level – 指定路由器的优先级。默认值是1。范围是0到255。优先级为0的路由器不会被选中作为指定路
由器。当同一个网络的两个路由器都可作为指定路由器时，优先级高的路由器会被选中；如果优先级也
相同，Router ID高的会被选中。
使用no ip ospf priority命令恢复默认优先级。
配置接口的网络类型
OSPF协议的接口的网路类型有以下三种：广播、点到点（Point-to-point）以及点到多点（Point-tomultipoint）网络类型。默认情况下，接口的网络类型为广播类型。配置接口的网络类型，在接口配置模式
下，使用以下命令：
ip ospf network {point-to-point | point-to-multipoint}
l
point-to-point – 指定接口网络类型为点到点网络类型。
l
point-to-multipoint -指定接口网络类型为点到多点网络类型。
在隧道接口配置模式下，使用该命令no的形式恢复接口网络类型为广播类型：
no ip ospf network
通过show命令查看OSPF信息
显示OSPF路由信息，在任何模式下使用以下命令：
show ip route ospf [vrouter vrouter-name]
l
vrouter-name - 显示指定的VRouter的OSPF路由信息。
显示防火墙的OSPF信息，在任何模式下使用以下命令：
show ip ospf [vrouter vrouter-name] [process process-id]
l
vrouter-name - 指定VRouter名称。
l
process process-id – 指定OSPF进程ID。
显示防火墙OSPF协议的数据库信息，在任何模式下使用以下命令：

<!-- 来源页 560 -->
show ip ospf database {asbr-summary | external | nssa-external | network | router |
summary} [A.B.C.D] [{adv-router A.B.C.D} | self-originate] [vrouter vrouter-name] [process
process-id]
l
asbr-summary – 显示自制系统边界路由LSAs。
l
external – 显示外部路由LSAs。
l
nssa-external - 显示NSSA的外部LSA的有关信息。
l
network – 显示网络LSAs。
l
router – 显示路由LSAs。
l
summary – 显示汇总LSAs。
l
A.B.C.D - 链路状态ID，以IP地址形式表示。
l
adv-router A.B.C.D – 显示指定路由器的LSAs。
l
self-originate - 只显示自己产生的LSA（从本地路由器）。
l
vrouter-name - 指定VRouter名称。
l
process process-id – 指定OSPF进程ID。
show ip ospf database [max-age | self-originate] [vrouter vrouter-name] [process processid]
l
max-age - 指定最大老化时间。
l
self-originate - 只显示自己产生的LSA（从本地路由器）。
l
vrouter-name - 指定VRouter名称。
l
process process-id – 指定OSPF进程ID。
显示OSPF接口信息，在任何模式下使用以下命令：
show ip ospf interface [interface-name] [vrouter vrouter-name] [process process-id]
显示OSPF虚拟链路信息，在任何模式下使用以下命令：
show ip ospf virtual-links [vrouter vrouter-name] [process process-id]
显示OSPF邻居信息，在任何模式下使用以下命令：
show ip ospf neighbor [A.B.C.D | detail] [vrouter vrouter-name] [process process-id]
显示OSPF路由信息，在任何模式下使用以下命令：
show ip ospf route [A.B.C.D] [vrouter vrouter-name] [process process-id]
显示路由映射表信息，在任何模式使用以下命令：

<!-- 来源页 561 -->
show route-map [name]
显示路由访问控制列表信息，在任何模式使用以下命令：
show access-list route [name]
显示OSPF路由过滤信息，在任何模式下使用以下命令：
show ip ospf distribute-list [vrouter vrouter-name] [process process-id]
用户可以通过以下命令查看OSPF邻居关系断开信息，诊断和分析邻居关系异常的原因。系统最多显示20条
最新的邻居关系断开记录。显示OSPF邻居关系断开（Down）的信息，在任何模式下使用以下命令：
show ip ospf neighbor last-nbr-down [vrouter vrouter-name] [process process-id]
l
vrouter-name - 指定VRouter名称。若不指定，会显示trust-vr内所有OSPF进程的邻居关系断开信
息。
l
process process-id – 显示指定进程的OSPF邻居关系断开信息。若不指定，会显示指定VR内
（vrouter-name）所有的OSPF进程的邻居关系断开信息。
以下是一个返回结果示例：
hostname# show ip ospf neighbor last-nbr-down
OSPF Router with ID 90.1.1.11, OSPF Process ID 1
Last Down OSPF Neighbor
Neighbor Ip Address : 90.1.1.2 （邻居接口的IP地址）
Neighbor Area Id : 0.0.0.0 （邻居所属的区域）
Neighbor Router Id : 90.1.1.21 （邻居的Router ID）
Interface : ethernet0/2 （与邻居相连的本地接口）
Down Reason : Neighbor Down Due to 1-Wayhello Received （邻居断开的具体原因）
Down Time : 2024-12-11 10:51:15 （邻居断开的具体日期和时间）
Hello Last Sent Time : 2024-12-11 10:51:07 （最后一次发送Hello报文的时间）
Hello Last Received Time : 2024-12-11 10:51:15 （最后一次接收Hello报文的时间）
配置IS-IS
IS-IS（Intermediate System-to-Intermediate System）最初是ISO为CLNP（Connection-Less
Network Protocol）设计的一种动态路由协议。为了提供对IP的路由支持，IETF（Internet Engineering
Task Force）在RFC 1195中对IS-IS进行了扩充和修改，使它能够同时应用在TCP/IP和OSI环境中，称为集
成化IS-IS （Integrated IS-IS或Dual IS-IS）。IS-IS属于IGP（Interior Gateway Protocol），用于自
治系统内部。IS-IS是一种链路状态协议，使用SPF（Shortest Path First）算法进行路由计算。
StoneOS支持应用在TCP/IP网络环境中的IS-IS动态路由协议。

<!-- 来源页 562 -->
用户可以为不同的VRouter分别配置IS-IS动态路由协议。IS-IS协议配置包括以下各项：
l 指定路由器类型
l 使能接口IS-IS
l 配置接口IS-IS类型
l 配置网络类型为点对点类型
l 配置NET地址
l 配置管理距离
l 配置度量类型
l 配置接口度量值
l 引入路由
l 发布缺省路由
l 配置Hello报文发送时间间隔
l 配置Hello报文失效乘数
l 配置Hello报文填充功能
l 配置被动接口
l 配置DIS选举优先级
l 配置LSP生成时间间隔
l 配置LSP最大生存时间
l 配置LSP刷新时间
l 配置SPF计算时间间隔
l 配置过载标志位
l 配置主机名映射
l 配置认证
l 配置接口认证模式
IS-IS基本配置
IS-IS动态路由协议的基本配置需要在IS-IS路由配置模式下进行。进入IS-IS路由配置模式，依次使用以下命
令：
ip vrouter vrouter-name – 在全局配置模式下执行此命令，进入VRouter配置模式。

<!-- 来源页 563 -->
router isis – 进入IS-IS路由配置模式，同时在此VRouter创建一个IS-IS进程。每个VRouter的IS-IS进程之
间相互独立。
需要关闭IS-IS进程时，在VRouter配置模式下，使用no router isis。
指定路由器类型
路由器类型包括：Level-1路由器，Level-2路由器，以及Level-1-2路由器。指定路由器类型，在IS-IS路
由配置模式下，使用如下命令：
is-type [level-1 | level-1-2 | level-2-only]
l
level-1 | level-1-2 | level-2-only – 指定路由器类型为Level-1路由器（level-1）, Level-2路由器
(level-2), Level-1-2路由器（level-1-2）。路由器默认类型为Level-1-2类型。只有当路由器类型为
Level-1-2时，用户可对接口的类型进行指定。
取消路由器类型配置，在IS-IS路由配置模式下，使用no is-type命令。
使能接口IS-IS
默认情况下，IS-IS功能在接口上处于关闭状态。在当前路由器上创建IS-IS进程后，需要在接口上使能ISIS。在接口配置模式下，使用如下命令：
isis enable
使用no isis enable命令在接口上关闭IS-IS功能。
提示: 系统支持在GRE over IPSec场景下使能tunnel接口IS-IS。并且，使能IS-IS协议后的
tunnel接口仅支持与山石网科设备对接。支持使能tunnel接口IS-IS的型号包含A系列，K系列
（除K20803、K9180）、云·界。
配置接口IS-IS类型
当路由器类型是Level-1时，接口的邻接类型只能为Level-1；当路由器类型是Level-2时，接口的邻接类型
只能为Level-2；当路由器类型是Level-1-2时，接口的邻接类型默认为level-1-2类型。配置接口的邻接类
型，在接口配置模式下，使用如下命令：
isis circuit-type [level-1 | level-1-2 | level-2-only]
l
level-1 | level-1-2 | level-2-only – 指定接口类型为level-1邻接类型接口（level-1），level-2邻
接类型接口（level-2-only）或者level-1-2邻接类型接口（level-1-2）。

<!-- 来源页 564 -->
配置网络类型为点对点类型
当只有两台设备接入到广播网络时，可以配置接口所在链路的类型为点对点链路类型。对于点对点链路类
型，IS-IS不进行DIS选举和CSNP泛洪。在接口配置模式下，使用如下命令：
isis network point-to-point
使用no isis network point-to-point命令取消点对点链路类型设置。
IS-IS路由信息配置
配置NET地址
NET（Network Entity Title，网络实体名称）指示的是IS本身的网络层信息，不包括传输层信息，可以看
作是一类特殊的NSAP，即SEL为0的NSAP地址。NET地址用来标识开启IS-IS进程的设备。一个IS-IS进程的
设备最多可以配置3个NET地址。这三个NET地址的区域地址可以不同，但是System ID必须相同。指定设备
的NET地址，在IS-IS路由配置模式下，使用如下命令：
net net [local]
l
net – 指定NET地址。在建立Level-1邻居时，区域地址必须相同，否则无法建立邻居。在建立Level-2
邻居时，不检查区域地址是否相同。
l
local - 指定NET地址为本地配置，该配置适用于HA Peer模式，并且不进行HA配置同步。默认情况
下，NET地址为非本地配置。
使用no net net命令取消对NET地址的设置。
配置管理距离
指定IS-IS路由的管理距离，在IS-IS路由配置模式下，使用以下命令：
distance distance-value
l
distance-value – 为IS-IS路由指定管理距离。范围是1到255，默认值是115。
使用no distance命令恢复缺省管理距离。
配置度量类型
当度量类型为narrow时，路由器只生成和接收metric field的类型为narrow类型的报文。接口度量值的取
值范围为0到63。对于大型网络，路由的最大度量值为1023。当路由度量值大于1023时，认为目标不可
达。当度量类型为wide时，路由器仅生成和接收metric field的类型为wide类型的报文。接口度量值的取
值范围为0到16777215。当度量类型为transition时，路由器既可以接收/发送narrow类型的报文，也可
以接收/发送wide类型的报文。配置度量类型，在IS-IS路由配置模式下，使用如下命令：
metric-style {wide | narrow | transition}

<!-- 来源页 565 -->
l
wide – 路由器仅生成和接收metric field的类型为wide类型的报文。
l
narrow – 路由器只生成和接收metric field的类型为narrow类型的报文。默认为narrow。
l
transition – 路由器既可以接收/发送narrow类型的报文，也可以接收/发送wide类型的报文。
使用no metric-style恢复默认度量类型。
配置接口度量值
度量值用来计算经过此链路到达网络目的地址的链路开销。配置接口所在链路的度量值，在接口配置模式
下，使用如下命令：
isis metric value [level-1 | level-2]
l
value – 指定接口所在链路的度量值。取值范围为1到16777214。默认值为10。当接口的度量类型为
narrow时，度量值不能超过63。
l
level-1 | level-2 – 使用level-1参数指定Level-1 路由信息的度量值。使用level-2参数指定Level-2
路由信息的度量值。不指定level-1和level-2参数时，设置的度量值将会同时对Level-1 和Level-2路
由信息生效。
使用no isis metric命令恢复接口度量值的默认值。
引入路由
IS-IS协议允许用户将设备上其它路由协议（直连、静态、OSPF、BGP和RIP）的路由信息引入到IS-IS中，
并向外发布。同时，用户可以设置被引入路由的度量。配置引入路由，在IS-IS路由配置模式下使用以下命
令：
redistribute {connected | static | ospf | bgp | rip} [level-1 | level-1-2 | level-2] [metric value]
[metric-type {external | internal}] [route-map name]
l
connected | static | ospf | bgp | rip – 指定引入路由的类型，可以是直连路由（connected）、静
态路由（static）、OSPF（ospf），BGP（bgp）或者RIP (rip)。
l
level-1 | level-1-2 | level-2 – 指定引入路由的级别，可以作为Level-1路由（level-1）、Level-2
路由（level-2）或者同时作为Level-1和Level-2路由（level-1-2）。默认值为level-2。
l
metric value – 指定引入路由的度量。范围是0到4294967295。默认值为0。当路由器的度量类型为
narrow时，引入路由的度量值不能超过63。
l
metric-type {external | internal} – 当指定metric类型为external时，metric值为使用命令metric
value中配置的值加64；当指定metric类型为internal时，metric值为命令metric value中配置的数
值。默认类型为internal。

<!-- 来源页 566 -->
l
route-map name - 指定用于过滤引入路由信息的路由映射表。有关路由映射表的更多信息，请参阅"
路由映射表" 在第591页。
使用no redistribute {connected | static | ospf | bgp | rip} [level-1 | level-1-2 | level-2]命令取消
指定类型路由的引入。
发布缺省路由
对于引入其他协议的路由信息时所存在的缺省路由，不会被路由器引入并使用。如果需要在路由域中发布缺
省路由，在IS-IS路由配置模式下使用以下命令：
default-information originate
当配置了此命令的路由器的路由表中存在一条缺省路由，IS-IS将只通过Level-2 LSP通告此路由。
使用no default-information originate命令取消发布缺省路由。
IS-IS网络优化
配置Hello报文发送时间间隔
配置接口发送Hello报文的时间间隔，在接口配置模式下，使用如下命令：
isis hello-interval value [level-1 | level-2]
l
value – 接口发送Hello报文的时间间隔。取值范围为1到600。单位为秒。默认值为3秒。
l
level-1 | level-2 – 使用level-1参数指定Level-1 Hello报文的发送时间间隔。使用level-2参数指定
Level-2 Hello报文的发送时间间隔。默认为Level-2 和Level-1Hello报文。
使用no isis hello-interval命令将Hello报文发送时间间隔恢复为默认值。
配置Hello报文失效乘数
在指定抑制时间内，如果路由器没有收到来自邻居的Hello报文，将宣告邻居失效。抑制时间等于Hello报文
失效乘数与Hello报文发送时间间隔的乘积，。配置Hello报文失效乘数，在接口配置模式下，使用如下命
令：
isis hello-multiplier value [level-1 | level-2]
l
value – 指定Hello报文失效乘数。取值范围为2到100。默认值为10。
l
level-1 | level-2 – 使用level-1参数指定Level-1 Hello报文的失效乘数。使用level-2参数指定
Level-2 Hello报文的失效乘数。默认为Level-1和Level-2 Hello报文。
使用no isis hello-multiplier命令恢复报文失效乘数的默认值。

<!-- 来源页 567 -->
配置Hello报文填充功能
使用Hello报文填充功能将Hello报文填充到接口MTU大小。配置Hello报文填充功能，在接口配置模式下，
使用如下命令：
isis hello padding
使用no isis hello padding命令取消Hello报文填充功能。
配置DIS选举优先级
在广播类型网络中，通过指定接口的DIS(Designated IS)优先级，影响DIS选举结果。在DIS选举中，接口
的DIS优先级高的IS被选举为DIS。当DIS优先级相同时，则MAC地址最大的接口所属的IS被选举为DIS。配
置接口的DIS选举优先级，在接口配置模式下，使用如下命令：
isis priority value [level-1 | level-2]
l
value – 指定DIS选举优先级。取值范围为0到127。默认值为64。
l
level-1 | level-2 – 使用level-1参数指定Level-1接口的DIS选举优先级。使用level-2参数指定
Level-2 接口的DIS选举优先级。默认为Level-1和Level-2接口设置相同的DIS选举优先级。
使用no isis priority [level-1 | level-2]命令恢复指定级别接口的DIS选举优先级。
配置被动接口
如果把接口配置为被动接口，则此被动接口不向外发送和接受IS-IS报文，并且此接口不与相邻路由器建立邻
居关系。但仍然可以把该接口直连网络的路由信息放在LSP中从其他接口宣告出去。配置被动接口，在接口
配置模式下，使用如下命令：
isis passive
使用no isis passive命令取消被动接口设置。
配置LSP生成时间间隔
为了防止网络拓扑频繁变化而导致LSP频繁重新生成，用户可配置LSP生成时间间隔，以抑制网络变化频繁
导致占用过多的带宽资源和路由器资源。配置LSP生成时间间隔，在IS-IS路由配置模式下，使用如下命令：
lsp-gen-interval value [level-1 | level-2]
l
value – 指定LSP生成时间间隔。取值范围为1到120。默认值为30。单位为秒。
l
level-1 | level-2 – 选择level-1仅为Level-1 LSPs指定生成时间间隔；选择level-2仅为level-2
LSPs指定生成时间间隔。不指定参数时，配置的生成时间间隔适用于Level-1 LSP和Level-2 LSP。
使用no lsp-gen-interval命令恢复默认值。

<!-- 来源页 568 -->
配置LSP最大生存时间
为LSP配置最大生存时间。当LSP的最大生存时间递减为0时，IS-IS协议将在LSDB中把此LSP继续保持60
秒。若还未收到此LSP的更新，则删除此LSP。配置LSP最大生存时间，在IS-IS路由配置模式下，使用如下
命令：
max-lsp-lifetime value
l
value – 指定LSP的最大生存时间。取值范围为350到65535。默认值为1200。单位为秒。
使用no max-lsp-lifetime命令恢复默认值。
配置LSP刷新时间
每一个LSP都有一个最大生存时间，因此每个路由器必须定时刷新自己生成的LSP，以防止LSP的最大生存时
间减小至0。用户可对LSP的刷新周期进行配置。配置LSP刷新时间，在IS-IS路由配置模式下，使用如下命
令：
lsp-refresh-interval value
l
value – 指定LSP的刷新时间。取值范围为1到65535。默认值为900。单位为秒。需要确保刷新时间比
LSP最大生存时间少300秒以上，使刷新后的LSP可以在原LSP过期前到达区域内的设备。
使用no lsp-refresh-interval命令恢复默认值。
配置SPF计算时间间隔
当LSDB发生变化时需要进行路由计算。计算SPF的时间间隔可以由用户根据需要进行配置。配置SPF计算时
间间隔，在IS-IS路由配置模式下，使用如下命令：
spf-interval value [level-1 | level-2]
l
value – 指定计算SPF的时间间隔。取值范围为1到120。默认值为10。单位为秒。
l
level-1 | level-2 – 选择level-1仅为Level-1 SPF指定计算时间间隔；选择level-2仅为level-2 SPF
指定计算时间间隔。不指定参数时，配置的计算时间间隔适用于Level-1 SPF和Level-2 SPF的计算。
使用no spf-interval命令恢复默认值。
配置过载标志位
当路由器因资源不足而导致LSDB不完整或不准确时，会在通告的LSPs中设置过载标志位。其它路由器在收
到此类型LSPs后，就不会再利用这台路由器转发需要经过它传送的数据，但到此路由器直连地址的报文仍然
可以被转发给此路由器。为路由器手工配制过载标志位，在IS-IS路由配置模式下，使用如下命令：
set-overload-bit
使用no set-overload-bit命令取消配置过载标志位。

<!-- 来源页 569 -->
配置主机名映射
在IS-IS路由域中，System ID作为NET地址的一部分，用来在区域内唯一标识主机或路由器。主机名映射可
以将System ID映射到主机名。IS-IS的路由器维护一个主机名到System ID的映射关系表。配置主机名映
射，在IS-IS路由配置模式下，使用如下命令：
hostname dynamic
使用no hostname dynamic取消主机名映射配置。
IS-IS网络安全性
配置认证
对路由器之间所发送的LSP报文，CSNP报文，PSNP报文进行认证配置。认证配置只影响路由信息的学习，
不影响邻居的建立。认证证方式有两种，分别是明文认证和MD5密文认证。明文认证不能提供安全保障。未
加密的认证字随报文一同传送。默认为明文认证。配置验证方式，在IS-IS路由配置模式下，使用如下命令：
authentication {md5 | text} [level-1 | level-2]
l
md5 | text – 使用MD5认证方式（md5）或明文认证（text）。
l
level-1 | level-2 – 使用level-1参数为Level-1路由器之间的报文指定认证方式。使用level-2参数为
Level-2路由器之间的报文指定认证方式。通过配置Level-1路由器之间的认证，可以防止将从不可信任
的路由器学习到的路由信息加入到Level-1的LSDB中。同一区域内的Level-1路由器必须配置相同的认
证方式和认证密码。通过配置Level-2路由器间的认证，可以防止将不可信的路由信息注入Level-2路由
器。同一路由域中所有Level-2路由器必须配置相同的认证方式和认证密码。
取消认证配置，在IS-IS路由配置模式下，使用no authentication mode。
指定认证方式后，需要继续指定认证所使用的秘钥。为Level-1路由器之间报文的认证方式指定秘钥，使用
如下命令：
area-password word
l
word – 指定认证所使用的秘钥。秘钥的最大长度为32字符。
删除指定的密钥，使用no area-password命令。
为Level-2路由器之间报文的认证方式指定秘钥，使用如下命令：
domain-password word
l
word – 指定认证所使用的秘钥。秘钥的最大长度为32字符。
删除指定的密钥，使用no domain-password命令。

<!-- 来源页 570 -->
配置接口认证模式
接口认证用来确认邻居的合法性，防止与无法信任的路由器形成邻居。配置接口认证后，认证密码将会封装
到Hello报文中。通过检查才会形成邻居关系，否则将不会形成邻居关系。两台路由器要形成邻居关系必须
配置相同的认证模式和认证密码。配置接口认证模式，在接口配置模式下，使用如下命令：
isis authentication {md5 | text} [level-1 | level-2]
l
md5 | text – 使用MD5认证方式（md5）或明文认证（text）。
l
level-1 | level-2 – 使用level-1参数为Level-1路由器之间的Hello报文指定认证方式。使用level-2
参数为Level-2路由器之间的Hello报文指定认证方式。
使用no isis authentication命令取消接口认证。
配置接口认证模式后，需要继续指定认证所使用的秘钥。在接口配置模式下，使用如下命令：
isis password word [level-1 | level-2]
l
word – 指定认证所使用的秘钥。秘钥的最大长度为32字符。
l
level-1 | level-2 – 使用level-1参数为Level-1路由器之间的Hello报文认证指定密码。使用level-2
参数为Level-2路由器之间的Hello报文认证指定密码。
使用no isis password命令取消指定的密钥。
查看IS-IS信息
显示IS-IS进程信息及相关配置，在任何模式下使用以下命令：
show isis [vrouter vrouter-name]
l
vrouter-name - 显示指定的VRouter的IS-IS进程信息及相关配置。
显示IS-IS链路状态数据库，任何模式下使用以下命令：
show isis database [detail] [vrouter vrouter-name]
l
detail – 显示链路状态数据库的详细信息。
l
vrouter-name - 显示指定的VRouter的链路状态数据库信息。
显示IS-IS接口信息，在任何模式下使用以下命令：
show isis interface [interface-name]
显示IS-IS邻居信息，在任何模式下使用以下命令：
show isis neighbor [detail] [vrouter vrouter-name]
显示动态主机名配置，在任何模式下使用以下命令：

<!-- 来源页 571 -->
show isis hostname [vrouter vrouter-name]
显示IS-IS路由信息，在任何模式下使用以下命令：
show isis route [A.B.C.D/M] [vrouter vrouter-name]
显示路由引入信息，在任何模式下使用以下命令：
show isis route redistribute [level-1 | level-2] [A.B.C.D/M] [vrouter vrouter-name]
例：在GRE over IPsec场景下应用IS-IS实现总部与分支通信
当企业需通过GRE over IPsec VPN实现总部与分支的跨网络连接，并依赖IS-IS路由协议完成内网路由交互
时，防火墙支持以下能力以满足需求：
l 在GRE over IPsec隧道接口上启用IS-IS协议，使隧道两端设备可基于隧道建立IS-IS邻居关系，实现路由信息动态
交互；
l 在IS-IS路由重发布时引用route-map，通过匹配路由前缀、标签等条件筛选路由，并为路由设置标签，实现精
细化路由管理。
型号说明：
l
支持：SG-6000-A系列
l
支持：SG-6000-K系列（除SG-6000-K20803、K9180平台）
l
支持：云·界
典型配置案例
某企业需实现总部与分支网络的互联互通，在总部与分支出口分别部署防火墙（总部防火墙为Device A，分
支防火墙为Device B）。通过在两台防火墙之间建立GRE over IPsec隧道，并在该隧道环境中启用IS-IS路
由协议，以实现总部与分支内网路由信息的动态交互，保障数据的高效传输。
提示: 该例以提供配置思路与关键步骤为主，仅完成路由交互，未做路由生效后的业务配置说明。
真实组网环境的业务配置，请根据设备型号、软件版本及网络规划进行调整。
前提条件：已完成GRE over IPsec隧道配置，隧道接口状态正常；总部与分支设备的隧道接口已配置同网段
IP地址，确保可正常连通。
步骤1：进入隧道接口配置模式并启用IS-IS，两端设备通过隧道交互IS-IS邻居信息。
Device A

<!-- 来源页 572 -->
hostname(config)# interface tunnel1 // 进入隧道接口配置模式，tunnel1为已创建的GRE隧道接口
hostname(config-interface)# zone "trust"
hostname(config-interface)# ip address 22.1.1.1 255.255.255.0
hostname(config-interface)# manage ping
hostname(config-interface)# tunnel gre "gre1" gw 202.97.xx.xx // gw需填写Device B的实际公网IP
hostname(config-interface)# isis enable // 在隧道接口上启用IS-IS协议
hostname(config-interface)# exit
Device B
hostname(config)# interface tunnel1
hostname(config-interface)# zone "trust"
hostname(config-interface)# ip address 22.1.1.2 255.255.255.0
hostname(config-interface)# manage ping
hostname(config-interface)# tunnel gre "gre1" gw 202.97.xx.yy // gw需填写Device A的实际公网IP
hostname(config-interface)# isis enable
hostname(config-interface)# exit
步骤2：进入IS-IS路由配置模式，配置网络实体标识（NET），用于标识设备在IS-IS协议中的唯一地址。
分支设备需与总部设备配置相同的IS-IS区域地址，才能与总部设备建立邻居关系。再设置IS-IS度量模式为
宽度量，IS-IS的路由标签功能仅在宽度量模式下支持，窄度量模式不支持扩展TLV携带标签信息。
Device A
hostname(config)# ip vrouter trust
hostname(config-vrouter)# router isis
hostname(config-router)# net 49.0001.0000.0000.0001.00
hostname(config-router)# metric-style wide
hostname(config-router)# exit
Device B
hostname(config)# ip vrouter trust
hostname(config-vrouter)# router isis
hostname(config-router)# net 49.0001.0000.0000.0002.00
hostname(config-router)# metric-style wide
hostname(config-router)# exit
步骤3：配置ACL筛选需重发布的路由前缀。
ACL（访问控制列表）用于匹配需要重发布到IS-IS的路由前缀，避免无关路由进入。配置后，仅允许
111.1.1.0/24、112.1.0.0/20、113.1.1.0/24网段的路由通过，112.1.1.0/24被拒绝。
提示: 本例后续配置均围绕“总部Device A向分支Device B发布内网路由” ，若需分支Device
B向总部发布路由实现双向互通，可参考相同思路。

<!-- 来源页 573 -->
Device A
hostname(config)# access-list route "1" // 创建名为“1”的路由ACL
hostname(config)# access-list route "1" permit 111.1.1.0/24 // 允许111.1.1.0/24网段路由
hostname(config)# access-list route "1" deny 112.1.1.0/24 // 拒绝112.1.1.0/24网段路由
hostname(config)# access-list route "1" permit 112.1.0.0/20 // 允许112.1.0.0/20网段路由（包含
112.1.1.0/24）
hostname(config)# access-list route "1" permit 113.1.1.0/24 // 允许113.1.1.0/24网段路由
hostname(config)# exit
步骤4：配置route-map引用ACL，并配置match tag、set tag等参数，实现路由匹配与标签设置。
配置后，携带标签20且匹配ACL“1” 的路由，将被标记为8888；携带标签10且匹配ACL“1” 的路由，
将被标记为9999；其他匹配ACL“1”但未携带标签10、20 的路由，标记为9238493；未匹配ACL“1”
的路由，标记为9238493。
Device A
hostname(config)# route-map "rmp" permit 1 // 创建名为“rmp”的route-map，路由映射表下路由匹配规
则的序列号为1
hostname(config-route-map)# match tag 20 // 匹配携带标签20的路由
hostname(config-route-mapg)# match ip address "1" //匹配ACL“1”的路由
hostname(config-route-map)# set tag 8888 // 为匹配的路由设置新标签8888
hostname(config-route-map)# exit
hostname(config)# route-map "rmp" permit 65534
hostname(config-route-map)# match tag 10
hostname(config-route-mapg)# match ip address "1"
hostname(config-route-map)# set tag 9999
hostname(config-route-map)# exit
hostname(config)# route-map "rmp" permit 65535
hostname(config-route-map)# set tag 9238493
hostname(config-route-map)# exit
步骤5：配置总部设备的静态路由并关联标签。配置后，系统生成多条静态路由，其中部分路由携带标签
（如112.1.1.0/24携带标签10、113.1.1.0/24 携带标签20）。这些标签将作为后续route-map识别不
同路由、进行针对性筛选与标签设置操作的标识。
Device A
hostname(config)# ip route 111.1.1.0/24 1.1.1.2
hostname(config)# ip route 112.1.1.0/24 1.1.1.2 tag 10
hostname(config)# ip route 113.1.1.0/24 1.1.1.2 tag 20
hostname(config)# ip route 114.1.1.0/24 1.1.1.2 tag 123
hostname(config)# ip route 115.1.1.0/24 1.1.1.2 tag 321
hostname(config)# exit
步骤6：配置IS-IS重发布静态路由并引用route-map。
配置后，总部Device A设备的静态路由被引入到IS-IS域。同时，只有符合route-map“rmp” 筛选条件

<!-- 来源页 574 -->
的静态路由被重发布，且按规则为筛选后的路由设置标签。筛选并设好标签的路由进入IS-IS路由表，经GRE
over IPsec隧道发送至分支机构Device B设备，完成总部到分支的路由交互。
Device A
hostname(config)# router isis
hostname(config-router)# redistribute static route-map "rmp" // 重发布静态路由时应用routemap“rmp”
hostname(config-router)# exit
步骤7：验证结果。在Device B上执行show命令后，可查看同步自Device A的总部路由，这些路由已按
Device A中route-map的规则完成标签设置，验证总部到分支的路由交互已正常生效。
Device B
hostname# show ip route isis //查看IS-IS路由
Routing Table for Virtual Router <trust-vr>
=================================================
I>* 111.1.1.0/24 [115/10/1] via 22.1.1.1, tunnel1, 00:05:08 tag 9238493
I>* 112.1.1.0/24 [115/10/1] via 22.1.1.1, tunnel1, 00:05:08 tag 9238493
I>* 113.1.1.0/24 [115/10/1] via 22.1.1.1, tunnel1, 00:05:08 tag 8888
I>* 114.1.1.0/24 [115/10/1] via 22.1.1.1, tunnel1, 00:05:08 tag 9238493
I>* 115.1.1.0/24 [115/10/1] via 22.1.1.1, tunnel1, 00:05:08 tag 9238493
BGP
BGP是边界网关协议（Border Gateway Protocol）的缩写。自治系统（Autonomous System）是处于
一个管理机构控制之下的路由器和网络群组。BGP是在自治系统之间或在一个自治系统之内动态交换路由信
息的路由协议，在同一自治系统间运行BGP路由协议形成的邻居关系，称为IBGP（Internal Border
Gateway Protocol）邻居关系；在不同自治系统间运行BGP路由协议形成的邻居关系，称为EBGP
（External Border Gateway Protocol）邻居关系。BGP使用TCP传输协议，端口号为179，并且支持无
类别域间选路（CIDR）。
BGP特点
BGP具有以下特点：
l 首次建立TCP连接后，BGP邻居之间交换整个BGP路由表，之后仅交换更新路由信息。
l 周期性发送KEEPALIVE报文校验TCP的连通性。
l BGP路由器仅选择最优路径发布到BGP邻居。
l BGP是一种距离矢量的路由协议，从设计上避免了环路的发生。

<!-- 来源页 575 -->
发送BGP消息的路由器称为BGP发言人，它接收或产生新的路由信息，并发布给其它BGP发言人。当BGP发
言人收到来自其它自治系统的新路由时，如果该路由比当前已知路由更优、或者当前还没有该路由，它就把
这条路由发布给所有其它BGP发言人。相互交换消息的BGP发言人之间互称对等体（peer），多个相关的对
等体可以构成对等体组（peer group）。对等体组的作用是简化配置，不影响实际的对等体关系的建立与
路由的传递。
BGP报文类型
BGP有4种类型的报文，分别为OPEN、UPDATE、NOTIFICATION和KEEPALIVE。BGP对等体间通过发送
OPEN报文来交换各自的版本、自治系统号、保持时间、BGP标识符等信息，进行协商。OPEN报文主要用于
建立邻居（BGP对等体）关系，它是BGP路由器之间的初始握手消息，应该发生在任何通告消息之前。对等
体在收到OPEN消息之后，即以KEEPALIVE消息作为响应。一旦握手成功，则这些BGP邻居就可以进行
UPDATE（更新）、KEEPALIVE（保持激活）以及NOTIFICATION（通知）等消息的交换操作。UPDATE报
文携带的是路由更新信息，其中包括撤销路由信息和可达路由信息及其路径属性。当BGP检测到差错（连接
中断、协商出错、报文差错等）时，发送NOTIFICATION 报文，关闭同对等体的连接。KEEPALIVE报文在
BGP对等体间周期性发送，以确保连接有效。
BGP GR
GR（Graceful Restart）即平滑重启，也被称作NSF（Non-Stop Forwarding）。
BGP GR技术可以保证设备在主备切换或者设备重启时转发层面能够继续数据的转发，且控制层面邻居关系
的重建及路由计算不会影响转发层面的功能，从而减少单点故障以及主备切换时路由震荡对网络的影响，提
升整网的可靠性，避免流量中断对用户重要业务的影响。
BGP GR基础概念：
l End-of-RIB标记：End-of-RIB标记实际上是一个特殊的BGP Update message。它没有可达的NLRI（网络可达
层信息，Network Layer Reachability Information），同时撤回NLRI也为空。其主要作用是当前设备从对等体
收到End-of-RIB 标记之后，表明该对等体所有需要通告的更新已经发送完毕。
l Graceful Restart Capability：为支持GR功能，BGP协议新增了一个BGP Capability，即Graceful Restart
Capability。它在BGP连接建立时，随着Open message进行发布。它可以声明当前设备在BGP重启时依然能够
维持转发能力，还可以声明当前设备在初始的update发送完毕后能产生End-of-RIB 标记。
l GR Restarter：指发生主备切换或者BGP协议重启时，以GR方式重启的设备。
l GR Helper：GR Restarter的邻居，具有GR能力，协助GR Restarter进行GR的设备。
一台设备既可以作为GR Restarter，也可以作为GR Helper，其角色确定由该设备在BGP GR过程中的实际
作用决定。
以设备HA为例，BGP GR的工作过程如下：

<!-- 来源页 576 -->
1. 在HA切换后，新主设备作为GR Restarter与GR Helper重新建立BGP连接。
2. GR Helper断开与旧主设备的BGP邻居，将从旧主设备学习的BGP路由标记为stale状态（失效路由），但仍按照
这些路由转发数据报文，并启动对等体陈旧路由保持时间（通过graceful-restart stale-path-time time配
置）。
3. GR Restarter如果在通告的GR等待重建时间（通过graceful-restart restart-path-time time配置）内与GR
Helper成功建立BGP会话，则二者建立BGP邻居关系并进行路由信息交互。如果在通告的GR等待重建时间内未
与GR Helper建立BGP邻居关系，GR Helper将立即删除与GR Restarter相关的路由。
4. GR Helper与GR Restarter建立邻居关系后，发送本地更新，并在更新完成后通告End-of-RIB标记，表示更新发
送完毕。即便GR Helper本地没有需要通告的更新，也必须发送End-of-RIB标记。
5. GR Restarter在收到所有对等体发送的End-of-RIB标记后开始选择最佳路径。如果一直没收到必须的全部Endof-RIB标记，GR Restarter会在所配置的GR等待End-of-Rib标记时间（通过graceful-restart wait-for-ribtime time配置）结束后开始选择最佳路径。
6. 最佳路径选择完毕后，GR Restarter更新RIB路由表，产生BGP路由更新并发送给BGP邻居，无论是否有更新，
都需通告End-of-RIB标记。
7. GR Helper收到路由更新后，将相关路由的stale标记移除；在收到GR Restarter发送的End-of-RIB标记后，移除
仍有stale标记的路由。
8. 如果在对等体陈旧路由保持时间内一直未完成路由信息的交互，则GR Restarter会强制退出GR过程，根据已经学
习到的BGP路由信息更新RIB表项，删除老化的RIB表项。
注意:
l
BGP GR功能不支持HA Peer模式。
l
以下场景中的设备可以作为GR Restarter，除以下场景外其它场景中的设备只支持作为GR
Helper：
l
进行设备HA切换的新主设备;
l
进行双主控（SCM）HA切换的设备（X系列所有型号、K系列K20803/K9180）。
l
如果主备设备间的HA连接断开，则BGP GR功能不生效。
配置BGP协议
用户可以为不同的VRouter分别配置BGP协议。BGP协议配置包括以下各项：

<!-- 来源页 577 -->
l 进入BGP配置模式
l 指定Router ID
l 创建聚合路由
l 添加静态BGP路由
l 配置定时器
l 指定BGP路由管理距离
l 指定缺省度量
l 创建BGP对等体组
l 添加BGP对等体到对等体组
l 配置BGP对等体
l 配置BGP MD5认证
l 激活BGP连接
l 配置缺省信息发布
l 配置描述信息
l 配置BGP对等体定时器
l 配置下一跳为自身
l 配置EBGP多跳
l 关闭对等体或者对等体组
l 重置BGP连接
l 引入路由
l 配置基于AS路径访问控制列表的路由过滤
l 配置向对等体或者对等体组发送团体属性
l 配置基于路由映射表的路由过滤
l 等价负载均衡
l 开启/关闭EBGP的multipath-relax功能
l 配置BGP GR
l 查看BGP信息

<!-- 来源页 578 -->
进入BGP配置模式
对BGP协议的配置需要在BGP路由模式下进行。进入BGP路由模式，在VRouter配置模式下，使用以下命
令：
ip vrouter vrouter-name （从全局模式进入VRouter配置模式）
router bgp number
l
number – 指定自治系统的编号。范围是1到4294967295。
运行该命令后，系统的BGP路由功能被开启，为指定的自治系统创建BGP实例，并且进入BGP实例配置模
式。
在VRouter配置模式下，使用no router bgp number删除BGP实例。
指定Router ID
每一台运行BGP协议的路由器都必须拥有一个Router ID。Router ID是每个路由器在整个BGP域中的唯一
标识，使用IP地址的形式表示。如果不指定Router ID，系统会将设备上回环接口的最大IP地址设置为
Router ID，如果没有回环接口或者回环接口未配置IP地址，则选择其他接口的最大IP作为Router ID。指定
Router ID，在BGP实例配置模式下，使用以下命令：
router-id A.B.C.D
l
A.B.C.D – 指定BGP协议使用的Router ID，为IP地址形式。
在BGP实例配置模式下，使用该命令no的形式取消Router ID的指定：
no router-id
创建聚合路由
用户可以将BGP路由表内的路由条目进行聚合。创建聚合路由，在BGP实例配置模式下，使用以下命令：
aggregate-address {A.B.C.D/M | A.B.C.D A.B.C.D} [as-set] [summary-only]
l
A.B.C.D/M | A.B.C.D A.B.C.D – 指定聚合网络地址。Hillstone设备支持两种方式，A.B.C.D/M或者
A.B.C.D A.B.C.D，例如1.1.1.0/24或者1.1.1.0 255.255.255.0。
l
as-set – 如果指定该参数，系统会将被聚合路由的路径信息作为自己的路径信息发布给其它路由器。
l
summary-only – 如果指定该参数，系统将只发布聚合路由。
在BGP实例配置模式下，使用该命令no的形式取消聚合路由的指定：
no aggregate-address {A.B.C.D/M | A.B.C.D A.B.C.D}
添加静态BGP路由
向BGP路由表中添加静态BGP路由条目，在BGP实例配置模式下，使用以下命令：

<!-- 来源页 579 -->
network {A.B.C.D/M | A.B.C.D A.B.C.D}
l
A.B.C.D/M | A.B.C.D A.B.C.D – 指定BGP静态路由条目信息。设备支持两种方式，A.B.C.D/M或者
A.B.C.D A.B.C.D，例如1.1.1.0/24或者1.1.1.0 255.255.255.0。
在BGP实例配置模式下使用该命令no的形式删除指定的静态路由条目：
no network {A.B.C.D/M | A.B.C.D A.B.C.D}
配置定时器
用户可以配置两个BGP定时器，分别是KEEPALIVE（保持激活）和HOLDDOWN（保持时间），描述如下：
l
KEEPALIVE（保持激活）：StoneOS向BGP对等体发送保持激活信息的频率。默认为每隔60秒发送一
次。
l
HOLDDOWN（保持时间）：如果本地路由器在保持时间结束后仍没有收到某对等体的保持激活信息，
则判断为该对等体老化。默认为180秒。
配置定时器，在BGP实例配置模式下，使用以下命令：
timers keepalive holddown
l
keepalive – 指定发送保持激活信息的频率，单位为秒。默认是60秒。取值范围是0到65535，且小于
或者等于HOLDDOWN/3的值，如果大于HOLDDOWN/3，实际生效的时间将为HOLDDOWN/3。参数
值为0表示不发送KEEPALIVE信息。
l
holddown – 指定保持时间，单位为秒。默认是180秒。取值范围是0或者3到65535。参数值为0表示
不检查保持时间。
在BGP实例配置模式下使用该命令no的形式恢复定时器的默认值：
no timers
指定BGP路由管理距离
用户可以为从其它对等体获得的BGP路由以及本地BGP路由指定管理距离。指定BGP路由管理距离，在BGP
实例配置模式下，使用以下命令：
distance ebgp-distance ibgp-distance local-distance
l
ebgp-distance – 指定EBGP路由管理距离。默认值为20。取值范围是1到255的整数。
l
ibgp-distance – 指定IBGP路由管理距离。默认值为200。取值范围是1到255的整数。
l
local-distance – 指定本地路由管理距离。默认值为200。取值范围是1到255的整数。
在BGP实例配置模式下使用该命令no的形式恢复默认BGP路由管理距离：

<!-- 来源页 580 -->
no distance
指定缺省度量
默认情况下，引入的IGP路由的度量保持不变，引入的直连路由的度量为0。用户可以为引入路由指定缺省度
量。指定引入路由的缺省度量，在BGP实例配置模式下，使用以下命令：
default-metric value
l
value – 指定缺省度量值。范围是1到4294967295。
在BGP实例配置模式下使用该命令no的形式恢复默认情况：
no default-metric
创建BGP对等体组
使用BGP对等体组，可以简化配置，也可以使信息更新更为有效。创建BGP对等体组，在BGP实例配置模式
下，使用以下命令：
neighbor peer-group-name peer-group
l
peer-group-name – 指定将要创建的对等体组的名称。
在BGP实例配置模式下使用该命令no的形式删除已创建的BGP对等体组：
no neighbor peer-group-name peer-group
添加BGP对等体到对等体组
添加BGP对等体到对等体组，在BGP实例配置模式下，使用以下命令：
neighbor A.B.C.D peer-group peer-group-name
l
A.B.C.D – 指定将要添加的BGP对等体的IP地址。
l
peer-group-name – 指定系统中已创建的对等体组的名称。
在BGP实例配置模式下使用该命令no的形式将BGP对等体从对等体组中删除：
no neighbor A.B.C.D peer-group peer-group-name
配置BGP对等体
用户需要为当前设备指定BGP对等体（对等体组），交换BGP路由信息。配置BGP对等体（对等体组），在
BGP实例配置模式下，使用以下命令：
neighbor {A.B.C.D | peer-group} remote-as number

<!-- 来源页 581 -->
l
A.B.C.D | peer-group – 指定对等体IP地址或者对等体组的名称。
l
number – 指定所配置对等体或者对等体组所在的自治区域的编号。
在BGP实例配置模式下使用该命令no的形式取消BGP对等体或者对等体组的指定：
no neighbor {A.B.C.D | peer-group} remote-as
配置BGP MD5认证
为提高BGP的安全性，用户可以配置BGP对等体或者对等体组在建立TCP连接时进行MD5认证，认证通过后
才可以建立TCP连接。配置BGP MD5认证，在BGP实例配置模式下，使用以下命令：
neighbor {A.B.C.D | peer-group} password password
l
A.B.C.D | peer-group – 指定对等体IP地址或者对等体组的名称。
l
password password – 指定MD5密码串，范围是1到32个字符。
在BGP实例配置模式下使用该命令no的形式取消BGP MD5认证的配置：
no neighbor {A.B.C.D | peer-group} password
注意: 参与MD5认证的对等体或者对等体组的密码必须一样。
激活BGP连接
默认情况下，已配置的BGP对等体或者对等体组与当前设备的BGP连接是激活的。用户可以关闭连接也可以
重新激活BGP连接。激活BGP连接，在BGP实例配置模式下，使用以下命令：
neighbor {A.B.C.D | peer-group} activate
l
A.B.C.D | peer-group – 指定对等体IP地址或者对等体组的名称。
在BGP实例配置模式下使用该命令no的形式关闭指定对等体或者对等体组的BGP连接：
no neighbor {A.B.C.D | peer-group} activate
配置缺省信息发布
用户可以指定当前设备是否将默认路由发布到其它BGP对等体或者对等体组。默认情况下，不发送默认路
由。
配置缺省信息发布到BGP对等体或者对等体组，在BGP实例配置模式下，使用以下命令：
default-information originate
如果路由表中没有默认路由，系统将不会发布默认路由。
在BGP实例配置模式下，使用该命令no的形式取消缺省信息发布：

<!-- 来源页 582 -->
no default-information originate
配置缺省信息发布到BGP对等体或者对等体组，在BGP实例配置模式下，使用以下命令：
neighbor {A.B.C.D | peer-group} default-originate
l
A.B.C.D | peer-group – 指定对等体IP地址或者对等体组的名称。
如果路由表中没有默认路由，系统将会构造一条默认路由发布到BGP对等体或者对等体组。
在BGP实例配置模式下使用该命令no的形式取消缺省信息发布：
no neighbor {A.B.C.D | peer-group} default-originate
配置描述信息
为对等体或者对等体组配置描述信息，在BGP实例配置模式下，使用以下命令：
neighbor {A.B.C.D | peer-group} description description
l
A.B.C.D | peer-group – 指定对等体IP地址或者对等体组的名称。
l
description – 指定描述信息。范围是1到80个字符。
在BGP实例配置模式下使用该命令no的形式取消对等体或者对等体组的描述信息：
no neighbor {A.B.C.D | peer-group} description
配置BGP对等体定时器
默认情况下，在整个BGP系统中，BGP对等体或对等体组之间的定时器按照timer keepalive holddown设
置的值生效，用户可以为某个特定的BGP对等体或者对等体组指定不同的定时器数值，该数值优先级高于
timer keepalive holddown设置的值。为BGP对等体或者对等体组指定定时器数值，在BGP实例配置模式
下，使用以下命令：
neighbor {A.B.C.D | peer-group} timers keepalive holddown
l
A.B.C.D | peer-group – 指定对等体IP地址或者对等体组的名称。
l
keepalive – 指定发送保持激活信息的频率，单位为秒。默认是60秒。取值范围是0到65535，且小于
或者等于HOLDDOWN/3的值，如果大于HOLDDOWN/3，实际生效的时间将为HOLDDOWN/3。参数
值为0表示不发送KEEPALIVE信息。
l
holddown – 指定保持时间，单位为秒。默认是180秒。取值范围是0或者3到65535。参数值为0表示
不检查保持时间。
在BGP实例配置模式下使用该命令no的形式取消对BGP对等体或对等体组定时器的指定：
no neighbor {A.B.C.D | peer-group} timers

<!-- 来源页 583 -->
配置下一跳为自身
配置该功能后，路由器将通告对等体或者对等体组BGP路由的下一跳为该路由器自身。配置下一跳路由为自
身，在BGP实例配置模式下，使用以下命令：
neighbor {A.B.C.D | peer-group} next-hop-self
l
A.B.C.D | peer-group - 指定对等体IP地址或者对等体组的名称。
在BGP实例配置模式下使用该命令no的形式取消下一跳为自身的指定：
no neighbor {A.B.C.D | peer-group} next-hop-self
配置EBGP多跳
对于运行在自治系统之间的BGP（即EBGP），如果BGP对等体或对等体组没有直接连接，用户需要配置
EBGP多跳才能在设备之间创建邻居关系。配置EBGP多跳，在BGP实例配置模式下，使用以下命令：
neighbor {A.B.C.D | peer-group} ebgp-multihop [ttl]
l
A.B.C.D | peer-group - 指定对等体IP地址或者对等体组的名称。
l
ttl - 指定到对等体IP地址或者对等体组的最大下一跳数。取值范围是1到255，默认值是255。如果在达
到最大下一跳数后仍无法找到指定的对等体或对等体组，系统会认为创建邻居关系失败。
在BGP实例配置模式下使用该命令no的形式取消EBGP多跳：
no neighbor {A.B.C.D | peer-group} ebgp-multihop
关闭对等体或者对等体组
用户可以关闭指定的对等体或者对等体组。关闭对等体或者对等体组后，所有与被关闭对等体或者对等体组
相关的会话都会被中断，所有相关的路由信息也会被删除。关闭对等体或者对等体组，在BGP实例配置模式
下，使用以下命令：
neighbor {A.B.C.D | peer-group} shutdown
l
A.B.C.D | peer-group – 指定对等体IP地址或者对等体组的名称。
在BGP实例配置模式下使用该命令no的形式开启对等体或者对等体组：
no neighbor {A.B.C.D | peer-group} shutdown
重置BGP连接
重置BGP连接，在执行模式下，使用以下命令：
clear ip bgp {* | A.B.C.D | external | peer-group peer-group-name | number} [vrouter
vrouter-name]

<!-- 来源页 584 -->
l
* - 重置当前所有BGP会话连接。
l
A.B.C.D – 重置指定对等体的BGP连接。
l
external – 重置所有EBGP连接。
l
peer-group peer-group-name – 重置指定BGP对等体组的连接。
l
number – 重置指定自治系统中的BGP连接。
l
vrouter vrouter-name – 指定需重置连接所在的VRouter。
引入路由
BGP协议允许用户引入其它路由协议（OSPF、直连、静态、IS-IS和RIP）的路由信息，并向外发布。同时，
用户可以设置被引入路由的度量，还可以引用路由映射表对路由信息进行过滤，仅允许引入或拒绝引入特定
的路由信息。配置引入路由，在BGP实例配置模式下使用以下命令：
redistribute {ospf | isis | connected | static | rip} [metric value] [route-map name]
l
ospf | isis | connected | static | rip – 指定引入路由的类型，可以是OSPF（ospf）、IS-IS
（isis）、直连路由（connected）、静态路由（static）或者RIP（rip）。
l
metric value – 指定引入路由的度量。范围是0到4294967295。如果不指定该数值，系统会使用BGP
的缺省度量（通过default-metric value配置）。
l
route-map name – 指定用于过滤引入路由信息的路由映射表。有关路由映射表的更多信息，请参阅"
路由映射表" 在第591页。
用户可以配置多条该命令引入不同类型的路由。
使用no redistribute {ospf | isis | connected | static | rip}命令取消指定类型路由的引入。
配置团体属性值显示为AA:NN格式
BGP路由团体属性支持显示为AA:NN格式（RFC1997标准的Community格式），通过show命令查看BGP
团体属性时，用户自定义的团体属性值显示为AA:NN格式。配置团体属性值显示为AA:NN格式，在全局配
置模式下，使用以下命令：
ip bgp-community new-format
使用该命令no的形式取消团体属性显示为AA:NN格式：
no ip bgp-community new-format

<!-- 来源页 585 -->
注意: 配置该命令后，通过show configuration命令查看结果时，自定义的团体属性值显示为十
进制格式；通过show route-map、show ip community-list以及show ip bgp [A.B.C.D]命
令查看结果时，自定义的团体属性值显示为AA:NN格式。
配置基于AS路径访问控制列表的路由过滤
BGP协议支持通过AS路径访问控制列表对对等体（对等体组）引入的路由或者向外发布的路由进行过滤。配
置基于AS路径访问控制列表的路由过滤，在BGP实例配置模式下，使用以下命令：
neighbor {A.B.C.D | peer-group} filter-list access-list-number {in | out}
l
A.B.C.D | peer-group – 指定BGP对等体的IP地址或者对等体组的名称。
l
access-list-number – 指定AS路径访问控制列表号。有关AS路径访问控制列表的更多信息，请参阅
"AS路径访问控制列表" 在第599页。
l
in | out – 指定对引入的路由（in）或者向外发布的路由（out）进行过滤。
使用该命令no的形式取消基于AS路径访问控制列表的路由过滤配置：
no neighbor {A.B.C.D | peer-group} filter-list {in |out}
配置向对等体或者对等体组发送团体属性
配置向对等体（对等体组）发送团体属性，在BGP实例配置模式下，使用以下命令：
neighbor {A.B.C.D | peer-group} send-community {standard | extended | both}
l
A.B.C.D | peer-group – 指定BGP对等体的IP地址或者对等体组的名称。
l
standard | extended | both – 指定发送团体属性的类别，可以是标准团体属性（standard），扩展
团体属性（extended），或者标准团体属性和扩展团体属性（both）。
使用该命令no的形式取消发送团体属性配置：
no neighbor {A.B.C.D | peer-group} send-community
配置基于路由映射表的路由过滤
BGP协议支持通过路由映射表对对等体（对等体组）引入的路由或者向外发布的路由进行过滤。配置基于路
由映射表的路由过滤，在BGP实例配置模式下，使用以下命令：
neighbor {A.B.C.D | peer-group} route-map name {in |out}

<!-- 来源页 586 -->
l
A.B.C.D | peer-group – 指定BGP对等体的IP地址或者对等体组的名称。
l
route-map name – 指定指定用于路由过滤的路由映射表。有关路由映射表的更多信息，请参阅"路由
映射表" 在第591页。
l
in | out – 指定对引入的路由（in）或者向外发布的路由（out）进行过滤。
使用该命令no的形式取消基于路由映射表的路由过滤配置：
no neighbor {A.B.C.D | peer-group} route-map name{in |out}
等价负载均衡
配置BGP负载均衡的最大路径数，在BGP实例配置模式下，使用以下命令：
maximum-paths {ebgp | ibgp} maximum-number
l
maximum-number – 指定EBGP/IBGP最大ECMP路径数。配置路径数后，若存在多条等价路径，多条
路径均会被加入到路由表中。这样即可使BGP在多条路径上实现负载均衡。取值范围是1到8，默认值是
1。
在BGP实例配置模式下，使用该命令no的形式取消等价负载均衡：
no maximum-paths {ebgp | ibgp}
注意: 配置该功能前，用户需先开启ECMP功能。如何开启ECMP，请参阅“等价多径路由
(ECMP)”。
开启/关闭EBGP的multipath-relax功能
对于EBGP在通过不同AS路径去往同一个目的网络，系统支持开启EBGP的multipath-relax功能，从而使
EBGP在不同AS路径上实现负载均衡。在BGP实例配置模式下，使用以下命令：
l
开启：bestpath as-path multipath-relax
l
关闭：no bestpath as-path multipath-relax
配置BGP GR
配置BGP GR包含以下内容：
l 启用BGP GR
l 配置GR等待重建时间
l 配置GR陈旧路由保持时间
l 配置GR等待End-of-Rib标记时间

<!-- 来源页 587 -->
启用BGP GR
启用BGP GR功能，在BGP实例配置模式下，使用以下命令：
graceful-restart
在BGP实例配置模式下，使用no graceful-restart命令关闭BGP GR功能。
配置GR等待重建时间
配置对端等待重建BGP会话的最大时间，在BGP实例配置模式下，使用以下命令：
graceful-restart restart-time time
l
time - 指定对端等待重建BGP会话的最大时间。取值范围为1到3600秒。默认值为120秒。
在BGP实例配置模式下，使用no graceful-restart restart-time命令恢复默认值。
配置GR陈旧路由保持时间
配置保持重新启动对等体的陈旧路由的最大时间，在BGP实例配置模式下，使用以下命令：
graceful-restart stale-path-time time
l
time - 指定保持重新启动对等体的陈旧路由的最大时间。取值范围为1到3600秒。默认值为360秒。
在BGP实例配置模式下，使用no graceful-restart stale-path-time命令恢复默认值。
配置GR等待End-of-Rib标记时间
配置GR Restarter等待邻居End-of-RIB标记的最大时间，在BGP实例配置模式下，使用以下命令：
graceful-restart wait-for-rib-time time
l
time - 指定GR Restarter等待邻居End-of-RIB标记的最大时间。取值范围为1到3600秒。默认值为
180秒。
在BGP实例配置模式下，使用no graceful-restart wait-for-rib-time命令恢复默认值。
查看BGP信息
显示BGP路由信息，在任何模式下使用以下命令：
show ip route bgp [vrouter vrouter-name]
l
vrouter-name - 显示指定VRouter的BGP路由信息。
显示整个BGP路由表的路由信息，在任何模式下使用以下命令：

<!-- 来源页 588 -->
show ip bgp [A.B.C.D | A.B.C.D/M] [vrouter vrouter-name]
l
A.B.C.D | A.B.C.D/M – 显示到指定网络的BGP路由信息。
l
vrouter-name - 显示指定VRouter的BGP路由信息。
显示BGP数据库中存储的所有自治系统路径信息，在任何模式下使用以下命令：
show ip bgp paths [vrouter vrouter-name]
l
vrouter-name - 显示指定的VRouter的自治系统路径信息。
显示所有BGP连接的状态参数，包括前缀、路径和属性信息等，在任何模式下使用以下命令：
show ip bgp summary [vrouter vrouter-name]
l
vrouter-name - 显示指定VRouter的BGP连接状态参数。
显示BGP团体属性列表信息，在任何模式下使用以下命令：
show ip community [community-list-name]
l
community-list-name –显示指定名称或者序号的团体属性列表信息。如不输入该参数，则显示所有
团体属性列表信息。
show ip as-path-access-list [access-list-number]
l
access-list-number –显示指定序号的AS路径访问控制列表信息。如不输入该参数，则显示所有AS路
径访问控制列表信息。
显示BGP对等体状态，在任何模式下使用以下命令：
show ip bgp neighbor [A.B.C.D | X:X:X:X::X] [log-info] [vrouter vrouter-name]
l
A.B.C.D | X:X:X:X::X– 指定要显示状态的BGP对等体的IP地址，可以为IPv4地址（A.B.C.D）或者
IPv6地址（X:X:X:X::X）。
l
log-info - 显示BGP对等体日志信息。用户可以通过日志信息中的对等体断开信息，诊断和分析邻居关
系异常的原因。系统最多显示10条最新的日志信息。
l
vrouter-name - 显示指定VRouter的BGP对等体的状态。
以下是一个返回结果示例：
hostname# show ip bgp neighbor 90.1.1.2 log-info
BGP neighbor: 90.1.1.2
Date/Time State Notification Error/SubError

<!-- 来源页 589 -->
2024-12-11 10:51:17 Up
2024-12-11 10:51:05 Down BGP Notification send 4/0
Hold Timer Expired
Keepalive last sent time : 2024-12-11 10:51:03
Keepalive last received time : 2024-12-11 10:50:59
2024-12-11 10:50:51 Up
2024-12-11 10:50:44 Down BGP Notification received 6/4
Cease/Administrative Reset
Keepalive last sent time : 2024-12-11 10:50:44
Keepalive last received time : 2024-12-11 10:50:44
回显参数说明：
l
Date/Time：显示日志条目的具体日期和时间。
l
State Notification：显示BGP对等体的状态，可以为“连接”（Up）或者“断开”（Down）。如
果对等体的状态为断开，则会进一步显示断开的原因。
l
Notification Error/SubError：如果对等体状态为Down，并且是由于收到或发送Notification消息
导致的，系统会显示导致断开的错误码/子错误码。同时，还会显示最近一次发送和接收Keepalive报
文的时间。
示例解释：
对以上返回信息中两条对等体状态为Down的日志解释如下：
l
2024年12月11日10:51:05，BGP对等体断开，原因是发送了一个Notification消息（错误码
4/0），具体原因为Holdtimer超时。最后一次发送Keepalive报文的时间为10:51:03，最后一次接
收Keepalive报文的时间为10:50:59。
2024年12月11日10:50:44，BGP对等体断开，原因是收到了一个Notification消息（错误码
6/4），具体原因为管理重置。最后一次发送和接收Keepalive报文的时间均为10:50:44。
BGP路由反射器
在AS内部，为确保IBGP对等体之间能够正常交换路由信息，传统做法是在这些对等体之间建立全连接关系
（Full-mesh）。然而，随着网络规模的扩大，IBGP对等体的数量急剧增加，建立全连接网络的配置变得十
分复杂，配置完成后对网络资源和设备CPU资源的消耗变大。
为了解决这个问题，系统支持BGP路由反射器功能。BGP路由反射器是一种网络优化机制，它允许在AS内部
将一台或多台设备配置为路由反射器，其他BGP设备作为客户机与路由反射器建立连接。路由反射器作为信

<!-- 来源页 590 -->
息存储和转发中心，负责在客户机之间反射（转发）路由信息，从而避免了在大量IBGP对等体之间建立全连
接关系。
BGP路由反射器基本原理
在AS内部，将一台路由器配置为路由反射器（Route Reflector，简称RR），其他路由器根据需求配置为客
户机（Client）或非客户机（Non-Client）。RR和客户机组成一个集群（Cluster），同一集群内的客户机
只需要与RR之间建立IBGP连接，交换路由信息，不需要与其他客户机建立IBGP连接。这种配置减少了AS内
部的IBGP连接数量。
如下图所示，AS1000内部有6台路由器，将其中一台路由器配置为RR，三台路由器配置为客户机，其余两
台作为非客户机。RR和客户机组成一个集群。这种配置下，仅需要建立6条IBGP连接，与未配置RR时需要建
立15条连接（按照n(n-1)/2计算）相比，连接数量显著减少。注意，非客户机仍然需要与RR及其他非客户
机建立全连接。
路由反射器相关角色如下：
l 路由反射器（Route Reflector，简称RR）：将从IBGP对等体学到的路由反射到其他IBGP对等体的BGP设备。
l 客户机（Client）：与RR形成反射邻居关系的IBGP设备。在AS内部，客户机只需要与RR直连。
l 非客户机（Non-Client）：既不是RR也不是客户机的IBGP设备。在AS内部，非客户机与RR之间以及所有的非客
户机之间仍然需要建立全连接关系。
l 始发者（Originator）：在AS内部始发路由的设备。具有Originator_ID属性，该属性用于防止集群内产生路由
环路。
l 集群（Cluster）：RR和RR客户机组成的集合。具有Cluster_List属性，该属性用于防止集群间产生路由环路。
RR的路由反射规则如下：

<!-- 来源页 591 -->
l 从非客户机学到的路由，发布给此RR的所有客户机。
l 从客户机学到的路由，发布给此RR的所有客户机和非客户机。
l 从EBGP邻居学到的路由，发布给此RR的所有客户机和非客户机。
BGP路由反射器防止路由环路机制
BGP路由反射器通过Originator_ID属性和Cluster_List属性来防止路由环路的发生。
Originator_ID由RR创建，携带AS内部路由始发者的Router ID。Originator_ID属性用于防止集群内产生
路由环路：
l 当RR首次反射一条路由时，它会在该路由中添加Originator_ID属性，从而标识发起该路由的设备。如果RR发现
路由中已经包含了Originator_ID属性，它将不会创建新的Originator_ID属性。
l 当其他BGP对等体接收到这条路由时，它们会将收到的Originator_ID和自身的Router ID进行比较，如果两者相
同，说明这条路由是由自身发起的，因此对等体会忽略这条路由，防止了路由环路的产生。
在AS内部，每个RR使用唯一的Cluster_ID作为标识。Cluster_List属性则用于记录路由在反射过程中经过
的所有RR的Cluster_ID，即路由反射的完整RR路径。Cluster_List属性用于防止集群间产生路由环路：
l 当RR首次反射一条路由时，它会将自身的Cluster_ID添加到Cluster_List中。如果路由中没有Cluster_List，RR会
创建一个。
l 当RR收到一条路由更新时，它会检查该路由的Cluster_List。如果Cluster_List中已经有本地Cluster_ID，说明该
路由已经经过了当前RR，因此RR会丢弃这条路由，避免环路。如果Cluster_List中没有本地Cluster_ID，RR会将
其添加进去，并继续反射该更新路由。
配置路由反射器
配置BGP路由反射器包含以下内容：
l 配置BGP路由反射器客户机
l 配置BGP路由反射器Cluster_ID
l 允许/禁止客户机到客户机的路由反射
注意: 只需要在RR上进行BGP路由反射器的配置，不需要在客户机上进行BGP路由反射器的配置。
配置BGP路由反射器客户机
将IBGP对等体配置为路由反射器的客户机，在BGP实例配置模式下，使用以下命令：

<!-- 来源页 592 -->
neighbor {A.B.C.D | X:X:X:X::X | peer-group} route-reflector-client
l
A.B.C.D | X:X:X:X::X | peer-group - 指定IBGP对等体IPv4地址（A.B.C.D）、IPv6地址
（X:X:X:X::X）或者对等体组的名称（peer-group）。
在BGP实例配置模式下，使用no neighbor {A.B.C.D | X:X:X:X::X | peer-group} route-reflectorclient命令取消路由反射器客户机的配置。
配置BGP路由反射器Cluster_ID
配置路由反射器的Cluster_ID，在BGP实例配置模式下，使用以下命令：
cluster-id {A.B.C.D | number}
l
A.B.C.D | number - 指定路由反射器的Cluster_ID为IPv4地址（A.B.C.D）或者十进制数字
（number）。默认为路由反射器自身的Router ID。
在BGP实例配置模式下，使用no cluster-id 命令取消BGP路由反射器Cluster_ID的配置。
允许/禁止客户机到客户机的路由反射
在某些网络环境中，路由反射器的客户机之间已经建立了IBGP全连接，此时客户机无需再通过RR进行路由
反射，以免占用不必要的带宽资源。这种情况下，用户可以选择禁止客户机之间的路由反射，从而减少路由
更新。默认情况下，系统允许客户机到客户机的路由反射。允许/禁止客户机到客户机的路由反射，在BGP实
例配置模式下，使用以下命令：
l
允许：client-to-client reflection
l
禁止：no client-to-client reflection

<!-- 来源页 593 -->
路由对象
路由对象包括以下各项：
l "路由映射表" 在第591页
l "路由访问控制列表" 在第596页
l "AS路径访问控制列表" 在第599页
l "团体属性列表" 在第599页
路由映射表
OSPF协议、OSPFv3协议、BGP协议、IPv4 IS-IS协议以及IPv6 BGP协议允许用户引入其它路由协议的路
由信息，并向外发布。默认情况下，系统会引入所有的路由信息。用户可以引用路由映射表对引入的路由信
息进行过滤。路由映射表主要由路由匹配规则和匹配成功后所执行操作（允许或拒绝）两部分组成。如果引
入的路由信息命中了任何路由匹配规则，系统就会执行对应的操作，允许或拒绝引入这些路由信息。
注意:
l
如果用户设置的操作是允许，匹配成功后系统仅允许引入匹配的路由信息，拒绝引入所有未匹
配的路由信息。
l
如果用户设置的操作是拒绝，匹配成功后系统会拒绝引入匹配的路由信息，但仍允许引入未匹
配的路由信息。
用户可通过以下步骤配置路由映射表，实现对引入路由信息的过滤：
1. 创建路由映射表并在表中创建路由匹配规则。不同的匹配规则通过序列号区分。序列号越小，匹配优先级越高。
默认情况下，引入的路由信息命中任何路由匹配规则，系统将不再继续匹配后续的规则；如果引入的路由信息没
有命中任何匹配规则，系统将执行拒绝操作。
2. 在路由匹配规则中配置匹配条件。匹配条件可以是引入路由的AS路径、团体属性、下一跳接口、目的地址、下一
跳地址、度量值或者标记值，不同的引入路由协议支持配置的匹配条件不同。一条路由匹配规则中可以包含多个
匹配条件，这些匹配条件之间是与（AND）关系，即引入的路由信息必须满足匹配规则中的所有匹配条件才会认
定为命中了该条规则。
匹配条件
不同的引入路由协议对匹配条件的支持情况
IS-IS
OSPF
OSPFv3
BGP
IPv6 BGP
AS路径
x
x
x
支持
支持
团体属性
x
x
x
支持
支持

<!-- 来源页 594 -->
匹配条件
不同的引入路由协议对匹配条件的支持情况
IS-IS
OSPF
OSPFv3
BGP
IPv6 BGP
下一跳接口
x
支持
支持
x
x
IPv4目的地址
支持
支持
x
支持
x
IPv6目的地址
x
x
支持
x
支持
IPv4下一跳地址
x
支持
x
支持
x
IPv6下一跳地址
x
x
x
x
支持
度量值
x
支持
x
支持
支持
标记值
支持
支持
x
支持
x
说明：“x”表示不支持。
3. 如果匹配条件为路由的目的地址或下一条地址，配置匹配时所引用的路由访问控制列表。有关路由访问控制列表
的更多信息，请参阅"路由访问控制列表" 在第596页。
4. 如有需要，设置系统在命中一条路由匹配规则后继续匹配其他规则。
5. 如有需要，修改引入路由的部分属性后再对外发布。不同的引入路由协议支持修改的路由属性不同。
路由属性
不同的引入路由协议对可以修改的路由属性的支持情况
IS-IS
OSPF
OSPFv3
BGP
IPv6 BGP
AS路径
x
x
x
支持
支持
团体属性列表
x
x
x
支持
支持
团体属性
x
x
x
支持
支持
下一跳接口
x
x
x
x
x
IPv4目的地址
x
x
x
x
x
IPv6目的地址
x
x
x
x
x
IPv4下一跳地址
x
x
x
支持
x
IPv6下一跳地址
x
x
x
x
支持
度量值
x
支持
支持
支持
支持
度量类型
x
支持
支持
x
x
来源属性
x
x
x
支持
支持
标记值
支持
支持
x
x
x
本地优先属性
x
x
x
支持
支持
说明：“x”表示不支持。
配置路由映射表
配置路由映射表包括以下几项：

<!-- 来源页 595 -->
l 创建路由映射表和路由匹配规则
l 配置匹配条件
l 匹配多条路由匹配规则
l 修改引入路由属性
创建路由映射表和路由匹配规则
创建路由映射表并在表中配置路由匹配规则，在全局配置模式下，使用以下命令：
route-map name {deny | permit} sequence
l
route-map name – 指定路由映射表名称，并进入路由映射表配置模式。取值范围是1到31个字符。如
果该名称已经存在，则直接进入路由映射表配置模式。
l
deny | permit – 指定对匹配的路由信息所执行的操作。deny为拒绝，permit为允许。
l
sequence – 指定该路由映射表下路由匹配规则的序列号。取值范围是1到65535。
使用该命令no的形式删除路由映射表：
no route-map name [sequence]
l
sequence – 仅删除路由映射表中指定序列号的匹配规则。
配置匹配条件
配置路由匹配规则中的匹配条件，在路由映射表配置模式下，使用以下命令：
match {as-path access-list-number | community {community-list-name | community-listnumber} [exact-match] | interface interface-name | ip address access-list | ipv6 address
access-list | ip next-hop access-list | ipv6 next-hop access-list | metric metric-value | tag
tag-value }
l
as-path access-list-number - 匹配路由的AS路径。access-list-number为用户配置的AS路径访
问控制列表号。如果路由的AS路径匹配该访问控制列表中允许的AS路径，则认为匹配成功。有关AS路
径访问控制列表配置的更多信息，请参阅"AS路径访问控制列表" 在第599页。
l
community {community-list-name | community-list-number} [exact-match] - 匹配路由的团
体属性。community-list-name为团体属性列表名称；community-list-number为团体属性列表
号；exact-match指定对团体属性进行精确匹配。有关团体属性列表配置的更多信息，请参阅"团体属
性列表" 在第599页。

<!-- 来源页 596 -->
l
interface interface-name - 匹配路由的下一跳接口。
l
ip address access-list - 匹配路由的IPv4目的地址。access-list为用户配置的路由访问控制列表。
如果路由的目的地址属于该访问控制列表中允许的地址，则认为匹配成功。有关访问控制列表配置的更
多信息，请参阅"路由访问控制列表" 在第596页。
l
ipv6 address access-list - 匹配路由的IPv6目的地址。access-list为用户配置的路由访问控制列
表。如果路由的目的地址属于该访问控制列表中允许的地址，则认为匹配成功。有关访问控制列表配置
的更多信息，请参阅"路由访问控制列表" 在第596页。
l
ip next-hop access-list - 匹配路由的IPv4下一跳地址。access-list为用户配置的路由访问控制列
表。如果路由的下一跳地址属于该访问控制列表中允许的地址，则认为匹配成功。有关访问控制列表配
置的更多信息，请参阅"路由访问控制列表" 在第596页。
l
ipv6 next-hop access-list - 匹配路由的IPv6下一跳地址。access-list为用户配置的路由访问控制列
表。如果路由的吓一跳地址属于该访问控制列表中允许的地址，则认为匹配成功。有关访问控制列表配
置的更多信息，请参阅"路由访问控制列表" 在第596页。
l
metric metric-value - 匹配路由的度量值。取值范围是0到4294967295。
l
tag tag-value - 匹配路由的标记值。如果此处配置的路由的标记值匹配静态路由中的标记值，则认为
匹配成功。取值范围是1到4294967295。
重复以上命令向路由匹配规则中添加多个匹配条件。使用该命令no的形式删除匹配条件：
no match {as-path | community | interface | ip address | ipv6 address | ip next-hop | ipv6
next-hop | metric | tag}
注意: 如果用户仅创建了路由映射表但没有在映射表中配置任何路由匹配规则，系统默认会认为引
入的路由信息匹配成功。
例如，设置OSPF协议仅引入BGP协议中下一跳接口为eth0/1且度量值为50的路由信息，命令行如下：
hostname(config)# route-map test permit 10
hostname(config-route-map)# match interface ethernet0/1
hostname(config-route-map)# match metric 50
hostname(config-route-map)# exit
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# router ospf
hostname(config-router)# redistribute bgp route-map test

<!-- 来源页 597 -->
hostname(config-router)# end
匹配多条路由匹配规则
默认情况下，如果引入的路由信息命中任何路由匹配规则，系统将不再继续匹配后续的规则。用户可以设置
系统在命中一条规则后仍继续匹配其他规则，以实现更精细的控制。设置系统在匹配成功后继续匹配其他规
则，在路由映射表配置模式下，使用以下命令：
continue [sequence]
l
sequence – 指定继续匹配的规则序列号。取值范围是1到65535。该序列号必须大于当前规则的序列
号。如果没有指定此参数，系统在当前规则匹配成功后会继续匹配下一条规则。
使用该命令no的形式取消继续匹配其他规则：
no continue
例如，也可以通过以下命令行设置OSPF协议仅引入BGP协议中下一跳接口为eth0/1且度量值为50的路由信
息：
hostname(config)# route-map test permit 10
hostname(config-route-map)# match interface ethernet0/1
hostname(config-route-map)# continue 20
hostname(config-route-map)# exit
hostname(config)# route-map test permit 20
hostname(config-route-map)# match metric 50
hostname(config-route-map)# exit
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# router ospf
hostname(config-router)# redistribute bgp route-map test
hostname(config-router)# end
修改引入路由属性
修改引入路由的属性，在路由映射表配置模式下，使用以下命令：
set {as-path prepend as-number | commu-list {community-list-name | community-listnumber} delete | community {[internet] [local-AS] [no-advertise] [no-export] [communitylist-number]} [additive] | ip next-hop A.B.C.D | ipv6 next-hop X:X:X:X::X | metric metric-

<!-- 来源页 598 -->
value | metric-type {type-1 | type-2} | origin {egp | igp | incomplete} | tag tag-value | localpreference value}
l
as-path prepend as-number - 在引入路由的AS路径后添加新的AS路径。取值范围为1到65535之
间的数字，多个数字之间用空格隔开。
l
commu-list {community-list-name | community-list-number} delete - 指定团体属性列表名称
（community-list-name）或者团体属性列表号（community-list-number），删除匹配的团体属
性。
l
community {[internet] [local-AS] [no-advertise] [no-export] [community-list-number]}
[additive] - 修改引入路由的团体属性。BGP的团体属性具有可传递性，是一种用于简化路由策略执行
的标记，为路由分配特定团体属性之后，可以基于该团体属性值进行BGP属性配置，BGP路由最大支持
配置8个团体属性值。community-number为十进制格式的团体属性值，是1到4294967295之间的数
字，aa:nn为AA:NN格式的团体属性值。additive为在引入路由的团体属性中添加新的团体属性。
l
ip next-hop A.B.C.D - 修改引入路由的IPv4下一跳地址。
l
ipv6 next-hop X:X:X:X::X - 修改引入路由的IPv6下一跳地址。
l
metric metric-value - 修改引入路由的度量值。取值范围是0到4294967295。
l
metric-type {type-1 | type-2} - 修改外部路由的度量类型。type-1指将外部路由度量类型修改为
Type1类型，type-2指将外部路由度量类型修改为Type2类型。
l
origin {igp | egp | incomplete} - 修改引入路由的来源属性。igp指将引入路由的来源修改为起始于
AS内部；egp指将引入路由的来源修改为通过EGP获得；incomplete指将引入路由的来源修改为通过
其他方法获得。
l
tag tag-value - 修改引入路由的标记值。取值范围是1到4294967295。
l
local-preference value - 修改引入路由的本地优先属性。取值范围是0到4294967295。
使用该命令no的形式取消对路由属性的修改并还原到引入路由时的设置：
no set {as-path prepend | commu-list | community | ip next-hop | ipv6 next-hop | metric |
metric-type | origin | tag | local-preference}
路由访问控制列表
路由匹配规则中的目的地址和下一跳地址匹配是通过引用路由访问控制列表实现的。路由访问控制列表主要
由IP地址匹配规则和匹配成功后所执行操作（允许或拒绝）两部分组成。如果目的地址或下一跳地址匹配指
定的IP地址，系统会继续执行指定的操作。一个路由访问控制列表中可以包含多条IP地址匹配规则，系统按
照添加时间顺序依次匹配，命中任何一条规则会立即结束匹配；如果匹配失败，系统会执行拒绝操作。

<!-- 来源页 599 -->
配置路由访问控制列表
配置路由访问控制列表包括以下几项：
l 配置IPv4路由访问控制列表
l 配置IPv6路由访问控制列表
配置IPv4路由访问控制列表
配置IPv4路由访问控制列表，在全局配置模式下，执行以下命令：
access-list route name [{deny | permit} {{A.B.C.D/M | A.B.C.D A.B.C.D} [exact-match] | any}]
l
name - 指定路由访问控制列表的名称并进入路由访问控制列表配置模式。取值范围是1到31个字符。如
果该名称已经存在，则直接进入路由访问控制列表配置模式。
l
deny | permit - 指定对匹配的IPv4地址所执行的操作。deny为拒绝，permit为允许。
l
A.B.C.D/M | A.B.C.D A.B.C.D - 指定需要匹配的IPv4地址。支持两种方式，A.B.C.D/M或者A.B.C.D
A.B.C.D，例如1.1.1.0/24或者1.1.1.0 255.255.255.0。
l
exact-match - 对IPv4地址前缀进行精确匹配（不包括掩码）。
l
any - 匹配任意IPv4地址。
使用该命令no的形式删除IPv4路由访问控制列表：
no access-list route name [{deny | permit} {{A.B.C.D/M | A.B.C.D A.B.C.D} [exact-match] |
any}]
如果指定了具体的IP地址匹配规则，该命令只从路由访问控制列表中删除对应的规则而不会删除整个访问控
制列表。
为IPv4路由访问控制列表添加描述信息，在全局配置模式下，使用以下命令：
access-list route name description description
l
name – 指定路由访问控制列表的名称。取值范围是1到31个字符。
l
description – 指定描述信息。取值范围是1到31个字符。
使用该命令no的形式删除描述信息：
no access-list route name description
例如，设置OSPF协议拒绝引入BGP协议中下一跳地址为192.168.1.1和192.168.2.0网段中IP地址和的路由
信息，命令行如下：
hostname(config)# route-map test deny 10

<!-- 来源页 600 -->
hostname(config-route-map)# match ip next-hop access_list
hostname(config-route-map)# exit
hostname(config)# access-list route access_list permit 192.168.1.1/32
hostname(config)# access-list route access_list permit 192.168.2.0/24
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# router ospf
hostname(config-router)# redistribute bgp route-map test
hostname(config-router)# end
配置IPv6路由访问控制列表
配置IPv6路由访问控制列表，在全局配置模式下，执行以下命令：
ipv6 access-list route name [{deny | permit} {X:X:X:X::X/M [exact-match] | any}]
l
name - 指定路由访问控制列表的名称并进入路由访问控制列表配置模式。取值范围是1到31个字符。如
果该名称已经存在，则直接进入路由访问控制列表配置模式。
l
deny | permit - 指定对匹配的IPv6地址所执行的操作。deny为拒绝，permit为允许。
l
X:X:X:X::X/M - 指定需要匹配的IPv6地址前缀和前缀长度。
l
exact-match - 对IPv6地址前缀进行精确匹配（不包括前缀长度）。
l
any - 匹配任意IPv6地址。
使用该命令no的形式删除IPv6路由访问控制列表：
no ipv6 access-list route name [{deny | permit} {X:X:X:X::X/M [exact-match] | any}]
如果指定了具体的IP地址匹配规则，该命令只从路由访问控制列表中删除对应的规则而不会删除整个访问控
制列表。
为IPv6路由访问控制列表添加描述信息，在全局配置模式下，使用以下命令：
ipv6 access-list route name description description
l
name – 指定路由访问控制列表的名称。取值范围是1到31个字符。
l
description – 指定描述信息。取值范围是1到31个字符。
使用该命令no的形式删除描述信息：
no ipv6 access-list route name description

<!-- 来源页 601 -->
AS路径访问控制列表
AS路径是路由在到达目的网络之前所经过的AS号码序列。在到达目的网络之前，BGP路由每经过一个AS，
在出AS时就会将AS号码添加到AS路径中。
用户可以通过AS路径访问控制列表实现路由过滤。AS路径访问控制列表主要由正则表达式和匹配成功后所
执行操作（允许或拒绝）两部分组成。如果正则表达式匹配路由的AS路径，系统会继续执行指定的操作；如
果匹配失败，系统会执行拒绝操作。系统最多允许配置64个AS路径访问控制列表，每个AS路径访问控制列
表最多允许配置8条正则表达式。
配置AS路径访问控制列表
配置AS路径访问控制列表，在全局配置模式下使用以下命令:
ip as-path access-list access-list-number {deny | permit} regular-expression
l
access-list-number – 指定AS路径访问控制列表号。范围为1到500。
l
deny | permit – 指定对匹配的路由所执行的操作。deny为拒绝，permit为允许。
l
regular-expression – 指定用于匹配AS路径的正则表达式。StoneOS支持PCRE（Perl Compatible
Regular Expressions）正则表达式语法。
在全局配置模式下使用该命令no的形式删除AS路径访问控制列表：
no ip as-path access-list access-list-number [{deny | permit} regular-expression]
例如，配置序号为1的AS路径控制列表，拒绝经过AS 31的路由，但允许其他路由，请输入以下命令：
hostname(config)# ip as-path access-list 1 deny _31_
hostname(config)# ip as-path access-list 1 permit .*
hostname(config)#
团体属性列表
在BGP中，团体属性标识一组具有相同特征的路由信息，与其所在的IP子网和AS无关。除用户自定义的团体
属性外，系统支持如下的公认团体属性：
l No-export：带有这一团体属性值的路由不能通告给AS之外的对等体。
l No-adverties：带有这一团体属性值的路由不能通告给任何BGP对等体。
l Local-as：带有这一团体属性值的路由可以通告给本地AS内的其他对等体，不能通告到本地AS以外的对等体。
l Internet：带有这一团体属性值的路由可以通告给任何BGP邻居。默认情况下所有路由都携带该属性。

<!-- 来源页 602 -->
配置团体属性列表
团体属性列表主要由团体属性和匹配成功后所执行的操作（允许或拒绝）两部分组成。如果引入路由的团体
属性匹配指定的团体属性，系统会继续执行指定的操作；如果匹配失败，系统会执行拒绝操作。系统最多允
许配置128个团体属性列表，每个团体属性列表最多允许配置一条Permit规则和一条Deny规则。配置团体
属性列表，在全局配置模式下，使用以下命令：
ip community-list {standard community-list-name | community-list-number} {deny | permit}
{[internet] [local-as] [no-advertise] [no-export] [community-number]}
l
standard community-list-name – 指定团体属性列表名称。为1到31个字符的字符串。
l
community-list-number - 指定团体属性列表号。范围为1到99。
l
deny | permit – 指定对匹配的路由所执行的操作。deny为拒绝，permit为允许。
l
[internet] [local-as] [no-advertise] [no-export] [community-number] – 指定团体属性，可以
同时指定多个团体属性，不同团体属性间用空格隔开。对于满足匹配条件的路由条目，BGP引入静态路
由时支持根据静态路由的标记值配置团体属性值，BGP路由最大支持配置8个团体属性值。communitynumber为十进制格式的团体属性值，是1到4294967295之间的数字，aa:nn为AA:NN格式的团体属
性值。
在全局配置模式下使用该命令no的形式删除团体属性列表：
no ip community-list {standard community-list-name | community-list-number}
等价多径路由（ECMP）
等价多径路由（ECMP）是对经过安全设备的数据流量在多条等价路径（同协议）上进行负载均衡转发的方
法。
配置ECMP功能
默认情况下，系统的ECMP功能为开启状态，并允许最多40条等价路由条目进行负载均衡。在VRouter配置
模式下，使用以下命令开启或关闭ECMP功能：
ecmp enable ecmp-route-num
l
ecmp-route-num – 系统允许的最大ECMP路由条目数。取值范围为1到1000。当取值为1时表示不使
用ECMP功能。
配置ECMP选路方式
在全局配置模式下，使用以下命令配置ECMP选路方式：
ecmp-route-select {by-5-tuple | by-src | by-src-and-dst}

<!-- 来源页 603 -->
l
by-5-tuple – 基于五元组（源IP地址、目的IP地址、源端口、目的端口和服务类型）进行选路。
l
by-src – 基于源IP地址进行选路。
l
by-src-and-dst - 基于源IP地址和目的IP地址进行选路。该方式为系统默认选路方式。

<!-- 来源页 604 -->
静态组播路由
组播是将数据从一个源点传送到多个目的节点的一种通信方式。发送数据的源点称为组播源，接收数据的多
个节点构成组播组。组播源将数据发送至目的地址，其地址范围是224.0.0.0至239.255.255.255之间的D
类地址，称为组播地址。
互联网内任意一台主机均可作为组播源，源点只发送一份数据至组播地址，组内的所有接收者均可接收到相
同的数据。应用组播方式传递信息，能够有效的节约网络带宽；如果接入网络用户数量增加，不会增大发送
数据主机的负担，降低了网络负荷。
用户可以通过手工配置组播路由规则来实现将数据从组播源传送给组播成员。组播路由规则需要定义以下信
息：
l 组播源和组播地址：即组播源IP和目的IP。
l 入接口和出接口：匹配对应组播源和组播地址的数据从组播路由规则中指定的入接口进，从指定的出接口出。
开启/关闭组播路由功能
默认情况下，组播路由功能为关闭状态。在VRouter配置模式下，使用以下命令开启或关闭组播路由功能：
l
开启组播路由：ip multicast-routing
l
关闭组播路由：no ip multicast-routing
配置静态组播路由
在VRouter配置模式下，使用以下命令创建静态组播路由：
ip mroute A.B.C.D A.B.C.D [iif interface-name] [eif interface-name]
l
A.B.C.D A.B.C.D – 指定组播源和组播地址。第一个A.B.C.D为组播源IP地址；第二个A.B.C.D为组播地
址，其地址范围是224.0.0.0 至239.255.255.255 之间。
l
iif interface-name – 指定入接口名称。在此命令中，最多允许用户指定2个入接口名称。
l
eif interface-name – 指定出接口名称。在此命令中，最多允许用户指定4个出接口名称。
在VRouter配置模式下，使用该命令的no形式删除静态组播路由：
no ip mroute A.B.C.D A.B.C.D [iif interface-name] [eif interface-name]

<!-- 来源页 605 -->
指定入接口/出接口
用户可以为已创建的静态组播路由条目配置入接口或出接口。系统允许为每条组播路由条目最多配置2个入
接口，32个出接口。入接口或出接口的配置需要在静态组播路由配置模式下进行。进入静态组播路由配置模
式，在VRouter配置模式下，使用以下命令：
ip mroute A.B.C.D A.B.C.D
l
A.B.C.D A.B.C.D – 指定组播源和组播地址。第一个A.B.C.D为组播源IP地址；第二个A.B.C.D为组播地
址。
为已创建的静态组播路由条目指定入接口或出接口名称，在静态组播路由配置模式下，使用以下命令：
l
指定入接口名称：iif interface-name
l
指定出接口名称：eif interface-name
多次执行以上命令配置多个入接口或出接口。
显示组播路由信息
用户可以在任何模式下，随时使用show命令查看组播路由信息。命令如下：
show ip mroute [A.B.C.D A.B.C.D | static | summary] [vrouter vr-name]
l
show ip mroute – 显示全部组播路由信息。
l
A.B.C.D A.B.C.D – 通过指定组播源地址和组播地址，显示其组播路由信息。第一个A.B.C.D为组播源
地址，第二个A.B.C.D为组播地址。
l
static – 显示静态组播路由信息。
l
summary – 显示组播路由的摘要信息。
l
vrouter vr-name – 显示指定VRouter下的组播路由信息。
显示组播FIB信息
用户可以在任何模式下，使用以下命令查看组播FIB信息：
show mfib [A.B.C.D A.B.C.D | summary] [vrouter vr-name]
l
show mfib – 显示所有组播FIB信息。
l
A.B.C.D A.B.C.D – 通过指定组播源地址和组播地址，显示其组播FIB信息。第一个A.B.C.D为组播源地
址，第二个A.B.C.D为组播地址。

<!-- 来源页 606 -->
l
summary – 显示组播FIB的摘要信息。
l
vrouter vr-name – 显示指定VRouter下的组播FIB信息。

<!-- 来源页 607 -->
互联网组管理协议IGMP
互联网组管理协议IGMP（Internet Group Message Protocol）是用于在主机和路由器之间建立并维护组
播成员关系的协议。通过IGMP协议，主机向路由器报告组成员的加入和离开，路由器周期性地发送查询报文
查看是否有组成员处于活动状态，如果未收到组播成员的报告报文，则认为该组播组中已无组成员。
当前版本的StoneOS支持IGMPv1（由RFC1112定义）、IGMPv2（由RFC2236定义）和IGMPv3（由
RFC3376定义）。并且支持IGMP Proxy（工作在应用层）和IGMP Snooping（工作在链路层）两个功
能。
本章节包含以下内容：
l IGMP Proxy
l IGMP Snooping
l 携带Router-Alert选项
IGMP Proxy
IGMP Proxy靠代理拦截主机和路由器之间的IGMP报文来建立组播路由表项，进行组播数据的转发。IGMP
Proxy在安全设备的两个接口上分别实现不同的功能。上联到组播路由器的上行接口代理实现主机的功能，
响应来自路由器的查询。当组播组新增一个成员或者最后一个成员退出时，安全设备通过上行接口主动发送
成员报告报文或者离开报文。下联到用户主机的下行接口代理实现路由器的功能，进行组成员的登记、查询
和删除工作。
配置IGMP代理，请按照以下步骤进行操作：
1. 启用组播路由功能。具体操作，请参阅“开启/关闭组播路由功能”。
2. 启用IGMP代理功能。
3. 配置上行接口为主机模式，代理主机功能。
4. 配置下行接口为路由器模式，代理IGMP路由器功能。
5. 配置策略规则。
启用IGMP代理
在VRouter配置模式下，使用以下命令启用或禁用IGMP代理功能：
l
启用IGMP代理：ip igmp-proxy enable
l
禁用IGMP代理：no ip igmp-proxy enable
在全局配置模式下，使用以下命令进入VRouter配置模式：

<!-- 来源页 608 -->
ip vrouter vrouter-name
l
vrouter-name – 指定VRouter的名称。如果指定的名称已存在，则直接进入VRouter配置模式。
配置接口的IGMP代理模式
在接口配置模式下，用户可使用以下命令配置接口的IGMP代理模式，使它处于主机模式或路由器模式：
ip igmp-proxy {router-mode | host-mode} [A.B.C.D] [v2| v3]
l
router-mode – 配置下行接口的IGMP代理模式为路由器模式。
l
host-mode – 配置上行接口的IGMP代理模式为主机模式。
l
[A.B.C.D] – 指定组播组地址。配置组播地址后，系统认为IGMP代理模式仅对此组播地址有效。
l
v2 – 指定接口发送的IGMP报文的协议版本为IGMPv2。默认情况下，使用IGMPv2协议。
l
v3 – 指定接口发送的IGMP报文的协议版本为IGMPv3。
在接口配置模式下，使用该命令no的形式取消指定接口的IGMP代理模式：
no ip igmp-proxy {router-mode | host-mode} [A.B.C.D]
查看IGMP Proxy信息
用户可以在任何模式下，随时使用show命令查看IGMP Proxy信息。命令如下：
show ip igmp-proxy [A.B.C.D] [vrouter vrouter-name]
l
show ip igmp-proxy – 查看系统中全部IGMP Proxy信息。
l
[A.B.C.D] – 查看指定的组播组地址的IGMP Proxy信息。
l
[vrouter vrouter-name] – 查看指定的VRouter下的IGMP Proxy信息。
IGMP Snooping
IGMP Snooping是通过监听主机和路由器之间的IGMP报文，在二层设备上建立针对某个组播地址的组播路
由表项。开启IGMP Snooping功能后，安全设备根据组播路由表项转发组播数据，有效的减少了组播通信
的开销。如果没有开启IGMP Snooping功能，安全设备只能广播组播数据。
配置IGMP Snooping，请按照以下步骤进行操作：
1. 开启组播路由功能。具体操作，请参阅“开启/关闭组播路由功能”。
2. 开启IGMP Snooping功能。
3. 配置IGMP Snooping。
4. 配置策略规则。

<!-- 来源页 609 -->
启用IGMP Snooping
在VSwitch配置模式下，使用以下命令启用或禁用IGMP Snooping功能：
l
启用IGMP Snooping功能：ip igmp-snooping enable
l
禁用IGMP Snooping功能：no ip igmp-snooping enable
在全局配置模式下，使用以下命令创建或进入VSwitch配置模式：
vswitch vswitch Number
l
Number – 指定VSwitch的数字标识。Number的取值范围根据平台不同而不同。例如，命令vswitch
vswitch2创建了名为VSwitch2的VSwitch，同时也创建了VSwitchif2接口，并且进入VSwitch2的配
置模式。如果指定的VSwitch名称已存在，则直接进入VSwitch配置模式。
配置IGMP Snooping
在接口配置模式下，使用以下命令配置IGMP Snooping功能：
ip igmp-snooping {router-mode [A.B.C.D] | host-mode [A.B.C.D] | disable | auto}
l
router-mode – 配置下行接口的IGMP Snooping模式为路由器模式。
l
host-mode – 配置上行接口的IGMP Snooping模式为主机模式。
l
[A.B.C.D] – 指定组播组地址。
l
disable – 禁用接口的IGMP Snooping功能。
l
auto – 指定该参数，系统通过IGMP报文自动确定接口的模式。
在接口配置模式下，使用该命令no的形式取消配置IGMP Snooping功能：
no ip igmp-snooping {router-mode A.B.C.D | host-mode A.B.C.D}
未知组播丢弃
默认情况下，未知组播丢弃功能为关闭状态。开启该功能后，安全设备将丢弃发往未知组播组的报文，从而
节省带宽。在VSwitch配置模式下，使用以下命令开启未知组播丢弃功能：
unknown-multicast drop
在VSwitch配置模式下，使用该命令no的形式关闭未知组播丢弃功能：
no unknown-multicast drop
查看IGMP Snooping信息
用户可以在任何模式下，随时使用show命令查看IGMP Snooping信息。命令如下：

<!-- 来源页 610 -->
show ip igmp-snooping [A.B.C.D] [vswitch name]
l
show ip igmp-snooping - 显示全部IGMP Snooping信息。
l
[A.B.C.D] – 查看指定的组播组地址的IGMP Snooping信息。
l
[vswitch name] – 查看指定的VSwitch下的IGMP Snooping信息。
携带Router-Alert选项
通常情况下，网络设备收到报文时，只有目的IP地址为本设备接口地址的报文才会上送给相应的协议模块处
理。如果协议报文的目的地址不是本设备的接口地址，比如IGMP协议报文，由于其目的地址为组播地址，这
种情况下就无法上送给IGMP协议模块处理，导致正常的组成员关系不能维护。为了解决此类问题，RouterAlert选项应运而生。如果报文中携带Router-Alert选项，设备在接收到此类报文后，会直接上送给相应的
协议模块处理，而不检查目的地址。
在发送IGMP报文时，可以选择是否需要携带Router-Alert选项。默认情况下，设备发送的IGMP报文中不携
带Router-Alert选项。当需要与支持Router-Alert选项的设备互通时，用户可以开启携带Router-Alert选
项功能。
开启携带Router-Alert选项功能，在VRouter配置模式下，使用以下命令：
ip igmp send-router-alter
关闭携带Router-Alert选项功能，在VRouter配置模式下，使用以下命令：
no ip igmp send-router-alter

<!-- 来源页 611 -->
协议无关组播（PIM）
协议无关组播PIM（Protocol Independent Multicast），表示为IP组播提供路由信息的可以是静态路由
或任意单播路由协议（如RIP、OSPF、IS-IS等）。组播路由和所采用的单播路由协议无关，只要是能够通过
单播路由协议产生相应的组播路由表项即可。
根据机制的不同，PIM分为以下两种模式：
l PIM-DM（Protocol Independent Multicast-Dense Mode）：协议无关组播－密集模式，适用于小规模、接收
者分布较为密集的情况。
l PIM-SM（Protocol Independent Multicast-Sparse Mode）：协议无关组播－稀疏模式，适用于大规模、接
收者分布较为稀疏的情况。
PIM-SM基本原理
PIM-SM（Protocol Independent Multicast-Sparse Mode，协议无关组播-稀疏模式）可以有效解决
“点到多点”的数据传输问题，使用户能够按需接收数据。
PIM-SM假设网络中所有主机都不需要接收组播数据，只有在主机明确提出需要接收组播数据时，PIM设备
才会向该主机转发组播数据。
PIM-SM通过配置的RP（Rendezvous Point，汇聚点）和BSR（BootStrap Router，自举路由器），向
PIM域中的PIM设备发送组播信息，从而构建RPT（Rendezvous Point Tree，共享树），组播数据通过RP
沿着RPT转发给接收者。
PIM-SM相关概念如下：

<!-- 来源页 612 -->
l PIM域: 由PIM设备所组成的PIM网络。
l DR（Designated Router）:称为指定路由器，在PIM域中，包括两种DR:
l 组播源DR：组播源DR是与组播源直接相连且负责向RP发送注册报文的PIM设备。
l 接收者DR：与组播组成员（通常为接收者主机）直接相连且负责向该组成员转发组播数据的PIM设备。
l RP（Rendezvous Point）：称为汇聚点，是PIM域的转发核心，分为静态RP和动态RP。PIM-SM中建立的RPT
（Rendezvous Point Tree），就是一棵以RP为根，以存在组播数据接收者的PIM设备为叶子的共享树。
l BSR（BootStrap Router）：称为自举路由器，负责收集和分发网络内的RP信息。
l RPT（Rendezvous Point Tree）：称为共享树。以RP（Rendezvous Point）为根，组播组成员为叶子的组播
分发树称为RPT。
l SPT（Shortest Path Tree）：称为最短路径树。以组播源为根，组播组成员为叶子的组播分发树称为SPT。
PIM-SSM
使用PIM-SM模式实现组播数据传输需要在网络中维护RP（Rendezvous Point，汇聚点），当网络中的接
收者已经知道了组播源的具体位置，希望直接向组播源请求组播数据时，PIM-SSM（Protocol
Independent Multicast-Source-Specific Multicast，协议无关组播－指定源组播）可为指定源组播提
供解决方案，通过IGMPv3来维护主机与路由器之间的关系，实现组播组成员的快速加入，直接在组播源和
组成员之间建立SPT（Shortest Path Tree, 最短路径树），无需维护RP，组播数据沿着SPT转发给接收
者。
PIM-DM基本原理
PIM-DM（Protocol Independent Multicast-Dense Mode，协议无关组播-密集模式）可以有效解决组
播数据在密集网络中的高效分发问题，确保网络带宽的合理利用和动态组成员管理的灵活性。
PIM-DM假设网络中的组播接收者分布非常稠密，每个网段都可能存在组播接收者，当有活跃的组播源出现
时，它会将组播源发来的组播报文扩散到整个网络的PIM路由上，再裁剪掉不存在组播接收者的分支。
PIM-DM通过周期性的进行“扩散（Flooding）-剪枝（Prune）”，来构建并维护一棵连接组播源和组播
接收者的单向无环SPT（Source Specific Shortest Path Tree，单向无环最短路径树）。如果在下一次
“扩散-剪枝”进行前，被裁剪掉的分支由于其最后一跳路由器上有新的组播接收者加入而希望提前恢复转发
状态，也可通过嫁接（Graft）机制主动恢复其对组播报文的转发。
PIM-DM的关键工作机制包括邻居发现、扩散（Flooding）、剪枝（Prune）、嫁接（Graft）和断言
（Assert）。

<!-- 来源页 613 -->
邻居发现
邻居发现是通过路由器之间周期性发送的Hello消息来实现的。当一个路由器启用PIM功能后，它会在其所有
使能了PIM的接口上定期发送Hello消息。这些消息包含必要的协议参数信息，用于在直接相连的路由器之间
建立和维护邻居关系。
Hello消息是组播发送的，通常发送到组播地址224.0.0.13，这个地址是PIM路由器专用的组播地址。当相
邻的路由器收到这些Hello消息时，它们会确认彼此的邻居身份，并开始交换PIM协议信息。这个过程确保了
PIM路由器能够发现在同一网段内的其他PIM路由器，并建立起稳定的邻居关系。
为了维护这种邻居关系，路由器会持续监听来自邻居的Hello消息。如果在设定的时间内（通常称为
Holdtime）没有收到来自特定邻居的Hello消息，该邻居关系将被视为失效，相应的路由信息也会从PIM路
由表中移除。
扩散（Flooding）机制
当PIM-DM网络中出现活跃的组播源，其发送的组播报文将在全网内扩散。如下图所示，当路由器A（即组
播源DR A）接收到组播源Server发送的组播报文后，会根据单播路由表进行RPF（Reverse Path
Forwarding，反向路径转发）检查。若RPF检查通过，路由器A将创建组播路由（S，G）表项，并把路由
器B（即接收者DR B）和路由器C（即接收者DR C）相连的接口纳入下游接口列表，后续到达的组播报文会
被转发至路由器B和路由器C。
路由器B接收到来自路由器A的组播报文后，同样通过RPF检查，创建相应的组播路由（S，G）表项，并将
报文转发给连接的组播接收者PC1。而路由器C在接收到来自路由器A的组播报文后，鉴于其下游网段中不存
在组播接收者和PIM邻居，路由器C将对该组播路径执行剪枝，不再转发该组播报文。这一过程确保了组播报
文在网络中的有效扩散，同时通过剪枝机制避免了不必要的流量。
剪枝（Prune）机制
当PIM路由器接收到组播报文且通过RPF检查后，若判定下游网段无组播报文需求，该PIM路由器便会向上游
发送剪枝报文，以此通知上游路由器禁止相应下游接口的转发，并将此接口从组播路由（S，G）表项的下游

<!-- 来源页 614 -->
接口列表中移除。剪枝操作由最后一跳路由器发起，以逐跳向上的方式进行，最终使得组播转发路径仅保留
与组播接收者相连的分支。
被裁剪的下游接口会启动剪枝定时器，超时后该接口恢复转发功能，以便新加入的组播接收者能够接收到组
播报文。当下游不存在组播接收者时，最后一跳路由器会再次向上发起剪枝操作。通过这种周期性的“扩散
（Flooding）-剪枝（Prune）” 过程，PIM-DM能够周期性地刷新SPT。此外，当下游接口被剪枝后，若
下游最后一跳路由器有新的组播接收者加入，且期望在下次“扩散（Flooding）-剪枝（Prune）” 前恢
复组播报文转发，则会执行嫁接机制。
如下图所示，路由器C（即接收者DR C）判断下游网段无组播报文需求后，会向路由器A（即组播源DR A）
发送Prune消息，通知路由器A不必再向该下游网段转发数据。当路由器A收到Prune消息后，停止向该下游
接口转发数据，并将该下游接口从组播路由（S，G）表项中删除，以上过程称之为剪枝。由于路由器A上还
存在其他处于转发状态的下游接口，因此路由器A继续向路由器B（即接收者DR B）转发组播报文，且后续
到达的报文只向路由器B转发，从而实现了一棵连接组播源和组播接收者的单向无环SPT。
嫁接（Graft）机制
PIM-DM协议中的嫁接机制旨在加速新加入组播接收者获取组播数据流的过程。当最后一跳路由器通过IGMP
协议检测到新的组播接收者加入时，它会向上游路由器发送Graft消息，请求恢复向该分支转发组播数据
流。上游路由器接收到Graft消息后，会将相应的接口添加到组播路由（S，G）表项的下游接口列表中，从
而恢复组播数据流的转发。这一机制确保了新的组播接收者能够迅速接收到组播数据，而无需等待下一次周
期性的扩散过程。
如下图所示，路由器C（即接收者DR C）期望在下一次“扩散（Flooding）-剪枝（Prune）”周期之前
恢复对接收者PC2组播报文转发，因此向其上游路由器A（即组播源DR A）发送Graft消息，请求恢复对应
出接口的组播报文转发。路由器A在接收到Graft消息后，将恢复连接到路由器C的出接口的组播报文转发，
使得组播报文能够通过该下游接口顺利到达路由器C。

<!-- 来源页 615 -->
断言（Assert）机制
断言机制是PIM协议中用于解决多路由器转发相同组播报文至同一网段时可能出现的冲突问题。当多个PIM
路由器向同一网段转发组播报文时，它们会发送Assert消息以声明自己的转发优先权。通过比较IP地址的大
小，确定一个Assert Winner（即IP地址较大的路由器），该路由器继续向下游转发组播报文，而其他路由
器（Assert Loser）则停止转发。这一机制确保了组播报文在网络中的唯一性和有效性，同时允许周期性地
重新评估和调整转发权限。
如下图所示，路由器B和路由器C都能够接收来自组播源Server的组播报文，并且均通过RPF检查，从而在各
自的路由表中创建组播路由（S，G）表项。由于路由器B和路由器C的下游接口都连接到同一网段，它们会
尝试同时向该网段转发组播数据。
断言过程如下：
1. 路由器B和路由器C从各自下游接口接收到来自对方发来的组播报文，由于RPF检查均失败，报文将被丢弃。同
时，路由器B和路由器C分别向该网段发送Assert消息。
2. 路由器B将自身的IP地址与路由器C发来的Assert消息中携带的IP地址进行比较，由于自身IP地址较大而获胜。后
续路由器B仍向该网段转发组播报文，而路由器C在接收到组播报文后仍然因RPF检查失败而丢弃报文。
3. 路由器C将自身的IP地址与路由器B发来的Assert消息中携带的IP地址进行比较，由于自身IP地址较小而落败。后
续路由器C将停止通过该下游接口转发组播报文，并将其从自身的（S，G）表项的下游接口列表中删除。

<!-- 来源页 616 -->
配置协议无关组播（PIM）注意事项
对PIM的配置包括基本配置以及在不同的接口上配置PIM-SM/PIM-DM功能。
注意:
l
PIM-SM功能、PIM-DM功能分别与静态组播路由功能、IGMP Proxy功能互斥，且PIM-SM与
PIM-DM功能之间也是互斥的，不能同时配置。
l
PIM-SSM是在PIM-SM基础上实现的，在配置PIM-SSM之前，请先配置PIM-SM功能。
l
在HA环境下，PIM-SSM仅支持Active-Passive （A/P）模式。
l
仅支持在三层接口上开启PIM-SM/PIM-DM功能。
配置协议无关组播-稀疏模式（PIM-SM）
开始之前
l 阅读"协议无关组播（PIM）" 在第609页介绍
l 阅读"配置协议无关组播（PIM）注意事项" 在第614页
协议无关组播-稀疏模式（PIM-SM）的配置分为以下两部分：
1. 在指定虚拟路由器（VRouter）上，配置PIM基本信息并开启PIM-SM功能。具体配置包括：
l 开启/关闭组播路由功能（具体请参阅“静态组播路由> 开启/关闭组播路由功能”章节）
l 开启/关闭PIM-SM功能
l 配置候选RP
l 配置候选BSR

<!-- 来源页 617 -->
l 配置静态RP
l 指定关闭RPT向SPT切换
2. 在不同的接口上配置PIM-SM功能。具体配置包括：
l 开启/关闭接口的PIM-SM功能
l 配置接口的PIM被动模式
l 配置DR优先级
l 指定接口的Hello报文发送间隔
l 指定发送IGMP通用查询报文间隔
l 指定IGMP通用查询超时时间
l 指定IGMP通用查询最大响应时间
l 指定非直连组播源的组播源地址
l 将组播路由器接口加入组播组
l 配置组播路由反射功能
配置PIM基本配置并开启PIM-SM功能
用户可以为不同的VRouter分别配置PIM-SM。配置PIM基本配置并开启PIM-SM功能需要在PIM配置模式下
进行。进入PIM配置模式，请在全局配置模式下，使用以下命令：
ip vrouter vrouter-name （进入VRouter配置模式）
router pim（进入PIM配置模式）
开启/关闭PIM-SM功能
默认情况下，PIM-SM功能为关闭状态。在PIM配置模式下，使用以下命令开启或关闭PIM-SM功能：
l
开启PIM-SM：pim-sm enable
l
关闭PIM-SM：no pim-sm enable
配置候选RP
在PIM-SM域内选择几台PIM设备配置候选RP（Rendezvous Point, 汇聚点），从候选RP中选举产生RP。
必须同时配置候选BSR，由候选BSR（BootStrap Router, 自举路由器）选举产生BSR，BSR负责收集并发
布网络中的RP信息。
配置候选RP，在PIM配置模式下，使用以下命令：
rp-candidate interface-name [interval interval-time ] [priority level]

<!-- 来源页 618 -->
l
interface-name – 指定候选RP所在接口，该接口必须开启PIM-SM功能。
l
interval-time – 指定发送候选RP消息的时间间隔，单位是秒。范围是1到16383秒。默认值是60秒。
l
priority level – 指定优先级（数值越小，优先级越高）。在RP选举中，优先级较高的候选RP优先被选
举为RP。范围是0到255，默认值为0。
在PIM配置模式下，使用以上命令no的形式删除配置的候选RP：
no rp-candidate
注意: 当配置候选RP时，无需指定组播地址，默认组播地址为224.0.0.0/4。
配置候选BSR
在一个PIM-SM域中，需要配置一个或多个候选BSR，候选BSR之间通过自动选举，产生BSR，BSR负责收集
并发布RP信息。
配置候选BSR，在PIM配置模式下，使用以下命令：
bsr-candidate interface-name [priority level]
l
interface-name – 指定候选BSR所在接口，该接口必须开启PIM-SM功能。
l
priority level – 指定优先级（数值越大，优先级越高）。如果在PIM-SM域中，只有一个候选BSR，即
被选为BSR；如果存在多个候选BSR，在BSR选举中，优先级较高的候选BSR优先被选举为BSR。范围是
0到255，默认值为0。
在PIM配置模式下，使用以上命令no的形式删除配置的候选BSR：
no bsr-candidate
注意: 当使用动态RP时，候选BSR必须配置，同时，在PIM-SM域中至少配置一个候选BSR。
配置静态RP
当网络内仅有一个RP时，用户可以配置静态RP，这样可以避免候选RP和BSR之间频繁的信息交互占用带
宽。PIM-SM域内所有设备都必须配置完全相同的静态RP。
指定静态RP地址，在PIM配置模式下，使用以下命令：
rp-address A.B.C.D [A.B.C.D/M]
l
A.B.C.D – 指定静态RP所在接口IP地址。
l
A.B.C.D/M – 指定组播地址。

<!-- 来源页 619 -->
在PIM配置模式下，使用以上命令no的形式删除配置的静态RP地址：
no rp-address A.B.C.D [A.B.C.D/M]
指定关闭RPT向SPT切换
由于PIM-SM域中已构建的RPT（Rendezvous Point Tree, 共享树）不一定是路径最短的树，因此当组播
数据流量变大时，RP可能会成为故障点。为了解决这个问题，在默认情况下，RPT可以向SPT（Shortest
Path Tree, 最短路径树）切换，切换到SPT后，组播数据将直接从组播源沿着SPT发送到接收者。用户可以
根据需要，指定关闭RPT向SPT切换。
RPT向SPT切换前示意图：
RPT向SPT切换后示意图
指定关闭RPT向SPT切换，在PIM配置模式下，使用以下命令：
spt-threshold {0 | infinity}
l
0 – 指定RPT向SPT切换。该选项为默认选项。
l
infinity – 关闭RPT向SPT切换。
在PIM配置模式下，使用以上命令no的形式恢复默认向SPT切换：
no spt-threshold

<!-- 来源页 620 -->
配置接口的PIM-SM功能
接口的PIM-SM功能配置需要在接口配置模式下完成。PIM-SM功能在设备接口上的配置包括：
l 开启/关闭接口的PIM-SM功能
l 配置接口的PIM被动模式
l 配置DR优先级
l 指定接口的Hello报文发送间隔
l 指定发送IGMP通用查询报文间隔
l 指定IGMP通用查询超时时间
l 指定IGMP通用查询最大响应时间
l 指定非直连组播源的组播源地址
l 将组播路由器接口加入组播组
l 配置组播路由反射功能
开启/关闭接口的PIM-SM功能
默认情况下，接口的PIM-SM功能为关闭状态。用户可以在接口配置模式下，使用以下命令，开启或关闭指
定接口的PIM-SM功能：
l
开启指定接口的PIM-SM功能：ip pim sparse-mode
l
关闭指定接口的PIM-SM功能：no ip pim sparse-mode
注意: 仅支持三层接口上开启PIM-SM功能。
配置接口的PIM被动模式
接口在开启PIM-SM功能的情况下，如果有恶意主机模拟PIM Hello报文，并且大量发送时，可能导致设备
瘫痪。为避免发生上述安全问题，可以为该接口开启PIM被动模式。开启后，接口将不再接收和转发任何
PIM报文，接口上的所有PIM邻居都会被删除，并且该接口会自动成为DR。同时，接口开启PIM被动模式后
不会影响接口对IGMP报文的处理。
PIM被动模式一般通过结合接口加入组播组功能可以实现对组播流量转发的控制。
开始之前
在配置接口的PIM被动模式前，需要完成以下任务：

<!-- 来源页 621 -->
l
在接口配置模式下，使用ip pim sparse-mode命令开启接口的PIM-SM功能。
l
在VRouter配置模式下，使用ip multicast-routing命令开启组播路由功能。
注意:
l
该功能仅适用于与用户主机网段直连的PIM设备接口，且该网段上只能连接一台PIM设备。
l
配置该功能后，接口将不再接收和转发任何PIM协议报文，即该接口配置的其他PIM功能将失
效，请谨慎使用。
操作步骤
默认情况下，接口的PIM被动模式为关闭状态。开启接口的PIM被动模式，在接口配置模式下，使用以下命
令：
ip pim passive
在接口配置模式下，使用该命令no的形式将功能恢复为关闭状态：
no ip pim passive
检查配置结果
配置接口的PIM被动模式后，可以在接口配置模式下，使用show this命令查看是否配置成功。
以下是配置成功的返回结果示例：
hostname(config-if-eth0/3)#show this
interface ethernet0/3
ip pim passive
exit
配置DR优先级
DR（Designated Router）的优先级用来决定使用哪个路由器作为指定路由器（DR）。指定DR的优先
级，在接口配置模式下，使用以下命令：
ip pim dr-priority level
l
level – 指定DR的优先级（数值越大，优先级越高）。默认值是1。范围是0到4294967294。PIM-SM
域中的路由器都可指定作为DR，优先级高的路由器会被选中；如果优先级也相同，IP地址大的会被选
中。
使用no ip pim dr-priority命令恢复默认优先级。

<!-- 来源页 622 -->
指定接口的Hello报文发送间隔
接口开启PIM-SM功能后，会定期发送Hello报文。用户可以根据需要，指定接口的Hello报文的发送间隔，
在接口配置模式下，使用以下命令：
ip pim query-interval interval
l
interval – 指定接口的Hello报文发送间隔。范围是1到65535秒，默认值是30秒。
使用no ip pim query-interval命令恢复默认发送间隔值。
指定发送IGMP通用查询报文间隔
接收者主机所在的网络可能同时连接多台组播路由器。这些组播路由器之间通过自动选举，选举出一台路由
器作为查询器，负责维护接口上的IGMP组成员关系。对于Hillstone设备，在接口开启PIM-SM功能后，查
询器会主动发送的IGMP通用查询报文，来了解组播组成员的加入和离开。
指定发送IGMP通用查询报文间隔，在接口配置模式下，使用以下命令：
ip pim igmp-query-interval interval
l
interval – 指定接口发送IGMP通用查询报文间隔时间。范围是1到18000秒，默认值是60秒。
使用no ip pim igmp-query-interval命令恢复默认值。
指定IGMP通用查询超时时间
如果网络内的组播路由器在指定超时时间内，未收到IGMP通用查询报文，组播路由器之间将会重新进行查询
器的选举。
指定IGMP通用查询超时时间，在接口配置模式下，使用以下命令：
ip pim igmp-query-timeout timeout-value
l
timeout-value – 指定IGMP通用查询超时时间。范围是30到300秒，默认值是120秒。
使用no ip pim igmp-query-timeout命令恢复超时时间默认值。
指定IGMP通用查询最大响应时间
用户可以指定接收者主机接受到通用查询报文后的最大响应时间。当查询器发送2次IGMP通用查询报文后，
如果在指定的最大响应时间内，未收到接收者主机的响应，那么系统将会在组播路由表中删除该接收者。
指定IGMP通用查询最大响应时间，在接口配置模式下，使用以下命令：
ip pim igmp-query-max-response-time response-time
l
response-time – 指定IGMP通用查询最大响应时间。范围是1到25秒，默认值是10秒。
使用no ip pim igmp-query-max-response-time命令恢复超时时间默认值。

<!-- 来源页 623 -->
指定非直连组播源的组播源地址
系统作为组播源DR无法与组播源跨网段建立邻居，组播源DR会丢弃与入接口不同网段的组播报文，所以通
过配置非直连组播源的组播源地址，在组播域所有PIM设备与组播源单播路由可达的前提下，可以满足组播
源DR与组播源跨网段组播的场景。
指定非直连组播源的组播源地址，在接口配置模式下，使用以下命令：
ip pim non-direct multicast source source-address/netmask
l
source-address/netmask – 指定非直连组播源的组播源地址和子网掩码。
使用no ip pim non-direct multicast source source-address/netmask命令删除指定的非直连组播
源的组播源地址。
注意:
l
仅根VSYS支持配置非直连组播源的组播源地址。
l
最多可以配置10条非直连组播源的组播源地址条目。
将组播路由器接口加入组播组
在组播环境中，如果组播接收者想接收组播数据，需要主动向其相邻的组播路由器发送IGMP Report报文，
以加入该组播组。这样，组播路由器就可以向组播接收者的网络转发组播数据包，组播流量便可以从组播源
到达组播接收者。但是，当组播路由器没有连接组播接收者，或者连接的组播接收者无法发送IGMP Report
报文时，组播源发送的组播数据就无法到达该组播路由器。为解决该问题，用户可以通过在接口上配置IGMP
Join-group，将组播路由器的接口加入到组播组，接收来自组播组的数据流量。用户可以配置接口使用
IGMPv2协议/IGMPv3协议加入到指定组播组。
配置接口使用IGMPv2协议加入到指定组播组，在接口配置模式下，使用以下命令：
ip pim igmp join-group group-address
l
group-address - 指定接口使用IGMPv2协议加入的组播组IP地址。
在接口配置模式下，使用no ip pim igmp join-group group-address命令将接口从指定组播组中移
除。
配置接口使用IGMPv3协议加入到指定组播组，在接口配置模式下，使用以下命令：
ip pim igmpv3 join-group group-addresssource-address
l
group-address - 指定接口使用IGMPv3协议加入的组播组IP地址。
l
source-address - 指定接口接收组播源数据流量的IP地址。

<!-- 来源页 624 -->
在接口配置模式下，使用no ip pim igmp join-group group-address source-address命令将接口从
指定组播组中移除。
注意:
l
仅支持将三层接口加入到组播组。
l
将接口成功加入到组播组，需要同时满足以下条件：
l
该接口开启了PIM-SM功能。关于如何开启接口的PIM-SM功能，请参阅开启接口的
PIM-SM功能。
l
该接口所在设备为接受者DR，且优先级最高。关于如何配置DR优先级，请参阅配置DR
优先级。
l
该接口所在设备的上游设备的接口也需要开启PIM-SM功能。
配置组播路由反射功能
型号说明：
l
不支持：SG-6000-K20803、K9180、K7680、K7280、K6680、K6580平台
l
不支持：SG-6000-X系列
组播服务反射功能（MSR，Multicast Service Reflection）功能支持处理转发到Vif接口上的组播数据，
将原始组播流的源地址和组播组地址转换为新的组播流。当组播流量匹配上MSR条目中的入接口和反射前的
组播组地址时，就可以转换为该MSR条目中的反射后的组播组地址和源地址。
配置组播路由反射功能的MSR条目，在Vif接口配置模式下，使用以下命令：
ip service reflect interface-name destination dst-address-before to dst-address-after
mask-len mask-length source source-address-after
l
interface-name - 指定原始组播流的入接口。
l
dst-address-before - 指定原始组播流的组播组地址。
l
dst-address-after - 指定转换后的组播组地址。
l
mask-length - 指定转换后组播组地址的子网掩码。范围是0到32。
l
source-address-after - 指定转换后的组播源地址。需要和Vif接口IP配置在同一网段。

<!-- 来源页 625 -->
在接口配置模式下，使用no ip service reflect interface-name destination dst-address-before
mask-len mask-length命令删除指定的MSR条目。
注意:
l
仅根VSYS支持组播服务反射MSR功能。
l
使用组播服务反射MSR功能时，如果单播路由结合OSPF协议进行通告学习，Vif接口上的
OSPF网络类型需通过ip ospf network point-to-point命令配置成点到点类型，以便邻居设
备学习到非主机路由。
l
最多可以配置100条MSR条目。当编辑已有的MSR条目时，需要interface-name、dstaddress-before和mask-length保持不变，否则会创建新的MSR条目。
PIM-SSM
使用PIM-SM模式实现组播数据传输需要在网络中维护RP（Rendezvous Point，汇聚点），当网络中的接
收者已经知道了组播源的具体位置，希望直接向组播源请求组播数据时，PIM-SSM（Protocol
Independent Multicast-Source-Specific Multicast，协议无关组播－指定源组播）可为指定源组播提
供解决方案，通过IGMPv3来维护主机与路由器之间的关系，实现组播组成员的快速加入，直接在组播源和
组成员之间建立SPT（Shortest Path Tree, 最短路径树），无需维护RP，组播数据沿着SPT转发给接收
者。
配置PIM-SSM
PIM-SSM的基本配置包括：
l 开启/关闭组播路由功能（具体请参阅“静态组播路由>开启/关闭组播路由功能”章节）
l 配置PIM-SSM组播组地址范围
注意:
l
PIM-SSM是在PIM-SM基础上实现的，在配置PIM-SSM之前，请先配置PIM-SM功能（具体请
参阅“协议无关组播（PIM）>配置PIM-SM”章节）。
l
在HA环境下，PIM-SSM仅支持Active-Passive （A/P）模式。
配置PIM-SSM组播组地址范围
默认情况下，PIM-SSM组播地址范围是232.0.0.0/8。用户可以根据需要，配置PIM-SSM组播组地址范
围，须确保网络内所有PIM设备配置的PIM-SSM组地址范围一致。在配置PIM-SSM组播组地址范围后，

<!-- 来源页 626 -->
PIM-SSM功能将会被同时开启。
配置PIM-SSM组播组地址范围，在PIM配置模式下，使用以下命令：
pim-ssm {default | group-prefix/Mask }
l
default - 指定使用默认的PIM-SSM组播组地址范围232.0.0.0/8。
l
group-prefix/Mask - 指定特定的PIM-SSM组播组地址范围。
在PIM配置模式下，使用以上命令no的形式删除配置的PIM-SSM组播组地址范围：
no pim-ssm
配置IGMP报文过滤功能
用户可以通过配置该功能，对开启PIM-SM/PIM-SSM功能的接口收到的IGMP报文进行过滤，允许/拒绝接
收指定协议版本的IGMP报文中的组播源或组播组。默认情况下，允许接口接收所有IGMP报文。
指定接口允许/拒绝接收IGMPv1/IGMPv2报文中的组播组，在接口配置模式下，使用以下命令：
ip pim igmp {permit | deny} group-prefix/Mask
l
permit- 指定该接口允许接收IGMPv1/IGMPv2报文中的组播组。
l
deny-指定该接口拒绝接收IGMPv1/IGMPv2报文中的组播组。
l
group-prefix/Mask- 指定组播组地址范围。
在接口配置模式下，使用以上命令no的形式恢复默认值：
noip pim igmp {permit | deny}
指定接口允许/拒绝接收IGMPv3报文中的组播源和组播组，在接口配置模式下，使用以下命令：
ip pim igmpv3 {permit | deny} {any |source-prefix/Mask}{any |group-prefix/Mask}
l
permit- 指定该接口允许接收IGMPv3报文中的组播源和组播组。
l
deny-指定该接口拒绝接收IGMPv3报文中的组播源和组播组。
l
any |source-prefix/Mask- 指定组播源地址范围。any为任意组播源地址。
l
any |group-prefix/Mask - 指定组播组地址范围。any为任意组播组地址。
在接口配置模式下，使用以上命令no的形式恢复默认值：
no ip pim igmpv3 {permit | deny}
配置协议无关组播-密集模式（PIM-DM）
开始之前

<!-- 来源页 627 -->
l 阅读"协议无关组播（PIM）" 在第609页介绍
l 阅读"配置协议无关组播（PIM）注意事项" 在第614页
协议无关组播-密集模式（PIM-DM）的配置分为以下两部分：
1. 在指定虚拟路由器（VRouter）上，配置PIM基本信息并开启PIM-DM功能。具体配置包括：
l 开启/关闭组播路由功能（具体请参阅“静态组播路由> 开启/关闭组播路由功能”章节）
l 开启/关闭PIM-DM功能
2. 在不同的接口上配置PIM-DM功能。具体配置包括：
l 开启/关闭接口的PIM-DM功能
l 配置接口的PIM被动模式
配置PIM基本信息并开启PIM-DM功能
用户可以为不同的VRouter分别配置PIM-DM。配置PIM的基本信息并开启PIM-DM功能需要在PIM配置模式
下进行。进入PIM配置模式，请在全局配置模式下，使用以下命令：
ip vrouter vrouter-name （进入VRouter配置模式）
router pim（进入PIM配置模式）
开启/关闭PIM-DM功能
默认情况下，PIM-DM功能为关闭状态。在PIM配置模式下，使用以下命令开启或关闭PIM-DM功能：
l
开启PIM-DM：pim-dm enable
l
关闭PIM-DM：no pim-dm enable
配置接口的PIM-DM功能
接口的PIM-DM功能配置需要在接口配置模式下完成。PIM-DM功能在设备接口上的配置包括：
l 开启/关闭接口的PIM-DM功能
l 配置接口的PIM被动模式
开启/关闭接口的PIM-DM功能
默认情况下，接口的PIM-DM功能为关闭状态。用户可以在接口配置模式下，使用以下命令，开启或关闭指
定接口的PIM-DM功能：
l
开启指定接口的PIM-DM功能：ip pim dense-mode
l
关闭指定接口的PIM-DM功能：no ip pim dense-mode

<!-- 来源页 628 -->
注意: 仅支持三层接口上开启PIM-DM功能。
示例：
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/3)# zone trust
hostname(config-if-eth0/3)# ip address 1.1.1.1 255.255.255.0
hostname(config-if-eth0/3)# ip pim dense-mode
配置接口的PIM被动模式
接口在开启PIM-DM功能的情况下，如果有恶意主机模拟PIM Hello报文，并且大量发送时，可能导致设备
瘫痪。为避免发生上述安全问题，可以为该接口开启PIM被动模式。开启后，接口将不再接收和转发任何
PIM报文，接口上的所有PIM邻居都会被删除，并且该接口会自动成为DR。同时，接口开启PIM被动模式后
不会影响接口对IGMP报文的处理。
开始之前
在配置接口的PIM被动模式前，需要完成以下任务：
l
在接口配置模式下，使用ip pim dense-mode命令开启接口的PIM-DM功能。
l
在VRouter配置模式下，使用ip multicast-routing命令开启组播路由功能。
注意:
l
该功能仅适用于与用户主机网段直连的PIM设备接口，且该网段上只能连接一台PIM设备。
l
配置该功能后，接口将不再接收和转发任何PIM协议报文，即该接口配置的其他PIM功能将失
效，请谨慎使用。
操作步骤
默认情况下，接口的PIM被动模式为关闭状态。开启接口的PIM被动模式，在接口配置模式下，使用以下命
令：
ip pim passive
在接口配置模式下，使用该命令no的形式将功能恢复为关闭状态：
no ip pim passive
检查配置结果
配置接口的PIM被动模式后，可以在接口配置模式下，使用show this命令查看是否配置成功。

<!-- 来源页 629 -->
以下是配置成功的返回结果示例：
hostname(config-if-eth0/3)#show this
interface ethernet0/3
ip pim passive
exit
查看PIM相关信息
查看候选BSR信息
查看候选BSR信息，在任何模式下使用以下命令：
show ip pim bsr-route [vrouter vrouter-name]
l
vrouter-name - 显示指定VRouter的BSR信息。
查看启用PIM功能的接口信息
查看启用PIM功能的接口信息，在任何模式下使用以下命令：
show ip pim interface [interface-name]
l
interface-name - 显示指定接口的PIM信息。
查看PIM邻居信息
查看PIM邻居信息，在任何模式下使用以下命令：
show ip pim neighbor [vrouter vrouter-name]
l
vrouter-name - 显示指定VRouter的PIM邻居信息。
查看静态RP信息
查看静态RP信息，在任何模式下使用以下命令：
show ip pim rp [vrouter vrouter-name | mapping [vrouter vrouter-name]]
l
vrouter-name - 显示指定VRouter的RP信息。
l
mapping [vrouter vrouter-name] - 显示指定VRouter的所有RP映射信息。
查看RPF信息
查看RPF信息，在任何模式下使用以下命令：

<!-- 来源页 630 -->
show ip pim rpf source-address [vrouter vrouter-name]
l
source-address – 显示指定组播源IP地址的RPF信息。
l
vrouter-name - 显示指定VRouter下的组播源IP的RPF信息。
查看IGMP组播组信息
查看IGMP组播组信息，在任何模式下使用以下命令：
show ip pim igmp groups [group-address [vrouter vrouter-name]]
l
group-address – 显示指定IP地址的IGMP组播组信息。
l
vrouter vrouter-name – 显示指定VRouter下的IGMP组播组信息。
查看IGMP接口信息
查看IGMP接口信息，在任何模式下使用以下命令：
show ip pim igmp interface [interface-name]
l
interface-name – 显示指定接口（已开启PIM-SM或PIM-DM功能）的IGMP信息。
查看非直连组播源的组播源地址信息
查看非直连组播源的组播源地址信息，在任何模式下使用以下命令：
show ip pim non-direct multicast source interface-name
l
interface-name – 显示指定接口（已开启PIM-SM功能）的非直连组播源的组播源地址信息。
例如：
hostname(config)# show ip pim non-direct multicast source ethernet0/3
Multicast Non-directly Connected Source Address Table for Interface <ethernet0/3>
=================================================
Interface id Source Mask（显示使用PIM协议的接口ID、组播源地址、子网掩码）
-------------------------------------------------
33 1.1.1.0 24
33 2.1.1.0 24
33 3.1.1.0 24
=================================================

<!-- 来源页 631 -->
协议无关组播（PIMv6）
PIMv6用于实现组播数据在IPv6网络环境中的传输。PIMv6表示为IP组播提供路由信息的可以是IPv6静态路
由或任意IPv6单播路由协议（如RIPng、OSPFv3、IPv6 IS-IS等）。组播路由和所采用的单播路由协议无
关，只要是能够通过单播路由协议产生相应的组播路由表项即可。
PIMv6与PIM的机制和实现原理相同，PIMv6仅支持IPv6 PIM-SM模式。PIMv6与PIM的不同主要有：
l 使用不同的组播成员管理协议，PIM使用IGMP协议，PIMv6使用MLD协议
l PIM支持PIM-SSM，PIMv6不支持PIM-SSM
组播侦听者发现协议（MLD）
组播侦听者发现协议MLD（Multicast Listener Discovery）是负责IPv6组播成员管理的协议，用来在
IPv6主机和与其直连的组播设备之间建立、维护组播组成员关系。
目前MLD有两个版本：MLDv1版本（由RFC2710定义）、MLDv2版本（由RFC3810定义）。
注意: 目前，系统仅支持MLDv1版本。
MLDv1版本
MLDv1的工作原理是基于查询和响应机制完成对IPv6组播组成员的管理。
MLDv1包括四种类型的报文：
l 普遍组查询报文（General Query）：查询器向共享网络上所有主机和路由器发送的查询报文，用于了解哪些组
播组存在成员。
l 特定组查询报文（Multicast Address Specific Query）：查询器向共享网段内指定组播组发送的查询报文，用
于查询该组播组是否存在成员。
l 成员报告报文（Multicast Listener Report）：主机向查询器发送的报告报文，用于申请加入某个组播组或者应
答查询报文。
l 成员离开报文（Multicast Listener Done）：主机离开组播组时主动向查询器发送的报文，用于宣告自己离开了
某个组播组。
MLDv2版本
MLDv2在MLDv1的基础上，增加了成员主机可以指定接受或不接受某些组播源的报文的功能。

<!-- 来源页 632 -->
MLDv2报文包含两大类：查询报文和成员报告报文。MLDv2没有定义专门的成员离开报文，成员离开通过
特定类型的报告报文来传达。
配置协议无关组播（PIMv6）
对IPv6 PIM-SM的配置包括基本配置以及在不同的接口上配置IPv6 PIM-SM功能。
IPv6 PIM-SM的基本信息配置包括：
l 开启/关闭组播路由功能（具体请参阅“配置IPv6静态组播路由”）
l 开启/关闭IPv6 PIM-SM功能
l 配置候选RP
l 配置候选BSR
l 配置静态RP
l 指定关闭RPT向SPT切换
配置接口的IPv6 PIM-SM功能包括：
l 开启/关闭接口的IPv6 PIM-SM功能
l 配置接口的IPv6 PIM被动模式
l 配置DR优先级
l 指定接口的Hello报文发送间隔
l 指定发送MLD主机查询报文间隔
l 指定MLD主机查询超时时间
l 指定MLD主机查询最大响应时间
配置PIMv6基本信息
IPv6 PIM-SM的基本配置
用户可以为不同的VRouter分别配置IPv6 PIM-SM。对IPv6 PIM-SM的基本配置需要在IPv6 PIM-SM模式
下进行。进入IPv6 PIM-SM配置模式，请在全局配置模式下，使用以下命令：
ip vrouter vrouter-name （进入VRouter配置模式）
ipv6 multicast-routing（开启IPv6组播路由）
ipv6 router pim（进入IPv6 PIM-SM配置模式）

<!-- 来源页 633 -->
开启/关闭IPv6 PIM-SM功能
默认情况下，IPv6 PIM-SM功能为关闭状态。在IPv6 PIM-SM配置模式下，使用以下命令开启或关闭IPv6
PIM-SM功能：
l
开启IPv6 PIM-SM：pim-sm enable
l
关闭IPv6 PIM-SM：no pim-sm enable
配置候选RP
在IPv6 PIM-SM域内选择几台PIM设备配置候选RP（Rendezvous Point, 汇聚点），从候选RP中选举产生
RP。必须同时配置候选BSR，由候选BSR（BootStrap Router, 自举路由器）选举产生BSR，BSR负责收集
并发布网络中的RP信息。
配置候选RP，在IPv6 PIM-SM配置模式下，使用以下命令：
rp-candidate ipv6-address [interval interval-time ] [priority level]
l
ipv6-address – 指定候选RP接口的IPv6地址，不可以配置为link-local地址，且该接口必须开启IPv6
PIM-SM功能。
l
interval-time – 指定发送候选RP消息的时间间隔，单位是秒。范围是1到16383秒。默认值是60秒。
l
priority level – 指定优先级（数值越小，优先级越高）。在RP选举中，优先级较高的候选RP优先被选
举为RP。范围是1到192，默认值为192。
在IPv6 PIM-SM配置模式下，使用以上命令no的形式删除配置的候选RP：
no rp-candidate
注意: 当配置候选RP时，无需指定组播地址，默认组播地址为FF00::/8。
配置候选BSR
在一个PIM-SM域中，需要配置一个或多个候选BSR，候选BSR之间通过自动选举，产生BSR，BSR负责收集
并发布RP信息。
配置候选BSR，在IPv6 PIM-SM配置模式下，使用以下命令：
bsr-candidate ipv6-address [priority level]
l
ipv6-address– 指定候选BSR接口的IPv6地址，不可以配置为link-local地址，且该接口必须开启IPv6
PIM-SM功能。

<!-- 来源页 634 -->
l
priority level – 指定优先级（数值越大，优先级越高）。如果在IPv6 PIM-SM域中，只有一个候选
BSR，即被选为BSR；如果存在多个候选BSR，在BSR选举中，优先级较高的候选BSR优先被选举为
BSR；如果优先级相同，IP地址大的会被选举为BSR。范围是0到255，默认值为0。
在IPv6 PIM-SM配置模式下，使用以上命令no的形式删除配置的候选BSR：
no bsr-candidate
注意: 当使用动态RP时，候选RP必须配置，同时，在IPv6 PIM-SM域中至少配置一个候选BSR。
配置静态RP
当网络内仅有一个RP时，用户可以配置静态RP，这样可以避免候选RP和BSR之间频繁的信息交互占用带
宽。IPv6 PIM-SM域内所有设备都必须配置完全相同的静态RP。
指定静态RP地址，在IPv6 PIM-SM配置模式下，使用以下命令：
rp-address ipv6-rp-address [ipv6_multicast_addr/length]
l
ipv6-rp-address – 指定静态RP所在接口IP地址,不可以配置为link-local地址。
l
ipv6_multicast_addr/length – 指定组播地址。
在IPv6 PIM-SM配置模式下，使用以上命令no的形式删除配置的静态RP地址：
no rp-address ipv6-rp-address[ipv6_multicast_addr/length]
指定关闭RPT向SPT切换
由于IPv6 PIM-SM域中已构建的RPT（Rendezvous Point Tree, 共享树）不一定是路径最短的树，因此当
组播数据流量变大时，RP可能会成为故障点。为了解决这个问题，在默认情况下，RPT可以向SPT
（Shortest Path Tree, 最短路径树）切换，切换到SPT后，组播数据将直接从组播源沿着SPT发送到接收
者。用户可以根据需要，指定关闭RPT向SPT切换。
RPT向SPT切换前示意图：

<!-- 来源页 635 -->
RPT向SPT切换后示意图
指定关闭默认RPT向SPT切换，在IPv6 PIM-SM配置模式下，使用以下命令：
spt-threshold infinity
在IPv6 PIM-SM配置模式下，使用以上命令no的形式恢复默认向SPT切换：
no spt-threshold infinity
配置接口的IPv6 PIM-SM功能
接口的IPv6 PIM-SM功能配置需要在接口配置模式下完成。IPv6 PIM-SM功能在设备接口上的配置包括：
l 开启/关闭接口的IPv6 PIM-SM功能
l 配置接口的IPv6 PIM被动模式
l 配置DR优先级
l 指定接口的Hello报文发送间隔
l 指定发送MLD主机查询报文间隔
l 指定MLD主机查询超时时间
l 指定MLD主机查询最大响应时间
开启/关闭接口的IPv6 PIM-SM功能
默认情况下，接口的IPv6 PIM-SM功能为关闭状态。用户可以在接口配置模式下，使用以下命令，开启或关
闭指定接口的IPv6 PIM-SM功能：
l
开启指定接口的PIM-SM功能：ipv6 pim sparse-mode
l
关闭指定接口的PIM-SM功能：no ipv6 pim sparse-mode
注意: 仅支持三层接口上开启IPv6 PIM-SM功能。

<!-- 来源页 636 -->
配置接口的IPv6 PIM被动模式
接口在开启IPv6 PIM-SM功能的情况下，如果有恶意主机模拟IPv6 PIM Hello报文，并且大量发送时，可能
导致设备瘫痪。为避免发生上述安全问题，可以为该接口开启IPv6 PIM被动模式。开启后，接口将不再接收
和转发任何IPv6 PIM报文，接口上的所有IPv6 PIM邻居都会被删除，并且该接口会自动成为DR。同时，接
口开启PIM被动模式后不会影响接口对MLD报文的处理。
开始之前
在配置接口的IPv6 PIM被动模式前，需要完成以下任务：
l
在接口配置模式下，使用ipv6 pim sparse-mode命令开启接口的IPv6 PIM-SM功能。
l
在VRouter配置模式下，使用ipv6 multicast-routing命令开启组播路由功能。
注意:
l
该功能仅适用于与用户主机网段直连的IPv6 PIM设备接口，且该网段上只能连接一台PIM设
备。
l
配置该功能后，接口将不再接收和转发任何IPv6 PIM协议报文，即该接口配置的其他IPv6 PIM
功能将失效，请谨慎使用。
l
IPv6 PIM被动模式目前暂不支持结合接口加入组播组功能实现对组播流量转发的控制。
操作步骤
默认情况下，接口的IPv6 PIM被动模式为关闭状态。开启接口的IPv6 PIM被动模式，在接口配置模式下，
使用以下命令：
ipv6 pim passive
在接口配置模式下，使用该命令no的形式将功能恢复为关闭状态：
no ipv6 pim passive
检查配置结果
配置接口的PIM被动模式后，可以在接口配置模式下，使用show this命令查看是否配置成功。
以下是配置成功的返回结果示例：
hostname(config-if-eth0/3)#show this
interface ethernet0/3
ip pim passive
exit

<!-- 来源页 637 -->
配置DR优先级
DR（Designated Router）的优先级用来决定使用哪个路由器作为指定路由器（DR）。指定DR的优先
级，在接口配置模式下，使用以下命令：
ipv6 pim dr-priority level
l
level – 指定DR的优先级（数值越大，优先级越高）。默认值是1。范围是0到4294967295。IPv6
PIM-SM域中的路由器都可指定作为DR，优先级高的路由器会被选中；如果优先级也相同，IP地址大的
会被选中。
使用no ipv6 pim dr-priority命令恢复默认优先级。
指定接口的Hello报文发送间隔
接口开启IPv6 PIM-SM功能后，会定期发送Hello报文。用户可以根据需要，指定接口的Hello报文的发送
间隔，在接口配置模式下，使用以下命令：
ipv6 pim hello-interval interval
l
interval – 指定接口的Hello报文发送间隔。范围是1到3600秒，默认值是30秒。
使用no ipv6 pim hello-interval命令恢复默认发送间隔值。
指定发送MLD主机查询报文间隔
接收者主机所在的网络可能同时连接多台组播路由器。这些组播路由器之间通过自动选举，选举出一台路由
器作为查询器，负责维护接口上的MLD组成员关系。对于设备，在接口开启IPv6 PIM-SM功能后，查询器
会主动发送的MLD主机查询报文，主机接收到该报文，会回应MLD报告该报文。
指定发送MLD主机查询报文间隔，在接口配置模式下，使用以下命令：
ipv6 pim mld query-interval interval
l
interval – 指定接口发送MLD主机查询报文间隔时间。范围是1到1800秒，默认值是125秒。
使用no ipv6 pim mld query-interval命令恢复默认报文间隔值。
指定MLD主机查询超时时间
如果网络内的组播路由器在指定超时时间内，未收到MLD主机查询消息，组播路由器将会自动选举出一台路
由器来接管查询器，负责发送主机查询消息。
指定MLD主机查询超时时间，在接口配置模式下，使用以下命令：
ipv6 pim mld query-timeout timeout-value
l
timeout-value – 指定MLD主机查询超时时间。范围是3到3620秒，默认值是260秒。

<!-- 来源页 638 -->
使用no ipv6 pim mld query-timeout命令恢复默认超时时间值。
指定MLD主机查询最大响应时间
用户可以指定接收者主机接受到通用查询消息后的最大响应时间。如果在最大响应时间内，未收到接收者主
机的响应，那么系统将会在组播路由表中删除该接收者。
指定MLD主机查询最大响应时间，在接口配置模式下，使用以下命令：
ipv6 pim mld query-max-response-time response-time
l
response-time – 指定MLD主机查询最大响应时间。范围是1到32秒，默认值是10秒。
使用no ipv6 pim mld query-max-response-time命令恢复默认最大响应时间值。
显示IPv6 PIM-SM信息
显示BSR信息，在任何模式下使用以下命令：
show ipv6 pim bsr-router[vrouter vrouter-name]
l
vrouter-name - 显示指定VRouter的BSR信息。
显示配置IPv6 PIM-SM功能接口信息，在任何模式下使用以下命令：
show ipv6 pim interface [interface-name]
l
interface-name - 显示指定接口的PIM信息。
显示IPv6 PIM邻居信息，在任何模式下使用以下命令：
show ipv6 pim neighbor [vrouter vrouter-name]
l
vrouter-name - 显示指定VRouter的IPv6 PIM邻居信息。
显示RP信息，在任何模式下使用以下命令：
show ipv6 pim rp [vrouter vrouter-name | mapping [vrouter vrouter-name]]
l
vrouter-name - 显示指定VRouter的RP信息。
l
mapping [vroutervrouter-name] - 显示指定VRouter的所有RP映射信息。
显示RPF信息，在任何模式下使用以下命令：
show ipv6 pim rpfsource-address [vrouter vrouter-name]
l
source-address – 显示指定组播源IP地址的RPF信息。
l
vrouter-name - 显示指定VRouter下的组播源IP的RPF信息。

<!-- 来源页 639 -->
显示MLD组播组信息，在任何模式下使用以下命令：
show ipv6 pim mld groups [group-address [vrouter vrouter-name]]
l
group-address – 显示指定IP地址的MLD组播组信息。
l
vrouter vrouter-name – 显示指定VRouter下的MLD组播组信息。
显示MLD接口信息，在任何模式下使用以下命令：
show ipv6 pim mld interfaces [interface-name]
l
interface-name – 显示指定接口（已开启IPv6 PIM-SM功能）的MLD信息。

<!-- 来源页 640 -->
BFD
BFD（Bidirectional Forwarding Detection，双向转发检测）提供了一种标准化、通用化的检测机制，
用于快速检测和监控网络链路或IP路由的双向转发连通性。它可以提高网络故障的检测速度，使得协议邻居
之间能够迅速识别通信故障，从而快速切换至备用路径，恢复数据转发。这有助于在网络发生故障时，实现
毫秒级的快速收敛，保障业务的连续性。
BFD在两台路由器之间建立会话，用来监测它们之间的双向通信路径是否正常，并为上层协议（如路由协
议）提供支持。BFD自身不具备自动发现对端的功能，需要靠被服务的上层协议告诉它和谁建立会话。会话
建立后，如果在检测时间内没有收到对端的BFD报文，则认为链路出现了故障，并立即通知对应的上层协
议，由上层协议进行相应的处理。
当前版本的StoneOS支持BFD与静态路由、OSPF、BGP路由协议联动，实现在运行静态路由、OSPF、BGP
路由协议的链路上进行转发连通状况检测。
BFD工作模式
BFD会话建立有两种模式：主动模式和被动模式。目前只支持主动模式，不支持被动模式。
l 主动模式：在建立会话前不管是否收到对端发来的BFD控制报文，都会主动发送BFD控制报文。
l 被动模式：在建立会话前不会主动发送BFD控制报文，直到收到对端发送来的控制报文。在会话初始化过程中，
通信双方至少要有一个运行在主动模式才能成功建立起会话。
BFD会话建立后有两种检测模式：异步模式和查询模式。通信双方要求运行在相同的模式。
l 异步模式：以异步模式运行的设备周期性地发送BFD控制报文，如果在检测时间内对端没有收到BFD控制报文，
则认为链路故障，BFD会话不可用。
l 查询模式：以查询模式运行的设备不会周期性的发送BFD控制报文，而是在需要检测连通性时，发送一个查询报
文，如果在检测时间内本端设备没有收到对端发送的回应报文，则认为链路故障，BFD会话不可用。
BFD Echo功能
BFD Echo功能即BFD回声功能，本端设备周期性地发送BFD Echo报文，远端设备不对报文进行处理，只通
过转发通道将报文返回到本端。通过Echo功能，可以更快的检测故障。
Echo功能可以和两种检测模式配合使用，如果在异步模式下启用Echo功能，可以减少控制报文的发送；如
果在查询模式下启用Echo功能，在BFD会话建立后可以取消发送BFD控制报文。

<!-- 来源页 641 -->
注意: 若需要使用Echo功能，在本端设备开启Echo功能的基础上，对端设备必须能够对Echo报文
进行转发，否则Echo功能不生效。
BFD配置流程
BFD可以进行单跳检测和多跳检测，用户可根据组网环境自行选择。
l 单跳检测：指对两个直连设备进行IP连通性检测，这里所说的“单跳”是IP的一跳。
l 多跳检测：指对两个非直连设备间任意路径的链路连通情况进行检测。
单跳检测配置流程
配置BFD单跳检测，建议用户按照以下步骤进行操作：
1. 配置接口的BFD参数：根据组网环境配置相关接口的BFD参数，详情请参见“配置接口”章节。
2. （按需）配置Echo功能：BFD Echo功能适用于对端设备无法支持BFD协议的场景。用户可根据需求进行配置。
3. 配置BFD与路由联动：在路由协议中开启并配置BFD功能，建立BFD与路由联动，实现链路故障时快速触发路由
收敛，保障网络的稳定性。
注意: 若不配置Echo功能，则需两端设备均启用并配置BFD功能；若配置Echo功能，则仅需本端
启用并配置BFD功能。
多跳检测配置流程
目前BFD多跳检测仅支持与BGP路由进行联动。用户需在两端设备中均启用并配置BFD功能，以实现BFD多
跳检测，其配置流程如下：
1. 配置BFD多跳检测模板：新建多跳检测模板，并指定BFD控制报文的加密认证方式、最小发送间隔、检测时间倍
数等参数。
2. 配置BFD与BGP路由联动：在BGP路由协议中绑定已配置的BFD多跳检测模板，建立BFD与BGP路由联动，实现
毫秒级链路故障检测，增强BGP协议的收敛性能。
注意: BFD多跳会话检测仅支持异步模式，不支持查询模式和Echo功能。
配置BFD基本功能
BFD基本功能的配置包括以下各项：

<!-- 来源页 642 -->
l 配置BFD检测模式
l 配置BFD会话参数
l 开启/关闭Echo功能
l 指定接收Echo报文时间间隔
l 配置Echo报文的源IP地址
l 配置BFD多跳检测
l 调整BFD规格
l 显示BFD会话信息
配置BFD检测模式
BFD会话建立后有两种检测模式：异步模式和查询模式。通信双方要求运行在相同的模式。默认情况下，
BFD会话的检测模式为异步模式。用户可以根据需要指定BFD会话检测模式为查询模式，在接口配置模式
下，使用以下命令：
bfd demand enable
在接口配置模式下使用该命令no的形式恢复默认为异步模式：
no bfd demand enable
配置BFD会话参数
在BFD会话建立之后，用户可以根据需要修改发送或接收BFD会话报文的最小时间间隔以及检测时间倍数。
配置BFD会话检测参数，在接口配置模式下，使用以下命令：
bfd min-tx min-tx-value min-rx min-rx-value detect-multiplier value
l
min-tx-value – 指定发送BFD报文的最小时间间隔，单位是毫秒。默认值为100，取值范围为100到
1000。
l
min-rx-value – 指定接收BFD报文的最小时间间隔，单位是毫秒。默认值为100，取值范围为100到
1000。
l
value– 指定检测时间倍数，用来计算检测超时时间。
使用no bfd min-tx min-rx detect-multiplier恢复默认BFD会话参数。

<!-- 来源页 643 -->
注意: 检测超时时间计算方法如下：
l
异步模式：超时时间= max(本端配置的min-tx-value,对端配置的min-rx-value)* 对端检测
时间倍数。
l
查询模式下并开启Echo功能：超时时间= max(本端配置的min-tx-value,对端配置的接收
Echo报文时间间隔)* 本端检测时间倍数。
l
异步模式下并开启echo功能：超时时间= max(本端配置的min-tx-value,对端配置的接收
Echo报文时间间隔)* 对端检测时间倍数
以异步模式下开启Echo功能为例：当本端配置的BFD最小报文发送间隔为200ms、对端配置
的接收Echo报文时间间隔为100ms、对端检测时间倍数为3。超时时间计算方式为：本端配置
的BFD最小报文发送间隔*对端检测时间倍数=200*3=600ms。
关于如何配置接收Echo报文时间间隔，请参阅“指定接收Echo报文时间间隔”。
开启/关闭Echo功能
默认情况下，Echo功能是关闭的，启用此功能，在接口配置模式下，使用以下命令：
bfd echo enable
在接口配置模式下，用该命令no的形式关闭此功能：
no bfd echo enable
指定接收Echo报文时间间隔
指定接收BFD Echo报文时间间隔，在接口配置模式下，使用以下命令：
bfd min-echo-rx value
l
value – 指定接收BFD Echo报文时间间隔，单位为毫秒。取值范围是100到1000毫秒。默认为0，即表
示不接收BFD Echo报文。
在接口配置模式下，使用no bfd min-echo-rx命令恢复默认值。
配置Echo报文的源IP地址
为了避免对端发送大量的ICMP重定向报文造成网络拥塞，用户需要配置Echo报文的源IP地址，在全局配置
模式下，使用以下命令：
bfd echo-source-ip echo-src-address
l
echo-src-address – 指定BFD Echo报文的源IP地址。

<!-- 来源页 644 -->
在全局配置模式下，使用no bfd echo-source-ip命令删除Echo报文的源IP地址。
注意:
l
Echo报文的源IP地址用户可以任意指定。建议用户配置Echo报文的源IP地址不属于该设备任
何一个接口所在网段。
l
本端发送Echo报文的目的地址使用本端接口地址。
配置BFD多跳检测
多跳检测指对两个非直连设备间任意路径的链路连通情况进行检测。目前BFD多跳检测仅支持与BGP路由进
行联动。用户需在两端设备中均启用并配置BFD功能，以实现BFD多跳检测，配置流程请参见多跳检测配置
流程。
创建BFD多跳检测模板
BFD多跳检测模板用于指定BFD控制报文的加密认证方式、发送或接收BFD多跳会话报文的最小时间间隔以
及检测时间倍数。创建BFD多跳检测模板，在全局配置模式下使用以下命令：
bfd template template-name multi-hop
l
template-name - 指定所创建的BFD多跳检测模板的名称，并且进入该BFD多跳检测模板配置模式。
如果指定名称已存在，则直接进入BFD多跳检测模板配置模式。
使用no bfd template template-name删除指定的BFD多跳检测模板。
指定BFD控制报文的加密认证方式
随着网络跳数的增多，BFD控制报文可能更加容易被篡改，在BFD多会话中，支持对BFD控制报文进行加密
认证。指定BFD控制报文的加密认证方式，在BFD多跳检测模板配置模式下，使用以下命令：
authentication-type {m-md5 | m-sha1 | md5 | sha1 | simple} key-id {plain plain-string}
l
m-md5 | m-sha1 | md5 | sha1 | simple - 指定所采用的认证算法：Meticulous MD5算法（mmd5）、Meticulous SHA1算法（m-sha1）、MD5算法（md5）、SHA1算法（sha1）以及简单认
证（simple）。
l
key-id – 指定认证ID。
l
plain plain-string – 以明文的方式指定密钥。
在BFD多跳检测模板配置模式下，使用no authentication-type删除配置的BFD控制报文加密方式。

<!-- 来源页 645 -->
配置BFD多跳会话参数
在BFD多跳会话建立之后，用户可以根据需要修改发送或接收BFD多跳会话报文的最小时间间隔以及检测时
间倍数。配置BFD会话检测参数，在BFD多跳检测模板配置模式下，使用以下命令：
interval min-tx min-tx-value min-rx min-rx-value detect-multiplier value
l
min-tx-value – 指定发送BFD多跳会话报文的最小时间间隔，单位是毫秒。默认值为100，取值范围为
100到1000。
l
min-rx-value – 指定接收BFD多跳会话报文的最小时间间隔，单位是毫秒。默认值为100，取值范围为
100到1000。
l
detect-multiplier value – 指定检测时间倍数，用来计算检测超时时间。默认值为3，取值范围是3到
50。
l
在BFD多跳检测模板配置模式下，使用no interval min-tx min-rx detect-multiplier恢复默认BFD
多跳会话参数。
注意: BFD多跳检测超时时间计算方法如下：
l
异步模式：超时时间= max(本端配置的min-tx-value,对端配置的min-rx-value)* 对端检测
时间倍数。
示例：
当本端配置的BFD最小报文发送间隔为100ms，对端配置的BFD最小报文接收间隔为200ms，对
端检测超时倍数为3时。超时时间的计算方式为：对端配置的BFD最小报文接收间隔*对端检测超时
倍数=200*3=600ms。
调整BFD规格
系统支持动态调整BFD规格，在全局配置模式下使用以下命令：
capacity maxium_bfd_session_num number
l
number – 指定调整后的BFD规格值。可配置的BFD规格值，下限为设备默认的BFD规格值，上限为该
默认值的2倍。用户可通过Tab键联想获取可配置的最大值，联想后会显示<1-max>，其中“max”即
为当前设备支持的BFD规格最大可配置值。
BFD规格调整后，需重启设备，配置才能生效。设备重启后，在任意模式下，使用show capacity
dynamic命令，查看当前系统已修改的规格参数，并验证修改后的BFD规格是否生效。

<!-- 来源页 646 -->
显示BFD会话信息
显示BFD会话信息，在任何模式下使用以下命令：
show bfd session [interface interface-name | neighbor A.B.C.D | detail ]
l
interface interface-name - 显示指定接口的BFD会话信息。
l
A.B.C.D – 指定相邻路由器的ID。
l
detail – 显示所有路由器的BFD会话详细信息。
配置BFD与路由协议联动
BFD与路由协议联动的配置包括以下各项：
l 配置BFD与静态路由联动
l 配置BFD与OSPF联动
l 配置BFD与BGP联动
l 配置BFD与IS-IS联动
配置BFD与静态路由联动
由于静态路由没有发现邻居机制，BFD与静态路由联动，如果BFD会话检测到故障，则表明该静态路由下一
跳不可达，即不会添加此路由到路由表中，从而实现快速路由选路。
配置BFD与静态路由联动，对指定的静态路由下一跳开启BFD检测功能，在VRouter配置模式下，使用以下
命令：
ip route {A.B.C.D/M | A.B.C.D A.B.C.D} interface-name A.B.C.D bfd
l
A.B.C.D/M | A.B.C.D A.B.C.D – 指定静态路由条目的网络地址。设备支持两种配置方式，A.B.C.D/M
或者A.B.C.D A.B.C.D，例如1.1.1.0/24或者1.1.1.0 255.255.255.0。
l
interface-name A.B.C.D – 指定下一跳接口地址。
l
bfd – 对指定下一跳开启BFD检测功能。
在VRouter配置模式下，使用以上命令no的形式取消BFD与指定静态路由联动：
no ip route {A.B.C.D/M | A.B.C.D A.B.C.D} interface-name A.B.C.D bfd
配置BFD与OSPF联动
通过BFD与OSPF联动，实现优于OSPF协议Hello检测机制的快速链路检测，从而提高OSPF协议的收敛性
能。

<!-- 来源页 647 -->
配置BFD与OSPF联动，对指定的OSPF相关接口上开启BFD检测功能，在接口配置模式下，使用以下命令：
ip ospf bfd
在接口配置模式下，使用以上命令no的形式取消BFD与OSPF联动：
no ip ospf bfd
配置BFD与BGP联动
配置BFD与BGP联动，对指定的BGP邻居开启BFD检测功能，在BGP实例配置模式下，使用以下命令：
neighbor A.B.C.D fall-over bfd [multi-hop bfd-template-name]
l
A.B.C.D – 指定BGP对等体的IP地址。
l
multi-hop bfd-template-name – 当使用多跳检测方式时，指定BFD多跳检测模板名称以绑定该模
板。如果不指定该参数，即使用单跳检测方式。
在BGP实例配置模式下，使用以上命令no的形式取消BFD与指定BGP邻居联动：
no neighbor A.B.C.D fall-over bfd
配置BFD与IS-IS联动
通过BFD与IS-IS联动，配合IS-IS协议更快的发现邻接方面出现的故障，从而实现路由的快速收敛。
配置BFD与IS-IS联动，对指定的IS-IS相关接口上开启BFD检测功能，在接口配置模式下，使用以下命令：
isis bfd
在接口配置模式下，使用以上命令no的形式取消BFD与IS-IS联动：
no isis bfd

<!-- 来源页 648 -->
MPLS
MPLS（Multiprotocol Label Switching）是一种基于标签进行报文转发的技术。标签是一个具有固定长
度的本地标识符，封装于链路层和网络层之间，用于标识一个报文所属的FEC（Forwarding Equivalent
Class），使一组报文可以按照同一种方式转发，例如通过同一条路径或者经过同样的转发处理。对于携带
MPLS标签的报文，只需要基于标签的查找和替换来转发，而不需要像在传统的IP转发技术中基于目的IP地
址进行转发。
MPLS网络以LSR（Label Switching Router）为基本组成单元。位于MPLS网络边缘的LSR用于和非MPLS
网络连接，称为LER（Label Edge Router）。当一个IP报文进入MPLS网络时，入口LER会对IP报文的首
部进行分析，并为IP包添加标签后转发到下一跳，后续的所有MPLS网络中的节点都会依据收到的报文的标
签进行转发，不会再对IP首部做分析，直到离开MPLS网络前由出口LER删除标签.
在MPLS网络中，当StoneOS设备基于二层安全域部署时，支持对MPLS报文做解封装，然后将获取到的IP报
文发送给相应的业务模块进行安全控制。完成处理后，再重新封装上之前剥掉的标签再透传给其他LSR。
MPLS解封装支持最多5层标签，超过5层标签的MPLS报文会被视为非IP报文，根据l2-nonip-action命令
的配置进行处理。
开启/关闭MPLS报文安全控制功能
MPLS报文安全控制功能默认为关闭。开启该功能，在VSwitch配置模式（通过vswitch vswitchNumber
命令进入）下使用以下命令：
mpls-tunnel-inspection-enable
关闭该功能，在VSwitch配置模式下使用以下命令：
no mpls-tunnel-inspection-enable
开启/关闭MPLS调试功能
开启MPLS调试功能，在任何模式下使用以下命令：
debug dp mpls {basic | error}
l
basic - 开启MPLS基本信息调试。
l
error - 开启MPLS错误信息调试。
开启MPLS调试功能，在任何模式下使用以下命令：
undebug dp mpls {basic | error}

<!-- 来源页 649 -->
l
basic - 关闭MPLS基本信息调试。
l
error - 关闭MPLS错误信息调试。

<!-- 来源页 650 -->
路由配置举例
本节介绍路由相关配置举例，包括：
l "例：开启/关闭静态路由查询功能配置举例" 在第648页
l "多VR配置举例" 在第649页
l "例：静态组播路由配置举例" 在第653页
l "BFD配置举例" 在第655页
l "例：IGMP Proxy配置举例" 在第659页
l "例：IGMP Snooping配置举例" 在第661页
l "例：PIM-SM配置举例" 在第663页
l "例：Web视频引流配置案例" 在第665页
例：开启/关闭静态路由查询功能配置举例
设备的ethernet0/0和ethernet0/1两个接口分别连接网通和电信的两条线路，内网中Trust域和Trust1域
的流量走网通线路，其它的流量走电信线路。组网图如下图所示：
如上图所示，接口etherent0/0和ethernet0/1属于untrust域，IP地址分别是202.10.11.2和
202.10.10.2，接口etherent0/2和ethernet0/3属于Ttrust域，IP地址分别是202.10.2.1/24和
202.10.3.1/24，接口etherent0/4和ethernet0/5属于Ttrust1域，IP地址分别是202.10.4.1/24和

<!-- 来源页 651 -->
202.10.5.1/24，接口etherent0/6、ethernet0/7和etherent0/8属于Ttrust2域，IP地址分别是
202.10.6.1/24、202.10.7.1/24和202.10.8.1/24。
配置步骤
以下配置步骤略去安全域以及接口配置，重点描述路由配置。路由配置：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 0.0.0.0/0 202.10.10.2（默认流量走电信）
hostname(config-vrouter)# ip route source 202.10.2.1/24 202.10.11.2（该网段流量走网
通）
hostname(config-vrouter)# ip route source 202.10.3.1/24 202.10.11.2（该网段流量走网
通）
hostname(config-vrouter)# ip route source 202.10.4.1/24 202.10.11.2（该网段流量走网
通）
hostname(config-vrouter)# ip route source 202.10.5.1/24 202.10.11.2（该网段流量走网
通）
根据以上源路由配置，Trust和Trust1域的流量都走网通线路，而其它的流量走电信线路。如果由于某些原
因，网通线路故障，Trust和Trust1域的用户将无法上网，此时需要将以上的四条源路由删除，流量才会全
部汇总到电信线路进行传输。如果相关的源路由很多，删除工作和线路故障排除后的路由添加工作的工作量
将十分庞大，同时也容易出错。现在的解决方案是：线路故障时，关闭源路由的查询，Trust和Trust1域的
用户就都可以走默认路由通过电信线路上网。配置命令如下：
hostname(config)# route disable sbr
故障排除后，重新开启源路由的查询功能：
hostname(config)# route enable sbr
多VR配置举例
提示: 本示例所展示的操作步骤，基于StoneOS 5.5R11版本进行配置。若有变动，请以实际页面
为准。
本节介绍几个多VR配置的具体实例，包括
l 多VR独立转发
l 跨VR转发

<!-- 来源页 652 -->
多VR独立转发
Trust-vr和VR1两个VR中有重叠的IP地址段，但是要求两个VR的数据转发各自进行，互不影响。组网图如下
图所示：
系统有两个VR，分别是trust-vr和VR1。接口ethernet0/1属于zone1，ethernet0/2属于zone2，
zone1和zone2均属于trust-vr；接口ethernet0/3属于zone3，ethernet0/4属于zone4，zone3和
zone4均属于VR1。接口ethernet0/1和ethernet0/3的IP地址重叠，而ethernet0/2和ethernet0/4的IP
地址也重叠。
配置步骤
第一步：开启Hillstone设备的多VR功能：
hostname# exec vrouter enable
Warning: please reboot the device to make the change validation!
hostname# reboot
System reboot, are you sure? y/[n]: y
第二步：重启设备后，创建VR1：
hostname(config)# ip vrouter VR1
第三步：配置接口以及安全域（zone1和zone2默认属于trust-vr）：
hostname(config)# zone zone1
hostname(config-zone-zone1)# exit
hostname(config)# zone zone2
hostname(config-zone-zone2)# exit
hostname(config)# zone zone3

<!-- 来源页 653 -->
hostname(config-zone-zone3)# vrouter VR1
hostname(config-zone-zone3)# exit
hostname(config)# zone zone4
hostname(config-zone-zone4)# vrouter VR1
hostname(config-zone-zone4)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone zone1
hostname(config-if-eth0/1)# ip address 10.1.1.1/24
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# zone zone2
hostname(config-if-eth0/2)# ip address 10.1.2.1/24
hostname(config-if-eth0/2)# exit
hostname(config)# interface ethernet0/3
hostname(config-if-eth0/3)# zone zone3
hostname(config-if-eth0/3)# ip address
10.1.1.1/24
hostname(config-if-eth0/3)# exit
hostname(config)# interface ethernet0/4
hostname(config-if-eth0/4)# zone zone3
hostname(config-if-eth0/4)# ip address 10.1.2.1/24
hostname(config-if-eth0/4)# exit
hostname(config)#
跨VR转发
系统有两个VR，即trust-vr和VR1。要求实现trust-vr通过VR1进行数据转发。组网图如下图所示：

<!-- 来源页 654 -->
系统有两个VR，分别是trust-vr和VR1。接口ethernet0/1属于zone1，zone1属于VR1；接口
ethernet0/2和ethernet0/3属于zone2，zone2属于trust-vr。通过配置，实现trust-vr通过VR1进行数
据转发。
配置步骤
第一步：开启设备的多VR功能：
hostname# exec vrouter enable
Warning: please reboot the device to make the change validation!
hostname# reboot
System reboot, are you sure? y/[n]: y
第二步：重启设备后，创建VR1：
hostname(config)# ip vrouter VR1
第三步：配置接口以及安全域（zone2默认绑定到trust-vr中）：
hostname(config)# zone zone1
hostname(config-zone-zone1)# vrouter VR1
hostname(config-zone-zone1)# exit
hostname(config)# zone zone2
hostname(config-zone-zone2)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone zone1
hostname(config-if-eth0/1)# ip address 1.1.1.1/24
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/2

<!-- 来源页 655 -->
hostname(config-if-eth0/2)# zone zone2
hostname(config-if-eth0/2)# ip address 10.1.1.1/24
hostname(config-if-eth0/2)# exit
hostname(config)# interface ethernet0/3
hostname(config-if-eth0/3)# zone zone2
hostname(config-if-eth0/3)# ip address 10.1.2.1/24
hostname(config-if-eth0/3)# exit
hostname(config)#
第四步：配置跨VR转发路由：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 0.0.0.0/0 vrouter VR1
hostname(config-vrouter)# exit
hostname(config)# ip vrouter VR1
hostname(config-vrouter)# ip route 10.1.1.0/24 vrouter trust-vr
hostname(config-vrouter)# ip route 10.1.2.0/24 vrouter trust-vr
hostname(config-vrouter)# exit
hostname(config)#
例：静态组播路由配置举例
组播源发送数据至组播组，组播地址为224.91.91.2。接口ethernet0/0属于trust安全域，为组播数据入接
口；接口ethernet0/1属于untrust安全域，为组播数据出接口。配置静态组播路由使组播数据可以正常转
发给属于组播组的客户端PC。组网图如下图所示：

<!-- 来源页 656 -->
配置步骤
第一步：配置接口和安全域：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 1.1.1.1/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 2.1.1.1/24
hostname(config-if-eth0/1)# exit
hostname(config)#
第二步：配置并开启静态组播功能：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip multicast-routing
hostname(config-vrouter)# ip mroute 1.1.1.2 224.91.91.2 iif ethernet0/0 eif
ethernet0/1
hostname(config-vrouter)# exit
hostname(config)#
第三步：配置策略：
hostname(config)# address src

<!-- 来源页 657 -->
hostname(config-addr)# ip 1.1.1.2/32
hostname(config-addr)# exit
hostname(config)# address dst
hostname(config-addr)# ip 224.91.91.2/32
hostname(config-addr)# exit
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# src-addr src
hostname(config-policy-rule)# dst-addr dst
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
BFD配置举例
提示: 本示例所展示的操作步骤，基于StoneOS 5.5R11版本进行配置。若有变动，请以实际页面
为准。
本节列举3个BFD的配置实例，分别是：
l BFD与静态路由联动配置举例
l BFD与OSPF联动配置举例
l BFD与BGP联动配置举例
组网需求
两台防火墙和两台路由器组成一个冗余链路，路由器与防火墙之间采用BFD检测。Router1可达网段为
100.1.1.1/24。以Router1与防火墙A之间的配置为例，介绍BFD与静态路由、OSPF、BGP联动的配置。
组网图如下图所示：

<!-- 来源页 658 -->
配置步骤
BFD与静态路由联动配置
第一步：配置防火墙A的接口。
防火墙A
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone untrust
hostname(config-if-eth0/0)# ip address 1.1.1.1/24
hostname(config-if-eth0/0)# exit
hostname(config)#
第二步：在防火墙A的接口上配置BFD会话参数。检测模式默认为异步模式。
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# bfd min-tx 100 min-rx 100 detect-multiplier 3
hostname(config-if-eth0/0)# exit

<!-- 来源页 659 -->
hostname(config)#
第三步：在防火墙A上配置BFD与静态路由Router1联动。
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 100.1.1.1/24 ethernet0/0 1.1.1.2 bfd
hostname(config-vrouter)# exit
hostname(config)#
第四步：配置Router1的接口以及BFD基本功能。接口地址1.1.1.2/24。
BFD与OSPF联动配置
第一步：配置防火墙A的接口。
防火墙A
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone untrust
hostname(config-if-eth0/0)# ip address 1.1.1.1/24
hostname(config-if-eth0/0)# exit
hostname(config)#
第二步：在防火墙A的接口上配置BFD会话参数。检测模式指定为查询模式并开启Echo功能，以及配置BFD
与OSPF联动。
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# bfd demand enable
hostname(config-if-eth0/0)# bfd echo enable
hostname(config-if-eth0/0)# bfd min-echo-rx 100
hostname(config-if-eth0/0)# ip ospf bfd
hostname(config)#
第三步：在防火墙A上配置OSPF协议。
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# router ospf
hostname(config-router)# router-id 1.1.1.1

<!-- 来源页 660 -->
hostname(config-router)# network 1.1.1.1/24 area 0
hostname(config-router)# exit
hostname(config)#
第四步：配置Router1的接口、BFD基本功能以及OSPF协议。接口地址1.1.1.2/24，检测模式指定为查询
模式并开启Echo功能，且需要能够对Echo报文进行转发。
BFD与BGP联动配置
第一步：配置防火墙A的接口。
防火墙A
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone untrust
hostname(config-if-eth0/0)# ip address 1.1.1.1/24
hostname(config-if-eth0/0)# exit
hostname(config)#
第二步：在防火墙A的接口上配置BFD会话参数。检测模式指定为查询模式并开启Echo功能。
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# bfd demand enable
hostname(config-if-eth0/0)# bfd min-echo-rx 100
hostname(config-if-eth0/0)# bfd echo enable
hostname(config-if-eth0/0)# exit
hostname(config)#
第三步：在防火墙A上配置BGP协议以及配置BFD与BGP联动。
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# router bgp 100
hostname(config-router)# router-id 1.1.1.1
hostname(config-router)# neighbor 1.1.1.2 fall-over bfd
hostname(config-router)# network 1.1.1.1/24
hostname(config-router)# exit
hostname(config)#

<!-- 来源页 661 -->
第四步：配置Router1的接口、BFD基本功能以及BGP协议。接口地址1.1.1.2/24，检测模式指定为查询模
式并开启Echo功能，且需要能够对Echo报文进行转发。
例：IGMP Proxy配置举例
组播源发送数据至组播组，组播地址为224.91.91.2。ethernet0/0为上行接口，ethernet0/1和
ethernet0/2为下行接口。配置IGMP Proxy使组播数据可以正常转发给属于组播组的客户端PC。组网图如
下图所示：
配置步骤
第一步：配置接口和安全域：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone untrust
hostname(config-if-eth0/0)# ip address 10.0.0.2/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone trust
hostname(config-if-eth0/1)# ip address 192.168.0.1/24
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# zone trust
hostname(config-if-eth0/2)# ip address 192.168.1.1/24

<!-- 来源页 662 -->
hostname(config-if-eth0/2)# exit
hostname(config)#
第二步：开启组播路由功能：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip multicast-routing
hostname(config-vrouter)# exit
hostname(config)#
第三步：开启并配置IGMP Proxy功能：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip igmp-proxy enable
hostname(config-vrouter)# exit
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# ip igmp-proxy host-mode
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# ip igmp-proxy router-mode
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# ip igmp-proxy router-mode
hostname(config-if-eth0/2)# exit
hostname(config)#
第四步：配置策略：
hostname(config)# address src
hostname(config-addr)# ip 1.1.1.2/32
hostname(config-addr)# exit
hostname(config)# address dst
hostname(config-addr)# ip 224.91.91.2/32
hostname(config-addr)# exit

<!-- 来源页 663 -->
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr src
hostname(config-policy-rule)# dst-addr dst
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
例：IGMP Snooping配置举例
组播源发送数据至组播组，组播地址为224.91.91.2。设备工作在透明模式，ethernet0/0为上行接口，
ethernet0/1和ethernet0/2为下行接口。配置IGMP Snooping使组播数据可以正常转发给属于组播组的
客户端PC。
配置步骤
第一步：配置接口和安全域：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone l2-untrust
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone l2-trust
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# zone l2-trust
hostname(config-if-eth0/2)# exit
hostname(config)# interface vswitchif1
hostname(config-if-vsw1)# ip address 192.30.1.100 255.255.255.0

<!-- 来源页 664 -->
hostname(config-if-vsw1)# exit
hostname(config)#
第二步：开启组播路由功能：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip multicast-routing
hostname(config-vrouter)# exit
hostname(config)#
第三步：开启并配置IGMP Snooping功能：
hostname(config)# vswitch vswitch1
hostname(config-vswitch)# ip igmp-snooping enable
hostname(config-vswitch)# exit
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# ip igmp-snooping host-mode
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# ip igmp-snooping router-mode
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# ip igmp-snooping router-mode
hostname(config-if-eth0/2)# exit
hostname(config)#
第四步：配置策略：
hostname(config)# address src
hostname(config-addr)# ip 1.1.1.2/32
hostname(config-addr)# exit
hostname(config)# address dst
hostname(config-addr)# ip 224.91.91.2/32
hostname(config-addr)# exit

<!-- 来源页 665 -->
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone l2-untrust
hostname(config-policy-rule)# dst-zone l2-trust
hostname(config-policy-rule)# src-addr src
hostname(config-policy-rule)# dst-addr dst
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
例：PIM-SM配置举例
本节介绍一个PIM-SM的配置举例。
组网需求
组播源发送数据至组播组，组播地址为224.91.91.2。接收者PC通过组播方式接收组播数据，整个PIM域采
用SM模式。假设设备作为候选RP，接口loopback1作为选举RP的接口，接口ethernet0/0作为组播数据入
接口；接口ethernet0/1作为组播数据出接口。通过配置PIM-SM功能使组播数据可以正常转发给接收者
PC。
PIM-SM配置举例组网图

<!-- 来源页 666 -->
配置步骤
第一步：开启组播路由功能。
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip multicast-routing
hostname(config-vrouter)# exit
hostname(config)#
第二步：开启并配置PIM-SM功能：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter))# router pim
hostname(config-vrouter)# pim-sm enable
hostname(config-vrouter)# rp-candidate loopback1
hostname(config-vrouter)# bsr-candidate loopback1
hostname(config-vrouter))# exit
hostname(config)#
第三步：配置接口并开启该接口的PIM-SM功能：
hostname(config)# interface loopback1
hostname(config-if-loo1))# zone trust
hostname(config-if-loo1)# ip address 2.2.2.2/24
hostname(config-if-loo1)# ip pim sparse-mode
hostname(config-if-loo1))# exit
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone untrust
hostname(config-if-eth0/0)# ip address 1.1.1.2/24
hostname(config-if-eth0/0)# ip pim sparse-mode
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone trust
hostname(config-if-eth0/1)# ip address 2.1.1.2/24

<!-- 来源页 667 -->
hostname(config-if-eth0/1)# ip pim sparse-mode
hostname(config-if-eth0/1)# exit
hostname(config)#
例：Web视频引流配置案例
设备部署在互联网入口处，ethernet0/0接口连接PC，ethernet0/2和ethernet0/3两个接口分别连接电
信和网通的两条线路。配置DNS重定向和PBR策略之后，匹配到默认路由的流量将从ethernet0/2接口出
去，匹配到策略路由的流量（如优酷）从ethernet0/3接口出去。组网图如下图所示：
配置如下：
第一步：配置接口和安全域：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 192.168.1.1/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# zone dmz

<!-- 来源页 668 -->
hostname(config-if-eth0/2)# ip address 10.180.41.52/20
hostname(config-if-eth0/2)# exit
hostname(config)# interface ethernet0/3
hostname(config-if-eth0/3)# zone dmz
hostname(config-if-eth0/3)# ip address 172.31.1.240/24
hostname(config-if-eth0/3)# exit
hostname(config)#
第二步：配置策略：
hostname(config)# rule id 1 from any to any service any permit
第三步：创建SNAT：
hostname(config)# nat
hostname(config-nat)# snatrule from any to any service any trans-to eif-ip mode
dynamicport
第四步：配置默认路由：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 0.0.0.0/0 10.180.32.1
第五步：配置策略路由并绑定接口：
hostname(config)# pbr-policy test
hostname(config-pbr)# match top any any any YOUKU-DNS nexthop 172.31.1.1
Match id 1 is created.
hostname(config-pbr)# match id 1
hostname(config-pbr-match)# application YOUKU
hostname(config-pbr-match)# application RTMFP
hostname(config-pbr-match)# exit
hostname(config-pbr)# exit
hostname(config)# exit
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# bind pbr-policy test

<!-- 来源页 669 -->
hostname(config-if-eth0/0)# exit
第六步：配置ISP路由：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route China-netcom 172.31.1.1
hostname(config-vrouter)# exit
第七步：升级APP特征库：
hostname(config)# exec app update professional
第八步：开启应用识别
hostname(config)# zone trust
hostname(config-zone-trust)# application-identify
第九步：开启DNS重定向，并配置DNS服务器IP地址：
hostname(config)# app cache dns-redirect enable
Please specify the IP address for the DNS server
hostname(config)# ip name-server 58.240.57.33
