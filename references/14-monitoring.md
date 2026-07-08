# 监控

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 17  监控
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 2495 -->
17 监控
系统监控部分包含如下功能：
l "监控" 在第2494页：对设备数据进行统计，并以柱状图、折线图、表格等方式呈现出来，帮助用户通过统计数
据掌握设备状况，排查问题。
l "日志" 在第2539页：记录并输出设备的各种日志信息，分别是设备系统、威胁、会话、NAT、URL等。
l "NetFlow" 在第2591页：采集用户的入接口流量信息，通过服务器对流量的分析，实现对网络流量的检测、监
控以及流量计费等。

<!-- 来源页 2496 -->
监控
系统提供以下多种监控方式。
如设备开启IPv6功能，系统支持同时统计IPv4地址和IPv6地址的带宽、会话数、AD、URL和应用。支持
IPv6统计的监控包含：用户监控、应用监控、云应用监控、设备监控、URL访问、应用阻断、自定义监控。
l 用户监控：展现指定时间周期内（实时、最近1小时、最近1天、最近1月）不同用户的各类统计信息，包括用户
带宽流量和用户并发连接个数。
l 应用监控：展现指定时间周期内（实时、最近1小时、最近1天、最近1月）不同应用、应用的类别、应用的子分
类、应用的风险等级、应用技术、应用特征的各类统计信息，包括应用带宽流量和应用并发连接个数。
l 云应用监控：展现指定时间内不同云应用的使用统计信息，包括流量排名、并发连接。（仅支持WebUI方式）
l 共享接入监控：展现指定过滤条件（虚拟路由器、IP、接入数量）下接入终端的统计信息，包括用户的操作系
统、在线时间、上线时间和最后在线时间。
l 用户配额监控：展示用户流量配额的统计信息列表。
l 管道监控：展现指定周期内（实时、最近1小时、最近1天、最近1周、最近1月）的管道流量统计信息。（仅支持
WebUI方式）
l 系统监控：展现指定时间周期内（实时、最近1小时、最近1天、最近1月）的包括整机流量、接口流量、安全域
流量、在线IP数、CPU/内存状态、会话以及硬件状态统计信息。
l URL访问：系统配置URL过滤功能后，展现用户/IP、URL访问以及URL类别统计信息。
l 链路状态监控：链路状态监控是通过统计链路中特定接口的采样流量信息，包括延迟、丢包率、抖动、带宽利用
率，从而实现链路整体状态的监控和展示。
l 设备监控：展现所有识别的设备的厂商、类型、在线设备以及设备列表信息。
l 终端标签主机列表：用于展示智铠（EDR）平台同步给防火墙设备的终端信息以及ZTNA策略匹配的终端信息，
帮助用户快速掌握终端设备的详细状态，从而更好地进行网络安全管理和策略配置。
l 应用阻断：系统配置安全策略阻断应用功能后，展现被阻断的应用以及用户/IP统计信息。
l 关键字阻断：系统配置上网行为控制的文件内容过滤、网页关键字、邮件过滤、Web外发信息功能后，展现文件
内容关键字、网页关键字、邮件内容关键字、Web外发信息关键字阻断次数统计信息以及用户/IP统计信息。
l 认证用户：系统配置Web认证、单点登录、802.1x认证、SSL VPN、L2TP VPN等功能后，统计认证登录的用户
信息。
l 锁定用户：展现被锁定的用户信息，包括被锁定用户的名称、锁定时间、锁定时长以及可以执行的操作。

<!-- 来源页 2497 -->
l 锁定IP：展现被锁定的IP信息，包括被锁定IP地址、锁定时间、锁定时长以及可以执行的操作。
l 监控配置：开启或者关闭指定监控项目。
l 自定义监控：配置自定义监控统计集为用户提供更加灵活的统计信息查看方法。
l 长期监控：能够对设备的流量和会话进行持续监控统计和存储，满足用户对网络监控和诊断的需求。

<!-- 来源页 2498 -->
用户监控
用户监控用于统计属于特定用户、用户组、地址簿的数据量、数据包。如设备开启IPv6功能，系统支持IPv4
和IPv6地址的统计。
配置监控地址簿
监控地址簿用来储存需要统计地址簿流量的用户地址条目，即在全局地址簿中选择需要统计的地址条目。在
全局配置模式下，使用以下命令：
statistics address address-entry-name
l
address-entry-name – 指定地址条目名称。
使用该命令no的形式关闭基于指定地址的统计功能：
no statistics address address-entry-name
查看地址簿的监控统计信息
在任何模式下，使用以下命令查看地址簿的监控统计信息：
show statistics address [address-entry-name] [current | lasthour | lastday | lastmonth]
l
address-entry-name – 指定地址条目名称。如果不指定该参数，该命令将显示系统中所有被统计功能
所引用地址条目的流量统计信息。
l
current – 指定显示地址条目的即时流量统计信息。
l
lasthour – 指定显示地址条目前60分钟每30秒的流量统计信息。
l
lastday – 指定显示地址条目前24小时每10分钟的流量统计信息。
l
lastmonth - 指定显示地址条目前30天每天的流量统计信息。
配置内网监控地址簿
配置内网监控地址簿，系统会根据该地址簿对外网到内网中的流量进行匹配，并将匹配到的流量统计到内网
IP侧。在全局配置模式下，使用以下命令：
statistics-filter {address | ipv6-address} address-entry-name
l
address-entry-name – 指定地址条目名称。
使用该命令no的形式取消配置内网监控地址簿：
no statistics-filter {address | ipv6-address} address-entry-name

<!-- 来源页 2499 -->
查看内网地址簿的监控统计信息
在全局配置模式下，使用以下命令查看地址簿的监控统计信息：
show statistics-filter address {address | ipv6-address}
查看用户监控相关统计集统计信息
用户监控相关预定义统计集如下：
类别
名称
描述
用户监控
predef_user_bw
统计所有用户的流量。
predef_ztna_user_bw
统计所有ZTNA用户的流量。
predef_user_sess
统计所有用户的会话数。
predef_user_app_bw
统计所有用户下应用的流量。
predef_exstat_exstat_ip_bw
统计所选地址簿下用户的流量。
predef_exstat_exstat_ip_sess
统计所选地址簿下用户的会话数。
predef_exstat_exstat_app_bw
统计所选地址簿下应用的流量。
predef_exstat_exstat_app_sess
统计所选地址簿下应用的会话数。
statistics-set predef_dip_bw
统计所选目的IP地址的流量信息。
查看用户监控相关统计集信息，具体命令请参阅“查看统计集信息”。
非根VSYS同样支持用户监控，但是不支持地址簿监控。

<!-- 来源页 2500 -->
应用监控
基于应用的监控统计功能，可以统计指定应用的即时流量统计信息、前60分钟每30秒的流量统计信息、前
24小时每10分钟的流量统计信息和前30天每天的流量统计信息。如设备开启IPv6功能，系统支持IPv4和
IPv6地址的统计。
配置监控应用组
配置监控应用组，在全局配置模式下，使用以下命令：
statistics application-group application-group-name
l
application-group-name – 指定应用组名称。
使用该命令no的形式删除监控应用组指定应用组：
no statistics application-group application-group-name
查看基于应用的统计信息
在任何模式下，使用以下命令查看基于应用的流量统计信息：
show statistics application-group [application-group-name] [current | lasthour | lastday |
lastmonth]
l
application-group-name – 指定应用组名称。如果不指定该参数，该命令将显示系统中所有被流量
统计功能所引用应用组的流量统计信息。
l
current – 指定显示应用组的即时流量统计信息。
l
lasthour – 指定显示应用组前60分钟每30秒的流量统计信息。
l
lastday – 指定显示应用组前24小时每10分钟的流量统计信息。
l
lastmonth – 指定显示应用组前30天每天的流量统计信息。
查看应用监控相关统计集统计信息
应用监控相关预定义统计集如下：

<!-- 来源页 2501 -->
类别
名称
描述
应用监控
predef_app_bw
统计所有应用的流量。
predef_app_sess
统计所有应用的会话数。
predef_exstat_exstat_ip_bw
统计所选应用组下用户的流量。
predef_exstat_exstat_ip_sess
统计所选应用组下用户的会话数。
predef_exstat_exstat_app_bw
统计所选应用组下应用的流量。
predef_exstat_exstat_app_sess
统计所选应用组下应用的会话数。
statistics-set predef_dip_bw
统计所选目的IP地址的流量信息。
查看应用监控相关统计集信息，具体命令请参阅“查看统计集信息”。
非根VSYS同样支持应用监控，但是不支持应用组监控。

<!-- 来源页 2502 -->
共享接入监控
查看指定过滤条件下的终端接入监控信息，在任何模式下，使用以下命令：
show host share-access [ip ip-address | device-num number] [vrouter vrouter-name]
l
ip ip-address – 以源IP地址为条件进行过滤。系统显示指定IP地址的终端接入监控信息。
l
device-num number – 以共享接入数量为条件进行过滤。系统显示指定接入数量的终端接入监控信
息。
l
vrouter vrouter-name – 以VRouter为条件进行过滤。系统显示指定VRouter的终端接入监控信息。
系统监控
非根VSYS同样支持系统监控，但是不支持硬件状态监控。如设备开启IPv6功能，系统支持IPv4和IPv6地址
的统计。
查看接口的统计信息
在任何模式下，使用以下命令查看指定接口的流量统计信息：
show statistics interface-counter interface interface-name {second | minute | hour | day} [  
IPv4 | IPv6 | nonip]
l
interface-name – 指定接口名称。
l
second – 指定显示接口前60秒钟每秒的流量统计信息。
l
minute – 指定显示接口前60分钟每分钟的流量统计信息。
l
hour – 指定显示接口前24小时每小时的流量统计信息。
l
day– 指定显示接口前30天的流量统计信息。
l
IPv4 | IPv6 | nonip - 指定显示接口的IPv4、IPv6地址类型的流量或者非IP数据包的流量。如不指定该
参数，将会默认统计全部流量信息。
查看设备监控相关统计集统计信息
设备监控相关预定义统计集如下：

<!-- 来源页 2503 -->
类别
名称
描述
设备监控
predef_zone_ bw
统计所有安全域的流量
predef_if_bw
统计所有接口的流量
predef_zone_sess
统计所有安全域的会话数
predef_if_sess
统计所有接口的会话数
查看设备监控相关统计集信息，具体命令请参阅“ 查看统计集信息“。
查看硬盘模块信息
硬盘模块主要用于日志和报表的本地存储，实现在本机上的设备监控、行为审计等功能。查看硬盘模块的安
装情况以及使用率，在任何模式下，使用以下命令：
show disk
查看云·界设备虚拟硬盘使用情况
云·界的虚拟硬盘分为系统分区和数据分区，其中系统分区用于存储系统文件，数据分区用于存储日志和报
表。查看云·界虚拟硬盘的使用情况，在任何模式下，使用以下命令：
show disk
示例：
hostname# show disk
显示云·界虚拟硬盘的系统盘使用情况
The percentage of system disk utilization: 18.6%
total(KB) used(KB) free(KB)
1888268 351952 1536316
显示云·界虚拟硬盘的数据盘使用情况
The percentage of data disk utilization: 14.2%
total(KB) used(KB) free(KB)
3997376 567056 3430320
hostname#
查看内存使用率
在任意模式下，使用以下命令查看系统内存的使用情况：
show memory
在任意模式下，使用以下命令查看系统内存中文件系统所占用的内存大小：

<!-- 来源页 2504 -->
show memory filesys
在任意模式下，使用以下命令查看系统CP（控制平面）和DP（数据平面）的内存使用情况：
show memory detail
说明：CP内存用于存储系统配置和管理产生的数据，DP内存用于存储系统流量转发和业务产生的数据。
查看CPU利用率
查看设备的CPU的利用率，在任何模式下，使用以下命令：
l
查看CPU的利用率：show cpu
示例：
hostname#show cpu
Average cpu utilization : 0.3%
Current cpu utilization : 0.2%
Last 1 minute : 0.3%
Last 5 minutes : 0.3%
Last 15 minutes : 0.3%
l
查看每核CPU的利用率：show cpu detail
示例：
hostname#show cpu detail
Average cpu utilization since last boot(%):（每核CPU最近1次启动后的平均利用率）
...
Current cpu utilization (%):（每核CPU的当前利用率）
...
Cpu utilization in last 60 seconds(%):（每核CPU最近1分钟的利用率）
...
Cpu utilization in last 60 minutes(%):（每核CPU最近1小时的利用率）
...
Cpu utilization in last 24 hours(%)：（每核CPU最近1天的利用率）
...
Cpu utilization in last 7 days(%):（每核CPU最近7天的利用率）

<!-- 来源页 2505 -->
...
修改登录页产品名称
系统支持修改设备登录页面显示的产品名称，在全局配置模式下，使用以下命令：
product -category-namename
l
name - 指定登录页面显示的产品名称，取值范围是1-128个字符。
开启/关闭时延统计功能
时延统计功能用于采集流量会话中的关键时延指标，包括客户时延、服务时延以及应用时延。该功能主要服
务于日常运维场景，帮助用户基于会话质量数据（如持续时长、目的IP地理位置、各类时延、数据流、收发
包数等）进行更精细化的监控与问题分析，从而快速定位故障根因，有效提升运维效率与质量。
该功能默认为关闭状态。开启该功能后，系统将对后续新建的会话进行时延数据统计。
注意: 当DP（Data plane，数据平面）内存剩余容量不足总量的3%时，若开启该功能，系统会弹
出“可用内存过低，不建议启用”的提示，用户可酌情选择是否启用。
开启/关闭时延统计功能，在Flow配置模式下，使用以下命令：
l
开启：session-latency-statistics enable
l
关闭：session-latency-statistics disable
查看时延统计功能配置状态
查看时延统计功能的配置状态，在任何模式下，使用以下命令：
show flow session-latency-statistics
示例：
hostname# show flow session-latency-statistics
session-latency-statistics enable

<!-- 来源页 2506 -->
URL访问
查看URL访问相关统计集统计信息
URL访问相关预定义统计集如下：
类别
名称
描述
URL访问
predef_url_hit
统计URL命中次数。
predef_user_url
统计用户访问URL的次数。
predef_url_cat_hit
统计URL类别的命中次数。
predef_user_url_cat_hit
统计用户访问URL类别的次数。
如设备开启IPv6功能，系统支持IPv4和IPv6地址的统计。
仅支持通过CLI查看URL访问相关统计集信息，具体命令请参阅“查看统计集信息”。
提示: K20803、K9180、K7680、K7280、K6680、K6580以及X系列的非根VSYS同样支持URL
访问。

<!-- 来源页 2507 -->
链路状态监控
系统支持通过统计链路中特定接口的采样流量信息，包括延迟、丢包率、抖动，从而实现链路整体状态的监
控和展示。也支持对特定目的IP或域名进行链路探测，统计指定链路的流量信息，包括延迟、抖动和丢包
率。
开启/关闭接口的链路用户体验功能
开启接口的链路用户体验功能，需要首先配置绑定接口并进入链路监控配置模式，在全局配置模式下，使用
以下命令：
link-perf-monitor interface interface-name
l
interface-name – 指定接口名称。
使用no link-perf-monitor interface interface-name命令删除绑定接口。
开启接口的链路用户体验功能，在链路监控配置模式下，使用以下命令：
monitor on
使用no monitor on命令关闭接口的链路用户体验功能。
开启/关闭接口的应用维度
开启接口的应用维度后，系统可以统计链路中特定接口下具体应用的信息，包括延迟、丢包率、抖动。接口
的应用维度默认情况下是关闭的。开启应用维度，在链路监控配置模式下，使用以下命令：
application on
使用no application on命令关闭指定接口的应用维度。
指定描述信息
为开启链路用户体验功能的接口指定描述信息，在链路监控配置模式下，使用以下命令：
description string
l
string - 接口的描述信息。
使用no description命令删除接口的描述信息。
查看链路状态监控配置信息
查看链路状态监控的所有配置信息，在任何模式下使用以下命令：
show link-perf-monitor information

<!-- 来源页 2508 -->
查看链路用户体验统计信息
查看链路用户体验统计信息，在任何模式下使用以下命令：
show link-perf-monitor statistics [interface interface-name [application application-name][ 
history {minute | hour | day | month}]] [ ipv4 | ipv6]
l
interface interface-name – 按照指定接口显示链路用户体验统计信息。
l
application application-name – 按照指定应用显示链路用户体验统计信息。如果不指定该参数，则
显示指定接口的所有统计信息。
l
history {minute | hour | day | month}–显示历史链路用户体验统计信息。
l
ipv4 | ipv6 - 按照指定IP地址类型显示链路用户体验统计信息。如果不指定该参数，将默认显示包含
IPv4和IPv6的整体链路用户体验统计信息。
配置链路探测目的
系统支持对特定目的IP或域名进行链路探测，统计指定链路的流量信息。
进入链路状态探测模式
配置探测目的，需要首先进入链路状态探测模式，在全局模式下，使用以下命令：
link-detect-object
配置IPv4类型的链路探测目的IP
配置IPv4类型的链路探测目的IP，在链路状态探测模式下，使用以下命令：
ip A.B.C.D protocol {tcp [port port-number] | icmp} [description description]
l
A.B.C.D- 指定探测目的的IP地址。
l
tcp [port port-number]- 指定协议类型为TCP，并指定协议端口号。
l
icmp- 指定协议类型为ICMP。
l
description description- 指定对该链路的描述信息。
使用no ip A.B.C.D删除配置的探测目的IP。
配置IPv6类型的链路探测目的IP
配置IPv6类型的链路探测目的IP，在链路状态探测模式下，使用以下命令：
ipv6 X:X:X:X::X protocol {tcp [port port-number] | icmp6} [description description]

<!-- 来源页 2509 -->
l
X:X:X:X::X- 指定探测目的的IPv6地址，取值不区分大小写。
l
tcp [port port-number]- 指定协议类型为TCP，并指定协议端口号。
l
icmp6- 指定协议类型为ICMPv6。
l
description description- 指定对该链路的描述信息。
使用no ipv6 X:X:X:X::X删除配置的探测目的IP。
配置域名类型的链路探测目的
配置域名类型的链路探测目的，在链路状态探测模式下，使用以下命令：
domain-name domian-name ip-type {ipv4 | ipv6} protocol {tcp [port port-number] | icmp6}
[description description]
l
domian-name - 指定探测目的的域名。名称长度可以是1到64个字符，取值不区分大小写。
l
ipv4 | ipv6 - 指定域名的探测类型，可以是ipv4或ipv6。
l
tcp [port port-number] - 指定协议类型为TCP，并指定协议端口号。
l
icmp6- 指定协议类型为ICMPv6。
l
description description - 指定对该链路的描述信息。
使用no domain-name domian-name删除配置的探测目的域名。
配置链路探测规则
系统支持配置链路探测规则进行持续性链路质量探测，查看指定探测目的IP/域名到链路、链路到探测目的
IP/域名的持续性流量统计信息，包括延迟、抖动和丢包率。
注意:
l
非根VSYS不支持链路探测功能。
l
链路探测功能暂不支持在HA Active-Active模式下使用。
l
每个链路探测规则下绑定的所有接口需要属于同一个虚拟路由器。
l
当流量延迟大于等于2000ms时，会在WebUI页面的延迟趋势图中以红点标记。
进入链路状态探测模式
创建链路探测规则名称并进入链路探测规则模式，在全局模式下，使用以下命令：
active-detect-rule rule-name

