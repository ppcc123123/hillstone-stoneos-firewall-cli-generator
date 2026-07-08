# 常用Show命令

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 19 常用的Show命令
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 2629 -->
19 常用的Show命令
查看设备基本信息
命令
简要描述
show version
查看设备版本信息。
show configuration
查看设备配置信息。
show cpu （detail ）
查看设备CPU利用率。
show memory
查看设备内存利用率。
show process [ processname ]
查看进程相关的信息。
show interface interfacename
查看设备的接口信息。
show arp
查看IP-MAC绑定信息。
show arp generic
查看ARP表条目使用情况。
show mac
查看MAC-端口绑定信息。
show mac generic
查看MAC表条目使用情况。
show ip route
查看设备的路由信息。
show session
查看设备的会话信息。
show service
查看所有服务的信息。
show snat / show dnat
查看NAT配置信息。
show snat resource (detail)
查看SNAT的资源利用情况。
show admin host
查看可信主机配置。
show admin user
查看用户登录权限配置。
show clock
查看系统时间配置。
show track
查看监测对象的信息。
show user/ show online
查看用户/在线用户信息。
show this
查看当前对象的配置信息。

<!-- 来源页 2630 -->
查看设备硬件信息
命令
简要描述
show environment
查看设备的温度和风扇盘或风扇转速。
show module
查看扩展模块的信息以及工作状态。
show transceiver
查看光模块的相关信息。
查看设备环境相关信息
当设备的CPU或内存过高或其他性能指标较高时，用户可首先查看设备上与硬件环境相关的信息（如设备的
温度、风扇盘、电源和电压情况），以排查物理环境相关的因素。
注意: 对于部分没有带单独风扇盘的设备，不会显示具体的温度和风扇运行状态，只会简单提示
“normal state”，若状态不正常，设备通常就无法启动了。
通过CLI登录设备后，在任意视图下执行命令show environment，如下所示：
SG-6000(config)# show environment
Temperature information(C):
=====================================================
Description Temperature Range（显示设备测温点的温度信息）
-----------------------------------------------------
CPU 52 0-90
Slot_Inlet 35 0-90
Chassis_Outlet 38 0-90
Switch 52 0-90
Chassis_Inlet 35 0-90
------------------------------------------------------
Fan information:（显示设备的风扇信息）
======================================================
Description Status
------------------------------------------------------
Fan Fine

<!-- 来源页 2631 -->
------------------------------------------------------
Power information:（显示设备的电源信息）
======================================================
Description Status
------------------------------------------------------
PS0 Fine
PS1 Fail/No power
------------------------------------------------------
Voltage information:（显示设备的电压信息）
======================================================
Description Voltage Range
------------------------------------------------------
CPU 1.004 0.970-1.030
DRAM 1.514 1.425-1.575
VDD_1V1 1.096 1.070-1.130
Switch 1.096 1.070-1.130
VDD_2V5 2.513 2.425-2.575
VDD_1V8 1.786 1.745-1.855
显示信息
说明
Temperature
information
显示CPU、扩展槽、Chassis_Outlet的具体温度相关的信息。
Fan information
显示风扇盘相关的信息。
Power information
显示电源模块相关的信息。PS0、PS1标识电源模块1、电源模块2。Fine表示正常、
Fail/No power表示异常或关闭状态。
Voltage
information
显示设备各部分的所使用的具体电压信息。

<!-- 来源页 2632 -->
查看扩展模块相关信息
查看扩展模块的相关信息，包括所在槽位、状态、序列号等。常用于定位扩展模块的故障问题时使用。如下
发命令后，系统未输出扩展模块的槽位信息，说明扩展模块出现异常。
通过CLI登录设备后，在任意视图下执行命令show module，如下所示：
SG-6000(config)# show module
NO. Name State Module Type Serial Number
--- ------------ ------------ ---------------- ----------------
1 slot1 Online IOM-16SFP-80 1705611***000327
2 slot2 Empty
3 slot3 Empty
4 slot4 Empty
5 slot5 Empty
6 slot6 Empty
7 slot7 Empty
8 slot8 Online SSM-80 1705533***0000431
9 slot9 Online SSM-80 1705546***0002033
10 slot10 Empty
11 slot11 Empty
12 slot12 Online SCM-20(M) 13045***0005433
显示信息
说明
NO.
显示序号。
Name
显示扩展槽位名称。
State
显示扩展槽的状态。
Module Type
显示扩展模块的类型。
Serial Number
显示扩展模块的序列号。

<!-- 来源页 2633 -->
查看光模块状态信息
查看光模块状态信息，包括SN序列号、功率、温度、电压以及模块类型。常用于定位光模块的故障问题时使
用。
通过CLI登录设备后，在任意视图下执行命令show transceiver，如下所示：
SG-6000# show transceiver
Transceiver status information is shown as below:
================ xethernet0/6 =====================
SFP+/XFP information: FINISARCORP / FTLF8519P2BNL / 111230
Part Number：FTLF8519P2BNL
Serial Number: PLT4PH9
Transmission media: Multi-mode
Module temperature: 32.38
Module temperature warning range:[-30.00 , 93.00 ]
Tx supply voltage: 3.34 V
Tx supply voltage warning range:[ 2.90 , 3.70 ]
Tx bias current: 5.59 mA
Tx bias current warning range:[2.00 ，14.00 ]
Tx optical power: -5.55 dBm
Tx optical power warning range:[-11.00 ,-2.00 ]
Rx optical power: -6.69 dBm
Rx optical power warning range:[-18.01 , -1.00 ]
Module Wavelength: 850.00 nm
single module max transmit distance: 0 km
OM1 max transmit distance: 150 m
OM2 max transmit distance: 300 m
OM3 max transmit distance: 0 m
copper max transmit distance: 0 m
===============================================================

<!-- 来源页 2634 -->
显示信息
说明
Part Number
显示光模块的PN号。
注意: 仅以下版本支持显示该参数：
l
StoneOS 5.5R10P6及以后的P版本
l
StoneOS 5.5R11F1及以后的F版本
l
StoneOS 5.5R12及以后的R版本
Serial Number
显示光模块的序列码。
Transmission
media
显示光模块的传输模式，单模（Single-mode）或多模（Multi-mode）。
Module
temperature
显示光模块的当前温度。
Module
temperature
warning range
显示光模块温度的范围。
Tx supply voltage
显示光模块的发送电源电压。
Tx supply voltage
warning range
显示光模块的发送电源电压范围。
Tx bias current
显示光模块的发送偏置电流。
Tx bias current
warning range
显示光模块的发送偏置电流范围。
Tx optical power
显示光模块的发送光功率。（40GE模块不支持）
Tx optical power
warning range
显示光模块的发送光功率范围。
Rx optical power
显示光模块的接收光功率。
Rx optical power
warning range
显示光模块的接收光功率范围。
Module
Wavelength
显示光模块的波长。
single module
max transmit
distance
显示单模最大传输距离。
OM1 max transmit
distance
显示OM1光纤最大传输距离。

