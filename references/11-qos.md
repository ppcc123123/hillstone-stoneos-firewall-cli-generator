# 流量管理(QoS)

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 14 流量管理
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 1976 -->
14 流量管理
本章包含以下内容：
l iQoS：介绍了iQoS的实现机制、智能流量管理的处理流程、管道的概念及如何配置iQoS等。
l QoS：介绍了QoS的实现原理（包括分类和标记、管制和整形、拥塞管理和避免等）、多层QoS、弹性QoS、如
何配置QoS以及相关的配置举例等。
l 负载均衡：介绍了"服务器负载均衡" 在第2056页和"链路负载均衡" 在第2062页的概念及配置方法。
l 会话限制：介绍了会话限制的相关概念及配置方法。

<!-- 来源页 1977 -->
智能流量管理（iQoS）/QoS管理
注意:
l
如果用户在升级到5.5版本前已经配置了旧版QoS功能，则旧版QoS在升级后生效，无对应的
WebUI，需要在CLI中进行配置；iQoS功能将在WebUI上隐藏且不生效。
l
如果用户在升级到5.5版本前，没有配置旧版QoS功能，在升级后，将默认启动iQoS功能，可
在WebUI进行配置。此时，旧版QoS功能不生效。
l
旧版QoS功能配置方法，请参阅《StoneOS命令行手册》。
本章内容包含智能流量管理（iQoS）和QoS管理，与产品版本的具体关系如下表所示，请根据购买的产品版
本参见对应的手册说明。iQoS/QoS与产品版本对应关系如下：
产品版本
说明
5.5前的版本，没有配置QoS管理功能
升级后，系统默认使用iQoS管理功能。
5.5前的版本，已配置QoS管理功能
升级后，QoS管理功能仍然生效。建议用户使用iQoS管理功能，
iQoS支持原QoS的所有功能，切换到iQoS管理功能的方法，请参见
切换QoS/iQoS。
5.5版本和5.5后的版本
系统默认使用iQoS管理功能。
切换QoS/iQoS
如果用户使用的是5.5前的版本，没有配置QoS管理功能，系统升级后默认使用iQoS管理功能，可在WebUI
及CLI中进行配置。此时，QoS管理功能不生效。
从QoS切换到iQoS管理功能
如果用户在使用的是5.5前的版本，已经配置了QoS管理功能，系统升级后默认使用QoS管理功能，但只支
持在CLI中进行配置。建议用户使用iQoS，iQoS包括QoS的所有功能，从QoS切换到iQoS管理功能，在任
意模式下，使用如下命令：
exec iqos enable
从iQoS切换到QoS管理功能
若需要从iQoS切换到QoS管理功能，用户可以在任意模式下，使用如下命令：
exec iqos disable

<!-- 来源页 1978 -->
iQoS介绍
随着网络应用的快速发展以及网民数量的增加，网络带宽的压力也与日俱增，这导致企事业单位包括运营商
都面临着网络拥堵和带宽资源有效利用的问题。设备提供的iQoS（智能流量管理）功能，能够保障和管理优
化重要带宽，提高用户的网络体验和带宽资源利用率。
iQoS为特定流量提供更高优先服务的同时控制抖动和延迟的能力，并且能够降低数据传输丢包率。当网络过
载或拥塞时，系统能够确保重要业务流量的正常传输。iQoS功能受许可证控制，安装许可证后，iQoS功能
才可使用。
实现机制
数据包进入系统后，首先会被分类和标记。对于分类标记后的流量，系统会通过整形机制使流量平滑的转发
或管制机制丢弃。若选择整形机制转发流量，系统则会通过拥塞管理机制和拥塞避免机制对数据包进行管
理，为数据包排列优先次序并且在发生拥塞时保证高优先级数据包优先调度。
通常来讲，实现流量管理的工具包括：
l 分类和标记工具：分类和标记的过程就是识别出需进行不同处理（优先或者区分）的流量的过程。分类和标记是
执行iQoS的第一步。
l 管制和整形工具：识别流量违约并做出响应。管制和整形使用同样的算法识别流量违约，但是做出的响应不同。
管制工具对流量违约进行即时检查，发现违约后立即采取设定的动作进行处理。整形工具是一个与排队机制一起
工作的流量平滑工具，整形的目的是控制流量永远不超出指定的速率，使流量平滑地转发。
l 拥塞管理工具：即排队工具，应用在产生拥塞处。由于网络之间的速率不匹配，在广域网或者局域网中都有可能
出现拥塞。只有当发生拥塞时，排队工具才会被启用。
l 拥塞避免工具：拥塞避免工具是排队算法的补充，它的目的是为了处理基于TCP的数据流。
管道与流控层级
系统支持两层流控，即第一层流控和第二层流控。在每层流控中，流量的具体控制通过管道来实现。
管道
设备通过配置管道来实现iQoS。管道，即带宽通道，是一个虚拟概念。系统以管道为单位对流量进行划分，
并根据管道配置的流控动作对管道内的流量进行管控。所有流经设备的流量，都将按照设置的匹配条件进入
虚拟管道。未匹配到的流量将进入系统预定义的默认管道。
管道（除默认管道）必须包含两部分，分别是流量匹配条件和流量管理动作。

<!-- 来源页 1979 -->
l 流量匹配条件：定义设备需要匹配的流量，从而设备可以将流量进行区分。流经设备的流量会根据用户设置的条
件分类，划入对应的管道。系统为匹配到匹配条件的流量提供带宽控制。一个管道可以有多个流量匹配条件，各
个匹配条件之间为“或”的关系。流量只要匹配到其中一个匹配条件，就会进入该管道。
l 流量管理动作：对已被划分到管道中的流量所做的动作。流控分为正向控制和反向控制。正向控制即对从源到目
的方向的流量进行控制；反向控制即对从目的到源方向的流量进行控制。
为了给用户提供灵活和方便的配置，系统支持多级管道。配置多级管道，可将不同用户的不同应用分别限制
在一定带宽之内，从而能优先保障重要用户或重要应用的带宽。管道最多支持四级嵌套，默认管道不可嵌套
子管道。管道逻辑关系如下图所示：
l 用户可创建多个根管道，各个根管道之间是彼此独立的。每个根管道下均可嵌套三级子管道。
l 子管道的最小带宽之和不能大于其上一级管道的最小带宽，最大带宽也不能大于其上一级管道的最大带宽
l 用户若在根管道上配置了正向或反向的流量管理动作后，该根管道下的所有子管道都必须继承根管道设定的流量
方向。
l 仅配置了反向流量管理动作的管道不可用。
以某企业的应用场景为例说明如何嵌套多级管道。如下图所示，管理员可创建一个根管道，限制该企业北京
分公司的流量。创建一个子管道，限制其研发部门的流量。再创建子管道对研发部应用进行划分，限制不同
应用拥有不同的带宽。最后为某种应用的每用户设置子管道，限制该应用的每位用户的流量。

<!-- 来源页 1980 -->
流控层级
系统支持两层流控，即第一层流控和第二层流控。在每层流控中，流量的具体控制通过管道来实现。经过第
一层流控处理过的流量进入第二层流控，系统再根据第二层流控的管道设置对流量进行进一步管控。流量进
入设备后，iQoS处理流程如下图所示：
根据上图所示，系统的流控处理流程描述如下：
1. 流量首先进入第一层流控，系统根据第一层流控中管道的匹配条件设置划分流量到不同的管道中。不匹配任何管
道的流量进入默认管道。如果存在相同匹配条件的根管道，流量优先匹配位置靠前的根管道。流量进入根管道
后，再根据子管道的匹配条件逐层匹配。
2. 系统根据管道配置的流控动作对匹配到的流量进行管控。

<!-- 来源页 1981 -->
3. 经过第一层流控处理的流量进入第二层流控进行再次管控。系统在第二层流控中的管道匹配以及流量管控原理与
第一层流控相同。
4. 流控处理结束。
匹配方式介绍与案例
匹配方式
iQoS支持流模式和会话模式两种匹配方式：
l 流模式：按照流量传输方向定义正向流量和反向流量。当流量传输方向与匹配条件同向时定义为正向，即从源到
目的方向的流量为正向流量；当流量传输方向与匹配条件反向时定义为反向，即从目的到源方向的流量为反向流
量。
示例：若配置管道匹配条件为“源安全域：区域A；目的安全域：区域B”，则：
l 正向流量：从区域A到区域B的流量，流量传输方向与匹配条件同向，受管道的正向管控。
l 反向流量：从区域B到区域A的流量，流量传输方向与匹配条件反向，受管道的反向管控。
此时，如果服务器从区域B主动向区域A发送请求，流量从区域B到区域A，也将受管道的反向管控。
适用场景：流模式适用于限制服务器，比如限制特定方向的总流量，管控服务器端的出口总带宽等。
l 会话模式：以会话的形式对管道进行匹配，按照会话中的flow0（通常指会话中的请求流量）和flow1（通常指
会话中的响应流量）定义正向流量和反向流量。flow0的方向为正向，受管道的正向管控；flow1的方向为反
向，受管道的反向管控。同个会话的正反向流量仅绑定一条管道，反向管控不配置表示不做管控限制。
适用场景：会话模式适用于限制客户端，比如限制每个客户端的下载流量，控制用户的下载速度。
案例：使用会话模式限制每个客户端的下载流量
本案例主要介绍如何在会话模式下，限制每个客户端的下载流量。

<!-- 来源页 1982 -->
如图所示，有A、B两个区域，区域A有两个客户端，分别通过HTTP向区域B的服务器请求下载。此时正反向
管道带宽均为1000Mbps，需要限制每个客户端的下载流量为100Mbps。
其流量交互分别记录为：
l 1表示客户端A向服务器端的请求（flow0）；
l 2表示服务器端给客户端A的响应（flow1）；
l 3表示客户端B向服务器端的请求（flow0）；
l 4表示服务器端给客户端B的响应（flow1）。
思路分析
基于流模式：如果使用流模式进行限速，用户就需要确认好下载流量的方向，并根据客户端和服务器的IP地
址，精确配置多条匹配方式。如果环境中客户端或服务器数量较多时，配置操作就显得复杂繁琐。
基于会话模式：由于HTTP下载流量是基于flow1进行下载的，所以只需要对flow1进行限速100Mbps管
控。因此只需要在管道中配置一条策略“源安全域为A区域；目的安全域为B区域；正向管道带宽为
1000Mbps；反向管道带宽为1000Mbps，反向每源IP限速100Mbps”即可，大大简化用户的配置操作。
配置步骤
步骤一：开启iQoS
开启iQoS，请按照以下步骤进行操作：
1. 选择“策略> iQoS > 配置”。
2. 点击“开启iQoS”后的“启用”按钮。

<!-- 来源页 1983 -->
3. 选择匹配方式为“会话模式”。
步骤二：配置管道匹配条件
配置管道匹配条件，请按照以下步骤进行操作：
1. 选择“策略> iQoS > 策略”。
2. 点击“新建”按钮，打开<管道配置>页面。
3. 配置管道匹配条件，点击“匹配条件”区域的“新建”按钮，选择源安全域为区域A，目的安全域为区域B。
步骤三：配置流控动作
配置流控动作，请按照以下步骤进行操作：

<!-- 来源页 1984 -->
1. 在上一步的<管道配置>页面，继续配置流控动作。
2. 在“流控动作”区域，配置正向管道带宽为1000Mbps。
3. 在“流控动作”区域，配置反向管道带宽为1000Mbps，反向每源IP最大带宽为100Mbps。
4. 点击“确定”，完成配置。
步骤四：查看管道流量详情
点击“监控> 管道监控”，进入<管道监控>页面，查看各管道的流量详情。

<!-- 来源页 1985 -->
配置iQoS
系统通过创建管道来实现流量管理，进而保障和优化管理网络带宽。创建管道，包括：
1. 创建流量匹配条件，系统对匹配到匹配条件的流量进行控制。若为管道配置多个匹配条件，各匹配条件之间为
“或”的关系。
2. 根据需求创建流量白名单。目前仅根管道和默认管道支持配置白名单。配置后，系统将不对白名单中指定的流量
做流量管理。
3. 指定流量管理动作，即对已被划分到管道中的流量指定动作。
型号说明：
l
对于SG-6000-X20812、X20803、X9180-GS和X8180，不支持安装QSM模块，可以通
过安装SIOM模块来获取iQoS功能（需确保设备已经安装iQoS许可证）。
l
对于SG-6000-X9180，当设备没有QSM模块时，用户还可以安装IOM/SIOM模块来获取
iQoS功能（需确保设备已经安装iQoS许可证）。当通过安装IOM模块来获取iQoS功能
时，iQoS功能不支持整形模式；当通过安装SIOM模块来处理iQoS业务时，iQoS功能与通
过QSM模块实现iQoS功能一致。
l
对于SG-6000-X9180，当设备同时装有QSM和IOM模块时，QSM模块优先生效，来处理
iQoS业务。
l
对于SG-6000-K7680/K7280/K6680/K6580，iQoS功能不支持整形模式。
l
对于SG-6000-X9180，当设备同时装有QSM和IOM模块时，设备将不支持配置会话模式。
指定流控层级
指定进入第一层流控或第二层流控，并进入流控模式，用户可创建管道实现流量管理。在全局配置模式下，
使用以下命令：
qos-engine {first | second}
l
first – 指定进入第一层流控。
l
second –指定进入第二层流控。

<!-- 来源页 1986 -->
启用/禁用流控层级/根管道/子管道
启用/禁用流控层级
启用/禁用流控层级，在指定层级的流控模式下，使用以下命令：
l
禁用：disable
l
启用：no disable
启用/禁用根管道
启用/禁用根管道，在指定根管道配置模式下，使用以下命令：
l
禁用：disable
l
启用：no disable
启用/禁用子管道
启用/禁用子管道，在指定子管道配置模式下，使用以下命令：
l
禁用：disable
l
启用：no disable
注意: 被禁用的流控层级或者管道不参与流控处理。不可用的管道也不参与流控处理。
启用/禁用NAT IP匹配
在指定层级的流控模式下，用户可按需启用NAT IP匹配功能。启用后，对于该流控层级，系统将使用流量的
源NAT后和目的NAT前的IP地址作为匹配项。如果匹配成功，系统将会对这些IP地址进行流控管理。启用
NAT IP匹配功能，在指定层级的流控模式下，使用以下命令：
match-nat-ip enable
在指定层级的流控模式下，使用no match-nat-ip enable禁用NAT IP匹配。
注意: 在启用NAT IP匹配功能之前，必须配置NAT规则。否则，该配置不生效。
创建根管道
创建根管道，并进入该根管道配置模式。如果指定的根管道名称已经存在，则直接进入根管道配置模式。在
流控模式下，使用以下命令：

<!-- 来源页 1987 -->
root-pipe {pipe-name | default}
l
pipe-name –指定将要创建的根管道名称。
l
default –进入默认管道。
在流控模式下，使用该命令no的形式删除创建的根管道：
no root-pipe pipe-name
注意:
l
管道名字不能超过63个字符。
l
根管道下可嵌套3级子管道。
l
默认管道不能删除。
进入根管道配置模式后，可进行如下配置：
l 创建子管道
l 启用/禁用根管道
l 配置根管道流量匹配条件
l 配置根管道流量白名单
l 配置最大浮动带宽生效阈值
l 配置根管道流量管理动作
l 配置根管道流控模式
l 为根管道指定时间表
l 配置丢包记录日志
创建子管道
创建子管道，并进入子管道配置模式。如果指定的子管道名称已经存在，则直接进入子管道配置模式。在管
道配置模式下，使用以下命令：
pipe pipe-name
l
pipe-name –指定将要创建的子管道名称。
在管道配置模式下，使用该命令no的形式删除创建的子管道：
no pipe pipe-name

<!-- 来源页 1988 -->
注意:
l
管道名字不能超过63个字符。
l
删除子管道，需在其父管道配置模式下，使用no pipe pipe-name命令。
进入子管道配置模式后，可进行如下配置：
l 启用/禁用子管道
l 配置子管道流量匹配条件
l 创建子管道
配置流量匹配条件
配置匹配条件前，用户需先创建匹配条件并进入其匹配条件配置模式。如果指定的ID已存在，直接进入其匹
配条件配置模式。若不指定ID，系统将直接创建一个匹配条件并进去其配置模式。创建匹配条件并且进入匹
配条件配置模式。在管道配置模式下，使用以下命令：
pipe-map [id]
l
id – 指定匹配条件的ID。
使用no pipe-map [id]命令删除指定的匹配条件。
进入匹配条件配置模式后，可使用的配置流量匹配条件的命令如下：
l
指定流量源安全域的名称：src-zone src-zone
l
删除流量源安全域的名称：no src-zone
l
指定流量目的安全域的名称：dst-zone dst-zone
l
删除流量目的安全域的名称：no dst-zone
l
指定流量的源主机名称：src-host host-name
l
删除流量的源主机名称：no src-host host-name
l
指定流量的目的主机名称：dst-host host-name
l
删除流量的目的主机名称：no dst-host host-name
l
指定流量的源地址（IPv4或IPv6）：src-ip {ip/netmask | ip-address netmask | ipv6-
address/prefix }

<!-- 来源页 1989 -->
l
删除指定流量的源地址（IPv4或IPv6）：no src-ip {ip/netmask | ip-address netmask | ipv6-
address/prefix }
l
指定流量的目的地址（IPv4或IPv6）：dst-ip {ip/netmask | ip-address netmask | ipv6-
address/prefix }
l
删除流量的目的地址（IPv4或IPv6）：no dst-ip {ip/netmask | ip-address netmask | ipv6-
address/prefix }
l
指定流量的源地址范围（IPv4或IPv6）：src-range min-ip [max-ip]
l
删除流量的源地址范围（IPv4或IPv6）：no src-range min-ip [max-ip]
l
指定流量的目的地址范围（IPv4或IPv6）：dst-range min-ip [max-ip]
l
删除流量的目的地址范围（IPv4或IPv6）：no dst-range min-ip [max-ip]
l
指定流量的入接口名称：ingress-if interface-name
l
删除流量的入接口名称：no ingress-if interface-name
l
指定流量的出接口名称：egress-if interface-name
l
删除流量的出接口名称：no egress-if interface-name
l
指定流量的源地址条目（IPv4或IPv6）：src-addr address-book
l
删除流量的源地址条目（IPv4或IPv6）：no src-addr address-book
l
指定流量的目的地址条目（IPv4或IPv6）：dst-addr address-book
l
删除流量的目的地址条目（IPv4或IPv6）：no dst-addr address-book
l
指定用户及其所属的AAA服务器：user AAA-server user-name
l
删除用户及其所属的AAA服务器：no user AAA-server user-name
l
指定用户组及其所属的AAA服务器：user-group AAA-server usergroup-name
l
删除用户组及其所属的AAA服务器：no user-group AAA-server usergroup-name
l
指定应用或应用组，包括预定义应用和自定义应用：application app-name
l
删除应用或应用组，包括预定义应用和自定义应用：no application app-name
l
指定服务组或者服务的名称：service service-name
l
删除服务组或者服务的名称：no service service-name
l
指定ToS字段：tos tos-value
l
删除ToS字段：no tos tos-value

<!-- 来源页 1990 -->
l
指定Vlan信息：vlan vlan-id
l
删除Vlan信息：no vlan vlan-id
l
指定URL类别：url-category category-name
l
删除URL类别：no url-category category-name
l
指定TrafficClass字段：traffic-class traffic-class-value
l
删除TrafficClass字段：no traffic-class traffic-class-value
注意: iQoS不支持配置隧道接口。如需对隧道流量进行限速，请使用基于策略模式配置IPSec VPN
的方式，详细配置请参阅"配置IPSec VPN功能" 在第1400页。
配置流量白名单
配置流量白名单。配置后，系统将不对白名单中指定的流量做流量管理。用户可为根管道或默认管道指定流
量白名单。
配置白名单前，用户需先创建白名单并进入其白名单配置模式。如果指定的ID已存在，直接进入其白名单配
置模式。若不指定ID，系统将直接创建一个白名单并进去其配置模式。创建白名单并且进入白名单配置模
式，在管道配置模式下，使用以下命令：
exception-map [id]
l
id –指定白名单的ID。
使用no exception-map [id]命令删除指定的白名单。
进入白名单配置模式后，可使用的配置白名单匹配条件的命令如下：
l
指定流量源安全域的名称：src-zone src-zone
l
删除流量源安全域的名称：no src-zone
l
指定流量目的安全域的名称：dst-zone dst-zone
l
删除流量目的安全域的名称：no dst-zone
l
指定流量的入接口名称：ingress-if interface-name
l
删除流量的入接口名称：no ingress-if interface-name
l
指定流量的出接口名称：egress-if interface-name
l
删除流量的出接口名称：no egress-if interface-name
l
指定流量的源地址：src-ip {ip/netmask | ip-address netmask}

<!-- 来源页 1991 -->
l
删除指定流量的源地址：no src-ip {ip/netmask | ip-address netmask}
l
指定流量的目的地址：dst-ip {ip/netmask | ip-address netmask}
l
删除流量的目的地址：no dst-ip {ip/netmask | ip-address netmask}
l
指定用户及其所属的AAA服务器：user AAA-server user-name
l
删除用户及其所属的AAA服务器：no user AAA-server user-name
l
指定用户组及其所属的AAA服务器：user-group AAA-server usergroup-name
l
删除用户组及其所属的AAA服务器：no user-group AAA-server usergroup-name
l
指定应用或应用组，包括预定义应用和自定义应用：application app-name
l
删除应用或应用组，包括预定义应用和自定义应用：no application app-name
l
指定服务组或者服务的名称：service service-name
l
删除服务组或者服务的名称：no service service-name
l
指定ToS字段：tos tos-value
l
删除ToS字段：no tos tos-value
l
指定Vlan信息：vlan vlan-id
l
删除Vlan信息：no vlan vlan-id
l
指定URL类别：url-category category-name
l
删除URL类别：no url-category category-name
配置最大浮动带宽生效阈值
配置根管道实际流量占管道最大带宽比值的阈值上下限。当根管道带宽利用率低于阈值下限时，每个IP/用户
可占用的最大带宽值将可达到最大浮动带宽；当根管道带宽利用率高于阈值上限时，最大浮动带宽失效，当
根管道带宽利用率再次低于阈值下限时，最大浮动带宽重新生效。配置最大浮动带宽生效阈值，在根管道配
置模式下，使用以下命令：
flex-qos low-water-mark value high-water-mark value
l
low-water-mark value–指定根管道带宽利用率的下门限。取值范围为20%-75%，默认为40%。
l
high-water-mark value–指定根管道带宽利用率的上门限。取值范围为76%-90%，默认为80%。
在根管道配置模式下，使用no flex-qos恢复默认值。
配置根管道流量管理动作
配置根管道流量管理动作，在根管道配置模式下，使用以下命令：

<!-- 来源页 1992 -->
pipe-rule {forward | backward} bandwidth {Kbps | Mbps | Gbps} bandwidth-value [per-ipmin min-value] [per-ip-max max-value [delay delay-time] [flex-per-max {Kbps | Mbps}
value]] [per-ip-using {src-ip | dst-ip}] [tos-marking tos-value] [traffic-marking traffic-classvalue] [mode aggressive [strength-level level-value]] [priority value]
pipe-rule {forward | backward} bandwidth {Kbps | Mbps | Gbps} bandwidth-value [per-usermin min-value] [per-user-max max-value [delay delay-time] [flex-per-max {Kbps | Mbps}
value]] [tos-marking tos-value] [traffic-marking traffic-class-value] [mode aggressive
[strength-level level-value]] [priority value]
pipe-rule {forward | backward} bandwidth {Kbps | Mbps | Gbps} bandwidth-value averageusing {src-ip | dst-ip | user} [tos-marking tos-value] [ traffic-marking traffic-class-value ]
[mode aggressive [strength-level level-value]] [priority value]
l
forward – 对匹配到匹配条件中从源到目的方向的流量指定流控动作。
l
backward -对匹配到匹配条件中从目的到源方向的流量指定流控动作。
l
bandwidth {Kbps | Mbps | Gbps} bandwidth-value - 指定管道的最小带宽值。选择Kbps时，取
值范围为32Kbps到100000000Kbps；选择Mbps时，取值范围为1Mbps到100000Mbps；选择Gbps
时，取值范围为1Gbps到100Gbps。
l
per-ip-min min-value - 指定每个IP的最小带宽值。选择Kbps时，取值范围为32Kbps到
16000000Kbps；选择Mbps时，取值范围为1Mbps到16000Mbps。
l
per-ip-max max-value -指定每个IP的最大带宽值。选择Kbps时，取值范围为32Kbps到
16000000Kbps；选择Mbps时，取值范围为1Mbps到16000Mbps。
l
per-ip-using {src-ip|dst-ip} - 选择为管道内每个源IP（src-ip）或者目的IP（dst-ip）限制带宽。
该选项仅当用户配置了每IP最小/最大带宽值时生效。
l
per-user-min min-value - 指定每个用户的最小带宽值。选择Kbps时，取值范围为32Kbps到
16000000Kbps；选择Mbps时，取值范围为1Mbps到16000Mbps。
l
per-user-max max-value - 指定每个用户的最大带宽值。选择Kbps时，取值范围为32Kbps到
16000000Kbps；选择Mbps时，取值范围为1Mbps到16000Mbps。
l
delay delay-time – 指定延时时间。取值范围为1秒到3600秒。在延时时间范围内，对每IP/用户的最
大带宽限制不生效。
l
flex-per-max {Kbps | Mbps}–指定根管道最大浮动带宽值，需大于指定的每个IP/用户的最大带宽
值。当根管道带宽利用率低于下门限时，最大浮动带宽生效。选择Kbps时，取值范围为32Kbps到
1000000Kbps；选择Mbps时，取值范围为1Mbps到1000Mbps。