<!-- 来源页 2510 -->
l
rule-name - 指定链路探测规则的名称，并且进入进入链路探测规则模式。如果指定名称已存在，则直
接进入链路探测规则模式。
配置链路探测规则的链路
配置需要监控链路状态的接口，在链路探测规则模式下，使用以下命令：
interface interface-name
l
interface-name - 指定需要监控链路状态的接口，一条链路探测规则最多可指定8个接口。
使用no interface interface-name删除链路探测规则的链路。
配置链路探测规则的探测目的
配置需要监控链路状态的探测目的IP 地址或域名，在链路探测规则模式下，使用以下命令：
detect-object detect-object-name
l
detect-object-name - 指定需要监控链路状态的探测目的IP 地址或域名，一条链路探测规则最多可指
定8个探测IP或1个探测域名，探测IP和域名不可同时指定。
使用no detect-object detect-object-name删除链路探测规则的探测目的。
配置链路探测规则的丢包率阈值
配置链路探测规则的丢包率阈值，在链路探测规则模式下，使用以下命令：
loss-rate-thres loss-rate-threshold
l
loss-rate-threshold - 指定链路探测规则的丢包率阈值。取值范围是0到100，默认值是75。当丢包率
高于阈值时，会在WebUI页面的丢包趋势图中以红点标记。
使用no loss-rate-thres删除链路探测规则的丢包率阈值。
启用/禁用链路探测规则
默认情况下，配置好的链路探测规则是禁用状态。启用链路探测规则，在链路探测规则模式下，使用以下命
令：
switch on
使用no switch on禁用链路探测规则。
查看链路探测规则的配置信息
查看链路探测规则的配置信息，在任何模式下使用以下命令：
show link-detect-object {all | rule-name}

<!-- 来源页 2511 -->
l
all – 显示所有链路探测规则的配置信息。
l
rule-name - 显示指定链路探测规则的配置信息。
例如：
hostname(config)# show link-detect-object all
Total l3s-active-detect-rule number: 7( 显示链路探测规则的数量)
===================================================================
Name Status Loss-rate-threshold Interface-number Detect-object-number( 显
示链路探测规则的名称、状态丢包率阈值、关联的接口数量以及关联的探测目的数量)
-------------------------------------------------------------------------
-----------------------------------------------
4.123.com ON 75 1 1
70-trust ON 75 1 1
70-test ON 75 1 1
1 ON 75 2 2
test ON 75 1 1
111 ON 75 1 1
1234 ON 60 1
===================================================================
查看链路探测监控配置信息
查看链路状态监控配置信息，在任何模式下使用以下命令：
show link-detect-object {all | A.B.C.D | X:X:X:X::X | domian-name}
l
all – 显示所有目的地址的链路探测监控配置信息。
l
A.B.C.D | X:X:X:X::X | domian-name - 显示指定IPv4目的地址、IPv6目的地址或域名的链路探测
监控配置信息。

<!-- 来源页 2512 -->
应用阻断
应用阻断相关预定义统计集如下：
类别
名称
描述
应用阻断
predef_app_block
统计所有应用的阻断次数。
predef_user_app_block
统计用户的应用阻断次数。
predef_user_app_app_block
统计用户下各应用的阻断次数。
如设备开启IPv6功能，系统支持IPv4和IPv6地址的统计。
通过CLI查看应用阻断相关统计集信息，具体命令请参阅“查看统计集信息”。

<!-- 来源页 2513 -->
关键字阻断
关键字阻断相关预定义统计集如下：
类别
名称
描述
关键字阻断
predef_kw_block
统计所有文件内容关键字/网页关键字/邮件
过滤关键字/Web外发信息关键字的阻断次
数。
predef_user_kw_block
统计用户的关键字阻断次数。
predef_user_kw_kw_block
统计用户下各关键字的阻断次数。
仅支持通过CLI查看关键字阻断相关统计集信息，具体命令请参阅“查看统计集信息”。
注意: K20803、K9180、K7680、K7280、K6680、K6580以及X系列的非根VSYS同样支持关键
字阻断。

<!-- 来源页 2514 -->
认证用户
统计所有认证登录的用户信息。
相关命令如下：
show auth-user
显示通过认证的在线用户信息。
［命令］
show auth-user [username user-name interface interface-name | vrouter vrouter-name]
［句法描述］
username user-name -显示指定用户名的在线用户信息。
web-auth -显示所有在线Web认证用户信息。
scvpn -显示所有在线SCVPN用户信息。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
该命令会显示在线用户关联的用户组信息。如果一个用户关联超过256个用户组，则按照配置顺序只显示前
256个。
［命令实例］
hostname# show auth-user scvpn
show auth-user groupname
显示属于指定用户组的在线认证用户信息。
［命令］
show auth-user groupname group_name
［句法描述］
groupname group_name - 指定用户组名称。
［默认取值］

<!-- 来源页 2515 -->
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user groupname group1
show dp-auth-user
显示系统数据层面通过认证的在线用户信息。
［命令］
show dp-auth-user [{username user-name | webauth-ntlm | webauth-password | webauthsms | webauth-oauth} [interfaceinterface-name | vroutervrouter-name]]
［句法描述］
username user-name - 显示指定用户名的在线用户信息。
webauth-ntlm - 显示指定Webauth-NTLM类型的在线用户信息。
webauth-password - 显示指定Webauth-口令类型的在线用户信息。
webauth-sms - 显示指定Webauth-短信类型类型的在线用户信息。
webauth-oauth - 显示指定Webauth-OAuth类型的在线用户信息。
interface interface-name - 指定接口名称。
vrouter vrouter-name - 指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
仅做调试使用。
［命令实例］
hostname# show dp-auth-user

<!-- 来源页 2516 -->
show pseudo-group
显示用户组ID信息。
［命令］
show pseudo-group [aaa-server server-name group group-name]
［句法描述］
aaa-server server-name - 显示指定AAA服务器的用户组ID信息。
group group-name - 显示指定用户组名称的用户组ID信息。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
仅做调试使用。
［命令实例］
hostname# show pseudo-group
show auth-user agent
显示当前在线的Active-Directory服务器监控用户信息。
［命令］
show auth-user agent [interface interface-name | vrouter vrouter-name]
［句法描述］
interface interface-name -指定接口名称。
vrouter vrouter-name -指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。

<!-- 来源页 2517 -->
［命令实例］
hostname# show auth-user agent interface ethernet0/0
show auth-user dot1x
显示当前在线的802.1x类型的用户。
［命令］
show auth-user dot1x [interface interface-name | vrouter vrouter-name]
［句法描述］
interface interface-name -指定接口名称。
vrouter vrouter-name -指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user dot1x
show auth-user interface
显示使用指定接口做为认证入接口的在线认证用户信息。
［命令］
show auth-user interface interface-name
［句法描述］
interface-name -指定接口名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］

<!-- 来源页 2518 -->
无。
［命令实例］
hostname# show auth-user interface ethernet1/1
show auth-user ip
显示使用指定IP的在线认证用户信息。
［命令］
show auth-user ip {ip-address | ip-address to ip-address} [interface interface-name |
vrouter vrouter-name]
［句法描述］
ip ip-address - 指定IP地址，可指定IPv4或IPv6类型的地址。
ip ip-address to ip-address - 指定IP地址段，可指定IPv4或IPv6类型的地址。
interface interface-name - 指定接口名称。
vrouter vrouter-name - 指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user ip 10.180.32.1
hostname# show auth-user ip 10.180.32.1 to 10.182.32.2
show auth-user l2tp
显示所有L2TP实例当前在线的客户端信息。
［命令］
show auth-user l2tp [interface interface-name | vrouter vrouter-name]
［句法描述］
interface interface-name -指定接口名称。

<!-- 来源页 2519 -->
vrouter vrouter-name -指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user l2tp interface ethernet0/1
show auth-user mac
显示使用指定MAC地址的在线认证用户信息。
［命令］
show auth-user mac mac-address
［句法描述］
ip-address -指定IP地址。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user mac 0050.569d.0b7e
show auth-user radius-snooping
显示RADIUS报文监控用户信息。
［命令］
show auth-user radius-snooping [interface interface-name | vrouter vrouter-name | slot
slot-no]

<!-- 来源页 2520 -->
［句法描述］
interface interface-name 指定接口名称。
vrouter vrouter-name 指定VRouter名称。
slot slot-no 指定槽位号。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user radius-snooping
show auth-user static
显示静态绑定用户，包括与MAC地址或IP地址绑定的用户。
［命令］
show auth-user {static | mac mac-address | ip ip-address } [interface interface-name |
vrouter vrouter-name]
［句法描述］
mac mac-address -指定与用户绑定的MAC地址
ip ip-address -指定与用户绑定的IP地址
interface interface-name -指定接口名称。
vrouter vrouter-name -指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］

<!-- 来源页 2521 -->
hostname# show auth-user static
show auth-user scvpn
查看在线的SCVPN用户信息。
［命令］
show auth-user scvpn [interface interface-name | vrouter vrouter-name]
［句法描述］
interface interface-name -指定接口名称。
vrouter vrouter-name -指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user scvpn
show auth-user endpoint-tag
查看携带指定终端标签的用户信息。
［命令］
show auth-user [interface interface-name | vrouter vrouter-name | endpoint-tag endpointtag-name]
［句法描述］
interface interface-name -指定接口名称。
vrouter vrouter-name -指定VRouter名称。
endpoint-tag endpoint-tag-name - 指定终端标签的名称，支持部分匹配和全部匹配。
［默认取值］
无默认值。
［命令模式］

<!-- 来源页 2522 -->
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user endpoint-tag tag1
show auth-user ztna
查看在线的ZTNA用户信息。
［命令］
show auth-user ztna [interface interface-name | vrouter vrouter-name | endpoint-tag
endpoint-tag-name]
［句法描述］
interface interface-name -指定接口名称。
vrouter vrouter-name -指定VRouter名称。
endpoint-tag endpoint-tag-name - 指定ZTNA终端标签的名称，支持部分匹配和全部匹配。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user ztna endpoint-tag tag1
show auth-user ad-scripting
查看设备生成的用户认证信息。
［命令］
show auth-user ad-scripting [interface interface-name | vrouter vrouter-name]
［句法描述］
interface interface-name -指定接口名称。

<!-- 来源页 2523 -->
vrouter vrouter-name- 指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user ad-scripting
show auth-user ad-polling
查看设备生成的用户认证信息。
［命令］
show auth-user ad-polling [interface interface-name | vrouter vrouter-name]
［句法描述］
interface interface-name -指定接口名称。
vrouter vrouter-name -指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user ad-polling
show auth-user sso-radius
查看设备生成的用户认证信息。
［命令］
show auth-user sso-radius [interface interface-name | vrouter vrouter-name]

<!-- 来源页 2524 -->
［句法描述］
interface interface-name -指定接口名称。
vrouter vrouter-name- 指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user sso-radius
show auth-user sso-monitor
查看设备生成的用户认证信息。
［命令］
show auth-user sso-monitor [interface interface-name | vrouter vrouter-name]
［句法描述］
interface interface-name 指定接口名称。
vrouter vrouter-name 指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user sso-monitor
show auth-user webauth-ntlm
查看设备生成的用户认证信息。

<!-- 来源页 2525 -->
［命令］
show auth-user webauth-ntlm [interface interface-name | vrouter vrouter-name]
［句法描述］
interface interface-name 指定接口名称。
vrouter vrouter-name 指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user webauth-ntlm
show auth-user xauth
查看在线的XAUTH用户信息。
［命令］
show auth-user xauth [interface interface-name | vrouter vrouter-name]
［句法描述］
interface interface-name -指定接口名称。
vrouter vrouter-name -指定VRouter名称。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user xauth

<!-- 来源页 2526 -->
show auth-user webauth
查看在线的Web认证用户信息。
［命令］
show auth-user webauth [interface interface-name | vrouter vrouter-name]
［句法描述］
interface interface-name -显示指定接口的Web认证在线用户信息。
vrouter vrouter-name -显示指定VRouter的Web认证在线用户信息。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# show auth-user webauth
show auth-user vrouter
查看属于指定虚拟路由器（VRouter）的用户。
［命令］
show auth-user vrouter
［句法描述］
无。
［默认取值］
无默认值。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］

<!-- 来源页 2527 -->
hostname# show auth-user vrouter trust-vr

<!-- 来源页 2528 -->
自定义监控
系统的统计集功能可以对所有流经设备的数据进行统计。配置自定义监控统计集功能后，用户可以查看实时
的或者一定统计周期内，基于不同的统计数据类型以及数据组织方式的系统统计信息，并且可以根据不同需
求过滤统计信息，从而帮助用户更加详细和精确地了解系统的资源分配及网络安全状态。如设备开启IPv6功
能，系统支持IPv4和IPv6地址的统计。
数据组织方式
基于IP数据类型（数据组织方式）的统计数据信息表
方式
条件
统计数据类型
流量
会话
新建会话速
率
URL访问
次数
关键字阻
断次数
应用阻断
次数
无方向
发起者
(initiator)
统计发起会
话IP的流量
统计发起会
话IP的会话
个数
统计发起会
话IP的新建
会话速率
统计IP的
URL命中
次数
统计IP的
关键字阻
断次数
统计IP的
应用阻断
次数
回应者
(responder)
统计接收会
话IP的流量
统计接收会
话IP的会话
个数
统计接收会
话IP的新建
会话速率
属于安全域
(belong to
zone)
统计属于某
安全域的IP
的流量
统计属于某
安全域的IP
的会话数
统计属于某
安全域的IP
的新建会话
速率
不属于安全域
(not belong
to zone)
统计不属于
某安全域的
IP的流量
统计不属于
某安全域的
IP的会话数
统计不属于
某安全域的
IP的新建会
话速率
属于接口
(belong to
interface)
统计属于某
接口的IP的
流量
统计属于某
接口的IP的
会话数
统计属于某
接口的IP的
新建会话速
率
不属于接口
(not belong
to interface)
统计不属于
某接口的IP
的流量
统计不属于
某接口的IP
的会话数
统计不属于
某接口的IP
的新建会话
速率
双向
发起者
(initiator)
统计发起会
话IP的上行
和下行流量
统计发起会
话IP的接收
和发送会话
个数
统计发起会
话IP的接收
和发送新建
会话速率
统计IP的
URL命中
次数
统计IP的
关键字阻
断次数
统计IP的
应用阻断
次数

<!-- 来源页 2529 -->
方式
条件
统计数据类型
流量
会话
新建会话速
率
URL访问
次数
关键字阻
断次数
应用阻断
次数
回应者
(responder)
统计接收会
话IP的上行
和下行流量
统计接收会
话IP的接收
和发送会话
个数
统计接收会
话IP的接收
和发送新建
会话速率
属于安全域
(belong to
zone)
统计属于某
安全域的IP
的上行和下
行流量
统计属于某
安全域的IP
的接收和发
送会话个数
统计属于某
安全域的IP
的接收和发
送新建会话
速率
不属于安全域
(not belong
to zone)
统计不属于
某安全域的
IP的上行和
下行流量
统计不属于
某安全域的
IP的接收和
发送会话个
数
统计不属于
某安全域的
IP的接收和
发送新建会
话速率
属于接口
(belong to
interface)
统计属于某
接口的IP的
上行和下行
流量
统计属于某
接口的IP的
接收和发送
会话个数
统计属于某
接口的IP的
接收和发送
新建会话速
率
不属于接口
(not belong
to interface)
统计不属于
某接口的IP
的上行和下
行流量
统计不属于
某接口的IP
的接收和发
送会话个数
统计不属于
某接口的IP
的接收和发
送新建会话
速率
基于安全域、接口、用户、应用、URL、URL类别、VSYS为数据组织方式时的统计数据信息表
型号说明：仅SD-WAN系列平台不支持查看基于VSYS为数据组织方式的系统统计信息。
组织方式
方式
统计数据类型
流量
会话
新建会话速
率
URL命中
次数
关键字阻
断
应用阻断
次数
安全域
无方向
统计安全域的流
量
统计安全域
的会话个数
统计安全域
的新建会话
速率
统计安全
域的URL
命中次数
N/A
N/A

<!-- 来源页 2530 -->
组织方式
方式
统计数据类型
流量
会话
新建会话速
率
URL命中
次数
关键字阻
断
应用阻断
次数
双向
统计安全域的上
行和下行流量
统计安全域
的接收和发
送会话个数
统计安全域
的接收和发
送新建会话
速率
接口
无方向
统计接口的流量
统计接口的
会话个数
统计接口的
新建会话速
率
统计接口
的URL命
中次数
N/A
N/A
双向
统计接口的上行
和下行流量
统计接口的
接收和发送
会话个数
统计接口的
接收和发送
新建会话速
率
应用
N/A
统计应用的流量
统计应用的
会话个数
统计应用的
新建会话速
率
N/A
N/A
统计应用
的应用阻
断次数
用户
无方向
统计用户的流量
统计用户的
会话个数
统计用户的
新建会话速
率
统计用户
的URL命
中次数
统计用户
的关键字
阻断次数
统计用户
的应用阻
断次数
双向
统计用户的上行
和下行流量
URL
N/A
N/A
N/A
N/A
统计URL
命中次数
N/A
N/A
URL类别
N/A
N/A
N/A
N/A
统计URL
类别命中
次数
N/A
N/A
VSYS
N/A
统计VSYS的带
宽
统计VSYS的
会话个数
统计VSYS的
新建会话速
率
统计VSYS
的URL命
中次数
N/A
N/A
过滤条件类型
用户可以为统计集配置过滤条件，以统计特定条件下的数据信息，比如统计某个特定安全域的会话数、统计
某个特定目的IP的流量等。系统最多允许每个统计集配置32个过滤条件，其中用户名称、用户组和用户角色
每种最多可以配置8个过滤条件。如果为同一个统计集配置的多个过滤条件属于同一类型，那么这些过滤条
件之间为逻辑“或”（or）的关系；如果分属不同类型，那么这些过滤条件之间为逻辑“与”（and）的关
系。
自定义监控功能的所有过滤条件类型表