<!-- 来源页 2635 -->
显示信息
说明
OM2 max transmit
distance
显示OM2光纤最大传输距离。
OM3 max transmit
distance
显示OM3光纤最大传输距离。
copper max
transmit distance
显示铜缆最大传输距离。
注意:
l
由于设备物理硬件差异，部分光接口可能无法通过该命令读取光模块信息。
l
光模块TRAN-QSFP+BiDi不支持使用show transceiver。
查看版本信息
当发生故障时，需要通过show version 命令来查看当前设备的版本信息，用来排查是否版本缺陷造成的故
障问题，同时也便于山石网科技术人员进行问题复现以及故障定位等。
通过CLI登录设备后，在任意模式下，执行命令show version，如下所示：
SG-6000(config)# show version
Hillstone Networks StoneOS software, Version 5.5
Copyright (c) 2009-2021 by Hillstone Networks
Product name: SG-6000-***** S/N: 220664****000328 Assembly number:
A011
Boot file is SG6000-********-v6.bin from flash
Update magic: 0103137200
Built by buildmaster8 2021/01/27 08:54:02
Build PHASE 6
Uptime is 3 days 23 hours 17 minutes 21 seconds
System language is "en"
VRouter feature: enabled
IPS feature: enabled
IPS magic: 7bc631*******1e40aea28ca952fa0422b26

<!-- 来源页 2636 -->
AV feature: enabled
AV magic: 725a9********bb066704467be6a17eafd
URLDB feature: enabled
URLDB magic: fdb28c******ae42a13451b4bb465ae0e27c
APP feature: enabled
APP magic: a15b9*******9f4bb7da17d566017f726f54
SANDBOX feature: enabled
SANDBOX magic: 725a96c04383aef******67be6a17eafd
Botnet Prevention feature: enabled
Botnet Prevention magic: b7a5028816******7e353bc733
geolocation-IP-signature engine version: 3
Database version: PolarDB 2.0
查看版本的详细信息的隐藏命令，在任意模式下，执行命令show version detail，如下所示：
SG-6000(config)# show version detail
Hillstone Networks StoneOS software, Version 5.5
Copyright (c) 2009-2021 by Hillstone Networks
Product name: SG-6000-***** S/N: 2206642120000328 Assembly number:
A011
Boot file is SG6000-********-v6.bin from flash
Update magic: 0103137200
Built by buildmaster8 2021/01/27 08:54:02
Build PHASE 6
OS branch: 'HAWAII_R8_F1', Revision number: '230368'
OS last changed revision number: '230352'
Build ID: 20210127085402
Uptime is 3 days 23 hours 18 minutes 39 seconds
System language is "en"
iQoS feature: enabled
VRouter feature: enabled

<!-- 来源页 2637 -->
IPS feature: enabled
IPS magic: 7bc631653bc0******aea28ca952fa0422b26
AV feature: enabled
AV magic: 725a96c04383*****66704467be6a17eafd
URLDB feature: enabled
URLDB magic: fdb28c0ca28******51b4bb465ae0e27c
APP feature: enabled
APP magic: a15b99ff80539f******d566017f726f54
SANDBOX feature: enabled
SANDBOX magic: 725a96c04383******04467be6a17eafd
Botnet Prevention feature: enabled
Botnet Prevention magic: b7a5028816******7e353bc733
geolocation-IP-signature engine version: 3
Database version: PolarDB 2.0
显示信息
说明
Product name
显示产品名称。
S/N
显示产品序列号。
Boot file
显示启动文件及其版本号。
Update magic
升级文件幻数，用户可不关注。
Uptime
版本升级后运行的时长。
VRouter feature
虚拟路由器的功能开启状态。
IPS feature
显示IPS功能的开启状态。通过命令开启后，需要设备重启后，此处才能变为开启
（enable）状态，未重启前，此处将显示为（disable)关闭状态。
IPS magic
显示IPS特征库文件幻数，用户可不关注。
AV feature
显示AV功能的开启状态。通过命令开启后，需要设备重启后，此处才能变为开启
（enable）状态，未重启前，此处将显示为（disable)关闭状态。
AV magic
显示AV特征库文件幻数，用户可不关注。
URLDB feature
显示URL过滤功能的开启状态。通过命令开启后，需要设备重启后，此处才能变为开启
（enable）状态，未重启前，此处将显示为（disable)关闭状态。
APP feature
显示应用识别等功能的开启状态。通过命令开启后，需要设备重启后，此处才能变为开启

<!-- 来源页 2638 -->
显示信息
说明
（enable）状态，未重启前，此处将显示为（disable)关闭状态。
APP magic
显示APP特征库文件幻数，用户可不关注。
SANDBOX feature
显示云沙箱功能的开启状态。通过命令开启后，需要设备重启后，此处才能变为开启
（enable）状态，未重启前，此处将显示为（disable)关闭状态。
SANDBOX magic
显示云沙箱特征库文件幻数，用户可不关注。
Botnet Prevention
feature
显示僵尸网络防御功能的开启状态。通过命令开启后，需要设备重启后，此处才能变为开启
（enable）状态，未重启前，此处将显示为（disable)关闭状态。
Botnet Prevention
magic
显示僵尸网络防御特征库文件幻数，用户可不关注。
geolocation-IPsignature engine
version
显示IP地理库版本。
Database version
显示数据库版本。仅K系列设备（不含K9180）使用国产数据库PolarDB时，显示该信息。
查看设备配置信息
当设备配置的功能不生效或其他功能异常时，可以首先查看当前的配置信息，来排查是否由于配置缺失或配
置错误造成的。通过CLI登录设备后，查看配置信息时，在任何命令模式下输入以下常用命令:
l show configuration- 用于查看设备的当前配置信息。
l show configuration running- 用于查看设备的当前运行的配置信息记录。
l show configuration interface [ interface-name] - 用于查看设备的当前接口配置信息。
l show configuration address - 用于查看设备的当前地址簿配置信息。
l show configuration policy - 用于查看设备的当前策略配置信息。
l show configuration vrouter - 用于查看设备的当前路由配置信息。
l show configuration ha - 用于查看当前设备的HA配置信息。
通过CLI登录设备后，在任意视图下执行查看命令，如下show configuration示例：
SG-6000(config)# show configuration
Building configuration.
Running configuration:
# PREVIOUS CONFIGERATION START
# END OF PREVIOUS CONFIGERATION

<!-- 来源页 2639 -->
!
Version 5.5R8
ip vrouter "mgt-vr"
exit
ip vrouter "trust-vr"
exit
...
...
...
exit
参数
说明
Version
显示当前的版本号。从此处开始，将显示各功能模块的配置信息。
查看设备CPU/内存/进程信息
查看设备的CPU/内存利用率/进程信息，可以帮助用户排查引起CPU过高的几个因素，如设备流量过大、进
程占用较多或者遭受到网络攻击等，进而有针对性的进行故障定位。
l
show cpu- 用于查看设备CPU整体的平均利用率、当前CPU利用率、前1/5/15分钟的CPU利用率，通过查看故
障发生时或发生前的CPU利用率变化情况，可初步分析出可能的原因，如CPU利用率突然升高，可能是设备短时
遭受Flood攻击等原因。
l show cpu detail -用于查看更大范围的CPU利用率变化情况，包括设备最近1分钟的每秒的CPU利用率，最近1
小时每分钟的CPU利用率，以及最近1天每小时的CPU利用率。
l show memory-用于查看系统内存的使用情况，包括总内存容量、使用量、剩余容量、最近1分钟的每秒的内存
利用率、最近1小时每分钟的内存利用率、以及最近1天/7天每小时的内存利用率。
l show process- 用于查看设备当前运行的任务进程以及各个进程的CPU利用率、内存利用率、进程运行时间等信
息。通常用户可首先查看CPU利用率、内存利用率较高的进程，这些进程可能是造成故障或故障造成，然后有针
对性的对该进程的功能模块的配置等情况进行分析、定位。
通过CLI登录设备后，在任意模式下执行命令show cpu，如下所示：
SG-6000# show cpu