<!-- 来源页 1993 -->
l
tos-marking tos-value - 指定TOS字段。
l
traffic-marking traffic-class-value- 指定IPv6流量TrafficClass字段的数值。取值范围为0-
255。系统会将匹配成功的IPv6流量的TrafficClass字段值设置为该指定的数值。
l
traffic-marking
l
mode aggressive [strength-level level-value] - 开启对端抑制功能。默认情况下，该功能为关闭
状态。对端抑制功能可根据用户分配的带宽，使到达设备的流量尽可能与分配带宽相符，以减少设备上
的丢包。开启对端抑制功能后，默认抑制强度（strength-level）为1，抑制强度取值范围为1-8。数值
越大，抑制强度越大，丢包越少。
l
priority value - 指定管道优先级。取值范围为0到7，默认值为7。数值越小，表示该管道的优先级越
高。优先级较高的管道，系统将优先调度，并优先借用其他管道的空闲带宽。
l
average-using {src-ip | dst-ip | user} - 对管道内每个源IP（src-ip）或者目的IP（dst-ip）或者用
户（user）平均分配带宽。
使用该命令no的形式删除指定方向的流量管理动作。
注意:
l
不可同时指定每用户和每IP的带宽限制。
l
对端抑制功能只能在正反流控的一个方向开启。只有最末端管道支持配置对端抑制功能。
配置子管道流量管理动作
配置子管道流量管理动作，在子管道配置模式下，使用以下命令：
pipe-rule {forward | backward} {min | reserve-bandwidth} {percent | Kbps | Mbps | Gbps}
bandwidth-value max {percent | Kbps | Mbps | Gbps} bandwidth-value [per-ip-min minvalue] [per-ip-max max-value [delay delay-time] [flex-per-max {Kbps | Mbps} value]] [perip-using {src-ip | dst-ip}] [tos-marking tos-value] [traffic-marking traffic-class-value] [mode
aggressive [strength-level level-value]] [priority value]
pipe-rule {forward | backward} {min | reserve-bandwidth} {percent | Kbps | Mbps | Gbps}
bandwidth-value max {percent | Kbps | Mbps | Gbps} bandwidth-value [per-user-min minvalue] [per-user-max max-value [delay delay-time] [flex-per-max {Kbps | Mbps} value]]
[tos-marking tos-value] [traffic-marking traffic-class-value] [mode aggressive [strengthlevel level-value]] [priority value]

<!-- 来源页 1994 -->
l
forward – 对匹配到匹配条件中从源到目的方向的流量指定流控动作。
l
backward -对匹配到匹配条件中从目的到源方向的流量指定流控动作。
l
{min | reserve-bandwidth} {percent | Kbps | Mbps | Gbps} value -指定管道的最小带宽值，或为
管道设定保留带宽。min代表指定最小带宽。reserve-bandwidth代表指定保留带宽。设定最小带宽/
保留带宽时，percent表示此管道的最小带宽/保留带宽占父管道带宽的百分比，取值范围为1到100；
选择Kbps时，取值范围为32Kbps到100000000Kbps；选择Mbps时，取值范围为1Mbps到
100000Mbps；选择Gbps时，取值范围为1Gbps到100Gbps。
l
max {percent | Kbps | Mbps | Gbps} max-value - 指定管道的最大带宽值或最大带宽占比。
percent表示此管道的最大带宽占父管道带宽的百分比，取值范围为1到100；选择Kbps时，取值范围
为32Kbps到100000000Kbps；选择Mbps时，取值范围为1Mbps到100000Mbps；选择Gbps时，取
值范围为1Gbps到100Gbps。
l
per-ip-min min-value -指定每个IP的最小带宽值。选择Kbps时，取值范围为32Kbps到
16000000Kbps；选择Mbps时，取值范围为1Mbps到16000Mbps。
l
per-ip-max max-value -指定每个IP的最大带宽值。选择Kbps时，取值范围为32Kbps到
16000000Kbps；选择Mbps时，取值范围为1Mbps到16000Mbps。
l
per-ip-using {src-ip|dst-ip} - 选择为管道内每个源IP（src-ip）或者目的IP（dst-ip）限制带宽。
该选项仅当用户配置了每IP最小/最大带宽值时生效。
l
per-user-min min-value - 指定每个用户的最小带宽值。选择Kbps时，取值范围为32Kbps到
16000000Kbps；选择Mbps时，取值范围为1Mbps到16000Mbps。
l
per-user-max max-value - 指定每个用户的最大带宽值。选择Kbps时，取值范围为32Kbps到
16000000Kbps；选择Mbps时，取值范围为1Mbps到16000Mbps。
l
delay delay-time – 指定延时时间。取值范围为1秒到3600秒。在延时时间范围内，对每IP/用户的最
大带宽限制不生效。
l
flex-per-max {Kbps | Mbps}–指定子管道最大浮动带宽值，需大于指定的每个IP/用户的最大带宽
值。当根管道带宽利用率低于下门限时，最大浮动带宽生效。选择Kbps时，取值范围为32Kbps到
1000000Kbps；选择Mbps时，取值范围为1Mbps到1000Mbps。
l
tos-marking tos-value - 指定TOS字段。
l
traffic-marking traffic-class-value - 指定IPv6流量TrafficClass字段的数值，取值范围为0-
255。系统会将匹配成功的IPv6流量的TrafficClass字段值设置为该指定的数值。

<!-- 来源页 1995 -->
l
mode aggressive [strength-level level-value] - 开启对端抑制功能。默认情况下，该功能为关闭
状态。对端抑制功能可根据用户分配的带宽，使到达设备的流量尽可能与分配带宽相符，以减少设备上
的丢包。开启对端抑制功能后，默认抑制强度（strength-level）为1，抑制强度取值范围为1-8。数值
越大，抑制强度越大，丢包越少。
l
priority value - 指定管道优先级。取值范围为0到7，默认值为7。数值越小，表示该管道的优先级越
高。优先级较高的管道，系统将优先调度，并优先借用其他管道的空闲带宽。
注意:
l
不可同时指定每用户和每IP的带宽限制。
l
对端抑制功能只能在正反流控的一个方向开启。只有最末端管道支持配置对端抑制功能。
配置根管道的流控模式
根管道的流控模式可以为以下三种模式：
l
整形模式：配置该模式后，系统能够限制数据传输速率，使流量平滑地转发。根管道范围内流量将支持
带宽借用和优先级调度
l
管制模式：配置该模式后，系统将对超出带宽限制的流量进行丢弃。该模式不支持带宽借用和优先级调
度，且不做最小带宽保障。
l
统计模式：配置该模式后，系统仅对匹配到的流量进行监控和统计，不对流量进行任何控制。
带宽借用：即同一根管道内的所有子管道，在确保自身管道流量正常转发的情况下，可将空闲流量分配给带
宽不足的管道。
优先级调度：即在流量拥塞时，超出带宽限制的流量将进入等待队列，用户可设置优先级以确保某些应用优
先调度。
默认情况下。流控模式为整形模式。指定根管道的流控模式，在根管道配置模式下，使用以下命令：
qos-mode {police | shape | stat}
l
police – 指定流控模式为管制模式。
l
shape – 指定流控模式为整形模式。
l
stat – 指定流控模式为统计模式。

<!-- 来源页 1996 -->
注意: 对于SG-6000-K20803/K9180/K7680/K7280/K6680/K6580和X系列设备，当流量匹配
到第一层流控的整形模式管道后，若再匹配第二层流控的非整形模式管道，此管道对该流量的流控
将不生效。
配置根管道时间表
设备支持时间表功能，用户可以为根管道指定一个时间表条目，令根管道在指定的时间内生效。配置根管道
时间表功能，在根管道配置模式下，使用以下命令：
schedule schedule-name
l
schedule-name – 指定时间表的名称。
使用no schedule schedule-name取消时间表配置。
关于如何创建时间表，请参阅《系统管理》的“配置时间表功能”部分。
配置子管道时间表
用户可以为子管道指定一个时间表条目，令子管道在指定的时间内生效。配置子管道时间表功能，在子管道
配置模式下，使用以下命令：
schedule schedule-name
l
schedule-name – 指定时间表的名称。
使用no schedule schedule-name取消时间表配置。
关于如何创建时间表，请参阅《系统管理》的“配置时间表功能”部分。
配置丢包记录日志
当管道使用Per IP 限速后，若某IP 的流量超出设定阈值导致丢包，系统会自动生成日志，记录该IP 的丢包
时间、触发日志的管道名称、IP地址或用户名称、限速阈值等关键信息，帮助管理员快速定位“是否因限速
导致特定IP 的业务异常”。该功能默认为关闭状态。
在根管道配置模式下，使用以下命令配置丢包记录日志：
per-drop-report {enable | disable} interval value
l
enable - 开启丢包记录日志功能。
l
disable - 关闭丢包记录日志功能。
l
interval value - 设置同一IP 触发丢包后再次发送日志的时间间隔，以此避免单个IP 短时间内频繁触
发丢包时生成过多重复日志。

<!-- 来源页 1997 -->
注意:
l
同一时间，设备最多记录1000 个触发丢包的IP的日志；同时，单个管道最多记录其中100
个IP 的日志，避免日志量过大影响系统性能。
l
X系列QSM扩展模块不支持配置丢包记录日志。
l
仅当流控动作的限制类型设置为“限每用户” 或“限每IP” 时，该功能才会生效；若限制类
型为“不限制”，即使开启该功能，系统也不会生成相关丢包日志。
配置根管道绑定到QSM模块
对于部分Hillstone设备（SG-6000-X9180）配置iQoS功能时，可以将根管道绑定到指定QSM模块，提高
流量限制的准确性。配置根管道绑定到QSM模块，在根管道配置模式下，使用以下命令：
bind slot {number}
l
number –指定QSM模块所在的槽位号。
查看流控层级及管道的配置信息
查看流控层级及管道的配置信息，在任何模式下，使用以下命令：
show qos-engine {first | second} [root-pipe pipe-name]
l
first – 查看第一层流控及其管道的配置信息。
l
second -查看第二层流控及其管道的配置信息。
l
root-pipe pipe-name -查看指定根管道的配置信息。
配置阈值告警功能
系统支持管道使用率阈值告警功能。在开启该功能并指定告警阈值后，当管道使用率达到或超过指定的告警
阈值时，系统会记录警告级别的事件日志。对于同一个管道，系统记录事件日志的时间间隔为10秒钟，即每
10秒记录一次事件日志。
开启/关闭阈值告警功能
默认情况下，阈值告警功能为开启状态。开启/关闭阈值告警功能，在全局配置模式下，使用以下命令：
qos-threshold-switch {on | off}
l
on–开启阈值告警功能。
l
off–关闭阈值告警功能。

<!-- 来源页 1998 -->
指定告警阈值
指定管道使用率的告警阈值，在全局配置模式下，使用以下命令：
qos-threshold threshold
l
threshold–指定管道使用率的告警阈值。单位为百分比。取值范围为50到100。默认值为80。
显示阈值告警功能的启用状态
显示管道使用率的阈值告警功能的启用状态，在任何模式下，使用以下命令：
show qos-threshold
配置iQoS的匹配方式
iQoS支持流模式和会话模式两种匹配方式，两种匹配方式的差异及适用场景请参阅匹配方式介绍与案例章
节。
配置iQoS的匹配方式，在全局配置模式下，使用以下命令：
qos-match-method {flow | session}
l
flow - 指定iQoS的匹配方式为流模式，系统默认为流模式。
l
session - 指定iQoS的匹配方式为会话模式。
查看iQoS的匹配方式
查看iQoS的匹配方式，在任意模式下，使用以下命令：
show qos-match-method
回显参数中“flow”表示流模式，“session”表示会话模式。
返回结果示例如下：
hostname# show qos-match-method
Current vsys id 0, name root
iQoS match method is SESSION （当前匹配模式为会话模式）
iQoS match method is FLOW （当前匹配模式为流模式）

<!-- 来源页 1999 -->
QoS管理
QoS介绍
QoS（Quality of Service）即“服务质量”。它是指网络为特定流量提供更高优先服务的同时控制抖动和
延迟的能力，并且能够降低数据传输丢包率。当网络过载或拥塞时，QoS能够确保重要业务流量的正常传
输。
QoS是网络中管理数据流的可用带宽、延迟、抖动以及分组丢失的技术集合。所有的QoS机制的目的就是影
响这些特征中的至少一个，某些情况下甚至是全部。
QoS的实现
通常来讲，实现QoS管理功能的工具包括：
l 分类和标记工具
l 管制和整形工具
l 拥塞管理工具
l 拥塞避免工具
下图描绘了QoS的体系结构。
如上图所示，数据包通过入接口进入系统后，首先会被分类和标记。在这一过程中，系统会通过管制机制丢
弃一些数据包。然后，根据标记结果，数据包会被再次分类。系统会通过拥塞管理（Congestion
Management）机制和拥塞避免（Congestion Avoidence）机制对数据包进行管理，为数据包排列优先

<!-- 来源页 2000 -->
次序并且在发生拥塞时保证高优先级数据包的顺利通过。最后，系统会将经过QoS管理的数据包通过出接口
发送出去。
分类和标记
分类和标记的过程就是识别出需进行不同处理（优先或者区分）的流量的过程。分类和标记是执行QoS管理
的第一步。分类和标记应该在和源主机尽量接近的地方进行。
分类
通常来讲，分类工具依据封装报文的头部信息对流量进行分类。为做出分类决定，分类工具需要对头部信息
进行逐层深入检查。下图显示出头部信息的分类字段，而下表列出不同字段的分类标准。
Layer
标准描述
Layer 1
物理接口和子接口
Layer 2
MAC地址、802.1Q/p服务类别（CoS）位串和VLAN标识
Layer 3
IP优先权（IP Precedence）、DiffServ代码点（DSCP）和源/目的IP地址组
Layer 4
端口号（TCP或者UDP）
Layer 7
应用类型（Application Type）或者应用签名（Application Signature）
标记
可携带标记的字段如下：
l 第2层标记字段：802.1Q/p。
l 第3层标记字段：IP优先权和DSCP。
802.1Q/p
通过设置802.1Q头的802.1p用户优先级位（CoS）来标记以太网帧。在以太网第2层以太网帧中只有8种服
务类别（0到7）可以标记。数值的分配请参阅下表。
CoS值/IP优先权值
应用类型
7
预留（Reserved）
6
预留（Reserved）
5
语音（Voice）

<!-- 来源页 2001 -->
CoS值/IP优先权值
应用类型
4
视频会议（Video Conference）
3
呼叫信号（Call Signaling）
2
高优先级数据（High-priority Data）
1
中优先级数据（Medium-priority Data）
0
尽力服务数据（Best-effort Data）
IP优先权和DSCP
IP优先权与CoS相同，有8种服务（0到7）可以标记，请参考表30-2。
DSCP（DiffServ Code Point）是区分服务代码点。DSCP提供6位字段用于QoS标记，这6位字段是与IP优
先权相同的3位，再加上接下来的ToS字段的3位。因此，DSCP值的范围是0到63。下图为DSCP和IP优先权
位示意图。
DSCP值有两种表达方法，数字形式和关键字形式。关键字形式的DSCP值称为逐跳行为（PHB）。目前有三
类已定义的PHB，分别是尽力服务（BE或者DSCP 0）、确保转发（AFxy）和加速转发（EF）。具体信息请
参考RFC2547、2597和3246。
DSCP值将在后面的QoS处理中起到关键性的作用。
管制和整形
QoS管理提供管制和整形功能。管制和整形的作用是识别流量违约并做出响应。管制和整形使用同样的算法
识别流量违约，但是做出的响应不同。
管制工具对流量违约进行即时检查，发现违约后立即采取设定的动作进行处理。例如，管制工具可以确定负
载是否超出了定义的流量速率，然后对超出部分的流量进行重新标记或者直接丢弃。流量的出方向和入方向
都可以通过管制工具进行控制。
整形工具是一个与排队机制一起工作的流量平滑工具。整形的目的是将所有的流量发送到同一个接口，并且
控制流量永远不超出指定的速率，使流量平滑地通过该接口发送出去。整形工具通常应用在流量的出方向。
管制与整形相比较，具有以下区别，参见下表。
管制
整形
由于包被丢弃，引起TCP重传
通常延迟流量，很少引起TCP重传
不灵活和不可适应
通过排队机制来适应网络拥塞
入接口和出接口工具
出接口工具

<!-- 来源页 2002 -->
管制
整形
没有缓存的速率限制
有缓存的速率限制
令牌桶算法
Hillstone设备通过使用令牌桶算法评估流量是否违约。
令牌桶是一个存放令牌的容器，它有一定的容量。系统按设定的速度向桶中放置令牌，当桶中令牌满时，多
出的令牌溢出，桶中令牌不再增加。在用令牌桶评估流量时，是以令牌桶中的令牌数量是否足够满足数据包
的转发为依据的。如果桶中存在足够的令牌可以用来转发数据包（通常一个令牌拥有一个比特的转发权
限），称流量符合（conform）这个规格，否则称为超标（excess）。评估流量时令牌桶的参数设置包
括：
l CIR（Committed Information Rate）：向桶中放置令牌的速率，即允许的流量的平均速率。
l CBS（Committed Burst Size）：第一个令牌桶的容量，即每次突发所允许的最大的流量值。该值必须大于最大
包的长度。该令牌桶简称为C桶。
l EBS（Excess Burst Size）：第二个令牌桶的容量，即为允许的超出突发的最大流量值。该令牌桶简称为E桶。
当使用两个令牌桶进行流量评估时，依据“C桶有足够的令牌”、“C桶令牌不足，但E桶足够”以及“C桶和
E桶都没有足够的令牌”的情况，分别实施不同的操作控制。下图为双令牌桶算法示意图。
上图中，B=数据包的大小；Tc=CBS中令牌的数量；Te=EBS中令牌的数量。

<!-- 来源页 2003 -->
当CBS中的令牌数大于数据包的大小时，则该数据包符合规格（Conform），系统将根据配置进行操作；当
CBS中的令牌数小于数据包的大小，系统将检查EBS中令牌的数量，如果EBS中令牌数量大于数据包的大
小，则该数据包超出（Exceed），系统根据配置进行操作，如果EBS中的令牌数也小于数据包的大小，则该
数据包违约，系统再根据配置进行操作。
拥塞管理
拥塞管理工具是QoS工具中最重要的一个。拥塞管理工具即排队工具，应用在产生拥塞的接口上。由于网络
之间的速率不匹配，在广域网或者局域网中都有可能出现拥塞。只有当接口发生拥塞时，排队工具才会被启
用。Hillstone设备支持加权公平队列（CBWFQ）和低延迟队列（LLQ）。
l CBWFQ：基于类别的加权公平队列。使用户能够为某一类流量配置最小带宽。
l LLQ：低延迟队列。LLQ是PQ、CQ和WFQ的综合算法。LLQ一般用于语音和交互式视频。在配置时，所有LLQ类
型的应用所占总带宽不能超过链路带宽的33%。
拥塞避免
拥塞避免机制是排队算法的补充，并且依赖于排队算法。使用拥塞避免工具的目的是为了处理基于TCP的数
据流。Hillstone设备使用加权早期随机检测（WRED）算法实现拥塞避免。
配置QoS
Hillstone设备上通过配置QoS Profile，然后将配置好的QoS Profile应用到接口上来实现QoS管理。用户
可以将多个QoS Profile应用到一个接口上。通常情况下，配置QoS，需要经过以下三个步骤：
1. 配置Class。
该步骤为流量识别分类的过程。Class定义设备需要匹配的流量，从而设备可以将流量进行区分。
2. 配置QoS Profile。
QoS Profile定义了对匹配的流量所做的操作，包括管制、整形、拥塞管理和拥塞避免。
3. 绑定QoS Profile到接口。
只有将配置好的QoS Profile绑定到接口上，QoS功能才能在Hillstone设备上起作用。
配置Class
Hillstone设备支持以下类型的匹配条件：
l 应用类型匹配条件
l DSCP值匹配条件
l CoS值匹配条件
l IP地址范围匹配条件

<!-- 来源页 2004 -->
l 配置地址条目匹配条件
l QoS标签匹配条件
l IP优先权值匹配条件
l 入接口匹配条件
l 配置角色匹配条件
进入Class配置模式
定义流量的匹配条件，需要在Class配置模式下进行。进入Class配置模式，在全局配置模式下使用以下命
令：
class-map class-name
l
class-name – 指定Class的名称。执行该命令后，系统创建指定的Class，并且进入Class配置模式。
如果指定的名称已存在，则直接进入Class配置模式。
系统提供一个默认Class，名为class-default。在进行QoS管理时，没有匹配到的流量都将进入classdefault。class-default的最小带宽是接口带宽减去所有被预留的带宽。建议用户为class-default预留
25%的带宽，该数值为经过实践证明的最佳预留值。用户可以为每个Class最多配置10个匹配条件。
在全局配置模式下使用no class-map clas-name命令删除指定的Class。
配置应用类型匹配条件
Hillstone设备支持百余种应用，例如FTP、SMTP以及OSPF等。定义某种应用类型匹配条件，在Class配置
模式下，使用以下命令：
match application app-name
l
app-name – 指定应用类型的名称。该名称为系统预定义应用名称、预定义应用组名称、已创建的自定
义应用名称或者自定义应用组名称。
使用多条该命令定义多种匹配应用类型。
在Class配置模式下，使用no match application app-name命令删除指定的应用类型。
如果一个QoS Profile有多个Class包含相同Application ID的情况（通过show application list命令可查
看Application ID），系统将使用第一条匹配到的规则进行处理。
关于服务的具体信息，请参阅《防火墙》的“服务和应用”部分。
配置DSCP值匹配条件
定义DSCP值匹配条件，在Class配置模式下，使用以下命令：

<!-- 来源页 2005 -->
match dscp dscp-value1 [dscp-value2] [dscp-value3] [dscp-value4]
l
dscp-value – 指定DSCP的值。Hillstone设备支持两种DSCP值的表达方式，分别是0到63的数字和
RFC中预定义的DSCP值，例如af11、cs2等。一条命令中最多可以指定4个DSCP值，所有数值之间为
“或”的关系。
使用多条该命令配置多个DSCP值匹配条件。在Class配置模式下，使用如下命令删除指定的DSCP值匹配条
件：
no match dscp dscp-value1 [dscp-value2] [dscp-value3] [dscp-value4]
配置CoS值匹配条件
定义CoS值匹配条件，在Class配置模式下，使用以下命令：
match cos cos-value1 [cos-value2] [cos-value3] [cos-value4]
l
cos-value – 指定802.1Q的CoS值。取值范围为0到7的整数。一条命令中最多可以指定4个CoS值，所
有数值之间为“或”的关系。
使用多条该命令配置多个CoS值匹配条件。
在Class配置模式下，使用no match cos cos-value1 [cos-value2] [cos-value3] [cos-value4]命令
删除指定的CoS值匹配条件。
配置IP地址范围匹配条件
IP地址范围匹配条件用于配置IP QoS。定义IP地址范围匹配条件，在Class配置模式下，使用以下命令：
match ip-range start-ip end-ip
l
start-ip – 指定IP地址范围的起始IP地址。
l
end-ip – 指定IP地址范围的结束IP地址。
一个ip-range不能超过一个B类地址的范围。
使用多条该命令配置多个地址范围匹配条件。
在Class配置模式下，使用no match ip-range start-ip end-ip命令删除指定的IP地址范围匹配条件。
配置地址条目匹配条件
定义地址条目IP地址范围，在Class配置模式下，使用以下命令：
match address address-entry

<!-- 来源页 2006 -->
l
address-entry – 指定地址簿中已配置的地址条目的名称。
使用多条该命令配置多个地址条目匹配条件。
在Class配置模式下，使用no match address address-entry命令删除指定的地址条目匹配条件。
配置QoS标签匹配条件
定义QoS标签匹配条件，在Class配置模式下，使用以下命令：
match policy-qos-tag tag-value
l
tag-value– 指定QoS标签的值。范围是1到1024。用户在创建策略规则或者P2P Profile时，可以配置
QoS标签。
使用多条该命令配置多个QoS标签匹配条件。
在Class配置模式下，使用no match policy-qos-tag tag-value命令删除指定的QoS标签匹配条件。
关于如何创建策略规则以及如何配置QoS标签，请参阅《安全策略》。
配置IP优先权匹配条件
定义IP优先权（IP Precedence）匹配条件，在Class配置模式下，使用以下命令：
match precedence precedence-value1 [precedence-value2] [precedence-value3]
[precedence-value4]
l
precedence-value – 指定IP优先权值。范围是0到7。一条命令中最多可以指定4个IP优先权值，所有
数值之间为“或”的关系。
使用多条该命令配置多个IP优先权匹配条件。
在Class配置模式下，使用no match precedence precedence-value1 [precedence-value2]
[precedence-value3] [precedence-value4]命令删除指定的IP优先权匹配条件。
配置入接口匹配条件
定义入接口匹配条件，在Class配置模式下，使用以下命令：
match input-interface interface-name
l
interface-name – 指定入接口。
使用多条该命令配置多个入接口匹配条件。