<!-- 来源页 2531 -->
类型
描述
安全域（filter zone）
以安全域为条件进行过滤
安全域-流入（filter zone zone-name ingress）
以入安全域为条件进行过滤
安全域-流出（filter zone zone-name egress）
以出安全域为条件进行过滤
接口（filter interface）
以接口为条件进行过滤
接口-流入（filter interface if-name ingress）
以入接口为条件进行过滤
接口-流出（filter interface if-name egress）
以出接口为条件进行过滤
应用（filter application）
以应用为条件进行过滤
地址条目（filter ip）
以地址条目为条件进行过滤
地址条目-源（filter ip add-entry source）
以源地址（地址条目）为条件进行过滤
地址条目-目的（filter ip add-entry destination）
以目的地址（地址条目）为条件进行过滤
IP/掩码（filter ip A.B.C.D/M）
以IP为条件进行过滤
IP/掩码-源（filter ip A.B.C.D/M source）
以源IP为条件进行过滤
IP/掩码-目的（filter ip A.B.C.D/M destination）
以目的IP为条件进行过滤
用户（filter user）
以用户名称为条件进行过滤
用户组（filter user-group）
以用户组名称为条件进行过滤
用户角色（filter role）
以用户角色名称为条件进行过滤
服务（filter service）
以服务名称为条件进行过滤
配置自定义监控
自定义统计集配置包括：
l 创建统计集
l 配置统计数据类型
l 配置数据组织方式
l 配置过滤条件
创建统计集
创建统计集，在全局模式下使用以下命令：
statistics-set name
l
name – 指定统计集名称，范围为1到31个字符。

<!-- 来源页 2532 -->
执行该命令后，系统创建指定名称的统计集并且进入统计集配置模式；如果指定的统计集名称已存在，则直
接进入统计集配置模式。
在全局配置模式下，使用该命令no的形式删除指定统计集：
no statistics-set name
配置统计数据类型
统计集的统计数据类型包括流量、会话、新建会话速率、URL命中次数、关键字阻断次数和应用阻断次数。
配置统计数据类型，在统计集配置模式下使用以下命令：
target-data {bandwidth | session | rampup-rate | URL-hit| application-block| attack-rate }
[record-history] [root-vsys-only]
l
bandwidth | session | rampup-rate | URL-hit | application-block | attack-rate – 指定统计集
的统计数据类型。可以为带宽（bandwidth）、会话（session）、新建会话速率（rampuprate）、URL命中次数（URL-hit）或者应用阻断次数（application-block），或AD攻击防护次数
（attack-rate）。
l
record-history – 记录历史统计数据，最多支持记录最近30天的数据。
l
root-vsys-only – 指定仅统计Root VSYS中的数据。如果不配置此参数，则统计所有VSYS中的数据。
在统计集配置模式下，使用该命令no的形式取消指定统计集统计数据类型的配置：
no target-data
注意: 配置统计集时，
l
URL命中次数统计数据类型仅对安装有URL许可证的用户可用。
l
指定root-vsys-only参数后，数据组织方式不能指定为VSYS。
l
在非根VSYS下，如果需要按照URL访问次数统计（URL-hit），请提前配置该非根VSYS的
URL资源配额。
配置数据组织方式
统计集的数据组织方式包括IP、接口、安全域、应用、用户、URL、URL类别和VSYS。可配置的数据组织方
式会根据统计数据类型的不同而不同。非根VSYS同样支持IP、接口、安全域、应用、用户、URL和URL类别
数据组织方式。
配置数据组织方式，在统计集配置模式下使用以下命令：

<!-- 来源页 2533 -->
group-by {[ip [directional] [initiator | responder | belong-to-zone zone-name | not-belongto-zone zone-name | belong-to-interface interface-name | not-belong-to-interface
interface-name]] | interface [directional] | zone [directional] | application | user [directional]
| url | url-category | vsys}
l
ip – 指定统计集的数据组织方式为IP地址。用户可以通过initiator | responder | belong-to-zone
zone-name | not-belong-to-zone zone-name | belong-to-interface interface-name | notbelong-to-interface interface-name参数指定被统计IP的范围，可以是发起会话的IP
（initiator），接收会话的IP（responder），属于某特定安全域的IP（belong-to-zone zonename），不属于某特定安全域的IP（not-belong-to-zone zone-name），属于某特定接口的IP
（belong-to-interface interface-name）或者不属于某特定接口的IP（not-belong-tointerface interface-name）。
l
directional – 指定统计结果为双向的，即统计以IP、接口或者安全域为数据组织方式时的上行和下行带
宽、接收和发送会话数、接收和发送新建会话速率；如不配置，系统默认统计结果为无方向的，即统计
以IP、接口或者安全域为数据组织方式的所有带宽、会话或者新建会话速率。
l
interface – 指定统计集的数据组织方式为接口。
l
zone – 指定统计集的数据组织方式为安全域。
l
application – 指定统计集的数据组织方式为应用，此时的统计数据类型不可以为攻击速率、URL命中
次数和关键字阻断次数。
l
user – 指定统计集的数据组织方式为用户。
l
url – 指定统计集的数据组织方式为URL。
l
url-category – 指定统计集的数据组织方式为URL类别。
l
vsys – 指定统计集的数据组织方式为VSYS。
在统计集配置模式下，使用该命令no的形式取消指定统计集数据组织方式的配置：
no group-by
配置过滤条件
用户可以为统计集配置过滤条件，以统计特定条件下的数据信息，比如统计某个特定安全域的会话数、统计
某个特定目的IP的带宽等等。
添加/删除过滤条件
配置过滤条件，在统计集配置模式下，使用以下命令：

<!-- 来源页 2534 -->
filter {ip {A.B.C.D/M | address-entry} [source | destination] | interface name [ingress | egress]
| zone name [ingress | egress] | application name | user user-name aaa-server-name | usergroup user-group-name aaa-server-name | role role-name | service service-name}
l
ip {A.B.C.D/M | address-entry} – 以指定IP为条件进行过滤。IP可以是地址范围（比如10.101.0.1
255.255.255.0或者10.101.0.1/24）或者系统地址簿中的地址条目。如设备开启IPv6功能，系统支持
只查看IPv6地址的统计项。
l
source|destination – 以源IP地址（source）或者目的IP地址（destination）为条件进行过
滤。
l
interface name – 以指定接口为条件进行过滤。
l
ingress | egress – 以入接口（ingress）或出接口（egress）为条件进行过滤。
l
zone name – 以指定安全域为条件进行过滤。
l
ingress | egress – 以入安全域（ingress）或出安全域（egress）为条件进行过滤。
l
application name – 以指定应用为条件进行过滤。
l
user user-name aaa-server-name – 以指定用户名称为条件进行过滤。
l
user-group user-group-name aaa-server-name – 以指定用户组名称为条件进行过滤。
l
role role-name - 以指定用户角色名称为条件进行过滤。
l
service service-name - 以指定服务名称为条件进行过滤。
用户可以配置多条该命令，添加多个过滤条件。系统最多允许每个统计集配置32个过滤条件，其中用户名
称、用户组和用户角色每种最多可以配置8个过滤条件。如果为同一个统计集配置的多个过滤条件属于同一
类型，那么这些过滤条件之间为逻辑“或”（or）的关系；如果分属不同类型，那么这些过滤条件之间为逻
辑“与”（and）的关系。
在统计集配置模式下，使用该命令no的形式删除指定类型的过滤条件：
no filter {ip {A.B.C.D/M | address-entry } [source | destination] | interface name [ingress |
egress] | zone name [ingress | egress] | application name | user user-name aaa-server-name
| user-group user-group-name aaa-server-name | role role-name | service service-name}
取消所有类型的过滤条件，在统计集配置模式下使用以下命令：
no filter all
开启/关闭统计集统计功能
默认情况下，仅用户监控、应用监控、设备监控预定义统计集为开启状态，其他所有预定义统计集的统计功
能均为关闭状态。

<!-- 来源页 2535 -->
在统计集配置模式下，使用以下命令开启或关闭统计集的统计功能：
l
开启：active
l
关闭：no active
在根VSYS中执行上述命令后，会开启或关闭所有VSYS相应的预定义统计集功能(除non-root VSYS不支持
外)。非根VSYS中不能开启或关闭自身的预定义统计集功能。
查看统计集信息
用户可以在任何模式下通过以下命令查看系统预定义和用户自定义统计集的配置信息：
show statistics-set name [{current | history | history-max} [ IPv4 | IPv6 ] [sort-by {up | down |
item}]]
l
show statistics-set – 显示系统中所有统计集的配置信息。
l
name – 指定统计集名称，显示特定统计集的配置信息。
l
current | history | history-max – 指定显示特定统计集的数据统计信息，包括：
l
current – 显示特定统计集的当前数据统计信息。
l
history – 显示特定统计集的历史数据统计信息。系统以每5分钟为单位进行数据采样。
l
history-max – 显示特定统计集的历史数据峰值统计信息。该参数仅用于统计数据类型为会话
（session）的统计集。
l
IPv4 | IPv6 - 显示特定统计集的IPv4或IPv6类型的统计信息。
l
sort-by {up | down | item} – 指定特定统计集统计数据的排列顺序（从大到小排列）：
l
up - 按上行数据进行排序。
l
down – 当配置group-by时指定了directional参数，使用该参数按下行数据进行排序。
l
item - 按照group-by的对象进行排序。
查看Controller统计信息
Controller是系统中用来统计硬件层面收发数据包信息的统计单元。用户可以在任何模式下通过以下命令查
看Controller的统计信息：
show controller [slot slot-name [index index-num] [port port-number] | interface_name]
statistic
l
slot slot-name - 指定扩展模块所在的槽位号，查看该模块卡上所有接口的收发数据包数量的统计信
息。

<!-- 来源页 2536 -->
l
index index-num - 指定槽位对应转发芯片索引号，查看指定slot-name上对应转发芯片的数据包统
计信息。
l
port port-number - 指定接口号，该接口号为扩展模块上物理接口的标号，如0,1,2,3。查看扩展模块
上指定物理接口的数据包统计信息。
l
interface_name - 指定接口名称，查看设备上指定物理接口的数据包统计信息。
不指定以上任何参数时，show controller statistic表示查看设备上所有物理接口的数据包统计信息。
例如，使用show controller slot 0 port 0 statistic命令后，统计结果的输出信息如下：
hostname# show controller slot 0 port 0 statistic
ethernet0/0, physical port 0:
InGoodOctets: 2422834
InGoodPkts: 9053
InUnicastPkts: 0
InMulticastPkts: 9053
InUndersizePkts: 0
InFragments: 0
InMACRcvErrors: 0
DropEvents: 0
OutGoodOctets: 512
OutUnicastPkts: 0
OutMulticastPkts: 0
Collisions: 0
SingleCollisions: 0
ExcessiveCollisions: 0
Pkts64Octets: 8
Pkts128to255Octets: 3020
Pkts512to1023Octets: 0
InBadOctets: 0
InBadPkts: 0
InBroadcastPkts: 0
InControlPkts: 0
InOversizePkts: 0
InJabbers: 0
InCRCAlignErrors: 0
OutGoodPkts: 8
OutBroadcastPkts: 8
OutControlPkts: 0
OutDropDeferrals: 0
MultipleCollisions: 0
LateCollisions: 0
Pkts65to127Octets: 0
Pkts256to511Octets: 6033
Pkts1024toMaxOctets: 0
输出信息中各参数说明如下：

<!-- 来源页 2537 -->
参数
说明
备注
InGoodOctets
接收到的正常报文的字节统计总数。
InGoodPkts
接收到的正常报文的数据包总数。
对于X系列设备，该参数的统计数据
为单播数据包+组播数据包+广播数据
包。
InBadOctets
接收到的错包的字节统计总数。
InBadPkts
接收到的错误数据包总数。
对于X系列设备，该参数的统计数据
为以下数据的总和：UndersizePkts
（长度小于64字节的正常数据包总
数）+ OversizePkts（长度大于
1518字节的正常数据包总数）+
Fragments（带有帧校验错误或对齐
错误且长度小于64字节的数据包总
数）+ Jabbers（带有帧校验错误后
对齐错误且长度大于1518字节的数
据包总数）+ MACRcvErrors
（RxErr信号的出现次数）；
对于A系列、K9180、K2680、
K2380设备，该参数的统计数据为硬
件丢包计数。
InUnicastPkts
接收到的单播数据包总数。
InBroadcastPkts
接收到的广播数据包的总数（不包括组
播包）。
InMulticastPkts
接收到的组播数据包的总数（不包括广
播包）。
InControlPkts
接收到的流控帧总数
InUndersizePkts
接收到的长度小于64字节的正常数据包
总数。
InOversizePkts
接收到的长度大于1518字节的正常数据
包总数。
InFragments
接收到的带有帧校验错误（FCS
error）或对齐错误（Alignment
error）并且长度小于64字节数据包总
数。
InJabbers
接收到的带有帧校验错误（FCS
error）或对齐错误（Alignment

<!-- 来源页 2538 -->
参数
说明
备注
error）并且长度大于1518字节数据包
总数。
InMACRcvErrors
接收到的RxErr信号的出现次数。
InCRCAlignErrors
接收到的带有帧校验错误（FCS
error）或对齐错误（Alignment
error）并且字节长度在64-1518之间
的数据包总数。
DropEvents
由于资源不足而被丢弃的数据包的事件
总数；有时这个数字不一定是丢弃的数
据包数量，只是检测到这种情况的次
数。
对于X系列设备，该参数的统计数据
为带宽不足导致出现的丢包次数计
数；
对于A系列、K9180、K2680、
K2380设备，该参数的统计数据为接
收缓冲区分配失败次数计数。
OutGoodOctets
发送成功的字节总数。
OutGoodPkts
发送成功的数据包总数。
OutUnicastPkts
发送成功的单播数据包总数。
OutBroadcastPkts
发送成功的广播包总数（不包括组播
包）。
OutMulticastPkts
发送成功的组播包总数（不包括广播
包）。
OutControlPkts
发送成功的流控包总数。
OutDropDeferrals
由于过度延迟而丢弃的数据包总数。
对于A系列、K9180、K2680、
K2380设备，该参数的统计数据为发
送失败的数据包总数。
Cillisions
MAC层发送数据包冲突事件的数量，不
包括计入以下的Single、Multiple、
Excessive 或Late。
对于X系列设备，不支持该参数的统
计。
SingleCollisions
经历一次冲突的成功传输的数据包总
数。
对于X系列设备，不支持该参数的统
计。
MultipleCollisions
经历多次冲突的成功传输的数据包总
数。
对于X系列设备，不支持该参数的统
计。
ExcessiveCollisions
经历16次冲突的成功传输的数据包总
数。
对于X系列设备，该参数的统计数据
为多次冲突发生后在MAC层的丢帧计
数。
LateCollisions
使用无效FCS传输的帧数；若在当传输
对于X系列设备，该参数的统计数据

<!-- 来源页 2539 -->
参数
说明
备注
过程中修改帧时，帧的原始FCS无效并
且新的FCS也无效，此计数器也增加。
为MAC层延迟冲突计数。
Pkt64Octets
接收或发送的长度为64个字节的数据包
（包括错包）的总数。
Pkt65to127Octets
接收或发送的长度在65-127个字节之间
的数据包（包括错包）的总数。
Pkt128to255Octets
接收或发送的长度在128-255个字节之
间的数据包（包括错包）的总数。
Pkt256to511Octets
接收或发送的长度在256-511个字节之
间的数据包（包括错包）的总数。
Pkt512to1023Octets
接收或发送的长度在512-1023个字节
之间的数据包（包括错包）的总数。
Pkt1024toMaxOctets
接收或发送的长度大于等于1023个字节
的数据包（包括错包）的总数。

<!-- 来源页 2540 -->
长期监控
型号说明：
l
支持：安装有硬盘的A系列平台
l
支持：安装有硬盘的B系列平台
l
支持：安装有硬盘的K系列平台
l
不支持：A2200、A1800、A1600
l
不支持：K20803、K9180、K7680、K7280、K6680、K6580
l
不支持：X系列平台
l
不支持：云·界
l
不支持：SD-WAN系列平台
系统支持长期监控功能，能够对设备的流量和会话进行持续监控统计和存储，满足用户对网络监控和诊断的
需求。功能支持详情如下：
l 支持将最长180天的流量和会话统计数据存储到设备硬盘，并允许用户设置统计数据存储空间大小限制；
l 可以按照IP或者应用类型的方式查询统计数据，最长可以查询180天内任意连续31天的数据；
l 以列表、柱状图、折线图的方式展示统计数据。
配置长期监控
开启/关闭长期监控功能
默认情况下，系统的长期监控功能为关闭状态。开启/关闭长期监控功能，在全局配置模式下，使用以下命
令：
statistics-long-term {enable | disable}
l
enable - 开启长期监控功能。
l
disable - 关闭长期监控功能。

<!-- 来源页 2541 -->
日志
日志介绍
设备支持日志管理功能。记录并输出设备的各种日志信息，分别是设备系统、威胁、云沙箱、会话、NAT、
文件过滤、内容过滤、上网行为审计、共享接入以及URL等。
l 设备系统日志- 包含事件日志信息、网络日志信息以及配置日志信息。
l 事件日志- 包括错误、警告、通告、信息、调试、紧急、警报和严重8个级别的系统事件信息。
l 网络日志- 与网络服务操作相关的日志信息，例如PPPoE以及DDNS等。
l 配置日志- 与CLI配置相关的日志信息，例如接口配置等。
l 威胁日志- 与系统威胁相关的日志信息，例如攻击防护和应用安全等。
l 流量日志– 流量日志信息包含会话、NAT和上网日志信息三部分。
l 会话日志– 与会话相关的日志信息，例如会话的协议、源/目的IP地址、源/目的端口等。
l NAT日志– 与NAT行为相关的日志信息，例如NAT类型、源/目的IP地址、源/目的端口等。
l URL日志- 与上网行为相关的日志信息，例如用户的上网时间和网页访问情况、URL过滤等。
l IoT日志- 与IoT安全监控相关的日志信息。
l PBR日志- 策略路由日志信息，与策略路由相关日志信息。
l 文件过滤日志- 与文件过滤相关的日志信息。
l 内容过滤日志- 与内容过滤相关的日志信息，例如网页关键字过滤、Web外发信息、邮件过滤或者应用程序控
制。
l 上网行为审计日志- 与上网行为相关的日志信息，例如QQ用户、微信用户、微博用户的使用情况等。
l 云沙箱日志- 与沙箱检测相关的日志信息。
l 共享接入日志- 与多终端共享接入相关的日志信息。
l 终端标签日志- 与终端标签相关的日志信息。
l 调试– 系统调试信息。
系统的多种日志信息能够有效的记录设备的运行情况，从而为用户分析网络情况和防护网络攻击提供依据。

