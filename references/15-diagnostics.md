# 分析诊断

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 18 分析诊断
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 2597 -->
18 分析诊断
仅有部分平台支持该功能，请以实际页面为准。
系统支持以下分析诊断方式：
l "数据包路径检测" 在第2596页：依据系统对数据包的处理流程，对数据包进行检测，并通过图形化以及文字描
述的方式将检测过程及检测结果呈现给用户。
l "在线抓包工具" 在第2607页：实时抓取系统中的数据包，并能够将抓取到的数据包导出到本地硬盘，然后通过
第三方抓包工具查看数据包内容。
l "测试工具" 在第2619页：设备支持域名检查，支持使用网络连接测试工具Ping和Traceroute。当网络出现问题
时，用户可以用这些工具对网络进行测试，查找故障原因。
l "丢包统计" 在第2622页：支持对功能模块的丢包情况进行统计，帮助用户通过统计数据定位问题。
l 系统调试：系统调试功能可以帮助用户对错误进行诊断和定位。
l 修改dumpfile收集的检查周期：根据用户实际需求，合理调整dumpfile收集的检查周期，确保dumpfile能够准
确记录“持续异常” 的状态，为后续故障排查和系统优化提供精准的信息支持。（仅支持CLI方式配置）

<!-- 来源页 2598 -->
数据包路径检测
数据包路径检测功能依据系统对数据包的处理流程，对数据包进行检测，并通过图形化以及文字描述的方式
将检测过程及检测结果呈现给用户。可检测的数据包来源有模拟数据包、实时在线数据包以及已有数据包
（系统提供在线抓包功能方便用户获得数据包）。
不同来源的可检测数据包对应不同的检测方式，系统支持以下三种数据包检测方式：
l 模拟检测：模拟一个数据包并对该数据包在系统中的处理流程进行检测。
l 在线检测：实时检测系统中数据包的处理流程。能够同时对多个数据包进行检测。
l 导入检测：导入已有数据包并对该数据包在系统中的处理流程进行检测。能够同时对多个数据包进行检测。
配置数据包路径检测
用户可以进行以下数据包路径检测配置：
l "模拟检测" 在第2596页
l "在线检测" 在第2598页
l "导入检测" 在第2601页
模拟检测
开始之前
l 阅读"数据包路径检测" 在第2596页介绍。
进行模拟检测，请按照以下流程进行配置：
1. 配置模拟检测源
2. 开始模拟数据包路径检测
3. 导出模拟检测报文
4. （可选）停止模拟数据包路径检测
配置模拟检测源
配置模拟检测源的相关信息，包括源IP地址、目的IP地址、源端口、目的端口等。

<!-- 来源页 2599 -->
注意:
l
系统最多允许配置20个模拟检测源。
l
检测源的源IP地址类型和目的IP地址类型需要保持一致。
在全局配置模式下，使用以下命令，配置模拟检测源：
troubleshooting packet-trace emulation-template name type {tcp | udp} {src-ip ip-address |
src-ipv6 ipv6-address} src-port port-num {dst-ip ip-address | dst-ipv6 ipv6-address} dstport port-num ingress-interface interface-name [descriptiondescription]
troubleshooting packet-trace emulation-templatename type {icmp src-ip ip-address dst-ip
ip-address | icmpv6 src-ipv6 ipv6-address dst-ipv6 ipv6-address} type type-value code
code-value ingress-interface interface-name [descriptiondescription]
l
emulation-template name - 指定模拟检测源名称。
l
type {tcp | udp} / type {icmp | icmpv6} - 指定模拟检测源的协议类型，可以为TCP、UDP、ICMP或
者ICMPv6。
l
src-ip ip-address - 指定模拟检测源的源IPv4地址。
l
src-ipv6 ipv6-address - 指定模拟检测源的源IPv6地址。
l
dst-ip ip-address - 指定模拟检测源的目的IPv4地址。
l
dst-ipv6 ipv6-address - 指定模拟检测源的目的IPv6地址。
l
src-port port-num - 当模拟检测源的协议类型为TCP或者UDP时，指定源端口号。
l
dst-port port-num - 当模拟检测源的协议类型为TCP或者UDP时，指定目的端口号。
l
type type-value code code-value - 当模拟检测源的协议类型为ICMP或者ICMPv6时，指定
ICMP/ICMPv6 Type值和Code值。
l
ingress-interface interface-name - 指定模拟检测源的入接口。
l
description description - 该模拟检测源的描述信息。
在全局配置模式下，使用以下命令，删除指定的模拟检测源：
no troubleshooting packet-trace emulation-template name
［命令实例］
hostname(config)# troubleshooting packet-trace emulation-template temp1 type
udp src-ip 10.0.0.1 src-port 10 dst-ip 192.168.0.1 dst-port 100 ingress-interface
ethernet0/0

<!-- 来源页 2600 -->
开始模拟数据包路径检测
在任何模式下，使用以下命令，开始模拟数据包路径检测：
exec troubleshooting packet-trace emulation-template name start
l
emulation-template name - 指定模拟检测源名称。
［命令实例］
hostname# exec troubleshooting packet-trace emulation-template test start
停止模拟数据包路径检测
在任何模式下，使用以下命令，停止模拟数据包路径检测：
exec troubleshooting packet-trace stop
导出模拟检测报文
在执行模式下，使用以下命令，导出模拟检测报文：
export troubleshooting packet-trace emulation-template name to {{ftp | ftps | sftp} server
ip-address [user user-name password password] | tftp server ip-address} [vrouter vr-name]
[file-name]
l
{ftp | ftps | sftp} server ip-address [user user-name password password] - 指定将模拟检测
报文导出到FTP/FTPS/SFTP服务器。需要配置的参数为：
l
ip-address - 指定FTP/FTPS/SFTP服务器的IP地址。
l
user user-name password password – 指定访问FTP/FTPS/SFTP服务器使用的用户名和密
码。当不输入用户名和密码时表示采用匿名登录方式。
l
tftp server ip-address -指定将模拟检测报文导出到TFTP服务器。指定TFTP服务器的IP地址。
l
vrouter vr-name - 指定服务器所属的VR。系统默认为trust-vr。
l
file-name - 指定导出的模拟检测报文文件的名称。
［命令实例］
hostname# export troubleshooting packet-trace emulation-template temp1 to tftp
server 10.1.1.1
在线检测
开始之前