<!-- 来源页 2007 -->
在Class配置模式下，使用no match input-interface interface-name命令删除指定的入接口匹配条
件。
配置角色/用户/用户组匹配条件
角色/用户/用户组匹配条件用于配置角色QoS和应用QoS。定义角色匹配条件，在Class配置模式下，使用
以下命令：
match {role role-name| user aaa-server-name user-name | user-group aaa-server-name
user-group-name}
l
role-name – 指定角色名称。
l
aaa-server-name – 指定AAA服务器的名称。
l
user-name - 指定用户名称。
l
user-group-name - 指定用户组名称。
使用多条该命令配置多个角色匹配条件。
在Class配置模式下，使用no match {role role-name| user aaa-server-name user-name | usergroup aaa-server-name user-group-name}命令删除指定的角色匹配条件。
显示Class信息
显示Class信息，在任何模式下使用以下命令：
show class-map [class-name]
l
class-name – 显示指定名称的class信息。如不指定该参数，则显示系统中所有class的信息。
配置QoS Profile
QoS Profile配置了对匹配流量进行的QoS管理操作。同时，用户还可以通过时间表控制QoS Profile的生效
时间。Hillstone设备支持应用QoS、IP QoS以及角色QoS三种QoS管理方式，用户可以根据需要分别配置
应用QoS、IP QoS以及角色QoS的Profile。
进入QoS Profile配置模式
QoS Profile的配置需要在QoS Profile配置模式下进行。进入QoS Profile配置模式，在全局配置模式下，
使用以下命令：
qos-profile qos-profile-name

<!-- 来源页 2008 -->
l
qos-profile-name – 指定QoS Profile的名称。执行该命令后，系统创建指定名称的QoS Profile，并
且进入该QoS Profile配置模式；如果指定的名称已存在，则直接进入QoS Profile配置模式。
在全局配置模式下，使用no qos-profile qos-profile-name命令删除指定的QoS Profile。
为QoS Profile指定时间表
为QoS Profile指定时间表控制其生效时间，在QoS Profile配置模式下使用以下命令：
schedule schedule-name
l
schedule-name – 指定系统中已经配置的时间表名称。
配置多条该命令为QoS Profile指定多个时间表。用户可以为每个QoS Profile指定最多10个时间表。为避
免产生不可预知的问题，建议用户不要配置时间重叠的时间表。
在QoS Profile配置模式下使用该命令no的形式取消时间表的配置：
no schedule schedule-name
关于如何配置时间表，请参阅《系统管理》的“配置时间表功能”部分。
对匹配流量进行QoS管理配置，进入QoS Profile配置模式后，用户需要首先为该QoS Profile指定Class。
然后为符合Class匹配条件的流量指定QoS管理操作。用户最多可为每个QoS Profile指定64个Class（包含
默认Class class-default）。应用QoS Profile支持所有类型匹配条件，IP QoS仅支持IP地址范围匹配条
件（IP地址段和地址条目），角色QoS仅支持角色匹配条件。
为QoS Profile指定Class
为QoS Profile指定Class，在QoS Profile配置模式下，使用以下命令：
class class-name
• class-name – 指定Class的名称。执行该命令后，系统进入QoS Profile的Class配置模式。
使用no class class-name命令从QoS Profile中删除指定的Class。
在QoS Profile的Class配置模式下，用户可以为匹配的流量指定QoS管理操作，包括：
l 指定最小带宽保证
l 配置管制功能
l 配置整形功能
l 配置基于IP的QoS（IP QoS）
l 配置IP QoS优先级
l 配置低延迟队列

<!-- 来源页 2009 -->
l 配置拥塞避免功能
l 设置DSCP值
l 设置CoS值
l 设置IP优先权值
l 配置匹配优先级
l 配置基于角色的QoS（角色QoS）
指定最小带宽保证
为QoS Profile中的Class指定最小带宽，在QoS Profile的Class配置模式下使用以下命令：
bandwidth {bandwidth-value | percent percentage} [schedule schedule-name]
l
bandwidth-value – 指定Class的最小带宽值，单位是kbps。该带宽值也是系统进行CBWFQ计算时的
权重值。范围是32到1000000。
l
percent percentage – 指定Class的最小带宽占接口实际带宽的百分比。取值范围为1到100。
l
schedule-name – 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配置多次该命
令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的时间表。
在QoS Profile的Class配置模式下，使用no bandwidth命令取消Class的最小带宽配置。
配置管制功能
流量管制功能对流量进行限制，并且对符合规格（Conform）的流量以及超出的（Exceed）流量根据配置
进行不同的操作。配置流量管制功能，在QoS Profile的Class配置模式下使用以下命令：
police cir-value [cbs-value] [ebs-value] conform-action {drop | set-dscp-transmit dscpvalue | set-prec-transmit precedence-value | transmit} exceed-action {drop | set-dscptransmit dscp-value | set-prec-transmit precedence-value | transmit} [violate-action { drop|
set-dscp-transmit dscp-value | set-prec-transmit precedence-value | transmit}] [schedule
schedule-name]
l
cir-value – 指定CIR，即向令牌桶中放置令牌的速率，单位是kbps。该数值为Class的最大带宽限制
值，必须小于接口的实际带宽。范围是32到1000000。
l
cbs-value – 指定第一个令牌桶的容量，即CBS的大小，单位是字节。该数值必须小于接口的实际带
宽。范围是2048到51200000。

<!-- 来源页 2010 -->
l
ebs-value – 指定第二个令牌桶的容量，即EBS的大小，单位是字节。该数值必须小于接口的实际带
宽。范围是2048到51200000。
l
conform-action – 指定对符合规格数据包所做的操作，可以是以下各操作中的一种：
l
drop：丢弃数据包。
l
set-dscp-transmit dscp-value：为数据包设置DSCP值，然后传输数据包。
l
set-prec-transmit precedence-value：为数据包设置IP优先权值，然后传输数据包。
l
transmit：不改变并且传输数据包。
l
exceed-action - 指定对超出数据包所做的操作。可选择操作与conform-action相同。
l
violate-action - 指定对违约数据包所做的操作。可选择操作与conform-action相同。
l
schedule-name – 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配置多次该命
令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的时间表。
在QoS Profile的Class配置模式下使用no police命令取消Class管制功能的配置。
配置整形功能
流量整形限制数据传输速率，使流量平滑地通过接口发送出去。流量整形为出接口工具。配置Class的整形
功能，在QoS Profile的Class配置模式下使用以下命令：
shape cir-value [cbs-value] [ebs-value] [schedule schedule-name]
l
cir-value – 指定CIR，即向令牌桶中放置令牌的速率，单位是kbps。该数值为Class的最大带宽限制
值，必须小于接口的实际带宽。范围是32到1000000。
l
cbs-value – 指定第一个令牌桶的容量，即CBS的大小，单位是字节。该数值必须小于接口的实际带
宽。范围是2048到51200000。
l
ebs-value – 指定第二个令牌桶的容量，即EBS的大小，单位是字节。该数值必须小于接口的实际带
宽。范围是2048到51200000。
l
schedule-name – 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配置多次该命
令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的时间表。
在QoS Profile的Class配置模式下使用no shape命令取消Class整形功能的配置。
配置基于IP的QoS（IP QoS）
基于IP的QoS，即IP QoS，能够为局域网里的每一个IP进行最大带宽限制或者预留带宽。实现IP QoS，
QoS Profile中的Class必须包含IP地址范围（IP地址范围或者地址条目）匹配类型。IP QoS不能与其它类

<!-- 来源页 2011 -->
型QoS混用，即如果一个QoS Profile中配置了IP QoS，则该QoS Profile中的其它Class也必须配置IP
QoS。
配置IP QoS，在QoS Profile的Class配置模式下使用以下命令：
ip-qos {shared-bandwidth | per-ip} {max-bandwidth bandwidth | reserve-bandwidth
bandwidth [max-bandwidth bandwidth]} [schedule schedule-name]
l
shared-bandwidth – 范围内的所有IP地址共享最大带宽（通过max-bandwidth bandwidth参数配
置）或者预留带宽（通过reserve-bandwidth bandwidth参数配置）为指定带宽。IP地址范围由
Class的ip-range关键字指定。
l
per-ip – 指定范围内每一个IP地址能够得到的最大带宽（通过max-bandwidth bandwidth参数配
置）或者预留带宽（通过reserve-bandwidth bandwidth参数配置）为指定带宽。IP地址范围由
Class的ip-range关键字指定。
l
max-bandwidth bandwidth – 指定最大带宽值，即IP地址范围内IP地址共享（sharedbandwidth）或者每个IP地址（per-ip）可获得的最大带宽值，单位是kbps。范围是32到1000000。
当配置reserve-bandwidth时，max-bandwidth默认值是100000。
l
reserve-bandwidth bandwidth – 指定预留带宽值，即IP地址范围内IP地址共享（sharedbandwidth）或者每个IP地址（per-ip）可获得的预留带宽值，单位是kbps，该数值必须小于接口的
实际带宽。范围是32到1000000。
l
schedule-name – 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配置多次该命
令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的时间表。
在QoS Profile的Class配置模式下，使用no ip-qos {shared-bandwidth | per-ip} {max-bandwidth
bandwidth | reserve-bandwidth bandwidth [max-bandwidth bandwidth]} [schedule
schedule-name]命令取消基于IP的QoS的配置。
预留带宽分配原则
IP地址预留带宽遵循以下分配原则：
l
只有当匹配IP地址有流量时，系统才会为其预留指定的带宽；当IP地址流量终止时，预留带宽将会被重
新释放。
l
如果配置预留带宽总和大于接口带宽，并且接口带宽都被IP使用，新匹配IP地址的流量将进入classdefault，如果class-default的带宽为0，新匹配IP地址的流量将被丢弃。
例如，配置基于IP的QoS，指定IP1到IP20每个IP的预留带宽为1M，IP21到IP40每个IP的最大带宽为1M。
接口带宽为10M。

<!-- 来源页 2012 -->
当IP1-IP9和IP21-IP40有流量时，IP1-IP9分别获得1M预留带宽，IP1-IP9超出1M预留带宽的流量和IP21-
IP40的流量将竞争剩余的1M带宽；此时，如果IP10有流量，接口剩余1M带宽会被IP10预留。这样，IP1-
IP10各获得1M预留带宽，IP1-IP10超出1M预留带宽的流量和IP21-IP40的流量将进入class-default，但
是class-default的带宽为0（接口带宽被预留完），所以流量全部被丢弃。
配置IP QoS优先级
很多时候，用户的最大带宽是被限制在一个数值内的，此时，如果用户使用迅雷等P2P工具进行大量下载
时，就可能出现打开网页速度异常缓慢或者游戏响应慢的问题。为解决这一问题，Hillstone设备引入IP
QoS优先级机制，为每一个IP内部的流量根据应用类型分配不同优先级。高优先级的流量将会得到优先处
理。IP QoS优先级需要与基于IP的QoS共同使用，实现限流的同时为重要流量提供高优先级。设置IP QoS
优先级的QoS Profile只能绑定到接口的入方向。
系统支持1到5共5个IP QoS优先级，1为最高优先级，依次降低，3是缺省优先级。IP QoS优先级只在设备
内部生效，数据包离开Hillstone设备后，所标记的IP QoS优先级将失效。
使用IP QoS优先级需要对设备进行以下配置：
1.
在接口入方向根据流量应用类型设置IP QoS优先级。
2.
在接口出方向配置基于IP的QoS Profile，利用设置的IP QoS优先级。
设置IP QoS优先级，在QoS Profile的Class配置模式下使用以下命令：
set ip-qos-priority number
l
number – 指定IP QoS优先级。取值范围是1到5的整数。默认值为3。
在QoS Profile的Class配置模式下，使用no set ip-qos-priority命令恢复IP QoS默认优先级。
配置低延迟队列
低延迟队列（LLQ）是PQ、CQ和WFQ的综合算法。LLQ一般用于语音和交互式视频。在配置时，所有LLQ
类型的应用所占总带宽不能超过链路带宽的33%。配置Class的低延迟队列，在QoS Profile的Class配置模
式下使用以下命令：
priority {bandwidth-value | percent percentage} [burst-size] [schedule schedule-name]
l
bandwidth-value – 指定预留带宽，单位是kbps。范围是32到1000000。该带宽值是Class的最小带
宽保证。
l
percent percentage – 指定预留带宽占接口实际带宽的百分比。取值范围是1到100。
l
burst-size – 指定突发流量大小，单位为字节。范围是2048到51200000。

<!-- 来源页 2013 -->
l
schedule-name – 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配置多次该命
令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的时间表。
在QoS Profile的Class配置模式下使用no priority命令取消Class的低延迟队列配置。
配置拥塞避免功能
Hillstone设备使用加权随机先期检测（WRED）机制实现拥塞避免。使用WRED机制，可以在发生拥塞时，
使设备能够随机丢弃数据包，从而避免TCP全局同步现象，提高线路带宽利用率。默认情况下，设备的
WRED机制是关闭的。配置WRED机制，在QoS Profile的Class配置模式下使用以下命令：
random-detect [dscp-based | prec-based]
l
dscp-based – 指定WRED机制根据数据包的DSCP值计算其丢弃概率。
l
prec-based – 指定WRED机制根据数据包的IP优先权值计算其丢弃概率。该选项为系统的默认选项。
在QoS Profile的Class配置模式下使用no random-detect命令取消Class的拥塞避免功能配置。
设置CoS值
用户可以为发出数据包指定二层CoS值，结合match cos命令共同使用，使设备能够对数据包根据其标记的
CoS值实现QoS管理。设置CoS值的QoS Profile只能绑定到接口的入方向。为Class的流量设置CoS值，在
QoS Profile的Class配置模式下使用以下命令：
set cos cos-value
l
cos-value – 指定CoS值。取值范围是0到7的整数。
在QoS Profile的Class配置模式下使用no set cos 命令取消Class的CoS值配置。
设置DSCP值
用户可以通过设置DSCP值标记数据包，之后，其它的QoS功能可以根据该命令设置DSCP值对数据包进行操
作。设置DSCP的QoS Profile只能绑定到接口的入方向。同一个数据包不能既设置DSCP值，又设置IP优先
权值，二者只能选其一。为Class的流量设置DSCP值，在QoS Profile的Class配置模式下使用以下命令：
set dscp dscp-value
l
dscp-value – 指定DSCP值，可以数字形式（0到63）或者关键字形式（例如af11、cs2等）。
在QoS Profile的Class配置模式下使用no set dscp命令取消Class的DSCP值配置。

<!-- 来源页 2014 -->
设置IP优先权值
用户可以通过设置IP优先权值标记数据包，之后，其它的QoS功能可以根据该命令设置IP优先权值对数据包
进行操作。设置IP QoS优先级的QoS Profile只能绑定到接口的入方向。同一个数据包不能既设置IP优先权
值，又设置DSCP值，二者只能选其一。为Class的流量设置IP优先权值，在QoS Profile的Class配置模式
下使用以下命令：
set precedence precedence-value
l
precedence-value – 指定IP优先权值范围是0到7。
在QoS Profile的Class配置模式下使用no set precedence命令取消Class的IP优先权值配置。
配置匹配优先级
有时，一些流量可能会匹配QoS Profile中的多个Class，此时，就需要根据Class的优先级决定选择哪一个
Class。指定匹配优先级，在QoS Profile的Class配置模式下使用以下命令：
match-priority priority-number
• priority-number – 指定Class的匹配优先级。范围是1到256的整数，1为最高优先级，依次降低。除
class-default以外的其它所有Class的默认优先级是255。未配置优先级的Class按照添加到QoS Profile
中的先后顺序进行匹配；class-default的优先级是256，即默认情况下，该Class具有最低优先级。
在QoS Profile的Class配置模式下使用no match-priority命令取消Class的匹配优先级配置。
配置排除策略
Hillstone设备支持排除策略。配置排除策略后，系统不对指定流量做QoS控制。在QoS Profile配置模式
下，使用以下命令：
exception-list {ip-range A.B.C.D A.B.C.D | address address-entry}
l
A.B.C.D A.B.C.D – 指定IP地址范围。在该范围内的流量将不做带宽保障和限制。
l
address-entry – 指定地址簿名称。在该范围内的流量将不做带宽保障和限制。
在QoS Profile配置模式下使用no exception-list命令删除排除策略。
示例：通过配置，分配访问Internet的每个内网用户的最大带宽为1000k，但访问DMZ网段则不受带宽限
制。内网用户IP地址范围为10.101.1.0到10.101.1.150；DMZ网段中有多台公司内部服务器（如Web服务
器，FTP服务器等），IP地址范围为10.100.6.10到10.100.6.20。部分配置可参考以下命令：
hostname(config)# class-map internet
hostname(config-class-map)# match ip-range10.101.1.0 10.101.1.150

<!-- 来源页 2015 -->
hostname(config-class-map)# exit
hostname(config)# qos-profile ipqos
hostname (config-qos-profile)# exception-list ip-range 10.100.6.10 10.100.6.20
hostname (config-qos-profile)# class internet
hostname (config-qos-prof-cmap)# ip-qos per-ip max-bandwidth 1000
hostname (config-qos-prof-cmap)# exit
hostname (config-qos-profile)# exit
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# qos-profile input ipqos
hostname(config-if-eth0/2)# qos-profile output ipqos
hostname(config-if-eth0/2)# exit
hostname(config)#
配置基于角色的QoS（角色QoS）
基于角色的QoS，即角色QoS，能够对角色对应的用户进行最大带宽限制或者预留带宽。实现角色QoS，
QoS Profile中的Class必须包含角色匹配类型。角色QoS不能与其它类型QoS混用，即如果一个QoS
Profile中配置了角色QoS，则该QoS Profile中的其它Class也必须配置角色QoS。
配置角色QoS，在QoS Profile的Class配置模式下使用以下命令：
role-qos {share | per-user} {max-bandwidth bandwidth | reserve-bandwidth bandwidth
[max-bandwidth bandwidth]} [schedule schedule-name]
l
share – 匹配角色对应的所有用户共享最大带宽（通过max-bandwidth bandwidth参数配置）或者
预留带宽（通过reserve-bandwidth bandwidth参数配置）为指定带宽。IP地址范围由Class的iprange关键字指定。
l
per-user – 匹配角色对应的每一个用户能够得到的最大带宽（通过max-bandwidth bandwidth参数
配置）或者预留带宽（通过reserve-bandwidth bandwidth参数配置）为指定带宽。
l
max-bandwidth bandwidth – 指定最大带宽值，即匹配角色对应的所有用户共享（share）或者匹
配角色对应的每个用户（per-user）可获得的最大带宽值，单位是kpbs。范围是32到1000000。当配
置reserve-bandwidth时，max-bandwidth默认值是100000。

<!-- 来源页 2016 -->
l
reserve-bandwidth bandwidth – 指定预留带宽值，即匹配角色对应的所有用户共享（sharedbandwidth）或者匹配角色对应的每个用户（per-ip）可获得的预留带宽值，单位是kpbs，该数值必
须小于接口的实际带宽。范围是32到1000000。
l
schedule-name – 指定时间表名称。该条配置将会在时间表指定的时间范围内生效。可配置多次该命
令指定多个时间表（最多8个）。为避免产生不可预知的问题，建议用户不要配置时间重叠的时间表。
如果一个用户对应的多个角色均在QoS Profile中配置了角色QoS控制，第一个匹配到的角色QoS规则将会
对该用户生效。因此，存在单个用户对应多个角色的情况时，应注意角色QoS规则的配置顺序。
在QoS Profile的Class配置模式下，使用no role-qos {share | per-user} {max-bandwidth
bandwidth | reserve-bandwidth bandwidth [max-bandwidth bandwidth]} [schedule
schedule-name]命令取消角色QoS的配置。
无匹配角色的流量都将进入缺省Class，即class-default。默认情况下，系统不对class-default进行带宽
限制。
预留带宽分配原则
角色预留带宽遵循以下分配原则：
l
只有当匹配角色对应的用户有流量时，系统才会为其预留指定的带宽；当用户流量终止时，预留带宽将
会被重新释放。
l
如果配置预留带宽总和大于接口带宽，并且接口带宽都被用户使用，则新匹配角色对应用户的流量将进
入class-default，如果class-default的带宽为0，新匹配角色对应用户的流量将被丢弃。
例如，配置基于角色的QoS，指定role1到role20每个角色的预留带宽为1M，role21到role40每个角色的
最大带宽为1M。接口带宽为10M。role1到role40依次对应user1到user40。
当user1-user9和user21-user40有流量时，user1-user9分别获得1M预留带宽，user1-user9超出1M
预留带宽的流量和user21-user40的流量将竞争剩余的1M带宽；此时，如果user10有流量，接口剩余1M
带宽会被user10预留。这样，user1-user10各获得1M预留带宽，user1-user10超出1M预留带宽的流量
和user21-user40的流量将进入class-default，但是class-default的带宽为0（接口带宽被预留完），所
以流量全部被丢弃。
嵌套QoS Profile
嵌套QoS Profile，即为一个QoS Profile的Class绑定其它的QoS Profile，通过该方式，用户可以为不同
IP/角色/用户合理分配应用带宽，或者把不同应用的带宽合理分配给不同的IP/角色/用户。配置嵌套QoS
Profile，在QoS Profile的Class配置模式下使用以下命令：
qos-profile qos-profile-name

<!-- 来源页 2017 -->
l
qos-profile-name – 指定QoS Profile的名称，为系统中已创建的QoS Profile的名称。
在QoS Profile的Class配置模式下使用no qos-profile命令取消嵌套QoS Profile的配置。
注意: 使用嵌套QoS Profile，应注意以下几点：
l
应用QoS可以嵌套IP QoS Profile和角色QoS Profile，不可以嵌套应用QoS Profile；
l
被嵌套的IP QoS Profile和角色QoS Profile的带宽共享方式必须为共享方式，并且最多只可
包含16个Class（包括默认Class）；
l
IP QoS Profile和角色QoS Profile不可以互相嵌套；
l
被嵌套的应用QoS Profile最多可包含16个Class（包括默认Class）；被嵌套的应用QoS
Profile的最小带宽保证（bandwidth）和低延迟队列（priority）配置必须为百分比形式。
指定出接口QoS管理操作
用户可以为出接口流量指定QoS管理操作，包括管制或者整形。该功能适用于IP QoS和角色QoS。默认情况
下，系统会对已配置QoS功能的出接口流量进行管制。指定对出接口流量进行整形，在QoS Profile配置模
式下使用以下命令：
shaping-for-egress
在QoS Profile配置模式下使用no shaping-for-egress命令恢复默认管理操作。
设置无效Class
默认情况下，QoS Profile中配置的所有Class都是有效的。将QoS Profile中的特定Class设置为无效状
态，在QoS Profile的Class配置模式下使用以下命令：
disable
在QoS Profile的Class配置模式下使用no disable命令恢复默认状态。
注意: 设置为无效状态的Class仍然存在于所属的QoS Profile中。如需从QoS Profile中删除特定
Class，请使用no class class-name命令。
绑定接口
QoS Profile配置完成后，只有把它们绑定到接口上，配置的各种QoS功能才会生效。绑定QoS Profile到接
口，在接口配置模式下，使用以下命令：
qos-profile [1st-level | 2nd-level] {input | output} qos-profile-name

<!-- 来源页 2018 -->
l
1st-level | 2nd-level – 用于多层QoS。1st-level为第一层，2nd-level为第二层。当不指定层数
时，默认绑定到第二层。
l
input | output – 指定QoS Profile绑定到接口的方向，分别为入方向（input）和出方向
（output）。
l
qos-profile-name – 指定绑定的QoS Profile名称。
在接口配置模式下使用no qos-profile [1st-level | 2nd-level] {input | output} 命令取消QoS Profile
在指定方向与接口的绑定。
注意: IP QoS Profile和角色QoS Profile不可以绑定到同一个接口的不同层。
显示接口QoS信息
为接口配置QoS功能后，用户可以通过show命令查看接口的QoS配置情况以及QoS统计信息。命令如下：
show qos interface interface-name [1st-level-input | 1st-level-output | 2nd-level-input |
2nd-level-output] [detail]
l
interface-name – 指定接口名称。
l
1st-level-input – 指定仅查看接口第一层入方向的QoS统计信息。
l
1st-level-output - 指定仅查看接口第一层出方向的QoS统计信息。
l
2st-level-input – 指定仅查看接口第二层入方向的QoS统计信息。
l
2st-level-output - 指定仅查看接口第二层出方向的QoS统计信息。
l
detail – 指定除显示相应的统计信息外，还需要显示相应的QoS配置信息。
显示QoS Profile信息
用户可以在任何模式下随时使用show命令查看QoS Profile的配置信息。
show qos-profile [qos-profile-name]
l
qos-profile-name – 显示指定名称的QoS Profile的信息。如果不指定该参数，则显示系统中所有
QoS Profile的信息。
弹性QoS
弹性QoS功能适用于IP QoS和角色QoS。当配置QoS功能后，不同的IP地址可获得的最大带宽通常会被限制
在一个数值之内，此时，即使接口有闲置带宽，被限制的IP也不可以使用，造成资源的浪费。针对这一现
象，Hillstone设备提供弹性QoS功能，以实现带宽资源的充分利用。为实现对不同IP队列弹性QoS的单独