<!-- 来源页 2640 -->
Average cpu utilization : 0.1%（显示设备的平均CPU利用率）
Current cpu utilization : 0.2%（显示设备的当前CPU利用率）
Last 1 minute : 0.2%（显示设备过去1分钟内的CPU利用率）
Last 5 minutes : 0.2%（显示设备过去5分钟内的CPU利用率）
Last 15 minutes : 0.2%（显示设备过去15分钟内的CPU利用率）
通过CLI登录设备后，在任意模式下执行命令show cpu detail，如下所示：
SG-6000# show cpu detail
Average cpu utilization since last boot(%):
All CPU0 CPU1 CPU2 CPU3 CPU4 CPU5 CPU6 CPU7 CPU8 CPU9 CPU10 CPU11
(%) 1.6 5.6 0.9 0.1 6.3 6.3 0.0 0.0 0.0 0.0 0.0 0.0 0.0
Current cpu utilization (%):
All CPU0 CPU1 CPU2 CPU3 CPU4 CPU5 CPU6 CPU7
CPU8 CPU9 CPU10 CPU11
(%) 0.6 2.0 1.0 0.0 2.0 2.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0
Cpu utilization in last 60 seconds(%):
All CPU0 CPU1 CPU2 CPU3 CPU4 CPU5 CPU6 CPU7
CPU8 CPU9 CPU10 CPU11
59 : 0.6 2.0 1.0 0.0 2.0 2.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0
58 : 5.8 22.0 1.0 0.0 23.0 23.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0
.....
Cpu utilization in last 60 minutes(%):
All CPU0 CPU1 CPU2 CPU3 CPU4 CPU5 CPU6 CPU7
CPU8 CPU9 CPU10 CPU11
59 : 1.5 5.3 0.9 0.0 6.0 6.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0

<!-- 来源页 2641 -->
58 : 1.5 5.4 0.9 0.0 6.1 6.1 0.0 0.0 0.0
0.0 0.0 0.0 0.0
..........
Cpu utilization in last 24 hours(%):
All CPU0 CPU1 CPU2 CPU3 CPU4 CPU5 CPU6 CPU7
CPU8 CPU9 CPU10 CPU11
23 : 1.5 5.4 0.9 0.0 6.0 6.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0
22 : 1.5 5.4 0.9 0.0 6.0 6.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0
......
显示信息
说明
Average cpu
utilization
平均CPU利用率。
Current cpu
utilization
当前CPU利用率。
Last 1/5/
15minute
最近1分钟、5分钟、15分钟的CPU利用率。
Cpu utilization in
last 60 seconds
(%):
最近1分钟每秒的CPU利用率。
Cpu utilization in
last 60 minutes
(%):
最近1小时每分钟的CPU利用率。
Cpu utilization in
last 24 hours(%):
最近1天每小时的CPU利用率。
通过CLI登录设备后，在任意模式下执行命令show memory，如下所示：
SG-6000# show memory
The percentage of memory utilization: 31%
total(KB) used(KB) free(KB)
8099840 2550648 5549192

<!-- 来源页 2642 -->
Memory utilization in last 60 seconds(%):
memoryutil
59 : 31.5
58 : 31.5
57 : 31.5
56 : 31.5
.....
Memory utilization in last 60 minutes(%):
memoryutil
59 : 31.3
58 : 31.3
57 : 31.2
56 : 31.2
55 : 31.2
54 : 31.2
..........
Memory utilization in last 24 hours(%):
memoryutil
23 : 31.3
22 : 21.9
21 : 0.0
20 : 0.0
19 : 0.0
......
Memory utilization in last 7 days(%):
memoryutil
167: 31.3
166: 21.9
165: 0.0

<!-- 来源页 2643 -->
164: 0.0
163: 0.0
162: 0.0
......
显示信息
说明
The percentage of
memory utilization
平均内存利用率。
total(KB)
内存总容量
used(KB)
内存已使用容量
free(KB)
内存剩余容量
Memory utilization
in last 60 seconds
(%):
最近1分钟的每秒的内存利用率
Memory utilization
in last 60 minutes
(%):
最近1小时每分钟的内存利用率
Memory utilization
in last 24 hours(%):
最近1天每小时的内存利用率
Memory utilization
in last 7 days(%):
最近7天每小时的内存利用率
通过CLI登录设备后，在任意视图下执行命令show process，如下所示：
SG-6000# show process
Tasks: 86 total, 24 running, 62 sleeping, 0 stopped
Pid Process State Priority Cpu(%) Memory(%) Runtime Fdnum
1677 chassisd R 18 0.4 0.4 19:24.99 13
1713 ipcagent S 0 0.1 0.7 29:45.94 9
1730 cloudagent S 20 0.1 0.6 6:45.99 14
1641 monitord S 0 0.0 0.4 38:22.34 9
1649 monitord S 20 0.0 0.2 1:21.74 8
1678 mgd S 20 0.0 0.8 0:13.95 8

<!-- 来源页 2644 -->
1679 ioagent S 20 0.0 1.0 0:30.44 9
1685 admind S 20 0.0 0.4 0:16.72 7
1687 updated S 20 0.0 1.4 0:36.33 9
1688 cloud S 20 0.0 0.4 0:10.69 11
1689 dnsd S 20 0.0 0.3 4:59.04 9
1690 dnssnpd S 20 0.0 0.3 0:07.80 7
1691 logd S 20 0.0 0.5 3:54.35 37
显示信息
说明
Tasks
显示当前任务进程总体情况。
86 total - 显示总共进程数量。
24 running - 显示正在运行的进程的数量。
62 sleeping - 显示处于休眠状态的进程数量。
0 stopped - 显示被终止的进程的数量。
Pid
显示进程的ID。
Process
显示进程名称。
State
显示进程的状态。
Priority
显示进程的优先级。
Cpu(%)
显示进程占用的CPU百分比。
Memory(%)
显示进程占用的内存百分比。
Runtime
显示进程运行的时间。
Fdnum
显示进程的文件描述符。
查看设备CPU型号和操作系统内核版本
型号说明：
仅云·界国产系列平台支持该功能。
查看设备CPU型号
用户可以在任意模式下，使用以下命令查看设备的CPU型号：
show cputype

<!-- 来源页 2645 -->
例如：
hostname# show cputype
CPU type : HUAWEI,Kunpeng 920 ( 显示设备采用的CPU型号为华为鲲鹏920。)
查看操作系统内核版本信息
用户可以在任意模式下，使用以下命令查看操作系统内核版本信息：
show kernelversion
例如：
hostname# show kernelversion
kernel version : Kylin Kernel Version 4.4.131 ( 显示设备的操作系统为银河麒麟
V10，内核版本号为4.4.131。)
查看接口信息
通过查看接口信息，分析接口的状态、收发包情况、丢包情况，可以帮助用户快速定位故障、锁定问题原
因。常用命令如下：
show interface- 用于查看所有接口信息。
show interface interface-name - 用于查看具体某个接口的信息。当出现转发类故障时，可对故障的
上下行接口信息进行查看并分析。
show statistics interface-counter interface interface-name {second | minute | hour} - 用于查
看接口前60秒钟每5秒/前60分钟每分钟/前24小时每小时的流量统计信息，可用于分析流量转发等的故障分
析。
查看所有接口信息
通过CLI登录设备后，在任意视图下执行show interface命令可以查看所有接口状态信息。如下所示：
SG-6000# show interface
H:physical state;A:admin state;L:link state;P:protocol state;U:up;D:down;K:ha ke ep
up;C:lacp down
N:Not shared;S:Shared;E:Exported to vsys;V:Vsys interface
=======================================================================
Interface name IPv4 address/mask IPv6 address/prefix Zone name Vsys H A L P MAC
address F Description