<!-- 来源页 2601 -->
l 阅读"数据包路径检测" 在第2596页介绍。
进行在线检测，请按照以下流程进行配置：
1. 配置在线检测源
2. 开始在线数据包路径检测
3. 导出在线检测报文
4. （可选）停止在线数据包路径检测
配置在线检测源
配置在线检测源的相关信息，包括源IP地址、目的IP地址、源端口、目的端口等。
注意:
l
系统最多允许配置5个在线检测源。
l
检测源的源IP地址类型和目的IP地址类型需要保持一致。
在全局配置模式下，使用以下命令，配置在线检测源：
troubleshooting packet-trace filter name type live-traffic {[[src-ip ip-address] | [src-ipv6
ipv6-address] | [user aaa-server user-name] | [user-group aaa-server user-name]] [src-port
port-num] [[dst-ip ip-address] | [dst-ipv6 ipv6-address] | [url url]] [dst-port port-num] [proto
{tcp | udp | icmp | icmpv6 | proto-num}] [application app-name] [ingress-interface interfacename]} [description description]
l
filter name - 指定在线检测源名称。
l
[src-ip ip-address] | [src-ipv6 ipv6-address] - 指定在线检测源的源IPv4地址或源IPv6地址。
l
user aaa-server user-name - 指定在线检测源的源用户，并指定用户所属的AAA服务器。
l
user-group aaa-server user-name - 指定在线检测源的源用户组，并指定用户组所属的AAA服务
器。
l
src-port port-num - 指定在线检测源的源端口号。
l
[dst-ip ip-address] | [dst-ipv6 ipv6-address] - 指定在线检测源的目的IPv4地址或目的IPv6地
址。
l
url url - 指定在线检测源的目的URL地址。
l
dst-port port-num - 指定在线检测源的目的端口号。

<!-- 来源页 2602 -->
l
proto {tcp | udp | icmp | icmpv6 | proto-num} - 指定在线检测源的协议类型或者协议号。当指定
ICMP或ICMPv6协议时，若检测源的源/目的IP地址为IPv4，建议指定ICMP协议；若为IPv6，则指定
ICMPv6协议。
l
application app-name - 指定在线检测源的应用类型。
l
ingress-interface interface-name - 指定在线检测源的入接口。
l
description description - 该在线检测源的描述信息。
在全局配置模式下，使用以下命令，删除指定的在线检测源：
no troubleshooting packet-trace filter name
［命令实例］
hostname(config)# troubleshooting packet-trace filter test type live-traffic dst-ip
10.1.1.1 application http ingress-interface ethernet0/0
开始在线数据包路径检测
在任何模式下，使用以下命令，开始在线数据包路径检测：
exec troubleshooting packet-trace filter name [packet-capture] start [time-out value]
l
filter name - 指定在线检测源名称。
l
packet-capture - 开启在线抓包功能。
l
time-out value - 指定检测的时间长度，默认为30分钟，范围为1到1440分钟。达到指定时间时，系
统会自动停止检测。
［命令实例］
hostname# exec troubleshooting packet-trace filter 123 start time-out 60
停止在线数据包路径检测
在任何模式下，使用以下命令，停止在线数据包路径检测：
exec troubleshooting packet-trace stop
导出在线检测报文
在执行模式下，使用以下命令，导出在线数据包路径检测时抓取的数据包文件：
export troubleshooting packet-trace packet-capture-file to {{ftp | ftps | sftp} server ipaddress [user user-name password password] | tftp server ip-address} [vroutervr-name]
[file-name]

<!-- 来源页 2603 -->
l
{ftp | ftps | sftp} server ip-address [user user-name password password] - 指定将数据包文
件导出到FTP/FTPS/SFTP服务器。需要配置的参数为：
l
ip-address - 指定FTP/FTPS/SFTP服务器的IP地址
l
useruser-namepasswordpassword - 指定访问FTP/FTPS/SFTP服务器使用的用户名和密
码。当不输入用户名和密码时表示采用匿名登录方式。
l
tftp server ip-address - 指定将数据包文件导出到TFTP服务器。指定TFTP服务器的IP地址。
l
vrouter vr-name - 指定服务器所属的VR。系统默认为trust-vr。
l
file-name - 指定导出的数据包文件的名称。若不指定，默认导出的数据包文件名称为ts_
pktdump.pcap（X系列及K9180设备导出的数据包文件名称为ts_pktdump.tar.gz）。
［命令实例］
hostname# export troubleshooting packet-trace packet-capture-file to tftp server
10.1.1.1
导入检测
开始之前
l 阅读"数据包路径检测" 在第2596页介绍。
进行导入检测，请按照以下流程进行配置：
1. 导入数据包
2. 配置导入检测源
3. 开始导入数据包路径检测
4. （可选）停止导入数据包路径检测
导入数据包
为导入数据包路径检测导入数据包，在执行模式下，使用以下命令：
import troubleshooting packet-trace replay-file from {{ftp | ftps | sftp} server ip-address
[user user-name password password] | tftp server ip-address} [vrouter vr-name] file-name
l
{ftp | ftps | sftp} server ip-address [user user-name password password] - 指定从
FTP/FTPS/SFTP服务器导入数据包文件。需要配置的参数为：