<!-- 来源页 2019 -->
控制，StoneOS分别提供全局弹性QoS和Class弹性QoS配置。默认情况下，系统的全局弹性QoS功能是关
闭的，此时，无论Class的弹性QoS功能设置为开启还是关闭，它们的弹性QoS功能均无效。只有全局弹性
QoS和Class弹性QoS均为开启状态时，Class的弹性QoS功能才可生效。
用户可以为全局弹性QoS设置最大和最小两个门限值，缺省最小门限值为75，缺省最大门限值为85。默认情
况下，开启弹性QoS功能后，当出口带宽利用率小于75%时，用户可以使用的实际带宽缓慢的呈线性增加
（用户可配置该增加速率）；当带宽利用率到达85%时，用户使用的带宽呈指数减少，直到实际限定的带
宽；当接口带宽使用率在最小门限和最大门限之间的时候，弹性QoS处于稳定状态，即用户带宽不会增加也
不会减少。
配置全局弹性QoS功能
配置全局弹性QoS功能，在全局配置模式下，使用以下命令：
flex-qos low-water-mark value high-water-mark value
l
low-water-mark value – 指定最小门限值。范围是50到80。默认值是75。
l
high-water-mark value – 指定最大门限值。范围是81到90。默认值是85。
在全局配置模式下，使用no flex-qos命令关闭弹性QoS功能。
指定带宽增加的速率
开启全局弹性QoS功能后，当出口带宽利用率小于最小门限时，用户的可使用带宽将会增加。用户可以在全
局配置模式下使用以下命令指定带宽增加的速率：
flex-qos-up-rate rate
l
rate – 指定带宽增长速率，单位是倍/分钟。用户使用带宽的增长计算方法为“增长速率*IP配置带
宽”。默认值为1，取值范围为1到16。
在全局配置模式下，使用该命令no的形式恢复默认增长速率：
no flex-qos-up-rate
注意: 配置的增长速率过大可能导致带宽上下剧烈变化。
开启/关闭Class的弹性QoS功能
默认情况下，Class的弹性QoS功能为开启状态。开启或者关闭Class的弹性QoS功能，在QoS Profile的
Class配置模式下使用以下命令：

<!-- 来源页 2020 -->
l
开启：flex-qos
l
关闭：no flex-qos
指定带宽上涨的最大限制
开启Class的弹性QoS功能后，用户可以为Class的每个IP地址指定带宽上涨的最大限制。指定该最大限制，
在QoS Profile的Class配置模式下使用以下命令：
flex-qos max-bandwidth bandwidth
l
bandwidth – 指定带宽上涨的最大限制，单位为kbps。默认值是IP配置带宽的100倍。取值范围是64
到1000000。
在QoS Profile的Class配置模式下使用该命令no的形式恢复默认上涨最大限制：
no flex-qos max-bandwidth bandwidth
多层QoS
Hillstone设备的应用QoS和IP QoS是两个独立的数据流控制工具。应用QoS从全局出发，调度安排经过系
统的数据流，让高优先级的数据得到更好更快的服务；IP QoS从每一个独立的IP出发，限定每一个IP的带
宽。同时使用这两种QoS，即为多层QoS。配置多层QoS后，通过系统的流量需要经过两层QoS控制。
多层QoS的推荐配置为：在第一层使用应用QoS，在第二层使用IP限流。流量通过第一层应用QoS时，重要
数据，例如游戏、VoIP，可以被加速，非重要数据，如P2P，会被丢弃或延迟。由此，通过第一层应用QoS
后，整个系统中的流量就具备了优先顺序。所有经过第一层应用QoS的流量进入第二层IP限流，实现限流控
制。

<!-- 来源页 2021 -->
QoS配置举例
本节列举14个QoS的配置实例，分别是：
l 例1：匹配优先级
l 例2：分类与标记
l 例3：管制与整形
l 例4：基于应用的QoS
l 例5：最小带宽保证
l 例6：低延迟队列&拥塞避免
l 例7：IP QoS（1）
l 例8：IP QoS（2）
l 例9：IP QoS中的多VR应用
l 例10：IP QoS优先级
l 例11：角色QoS
l 例12：嵌套QoS Profile
l 例13：多层QoS
l 例14：综合用例
例1：匹配优先级配置举例
例如，名为Profile1的QoS Profile中有两个Class，class1和class2，其中class1的匹配条件为HTTP服
务，class2的匹配条件是QoS标签为2。配置命令如下：
第一步：配置class1和class2：
hostname(config)# class-map class1
hostname(config-class-map)# match application http
hostname(config-class-map)# exit
hostname(config)# class-map class2
hostname(config-class-map)# match policy-qos-tag 2
hostname(config-class-map)# exit
hostname(config)#class trashmatch address 1m
第二步：配置Profile1：

<!-- 来源页 2022 -->
hostname(config)# qos-profile profile1
hostname(config-qos-profile)# class class1
hostname(config-qos-prof-cmap)# set dscp 20
hostname(config-qos-prof-cmap)# match-priority 1
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class class2
hostname(config-qos-prof-cmap)# set dscp 35
hostname(config-qos-prof-cmap)# match-priority 15
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
第三步：将Profile1绑定到接口ethernet0/3上：
hostname(config)# interface ethernet0/3
hostname(config-if-eth0/3)# qos-profile input profile1
hostname(config-if-eth0/3)# exit
hostname(config)#
经过以上配置后，通过ethernet0/3流入Hillstone设备的流量中，应用类型为HTTP且Policy QoS标签为2
的流量的DSCP值会被标记为20，而不是35，因为class1的优先级高于class2，所以流量匹配class1。
例2：分类与标记
分类与标记配置举例。接口的入方向绑定了一个QoS Profile，把HTTP的流量标记成DSCP值为af11，把
QoS标签为1（在创建策略规则和P2P Profile时配置QoS标签值）的包标记成cs7，把FTP的包标记上ef。
系统和因特网都将按照RFC定义的标准处理af11、cs7和ef这3个DSCP值。
第一步：配置名为http、ftp和trash的class，对流量进行分类：
hostname(config)# class-map http
hostname(config-class-map)# match application http
hostname(config-class-map)# exit
hostname(config)# class-map ftp
hostname(config-class-map)# match application ftp
hostname(config-class-map)# exit

<!-- 来源页 2023 -->
hostname(config)# class-map trash
hostname(config-class-map)# match policy-qos-tag 1
hostname(config-class-map)# exit
hostname(config)#
第二步：配置QoS Profile，为不同类型的应用做标记：
hostname(config)# qos-profile classification
hostname(config-qos-profile)# class http
hostname(config-qos-prof-cmap)# set dscp af11
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class ftp
hostname(config-qos-prof-cmap)# set dscp ef
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)#
hostname(config-qos-prof-cmap)# set dscp cs7
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
第三步：将配置的QoS Profile绑定到接口ethernet0/0，对从ethernet0/0进入设备的流量按照配置的
QoS Profile进行分类：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# qos-profile inputclassification
hostname(config-if-eth0/0)# exit
hostname(config)#
例3：管制与整形
管制与整形配置举例。该例将HTTP流量整形到12.8M，而将P2P流量管制到6.4M。在例2中，已经将HTTP
流量标记为af11，将P2P流量标记为cs7。该例将基于例2的分类和标记结果进行配置。
第一步：配置名为af11和cs7的class：
hostname(config)# class-map af11

<!-- 来源页 2024 -->
hostname(config-class-map)# match dscp af11
hostname(config-class-map)# exit
hostname(config)# class-map cs7
hostname(config-class-map)# match dscp cs7
hostname(config-class-map)# exit
hostname(config)#
第二步：配置QoS Profile，分别对HTTP流量和P2P流量做整形和管制：
hostname(config)# qos-profile control
hostname(config-qos-profile)# class af11
hostname(config-qos-prof-cmap)# shape 12800
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class cs7
hostname(config-qos-prof-cmap)# police 6400 8000 8000conform-action transmit
exceed-action drop
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
第三步：将配置的QoS Profile绑定到接口ethernet0/1，对从ethernet0/1流出的HTTP和P2P流量按照配
置的QoS Profile进行管理：
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# qos-profile output control
hostname(config-if-eth0/1)# exit
hostname(config)#
例4：基于应用的QoS
基于应用的QoS配置举例。对P2P流量进行限流，使P2P流量按照1M每秒的速率通过ethernet0/0传输出
去。在例2中，已经将P2P流量标记为cs7。该例将基于例2的分类和标记结果进行配置。
第一步：配置名为cs7的class：
hostname(config)# class-map cs7

<!-- 来源页 2025 -->
hostname(config-class-map)# match dscp cs7
hostname(config-class-map)# exit
hostname(config)#
第二步：配置名为p2p的profile，对与cs7相匹配的流量（P2P）做限流，使其最大通过的流量为1M每秒，
并丢弃多出的流量：
hostname(config)# qos-profile p2p
hostname(config-qos-profile)# class cs7
hostname(config-qos-prof-cmap)# police 1000 conform-action transmit exceedaction drop
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
第三步：将配置的QoS Profile绑定到接口ethernet0/0，对通过ethernet0/0流出的P2P流量进行限流：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# qos-profile output p2p
hostname(config-if-eth0/0)# exit
hostname(config)#
例5：最小带宽保证
最小带宽保证配置举例。该例体现了当使用CBWFQ算法时，系统是如何保证QoS Profile中不同class的带
宽的。在例2中，已经将HTTP流量标记为af11，将P2P流量标记为cs7。该例将基于例2的分类和标记结果
进行配置。
第一步：配置名为af11和cs7的class：
hostname(config)# class-map af11
hostname(config-class-map)# match dscp af11
hostname(config-class-map)# exit
hostname(config)# class-map cs7
hostname(config-class-map)# match dscp cs7
hostname(config-class-map)# exit
hostname(config)#
第二步：创建名为qos-profile1的QoS Profile，为af11和cs7两个class配置最小带宽值。

<!-- 来源页 2026 -->
hostname(config)# qos-profile qos-profile1
hostname(config-qos-profile)# class af11
hostname(config-qos-prof-cmap)# bandwidth 5000
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class cs7
hostname(config-qos-prof-cmap)# bandwidth 2500
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
第三步：配置ethernet0/2的上行带宽，并且将policy1绑定到接口ethernet0/2：
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# bandwidth upstream 10000000
hostname(config-if-eth0/2)# qos-profile output qos-profile1
hostname(config-if-eth0/2)# exit
hostname(config)#
如果ethernet0/2的上行带宽为10M，完成以上配置后，class-default将会获得2.5M（10-5-2.5）的带
宽，并且class-default的默认队列也是CBWFQ。
使用以上配置处理流量时，如果到达class1的实际流量为20M，到达class2的实际流量为15M，而classdefault没有流量，设备在处理时，会将class-default的2.5M带宽按照比例分配给class1和class2使用。
例6：低延迟队列&拥塞避免
低延迟队列（LLQ）配置举例。为语音流量预留3M带宽，设置HTTP流量的最小带宽保证为4M，管制P2P流
量的带宽到6.4M，并且丢弃超出的P2P流量。在例2中，已经将语音流量标记为ef，HTTP流量标记为
af11，P2P流量标记为cs7。该例将基于例2的分类和标记结果进行配置。
第一步：配置名为af11、cs7和ef的class：
hostname(config)# class-map ef
hostname(config-class-map)# match dscp ef
hostname(config-class-map)# exit
hostname(config)# class-map af11
hostname(config-class-map)# match dscp af11

<!-- 来源页 2027 -->
hostname(config-class-map)# exit
hostname(config)# class-map cs7
hostname(config-class-map)# match dscp cs7
hostname(config-class-map)# exit
hostname(config)#
第二步：创建名为llq的QoS Profile，对ef、af11和cs7三个class进行配置：
hostname(config)# qos-profile llq
hostname(config-qos-profile)# class ef
hostname(config-qos-prof-cmap)# priority 3000
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class af11
hostname(config-qos-prof-cmap)# bandwidth 4000
hostname(config-qos-prof-cmap)# random-detect
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class cs7
hostname(config-qos-prof-cmap)# police 6400 8000 8000 conform-action transmit
exceed-action drop
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class class-default
hostname(config-qos-prof-cmap)# random-detect
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
第三步：配置ethernet0/3的上行带宽，并且将配置的QoS Profile绑定到接口ethernet0/3，对通过
ethernet0/3流出的流量进行限流：
hostname(config)# interface ethernet0/3
hostname(config-if-eth0/3)# bandwidth upstream10000000
hostname(config-if-eth0/3)# qos-profile output llq
hostname(config-if-eth0/3)# exit

<!-- 来源页 2028 -->
hostname(config)#
在该例中，接口ethernet0/3的带宽为10M，class cs7被执行管制，不加入计算，因此，class-default
的带宽为3M（10-3-4）。当class-default没有流量时，class cf11将会得到7M（5+2）带宽，class ef
永远保持3M带宽不变。
例7：IP QoS（1）
IP QoS配置举例。使Class ip-range1内的每个IP地址都有最多2M带宽，Class ip-range2中的所有IP地
址共享10M带宽。
第一步：配置class：
hostname(config)# class-map ip-range1
hostname(config-class-map)# match ip-range 2.2.0.0 2.2.10.255
hostname(config-class-map)# exit
hostname(config)# class-map ip-range2
hostname(config-class-map)# match ip-range 192.168.100.200 192.168.100.200
hostname(config-class-map)# exit
hostname(config)#
第二步：配置QoS Profile：
hostname(config)# qos-profile profile1
hostname(config-qos-profile)# class ip-range1
hostname(config-qos-prof-cmap)# ip-qos per-ip max-bandwidth 2000
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class ip-range2
hostname(config-qos-prof-cmap)# match-priority 3
hostname(config-qos-prof-cmap)# ip-qos shared-bandwidth max-bandwidth 10000
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
第三步：绑定QoS Profile到接口：

<!-- 来源页 2029 -->
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# qos-profile input profile1
hostname(config-if-eth0/2)# qos-profile output profile1
hostname(config-if-eth0/2)# exit
hostname(config)#
例8：IP QoS（2）
基于IP的QoS配置举例：使class ip-range1内所有IP地址共享2M带宽的同时限制每个IP地址的带宽不能超
过800k。
设备通过ethernet0/1连接Internet，ethernet0/0连接内网，要求内网中的IP地址段1.1.1.1 1.1.1.255
共享2M带宽的同时该段中的每个IP的带宽不超过800k。该需求可以通过三种方法来实现：
方法1
方法1通过WebUI配置分别在内网和外网接口配置不同限制条件的IP QoS规则实现该需求。参考以下配置步
骤：
1. 从页面左侧导航树选择并点击“配置h控制h流量管理”，进入QoS页面。
2. 点击『IP QoS』标签，然后点击『新建』。
3. 在<IP QoS>对话框做以下配置：
l 规则名称：exam_ipqos1
l 接口绑定：ethernet0/0
l IP地址：IP范围，1.1.1.1到1.1.1.255，然后点击『添加』
l 上行带宽：每IP，指定最大带宽为800
l 下行带宽：每IP，指定最大带宽为800
4. 点击『确定』。
5. 在IP QoS页面，点击『新建』并在<IP QoS>对话框做以下配置：
l 规则名称：exam_ipqos2
l 接口绑定：ethernet0/1
l IP地址：IP范围，1.1.1.1到1.1.1.255，然后点击『添加』
l 上行带宽：共享，指定最大带宽为2000
l 下行带宽：共享，指定最大带宽为2000

<!-- 来源页 2030 -->
6. 点击『确定』。
方法2
方法2通过配置两个IP QoS profile实现该需求。参考以下配置步骤：
第一步：创建名为ip-range的class
hostname(config)# class-map ip-range
hostname(config-class-map)# match ip-range 1.1.1.1 1.1.1.255
hostname(config-class-map)# exit
hostname(config)#
第二步：创建名为ipq-share的QoS profile，使范围内所有IP地址共享2M带宽：
hostname(config)# qos-profile ipq-share
hostname(config-qos-profile)# class ip-range
hostname(config-qos-prof-cmap)# ip-qos share max-bandwidth 2000
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
hostname(config)# qos-profile ipq-per
hostname(config-qos-profile)# class ip-range
hostname(config-qos-prof-cmap)# ip-qos per-ip max-bandwidth 800
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
第四步：绑定QoS Profile到接口（先限定各自带宽再限定总带宽）：
上传的绑定方法：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# qos-profile input ipq-per
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1

<!-- 来源页 2031 -->
hostname(config-if-eth0/1)# qos-profile output ipq-share
hostname(config-if-eth0/1)# exit
hostname(config)#
下载的绑定方法：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# qos-profile output ipq-share
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# qos-profile input ipq-per
hostname(config-if-eth0/1)# exit
hostname(config)#
方法3
方法3通过配置配置一个应用QoS profile、一个IP QoS profile来实现该需求。参考以下配置步骤：
第一步：创建名为ip-range的class：
hostname(config)# class-map ip-range
hostname(config-class-map)# match ip-range 1.1.1.1 1.1.1.255
hostname(config-class-map)# exit
hostname(config)#
第二步：创建名为appq的QoS profile，使范围内所有IP地址共享2M带宽：
hostname(config)# qos-profile appq
hostname(config-qos-profile)# class ip-range
hostname(config-qos-prof-cmap)# police 2000conform-action transmit exceedaction drop
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
第三步：创建名为ipq-per的QoS profile，使范围内每一IP地址的带宽不超过800k：

<!-- 来源页 2032 -->
hostname(config)# qos-profile ipq-per
hostname(config-qos-profile)# class ip-range
hostname(config-qos-prof-cmap)# ip-qos per-ip max-bandwidth 800
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
第四步：绑定QoS Profile到接口（先限定总带宽再限定各自带宽）：
上传的绑定方法：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# qos-profile input ipq-per
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# qos-profile output appq
hostname(config-if-eth0/1)# exit
hostname(config)#
下载的绑定方法：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# qos-profile output appq
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# qos-profile input ipq-per
hostname(config-if-eth0/1)# exit
hostname(config)#
例9：IP QoS中的多VR应用
现有200个IP地址段，分别为ip-range1（从1.1.1.1到1.1.1.10）、ip-range2（从2.1.1.1到
2.1.1.10）……ip-range200（从200.1.1.1到200.1.1.10）。要求通过IP QoS配置，限定每个IP地址段
的最大带宽为一定数值（比如1M、4M、10M……）。
由于每个QoS Profile最多支持64个Class，要实现200个IP地址段的不同带宽限制，该示例采用多VR与IP
QoS相结合的方案。如下图所示：

<!-- 来源页 2033 -->
如上图，系统有两个VR，分别是trust-vr和VR1。在VR1中进行SNAT转换，将200个IP地址段分别转换成单
个IP，即将ip-range1、ip-range2……ip-range200分别转换为IP1、IP2……IP200；然后将转换后的
200个IP地址根据带宽进行分类，并在trust-vr中通过IP QoS配置对不同类的IP地址进行带宽限制。
第一步：开启Hillstone设备的多VR功能：
hostname# exec vrouter enable
Warning: please reboot the device to make the change validation!
hostname# reboot
System reboot, are you sure? y/[n]: y
第二步：重启设备后，创建VR1：
hostname(config)# ip vrouter VR1
hostname(config-vrouter)# exit
hostname(config)#
第三步：配置安全域：
hostname(config)# zone trust
hostname(config-zone-trust)# vrouter VR1
hostname(config-zone-trust)# exit

<!-- 来源页 2034 -->
hostname(config)#
第四步：创建200条地址条目，分别包含200个地址段：
hostname(config)# address ip-range1
hostname(config-addr)# range 1.1.1.1 1.1.1.10
hostname(config-addr)# exit
hostname(config)# address ip-range2
hostname(config-addr)# range 2.1.1.1 2.1.1.10
hostname(config-addr)# exit
……
hostname(config)# address ip-range200
hostname(config-addr)# range 200.1.1.1 200.1.1.10
hostname(config-addr)# exit
hostname(config)#
第五步：创建200条地址条目，分别包含200个IP地址：
hostname(config)# address ip1
hostname(config-addr)# ip 1.1.1.100/32
hostname(config-addr)# exit
hostname(config)# address ip2
hostname(config-addr)# ip 2.1.1.100/32
hostname(config-addr)# exit
……
hostname(config)# address ip200
hostname(config-addr)# ip 200.1.1.100/32
hostname(config-addr)# exit
hostname(config)#
第六步：在VR1中创建200条SNAT规则，将200个地址段分别转换成200个IP地址：
hostname(config)# ip vrouter VR1
hostname(config-vrouter)# snatrule id 1 from ip-range1 to any evr trust-vr trans-to

<!-- 来源页 2035 -->
ip1
hostname(config-vrouter)# snatrule id 2 from ip-range2 to any evr trust-vr trans-to
ip2
……
hostname(config-vrouter)# snatrule id 200 from ip-range200 to any evr trust-vr
trans-to ip200
hostname(config-vrouter)# exit
hostname(config)#
第七步：将SNAT转换后的200个IP地址按照带宽进行分类，并创建地址条目，每个地址条目包含具有相同带
宽的IP地址：
hostname(config)# address 1m
hostname(config-addr)# member ip1
hostname(config-addr)# member ip5
hostname(config-addr)# member ip6
……
hostname(config-addr)# exit
hostname(config)# address 4m
hostname(config-addr)# member ip101
hostname(config-addr)# member ip15
……
hostname(config-addr)# exit
……
hostname(config)#
第八步：创建Class，每个Class配置一条地址条目匹配条件：
hostname(config)# class-map 1m
hostname(config-class-map)#
hostname(config-class-map)# exit
hostname(config)# class-map 4m
hostname(config-class-map)# match address 4m

<!-- 来源页 2036 -->
hostname(config-class-map)# exit
……
hostname(config)#
第九步：创建名为ipq的QoS profile：
hostname(config)# qos-profile ipq
hostname(config-qos-profile)# class 1m
hostname(config-qos-prof-cmap)# ip-qos per-ip max-bandwidth 1000
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class 4m
hostname(config-qos-prof-cmap)# ip-qos per-ip max-bandwidth 4000
hostname(config-qos-prof-cmap)# exit
……
hostname(config)#
第十步：绑定QoS Profile到接口：
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# qos-profile input ipq
hostname(config-if-eth0/2)# qos-profile output ipq
hostname(config-if-eth0/2)# exit
hostname(config)#
例10：IP QoS优先级
通过配置，保证网页浏览和游戏具有最高优先级。设备通过ethernet0/0（176.133.13.8）连接
Internet；PC1（10.200.2.2）和PC2（10.200.1.2）分别连接设备的ethernet0/1（10.200.2.1）和
ethernet0/2（10.200.1.1）。
第一步：配置Class：
hostname(config)# class-map http
hostname(config-class-map)# match application http
hostname(config-class-map)# exit
hostname(config)# class-map game

<!-- 来源页 2037 -->
hostname(config-class-map)# match application game_kart
hostname(config-class-map)# match application game_dance
hostname(config-class-map)# exit
hostname(config)# class-map ip-range1
hostname(config-class-map)# match ip-range 10.200.2.2 10.200.2.255
hostname(config-class-map)# exit
hostname(config)# class-map ip-range2
hostname(config-class-map)# match ip-range 10.200.1.2 10.200.1.255
hostname(config-class-map)# exit
hostname(config)#
第二步：配置QoS Profile：
hostname(config)# qos-profile ip-priority-mark
hostname(config-qos-profile)# class game
hostname(config-qos-prof-cmap)# set ip-qos-priority 1
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class http
hostname(config-qos-prof-cmap)# set ip-qos-priority 2
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)# qos-profile ip-qos
hostname(config-qos-profile)# class ip-range1
hostname(config-qos-prof-cmap)# ip-qos per-ip max-bandwidth 3000
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class ip-range2
hostname(config-qos-prof-cmap)# ip-qos per-ip max-bandwidth 2000
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
第三步：绑定QoS Profile到接口：

<!-- 来源页 2038 -->
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# qos-profile input ip-priority-mark
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# qos-profile input ip-priority-mark
hostname(config-if-eth0/2)# exit
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# qos-profile output ip-qos
hostname(config-if-eth0/0)# exit
hostname(config)#
例11：角色QoS
通过配置，使角色role1对应的每个用户（user11和user12）可获得最大1M带宽，角色role2（user21、
user22和user23）对应的所有用户共享4M带宽，class-default用户限制为每人200k。
第一步：配置角色和用户：
hostname(config)# role role1
hostname(config)# role role2
hostname(config)# aaa-server local type local
hostname(config-aaa-server)# user user11
hostname(config-user)# exit
hostname(config-aaa-server)# user user12
hostname(config-user)# exit
hostname(config-aaa-server)# user user21
hostname(config-user)# exit
hostname(config-aaa-server)# user user22
hostname(config-user)# exit
hostname(config-aaa-server)# user user23
hostname(config-user)# exit
hostname(config-aaa-server)# exit

<!-- 来源页 2039 -->
hostname(config)# role-mapping-rule rule1
hostname(config-role-mapping)# match user user11 role role1
hostname(config-role-mapping)# match user user12 role role1
hostname(config-role-mapping)# match user user21 role role2
hostname(config-role-mapping)# match user user22 role role2
hostname(config-role-mapping)# match user user23 role role2
hostname(config-role-mapping)# exit
hostname(config)# aaa-server local type local
hostname(config-aaa-server)# role-mapping-rule rule1
hostname(config-aaa-server)# exit
hostname(config)#
第二步：为用户配置适当的访问管理方式，可以是Web认证、SCVPN或者802.1X。
第三步：配置Class：
hostname(config)# class-map class1
hostname(config-class-map)# match role role1
hostname(config-class-map)# exit
hostname(config)# class-map class2
hostname(config-class-map)# match role role2
hostname(config-class-map)# exit
hostname(config)#
第四步：配置QoS Profile：
hostname(config)# qos-profile role-profile
hostname(config-qos-profile)# class class1
hostname(config-qos-prof-cmap)# role-qos per-user max-bandwidth 1000
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class class2
hostname(config-qos-prof-cmap)# role-qos share max-bandwidth 4000
hostname(config-qos-prof-cmap)# exit