<!-- 来源页 2646 -->
-----------------------------------------------------------------------
redundant1 0.0.0.0/0 N/A NULL root D U D D 001c.5431.cd72 N ------
redundant1.2 0.0.0.0/0 N/A NULL root D U D D 001c.5431.cd72 N ------
tunnel1 20.1.1.1/24 N/A trust root U U U U 001c.5431.cea6 N ------
vswitchif1 0.0.0.0/0 N/A NULL root D U D D 001c.5431.cd7a N ------
vswitchif2 0.0.0.0/0 N/A NULL root D U D D 001c.5431.cd7b N ------
ethernet0/0 192.168.1.1/24 N/A mgt root U U U U 001c.5431.cd40 N ------
ethernet0/1 0.0.0.0/0 N/A NULL root U U U D 001c.5431.cd41 N ------
ethernet0/2 1.1.1.1/24 N/A trust root D U D D 001c.5431.cd42 N ------
ethernet0/3 10.180.161.105/16 N/A trust root U U U U 001c.5431.cd43 N ------
ethernet0/4 0.0.0.0/0 N/A NULL root D U D D 001c.5431.cd44 N ------
ethernet0/5 0.0.0.0/0 N/A NULL root D U D D 001c.5431.cd45 N ------
ethernet0/6 0.0.0.0/0 N/A NULL root D U D D 001c.5431.cd46 N ------
ethernet0/7 0.0.0.0/0 N/A NULL root D U D D 001c.5431.cd47 N ------
ethernet0/8 0.0.0.0/0 N/A NULL root D U D D 001c.5431.cd48 N ------
ethernet0/9 0.0.0.0/0 N/A NULL root D U D D 001c.5431.cd49 N ------
=======================================================================
说明：因为物理接口是预定义的，所以不管有没有对物理接口进行配置，它们都会被列在接口表里。子接
口、冗余接口、集聚接口和隧道接口只有在进行配置后才会被列出。
显示信息
说明
Interface name
显示接口的名称。
IP address/mask
显示接口的IP地址。
Zone name
显示接口的绑定域的名称。
Vsys
显示接口所属虚拟系统的名称。
H (Physical state)
显示接口的物理状态是否为可用（UP/DOWN）。
A (Admin state)
显示接口的管理状态是否为可用（UP/DOWN）。
L (Link state)
显示接口的链路状态是否为可用（UP/DOWN）。
P (Protocol state)
显示接口的协议状态是否为可用（UP/DOWN）。
MAC address
显示接口的MAC地址。
Description
显示接口的描述信息。

<!-- 来源页 2647 -->
H、A、L和P是接口的四种状态。状态的值为可用（UP）或不可用（DOWN）。
l H（Physical state）：接口的物理状态。如果接口的物理连接是完好的，该接口PHY值就是UP，反之则为
DOWN。
l A（Admin state）：接口的管理状态。用户可以通过no shutdown和shutdown命令来打开和关闭接口。如果
接口被打开，该接口的A值就是UP，反之则为DOWN。
l L（Link state）：接口的链路状态。链路状态的值由H和A的值来决定。只有H和A均为UP时，L的值才为UP。
l P（Protocol state）：接口的协议状态。只有当接口的链路状态为UP并且IP地址已经被分配到该接口，P的值才
会为UP。
查看具体指定接口的信息
通过CLI登录设备后，在任意视图下执行show interface interface-name命令可以具体指定接口的信
息。如下所示：
SG-6000# show interface ethernet0/3
---------------------------------------------------------------------------------
Interface ethernet0/3
Description:
Physical down Admin up
Link down Protocol down
Interface ID:33
IP address:0.0.0.0 0.0.0.0
MAC address:001c.542b.d643
IP MTU:1500
ARP learn:enable
ARP disable-dynamic-entry:disable
ARP timeout:1200
Duplicate address detection alarm enable
Speed mode:1000
Duplex mode:full
link type :auto

<!-- 来源页 2648 -->
media type:fiber
QoS input profile : 1st-level --
2nd-level --
QoS output profile: 1st-level --
2nd-level --
downstream bandwidth is 1000000000
upstream bandwidth is 1000000000
Bind to zone NULL
Belong to vsys root
Auth-arp disable
manage service:NULL
Secondary IP address0: 0.0.0.0 mask:0.0.0.0
Secondary IP address1: 0.0.0.0 mask:0.0.0.0
Secondary IP address2: 0.0.0.0 mask:0.0.0.0
Secondary IP address3: 0.0.0.0 mask:0.0.0.0
Secondary IP address4: 0.0.0.0 mask:0.0.0.0
Secondary IP address5: 0.0.0.0 mask:0.0.0.0
Secondary IP address6: 0.0.0.0 mask:0.0.0.0
Secondary IP address7: 0.0.0.0 mask:0.0.0.0
Secondary IP address8: 0.0.0.0 mask:0.0.0.0
Secondary IP address9: 0.0.0.0 mask:0.0.0.0
===============================================================
显示信息
说明
Physical down Admin up
显示接口的物理（Physical ）状态和管理（Admin）状态。
Link down Protocol down
显示接口的连接（Link）状态和协议（  Protocol ）状态。
Interface ID:33
显示接口的ID号。
IP address
显示接口的IP地址。
MAC address:
显示接口的MAC地址。

<!-- 来源页 2649 -->
显示信息
说明
IP MTU
显示接口的MTU值。
ARP learn
显示接口的ARP学习状态。
ARP disable-dynamic-entry
显示接口的ARP动态学习的关闭状态。enable表示不允许动态学习获取ARP加
入到ARP表，disable反之。
ARP timeout
显示接口的ARP超时时间。
Duplicate address detection
alarm
显示接口的描述信息。
Speed mode
显示接口的速率模式，1000M/100M/10M。
Duplex mode
显示接口的单双工模式。
link type
显示接口的连接类型。
media type
显示接口的媒介类型，电口或光口。
QoS input profile
显示QoS的入方向所用的流控模板。
QoS output profile
显示QoS的出方向所用的流控模板。
downstream bandwidth
显示接口的下行带宽限制。
upstream bandwidth
显示接口的上行带宽限制。
Bind to zone NULL
显示接口所绑定的安全域。
Belong to vsys root
显示接口所属的VSYS。
Auth-arp disable
显示接口认证ARP的开启状态。
manage service:NULL
显示接口的管理方式。
Secondary IP address0:
0.0.0.0 mask:0.0.0.0
显示接口的二级IP和掩码。
查看接口的统计信息
在任何模式下，使用以下命令查看指定接口的流量统计信息：
show statistics interface-counter interfaceinterface-name {second | minute | hour}
l interface-name – 指定接口名称。
l second – 指定显示接口前60秒钟每5秒的流量统计信息。
l minute – 指定显示接口前60分钟每分钟的流量统计信息。
l
hour – 指定显示接口前24小时每小时的流量统计信息。
通过CLI登录设备后，在任意视图下执行show interface interface-name命令可以某个接口的信息。如
下示例：