<!-- 来源页 2542 -->
日志的严重等级
系统的事件日志信息根据日志信息的严重程度区分的。系统日志的严重等级可分为8级，关于各级的具体信
息，请参阅下表：
级别
级别号
描述
日志定义
紧急
（Emergencies）
0
系统不可用信息。
LOG_EMERG
警报（Alerts）
1
需要立即处理的信息，如设备受到攻击等。
LOG_ALERT
严重（Critical）
2
危急信息，如硬件出错。
LOG_CRIT
错误（Errors）
3
错误信息。
LOG_ERR
警告（Warnings）
4
报警信息。
LOG_WARNING
通告
（Notifications）
5
非错误信息，但需要特殊处理。
LOG_NOTICE
信息
（Informational）
6
通知信息。
LOG_INFO
调试（Debugging）7
调试信息，包括正常的使用信息。
LOG_DEBUG
日志信息输出目的地
日志信息可以输出到不同的目的地，设备支持以下7种日志信息输出目的地，用户可以根据自己的需要指
定：
l Console - 将日志信息输出到Console端口终端。
l 终端（Remote）- 包括Telnet和SSH两种终端。
l 内存缓存（Buffer）- 内存缓存。
l 文件（File）- 默认情况下，系统会生成一个文件记录日志信息，用户可以指定将信息输出到USB口的文件中。
l 系统日志服务器- 包括Syslog服务器和IPFIX服务器。系统可以将所有类型的日志信息输出到UNIX 或Windows
Syslog Server；也可以将NAT444日志信息（仅用户分配端口日志和用户释放端口日志）输出到IPFIX服务器。
l Email地址- 将日志信息发送到某个邮件地址。
l 本地数据库（Localdb）- 将日志信息发送到本地数据库。本地数据库存在于硬盘卡中。
l 手机短信- 将日志信息以短信的形式发送到某个手机上。

<!-- 来源页 2543 -->
日志信息格式
为方便用户查阅和分析系统日志信息，系统按照固定的格式输出日志信息。该格式为：<设备号*8+日志严重
等级> 时间设备序列号（VSYS名称）日志ID HillstoneNetworks#日志类型@模块：日志描述请参阅以
下示例：
<188>Mar 8 17:26:44 5821838205000143(root) 4424363e HillstoneNetworks#Traffic@FLOW:
SESSION: 2.1.1.200:53262(ethernet0/1)->3.1.1.200:21(ethernet0/0), Protocol TCP, vr trustvr, policy 11, user -@-, host -, mac 0000.0000.0000, zone from trust to trust, session start

<!-- 来源页 2544 -->
配置IPFIX服务器
IPFIX（IP Flow Information Export，即IP数据流信息输出）是一种网络监控和数据交换的标准协议，主
要用于收集和传输网络流量信息。IPFIX是NetFlow V9协议的一个标准化版本，由IETF（Internet
Engineering Task Force）定义，旨在提供一种标准化的方法来捕获网络中的流量数据。这些数据通常包
括流的统计信息，如源和目的IP地址、端口号、协议类型等。因此，IPFIX被广泛应用于网络管理和优化、安
全监控、流量分析和计费系统等场景。
为满足客户CGNAT（运营商级NAT，也称为NAT444）使用场景需求，防火墙设备支持通过配置IPFIX服务
器相关信息，将采集到的NAT444日志以对应的模板格式输出到指定的IPFIX服务器。NAT444日志模板为系
统内置模板，系统会根据配置的模板刷新时间间隔定时更新，以确保IPFIX服务器能正常解析并获取到
NAT444日志数据。
在NAT444地址转换中，系统会产生5条NAT444日志，分别为：用户分配端口日志、用户释放端口日志、端
口耗尽告警日志、NAT444会话开始日志以及NAT444会话结束日志。其中，仅用户分配端口日志和用户释
放端口日志支持输出至IPFIX服务器。
注意: 每个VSYS最多允许配置3台IPFIX服务器。
将日志信息输出到IPFIX服务器，用户需要进行如下配置：
l 创建IPFIX服务器
l 配置IPFIX服务器参数
l 指定模板刷新时间
l 指定输出日志类型
l 查看IPFIX服务器的配置信息
创建IPFIX服务器
对IPFIX Server的各项配置需要在IPFIX Server配置模式下进行。创建IPFIX Server并进入IPFIX Server配
置模式，在全局配置模式下，使用以下命令：
logging ipfix-server server-name
l
server-name – 指定IPFIX Server的名称，范围为1到127个字符。
执行该命令后，系统创建指定名称的IPFIX Server，并且进入IPFIX Server配置模式；如果指定的名称已存
在，则直接进入IPFIX Server配置模式。
在全局配置模式下使用该命令no的形式删除指定的IPFIX Server：

<!-- 来源页 2545 -->
no logging ipfix-server server-name
配置IPFIX服务器参数
创建IPFIX Server后，用户需要配置IPFIX Server的IP地址或主机名称、UDP端口、绑定方式以及虚拟路由
器，在IPFIX Server配置模式下，使用以下命令：
server { ip ip-address | hostname hostname} udp udp-port-number bindtype { vrouter vrname | source-interface interface-name}
l
ip ip-address | hostname hostname– 指定IPFIX Server的IP地址或者主机名称。
l
udp udp-port-number - 指定IPFIX服务器的UDP协议端口号，即IPFIX服务器的目的端口号。范围是
1-65535。默认为9996。
l
bindtype { vrouter vr-name | source-interface interface-name} - 指定IPFIX Server所属的
VRouter或发送日志信息的源接口。vrouter vr-name表示指定VRouter的名称；source-interface
interface-name表示指定发送日志信息的源接口，设备会以指定接口的IP地址为源IP，向IPFIX服务器
发送日志信息，如果该接口配有管理IP地址，优先使用管理IP地址。
在IPFIX Server配置模式下，使用该命令no的形式删除指定的IPFIX Server的所有配置信息：
no server
注意: 执行no server命令后，UDP端口配置恢复默认值9996。
指定模板刷新时间
指定系统内置的NAT444日志模板的刷新时间间隔。指定后，系统会根据设置的时间间隔，定时刷新
NAT444日志模板，以确保IPFIX服务器能正常解析并获取到NAT444日志数据。
指定模板刷新时间，在IPFIX Server配置模式下，使用以下命令：
refresh-time time-value
l
time-value – 指定模板刷新时间间隔，范围是1-3600分钟，默认为30分钟。
在IPFIX Server配置模式下，使用该命令no的形式恢复系统默认的模板刷新时间：
no refresh-time
指定输出日志类型
指定输出到IPFIX服务器的日志类型，当前仅支持NAT日志类型。在IPFIX Server配置模式下，使用以下命
令：
log-enable nat

<!-- 来源页 2546 -->
在IPFIX Server配置模式下，使用该命令no的形式删除指定的日志类型：
no log-enable nat
查看IPFIX服务器的配置信息
用户可以在任何模式下通过以下命令查看IPFIX服务器的配置信息：
show logging ipfix-server
示例：
hostname# show logging ipfix-server
servername hostname bindname protocol port logtype refreshtime
--------------------------------------------------------------------------------------------
ipfix 2.2.2.2 trust-vr UDP 5400 nat 30

<!-- 来源页 2547 -->
配置系统日志功能
通过CLI，用户可以对系统日志功能做以下配置：
l 开启和关闭日志功能
l 事件日志信息的输出及过滤
l 威胁日志信息的输出
l 配置、调试和网络日志信息的输出
l 配置调试功能的使用条件
l 流量日志信息的输出
l 数据安全日志（文件过滤日志、内容过滤日志、上网行为审计日志）信息的输出
l 云沙箱日志信息的输出
l 配置日志的存储周期
l 配置日志备份服务器
l 终端防护日志信息的输出
l 设备日志信息的输出
l 配置日志信息存储到硬盘
l 配置Syslog Server
l 指定发送源端口
l 配置日志信息的Facility字段
l 配置二进制日志报文头的版本号字段
l 设置流量日志的主机名称/用户名称的显示状态
l 开启/关闭会话结束日志记录TCP状态信息功能
l 设置威胁日志的用户名称的显示状态
l 配置日志信息输出到Email地址
l 配置日志信息输出到手机
l 配置日志参数
l 开启/关闭威胁日志记录认证用户信息功能
l 配置长期存储日志文件

<!-- 来源页 2548 -->
l 配置备份日志文件
l 配置日志文件备份服务器
l 查看日志文件备份服务器
l 显示日志配置相关信息
l 显示日志信息
l 导出日志信息
l 清除日志信息
开启和关闭日志功能
默认情况下，流量日志功能是关闭的（打开流量日志功能会影响系统性能）。开启或者关闭系统的各种日志
功能，请在全局配置模式下输入以下命令：
l
开启：logging {event | configuration | operation | network | traffic {session | nat | urlfilter |
device} | debug | threat | data-security [dlp | cf | nbr]} on
l
关闭：no logging {event | configuration | operation | network | traffic {session | nat |
urlfilter | device} | debug | threat | data-security [dlp | cf | nbr]} on
事件日志信息的输出及过滤
用户可以根据需要指定事件日志信息的输出目的地，并且按照日志信息的严重级别对输出信息进行过滤。
将事件日志信息输出到console、远程终端、Syslog服务器、手机、设备硬盘卡或者使用事件日志email提
醒功能，并且对日志信息进行过滤，在全局配置模式下使用以下命令：
logging event to {console | remote | syslog| sms | email | localdb} [severity severity-level]
l
console – 指定将事件日志信息输出到console口。
l
remote – 指定将事件日志信息输出到远程终端。
l
syslog – 指定将事件日志信息输出到Syslog Server。关于如何配置Syslog Server，请参阅“配置
Syslog_Server”。
l
sms – 指定将严重等级在严重（Critical）以上的事件日志信息以短信的形式输出到某个手机。
l
email – 指定将日志信息输出到Email地址。关于如何配置Email地址，请参阅“配置Email地址”。
l
localdb –指定将事件日志信息输出到设备硬盘卡。（该功能仅部分型号设备支持。）

<!-- 来源页 2549 -->
l
severity severity-level – 指定输出的事件日志信息的级别从而对事件日志信息进行过滤。输出信息的
级别将会是指定级别或者高于指定级别，即数字等于或者小于指定级别。例如指定级别是通告，系统将
会输出通告、警告和错误级别的日志信息。
在全局配置模式下，用以上命令no的形式可以关闭相关的输出功能。命令如下：
no logging event to {console | remote | syslog | sms |email | localdb}
将事件日志信息输出到内存缓存，并且对日志信息进行过滤，在全局配置模式下使用以下命令：
logging event to buffer [severity severity-level] [size buffer-size]
l
severity severity-level – 指定输出的事件日志信息的级别从而对事件日志信息进行过滤。输出信息的
级别将会是指定级别或者高于指定级别，即数字等于或者小于指定级别。例如指定级别是通告，系统将
会输出通告、警告和错误级别的日志信息。
l
size buffer-size –指定内存缓存的大小。范围是4096到1048576字节。默认值为1048576。
在全局配置模式下，用以上命令no logging event to buffer命令关闭相关的输出功能。
将事件日志信息输出到文件，并且对日志信息进行过滤，在全局配置模式下使用以下命令：
logging event to file [severity severity-level] [name [usb0 | usb1] file-name] [size file-size]
l
severity severity-level – 指定输出的事件日志信息的级别从而对事件日志信息进行过滤。输出信息的
级别将会是指定级别或者高于指定级别，即数字等于或者小于指定级别。例如指定级别是通告，
StoneOS将会输出通告、警告和错误级别的日志信息。
l
name [usb0 | usb1] file-name –该参数用来指定保存日志信息的U盘和日志信息文件的名称。
l
size file-size – 将事件日志信息输出到文件（U盘或者Flash）时，该参数用来指定日志信息文件的大
小。范围是4096到1048576字节。默认是1048576字节。
在全局配置模式下，用以上命令no logging event to file命令关闭相关的输出功能。
威胁日志信息的输出
用户可以根据需要指定威胁日志信息的输出目的地。将威胁日志信息输出到console、远程终端、Syslog服
务器、设备硬盘卡或者Email地址，在全局配置模式下使用以下命令：
logging threat to {console | remote | syslog [ custom-format [distributed [round-robin | srcip-hash]]]| email | localdb}[severity severity-level]
l
console – 指定将威胁日志信息输出到console口。
l
remote – 指定将威胁日志信息输出到远程终端。

<!-- 来源页 2550 -->
l
syslog – 指定将威胁日志信息输出到Syslog Server。关于如何配置Syslog Server，请参阅“配置
Syslog_Server”。
l
custom-format – 发送明文日志信息。默认情况下，系统发送明文日志信息。
l
distributed – 分布发送日志信息到多台Syslog服务器。
l
src-ip-hash | round-robin – 指定服务器选择算法。src-ip-hash为源地址哈希算法。round-robin
为轮询调度算法，该算法为系统默认算法。
l
email – 指定将日志信息输出到Email地址。关于如何配置Email地址，请参阅“配置Email地址”。
l
localdb – 指定日志信息的输出目的地为设备硬盘卡。（仅部分型号设备支持）。
l
severityseverity-level – 指定输出的威胁日志信息的级别从而对威胁日志信息进行过滤。输出信息的
级别将会是指定级别或者高于指定级别，即数字等于或者小于指定级别。例如指定级别是通告，系统将
会输出通告、警告和错误级别的日志信息。
在全局配置模式下，用以上命令no的形式可以关闭相关的输出功能。命令如下：
no logging threat to {console | remote | syslog | email| localdb }
将威胁日志信息输出到内存缓存，在全局配置模式下使用以下命令：
logging threat to buffer [severity severity-level] [size buffer-size]
l
severity severity-level – 指定输出的威胁日志信息的级别从而对威胁日志信息进行过滤。输出信息的
级别将会是指定级别或者高于指定级别，即数字等于或者小于指定级别。例如指定级别是通告，
StoneOS将会输出通告、警告和错误级别的日志信息。
l
size buffer-size –指定内存缓存的大小。范围是4096到1048576字节。默认值为1048576。
在全局配置模式下，用该命令no logging threat to buffer命令关闭相关的输出功能。
将威胁日志信息输出到文件，在全局配置模式下使用以下命令：
logging threat to file [severity severity-level] [name [usb0 | usb1] file-name] [size file-size]
l
severity severity-level – 指定输出的威胁日志信息的级别从而对威胁日志信息进行过滤。输出信息的
级别将会是指定级别或者高于指定级别，即数字等于或者小于指定级别。例如指定级别是通告，系统将
会输出通告、警告和错误级别的日志信息。
l
name [usb0 | usb1] file-name –该参数用来指定保存日志信息的U盘和日志信息文件的名称。
l
size file-size – 将威胁日志信息输出到文件（U盘或者Flash）时，该参数用来指定日志信息文件的大
小。范围是4096到1048576字节。默认是1048576字节。
在全局配置模式下，用以上命令no logging threat to file命令关闭相关的输出功能。

<!-- 来源页 2551 -->
配置、操作、调试和网络日志信息的输出
用户可以根据需要指定日志信息的输出目的地，可以是缓存、Console口、Syslog服务器、文件和设备硬盘
卡。操作日志和调试日志不可输出到设备硬盘卡。
将日志信息输出到Console口、Syslog服务器或者设备硬盘卡，在全局配置模式下使用以下命令：
logging {configuration | network} to {console | syslog | localdb}
l
configuration | network – 指定将要输出的日志信息的类型，可以是配置（configuration）或者网
络（network）。
l
console – 指定日志信息的输出目的地为Console口。
l
syslog - 指定日志信息的输出目的地为Syslog Server。关于如何配置Syslog Server，请参阅“配置
Syslog Server”。
l
localdb – 指定日志信息的输出目的地为设备硬盘卡。（仅部分型号设备支持）。
logging [ debug | operation ]to {console | syslog}
l
console – 指定调试（debug）和操作（operation）日志信息的输出目的地为Console口。
l
syslog - 指定调试（debug）和操作（operation）日志信息的输出目的地为Syslog Server。关于如
何配置Syslog Server，请参阅“配置Syslog Server”。
在全局配置模式下，用no logging {configuration| operation | debug | network} to {console |
syslog | localdb}命令关闭相关的输出功能。
将配置、操作和网络日志信息输出到文件，在全局配置模式下使用以下命令：
logging {configuration | operation | network} to file [name [usb0 | usb1] file-name] [size
file-size]
l
configuration | operation | network – 指定将要输出的日志信息的类型，可以是配置
（configuration）、操作（Operation）或者网络（network）。
l
name [usb0 | usb1] file-name –该参数用来指定保存日志信息的U盘和日志信息文件的名称。
l
size file-size – 将配置、操作和网络日志信息输出到文件（U盘或者Flash）时，该参数用来指定日志
信息文件的大小。范围是4096到1048576字节。默认是1048576字节。
在全局配置模式下，用以上命令no logging {configuration | operation | network} to file命令关闭相
关的输出功能。
将配置、操作、调试和网络日志信息输出到内存缓存，在全局配置模式下使用以下命令：
logging {configuration | operation | debug | network} to buffer [size buffer-size]

<!-- 来源页 2552 -->
l
configuration | operation | debug | network – 指定将要输出的日志信息的类型，可以是配置
（configuration）、操作（Operation）、调试（debug）或者网络（network）。
l
size buffer-size - 内存缓存的大小。范围是4096到524288字节。默认值为1048576。
在全局配置模式下，用no logging {configuration | operation | traffic | debug | network} to
buffer命令关闭相关的输出功能。
将调试日志信息输出到内存缓存时，如果日志信息超过了内存缓存空间，默认情况下，新的日志信息会覆盖
旧的日志信息。用户可以配置当日志信息超过内存缓存空间时，新的日志信息不覆盖旧的日志信息。进行此
配置，在全局配置模式下使用以下命令：
l
logging debug-buffer stop-overwrite：当日志信息超过内存缓存空间时，系统将停止存储新的调
试日志信息。
l
no logging debug-buffer stop-overwrite：超过内存缓存空间的调试日志信息将自动覆盖旧的日志
信息。
在任意模式下，用户可以通过show logging命令查看当日志信息超过内存缓存空间时，新的调试日志信息
是否覆盖旧的调试日志信息配置情况。
例如：
hostname(config)# show logging
Logging facility: local7
Debug log status: On
==================================================
Destination Status Size Overwrite
--------------------------------------------------
Console Off - -
Buffer On 524288 no( 当日志信息超过内存缓存空间时，新的调试日志信息不会覆盖旧
的调试日志信息)
File Off 1048576 -
Syslog Off - -
==================================================