<!-- 来源页 2604 -->
l
ip-address - 指定FTP/FTPS/SFTP服务器的IP地址
l
user user-name password password - 指定访问FTP/FTPS/SFTP服务器使用的用户名和密
码。当不输入用户名和密码时表示采用匿名登录方式。
l
tftp server ip-address - 指定从TFTP服务器导入数据包文件。指定TFTP服务器的IP地址。
l
vrouter vr-name - 指定服务器所属的VR。系统默认为trust-vr。
l
file-name - 指定要导入的数据包文件的名称。
［命令实例］
hostname# import troubleshooting packet-trace replay-file from ftp server 10.1.1.1
user user1 password password1 test.pcap
配置导入检测源
配置导入检测源的相关信息，包括源IP地址、目的IP地址、源端口、目的端口、入接口等。
注意:
l
系统最多允许配置5个导入检测源。
l
检测源的源IP地址类型和目的IP地址类型需要保持一致。
在全局配置模式下，使用以下命令，配置导入检测源：
troubleshooting packet-trace filter name type replay-file {[src-ip ip-address | src-ipv6 ipv6-
address] [src-port port-num] [dst-ip ip-address | dst-ipv6 ipv6-address] [dst-port port-num]
[proto {tcp | udp | icmp | icmpv6 | proto-num}] [application app-name] ingress-interface
interface-name} [description description]
l
filter name - 指定导入检测源名称。
l
src-ip ip-address | src-ipv6 ipv6-address - 指定导入检测源的源IPv4地址或源IPv6地址。
l
src-port port-num - 指定导入检测源的源端口号。
l
dst-ip ip-address | dst-ipv6 ipv6-address - 指定导入检测源的目的IPv4地址或目的IPv6地址。
l
dst-port port-num - 指定导入检测源的目的端口号。
l
proto {tcp | udp | icmp | icmpv6 | proto-num} - 指定导入检测源的协议类型或者协议号。当指定
ICMP或ICMPv6协议时，若检测源的源/目的IP地址为IPv4，建议指定ICMP协议；若为IPv6，则指定
ICMPv6协议。
l
application app-name -指定导入检测源的应用类型。

<!-- 来源页 2605 -->
l
ingress-interface interface-name -指定导入检测源的入接口。
l
description description -该导入检测源的描述信息。
在全局配置模式下，使用以下命令，删除指定的导入检测源：
no troubleshooting packet-trace filter name
［命令实例］
hostname(config)# troubleshooting packet-trace filter test1 type replay-file src-ip
10.0.0.1 ingress-interface ethernet0/0
开始导入数据包路径检测
在任何模式下，使用以下命令，开始导入数据包路径检测：
exec troubleshooting packet-trace filter name start
l
filter name - 指定导入检测源名称。
［命令实例］
hostname# exec troubleshooting packet-trace filter test1 start
停止导入数据包路径检测
在任何模式下，使用以下命令，停止导入数据包路径检测：
exec troubleshooting packet-trace stop
查看数据包路径检测状态及结果
本章节包括如下内容：
l 查看数据包路径检测状态
l 查看数据包路径检测结果
查看数据包路径检测状态
型号说明：X系列设备支持按照槽位号显示相应的数据包路径检测状态信息。
在任何模式下，使用以下命令，查看数据包路径检测状态信息：
show troubleshooting packet-trace status

<!-- 来源页 2606 -->
［命令实例］
hostname(config)# show troubleshooting packet-trace status
show troubleshooting packet-trace result
查看数据包路径检测结果
型号说明：X系列设备支持按照槽位号显示相应的数据包路径检测结果信息。
在任何模式下，使用以下命令，查看数据包路径检测结果信息：
show troubleshooting packet-trace result

<!-- 来源页 2607 -->
报文回放检测
在进行安全防护功能的验证、展示或进行检测率的对比测试时，通常需要搭建专门的测试环境来对报文进行
回放，这无疑是给测试工作增添了额外负担，不便于用户进行测试。因此，防火墙支持报文回放检测，能够
在设备上直接完成报文的上传与回放，无需额外搭建复杂的测试环境，可以更便捷地进行安全防护效果的验
证以及检测率的对比测试，大大提高了测试效率和灵活性。
提示: 仅支持对以下功能进行报文回放检测：
l
入侵防御检测
l
病毒过滤检测
l
僵尸网络防御
l
边界流量过滤
l
加密流量检测
l
沙箱防护
l
攻击防护
l
URL过滤
l
数据安全
配置报文回放检测
用户可以通过命令行配置回放报文接口，并查看报文回放检测功能的配置信息。
l 配置回放报文接口
l 查看报文回放检测配置信息
配置回放报文接口
配置回放报文接口，在全局配置模式下，使用以下命令：
pcap-replay interface interface-name
l
interface-name - 指定回放报文接口的名称，指定的接口需要绑定TAP安全域。
取消配置回放报文接口，在全局配置模式下，使用以下命令：
no pcap-replay interface

<!-- 来源页 2608 -->
查看报文回放检测配置信息
查看报文回放检测配置信息，在任意模式下，使用以下命令：
show pcap-replay configuration
返回结果示例如下：
hostname# show pcap-replay configuration
Pcap replay configuration:
Replay interface: ethernet0/7（回放报文接口为ethernet0/7）