<!-- 来源页 2650 -->
B9DUT1# show statistics interface-counter interface ethernet0/0 day
ethernet0/0 stats in last 30 days
In Pkts In Bytes Out Pkts Out Bytes
29 : 61796 68767259 42786 2543003
28 : 58089 64135753 36994 2448251
27 : 69653 72866651 50967 3462649
26 : 59048 64459617 42487 2888759
25 : 62476 64837369 44170 2971098
24 : 60654 64724740 44360 4230523
23 : 31470 7816451 20798 6351717
22 : 0 0 0 0
21 : 0 0 0 0
20 : 0 0 0 0
19 : 0 0 0 0
18 : 0 0 0 0
17 : 0 0 0 0
16 : 0 0 0 0
15 : 0 0 0 0
.........
显示信息
说明
In Pkts
显示接口入方向的流量包的个数。
In Bytes
显示接口入方向的流量包的字节数。
Out Pkts
显示接口出方向的流量包的个数。
Out Bytes
显示接口出方向的流量包的字节数。
查看IP-MAC绑定信息
当遇到设备报文转发问题时，可以通过查看IP与MAC地址的绑定信息，同时结合对上下流量的抓包情况，进
行逐步排查。用户可以通过以下命令查看：

<!-- 来源页 2651 -->
l show arp [vroutervrouter-name]- 用于查看系统的IP-MAC绑定信息、类型及老化时间等，示例如下：
SG-6000# show arp
Total entries: 2
Flag: I:Authenticated ARP Driver incompatible; N:Secure Defender not
installed
===============================================================
Protocol Address Age(sec) Hardware Addr Type Flag Interface/VR
---------------------------------------------------------------------
-----------
Internet 10.180.14.99 1053 0050.569a.d980 ARPA ethernet0/3
Internet 10.180.0.1 223 001c.5482.f819 ARPA ethernet0/3
===============================================================
显示信息
说明
Flag
ARP的标志位：
I:Authenticated ARP Driver incompatible; -表示不兼容。
N:Secure Defender not installed- 表示未安装安全防护。
Protocol
显示ARP表的协议类型。
Address
显示IP地址。
Age(sec)
显示ARP表的老化时间。
Hardware Addr
显示IP地址所对应的硬件MAC地址。
Type
显示协议类型。
Flag
显示ARP的标志位。
Interface/VR
显示arp表对应的接口或虚拟路由器的名称。
查看MAC地址与端口绑定关系
当遇到设备报文转发问题时，通常也需要通过查看MAC地址和端口的绑定信息来进一步定位报文转发的走
向，来进一步分析和定位问题。用户可以通过以下命令进行查看：
show mac - 用于查看MAC-端口的绑定信息，包括静态与动态的绑定表。
通过CLI登录设备后，在任意视图下执行命令show mac，如下所示：
SG-6000# show mac

<!-- 来源页 2652 -->
Type: I:invalid; L:self; S:static; D:dynamic
=====================================================================
===========
MAC Address Switch Interface Type Age(sec)
---------------------------------------------------------------------
-----------
001c.5431.cd7b vswitchif2 vswitchif2 L -
001c.5431.cd7a vswitchif1 vswitchif1 L -
=====================================================================
===========
Total 2 MAC entries showed.
显示信息
说明
MAC Address
显示MAC地址。
Switch
显示MAC地址所属的虚拟交换机。
Interface
显示MAC地址所属的虚拟交换机接口。
Type
显示MAC地址类型。
l I:invalid - 表示无效地址。
l L:self - 表示接口自身的MAC地址
l S:static - 表示静态MAC地址。
l D:dynamic - 表示动态MAC地址。
Age(sec)
显示MAC地址的老化时间。
查看路由表/ARP表/MAC表
设备通过路由表信息进行三层转发报文，当三层转发存在故障时，应首先查看路由表进行排查，然后再结合
ARP表和MAC表的信息，进行逐步排查。
l show ip route- 用于查看系统的所有的路由信息。包括静态、ISP、RIP、OSPF、BGP等。
l show arp generic- 用于查看ARP表条目使用情况。
l show mac generic- 用于查看MAC表条目使用情况。包括共有多少MAC表项以及多少MAC表项正在使用中。
通过CLI登录设备后，在任意视图下执行命令show ip route，如下所示：

<!-- 来源页 2653 -->
SG-6000# show ip route
Codes: K - kernel route, C - connected, S - static, Z - ISP, R - RIP, O - OSPF,
B - BGP, D - DHCP, P - PPPoE, W - wireless, H - HOST, G - SCVPN, V - VPN, M - IMPORT,
I - ISIS, Y - SYNC, L - llb outbound, > - selected first nexthop, * - FIB route, b - BFD enable
Routing Table for Virtual Router <trust-vr>
==============================================================================
S>* 0.0.0.0/0 [1/0/1] via 10.160.29.1, ethernet0/0
C>* 10.160.29.0/24 is directly connected, ethernet0/0
H>* 10.160.29.11/32 [0/0/1] is local address, ethernet0/0
C>* 100.1.1.0/24 is directly connected, ethernet1/12
H>* 100.1.1.101/32 [0/0/1] is local address, ethernet1/12
K>* 123.1.1.0/24 is directly connnected, ha-interface
K>* 123.1.1.2/32 is local address, ha-interface
C>* 200.1.1.0/24 is directly connected, ethernet1/10
H>* 200.1.1.101/32 [0/0/1] is local address, ethernet1/10
==============================================================================
Routing Table for Virtual Router <mgt-vr>
==============================================================================
显示信息
说明
S>* 0.0.0.0/0 [1/0/1] via
10.160.29.1, ethernet0/0
S - static表示静态路由，0.0.0.0/0目的网络地址，via 10.160.29.1表示下一
跳的地址，ethernet0/0表示出接口。其他路由信息，可参考此示例。
通过CLI登录设备后，在任意视图下执行命令show arp generic，如下所示：
SG-6000# show arp generic
Total ARP entries: 4096
Free entries: 4095
Dynamic entries: 1
Static entries: 0
Wait entries: 0

<!-- 来源页 2654 -->
Timeout entries: 0
显示信息
说明
Total ARP entries
显示ARP表项的总数
Free entries
显示剩余ARP表项的数量
Dynamic entries
显示动态ARP表项的数量
Static entries
显示静态ARP表项的数量
Wait entries
显示待响应ARP的数量
Timeout entries
显示ARP表项的超时条目数量
通过CLI登录设备后，在任意视图下执行命令show mac generic，如下所示：
SG-6000# show mac generic
Total: 8192
Free: 8187
Static: 1
Dynamic: 4
显示信息
说明
Total
显示MAC地址表项的总数
Free
显示剩余MAC地址表项的数量
Static
显示静态MAC地址表项的数量
Dynamic
显示动态MAC地址表项的数量
清除MAC表项，请在执行模式下使用以下命令：
clear mac [interface interface-name]
查看会话信息
通过查看会话信息，可以判断的TCP、UDP、SSH等协议的连接状态、接收状态是否正常。当新连接无法正
常建立或业务流量无法正常转发时，可首先查看会话是否正常。
通过CLI登录设备后，在任意视图下执行如下命令show session进行查看：
SG-6000# show session
Device: max 3825000, alloc 2, deny session 0, free 3824998, tunnel 0,
alloc failed 0