<!-- 来源页 2553 -->
输出调试日志到文件
用户可以将调试日志输出到文件，然后通过export log debug命令导出到指定文件服务器或U盘。导出到
指定文件服务器或U盘，请参阅导出日志信息。默认情况下，输出调试日志到文件的功能为关闭状态。开启
输出调试日志到文件的功能，在全局配置模式下使用以下命令：
logging debug to file
指定调试日志文件的大小，在全局配置模式下使用以下命令：
logging debug to file size file-size
l
size file-size – 指定调试日志文件的大小。不同平台支持的文件大小和默认值不同，请以实际为准。
在全局配置模式下，使用no logging debug to file命令关闭将调试日志输出到文件的功能。
在任意模式下，使用show logging debug file命令查看输出的调试日志文件的内容。
配置调试功能使用条件
在开启调试功能时，CPU使用率可能会升高而影响到业务转发。用户可以根据情况配置调试功能和业务转发
的优先级。默认情况下，调试功能优先。
指定业务优先，在全局配置模式下，使用以下命令：
log debug-limit cpu-threshold value
l
value - 指定CPU使用率的阈值，单位为百分比。取值范围是0到99。取值为0表示调试优先。取值不为
0时，表示业务转发优先。在业务转发优先场景下，当系统存在多个CPU时，任意一个CPU的使用率达到
指定的阈值时，即认为调试功能影响到了业务转发，将关闭调试功能。
指定调试优先，在全局配置模式下，使用no log debug-limit cpu-threshold或log debug-limit cputhreshold 0命令。
在开启调试功能时，用户可以配置定时器控制调试功能的执行时间，当定时器超时时，将关闭调试功能。在
全局配置模式下，使用以下命令：
log debug-limit time value
l
value - 指定调试功能的执行时间，取值范围是1到60秒。
取消调试的执行时间配置，在全局配置模式下使用no log debug-limit time命令。
注意：同时配置了业务优先和定时器功能时，二者中任何一个达到限制的使用条件，即会关闭调试功能。

<!-- 来源页 2554 -->
流量日志信息的输出
流量日志信息分为会话、NAT和上网日志信息三部分，可以输出到缓存、Console口、Syslog服务器、
IPFIX服务器（仅NAT日志支持输出到IPFIX服务器）和本地硬盘。用户可以根据需要指定不同类别日志信息
的输出目的地。
将流量日志信息输出到Console口、Syslog服务器或者内存缓存，在全局配置模式下使用以下命令：
logging traffic {session | nat | urlfilter} to {console | syslog | buffer [size buffer-size] }
将NAT流量日志信息输出到IPFIX服务器，在全局配置模式下使用以下命令：
logging traffic nat to ipfix-server
将会话、NAT、URL流量日志信息输出到本地硬盘，在全局配置模式下使用以下命令：
logging traffic {session | nat | urlfilter} to localdb
l
session | nat | urlfilter – 指定将要输出的日志信息的类型，可以是会话（session）、NAT（nat）
或者URL（urlfilter）。
l
console | syslog | buffer – 指定日志信息的输出目的地，可以是Console口（console）、输出到
Syslog Server（syslog）或者内存缓存。关于如何配置Syslog Server，请参阅“配置Syslog
Server”。
l
ipfix-server - 指定NAT日志信息（仅NAT444日志）的输出目的地为IPFIX服务器。关于如何配置
IPFIX Server，请参阅“配置IPFIX服务器”。
l
localdb – 指定会话、NAT、URL日志信息(上网urlfilter日志信息暂不支持)的输出目的地为设备硬盘
卡。带硬盘的云·界、K系列（不含K9180）、X系列（不含X9180）、A系列（不含A2200、A1800和
A1600）防火墙支持该功能。
l
size buffer-size - 内存缓存的大小。范围是4096到2097152字节。默认值为1048576。
在全局配置模式下，使用no logging traffic {session | nat | urlfilter} to {console | syslog | buffer
}、no logging traffic nat to ipfix-server或no logging traffic {session | nat | urlfilter} to
localdb命令关闭相关的输出功能。
数据安全日志信息的输出
数据安全日志（文件过滤日志、内容过滤日志、上网行为审计日志）信息可以输出到缓存、Console口、
Syslog服务器。用户可以根据需要指定数据安全日志（文件过滤日志、内容过滤日志、上网行为审计日志）
信息的输出目的地。

<!-- 来源页 2555 -->
输出数据安全日志（文件过滤日志、内容过滤日志、上网行为审计日志）信息到Console、Syslog服务器，
在全局配置模式下使用以下命令：
logging data-security [dlp | cf | nbr] to {console | syslog[binary-format [distributed [src-iphash | round-robin]] | custom-format]] }
l
console – 指定将数据安全日志（文件过滤日志、内容过滤日志、上网行为审计日志）信息输出到
console口。
l
syslog – 指定将数据安全日志（文件过滤日志、内容过滤日志、上网行为审计日志）信息输出到Syslog
Server。关于如何配置Syslog Server，请参阅“配置Syslog Server”。
l
binary-format – 发送二进制类型日志信息。
l
distributed – 分布发送二进制日志信息到多台Syslog服务器。
l
src-ip-hash | round-robin – 指定服务器选择算法。src-ip-hash为源地址哈希算法。round-robin
为轮询调度算法，该算法为系统默认算法。
l
custom-format – 发送明文日志信息。默认情况下，系统发送明文日志信息。
在全局配置模式下，用以上命令no的形式可以关闭相关的输出功能。命令如下：
no logging data-security [dlp | cf | nbr] to {console | syslog }
将数据安全日志（文件过滤日志、内容过滤日志、上网行为审计日志）信息输出到内存缓存，在全局配置模
式下使用以下命令：
logging data-security [dlp | cf | nbr] to buffer [size buffer-size]
l
size buffer-size –指定内存缓存的大小。范围是4096到524288字节。默认值为524288。
在全局配置模式下，用该命令no logging data-security [dlp | cf | nbr] to buffer命令关闭相关的输出
功能。
云沙箱日志信息的输出
云沙箱日志可以输出到缓存、Console口、文件、Syslog服务器。用户可以根据需要指定云沙箱日志的输出
目的地。指定前，用户需在全局配置模式下，使用以下命令开启云沙箱日志功能：
logging sandbox on
在全局配置模式下，使用no logging sandbox on命令关闭云沙箱日志功能。
指定云沙箱日志输出地，在全局配置模式下，使用以下命令：
logging sandbox to {console | syslog | buffer [size buffer-size] | file file-name [size filesize]}

<!-- 来源页 2556 -->
l
console – 指定将云沙箱日志信息输出到console口。
l
syslog – 指定将云沙箱日志信息输出到Syslog服务器。
l
buffer [size buffer-size] - 将云沙箱日志信息输出到内存缓存，并指定缓存的大小。范围是4096到
524288字节。默认值为524288。
l
file file-name [size file-size] - 指定将云沙箱日志信息输出到文件，并指定日志信息文件的大小。范
围是4096到1048576字节。默认是1048576字节。
在全局配置模式下，用以上命令no logging sandbox to {console | syslog | buffer | file}命令关闭相关
的输出功能。
设备日志信息的输出
IT设备和IoT设备的设备日志信息可以输出到缓存、Console口、Syslog服务器。用户可以根据需要指定设
备日志信息的输出目的地。指定前，用户需在全局配置模式下，使用以下命令开启设备日志功能：
logging device on
在全局配置模式下，使用no logging device on命令关闭设备日志日志功能。
输出设备日志信息到缓存、Console、Syslog服务器，在全局配置模式下使用以下命令：
logging device to {console | buffer [size buffer-size] | syslog [custom-format [distributed
[src-ip-hash | round-robin]]]}
l
console – 指定将设备日志信息输出到Console口。
l
syslog – 指定将设备日志信息输出到Syslog Server。关于如何配置Syslog Server，请参阅“配置
Syslog Server”。
l
custom-format – 发送明文日志信息。默认情况下，系统发送明文日志信息。
l
distributed – 分布发送明文日志信息到多台Syslog服务器。
l
src-ip-hash | round-robin – 指定服务器选择算法。src-ip-hash为源地址哈希算法。round-robin
为轮询调度算法，该算法为系统默认算法。
l
custom-format – 发送明文日志信息。默认情况下，系统发送明文日志信息。
在全局配置模式下，使用以上命令no的形式可以关闭相关的输出功能。命令如下：
no logging device to {console | buffer | syslog}

<!-- 来源页 2557 -->
配置日志信息的输出格式
系统按照固定的格式输出日志信息。默认情况下，输出到Syslog Server的日志信息会显示
HillstoneNetworks#字段，不显示年份、主机名称和日志严重等级，将按照以下默认格式输出：<设备号
*8+日志严重等级> 时间设备序列号(VSYS名称) 日志ID HillstoneNetworks#日志类型@模块: 日志描
述。
提示: 按照RFC 3164/5424定义的日志标准：
l
标准格式为：<设备号*8+日志严重等级> 时间主机名称日志ID HillstoneNetworks#日志类
型@模块: 日志描述
l
非标准格式为：<设备号*8+日志严重等级> 时间设备序列号(VSYS名称) 日志ID
HillstoneNetworks#日志类型@模块: 日志描述。
默认格式日志输出示例如下：
<188> Apr 11 02:48:22 25083xxxxxx05643(root) 42340401 HillstoneNetworks#Event@MGMT:
Admin user "hillstone" cleared Debug log\n\000
用户可以根据需要配置日志信息的输出格式。使用以下命令：
l
指定输出的日志信息显示四位数年份：在全局配置模式下，输入logging syslog 4digit-yeartimestamp
输出格式为：<设备号*8+日志严重等级> 四位数年份-日期时区设备序列号(VSYS名称) 日志ID
HillstoneNetworks#日志类型@模块: 日志描述
输出示例为：<188> 2024-04-11T02:49:23.380569Z 25083xxxxxx05643(root) 421c041f
HillstoneNetworks#Event@MGMT: Admin user "hillstone" logout through SSH, the IP is
X.X.X.X, and the corresponding login time is 2024-04-11 02:43:25.\n
l
指定输出的日志信息显示主机名称和日志严重等级：在全局配置模式下，输入logging syslog
additional-information
输出格式为：<设备号*8+日志严重等级> 时间设备序列号(VSYS名称)[h:主机名称日志][p:严重等级] 日
志ID HillstoneNetworks#日志类型@模块: 日志描述
输出示例为：<186> Apr 11 02:50:46 25083xxxxxx05643(root)[h:SG-6000][p:2] 42080a0d
HillstoneNetworks#Event@MGMT: hillstone save system configuration via SSH.\n\000

<!-- 来源页 2558 -->
l
指定输出的日志信息不显示HillstoneNetworks#字段：logging syslog company-name null
输出格式为：：<设备号*8+日志严重等级> 时间设备序列号（VSYS名称）日志ID 日志类型@模块：
日志描述
l
指定输出的日志信息显示主机名称，不显示设备序列号：
1.
在全局配置模式下，进入指定的Syslog服务器配置模式：logging syslog-server servername
2.
在指定的Syslog服务器配置模式下，输入hostname standard
输出格式为：<设备号*8+日志严重等级> 时间主机名称日志ID HillstoneNetworks#日志类型
@模块: 日志描述
输出示例为：<189> Apr 11 02:46:32 SG-6000 43240501
HillstoneNetworks#Event@NET: Static entry is created, 1.1.1.1, 1111.1111.1111,
trust-vr\n\000
在全局配置模式下，使用以下命令取消输出的日志信息显示年份、主机名称和日志严重等级，以及恢复默认
显示的HillstoneNetworks#字段：
l
取消显示四位数年份：在全局配置模式下，输入no logging syslog 4digit-year-timestamp
l
取消显示主机名称和日志严重等级：在全局配置模式下，输入no logging syslog additionalinformation
l
恢复默认显示的HillstoneNetworks#字段：logging syslog company-name default
l
显示设备序列号，取消显示主机名称：在指定的Syslog服务器配置模式下，输入no hostname
standard

<!-- 来源页 2559 -->
配置日志的存储周期
型号说明：
l
不支持：SG-6000-A200、A200W、A200G4、A200WG4、A200-A、A200G4-A、
A200W-A、A200WG4-A
l
不支持：SG-6000-A2200、A1800、A1600
l
不支持：SG-6000-X9180
l
不支持：SG-6000-SD-WAN系列平台
用户可配置事件、网络、配置、会话、威胁、NAT、云沙箱、URL日志的存储周期，超出存储周期的日志将
会被自动删除。存储周期范围是6到12月。在全局配置模式下，使用以下命令：
logging {event | network | configure | threat | sandbox | traffic session | traffic nat | traffic
urlfilter} to localdb storage-time value
l
event | network | configure | threat | sandbox | traffic session | traffic nat | traffic urlfilter
- 指定日志类型，包括事件日志（event）、网络日志（network）、配置日志（configure）、威胁日
志（threat）、云沙箱日志（sandbox）、会话日志（traffic session）、NAT日志（traffic
nat）、URL日志（traffic urlfilter）。
l
storage-time value - 指定日志的存储周期，超出存储周期的日志将会被自动删除。取值范围为6-12
月。
在全局配置模式下，使用以上命令no的形式取消对事件、网络、配置、会话、威胁、NAT、云沙箱、URL日
志存储周期的配置。
no logging {event | network | configure | threat | sandbox | traffic session | traffic nat | traffic
urlfilter} to localdb storage-time
配置日志备份服务器
用户可配置日志备份服务器，将系统中删除的日志转存至指定的服务器。安装有硬盘的K系列设备支持此功
能。
在全局配置模式下，使用以下命令：
logging storage-mgmt localdb backup-to-server {server-ip user user-name password
password filename}

<!-- 来源页 2560 -->
在全局配置模式下，使用以上命令no的形式取消对日志备份服务器的配置。
no logging storage-mgmt localdb backup-to-server
会话日志和NAT日志输出到本地硬盘功能优化
通常情况下，系统的日志处理进程（LOGD）和数据库存储进程（MYSQLD）工作在CPU的Core0上。当将
会话日志和NAT日志输出到本地硬盘时，大量快速的日志数据存储操作会导致Core0处于高负荷运行状态，
存在影响系统其他功能模块正常工作的风险。为解决该问题，当将会话日志和NAT日志输出到本地硬盘时，
用户可以将日志处理进程和数据库存储进程从Core0移至Core MAX，并对日志信息发送至日志处理进程的
速度进行限制。Core MAX为系统中最大编号的CPU核，例如，当系统CPU总核数为12时，CPU编号通常为
Core0 至Core11，Core11即为Core MAX。
建议在将会话日志和NAT日志输出到本地硬盘时，如果Core0性能消耗过大或需要调大日志信息发送至日志
处理进程的速率，可以将日志处理进程和数据库存储进程从Core0移至Core MAX，再调整日志信息发送至
日志处理进程的速率。
将日志处理进程和数据库存储进程绑定至Core MAX
将日志处理进程和数据库存储进程绑定至Core MAX，在全局配置模式下使用以下命令：
cp-multi-cores logd
在全局配置模式下使用no cp-multi-cores logd命令，取消日志处理进程和数据库存储进程与Core MAX
的绑定。
型号说明：
l
将日志处理进程和数据库存储进程绑定至Core MAX功能，仅SG-6000-A2700及以上型号
设备支持。
注意:
l
将日志处理进程和数据库存储进程绑定至Core MAX或者取消绑定，需要重启设备使配置生
效。
l
将日志处理进程和数据库存储进程绑定至Core MAX前，用户需要首先在全局配置模式下，使
用flow-core-num number命令，指定系统数据层面占用CPU核的数量。其中，number的
取值建议为max_core_number-1，max_core_number为系统的CPU核总数。例如，当系
统CPU总核数为12时，配置命令为flow-core-num 11。该配置需要重启设备才会生效。

<!-- 来源页 2561 -->
配置日志信息发送至日志处理进程的速率
配置日志信息发送至日志处理进程的速率，在全局配置模式下使用以下命令：
logging speed-limit to {local value | syslog value}
l
local value - 指定日志信息发送至日志处理进程的速率。取值范围为1-65535条/秒，默认值为3000
条/秒。
l
syslog value - 指定日志信息发送至Syslog服务器的速率。取值范围为1-65535条/秒，默认值为
1000条/秒。
注意: 该功能仅针对单张业务模块卡（如SSM模块卡、SIOM模块卡等）生效。
在全局配置模式下使用no logging speed-limit命令恢复日志信息发送至日志处理进程的默认速率。
查看日志信息发送至日志处理进程的速率配置，在任意模式下使用以下命令：
show logging speed-limit
配置Syslog Server
将日志信息输出到Syslog Server，用户需要配置Syslog Server的相关配置信息，包括：
l 创建Syslog Server
l 配置Syslog Server地址/主机名称
l 指定绑定方式
l 指定Syslog Server的日志格式
l 指定协议类型
l 指定目的端口号
l 开启/关闭Syslog_Server证书禁止检查功能
l 指定输出日志类型
l 指定Syslog Server描述信息
创建Syslog Server
对Syslog Server的各项配置需要在Syslog Server配置模式下进行。创建Syslog Server并进入Syslog
Server配置模式，在全局配置模式下，使用以下命令：
logging syslog-server server-name