<!-- 来源页 2040 -->
hostname(config-qos-profile)# class class-default
hostname(config-qos-prof-cmap)# role-qos per-user max-bandwidth 200
hostname(config-qos-profile)# exit
hostname(config)#
第五步：绑定QoS Profile到接口：
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# qos-profile input role-profile
hostname(config-if-eth0/2)# qos-profile output role-profile
hostname(config-if-eth0/2)# exit
hostname(config)#
例12：嵌套QoS Profile
在例10的基础上，配置嵌套QoS Profile，实现以下控制：
l 对于角色对应的用户，保证HTTP和FTP应用的使用带宽，限制P2P应用；
l 对于无角色用户，不对应用进行控制。
关于角色、用户配置、角色相关Class配置以及QoS Profile接口绑定配置，参见例10。
第一步：配置应用Class：
hostname(config)# application-group p2p
hostname(config-svc-group)# application bt
hostname(config-svc-group)# application emule
hostname(config-svc-group)# application xunlei
hostname(config-svc-group)# application vagaa
hostname(config-svc-group)# application pplive
hostname(config-svc-group)# application kugoo
hostname(config-svc-group)# exit
hostname(config)# class-map http
hostname(config-class-map)# match application http
hostname(config-class-map)# exit
hostname(config)# class-map ftp

<!-- 来源页 2041 -->
hostname(config-class-map)# match application ftp
hostname(config-class-map)# exit
hostname(config)# class-map p2p
hostname(config-class-map)# match application p2p
hostname(config-class-map)# exit
hostname(config)#
hostname(config)# role role1
hostname(config)# role role2
hostname(config)# role role3
hostname(config)# aaa-server local type local
hostname(config-aaa-server)# user user1
hostname(config-user)# exit
hostname(config-aaa-server)# user user2
hostname(config-user)# exit
hostname(config-aaa-server)# user user21
hostname(config-user)# exit
hostname(config-aaa-server)# user user22
hostname(config-user)# exit
hostname(config-aaa-server)# user user23
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)# role-mapping-rule rule1
hostname(config-role-mapping)# match user user1 role role1
hostname(config-role-mapping)# match user user2 rolerole1
hostname(config-role-mapping)# match user user21 role role2
hostname(config-role-mapping)# match user user22 role role2
hostname(config-role-mapping)# match user user23 role role3
hostname(config-role-mapping)# exit
hostname(config)# aaa-server local type local

<!-- 来源页 2042 -->
hostname(config-aaa-server)# role-mapping-rule rule1
hostname(config-aaa-server)# exit
hostname(config)# class-map class1
hostname(config-class-map)# match role role1
hostname(config-class-map)# exit
hostname(config)# class-map class2
hostname(config-class-map)# match role role2
hostname(config-class-map)# exit
hostname(config)# class-map class3
hostname(config-class-map)# match role role3
第二步：配置QoS Profile：
hostname(config)# qos-profile app-qos
hostname(config-qos-profile)# class http
hostname(config-qos-prof-cmap)# bandwidth percent 40
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class ftp
hostname(config-qos-prof-cmap)# bandwidth percent 20
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class p2p
hostname(config-qos-prof-cmap)# police 32 conform-action transmit exceed-action
drop
hostname(config)# qos-profile role-profile
hostname(config-qos-profile)# class class1
hostname(config-qos-prof-cmap)# role-qos per-user max-bandwidth 1000
hostname(config-qos-prof-cmap)# qos-profile app-qos
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class class2
hostname(config-qos-prof-cmap)# role-qos share max-bandwidth 4000
hostname(config-qos-prof-cmap)# qos-profile app-qos

<!-- 来源页 2043 -->
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class class3
hostname(config-qos-prof-cmap)# role-qos per-user max-bandwidth 200
hostname(config-qos-profile)# exit
hostname(config)#
例13：多层QoS
本节介绍一个多层QoS实例。
需求描述
用户带宽总量为600M，内部使用最高峰可达5000台PC。通过QoS配置，实现以下需求：
l 在网络链路使用率达85%时，将每个用户使用的最大带宽限制到100k；当网络链路空闲时，不做限制。系统中
P2P的流量不能超过200M。
l 流量的智能化分配：当用户上网时，如果仅用P2P软件下载资源，系统将全部流量分配给P2P，如BT；此后，如
果用户同时开始浏览网页，则优先保证网页浏览的应用需求，并且使P2P应用始终都在下载资源，只是P2P下载
获得的流量会从早期的占有所有带宽变为只占用少量带宽。
组网图请参照下图：

<!-- 来源页 2044 -->
第一层应用QoS配置步骤
第一层应用QoS限制P2P流量不超过200M。
第一步：在策略规则中标记P2P流量，分配QoS标签为16：
hostname(config)# servgroup p2p
hostname(config-svc-group)# service bt*
hostname(config-svc-group)# service emule*
hostname(config-svc-group)# service xunlei*
hostname(config-svc-group)# service vagaa*
hostname(config-svc-group)# service pplive*
hostname(config-svc-group)# service kugoo*
hostname(config-svc-group)# exit
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# policy-qos-tag 16
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service p2p
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any

<!-- 来源页 2045 -->
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
第二步：配置QoS Profile对P2P流量做限制：
hostname(config)# class-map match-p2p
hostname(config-class-map)# match policy-qos-tag 16
hostname(config-class-map)# exit
hostname(config)# qos-profile p2p-limit
hostname(config-qos-profile)# class match-p2p
hostname(config-qos-prof-cmap)# police 200000 conform-action transmit exceedaction drop
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
第三步：绑定P2P限流QoS Profile到广域网入接口：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# qos-profile 1st-level input p2p-limit
hostname(config-if-eth0/0)# exit
hostname(config)#
第二层IP限流配置步骤
第一步：配置IP QoS的优先级，使网页浏览（HTTP）优先级高于P2P应用：
hostname(config)# class-map http
hostname(config-class-map)# match application http
hostname(config-class-map)# exit
hostname(config)# qos-profile ip-priority
hostname(config-qos-profile)# class http
hostname(config-qos-prof-cmap)# set ip-qos-priority 1
hostname(config-qos-profile)# class match-p2p

<!-- 来源页 2046 -->
hostname(config-qos-prof-cmap)# set ip-qos-priority 5
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
第二步：将优先级QoS Profile绑定到接口：
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# qos-profile 2nd-level input ip-priority
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# qos-profile 2nd-level input ip-priority
hostname(config-if-eth0/2)# exit
hostname(config)# interface ethernet0/3
hostname(config-if-eth0/3)# qos-profile 2nd-level input ip-priority
hostname(config-if-eth0/3)# exit
hostname(config)#
第三步：配置IP限流：
hostname(config)# class-map ip-range
hostname(config-class-map)# match ip-range 10.200.1.0 10.200.3.255
hostname(config-class-map)# exit
hostname(config)# qos-profile ip-qos-limit
hostname(config-qos-profile)# class ip-range
hostname(config-qos-prof-cmap)# ip-qos per-ip max-bandwidth 100
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# qos-profile 2nd-level output ip-qos-limit
hostname(config-if-eth0/0)# qos-profile 2nd-level input ip-qos-limit
hostname(config-if-eth0/0)# exit

<!-- 来源页 2047 -->
hostname(config)#
第四步：配置设备的弹性QoS功能：
hostname(config)# flex-qos low-water-mark 75 high-water-mark 85
例14：综合用例
本节介绍一个综合QoS用例：对系统中所有应用进行限制，并且对不同的用户进行总带宽限制和应用带宽限
制。
需求描述
用户总带宽为600M，通过QoS配置，实现以下需求：
l 对应用带宽进行控制：保证实时语音至少获得总带宽的15%，保证关键业务至少获得总带宽的30%，保证网页浏
览至少获得总带宽的20%，保证P2P根据不同的时段获得20M到300M不等的带宽。
l 对内网每个用户进行带宽控制：保证Group1中每个用户最大可获得1M带宽，Group2中每个用户最大可获得
1.5M带宽，Group3中每个用户最大可获得2M带宽。
l 对内网每个用户进行应用带宽的细粒度控制：保证实时语音带宽占用户带宽的15%，关键业务占用户带宽的
30%，网页浏览占用户带宽的20%，P2P占用户带宽的10%。
组网图如下图所示：

<!-- 来源页 2048 -->
以上需求需要通过配置两层QoS来实现：第一层对系统中的应用进行控制，第二层对每一个用户进行控制。
配置步骤
第一步：配置接口和安全域：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone untrust
hostname(config-if-eth0/0)# ip address 176.133.13.8/32
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone trust
hostname(config-if-eth0/1)# ip address 10.200.1.1/24
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# zone trust
hostname(config-if-eth0/2)# ip address 10.200.2.1/24
hostname(config-if-eth0/2)# exit

<!-- 来源页 2049 -->
hostname(config)# interface ethernet0/3
hostname(config-if-eth0/3)# zone trust
hostname(config-if-eth0/3)# ip address 10.200.3.1/24
hostname(config-if-eth0/3)# exit
hostname(config)# zone trust
hostname(config-zone-trust)# application-identify
hostname(config-zone-trust)# exit
hostname(config)#
第二步：配置用户、用户组、角色：
hostname(config)# aaa-server local
hostname(config-aaa-server)# user user1
hostname(config-user)# password 111111
hostname(config-user)# exit
hostname(config-aaa-server)# user user2
hostname(config-user)# password 222222
hostname(config-user)# exit
hostname(config-aaa-server)# user user3
hostname(config-user)# password 333333
hostname(config-user)# exit
hostname(config-aaa-server)# user-group group1
hostname(config-user-group)# member user user1
hostname(config-user-group)# exit
hostname(config-aaa-server)# user-group group2
hostname(config-user-group)# member user user2
hostname(config-user-group)# exit
hostname(config-aaa-server)# user-group group3
hostname(config-user-group)# member user user3
hostname(config-user-group)# exit

<!-- 来源页 2050 -->
hostname(config-aaa-server)# exit
hostname(config)# role role1
hostname(config)# role role2
hostname(config)# role role3
hostname(config)# role-mapping-rule rule1
hostname(config-role-mapping)# match user-group group1 role role1
hostname(config-role-mapping)# match user-group group2 role role2
hostname(config-role-mapping)# match user-group group3 role role3
hostname(config-role-mapping)# exit
hostname(config)# aaa-server local
hostname(config-aaa-server)# role-mapping-rule rule1
hostname(config-aaa-server)# exit
hostname(config)#
第三步：配置路由和NAT规则：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 0.0.0.0 0.0.0.0 176.133.13.1
hostname(config-vrouter)# snatrule from any to 176.133.13.8 trans-to eif-ip mode
dynamicport
hostname(config-vrouter)# exit
hostname(config)#
第四步：配置Web认证以及策略规则：
hostname(config)# address authaddr
hostname(config-addr)# ip 10.200.0.0/16
hostname(config-addr)# exit
hostname(config)# address group1
hostname(config-addr)# ip 10.200.1.0/24
hostname(config-addr)# exit
hostname(config)# address group2

<!-- 来源页 2051 -->
hostname(config-addr)# ip 10.200.2.0/24
hostname(config-addr)# exit
hostname(config)# address group3
hostname(config-addr)# ip 10.200.3.0/24
hostname(config-addr)# exit
hostname(config)# webauth
hostname(config-webauth)# enable
hostname(config-webauth)# protocal http
hostname(config-webauth)# exit
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# src-addr authaddr
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# role unknown
hostname(config-policy-rule)# action webauth local
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# src-addr group1
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# role role1
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# rule

<!-- 来源页 2052 -->
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# src-addr group2
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# role role2
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# src-addr group3
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# role role3
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
第五步：配置时间表：
hostname(config)# schedule working
hostname(config-schedule)# periodic daily 06:00 to 18:00
hostname(config-schedule)# exit
hostname(config)# schedule evening
hostname(config-schedule)# periodic daily 18:00 to 21:00
hostname(config-schedule)# exit
hostname(config)# schedule night
hostname(config-schedule)# periodic daily 21:00 to 06:00

<!-- 来源页 2053 -->
hostname(config-schedule)# exit
hostname(config)#
第六步：配置QoS Class（关键业务根据环境不同而不同，此处以POP3为例进行配置）：
hostname(config)# class-map voip
hostname(config-class-map)# match application SIP*
hostname(config-class-map)# match application SIP
hostname(config-class-map)# exit
hostname(config)# class-map critical
hostname(config-class-map)# match application POP3
hostname(config-class-map)# exit
hostname(config)# class-map websurf
hostname(config-class-map)# match application HTTP
hostname(config-class-map)# exit
hostname(config)# class-map p2p
hostname(config-class-map)# match application APP_P2P
hostname(config-class-map)# match application APP_P2P_STREAM
hostname(config-class-map)# exit
hostname(config)# class-map group1
hostname(config-class-map)# match role role1
hostname(config-class-map)# exit
hostname(config)# class-map group2
hostname(config-class-map)# match role role2
hostname(config-class-map)# exit
hostname(config)# class-map group3
hostname(config-class-map)# match role role3
hostname(config-class-map)# exit
hostname(config)#
第七步：配置应用控制QoS Profile：

<!-- 来源页 2054 -->
hostname(config)# qos-profile p2p-fine-control
hostname(config-qos-profile)# class group1
hostname(config-qos-prof-cmap)# role-qos share max-bandwidth 8000 schedule
working
hostname(config-qos-prof-cmap)# role-qos share max-bandwidth 80000 schedule
evening
hostname(config-qos-prof-cmap)# role-qos share max-bandwidth 150000 schedule
night
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class group2
hostname(config-qos-prof-cmap)# role-qos share max-bandwidth 8000 schedule
working
hostname(config-qos-prof-cmap)# role-qos share max-bandwidth 80000 schedule
evening
hostname(config-qos-prof-cmap)# role-qos share max-bandwidth 150000 schedule
night
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class group3
hostname(config-qos-prof-cmap)# role-qos share max-bandwidth 8000 schedule
working
hostname(config-qos-prof-cmap)# role-qos share max-bandwidth 80000 schedule
evening
hostname(config-qos-prof-cmap)# role-qos share max-bandwidth 150000 schedule
night
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)# qos-profile application
hostname(config-qos-profile)# class voip
hostname(config-qos-prof-cmap)# bandwidth percent 15
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class critical

<!-- 来源页 2055 -->
hostname(config-qos-prof-cmap)# bandwidth percent 30
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class websurf
hostname(config-qos-prof-cmap)# bandwidth percent 20
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class p2p
hostname(config-qos-prof-cmap)# shape 20000 schedule working
hostname(config-qos-prof-cmap)# shape 150000 schedule evening
hostname(config-qos-prof-cmap)# shape 300000 schedule night
hostname(config-qos-prof-cmap)# qos-profile p2p-fine-control
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
第八步：配置用户应用控制QoS Profile：
hostname(config)# qos-profile user-app-fine-control
hostname(config-qos-profile)# class voip
hostname(config-qos-prof-cmap)# bandwidth percent 15
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class critical
hostname(config-qos-prof-cmap)# bandwidth percent 30
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class websurf
hostname(config-qos-prof-cmap)# bandwidth percent 20
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class p2p
hostname(config-qos-prof-cmap)# bandwidth percent 10
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit

<!-- 来源页 2056 -->
hostname(config)# qos-profile user-qos
hostname(config-qos-profile)# class group1
hostname(config-qos-prof-cmap)# role-qos per-user max-bandwidth 1000
hostname(config-qos-prof-cmap)# qos-profile user-app-fine-control
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class group2
hostname(config-qos-prof-cmap)# role-qos per-user max-bandwidth 1500
hostname(config-qos-prof-cmap)# qos-profile user-app-fine-control
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# class group3
hostname(config-qos-prof-cmap)# role-qos per-user max-bandwidth 2000
hostname(config-qos-prof-cmap)# qos-profile user-app-fine-control
hostname(config-qos-prof-cmap)# exit
hostname(config-qos-profile)# exit
hostname(config)#
第九步：绑定QoS Profile：
hostname(config)# zone untrust
hostname(config-zone-untrust)# qos 1st-level output application
hostname(config-zone-untrust)# qos 2nd-level input user-qos
hostname(config-zone-untrust)# qos 2nd-level output user-qos
hostname(config-zone-untrust)# exit
hostname(config)# zone trust
hostname(config-zone-trust)# qos 1st-level output application
hostname(config-zone-trust)# exit
hostname(config)#
推荐配置
为使用户能够更合理而有效的使用Hillstone设备的QoS功能，这里针对不同的应用类型推荐相应的配置，
供用户参考。请参阅下表：

<!-- 来源页 2057 -->
应用特性
应用举例
推荐配置
占用一定量带宽、重要的实时
性应用
VoIP、交互式视频
等
使用priority命令为其保留足够带宽，保留的带宽不
能被其他应用占用
占用少量带宽、重要的实时性
应用
SNMP 、Telnet等
使用bandwidth命令保证其最小带宽使用量
占用大量带宽、重要的非实时
性应用
Email、文件传输
等
使用bandwidth命令保证其最小带宽使用量并且可
使用空闲带宽
占用大量带宽但不重要的应用
P2P等
使用police命令对其进行最大带宽限制
占用带宽量不大，场合不同，
重要性不同
游戏
重要：使用bandwidth保证最小带宽不重要：使用
police进行最大带宽限制

<!-- 来源页 2058 -->
服务器负载均衡
服务器负载均衡功能（SLB），可以通过负载均衡算法均衡流量到不同的内网服务器，从而达到充分利用各
内网服务器，提高业务处理能力。可通过如下方式进行服务器负载均衡：
l 均衡流量到不同的内网服务器的指定端口，适用于不同内网服务器在各自指定端口分别且同时提供同一个应用服
务的场景。
l 均衡流量到同一内网服务器的不同端口，适用于同一服务器在多个端口运行多个进程来提供同一个应用服务的场
景。
l 结合以上两种方式进行流量均衡。
注意: 服务器负载均衡配置仅支持通过CLI配置，详情参见《StoneOS命令行手册》。
配置服务器负载均衡
通过CLI配置服务器负载均衡功能，包含以下配置：
l 添加/删除SLB服务器池条目
l 配置SLB服务器池条目
l 配置最小活跃真实服务数
l 配置服务器负载均衡的算法
l 添加/删除服务器负载均衡的监测规则
l 配置监测警戒值
l 配置DNAT规则引用SLB服务器池条目
添加/删除SLB服务器池条目
StoneOS系统拥有一个全局SLB服务器池，是一个用来储存内网服务器的IP地址范围与其名称的对应关系的
数据库。SLB服务器池中的IP地址与名称的对应关系条目被称作SLB服务器池条目。
用户需要为全局SLB服务器池定义SLB服务器池条目。在全局配置模式下，使用slb-server-pool命令向SLB
服务器池中添加一个SLB服务器池条目，同时进入SLB服务器池配置模式：
slb-server-pool pool-name ipv6

<!-- 来源页 2059 -->
l
pool-name - 指定要添加的SLB服务器池条目的名称。
l
ipv6 - 指定添加的SLB服务池为IPv6类型。
使用该命令no的形式将SLB服务器池条目从SLB服务器池中删除：
no slb-server-pool pool-name
注意: 已经被引用的SLB服务器池条目不能被删除。
配置SLB服务器池条目
SLB服务器池条目参数包括IP地址范围、端口数、权重、最大连接数等。SLB服务器池条目的IP地址范围以下
2种：
l IPv4地址/子网掩码，如10.100.2.0/24、10.100.20.1/32等。
l IPv4地址段，如10.100.2.3 – 10.100.2.100。
l IPv6地址/前缀长度，如2000::2/127。
l IPv6地址段，如2000::2 - 2000::5。
添加IPv4类型成员
在SLB服务器池配置模式下，使用以下命令来为SLB服务器池条目添加IPv4类型成员并配置相关参数。最多
可添加256个成员。
server {ip ip/netmask | ip-range min-ip [max-ip]} [port port-num ]{weight-per-server
weight-num} [max-connection-per-server max-num]
l
ip ip-address – 指定服务器的IPv4地址和网络掩码。
l
ip-range start-ip [max-ip] – 指定服务器IPv4地址范围段。start-ip为起始IP地址，end-ip为结束
IP地址。
l
port port-num – 指定服务器端口号。
l
weight-per-server weight-num – 指定负载均衡中流量转发的权重。范围是1到255。
l
max-connection-per-server max-num – 指定服务器最大连接数。范围是1到1000000000，默认
值是0，表示无最大连接数限制。
使用以上命令no的形式删除指定SLB服务器池条目IPv4类型成员：
no server {ip ip/netmask | ip-range min-ip [max-ip]} [port port-num ]{weight-per-server
weight-num} [max-connection-per-server max-num]

<!-- 来源页 2060 -->
添加IPv6类型成员
在SLB服务器池配置模式下，使用以下命令来为SLB服务器池条目添加IPv6类型成员并配置相关参数。最多
可添加256个成员。
server {ipv6 ipv6-address/Mask | ipv6-range min-ipv6-address [max-ipv6-address]} [port
port-num ]{weight-per-server weight-num} [max-connection-per-server max-num] [priority
value]
l
ipv6 ipv6-address/Mask– 指定服务器的IPv6地址和前缀长度。
l
ipv6-range min-ipv6-address [max-ipv6-address] – 指定服务器IPv6地址范围段。min-ipv6-
address为起始IP地址，max-ipv6-address为结束IP地址。
l
port port-num – 指定服务器端口号。
l
weight-per-server weight-num – 指定负载均衡中流量转发的权重。范围是1到255。
l
max-connection-per-server max-num – 指定服务器最大连接数。范围是1到1000000000，默认
值是0，表示无最大连接数限制。
l
priority value – 指定服务器的优先级，范围是1-100，默认值是1，数值越大则优先级越高。
使用以上命令no的形式删除指定SLB服务器池条目IPv6类型成员：
no server {ipv6 ipv6-address/Mask | ipv6-range min-ipv6-address [max-ipv6-address]} [port
port-num ]
配置最小活跃真实服务数
系统按照配置的最小活跃服务器数，从高优先级依次向低优先级检查，当检查到的该优先级内活跃服务器数
满足最小活跃服务器数时，该优先级范围内的活跃服务器将会参与流量的分配；当不满足最小活跃服务器数
或其中有服务器状态变为不可达导致目前优先级范围内的活跃服务数小于最小活跃服务器数时，继续检查低
一优先级的服务器，直到活跃服务器数满足最小活跃服务器数。指定最小同时工作的活跃服务器数，在SLB
服务器池配置模式下，使用以下命令：
minmum-working-servers value
l
value– 指定最小同时工作的活跃服务器数，范围是1-256，默认值是256。
使用以上命令no的形式删除配置的最小活跃服务器数：
no minmum-working-servers

<!-- 来源页 2061 -->
配置服务器负载均衡的算法
系统支持的服务器负载均衡算法包括：加权散列算法、加权最小连接数算法和加权轮询算法。默认情况下，
使用加权散列算法。配置服务器负载均衡的算法，在SLB服务器池配置模式下，使用以下命令：
load-balance-algorithm {weighted-hash | weighted-round-robin [sticky [timeout value]] |
weighted-least-connection [sticky [timeout value]]}
l
weighted-hash - 指定负载均衡的算法为加权散列算法。
l
weighted-round-robin - 指定负载均衡的算法为加权轮询算法。
l
weighted-least-connection - 指定负载均衡的算法为加权最小连接数算法。
l
sticky [timeout value]– 指定使用sticky，使每一个源IP产生的所有会话将被映射到同一个服务器上。
timeoutvalue指定会话保持时间，即在该时间范围内sticky功能生效。X系列设备和K9180设备在使用
sticky时，需要在Flow配置模式下配置session-schedule-mode src-ip命令才能使sticky功能生效。
添加/删除服务器负载均衡的监测规则
添加服务器负载均衡的监测规则，在SLB服务器池配置模式下，使用以下命令：
monitor {track-ping | {track-tcp | track-udp } [port port-num]} [src-interface interface_name]
interval interval-value threshold number weight weight-num
l
track-ping - 指定监测规则协议类型为PING。
l
track-tcp - 指定监测规则协议类型为TCP。
l
track-udp - 指定监测规则协议类型为UDP
l
port port-num - 指定监测规则端口号，范围是0到65535。
l
当SLB服务器池中的成员具有同一IP地址和不同端口号时，配置监测规则不需要指定端口号。系统
将对地址池中的IP地址及其端口号进行监测。
l
当SLB服务器池中的成员只配置了IP地址，没有配置端口号时，配置监测规则必须指定端口号。系
统将对地址池中的IP地址的指定端口号进行监测。
l
当SLB服务器池中的成员都配置了IP地址和端口号且这些IP地址没有重复的时候，配置监测规则可
选择是否指定端口号。如果指定端口号，系统将对地址池中的IP地址的指定端口号进行监测。如果
不指定端口号，系统将对地址池中成员的IP地址及其端口号进行监测。