<!-- 来源页 2609 -->
在线抓包工具
在线抓包工具支持创建抓包任务进行抓包，用户可在抓包任务中设置流量出入接口，以及添加一条或多条抓
包规则，实时抓取多种条件的数据包，同时可随时查看当前抓包及丢包的情况。抓取到的数据包可被下载或
导出到本地硬盘，然后用户可以通过第三方抓包工具查看数据包内容。
在线抓包命令
配置抓包任务
包括配置抓包任务、抓包规则、开始/停止抓包、导出抓包文件、清除抓包文件。
packet-capture task
创建在线抓包任务并进入抓包任务配置模式。使用该命令no的形式删除指定的在线抓包任务。
［命令］
packet-capture task task-name
no packet-capture task task-name
［句法描述］
task-name -指定在线抓包任务的名称，并进入抓包任务配置模式。
［默认取值］
无。
［命令模式］
全局配置模式。
［使用指导］
每个VSYS最多支持配置5个抓包任务。
［命令实例］
hostname(config)# packet-capture task task1
include-self-traffic
开启抓取自流量功能，抓取的数据包中将包含设备自身收发的流量。
［命令］
include-self-traffic
no include-self-traffic

<!-- 来源页 2610 -->
［句法描述］
无。
［默认取值］
开启。
［命令模式］
抓包任务配置模式。
［使用指导］
当抓包模式为会话模式时，支持配置该功能。
［命令实例］
hostname(config-pkt-task)# include-self-traffic
only-new-session
开启只抓取新建会话数据报文功能。
［命令］
only-new-session [pak-num-per-session number]
no only-new-session
［句法描述］
pak-num-per-session number - 指定每条新建会话可以抓取的数据报文数量，该数量从会话建立时开始
计数。默认值为20个，取值范围为1到255个。例如，如果指定每条新建会话可以抓取的数据报文数量为100
个，系统将会抓取每条新建会话的前100个数据报文。
［默认取值］
禁用。
［命令模式］
抓包任务配置模式。
［使用指导］
当抓包模式为会话模式时，支持配置该功能。
［命令实例］
hostname(config-pkt-task)# only-new-session pak-num-per-session 100
interface
配置在线抓包任务的接口。使用该命令no的形式删除在线抓包任务的接口。

<!-- 来源页 2611 -->
［命令］
interface interface-name
no interface
［句法描述］
interface-name - 指定抓包任务的接口名称。在线抓包任务无法基于隧道接口和管理口抓取数据包。
［默认取值］
无。
［命令模式］
抓包任务配置模式。
［使用指导］
无。
［命令实例］
hostname(config-pkt-task)# interface ethernet0/0
direction
配置接口的流量方向。使用该命令no的形式删除接口的流量方向。
［命令］
direction {in | out}
no direction
［句法描述］
in - 指定抓取从接口进入设备的数据报文。如果没有抓取到，该报文可能已被防火墙防护或没有进入防火
墙。若没有进入防火墙，如有需要可以进一步排查上行链路或上行设备的情况。
out - 指定抓取从接口流出设备的数据报文。如果抓取到，如有需要可以进一步排查下行链路或下行设备的
情况。
如果未配置direction，则默认指定接口同时设置了入方向和出方向，根据抓取的数据包可判断该接口实际
的流量方向。
［默认取值］
无。
［命令模式］
抓包任务配置模式。

<!-- 来源页 2612 -->
［使用指导］
无。
［命令实例］
hostname(config-pkt-task)# direction in
配置抓包模式
配置抓包模式，在抓包任务配置模式下，使用以下命令：
task-info mode {session-mode | packet-mode}
l
session-mode - 会话模式。该模式下，系统可以高性能地抓取所有已建立会话且符合抓包规则的数据
报文。默认为会话模式。
l
packet-mode - 数据包模式。当系统资源充足时，该模式下，系统可以抓取全流量的数据报文。
取消配置抓包模式，在抓包任务配置模式下，使用以下命令：
no task-info mode {session-mode | packet-mode}
统一删除抓包模式、单包最大长度、抓包数量、抓包时长以及描述的配置信息，在抓包任务配置模式下，使
用以下命令：
no task-info
注意:
l
会话模式下不支持抓取硬件快转的数据报文。
l
数据包模式下不支持抓取硬件快转和IOM卡快转的数据报文。
配置单包最大长度
配置单包最大长度，在抓包任务配置模式下，使用以下命令：
task-info max-len-per-paklength
l
length - 指定每个数据包的最大抓取长度。范围是1-65536个字节。若不指定，则默认抓取完整的数据
包。当数据包的长度大于指定长度时，系统将按照指定长度抓取数据包；当数据包的长度小于或等于指
定长度时，系统将抓取完整的数据包。
取消配置单包最大长度，在抓包任务配置模式下，使用以下命令：
no task-info max-len-per-pak

<!-- 来源页 2613 -->
统一删除抓包模式、单包最大长度、抓包数量、抓包时长以及描述的配置信息，在抓包任务配置模式下，使
用以下命令：
no task-info
配置抓包数量
配置抓包数量，在抓包任务配置模式下，使用以下命令：
task-info pcap-num number-value
l
number-value - 指定抓包任务的抓包总数量，范围是1到4294967295个。在抓包任务的生效时间
（抓包时长）内，若抓包数量达到配置的总数量时，系统自动停止抓包。
取消配置抓包数量，在抓包任务配置模式下，使用以下命令：
no task-info pcap-num
统一删除抓包模式、单包最大长度、抓包数量、抓包时长以及描述的配置信息，在抓包任务配置模式下，使
用以下命令：
no task-info
配置抓包时长
配置抓包时长，在抓包任务配置模式下，使用以下命令：
task-info pcap-time time-value
l
time-value - 指定抓包任务的生效时长，范围是1到720分钟。
取消配置抓包时长，在抓包任务配置模式下，使用以下命令：
no task-info pcap-time
统一删除抓包模式、单包最大长度、抓包数量、抓包时长以及描述的配置信息，在抓包任务配置模式下，使
用以下命令：
no task-info
配置描述信息
配置抓包任务的描述信息，在抓包任务配置模式下，使用以下命令：
task-info description description
l
description - 指定抓包任务的描述信息。范围是1到255个字符。
取消配置抓包任务的描述信息，在抓包任务配置模式下，使用以下命令：
no task-info description