<!-- 来源页 2562 -->
l
server-name – 指定Syslog Server的名称，范围为1到127个字符。
执行该命令后，系统创建指定名称的Syslog Server，并且进入Syslog Server配置模式；如果指定的名称
已存在，则直接进入Syslog Server配置模式。
在全局配置模式下使用该命令no的形式删除指定的Syslog Server：
no logging syslog-server server-name
配置Syslog Server地址/主机名称
配置Syslog Server的IP地址或主机名称，在Syslog Server配置模式下，使用以下命令：
server { ip ip-address | hostname hostname}
l
ip ip-address | hostname hostname– 指定Syslog Server的IP地址或者主机名称。
在Syslog Server配置模式下，使用该命令no的形式删除指定的Syslog Server IP地址或者主机名称：
no server { ip | hostname }
指定绑定方式
指定Syslog Server所属的VRouter或发送日志信息的源接口，在Syslog Server配置模式下，使用以下命
令：
bind {vrouter vr-name | source-interface interface-name}
l
vrouter vr-name – 指定VRouter的名称。
l
source-interface interface-name - 指定发送日志信息的源接口，设备会以指定接口的IP地址为源
IP，向Syslog服务器发送日志信息。如果该接口配有管理IP地址，优先使用管理IP地址。
在Syslog Server配置模式下，使用该命令no的形式删除指定的VRouter或者源接口：
no bind {vrouter | source-interface}
指定Syslog Server的日志格式
指定Syslog服务器的日志格式兼容类型，包括CUCC，ECFW，SGCC-S5000和SGCC-S6000，请根据对应
的日志服务器类型进行选择。在Syslog Server配置模式下，使用以下命令：
format-type { CUCC [support-default] | SGCC-S5000 | SGCC-S6000 | ECFW }
l
CUCC [support-default] - 指定日志信息的发送格式。CUCC指按照中国联通日志格式发送NAT444日
志信息。support-default指按照默认格式发送其它类型的日志信息。
l
SGCC-S5000 - 指定日志发送格式为国家电网S5000系列设备日志格式。

<!-- 来源页 2563 -->
l
SGCC-S6000 - 指定日志发送格式为国家电网S6000系列设备日志格式。
l
ECFW - 指定日志发送格式为天翼云威胁日志格式。
恢复默认的日志发送格式（即山石网科设备的标准日志格式），在Syslog Server配置模式下，使用以下命
令：
no format-type
指定协议类型
指定Syslog Server的协议类型，在Syslog Server配置模式下，使用以下命令：
protocol {tcp | udp | secure-tcp}
l
tcp | udp | secure-tcp– 指定协议类型，包括TCP、UDP或者Secure-TCP协议。Secure-TCP协议采
用TLS加密协议。
在Syslog Server配置模式下，使用该命令no的形式删除指定的协议类型：
no protocol
指定目的端口号
指定Syslog Server的目的端口号，在Syslog Server配置模式下，使用以下命令：
dst-port port-number
l
port-number– 指定目的端口号。
在Syslog Server配置模式下，使用该命令no的形式删除指定的目的端口号：
no dst-port
开启/关闭Syslog Server证书禁止检查功能
若Syslog Server的协议类型指定为“Secure-TCP”协议（secure-tcp），用户可根据需要开启Syslog
服务器证书禁止检查功能，即不需验证证书即可正常传输日志，在Syslog Server配置模式下，使用以下命
令：
l 开启：server-cert-check-disable
l 关闭：no server-cert-check-disable
指定输出日志类型
指定输出到Syslog服务器的日志类型，在Syslog Server配置模式下，使用以下命令：
log-enable log-type [log-subtype]

<!-- 来源页 2564 -->
l
log-type - 指定日志信息类型。
l
log-subtype - 对于包含子类型的日志类型，需指定该参数用于指定日志信息子类型。
在Syslog Server配置模式下，使用该命令no的形式删除指定的日志类型：
no log-enable log-type [log-subtype]
指定Syslog Server描述信息
为Syslog Server添加描述信息，在Syslog Server配置模式下，使用以下命令：
description description
l
description – 指定Syslog Server的描述信息。范围是1到255字节。
在Syslog Server配置模式下，使用该命令no的形式删除Syslog Server的描述信息。
no description
指定发送源端口
系统支持指定向Syslog Server发送日志信息时使用的源端口号。指定后，将日志信息输出到Syslog
Server时，系统将会使用该源端口。若不指定，系统将默认使用随机源端口将日志信息输出到Syslog
Server。
在全局配置模式下，使用以下命令：
logging syslog {src-port port-number}
l
src-portport-number - 指定系统向Syslog Server发送日志信息时使用的源端口号。范围是1024到
65535。
在全局配置模式下使用以上命令no的形式取消对发送源端口号的配置，使用默认的随机源端口号将日志信息
输出到Syslog Server。
no logging syslog {src-port port-number}
注意:
l
用户仅可通过WebUI的方式查看已配置的发送源端口号，点击“监控> 日志配置> 发送源端
口设置”进行查看。
l
对于发送到Syslog服务器的二进制日志，将不受发送源端口配置的影响，通过UDP协议使用端
口5566进行发送。

<!-- 来源页 2565 -->
l
当启用SNAT功能时，系统会根据NAT转换后的网络地址端口资源随机选择端口作为发送源端
口。
配置GBK编码
输出到Syslog Server的日志信息默认的编码格式为UTF-8，用户可根据需要开启GBK编码。开启GBK编码
格式后，输出到Syslog Server的日志编码格式将变为GBK编码。在全局配置模式下，使用以下命令：
logging syslog GBK
在全局配置模式下使用no logging syslog GBK命令关闭GBK编码，日志编码格式将恢复为UTF-8编码。
配置日志信息的Facility字段
Facility字段用于标识生成日志信息的设备，当把日志信息输出到Syslog服务器时，Syslog服务器中会显示
该Facility字段。系统支持对日志信息的Facility字段进行全局配置，也支持单独指定事件日志和流量日志的
Facility字段，且单独指定的Facility字段优先级高于全局配置的Facility字段。如不配置，Facility字段默
认为local7。
全局配置日志信息的Facility字段
系统支持对日志信息的Facility字段进行全局配置，该配置对所有类型的日志均可生效。全局配置日志信息
的Facility字段，在全局配置模式下，使用以下命令：
logging facility localx
• localx – 指定日志信息的Facility字段。x的范围是0到7的整数，默认值是7。
在全局配置模式下，使用no logging facility恢复默认值。
单独指定事件日志和流量日志的Facility字段
单独指定事件日志和流量日志的Facility字段，在全局配置模式下，使用以下命令：
logging {event | traffic} facility localx
• localx – 指定事件日志和流量日志的Facility字段。x的范围是0到7的整数。
在全局配置模式下，使用no logging {event | traffic} facility命令删除已指定的Facility字段。
查看事件日志和流量日志的Facility字段
查看日志信息的Facility字段，在任意模式下，使用以下命令：
show logging facility
以下是返回结果示例：

<!-- 来源页 2566 -->
hostname#show logging facility
Event：local0
Traffic：local2
配置二进制日志报文头的版本号字段
以二进制格式发送日志时，多条日志会被合并在同一个报文中发送，每个报文会有一个标准的报文头，报文
头中有验证码、版本号、包含日志数量、设备基本信息这四个字段。其中，设备基本信息字段里会包含设备
的主机名称（hostname），用于标识发送日志的设备。版本号字段分为2、3、4三种，版本号2和版本号3
用于区分解析日志时提取的主机名称长度上限为32字节或64字节，版本号4在主机名称长度上限为64字节的
基础上增加了虚拟系统名称（vsysname）和SN号（sn）。
默认情况下，二进制日志报文头的版本号为2，此时主机名称长度上限为32字节。若设备的主机名称超过此
长度限制，可能会导致在解析二进制日志时，主机名称显示不完整。为避免该问题，系统支持通过配置二进
制日志报文头的版本号来调整主机名称的长度限制。用户可以根据需要将版本号配置为2或3，以适应不同长
度的主机名称。
l
版本号配置为2时：主机名称的长度上限保持为32字节。
l
版本号配置为3时：主机名称的长度上限扩展至64字节。
如果二进制日志报文头中需要携带虚拟系统名称和SN号，则用户可以将版本号配置为4。此外，当设备向
HSM发送二进制日志时，二进制日志报文头的版本号默认为4。
l
版本号配置为4时：主机名称的长度上限为64字节，虚拟系统名称的长度上限为32字节，SN号的长度上
限为32字节。
配置二进制日志报文头的版本号字段，在全局配置模式下，使用以下命令：
logging syslog binary-format version version-number
l
version-number - 指定二进制日志报文头的版本号为2、3或者4。默认情况下，二进制日志报文头的
版本号为2；但当设备向HSM发送二进制日志时，二进制日志报文头的版本号默认为4。
设置流量日志的主机名称/用户名称的显示状态
流量日志信息分为会话、NAT和上网日志信息三类，默认情况下，流量日志中不显示主机名称和用户名称。
在全局配置模式下，输入以下命令使流量日志中显示主机名称或用户名称：
l
在会话、NAT和上网日志日志中显示主机名称：logging content hostname
l
在会话日志中显示用户名称：logging session content username
执行以上命令后，系统显示的流量日志信息中将包含主机名称/用户名称。

<!-- 来源页 2567 -->
注意: 配置NetBIOS名字解析功能是流量日志中主机名称显示的前提条件。详细的配置步骤，请参
阅的“"配置NetBIOS名字解析功能" 在第899页”部分。
在全局配置模式下，使用以上命令no的形式取消主机名称/用户名称的显示：
l
no logging {session | nat | urlfilter} content hostname
l
no logging session content username
开启/关闭会话结束日志记录TCP状态信息功能
为方便用户通过会话结束日志中的TCP状态去判断TCP服务的业务状态，系统支持开启/关闭会话结束日志记
录TCP状态信息功能。启用该功能后，对于产生的TCP协议会话结束日志，系统会在“会话结束原因”中记
录会话结束时的TCP状态信息。该功能默认为关闭状态。
开启会话结束日志记录TCP状态信息功能，在全局配置模式下，输入以下命令：
logging session content tcp-state
在全局配置模式下，使用以上命令no的形式关闭会话结束日志记录TCP状态信息功能：
no logging session content tcp-state
设置威胁日志的用户名称的显示状态
默认情况下，威胁日志中不显示认证用户名称。在威胁日志中显示用户名称，在全局配置模式下，输入以下
命令：
logging threat content username
在全局配置模式下，使用以上命令no的形式取消认证用户名称的显示：
no logging threat content username
配置手机短信相关配置
系统支持将严重等级在严重（Critical）以上的事件日志信息以短信的形式输出到某个手机，需要配置接收
日志信息的手机号码和指定短信发送方式。
配置接收日志信息的手机号码
指定接收事件日志的手机号码，在全局配置模式下，使用以下命令：
logging sms phone-number
l
phone-number – 指定接收事件日志的手机号码。
在全局配置模式下使用no logging sms phone-number命令取消手机号码的指定。

<!-- 来源页 2568 -->
指定短信发送方式
指定短信发送方式，在全局配置模式下，使用以下命令：
logging sms send-mode {modem | gateway sp-name | disable}
l
modem– 指定通过短信猫发送日志信息到手机。
l
gateway sp-name – 指定通过短信网关发送日志信息到手机。用户可通过在gateway参数后使用Tab
键，查看已创建的短信网关SP实例的名称列表，并输入选择的SP实例名称。
l
disable- 关闭通过短信形式发送日志信息功能。
配置日志信息输出到Email地址
系统支持日志信息输出到指定的Email地址，用户需要配置接收日志信息邮件的Email地址以及SMTP服务器
实例。
配置Email地址
配置接收日志信息邮件的Email地址。配置Email地址，在全局配置模式下，使用以下命令：
logging email to email-address smtp smtp-instance
l
email-address – 指定接收日志信息邮件的Email地址。
l
smtp smtp-instance – 指定用于发送邮件的SMTP服务器实例的名称（必须为系统中已经配置成功的
SMTP服务器实例）。
在全局配置模式下使用以上命令no的形式取消对Email地址的配置。
no logging email to email-address
配置SMTP服务器实例
配置SMTP服务器实例，在全局配置模式下，使用以下命令：
smtp name smtp-name server {ip-address | hostname} {from email-addr | vrouter vr-name
from email-addr }[username user-name password password] [ mode { plain | starttls | ssl}] [ 
port server-port]
l
smtp-name – 指定SMTP服务器实例的名称。
l
ip-address | hostname – 指定SMTP服务器的IP地址或者主机名称。
l
email-addr – 指定发件人地址。
l
vrouter vr-name – 指定SMTP服务器的VRouter的名称。

<!-- 来源页 2569 -->
l
username user-name password password – 指定发件人帐号的用户名和密码。
l
mode { plain | starttls | ssl}- 指定系统发送的日志信息邮件的传输方式。
l
plain- 指定为plain方式，日志信息邮件将使用明文且非加密的方式传输。该方式为默认传输方
式。
l
starttls- STARTTLS是对纯文本通信协议的扩展，它将纯文本连接升级为加密连接。指定为
starttls方式，日志信息邮件将使用加密方式传输。
l
ssl - SSL协议是为网络通信提供安全及数据完整性的一种安全协议。指定为ssl方式，日志信息邮
件将使用加密方式传输。
l
port server-port - 指定SMTP服务器的端口号。范围是1到65535。不同传输方式下的默认端口号不
同，PLAIN：25，STARTTLS：25，SSL：465 。
在全局配置模式下，使用no smtp name smtp-name命令删除指定的SMTP服务器实例。
发送测试邮件
完成SMTP实例的配置后，系统可以发送测试邮件，然后用户根据是否收到测试邮件，来排查SMTP服务器的
配置是否正确，或系统与SMTP服务器之间是否网络可达，从而提升用户使用邮件告警功能的体验。
在任意配置模式下，使用以下命令发送测试邮件：
exec send-test-mail to email-addr smtp smtp-name [title title][content content]
l
email-addr - 指定接收测试邮件的邮箱地址。
l
smtp-name - 指定配置好的SMTP实例名称。
l
title - 指定系统发送测试邮件时使用的标题，可输入1-127字符。如不指定，系统将使用默认的标题
“测试邮件”。
l
content - 指定系统发送测试邮件时的正文内容，可输入1-1023字符。如不指定，系统将使用测试邮件
的默认内容进行发送，默认内容为“尊敬的客户您好：本邮件是根据防火墙客户提供的个人邮箱发送的
电子邮件，若您并非防火墙用户，请忽略该邮件，谢谢！”。
配置策略路由日志功能
开启策略路由日志功能后，当策略路由规则被流量匹配到后，系统会产生策略路由日志。
开启策略路由日志功能
设备支持基于策略路由规则来开启日志功能。默认情况下，策略路由日志功能是关闭的。开启或者关闭策略
路由日志功能，请在PBR策略规则配置模式下输入以下命令：

<!-- 来源页 2570 -->
l
开启：log enable
l
关闭：no log enable
如果需要显示策略路由日志，请在全局配置模式下，输入以下命令来开启策略路由日志显示功能：
logging traffic pbr on
在全局配置模式下，使用no logging traffic pbr on命令来关闭策略路由日志显示功能。
当配置了目的路由优先查找后，即使流量匹配到了策略路由规则，系统也不会产生策略路由日志。
策略路由日志信息的输出
策略路由的流量日志可以输出到Console终端、Syslog服务器和内存缓存。用户可以根据需要指定输出目的
地。
将策略路由的流量日志信息输出到Console终端、Syslog服务器或者内存缓存，在全局配置模式下使用以下
命令：
logging traffic pbr to {console | syslog | buffer [size buffer-size]}
l
console | syslog | buffer – 指定日志信息的输出目的地，可以是Console终端（console）、输出到
Syslog Server（syslog）或者内存缓存。关于如何配置Syslog Server，请参阅“配置Syslog
Server”。
l
size buffer-size - 内存缓存的大小。范围是4096到2097152字节。默认值为1048576。
在全局配置模式下，用no logging traffic pbr to {console | syslog | buffer}命令关闭相应的输出功
能。
设备不支持输出：
l
二进制格式的策略路由日志。
l
IPv6的策略路由日志。
配置PBR日志主机名/用户名的显示状态
默认情况下，策略路由日志中不显示主机名和用户名信息。在策略路由日志中显示主机名或用户名信息，请
在全局配置模式下，使用以下命令：
logging pbr content {hostname | username}
在全局配置模式下，用no logging pbr content {hostname | username}命令取消在策略路由日志中显
示主机名或用户名信息。

<!-- 来源页 2571 -->
显示策略路由日志信息
用户可以在任何模式下通过以下命令查看所有的策略路由日志信息：
show logging traffic pbr
配置日志参数
系统支持配置事件日志、网络日志、配置日志的参数，包括日志的级别、描述信息，也可以关闭指定日志生
成。
注意:
l
对于支持将事件日志、网络日志、配置日志信息存储到本地数据库的设备，不支持配置日志参
数。
l
非根VSYS不支持配置日志参数。
关闭日志生成
关闭指定ID日志的生成，请在全局配置模式下，使用以下命令：
logging logid [hex] log-id off [description description]
l
hex - 指定日志ID格式为十六进制。如不指定该参数，默认日志ID格式为十进制。
l
log-id - 关闭指定ID的日志生成。说明：指定十六进制的日志ID时，无需输入十六进制前缀“0x”。
l
description description - 修改指定ID的日志描述信息。
在全局模式下，使用命令no logging logid[hex] log-id off取消关闭指定ID日志的生成。
配置日志级别
配置日志级别，请在全局配置模式下，使用以下命令：
logging logid [hex] logid severity severity-level [description description]
l
hex - 指定日志ID格式为十六进制。如不指定该参数，默认日志ID格式为十进制。
l
log-id - 关闭指定ID的日志生成。说明：指定十六进制的日志ID时，无需输入十六进制前缀“0x”。
l
severity severity-level - 指定日志的级别，包括紧急（EMERG）、警报（ALERT）、严重
（ALERT）、错误（ERR）、警告（WARNING）、通告（NOTICE）及信息（INFO）。
l
description description - 修改指定ID的日志描述信息。
在全局模式下，使用命令no logging logid [hex] logid severity取消配置指定ID日志的级别。

<!-- 来源页 2572 -->
开启/关闭威胁日志记录认证用户信息功能
用户可以开启威胁日志记录认证用户信息功能，开启该功能后，威胁日志中会记录认证用户信息，包括AAA
服务器、用户名称、主机名称。默认情况下，该功能为关闭状态，开启威胁日志记录认证用户信息功能，请
在全局配置模式下，使用以下命令：
logging threat content username
在全局配置模式下，使用no logging threat content username命令关闭威胁日志记录认证用户信息功
能。
显示配置日志参数的日志条目
显示配置了日志参数的日志条目，请在全局模式下，使用以下命令：
show logging logid config
配置长期存储日志文件
系统支持长期存储事件日志文件和配置日志文件。该功能默认为关闭状态。
配置长期存储日志文件，在全局配置模式下，使用以下命令：
logging {event | configuration} to file storage-time time-value
l
event | configuration - 指定需要长期存储的日志文件类型，包括事件日志文件（event）和配置日志
文件（configuration）。
l
time-value - 指定日志文件的存储周期，超出存储周期的日志文件将会被自动删除。取值范围为6-12
月。
关闭长期存储日志文件，在全局配置模式下，使用以下命令：
no logging {event | configuration} to file storage-time
配置备份日志文件
系统支持定期将日志信息文件通过FTP/TFTP传输到日志文件备份服务器进行备份。用户也可以手动进行全
量备份，将设备近一年的日志信息文件全部传输到日志文件备份服务器进行备份，但不包含当天的日志数
据。
注意: 备份日志文件前，请先检查日志文件备份服务器的配置以及连通性。相关配置参见配置日志
文件备份服务器章节。
备份日志文件，在全局配置模式下，使用以下命令：