<!-- 来源页 2655 -->
VSYS id 0: max 3825000, reserve 0, alloc 2, deny session 0, alloc
failed 0
=====================================================================
=
session: id 2, proto 6, flag 0, flag1 20000, flag2 0, flag3 0,
created 630348, life 1800, policy default,app 112(SSH) flag 0x0,
auth_user_id 0, reverse_auth_user_id 0
flow0(33(ethernet0/3)/40200810): 10.88.15.244:52115-
>10.180.161.105:22
flow1(33(ethernet0/3)/818): 10.180.161.105:22->10.88.15.244:52115
session: id 5, proto 2, flag 0, flag1 0, flag2 0, flag3 0, created
631593, life 5, policy default,app 0(Other) flag 0x0, auth_user_id 0,
reverse_auth_user_id 0
flow0(33(ethernet0/3)/890): 10.180.187.24:1->224.0.0.22:1
flow1(33(ethernet0/3)/18): 224.0.0.22:1->10.180.187.24:1
显示信息
说明
Device
显示设备整体的会话情况（多个CPU会显示所有CPU处理的会话情况）。
l max 3825000：显示设备支持的最大会话数。
l alloc 2：显示当前已分配的会话数。
l deny session 0：显示系统拒绝的会话数。
l free 3824998：系统空闲的会话数。
l tunnel 0：显示Tunnel会话总数。
l alloc failed 0：显示分配失败的是会话数。
VSYS
显示VSYS相关的会话数。
l VSYS id 0：显示vsys的ID号。
l reserve 0：显示该vSYS预留的会话数。
session
显示会话的总体信息。
l session: id 2：显示会话的ID。
l proto 6:显示该会话对应的协议号。

<!-- 来源页 2656 -->
显示信息
说明
l flag 0, flag1 20000, flag2 0, flag3 0:显示会话的标志位。
l created 630348：显示会话的创建时间的标识。
l life 1800:显示会话的生存时间。
l policy default:显示会话匹配上的策略。
l app 112(SSH) flag 0x0：显示该会话所对应的应用、应用ID（应用名称）、标志
位。
l auth_user_id 0, reverse_auth_user_id 0显示该会话所对应的认证用户ID和反向
认证用户ID。
flow
显示会话流的具体信息。
flow0(33(ethernet0/3)/40200810):显示会话流的id（端口id （端口号）/标志位）
信息。
10.88.15.244:52115->10.180.161.105:22:显示会话流的源IP：源端口—>目的IP：
目的端口。
查看所有服务的信息
服务簿可以被引用在安全策略、NAT、策略路由等功能模块中，当遇到这些模块功能异常时，可以进行排查
具体服务簿中的端口是否配置错误。用户可以通过以下命令查看：
l show service- 查看到所有服务的信息，包括所有预定义服务和用户自定义服务的名称、协议、目的端口、源端
口、超时时间信息以及未被系统其它功能模块引用的服务信息。示例如下：
SG-6000# show service
Name Protocol Dst-Port/Type Src-Port/Code Timeout
Total configured: 111
Any Any - - -
AFS TCP 7002-7009 Any -
UDP 7002-7009 Any -
AIM TCP 5190-5194 Any -
BFD UDP 3784-3785 Any -
UDP 4784 Any -
BGP TCP 179 Any -

<!-- 来源页 2657 -->
CHARGEN UDP 19 Any -
COPA-WEBSERVER TCP 1102 Any -
DayTime TCP 13 Any -
UDP 13 Any -
DHCP-Relay UDP 67-68 Any -
DHCPCv6 TCP 546 Any -
UDP 546 Any -
DHCPSv6 TCP 547 Any -
UDP 547 Any -
DISCARD UDP 9 Any -
DNS UDP 53 Any -
TCP 53 Any -
DoT TCP 853 Any -
ECHO UDP 7 Any -
显示信息
说明
Name
显示服务名称。
Protocol
显示服务协议类型。
Dst-Port/Type
显示服务目的端口号或者ICMP类型字段。
Src-Port/Code
显示服务源端口号或者ICMP代码字段。
Timeout
显示服务的超时时间。
查看NAT配置信息
当设备NAT转发出现问题时，可通过查看NAT配置是否正常进行排查。用户可以通过以下命令查看：
l show snat- 用于查看系统中SNAT的配置信息。
l show dnat- 用于查看系统中DNAT的配置信息。
通过CLI登录设备后，在任意视图下执行命令show snat，如下所示：
SG-6000# show snat
--------------------------------------------------------------------------------

<!-- 来源页 2658 -->
vr name:trust-vr
snat rules total number is :1
==============================================================================
==
id ingress if from to service egress if/vr translate to mode start end size
--------------------------------------------------------------------------------
1 1.1.1.1/32 2.2.2.2/32 Any egress if's IP Dyn-Pt
==============================================================================
==
Routing Table for Virtual Router <mgt-vr>
==============================================================================
==
显示信息
说明
id
显示SNAT规则的ID号。
ingress if
显示SNAT规则流量的入接口。
from
显示SNAT规则流量的源IP地址。
to
显示SNAT规则流量的目的地址。
service
显示SNAT配置的服务信息。
egress if/vr
显示SNAT规则流量的出接口或者流量的下一跳VRouter。
translate to
显示SNAT配置的转换后IP地址信息。
mode
显示SNAT配置的转换模式。
start end
显示起始和终止的端口号。NAT444 规则中使用。用户可不关注。
size
NAT444 规则中使用。用户可不关注。
通过CLI登录设备后，在任意视图下执行命令show dnat，如下所示：
SG-6000# show dnat
----------------------------------------------------------------
vr name:trust-vr
dnat rules total number is :1
================================================================
id ingress interface from to service translate to port slb

<!-- 来源页 2659 -->
-----------------------------------------------------------------
1 Any 192.168.10.1/32 Any 192.168.20.2/32
track ping enabled
=================================================================
显示信息
说明
id
显示DNAT规则的ID号。
ingress interface
显示DNAT规则流量的入接口。
from
显示DNAT规则流量的源IP地址。
to
显示DNAT规则流量的目的地址。
service
显示DNAT配置的服务信息。
translate to
显示DNAT配置的转换后IP地址信息。
port
显示DNAT配置的内网服务器端口号。
slb
显示DNAT规则是否启用负载均衡功能。
track ping
显示DNAT规则是否启用Ping跟踪功能。
查看SNAT的资源利用情况
当设备出现访问网络卡顿、丢包问题时，需要查看SNAT的资源利用情况，进一步排查源端口地址池中资源
的利用情况，判断NAT地址中IP资源或TCP/UDP端口资源是否已耗尽。用户可以通过以下命令查看：
l show snat resource- 当SNAT的转换模式为dynamicport时，该参数用来指定显示转换地址池端口资源的利用
情况。示例如下：
SG-6000# show snat resource
snat rule id:3
resource usage:
TCP ports:0% (9 of 64512 current available: 64503)
UDP ports:0% (6 of 64512 current available: 64506)
ICMP ports:0% (0 of 64512 current available:64512)
snat rule id:2
resource usage: N/A
snat rule id:4

<!-- 来源页 2660 -->
resource usage: N/A
snat rule id:1
resource usage: N/A
snat rule id:5
resource usage: N/A
-------------------------------------------------------------
显示信息
说明
TCP ports：
显示TCP协议端口占用的情况。
UDP ports:
显示UDP协议端口占用的情况。
ICMP ports:
显示ICMP协议端口占用的情况。
查看可信主机/用户登录权限
当出现设备无法登录的问题，如某些IP地址/登录方式（Telnet、HTTP等）无法登录设备、某些用户账号无
法登录设备。查看可信主机/用户登录权限，进而有针对性的进行故障定位。
l show admin host- 用于查看可信主机配置。如果用户IP或MAC在可信主机内，再确认可信主机是否开启了对应
的管理方式（Telnet、HTTP、HTTPS等）。
l show admin user-用于查看登录用户的登录类型配置，确认是否开启了对应的登录方式（Telnet、HTTP、
HTTPS等）。
通过CLI登录设备后，在任意视图下执行命令show admin host，如下所示：
SG-6000# show admin host
========================================================================
Addr Addr Type Login type
------------------------------------------------------------------------
0.0.0.0/0 IPv4 Telnet SSH HTTP HTTPS NETCONF
::/0 IPv6 SSH HTTP HTTPS
========================================================================
通过CLI登录设备后，在任意视图下执行命令show admin user，如下所示：
SG-6000# show admin user