<!-- 来源页 2614 -->
统一删除抓包模式、单包最大长度、抓包数量、抓包时长以及描述的配置信息，在抓包任务配置模式下，使
用以下命令：
no task-info
filter-rule
配置抓包规则。使用该命令no的形式删除指定的抓包规则。
［命令］
filter-rule id id [src-ip ipv4-address/mask |src-ipv6ipv6-address/prefix | src-ip-minminipv4 src-ip-max max-ipv4 | src-ipv6-min min-ipv6 src-ipv6-max max-ipv6 |user aaa-server
user-name | user-group aaa-server user-name] [src-port port-num] [dst-ip ipv4-
address/mask |dst-ipv6ipv6-address/prefix | dst-ip-min min-ipv4 dst-ip-max max-ipv4 |
dst-ipv6-min min-ipv6 dst-ipv6-max max-ipv6 |url url ] [dst-port port-num] [proto {tcp | udp
| icmp | proto-num}] [application app-name]
no filter-rule id id
［句法描述］
filter-rule id id -指定抓包规则的ID，范围是1-8。
src-ip ipv4-address/mask - 指定需要抓取数据包的IPv4类型的源地址及掩码，不指定表示any。
src-ipv6 ipv6-address/prefix - 指定需要抓取数据包的IPv6类型的源地址及掩码，不指定表示any。
src-ip-min min-ipv4 src-ip-max max-ipv4 - 指定需要抓取数据包的IPv4类型的源地址范围，不输入
表示any。
src-ipv6-min min-ipv6 src-ipv6-max max-ipv6- 指定需要抓取数据包的IPv6类型的源地址范围，不
输入表示any。
user aaa-server user-name -指定需要抓取数据包的源用户，并指定用户所属的AAA服务器。
user-group aaa-server user-name -指定需要抓取数据包的源用户组，并指定用户组所属的AAA服务
器。
src-port port-num -指定需要抓取数据包的源端口号。
dst-ip ipv4-address/mask - 指定需要抓取数据包的IPv4类型的目的地址及掩码，不指定表示any。
dst-ipv6 ipv6-address/prefix - 指定需要抓取数据包的IPv6类型的目的地址及前缀长度，不指定表示
any。
dst-ip-min min-ipv4 dst-ip-max max-ipv4 - 指定需要抓取数据包的IPv4类型的目的地址范围，不输
入表示any。

<!-- 来源页 2615 -->
dst-ipv6-min min-ipv6 dst-ipv6-max max-ipv6- 指定需要抓取数据包的IPv6类型的目的地址范围，
不输入表示any。
url url-指定需要抓取数据包的目的URL地址。
dst-port port-num -指定需要抓取数据包的目的端口号。
proto {tcp | udp | icmp | proto-num} -指定需要抓取数据包的协议类型或者协议号。
application app-name -指定需要抓取数据包的应用类型。
［默认取值］
any。
［命令模式］
抓包任务配置模式。
［使用指导］
当抓包模式为会话模式时，支持配置该功能。
同一个抓包任务中最多允许创建8个抓包规则。
［命令实例］
hostname(config-pkt-task)# filter-rule id 1 src-ip 1.1.1.1 src-port 23 dst-ip 2.2.2.2 dst-port
23 application http
exec packet-capture
开始/停止在线抓包。
［命令］
开始在线抓包：exec packet-capture task task-name start
停止在线抓包：exec packet-capture stop
［句法描述］
task name 指定开始在线抓包的任务名称。
［默认取值］
无。
［命令模式］
任何模式。
［使用指导］
无。

<!-- 来源页 2616 -->
［命令实例］
hostname# exec packet-capture task task1 start
hostname# exec packet-capture stop
export packet-capture-file
导出已抓取的数据包文件。
［命令］
export packet-capture-file {tar task-name | file task-name file-name} to {{ftp | ftps | sftp}
server ip-address [user user-name password password] | tftp server ip-address} [vrouter vrname] [file-name]
［句法描述］
tar task-name | file task-name file-name- 导出抓包任务的所有文件压缩包或某个指定文件。
{ftp | ftps | sftp} server ip-address [user user-name password password] -指定将数据包文件导
出到FTP/FTPS/SFTP服务器。需要配置的参数为：
l
ip-address - 指定FTP/FTPS/SFTP服务器的IP地址。
l
user user-name password password – 指定访问FTP/FTPS/SFTP服务器使用的用户名和密码。当
不输入用户名和密码时表示采用匿名登录方式。
tftp server ip-address -指定将数据包文件导出到TFTP服务器。指定TFTP服务器的IP地址。
vrouter vr-name -指定服务器所属的VR。
file-name -指定导出的数据包文件的名称。
［默认取值］
vrouter vr-name - trust-vr；
［命令模式］
全局配置模式。
［使用指导］
仅带硬盘的设备支持该CLI，X系列设备、K9180及其他无硬盘设备请通过WebUI方式导出数据包文件。
导出抓包文件时，如果抓包文件过大可能会导致文件因导出超时而失败，建议单次抓包的文件不大于
500M。
［命令实例］
hostname# export packet-capture-file tar test to tftp server 10.1.1.1