<!-- 来源页 2573 -->
logging {event | configuration} to file backup file-transfer-server server-name [daily |
weekly | monthly | full-sync]
l
event | configuration - 指定需要备份的日志文件类型，包括事件日志文件（event）和配置日志文件
（configuration）。
l
server-name - 指定日志文件备份服务器的名称。
l
daily | weekly | monthly - 指定增量备份周期，包括每天/每周/每月，默认为每周。指定后，系统将
定期把周期内新增的日志信息文件传输到日志文件备份服务器。
l
full-sync - 进行全量备份。系统会将设备近一年的日志信息文件全部传输到日志文件备份服务器进行备
份，但不包含当天的日志数据。在备份大量日志信息文件时，系统需要一定时间进行分批备份，请用户
耐心等待。
取消备份日志文件，在全局配置模式下，使用以下命令：
no logging {event | configuration} to file backup file-transfer-server server-name
配置日志文件备份服务器
用户可以配置日志文件备份服务器，用于接收日志信息备份文件。
配置日志文件备份服务器，在全局配置模式下，使用以下命令：
logging file-transfer-server name vrouter vrouter-name {ftp server-ip ip-address [user
user-name password password] | tftp server-ip ip-address} [filepath]
l
file-transfer-server name - 指定日志文件备份服务器的名称，取值范围为1-31个字符。
l
vrouter vrouter-name - 指定日志文件备份服务器所属的虚拟路由器。
l
ftp | tftp - 指定通过FTP协议或者TFTP协议传输日志信息文件。
l
server-ip ip-address - 指定日志文件备份服务器的IP地址。
l
user user-name - 指定日志文件备份服务器的用户名，取值范围为1-31个字符。
l
password password - 指定日志文件备份服务器的密码，取值范围为1-31个字符。
l
filepath - 指定日志文件备份服务器的路径，系统会将日志信息文件文件上传到指定的服务器路径下。
取值范围为1-255个字符。
删除日志文件备份服务器，在全局配置模式下，使用以下命令：
no logging file-transfer-server name

<!-- 来源页 2574 -->
查看日志文件备份服务器
查看日志文件备份服务器，在任意模式下，使用以下命令：
show logging file-transfer-server
以下是返回结果示例：
hostname(config)# show logging file-transfer-server
Logging file transfer server table:
=============================================================
Name VR Protocol Server-ip User Filepath
---------------------------------------------------------------------
----------------------------------------------------------
test trust-vr FTP 1.1.1.1 user /path
=============================================================
显示日志配置信息
用户可以在任何模式下通过以下命令查看日志配置信息：
l
查看系统日志信息配置状态：show logging
l
查看Syslog服务器的配置信息：show logging syslog-server
l
查看Email地址的配置信息：show logging email
l
查看系统日志信息的统计信息：show logging statistics
l
查看SMTP服务器配置信息：show smtp
l
查看日志中主机名称和用户名称的显示状态：show logging content
l
查看接收事件日志的手机配置信息：show logging sms
显示日志信息
用户可以在任何模式下通过以下命令查看日志信息：
l
显示事件日志信息：
show logging event [severity severity-level]
l
显示调试、网络或者威胁日志信息：
show logging {debug [slot slot-number] [cpu cpu-number]| network | threat }

<!-- 来源页 2575 -->
l
显示配置日志信息：
show logging configuration
l
显示操作日志信息：
show logging [operation]
l
显示数据安全日志（文件过滤日志、内容过滤日志、上网行为审计日志）：
show logging data-security [dlp | cf | nbr]
l
显示所有流量日志信息：
show logging traffic
l
显示流量日志信息（会话日志部分）：
show logging traffic session filter-session [src-ip A.B.C.D | src-port port-num | dst-ip
A.B.C.D | dst-port port-num | protocol {icmp | tcp | udp | others} | policy-id policy-id |
action {policy-deny | session-start | session-end | policy-default}]
l
显示流量日志信息（NAT日志部分）：
show logging traffic nat filter-nat [src-ip A.B.C.D | src-port port-num | dst-ip A.B.C.D |
dst-port port-num | protocol {icmp | tcp | udp | others} | trans-src-ip A.B.C.D | trans-srcport port-num | trans-dst-ip A.B.C.D | trans-dst-port port-num | snat-rule-id rule-id |
dnat-rule-id rule-id | bnat-rule-id rule-id]
l
显示流量日志信息（URL日志部分）：
show logging traffic urlfilter
l
显示IT和IoT设备的设备日志信息：
show logging device
导出日志信息
用户可以导出调试、事件和威胁日志信息，导出的目的地包括FTP/FTPS/SFTP服务器、TFTP服务器和U
盘。
导出调试、事件或威胁日志信息到FTP/FTPS/SFTP服务器
导出调试、事件或威胁日志信息到FTP/FTPS/SFTP服务器，在执行模式使用以下命令：
export log {debug | event | threat } to {ftp | ftps | sftp} server ip-address vrouter vroutername user user-name password password [file-name]

<!-- 来源页 2576 -->
l
debug | event | threat - 指定导出的系统日志的类型。
l
ip-address - 指定FTP/FTPS/SFTP服务器的IP地址。
l
vrouter-name - 指定虚拟路由器的名称。
l
user user-name password password - 指定访问FTP/FTPS/SFTP服务器的用户名和密码。
l
file-name - 指定导出的日志信息文件的名称。
导出调试、事件或威胁日志信息到TFTP服务器
导出调试、事件或威胁日志信息到TFTP服务器，在执行模式下使用以下命令：
export log {debug | event | threat} to tftp server ip-address [file-name]
导出调试、事件或威胁日志信息到U盘
导出调试、事件或威胁日志信息到U盘，在执行模式下使用以下命令：
export log {debug | event | threat } to {usb0 | usb1} [file-name]
清除日志信息
用户可以通过命令将日志信息从系统中清除。清除系统日志信息，在执行模式下，使用以下命令：
clear logging { configuration | operation | debug | event | network | threat | traffic {session |
nat | urlfilter} | data-security [dlp | cf | nbr] | device}
l
configuration -清除所有系统存储的配置日志信息。
l
operation -清除所有系统存储的操作日志信息。
l
debug – 清除所有系统存储的调试日志信息。
l
event – 清除所有系统存储的事件日志信息。
l
network – 清除所有系统存储的网络日志信息。
l
threat – 清除所有系统存储的威胁日志信息。
l
traffic {session | nat | urlfilter}– 清除所有系统存储的流量日志信息，可以是会话（session）、
NAT（nat）或者URL（urlfilter）日志信息。
l
data-security [dlp | cf | nbr] – 清除所有系统存储的数据安全日志信息，可以是文件过滤日志
（dlp）、内容过滤日志（cf）、上网行为审计日志（nbr）。
l
device – 清除所有系统存储的IT和IoT设备的设备日志信息。

<!-- 来源页 2577 -->
注意: 该命令不能清除以下重要的事件日志信息：
l
重启：系统重启、模块卡重启；
l
硬件发生异常：风扇、电源等；
l
配置信息删除或回滚；
l
主备设备切换；
l
双主控HA。

<!-- 来源页 2578 -->
日志分布式外发
设备产生大量的日志信息时，单台Syslog服务器可能无法满足日志信息的接收需求。针对这一问题，
Hillstone设备提供日志分布式外发功能，即设备能够按照一定的算法把日志信息分布发送到多个Syslog服
务器，进而缓解单台Syslog服务器的压力，保证日志信息的完整、快速发送和接收。
注意: 当前版本仅支持流量和数据安全日志信息的分布式发送以及威胁日志的明文日志分布式发
送。
配置流量日志信息的分布式发送功能
配置流量日志信息的分布式发送功能，在全局配置模式下使用以下命令：
logging traffic {session | nat} to syslog server server-name [binary-format | custom-format]
[full | distributed {src-ip-hash | round-robin}]
logging traffic urlfilter to syslog [binary-format | custom-format] [distributed {src-ip-hash |
round-robin}]
l
traffic {session | nat | urlfilter} – 指定分布发送式发送的日志信息类型。
l
syslog – 发送日志信息到Syslog服务器。
l
server server-name - 为指定Syslog服务器配置分发方式和分布式算法。
l
binary-format | custom-format - 指定日志信息的分发方式，发送二进制类型或明文日志信息。默
认情况下，系统发送明文日志信息。
l
full - 发送全量日志信息到Syslog服务器，默认情况下，系统将发送全量日志信息。
l
distributed [src-ip-hash | round-robin] – 分布发送日志信息到多台Syslog服务器并指定分布式算
法。src-ip-hash为源地址哈希算法，round-robin为轮询调度算法，默认为轮询调度算法。
在全局配置模式下，使用以下命令取消日志信息到Syslog服务器的输出：
no logging traffic {session | nat | urlfilter} to syslog
查看流量日志信息的分布式发送配置
查看流量日志信息中的会话日志和NAT日志的分布式发送功能配置，包括每个Syslog服务器的分发方式和分
布式算法。在全局配置模式下使用以下命令：
show logging traffic {{session | nat} syslog-server | urlfilter}
l
session | nat | urlfilter - 查看指定日志类型的分布式发送配置。

<!-- 来源页 2579 -->
SG-6000# show logging traffic session syslog-server
Server Name (* - set individual)
=====================================================================
server-name data-format distribute-mode
---------------------------------------------------------------------
security_management plaintext round-robin
=====================================================================
配置数据安全日志信息的分布式发送功能
配置数据安全日志信息的分布式发送功能，在全局配置模式下使用以下命令：
logging data-security [dlp | cf | nbr] to syslog [binary-format | custom-format] [distributed
{src-ip-hash | round-robin}]
l
data-security [dlp | cf | nbr] – 指定分布发送式发送的日志信息类型。
l
syslog – 发送日志信息到Syslog服务器。
l
binary-format – 发送二进制类型日志信息。
l
distributed – 分布发送二进制日志信息到多台Syslog服务器。
l
src-ip-hash | round-robin – 指定服务器选择算法。src-ip-hash为源地址哈希算法，round-robin
为轮询调度算法，默认为轮询调度算法。
l
custom-format – 发送明文日志信息。默认情况下，系统发送明文日志信息。
在全局配置模式下，使用以下命令取消日志信息到Syslog服务器的输出：
no logging data-security [dlp | cf | nbr] to syslog
配置威胁日志信息的明文日志分布式发送功能
配置威胁日志信息的明文日志分布式发送功能，在全局配置模式下使用以下命令：
logging threat to syslog [custom-format [distributed [src-ip-hash | round-robin]]]
l
custom-format – 发送明文日志信息。默认情况下，系统发送明文日志信息。
l
syslog – 发送日志信息到Syslog服务器。
l
distributed – 分布发送日志信息到多台Syslog服务器。
l
src-ip-hash | round-robin – 指定服务器选择算法。src-ip-hash为源地址哈希算法。round-robin
为轮询调度算法，该算法为系统默认算法。
在全局配置模式下，使用以下命令取消日志信息到Syslog服务器的输出：
no logging threat to syslog

<!-- 来源页 2580 -->
即时通信服务器
企业微信、钉钉和飞书是当下被众多企业广泛采用的综合性办公软件平台，它们集成了即时通讯、协同办
公、日程管理、文件共享等多种功能，以提升企业内部沟通与协作效率。防火墙支持向企业微信、钉钉和飞
书发送事件日志和威胁日志，通过特定API接口以消息形式发送至这些办公软件的群组中，以便相关运维人
员及时知晓。
在系统上配置即时通信服务器，有以下作用：
及时通知运维人员：运维团队能在第一时间收到防火墙发出的告警消息，无论其身处何地，只要手机或电脑
登录了对应的办公软件，即可迅速响应，避免安全事件或故障的扩大化。例如，当防火墙检测到有异常的外
部IP 地址频繁尝试入侵企业网络时，威胁日志能立即推送到运维人员的企业微信上，使其及时采取封禁IP
等应对措施。
契合现有办公流程：企业员工日常频繁使用企业微信、钉钉或飞书进行工作沟通。将事件日志和威胁日志日
志集成到这些熟悉的平台，无需员工再额外登录专门的监控系统查看告警，减少了操作步骤，提高了运维响
应效率。
便于集中管理与跟踪：在办公软件中接收事件日志和威胁日志，方便企业对所有安全及运维相关信息进行集
中管理。企业可以在办公软件内创建专门的告警群组，将相关人员加入其中，大家可以在群内针对告警进行
讨论、记录处理过程和结果，便于后续跟踪和复盘，提升整体运维管理水平。
即时通信服务器配置流程
1. 在企业微信、钉钉或飞书的指定群组中添加群机器人，添加成功后，群机器人自动生成Webhook地址和数字签
名。
2. 在防火墙中配置即时通信服务器，复制已获取的Webhook地址和数字签名到配置中。如果相关平台不支持设置
签名校验，则系统无需配置数字签名。
3. 在日志配置中，对事件日志和威胁日志开启日志输出到即时通信服务器，以及设置最小日志级别。
4. 防火墙通过群机器人，将事件日志和威胁日志以消息形式发送到指定群组中。
配置即时通信服务器
用户可以配置企业微信、钉钉和飞书的即时通信服务器。系统将会通过配置好的即时通信服务器，将事件日
志、威胁日志以消息形式发送到指定的群组中。
前提条件
配置即时通信服务器前，请先在企业微信、钉钉和飞书的群组中添加群机器人，用于获取Webhook地址和
数字签名。如果相关平台不支持设置签名校验，则系统无需配置数字签名。

<!-- 来源页 2581 -->
本节包含如下内容：
l 创建/删除即时通信服务器
l 配置Webhook地址
l 配置数字签名
l 配置绑定方式
创建/删除即时通信服务器
创建即时通信服务器，在全局配置模式下，使用以下命令：
logging webhook-server webhook-server-name server-type {dingtalk | lark | wechatcom}
l
algorithm-name - 指定即时通信服务器的名称。范围是1到31个字符。
l
dingtalk | lark | wechatcom - 指定即时通信服务器的类型。dingtalk为钉钉，lark为飞书，
wechatcom为企业微信。
执行该命令后，系统创建指定名称和类型的即时通信服务器，进入即时通信服务器配置模式。如果指定的即
时通信服务器已存在，则直接进入即时通信服务器配置模式。
在全局配置模式下，使用该命令no的形式删除指定的即时通信服务器：
no logging webhook-server webhook-server-name
编辑已有即时通信服务器
编辑已有即时通信服务器，在全局配置模式下，使用以下命令：
logging webhook-server webhook-server-name
l
webhook-server-name – 指定已有即时通信服务器的名称，范围是1到31个字符。
执行该命令后，直接进入即时通信服务器配置模式。
配置Webhook地址
Webhook地址是即时通信服务器的URL地址。配置Webhook地址，在即时通信服务器配置模式下，使用以
下命令：
webhook-url url-address
l
url-address - 指定即时通信服务器的Webhook地址。Webhook地址从群机器人设置中复制获取。
提示：对于带?的Webhook地址，需要分两部分复制。先复制?之前的地址，然后在命令行中点击鼠标右
键复制进来，接着键入crtl+v，再复制?及之后的地址。

<!-- 来源页 2582 -->
在即时通信服务器配置模式下，使用该命令no的形式删除指定即时通信服务器的Webhook地址：
no webhook-url
配置数字签名
配置数字签名，在即时通信服务器配置模式下，使用以下命令：
webhook-key key
l
key - 指定即时通信服务器的签名密钥。密钥从群机器人设置中复制获取。密钥为数字签名，用于保护
数据传输。当系统向即时通信服务器发送请求时，即时通信服务器需要通过签名校验保障报文来源可
信。
提示：对于带?的Webhook地址，需要分两部分复制。先复制?之前的地址，然后键入crtl+v，再复制?
及之后的地址。
在即时通信服务器配置模式下，使用该命令no的形式删除指定即时通信服务器的Webhook地址：
no webhook-key
配置绑定方式
配置绑定方式，在即时通信服务器配置模式下，使用以下命令：
bind {vrouter vrouter-name | source-interface interface-name}
l
vrouter-name - 指定绑定方式为虚拟路由器。系统通过虚拟路由器对应的接口向即时通信服务器发送
日志信息。在vrouter参数后面使用Tab键，查看系统中已存在的虚拟路由器。
l
interface-name - 指定绑定方式为源接口。系统通过源接口向即时通信服务器发送日志信息。在
source-interface参数后面使用Tab键，查看系统中已存在的接口。
在即时通信服务器配置模式下，使用该命令no的形式删除指定即时通信服务器的绑定方式：
no bind {vrouter | source-interface}
配置源端口
系统支持指定向即时通信服务器发送日志信息时使用的源端口号。指定后，将日志信息输出到即时通信服务
器时，系统将会使用该源端口。若不指定，系统将默认使用随机源端口将日志信息输出到即时通信服务器。
配置系统向即时通信服务器发送日志信息的源端口，在即时通信服务器配置模式下，使用以下命令：
src-port port-number
l
port-number - 指定系统向即时通信服务器发送日志信息时使用的源端口号。范围是1024到65535。

<!-- 来源页 2583 -->
在即时通信服务器配置模式下，使用该命令no的形式取消对源端口号的配置，使用默认的随机源端口号将日
志信息输出到即时通信服务器：
no src-port
配置发送日志信息的速度
配置系统向即时通信服务器发送日志信息的速度，在即时通信服务器配置模式下，使用以下命令：
send-speed count
l
count - 指定发送日志信息的速度。范围是每分钟1到20条。默认是每分钟最多发送20条日志信息。
在即时通信服务器配置模式下，使用该命令no的形式恢复默认值：
no send-speed
将事件日志、威胁日志输出到即时通信服务器
将事件日志、威胁日志信息输出到即时通信服务器，并且对日志信息进行过滤，在全局配置模式下使用以下
命令：
logging {event | threat} to webhook-server [severity severity-level]
l
event – 指定将事件日志信息输出到即时通信服务器。
l
threat – 指定将威胁日志信息输出到即时通信服务器。
l
severity severity-level – 指定输出的事件日志信息的级别从而对事件日志信息进行过滤。输出信息的
级别将会是指定级别或者高于指定级别，即数字等于或者小于指定级别。在severity参数后面使用Tab
键，查看系统支持设置的最小日志级别。
日志输出到即时通信服务器，威胁日志默认最小日志级别是警告；事件日志默认最小日志级别是严重。
例如指定级别是严重，系统将会输出严重、警报和紧急级别的日志信息。
在全局配置模式下，使用以上命令no的形式可以关闭相关日志输出到即时通信服务器的功能。命令如下：
logging {event | threat} to webhook-server
查看事件日志、威胁日志输出到即时通信服务器的开关启用状态
查看事件日志、威胁日志输出到即时通信服务器的开关启用状态，以及最小日志级别，在任意模式下使用以
下命令：
show logging
例如：
SG-6000(config)# show logging