<!-- 来源页 2661 -->
========================================================================
Username Role authentication server Console Telnet SSH HTTP HTTPS NETCONF
------------------------------------------------------------------------
admin admin local Y - Y - Y -
auditor auditor local Y - Y - Y -
hillstone admin local Y Y Y Y Y -
jnlin_au auditor local Y Y Y Y Y -
jnlin_op operator local Y Y Y Y Y -
operator operator local Y - Y - Y -
ping admin local Y Y Y Y Y -
zhwu admin local Y Y Y Y Y -
zhwu_ad admin local Y Y Y Y Y -
zhwu_ad_1 admin local Y Y Y Y Y -
zhwu_au auditor local Y Y Y Y Y -
zhwu_au_1 auditor local Y Y Y Y Y -
zhwu_op operator local Y Y Y Y Y -
========================================================================
查看系统时间配置
当排查设备日志时，发现系统时间和实际时间不一致时，可进一步查看防火墙系统时间。用户可以通过以下
命令查看：
l show clock- 用于查看当前的时区配置信息。示例如下：
SG-6000# show snat resource
snat rule id:3
resource usage:
TCP ports:0% (9 of 64512 current available: 64503)
UDP ports:0% (6 of 64512 current available: 64506)
ICMP ports:0% (0 of 64512 current available:64512)

<!-- 来源页 2662 -->
snat rule id:2
resource usage: N/A
snat rule id:4
resource usage: N/A
snat rule id:1
resource usage: N/A
snat rule id:5
resource usage: N/A
-------------------------------------------------------------
查看用户/用户组/在线用户信息
在任何模式下，使用以下命令查看用户或用户组的信息。
l
查看系统中所有用户的信息：
show user
l
查看系统中的用户信息：
show user aaa-serverserver-name [nameuser-name]
l
查看静态绑定用户的信息：
show user-binding aaa-serverserver-name
l
查看系统中的用户组信息：
show user-group aaa-serverserver-name
l
查看当前在线的用户信息，包括用户名称、登录方式、登录时间等信息：
show online
以下是返回结果示例：
hostname#show online
=================================================================
USER VSYS VIA IDLE TIME HOST
-----------------------------------------------------------------
hillstone root Console 00:51 Dec 21 15:28 localhost

<!-- 来源页 2663 -->
hillstone root SSH . Dec 26 13:45 10.88.15.43
hillstone root HTTP . Dec 26 13:45 10.88.15.43
=================================================================
查看监测对象的信息
查看系统中指定监测对象的配置信息。在任意模式下，使用以下命令：
show track track-object-name
l
track-object-name – 指定监测对象名称。范围是1到31个字符。
查看系统中所有监测对象的配置信息，包含监测对象的总数以及每个监测对象的详细配置。在任意模式下，
使用以下命令：
show track
以下是一个返回结果示例：
例如当监测接口的链路状态时，可以显示被监测接口的名称、该条监测失败对整个监测对象失败贡献的权重
值、接口的链路状态。
hostname# show track
==============================================================================
============================
Total track number: 3（系统中监测对象的总数）
Track name: test（监测对象名称）
------------------------------------------------------------------------------------------------
-----------------------------------------------------------------
used type: not used（监测对象未被使用）; status: UNKNOWN; link status: UNKNOWN;
track ID: 1; local: no; hold: no; threshold: 255; delay threshold: 255; bandwidth
threshold: 255; if ID: 0; snat cnt: 0; dynamic-ping-msg-id: disable（Ping报文动态ID功能未
开启）; hold notify: disable（监测对象异常时，不通知使用该监测对象的模块）
track interface:（监测接口的链路状态）
------------------------------------------------------------------------------------------------
-----------------------------------------------------------------
Track interface weight status（被监测接口的名称该条监测失败对整个监测对象失败贡献的权重值接

<!-- 来源页 2664 -->
口的链路状态）
------------------------------------------------------------------------------------------------
-----------------------------------------------------------------
ethernet0/1 255 unknown
- - More - -
查看当前对象的配置信息
当用户在某一配置模式下完成指定对象的配置之后，用户可以当前配置模式下，使用show this命令查看当
前对象的配置信息。
下表列出了目前系统支持查看当前配置信息的对象名称和配置模式：
对象名称
配置模式
配置模式提示符
管理员
管理员配置模式
hostname(config-admin)#
管理员密码策略
管理员密码策略配置模式
hostname(config-pwd-policy)#
AAA服务器
AAA服务配置模式
hostname(config-aaa-server)#
接口
接口配置模式
hostname(config-if-eth0/0)#
安全域
安全域配置模式
hostname(config-zone-trust)#
地址簿
地址配置模式
hostname(config-addr)#
服务
服务配置模式
hostname(config-service)#
服务组
服务组配置模式
hostname(config-svc-group)#
策略路由
PBR策略配置模式
hostname(config-pbr)#
VRouter
VRouter配置模式
hostname(config-vrouter)#
为trust-vr配置
NAT
NAT配置模式
hostname(config-nat)#
流量管理
第一层/第二层流控模式
hostname(config-qos-engine)#
安全策略
策略规则配置模式
hostname(config-policy-rule)
域名簿
域名配置模式
hostname(config-host)#
应用簿
应用配置模式
hostname(config-application)#
DNS代理
DNS代理规则配置模式
hostname(config-dns-proxy-rule)#
SSL代理
SSL代理Profile配置模式
hostname(config-sslproxyprofile)#
VSYS
非根VSYS配置模式
hostname(config-vsys)#
VSYS Profile配置模式
hostname(config-vsys-profile)#

<!-- 来源页 2665 -->
查看在线用户信息
系统支持查看当前在线的用户信息，包括用户名称、登录方式、登录时间等信息。
查看在线用户信息，在任意模式下，使用以下命令：
show online
以下是返回结果示例：
hostname#show online
===============================================================
==
USER VSYS VIA IDLE TIME HOST
-----------------------------------------------------------------
hillstone root Console 00:51 Dec 21 15:28 localhost
hillstone root SSH . Dec 26 13:45 10.88.15.43
hillstone root HTTP . Dec 26 13:45 10.88.15.43
===============================================================
==
查看硬件快转的配置信息/状态
型号说明：
l
支持：SG-6000-A7600、A6800以及A系列ASIC防火墙。
l
支持：SG-6000-K20803、K7680、K7280、K6680以及K系列ASIC防火墙。
查看硬件快转配置信息
查看当前设备硬件快转功能的配置信息，包括硬件快转功能的启用状态、硬件快转流表的快速老化功能的启
用状态、TCP短连接不进行硬件快转功能的启用状态。
查看硬件快转功能的配置信息，在任意模式下，使用以下命令：
show hardware fast-forward configuration
以下是返回结果示例：

<!-- 来源页 2666 -->
hostname#show hardware fast-forward configuration
==================================================
Hardware Fast-forward Information
==================================================
Hardware Fast-forward: enable( 显示硬件快转功能的启用状态)
Hardware short tcp performance optimization: disable
Hardware session Fast-aging: enable
==================================================
查看硬件快转的状态
查看硬件快转的状态，包括快转的会话数、设备整机当前的会话数、快转的流量速率、设备整机转发的流量
速率、每秒快转的数据包数量、设备整机每秒转发的数据包数量以及相应的比值。
查看硬件快转的状态，在任意模式下，使用以下命令：
show hardware fast-forward state
以下是返回结果示例：
项目
说明
Fast session
number
快转的会话数。
session number
设备整机当前的会话数。
Fast traffic
快转的流量速率。
Traffic
设备整机转发的流量速率。
Fast PPS
每秒快转的数据包数量。
PPS
设备整机每秒转发的数据包数量。