<!-- 来源页 2617 -->
clear packet-capture task
清除指定抓包任务下的抓包文件。
［命令］
clear packet-capture task task-name
［句法描述］
task-name- 指定需要清除抓包文件的抓包任务名称。
［默认取值］
无。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname# clear packet-capture task task1
抓包全局配置
抓包全局配置项根据设备的类型不同而不同：
l 对于带硬盘的设备，仅在根VSYS下，用户可以配置抓包文件占硬盘总大小的百分比。
l 对于无硬盘的设备，在根VSYS下，用户可以配置抓包文件占剩余内存最大百分比、报文保存时长和内存占用上
限；在非根VSYS下，用户仅可配置报文保存时长。其中，SG-6000 X系列设备、SG-6000-
K20803/K9180/K7680/K7280/K6680设备不管是否带硬盘，抓包全局配置项都按无硬盘处理。
packet-capture save-mem
配置抓包文件占剩余内存最大百分比（无硬盘的设备）或占硬盘总大小的百分比（带硬盘的设备）。使用该
命令no的形式恢复默认值。
［命令］
packet-capture save-mem mem-percent
no packet-capture save-mem
［句法描述］

<!-- 来源页 2618 -->
mem-percent -指定抓包文件占剩余内存最大百分比（无硬盘的设备）或占硬盘总大小的百分比（带硬盘
的设备），范围是5%-50%。
［默认取值］
10%。
［命令模式］
全局配置模式。
［使用指导］
无。
［命令实例］
hostname(config)# packet-capture save-mem 20
packet-capture save-time
配置抓包文件保存的时长。使用该命令no的形式恢复默认值。
［命令］
packet-capture save-time save-time-value
no packet-capture save-time
［句法描述］
save-time-value -指定抓包文件保存的时长，单位为分钟，范围是1-1440分钟。
［默认取值］
30分钟。
［命令模式］
全局配置模式。
［使用指导］
仅无硬盘设备支持该命令。
［命令实例］
hostname(config)# packet-capture save-time 60
packet-capture dp-mem-max
配置抓包文件允许占用设备内存的上限。使用该命令no的形式恢复默认值。
［命令］
packet-capture dp-mem-max dp-mem-max-percent

<!-- 来源页 2619 -->
no packet-capture dp-mem-max
［句法描述］
dp-mem-max-percent - 指定抓包文件允许占用设备内存的上限百分比，范围是50%-90%。当设备内存
占比超过配置的上限时，系统自动停止抓包。
［默认取值］
60%。
［命令模式］
全局配置模式。
［使用指导］
仅无硬盘设备支持该命令。
［命令实例］
hostname(config)# packet-capture dp-mem-max 80
Show命令
show packet-capture status
显示抓包状态信息。
［命令］
show packet-capture status [task task-name [ cpu cpu-number | slot slot-number]]
［句法描述］
task task-name -显示指定名称的抓包任务状态信息。
cpu cpu-number | slot slot-number - 显示指定CPU或槽位号的抓包状态信息。部分设备（X系列设
备、K9180）支持。
［默认取值］
无。
［命令模式］
任何模式。
［使用指导］
仅X系列设备、K9180支持显示指定CPU或槽位号的抓包状态信息。
［命令实例］
hostname(config)# show packet-capture status task test

<!-- 来源页 2620 -->
show packet-capture task
显示抓包任务信息。
［命令］
show packet-capture task
［句法描述］
无。
［默认取值］
无。
［命令模式］
任何模式。
［使用指导］
无。
［命令实例］
hostname(config)# show packet-capture task

<!-- 来源页 2621 -->
测试工具
设备支持域名检查，支持使用网络连接测试工具Ping和Traceroute。当网络出现问题时，用户可以用这些
工具对网络进行测试，查找故障原因。
非根VSYS同样支持测试工具，包括域名检查、Ping和Traceroute。
测试工具命令
系统支持网络连接测试工具Ping和Traceroute，当网络出现问题时，用户可以用这些工具对网络进行测
试，查找故障原因。
Ping命令
Ping命令主要用于检查网络连接状态以及主机是否可达。用户可以随时在任何CLI命令模式下使用Ping命
令，检查网络连接状态及主机是否可达。其使用方法为：
ping [ipv6] {ip-address | hostname} [count number] [size number] [source ip-address]
[timeout time] [vrouter vrouter-name]
l
ipv6 - 指定对端IP地址的类型为IPv6。
l
ip-address | hostname – 指定接收Ping报文的目的地址，可以是IP地址，也可以是主机名称。在双
栈系统固件下，可以是IPv6地址。
l
count number – 指定发送Ping包的个数。范围是1到65535。默认情况下，系统会发送5个Ping包。
l
size number – 指定发送Ping包的大小。范围是28到65500字节（byte）。
l
source ip-address – 指定发送Ping包的源地址，可以是接口名称或者IP地址。
l
timeout time – 指定发送Ping包的超时时间。范围是0到3600毫秒。默认值是0，即为没有超时时间限
制。
l
vrouter vrouter-name – 指定发送Ping包的出接口所属的VRouter。默认为缺省VR，即trust-vr。
命令输出结果包括以下两部分：
l
对每个ping报文的响应情况。如果在超时时间到后仍没有收到响应报文，则输出Destination Host
Not Responding等，否则显示响应报文中报文序号、TTL和响应时间；如果ping包没有到达目的路由
或发送ping包的接口发生变化，则输出Network is unreachable；如果接受Ping报文的目的地址无法
解析时，则输出unknown host hostname。