<!-- 来源页 2062 -->
l
src-interface interface_name - 指定监测规则源接口。指定后，系统将使用该接口的IP地址发送
Ping/TCP/UDP报文。若要取消对监测规则源接口的指定，将src-interface 和interface_name对应
的参数删除后，重新执行添加服务器负载均衡的监测规则的命令。
l
interval interval-value - 指定发送报文间隔，范围是1到255。
l
threshold number - 指定判断监测失败的警戒值。如果系统连续未收到该参数指定个数的响应报文，
就判断为监测失败，即目标不可达。取值范围是1到255。默认值是3。
l
weight weight-num - 指定该条监测失败对整个监测对象失败贡献的权重值，范围是1到255。
使用该命令no的形式删除服务器负载均衡的监测规则：
no monitor{track-ping | {track-tcp | track-udp } [port port-num]}
配置监测警戒值
当失败监测规则的权重之和高于设置的监测警戒值后，则认为该服务器不可用。指定监测警戒值，在SLB服
务器池配置模式下，使用以下命令：
monitor threshold number
l
number - 指定监测警戒值。范围是1到255。
配置DNAT规则引用SLB服务器池条目
DNAT规则可以引用SLB服务器池条目，来实现服务器负载均衡功能。在VRouter配置模式下使用以下命
令：
dnatrule [id id] [before id | after id | top] from src-address to dst-address [service servicename] trans-to trans-to-address [slb-server-pool pool-name] [port port] [load-balance]
[track-tcp port] [track-ping] [log] [group group-id] [description description]
l
slb-server-pool pool-name – 指定引用的SLB服务器池条目名称，可以引用IPv4或IPv6类型SLB服
务器池条目。
关于如何DNAT规则其他参数介绍，请参考《防火墙》的“网络地址转换”部分中“创建DNAT规则”一节。
查看服务器负载均衡信息
查看SLB服务器池条目以及监测规则信息
查看SLB服务器池条目以及监测规则信息，在任意模式下，使用以下命令：
show slb-server-pool pool-name

<!-- 来源页 2063 -->
l
pool-name –指定SLB服务器池条目的名称。
查看负载均衡服务器的SLB地址池
查看负载均衡服务器的SLB地址池，在任意模式下，使用以下命令：
show load-balance server
查看负载均衡服务器信息
查看负载均衡服务器信息，在任意模式下，使用以下命令：
show load-balance slb-server-pool pool-name
查看引用负载均衡的DNAT规则信息
查看引用负载均衡的DNAT规则信息，在任意模式下，使用以下命令：
show load-balance rule

<!-- 来源页 2064 -->
链路负载均衡
对于多ISP链路，系统利用实时链路监控技术和动态链路探测技术将流量合理分发到不同链路，缩小了各链
路上的网络时延、抖动、丢包率，从而获得较为平衡的带宽利用率。用户可以在出站方向和入站方向分别启
用链路负载均衡功能。出站和入站方向使用两种不同的动态链路探测技术，分别是出站的实时链路监控技术
和入站的SmartDNS技术。最终根据探测的结果，实现流量的自动负载均衡。
本节包含：
l 入站负载均衡
l 出站负载均衡
l 链路负载均衡功能配置举例（通过CLI配置）
出站负载均衡
介绍
在出站方向，对于多ISP链路，系统可以根据流量目的地址所属的ISP，将其合理地分配到相应的ISP链路进
行转发；也可以利用实时链路监控技术、动态链路探测技术和其他负载均衡算法将流量分发到不同链路，从
而获得较为平衡的带宽利用率。
用户可以配置灵活的SLA模板（SLA Profile）和调度策略（Schedule Policy），将SLA模板、调度策略与
路由（目前系统仅支持目的路由和策略路由）绑定形成LLB规则，以实现对出站链路流量的控制及负载均
衡。
注意: 若一条LLB规则同时绑定了调度策略和SLA模板，则仅当调度策略的首选调度算法、二级调
度算法或备选调度算法中任一选项采用“动态就近”算法时，SLA模板才会生效。
出站负载均衡处理流程
设备对出站链路流量的负载均衡处理流程如下：

<!-- 来源页 2065 -->
型号说明：该出站负载均衡处理流程仅以下平台支持。
l
A系列平台。
l
K系列平台（K20803/K9180/K7680/K7280/K6680/K6580除外）。
l
云·界。
l
SD-WAN平台。
1. 对于出站链路流量，依次匹配会话保持、负载均衡算法。
2. 如匹配会话保持，设备将直接选择会话保持中的链路。
3. 如未匹配到会话保持，设备将根据均衡算法，在不繁忙的链路中为出站流量选路。
4. 如匹配ISP均衡算法，设备根据流量目的地址所属的ISP，进行选路。若匹配到多条可用的ISP链路，设备再继续
根据二级均衡算法，为该流量选路；若未匹配到相应的ISP链路，设备将根据备选均衡算法，为该流量选路。
5. 如匹配其他均衡算法，设备根据指定的均衡算法进行选路。
6. 设备通过选出的链路对流量进行转发。
注意:
l
若启用了会话保持功能，当为出站流量选择出口链路时，优先匹配会话保持。然后使用匹配到
的会话保持表中的链路，对流量进行转发。
l
若未匹配到会话保持表或没有启用会话保持功能，系统将根据均衡算法，在不繁忙的链路中为
流量选择出口链路；若所有链路均处于繁忙状态，系统将根据ECMP选择路由对流量进行转
发。
设备对出站链路流量的负载均衡处理流程如下：
型号说明：该出站负载均衡处理流程仅以下平台支持。
l
K系列平台：K20803、K9180、K7680、K7280、K6680、K6580。
l
X系列平台。

<!-- 来源页 2066 -->
1. LLB根据每条链路的延迟权重、丢包权重、抖动权重、带宽权重等关键参数，综合计算每条链路的开销。
2. 系统将更多的出站流量分配给开销较小的链路，同时减少在开销较大链路上的流量分配，实现出站流量的高效均
衡负载。
配置思路
请按照以下思路进行出站负载均衡配置：
1. 配置接口的链路信息，以确保系统可以根据接口配置的链路负载均衡优先级、权值、带宽阈值等信息实现智能选
路。详见“接口> 配置接口”章节说明。
说明：K20803、K9180、K7680、K7280、K6680、K6580、X系列设备不支持配置接口的链路信息。
2. 配置调度策略（Schedule Policy）
调度策略包含了多种负载均衡算法以及算法的各项参数，用户可以根据需要进行灵活配置。例如，首选调度算
法、二级算法、备选调度算法、优先级调度策略、均衡模式、带宽利用率阈值、探测开关、探测模式、均衡方
向、链路开销值（Cost值）的影响因子等。系统会根据指定负载均衡算法及其相关配置进行链路选择，并对流量
进行负载均衡。下面以“动态就近”算法并开启链路探测功能为例进行说明：
l 对于以下型号设备，如果均衡模式为兼容模式，系统会选择原有链路（缓存中的链路）进行流量转发。这
种模式适用于对链路切换比较敏感的业务，如银行业务。
型号说明：
l
K系列设备：K20803、K9180、K7680、K7280、K6680、K6580。
l
X系列设备。
l 对于以下型号设备，如果开启了会话保持功能，系统在为出站流量选择出口链路时，优先匹配会话保持。
然后使用匹配到的会话保持表中的链路，对流量进行转发。这种模式适用于对链路切换比较敏感的业务，
如银行业务。

<!-- 来源页 2067 -->
型号说明：
l
A系列平台。
l
K系列平台（K20803/K9180/K7680/K7280/K6680/K6580除外）。
l
云·界。
l
SD-WAN平台。
l 当首选均衡算法为“动态就近”时，如果开启了链路探测功能，且LLB规则中未绑定域名簿，系统会根据
用户配置的参数对网络链路状态进行探测，选出最优链路：
l 当链路带宽利用率低于用户设定的带宽利用率阈值时，系统将根据延迟权重、丢包权重、抖动权重
计算链路质量，优先选择质量高的链路；
l 当链路带宽利用率高于用户设定的带宽利用率阈值时，系统将根据延迟权重、丢包权重、抖动权
重、带宽权重、链路带宽、带宽利用率来计算链路质量，优先选择质量高的链路。
l 当首选均衡算法为“动态就近”时，如果开启了链路探测功能，且LLB规则中绑定了域名簿，系统将采用
针对域名的实时探测技术，以确保选路结果更为准确。这种方式适用于特定域名情况下的链路选择：
l 当客户端的访问请求匹配上了绑定的域名簿时，系统将对相应出口链路的质量发起主动探测，然后
将主动探测的结果作为选路的依据。
l 当客户端的访问请求未匹配绑定的域名簿时，若链路带宽利用率低于用户设定的带宽利用率阈值，
系统将根据延迟权重、丢包权重、抖动权重计算链路质量，优先选择质量高的链路；若链路带宽利
用率高于用户设定的带宽利用率阈值，系统将根据延迟权重、带宽权重、链路带宽、带宽利用率计
算链路质量，优先选择质量高的链路。
注意: 链路探测功能默认为开启状态。用户可以通过show llb profile命令查看链路探测功能
的状态，如果功能为关闭状态，可以使用dynamic-extra-conf detect enable命令开启。
3. 配置LLB规则（LLB Rule）
将调度策略绑定到路由上（目前系统仅支持目的路由和策略路由），形成LLB规则，实现对出站链路流量的控制
和负载均衡。
如果需要基于自定义的链路质量标准（延迟、抖动和丢包率），对业务流量的出口链路进行筛选，可以配置
SLA模板（SLA Profile）。通过SLA模板筛选出符合SLA标准的链路，并将SLA模板与调度策略一同绑定到
路由上，实现更精细的链路流量控制和负载均衡。

<!-- 来源页 2068 -->
链路负载均衡算法
系统支持多种出站流量的链路负载均衡算法，包括：
算法
描述
任意域名就近
(Host Any Dynamic
Proximity)
对于客户端发起的域名形式的访问请求，由设备的DNS代理转发给DNS服务器解析后，对
于客户端后续的业务访问请求，设备可以对相应出口链路质量进行主动探测，然后根据探测
结果，选择质量最优的链路对业务流量进行转发。
对于业务发起的IP地址形式的访问请求，也将触发设备对访问地址相应出口链路的主动探
测，后续客户端请求达到时，设备将根据探测结果，选择质量最优的链路对业务流量进行转
发。
l 主动探测功能开启：设备按照上述流程为客户端访问请求选择合适的链路。
l 主动探测功能关闭：对于域名形式的访问请求，设备为业务流量选择DNS响应报文的
入接口进行转发；对于IP地址形式的访问请求，该算法不生效，设备将根据备选调度算
法进行选路。
注意:
l
IPv4 和IPv6 协议类型下，分别最多仅能配置1 条引用任意域名就近
算法的LLB规则。
l
绑定策略路由的LLB规则不支持引用任意域名就近算法。
型号说明：不支持：SG-6000-K20803、K9180、K7680、K7280、
K6680、K6580平台以及SG-6000-X系列平台。
动态就近
(Dynamic
Proximity)
当LLB规则未绑定域名簿时，设备将采用被动探测的方式，获取各链路的时延、抖动、丢包
率和带宽利用率。
l 链路探测功能开启：当链路带宽利用率低于用户设定的接口带宽阈值时，系统将只根据
延时、丢包、抖动计算链路质量，优先选择质量高的链路；当链路带宽利用率高于用户
设定的接口带宽阈值时，系统将综合延时、丢包、抖动和带宽利用率来计算链路质量，
优先选择质量高的链路。
l 链路探测功能关闭：系统仅根据各出口链路的带宽利用率来选路，优先选用带宽利用率
低的链路。
当LLB规则绑定域名簿时，设备将采用主动探测和被动探测相结合的方式，获取各链路的时
延、抖动、丢包率和带宽利用率。

<!-- 来源页 2069 -->
算法
描述
l 链路探测功能开启：
o 若客户端的访问请求匹配上了绑定的域名簿，系统将对相应出口链路的质量发起
主动探测，然后将主动探测的结果作为选路的依据。
o 若客户端的访问请求未匹配上绑定的域名簿，当链路带宽利用率低于用户设定的
接口带宽阈值时，系统将只根据延时、丢包、抖动计算链路质量，优先选择质量
高的链路；当链路带宽利用率高于用户设定的接口带宽阈值时，系统将综合延
时、丢包、抖动和带宽利用率来计算链路质量，优先选择质量高的链路。
l 链路探测功能关闭：系统仅根据各出口链路的带宽利用率来选路，优先选用带宽利用率
低的链路。
目的IP哈希
(Hash Dst IP)
对流量的目的地址进行哈希运算，根据运算的结果进行选路。
加权目的IP哈希
(Weighted Hash
Dst IP)
在目的IP哈希的基础上，设备根据接口的权值，按比例进行选路。当新的出站流量到达时，
接口权值越大对应的出口链路转发的流量越多。
源IP哈希
(Hash Src IP)
对流量的源地址进行哈希运算，根据运算的结果进行选路。
加权源IP哈希
(Weighted Hash
Src IP)
在源IP哈希的基础上，设备根据接口的权值，按比例进行选路。当新的出站流量到达时，接
口权值越大，对应的出口链路转发的流量越多。
源IP端口哈希
(Hash Src IP Port)
对流量的源地址和端口进行哈希运算，根据运算的结果进行选路。
加权源IP端口哈希
(Weighted Hash
Src IP Port)
在源IP端口哈希的基础上，设备根据接口的权值，按比例进行选路。当新的出站流量到达
时，接口权值越大，对应的出口链路转发的流量越多。
ISP
将流量的目的地址与系统ISP信息进行匹配，根据匹配的结果进行选路。
最小带宽
(Least Bandwidth)
设备会记录每个接口上的上行带宽、下行带宽或上行与下行带宽总和。当新的出站流量到达
时，设备将选择带宽或带宽总和最小的接口进行转发。
加权最小带宽
（Weighted Least
Bandwidth）
在最小带宽的基础上，设备根据接口的权值，按比例进行选路。当新的出站流量到达时，将
为其选择当前带宽（总和）与接口权值的比值最小的链路。（计算方法：上行带宽、下行带
宽或上行与下行带宽总和除以接口权值）。
最小连接数
(Least Connection)
设备会记录每个接口上的连接数。当新的出站流量到达时，设备将选择连接数最少的接口进
行转发。
加权最小连接
(Weighted Least
在最少连接数分发的基础上，设备根据接口的权值，按比例进行选路。当新的出站流量到达
时，将为其选择当前连接数与接口权值的比值最小的链路。（计算方法：接口上的连接数除

<!-- 来源页 2070 -->
算法
描述
Connection)
以接口权值）。
轮询
(Round Robin)
设备将流量轮流分配给每条出口链路。
加权轮询
(Weighted Round
Robin)
在轮询的基础上，设备根据接口的权值，按比例进行选路。接口权值越大，对应的出口链路
流量越多。
限制条件
型号说明：仅A系列平台、K系列平台（除K20803/K9180/K7680/K7280/K6680/K6580之
外的所有型号）、云·界平台以及SD-WAN平台支持配置与负载均衡算法有关的功能，如带宽统
计周期、链路负载均衡的优先级调度策略、综合考虑其它调度结果、负载均衡算法、会话保持
方法等功能。
在进行出站负载均衡配置时，请仔细阅读以下限制。
注意:
l
配置调度策略时，非根VSYS下不支持配置与负载均衡算法有关的功能，如带宽统计周期、链路
负载均衡的优先级调度策略、综合考虑其它调度结果、负载均衡算法、会话保持方法等。
l
配置调度策略时，对于链路状态探测的各项参数配置、负载均衡模式配置以及数据流量方向的
配置，不同平台需要执行的命令有所区别，请以实际平台为准。
o
A系列、K系列（除K20803/K9180/K7680/K7280/K6680/K6580之外的所有型
号）、云·界、SD-WAN：在进行上述功能配置时，必须使用dynamic-extra-conf
xxxx形式的命令，例如，开启链路探测使用dynamic-extra-conf detect enable命
令。详情请参阅“配置调度策略”章节中对应功能说明。
o
X系列、K20803/K9180/K7680/K7280/K6680/K6580：在进行上述功能配置时，不
能使用dynamic-extra-conf xxxx形式的命令，例如，开启链路探测使用detect
enable命令。详情请参阅“配置调度策略”章节中对应功能说明。
l
若一条LLB规则同时绑定了调度策略和SLA模板，则仅当调度策略的首选调度算法、二级调度算
法或备选调度算法中任一选项采用“动态就近”算法时，SLA模板才会生效。

<!-- 来源页 2071 -->
配置调度策略
开始之前
l 阅读出站负载均衡"介绍" 在第2062页。
l 阅读"出站负载均衡处理流程" 在第2062页。
l 阅读"链路负载均衡算法" 在第2066页介绍。
前置条件
请提前完成接口的链路配置，以确保系统可以根据接口配置的链路负载均衡优先级、权值、带宽阈值等信息
实现智能选路。详见“接口> 配置接口”章节说明。
新建调度策略
新建或配置调度策略，在全局配置模式下，使用以下命令：
llb profile llb-profile-name [ipv6]
l
llb-profile-name – 指定调度策略的名称。执行该命令后，系统创建指定名称的调度策略，并且进入该
LLB Profile配置模式；如果指定的名称已存在，则直接进入LLB Profile配置模式。
l
ipv6– 指定新建或配置的调度策略为IPv6类型。若不指定，调度策略则为IPv4类型。
在全局配置模式下，使用no llb profile llb-profile-name命令删除指定的调度策略。
注意: IPv4类型的调度策略和IPv6类型的调度策略不允许重名。
配置负载均衡算法
配置负载均衡算法后，当新的出站流量到达时，系统将按照指定的算法为其选择出口链路。
系统支持多种流量出站的负载均衡算法，详细说明请参阅"链路负载均衡算法" 在第2066页介绍。
在LLB Profile配置模式下，使用以下命令配置负载均衡算法：
balance {prefer {host-any-dynamic-proximity | dynamic-proximity | hash-dst-ip | weightedhash-dst-ip |hash-src-ip | weighted-hash-src-ip | hash-src-ip-port| weighted-hash-src-ipport | least-bandwidth | least-connection | weighted-least-connection| round-robin |
weighted-least-bandwidth | weighted-round-robin |isp [dynamic-proximity | hash-dst-ip |
weighted-hash-dst-ip |hash-src-ip | weighted-hash-src-ip | hash-src-ip-port| weightedhash-src-ip-port | least-bandwidth | least-connection | weighted-least-connection| roundrobin | weighted-least-bandwidth | weighted-round-robin] }| alternative {dynamic-proximity
| hash-dst-ip | weighted-hash-dst-ip |hash-src-ip | weighted-hash-src-ip | hash-src-ip-port|

<!-- 来源页 2072 -->
weighted-hash-src-ip-port | least-bandwidth | least-connection | weighted-leastconnection| round-robin | weighted-least-bandwidth | weighted-round-robin}}
l
prefer - 指定负载均衡的首选算法。
l
host-any-dynamic-proximity - 指定首选均衡算法为任意域名就近算法。指定该算法后，系统
将根据主动探测的相关配置，为出站流量智能选路。主动探测的详细信息，请参阅“配置主动探
测”。
型号说明：不支持：SG-6000-K20803、K9180、K7680、K7280、K6680、
K6580平台以及SG-6000-X系列平台。
l
dynamic-proximity - 指定首选均衡算法为动态就近算法。该参数为默认算法。指定该算法后，
根据链路探测相关参数的配置，系统为出站流量智能选路。链路探测配置的详细信息，请参阅“配
置链路探测”。
l
hash-dst-ip - 指定首选均衡算法为目的IP哈希算法。
l
weighted-hash-dst-ip - 指定首选均衡算法为加权目的IP哈希算法。
l
hash-src-ip - 指定首选均衡算法为源IP哈希算法。
l
weighted-hash-src-ip - 指定首选均衡算法为加权源IP哈希算法。
l
hash-src-ip-port - 指定首选均衡算法为源IP端口哈希算法。
l
weighted-hash-src-ip-port - 指定首选均衡算法为加权源IP端口哈希算法。
l
least-bandwidth - 指定首选均衡算法为最小带宽算法。
l
least-connection - 指定首选均衡算法为最小连接数算法。
l
weighted-least-connection - 指定首选均衡算法为加权最小连接数算法。
l
round-robin - 指定首选均衡算法为轮询算法。该参数为默认算法。
l
weighted-least-bandwidth - 指定首选均衡算法为加权最小带宽算法。
l
weighted-round-robin - 指定首选均衡算法为加权轮询算法。
说明：当指定负载均衡算法为weighted-hash-src-ip、weighted-hash-dst-ip、weightedhash-src-ip-port、weighted-least-connection、weighted-least-bandwidth或者
weighted-round-robin时，系统将根据接口的权值，按比例进行选路。接口权值的具体配置信
息，请参阅“配置接口的链路负载均衡权值”部分。

<!-- 来源页 2073 -->
l
isp [dynamic-proximity | hash-dst-ip | weighted-hash-dst-ip |hash-src-ip |
weighted-hash-src-ip | hash-src-ip-port| weighted-hash-src-ip-port | leastbandwidth | least-connection | weighted-least-connection| round-robin | weightedleast-bandwidth | weighted-round-robin] - 指定首选均衡算法为ISP算法，并且同时需指
定二级均衡算法。若存在多条链路与流量目的IP的ISP相匹配，需要根据二级算法，在多条链路中
再次进行选路。系统默认的二级均衡算法为round-robin。
说明：当指定负载均衡算法为isp时，系统将接口配置的ISP信息，作为链路对应的ISP信息，从而
进行选路。配置接口ISP的具体信息，请参阅“配置接口所属ISP”部分。
l
alternative {dynamic-proximity | hash-dst-ip | weighted-hash-dst-ip |hash-src-ip |
weighted-hash-src-ip | hash-src-ip-port| weighted-hash-src-ip-port | least-bandwidth |
least-connection | weighted-least-connection| round-robin | weighted-least-bandwidth |
weighted-round-robin} - 当首选均衡算法为isp 或host-any-dynamic-proximity时，指定备选
均衡算法。系统通过首选均衡算法没有为流量匹配到合适的链路，需要根据备选均衡算法，为流量重新
进行选路。
在LLB Profile配置模式下，使用no balance {prefer | alternative}命令恢复默认负载均衡算法。
注意:
l
当流量出站的负载均衡算法配置为“最小带宽”或“加权最小带宽” 时，用户可以根据需要，
指定流量带宽的统计周期。
l
若根据负载均衡算法选出的链路均处于繁忙状态，系统将使用默认路由对流量进行转发。
配置带宽统计周期
当流量出站的负载均衡算法配置为“最小带宽”或“加权最小带宽” 时，用户可以根据需要，指定流量带宽
的统计周期。为出站流量的负载均衡配置带宽统计周期，在全局配置模式下，使用以下命令：
llb bandwidth-statistics-period value
l
value - 指定带宽统计周期。取值范围是1到300秒，默认值为120秒。
在全局配置模式下，使用no llb bandwidth-statistics-period命令恢复默认值。
开启综合考虑其它调度结果功能
当均衡算法指定为“轮询” 或“加权轮询” 时，系统支持开启链路负载均衡的综合调度功能。开启该功能
后，系统将综合会话保持算法对链路的调度结果，进行智能选路。当新的出站流量到达时，系统会根据当前
各链路承载流量的情况，优先选择承载流量较少的链路对其进行转发。

<!-- 来源页 2074 -->
在LLB Profile配置模式下，使用以下命令开启综合调度功能：
balance comprehensive
l
comprehensive - 开启链路负载均衡的综合调度功能，系统默认关闭该功能。
在LLB Profile配置模式下，使用no balance comprehensive命令关闭综合调度功能。
配置链路负载均衡的优先级调度策略
启用链路的优先级调度策略，需指定最小活跃链路数，即参与链路负载均衡调度的链路的最少个数，取值范
围是1到32。
在LLB Profile配置模式下，使用以下命令开启链路负载均衡的优先级调度策略：
min-active-link value
l
value - 指定最小活跃链路数。取值范围是0到32，默认值是0，表示关闭链路负载均衡的优先级调度功
能。
在LLB Profile配置模式下，使no min-active-link命令恢复最小活跃链路数的默认值。
设备出口链路的优先级由其对应接口的链路负载均衡优先级决定。如设备上存在10条出口链路，最小活跃链
路数为6，那么根据出口链路对应接口的优先级排序，最高优先级的所有可用链路优先加入调度；如果最高
优先级的链路小于6条，次优先级的所有可用链路将加入调度。以此类推，直到参与调度的可用链路数大于
等于6或者所有的可用链路均参与调度为止。当某条参与调度的链路不可用，导致实际参与调度的链路条数
小于6时，设备会继续从未参与调度的链路中，选择最高优先级的所有可用链路加入调度，直到满足条件；
当高优先级的链路从不可用变为可用时，将重新加入调度。
举例说明，接口eth0/1、eth0/2、eth0/3和eth0/4的链路负载均衡优先级分别为10、20、30和20；接
口eth0/1、eth0/2、eth0/3和eth0/4的ISP分别为China-telecom、China-telecom、Chinatelecom和China-mobile。调度策略的首选均衡算法为“ISP”，备选均衡算法为“轮询”，开启优先级
调度策略，最小活跃链路数为2。其他选项保持默认配置，并为调度策略关联LLB规则。使用电信运营商的客
户发送请求达到设备后，因为LLB均衡算法为ISP，所以接口eth0/1、eth0/2和eth0/3对应的出口链路将
参与调度；因为接口eth0/1和eth0/2优先级较高，所以设备最终将该电信客户端请求轮流分配给接口
eth0/1、eth0/2。
配置主动探测
当指定流量的首选均衡算法为“任意域名就近”时，系统会自动启用主动探测功能。客户端的DNS请求经设
备转发给DNS服务器解析，返回的DNS响应到达设备时，设备会在探测表中记录解析得到的IP地址，及IP地
址对应的设备出接口。当客户端收到DNS响应，首次发起的业务访问流量到达设备时，设备将选择之前DNS
响应到达设备的入接口作为业务访问流量的出接口；同时，对于客户端访问的记录在探测表中的IP地址，系
统将主动从该IP地址对应的各出接口发送探测报文，用来探测各出接口对应链路的质量。当客户端再次发起
业务访问时，系统将根据探测结果，选择质量最优的链路进行转发。