<!-- 来源页 2667 -->
项目
说明
提示: PPS即Packet Per Second（包/ 秒），表示以数据包为单位的传
输速率。一般用于评估系统对网络的转发能力。
ratio
比值。例如，“每秒快转的数据包数量”占“设备整机每秒转发的数据包数量”的百分比。
查看/清除整机吞吐与WAN安全域接口速率历史峰值
查看整机吞吐与WAN安全域接口速率历史峰值
用户可以查看以下两类历史峰值数据，从而掌握设备性能及WAN链路带宽占用情况，快速定位性能瓶颈来
源，并据此有针对性地开展优化与处置工作。
l
整机吞吐历史峰值：反映设备整机的最大数据转发能力。当峰值接近设备规格上限，则表明设备可能存
在性能瓶颈。
l
WAN安全域接口上下行速率历史峰值：统计所有已配置WAN安全域的接口上下行速率峰值，可直观反映
WAN链路的带宽占用情况。
系统支持显示当前小时、上一小时、当天、上一天、当周、上周以及设备开机以来的最大吞吐值和对应的时
间点。
l
当前小时：从当前小时的开始时间到当前时间点。例如：当前时间为14:20:20，则当前小时是指从
14:00:00到14:20:20。
l
上一小时：从上一小时的开始时间到结束时间。例如：当前时间为14:20:20，则上一小时是指从
13:00:00到13:59:59。
l
当天：从当天的00:00:00到当前时间点。
l
上一天：从上一天的00:00:00到上一天的23:59:59。
l
当周：从本周一的00:00:00到当前时间点。
l
上周：从上周一的00:00:00到上周日的23:59:59。
l
开机以来：从设备开机的时间点开始到当前时间点。
查看设备整机吞吐历史峰值，在任意模式下，使用以下命令：
show statistics max-history throughput
查看所有已配置WAN安全域的接口上下行速率峰值，在任意模式下，使用以下命令：
show statistics max-history throughput WAN

<!-- 来源页 2668 -->
以下是一个返回结果示例：
hostname# show statistics max-history throughput
Max Throughput
Current Hour: 14.01 Mbps (at 2025-05-06 09:14:00)
Previous Hour: 37.48 Kbps (at 2025-05-06 08:59:48)
Current Day: 14.01 Mbps (at 2025-05-06 09:14:00)
Previous Day: 177.79 Kbps (at 2025-05-05 12:36:08)
Current Week: 14.01 Mbps (at 2025-05-06 09:14:00)
Previous Week: 11.44 Mbps (at 2025-04-30 15:30:22)
Since Last Boot: 14.01 Mbps (at 2025-05-06 09:14:00)
hostname# show statistics max-history throughput wan
Max History Throughput of WAN zone:
Current Hour : Up : 1.99 Gbps (at 2026-03-26 13:48:55) 
                        Down : 1.99 Gbps (at 2026-03-26 13:48:55)
                        Total: 3.98 Gbps (at 2026-03-26 13:48:55)
Previous Hour : Up : 0 bps (at 2026-03-26 12:59:59) 
                          Down : 0 bps (at 2026-03-26 12:59:59)
                          Total: 0 bps (at 2026-03-26 12:59:59)
Current Day : Up : 2.00 Gbps (at 2026-03-26 01:20:59)
                       Down : 2.00 Gbps (at 2026-03-26 01:20:59)
                       Total: 4.00 Gbps (at 2026-03-26 01:20:59)
Previous Day : Up : 2.00 Gbps (at 2026-03-25 22:11:59)
                         Down : 2.00 Gbps (at 2026-03-25 22:11:59)
                         Total: 4.00 Gbps (at 2026-03-25 22:11:59)
Current Week : Up : 2.00 Gbps (at 2026-03-25 22:11:59)
                         Down : 2.00 Gbps (at 2026-03-25 22:11:59)
                         Total: 4.00 Gbps (at 2026-03-25 22:11:59)
Previous Week : Up : No data available
                           Down : No data available
                           Total: No data available
Since Last Boot: Up : 2.00 Gbps (at 2026-03-25 22:11:59) 
                           Down : 2.00 Gbps (at 2026-03-25 22:11:59) 
                           Total: 4.00 Gbps (at 2026-03-25 22:11:59)
清除整机吞吐与WAN安全域接口速率历史峰值
当设备系统时间发生修改时，已统计的整机吞吐及所有已配置WAN安全域的接口上下行速率历史峰值数据将
失效。此时用户需先清除历史统计数据，使系统基于设备当前时间重新启动统计。
清除整机吞吐与WAN安全域接口速率历史峰值，在任意模式下，使用以下命令：
clear statistics max-history throughput

<!-- 来源页 2669 -->
查看/清除设备的历史CPU使用率峰值
查看设备的历史CPU使用率峰值
用户可以查看设备的历史CPU使用率峰值，以此来判断设备是否达到性能瓶颈。系统支持显示当前小时、上
一小时、当天、上一天、当周、上周以及设备开机以来的最大CPU使用率和对应的时间点。
l
当前小时：从当前小时的开始时间到当前时间点。例如：当前时间为14:20:20，则当前小时是指从
14:00:00到14:20:20。
l
上一小时：从上一小时的开始时间到结束时间。例如：当前时间为14:20:20，则上一小时是指从
13:00:00到13:59:59。
l
当天：从当天的00:00:00到当前时间点。
l
上一天：从上一天的00:00:00到上一天的23:59:59。
l
当周：从本周一的00:00:00到当前时间点。
l
上周：从上周一的00:00:00到上周日的23:59:59。
l
开机以来：从设备开机的时间点开始到当前时间点。
查看设备的历史CPU使用率峰值，在任意模式下，使用以下命令：
show statistics max-history cpu [cpux/y]
l
cpux/y - X系列设备、K9180、K6580可以查看指定子卡的历史CPU使用率峰值。
以下是一个返回结果示例：
hostname# show statistics max-history cpu
Max CP Cpuutil （管理平面CP的CPU利用率峰值）
Current Hour: 3.02% (at 2025-04-24 20:03:29)
Previous Hour: 3.00% (at 2025-04-24 19:31:39)
Current Day: 3.02% (at 2025-04-24 20:03:29)
Previous Day: No data available
Current Week: 3.02% (at 2025-04-24 20:03:29)
Previous Week: No data available
Since Last Boot: 3.02% (at 2025-04-24 20:03:29)
Max DP Cpuutil （数据平面DP的CPU利用率峰值）
Current Hour: 3.02% (at 2025-04-24 20:03:29)
Previous Hour: 3.00% (at 2025-04-24 19:31:39)
Current Day: 3.02% (at 2025-04-24 20:03:29)
Previous Day: No data available
Current Week: 3.02% (at 2025-04-24 20:03:29)

<!-- 来源页 2670 -->
Previous Week: No data available
Since Last Boot: 3.02% (at 2025-04-24 20:03:29)
清除设备的历史CPU使用率峰值
清除设备的历史CPU使用率峰值，在任意模式下，使用以下命令：
clear statistics max-history cpu
注意: 修改设备的时区或时间后，需要清除历史CPU使用率峰值数据，确保之后记录的CPU使用率
峰值信息准确。