<!-- 来源页 2622 -->
l
最后的统计信息，包括发送报文数、接收报文数、未响应报文百分比、命令执行时间和响应时间的最
小、平均、最大和平均偏差值。
以下是Ping命令使用示例：
hostname(config)# ping 10.200.3.1
Sending ICMP packets to 10.200.3.1
Seq ttl time(ms)
1 128 2.53
2 128 1.48
3 128 1.48
4 128 1.47
5 128 1.46
statistics:
5 packets sent, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 1.464/1.689/2.536/0.423 ms
Traceroute命令
Traceroute用于测试数据包从发送主机到目的地所经过的网关。它主要用于检查网络连接是否可达，以及分
析网络什么地方发生了故障。Traceroute通常的执行过程是：首先发送一个TTL为1的数据包，因此第一跳
发送回一个ICMP错误消息以指明此数据包不能被发送（因为TTL超时），之后此数据包被重新发送，TTL为
2，同样第二跳返回TTL超时，这个过程不断进行，直到到达目的地。执行这些过程的目的是记录每一个
ICMP TTL超时消息的源地址，以提供一个IP数据包到达目的地所经历的路径。系统支持对IPv4和IPv6的对
端地址进行测试。
用户可以随时在任何CLI命令模式下使用Traceroute命令测试数据包经过的网关。其使用方法为：
traceroute [ipv6] {ip-address | hostname} [numberic] [port port-number] [probe probenumber] [timeout time] [ttl [min-ttl] [max-ttl]] [source interface] [use-icmp] [vrouter vroutername]
l
ipv6 - 指定对端IP地址的类型为IPv6。
l
ip-address | hostname – 指定traceroute命令的目的地址，可以是IP地址，也可以是主机名称。在
双栈系统固件下，可以是IPv6地址。
l
numberic - 指定用数字的方式显示地址，而不对地址进行解析。

<!-- 来源页 2623 -->
l
port port-number – 指定UDP端口号。范围是1到65535。默认端口号为33434。
l
probe probe-number – 指定traceroute命令在每一跳发出的探测包的数目。范围是1到65535。默
认值是3。
l
timeout time – 指定发送下一个探测包的超时时间。范围是1到3600秒。默认值是5秒。
l
ttl [min-ttl] [max-ttl] – min-ttl用来指定最小TTL值，范围是1到255，默认值是1。max-ttl用来指定
最大TTL值，范围是1到255，默认值是30。指定TTL值，用来显示min-ttl跳到max-ttl跳的回显。
l
source interface – 指定发送traceroute探测包的源地址，只可以是源接口名称。
l
use-icmp – 指定使用ICMP包进行探测。如不配置该参数，系统将使用UDP包进行探测。
l
vrouter vrouter-name – 指定发送traceroute探测包的出接口所属的VRouter。默认为缺省
VRouter，即trust-vr。
以下是使用traceroute命令分析网络情况的示例：
hostname(config)# traceroute 210.74.176.150
traceroute to 210.74.176.150 (210.74.176.150), 30 hops max, 52 byte packets
1 10.200.3.1 (10.200.3.1) 0.572 ms 0.541 ms 0.359 ms
2 192.168.3.1 (192.168.3.1) 0.601 ms 0.754 ms 0.522 ms
3 202.106.149.177 (202.106.149.177) 1.169 ms 1.723 ms 1.104 ms
4 61.148.16.133 (61.148.16.133) 2.272 ms 1.940 ms 2.370 ms
5 61.148.4.17 (61.148.4.17) 2.770 ms 61.148.4.101 (61.148.4.101) 6.030 ms
61.148.4.21 (61.148.4.21) 2.584 ms
6 202.106.227.45 (202.106.227.45) 4.893 ms 5.010 ms 3.917 ms
7 202.106.193.70 (202.106.193.70) 5.407 ms 202.106.193.126 (202.106.193.126) 4.247
ms 202.106.193.70 (202.106.193.70) 6.954 ms
8 61.148.143.30 (61.148.143.30) 3.459 ms 3.758 ms 2.853 ms
9 * * *
10 * * *
从以上示例结果中可以看出，从源主机到目的主机经过了哪些网关，以及哪些网关出现了故障。

<!-- 来源页 2624 -->
丢包统计
型号说明：
l
支持：安装有硬盘的SG-6000 A系列设备（不含SG-6000-A1600/A1800/A2200）
l
支持：安装有硬盘的SG-6000 B系列设备
l
支持：云·界的RESTful API支持丢包统计。
系统支持对功能模块的丢包情况进行统计，帮助用户通过统计数据定位问题。功能支持详情如下：
l 支持统计功能模块的丢包数量，并以列表、柱状图、折线图的方式展示统计数据；
l 支持查看功能模块的详细丢包统计信息，包括丢包的时间、五元组信息（源IP、源端口、目的IP、目的端口、协
议）、丢包模块；
l 允许手动开启丢包五元组统计，记录丢包五元组信息；或者设置异常丢包阈值，达到阈值后触发丢包五元组信息
统计；
l 支持将丢包统计数据存储到设备硬盘，允许用户设置统计数据存储空间大小限制。
丢包统计命令
始终记录丢包五元组信息
用户可以开启始终记录丢包五元组信息功能，开启该功能后系统会始终统计并记录所有功能模块的丢包五元
组信息（源IP、源端口、目的IP、目的端口、协议）。开启始终记录丢包五元组信息功能，请在全局配置模
式下，使用以下命令：
module-drop-counter force-cap-packet enable
在全局配置模式下，使用no module-drop-counter force-cap-packet enable命令关闭始终记录丢包
五元组信息功能。
注意: 开启始终记录丢包五元组信息功能后，功能模块的丢包阈值设置及丢包增长率阈值设置均无
效。