<!-- 来源页 2075 -->
型号说明：不支持：SG-6000-K20803、K9180、K7680、K7280、K6680、K6580平台以
及SG-6000-X系列平台。
在LLB Profile配置模式下，使用以下命令配置主动探测功能的相关参数：
host-detect {interval interval | max-table-size value | timeout time}
l interval - 指定系统主动发送探测报文的时间间隔。取值范围是60到86400秒，默认值是600秒。
l value - 指定探测表可以记录的表项的最大个数。不同平台支持配置的表项大小不同，请以实际情况为准。
l time - 指定探测表项的超时时间。如果超过该时间，系统将清除相应的探测表项。取值范围是300到86400秒，
默认值是3600秒。
在LLB Profile配置模式下，使用no host-detect {interval | timeout}命令恢复默认值。
配置链路探测功能
用户可根据需要，配置链路状态探测的各项参数。系统将根据链路探测的配置，为出站流量智能选路。对于
SG-6000 A系列、K系列（除K20803/K9180/K7680/K7280/K6680/K6580之外的所有型号）和云·界平
台，仅当流量的负载均衡算法为“动态就近（dynamic-proximity）”时，该配置生效。
l 开启和关闭链路探测
l 配置链路探测掩码/前缀
l 配置带宽利用率阈值
l 配置计算链路状态时各项权值
l 配置链路权重刷新时间
l 配置子网条目最大值
开启和关闭链路探测
默认情况下，链路探测功能为开启状态。关闭和开启探测，在LLB Profile配置模式下，使用以下命令：
dynamic-extra-conf detect {disable | enable}
l
disable – 禁用探测功能。禁用探测功能后，系统仅根据各出口链路的带宽占用率来选路，优先选用带
宽占用率低的链路。
l
enable – 启用探测功能。当探测功能开启后，设备将采用主动探测和被动探测相结合的方式，根据用户
配置的链路状态探测的各项参数，对网络链路状态进行探测，然后选出最优路由。选择的优先级如下：

<!-- 来源页 2076 -->
1.
当LLB规则绑定域名簿，且客户端的访问请求匹配上了绑定的域名簿时，系统将对相应出口链路的
质量发起主动探测，然后将主动探测的结果作为选路的依据。
2.
当LLB规则未绑定域名簿，或者绑定域名簿但客户端的访问请求未匹配绑定的域名簿时，若链路带
宽占用率低于用户设定的带宽阈值，系统将只根据延时、丢包、抖动计算链路质量，优先选择质量
高的链路；若链路带宽占用率高于用户设定的带宽阈值，系统将综合延时、丢包、抖动和带宽占用
率来计算链路质量，优先选择质量高的链路。
对于SG-6000 K20803/K9180/K7680/K7280/K6680/K6580和X系列平台，请使用detect {disable |
enable}命令进行配置。
提示: 对于用户需配置的参数，详细信息请参阅“配置计算链路状态时各项权值”部分。
配置链路探测掩码/前缀
在LLB Profile配置模式下，使用以下命令配置链路探测时的掩码：
dynamic-extra-conf detect {netmask {A.B.C.D | num} | prefix prefix-len}
l
netmask {A.B.C.D | num} - 指定需要探测的IPv4类型目的IP网段。系统将对该IPv4网段的流量进行实
时监控，并根据监控统计结果进行流量负载均衡调整。系统支持两种格式，A.B.C.D 和num。A.B.C.D
的取值范围255.255.240.0到255.255.255.255，默认值为255.255.255.240；num的取值范围是20
到32，默认值为28。
l
prefix prefix-len - 指定需要探测的IPv6类型目的IP网段。系统将对该IPv6网段的流量进行实时监控，
并根据监控统计结果进行流量负载均衡调整。prefix-len 的取值范围是64到96，默认值为64。
在LLB Profile配置模式下，使用no dynamic-extra-conf detect { netmask | prefix }恢复参数默认
值。
对于SG-6000 K20803/K9180/K7680/K7280/K6680/K6580和X系列平台，请使用detect {netmask
{A.B.C.D | num} | prefixprefix-len} 命令进行配置。
配置带宽利用率阈值
指定接口带宽利用率阈值，在LLB Profile配置模式下，使用以下命令：
dynamic-extra-conf detect threshold value

<!-- 来源页 2077 -->
l
value – 指定接口带宽利用率阈值。当接口的带宽利用率没有超过阈值时，系统将只分析链路的时延、
抖动、丢包状况来动态调整选路的方法；当接口的带宽利用率超过阈值时，系统将同时分析各链路上
“带宽利用率”这一参数来调整选路方法。value的取值范围为1至100（1%-100%），默认为60%。
在LLB Profile配置模式下，使用no dynamic-extra-conf detect threshold恢复参数默认值。
对于SG-6000 K20803/K9180/K7680/K7280/K6680/K6580和X系列平台，请使用detect
threshold value命令进行配置。
配置计算链路状态时各项权值
型号说明：SG-6000 A系列、K系列（除K20803/K9180/K7680/K7280/K6680/K6580之
外的所有型号）和云·界平台仅支持通过CLI命令进行配置。
指定链路Cost值的影响因子。影响因子是用于计算链路Cost值的参数，包括链路的延迟、抖动、丢包率和带
宽权重，即链路的延迟、抖动、丢包率和带宽对链路Cost值的影响占比。用户可以选择预定义影响因子，也
可以配置自定义影响因子。
dynamic-extra-conf detect weight-factors {predefine {delay-template | jitter-template |
loss-template} | delay-factor jitter-factor loss-rate-factor BW-rate-threshold-factor [BWrate-factor]}
l
delay-template - 该项中延迟、抖动、丢包率和带宽权重分别为10、2、4、1，即链路时延对链路
Cost值的影响占比最大。
l
jitter-template - 该项中延迟、抖动、丢包率和带宽权重分别为1、10、4、1，即链路抖动对链路
Cost值的影响占比最大。
l
loss-template - 该项中延迟、抖动、丢包率和带宽权重分别为1、2、10、1，即链路丢包率对链路
Cost值的影响占比最大。
l
delay-factor - 指定链路时延的占比。取值范围是0到15，默认值是1。
l
jitter-factor - 指定链路抖动的占比。取值范围是0到15，默认值是2。
l
loss-rate-factor - 指定链路丢包率的占比。取值范围是0到15，默认值是4。
l
BW-rate-threshold-factor - 指定链路带宽利用率超过阈值时，带宽利用率的占比。取值范围是0到
15，默认值是1。
l
BW-rate-factor - 指定链路当前带宽利用率的占比。取值范围是0到15，默认值是1。
在LLB Profile配置模式下，使用no dynamic-extra-conf detect weight-factors恢复参数默认值。

<!-- 来源页 2078 -->
对于SG-6000 K20803/K9180/K7680/K7280/K6680/K6580和X系列平台，请使用detect weightfactors {predefine {delay-template | jitter-template | loss-template} | delay-factor jitterfactor loss-rate-factor BW-rate-threshold-factor [BW-rate-factor]} 命令进行配置。
配置链路权重刷新时间
指定更新链路各项权重的间隔时间，在LLB Profile配置模式下，使用以下命令：
dynamic-extra-conf detect weight-update-interval value
l
value - 指定更新系统链路状态权重的间隔时间。取值范围是1到300秒，默认值是1秒。
在LLB Profile配置模式下，使用no dynamic-extra-conf detect weight-update-interval恢复参数默
认值。
对于SG-6000 K20803/K9180/K7680/K7280/K6680/K6580和X系列平台，请使用detect weightupdate-interval value命令进行配置。
配置子网条目最大值
配置LLB Profile子网条目的最大数目，在LLB Profile配置模式下，使用以下命令：
dynamic-extra-conf detect max-entry-number value
l
value – 指定系统可配置LLB profile子网条目的最大数值。默认值依据平台不同而不同，请以实际为
准。
在LLB Profile配置模式下，使用no dynamic-extra-conf detect max-entry-number恢复参数默认
值。
对于SG-6000 K20803/K9180/K7680/K7280/K6680/K6580和X系列平台，请使用detect max-entrynumber value命令进行配置。
配置会话保持方法
指定负载均衡的会话保持方法。通过配置会话保持方法，系统将符合会话保持条件的流量，都保持到同一条
链路进行转发。在LLB Profile配置模式下，使用以下命令配置会话保持方法：
persistence method {dst-ip | src-dst-ip | src-ip}
l
src-ip - 对于来自同一客户端的流量，选择同一条链路进行转发。
l
src-dst-ip - 对于来自同一客户端且目的地址相同的流量，选择同一条链路进行转发。
l
dst-ip - 对于目的地址相同的流量，选择同一条链路进行转发。
在LLB Profile配置模式下，使用no persistence method命令删除会话保持方法。

<!-- 来源页 2079 -->
注意: 为出站流量选择出口链路时，先匹配会话保持。若匹配到了会话保持表中的链路，即使该链
路处于繁忙状态，设备仍然使用该链路转发流量。
配置会话保持超时时间
指定会话保持的超时时间。超过指定的时间值，设备将清除相应的会话保持表信息。在LLB Profile配置模式
下，使用以下命令配置会话保持超时时间：
persistence timeout value
l
value - 指定会话保持的超时时间。取值范围是60到65535秒，默认值是300秒。
在LLB Profile配置模式下，使用no persistence timeout命令恢复会话超时时间的默认值。
配置链路繁忙保护
型号说明：仅SG-6000 A系列、K系列（除K20803/K9180/K7680/K7280/K6680/K6580
之外的所有型号）、云·界平台支持该功能。
用户可以为出口链路配置繁忙保护，即配置接口的实际带宽值和带宽阈值。当某条链路的出口流量达到接口
指定的带宽阈值时，若系统通过负载均衡算法为流量选择出口链路，则将优先选择其他不繁忙的链路；当系
统通过会话保持算法为流量选择出口链路时，若匹配到了相应的会话保持表项，则忽略链路繁忙保护功能，
选择匹配到的链路转发流量。
在接口配置模式下，使用以下命令：
bandwidth {downstream | upstream} {threshold value| bandwidth}
l
downstream - 配置接口下行方向上的最大带宽值与带宽阈值。
l
upstream - 配置接口上行方向上的最大带宽值与带宽阈值。
l
threshold value - 指定接口的带宽阈值。取值范围是0到100（0%到100%），默认值是0，表示不限
制。
l
bandwidth - 指定接口的最大带宽值。范围是512,000 到1000,000,000,000bps。默认值是
1000,000,000bps。
在接口配置模式下，使用no bandwidth {downstream | upstream} [threshold]命令恢复接口的最大带
宽和带宽阈值的默认值。

<!-- 来源页 2080 -->
注意: 非根VSYS不支持该配置。
指定记录日志信息
当链路的带宽利用率超过指定的限制值时，系统将会记录日志信息。指定记录日志信息，使用以下命令：
log enable [utilization-limit utilization-limit]
l
utilization-limit utilization-limit - 指定链路带宽利用率的限制值，范围是1到100，默认值为90。
用户取消记录日志信息，使用命令：no log enable。
配置数据流量的方向
系统计算负载均衡的带宽利用率时，需配置数据流量的方向。对于SG-6000 A系列、K系列（除
K20803/K9180/K7680/K7280/K6680/K6580之外的所有型号）和云·界平台，仅当均衡算法为“最小带
宽（ least-bandwidth）或加权最小带宽（weighted-least-bandwidth）”时，该配置生效。
在LLB Profile配置模式下，使用以下命令配置数据流量的方向：
dynamic-extra-conf bandwidth-balance-direction {bidirection | downstream | upstream}
l
bidirection – 系统将取数据流的入和出两个方向上带宽利用率较大的值与带宽利用率阈值进行比较，进
而调整选路方法。
l
downstream – 系统将取数据流的入方向上的带宽利用率的值与带宽利用率阈值进行比较，进而调整选
路方法。该参数为默认方向。
l
upstream - 系统将取数据流出方向上带宽利用率的值与带宽利用率阈值进行比较，进而调整选路方
法。
使用no dynamic-extra-conf bandwidth-balance-direction恢复默认模式。
对于SG-6000 K20803/K9180/K7680/K7280/K6680/K6580和X系列平台，请使用bandwidthbalance-direction {bidirection | downstream | upstream}命令进行配置。
配置负载均衡模式
用户配置负载均衡的模式，使用以下命令：
dynamic-extra-conf mode {compatibility [upper-limit value lower-limit value] |
performance}
l
compatibility – 配置负载均衡模式为高兼容模式。当链路负载变动时，系统不会频繁地切换链路，而
是优先保证业务尽量在原有链路上。此模式多适用于对链路切换比较敏感的业务，如银行业务。upper-

<!-- 来源页 2081 -->
limit value表示上行流量带宽利用率阈值，lower-limit value表示下行流量带宽利用率阈值。upperlimit和lower-limit的取值范围是1到100（1%到100%）
l
performance –配置负载均衡为高性能模式，此模式下系统会跟据链路实时的时延、抖动、丢包情况，
迅速调整以最大限度的保持链路负载均衡。该模式为默认模式。
使用no dynamic-extra-conf mode恢复默认模式。
对于SG-6000 K20803/K9180/K7680/K7280/K6680/K6580和X系列平台，请使用mode
{compatibility [upper-limit value lower-limit value] | performance}命令进行配置。
配置负载均衡描述信息
用户配置负载均衡的描述信息，使用以下命令：
description description
l
description – 配置LLB Profile的描述信息。
用户取消配置描述信息，使用命令：no description。
配置链路主动探测间隔
配置链路主动探测间隔，即系统针对指定host发送探测数据包的时间间隔，使用以下命令：
host-detect interval interval
l
interval- 指定链路探测间隔时间，范围是60到86400秒，默认为600秒。
使用该命令no的形式恢复链路主动探测的时间间隔默认值：
no host-detect interval
查看指定域名的链路探测结果
查看指定域名进行链路探测的结果，在任意模式下，使用以下命令：
show llb rule rule-name spec-host task {all | host-name} [slot slot-number]
l
rule-name – 指定LLB规则名称。
l
spec-host task { all | host-name} - 查看根据指定域名进行链路探测的结果。
l
all- 查看LLB规则中所有域名的链路探测结果。
l
host-name- 指定域名，查看该域名的链路探测结果。
l
slot slot-number - 指定模块卡所在的槽位号，查看该模块卡上根据所有域名（all）或者指定域名
（host-name）的链路探测结果。仅X系列设备支持此参数。

<!-- 来源页 2082 -->
查看调度策略配置信息
查看调度策略配置信息，在任意模式下，使用以下命令：
show llb profile [profile-name]
l
profile-name – 查看指定名称的调度策略配置信息。如不指定，则查看所有调度策略配置信息。
查看带宽统计周期
查看系统当前的带宽统计周期，在任意配置模式下，使用以下命令：
show llb bandwidth-statistics-period
查看LLB规则的相关统计信息
查看LLB规则的相关统计信息，在任意配置模式下，使用以下命令：
show statistics llb [slot slot-number] rule rule-name
l rule-name – 指定LLB规则名称。
l slot slot-number - 指定模块卡所在的槽位号，查看该模块卡上的LLB规则的相关统计信息。
型号说明：仅SG-6000-X系列设备支持此参数。
配置SLA模板
型号说明：
l
不支持：K20803、K9180、K7680、K7280、K6680、K6580。
l
不支持：X系列平台。
开始之前
l 阅读出站负载均衡"介绍" 在第2062页。
l 阅读"出站负载均衡处理流程" 在第2062页。
l 阅读"链路负载均衡算法" 在第2066页介绍。
SLA（服务等级协议）是衡量网络链路服务质量等级的标准。它通过采集链路延迟、抖动和丢包率等关键性
能指标，评估链路在稳定性、响应速度及数据完整性等方面的质量。同时，系统将实时的链路状态与预设的

<!-- 来源页 2083 -->
SLA 标准进行对比，动态判断链路是否符合当前的服务质量等级。在链路负载均衡（LLB）的应用中，SLA
被用于实时评估链路状态，并作为流量调度与链路选择的关键判断依据。LLB 若仅按ISP、带宽或连接数等
方式进行流量分配，可能将业务流量引导至质量较差的链路，影响传输效率。而通过引入SLA，LLB 可优先
选择符合服务质量等级的链路进行流量分发，确保业务流量始终运行在满足性能要求的链路上，从而提升链
路资源利用率和保障业务连续性。
LLB 若仅依赖带宽或连接数进行流量分配，可能将业务流量引导至质量较差的链路，影响传输效率。而通过
引入SLA，LLB 可优先选择符合服务质量等级的链路进行流量分发，确保业务流量始终运行在满足性能要求
的链路上，从而提升链路资源利用率和保障业务连续性。
注意: 若一条LLB规则同时绑定了调度策略和SLA模板，则仅当调度策略的首选调度算法、二级调
度算法或备选调度算法中任一选项采用“动态就近”算法时，SLA模板才会生效。
通过Session Rematch 保障业务连续性
由于设备默认启用了session rematch机制，能够在LLB 链路状态更新时动态调整会话转发路径，确保其
始终匹配当前最优有效路径。这种机制能保持会话连续性，避免因路径变化导致的连接中断，尤其适用于视
频直播、在线会议等对实时性要求较高的场景。
注意: 在VPN 多隧道负载均衡场景中，当LLB 探测到某隧道链路质量不达标时，系统不会触发
session rematch机制，已建立的业务会话将维持原隧道转发，不切换至其他隧道。
关闭NAT场景下的Session Rematch
针对企业核心业务（如OA 系统、财务平台）部署在公网服务器（如云服务器）的场景，内网用户需通过
NAT 将内网地址转为公网地址，才能访问这类公网业务。当其通过某链路访问时，业务平台会记录当前
NAT 分配的公网IP，并以此为身份标识维持会话连接；若该链路出现质量波动，session rematch 机制使
系统用新的公网IP去访问业务平台，建立新的会话连接。这就导致了原来的登录失效、文件传输中断、操作
流程需重新建立等问题。
如需保障NAT 场景下的会话连续性，可通过命令关闭NAT 会话的session rematch。关闭后，无论原链
路质量如何、是否满足SLA 规定标准，NAT 会话均不会触发链路切换，始终使用原链路的公网IP 访问业务
平台，原有会话持续有效。
配置SLA Profile
新建或配置SLA Profile，在全局配置模式下，使用以下命令：
sla-profile profile-name