<!-- 来源页 2584 -->
Logging facility: local7
Event log status: On
========================================================
Destination Status Severity Size
--------------------------------------------------------
Console Off warnings -
Remote Off warnings -
Buffer On debugging 1048576
File Off warnings 1048576
Syslog Off debugging -
Email Off warnings -
Sms Off critical -
Localdb On debugging -
Webhook On critical -（显示事件日志输出到即时通信服务器的开关已开启，最小日志级别是严重）
========================================================
Threat log status: On
========================================================
Destination Status Severity Size Format Distribute Mode
--------------------------------------------------------------------------------
Console Off warnings - - - -
Remote Off warnings - - - -
Buffer On informational 524288 - - -
File Off warnings 1048576 - - -
Syslog Off informational - - - -
Email Off warnings - - - -
Localdb Off informational - - - -
Webhook Off warnings - - - -（显示威胁日志输出到即时通信服务器的开关未开启，最小日志级别是
警告）
=========================================================

<!-- 来源页 2585 -->
日志过滤
为解决同类型的海量日志外发至服务器后，用户难以高效定位关键信息、且大量无效日志占用存储资源的问
题，系统提供了灵活的日志过滤功能。该功能支持用户自定义过滤条件，在日志外发前进行精准过滤，仅将
符合条件的日志发送至服务器，从而有效提升日志外发的精准度，减轻用户侧的筛选压力。
该功能仅对已满足系统最小日志级别要求的日志生效；在此基础上，若系统已配置具体过滤规则，则过滤功
能会进一步对这些日志进行匹配，最终仅外发同时满足级别要求和过滤规则的日志（即二者取交集），若未
配置任何过滤规则，则过滤功能不执行额外操作，直接外发所有符合级别要求的日志。
目前仅威胁日志支持该功能。系统执行威胁日志过滤外发的流程图如下所示：
1. 日志分类判定：将系统产生的日志进行分类并判断是否为威胁日志。若不是，则按照各类日志配置直接外发；若
是，则进入下一处理环节。
2. 最小日志级别筛选：系统依据威胁等级与日志级别的映射关系表，结合预设的“最小日志级别”条件进行日志筛
选。日志级别由高到低依次为“严重”、“警告”、“信息”，即严重级别高于警告，警告高于信息。
l 威胁等级所对应的日志级别低于“最小日志级别”阈值的日志，不予外发，流程终止。
l 威胁等级所对应的日志级别达到或高于“最小日志级别”阈值的日志，进入下一处理环节。
以最小日志级别预设为“严重”为例：威胁等级为“高”和“严重”的日志，其对应日志级别达到阈
值，通过筛选；威胁等级为“低”和“中”的日志，其对应日志级别为“警告”，低于阈值，不予外
发。

<!-- 来源页 2586 -->
以下是威胁等级与日志级别的映射关系表：
威胁等级
对应日志级别
低
警告
中
警告
高
严重
严重
严重
3. 过滤规则配置判定：检查是否已配置日志过滤规则。若未配置，系统则直接转发符合最小日志级别条件的日志，
不会执行下一步过滤操作；若已配置，则进入下一处理环节。
4. 过滤规则匹配：根据已配置的过滤规则条件对日志进行匹配。符合规则条件的威胁日志予以外发；不符合规则条
件的威胁日志不予外发。
威胁日志过滤规则、过滤规则条件请见以下示意图：
l ①：过滤规则。用于定义筛选条件。在日志过滤配置中最多可包含一条过滤规则。
l ②：过滤规则条件之一：过滤字段。当前仅支持选择“威胁等级”字段。
l ③：过滤规则条件之一：关系运算符。威胁等级使用6种关系运算符，分别为等于、大于、大于等于、小于、小
于等于、不等于。
l ④：过滤规则条件之一：阈值。威胁等级阈值包含低、中、高、严重4个级别，其严重程度由高到低依次为：严
重> 高> 中> 低。
过滤规则匹配原则：根据最小日志级别条件与过滤规则的交集进行过滤，即最终外发的日志必须同时满足两
者设定的威胁等级匹配条件。
过滤规则匹配逻辑：

<!-- 来源页 2587 -->
l 一条过滤规则必须包含过滤字段、关系运算符以及阈值三个条件。
l 一条过滤规则内的多个条件为“且”的关系，即匹配时必须全部条件均满足，才算匹配规则。
下表列出几种匹配示例，供参考。其中，“最小日志级别允许的等级集合”依据威胁等级与日志级别的映射
关系得出，再与过滤规则筛选的集合进行交集运算，得到最终匹配结果。
最小日志级别
过滤规则
匹配结果
警告
过滤字段：威胁等级
关系运算符：小于
阈值：低
× 不匹配
不存在更小级别。
警告
过滤字段：威胁等级
关系运算符：大于
阈值：中
× 不匹配
两者交集为空，故匹配失败。
运算公式：{低，中} ∩{高，严重} = ∅（空集）
警告
过滤字段：威胁等级
关系运算符：不等于
阈值：严重
√匹配
两者交集为“低、中”，非空，故匹配成功。
运算公式：{低，中} ∩{低，中，高} = {低，中}
严重
过滤字段：威胁等级
关系运算符：等于
阈值：严重
√匹配
两者交集为“严重”，非空，故匹配成功。
运算公式：{高，严重} ∩{严重} = {严重}
严重
过滤字段：威胁等级
关系运算符：小于等于
阈值：中
× 不匹配
两者交集为空，故匹配失败。
运算公式：{高，严重} ∩{低，中} = ∅（空集）
严重
过滤字段：威胁等级
关系运算符：大于等于
阈值：高
√匹配
两者交集为“高、严重”，非空，故匹配成功。
运算公式：{高，严重} ∩{高，严重} = {高，严重}
配置日志过滤器
目前，系统仅支持配置一个威胁日志过滤器。配置日志过滤器，在全局配置模式下，使用以下命令：
logging threat filter filter-name
l
filter-name - 指定日志过滤的名称。取值范围是1到127个字符。
执行该命令后，系统创建指定名称的日志过滤器，并进入日志过滤配置模式。如果指定的日志过滤器已存
在，则直接进入日志过滤配置模式。
在全局配置模式下，使用该命令no的形式删除指定的日志过滤器及其所有配置：
no logging threat filter filter-name

<!-- 来源页 2588 -->
添加描述
为威胁日志过滤器添加相关描述信息，在日志过滤配置模式下，使用以下命令：
description description
l
description - 输入详细的描述信息，取值范围为1-255个字符。
在日志过滤配置模式下，使用该命令no的形式删除描述信息：
no description
配置过滤规则集合
过滤规则集合通常由一条或多条过滤规则构成。目前，系统仅支持配置一个过滤规则集合。
配置过滤规则集合，在日志过滤配置模式下，使用以下命令：
filter-group [id]
l
id - 指定过滤规则集合的ID。目前仅支持ID为1。若不指定，则由系统自动分配。
执行该命令后，系统创建指定ID的过滤规则集合，并进入日志过滤规则配置模式。如果指定的过滤规则集合
已存在，则直接进入日志过滤规则配置模式。
在日志过滤配置模式下，使用该命令no的形式删除指定ID的过滤规则集合及其包含的过滤规则：
no filter-group id
配置过滤规则
目前，一个过滤规则集合下仅支持配置一条过滤规则。一条过滤规则包含过滤字段（仅支持“威胁等级”字
段）、关系运算符以及阈值三个条件。
配置过滤规则，在日志过滤规则配置模式下，使用以下命令：
match [id] threat_severity {= | > | >= | < | <= | !=} {low | medium | high | critical}
l
id - 指定过滤规则ID。目前仅支持ID为1。若不指定，则由系统自动分配。
l
threat_severity - 威胁等级。
l
{= | > | >= | < | <= | !=} - 关系运算符。支持等于（=）、大于（>）、大于等于（>=）、小于（<）、小
于等于（<=）以及不等于（!=）6种运算符。
l
{low | medium | high | critical} - 威胁等级阈值。支持低（low）、中（medium）、高（high）以
及严重（critical）4个级别，其严重程度由高到低依次为：严重> 高> 中> 低。

<!-- 来源页 2589 -->
绑定日志外发目的地
绑定日志需要外发的目的地。目前，系统仅支持将匹配过滤规则的威胁日志外发到本地数据库、邮箱以及日
志服务器。
注意: 配置日志过滤时，必须确保所绑定的日志外发目的地已在日志设置中同步开启，否则日志将
无法外发至该目的地。
绑定日志外发目的地，在日志过滤配置模式下，使用以下命令：
bind {email | localdb | syslog-server server-name}
l
email - 将过滤后的日志外发到邮箱。
l
localdb - 将过滤后的日志外发到本地数据库。
l
syslog-server server-name - 将过滤后的日志外发到指定名称的日志服务器。
如需绑定多个目的地，可重复执行上述命令进行配置。
在日志过滤配置模式下，使用该命令no的形式取消绑定配置：
no bind {email | localdb | syslog-server server-name}
查看日志过滤配置
查看日志过滤配置，在任意模式下使用以下命令：
show logging threat filter
例如：
hostname# show logging threat filter
===============================================
----------------------------------------------------------
filter-name: test
description:
group 1:
    match 1: threat_severity = medium
bind-email: off
bind-localdb: on
bind-syslog-server: on

<!-- 来源页 2590 -->
security_management
    test
-----------------------------------------------------------
================================================

<!-- 来源页 2591 -->
日志功能配置举例
本节介绍两个典型的日志功能CLI配置示例，分别为向Console口输出日志信息配置示例和向Syslog Server
输出日志信息配置示例。
示例1：向Console口输出事件日志信息
第一步：开启事件日志功能。
hostname# configure
hostname(config)# logging event on
第二步：配置Console口日志输出，信息级别为Debugging。
hostname(config)# logging event to console severity debugging
示例2：向Syslog Server输出事件日志信息
第一步：开启日志功能，将IP地址为202.38.1.10的工作站用作Syslog Server，类型为UDP，设置信息级
别为Informational。
hostname(config)# logging event on
hostname(config)# logging syslog 202.38.1.10 udp 514 type event
hostname(config)# logging event to syslog severity informational
第二步：开启Syslog Server。
示例3：向本地文件输出流量日志信息
第一步：配置监测对象。将IP地址为202.38.1.10的工作站用作Syslog Server，作为监测对象。
hostname(config)# track abc
hostname(config-trackip)# threshold 3
hostname(config-trackip)# ip 202.38.1.10 interface ethernet0/1 interval 2
第二步：开启流量日志输出到Syslog Server功能，将IP地址为202.38.1.10的工作站用作Syslog
Server，VRouter的名称为trust-vr，类型为UDP，端口号为514，日志信息类型为traffic流量日志信息
（NAT日志部分）。
hostname(config)# logging traffic nat on
hostname(config)# logging syslog 202.38.1.10 vrouter "trust-vr" udp 514 type traffic
nat

<!-- 来源页 2592 -->
hostname(config)# logging traffic nat to syslog
第三步：开启Syslog Server。
第四步：配置流量日志输出到本地文件，文件夹名称为”aa”。
hostname(config)# logging traffic nat to file name usb0 aa
第五步：开启Syslog Server监测功能以及指定最大发送速率为600。
hostname(config)# logging traffic nat to syslog track abc local-backup rate-limit 600

<!-- 来源页 2593 -->
NetFlow
NetFlow是一种数据交换方式，统计记录网络中数据包的源\目的地址、端口号等信息，是网络流量统计和
分析的一种重要手段。
系统的NetFlow功能，支持NetFlow V9，能够根据配置的NetFlow模板规则采集用户的入接口流量信息，
并发送到带有NetFlow数据分析工具的服务器，通过服务器对流量的分析，实现对网络流量的检测、监控以
及流量计费等。
NetFlow配置
系统支持基于接口的NetFlow配置方式。用户需要按照以下步骤进行操作：
1. 开启全局NetFlow功能。
2. 配置NetFlow Profile，在Profile中指定主动超时时间、模板刷新率、配置用于NetFlow数据分析的服务器等。
3. 绑定NetFlow Profile到接口。
开启全局NetFlow功能
开启全局NetFlow功能，在全局配置模式下，使用以下命令：
netflow enable
使用no netflow enable关闭全局NetFlow功能。
注意: 开启或关闭全局NetFlow功能后，需要重启设备使配置生效。
开启NetFlow采样功能
开启NetFlow采样功能后，系统会按照指定间隔对报文进行采样。该功能默认为关闭状态，即对所有报文进
行采样。
开启NetFlow采样功能，在全局配置模式下，使用以下命令：
netflow sampler fix-packets interval-value
l
interval-value - 指定NetFlow的采样间隔。取值范围为1-65535。例如将间隔配置为100，则从配置
生效起，系统会对接收到的第1个、第101个、第201个及后续相同间隔的报文进行采样，并上送采样报
文进行分析。
关闭NetFlow采样功能，在全局配置模式下，使用以下命令：
no netflow sampler

<!-- 来源页 2594 -->
创建NetFlow Profile
NetFlow Profile用于指定主动超时时间、模板刷新率、配置用于NetFlow数据分析的服务器等。创建
NetFlow Profile，在全局配置模式下，使用以下命令：
netflow-profile netflow-profile-name
l
netflow-profile-name - 指定所创建的NetFlowProfile的名称，并且进入该NetFlow Profile的配置
模式。如果指定名称已存在，则直接进入NetFlow Profile配置模式。
使用no netflow-profile netflow-profile-name删除指定的NetFlow Profile。
指定模板刷新率
用户可以根据需要，指定NetFlow模板按照时间或者数据包个数来进行刷新。在NetFlow Profile配置模式
下，使用以下命令：
l
时间：template-refresh-minute refresh-value
refresh-value -指定NetFlow模板按照时间进行刷新，即指定NetFlow模板的刷新周期。范围是1到
3600分钟，默认值是30分钟。
l
数据包：template-refresh-packet packet-value
packet-value - 指定NetFlow模板按照数据包个数进行刷新，即当NetFlow数据包个数达到指定值
packet-value后，该NetFlow模板刷新一次。范围是1到600个，默认值是20个。
指定主动超时时间
主动超时时间，指发送NetFlow流量信息的频率时间。在主动超时时间结束后，设备将发送一次采集的
NetFlow流量信息到指定服务器。在NetFlow Profile配置模式下，使用以下命令：
active-timeout timeout-value
l
timeout-value – 指定主动超时时间。范围是1到60分钟，默认值是5分钟。
在NetFlow Profile配置模式下使用no active-timeout命令恢复主动超时时间的默认值。
配置NetFlow服务器
配置用于NetFlow数据分析的服务器，在NetFlow Profile配置模式下，使用以下命令：
server name [ip ip-address | ipv6 ipv6-address | port port-number]
l
name – 指定服务器名称。范围是1到32个字符。
l
ip ip-address – 指定服务器IPv4地址。

<!-- 来源页 2595 -->
l
ipv6 ipv6-address – 指定服务器IPv6地址。
l
port port-number – 指定服务器端口号。范围是1到65535，默认值是9996。
在NetFlow Profile配置模式下使用no server name命令删除指定名称的服务器。
注意: 系统最多允许配置2个NetFlow服务器。
指定包含企业字段
指定采集的NetFlow流量信息中包含企业字段信息，在NetFlow Profile配置模式下，使用以下命令：
export-enterprise-fields
在NetFlow Profile配置模式下使用no export-enterprise-fields命令取消包含企业字段信息。
指定源接口
指定发送NetFlow流量信息的源接口，在NetFlow Profile配置模式下，使用以下命令：
source interface interface-name {address interface-address | address-ipv6 interfaceaddress-ipv6}
l
interface-name – 指定发送NetFlow流量信息的源接口名称。
l
address interface-address – 指定发送NetFlow流量信息的源接口名称后，系统会按照接口配置自
动获取并显示该源接口的管理IPv4地址或者接口二级IPv4地址。
l
address-ipv6 interface-address-ipv6 – 指定发送NetFlow流量信息的源接口名称后，系统会按照
接口配置自动获取并显示该源接口的IPv6地址。
在NetFlow Profile配置模式下使用no source命令取消源接口的指定。
绑定NetFlow Profile到接口
将NetFlow Profile绑定到接口后，系统将会根据绑定的NetFlow Profile采集用户的入接口流量信息。绑
定NetFlow Profile到接口，在接口配置模式下，使用以下命令：
netflow-profile netflow-profile-name
l
netflow-profile-name – 指定绑定到接口的NetFlow Profile的名称。
在接口配置模式下使用该命令no的形式取消NetFlow Profile的绑定：no netflow-profile
显示NetFlow信息
在任何模式下，输入以下命令显示NetFlow Profile信息：

<!-- 来源页 2596 -->
show netflow-profile [netflow-profile-name]
l
netflow-profile-name –显示指定的NetFlow Profile信息。不配置netflow-profile-name，则显
示所有的NetFlow Profile信息。
例如：
hostname(config)# show netflow-profile 123
netflow-profile "123" (ID 1)( 显示NetFlow Profile的名称)
template refresh minute: 30( 显示NetFlow Profile的刷新时间周期)
template refresh packet: 20( 显示NetFlow数据包到达20个时，刷新一次NetFlow
Profile)
active timeout: 5( 显示主动超时时间)
enterprise fields: disable( 显示NetFlow流量信息中是否包含企业字段信息)
source interface: ethernet0/1( 显示发送NetFlow流量信息的源接口)
source address-ipv4: 20.1.1.2( 显示该源接口的管理IPv4地址或者接口二级IPv4地址)
source address-ipv6: 2020::2( 显示该源接口的IPv6地址)
server[1]: 124( 显示用于NetFlow数据分析的服务器)
ipv4: 10.10.10.2( 显示服务器IPv4地址)
ipv6: 1000::1( 显示服务器IPv6地址)
port: 12( 显示服务器端口)
server[2]:
ipv4: 0.0.0.0
ipv6: ::
port: 0
在任何模式下，输入以下命令显示NetFlow 统计信息：
show netflow [generic] | [slot slot-no]
l
generic –显示NetFlow 统计表项信息。
l
slot slot-no – 指定显示某个特定槽位的NetFlow统计信息。