<!-- 来源页 2625 -->
设置丢包阈值
用户可以为功能模块设置丢包阈值，当功能模块的丢包数量超过该阈值时，会被判断为异常丢包，并记录异常丢包的
五元组信息。为功能模块设置丢包阈值，请在全局配置模式下，使用以下命令：
module-drop-counter module module-name threshold number
l module-name - 指定功能模块名称。
l number - 指定丢包阈值。取值范围为0-20000。默认值为0，表示未设置阈值，始终统计并记录丢包五元组信
息。
在全局配置模式下，使用no module-drop-counter modulemodule-name命令恢复默认阈值。
设置丢包增长率阈值
用户可以为功能模块设置丢包增长率阈值，当功能模块的丢包增长率超过该阈值时，会被判断为异常丢包，
并记录异常丢包的五元组信息。为功能模块设置丢包增长率阈值，请在全局配置模式下，使用以下命令：
module-drop-counter growth-rate number
l number - 指定丢包增长率阈值。取值范围为0-100。默认值为0，表示未设置阈值，始终统计并记录丢包五元组
信息。
在全局配置模式下，使用no module-drop-counter growth-rate令恢复默认阈值。

<!-- 来源页 2626 -->
系统调试
系统具有调试功能，供用户查阅与分析。
系统调试功能
系统调试功能可以帮助用户对错误进行诊断和定位。设备的各种协议和功能基本上都具有相应的调试功能。
默认情况下，所有协议和功能的系统调试功能都是关闭的。用户只可以通过CLI对系统调试功能进行配置。开
启设备的系统调试功能，请在任何模式下输入以下命令：
debug {all | function-name}
l
all– 开启设备所有协议和功能的系统调试功能。
l
function-name – 开启设备指定协议或功能的系统调试功能。
在任何配置模式输入以下命令关闭所有或指定功能的系统调试功：
undebug {all | function-name}
用户还可以通过双击“ESC”键关闭debug功能。由于部分信息被缓存，关闭过程可能会持续几分钟。
查看调试功能开启或者关闭状态，请在任何模式下输入以下命令：
show debug
注意: 调试功能开启后，如果需要在终端输出debug信息，请开启系统的debug日志功能（执行
logging debug on命令）。
收集并保存技术支持信息到文件
为了便于定位系统故障，系统支持收集show相关命令的显示信息，并保存成tech-support文件。收集并
保存技术支持信息到文件，在任意模式下，使用以下命令：
show tech-support [cpu cpu-number | all]
l
cpu-number –收集并保存指定CPU的技术支持信息到文件。该参数仅在多CPU系统中显示。
l
all –收集并保存所有技术支持信息到文件。该参数仅在多CPU系统中显示。
注意: 单CPU系统直接通过show tech-support命令收集并保存所有技术支持信息到文件。

<!-- 来源页 2627 -->
显示技术支持信息
显示技术支持信息到Console口，在任意模式下，使用以下命令：
show tech-support [cpu cpu-number | all] toconsole
l
cpu-number – 显示指定CPU的技术支持信息到Console口。该选项仅在多CPU系统中显示。
l
all –显示所有技术支持信息到Console口。该选项仅在多CPU系统中显示。
注意: 单CPU系统直接通过show tech-support toconsole命令显示技术支持信息到Console
口。
显示nvramlog或watchdoglog日志信息
显示tech-support文件中的nvramlog或者watchdoglog日志信息，在任意模式下，使用以下命令：
show tech-support log-name
l
log-name - 指定需要显示的日志信息的名称。可以指定为nvramlog或者watchdoglog。

<!-- 来源页 2628 -->
修改dumpfile收集的检查周期
dumpfile（转储文件）是指防火墙系统在出现进程死锁/处理耗时等特定条件下生成的一种记录当前系统运
行状态的二进制文件。它包含了系统内存、进程数据、堆栈信息等关键内容，常用于故障定位和问题分析。
在防火墙系统中，dumpfile收集的检查周期是指系统检查业务数据层面（DP）任务处理是否出现异常状态
（如进程死锁/处理耗时等）的周期时长。当系统在预设周期内监测到DP任务处理出现异常，会自动触发
dumpfile收集流程。默认情况下，dumpfile收集的检查周期时间为2秒。用户可根据实际需求，合理调整
dumpfile收集的检查周期，确保dumpfile能够准确记录“持续异常” 的状态，为后续故障排查和系统优
化提供精准的信息支持。
修改dumpfile收集的检查周期，在Flow配置模式下（进入Flow配置模式，在全局配置模式下，使用flow
命令），使用下输入以下命令：
dp-dumpfile interval value
l
value– 指定dumpfile收集的检查周期，取值范围为500到2000毫秒（即500毫秒~2秒）。默认为2
秒。
在Flow配置模式下，使用以下命令，恢复默认值：
no dp-dumpfile interval
下一步
在dumpfile收集成功后，用户可通过以下两种方式获取并分析故障数据：
l WebUI操作路径：登录防火墙管理界面，选择“系统> 设备管理> 设置及操作> 系统操作”，然后点击系统调
试信息后的“导出”按钮，导出tech-support文件压缩包。解压后可在flash/dump_file目录下查看对应的
dumpfile文件。
l CLI命令操作：在任意模式下，使用export tech-support to { ftp | tftp } server ip-address [useruser-name
password password] [vrouter vrouter-name] 命令导出tech-support文件压缩包。该方式导出tech-support
文件可能需要较长时间，请谨慎使用。
提示: 建议用户优先采用WebUI方式导出文件至本地进行分析，该方式相较于CLI命令操作更便捷
且便于深度诊断。