<!-- 来源页 2084 -->
l
profile-name – 指定SLA Profile的名称。执行该命令后，系统创建指定名称的SLA Profile，并且进
入该SLA Profile配置模式；如果指定的名称已存在，则直接进入SLA Profile配置模式。
在全局配置模式下，使用no sla-profile profile-name命令删除指定的SLA Profile。
关闭和开启SLA功能
开启SLA功能后，系统才会基于SLA Profile的配置，进行链路质量探测和路径选择。默认情况下，SLA功能
为开启状态。关闭或开启SLA功能，在SLA Profile配置模式下，使用以下命令：
sla-status {disable | enable}
l
disable – 关闭SLA功能。
l
enable – 启用SLA功能。
配置探测模式
SLA探测模式包含被动探测模式和主动探测模式：
l
被动探测模式：通过对出口链路中的TCP流量进行采样，获取链路的延迟、抖动和丢包率质量参数。该模
式为默认模式。
l
主动探测模式：由链路出接口主动向指定的目的地址发送探测报文，获取链路的延迟、抖动和丢包率质
量参数。当选择此模式时，用户需要在后续配置项中分别指定探测报文的协议类型、目的地址、探测间
隔和发包数。
指定探测模式为被动探测模式，在SLA Profile配置模式下，使用以下命令：
detect-mode passive type {ipv4 | ipv6}
l
ipv4 | ipv6 - 指定被动探测的IP类型，可为IPv4类型和IPv6类型，默认为IPv4类型。
指定探测模式为主动探测模式，在SLA Profile配置模式下，使用以下命令：
detect-mode active type {ipv4 protocol {icmp | tcp port port-number} | ipv6 protocol {icmp6 |
tcp port port-number}} [interval num [number num]]
l
ipv4 protocol {icmp | tcp port port-number} - 指定主动探测模式为IPv4类型。同时配置发送探测
报文的协议类型，可以为ICMP或者TCP，默认为ICMP。指定TCP时需要同时输入端口号。
l
ipv6 protocol {icmp6 | tcp port port-number - 指定主动探测模式为IPv6类型。同时配置发送探测
报文的协议类型，可以为ICMPV6或者TCP，默认为ICMPV6。指定TCP时需要同时输入端口号。

<!-- 来源页 2085 -->
l
interval num - 指定主动探测模式时探测报文的发送时间间隔，取值范围是2到5秒，默认值为2。
l
number num - 指定主动探测模式时探测报文的单次发送数量，取值范围是5到10，默认值为5。
配置主动探测地址或域名
在主动探测模式下，指定1 至2 个探测报文的目的地址，支持IP 地址（IPv4/IPv6）或域名形式。设置多
个探测目标地址，可避免因单一服务器异常导致链路状态误判，从而更准确地评估链路的实际健康状况。若
指定2个探测报文的目的地址，任何一个探测成功，均表示链路正常。
配置探测地址或域名，在SLA Profile配置模式下，使用以下命令：
detect-object {domain domain-name | ip ipv4-address | ipv6 ipv6-address}
l
domain domain-name - 指定探测报文的目的域名地址，最多支持指定2个域名。
l
ip ipv4-address - 指定探测报文的目的IPv4地址，最多支持指定2个IP地址。
l
ipv6 ipv6-address - 指定探测报文的目的IPv6地址，最多支持指定2个IP地址。
在SLA Profile配置模式下，使用no detect-object {domain domain-name| ip ipv4-address | ipv6
ipv6-address}命令删除配置的探测地址。
开启或关闭SLA阈值
在SLA Profile 配置模式下，通过以下命令控制SLA 各探测项（延迟、抖动、丢包率）的阈值开关：
l
关闭延迟阈值：sla-delay-disable （关闭后即不进行链路延迟探测）
l
关闭抖动阈值：sla-jitter-disable （关闭后即不进行链路抖动探测）
l
关闭丢包率阈值：sla-lossrate-disable （关闭后即不进行链路丢包率探测）
使用以上命令的no命令（如no sla-delay-disable），可开启对应探测项的阈值开关，恢复该链路指标的
探测。
配置SLA阈值
配置SLA阈值，在SLA Profile配置模式下，使用以下命令：
threshold {delay-thres num | jitter-thres num | lossrate-thres num}
l
delay-thres num - 指定SLA延迟阈值。取值范围是0到100000毫秒，默认值为5，0表示不进行链路
延迟探测。
l
jitter-thres num - 指定SLA抖动阈值。取值范围是0到100000毫秒，默认值为5，0表示不进行链路抖
动探测。

<!-- 来源页 2086 -->
l
lossrate-thres num - 指定SLA丢包率阈值。取值范围是0到100（0%-100%），默认值为5，0表示
不进行链路丢包率探测。
在SLA Profile配置模式下，使用no threshold {delay-thres| jitter-thres | lossrate-thres}命令取消配
置的SLA阈值，恢复默认值。
配置激活所需成功次数
配置链路从失活状态切换至活跃状态的累计成功探测次数。系统仅对已开启的探测项（延迟、抖动、丢包
率）进行检测，并与预设SLA阈值比对，仅当所有已开启的探测项均满足阈值要求（即全部符合质量要求）
时，计为1次成功探测。当累计成功探测次数达到或超过配置值时，链路状态由失活转为活跃，成为可用出
口链路。
配置激活所需成功次数，在SLA Profile配置模式下，使用以下命令：
activation num
l
num - 配置链路从失活状态变为活跃状态需要的激活成功次数。取值范围是1到100，默认值为5。
在SLA Profile配置模式下，使用no activation 命令取消配置的激活所需成功次数，恢复默认值。
配置退出激活所需失败次数
配置链路从活跃状态切换至失活状态的累计失败探测次数。系统仅对已开启的探测项（延迟、抖动、丢包
率）进行检测，并与预设SLA阈值比对，只要任意一项已开启的探测项不满足阈值要求（即不符合质量要
求），即计为1次失败探测。当累计失败探测次数达到或超过配置值时，链路状态由活跃转为失活，不再作
为可用出口链路。
配置退出激活所需失败次数，在SLA Profile配置模式下，使用以下命令：
inactivation num
l
num - 配置链路从活跃状态变为失活状态需要的退出激活失败次数。取值范围是1到100，默认值为5。
在SLA Profile配置模式下，使用no inactivation 命令取消配置的退出激活所需失败次数，恢复默认值。
开启/关闭NAT场景下的Session Rematch
针对企业核心业务（如OA 系统、财务平台）部署在公网服务器（如云服务器）的场景，内网用户需通过
NAT 将内网地址转为公网地址，才能访问这类公网业务。当其通过某链路访问时，业务平台会记录当前
NAT 分配的公网IP，并以此为身份标识维持会话连接；若该链路出现质量波动，session rematch 机制使
系统用新的公网IP去访问业务平台，建立新的会话连接。这就导致了原来的登录失效、文件传输中断、操作
流程需重新建立等问题。如需保障NAT 场景下的会话连续性，可通过命令关闭NAT 会话的session
rematch。

<!-- 来源页 2087 -->
默认情况下，系统会对NAT会话和非NAT会话统一执行session rematch操作。开启/关闭NAT场景下的
session rematch，在全局配置模式下，使用以下命令：
l
开启（默认状态）：no nat-rematch disable
l
关闭：nat-rematch disable
查看SLA Profile配置信息
查看SLA Profile配置信息，在任意模式下，使用以下命令：
show sla-profile [profile-name]
l
profile-name – 查看指定名称的SLA Profile配置信息。如不指定，则查看所有SLA Profile配置信
息。
配置LLB规则
开始之前
l 阅读出站负载均衡"介绍" 在第2062页。
l 阅读"出站负载均衡处理流程" 在第2062页。
l 阅读"链路负载均衡算法" 在第2066页介绍。
前置条件
l 请提前完成接口的链路配置，以确保系统可以根据接口配置的链路负载均衡优先级、权值、带宽阈值等
信息实现智能选路。详见“接口> 配置接口”章节说明。
l 请提前完成调度策略配置，以确保在配置LLB规则时可以直接引用需要的调度策略。
l 如果需要基于自定义的链路质量标准（延迟、抖动和丢包率），对业务流量的出口链路进行筛选，请提前配置
SLA模板（SLA Profile），以确保在配置LLB规则时可以直接引用需要的SLA模板。
配置LLB规则
将SLA模板（可选）、调度策略与路由绑定形成LLB规则，以实现对出站链路流量的控制和负载均衡。目前
支持绑定有目的路由（DBR）和策略路由(PBR)。配置LLB规则，在全局模式下，使用以下命令：
llb rule rule-name [ipv6] {pbr pbr-name id match-id | dbr [vrouter vr-name] {{X:X:X:X::X/M}
| {A.B.C.D/M | A.B.C.D A.B.C.D}} {profile profile-name} [sla-profile profile-name] [host hostbook-name]

<!-- 来源页 2088 -->
l
rule-name – 指定LLB规则名称。
l
ipv6– 指定配置的LLB rule为IPv6类型。若不指定，则LLB rule为IPv4类型。
l
pbr pbr-name – 指定策略路由名称。
l
id match-id – 配置策略路由id。需根据LLB规则配置的IP类型选择同类型的策略路由规则。
l
dbr vroutervr-name – 指定目的路由的Vrouter。
l
{X:X:X:X::X/M} | {A.B.C.D/M | A.B.C.D A.B.C.D} – 指定Vrouter目的地址。当LLB规则配置为IPv6
类型时，使用X:X:X:X::X/M方式指定IPv6目的地址。当LLB规则配置为IPv4类型时，设备支持使用两
种方式指定IPv4目的地址，A.B.C.D/M或者A.B.C.D A.B.C.D，例如1.1.1.0/24或者1.1.1.0
255.255.255.0。
l
profile profile-name – 绑定指定的调度策略。需根据LLB规则配置的IP类型选择同类型的调度策略。
l
sla-profile profile-name - 绑定指定的SLA Profile。需根据LLB规则配置的IP类型选择同类型的SLA
Profile。对于A系列平台、K系列平台（K20803/K9180/K7680/K7280/K6680/K6580除外）、云·
界平台以及SD-WAN平台，仅当调度策略的首选调度算法、二级调度算法或备选调度算法中任一选项采
用“动态就近”算法时，SLA模板才会生效。
l
host host-book-name - 绑定指定的域名簿。
在全局配置模式下，使用no llb rule llb-rule-name命令删除指定的LLB规则。
注意: IPv4类型的LLB规则和IPv6类型的LLB规则不允许重名。
查看LLB规则配置信息
查看LLB规则配置信息，在任意模式下，使用以下命令：
show llb rule [rule-name]
l
rule-name – 查看指定名称的LLB规则配置信息。如不指定，则查看所有LLB规则配置信息。
入站负载均衡
对入站流量启用负载均衡功能后，系统可以根据DNS请求的来源将域名解析成不同的IP地址，并将不同的
ISP所对应的IP地址返回给相应的请求用户，从而达到减少跨ISP访问的目的。这种解析方式被称为智能域名
解析（SmartDNS）。
用户可通过以下步骤启用入站负载均衡功能：

<!-- 来源页 2089 -->
1. 启用SmartDNS。启用该功能是实现入站负载均衡的前提条件。默认情况下，SmartDNS功能为启用状态。
2. 配置SmartDNS规则表。系统根据SmartDNS规则表的匹配规则对源自不同链路的DNS请求返回不同的IP地址。
配置入站负载均衡
启用SmartDNS功能
默认情况下，SmartDNS功能为启用状态。禁用或启用该功能，在全局配置模式下，使用以下命令：
llb inbound smartdns {disable | enable}
l
disable – 禁用SmartDNS功能。
l
enable – 启用SmartDNS功能。
配置SmartDNS规则表
SmartDNS规则表的配置包括创建规则表以及在规则表中指定域名、返回IP地址和匹配规则。系统根据匹配
规则将域名解析为不同ISP链路对应的IP地址。
创建SmartDNS规则表
创建SmartDNS规则表，在全局配置模式下，使用以下命令：
llb inbound smartdns name
l
name – 新建一个SmartDNS规则表，并进入SmartDNS规则表配置模式。如果指定的名称已存在，则
直接进入到该SmartDNS规则表的配置模式。系统最多支持2500个SmartDNS规则表。
在全局配置模式下，使用该命令的no形式删除指定的SmartDNS规则表：
no llb inbound smartdns name
指定域名
指定需要被智能解析的域名，在SmartDNS规则表配置模式下，使用以下命令：
domain domain-name
l
domain-name – 指定需要被智能解析的域名。取值范围是1到255个字符。
重复使用以上命令向SmartDNS规则表中添加多个域名。每个规则表最多支持64个不同的域名（不区分大小
写）。
在SmartDNS规则表配置模式下，使用该命令的no形式从规则表中删除指定的域名：
no domain domain-name

<!-- 来源页 2090 -->
指定返回IP地址
用户可以对不同ISP链路上的请求指定不同的返回IP地址。系统判断请求来源的依据是ISP路由中的地址簿
（ISP静态地址簿）。如果请求源地址匹配上述地址簿中的地址条目，则系统返回指定的IP地址。在
SmartDNS规则表配置模式下，使用以下命令：
ip ip-address isp isp-name [interface interface-name] [weight value]
l
ip-address – 指定返回的IP地址。用户可以为一个域名最多配置64个IP地址。
l
isp isp-name – 指定请求源地址需要匹配的ISP名称。当请求源地址匹配该ISP中的地址条目，系统返
回指定的IP地址（ip ip-address）。isp-name为系统中预定义或用户自定义的ISP名称。每个ISP名称
最多可以对应16个IP地址。
l
interface interface-name – 为返回IP地址指定入站接口。系统将根据入站接口的监测结果或入站接
口协议状态来判断返回IP地址是否有效，系统只返回有效的IP地址给请求源。当入站接口上配置了监测
对象，若监测成功，则返回IP地址有效；否则IP地址无效。当入站接口没有配置监测对象，若该接口的
协议状态为UP，则返回IP地址有效；否则IP地址无效。若用户不配置入站接口，返回IP地址始终有效。
l
weight value – 指定返回IP地址的权重。取值范围是1到100，默认值为1。SmartDNS规则表中一个
域名可能对应多个IP地址，系统会根据权重值对IP地址进行排序后返回给用户。
在SmartDNS规则表配置模式下，使用该命令的no形式从规则表中删除指定的IP地址：
no ip ip-address
注意:
l
用户无法删除正在被SmartDNS规则表引用的ISP路由。有关ISP路由的更多信息，请参考《路
由》的“ISP路由”部分。
l
在完成域名、返回IP地址等配置之前，新建的SmartDNS规则表处于禁用状态。
查看链路负载均衡信息
查看出站方向链路负载均衡的配置信息
查看出站方向链路负载均衡的配置信息，在任意模式下，使用以下命令：
show llb {profile [profile-name]| rule [rule-name]}

<!-- 来源页 2091 -->
l
profile [profile-name] – 查看出站方向链路负载均衡模板。profile-name为模板名称。
l
rule [rule-name] – 查看出站方向链路负载均衡的规则。rule-name为规则名称。
查看入站方向的负载均衡及SmartDNS规则表的配置信息
查看入站方向的负载均衡及SmartDNS规则表的配置信息，在任意模式下，使用以下命令：
show llb inbound [smartdns name]
l
inbound – 查看入站方向链路负载均衡的配置信息。
l
smartdns name – 指定SmartDNS规则表的名称。
例如，使用show llb inbound smartdns test命令查看系统中名为test的SmartDNS规则表的配置信息。
以下是一个返回结果示例：
hostname# show llb inbound smartdns test
domain:domain name; IP: ip address; ISP: isp name; IF: interface;
PROXY: proximity address book status; E: enable; D:disable
TRACK: track object name; W: ip weight; S:ip status;A:active; I: inactive
=========================================================================
-------------------------------------------------------------------------
table name: test（SmartDNS规则表名称）
table status: enable（SmartDNS规则表状态）
domain count: 1（域名数量）
rule count: 1（域名解析规则数量）
domains: www.test.com;（需要被智能解析的域名）
ip addresses:
-------------------------------------------------------------------------
IP ISP IF PROX TRACK W S
1.1.1.1 China-telecom ethernet0/1 E 1 I
=======================================================================

<!-- 来源页 2092 -->
l
有关TRACK列下监测对象的更多信息，请参考《系统管理》的“配置监测对象”部分。
l
S列下所显示规则状态可能为活跃（active）或非活跃（inactive），由接口及接口上的监测对象决定：
l
如果只配置了引用的ISP路由（isp isp-name）但没有配置接口（interface interfacename），规则状态始终为活跃；
l
如果配置了接口（interface interface-name）但接口上没有配置监测对象，接口的协议状态为
可用（UP）时规则状态为活跃，协议状态为不可用（DOWN）时规则状态为非活跃；
l
如果配置了接口（interface interface-name）且接口上配置了监测对象，监测成功时规则状态
为活跃，监测失败时规则状态为非活跃。
例：链路负载均衡配置举例
本节介绍一个入站链路负载均衡功能的配置举例。
组网需求
设备的ethernet0/6和ethernet0/7两个接口分别连接电信和网通的两条线路。配置入站链路负载均衡功能
后，设备对电信用户发送的DNS请求返回电信ISP静态地址簿中所对应的IP地址，对网通用户所发送的DNS
请求返回网通静态ISP地址簿中所对应的IP地址。组网图如下图所示：
配置步骤
以下配置步骤略去接口配置，重点描述ISP信息和入站链路负载均衡功能的相关配置。
第一步：配置ISP信息：
hostname(config)# isp-network telecom
hostname(config-isp)# 101.1.1.0/24
hostname(config-isp)# exit

<!-- 来源页 2093 -->
hostname(config)# isp-network netcom
hostname(config-isp)# 201.1.1.0/24
hostname(config-isp)# exit
第二步：启用SmartDNS功能并配置SmartDNS规则表：
hostname(config)# llb inbound smartdns enable
hostname(config)# llb inbound smartdns test
hostname(config-llb-smartdns)# domain www.test.com
hostname(config-llb-smartdns)# ip 100.1.1.2 isp telecom interface ethernet0/0
weight 10
hostname(config-llb-smartdns)# ip 200.1.1.2 isp netcom interface ethernet0/1
weight 10
hostname(config-llb-smartdns)# exit
第三步：使用show命令确认上述配置已经生效：
hostname(config)# show isp-network all
ISP telecom status: Active
Binding to nexthop: 0
Subnet(IP/Netmask): 1
101.1.1.0/24
ISP netcom status: Active
Binding to nexthop: 0
Subnet(IP/Netmask): 1
201.1.1.0/24
hostname(config)# show llb inbound smart test
domain:domain name; IP: ip address; ISP: isp name; IF: interface;
PROXY: proximity address book status; E: enable; D:disable
TRACK: track object name; W: ip weight; S:ip status;A:active;
I: inactive
==================================================================
-------------------------------------------------------------------------

<!-- 来源页 2094 -->
name: test
domain count: 1
rule count: 2
status: enable
domains: www.test.com;
ip addresses:
-------------------------------------------------------------------------
ID IP ISP IF PROX TRACK W S
1 100.1.1.2 telecom ethernet0/0 D 10 A
3 200.1.1.2 netcom ethernet0/1 D 10 A
===================================================================
此时PC1请求域名www.test.com，设备会返回电信的IP地址100.1.1.2；PC2请求域名www.test.com，
设备会返回网通的IP地址200.1.1.2。

<!-- 来源页 2095 -->
会话限制
设备支持基于安全域的会话限制功能。用户可以对安全域内的源IP地址、目的IP地址、指定的IP地址、应用
或角色/用户/用户组进行会话数量或者建立会话速率控制，从而保护连接表不被DoS攻击填满，并且能够在
一定程度上限制一些应用的带宽，如IM或者P2P等。
配置会话限制
配置会话限制功能
配置会话限制功能，在安全域配置模式下，使用以下命令：
ad session-limit [id id] {{src-ip address-entry dst-ip address-entry | ip address-entry }
[protocol protocol-id ] [application application-name] [role role-name | user aaa-servername user-name | user-group aaa-server-name user-group-name]} {session {unlimit | max
number [per-srcip | per-dstip | per-ip] | per-user} | ramp-rate [per-sec] max number}
[schedule schedule-name] [include-to-self] [log]
l
id id – 指定安全域的会话限制规则ID。
l
src-ip address-entry – 限制安全域的源IP地址会话数。address-entry为src-ip的IP地址范围。该参
数值为地址簿中定义的一条地址条目。
l
dst-ip address-entry – 限制安全域的目的IP地址会话数。address-entry为dst-ip的IP地址范围。
该参数值为地址簿中定义的一条地址条目。
l
ip address-entry – 限制安全域中某个IP地址段的会话数。address-entry为ip的IP地址范围。该参
数值为地址簿中定义的一条地址条目。
l
protocol protocol-id – 限制安全域中特定IP协议类型的会话数。protocol-id为ip的协议号，取值范
围为1到255。
l
application application-name – 限制安全域中特定应用的会话数。
l
role role-name – 限制特定角色的会话数。
l
user aaa-server-name user-name – 限制特定用户的会话数。aaa-server-name为用户所属的
AAA服务器名称，user-name为用户名称。
l
user-group aaa-server-name user-group-name – 限制特定用户组的会话数。aaa-servername为用户组所属的AAA服务器名称，user-name为用户组名称。

<!-- 来源页 2096 -->
l
blocklist block-type ip block-time value– 在IP限制模式为“每个IP”下，将单个IP添加到动态IP
黑名单中进行阻断并指定阻断时间。value为阻断时间。取值范围为60-1296000秒，默认情况下为60
秒。当单个IP的并发会话数/新建会话数达到会话限制阈值后，支持将该IP加入动态IP黑名单，系统将对
黑名单中的IP执行阻断操作，直到阻断时间结束。该配置在默认情况下为关闭状态。
l
session {unlimit | max number [per-srcip | per-dstip | per-ip] | per-user} – 指定IP地址或角色
的最大会话数。unlimit为无会话数限制。session max number指定地址条目中所有IP地址的最大会
话数或者角色对应的所有用户的最大会话数；如果使用per-srcip、per-dstip、per-ip或者per-user
关键字，则session max number指定的为每个IP地址的最大会话数或者角色对应的每个用户的最大
会话数。per-srcip、per-dstip、per-ip和per-user四个关键字需和前面的src-ip、dst-ip、ip和
role关键字一一对应，如：只有在前面指定了src-ip才可以在后面选择per-srcip。
l
ramp-rate max number – 指定IP地址或者角色每5秒钟可建立的最大会话数。
l
ramp-rate max per-sec number – 指定IP地址或者角色每秒种可建立的最大会话数。
l
schedule schedule-name – 指定会话限制规则的生效时间。
l
include-to-self - 指定对to-self流量进行会话限制，例如本机管理流量等。默认情况下，系统不对toself流量进行会话限制。
l
log– 指定记录会话限制日志。
注意: 会话限制功能支持IPv4地址和IPv6地址。如开启接口的IPv6功能，用户可配置IPv6类型的
地址条目。源地址条目与目的地址条目的地址类型需一致。
在安全域配置模式下，使用以下命令删除安全域的会话限制规则：
no ad session-limit id id
l
id id – 安全域的会话限制规则ID。可通过show session-limit命令获取相应规则的ID。
删除特定会话限制规则中被丢弃会话数的统计信息
配置会话限制功能后，超出最大会话数限制的会话将被丢弃，用户可以通过show session-limit命令查看
被丢弃的会话数统计信息。删除特定会话限制规则中被丢弃会话数的统计信息，请在任何置模式下使用以下
命令：
clear session-limit id id statistics
l
id id – 指定规则ID以删除特定会话限制规则中被丢弃的会话数统计信息。

<!-- 来源页 2097 -->
注意: 在设备上启用了Full-cone NAT功能后，会话限制中的目的IP地址指的是DNAT转换之前的
IP地址。有关Full-cone NAT功能的更多信息，请参考《防火墙》的“Full-cone NAT”部分。
会话限制显示
配置会话限制功能后，在任何模式下使用以下命令查看会话限制配置信息：
show session-limit

<!-- 来源页 2098 -->
流量配额
系统支持流量配额功能，可以对用户/用户组每天或者每月的流量配额进行限制和控制。当用户流量达到流量
配额规则模板限定的日配额或者月配额时，系统将阻断该用户的流量。
型号说明：
l
不支持：SG-6000-A7600、A6800，以及SG-6000-A系列ASIC防火墙。
l
不支持：SG-6000-K20803、K9180、K7680、K7280、K6680、K6580平台，以及SG-
6000-K系列ASIC防火墙。
l
不支持：SG-6000-X系列。
配置流量配额功能
通过CLI配置流量配额功能，请按照以下步骤进行操作：
1. 配置流量配额Profile，在流量配额Profile中指定用户流量的日配额、月配额。
2. 创建用户/用户组流量配额规则，在用户/用户组流量配额规则中指定限制的用户/用户组，并且将指定流量配额
Profile绑定到配额规则。
3. 在指定安全域下开启流量配额功能。
配置流量配额Profile
创建流量配额Profile，在全局配置模式下使用以下命令：
user-quota profile profile-name
l
profile-name - 指定所创建的流量配额Profile的名称，并且进入该流量配额Profile的配置模式。如果
指定名称已存在，则直接进入流量配额Profile配置模式。
使用no user-quota profile profile-name删除指定的流量配额Profile。
指定日配额
指定日配额，在流量配额Profile配置模式下，使用以下命令：
daily daily-value unit {KB |MB | GB | TB}

<!-- 来源页 2099 -->
l
daily-value – 指定流量日配额值，取值范围为1至65535。
l
unit {KB |MB | GB | TB}– 指定流量日配额值单位。
使用no daily 删除指定的流量日配额。
指定月配额
指定月配额，流量配额Profile配置模式下，使用以下命令：
monthly daily-value unit {KB |MB | GB | TB}
l
daily-value – 指定流量月配额值，取值范围为1至65535。
l
unit {KB |MB | GB | TB}– 指定流量月配额值单位。
使用no monthly 删除指定的流量月配额。
配置用户流量配额规则
创建用户流量配额规则，在全局配置模式下，使用以下命令：
user-quota user-rule rule-name
l
rule-name - 指定所创建的用户流量配额规则的名称，并且进入该用户流量配额规则的配置模式。如果
指定名称已存在，则直接进入用户流量配额规则配置模式。
使用no user-quota user-rule rule-name删除指定的用户流量配额规则。
指定用户流量配额规则限制用户
指定用户流量配额规则限制的用户，在用户流量配额规则配置模式下，使用以下命令：
user aaa-server-name user-name
l
aaa-server-name– 指定系统中已经配置的AAA服务器的名称。
l
user-name - 指定限制的用户名称。
在用户流量配额规则配置模式下，使用该命令no的形式删除指定的用户：
no user aaa-server-name user-name
绑定流量配额Profile到用户流量配额规则
绑定流量配额Profile到用户流量配额规则，在用户流量配额规则配置模式下，使用以下命令：
profile profile-name
l
profile-name - 指定绑定到用户流量配额规则的流量配额Profile的名称。

<!-- 来源页 2100 -->
在用户流量配额规则配置模式下，使用该命令no的形式取消流量配额Profile的绑定：
no profile
配置用户组流量配额规则
创建用户组流量配额规则，在全局配置模式下，使用以下命令：
user-quota group-rule group-name
l
group-name - 指定所创建的用户组流量配额规则的名称，并且进入该用户组流量配额规则的配置模
式。如果指定名称已存在，则直接进入用户组流量配额规则配置模式。
使用no user-quota group-rule group-name删除指定的用户组流量配额规则。
指定用户组流量配额规则限制用户组
指定用户组流量配额规则限制的用户组，在用户组流量配额规则配置模式下，使用以下命令：
user-group aaa-server-name group-name
l
aaa-server-name– 指定系统中已经配置的AAA服务器的名称。
l
group-name - 指定限制的用户组名称。
在用户流量配额规则配置模式下，使用该命令no的形式删除指定的用户组：
no user-group aaa-server-name group-name
绑定流量配额Profile到用户组流量配额规则
绑定流量配额Profile到用户组流量配额规则，在用户组流量配额规则配置模式下，使用以下命令：
profile profile-name
l
profile-name - 指定绑定到用户组流量配额规则的流量配额Profile的名称。
在用户组流量配额规则配置模式下，使用该命令no的形式取消流量配额Profile的绑定：
no profile
修改流量配额规则优先级
修改用户流量配额规则优先级
修改用户流量配额规则优先级，在全局配置模式下，使用以下命令：
user-quota user-rule rule-name [ move] { before name rule-name | after name rule-name |
top | bottom }

<!-- 来源页 2101 -->
l
rule-name – 指定需要修改优先级的用户流量配额规则名称。
l
before name rule-name – 指定用户流量配额规则修改后的优先级为某个规则名称之前。
l
after name rule-name – 指定用户流量配额规则修改后的优先级为某个规则名称之后。
l
top – 指定用户流量配额规则修改后的优先级为所有规则的首位。
l
bottom – 指定用户流量配额规则修改后的优先级为所有规则的末位。
修改用户组流量配额规则优先级
修改用户组流量配额规则优先级，在全局配置模式下，使用以下命令：
user-quota group-rule group-name [ move] { before name group-name | after name groupname | top | bottom }
l
group-name – 指定需要修改优先级的用户组流量配额规则名称。
l
before name group-name – 指定用户组流量配额规则修改后的优先级为某个规则名称之前。
l
after namegroup-name – 指定用户组流量配额规则修改后的优先级为某个规则名称之后。
l
top – 指定用户组流量配额规则修改后的优先级为所有规则的首位。
l
bottom – 指定用户组流量配额规则修改后的优先级为所有规则的末位。
开启/关闭安全域的流量配额功能
开启/关闭指定安全域的流量配额功能，请在安全域配置模式下使用以下命令：
l
开启流量配额功能：user-quota enable
l
关闭流量配额功能：no user-quota enable
重置用户累积流量
用户可以根据需要，重置统计的用户流量累积值，在全局配置模式下，使用以下命令：
user-quota reset [user-name ]{daily | monthly | all}
l
user-name - 指定需要重置累积流量的用户名称。
l
daily - 指定重置用户的日累积流量。
l
monthly - 指定重置用户的月累积流量。
l
all - 指定重置用户的所有累积流量值。
显示流量配额Profile信息
在任何模式下，输入以下命令显示流量配额profile信息：

<!-- 来源页 2102 -->
show user-quota profile
显示用户流量配额规则信息
在任何模式下，输入以下命令显示用户流量配额规则信息：
show user-quota user-rule
显示用户组流量配额规则信息
在任何模式下，输入以下命令显示用户组流量配额规则信息：
show user-quota group-rule
显示开启流量配额功能的安全域
在任何模式下，输入以下命令显示开启了流量配额功能的安全域信息：
show user-quota zone
显示用户流量配额统计信息
在任何模式下，输入以下命令显示用户流量配额统计信息：
show user-quota {user | user-group}[aaa-server-name user-name]

<!-- 来源页 2103 -->
接收队列预丢弃
当系统资源不足时，数据包进入系统后，可能会待在接收队列中等待处理的时间过长，对网络的时延影响较
大，一些上层应用的用户体验会变差。用户可以开启接收队列预丢弃功能，对缓存的报文进行选择丢包，释
放系统的部分资源的同时会引发应用重传报文，从而在系统压力比较大的时候改善用户体验。
配置接收队列预丢弃
配置接收队列预丢弃功能，在全局配置模式下，使用以下命令：
flow head-drop-packet low-water-mask value interval time
l
low-water-mask value - 指定接收队列预丢弃的低水位线阈值。指定后，在统计周期内，当系统处理
的数据包的个数高于此值时，系统会开始预丢弃部分数据包，以减少时延；低于此值时，则不丢包，防
止流量极低时误丢包。value的取值范围为0-500000，默认值为8192。
l
interval time - 指定统计周期。指定后，系统以此为周期统计处理的数据包个数，用于判断是否超过低
水位线阈值。单位：毫秒，取值范围为100-1000毫秒。
在全局配置模式下，使用命令no head-drop-packet关闭接收队列预丢弃功能。
显示接收队列预丢弃信息
配置接收队列预丢弃功能后，在任何模式下，使用以下命令查看接收队列预丢弃信息：
show flow head-drop-packet
