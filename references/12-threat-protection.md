# 威胁防护

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 15 威胁防护
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 2104 -->
15 威胁防护
本章节包含以下内容：
l "病毒过滤" 在第2138页：介绍了如何检测并防护针对不同文件类型（GZIP、BZIP2、TAR、ZIP、RAR、PE、
HTML、MAIL、RIFF、ELF、PDF、MS OFFICE、Raw Data和Others）和常用协议类型（HTTP、FTP、、
HTTPS、SMTP、POP3、IMAP4以及SMB）的病毒攻击。
l "攻击防护" 在第2107页: 介绍了常见的网络攻击、如何配置攻击防护功能以及攻击防护配置举例。
l "沙箱防护" 在第2166页：介绍了沙箱防护功能、如何配置沙箱防护规则以及如何更新沙箱所使用的域名白名
单。
l "入侵防御" 在第2178页：介绍了如何检测并防护针对主流应用层协议（DNS、FTP、HTTP、POP3、SMTP、
TELNET、MYSQL、MSSQL、ORACLE、NETBIOS等）的入侵攻击、基于Web的攻击行为以及常见的木马攻击。
l "IP地理库" 在第2277页：介绍了如何更新IP地理库。（仅支持CLI方式配置）。
l "威胁防护特征库" 在第2281页：介绍了威胁防护特征库与他的升级方式。
l "僵尸网络防御" 在第2292页：介绍了如何配置基于安全域和基于策略的僵尸网络防御功能从而进行僵尸网络检
查。
l "加密流量检测" 在第2314页：介绍了如何配置加密流量检测功能从而对加密攻击流量进行检测。
l "蜜罐诱捕" 在第2320页：介绍了如何在防火墙设备中连接蜜罐系统并配置诱捕规则，将命中诱捕规则的攻击者IP
引流到蜜罐系统中进行封堵，避免用户的真实业务环境遭到攻击。
l "企业IT设备和IoT设备统一管理" 在第2338页：介绍了如何配置整体的设备管理功能，可实现对于企业内部IT设
备、IoT设备的发现、识别、安全管控和威胁治理。
l 重保模式：介绍了如何配置重保模式的安全防护模板、特征库和黑白名单，可实现重保期间迅速、高效地识别和
阻断各种攻击。
l "云网协同DNS安全防御" 在第2329页：介绍如何配置未知域名云端协同查询功能和云端DNS安全检测功能。

<!-- 来源页 2105 -->
安全防护全局配置
安全防护全局配置包括：
l 配置抓包取证模式
l 开启/关闭代理IP信息显示功能
l 配置代理IP的提取位置
l 配置攻击者/受害者IP解析功能
l 配置解析方式
l 开启/关闭密码信息外发功能
开启/关闭代理IP信息显示功能
开启该功能后，在HTTP代理的部署环境下，当系统检测到威胁事件时，系统能够记录相应HTTP流量中的代
理IP信息。用户可以在威胁日志和威胁事件中查看代理IP地址。该功能默认为开启状态。
开启/关闭代理IP信息显示功能，在全局配置模式下，使用以下命令：
l
开启：proxy-ip enable
l
关闭：proxy-ip disable
注意:
l
代理IP信息展示功能对入侵防御、病毒过滤、黑白名单、僵尸网络防御功能生效。
l
代理IP信息展示功能独立生效，不会影响攻击者/受害者IP解析功能以及CC防护中的XForwarded-For配置。
配置代理IP的提取位置
用户能够选择提取代理IP信息中的第一个、最后一个或者全部IP信息，默认为记录全部代理IP信息。
配置代理IP的提取位置，在全局配置模式下，使用以下命令：
extract proxy-ip position {first | last | all}
l
first - 提取代理IP信息中的第一个代理IP信息。
l
last - 提取代理IP信息中的最后一个代理IP信息。
l
all - 提取代理IP信息中的全部代理IP信息。

<!-- 来源页 2106 -->
注意: 选择提取全部代理IP信息后，系统最多记录并展示前5个代理IP信息。
配置攻击者/受害者IP解析功能
开启攻击者/受害者IP解析功能后，在HTTP代理的部署场景下，当设备产生威胁信息（包括威胁日志和威胁
事件）时，威胁信息中的攻击者/受害者字段会记录为真实IP；关闭后，威胁信息中的攻击者/受害者字段会
记录为HTTP代理IP。该功能默认为开启状态。
注意:
l
攻击者/受害者IP解析功能对入侵防御、病毒过滤、沙箱防护、僵尸网络防御功能生效。
l
在功能开启状态下，如果源IP为攻击者，则威胁信息中的攻击者字段会记录为真实IP；如果源
IP为受害者，则威胁信息中的受害者字段会记录为真实IP。
开启攻击者/受害者IP解析功能，在全局配置模式下，使用以下命令：
attacker-victim ip-parsing enable
关闭攻击者/受害者IP解析功能，在全局配置模式下，使用以下命令：
attacker-victim ip-parsing disable
配置解析方式
开启攻击者/受害者IP解析功能后，用户还需要配置解析方式，最多能够配置10条解析方式。若不配置解析
方式，则攻击者/受害者IP解析功能将不生效。
进入解析方式配置模式
进入解析方式配置模式，在全局配置模式下，使用以下命令：
attacker-victim ip-parsing method
配置解析方式
配置解析方式，在解析方式配置模式下，使用以下命令：
method id id set header {X-Forwarded-For direction {left | right} position number | X-Real-Ip
| cdn-src-ip}

<!-- 来源页 2107 -->
l
id - 指定解析方式的ID，取值范围为1-10。
l
X-Forwarded-For - 指定从X-Forwarded-For请求头中获取真实IP。系统会在请求头中依次提取前5
个IP（若不足5个则全部提取），用户还需配置取左/取右第number个IP作为真实IP。当配置的个数超
过系统提取到的IP数时，则获取不到真实IP。例如，配置取右第3个IP，而系统在请求头中只提取到了2
个IP，那么该解析方式将获取不到真实IP。
l
left | right - 指定从左开始选择真实IP或者从右开始选择真实IP。
l
number - 指定选择第number个IP作为真实IP。取值范围为1-5。
l
X-Real-Ip - 指定从X-Real-IP请求头中获取真实IP。
l
cdn-src-ip - 指定从cdn-src-ip请求头中获取真实IP。
删除解析方式，在全局配置下，使用以下命令：
no method id id
调整解析方式优先级
列表中位置越靠前的解析方式，匹配优先级越高。
调整解析方式优先级，在解析方式配置模式下，使用以下命令：
method id id move {after id move-id | before id move-id | bottom | top}
l
id - 指定需要调整优先级的解析方式ID。
l
after id move-id - 移动到指定ID的解析方式后。
l
before id move-id - 移动到指定ID的解析方式前。
l
bottom - 移动到所有解析方式的末位。
l
top - 移动到所有解析方式的首位。
查看解析方式配置信息
用户可以查看解析方式的配置信息以及优先级。列表中位置越靠前的解析方式，匹配优先级越高。
查看解析方式配置信息，在任意模式下，使用以下命令：
show security configurations
以下是返回结果示例：
hostname(config)# show security configurations
proxy ip show status: enabled ( 已开启代理IP信息显示功能)

<!-- 来源页 2108 -->
logging position of proxy ip: all ( 提取代理IP信息中的全部代理IP信息)
threat-syslog-send-payload: off ( 未开启IPS威胁日志携带攻击数据报文功能)
threat-syslog-send-payload encode base64 ( 已开启攻击数据报文的base64编
码功能)
attacker-victim ip-parsing status: enabled ( 已开启攻击者/受害者IP解析功
能)
======================================================
ID Header Direction Position ( 解析方式配置信息列表)
------------------------------------------------------
2 X-Real-IP N/A N/A
1 X-Forwarded-For Right 1
------------------------------------------------------
password-exfiltration: disable ( 未开启密码信息外发功能)
开启/关闭密码信息外发功能
开启后系统会将弱口令事件、暴力破解成功事件、HTTP明文密码事件中的密码信息上送至云景和智源平台，
同时能够将暴力破解成功事件中的密码信息外发至第三方平台。该功能默认为关闭状态。
开启/关闭密码信息外发功能，在全局配置模式下，使用以下命令：
l
开启：password-exfiltration enable
l
关闭：password-exfiltration disable

<!-- 来源页 2109 -->
攻击防护
介绍
网络中存在多种防不胜防的攻击，如侵入或破坏网络上的服务器、盗取服务器的敏感数据、破坏服务器对外
提供的服务，或者直接破坏网络设备导致网络服务异常甚至中断。作为网络安全设备，必须具备攻击防护功
能来检测各种类型的网络攻击，从而采取相应的措施保护内部网络免受恶意攻击，以保证内部网络及系统正
常运行。
系统提供基于安全域的攻击防护功能，能够对网络攻击进行合理处理从而保证用户网络系统的安全。
常见网络攻击概述
本节介绍一些常见的网络攻击。设备能够对这些网络攻击进行合理处理从而保证用户网络系统的安全。
ICMP Flood和UDP Flood攻击
这种攻击在短时间内向被攻击目标发送大量的ICMP消息（如ping）和UDP报文，请求回应，致使被攻击目
标负担过重而不能完成正常的传输任务。
ARP欺骗攻击
局域网的网络流通根据MAC地址进行传输。ARP欺骗攻击是通过填写错误的发送端MAC地址和IP地址，使目
标主机的ARP缓存表中IP地址和MAC地址对应关系错误。导致目标主机后续将IP数据报文时发给错误主机，
目标网络不通且报文资源被窃取。
SYN Flood攻击
由于资源的限制，服务器只能允许有限个TCP连接。而SYN Flood攻击正是利用这一点，它伪造一个SYN报
文，将其源地址设置成伪造的或者不存在的地址，然后向服务器发起连接。服务器在收到报文后用SYN-ACK
应答，而此应答发出去后，不会收到ACK报文，从而造成半连接。如果攻击者发送大量这样的报文，会在被
攻击主机上出现大量的半连接，直到半连接超时，从而消耗尽其资源，使正常的用户无法访问。在连接不受
限制的环境里，SYN Flood会消耗掉系统的内存等资源。
SIP Flood攻击
SIP(Session Initiation Protocol)是一个应用层的信令控制协议，它被用来发起、修改和终止交互式多媒
体会话，例如多媒体会议或者IP电话。SIP Flood攻击由攻击者在短时间内向被攻击SIP服务器发送大量的
INVITE请求，导致SIP服务器资源耗尽，无法响应合法用户的呼叫请求。

<!-- 来源页 2110 -->
WinNuke攻击
WinNuke攻击通常向装有Windows系统的特定目标的NetBIOS端口（139）发送OOB（out-of-band）
数据包，引起一个NetBIOS片断重叠，致使被攻击主机崩溃。还有一种是IGMP分片报文。一般情况下，
IGMP报文是不会分片的，所以，不少系统对IGMP分片报文的处理有问题。如果收到IGMP分片报文，则基
本可判定受到了攻击。
IP地址欺骗（IP Spoofing）攻击
IP地址欺骗攻击是一种获取对计算机未经许可的访问的技术，即攻击者通过伪IP地址向计算机发送报文，并
显示该报文来自于真实主机。对于基于IP地址进行验证的应用，此攻击方法能够使未被授权的用户访问被攻
击系统。即使响应报文不能到达攻击者，被攻击系统也会遭到破坏。
ICMP重定向攻击
ICMP重定向报文属于ICMP控制报文的一种，它用于提示主机改变路由从而使路由路径最优化。ICMP重定向
攻击是指攻击者通过向被攻击者发送虚假ICMP重定向报文，以改变被攻击者的主机路由表，从而达到干扰主
机正常IP报文发送的目的。
地址扫描与端口扫描攻击
这种攻击运用扫描工具探测目标地址和端口，对此作出响应的表示其存在，从而确定哪些目标系统确实存活
着并且连接在目标网络上，这些主机使用哪些端口提供服务。
Ping of Death攻击
Ping of Death就是利用一些尺寸超大的ICMP报文对系统进行的一种攻击。IP报文的字段长度为16位，这
表明一个IP报文的最大长度为65535字节。对于ICMP 回应请求报文，如果数据长度大于65507字节，就会
使ICMP数据、IP头长度（20字节）和ICMP头长度（8字节）的总合大于65535字节。一些路由器或系统在
接收到这样一个报文后会由于处理不当，造成系统崩溃、死机或重启。
Teardrop攻击防护
Teardrop攻击是一种拒绝服务攻击。是基于UDP的病态分片数据包的攻击方法，其工作原理是向被攻击者
发送多个分片的IP包（IP分片数据包中包括该分片数据包属于哪个数据包以及在数据包中的位置等信息），
某些操作系统收到含有重叠偏移的伪造分片数据包时将会出现系统崩溃、重启等现象。
Land攻击
在Land攻击中，攻击者将一个特别打造的数据包的源地址和目标地址都设置成被攻击服务器地址。这样被攻
击服务器向它自己的地址发送消息，结果这个地址又发回消息并创建一个空连接，每一个这样的连接都将保
留直到超时。在这种Land攻击下，许多服务器将崩溃。

<!-- 来源页 2111 -->
Smurf攻击
Smurf攻击分简单和高级两种。简单Smurf攻击用来攻击一个网络。方法是将ICMP应答请求包的目标地址设
置为被攻击网络的广播地址，这样该网络的所有主机都会对此ICMP应答请求作出答复，从而导致网络阻塞。
高级Smurf攻击主要用来攻击目标主机。方法是将ICMP应答请求包的源地址更改为被攻击主机的地址，最终
导致被攻击主机崩溃。理论上讲，网络的主机越多，攻击的效果越明显。
Fraggle攻击
Fraggle攻击与Smurf攻击为同种类型攻击。不同之处在于Fraggle攻击使用UDP包形成攻击。
IP Fragment攻击
攻击者通过向目标主机发送分片偏移小于5的分片报文，导致主机对分片报文进行重组时发生错误而造成系
统崩溃。
IP Option攻击
攻击者利用IP报文中的异常选项的设置，达到探测网络结构的目的，也可由于系统缺乏对错误报文的处理而
造成系统崩溃。
Huge ICMP包攻击
某些主机或设备收到超大的报文，会引起内存分配错误而导致协议栈崩溃。攻击者通过发送超大ICMP报文，
让目标主机崩溃，达到攻击目的。
TCP Flag异常攻击
不同操作系统对于非常规的TCP标志位有不同的处理。攻击者通过发送带有非常规TCP标志的报文探测目标
主机的操作系统类型，若操作系统对这类报文处理不当，攻击者便可达到使目标主机系统崩溃的目的。
DNS Query Flood攻击
DNS服务器收到任何DNS Query报文时都会试图进行域名解析并且回复该DNS报文。攻击者通过构造并向
DNS服务器发送大量虚假DNS Query报文，占用DNS服务器的带宽或计算资源，使得正常的DNS Query得
不到处理。
DNS Reply Flood攻击
DNS服务器收到任何DNS Reply报文时都会对其进行处理。攻击者通过构造并向DNS服务器发送大量DNS
Reply报文，导致DNS缓存服务器因处理这些DNS Reply报文而资源耗尽，影响正常业务。

<!-- 来源页 2112 -->
TCP Split Handshake攻击
客户端与恶意TCP服务器建立TCP连接时，恶意服务器伪造SYN包及其内容，向客户端发起TCP连接。建立
TCP连接后，恶意TCP服务器反转角色变成了发起TCP连接的“客户端”，使得恶意流量进入内网。
ICMP不可达攻击
ICMP不可达攻击是一种利用ICMP不可达报文干扰或中断目标设备网络通信的攻击方式。攻击者通常会发送
大量伪造的ICMP不可达报文来干扰设备的正常通信，导致流量异常或引发网络拥塞，影响设备性能。
ARP Flood攻击
ARP Flood攻击是指利用ARP协议的广播特性，通过发送大量伪造的ARP请求或响应报文，对目标网络设备
进行攻击。这些伪造的ARP报文可能包含错误的IP-MAC映射关系，设备获取后将导致通信失败。此外，大
量的ARP伪造报文会大大占用系统资源，导致系统业务无法正常运行。
HTTPS Flood攻击
HTTPS洪水攻击是一种针对HTTPS加密协议服务的分布式拒绝服务（DDoS）攻击，其核心目标是通过向目
标服务器发送大量伪造或半合法的HTTPS请求，耗尽服务器的CPU、内存、网络带宽等关键资源，最终导致
服务器无法正常处理合法用户的HTTPS请求，造成服务中断或响应极度缓慢。
配置攻击防护功能
设备的攻击防护功能在默认情况下，只有部分功能在Untrust安全域是开启的，包括IP地址欺骗攻击防护、
IP地址扫描攻击防护、IP协议扫描攻击防护、TCP端口扫描防护、UDP端口扫描防护、ICMP Flood攻击防
护、SYN Flood攻击防护、UDP Flood攻击防护、WinNuke攻击防护、Ping of Death攻击防护、
Teardrop攻击防护、IP Option攻击防护、IP Fragment攻击防护、IP Directed Broadcast攻击防护、
Land攻击防护、ICMP重定向攻击防护和ICMP不可达攻击防护。
开启安全域的所有攻击防护功能
开启安全域的所有攻击防护功能，在安全域配置模式下，使用以下命令：
ad all
在安全域配置模式下使用no ad all命令关闭安全域的所有攻击防护功能。
提示: 如果需要对ZTNA接入用户的流量进行攻击防护检查及防御，需要在隧道接口的安全域开启
攻击防护功能。
用户可以对各种攻击防护功能的具体参数根据需求进行配置。设备的攻击防护配置包括：

<!-- 来源页 2113 -->
l 配置IP地址扫描攻击防护功能
l 配置ICMP重定向攻击防护功能
l 配置ICMP不可达攻击防护功能
l 配置IP协议扫描攻击防护功能
l 配置TCP端口扫描防护功能
l 配置UDP端口扫描防护功能
l 配置IP地址欺骗攻击防护功能
l 配置SYN Flood攻击防护功能
l 配置SYN-Proxy功能
l 配置SIP Flood攻击防护功能
l 配置ICMP Flood攻击防护功能
l 配置UDP Flood攻击防护功能
l 配置HTTPS Flood攻击防护功能
l 配置Flood防护阈值学习功能
l 配置Huge ICMP包攻击防护功能
l 配置WinNuke攻击防护功能
l 配置Ping of Death攻击防护功能
l 配置Teardrop攻击防护功能
l 配置IP Option攻击防护功能
l 配置TCP异常攻击防护功能
l 配置Land攻击防护功能
l 配置IP 碎片攻击防护功能
l 配置Smurf和Fraggle攻击防护功能
l 配置ARP欺骗防护功能
l 配置ARP Flood攻击防护功能
l 配置DNS Query Flood攻击防护功能
l 配置DNS Reply Flood攻击防护功能
l 配置攻击防护源认证功能

<!-- 来源页 2114 -->
l 配置TCP Split Handshake攻击防护功能
l 配置攻击防护白名单
l 显示安全域的攻击防护配置和统计信息
配置IP地址扫描攻击防护功能
用户可以单独开启或者关闭安全域的IP地址扫描攻击防护功能，也可以配置地址扫描的警戒时间值和设备采
取的行为。配置指定域的IP地址扫描攻击防护功能，在安全域配置模式使用以下命令：
ad ip-sweep [threshold value | action {alarm | drop | block [block-time number]} | tcp]
l
ad ip-sweep – 开启安全域的IP地址扫描攻击防护功能。使用no ad ip-sweep关闭该功能。
l
threshold value – 指定地址扫描的时间警戒值。如果设备探测到在该指定时间内同一个源IP地址发送
10个以上的ICMP/TCP包到不同的主机，设备就认为是受到IP地址扫描攻击。默认值是1，单位是毫秒，
取值范围是1到1800000毫秒。使用no ad ip-sweep threshold命令恢复警戒默认值。
l
action {alarm | drop | block [block-time number]} – 指定设备对于IP地址扫描攻击的所采取的行
为。使用no ad ip-sweep action恢复默认操作。
o
alarm– 在指定时间内（threshold value），同一个源IP地址允许10个发往不同主机的
ICMP/TCP包通过，超出10个系统会发出警报但允许通过。
o
drop – 在指定时间内（threshold value），同一个源IP地址仅允许10个发往不同主机的
ICMP/TCP包通过，超出的ICMP/TCP包将会被系统丢弃并且发出警报。默认行为是drop。
o
block [block-time number]- 在指定时间内（threshold value）将设备探测到的源IP加入黑
名单，并且在指定阻断时间内阻止源IP地址发出的数据包通过。block-time number- 指定阻断
时长，单位为秒，取值范围是1分钟到15天。当不配置阻断时长，默认为永久阻断（block）。
l
tcp- 指定设备探测在指定时间（threshold value）内同一个源IP地址发送10个以上的TCP包到不同的
主机，设备就认为是受到IP地址扫描攻击。用no ad ip-sweep tcp关闭对TCP包的探测功能。
注意:
在TAP安全域不支持配置攻击防护（AD）阻断功能。
配置ICMP重定向攻击防护功能
用户可以单独开启或者关闭安全域的ICMP重定向攻击防护功能，也可以配置受到ICMP重定向攻击后设备采
取的行为。配置指定域的ICMP重定向攻击防护功能，在安全域配置模式使用以下命令：
ad icmp-redirect [action {alarm | drop}]

<!-- 来源页 2115 -->
l
ad icmp-redirect– 开启安全域的ICMP重定向攻击防护功能。使用no ad icmp-redirect关闭该功
能。该功能默认为开启状态。
l
action {alarm | drop}– 指定设备对于ICMP重定向攻击的所采取的行为。alarm– 发出警报但是允许包
通过；drop – 发出警报并且丢弃攻击包。默认行为是drop。使用no ad icmp-redirect action恢复默
认操作。
配置ICMP不可达攻击防护功能
ICMP不可达攻击是一种利用ICMP不可达报文干扰或中断目标设备网络通信的攻击方式。攻击者通常会发送
大量伪造的ICMP不可达报文来干扰设备的正常通信，导致流量异常或引发网络拥塞，影响设备性能。用户可
以通过ICMP不可达攻击防护功能，过滤掉ICMP不可达报文，确保设备接收到的ICMP报文是真实可靠的，从
而维护网络拓扑的准确性和网络的可用性。
配置ICMP不可达攻击防护功能，在安全域配置模式下，使用以下命令：
ad icmp-unreachable [action {alarm | drop}]
l
ad icmp-unreachable - 开启安全域的ICMP不可达攻击防护功能。该功能默认为开启状态。
l
action {alarm | drop} - 指定设备对于ICMP不可达攻击所采取的处理动作。指定alarm为发出警报但
是允许报文通过；指定drop为发出警报并且丢弃ICMP不可达攻击报文。若不指定，默认处理动作为
drop。
恢复ICMP不可达攻击防护功能的默认处理动作，在安全域配置模式下，使用以下命令：
no ad icmp-unreachable action
关闭ICMP不可达攻击防护功能，在安全域配置模式下，使用以下命令：
no ad icmp-unreachable
配置IP协议扫描攻击防护功能
用户可以单独开启或者关闭安全域的IP协议扫描攻击防护功能，也可以配置IP协议扫描的警戒时间值和设备
采取的行为。配置指定域的IP协议扫描攻击防护功能，在安全域配置模式使用以下命令：
ad ip-proto-scan [threshold value | action {alarm | drop | block [block-time number]}]
l
ad ip-proto-scan – 开启安全域的IP协议扫描攻击防护功能。使用no ad ip-proto-scan关闭该功
能。

<!-- 来源页 2116 -->
l
threshold value – 指定IP协议扫描的时间警戒值。如果设备探测到在该指定时间内同一个源IP地址发
送10个以上相同IP协议的数据包到同一台主机，设备就认为是受到IP协议扫描攻击。默认值是10，单位
是毫秒，取值范围是1到1800000毫秒。使用no ad ip-proto-scan threshold命令恢复警戒默认值。
l
action {alarm | drop | block [block-time number]} – 指定设备对于IP协议扫描攻击所采取的行
为。使用no ad ip-proto-scan action恢复默认操作。
o
alarm – 在指定时间内（threshold value），同一个源IP地址允许10个发往同一主机的相同IP
协议数据包通过，超出10个系统会发出警报但允许通过。
o
drop – 在指定时间内（threshold value），同一个源IP地址仅允许10个发往同一主机的相同IP
协议数据包通过，超出的IP协议报文将会被系统丢弃并且发出警报。默认行为是drop。
o
block [block-time number]- 在指定时间内（threshold value）将设备探测到的源IP加入黑
名单，并且在指定阻断时间内阻止源IP地址发送的不同协议的数据包通过。block-time number
- 指定阻断时长，单位为秒，取值范围是1分钟到15天。当不配置阻断时长，默认为永久阻断
（block）。
注意:
在TAP安全域不支持配置攻击防护（AD）阻断功能。
配置TCP端口扫描防护功能
用户可以单独开启或者关闭安全域的TCP端口扫描防护功能，也可以配置TCP端口扫描的警戒时间值和设备
采取的行为。配置安全域的TCP端口扫描防护功能，在安全域配置模式使用以下命令：
ad port-scan [threshold value | action {alarm | drop | block [block-time number]}]
l
ad port-scan– 开启安全域的TCP端口扫描攻击防护功能。使用no ad port-scan关闭该功能。
l
threshold value– 指定TCP端口扫描的时间警戒值。如果设备探测到在该指定时间内同一个源IP地址发
送10个以上TCP SYN包到同一目标的不同端口，设备就认为是受到了TCP端口扫描攻击。默认值是5，单
位是毫秒，取值范围是1到1800000毫秒。使用no ad port-scan threshold命令恢复警戒默认值。
l
action {alarm | drop | block [block-time number]} – 指定设备对于TCP端口扫描所采取的行为。
使用no ad port-scan action恢复默认操作。
o
alarm – 在指定时间内（threshold value），同一个源IP地址允许10个发往同一目标的不同端
口的TCP SYN包通过，超出10个系统会发出警报但允许通过。

<!-- 来源页 2117 -->
o
drop – 在指定时间内（threshold value），同一个源IP地址仅允许10个发往同一目标的不同端
口的TCP SYN包通过，超出的TCP SYN包将会被系统丢弃并且发出警报。默认行为是drop。
o
block [block-time number]- 在指定时间内（threshold value）将设备探测到的源IP加入黑
名单，并且在指定时间内阻断源IP地址发往不同端口的TCP SYN包通过。block-time number -
指定阻断时长，单位为秒，取值范围是1分钟到15天。当不配置阻断时长，默认为永久阻断
（block）。
注意:
在TAP安全域不支持配置攻击防护（AD）阻断功能。
配置UDP端口扫描防护功能
用户可以单独开启或者关闭安全域的UDP端口扫描防护功能，也可以配置UDP端口扫描的警戒时间值和设备
采取的行为。配置安全域的UDP端口扫描防护功能，在安全域配置模式使用以下命令：
ad udp-port-scan [threshold value | action {alarm | drop | block [block-time number]}]
l
ad udp-port-scan – 开启安全域的UDP端口扫描防护功能。使用no ad udp-port-scan关闭该功
能。
l
threshold value – 指定UDP端口扫描的时间警戒值。如果设备探测到在该指定时间内同一个源IP地址
发送10个以上UDP包到同一目标的不同端口，设备就认为是受到了端口扫描攻击。默认值是5，单位是
毫秒，取值范围是1到1800000毫秒。使用no ad udp-port-scan threshold命令恢复警戒默认值。
l
action {alarm | drop | block [block-time number]} – 指定设备对于UDP端口扫描所采取的行为。
使用no ad udp-port-scan action恢复默认操作。
o
alarm – 在指定时间内（threshold value），同一个源IP地址允许10个发往同一目标的不同端
口的UDP包通过，超出10个系统会发出警报但允许通过。
o
drop – 在指定时间内（threshold value），同一个源IP地址仅允许10个发往同一目标的不同端
口的UDP包通过，超出的UDP包将会被系统丢弃并且发出警报。默认行为是drop。
o
block [block-time number]- 在指定时间内（threshold value）将设备探测到的源IP加入黑
名单，并且在指定时间内阻断源IP地址发往不同端口的UDP包通过。block-time number - 指定
阻断时长，单位为秒，取值范围是1分钟到15天。当不配置阻断时长，默认为永久阻断
（block）。

<!-- 来源页 2118 -->
注意:
在TAP安全域不支持配置攻击防护（AD）阻断功能。
配置IP地址欺骗攻击防护功能
系统可防护三层IP地址欺骗攻击。
开启设备的三层IP地址欺骗攻击防护功能后，数据包进入设备后，系统会对其源IP地址进行反向路由查询，
并根据反向路由查询结果采取不同的行为，包括：
l 如果以该IP为源地址的数据包进入设备的安全域和以该IP为目的地址的数据包离开设备的安全域是一致的（根据
反向路由查询结果可以知道以该IP为目的地址的数据包离开设备的安全域），则该数据包正常通过。
l 反之，系统判断该数据包为非正常数据包，将发出警报并丢弃该数据包。
开启/关闭安全域的三层IP地址欺骗攻击防护功能
开启安全域的三层IP地址欺骗攻击防护功能，在三层安全域配置模式下使用以下命令：
ad ip-spoofing
在安全域配置模式下使用no ad ip-spoofing关闭安全域的IP地址欺骗攻击防护功能。
配置SYN Flood攻击防护功能
用户可以单独开启或者关闭域的SYN Flood攻击防护功能，也可以配置SYN Flood攻击的源IP、目的IP和目
的端口的警戒值以及设备的采取的行为。配置设备的SYN Flood攻击防护功能，在域配置模式下使用以下命
令：
ad syn-flood [source-threshold number | destination-threshold [ip-based | port-based]
number | destination [ip-based | port-based [address-book address-entry | A.B.C.D/M] |
action {alarm | drop}]
l
ad syn-flood – 开启安全域的SYN Flood攻击防护功能。使用no ad syn-flood关闭该功能。
l
source-threshold number – 指定一秒钟内从一个源IP地址发出的SYN包的个数，无论目标IP地址和
端口号是什么。如果设备探测到一秒钟内从同一个源IP地址发出的SYN包多于该指定数，就判断为受到
了SYN Flood攻击。默认值是1500个。取值范围是0到50000个。0表示不对源警戒值进行检测。使用
no ad syn-flood source-threshold命令恢复默认值。
l
destination-threshold [ip-based | port-based] number – 指定一秒钟内同一个目的IP地址（ipbased）或者同一目的IP的同一个目的端口（port-based）收到的SYN包个数，若不指定，则默认为
ip-based。如果设备探测到一秒钟同一个目的IP地址或者同一目的IP的同一个目的端口收到的SYN包多

<!-- 来源页 2119 -->
于该指定数，就认为是受到了SYN Flood攻击。默认值是1500个。取值范围是0到50000个。0表示不
对目的警戒值进行检测。使用no ad syn-flood destination-threshold [ip-base | port-base]命令
恢复默认值。
l
destination [ip-based | port-based [address-book address-entry | A.B.C.D/M] – 开启基于目
的IP地址（ip-based）或者目的端口（port-based）的SYN Flood攻击防护功能，若不指定，则默认
为ip-based。使用address-book address-entry | A.B.C.D/M参数，指定开启特定网段的基于目的
端口的SYN Flood攻击防护功能，其它网段做基于目的IP地址的SYN Flood攻击防护。目的IP地址掩码
取值范围是24到32。使用no ad syn-flood destination命令取消相应配置。
l
action {alarm | drop} – 指定设备对于SYN Flood攻击采取的行为。alarm– 发出警报但是允许包通
过；drop – 设备仅允许指定个数（source-threshold number | destination-threshold
number）的SYN包通过，并且发出警报；如果同时配置了源和目的警戒值，系统会先检查其是否为目
的SYN Flood攻击，如果是，则丢弃并报警，如果不是，再检查其是否为源SYN Flood攻击，是则丢弃
并报警。默认行为是drop。使用no ad syn-flood action恢复默认操作。
配置SYN-Proxy功能
设备还提供SYN-Proxy功能配合ad syn-flood命令来共同防护SYN Flood攻击。当ad syn-flood和SYNProxy功能都开启时，SYN-Proxy功能对已经通过ad syn-flood检测的数据包起效。
设备支持SYN-Cookie功能。SYN-Cookie是一种无状态的SYN-Proxy机制。
配置安全域的SYN-Proxy以及SYN-Cookie功能，在安全域配置模式下使用以下命令：
ad syn-proxy [min-proxy-rate number | max-proxy-rate number | proxy-timeout number |
cookie [hardware-offload-disable]]
l
ad syn-proxy – 开启安全域的SYN-Proxy功能用以防护SYN Flood攻击。使用no ad syn-proxy关
闭该功能。
l
min-proxy-rate number –指定激活SYN-Proxy机制或者SYN-Cookie机制（通过cookie参数开启
SYN-Cookie功能后）的最小SYN包个数值。如果一个目的IP地址的同一个端口在一秒钟内收到的SYN
包个数多于该参数的指定值，就会激活SYN-Proxy或者SYN-Cookie机制。number默认值是1000个每
秒，取值范围是0到50000。使用no ad syn-proxy min-proxy-rate恢复默认值。
l
max-proxy-rate number – 指定SYN-Proxy机制或者SYN-Cookie机制（通过cookie参数开启SYNCookie功能后）在指定时间内允许通过的最大SYN包个数。如果一个目的IP地址的同一个端口在一秒钟
内收到的SYN包个数多于该参数的指定值，设备会在当前秒和下一秒内仅允许该指定数值的SYN包通

<!-- 来源页 2120 -->
过，其它同类包将会被丢弃。number默认值是3000个每秒，取值范围是1到1500000。使用no ad
syn-proxy max-proxy-rate命令恢复默认值。
l
proxy-timeout number – 指定半连接的超时时间值。半连接达到该超时值后会被丢弃。默认值是
30，单位为秒，取值范围是1到180秒。使用no ad syn-proxy proxy-timeout命令恢复默认值。
l
cookie – 开启SYN-Cookie功能（如果需要开启该功能，请先开启SYN-Proxy功能）。该功能开启后，
能够在功能上扩大设备处理多个SYN包的能力，因此用户可以适当的增大min-proxy-rate和maxproxy-rate两个参数之间的范围。使用no ad syn-proxy cookie命令关闭SYN-Cookie功能。
l
hardware-offload-disable – 关闭SYN Cookie硬件加速功能（开启SYN-Cookie功能后，系统默认
开启SYN Cookie硬件加速功能）。触发SYN Cookie硬件加速功能后，将由专门的硬件芯片处理SYN报
文，从而降低CPU的资源消耗，提升安全防护效果。使用no ad syn-proxy cookie hardwareoffload-disable命令开启SYN Cookie硬件加速功能。
注意:
l
仅K20803、K7680、A7600支持SYN Cookie硬件加速功能。
l
开启SYN Cookie硬件加速后，max-proxy-rate（最大代理速率）将不生效。在达到minproxy-rate（最小代理速率）后，系统将对SYN报文进行SYN-Cookie处理。
l
触发SYN Cookie硬件加速后，由于SYN报文不上送至CPU进行处理，所以系统将无法进行
SYN洪水攻击防护阈值学习。
l
SYN Cookie硬件加速不支持IP验证功能。IP验证功能参见“威胁防护> 攻击防护> 配置攻击
防护功能”章节。
配置SIP Flood攻击防护功能
用户可以单独开启或者关闭安全域的SIP Flood攻击防护功能，也可以配置SIP报文个数的警戒值以及设备采
取的操作。配置设备的SIP Flood攻击防护功能，在安全域配置模式下使用以下命令：
ad sip-flood [destination-threshold number | action {alarm | drop}]
l
ad sip-flood– 开启安全域的SIP Flood攻击防护功能。使用no ad sip-flood关闭该功能。
l
[destination-threshold number– 指定设备收到的目的地址相同的SIP INVITE报文的个数的警戒
值。即如果一秒钟内设备收到的到达同一个目的IP地址的SIP INVITE报文个数超过该警戒值，设备就判
断为受到SIP洪水攻击，从而采取相应的处理措施。number的默认值是2000个，取值范围是0到
800000000。使用no ad sip-flood destination-threshold恢复默认值。

<!-- 来源页 2121 -->
l
action {alarm | drop}]– 指定设备受到SIP洪水攻击而进行的处理行为。系统将在检测到发生攻击的下
一秒内，检查后续源IP地址主机是否存在真实SIP客户端，如果存在，则允许该源IP之后发送的SIP
INVITE报文通过；如果不存在，则攻击发生后3秒内对该源IP发送的SIP INVITE报文按照配置行为处
理，包括丢弃INVITE报文（drop）或者发出警报但允许INVITE报文通过（alarm）。默认行为是
drop。使用no ad sip-flood action恢复默认操作。
配置ICMP Flood攻击防护功能
用户可以单独开启或者关闭安全域的ICMP Flood攻击防护功能，也可以配置ICMP包个数的警戒值以及设备
采取的操作。配置设备的ICMP Flood攻击防护功能，在安全域配置模式下使用以下命令：
ad icmp-flood [threshold number | action {alarm | drop}]
l
ad icmp-flood – 开启安全域的ICMP Flood攻击防护功能。使用no ad icmp-flood关闭该功能。
l
threshold number – 指定设备收到的ICMP包的个数的警戒值。如果同一个目的IP地址在一秒钟内收到
的ICMP包的个数超过该警戒值，设备就判断为受到ICMP Flood攻击，从而采取相应的处理。number
的默认值是1500个，取值范围是1到50000。使用no ad icmp-flood threshold恢复默认值。
l
action {alarm | drop} – 指定设备对于ICMP Flood攻击采取的行为。alarm– 发出警报但是允许包通
过；drop–在发生攻击的当前秒和下一秒这段时间内，设备仅允许指定个数（threshold number）的
ICMP包通过，并且发出警报，在这段时间内的其它同类包将会被丢弃。默认行为是drop。使用no ad
icmp-flood action恢复默认操作。
配置UDP Flood攻击防护功能
用户可以单独开启或者关闭安全域的UDP Flood攻击防护功能，也可以配置UDP包个数的警戒值以及设备采
取的操作。配置设备的UDP Flood攻击防护功能，在安全域配置模式下使用以下命令：
ad udp-flood [session-state-check [source-threshold number | destination-threshold
number | action {alarm | drop}] | source-threshold number | destination-threshold number |
action {alarm | drop} | hardware-offload-disable]
l
ad udp-flood – 开启安全域的UDP Flood攻击防护功能。使用no ad udp-flood关闭该功能。
l
session-state-check – 开启会话状态检查功能。开启后，系统将对识别到会话的UDP报文的回包流量
不做UDP Flood攻击的检查。使用no ad udp-flood session-state-check关闭该功能，即默认对所
有UDP报文都做UDP Flood攻击的检查。
l
source-threshold number – 指定设备发送的UDP包的个数的警戒值。如果同一个源IP地址在一秒钟
内发送的UDP包的个数超过该警戒值，设备就判断为受到UDP Flood攻击，从而采取相应的处理。

<!-- 来源页 2122 -->
number的默认值是1500个，取值范围是0到300000。使用no ad udp-flood source-threshold恢
复默认值。
l
destination-threshold number –指定设备收到的UDP包的个数的警戒值。如果同一个目的IP地址的
同一个端口号在一秒钟内收到的UDP包的个数超过该警戒值，设备就判断为受到UDP Flood攻击，从而
采取相应的处理。number的默认值是1500个，取值范围是0到300000。使用no ad udp-flood
destination-threshold恢复默认值。
l
action {alarm | drop} – 指定设备对于UDP Flood攻击采取的行为。alarm– 发出警报但是允许包通
过；drop–在发生攻击的当前秒和下一秒这段时间内，设备仅允许指定个数（source-threshold
number | destination-threshold number）的UDP包通过，并且发出警报，在这段时间内的其它同
类包将会被丢弃。默认行为是drop。使用no ad udp-flood action恢复默认操作。
l
hardware-offload-disable – 关闭硬件加速功能，该功能默认为开启状态。开启硬件加速功能后，将
由专门的硬件芯片处理UDP报文，从而降低CPU的资源消耗，提升安全防护效果。使用no ad udpflood hardware-offload-disable命令开启硬件加速功能。仅K20803、K7680、A7600支持硬件加
速功能。
配置HTTPS Flood攻击防护功能
HTTPS Flood攻击是一种针对HTTPS加密协议服务的分布式拒绝服务（DDoS）攻击，其核心目标是通过向
目标服务器发送大量伪造或半合法的HTTPS请求，耗尽服务器的CPU、内存、网络带宽等关键资源，最终导
致服务器无法正常处理合法用户的HTTPS请求，造成服务中断或响应极度缓慢。用户可以单独开启或者关闭
安全域的HTTPS Flood攻击防护功能，也可以配置HTTPS报文个数的警戒值以及设备采取的处理动作。
注意: HTTPS Flood攻击防护功能仅对端口号为443的HTTPS报文有效。
配置设备的HTTPS Flood攻击防护功能，在安全域配置模式下，使用以下命令：
ad https-flood [destination-threshold number | action {alarm | drop}]
l
ad https-flood – 开启安全域的HTTPS Flood攻击防护功能。该功能默认为关闭状态。
l
destination-threshold number – 指定设备收到的目的地址相同的HTTPS报文个数的警戒值。如果一
秒钟内设备收到的到达同一个目的IP地址的HTTPS报文个数超过该警戒值，设备就判断为受到HTTPS洪
水攻击，从而采取相应的处理动作。取值范围为0-300000个/秒，默认为2000个/秒。
l
action {alarm | drop} – 指定设备受到HTTPS洪水攻击而采取的处理动作。指定alarm为发出警报但
是允许报文通过；指定drop则在发生攻击的当前秒和下一秒这两秒时间内，设备仅允许指定个数

<!-- 来源页 2123 -->
（destination-threshold number）的HTTPS报文通过，并且发出警报，在这段时间内超出上限的其
它同类报文将会被丢弃。若不指定，默认处理动作为drop。
恢复HTTPS Flood攻击防护功能的默认警戒值，在安全域配置模式下，使用以下命令：
no ad https-flood destination-threshold
恢复HTTPS Flood攻击防护功能的默认处理动作，在安全域配置模式下，使用以下命令：
no ad https-flood action
关闭HTTPS Flood攻击防护功能，在安全域配置模式下，使用以下命令：
no ad https-flood
配置Flood防护阈值学习功能
针对Flood攻击，系统支持Flood防护阈值学习功能，通过统计各种正常业务流量数据，进行检测阈值的智
能学习，得到各种攻击流量类型对应的合理阈值，为攻击检测阈值提供合理参考。配置设备的Flood防护阈
值学习功能，包括配置Flood防护阈值学习参数和开启Flood防护阈值学习。
注意: 智能学习前，需要将Flood 类攻击的防御阈调整至较大数值，确保不会对当前业务流量造成
影响，防止学习结果异常。
配置Flood防护阈值学习参数
配置Flood防护阈值学习参数，请在安全域模式下使用以下命令：
ad threshold-learning {duration {day | hour | minute} number | learn-mode {one-time |
periodic {day | hour | minute} number} apply-mode {manual | auto} coefficient {default |
loose | strict | userdefine number}}
l
duration {day | hour | minute} number– 指定Flood防护阈值学习的学习时间，单位可以是
“天”、“小时”和“分钟”。使用no ad threshold-learning duration恢复默认学习时间。
l
day– 指定学习时间单位为“天”，取值范围是1到365天，默认是1天。
l
hour– 指定学习时间单位为“小时”，取值范围是1到8760小时，默认是1小时。
l
minute– 指定学习时间单位为“分钟”，取值范围是10-525600分钟，即学习时间不能小于10
分钟，默认是1440分钟。
l
learn-mode {one-time | periodic {day | hour | minute} number– 指定Flood防护阈值学习的学
习类型，可以是单次学习或周期学习。默认是单次学习。使用no ad threshold-learning learn-

<!-- 来源页 2124 -->
mode恢复默认学习类型。
l
one-time– 指定学习类型为单次学习，单次学习只进行一次学习任务，结束后自动停止学习任
务。
l
periodic {day | hour | minute} number– 指定学习类型为周期学习，周期学习按照指定周期
进行循环学习，需要手动停止学习任务。当指定学习类型为周期学习时，还需指定周期学习间隔。
周期间隔是指从上次学习结束到下次学习开始开始之间的间隔时间。单位可以是“天”、“小时”
和“分钟”。
l
day– 指定学习时间单位为“天”，取值范围是1到365天，默认是7天。
l
hour– 指定学习时间单位为“小时”，取值范围是1到8760小时，默认是1小时。
l
minute– 指定学习时间单位为“分钟”，取值范围是10-525600分钟，即学习时间不能
小于10分钟，默认是1440分钟。
l
apply-mode {manual | auto}– 指定Flood防护阈值学习结果的应用模式，可以是“手动应用”或者
“自动应用”。默认是手动应用。使用no ad threshold-learning apply-mode恢复默认应用类型。
l
manual– 指定应用模式为手动应用，根据需要将阈值学习结果应用至相应的Flood攻击防护项的
警戒值配置中。
l
auto– 指定应用模式为自动应用，所有已开启的Flood攻击防护项的警戒值将自动配置为学习完
成后的阈值结果并进行下发。
l
coefficient {predefine {default | loose | strict} | userdefine number}– 最终的阈值学习结果=学
习时间内的最大流量速率*阈值系数。指定Flood防护阈值学习的阈值学习系数，其单位为百分比。使用
no ad threshold-learning coefficient恢复默认阈值学习系数。
l
default – 指定默认阈值学习系数200。
l
loose– 指定宽松阈值学习系数4000。
l
strict– 指定严格阈值学习系数100。
l
userdefine number– 指定自定义阈值学习系数，取值范围是100到4000。
应用Flood防护阈值学习结果
应用Flood防护阈值学习结果，在任意模式下，使用以下命令：
exec ad-threshold-learning apply {icmp-flood | sip-flood | https-flood | {udp-flood | dnsquery-flood | dns-query-recursion-flood | dns-reply-flood} {source-threshold | destination-

<!-- 来源页 2125 -->
threshold} | syn-flood {source-threshold | destination-threshold | destination-thresholdport}} zone zone-name
l
icmp-flood | sip-flood | https-flood | udp-flood | dns-query-flood | dns-query-recursionflood | dns-reply-flood | syn-flood - 指定应用ICMP洪水攻击防护阈值学习结果、SIP洪水攻击防护
阈值学习结果、HTTPS洪水攻击防护阈值学习结果、UDP洪水攻击防护阈值学习结果、DNS查询洪水攻
击防护阈值学习结果、DNS递归查询洪水攻击防护阈值学习结果、DNS响应洪水攻击防护阈值学习结
果、SYN洪水攻击防护阈值学习结果。
l
source-threshold | destination-threshold | destination-threshold-port - 指定应用源IP阈值
学习结果、目的IP阈值学习结果、目的端口阈值学习结果。
l
zone zone-name – 指定已开启Flood攻击防护功能的安全域的名称。
开启/停止Flood防护阈值学习
开始/停止Flood防护阈值学习，在任意模式下，使用以下命令：
exec ad-threshold-learning {start | stop} zone zone-name
l
start – 开始Flood防护阈值学习。
l
stop – 停止正在进行的Flood防护阈值学习。
l
zone zone-name – 指定已开启Flood攻击防护功能的安全域的名称。
配置Huge ICMP包攻击防护功能
用户可以单独开启或者关闭安全域的Huge ICMP攻击防护功能，也可以配置ICMP包的大小的警戒值以及设
备采取的行为。配置设备的Huge ICMP报攻击防护功能，在安全域配置模式下使用以下命令：
ad huge-icmp-pak [threshold number | action {alarm | drop}]
l
ad huge-icmp-pak – 开启安全域的Huge ICMP包攻击防护功能。使用no ad huge-icmp-pak关闭
该功能。
l
threshold number – 指定ICMP包的大小的警戒值。如果收到的ICMP包的大小大于该指定值，设备就
判断为受到Huge ICMP包攻击，从而采取相应的处理措施。number默认值是1024字节，取值范围是1
到50000字节。使用no ad huge-icmp-pak threshold恢复默认值。
l
action {alarm | drop} – 指定设备对于Huge ICMP包攻击采取的行为。alarm– 发出警报但是允许包
通过；drop– 发出警报并且丢弃攻击包。默认行为是drop。使用no ad udp-flood action恢复默认操
作。

<!-- 来源页 2126 -->
配置WinNuke攻击防护功能
WinNuke攻击防护功能开启后，当设备发现受到WinNuke攻击后，会丢弃攻击包并且发出警报通知。开启
安全域的WinNuke攻击防护功能，在安全域配置模式使用以下命令：
ad winnuke
在安全域配置模式下，使用no ad winnuke关闭安全域的WinNuke攻击防护功能。
配置Ping of Death攻击防护功能
Ping of Death攻击防护功能开启后，当设备发现受到Ping of Death攻击后，会丢弃攻击包并且发出警报
通知。开启安全域的Ping of Death攻击防护功能，在安全域配置模式使用以下命令：
ad ping-of-death
在安全域配置模式下，使用no ad ping-of-death关闭安全域的Ping of Death攻击防护功能。
配置Teardrop攻击防护功能
Teardrop攻击防护功能开启后，当设备发现受到Teardrop攻击后，会丢弃攻击包并且发出警报通知。开启
安全域的Teardrop攻击防护功能，在安全域配置模式使用以下命令：
ad tear-drop
在安全域配置模式下，使用no ad tear-drop关闭安全域的Teardrop攻击防护功能。
配置IP Option攻击防护功能
IP Option攻击防护功能开启后，默认情况下当设备发现受到IP Option攻击后，会丢弃攻击包并且发出警报
通知。用户可以根据需要改变设备的行为。设备会对以下IP Option类型进行防护：Security、Loose
Source Route、Record Route、Stream ID、Strict Source Route和Timestamp。配置IP Option攻
击防护功能，在安全域配置模式使用以下命令：
ad ip-option [action {alarm | drop}]
l
ad ip-option – 开启安全域的IP Option攻击防护功能。使用no ad ip-option命令关闭该功能。
l
action {alarm | drop} – 指定设备对于IP Option攻击采取的行为。alarm– 发出警报但是允许包通
过；drop– 发出警报并且丢弃攻击包。默认行为是drop。使用no ad ip-option action恢复默认行
为。
配置TCP异常攻击防护功能
TCP异常攻击防护功能开启后，默认情况下当设备发现受到TCP异常攻击后，会丢弃攻击包并且发出警报通
知。用户可以根据需要改变设备的行为。当设备检测到以下各种情况，就会判断为受到TCP异常攻击：

<!-- 来源页 2127 -->
l
SYN包被分片
l
TCP Flag异常攻击：
l
TCP包仅设置了FIN flag；
l
TCP包仅没有设置flag；
l
TCP包的FIN和RST flag同时被设置；
l
TCP包的SYN和URG flag同时被设置；
l
TCP包的SYN和RST flag同时被设置；
l
TCP包的SYN和FIN flag同时被设置。
配置TCP异常攻击防护功能，在安全域配置模式使用以下命令：
ad tcp-anomaly [action {alarm | drop}]
l
ad tcp-anomaly – 开启安全域的TCP异常攻击防护功能。使用no ad tcp-anomaly命令关闭该功
能。
l
action {alarm | drop} – 指定设备对于TCP异常攻击采取的行为。alarm– 发出警报但是允许包通
过；drop– 发出警报并且丢弃攻击包。默认行为是drop。使用no ad tcp-anomaly action恢复默认
操作。
配置Land攻击防护功能
Land攻击防护功能开启后，默认情况下当设备发现受到Land攻击后，会丢弃数据包并且发出警报通知。用
户可以根据需要改变设备的行为。配置Land攻击防护功能，在安全域配置模式使用以下命令：
ad land-attack [action {alarm | drop}]
l
ad land-attack – 开启安全域的Land攻击防护功能。使用no ad land-attack命令关闭该功能。
l
action {alarm | drop} – 指定设备对于Land攻击采取的行为。alarm– 发出警报但是允许包通
过；drop– 发出警报并且丢弃攻击包。默认行为是drop。使用no ad land-attack action恢复默认操
作。
配置IP 碎片攻击防护功能
数据包在不同网络间进行传输时，有时需要根据网络的MTU值将数据包分片。攻击者可以通过修改IP碎片在
重组过程中发现漏洞进行攻击。当被攻击方收到被修改过的IP碎片后，轻则不能正确重组碎片，重则导致整
个系统崩溃。

<!-- 来源页 2128 -->
默认情况下当设备发现受到IP碎片攻击后，会丢弃攻击包并且发出警报通知。用户可以根据需要改变设备的
行为。配置IP 碎片攻击防护功能，在安全域配置模式使用以下命令：
ad ip-fragment [action {alarm | drop}]
l
ad ip-fragment – 开启安全域的IP碎片攻击防护功能。使用no ad ip-fragment命令关闭该功能。
l
action {alarm | drop} – 指定设备对于IP碎片攻击采取的行为。alarm– 发出警报但是允许包通
过；drop– 发出警报并且丢弃攻击包。默认行为是drop。使用no ad ip-fragment action恢复默认操
作。
配置Smurf和Fraggle攻击防护功能
Smurf和Fraggle攻击防护功能开启后，默认情况下当设备发现受到Smurf或者Fraggle攻击后，会丢弃数
据包并且发出警报通知。用户可以根据需要改变设备的行为。配置Smurf和Fraggle攻击防护功能，在安全
域配置模式下使用以下命令：
ad ip-directed-broadcast [action {alarm | drop}]
l
ad ip-directed-broadcast – 开启安全域的Smurf和Fraggle攻击防护功能。使用no ad ipdirected-broadcast命令关闭该功能。
l
action {alarm | drop} – 指定设备对于Smurf和Fraggle攻击采取的行为。alarm– 发出警报但是允许
包通过；drop– 发出警报并且丢弃所有包。默认行为是drop。使用no ad ip-directed-broadcast
action恢复默认操作。
配置ARP欺骗防护功能
设备的ARP欺骗防护功能能够保护内网不受ARP欺骗攻击。配置ARP欺骗防护功能，在安全域配置模式使用
以下命令：
ad arp-spoofing {reverse-query | ip-number-per-mac number [action [drop | alarm]] |
gratuitous-arp-send-rate number}
l
reverse-query – 开启ARP反向查询功能。当设备收到ARP请求后，会记录IP地址并且发送ARP请求，
检查是否会收到不同MAC地址的返回包或者返回包的MAC地址与ARP请求包的MAC地址是否相同。使用
no ad arp-spoofing reverse-query 命令关闭ARP反向查询功能。
l
ip-number-per-mac number – 指定ARP表中每个MAC地址对应的IP地址数的阈值。范围是1-
1024，默认值为100。指定后，若一个MAC地址在30秒内对应的IP地址数超过该阈值，系统将按照
action [drop | alarm]参数的配置进行处理，处理行为可以是发出警报并且丢弃该ARP包（drop）或

<!-- 来源页 2129 -->
者发出警报但是允许包通过（alarm）。使用no ad arp-spoofing ip-number-per-mac命令恢复默
认值。
l
gratuitous-arp-send-rate number– 指定设备每秒钟发出Gratuitous ARP包的个数。范围是1到
10，默认值为10。使用no ad arp-spoofing gratuitous-arp-send-rate命令恢复默认值。
配置ARP Flood攻击防护功能
ARP Flood攻击是指利用ARP协议的广播特性，通过发送大量伪造的ARP请求或响应报文，对目标网络设备
进行攻击。这些伪造的ARP报文可能包含错误的IP-MAC映射关系，设备获取后将导致通信失败。此外，大
量的ARP伪造报文会大大占用系统资源，导致系统业务无法正常运行。用户可以通过ARP Flood攻击防护功
能，对ARP流量进行限流，当设备收到的ARP报文达到告警阈值时，设备将丢弃超过上限的ARP报文。
配置ARP Flood攻击防护功能，在安全域配置模式下，使用以下命令：
ad arp-flood [threshold number | action {alarm | drop}]
l
ad arp-flood - 开启安全域的ARP Flood攻击防护功能。该功能默认为关闭状态。
l
threshold number - 指定设备收到的ARP报文个数的警戒值。如果设备在一秒钟内收到的ARP报文的
个数超过指定的警戒值，设备就会判断为受到ARP Flood攻击，从而采取相应的处理动作。取值范围为
1-300000个/秒，默认为1500个/秒。
l
action {alarm | drop} - 指定设备对于ARP Flood攻击采取的处理动作。指定alarm为发出警报但是
允许报文通过；指定drop则在发生攻击的当前秒和下一秒这两秒时间内，设备仅允许指定个数
（threshold number）的ARP报文通过，并且发出警报，在这段时间内超出上限的其它同类报文将会
被丢弃。若不指定，默认处理动作为drop。
恢复ARP Flood攻击防护功能的默认警戒值，在安全域配置模式下，使用以下命令：
no ad arp-flood threshold
恢复ARP Flood攻击防护功能的默认处理动作，在安全域配置模式下，使用以下命令：
no ad arp-flood action
关闭ARP Flood攻击防护功能，在安全域配置模式下，使用以下命令：
no ad arp-flood
配置DNS Query Flood攻击防护功能
DNS是域名系统（Domain Name System）的简称，用来实现域名转换为IP地址和IP地址解析为域名。
DNS是应用层协议，既可以基于TCP连接也可以基于UDP连接，DNS Query Flood攻击主要是指基于UDP
的DNS查询报文洪水攻击。

<!-- 来源页 2130 -->
DNS Query Flood攻击采用的方法是向被攻击的DNS服务器发送大量的域名解析请求，通常请求解析的域
名是随机生成或者是网络上根本不存在的域名。被攻击的DNS服务器在接收到域名解析请求时，首先会在服
务器上查找是否有对应的缓存，如果查找不到并且该域名无法直接由服务器解析时，DNS服务器会向其上层
DNS服务器递归查询域名信息。域名解析的过程给服务器带来了很大的负载，每秒钟域名解析请求超过一定
的数量就会造成DNS服务器解析域名超时。
设备支持DNS Query Flood攻击防护功能，用户可以单独开启或者关闭安全域的DNS Query Flood攻击防
护功能，也可以配置DNS查询报文个数的警戒值以及设备采取的操作。配置设备的DNS Query Flood攻击
防护功能，在安全域配置模式下使用以下命令：
ad dns-query-flood [recursion] [source-threshold number] [destination-threshold number |
action {alarm | drop}]
l
ad dns-query-flood – 开启安全域的DNS Query Flood攻击防护功能。使用no ad dns-queryflood关闭该功能。
l
recursion – 指定仅限制DNS递归查询报文。当不设置此选项时，表示限制所有DNS查询报文。
l
source-threshold number – 指定设备发送的DNS查询报文或DNS递归查询报文的个数的警戒值。如
果一秒钟内同一个源IP地址发送的DNS查询报文个数超过该警戒值，设备就判断为受到DNS Query
Flood攻击，从而采取相应的处理措施。number的默认值是1500个，取值范围是0到300000。使用
no ad dns-query-flood source-threshold恢复默认值。
l
destination-threshold number – 指定设备收到的DNS查询报文或DNS递归查询报文的个数的警戒
值。如果一秒钟内设备收到的到达同一个目的IP地址的DNS查询报文个数超过该警戒值，设备就判断为
受到DNS Query Flood攻击，从而采取相应的处理措施。number的默认值是1500个，取值范围是0到
300000。使用no ad dns-query-flood destination-threshold恢复默认值。
l
action {alarm | drop} – 指定设备对DNS Query Flood攻击采取的行为。alarm–发出警报但是允许
DNS查询报文通过；drop–在发生攻击的当前秒和下一秒这段时间内，设备仅允许指定个数
（threshold number）的DNS查询报文或DNS递归查询报文通过，并且发出警报，在这段时间内的其
它同类包将会被丢弃。默认行为是drop。使用no ad dns-flood action恢复默认操作。
注意: DNS Query Flood攻击防护功能仅对UDP DNS查询报文有效。
配置DNS Reply Flood攻击防护功能
设备支持DNS响应洪水攻击防护功能，用户可以单独开启或者关闭安全域的DNS Reply Flood攻击防护功
能，也可以配置DNS响应报文个数的警戒值以及设备采取的操作。配置设备的DNS Reply Flood攻击防护
功能，在安全域配置模式下使用以下命令：

<!-- 来源页 2131 -->
ad dns-reply-flood [ source-threshold number ] [ destination-threshold number | action {
alarm | drop }]
l
ad dns-reply-flood – 开启安全域的DNS Reply Flood攻击防护功能。使用no ad dns-replyflood关闭该功能。
l
source-threshold number – 指定设备发送的DNS响应报文的个数的警戒值。如果一秒钟内同一个源
IP地址发送的DNS响应报文个数超过该警戒值，设备就判断为受到DNS Reply Flood攻击，从而采取相
应的处理措施。number的默认值是1500个，取值范围是0到300000。使用no ad dns-reply-flood
source-threshold恢复默认值。
l
destination-threshold number – 指定设备收到的DNS响应报文的个数的警戒值。如果一秒钟内设备
收到的到达同一个目的IP地址的DNS响应报文个数超过该警戒值，设备就判断为受到DNS Reply Flood
攻击，从而采取相应的处理措施。number的默认值是1500个，取值范围是0到300000。使用no ad
dns-reply-flood destination-threshold恢复默认值。
l
action {alarm | drop} – 指定设备对DNS Reply Flood攻击采取的行为。alarm–发出警报但是允许
DNS响应报文通过；drop–在发生攻击的当前秒和下一秒这段时间内，设备仅允许指定个数
（threshold number）的DNS响应报文通过，并且发出警报，在这段时间内的其它同类包将会被丢
弃。默认行为是drop。使用no ad dns-flood action恢复默认操作。
注意: DNS Reply Flood攻击防护功能仅对UDP DNS响应报文有效。
配置攻击防护源认证功能
开启攻击防护源认证功能后，系统在检测到泛洪攻击流量时会启用动态源认证机制，通过认证的源在限定时
间内将直接放行，从而保障业务流量稳定。
开启攻击防护源认证功能
开启攻击防护源认证功能，在全局配置模式下，使用以下命令：
ad-ip-certified {dns-query-flood | dns-query-flood-recursion | dns-reply-flood | https-flood
| syn-cookie | syn-proxy}
l
dns-query-flood | dns-query-flood-recursion | dns-reply-flood | https-flood | syn-cookie
| syn-proxy - 开启指定类型的攻击防护源认证功能，包括DNS查询洪水攻击防护（dns-queryflood）、DNS递归查询洪水攻击防护（dns-query-flood-recursion）、DNS响应洪水攻击防护

<!-- 来源页 2132 -->
（dns-reply-flood）、HTTPS洪水攻击防护（https-flood）、SYN Proxy功能（syn-proxy）、
SYN Cookie功能（syn-cookie）。
关闭攻击防护源认证功能，在全局配置模式下使用以下命令：
no ad-ip-certified {dns-query-flood | dns-query-flood-recursion | dns-reply-flood | httpsflood | syn-cookie | syn-proxy}
配置攻击防护源认证名单的超时时间
配置攻击防护源认证名单的超时时间，超过指定时间的已通过认证和未通过认证的条目将被删除，系统将重
新进行认证。
配置超时时间，在全局配置模式下，使用以下命令：
ad-ip-certified timeout timeout-value
l
timeout-value - 指定攻击防护源认证名单的超时时间，取值范围是60到86400秒，默认值是3600
秒。
使用no ad-ip-certified timeout恢复默认值。
显示攻击防护源认证名单
显示攻击防护源认证名单，在任意模式下，使用以下命令：
show ad ip-certified [ad-type { dns-query-flood | dns-query-flood-recursion | dns-replyflood | sip-flood | syn-cookie | syn-proxy} | ip-address {A.B.C.D | X:X:X:X::X} | state {certified
| uncertified | wait-certified}]
l
ad-type { dns-query-flood | dns-query-flood-recursion | dns-reply-flood | sip-flood |
syn-cookie | syn-proxy} - 显示指定类型的攻击防护源认证名单。
l
ip-address {A.B.C.D | X:X:X:X::X} - 显示指定IP地址的攻击防护源认证名单，支持IPv4地址和IPv6
地址。
l
state {certified |uncertified | wait-certified} - 显示指定验证状态的攻击防护源认证名单。
显示攻击防护源认证功能配置信息
显示攻击防护源认证功能配置信息，包括启用状态和超时时间，在任意模式下使用以下命令：
show ad ip-certified configuration
以下是返回结果示例。若部分返回结果为空，则表示未开启对应的攻击防护源认证功能。
hostname# show ad ip-certified configuration

<!-- 来源页 2133 -->
ad ip-certified https-flood （已启用HTTPS洪水攻击防护的源认证功能）
ad ip-certified dns-query-flood （已启用DNS查询洪水攻击防护的源认证功能）
ad ip-certified dns-reply-flood （已启用DNS响应洪水攻击防护的源认证功能）
ad ip-certified timeout: 3600s （IP验证名单的超时时间为3600秒）
配置TCP Split Handshake攻击防护功能
TCP Split Handshake攻击防护功能开启后，默认情况下当设备发现受到此类型攻击后，会丢弃数据包并且
发出警报通知。用户可以根据需要改变设备的行为。配置TCP Split Handshake攻击防护功能，在安全域配
置模式使用以下命令：
ad tcp-split-handshake [action {alarm | drop}]
l
ad tcp-split-handshake – 开启安全域的TCP Split Handshake攻击防护功能。使用no ad tcpsplit-handshake命令关闭该功能。
l
action {alarm | drop} – 指定设备对于TCP Split Handshake攻击采取的行为。alarm发出警报但是
允许包通过；drop发出警报并且丢弃攻击包。默认行为是drop。使用no ad land-attack action恢
复默认操作。
配置攻击防护白名单
开启攻击防护功能后，安全域中的所有流量都会受到攻击防护功能的检查。在实际应用中，用户可能出于测
试等目的不希望对某些主机所发送的流量进行检查。针对这种情况，用户可以将特定的地址或地址范围（源
地址或者目的地址）添加到攻击防护白名单，支持IPv4地址和IPv6地址。白名单中的地址或地址范围不受攻
击防护功能的检查。
配置攻击防护白名单，在安全域配置模式下，使用以下命令：
ad allowlist [id id] {source-ip | destination-ip} {IPv4-address/M | IPv6-address/prefix |
address-entry}
l
id – 指定白名单规则的ID。各设备型号ID取值范围不同。如果不指定，系统将自动为该条规则分配一个
ID。
l
source-ip | destination-ip- 指定白名单中的地址类型：源地址（source-ip）或者目的地址
（destination-ip）。
l
IPv4-address/M–指定添加到白名单规则中的IPv4地址和网络掩码。
l
IPv6-address/prefix - 指定添加到白名单规则中的IPv6地址和前缀长度，取值范围为120至128。
l
address-entry–指定添加到白名单规则中的地址条目。
使用该命令no的形式删除指定的白名单规则：

<!-- 来源页 2134 -->
no ad allowlist [id id] {source-ip | destination-ip}{IPv4-address/M | IPv6-address/prefix |
address-entry}
显示安全域的攻击防护配置和统计信息
系统能够显示安全域的攻击防护配置和统计信息。显示安全域的攻击防护配置和统计信息，在任何模式下使
用以下命令：
show ad zone zone-name {statistics | configuration | allowlist | threshold-clearning
{configuration | status | result}}
l
zone-name – 指定安全域的名称。
l
statistics – 显示指定安全域的统计信息。
l
configuration – 显示指定安全域的攻击防护配置信息。
l
allowlist – 显示指定安全域的攻击防护白名单配置信息。
l
threshold-clearning {configuration | status | result}– 显示指定安全域的Flood防护阈值学习配
置（configuration）、学习状态（status）和学习结果（result）信息。
例：攻击防护配置举例
本节介绍攻击防护的配置举例以帮助用户更好的理解与配置设备的攻击防护功能。
Land攻击防护功能配置举例
本小节介绍Land攻击防护功能的配置实例。
组网需求
将设备的以太网口ethernet 0/0配置为Trust域，以太网口ethernet 0/2配置为Untrust域，以太网口
ethernet 0/1配置为DMZ域。需要对DMZ域内的服务器进行Land攻击防护。下图为该需求的组网图：

<!-- 来源页 2135 -->
配置步骤
第一步：配置设备接口ethernet0/0。
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 192.168.1.1/24
hostname(config-if-eth0/0)# exit
hostname(config)#
第二步：配置设备接口ethernet0/2。
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# zone untrust
hostname(config-if-eth0/2)# ip address 202.1.0.1/24
hostname(config-if-eth0/2)# exit
hostname(config)#
第三步：配置设备接口ethernet0/1。
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone dmz
hostname(config-if-eth0/1)# ip address 10.0.0.1/8

<!-- 来源页 2136 -->
hostname(config-if-eth0/1)# exit
hostname(config)#
第四步：配置策略规则。
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zone dmz
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config)#
第五步：开启untrust域的Land攻击防护功能。
hostname(config)# zone untrust
hostname(config-zone)# ad land-attack
hostname(config-if)# exit
hostname(config)#
第六步：检测对服务器10.110.1.1配置的Land攻击防护功能。给报文设置相同的源IP和目的IP地址，向
10.110.1.1发送。设备检测到Land攻击，并报警。
SYN Flood攻击防护功能配置举例
本小节介绍SYN Flood攻击防护功能的配置实例。
组网需求
将设备的以太网口ethernet0/0配置为Trust域，以太网口ethernet0/2配置为Untrust域，以太网口
ethernet0/1配置为DMZ域。需要对DMZ域内的服务器进行SYN Flood攻击防护。
配置步骤
第一步：配置设备接口ethernet0/0。

<!-- 来源页 2137 -->
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 192.168.1.1/24
hostname(config-if-eth0/0)# exit
hostname(config)#
第二步：配置设备接口ethernet0/2。
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# zone untrust
hostname(config-if-eth0/2)# ip address 202.1.0.1/24
hostname(config-if-eth0/2)# exit
hostname(config)#
第三步：配置设备接口ethernet0/1。
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone dmz
hostname(config-if-eth0/1)# ip address 10.0.0.1/8
hostname(config-if-eth0/1)# exit
hostname(config)#
第四步：配置策略规则。
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zone dmz
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config)#

<!-- 来源页 2138 -->
第五步：开启untrust域的SYN Flood攻击防护功能。
hostname(config)# zone untrust
hostname(config-zone)# ad syn-flood
hostname(config-if)# exit
hostname(config)#
第六步：检测对服务器10.110.1.1配置的SYN Flood攻击防护功能。以大于1500包/秒的速度向服务器
10.110.1.1发送报文。设备检测到SYN Flood攻击，并报警。
IP地址扫描攻击防护功能配置举例
本小节介绍IP地址扫描攻击防护功能的配置实例。
组网需求
将设备的以太网口ethernet0/0配置为Trust域，以太网口ethernet0/2配置为Untrust域，以太网口
ehernet0/1配置为DMZ域。需要对DMZ域内的服务器进行IP地址扫描攻击防护。
配置步骤
第一步：配置设备接口ethernet0/0。
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 192.168.1.1/24
hostname(config-if-eth0/0)# exit
hostname(config)#
第二步：配置设备接口ethernet0/2。
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# zone untrust
hostname(config-if-eth0/2)# ip address 202.1.0.1/24
hostname(config-if-eth0/2)# exit
hostname(config)#
第三步：配置设备接口ethernet0/1。
hostname(config)# interface ethernet0/1

<!-- 来源页 2139 -->
hostname(config-if-eth0/1)# zone dmz
hostname(config-if-eth0/1)# ip address 10.0.0.1/8
hostname(config-if-eth0/1)# exit
hostname(config)#
第四步：配置策略规则。
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zone dmz
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config)#
第五步：开启untrust域的IP地址扫描攻击防护功能。
hostname(config)# zone untrust
hostname(config-zone)# ad ip-sweep
hostname(config-if)# exit
hostname(config)#
第六步：检测配置的IP扫描攻击防护功能。用smartbits构造报文，对ethernet0/2进行IP扫描攻击，以大
于10包/毫秒的速度向202.1.0.1发送。设备检测到扫描攻击，并报警。

<!-- 来源页 2140 -->
病毒过滤
系统的病毒过滤功能能够为用户提供高速、高性能以及低延迟的病毒过滤解决方案。配置病毒过滤功能后，
设备能够探测各种病毒威胁，例如恶意软件、恶意网站等，并且根据配置对发现的病毒进行处理。
病毒过滤功能可检测最易携带病毒的文件类型和常用的协议类型（HTTP、FTP、HTTPS、SMTP、POP3、
IMAP4以及SMB）并对其进行病毒防护。对于SMB协议，系统还支持断点续传场景下的病毒文件过滤和阻
断。可扫描文件类型包括存档文件（包含压缩存档文件，支持压缩类型有GZIP、BZIP2、TAR、ZIP和
RAR）、PE、HTML、MAIL、RIFF、ELF、PDF、MS OFFICE、Raw Data和Others。其中Other表示对除
页面可选择的文件类型以外的其他类型文件进行病毒扫描，主要包括GIF，BMP，PNG，JPEG，FWS，
CWS，RTF，MPEG，Ogg，MP3，wma，WMV，ASF，RM等。
系统支持基于安全域和基于策略的病毒过滤配置方式。为安全域配置病毒过滤规则后，系统将会对以绑定安
全域为源安全域/目的安全域的流量根据病毒过滤规则配置进行病毒过滤检查。将病毒过滤规则绑定到策略规
则后，系统将会对与策略规则相匹配的流量根据规则配置进行病毒过滤检查。
如设备开启了IPv6，病毒过滤功能支持扫描IPv6地址的病毒。
系统的病毒过滤特征库包含千万余种以上病毒特征，支持病毒过滤特征库的默认每日自动升级，也可以手动
实时升级，请参阅升级管理的升级特征库部分。
注意: 病毒过滤功能受许可证控制，即为支持病毒过滤功能的设备安装病毒过滤（AV）许可证
后，功能才可使用。
配置病毒过滤
实现系统的病毒过滤功能，用户需要按照以下步骤进行操作：
1. 定义病毒过滤Profile，在Profile中指定扫描文件类型、扫描协议、系统发现病毒后采取的动作以及标签邮件功
能。
2. 绑定病毒过滤Profile到适当的策略规则或者将病毒过滤Profile绑定到安全域。如需对HTTPS流量进行病毒过滤检
查，请参照下文绑定病毒过滤Profile到策略规则。
系统还支持绑定病毒过滤Profile到ZTNA策略，对与ZTNA策略相匹配的流量进行病毒过滤和处理。相关配
置请参阅配置ZTNA策略。

<!-- 来源页 2141 -->
注意: 初次使用病毒过滤功能，需要首先更新病毒特征库。关于病毒特征库更新配置，请参阅“病
毒特征库更新配置”。为保证能够正常连接到默认更新服务器，请在更新前为设备配置DNS服务
器。
开启/关闭病毒过滤功能
安装病毒过滤功能许可证并重启设备后，系统的病毒过滤功能为开启状态。用户可以通过show version命
令查看系统的病毒过滤功能是否开启。开启或者关闭病毒过滤功能，在任何模式下使用以下命令：
exec av {enable | disable}
l
enable – 开启系统的病毒过滤功能。
l
disable – 关闭系统的病毒过滤功能。
执行以上命令后，需要重启设备才能相应地开启或者关闭病毒过滤功能。设备重启后，部分平台的最大并发
连接数会根据病毒过滤功能的开启或者关闭状态减少或者恢复正常。关于系统最大并发连接数变化的详细信
息，请参阅"调整系统最大并发连接数" 在第894页。
配置日志聚合以及聚合时间间隔
系统可将具有相同属性的病毒过滤日志进行聚合，并指定日志聚合的时间间隔，从而减少日志数量，避免日
志服务器接受冗余的日志信息。配置日志聚合以及聚合时间间隔，在全局配置模式下，使用以下命令：
av agg-log enable [by-src | by-dst | by-src-dst ] [aggregation-time value]
l
av agg-log enable - 将按照默认聚合类型（相同源IP、相同目的IP且相同病毒文件MD5值）和默认时
间间隔（10秒）进行日志聚合。
l
by-src - 将相同源IP、相同病毒文件MD5值的日志进行聚合。
l
by-dst - 将相同目的IP、相同病毒文件MD5值的日志进行聚合。
l
by-src-dst - 将相同源IP、相同目的IP且相同病毒文件MD5值的日志进行聚合。
l
value - 指定日志聚合的时间间隔。指定后，系统将对同一时间间隔内，同一聚合类型的日志只存入数
据库一次，不再重复存入多次。范围是10到600秒。如不指定，默认时间间隔为10秒。
在全局配置模式下使用no av agg-log enable指定日志聚合类型为“不聚合”，即不聚合日志。将每一条
病毒过滤日志分别存入数据库，不进行日志聚合。

<!-- 来源页 2142 -->
开启/关闭智能文件引擎检测功能
智能文件引擎的检测目标主要为PE、PDF、OFFICE与ELF文件，通过对缓存文件进行恶意文件的检测，并将
检测报文延迟发送，确保在检测到病毒文件时，能成功阻断其传输，从而提高病毒检测和过滤能力。如需更
新智能文件引擎特征库，请参阅病毒过滤智能文件引擎库更新配置。
开启/关闭智能文件引擎功能，在全局配置模式下，使用以下命令：
av-file-engine {enable | disable}
l
enable – 开启系统的智能文件引擎功能。
l
disable – 关闭系统的智能文件引擎功能。该功能默认为关闭状态。
型号说明：
以下设备型号支持该功能：
l
A系列：除SG-6000-A2200/A1800/A1600/A1600-
A/A200/A200W/A200G4/A200WG4/A200-A/A200G4-A/A200W-A/A200WG4-A
之外的其他设备。
l
K系列：K系列所有设备。
l
X系列：除SG-6000-X9180之外的其他设备。
l
云·界：部署在X86架构或者ARM架构服务器上的云·界。
注意:
l
病毒过滤功能开启后，才支持配置该功能。
l
当病毒过滤规则配置中的某个协议动作为填充魔术数时，使用该协议传输的文件不会进行智能
文件引擎检测。
l
当病毒过滤规则配置了抓包动作，即使智能文件引擎检测到威胁，也不会抓包。
配置缓存文件大小
智能文件引擎的检测目标主要为PE、PDF、OFFICE与ELF文件，需要先对目标文件进行缓存，再对缓存文件
进行恶意文件的检测。缓存文件越大，引擎的检测率就越高，同时内存开销也越大。缓存文件大小默认为
1024KB，通常情况下用户保持默认即可。当需要提高检测率时，用户可以根据需要进行调整。
配置缓存文件大小，在全局配置模式下，使用以下命令：

<!-- 来源页 2143 -->
av-file-engine cache-file-size number
l
number–指定智能文件引擎缓存区的大小，取值范围为128-10240KB，默认值为1024KB。
在全局配置模式下使用该命令no的形式恢复默认缓存文件大小：
no av-file-engine cache-file-size
配置延迟发送报文时间
为了确保智能文件引擎在检测到病毒文件时能够有效阻断其传输，系统支持配置延迟发送报文时间，该时间
允许智能文件引擎在发送检测报文之前，等待指定的时间以对文件扫描完成并获取扫描结果。在延迟发送时
间内，如果获取到了扫描结果，则根据扫描结果来确定报文是否要被发送；如果没有获取到扫描结果，则直
接发送报文。
配置延迟发送报文时间，在全局配置模式下，使用以下命令：
av-file-engine pak-hold-time time-number
l
time-number - 指定延迟发送报文的时间，取值范围为0-1000毫秒，默认为500毫秒。
在全局配置模式下使用该命令no的形式恢复默认延迟发送报文时间：
no av-file-engine pak-hold-time
配置长延迟发送报文时间
在智能文件引擎进行文件检测时，如果检测文件较大、CPU性能较差，会出现扫描结果出来较晚导致报文已
经被发送的情况，此时将无法有效阻断病毒文件的传输。因此系统支持配置更长的延迟发送报文时间，以确
保智能文件引擎在报文发送前能够完成文件扫描并获取扫描结果，从而能够有效阻断病毒文件的传输。
配置长延迟发送报文时间，在任意模式下，使用以下命令：
exec av-file-engine pak-hold-time num
l
num – 指定长延迟发送报文时间，取值范围为1001-5000毫秒。
注意: 长延迟发送报文时间配置一次性生效，不保存配置，重启后配置失效。
配置智能文件引擎参数
系统支持配置智能文件引擎参数，增加智能文件引擎的配置灵活性。用户可以针对不同的检测项目来调整配
置参数，从而达到预期的测试目的。系统支持对以下参数进行配置：引擎模式、扫描压缩文件大小、扫描压
缩文件个数、扫描解压缩层数、扫描超时时间和引擎灵敏度，同时系统支持重新加载引擎、恢复默认引擎参
数、重启智能文件引擎进程。

<!-- 来源页 2144 -->
注意: 智能文件引擎的参数配置需要重新加载引擎才能生效，所以在配置智能文件引擎参数后，需
要手动输入命令来重新加载引擎。重新加载引擎配置请参阅重新加载引擎章节。
配置引擎模式
智能文件引擎支持两种引擎模式，分别是轻量级模式和普通模式。轻量级模式不会对压缩文件进行解压缩，
扫描速度快，检测率稍低；普通模式会对压缩文件进行解压缩，扫描速度慢，检测率稍高。默认为轻量级模
式。
配置引擎模式，在全局配置模式下，使用以下命令：
av-file-engine mode {light | normal}
l
light – 指定引擎模式为轻量级模式，该模式为默认引擎模式。
l
normal – 指定引擎模式为普通模式。
在全局配置模式下使用该命令no的形式恢复默认引擎模式：
no av-file-engine mode
配置扫描压缩文件大小
被检测的文件压缩包内可能会有多个文件，配置扫描压缩文件大小后，当引擎扫描的文件总大小超过该配置
时，引擎将不再继续扫描，防止引擎扫描时间过长。
配置扫描压缩文件大小，在全局配置模式下，使用以下命令：
av-file-engine max-scan-size num
l
num – 指定引擎扫描压缩文件的大小，取值范围为5-50MB，默认为10MB。
在全局配置模式下使用该命令no的形式恢复默认扫描压缩文件大小：
no av-file-engine max-scan-size
配置扫描压缩文件个数
被检测的文件压缩包内可能会有多个文件，配置扫描压缩文件个数后，当引擎扫描的文件个数超过该配置
时，引擎将不再继续扫描，防止引擎扫描时间过长。
配置扫描压缩文件个数，在全局配置模式下，使用以下命令：
av-file-engine max-file-count num
l
num – 指定引擎扫描压缩文件的个数，取值范围为1-500个，默认为50个。

<!-- 来源页 2145 -->
在全局配置模式下使用该命令no的形式恢复默认扫描压缩文件个数：
no av-file-engine max-file-count
配置扫描解压缩层数
被检测的文件压缩包内可能会有多层压缩，配置扫描解压缩层数后，当引擎扫描时的解压缩层数超过该配置
时，引擎将不再继续扫描，防止引擎扫描时间过长。
配置扫描解压缩层数，在全局配置模式下，使用以下命令：
av-file-engine max-recursion num
l
num – 指定引擎扫描解压缩层数，取值范围为1-20层，默认为5层。
在全局配置模式下使用该命令no的形式恢复默认扫描解压缩层数：
no av-file-engine max-recursion
配置扫描超时时间
配置引擎扫描文件的超时时间，扫描超时之后，引擎将不再继续扫描，防止引擎扫描时间过长。
配置扫描超时时间，在全局配置模式下，使用以下命令：
av-file-engine max-scan-time num
l
num – 指定引擎扫描文件的超时时间，取值范围为0-2000毫秒，0表示不限制超时，默认为500毫秒。
在全局配置模式下使用该命令no的形式恢复默认扫描超时时间：
no av-file-engine max-scan-time
注意: 在智能文件引擎进行文件扫描时，只要扫描压缩文件大小、扫描压缩文件个数、扫描解压缩
层数、扫描超时时间中有一项超过阈值，引擎就会停止扫描。
配置引擎灵敏度
引擎灵敏度可以调整智能文件引擎的检测率和误报率。引擎灵敏度有三种模式可以配置，分别是Cautious、
Balanced和Positive，这三种模式的检测率和误报率依次增高。当需要检测率的时候，可以将灵敏度配置
为Positive模式，这样可以提高一些检测率，但相对的误报率也会提高。因此在保证正常使用时，建议用户
选择检测率和误报率较为均衡的Balanced模式。引擎灵敏度默认为Balanced模式。
配置引擎灵敏度，在全局配置模式下，使用以下命令：
av-file-engine sensitivity {Positive | Balanced | Cautious | Default}

<!-- 来源页 2146 -->
l
Positive – 指定引擎灵敏度为Positive模式。
l
Balanced – 指定引擎灵敏度为Balanced模式，该模式为默认引擎灵敏度。
l
Cautious – 指定引擎灵敏度为Cautious模式。
l
Default – 指定引擎灵敏度为默认模式。
在全局配置模式下也可以使用该命令no的形式恢复默认引擎灵敏度：
no av-file-engine sensitivity
重新加载引擎
智能文件引擎的参数配置需要重新加载引擎才能生效，所以在配置智能文件引擎参数后，需要手动输入命令
来重新加载引擎。
重新加载引擎实例，在任意模式下，使用以下命令：
exec av-file-engine reload
恢复默认引擎参数
系统支持快速恢复智能文件引擎参数的默认值，包含引擎模式、引擎灵敏度、扫描压缩文件大小、扫描压缩
文件个数、扫描解压缩层数、扫描超时时间。
恢复默认引擎参数，在任意模式下，使用以下命令：
exec av-file-engine param reset
重启智能文件引擎进程
智能文件引擎在进行连续检测后会占用大量内存，此时可能会影响到系统其他功能的正常使用，所以系统支
持手动重启智能文件引擎进程来释放被占用的内存。
重启智能文件引擎进程，在任意模式下，使用以下命令：
exec av-file-engine restart
注意: 智能文件引擎进程启动后的两分钟内，再次执行重启智能文件引擎进程命令将不会生效。
提升智能文件引擎检测性能
用户可以根据需要配置智能文件引擎检测性能提升功能。配置该功能后，系统将采用多核多进程技术进行智
能文件引擎检测，以提升其检测性能。

<!-- 来源页 2147 -->
指定系统数据层面占用CPU核的数量
提升智能文件引擎检测性能，用户需要首先指定系统数据层面占用CPU核的数量。指定后，智能文件引擎检
测进程数量为系统CPU核总数减去系统数据层面占用的CPU核的数量。指定系统数据层面占用CPU核的数
量，在全局配置模式下，使用以下命令：
flow-core-num number
l
number - 指定系统数据层面占用CPU核的数量。取值范围为max_core_number/2到max_core_
number-ber，max_core_number为系统的CPU核总数。指定后，智能文件引擎检测进程数量的计算
公式为：智能文件引擎检测进程数量=max_core_number（系统的CPU核总数）-flow-corenumber（系统数据层面占用CPU核的数量）。
在全局模式下使用no flow-core-num命令，取消系统数据层面占用CPU核数量的配置。
开启/关闭智能文件引擎多进程功能
默认情况下，智能文件引擎多进程功能为关闭状态。开启此功能，在全局配置模式下，使用以下命令：
cp-multi-cores av-file-engine
在全局模式下使用no cp-multi-cores av-file-engine命令，关闭此功能。
型号说明：
l
SG-6000-K20803、SG-6000-K9180、SG-6000-K7680、SG-6000-K7280、SG-
6000-K6680、SG-6000-K6580、X系列平台和CPU核数≤2的设备不支持该功能。
注意:
l
指定或取消指定系统数据层面占用CPU核的数量后，需要重启设备使配置生效。
l
开启/关闭智能文件引擎多进程功能后，需要重启设备使配置生效。
l
用户需要先指定系统数据层面占用CPU核的数量，然后开启智能文件引擎多进程功能，最后再
重启设备。设备重启后，智能文件引擎多进程功能才能够完全开启。
显示智能文件引擎检测信息
用户可以使用show命令查看智能文件引擎检测功能的启用状态、配置信息以及检测数量等。
显示智能文件引擎检测信息，在任何模式下，使用以下命令：

<!-- 来源页 2148 -->
show av-file-engine status
例如：
hostname# show av-file-engine status
AV file engine status : enabled （显示智能文件引擎功能已开启。）
Cache file max size (KB): 1024 （显示缓存文件大小为1024KB。）
Pak hold time (ms) : 500 （显示延迟发送报文时间为500毫秒。）
Running on core 0 : Yes （显示智能文件引擎功能仅在CPU0上运行。）
Detected: 2 （显示智能文件引擎检测到2个病毒。）
创建病毒过滤Profile
病毒过滤Profile中主要指定需要病毒扫描的文件类型、协议类型，以及系统发现病毒后的动作。创建病毒过
滤Profile，在全局配置模式下使用以下命令：
av-profile av-profile-name
l
av-profile-name - 指定所创建的病毒过滤Profile的名称，并且进入该病毒过滤Profile的配置模式。
如果指定名称已存在，则直接进入病毒过滤Profile配置模式。使用no av-profile av-profile-name
删除指定的病毒过滤Profile。
为实现精确扫描控制，在病毒过滤Profile配置模式下，用户可以分别指定需扫描协议类型以及动作和文件类
型。其中，协议类型为必配，而文件类型可以根据需要进行选择性配置。如果只配置协议类型，而未配置文
件类型，系统仅对通过指定协议传输的文本文件进行扫描。如果需要扫描的对象为通过指定类型传输的指定
类型文件，例如通过HTTP协议传输的HTML文件，用户需要在病毒过滤Profile中同时配置对HTTP协议和
HTML文件进行扫描。
注意: 默认情况下，根据病毒过滤的防护级别，系统自带六条默认病毒过滤规则：predef_low、
predef_middle、predef_high、predef_loose、predef_emergency、no-av，默认规则不
允许执行编辑或删除操作。
l
predef_low扫描最常见的文件类型，防护级别最低；
l
predef_middle扫描中等数量的文件类型，防护级别中等；
l
predef_high扫描全部文件类型，防护级别最高；
l
predef_loose扫描全部文件类型和协议类型，防护动作全部为只记录日志；

<!-- 来源页 2149 -->
l
predef_emergency重保模式模板，扫描所有文件类型和协议类型，一旦发现威胁，立即执行
重置连接的防护动作。
l
no-av不进行病毒过滤检测。
l
根据协议特点，邮件传输类协议推荐防护动作为填充魔术字，其他类推荐防护动作为重置连
接。
防恶意网站功能
为保护用户，防止用户点击恶意链接并访问恶意网站，系统提供防恶意网站功能。开启防恶意网站功能后，
系统会对用户试图访问的网站链接进行木马以及钓鱼等恶意网站检测，并根据系统发现病毒后的动作配置，
对恶意链接进行相应处理。关于系统发现病毒后的动作配置，请参阅“指定协议类型”。默认情况下，防恶
意网站功能是开启的。开启防恶意网站功能，在病毒过滤Profile配置模式下使用以下命令：
anti-malicious-sites
使用该命令no的形式关闭防恶意网站功能：
no anti-malicious-sites
指定防恶意网站访问控制动作
指定防恶意网站访问控制动作，在病毒过滤Profile配置模式下使用以下命令：
anti-malicious-sites [action{ log-only | reset-conn | warning}| pcap]
l
action {log-only | reset-conn | warning} – 指定对发现恶意网站采取的动作。
l
log-only – 产生日志信息。该选项为FTP、IMAP4、POP3或者SMTP协议发现病毒时系统采取的
默认动作。
l
reset-conn – 发现病毒后，重置病毒连接。
l
warning – 弹出警告提示页面，提示用户发现恶意网站。扫描发现恶意网站时，给出警告提示页
面，如下图所示。

<!-- 来源页 2150 -->
用户可以点击“为何要阻止此网站”按钮，跳转到Google诊断页面，查看阻止访问原因。
或者，点击“忽略此警告”链接，跳过警告提示页面，继续访问。跳过警告提示页面后，若用户一
小时之内再次访问该网站，将不会收到警告提示。
l
pcap – 指定对防恶意网站访问控制进行抓包取证，当系统检测到威胁时会抓取相关报文。
使用该命令no的形式取消对防恶意网站访问控制动作的指定。
no anti-malicious-sites [action {log-only | reset-conn | warning} | pcap]
注意: 对于不带硬盘的设备和带硬盘的A1600/A1800/A2200设备，开启抓包取证功能时，需同时
开启“加入用户体验改进计划”并开启云·景的威胁日志上报，抓包取证功能才能生效。在该情况
下，防火墙设备上将无法查看到抓包取证的报文数据，系统会将抓包取证的报文数据和威胁日志信
息上送至云·景，安全运营人员可以根据抓包取证的证据信息对威胁日志信息进行分析研判。
指定协议类型
指定病毒扫描协议类型，在病毒过滤配置模式下使用以下命令：
protocol-type {{ftp | imap4 | pop3 | smtp} [pcap | action {fill-magic | log-only | reset-conn} ] |
http [pcap |action {fill-magic | log-only | reset-conn | warning}] | smb [pcap | action {logonly | reset-conn}]
l
ftp – 指定对通过FTP协议传输的信息进行病毒扫描。
l
http – 指定对通过HTTP协议传输的信息进行病毒扫描。
l
imap4 – 指定对通过IMAP4协议传输的信息进行病毒扫描。
l
pop3 – 指定对通过POP3协议传输的邮件进行病毒扫描。
l
smtp – 指定对通过SMTP协议传输的邮件进行病毒扫描。
l
smb– 指定对通过SMB协议传输的信息进行病毒扫描。

<!-- 来源页 2151 -->
l
pcap – 指定对协议传输信息病毒扫描进行抓包取证，当系统检测到威胁时会抓取相关报文。
注意: 对于不带硬盘的设备和带硬盘的A1600/A1800/A2200设备，开启抓包取证功能时，需
同时开启“加入用户体验改进计划”并开启云·景的威胁日志上报，抓包取证功能才能生效。在
该情况下，防火墙设备上将无法查看到抓包取证的报文数据，系统会将抓包取证的报文数据和
威胁日志信息上送至云·景，安全运营人员可以根据抓包取证的证据信息对威胁日志信息进行分
析研判。
l
action {fill-magic | log-only | reset-conn | warning} – 指定对发现病毒的协议采取的动作。
l
fill-magic – 使用文件填充的方式处理病毒文件，即从文件中被病毒感染部分的起始位置起使用
魔术字（Virus is found, cleaned）进行填充，一直到被感染部分结束。
l
log-only – 产生日志信息。该选项为FTP、IMAP4、POP3或者SMTP协议发现病毒时系统采取的
默认动作。
l
reset-conn – 发现病毒后，重置病毒连接。
l
warning – 弹出警告提示页面，提示用户发现病毒或者恶意下载链接。该选项只对通过HTTP协议
传输的信息进行病毒扫描时有效，且为发现病毒或者恶意下载链接时系统采取的默认动作。
扫描发现病毒时，给出警告提示页面，如下图所示：
扫描发现恶意下载链接时，给出警告提示页面，如下图所示：

<!-- 来源页 2152 -->
用户可以点击“忽略此警告”链接，跳过警告提示页面，继续访问。跳过警告提示页面后，若用户
一小时之内再次访问该网站，将不会收到警告提示。
使用多条该命令可指定多个协议类型。
使用以上命令no的形式取消协议类型的指定：
no protocol-type {ftp | imap4 | pop3 | smtp | smb | http}
SMTP、POP3和IMAP4都是邮件传输协议，用来传送mail类型的文件。当配置对邮件进行扫描时，必须在
配置对SMTP、POP3或IMAP4协议进行扫描的同时配置对mail类型文件进行扫描；并且，由于邮件的正文
和附件都是嵌套在mail文件中的，因此还需要配置对邮件中可能包含的附件类型进行扫描。
指定文件类型
指定病毒扫描文件类型，在病毒过滤Profile配置模式下使用以下命令：
file-type {bzip2 | gzip | html | jpeg | mail | pe | rar | riff | tar | zip | 7-Zip | elf | pdf | office |
raw-data | others }
l
bzip2 – 指定对BZIP2压缩文件进行病毒扫描。
l
gzip – 指定对GZIP压缩文件进行扫描。
l
html – 指定对HTML类型文件进行病毒扫描。
l
jpeg – 指定对JPEG类型文件进行扫描。
l
mail – 指定对mail类型文件进行病毒扫描。
l
pe – 指定对PE类型文件进行扫描。PE即Portable Executable（可移植的执行体）的缩写。它是
Win32环境自身所带的执行体文件格式。可移植的执行体意味着此文件格式是跨Win32平台的：即使
Windows运行在非Intel的CPU上，任何Win32平台的PE装载器都能识别和使用该文件格式。另外，系
统还支持对已经加壳（支持的加壳类型有ASPack 2.12、UPack 0.399、UPX的所有版本以及FSG的
1.3、1.31、1.33和2.0版本）的PE文件进行扫描。
l
rar – 指定对RAR压缩文件进行病毒扫描。
l
riff – 指定对RIFF类型文件进行扫描。RIFF即Resource Interchange File Format（资源交换文件格
式）的缩写。是微软为Windows设计的一类多媒体文件格式，主要包括WAV和AVI两种。
l
tar – 指定对TAR压缩文件进行病毒扫描。
l
zip – 指定对ZIP压缩文件进行病毒扫描。
l
7-Zip - 指定对7-ZIP压缩文件进行病毒扫描。
l
elf – 指定对ELF类型文件进行病毒扫描。

<!-- 来源页 2153 -->
l
pdf – 指定对PDF类型文件进行病毒扫描。
l
office – 指定对office文件进行病毒扫描。
l
raw-data – 指定对txt文件和无法识别的文件进行病毒扫描。
l
others– 指定对除上述可配置文件类型以外的其他类型文件进行病毒扫描，主要包括GIF，BMP，
PNG，FWS，CWS，RTF，MPEG，Ogg，MP3，wma，WMV，ASF，RM等。
使用多条该命令可指定多个文件类型。
使用以上命令no的形式取消文件类型的指定：
no file-type { bzip2 | gzip | html | jpeg | mail | pe | rar | riff | tar | zip| 7-Zip | elf | pdf | office |
raw-data | others }
标签邮件功能
如果对通过SMTP协议传输的邮件进行病毒扫描，则用户可以对发出的电子邮件开启标签邮件功能，即系统
对邮件及其附件进行扫描，扫描病毒的结果会包含在邮件的主体中，随邮件一起发送。如果没有发现病毒，
则提示“No virus found”，如下表所示：
邮件正文
No virus found.
Checked by Hillstone AntiVirus
如发现病毒，则显示邮件中病毒相关信息，包括系统扫描文件的名称、文件的路径、扫描结果以及对该病毒
的执行动作，如下表所示：
邮件正文
Here are the AntiVirus scanning results:
Body: Found virus: virusname1, action: log;
Attachment1.zip/virustest1.exe: Found virus: virusname2,
action: log; Attachment2.tar/subfolder/file1.doc: Found virus: virusname3,
action: log;
Checked by Hillstone AntiVirus

<!-- 来源页 2154 -->
注意: 邮件中最多显示三个病毒文件（包含邮件主体和附件）的扫描信息。全部文件的扫描信息请
在日志中查看。
开启或关闭标签邮件功能
默认情况下，标签邮件功能是关闭的。用户需要在病毒过滤Profile配置模式下，输入以下命令开启标签邮件
功能：
label-mail
使用该命令no的形式关闭标签邮件功能：
no label-mail
配置邮件签名
在开启标签邮件功能后，用户可以指定标签邮件的签名。默认情况下，标签邮件签名为“Checked by
Hillstone AntiVirus”。邮件签名不支持中文签名。在病毒过滤配置模式下，输入以下命令配置签名：
mail-sig signature-string
l
signature-string – 配置标签邮件的签名。
在病毒过滤配置模式下，使用该命令no形式恢复默认值：
no mail-sig
配置病毒过滤白名单功能
当文件或URL进行病毒过滤检测后误报出威胁日志，可以将文件MD5值、URL或外部动态列表加入病毒过滤
白名单，用户可以对病毒过滤白名单进行编辑和删除。
外部动态列表可以应用于企业管理多台防火墙的场景中。通过将外部动态列表应用于防火墙的病毒过滤白名
单，企业可以实现高效、统一的策略管理。管理员仅需在服务器上更新外部动态列表文件，所有关联防火墙
便会按预设周期，自动同步文件内容。这种机制极大地简化了运维管理流程，避免了对每台防火墙逐一进行
配置更新，有效降低运维人员的工作负担，保障各防火墙病毒过滤白名单的一致性与及时性。
注意: 最多允许添加的病毒过滤白名单数量为1000条。
新增或编辑病毒过滤白名单，在全局配置模式下，使用以下命令：

<!-- 来源页 2155 -->
av-allowlist [id id-num] name whilelist-name {url url-str|md5 md5-str | md5-externaldynamic-list md5-external-dynamic-list | url-external-dynamic-list url-external-dynamiclist}
l
id-num - 指定病毒过滤白名单的序号。如果不配置ID，系统默认按顺序生成一个新的ID。编辑指定的
病毒过滤白名单条目，需要输入ID。
l
whilelist-name - 指定病毒过滤白名单的名称。
l
url-str - 指定病毒过滤白名单的URL。URL为不含“http(s)://”的URL地址。不支持设置带有通配符
的URL，例如*abc.com。
l
md5-str - 指定病毒过滤白名单的文件MD5值。MD5值为32位16进制的字符串。例如
d41d8cd98f00b204e9800998ecf8427e。
l
md5-external-dynamic-list - 指定外部动态列表的名称。仅支持指定HASH类型的外部动态列表。
md5-external-dynamic-list非自定义项，为系统中已配置的HASH类型的外部动态列表名称。
l
url-external-dynamic-list - 指定外部动态列表的名称。仅支持指定URL类型的外部动态列表。urlexternal-dynamic-list非自定义项，为系统中已配置的URL类型的外部动态列表名称。
删除病毒过滤白名单，在全局配置模式下，使用以下命令：
no av-allowlist id id-num
l
id-num - 指定病毒过滤白名单的序号。
显示病毒过滤白名单信息
在任何模式下，输入以下命令显示病毒过滤白名单信息：
show av-allowlist
例如：
hostname# show av-allowlist
AV allowlist total num: 1
=============================================================================
ID Name Type URL/MD5
-----------------------------------------------------------------------------------
1 123 URL abc.com
=============================================================================

<!-- 来源页 2156 -->
绑定病毒过滤Profile到安全域
将病毒过滤Profile绑定到安全域后，系统将会对以该安全域为源安全域/目的安全域的流量按照Profile配置
进行病毒过滤检查。当策略规则已经绑定了病毒过滤Profile，同时策略规则的目的安全域也绑定了病毒过滤
Profile，策略规则绑定的病毒过滤Profile将会生效，而目的安全域绑定的病毒过滤Profile无效。
绑定病毒过滤Profile到安全域，在安全域配置模式下，使用以下命令：
av enable av-profile-name
l
av-profile-name – 指定绑定到安全域的病毒过滤Profile的名称。一个安全域只能绑定一个病毒过滤
Profile。
在安全域配置模式下，使用该命令no的形式取消病毒过滤Profile的绑定：
no av enable
查看安全域与病毒过滤Profile的绑定信息，使用show av zone-binding命令。
绑定病毒过滤Profile到策略规则
将病毒过滤Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据Profile配置进行病毒过滤
检查。绑定病毒过滤Profile到策略规则，在策略规则配置模式下使用以下命令：
av {av-profile-name | no-av}
l
av-profile-name – 指定绑定到策略规则的病毒过滤Profile的名称。
l
no-av – 绑定名为“no-av”的预定义病毒过滤Profile到策略规则，含义为不做病毒过滤。当为策略规
则绑定该Profile后，即使系统中有相匹配的其他病毒过滤Profile，系统仍不会对流量进行病毒过滤检
测。
在策略规则配置模式下使用该命令no的形式取消病毒过滤Profile的绑定：no av
如果需要病毒过滤对HTTPS流量进行扫描，需要为此条策略规则（病毒过滤Profile绑定到的策略规则）启用
SSL代理功能。系统将根据SSL代理Profile解密HTTPS流量，对解密后的数据根据病毒过滤Profile进行检
测。根据安全策略规则的配置不同，系统将进行如下操作：
安全策略规则配置
操作
启用SSL代理
不启用病毒过滤
根据SSL代理Profile解密HTTPS流量，对解密后的数据不进行病毒过滤。
启用SSL代理
启用病毒过滤
根据SSL代理Profile解密HTTPS流量，对解密后的数据根据病毒过滤Profile进行病毒过滤。
不启用SSL代理
对HTTP流量根据病毒过滤Profile进行病毒过滤。对HTTPS流量不进行解密，不进行病毒过
滤，只进行转发。

<!-- 来源页 2157 -->
安全策略规则配置
操作
启用病毒过滤
当安全策略规则所关联的安全域也启用病毒过滤时，系统也将进行如下操作：
安全策略规则配置
安全域配置
操作
启用SSL代理
不启用病毒过滤
启用病毒过滤
根据SSL代理Profile解密HTTPS流量，对解密后的数据根据安全域配置的
病毒过滤Profile进行病毒过滤。
启用SSL代理
启用病毒过滤
启用病毒过滤
根据SSL代理Profile解密HTTPS流量，对解密后的数据根据安全策略规则
中配置的病毒过滤Profile进行病毒过滤。
不启用SSL代理
启用病毒过滤
启用病毒过滤
对HTTP流量根据安全策略规则中配置的病毒过滤Profile进行病毒过滤。
对HTTPS流量不进行解密，不进行病毒过滤，只进行转发。
更多关于SSL代理Profile的配置，请参阅“SSL代理”章节。
显示病毒过滤profile信息
在任何模式下，输入以下命令显示病毒过滤profile信息：
show av-profile
配置应用层压缩控制功能
配置应用层压缩控制功能后，系统会对传输的压缩文件进行解压，并能对超出最大压缩层数的文件以及加密
压缩文件按照指定的动作进行处理。支持解压缩的文件格式包括RAR、ZIP、TAR、GZIP、BZIP2以及7-
ZIP。解压控制功能配置命令，请参阅配置应用层压缩控制功能。
病毒特征库更新配置
默认情况下，系统会每日自动更新病毒特征库，用户可以根据需要更改病毒特征库更新配置。病毒特征库更
新配置包括：
l 配置病毒特征库更新模式
l 配置更新传输协议
l 配置更新服务器
l 指定HTTP代理服务器
l 指定更新时间
l 立即更新
l 导入病毒特征文件

<!-- 来源页 2158 -->
l 显示病毒特征信息
l 显示病毒特征库更新配置信息
配置病毒特征库更新模式
系统支持手动和自动两种更新方式。配置病毒特征库更新方式，在全局配置模式下，使用以下命令：
av signature update mode {auto | manual}
l
auto – 指定自动更新病毒特征库。该方式为系统的默认更新方式。
l
manual – 指定手动更新病毒特征库。
在全局配置模式下使用该命令no的形式恢复默认更新模式：
no av signature update mode
配置更新传输协议
系统支持通过HTTP和HTTPS对特征库进行更新，默认为HTTPS。配置特征库更新的传输协议为HTTP，在全
局配置模式下，使用以下命令：
av update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：
no av update protocol HTTP
配置更新服务器
系统提供默认的病毒特征库更新服务器，即update1.hillstonenet.com和update2.hillstonenet.com，
同时用户也可以根据需要配置其它更新服务器下载最新病毒特征。最多可配置3个。配置更新服务器，在全
局配置模式下，使用以下命令：
av signature update {server1 | server2 | server3} {ip-address | domain-name} [vrouter
vrouter-name] [src-interface src-interface-name]
l
server1 | server2 | server3 – 指定将要配置的服务器，服务器支持双栈协议，可配置IPv4地址和IPv6
地址。server1的默认值为update1.hillstonenet.com，server2的默认值为
update2.hillstonenet.com。
l
ip-address | domain-name – 指定更新服务器的名称，可以是IP地址形式（ip-address）也可以是
域名形式（domain-name，例如update1.hillstonenet.com）。
l
vrouter vrouter-name - 指定更新服务器所属的VRouter。若不指定则默认是trust-vr。

<!-- 来源页 2159 -->
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，病毒特征库更新时将通过该源接口对更新服务器发起访问。若不指定，则默认使用管理口作为源接
口。
在全局配置模式下，使用该命令no的形式取消更新服务器的指定：
no av signature update {server1 | server2 | server3}
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保特征库能够正常升级，需要在设备上指定代理服务器
的IP地址和端口号。
为病毒过滤特征库升级指定代理服务器，在全局配置模式下，使用如下命令：
av signature update proxy-server {main | backup} ip-address port-number
l
main | backup – 使用main参数指定主代理服务器，使用backup指定备份代理服务器。
l
ip-address port-number – 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no av signature update proxy-server {main | backup}命令。
指定更新时间
默认情况下，系统采用自动模式每日更新病毒特征库，并且为避免服务器流量过大，每日更新时间是随机
的。用户可以根据需要指定病毒特征库更新的频率和时间，在全局配置模式下，使用以下命令：
av signature update schedule {daily | weekly {mon | tue | wed | thu | fri | sat | sun} | monthly
date} [HH:MM]
l
daily – 指定频率为每天更新。
l
weekly {mon | tue | wed | thu | fri | sat | sun} – 指定频率为每周更新。mon | tue | wed | thu | fri
| sat | sun用来指定每周更新的日期。
l
monthly date - 指定频率为每月更新。date用来指定每月更新的日期，取值范围为1到31。如果某月
不包含所指定的日期（比如2月没有30号），则该月不会自动升级。
l
HH:MM – 指定更新的时间，例如09：00。
立即更新
无论更新模式为手动还是自动，用户都可以随时使用以下命令更新病毒特征库。立即更新病毒特征库，在任
何模式下，使用以下命令：

<!-- 来源页 2160 -->
exec av signature update
l
exec av signature update – 仅对当前病毒特征库与更新服务器最新发布病毒特征库的不同部分进行
更新。
导入病毒特征文件
在某些情况下，用户设备可能无法连接到更新服务器对病毒特征库进行更新，针对这一问题，系统提供病毒
特征文件导入功能，即通过FTP、FTPS、SFTP、TFTP服务器或者U盘将病毒特征文件导入到设备，从而更
新设备的病毒特征库。导入病毒特征文件，在执行模式下，使用以下命令：
import av signature from {{ftp | ftps |sftp} server ip-address [vrouter vrouter-name] [user
user-name password password] | tftp server ip-address [vrouter vrouter-name]} file-name
l
ftp | ftps |sftp - 指定服务器的类型。
l
ip-address – 指定FTP、FTPS、SFTP或者TFTP服务器的IP地址。
l
vrouter vrouter-name – 指定FTP、FTPS、SFTP或者TFTP服务器所属的VRouter。
l
user user-name password password – 指定FTP/FTPS/SFTP服务器的用户名和密码。
l
file-name – 指定导入的病毒特征文件的名称。
显示病毒特征库信息
用户可以随时使用相应的show命令查看设备的病毒特征库信息，包括病毒特征库版本、发布日期以及病毒
特征个数等。查看病毒特征库信息，在任何模式下使用以下命令：
show av signature info
显示病毒特征库更新配置信息
用户可以随时使用相应的show命令查看设备上的病毒特征库更新信息，包括更新服务器信息、更新模式、
更新频率及时间以及病毒特征库更新状况等。查看病毒特征库更新配置信息，在任何模式下使用以下命令：
show av signature update
病毒过滤智能文件引擎库更新配置
默认情况下，系统会每日自动更新病毒过滤智能文件引擎库，用户可以根据需要更改病毒过滤智能文件引擎
库更新配置。仅采用X86架构或者ARM架构的设备型号支持该功能。
病毒过滤智能文件引擎库更新配置包括：

<!-- 来源页 2161 -->
l 配置病毒过滤智能文件引擎库更新模式
l 配置更新传输协议
l 配置更新服务器
l 指定HTTP代理服务器
l 指定更新时间
l 立即更新
l 导入病毒过滤智能文件引擎库
l 显示病毒过滤智能文件引擎库版本信息
l 显示病毒过滤智能文件引擎库更新配置信息
配置病毒过滤智能文件引擎库更新模式
系统支持手动和自动两种更新方式。配置病毒过滤智能文件引擎库更新方式，在全局配置模式下，使用以下
命令：
av-file-engine update mode {auto | manual}
l
auto – 指定自动更新病毒过滤智能文件引擎库。该方式为系统的默认更新方式。
l
manual – 指定手动更新病毒过滤智能文件引擎库。
在全局配置模式下使用该命令no的形式恢复默认更新模式：
no av-file-engine update mode
配置更新传输协议
系统支持通过HTTP和HTTPS对病毒过滤智能文件引擎库进行更新，默认为HTTPS。配置病毒过滤智能文件
引擎库更新的传输协议为HTTP，在全局配置模式下，使用以下命令：
av-file-engine update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：
no av-file-engine update protocol HTTP
配置更新服务器
系统提供默认的病毒过滤智能文件引擎库更新服务器，即update1.hillstonenet.com和
update2.hillstonenet.com，同时用户也可以根据需要配置其它更新服务器下载最新病毒过滤智能文件引
擎库。最多可配置3个。配置更新服务器，在全局配置模式下，使用以下命令：

<!-- 来源页 2162 -->
av-file-engine update {server1 | server2 | server3} {ip-address | domain-name} [vrouter
vrouter-name] [src-interface src-interface-name]
l
server1 | server2 | server3 – 指定将要配置的服务器，服务器支持双栈协议，可配置IPv4地址和IPv6
地址。server1的默认值为update1.hillstonenet.com，server2的默认值为
update2.hillstonenet.com。
l
ip-address | domain-name – 指定更新服务器的名称，可以是IP地址形式（ip-address）也可以是
域名形式（domain-name，例如update1.hillstonenet.com）。
l
vrouter vrouter-name - 指定更新服务器所属的VRouter。
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，病毒过滤智能文件引擎库更新时将通过该源接口对升级服务器发起访问。若不指定，则默认使用管
理口作为源接口。
在全局配置模式下，使用该命令no的形式取消更新服务器的指定：
no av-file-engine update {server1 | server2 | server3}
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保病毒过滤智能文件引擎库能够正常升级，需要在设备
上指定代理服务器的IP地址和端口号。
为病毒过滤智能文件引擎库升级指定代理服务器，在全局配置模式下，使用如下命令：
av-file-engine update proxy-server {main | backup} ip-address port-number
l
main | backup– 使用main参数指定主代理服务器，使用backup指定备份代理服务器。
l
ip-address port-number – 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no av-file-engine update proxy-server {main | backup}命令。
指定更新时间
默认情况下，系统采用自动模式每日更新病毒过滤智能文件引擎库，并且为避免服务器流量过大，每日更新
时间是随机的。用户可以根据需要指定病毒过滤智能文件引擎库更新的频率和时间，在全局配置模式下，使
用以下命令：
av-file-engine update schedule {daily | weekly {mon | tue | wed | thu | fri | sat | sun} |
monthly date} [HH:MM]

<!-- 来源页 2163 -->
l
daily – 指定频率为每天更新。
l
weekly {mon | tue | wed | thu | fri | sat | sun – 指定频率为每周更新。mon | tue | wed | thu | fri
| sat | sun用来指定每周更新的日期。
l
monthly date - 指定频率为每月更新。date用来指定每月更新的日期，取值范围为1到31。如果某月
不包含所指定的日期（比如2月没有30号），则该月不会自动升级。
l
HH:MM – 指定更新的时间，例如09：00。
立即更新
无论更新模式为手动还是自动，用户都可以随时使用以下命令更新病毒过滤智能文件引擎库。立即更新病毒
过滤智能文件引擎库，在任何模式下，使用以下命令：
exec av-file-engine update
l
exec av-file-engine update – 仅对当前病毒过滤智能文件引擎库与更新服务器最新发布病毒过滤智
能文件引擎库的不同部分进行更新。
导入病毒过滤智能文件引擎库
在某些情况下，用户设备可能无法连接到更新服务器对病毒过滤智能文件引擎库进行更新，针对这一问题，
系统提供病毒过滤智能文件引擎库导入功能，即通过FTP、FTPS、SFTP、TFTP服务器或者U盘将病毒过滤
智能文件引擎库文件导入到设备，从而更新设备的病毒过滤智能文件引擎库。导入病毒过滤智能文件引擎
库，在执行模式下，使用以下命令：
import av-file-engine signature from {{ftp | ftps | sftp} server ip-address [vrouter vroutername] [user user-name password password] | tftp server ip-address [vrouter vroutername]} file-name
l
ftp | ftps | sftp - 指定服务器的类型。
l
ip-address – 指定FTP、FTPS、SFTP或者TFTP服务器的IP地址。
l
vrouter vrouter-name – 指定FTP、FTPS、SFTP或者TFTP服务器所属的VRouter。
l
user user-name password password – 指定FTP/FTPS/SFTP服务器的用户名和密码。
l
file-name – 指定导入的病毒过滤智能文件引擎库的文件名称。
显示病毒过滤智能文件引擎库版本信息
用户可以随时使用相应的show命令查看设备的病毒过滤智能文件引擎库信息，包括病毒过滤智能文件引擎
库版本、发布日期等。查看病毒过滤智能文件引擎库信息，在任何模式下使用以下命令：
show av-file-engine info

<!-- 来源页 2164 -->
例如：
hostname# show av-file-engine info
vendor: Hillstone Networks（显示病毒过滤智能文件引擎库所属公司。）
Current version: 3.0.230512（显示病毒过滤智能文件引擎库的当前版本。）
Release date: 2023/05/12 16:37:09（显示病毒过滤智能文件引擎库的发布日期。）
显示病毒过滤智能文件引擎库更新配置信息
用户可以随时使用相应的show命令查看设备上的病毒过滤智能文件引擎库更新信息，包括更新服务器信
息、更新模式、更新频率及时间以及病毒过滤智能文件引擎库更新状况等。查看病毒过滤智能文件引擎库更
新配置信息，在任何模式下使用以下命令：
show av-file-engine update
例如：
hostname# show av-file-engine update
av-file-engine signature update options:
protocol: HTTPS（显示病毒过滤智能文件引擎库更新的传输协议为HTTPS。）
server1:
server2: update2.hillstonenet.com, 443, trust-vr（显示病毒过滤智能文件引擎库更新服务器信
息。）
server3:
proxy server status: disable（显示未指定代理服务器。）
main proxy server:
backup proxy server:
mode: auto（显示病毒过滤智能文件引擎库更新模式为自动更新模式。）
schedule: daily 03:51（显示自动更新频率和时间。）
current status: normal（显示病毒过滤智能文件引擎库的更新状态为正常。）
last update result: Download signature failed; please confirm the servers are reachable
（显示病毒过滤智能文件引擎库上次更新的结果。）
last update time: Tue Sep 26 03:51:57 2023（显示病毒过滤智能文件引擎库最后更新时间。）

<!-- 来源页 2165 -->
配置病毒过滤黑名单功能
病毒过滤功能通过对恶意文件MD5 值与URL 的检测，构建起一套严密的防护体系。当企业收到上级单位通
知或监管部门通报时，可借助自定义黑名单功能，将通报提及的恶意文件MD5 值和URL，快速添加至防火
墙的病毒过滤模块。此举能够显著提升企业抵御特定病毒威胁的能力，强化病毒防护效能。
外部动态列表可以应用于企业管理多台防火墙的场景中。通过将外部动态列表应用于防火墙的病毒过滤黑名
单，企业可以实现高效、统一的策略管理。管理员仅需在服务器上更新外部动态列表文件，所有关联防火墙
便会按预设周期，自动同步文件内容。这种机制极大地简化了运维管理流程，避免了对每台防火墙逐一进行
配置更新，有效降低运维人员的工作负担，保障各防火墙病毒过滤黑名单的一致性与及时性。
前置条件
在病毒过滤黑名单中使用外部动态列表前，请先完成配置外部动态列表。
配置病毒过滤黑名单功能
注意: 最多允许添加的病毒过滤黑名单数量为1000条。
配置病毒过滤黑名单，在全局配置模式下，使用以下命令：
av-blocklist [id id-num] name blocklist-name{url url-str|md5 md5-str | md5-externaldynamic-list md5-external-dynamic-list | url-external-dynamic-list url-external-dynamiclist}
l id-num - 指定病毒过滤黑名单的序号。如果不配置ID，系统默认按顺序生成一个新的ID。编辑指定的病毒过滤
白名单条目，需要输入ID。
l whilelist-name - 指定病毒过滤黑名单的名称。
l url-str - 指定病毒过滤黑名单的URL。URL为不含“http(s)://”的URL地址。不支持设置带有通配符的URL，例
如*abc.com。
l md5-str - 指定病毒过滤黑名单的文件MD5值。MD5值为32位16进制的字符串。例如
d41d8cd98f00b204e9800998ecf8427e。
l md5-external-dynamic-list - 指定外部动态列表的名称。仅支持指定HASH类型的外部动态列表。md5-
external-dynamic-list非自定义项，为系统中已配置的HASH类型的外部动态列表名称。
l url-external-dynamic-list - 指定外部动态列表的名称。仅支持指定URL类型的外部动态列表。url-externaldynamic-list非自定义项，为系统中已配置的URL类型的外部动态列表名称。
删除病毒过滤黑名单，在全局配置模式下，使用以下命令：
no av-allowlist id id-num

<!-- 来源页 2166 -->
l id-num - 指定病毒过滤黑名单的序号。
显示病毒过滤黑名单信息
在任何模式下，输入以下命令显示病毒过滤黑名单信息：
show av-blocklist
例如：
hostname# show av-blocklist
AV blocklist total num: 1
=============================================================================
ID Name Type URL/MD5
-----------------------------------------------------------------------------------
1 123 URL abc.com
=============================================================================
例：病毒过滤配置举例
使用病毒过滤功能前，确认已经为设备安装了相应的病毒过滤许可证。
本节介绍病毒过滤配置举例，通过病毒过滤配置，使设备能够：
l 对Email及其附件进行病毒过滤扫描，并将发出的邮件病毒扫描结果显示在邮件中。Email通过SMTP和POP3协
议传输，附件中可能包含.exe和.jpeg文件。
l 对压缩文件进行扫描。RAR压缩文件中包含.jpeg文件，压缩文件通过FTP协议进行传输。
配置步骤
第一步：配置病毒过滤Profile，指定需要进行扫描的协议以及文件类型：
hostname(config)# av-profile email-scan
hostname(config-av-profile)# protocol-type smtp action fill-magic
hostname(config-av-profile)# protocol-type pop3 action fill-magic
hostname(config-av-profile)# protocol-type ftp action fill-magic
hostname(config-av-profile)# file-type pe
hostname(config-av-profile)# file-type jpeg
hostname(config-av-profile)# file-type mail

<!-- 来源页 2167 -->
hostname(config-av-profile)# label-mail
hostname(config-av-profile)# mail-sig “Checked by Mail AntiVirus”
hostname(config-av-profile)# exit
hostname(config)#
第二步：创建策略规则，并在规则中引用病毒过滤Profile：
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# av email-scan
hostname(config-policy-rule)# exit
hostname(config)#
第三步：通过show version命令查看系统病毒过滤功能的开启状态。如果为关闭，则运行以下命令开启系
统的病毒过滤功能并重启系统使其生效：
hostname(config)# exec av enable

<!-- 来源页 2168 -->
沙箱防护
沙箱在虚拟环境中执行可疑文件，收集可疑文件的动态行为，对这些动态行为进行分析，并根据分析结果判
断文件合法性。
系统的沙箱防护功能使用云沙箱和本地沙箱技术，将可疑文件上传到云·影（云沙箱）或者智影（本地沙
箱）。云·影或者智影对可疑文件分析，搜集可疑文件的动态行为，判断文件合法性，将分析结果反馈给系
统，并根据系统设置的动作对恶意文件进行处理。
沙箱防护功能包括如下内容：
l 收集及上传可疑文件：沙箱防护功能对设备流量进行解析，提取出流量里的可疑文件。
l 如果此可疑文件在本地数据库中暂无分析结果，则将其上传到云平台或者智影，并由云平台将可疑文件上
传到云·影进行检测或者由智影进行检测。如何连接云平台，请参考连接山石云平台一节。
l 如果此文件已经在本地数据库中标记为恶意文件，系统可根据设置的动作对恶意文件进行处理。
此外，用户需要配置沙箱防护规则，指定可疑文件标准。
l 检查分析结果并采取响应措施：沙箱防护功能从云·影或者智影接收到可疑文件的分析结果后，检查分析结果，
判断文件合法性，保存分析结果到本地数据库。若分析结果判定可疑文件为恶意文件，根据系统设置的动作（即
重置连接或报告日志）对恶意文件进行处理。如云·影或者智影第一次发现恶意文件，系统将记录威胁日志和云
沙箱日志，不能阻断该恶意链接。当恶意文件命中本地设备缓存的威胁信息，重置连接方可生效。
l 维护本地数据库：标识上传的文件，记录文件上传时间，保存其分析结果。此部分工作由沙箱防护功能自动完
成，无需相关配置。
注意: 云·影功能受许可证控制，当用户安装云沙箱许可证后，可以使用完整的沙箱检测功能，即可
分析多种类型文件；当用户未安装云沙箱许可证时，仅可启用使用免费云沙箱试用功能，试用有效
期为一年，且分析的文件类型仅限于Windows（PE）可执行文件。
配置沙箱防护
沙箱防护配置准备工作
使用沙箱防护功能前，必须完成以下准备工作：

<!-- 来源页 2169 -->
1. 确认系统版本支持沙箱防防护功能；
2. 当前设备已经连接到云平台。如何连接，请参考连接山石云平台一节。
3. 安装云沙箱防护许可证，然后重启设备。设备成功重启后，云影功能才可使用。
注意: 开启沙箱防护功能后，部分平台的最大并发连接数会减少。关于系统最大并发连接数变化的
详细信息，请参阅"调整系统最大并发连接数" 在第894页。
配置沙箱防护功能
系统支持基于安全域和基于策略的沙箱防护配置方式：
l 为安全域配置沙箱防护规则后，系统将会对以绑定安全域为目的安全域/源安全域的流量根据沙箱防护规则配置
进行沙箱防护检查。
l 为策略配置沙箱防护规则后，系统将会对与策略规则相匹配的流量根据沙箱防护规则配置进行沙箱防护检查。
l 若安全域和策略中均配置了沙箱防护规则，策略中的配置项将有更高的优先权；在安全域配置中，目的安全域的
优先权将高于源安全域。
系统还支持绑定沙箱防护规则到ZTNA策略，对与ZTNA策略相匹配的流量进行沙箱防护检查。相关配置请参
阅配置ZTNA策略。
基于安全域/基于策略的沙箱防护配置方式，请按照以下步骤进行操作：
1. 开启云影/智影。
2. 定义沙箱防护Profile，在Profile中指定域名白名单，配置可疑文件识别标准。
3. 绑定沙箱防护Profile到安全域/策略规则。
其中，沙箱防护Profile用于指定是否启用域名白名单，配置可疑文件识别标准。域名白名单中包含安全域
名，当文件的来源是域名白名单中的域名时，此文件被认为是合法文件，不会被上传到云影或者智影进行检
测。可疑文件识别标准是指将符合标准的文件判断为可疑文件，并上传到云影或者智影进行检测。可疑文件
的检查结果决定文件是合法文件或是恶意文件。
用户可使用系统默认的沙箱防护规则，也可自行创建规则。系统提供6个默认的沙箱防护规则predef_low、
predef_middle、predef_high、predef_pe、no_sandbox和predef_emergency：
l predef_low -- 宽松的沙箱检测策略。此规则开启域名白名单、可信证书验证，扫描
HTTP/FTP/POP3/SMTP/IMAP4/SMB协议流量，将PE类型文件作为检测对象。

<!-- 来源页 2170 -->
l predef_middle -- 中等的沙箱检测策略。此规则开启域名白名单、可信证书验证，扫描
HTTP/FTP/POP3/SMTP/IMAP4/SMB协议流量，将PE、APK、JAR、MS-Office、PDF文件作为检测对象。
l predef_high -- 严格的沙箱检测策略。此规则扫描HTTP/FTP/POP3/SMTP/IMAP4/SMB协议流量，将所有文件
类型（PE、APK、JAR、MS-Office、PDF、SWF、RAR、ZIP以及Script）作为检测对象。
l predef_pe – 仅支持PE文件检测的沙箱检测策略。此规则扫描HTTP/FTP/POP3/SMTP/IMAP4/SMB协议流量，
将PE文件作为检测对象。
l no_sandbox – 此规则不进行任何沙箱检测。
l predef_emergency - 重保模式模板，全面检测所有文件类型和协议类型，发现恶意文件后，重置恶意链接连
接。
开启/关闭云影或者智影
开启云影或者智影，在全局配置模式下使用以下命令：
sandbox {cloud-server-check | local-server-check} enable
l
cloud-server-check | local-server-check - 指定开启云影（cloud-server-check）或者智影
（local-server-check）。
在全局配置模式下，使用no sandbox {cloud-server-check | local-server-check} enable命令关闭
云影或者智影。
配置智影
配置智影的IP地址等参数，在全局配置模式下使用以下命令：
sandbox local-server address ip-address vrouter vr-name [port port]
l
address ip-address - 指定智影的IP地址。
l
vrouter vr-name - 指定智影所属虚拟路由器。
l
port port - 指定智影所属端口号，默认为443。
在全局配置模式下，使用no sandbox local-server address命令删除智影的参数配置。
创建沙箱防护Profile
沙箱防护Profile用于指定域名白名单，配置可疑文件识别标准。创建沙箱防护Profile，在全局配置模式下
使用以下命令：
sandbox-profile sandbox-profile-name

<!-- 来源页 2171 -->
l
sandbox-profile-name - 指定所创建的沙箱防护Profile的名称，并且进入该沙箱防护Profile的配置
模式。如果指定名称已存在，则直接进入沙箱防护Profile配置模式。
使用no sandbox-profile sandbox-profile-name删除指定的沙箱防护Profile。
开启域名白名单
域名白名单中预定义安全域名，当文件的来源是域名白名单中的域名时，此文件被认为是合法文件，不会被
上传到云影或者智影进行检测。
开启域名白名单，在沙箱防护Profile配置模式下，使用如下命令：
allowlist enable
使用no allowlist enable命令关闭域名白名单功能。
可信证书验证
系统支持对PE文件进行可信证书验证，即如文件的签名证书是可信的，系统将不对其进行检测。
开启可信证书验证，在沙箱防护Profile配置模式下，使用如下命令：
certificate-validation enable
使用no certificate-validation enable命令关闭可信证书验证功能。
指定可疑文件识别标准
将符合标准的文件判断为可疑文件，并上传到云影或者智影进行检测。可疑文件的检查结果决定文件是合法
文件或是恶意文件。
用户可设置如下识别标准：
将指定类型的文件识别为可疑文件，并将可疑文件上传至云影或者智影进行检测。支持识别PE（.exe）、
APK、JAR、MS-Office、PDF、SWF、RAR、ZIP、ELF、Script以及其他文件为可疑文件。在沙箱防护
Profile配置模式下，使用如下命令指定类型：
file-type {pe | apk | jar | swf | ms-office | pdf | rar | zip | elf | script | other} [use-server [cloudserver | local-server]
l
pe - 将PE（.exe）文件作为检测对象。
l
apk - 将Android安装文件作为检测对象
l
jar - 将Java文件作为检测对象。
l
swf - 将Flash文件作为检测对象。
l
ms-office - 将Windows Office文件识别为可疑文件。

<!-- 来源页 2172 -->
l
pdf - 将PDF文件作为检测对象。
l
rar | zip - 将压缩文件作为检测对象。
l
elf - 将ELF文件作为检测对象。
l
script - 将Script文件作为检测对象。
l
other - 将除上述文件类型以外的其他类型文件作为检测对象。
l
use-server [cloud-server | local-server] - 指定将可疑文件上传至云影（cloud-server）或者智影
（local-server）进行检测。默认情况下会上传至云影进行检测。
取消指定类型，使用no file-type {pe | apk | jar | swf | ms-office | pdf | rar | zip | elf | script |
other}命令。不指定类型表示沙箱防护功能不将任何文件识别为可疑文件。
指定协议类型
扫描指定类型的协议报文并指定该协议可疑流方向。支持扫描HTTP、FTP、POP3、SMTP、IMAP4及SMB
协议报文。对于SMB协议，系统还支持断点续传场景下的文件过滤和阻断。在沙箱防护Profile配置模式下，
使用如下命令指定协议类型：
protocol {http | ftp | imap4 | pop3 | smtp | smb} direction {download | upload | both}
l
http | ftp | imap4 | pop3 | smtp | smb - 指定协议类型。
l
download | upload | both - 指定该协议可疑流方向，包含上传upload、下载download、双向
both。
不指定协议类型，使用no protocol {http | ftp | imap4 | pop3 | smtp | smb}命令。不指定协议类型表示
沙箱防护功能不扫描任何协议的报文。
上述各个标准的逻辑关系为或。
指定对恶意文件的处理动作
当系统判断可疑文件为恶意后，将按指定的动作处理恶意文件。指定系统处理动作，在沙箱防护Profile配置
模式下，使用以下命令：
action {reset | log-only}
l
reset - 指定该参数后，系统发现恶意文件后，重置恶意链接连接，并记录威胁日志和云沙箱日志。
l
log-only – 指定该参数后，系统发现恶意文件后，对流量放行，仅记录日志信息（威胁日志和云沙箱日
志）。

<!-- 来源页 2173 -->
禁用可疑文件上传
系统在认定文件为可疑文件后，默认情况下，会上传该可疑文件文件到云影或者智影进行检测。用户可以根
据需求禁用可疑文件上传，即该可疑文件将不会被上传到云影或者智影。在沙箱防护Profile配置模式下，使
用以下命令：
file-upload-disable
使用no file-upload-disable命令取消禁用可疑文件上传，即恢复默认上传可疑文件功能。
绑定沙箱防护Profile到策略规则
将沙箱防护Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据沙箱防护Profile配置进行
沙箱防护检查。绑定沙箱防护Profile到策略规则，在策略规则配置模式下使用以下命令：
sandbox {sandbox-profile-name | predef_low | predef_middle | predef_high | no-sandbox |
predef_emergency | predef_pe}
l
sandbox-profile-name – 指定绑定到策略规则的沙箱防护Profile的名称。
l
predef_low – 绑定名为predef_low的预定义沙箱防护Profile到策略规则。
l
predef_middle – 绑定名为predef_middle的预定义沙箱防护Profile到策略规则。
l
predef_high – 绑定名为predef_high的预定义沙箱防护Profile到策略规则。
l
no-sandbox - 绑定名为no-sandbox的预定义沙箱防护Profile到策略规则。
l
predef_emergency - 绑定名为predef_emergency的预定义沙箱防护Profile到策略规则。
l
predef_pe - 绑定名为predef_pe的预定义沙箱防护Profile到策略规则。
在策略规则配置模式下使用该命令no的形式取消沙箱防护Profile的绑定：no sandbox
绑定沙箱防护Profile到安全域
将沙箱防护Profile绑定到安全域后，系统将会对安全域中的流量根据沙箱防护Profile配置进行沙箱防护检
查。绑定沙箱防护Profile到安全域，在安全域配置模式下使用以下命令：
sandbox enable {sandbox-profile-name | predef_low | predef_middle | predef_high | nosandbox | predef_emergency | predef_pe}
l
sandbox-profile-name – 指定绑定到安全域的沙箱防护Profile的名称。
l
predef_low – 绑定名为predef_low的预定义沙箱防护Profile到安全域。
l
predef_middle – 绑定名为predef_middle的预定义沙箱防护Profile到安全域。
l
predef_high – 绑定名为predef_high的预定义沙箱防护Profile到安全域。

<!-- 来源页 2174 -->
l
no-sandbox - 绑定名为no-sandbox的预定义沙箱防护Profile到安全域。
l
predef_emergency - 绑定名为predef_emergency的预定义沙箱防护Profile到安全域。
l
predef_pe - 绑定名为predef_pe的预定义沙箱防护Profile到安全域。
在安全域配置模式下使用该命令no的形式取消沙箱防护Profile的绑定：no sandbox enable
开启良性文件上报
开启良性文件上报，系统在认定文件为良性文件时，即上报该文件相关的沙箱日志。默认情况下，系统不对
良性文件结果记录日志。开启良性文件上报，在全局配置模式下，使用以下命令：
sandbox benign-file report enable
使用no sandbox benign-file report enable关闭良性文件上报。
开启灰文件上报
灰文件指无法断定其是良性文件或恶意文件的所有其他文件。开启灰文件上报，系统在认定文件为灰文件
时，将上报该文件相关的沙箱日志。默认情况下，系统不对灰文件结果记录日志。开启灰文件上报，在全局
配置模式下，使用以下命令：
sandbox greyware report enable
使用no sandbox greyware report enable关闭灰文件上报。
指定文件检测上限
系统将小于指定大小的文件作为检测对象。配置文件检测上限，在全局配置模式下，使用以下命令：
sandbox file-type {pe | apk | jar | swf | ms-office | pdf | rar | zip |elf | script | other} max-filesize size
l
pe - 将PE（.exe）文件作为检测对象。
l
apk - 将Android安装文件作为检测对象
l
jar - 将Java文件作为检测对象。
l
swf - 将Flash文件作为检测对象。
l
ms-office - 将Windows Office文件识别为可疑文件。
l
pdf - 将PDF文件作为检测对象。
l
rar | zip - 将压缩文件作为检测对象。
l
elf - 将ELF文件作为检测对象。
l
script - 将Script文件作为检测对象。

<!-- 来源页 2175 -->
l
other - 将除上述文件类型以外的其他类型文件作为检测对象。
l
max-file-size size - 指定文件大小。系统将小于指定大小的文件作为检测对象。
使用no sandbox file-type {pe | apk | jar | swf | ms-office | pdf | rar | zip | elf | script | other}
max-file-size size命令取消文件检测上限配置。
添加威胁条目到信任列表
威胁列表中的威胁条目的来源有以下3种方式：
l
设备收集可疑流量上传至云影或者智影。当云影或者智影确认其为恶意文件后，向设备返回结果及威胁
MD5值，该威胁条目将显示在威胁列表中。
l
设备发现可疑文件并在云影或者智影中查询到威胁MD5值，该威胁条目将显示在威胁列表中。
l
设备获取到云平台同步的威胁MD5信息后，当本地命中该威胁时，系统威胁列表中显示该威胁条目。
用户可将威胁条目，加入到信任列表中。信任列表中的条目一旦被匹配，对应的流量将被无条件放行，不受
沙箱防护规则中动作的控制。
在任何模式下，使用以下命令在信任列表中添加或移除威胁条目：
exec sandbox-threat value {trust | untrust}
l
value – 指定威胁条目的MD5的值。
l
trust – 将指定的威胁条目加入到信任列表。
l
untrust – 将指定的威胁条目从信任列表中移除。
显示沙箱防护信息
显示沙箱防护profile信息
在任何模式下，输入以下命令显示沙箱防护profile信息：
show sandbox-profile [sandbox-profile-name]
显示沙箱防护状态信息和上传统计信息
在任何模式下，输入以下命令显示沙箱防护状态信息和上传统计信息：
show sandbox status
显示沙箱威胁列表的威胁条目信息
在任何模式下，输入以下命令显示沙箱威胁列表的威胁条目信息：

<!-- 来源页 2176 -->
show sandbox threat-entry info
显示沙箱防护全局配置信息
在任何模式下，输入以下命令显示沙箱防护全局配置信息，包括已配置的沙箱检测的文件大小限制、良性文
件上报功能是否开启、灰文件上报功能是否开启：
show sandbox configuration
配置沙箱白名单更新
默认情况下，系统会每日自动更新沙箱域名白名单，用户可以根据需要更改更新配置。沙箱白名单更新配置
包括：
l 配置沙箱白名单更新模式
l 配置更新传输协议
l 配置更新服务器
l 指定HTTP代理服务器
l 指定更新时间
l 立即更新
l 导入沙箱白名单文件
l 显示沙箱白名单信息
l 显示沙箱白名单更新配置信息
配置沙箱白名单更新模式
系统支持手动和自动两种更新方式。配置沙箱白名单更新方式，在全局配置模式下，使用以下命令：
sandbox allowlist update mode {auto | manual}
l
auto – 指定自动更新沙箱白名单。该方式为系统的默认更新方式。
l
manual – 指定手动更新沙箱白名单。
在全局配置模式下使用该命令no的形式恢复默认更新模式：
配置更新传输协议
系统支持通过HTTP和HTTPS对沙箱白名单进行更新，默认为HTTPS。配置沙箱白名单更新的传输协议为
HTTP，在全局配置模式下，使用以下命令：
sandbox allowlist update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：

<!-- 来源页 2177 -->
no sandbox allowlist update protocol HTTP
no sandbox allowlist update mode
配置更新服务器
系统提供默认的沙箱白名单更新服务器，即update1.hillstonenet.com和update2.hillstonenet.com，
同时用户也可以根据需要配置其它更新服务器下载最新沙箱域名白名单。最多可配置3个。配置更新服务
器，在全局配置模式下，使用以下命令：
sandbox allowlist update {server1 | server2 | server3} {ip-address | domain-name}
[vroutervrouter-name] [src-interface src-interface-name]
l
server1 | server2 | server3 – 指定将要配置的服务器，服务器支持双栈协议，可配置IPv4地址和IPv6
地址。server1的默认值为update1.hillstonenet.com，server2的默认值为
update2.hillstonenet.com。
l
ip-address | domain-name – 指定更新服务器的名称，可以是IP地址形式（ip-address）也可以是
域名形式（domain-name，例如update1.hillstonenet.com）。
l
vrouter vrouter-name– 指定更新服务器绑定的虚拟路由器。若不指定则默认是trust-vr。
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，沙箱白名单更新时将通过该源接口对更新服务器发起访问。若不指定，则默认使用管理口作为源接
口。
在全局配置模式下，使用该命令no的形式取消更新服务器的指定：
no sandbox allowlist update {server1 | server2 | server3}
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保特征库能够正常升级，需要在设备上指定代理服务器
的IP地址和端口号。
为沙箱域名白名单升级指定代理服务器，在全局配置模式下，使用如下命令：
sandbox allowlist update proxy-server {main | backup} ip-address port-number
l
main | backup – 使用main参数指定主代理服务器，使用backup指定备份代理服务器。
l
ip-address port-number – 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no sandbox allowlist update proxy-server {main | backup}命令。

<!-- 来源页 2178 -->
指定更新时间
默认情况下，系统采用自动模式每日更新沙箱域名白名单，并且为避免服务器流量过大，每日更新时间是随
机的。用户可以根据需要指定沙箱白名单更新的频率和时间，在全局配置模式下，使用以下命令：
sandbox allowlist update schedule {daily | weekly {mon | tue | wed | thu | fri | sat | sun} |
monthly date} [HH:MM]
l
daily – 指定频率为每天更新。
l
weekly {mon | tue | wed | thu | fri | sat | sun} – 指定频率为每周更新。mon | tue | wed | thu | fri
| sat | sun用来指定每周更新的日期。
l
monthly date - 指定频率为每月更新。date用来指定每月更新的日期，取值范围为1到31。如果某月
不包含所指定的日期（比如2月没有30号），则该月不会自动升级。
l
HH:MM – 指定更新的时间，例如09：00。
立即更新
无论更新模式为手动还是自动，用户都可以随时使用以下命令更新沙箱白名单。立即更新沙箱白名单，在任
何模式下，使用以下命令：
exec sandbox allowlist update
l
exec sandbox allowlist update – 仅对当前沙箱白名单与更新服务器最新发布域名白名单的不同部
分进行更新。
导入沙箱白名单文件
在某些情况下，用户设备可能无法连接到更新服务器对沙箱白名单进行更新，针对这一问题，系统提供沙箱
白名单文件导入功能，即通过FTP、TFTP服务器或者U盘将沙箱白名单文件导入到设备，从而更新设备的沙
箱白名单。导入沙箱白名单文件，在执行模式下，使用以下命令：
import sandbox allowlist from {ftp server ip-address [user user-name password password] |
tftp server ip-address } [vrouter vr-name] file-name
l
ip-address – 指定FTP或者TFTP服务器的IP地址。
l
user user-name password password – 指定FTP服务器的用户名和密码。
l
vrouter vr-name – 指定FTP或者TFTP服务器所属的VRouter。
l
file-name – 指定导入的沙箱白名单文件的名称。

<!-- 来源页 2179 -->
显示沙箱白名单信息
用户可以随时使用相应的show命令查看设备的沙箱白名单信息，包括沙箱白名单版本以及发布日期。查看
沙箱白名单信息，在任何模式下使用以下命令：
show sandbox allowlist info
显示沙箱白名单更新配置信息
用户可以随时使用相应的show命令查看设备上的沙箱白名单更新信息，包括更新服务器信息、更新模式、
更新频率及时间以及白名单更新状况等。查看沙箱白名单更新配置信息，在任何模式下使用以下命令：
show sandbox allowlist update

<!-- 来源页 2180 -->
入侵防御
入侵防御系统（Intrusion Prevention System）简称IPS，能够实时监控多种网络攻击并根据配置对网络
攻击进行阻断等操作。
系统的入侵防御功能能够实现完整的基于状态的检查，从而极大降低误报率。当设备开启多项应用层数据检
测功能时，启用入侵防御功能不会导致设备性能的明显下降。另外，系统默认每天通过特征服务器自动更新
特征库，保证特征的完整性和正确性。
l 如接口开启了IPv6功能，IPS支持对IPv6地址进行扫描。
l 结合SSL代理功能，IPS支持对HTTPS流量进行扫描。
IPS检测及报告流程
入侵防御功能对流量的检测包括两部分，分别是特征匹配和协议解析：
l 协议解析：对流量所在协议进行分析，发现流量不符合协议的规定后，系统会根据配置处理流量（记录日志、重
置、阻断）。此种检测在入侵防御规则的协议部分进行配置。
l 特征匹配：提取流量的元素，对其进行特征匹配，发现其与特征库中特征相匹配后，系统会根据配置处理流量
（记录日志、重置、阻断）。此种检测在入侵防御规则的特征集部分进行配置。
注意: 入侵防御功能受许可证控制，即为支持入侵防御功能的设备安装入侵防御（IPS）许可证或
威胁防护（TP）许可证后，功能才可使用。
特征介绍
特征ID作为特征的唯一标识，根据协议进行分类。特征ID由两部分构成，分别为协议ID（第1位或者第1和
第2位）和攻击特征ID（后5位），例如ID“605001”中，“6”表示Telnet协议，“05001”表示攻击特
征ID。协议ID与协议的对应关系下表所示：
协议ID
协议
协议ID
协议
协议ID
协议
协议ID
协议
1
DNS
7
Other-TCP
13
TFTP
19
NetBIOS
2
FTP
8
Other-UDP
14
SNMP
20
DHCP
3
HTTP
9
IMAP
15
MySQL
21
LDAP
4
POP3
10
Finger
16
MSSQL
22
VoIP
5
SMTP
11
SUNRPC
17
Oracle
-
-
6
Telnet
12
NNTP
18
MSRPC
-
-

<!-- 来源页 2181 -->
上表中，“Other-TCP”表示除表中已列出的标准TCP协议以外的其他TCP协议；“Other-UDP”表示除表
中已列出的标准UDP协议以外的其他UDP协议。
IPS入侵防御配置准备工作
使用IPS入侵防御功能前，必须完成以下准备工作：
1. 确认StoneOS版本支持IPS功能。
2. 安装入侵防御（IPS）许可证或威胁防护（TP）许可证，然后重启设备。设备成功重启后，IPS功能即处于开启状
态。
注意: 开启入侵防御功能后，部分平台的最大并发连接数会减少。关于系统最大并发连接数变化的
详细信息，请参阅"系统最大并发连接数变化" 在第889页。
IPS入侵防御配置流程和指导
配置流程
IPS入侵防御功能配置的流程如下：
1. 开启系统IPS入侵防御功能，并指定IPS工作模式，详细配置请参阅“"配置入侵防御全局参数" 在第2256页”章
节。系统支持两种IPS工作模式，分别是只记录日志模式和IPS模式。系统默认情况下工作在IPS模式下。
l 只记录日志模式：提供协议异常和网络攻击行为的告警、日志功能，不对检出攻击做重置和阻断操作。
l IPS模式：在提供协议异常和网络攻击行为的日志功能的同时，还对检出攻击做重置和阻断操作。
提示: IPS入侵防御功能默认为开启状态，如无需切换IPS工作模式，可跳过该步骤。
2. （可选）为保障系统IPS入侵防御检测能力，请将IPS特征库更新至最新版本，详见"更新IPS特征库" 在第2264
页。
3. 根据安全防护需求，创建IPS入侵防御模板（简称“IPS模板”），并为该IPS模板配置相关的检测和防护规则，
如特征集规则、Web防护、口令防护、异常流量检测、抓包取证等。详细配置请参阅“配置IPS入侵防御模板”
章节。
4. （可选）根据用户需求，调整IPS入侵防御功能全局参数配置，如日志聚合、HTTP多重解码、抓取完整的威胁数
据等。若不进行调整，则使用系统默认配置。

<!-- 来源页 2182 -->
5. IPS模板配置完成后，用户需要将IPS模板绑定到指定安全域、策略规则或ZTNA策略上，才可执行相应的安全防
护能力。详细配置请参阅“"将IPS模板绑定到安全域或策略规则上" 在第2253页”章节。
l 将IPS Profile绑定到安全域的不同方向（出方向、入方向、双向），可将IPS功能应用到安全域不同方向
的流量。
l 将IPS Profile绑定到策略规则上，可将IPS功能应用到与策略规则相匹配的流量。如果需要IPS对HTTPS流
量进行扫描，需要为此条策略启用SSL代理功能，详细说明请参阅“对HTTPS流量进行IPS检测”。
l 将IPS Profile绑定到ZTNA策略上，可对与ZTNA策略相匹配的流量进行入侵防御检测和处理。详细配置请
参阅配置ZTNA策略。
注意: 如果策略规则绑定了IPS Profile，同时源安全域和目的安全域也绑定了IPS Profile，系
统IPS检测的优先级由高到低依次为：策略规则的IPS Profile > 目的安全域的IPS Profile >
源安全域的IPS Profile。
6. 完成上述步骤配置后，当系统发现入侵攻击，会生成相应的威胁日志信息。威胁日志信息中包含检测出的攻击特
征ID，用户可以通过运行show logging threat命令查看相关威胁日志的详情。
7. （可选）当用户发现某些IPS威胁告警存在误报时，可以通过配置IPS入侵防御白名单功能，对匹配到白名单的威
胁不再上报告警或阻断，以降低威胁的误报率。
配置指导
在IPS入侵防御功能配置中，多处配置都会对最终的攻击处理行为产生影响，因此，系统在决定处理行为时
遵循以下原则：
l IPS工作模式具有最高优先级。当系统的IPS工作模式指定为只记录日志模式时，无论其他相关配置是否指定动
作，最终的结果均为仅记录日志。
l 用户创建多个特征集规则且这些特征集规则中包含同一个特征时，如果不同特征集规则指定的行为不一致，那
么，当发现某个攻击的特征符合多个特征集规则中的同一个特征时：
l 总是采取更严格的行为对攻击进行处理。哪个特征集规则设置的行为更严格，则使用哪个特征集规则设置
的行为对攻击进行处理。严格程度：阻断IP > 阻断服务> 重置> 只记录日志> 默认。对于阻断IP和阻断服
务，如果在一个特征集规则中的配置为阻断IP15s，另外一个特征集规则中的配置为阻断服务30s，则，采
取的行为时阻断IP30s。
l 由于新建特征集时系统默认的处理动作为“默认”，其严格程度是最低的，所以只要用户重新选择了其他
动作（阻断IP 、阻断服务、重置、只记录日志），系统处理攻击时，总是会优先处理用户重新设置的

<!-- 来源页 2183 -->
动作。例如：特征集A采用默认动作，而某一特征的默认动作为“重置”，而另一特征集B的动作被用户设
置为了“只记录日志”，那么最终对匹配该特征的攻击的处理方式为用户设置的“只记录日志”。
l 只要一个特征集规则中配置了抓包，就会对异常数据包进行抓包。
l 通过选择特征创建的特征集规则所配置的行为，优先级高于通过过滤特征创建的特征集规则所配置的行
为。
l 对于已绑定到安全域或者已绑定到策略规则的IPS Profile，用户可以修改IPS Profile的配置。在对IPS Profile进
行修改时，系统对相关会话的处理遵循以下原则：
l 当IPS Profile的引用关系发生变化时，该变化对于已经建立的会话不能立即生效，即当将绑定到安全域
trust的IPS Profile由IPS-pro1变为IPS-pro2后，已经建立的会话仍使用IPS-pro1，只有新建立的会话使
用IPS-pro2。更改IPS Profile引用关系后，执行clear session命令可使配置对已有会话立即生效。
l 修改已被引用的IPS Profile中的特征集，变化将对已有会话立即生效。
注意: 对于不带硬盘的设备和带硬盘的A1600/A1800/A2200设备，开启抓包取证功能时，需同时
开启“加入用户体验改进计划”并开启云·景的威胁日志上报，抓包取证功能才能生效。在该情况
下，防火墙设备上将无法查看到抓包取证的报文数据，系统会将抓包取证的报文数据和威胁日志信
息上送至云·景，安全运营人员可以根据抓包取证的证据信息对威胁日志信息进行分析研判。
对HTTPS流量进行IPS检测
如果需要IPS对HTTPS流量进行扫描，需要为HTTPS流量所匹配的策略规则配置SSL代理功能。系统将为匹
配此条策略的HTTPS流量根据SSL代理Profile解密HTTPS流量，对解密后的数据根据IPS Profile进行IPS检
测。根据安全策略规则的配置不同，系统将进行如下操作：
安全策略规则配置
操作
启用SSL代理
不启用IPS
根据SSL代理Profile解密HTTPS流量，对解密后的数据不进行IPS检测。
启用SSL代理
启用IPS
根据SSL代理Profile解密HTTPS流量，对解密后的数据根据IPS Profile进行IPS检测。
不启用SSL代理
启用IPS
对HTTP流量根据IPS Profile进行IPS检测。对HTTPS流量不进行解密，不进行IPS检测，只
进行转发。
当安全策略规则所关联的安全域也启用IPS时，系统也将进行如下操作：
安全策略规则配置
安全域配置
操作
启用SSL代理
不启用IPS
启用IPS
根据SSL代理Profile解密HTTPS流量，对解密后的数据根据安全域配
置的IPS Profile进行IPS检测。

<!-- 来源页 2184 -->
安全策略规则配置
安全域配置
操作
启用SSL代理
启用IPS
启用IPS
根据SSL代理Profile解密HTTPS流量，对解密后的数据根据安全策略
规则中配置的IPS Profile进行IPS检测。
不启用SSL代理
启用IPS
启用IPS
对HTTP流量根据安全策略规则中配置的IPS Profile进行IPS检测。对
HTTPS流量不进行解密，不进行IPS检测，只进行转发。
提示: 更多关于SSL代理Profile的配置，请参阅SSL代理章节。
配置IPS入侵防御模板
开始之前
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。
配置IPS入侵防御模板（简称“IPS模板”）并将其绑定到指定安全域或策略规则上，系统才会对符合安全防
护策略的流量执行防御功能。启用并指定使用的IPS模板，请参阅"将IPS模板绑定到安全域或策略规则上" 在
第2253页。
系统提供多个预定义的IPS入侵防御模板（如下表所示），用户可以轻松地将这些模板应用于特定的安全区
域或策略规则上，以适应多样化的使用需求。同时，系统还支持用户自定义IPS入侵防御模板的功能，允许
用户根据自身需求创建个性化的模板，并为该IPS模板设置相应的检测与防护规则。
规则名称
描述
predef_default
通用严格型模板，包含可信度为中和高的攻击检测，对威胁进行检测，且处理行为默认为各
IPS特征的默认动作，适用于常规部署场景。
predef_loose
通用宽松型模板，包含所有类型的攻击检测，对威胁进行检测且处理行为默认为只记录日
志，适用于常规部署场景。
DMZ-server
针对DMZ服务器的模板，包含除TFTP和NETBIOS协议之外的所有攻击检测，对威胁进行检
测且处理行为默认为只记录日志。
web-server
针对Web服务器的模板，包含所有Web攻击类检测，以及对SQL注入和XSS注入的通用检
测，对威胁进行检测且处理行为默认为只记录日志。
Windows-server
针对Windows操作系统服务器的模板，包含针对Windows系统攻击的检测规则，对威胁进
行检测且处理行为默认为只记录日志。
General-server
针对常规类服务器的模板，包含针对漏洞扫描、拒绝服务攻击和后门木马类的攻击检测规
则，对威胁进行检测且处理行为默认为只记录日志。

<!-- 来源页 2185 -->
规则名称
描述
Unix-like-server
针对类Unix系统服务器的模板，包含针对Linux、Solaris系统攻击的检测规则，对威胁进行
检测且处理行为默认为只记录日志。
predef_critical
通用超严格模板，包含最新时段高危类型的攻击检测，对威胁进行检测且处理行为默认为重
置，适用于常规或需重点防护的部署场景。
predef_emergency
重保检测模板，配置了大多数重点防护的规则，防护能力较强但存在一些误报。适用于攻防
演练的场景。
no-ips
不进行入侵防御检测。
IPS入侵防御模板配置包含以下内容：
l "创建IPS模板并进入IPS Profile配置模式" 在第2183页
l "配置特征集" 在第2184页
l "配置Web防护信息" 在第2193页
l "配置口令防护信息" 在第2217页
l "配置IPS异常流量检测" 在第2224页
l "抓包取证" 在第2303页
创建IPS模板并进入IPS Profile配置模式
开始之前
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。
创建指定名称的IPS Profile并进入IPS Profile配置模式。如果指定的名称已存在，则直接进入IPS Profile
配置模式。
注意: 非根VSYS中同样支持预定义IPS Profile。
在全局配置模式下，使用以下命令，创建IPS模板并进入IPS Profile配置模式：
ips profile {no-ips | predef_default | predef_loose| predef_critical | DMZ-server | Generalserver | web-server | Unix-like-server | Windows-server | profile-name}

<!-- 来源页 2186 -->
l
no-ips - 指定使用名为“no-ips”的预定义IPS Profile，含义为不做IPS检测。
l
predef_default - 指定使用名为“predef_default”的预定义IPS Profile，包含可信度为中和高的所
有IPS 特征，对威胁进行检测并执行规则默认动作。
l
predef_loose - 指定使用名为“predef_loose”的预定义IPS Profile，包含所有类型的IPS特征，对
威胁进行检测且处理行为默认为只记录日志。
l
predef_critical - 指定使用名为“predef_critical”的预定义IPS Profile，包含最新时段高危类型的
攻击检测，对检测效果要求严格，且处理行为默认为重置。
l
DMZ-server - 指定使用名为“DMZ-server”的预定义IPS Profile，包含除TFTP和NETBIOS协议之
外的所有攻击检测，对威胁进行检测且处理行为默认为只记录日志。
l
General-server - 指定使用名为“General-server”的预定义IPS Profile，包含针对漏洞扫描、拒绝
服务攻击和后门木马类的攻击检测规则，对威胁进行检测且处理行为默认为只记录日志。
l
web-server - 指定使用名为“web-server”的预定义IPS Profile，包含所有Web攻击类检测，以及
对SQL注入和XSS注入的通用检测，对威胁进行检测且处理行为默认为只记录日志。
l
Unix-like-server - 指定使用名为“Unix-like-server”的预定义IPS Profile，包含针对Linux、
Solaris系统攻击的检测规则，对威胁进行检测且处理行为默认为只记录日志。
l
Windows-server - 指定使用名为“Windows-server”的预定义IPS Profile，包含针对Windows系
统攻击的检测规则，对威胁进行检测且处理行为默认为只记录日志。
l
profile-name -指定IPS Profile的名称。系统支持创建最多64个自定义IPS Profile，每个非根VSYS
下可以创建最多4个自定义IPS Profile。
在全局配置模式下，使用以下命令，删除指定名称的IPS Profile：
no ips profile profile-name
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)#
配置特征集
特征集是一组预定义的规则，用于匹配已知的攻击特征。它也是漏洞防护的重要支撑手段，为系统提供了识
别攻击行为的依据。用户通过配置特征集规则，可以指定系统需要检测和防护的漏洞类型，从而保护网络和
应用程序免受相应漏洞的攻击，提高网络安全性。例如，针对Web应用的SQL注入漏洞，用户可以配置相关

<!-- 来源页 2187 -->
的特征集规则，让系统依据这些规则对进入Web应用的流量进行检测和防护，一旦发现符合规则的攻击行
为，立即采取阻断或其他预设的安全措施。
特征集配置包括以下内容：
l 为指定IPS模板创建特征集规则
l 启用/禁用指定特征
开始之前
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。
前置条件
为保障系统入侵防御检测效果，请确保系统中的IPS特征库已是最新版本。详见"更新IPS特征库" 在第2264
页。
为指定IPS模板创建特征集规则
为指定IPS模板创建特征集规则时，用户可按需选择过滤特征集和选择特征集两种方式，对特征库进行筛选
与检索，从而选择出需要使用的特征集规则。
l 过滤特征集：由过滤条件筛选出来的特征集合，用户可以通过该方式快速选择出系统已分类的特征。
l 选择特征集：在特征库中一一检索出来的特征集合，用户可以通过该方式快速选择某个指定的特征。
注意: 用户创建多个特征集规则且这些特征集规则中包含同一个特征时，如果不同特征集规则指定
的行为不一致，那么，当发现某个攻击的特征符合多个特征集规则中的同一个特征时：
l
总是采取更严格的行为对攻击进行处理。哪个特征集规则设置的行为更严格，则使用哪个特征
集规则设置的行为对攻击进行处理。严格程度：阻断IP > 阻断服务> 重置> 只记录日志> 默
认。对于阻断IP和阻断服务，如果在一个特征集规则中的配置为阻断IP15s，另外一个特征集
规则中的配置为阻断服务30s，则，采取的行为时阻断IP30s。
l
由于新建特征集时系统默认的处理动作为“默认”，其严格程度是最低的，所以只要用户重新
选择了其他动作（阻断IP 、阻断服务、重置、只记录日志），系统处理攻击时，总是会优
先处理用户重新设置的动作。例如：特征集A采用默认动作，而某一特征的默认动作为“重
置”，而另一特征集B的动作被用户设置为了“只记录日志”，那么最终对匹配该特征的攻击
的处理方式为用户设置的“只记录日志”。

<!-- 来源页 2188 -->
l
只要一个特征集规则中配置了抓包，就会对异常数据包进行抓包。
l
通过选择特征创建的特征集规则所配置的行为，优先级高于通过过滤特征创建的特征集规则所
配置的行为。
创建过滤特征集并进入过滤规则配置模式
进行特征集配置时，可通过过滤条件筛选出特定的特征。
在IPS Profile配置模式下，使用以下命令，创建过滤特征集并进入过滤规则配置模式：
filter-class id [description name]
l
id - 指定过滤特征集的ID。取值范围为1~32。
l
description name - 指定过滤特征集的名称。取值范围为1~63个字符。
在IPS Profile配置模式下，使用以下命令，删除过滤特征集：
no filter-class id
［命令实例］
hostname(config)# ips profile test
hostname(config-http-sigset)# filter-class 1 description test2
通过软件名称筛选相关特征
通过过滤规则筛选特征时，可配置affected-software（软件名称）参数，筛选出指定软件相关的特征。
在过滤规则配置模式下，使用以下命令，配置affected-software（软件名称）参数：
affected-software {Apache | IE | Firefox | …}
l
Apache | IE | Firefox | … – 指定软件名称。用户可通过在affected-software参数后使用Tab键，查
看完整的软件列表。
在过滤规则配置模式下，使用以下命令，删除affected-software（软件名称）参数配置：
no affected-software {Apache | IE | Firefox | …}
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# filter-class 1
hostname(config-ips-filter-class)# affected-software Apache

<!-- 来源页 2189 -->
通过攻击类型筛选相关特征
通过过滤规则筛选特征时，可配置attack-type（攻击类型）参数，筛选出指定攻击类型的特征。
在过滤规则配置模式下，使用以下命令，配置attack-type（攻击类型）参数：
attack-type {Access-Control | SPAM | Mail | …}
［句法描述］
l
Access-Control | SPAM | Mail | … - 指定攻击类型。用户可通过在attack-type参数后使用Tab键，
查看完整的攻击类型列表。
在过滤规则配置模式下，使用以下命令，删除attack-type（攻击类型）参数配置：
no attack-type {Access-Control | SPAM | Mail | …}
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# filter-class 1
hostname(config-ips-filter-class)# attack-type WEB-PHP
通过组织名称筛选相关特征
通过过滤规则筛选特征时，可配置bulletin-board参数，筛选出指定组织发布的特征。
在过滤规则配置模式下，使用以下命令，配置bulletin-board参数：
bulletin-board {CVE | BID | OSVDB | …}
l
CVE | BID | OSVDB | … - 指定发布漏洞的组织名称。用户可通过在bulletin-board参数后使用Tab
键，查看完整的组织列表。
在过滤规则配置模式下，使用以下命令，删除bulletin-board参数配置：
no bulletin-board {CVE | BID | OSVDB | …}
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# filter-class 1
hostname(config-ips-filter-class)# bulletin-board CVE

<!-- 来源页 2190 -->
通过可信度级别筛选指定特征
通过过滤规则筛选特征时，可配置confidence参数，筛选出指定可信度级别的特征。
在过滤规则配置模式下，使用以下命令，配置confidence（可信度级别）参数：
confidence {Low | Medium | High}
l
Low | Medium | High – 指定特征规则的可信度级别：低、中、高，系统可筛选出指定可信度级别的特
征。
在过滤规则配置模式下，使用以下命令，删除confidence（可信度级别）参数配置：
no confidence {Low | Medium | High}
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# filter-class 1
hostname(config-ips-filter-class)# confidence Low
通过发布时间筛选相关特征
通过过滤规则筛选特征时，可配置issue-date（发布时间）参数，筛选出指定发布时间内的特征。
在过滤规则配置模式下，使用以下命令，配置issue-date（发布时间）参数：
issue-date year
l
year - 指定特征的发布年度。取值范围2004到2020。
在过滤规则配置模式下，使用以下命令，删除issue-date（发布时间）参数配置：
no issue-date year
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# filter-class 1
hostname(config-ips-filter-class)# issue-date 2006
通过指定协议筛选相关特征
通过过滤规则筛选特征时，可配置protocol（协议）参数，筛选出指定协议对应的特征。
在过滤规则配置模式下，使用以下命令，配置protocol（协议）参数：

<!-- 来源页 2191 -->
protocol {DNS | FTP | HTTP | …}
l
DNS | FTP | HTTP | … - 指定协议。用户可通过在protocol参数后使用Tab键，查看完整的协议列表。
在过滤规则配置模式下，使用以下命令，删除protocol（协议）参数配置：
no protocol { DNS | FTP | HTTP | …}
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# filter-class 1
hostname(config-ips-filter-class)# protocol Telnet
通过严重程度筛选指定特征
通过过滤规则筛选特征时，可配置severity（严重程度）参数，筛选出指定严重程度的特征。
在过滤规则配置模式下，使用以下命令，配置severity（严重程度）参数：
severity {Low | Medium | High}
l
Low | Medium | High - 指定严重程度。
在过滤规则配置模式下，使用以下命令，删除severity（严重程度）参数配置：
no severity {Low | Medium | High}
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# filter-class 1
hostname(config-ips-filter-class)# severity Low
通过操作系统筛选指定特征
通过过滤规则筛选特征时，可配置system（操作系统）参数，筛选出指定操作系统对应的特征。
在过滤规则配置模式下，使用以下命令，配置system（操作系统）参数：
system {Windows | Linux | FreeBSD | …}
l
Windows | Linux | FreeBSD | … - 指定操作系统。用户可通过在system参数后使用Tab键，查看完整
的操作系统列表。
在过滤规则配置模式下，使用以下命令，删除system（操作系统）参数配置：

<!-- 来源页 2192 -->
no system { Windows | Linux | FreeBSD | …}
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# filter-class 1
hostname(config-ips-filter-class)# system Linux
创建选择特征集并进入搜索规则配置模式
进行特征集配置时，可通过搜索条件筛选出特定的特征。
在IPS Profile配置模式下，使用以下命令，创建选择特征集并进入搜索规则配置模式：
search-class id [description name]
l
id - 指定选择特征集的ID。取值范围为1~32。
l
description name - 指定选择特征集的名称。取值范围为1~63个字符。
在IPS Profile配置模式下，使用以下命令，删除选择特征集：
no search-class id
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# search-class 1 description test1
通过特征信息检索相关特征
通过搜索规则筛选特征时，可指定特征的信息进行检索。系统将在如下字段中进行模糊检索：特征ID，特征
名称，描述信息，CVE-ID。
在搜索规则配置模式下，使用以下命令，指定特征的信息：
search-condition description
l
description - 指定特征的信息。
在搜索规则配置模式下，使用以下命令，删除指定特征的信息：
no search-condition description
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# search-class 1

<!-- 来源页 2193 -->
hostname(config-ips-filter-class)# search-condition DNS
通过特征ID检索指定特征
通过搜索规则筛选特征时，可配置signature id（特征ID）参数，筛选出指定ID的特征。
在搜索规则配置模式下，使用以下命令，配置signature id（特征ID）参数：
signature id id
l
id - 指定特征ID。
在搜索规则配置模式下，使用以下命令，删除signature id（特征ID）参数配置：
no signature id id
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# search-class 1
hostname(config-ips-filter-class)# signature id 105001
指定流量命中特征的处理动作
指定流量命中特征的处理动作。对于过滤规则和搜索规则筛选出的特征，当流量命中特征时，系统会按照指
定动作进行处理。默认为只记录日志（log-only）。
在过滤规则配置模式或者搜索规则配置模式下，使用以下命令，指定流量命中特征的处理动作：
action {block-ip { permanent | second timeout | hour timeout | day timeout } | block-service
{ permanent | second timeout | hour timeout | day timeout } | log-only | reset | default}
l
block-ip {permanent|second timeout | hour timeout | day timeout } - 匹配该特征后阻断攻击
者IP，并指定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout } - 匹配该特征后指
定阻断攻击者服务，并指定阻断时长。

<!-- 来源页 2194 -->
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
l
default - 匹配该特征后系统将按照特征规则中的动作进行处理。
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# filter-class 1
hostname(config-ips-filter-class)# action log-only
指定预定义特征的处理动作
用户可以修改指定IPS预定义特征的处理动作，从而更灵活地配置入侵防御检测，提升运维效率。用户所配
置的处理动作不会因为升级IPS特征库而恢复默认动作。
修改指定特征规则的处理动作，在全局配置模式下，使用以下命令：
ips signature id action {log-only | reset}
l
id - 指定预定义特征的ID，取值范围为100000-3099999。
l
log-only - 指定处理动作为仅记录日志。系统发现攻击后仅记录日志信息。
l
reset - 指定处理动作为重置。系统发现攻击后将重置连接（TCP）或者发送目标不可达包（UDP），并
且记录日志信息。
恢复指定特征规则的默认处理动作，在全局配置模式下，使用以下命令：
no ips signature id action
启用/禁用指定特征
系统提供以下两种启用/禁用指定特征的CLI配置方式：
1. 针对指定IPS Profile（IPS模板）进行配置：用户可以对某个特定的IPS Profile中的指定特征进行启用或禁用操
作。此配置方式仅对该特定IPS Profile生效，其他引用该特征的IPS Profile不受影响。
2. 针对所有IPS Profile进行全局配置：用户可以对所有IPS Profile中的某个指定特征进行启用或禁用操作。此配置
方式将对全局所有IPS Profile生效，即对所有引用该特征的IPS Profile均会受到此配置的影响。
用户可根据需要，灵活地管理IPS特征的启用或禁用状态。

<!-- 来源页 2195 -->
启用/禁用指定IPS Profile的特征
在IPS Profile配置模式下，使用以下命令，禁用/启用某个特定的IPS Profile中的指定特征：
禁用：disable signature id
启用：no disable signatureid
l
id - 指定被禁用/被启用的特征ID。
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# disable signature 160009
启用/禁用全局所有IPS Profile的特征
在全局配置模式下，使用以下命令，禁用/启用所有IPS Profile中的某个指定特征：
禁用：ips signature id disable
启用：no ips signature id disable
l
id - 指定被禁用/被启用的特征ID。
注意:
l
当某特征在被配置为禁用状态，该特征在特征集下亦为禁用状态。
l
非根VSYS不支持此命令。
［命令实例］
hostname(config)# ips signature 160009 disable
配置Web防护信息
开始之前
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。
本章节包括以下内容：

<!-- 来源页 2196 -->
l 创建Web漏洞检测模板
l 引用Web漏洞检测模板
l 配置可疑用户代理（UA）检测功能
l 指定HTTP请求方法
l Web服务器防护规则配置
创建Web漏洞检测模板
用户可以使用系统预定义的Web漏洞检测模板，也可以自行创建模板。系统最多支持创建65个Web漏洞检
测模板，包括预定义模板和自定义模板。每个非根VSYS下可以创建的自定义Web漏洞检测模板数量，与该
VSYS下可以创建的自定义入侵防御规则数量相同。
系统提供两个预定义的Web漏洞检测模板，预定义Web漏洞检测模板不可被删除和编辑。
模板名称
描述
web_predef_
default
通用Web防护模板。开启了对SQL注入和XSS注入的通用检测，对威胁进行检测和记
录。适用于常规部署场景。
该模板默认被“predef_default”、“web-server”和“General-server”入侵
防御规则引用。
web_predef_
emergency
重保检测Web模板。开启了对敏感目录、SQL注入和XSS注入的严格检测，对威胁进
行检测和记录。适用于攻防演练的场景。
该模板默认被“predef_emergency”入侵防御规则引用。
提示: 从旧版本升级至StoneOS 5.5R12P1及后续版本、StoneOS 5.5R12F1及后续版本后，已
配置Web防护功能的入侵防御规则会被自动转换，保证升级后与升级前防御效果一致。
创建Web漏洞检测模板并进入Web Profile配置模式，在全局配置模式下，使用以下命令：
ips web-profile name
l
name - 指定Web漏洞检测模板的名称，取值范围为1-95个字符。如果指定的名称已存在，则直接进入
Web Profile配置模式。
删除Web漏洞检测模板，在全局配置模式下，使用以下命令：
no ips web-profile name
注意: 如果Web漏洞检测模板已被入侵防御规则引用，则需要先解除引用，否则将无法删除。

<!-- 来源页 2197 -->
引用Web漏洞检测模板
在入侵防御规则中引用Web漏洞检测模板，在IPS Profile配置模式下，使用以下命令：
web-profile name
l
name - 指定需要引用的Web漏洞检测模板的名称。
取消引用Web漏洞检测模板，在IPS Profile配置模式下，使用以下命令：
no web-profile
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# web-profile test
配置可疑用户代理（UA）检测功能
可疑用户代理（User-Agent，简称UA）检测功能可对HTTP请求报文中的User-Agent进行检测，当系统
检测到HTTP请求报文中的User-Agent出现异常时，可以根据用户指定动作进行处理。
l 开启/关闭可疑用户代理检测功能
l 指定可疑用户代理检测处理动作
l 创建User-Agent白名单
l 添加自定义User-Agent字符串
开启/关闭可疑用户代理检测功能
系统支持开启/关闭可疑用户代理（User-Agent，简称UA）检测功能。开启该功能后，可通过识别HTTP报
文中的User-Agent字符串进行可疑信息的检测。该功能默认为关闭状态。
在IPS Profile配置模式下，使用以下命令，开启/关闭可疑用户代理检测功能：
l
开启：suspicious-ua-detection enable
l
关闭：suspicious-ua-detection disable
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# suspicious-ua-detection enable

<!-- 来源页 2198 -->
指定可疑用户代理检测处理动作
开启可疑用户代理检测功能后，用户可以指定相应的处理动作。系统默认处理动作为只记录日志（logonly）。当在HTTP报文中的User-Agent字符串检测出可疑信息时，系统会根据用户指定动作进行处理。
在IPS Profile配置模式下，使用以下命令，指定可疑用户代理检测处理动作：
suspicious-ua-detection action {block-ip {permanent | second timeout | hour timeout | day
timeout} | block-service {permanent | second timeout | hour timeout | day timeout} | log-only
| reset}
l
block-ip - 指定阻断攻击者服务IP。
l
block-service - 指定阻断攻击者服务。
l
permanent - 指定对攻击者IP或者服务进行永久阻断。
l
second timeout | hour timeout | day timeout - 指定对攻击者IP或者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
注意: 若配置好该命令行后再开启可疑用户代理检测功能，配置依旧生效。若用户未开启可疑用户
代理检测功能，该命令行可以配置，但无法生效。
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# suspicious-ua-detection action block-ip day 1
创建User-Agent白名单
创建可疑用户代理检测功能的User-Agent（简称UA）白名单条目。创建后，对于匹配到白名单中UA字符
串的流量，系统将不进行可疑用户代理检测。用户可以将预定义和自定义的UA字符串添加到UA白名单。
在全局配置模式下，使用以下命令，创建User-Agent白名单：
ips suspicious-ua-detection allowlist string
l
string - 指定加入白名单的UA字符串，范围为1-31字符。
在全局配置模式下，使用以下命令，删除指定的User-Agent白名单：
no ips suspicious-ua-detection allowlist string

<!-- 来源页 2199 -->
［命令实例］
hostname(config)# ips suspicious-ua-detection allowlist abc
添加自定义User-Agent字符串
添加可疑用户代理检测功能的自定义User-Agent（简称UA）字符串条目。添加后，系统将对该自定义UA
字符串条目进行检测，当检测出可疑信息时将指定相应的处理动作。最多可以添加16条自定义UA字符串条
目。
在全局配置模式下，使用以下命令，添加自定义User-Agent字符串：
ips suspicious-ua-detection user-define string
l
string - 指定自定义UA字符串，范围为1-31字符。
在全局配置模式下，使用以下命令，删除指定的自定义User-Agent字符串：
no ips suspicious-ua-detection user-define string
［命令实例］
hostname(config)# ips suspicious-ua-detection user-define abc
指定HTTP请求方法
指定系统拒绝的HTTP请求方法。默认情况下，所有HTTP请求方法都是允许的。当系统发现请求方法不允许
时，将直接断开连接。
指定系统拒绝的HTTP请求方法，在Web Profile配置模式下，使用以下命令：
deny-method {connect | delete | get | head | options | post | put | trace | webdav| others}
l
connect | delete | get | head | options | post | put | trace | webdav | others - 指定拒绝的
HTTP请求方法。
在协议配置模式下，使用以下命令，指定系统允许的HTTP请求方法：
no deny-method {connect | delete | get | head | options | post | put | trace | webdav| others}
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# deny-method post

<!-- 来源页 2200 -->
Web服务器防护规则配置
Web服务器防护规则包含对如下攻击行为的检测与防护：高频访问、敏感目录扫描、SQL注入攻击、XSS注
入攻击、外链攻击、盗链攻击、Iframe攻击、访问控制、CC攻击。
系统预定义一个名称为“default”的默认Web服务器防护规则，仅支持以下部分防护功能：敏感目录扫
描、SQL注入检查、XSS注入检查、iframe检查、访问控制、CC防护。该防护规则默认为启用状态，且不能
被禁用和删除。每个Web漏洞检测模板最多配置32个Web服务器防护规则，包括预定义规则和自定义规
则。
如果需要对Web服务器进行防护，用户可以进行如下配置：
l 创建Web服务器防护规则
l 指定域名
l 配置URL高频访问限制功能
l 配置Web站点外链检查功能
l 配置盗链检查功能
l 配置CC防护功能
l 配置Iframe检查功能
l 配置敏感目录扫描检测功能
l 配置SQL注入检查功能
l 配置XSS注入检查功能
l 配置访问控制功能
l 指定Web服务器黑名单的最大URL数目
l 指定Web服务器白名单的最大URL数目
l 启用/禁用Web服务器
创建Web服务器防护规则
创建Web服务器防护规则并进入Web服务器配置模式，在Web Profile配置模式下，使用以下命令：
web-server {default | server_name}
l
default - 配置预定义Web服务器防护规则。
l
server_name - 指定Web服务器防护规则的名称，取值范围为1-95个字符。
删除Web服务器防护规则，在Web Profile配置模式下，使用以下命令：

<!-- 来源页 2201 -->
no web-server server_name
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)#
指定域名
指定Web服务器域名，每个Web服务器最多允许配置5个域名。访问这些域名的流量将会通过Web服务器防
护规则的检查。系统不支持为默认Web服务器指定域名。
在Web服务器配置模式下，使用以下命令，指定Web服务器域名：
domain domain_name
l
domain_name - 指定Web服务器域名，为1到255个字符长度的字符串。
在Web服务器配置模式下，使用以下命令，删除Web服务器域名设置：
no domain domain_name
Web服务器域名遵循从后往前的最长匹配原则。例如，进行以下配置：
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# domain abc.com
hostname(config-web-server)# exit
hostname(config-web-profile)# web-server web_server2
hostname(config-web-server)# domain email.abc.com
完成上述配置后，访问news.abc.com的流量将匹配web_server1；访问www.email.abc.com的流量将
匹配web_server2；访问www.abc.com.cn的流量将匹配默认Web服务器。
配置URL高频访问限制功能
URL高频访问限制功能主要用于防范恶意流量攻击和资源滥用。用户可以通过为指定URL路径配置被访问次
数阈值及阻断IP时间，让系统实时监控并统计URL路径被访问的频率，以实现对频繁访问指定URL路径的源
IP进行限制。当源IP对指定URL路径的访问频率超过设定的阈值，系统便会立即阻断该IP对Web服务器的访
问，在阻断时间结束后，被阻断的IP才可以重新访问Web服务器，以此保障Web 服务器的稳定运行，防范
异常高频访问带来的威胁。

<!-- 来源页 2202 -->
注意: 非根VSYS不支持CC URL限制功能功能。
配置URL路径
为URL高频访问限制功能配置需要监控和统计的URL路径。配置后，系统将对访问该路径的HTTP请求进行访
问频率进行监控和统计。若访问频率超过阈值，系统将阻断该请求的源IP,该IP将无法访问Web服务器。
在Web服务器配置模式下，使用以下命令，配置URL路径：
cc-url url_string
l
url_string - 指定需要监控和统计的URL路径。指定后，包含该路径名称的所有路径也将被监控和统
计。系统会对访问这些路径的HTTP请求进行访问频率检查。若HTTP请求的访问频率超过阈值，会阻断
该请求的源IP，该IP将无法访问Web服务器。例如：配置/home/ab，系统将对访问
/home/ab/login与/home/abc/login的HTTP请求进行频率检查。URL路径不支持带主机名或域名
的路径格式，例如：不能配置www.baidu.com/home/login.html，应该配置
/home/login.html，而www.baidu.com应该配置在对应的Web服务器的域名设置里。系统最多允许
配置32条URL路径，每条路径长度取值范围为1-255字符。
在Web服务器配置模式下，使用以下命令，删除指定高频URL路径设置：
no cc-url url_string
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# cc-url /home/login.php
配置URL路径的被访问次数和阻断IP时间
为URL高频访问限制功能配置URL路径的被访问次数的阈值及阻断IP的时间。配置后，系统将统计URL路径
被访问的频率，若访问频率超过阈值，系统将阻断该请求的源IP，该IP将无法访问Web服务器。超过阻断时
间后，系统将释放阻断的IP，该IP可以重新访问Web服务器。
在Web服务器配置模式下，使用以下命令，配置URL路径的被访问次数的阈值及阻断IP的时间：
cc-url-limit threshold value action block-ip {permanent | second timeout | hour timeout |
day timeout}
l
value - 指定单个源IP每分钟访问URL路径的最大次数，默认为1次/分钟。当某源IP的访问的频率超过
此阈值，系统将会对此IP进行阻断。其取值范围为1-65535次/分钟。

<!-- 来源页 2203 -->
l
action block-ip { permanent|second timeout | hour timeout | day timeout } - 指定阻断攻击
者IP并指定阻断时长。
l
permanent - 指定对攻击者IP进行永久阻断。
l
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。系统默认为60秒。
在Web服务器配置模式下，使用以下命令，恢复默认值：
no cc-url-limit
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# cc-url /home/login.php
hostname(config-web-server)# cc-url-limit threshold 1500 action block-ip 100
配置Web站点外链检查功能
Web站点外链检查功能可有效管控Web服务器对外部站点资源的引用，并防止未经授权的外部链接访问本
Web服务器资源。用户通过启用该功能并配置外链行为的处理策略，能够精准保护网站资源，避免资源被滥
用（如未经授权直接链接图片、视频等），确保网站的安全性和资源的合理利用。
开启/关闭Web站点外链检查功能
在Web服务器配置模式下，使用以下命令，开启Web站点外链检查功能并配置外链行为的处理动作：
external-link-check enable action {reset | log}
l
reset | log - 为Web站点外链行为指定相应的控制动作：
o
reset - 发现站点外链行为后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信
息。
o
log - 发现站点外链行为后仅记录日志信息。
在Web服务器配置模式下，使用以下命令，关闭Web站点外链检查功能：
no external-link-check enable
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1

<!-- 来源页 2204 -->
hostname(config-web-server)# external-link-check enable action reset
配置外链特例URL
外链特例URL是指在Web站点外链检查中，被特别允许引用的外部URL。通过合理配置外链特例URL，用户
可以在保障网络安全的同时，灵活管理外部资源的合法引用，避免因外链检查误拦截必要资源，从而提升网
站或应用的可用性和用户体验。
注意: 每个Web服务器最多允许配置32个外链URL。
在Web服务器配置模式下，使用以下命令，配置外链特例URL：
external-link url
［句法描述］
url - 指定外链URL。该URL为一个绝对路径（必须带协议“http://”、“https://”或者“ftp://”），
例如，http://www.abc.com/script，表示该路径下所有文件都可以被Web服务器引用（被外链）。
在Web服务器配置模式下，使用以下命令，删除指定外链URL：
no external-link url
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# external-link http://www.abc.com/script
配置盗链检查功能
盗链检查功能旨在检测和防止未授权的外部网站直接通过链接访问Web服务器上的资源（如图片、视频、文
件等）。系统通过对HTTP报文的首部进行检查，获知HTTP请求的来源站点。如果来源站点在“盗链例外”
列表中，则放行；否则进行日志记录或重置连接，从而控制Web站点不被其他站点盗链和防止CSRF（Cross
Site Request Forgery跨网站请求欺骗）攻击发生。
开启/关闭盗链检查功能
为系统开启HTTP首部检查功能并配置盗链行为的处理动作。配置后，系统可对盗链和CSRF(Cross Site
Request Forgery跨网站请求欺骗)攻击行为的HTTP请求重置连接或记录日志。
在Web服务器配置模式下，使用以下命令，开启盗链检查功能并配置盗链行为的处理动作：
referrer-allow-list-check enable action {log | reset}

<!-- 来源页 2205 -->
l
reset | log - 为发生盗链行为的HTTP请求指定相应的动作：
o
reset - 发现盗链或攻击后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
o
log - 发现盗链或攻击后仅记录日志信息。
在Web服务器配置模式下，使用以下命令，关闭盗链检查功能：
no referrer-allow-list-check enable
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# referrer-allow-list-check enable action log
配置盗链特例URL
盗链特例URL是指在盗链检查中，被特别允许访问的首部特例URL。通过合理配置盗链特例URL，用户可以
在保护网站资源不被盗用的同时，允许合法的外部引用，避免因盗链检查误拦截必要资源，从而提升网站或
应用的可用性和用户体验。
注意: 每个Web服务器最多允许配置32条URL路径。
在Web服务器配置模式下，使用以下命令，配置盗链特例URL：
referer-allow-list url_string
l
url_string - 指定可以引用Web站点的首部特例URL。指定后，该URL可引用Web站点，其他未添加的
URL则不可以引用Web站点。
在Web服务器配置模式下，使用以下命令，删除首部特例URL的设置：
no referer-allow-list url_string
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# referer-allow-list www.abc.com
配置CC防护功能
CC（Challenge Collapsar）防护功能是一种专门用于抵御CC攻击（Challenge Collapsar攻击，即
HTTP Flood攻击）的网络安全措施。CC攻击是一种常见的DDoS攻击形式，攻击者通过大量HTTP请求淹没

<!-- 来源页 2206 -->
目标服务器，导致服务器资源耗尽，从而使合法用户无法正常访问服务。用户通过开启CC防护功能并为该功
能配置请求阈值、认证方法、访问限速、白名单等信息，能够有效拦截恶意请求，保护网站和Web服务器的
正常运行，从而最大限度地减少攻击带来的损害。
注意: 非根VSYS不支持CC防护功能。
开启/关闭CC防护功能
为系统开启HTTP协议CC防护功能并设置开启该功能的请求阈值。当HTTP连接请求速率达到设定阈值时，即
判断为发生CC攻击，并启动CC防护功能。
在Web服务器配置模式下，使用以下命令，开启CC防护功能并配置请求阈值：
http-request-flood enable [threshold request value]
l
threshold request value - 指定开启HTTP协议CC防护功能的请求阈值，默认为2000次/秒。取值范
围为0到1000000次/秒。
在Web服务器配置模式下，使用以下命令，关闭HTTP协议CC防护功能：
no http-request-flood enable
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# http-request-flood enable
配置认证方法
为CC防护功能配置认证方法。系统通过认证判断HTTP请求的源IP是否合法，从而识别攻击流量并进行防
护。如果某个源IP认证失败，系统将阻断该源IP发起的本次HTTP请求。
在Web服务器配置模式下，使用以下命令，配置认证方法：
http-request-flood auth {auto-js-cookie | auto-redirect | manual-CAPTCHA | manualconfirm} [crawlers-friendly]
l
auto-js-cookie | auto-redirect | manual-CAPTCHA | manual-confirm - 指定认证方法。
l
auto-js-cookie - 自动（JS Cookie）。该认证方法由浏览器自动完成认证交互。
l
auto-redirect - 自动（重定向）。该认证方法由浏览器自动完成认证交互。
l
manual-CAPTCHA - 手动（访问确认）。该认证方法需要HTTP请求发起者点击返回提示框上的

<!-- 来源页 2207 -->
“确认”按钮进行认证。
l
manual-confirm - 手动（验证码）。该认证方法需要请求发起者输入验证码进行认证。
l
crawlers-friendly - 指定不对爬虫进行认证。
在Web服务器配置模式下，使用以下命令，取消认证方法配置：
no http-request-flood auth
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# http-request-flood auth auto-js-cookie
配置代理限速
为CC防护功能配置代理限速。配置代理限速后，系统会检查每个源IP是否属于代理服务器，若属于，则根据
配置进行请求速率限制。
在Web服务器配置模式下，使用以下命令，配置代理限速：
http-request-flood proxy-limit threshold value {blockip timeout { permanent|second
timeout |hour timeout | day timeout}| reset} [nolog]
l
blockip timeout { permanent|second timeout | hour timeout | day timeout } | reset - 指定
系统对超出请求速率阈值的请求数的限制操作：
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长，单位为
秒/小时/天，范围是60到3600秒/1到24小时/1到15天。
o
reset - 重置超出的请求数的请求连接。
l
nolog - 指定不记录日志信息。
在Web服务器配置模式下，使用以下命令，取消代理限速配置：
no http-request-flood proxy-limit
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# http-request-flood proxy-limit threshold 10000 reset
nolog

<!-- 来源页 2208 -->
配置访问限速
为CC防护功能配置访问限速。配置访问限速后，系统会根据配置对每个源IP进行请求速率限制。
在Web服务器配置模式下，使用以下命令，配置访问限速：
http-request-flood request-limit threshold value {blockip timeout {permanent|second
timeout hour timeout day timeout }| reset} [nolog]
l
threshold value - 指定访问速率阈值。如果收到的请求速率超过该指定值且CC防护功能已开启，系统
会对超出的请求数做相应的限制操作。取值范围为0到1000000次/秒。
l
blockip timeout { permanent|second timeout | hour timeout day timeout }| reset - 指定
系统对超出请求速率阈值的请求数的限制操作：
l
permanent - 指定对攻击者IP或者服务进行永久阻断。
l
second timeout | hour timeout | day timeout - 指定对攻击者IP或者服务进行阻断的时
长，单位为秒/小时/天，范围是60到3600秒/1到24小时/1到15天。
l
reset - 重置超出的请求数的请求连接。
l
nolog - 指定不记录日志信息。
在Web服务器配置模式下，使用以下命令，取消访问限速配置：
no http-request-flood request-limit
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# http-request-flood request-limit threshold 10000 blockip
timeout 60
配置白名单
为CC防护功能配置白名单。添加到白名单中的源IP地址不做CC防护检查。
在Web服务器配置模式下，使用以下命令，配置白名单：
http-request-flood allow-list address_entry
l
address_entry - 指定不做CC防护检查的地址条目。地址条目不能为域名和IPv6地址。
注意: 如果白名单中源IP地址的流量超出CC防护请求阈值（http-request-flood enable
[threshold request value]），则会触发CC防护功能的开启。

<!-- 来源页 2209 -->
在Web服务器配置模式下，使用以下命令，取消CC防护白名单配置：
no http-request-flood allow-list
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# http-request-flood allow-list addr1
开启/关闭URL请求统计功能
在Web服务器配置模式下，使用以下命令，开启URL请求统计功能：
http-request-flood statistics enable
在Web服务器配置模式下，使用以下命令，关闭URL请求统计功能：
no http-request-flood statistics enable
注意: 执行http-request-flood statistics enable命令后，show ips sigset sigset-name
web-server server-name http-request-flood req-stat top命令才会生效。
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# http-request-flood statistics enable
配置x-forward-for字段取值
为CC防护功能配置HTTP请求的x-forward-for字段的取值。配置后，系统会按照该字段统计其访问频率，
当某设定的完整URL的被访问频率超过阈值且持续20s时，系统判定CC攻击发生。
在Web服务器配置模式下，使用以下命令，配置x-forward-for字段取值：
http-request-flood x-forward-for {first | last | all}
l
first | last | all - 指定x-forwarded-for字段的取值，first 为x-forwarded-for字段第一个值，last
为x-forwarded-for字段的最后一个值，all为x-forwarded-for字段的全部的值。
在Web服务器配置模式下，使用以下命令，取消x-forward-for字段的取值配置：
no http-request-flood x-forward-for
［命令实例］

<!-- 来源页 2210 -->
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# http-request-flood x-forward-for first
开启/关闭x-real-ip字段统计功能
为系统开启CC防护功能中HTTP请求的x-real-for字段统计。启用后，系统会对x-real-for字段的值进行统
计。
在Web服务器配置模式下，使用以下命令，开启/关闭x-real-ip字段统计功能：
l
开启：http-request-flood x-real-ip enable
l
关闭：no http-request-flood x-real-ip
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# http-request-flood x-real-ip enable
配置Iframe检查功能
Iframe（内联框架）是一种HTML元素，允许在一个网页中嵌入另一个网页。Iframe检查功能用于检测和控
制网页中Iframe（内联框架）的使用情况，防止因恶意嵌入导致的安全问题，如点击劫持、跨站脚本攻击
（XSS）等。该功能通过检查页面是否被嵌入到其他页面的Iframe中，或限制特定页面被嵌入到Iframe，
从而保护网站资源的安全性和完整性。
开启/关闭Iframe检查功能
为系统开启HTTP协议iframe检查功能并为发现隐藏Iframe行为指定相应的处理动作。通过iframe检查，
系统会识别出是否有隐藏的iframe的HTML页面，从而进行记录日志或重置连接。
在Web服务器配置模式下，使用以下命令，开启Iframe检查功能并配置指定处理动作：
iframe-check enable action {log | reset}
l
reset | log - 为隐藏iframe行为的HTTP请求指定相应的动作：
o
reset - 发现隐藏iframe行为后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信
息。
o
log - 发现隐藏iframe行为后仅记录日志信息。
在Web服务器配置模式下，使用以下命令，关闭Iframe检查功能：

<!-- 来源页 2211 -->
no iframe-check enable
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# iframe-check enable action log
配置Iframe高度和宽度
为iframe检查功能配置高度和宽度的限制。系统会根据设定的iframe高度和宽度来检查HTML页面中的
iframe，当高度和宽度中任意一项小于或等于设定值，系统将会识别为隐藏的iframe攻击发生，从而进行
记录日志或重置连接。
在Web服务器配置模式下，使用以下命令，配置Iframe高度和宽度：
iframe width width_value height height_value
l
width width_value - 指定iframe的限定的宽度值，取值范围为0-4096px。
l
height height_value - 指定iframe的限定的高度值，取值范围为0-4096px。
在Web服务器配置模式下，使用以下命令，删除Iframe设置：
no iframe
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# iframe width 0 height 1
配置敏感目录扫描检测功能
敏感目录扫描是一种针对Web服务器的常见攻击手段，攻击者使用目录扫描工具对Web服务器内的站点进行
遍历，以获取Web服务器的目录结构、后台文件、备份文件等敏感信息。
若攻击者试图对Web服务器进行敏感目录扫描，Web服务器将返回大量状态码为404的响应报文。此时系统
将对每分钟Web服务器返回的“404”响应报文进行计数：①若该数目大于10次，系统则对所有的HTTP 请
求报文中的URL进行解析，并将解析后的URL路径与内置的敏感文件字典进行匹配。若解析后的URL路径命
中敏感文件字典的次数超出指定的阈值，系统将按照用户指定的防护动作进行处理（只记录日志/重置/阻断
IP/阻断服务）；②若该数目大于等于100次，系统直接判定该行为是敏感目录扫描攻击，并按照指定的防护
动作进行处理（只记录日志/重置/阻断IP/阻断服务）。
开启/关闭敏感目录扫描功能

<!-- 来源页 2212 -->
系统支持开启/关闭Web服务器敏感目录扫描检测功能。该功能默认为关闭状态，启用后，系统会对每分钟
Web服务器返回的“404”响应报文进行计数，并按照用户指定阈值和动作进行防护。
在Web服务器配置模式下，使用以下命令，开启/关闭Web服务器敏感目录扫描检测功能：
l
开启：sensitive-file-scan enable
l
关闭：no sensitive-file-scan enable
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# sensitive-file-scan enable
指定防护敏感目录扫描攻击的阈值
指定系统防护敏感目录扫描攻击的阈值。指定后，当每分钟URL路径命中敏感文件字典的次数超过该阈值
时，系统将按照用户指定的动作进行防护。
在Web服务器配置模式下，使用以下命令，指定防护敏感目录扫描攻击的阈值：
sensitive-file-scan warning-value value
l
value - 指定每分钟最多命中敏感文件字典的次数，默认为10次/分钟。取值范围是10到100次/分钟。
注意: 若配置好该命令行后再开启Web服务器敏感目录扫描检测功能，配置依旧生效。若用户未开
启Web服务器敏感目录扫描检测功能，该命令行可以配置，但无法生效。
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# sensitive-file-scan warning-value 20
指定敏感目录扫描攻击的防护动作
指定系统对敏感目录扫描攻击的防护动作。若攻击者试图对Web服务器进行敏感目录扫描，Web服务器将返
回大量状态码为404的响应报文。此时系统将对每分钟Web服务器返回的“404”响应报文进行计数并指定
相应的防护动作。
在Web服务器配置模式下，使用以下命令，指定敏感目录扫描攻击的防护动作：

<!-- 来源页 2213 -->
sensitive-file-scan action {block-ip {permanent | second timeout | hour timeout | day
timeout} | block-service {permanent | second timeout | hour timeout | day timeout} | log-only
| reset}
l
block-ip {permanent | second timeout | hour timeout | day timeout}- 指定阻断攻击者IP并指
定阻断时长。
l
permanent - 指定对攻击者IP进行永久阻断。
l
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
l
permanent - 指定对攻击者服务进行永久阻断。
l
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。该选项为系统默认防护动作。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
注意: 若配置好该命令行后再开启Web服务器敏感目录扫描检测功能，配置依旧生效。若用户未开
启Web服务器敏感目录扫描检测功能，该命令行可以配置，但无法生效。
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# sensitive-file-scan action block-ip second 61
配置SQL注入检查功能
SQL注入检查是一种用于检查和防范SQL注入漏洞的安全机制，它通过分析用户输入、HTTP请求参数或URL
中的潜在恶意代码，识别可能的SQL注入攻击。用户通过开启SQL注入检查功能，并指定SQL注入检查点和
防护动作，可以有效降低SQL注入攻击的风险，从而保护Web应用程序的安全性。
开启/关闭SQL注入检查功能
为系统开启HTTP协议SQL注入检查功能并配置发现SQL注入攻击的防护动作。当SQL注入攻击事件为“严
重”级别事件时，若未指定防护动作，则在检测出SQL注入攻击后，默认仅记录日志。

<!-- 来源页 2214 -->
在Web服务器配置模式下，使用以下命令，开启SQL注入检查功能并配置发现SQL注入攻击的防护动作：
sql-injection-check enable action {block-ip {permanent | second timeout | hour timeout |day
timeout}| block-service {permanent |second timeout | hour timeout | day timeout}| log-only |
reset}
l
block-ip {permanent|second timeout |hour timeout | day timeout} - 指定阻断攻击者IP并指定
阻断时长。
l
permanent - 指定对攻击者IP进行永久阻断。
l
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
l
permanent - 指定对攻击者服务进行永久阻断。
l
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。该选项为系统默认的防护动作。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在Web服务器配置模式下，使用以下命令，关闭SQL注入检查功能：
sql-injection-check disable
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# sql-injection-check enable action reset
指定SQL注入检查点
为SQL注入检查指定检查点，可以为HTTP Cookie、HTTP Post、HTTP Referer或者HTTP URI。默认开启
全部检查点。如需关闭指定的SQL注入检查点，可在Web服务器配置模式下，使用以下命令：
sql-injection {cookie | post | referer | uri} disable
l
{cookie | post | referer | uri} disable - 关闭指定的SQL注入检查点。
在Web服务器配置模式下，使用以下命令，开启指定的SQL注入检查点：
no sql-injection {cookie | post | referer | uri} disable

<!-- 来源页 2215 -->
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# sql-injection cookie disable
配置XSS注入检查功能
XSS注入检查是一种用于检测和防御跨站脚本攻击（XSS）的安全机制，它通过监控和分析用户输入以及页
面输出内容，识别潜在的XSS漏洞，防止恶意脚本注入和执行。用户通过开启XSS注入检查功能，并指定
XSS注入检查点和防护动作，可以有效降低XSS攻击的风险，从而保护Web应用程序的安全性。
开启/关闭XSS注入检查功能
为系统开启HTTP协议XSS注入检查功能并配置发现XSS注入攻击的防护动作。当XSS注入攻击事件为“严
重”级别事件时，若未指定防护动作，则在检测出XSS注入攻击后，默认仅记录日志。
在Web服务器配置模式下，使用以下命令，开启XSS注入检查功能并配置发现XSS注入攻击的防护动作：
xss-check enable action {block-ip {permanent | second timeout | hour timeout |day timeout}|
block-service {permanent |second timeout | hour timeout | day timeout}| log-only | reset}
l
block-ip {permanent| second timeout |hour timeout | day timeout} - 指定阻断攻击者IP并指定
阻断时长。
l
permanent - 指定对攻击者IP进行永久阻断。
l
second timeout | hour timeout | day timeout- 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
l
permanent - 指定对攻击者服务进行永久阻断。
l
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。该选项为系统默认的防护动作。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在Web服务器配置模式下，使用以下命令，关闭XSS注入检查功能：
xss-check disable
［命令实例］

<!-- 来源页 2216 -->
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# xss-check enable action reset
指定XSS注入检查点
为Web服务器XSS注入检查指定检查点，可以为HTTP Cookie、HTTP Post、HTTP Referer或者HTTP
URI。默认开启全部检查点。如需关闭指定的XSS注入检查点，可在Web服务器配置模式下，使用以下命
令：
xss-injection {cookie | post | referer | uri} disable
l
{cookie | post | referer | uri} disable - 关闭指定的XSS注入检查点。
在Web服务器配置模式下，使用以下命令，开启指定的XSS注入检查点。
no xss-injection {cookie | post | referer | uri} disable
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# xss-injection uri disable
配置访问控制功能
访问控制功能主要用于精细化管理和限制用户对Web资源的访问行为，从而降低安全风险。用户通过开启访
问控制功能，并设置合理的访问控制规则，可以有效阻止恶意IP访问，避免敏感信息泄露和恶意攻击，保障
Web服务器的安全性和稳定性。
开启访问控制功能
为系统开启访问控制功能并配置发现Web站点非法访问行为的防护动作，防止攻击者利用上传漏洞植入恶意
代码、身份冒用绕过验证等手段向Web服务器发起攻击。
在Web服务器配置模式下，使用以下命令，开启访问控制功能并配置发现Web站点非法访问行为的防护动
作：
web-acl-check enable action {reset | log}
l
reset | log - 为Web站点非法访问行为指定相应的控制动作：

<!-- 来源页 2217 -->
l
reset - 发现非法访问行为后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信
息。
l
log - 发现非法访问行为后仅记录日志信息。
在Web服务器配置模式下，使用以下命令，关闭访问控制功能：
no web-acl-check enable
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# web-acl-check enable action reset
配置Web站点路径及其属性
配置Web站点路径并指定其属性，该路径为Web服务器的相对路径。
在Web服务器配置模式下，使用以下命令，配置Web站点路径及其属性：
web-acl url {static | deny}
l
url - 指定Web站点路径。
l
static | deny - 指定Web站点路径的属性：
l
static - 指定属性为静态。指定后Web站点路径下的资源仅静态资源（图片和普通文本）允许访
问，访问其他资源将按照访问控制功能（web-acl-check enable action {reset | log}）中配
置的动作进行处理。
l
deny - 指定属性为禁止。指定后Web站点路径下的资源均不允许访问。
在Web服务器配置模式下，使用以下命令，删除指定Web站点路径：
no web-acl url
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# web-acl /eee deny

<!-- 来源页 2218 -->
指定Web服务器黑名单的最大URL数目
指定Web服务器黑名单中能够包含的最大URL数目。当用户访问某静态页面时，如果系统发现该页面中包含
违反外链检查或者上传路径检查的内容，则将该页面的URL加入到黑名单，当用户再次访问该页面时会直接
命中黑名单，从而提高系统处理速度。
在Web服务器配置模式下，使用以下命令，指定Web服务器黑名单中能够包含的最大URL数目：
max-block-list size
l
size - 指定黑名单能够包含的最大URL数目，默认为0。取值范围是0到4096。
在Web服务器配置模式下，使用以下命令，恢复默认值：
no max-block-list
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# max-block-list 4096
指定Web服务器白名单的最大URL数目
指定Web服务器白名单中能够包含的最大URL数目。当用户访问某静态页面时，如果该页面没有发现任何违
反外链检查或者上传路径检查的内容，则将该页面的URL加入到白名单，当用户再次访问该页面时则直接命
中白名单，从而提高系统处理速度。使用该命令no的形式取消指定。
在Web服务器配置模式下，使用以下命令，指定Web服务器白名单中能够包含的最大URL数目：
max-allow-list size
size - 指定白名单能够包含的最大URL数目，默认为0。取值范围是0到4096。
在Web服务器配置模式下，使用以下命令，恢复默认值：
no max-allow-list
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# max-allow-list 4096

<!-- 来源页 2219 -->
启用/禁用Web服务器
系统支持启用/禁用自定义Web服务器。启用后，系统会对指定Web服务器进行防护。系统预定义的Web服
务器默认为启用状态，且不能被禁用。
在Web服务器配置模式下，使用以下命令，启用/禁用Web服务器：
l
启用：enable
l
禁用：no enable
［命令实例］
hostname(config)# ips web-profile test
hostname(config-web-profile)# web-server web_server1
hostname(config-web-server)# enable
配置口令防护信息
开始之前
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。
口令防护配置包括以下内容：
l 防暴力破解
l HTTP口令防护
l 弱口令检测
防暴力破解
进入防暴力破解配置模式后，可对Cassandra/CVS/DB2/FirebirdWire/FTP/HTTP/IMAP/IRC/Kerberos/LDAP/MongoDB/MSRPC/
MSsql/NNTP/Oracle/PGSQL/POP3/REDIS/RDP/Radius/Rexec/Rlogin/RSH/RTSP/SIP/SMB/SM
TP/Socket5/SSH/SUNRPC/SVN/
Sybase/Telnet/VNC协议下的暴力破解攻击进行阻断设置。

<!-- 来源页 2220 -->
进入防暴力破解配置模式
进入防暴力破解配置模式，在IPS Profile配置模式下使用以下命令：
brute-force
配置防暴力破解规则
在防暴力破解配置模式下，使用以下命令配置暴力破解规则：
{Cassandra | CVS | DB2 | Firebird-Wire | ftp | http | imap | IRC | Kerberos | ldap | MongoDB |
msrpc | MSsql | NNTP | Oracle | PGSQL | pop3 | Radius | rdp | REDIS | Rexec | Rlogin | RSH |
RTSP | SIP | smb | smtp | Socket5 | ssh | sunrpc | SVN | Sybase | telnet | vnc} times {block {ip |
service} {permanent | second timeout | hour timeout | day timeout} | log-only}
l
Cassandra | CVS | DB2 | Firebird-Wire | ftp | http | imap | IRC | Kerberos | ldap | MongoDB |
msrpc | MSsql | NNTP | Oracle | PGSQL | pop3 | Radius | rdp | REDIS | Rexec | Rlogin | RSH |
RTSP | SIP | smb | smtp | Socket5 | ssh | sunrpc | SVN | Sybase | telnet | vnc - 指定系统进行暴
力破解攻击检测的协议名称。
l
times - 指定系统默认五分钟内允许认证/登录失败的次数。取值范围是1到100000。
l
block {ip | service} - 指定对超出限定认证/登录失败频率的攻击者的IP地址（ip）或者服务
（service）进行阻断。
l
permanent - 指定对攻击者IP或者服务进行永久阻断。
l
second timeout | hour timeout | day timeout - 指定对攻击者IP或者服务进行阻断的时长，单位
分别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 指定对暴力破解攻击采取仅记录日志动作。
删除暴力破解规则，在暴力破解配置模式下，使用以下命令：
no {Cassandra | CVS | DB2 | Firebird-Wire | ftp | http | imap | IRC | Kerberos | ldap | MongoDB |
msrpc | MSsql | NNTP | Oracle | PGSQL | pop3 | Radius | rdp | REDIS | Rexec | Rlogin | RSH |
RTSP | SIP | smb | smtp | Socket5 | ssh | sunrpc | SVN | Sybase | telnet | vnc}
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# brute-force
hostname(config-ips-profile-bruteforce)# ftp 100 block ip second 61（表示对FTP协议下认证
/登录失败超过100次的攻击者IP进行阻断61秒。）

<!-- 来源页 2221 -->
HTTP口令防护
进入HTTP口令防护配置模式后，用户可以配置HTTP口令防护信息、开启/关闭HTTP明文密码检测功能。
进入HTTP口令防护配置模式
进入HTTP口令防护配置模式，在IPS Profile配置模式下使用以下命令：
password-protect
配置HTTP口令防护信息
系统通过解析HTTP登录报文中的用户名、密码及登录结果等相关信息，判断是否存在弱口令及暴力破解的行
为，并提供默认的用户名、密码及登录结果的字段列表。但由于HTTP协议内容依赖用户端与服务器的协商，
为避免漏报，用户可对实际报文中代表用户名、密码、登录成功或失败的字段进行自定义配置，从而对HTTP
协议进行弱口令及暴力破解的检测，并根据配置的规则进行相应的处理。
在HTTP口令防护配置模式下，使用以下命令，配置用户名、密码、登录成功响应码、登录成功字段、登录失
败响应码及登录失败字段。
l
配置用户名：http-username username
l
username - 指定HTTP登录报文中用户名的字段，不区分大小写，多个字段可通过;隔开，取值
范围是1-512个字符。系统默认提供5个用户名字段，分别为username、user、usrname、j_
username和login。
l
配置密码：http-userpassword password
l
password - 指定HTTP登录报文中密码的字段，不区分大小写，多个字段可通过;隔开，取值范
围是1-512个字符。系统默认提供5个密码字段，分别为password、passwd、pass、pwd和j_
password。
l
配置登录成功响应码：http-success-code success-code
l
success-code - 指定HTTP登录报文中登录成功的响应码，多个响应码可通过;隔开，取值范围是
1-512个字符。系统默认提供4个登录成功响应码，分别为200、302、201和303。
l
配置登录失败响应码：http-fail-code fail-code
l
fail-code - 指定HTTP登录报文中登录失败的响应码，多个响应码可通过;隔开，取值范围是1-
512个字符。系统默认提供6个登录失败响应码，分别为200、302、201、303、401和500。
l
配置登录成功字段：http-custom-success-login custom-success-login

<!-- 来源页 2222 -->
l
custom-success-login - 指定HTTP登录报文中登录成功的字段，不区分大小写，多个字段可通
过;隔开，取值范围是1-512个字符。系统默认提供4个登录成功字段，分别为loginsuccess、
login-success、OK=1和"successful"."true"。
l
配置登录失败字段：http-custom-fail-login custom-fail-login
l
custom-fail-login - 指定HTTP登录报文中登录失败的字段，不区分大小写，多个字段可通过;
隔开，取值范围是1-512个字符。系统默认提供6个登录失败字段，分别为loginerror、loginerror、loginerr、OK=0、"successful"."fail"和"result"=[]。
注意: 配置用户名、密码、登录成功响应码、登录成功字段、登录失败响应码及登录失败字段时，
需要在对应命令后输入字段值的16进制格式。例如：配置用户名为“hillstone;login”，需输入
http-username 68696C6C73746F6E653B6C6F67696E命令。
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# password-protect
hostname(config-ips-profile-pwd-protect)# http-username
68696C6C73746F6E653B6C6F67696E
开启/关闭HTTP明文密码检测功能
系统支持开启/关闭HTTP明文密码检测功能。默认情况下，该功能为关闭状态。启用该功能后，系统会对
HTTP报文中的密码字段进行检测，若密码字段没有经过加密，则发出报警日志。
在HTTP口令防护配置模式下使用以下命令，开启和关闭HTTP明文密码检测功能。
l
开启HTTP明文密码检测功能：http-plain-text-check enable
l
关闭HTTP明文密码检测功能：http-plain-text-check disable
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# password-protect
hostname(config-ips-profile-pwd-protect)# http-plain-text-check enable

<!-- 来源页 2223 -->
弱口令检测
进行入侵防御规则配置时，开启弱口令检测功能可对该规则下的
Cassandra/DB2/FTP/HTTP/IMAP/IRC/NNTP/PGSQL/POP3/REDIS/Rexec/Rlogin/RTSP/SMTP/S
ocket5/Sybase/Telnet协议的明文密码进行密码强度检测，符合弱口令检测条件的密码将被视为弱密码，
系统发出报警日志，可防止弱密码所引起的安全隐患。默认情况下，弱口令检测功能为开启状态。在进入弱
口令检测配置模式后，用户需要配置的参数包含：密码长度、密码字符种类、账号与密码相同检测、连续字
符检测、FTP匿名登录检测以及指定自定义弱密码。
进入弱口令检测配置模式
进入弱口令检测配置模式，在IPS Profile配置模式下使用以下命令：
check-weakpassword
使用该命令no的形式恢复弱口令检测默认配置，其中密码最短长度默认值为6、密码字符种类默认值为2、账
号与密码相同检测默认开启、连续字符检测默认开启、FTP匿名登录检测默认关闭，指定自定义弱密码无默
认值。
no check-weakpassword
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# check-password
hostname(config-ips-profile-weakpass)#
开启/关闭弱口令检测功能
系统支持开启/关闭弱口令检测功能，默认情况下，该功能为开启状态。
在弱口令检测配置模式下使用以下命令，开启和关闭弱口令检测功能。
l
开启弱口令检测功能：enable
l
关闭弱口令检测功能：disable
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# check-weakpassword
hostname(config-ips-profile-weakpass)# disable

<!-- 来源页 2224 -->
指定密码长度
指定弱口令功能检测密码的最短长度，小于该长度的密码将被检测为弱密码。
在弱口令检测配置模式下，使用以下命令，指定弱口令检测的密码长度：
length number
l
number - 指定弱口令功能检测密码的最短长度。范围是6到50位，系统默认为6位。
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# check-weakpassword
hostname(config-ips-profile-weakpass)# enable
hostname(config-ips-profile-weakpass)# length 8
指定密码字符种类
指定弱口令功能检测密码的最少字符种类，少于设定字符种类数的密码将被检测为弱密码。
在弱口令检测配置模式下，使用以下命令，指定弱口令检测的密码字符种类：
min-character-type number
l
number - 指定弱口令功能检测密码的最少字符种类。范围是1到4种，系统默认为2种。
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# check-weakpassword
hostname(config-ips-profile-weakpass)# enable
hostname(config-ips-profile-weakpass)# min-character-type 3
开启/关闭账号与密码相同的弱口令检测功能
系统支持开启/关闭检测用户名密码相等的弱口令检测功能。默认情况下，该功能为开启状态。启用该功能
后，与账号相同的密码将被检测为弱密码。
在弱口令检测配置模式下使用以下命令，开启/关闭账号与密码相同的弱口令检测功能。
l
开启：equal-username-check enable
l
关闭：equal-username-check disable

<!-- 来源页 2225 -->
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# check-weakpassword
hostname(config-ips-profile-weakpass)# enable
hostname(config-ips-profile-weakpass)# equal-username-check disable
开启/关闭连续字符检测功能
系统支持开启/关闭检测连续字符的弱口令检测功能。默认情况下，该功能为开启状态。启用该功能后，密码
长度小于10位且连续相同或顺序字符位数大于等于8位的密码将被检测为弱密码，如1aaaaaaaa，
1abcdefgh，a87654321。
在弱口令检测配置模式下使用以下命令，开启和关闭连续字符检测功能。
l
开启：serial-character-check enable
l
关闭：serial-character-check disable
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# check-weakpassword
hostname(config-ips-profile-weakpass)# enable
hostname(config-ips-profile-weakpass)# serial-character-check enable
开启/关闭FTP匿名登录检测功能
系统支持开启/关闭检测FTP匿名登录的弱口令检测功能。默认情况下，该功能为关闭状态。启用该功能后，
当用户使用FTP匿名登录时，系统将检测其密码为弱密码。
在弱口令检测配置模式下使用以下命令，开启和关闭FTP匿名登录检测功能。
l
开启：ftp-anonymous-login-check enable
l
关闭：ftp-anonymous-login-check disable
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# check-weakpassword
hostname(config-ips-profile-weakpass)# enable

<!-- 来源页 2226 -->
hostname(config-ips-profile-weakpass)# ftp-anonymous-login-check enable
添加自定义弱密码
在弱口令检测功能中的弱密码字典中增加指定的自定义弱密码，当系统检测到的密码与自定义弱密码相匹配
时，则认定该密码为弱密码。最多可添加100条自定义弱密码。
在弱口令检测配置模式下，使用以下命令，增加指定的自定义弱密码：
custom-password add weakpassword
l
weakpassword - 指定需要增加进弱密码字典的自定义弱密码。
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# check-weakpassword
hostname(config-ips-profile-weakpass)# enable
hostname(config-ips-profile-weakpass)# custom-password add password123
删除自定义弱密码
在弱口令检测功能中的弱密码字典中删除指定的自定义弱密码。
在弱口令检测配置模式下，使用以下命令，删除指定的自定义弱密码：
custom-password delete weakpassword
l
weakpassword - 指定需要从弱密码字典中删除的自定义弱密码。
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# check-weakpassword
hostname(config-ips-profile-weakpass)# enable
hostname(config-ips-profile-weakpass)# custom-password delete password123
配置IPS异常流量检测
开始之前

<!-- 来源页 2227 -->
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。
异常流量检测是IPS入侵防御的重要组成部分，旨在通过分析网络流量中的异常行为，识别并防范潜在的网
络攻击或恶意活动。其核心在于利用机器学习、深度学习等技术和算法，对网络流量数据进行实时监测和分
析，并检测出与正常流量模式不符的流量，从而有效防范各种网络攻击，如DDoS攻击、恶意软件传播等。
如需对网络中的异常流量进行检测，用户可进行如下配置：
l 配置反弹Shell检测功能
l 配置协议异常检查功能
配置反弹Shell检测功能
反弹Shell检测功能旨在检测和阻止攻击者通过反弹Shell技术获取目标主机的控制权。反弹Shell是一种常
见的攻击手段，攻击者通过在目标主机上执行恶意代码，使目标主机主动连接攻击者控制得服务器，建立一
个反向的命令行交互通道，从而获得目标主机的远程控制权限。反弹Shell检测功能就是通过对网络流量、系
统进程等多方面的监控和分析，来识别出这种异常的反向连接行为以及相关的恶意操作，及时发现潜在的入
侵行为，并按照用户指定的动作进行防护，避免系统被非法控制和数据泄露等安全事件的发生。
l 开启/关闭反弹Shell检测功能
l 指定发现反弹Shell攻击的防护动作
l 指定防护反弹Shell攻击的模式
l 指定反弹Shell检测项检测值
开启/关闭反弹Shell检测功能
系统支持开启/关闭反弹Shell检测功能。该功能默认为关闭状态，启用后，系统将对反弹Shell攻击进行检
测和防护，若发现攻击行为，系统将按照用户指定的动作进行防护。
在IPS Profile配置模式下，使用以下命令，开启/关闭反弹Shell检测功能：
l
开启：reverse-shell enable
l
关闭：no reverse-shell enable
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# reverse-shell enable

<!-- 来源页 2228 -->
指定发现反弹Shell攻击的防护动作
指定发现反弹Shell攻击后的防护动作。系统默认防护动作为只记录日志（log-only）。开启反弹Shell检测
功能后，系统将对反弹Shell攻击进行检测和防护，若发现攻击行为，系统将按照用户指定的动作进行防护。
在IPS Profile配置模式下，使用以下命令，指定发现反弹Shell攻击后的防护动作：
reverse-shell action {log-only | reset | block-ip {permanent | second timeout | hour timeout |
day timeout}}
l
action {log-only | reset | block-ip {permanent | second timeout | hour timeout | day
timeout}} - 指定系统对反弹Shell攻击的检测和防护动作。
o
log-only - 指定该参数后，系统发现反弹shell攻击后仅记录日志信息。
o
reset - 指定该参数后，系统发现反弹shell攻击后重置连接（TCP）或者发送目标不可达包
（UDP）并且记录日志信息。
o
block-ip {permanent | second timeout | hour timeout | day timeout} - 指定该参数后，
阻断反弹Shell攻击者的IP地址并设置阻断时间。permanent - 指定对攻击者IP或者服务进行永
久阻断。second timeout | hour timeout | day timeout - 指定对攻击者IP或者服务进行阻断
的时长，单位分别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
注意: 配置系统对反弹shell攻击的防护动作后，需保证反弹shell检测功能已开启，否则，该配置
仅保存但不生效。
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# reverse-shell enable
hostname(config-ips-profile)# reverse-shell action log-only
指定防护反弹Shell攻击的模式
指定系统对反弹Shell攻击的防护模式。系统默认的防护模式为低误报（low）。开启反弹Shell检测功能
后，系统将对反弹Shell攻击的关键词进行扫描检测，并指定系统对反弹Shell攻击的防护模式。
在IPS Profile配置模式，使用以下命令，指定系统对反弹Shell攻击的防护模式：
reverse-shell level {high | low}

<!-- 来源页 2229 -->
l
level {high | low} - 指定系统反弹Shell攻击的防护模式。
o
high - 高检测，指定该参数后，系统对反弹shell攻击的关键词进行扫描检测时，若关键词被命
中的次数超过2次就进行日志上报，可用于攻击检测要求比较高的场景。
o
low - 低误报，指定该参数后，系统对反弹shell攻击的关键词进行扫描检测时，若关键词被命中
的次数超过4次才进行日志上报，可用于系统性能要求比较高的场景。
注意: 配置系统对反弹shell攻击的防护模式后，需保证反弹shell检测功能已开启，否则，该配置
仅保存但不生效。
［命令实例］
hostname(config)# ips profile test
hostname(config-ips-profile)# reverse-shell enable
hostname(config-ips-profile)# reverse-shell level high
指定反弹Shell检测项的检测值
系统预设反弹Shell检测项，每一个检测项代表一个特征维度，命中特征维度越多，受到反弹shell攻击的可
能越大。系统根据流量的特征是否达到检测项的阈值以及检测项的权重判断是否受到了反弹Shell攻击。用户
可以根据需要对部分检测项的阈值进行修改，以降低反弹Shell误报。
配置异常端口检测的阈值
反弹Shell通常使用非标准协议端口或TCP-ANY端口进行通信。
在IPS Profile配置模式，使用以下命令，对所有端口进行检测：
ips reverse-shell checklist abnormal-port zero-trust
在IPS Profile配置模式，使用以下命令，仅对异常端口进行检测：
no ips reverse-shell checklist abnormal-port zero-trust
配置双端数据回应异常次数阈值
反弹Shell会话中，攻击机和目标机的响应时间可能表现出异常模式。例如，响应时间可能极短（接近零延
迟），或者响应时间极长且不稳定，反映出网络延迟或攻击者与目标机之间的不稳定连接。
flow0是指会话建立时的请求方向，flow1是指会话建立时的响应方向。默认flow0的数据回应时间小于0.8
秒且flow1的数据回应时间大于3秒时为回应异常，回应异常的次数大于等于3时，判断可能受到了反弹
Shell攻击。
在IPS Profile配置模式，使用以下命令，指定双端异常响应时间的阈值：

<!-- 来源页 2230 -->
ips reverse-shell checklist abnormal-reaction {cnt reaction-time | flow0 reaction-time |
flow1 reaction-time}
l
cnt reaction-time - 指定双端数据回应异常次数的阈值，范围是0到10000次。
l
flow0 reaction-time - 指定flow0的异常响应时间的阈值，范围是0到86400000毫秒。
l
flow1 reaction-time - 指定flow1的异常响应时间的阈值，范围是0到86400000毫秒。
在IPS Profile配置模式，使用以下命令，恢复双端异常响应时间的默认阈值：
no ips reverse-shell checklist abnormal-reaction {cnt | flow0 | flow1}
配置双端平均响应时间的阈值
与正常会话相比，反弹Shell的平均响应时间可能更长或更短。默认flow0的平均响应时间小于等于1秒且
flow1的平均响应时间大于等于2秒时，判断可能受到了反弹Shell攻击。
在IPS Profile配置模式，使用以下命令，指定双端平均响应时间的阈值：
ips reverse-shell checklist avg-reaction {flow0 reaction-time | flow1 reaction-time}
l
flow0 reaction-time - 指定flow0的平均响应时间的阈值，范围是0到86400000毫秒。
l
flow1 reaction-time - 指定flow1的平均响应时间的阈值，范围是0到86400000毫秒。
在IPS Profile配置模式，使用以下命令，恢复双端平均响应时间的默认阈值：
no ips reverse-shell checklist avg-reaction { flow0 | flow1}
配置双向包比例上限
反弹Shell会话中，双向数据包的比例可能失衡。例如，从目标机到攻击机的数据包数量可能远多于从攻击机
到目标机的数据包数量。默认flow0和flow1的数据包比例的上、下限在1到3时，判断可能受到了反弹Shell
攻击。
在IPS Profile配置模式，使用以下命令，指定双向包比例上限：
ips reverse-shell checklist bidir-rate {lower rate-value | upper rate-value}
l
lower rate-value - 指定双向包比例上限，范围是0到10000。
l
upper rate-value - 指定双向包比例下限，范围是0到10000。
在IPS Profile配置模式，使用以下命令，恢复双向包比例上限的默认值：
no ips reverse-shell checklist bidir-rate {lower | upper}
配置flow1中间隔时间阈值

<!-- 来源页 2231 -->
在反弹Shell会话中，同一流向（如从攻击机到目标机）的数据包之间的间隔时间可能表现出异常模式。例
如，间隔时间可能非常短且均匀。默认flow1的命令间隔波动大于20%，命令间隔数量大于等于5时，判断可
能受到了反弹Shell攻击。
在IPS Profile配置模式，使用以下命令，指定flow1中间隔时间阈值：
ips reverse-shell checklist cmd-interval {cnt cnt-threshold | wave-range wave-rangethreshold}
l
cnt cnt-threshold - 指定flow1命令间隔数量的阈值，范围是0到10000。
l
wave-range wave-range-threshold - 指定flow1命令间隔波动的阈值，范围是0到100%。
在IPS Profile配置模式，使用以下命令，恢复flow1中间隔时间的默认阈值：
no ips reverse-shell checklist cmd-interval {cnt | wave-range}
配置连接时间阈值
反弹Shell会话的连接时间可能较长且持续不断，默认连接时间大于等于300秒时，判断可能受到了反弹
Shell攻击。
在IPS Profile配置模式，使用以下命令，指定连接时间阈值：
ips reverse-shell checklist connection-time connection-time-threshold
l
connection-time-threshold - 指定连接时间阈值，范围是0到86400秒。
在IPS Profile配置模式，使用以下命令，恢复连接时间的默认阈值：
no ips reverse-shell checklist connection-time
配置双端交换次数
与正常会话相比，反弹Shell会话中攻击机和目标机之间的数据交换次数可能更多，默认命令次数大于等于
10次时，判断可能受到了反弹Shell攻击。
在IPS Profile配置模式，使用以下命令，指定双端交换次数的阈值：
ips reverse-shell checklist exchange-cnt exchange-cnt-time
l
exchange-cnt-time - 指定双端交换次数的阈值，范围是0到10000。
在IPS Profile配置模式，使用以下命令，恢复双端交换次数的默认值：
no ips reverse-shell checklist exchange-cnt
配置小包数量及小包比例的检测阈值

<!-- 来源页 2232 -->
反弹Shell会话中可能包含大量小数据包（如TCP ACK包或小数据传输包），这些小包可能用于维持连接或
进行隐蔽通信。小包比例较高可能是反弹Shell的一个特征。默认小包数量大于等于50，小包占比大于等于
80%时，判断可能受到了反弹Shell攻击。
在IPS Profile配置模式，使用以下命令，指定小包数量的检测阈值：
ips reverse-shell checklist small-pak-cnt small-pak-cnt
l
small-pak-cnt - 指定小包数量的检测阈值，范围是0到100000。
在IPS Profile配置模式，使用以下命令，恢复小包数量的检测阈值的默认值：
no ips reverse-shell checklist small-pak-cnt
在IPS Profile配置模式，使用以下命令，指定小包比例的阈值：
ips reverse-shell checklist small-pak-rate small-pak-rate
l
small-pak-rate - 指定小包比例的阈值，范围是0到100%
在IPS Profile配置模式，使用以下命令，恢复小包比例的阈值的默认值：
no ips reverse-shell checklist small-pak-rate
配置总字节数检测阈值
反弹Shell通信带宽较低，总流量字节数一般较小。默认总字节数小于等于256KB时，判断可能受到了反弹
Shell攻击。
在IPS Profile配置模式，使用以下命令，指定总字节数检测阈值：
ips reverse-shell checklist total-bytes total-bytes
l
total-bytes - 指定小包比例的阈值，范围是0到1073741824。
在IPS Profile配置模式，使用以下命令，恢复总字节数检测阈值的默认值：
no ips reverse-shell checklist total-bytes
开启/关闭反弹Shell过滤项
系统预设反弹Shell过滤项，符合条件的流量不进入检测。用户可以根据需要关闭指定的过滤项，解决该部分
流量无法检测的问题。
开启/关闭CPU超过80%不进入检测的过滤项
设备CPU利用率过高时，设备处理packet的速度较慢，甚至有丢包的现象，导致行为特征改变，产生漏报、
误报的现象。因此当CPU超过80%时，流量默认不进入检测。
在IPS Profile配置模式，使用以下命令开启/关闭CPU超过80%不进入检测的过滤项：

<!-- 来源页 2233 -->
关闭：ips reverse-shell allowlist disable-cpu-usage
开启：no ips reverse-shell allowlist disable-cpu-usage
开启/关闭目的地址为非公网地址不进入检测的过滤项
通常情况下仅检测公网IP的反弹情况，若目的IP不是公网地址，反弹Shell的风险较低。因此，目的IP不是公
网地址的流量默认不进入检查。
在IPS Profile配置模式，使用以下命令开启/关闭非公网地址不进入检测的过滤项：
关闭：ips reverse-shell allowlist disable-dst-addr-non-public
开启：no ips reverse-shell allowlist disable-dst-addr-non-public
开启/关闭非TCP协议不进入检测的过滤项
反弹Shell通常为TCP长连接，因此协议为非TCP的流量默认不进入检查。
在IPS Profile配置模式，开启/关闭非TCP协议不进入检测的过滤项使用以下命令：
关闭：ips reverse-shell allowlist disable-null-payload
开启：no ips reverse-shell allowlist disable-null-payload
开启/关闭Self流量不进入检测的过滤项
源IP或目的IP为本机地址时，通常不是外部反弹Shell。因此，对源IP或目的IP为本机地址的Self流量默认不
进入检测。
在IPS Profile配置模式，使用以下命令开启/关闭Self流量不进入检测的过滤项：
关闭：ips reverse-shell allowlist disable-self-traffic
开启：no ips reverse-shell allowlist disable-self-traffic
开启/关闭会话时间小于5s不进入检测的过滤项
交互式反弹Shell通常是长连接，因此会话持续时间小于5s的流量默认不进入检测。
在IPS Profile配置模式，使用以下命令开启/关闭会话时间小于5s不进入检测的过滤项：
关闭：ips reverse-shell allowlist disable-sess-duration
开启：no ips reverse-shell allowlist disable-sess-duration
开启/关闭会话超过8M字节后退出检测的过滤项
较大流量通常为文件传输/媒体/备份等，而非交互式Shell。因此会话中双向流量累计字节超过8MB的流量
默认不进入检测。
在IPS Profile配置模式，使用以下命令开启/关闭会话超过8M字节后退出检测的过滤项：
关闭：ips reverse-shell allowlist disable-sess-total-bytes
开启：no ips reverse-shell allowlist disable-sess-total-bytes

<!-- 来源页 2234 -->
开启/关闭知名远控应用不进入检测的过滤项
常见管理/远程服务端口以及知名的远程桌面协议（RDP、VNC等），通常是合法远程用途。因此该部分流
量默认不进入检测。
在IPS Profile配置模式，使用以下命令开启/关闭知名远控应用不进入检测的过滤项：
关闭：ips reverse-shell allowlist disable-std-remote-traffic
开启：no ips reverse-shell allowlist disable-std-remote-traffic
配置协议异常检查功能
系统支持对指定协议报文进行异常流量检测并按指定动作进行处理，包括HTTP、DNS、FTP、MSRPC、
POP3、SMTP、SUNRPC和Telnet等。
协议异常检查功能配置流程如下：
1. 创建自定义协议检查规则并进入协议配置模式
2. 开启/关闭协议异常检查功能
3. （可选）配置协议其他检查项
4. 将协议检查规则绑定到指定IPS模板
创建自定义协议检查规则并进入协议配置模式
基于已有预定义协议为模板创建自定义协议检查规则并进入协议配置模式。如果指定的名称已存在，则直接
进入协议配置模式。
在全局配置模式下，使用以下命令，创建自定义协议检查规则并进入协议配置模式：
ips sigset sigset-name template {dhcp | dns | finger | ftp | http | imap | ldap | msrpc | mssql |
mysql | netbios | nntp | oracle | other-tcp | other-udp | pop3 | smtp | snmp | sunrpc | telnet |
tftp | voip}
l
sigset-name - 指定协议检查规则的名称。
l
dhcp | dns … | voip - 指定作为模板的预定义协议。
注意:
l
预定义协议不可以被删除也不可以被编辑。
l
自定义协议检查规则的名称不可以与预定义协议同名，也不可以重复。
l
自定义协议检查规则的名称不可重复。

<!-- 来源页 2235 -->
在全局配置模式下，使用以下命令，删除指定的协议检查规则：
no ips sigset sigset-name
［命令实例］
hostname(config)# ips sigset http1 template http
hostname(config-http-sigset)#
开启/关闭协议异常检查功能
系统支持开启/关闭协议异常检查（即协议合法性检查）功能，以及检测到异常后采取的行为。该功能默认为
关闭状态，启用后，系统会对指定协议报文（包括HTTP、DNS、FTP、MSRPC、POP3、SMTP、SUNRPC
和Telnet等）进行合法性检查，当检测出指定协议报文不符合合法性检查信息时，系统会自动将其识别为异
常报文，并按照指定动作进行处理。
在协议配置模式下，使用以下命令，开启协议异常检查功能，并指定检测到异常后需采取的处理动作：
protocol-check enable action {{ block-service {permanent | second timeout | hour timeout |
day timeout} | block-ip {permanent | second timeout | hour timeout | day timeout} | log-only
| reset} pcap {disable | enable}
l
enable -启用协议合法性检查。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-ip {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指
定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
l
pcap {disable | enable} - enable对异常数据包进行抓包取证；disable不对异常数据包进行抓包取
证。

<!-- 来源页 2236 -->
注意: 对于不带硬盘的设备和带硬盘的A1600/A1800/A2200设备，开启抓包取证功能时，需
同时开启“加入用户体验改进计划”并开启云·景的威胁日志上报，抓包取证功能才能生效。在
该情况下，防火墙设备上将无法查看到抓包取证的报文数据，系统会将抓包取证的报文数据和
威胁日志信息上送至云·景，安全运营人员可以根据抓包取证的证据信息对威胁日志信息进行分
析研判。
在协议配置模式下，使用以下命令，关闭协议异常检查功能：
protocol-check disable
［命令实例］
hostname(config)# ips sigset http1 template http
hostname(config-http-sigset)# protocol-check strict
hostname(config-http-sigset)# protocol-check enable action log-only
启用/禁用协议异常相关的特征规则
开启协议异常检查功能后，系统默认启用该协议异常相关的所有特征规则，用户可根据需要，启用或禁用协
议异常相关的指定特征规则。当指定协议的某个特征规则被禁用后，系统将不对出现该特征的协议报文进行
检测和防护。例如：用户禁用了HTTP协议异常相关的360004特征规则（HTTP URI长度超过指定值）后，
系统就不会检测URI长度超出指定阈值的HTTP协议报文。
在协议配置模式下，使用以下命令，禁用/启用协议异常相关的特征规则：
禁用：disable protocol-anomaly id
启用：no disable protocol-anomaly id
l
id - 指定被禁用/启用的特征规则ID。
［命令实例］
hostname(config)# ips sigset http1 template http
hostname(config-http-sigset)# disable protocol-anomaly 360001
配置协议其他检查项
协议异常检查功能开启后，用户可以通过配置协议的其他检查项（如请求报文的最大长度、命令行最大长度
等），为系统制定更详细的协议检查规则。这些规则旨在对指定协议的报文进行深度检测和分析，以判断其
是否符合预设的规范和标准。当网络流量所在协议不符合这些规则时，系统会自动将该协议报文视为异常，
并按照指定动作对其进行相应的处理。
指定协议最大扫描长度

<!-- 来源页 2237 -->
指定HTTP，DNS，FTP，MSRPC，POP3，SMTP，SUNRPC和Telnet协议扫描的最大长度，默认协议扫
描最大长度为4096字节。
在协议配置模式下，使用以下命令，指定协议最大扫描长度：
max-scan-bytes length
l
length - 指定最大扫描长度，单位为字节。取值范围是0到65535字节，0表示不限制。
在协议配置模式下，使用以下命令，恢复默认值：
no max-scan-bytes
［命令实例］
hostname(config)# ips sigset test1 template other-tcp
hostname(config-other-tcp-sigset)# max-rsp-line-length 1000
开启/关闭服务器Banner信息保护功能
注意: 仅HTTP、FTP、POP3和SMTP协议适用。
Banner信息通常是在建立连接时，服务器向客户端发送的一段文本信息，包含了操作系统版本、服务版
本、设备型号等敏感信息。用户可以通过开启服务器（FTP、Web、POP3、SMTP）Banner信息保护功能
并设置新信息替换原有服务器banner信息，有效控制和隐藏服务的Banner信息，防止泄露过多的系统信息
给潜在攻击者，从而提高系统的安全性。
在协议配置模式下，使用以下命令，开启服务器Banner信息保护功能并指定Banner信息：
banner-protect enable [replace-with string]
l
enable - 开启服务器banner信息保护功能。
l
replace-with string - 指定banner信息。
在协议配置模式下，使用以下命令，关闭服务器Banner信息保护功能：
no banner-protect enable
［命令实例］
hostname(config)# ips sigset test template ftp
hostname(config-ftp-sigset)# banner-protect enable replace-with vsftp2.0
指定命令行最大长度
注意: 仅FTP、POP3和SMTP协议适用。

<!-- 来源页 2238 -->
指定FTP命令行/POP3客户端命令行/SMTP客户端命令行的最大长度（包含回车换行）以及发现异常后的处
理动作。当FTP命令行/POP3客户端命令行/SMTP客户端命令行长度超过系统设定阈值时，系统会将该
FTP/POP3/SMTP协议报文视为异常协议，并按照指定动作处理。若不指定，FTP命令行/POP3客户端命令
行/SMTP客户端命令行的最大长度默认为512字节，处理动作默认为只记录日志（log-only）。
在协议配置模式下，使用以下命令，指定FTP命令行/POP3客户端命令行/SMTP客户端命令行的最大长度
（包含回车换行）以及发现异常后的处理动作：
max-cmd-line-length length action {block-ip {permanent | second timeout | hour timeout |
day timeout} | block-service {permanent | second timeout | hour timeout | day timeout} | logonly | reset}
l
length - 指定命令行的最大长度，单位为字节。FTP命令行最大长度的取值范围是5到1024字
节；POP3和SMTP客户端命令行最大长度的取值范围是64到1024字节。
l
block-ip {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指
定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-cmd-line-length
［命令实例］
hostname(config)# ips sigset test1 template ftp
hostname(config-ftp-sigset)# max-cmd-line-length 80 action log-only
指定FTP服务器端响应的最大长度

<!-- 来源页 2239 -->
注意: 仅FTP协议适用。
指定系统允许的FTP服务器端响应的最大长度，以及发现异常后的处理动作。当FTP服务器端响应的长度超过
系统设定阈值时，系统会将该FTP协议报文视为异常协议，并按照指定动作处理。若不指定，系统允许的FTP
服务器端响应的最大长度默认为512字节，处理动作默认为只记录日志（log-only）。
在协议配置模式下，使用以下命令，指定系统允许的FTP服务器端响应的最大长度，以及发现异常后的处理
动作：
max-rsp-line-length length action {block-ip {permanent | second timeout | hour timeout |
day timeout} | block-service {permanent | second timeout | hour timeout | day timeout} | logonly | reset}
l
length - 指定最大响应长度，单位为字节。取值范围是5到1024字节。
l
block-ip {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指
定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-rsp-line-length
［命令实例］
hostname(config)# ips sigset test1 template ftp
hostname(config-ftp-sigset)# max-rsp-line-length 100 action log-only
指定POP3服务器/SMTP服务器返回错误的最大次数

<!-- 来源页 2240 -->
注意: 仅POP3和SMTP协议支持该功能。
指定系统允许的POP3服务器/SMTP服务器返回错误的最大次数（同一个POP3会话/SMTP会话中），以及
发现异常后的处理动作。系统通过对同一个POP3会话/SMTP会话中的服务器返回错误的次数进行限制，可
以有效防止用户的非法尝试。
当同一个POP3会话/SMTP会话中的服务器返回错误的次数超过系统允许的最大次数时，系统会将该
POP3/SMTP协议报文视为异常协议，并按照指定动作处理。若不指定，同一个POP3会话/SMTP会话中的
服务器返回错误的的最大次数默认为0，即不做次数限制。
在协议配置模式下，使用以下命令，指定系统允许的POP3服务器/SMTP服务器返回错误的最大次数（同一
个POP3会话/SMTP会话中），以及发现异常后的处理动作：
max-failure times action {block-ip {permanent | second timeout | hour timeout | day
timeout} | block-service {permanent | second timeout | hour timeout | day timeout} | log-only
| reset}
l
times - 指定系统允许的POP3服务器/SMTP服务器返回错误的最大次数（同一个POP3会话/SMTP会话
中）。范围为0到512。
l
block-ip {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指
定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-failure
［命令实例］
hostname(config)# ips sigset pop3-cus template pop3

<!-- 来源页 2241 -->
hostname(config-pop3-sigset)# max-failure 8 action log-only
指定POP3客户端命令参数的最大长度
注意: 仅POP3协议适用。
指定POP3客户端命令参数的最大长度以及发现异常后的处理动作。当POP3客户端命令参数长度超过系统设
定阈值时，系统会将该POP3协议报文视为异常协议，并按照指定动作处理。若不指定，POP3客户端命令参
数的最大长度默认为40字节，处理动作默认为只记录日志（log-only）。
在协议配置模式下，使用以下命令，指定POP3客户端命令参数的最大长度以及发现异常后的处理动作
max-arg-length length action {block-ip {permanent | second timeout | hour timeout |day
timeout}| block-service {permanent |second timeout | hour timeout | day timeout}| log-only
| reset}
l
length - 指定命令参数的最大长度，单位为字节。默认为40字节。
l
block-ip {permanent|second timeout |hour timeout | day timeout} - 指定阻断攻击者IP并指定
阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-arg-length
［命令实例］
hostname(config)# ips sigset pop3-cus template pop3
hostname(config-pop3-sigset)# max-arg-length 30 action log-only

<!-- 来源页 2242 -->
指定SMTP协议邮件附件名称的最大长度
注意: 仅SMTP协议适用。
指定系统允许的SMTP协议邮件附件名称的最大长度以及发现异常后的处理动作。当SMTP协议邮件附件名称
的长度超过系统允许的最大长度时，系统会将该SMTP协议报文视为异常协议，并按照指定动作处理。若不
指定，系统允许的SMTP协议邮件附件名称的最大长度默认为128字节，处理动作默认为只记录日志（logonly）。
在协议配置模式下，使用以下命令，指定系统允许的SMTP协议邮件附件名称的最大长度以及发现异常后的
处理动作：
max-content-filename-length length action {block-ip {permanent | second timeout | hour
timeout |day timeout}| block-service {permanent |second timeout | hour timeout | day
timeout}| log-only | reset}
l
length - 指定SMTP协议邮件附件名称的最大长度，单位为字节。取值范围是64到1024字节。
l
block-ip {permanent| second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指
定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-content-filename-length
［命令实例］
hostname(config)# ips sigset smtp-cus template smtp
hostname(config-smtp-sigset)# max-content-filename-length 512 action log-only

<!-- 来源页 2243 -->
指定SMTP协议Content-Type值的最大长度
注意: 仅SMTP协议适用。
指定系统允许的SMTP协议Content-Type值的最大长度以及发现异常后的处理动作。当SMTP协议
Content-Type值的长度超过系统允许的最大长度时，系统会将该SMTP协议报文视为异常协议，并按照指
定动作处理。若不指定，系统允许的SMTP协议Content-Type值的最大长度默认为128字节，处理动作默认
为只记录日志（log-only）。
在协议配置模式下，使用以下命令，指定系统允许的SMTP协议Content-Type值的最大长度以及发现异常
后的处理动作：
max-content-type-length length action {block-ip {permanent | second timeout | hour
timeout | day timeout} | block-service {permanent | second timeout | hour timeout | day
timeout} | log-only | reset}
l
length - 指定SMTP协议Content-Type值的最大长度，单位为字节。取值范围是64到1024字节。
l
block-ip {permanent| second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指
定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-content-type-length
［命令实例］
hostname(config)# ips sigset smtp-cus template smtp
hostname(config-smtp-sigset)# max-content-type-length 256 action log-only

<!-- 来源页 2244 -->
指定SMTP客户端命令中reverse-path和forward-path的最大长度
注意: 仅SMTP协议适用。
指定系统允许的SMTP客户端命令中reverse-path和forward-path的最大长度，以及发现异常后的处理动
作。当SMTP客户端命令中reverse-path和forward-path的长度超过系统设定阈值时，系统会将该SMTP
协议报文视为异常协议，并按照指定动作处理。若不指定，系统允许的SMTP客户端命令中reverse-path和
forward-path的最大长度默认为256字节，处理动作默认为只记录日志（log-only）。
在协议配置模式下，使用以下命令，指定系统允许的SMTP客户端命令中reverse-path和forward-path的
最大长度，以及发现异常后的处理动作：
max-path-length length action {block-ip {permanent | second timeout | hour timeout | day
timeout} | block-service {permanent |second timeout | hour timeout | day timeout} | log-only
| reset}
l
length - 指定系统允许的SMTP客户端命令中reverse-path和forward-path的最大长度，单位为字
节，范围为16到512（含标点符号）。
l
block-ip {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指
定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-path-length
［命令实例］
hostname(config)# ips sigset smtp-cus template smtp

<!-- 来源页 2245 -->
hostname(config-smtp-sigset)# max-path-length 128 action log-only
指定SMTP服务器端响应的最大长度
注意: 仅SMTP协议适用。
指定系统允许的SMTP服务器端响应的最大长度，以及发现异常后的处理动作。当SMTP服务器端响应的长度
（含回车换行）超过系统设定阈值时，系统会将该SMTP协议报文视为异常协议，并按照指定动作处理。若
不指定，系统允许的SMTP服务器端响应的最大长度默认为512字节，处理动作默认为只记录日志（logonly）。
在协议配置模式下，使用以下命令，指定系统允许的SMTP服务器端响应的最大长度，以及发现异常后的处
理动作：
max-reply-line-length length action {block-ip {permanent | second timeout | hour timeout |
day timeout} | block-service {permanent | second timeout | hour timeout | day timeout} | logonly | reset}
l
length - 指定系统允许的SMTP服务器端响应的最大长度，单位为字节，范围为64到1024（含回车换
行）。
l
block-ip {permanent| second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指
定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-reply-line-length
［命令实例］

<!-- 来源页 2246 -->
hostname(config)# ips sigset smtp-cus template smtp
hostname(config-smtp-sigset)# max-reply-line-length 1024 action log-only
指定SMTP客户端邮件文本的最大长度
注意: 仅对SMTP协议适用。
指定系统允许的SMTP客户端邮件文本的最大长度，以及发现异常后的处理动作。当SMTP客户端邮件文本的
长度超过系统设定阈值时，系统会将该SMTP协议报文视为异常协议，并按照指定动作处理。若不指定，系
统允许的SMTP客户端邮件文本的最大长度默认为1000字节，处理动作默认为只记录日志（log-only）。
在协议配置模式下，使用以下命令，指定系统允许的SMTP客户端邮件文本的最大长度，以及发现异常后的
处理动作：
max-text-line-length length action {block-ip {permanent | second timeout | hour timeout
|day timeout}| block-service {permanent | second timeout | hour timeout | day timeout} | logonly | reset}
l
length - 指定系统允许的SMTP客户端邮件文本的最大长度，单位为字节，范围为64到2048（含回车换
行）。
l
block-ip {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指
定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-text-line-length
［命令实例］

<!-- 来源页 2247 -->
hostname(config)# ips sigset smtp-cus template smtp
hostname(config-smtp-sigset)# max-text-line-length 1024 action log-only
指定HTTP协议URI的最大长度
注意: 仅对HTTP协议适用。
URI（Uniform Resource Identifier，统一资源标识符）是一个用于标识某一互联网资源名称的字符串，
其主要作用是在网络中对资源进行唯一标识，以便用户通过特定的协议进行交互操作。Web上可用的每种资
源，如HTML文档、图像、视频片段、程序等，都由一个URI进行标识。
用户通过指定HTTP协议URI的最大长度以及处理动作，可以检测出系统中URI长度超过系统设定阈值的HTTP
协议报文，并让系统按照指定动作对超出阈值的HTTP协议报文进行处理。
在协议配置模式下，使用以下命令，指定系统允许的HTTP协议URI的最大长度，以及发现异常后的处理动
作：
max-uri-length length action {block-ip {permanent | second timeout | hour timeout | day
timeout} | block-service {permanent | second timeout | hour timeout | day timeout} | log-only
| reset}
l
length - 指定URI最大长度，单位为字节，范围为64到4096。若不指定，系统默认为4096字节。
l
block-ip {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指
定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-uri-length

<!-- 来源页 2248 -->
［命令实例］
hostname(config)# ips sigset http1 template http
hostname(config-http-sigset)# max-uri-length 1000 action log-only
开启/关闭HTTP数据包扫描功能
注意: 仅对HTTP协议适用。
系统支持开启/关闭HTTP数据包扫描功能，该功能默认为关闭状态。当该功能处于关闭状态时，系统会自动
对服务器返回的HTTP数据包进行扫描，及时检测可能存在的安全隐患或协议异常情况。而一旦该功能被启
用，系统则会停止对服务器返回的HTTP数据包进行扫描。
在协议配置模式下，使用以下命令，开启/关闭HTTP数据包扫描功能：
l
开启：response-bypass
l
关闭：no response-bypass
［命令实例］
hostname(config)# ips sigset http1 template http
hostname(config-http-sigset)# response-bypass
指定MSRPC协议绑定报文的最大长度
注意: 仅MSRPC协议适用。
指定系统允许的MSRPC协议绑定报文的最大长度以及发现异常后的处理动作。当MSRPC协议绑定报文的长
度超过系统允许的最大长度时，系统会将该MSRPC协议报文视为异常协议，并按照指定动作处理。若不指
定，系统允许的MSRPC协议绑定报文的最大长度默认为2048字节，处理动作默认为只记录日志（logonly）。
在协议配置模式下，使用以下命令，指定系统允许的MSRPC协议绑定报文的最大长度以及发现异常后的处理
动作：
max-bind-length length action {block-ip {permanent | second timeout | hour timeout |day
timeout}| block-service {permanent |second timeout | hour timeout | day timeout}| log-only |
reset}

<!-- 来源页 2249 -->
l
length - 指定绑定报文的最大长度，单位为字节。取值范围是16到65535字节。
l
block-ip {permanent|second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指定
阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-bind-length
［命令实例］
hostname(config)# ips sigset msrpc-cus template msrpc
hostname(config-msrpc-sigset)# max-bind-length 3000 action log-only
指定MSRPC协议请求报文的最大长度
注意: 仅MSRPC协议适用。
指定系统允许的MSRPC协议请求报文的最大长度，以及发现异常后的处理动作。当MSRPC协议请求报文的
长度超过系统设定阈值时，系统会将该MSRPC协议报文视为异常协议，并按照指定动作处理。若不指定，系
统允许的MSRPC协议请求报文的最大长度默认为65535字节，处理动作默认为只记录日志（log-only）。
在协议配置模式下，使用以下命令，指定系统允许的MSRPC协议请求报文的最大长度，以及发现异常后的处
理动作：
max-request-length length action {block-ip {permanent | second timeout | hour timeout |
day timeout} | block-service {permanent | second timeout | hour timeout | day timeout} | logonly | reset}

<!-- 来源页 2250 -->
l
length - 指定请求报文的最大长度，单位为字节。取值范围是16到65535字节。
l
block-ip {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指
定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-request-length
［命令实例］
hostname(config)# ips sigset msrpc-cus template msrpc
hostname(config-msrpc-sigset)# max-request-length 60000 action log-only
指定Telnet用户名和密码的最大长度
注意: 仅Telnet协议适用。
指定系统允许的Telnet用户名和密码的最大长度，以及发现异常后的处理动作。当Telnet用户名和密码的长
度超过系统允许的最大长度时，系统会将该Telnet协议报文视为异常协议，并按照指定动作处理。若不指
定，系统允许的Telnet用户名和密码的最大长度默认为128字节，处理动作默认为只记录日志（logonly）。
在协议配置模式下，使用以下命令，指定系统允许的Telnet用户名和密码的最大长度以及发现异常后的处理
动作：
max-input-length length action {block-ip {permanent | second timeout | hour timeout | day
timeout} | block-service {permanent | second timeout | hour timeout | day timeout} | log-only
| reset}

<!-- 来源页 2251 -->
l
length - 指定Telnet用户名和密码的最大长度，单位为字节，范围为6到1024。
l
block-ip {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者IP并指
定阻断时长。
o
permanent - 指定对攻击者IP进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者IP进行阻断的时长。单位分别
为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
block-service {permanent | second timeout | hour timeout | day timeout} - 指定阻断攻击者
服务并指定阻断时长。
o
permanent - 指定对攻击者服务进行永久阻断。
o
second timeout | hour timeout | day timeout - 指定对攻击者服务进行阻断的时长。单位分
别为秒/小时/天，范围分别是60到3600秒/1到24小时/1到15天。
l
log-only - 匹配该特征后仅记录日志信息。
l
reset - 匹配该特征后重置连接（TCP）或者发送目标不可达包（UDP）并且记录日志信息。
在协议配置模式下，使用以下命令，恢复默认值：
no max-input-length
［命令实例］
hostname(config)# ips sigset telnet-cus template telnet
hostname(config-telnet-sigset)# max-input-length 30 action log-only
将协议检查规则绑定到IPS模板中
用户创建自定义协议检查规则后，需要将该协议检查规则绑定到IPS模板（IPS Profile）中才能生效，即对
系统中指定协议进行异常流量检测。
注意: 同种类型的协议检查规则不可以添加到同一个IPS Profile中，例如两个以HTTP为模板的自
定义协议检查规则不可以添加到同一个IPS Profile中。
在IPS Profile配置模式下，使用以下命令，将指定协议检查规则绑定到IPS Profile中：
sigset user-defined-profile
l
user-defined-profile - 指定添加已创建的自定义协议检查规则到IPS Profile中。
在IPS Profile配置模式下，使用以下命令，将指定协议检查规则从IPS Profile中删除：

<!-- 来源页 2252 -->
no sigset user-defined-profile
［命令实例］
hostname(config)# ips profile ips-profile1
hostname(config-profile)# sigset test
抓包取证
介绍
当威胁流量经过设备时，系统会抓取相关威胁报文，用户可以在对应的威胁日志中查看或下载抓取的报文。
同时可以结合连接云平台功能，将威胁报文数据上送至云端，助力用户快速完成威胁研判和处置。
使用限制和注意事项
通用
l 对于不带硬盘的设备和带硬盘的A1600/A1800/A2200设备，开启抓包取证功能时，需同时开启“加入用户体验
改进计划”并开启云·景的威胁日志上报，抓包取证功能才能生效。在该情况下，防火墙设备上将无法查看到抓
包取证的报文数据，系统会将抓包取证的报文数据和威胁日志信息上送至云·景，安全运营人员可以根据抓包取
证的证据信息对威胁日志信息进行分析研判。
抓包取证模式相关
l 抓包取证模式只对入侵检测和僵尸网络防御功能生效。
l 抓包取证模式为扩展模式时，最多支持抓取100个报文。
l 抓包取证模式为扩展模式时，若威胁报文数据超过了配置的“单次连接取证报文量上限”或超过100个报文，可
能会出现抓取的威胁报文数据不完整的情况。
l 若抓包取证功能占用的内存超过总DP（数据平面）内存的十分之一时，无论此时系统配置的抓包取证模式是基础
模式还是扩展模式，后续系统检测到威胁时采用的抓包取证模式均为基础模式。（可以使用show memory
detail命令查看系统DP内存使用情况）
入侵防御功能相关
l 反弹shell检测仅支持抓取检测出威胁的单个报文。
l 弱口令检测和HTTP明文密码检测不支持将证据报文上送至云端。
僵尸网络防御功能相关

<!-- 来源页 2253 -->
l TCP协议检测和DNS域名检测支持抓取检测出威胁的单个报文，也支持抓取后续的业务交互报文。
l Sinkhole恶意IP日志不支持抓包取证。
抓包取证配置步骤
1. 全局配置抓包取证模式。
抓包取证有基础和扩展两种模式，系统默认使用基础模式进行抓包取证。
l 基础模式：系统能够抓取检测到威胁时的报文。对于HTTP协议，系统会抓取请求和响应报文。
l 扩展模式：系统能够抓取检测到威胁时以及检测到威胁前的报文数据，抓取的报文数据量上限可以通过
“单个连接取证报文量”进行配置。对于僵尸网络检测功能中的HTTP协议以及入侵检测功能，系统会抓
取请求和响应报文。
配置抓包取证模式，在全局配置模式下，使用以下命令：
attack-forensics-mode {basic | extended limit value}
l basic - 指定使用基础模式进行抓包取证。
l extended limit value - 使用扩展模式进行抓包取证。使用扩展模式时，需要同时配置单个连接取证报文
量上限，达到上限后，对最早抓取的报文数据进行丢弃。范围是5-50KB，默认为5KB。
注意: 抓包取证模式只对入侵防御和僵尸网络防御功能生效。
2. 开启入侵防御/僵尸网络防御的抓包取证功能开关。
开启入侵防御/僵尸网络防御的抓包取证功能后，当系统检测到对应威胁时会抓取相关报文。用户可以在
对应的威胁日志中查看或下载抓取的报文。
l 开启僵尸网络防御的抓包取证功能，在僵尸网络防御Profile配置模式下，使用attack-forensic enable命
令。如需关闭此功能，可以在僵尸网络防御Profile配置模式下，使用attack-forensic disable命令。默认
情况下，默认情况下，僵尸网络防御的抓包取证功能为开启状态。
l 开启入侵防御的抓包取证功能，在IPS Profile配置模式下，使用pcap enable命令。如需关闭此功能，可
以在IPS Profile配置模式下，使用pcap disable命令。默认情况下，入侵防御的抓包取证功能为关闭状
态。
3. （可选）连接云平台，启用“加入用户体验改进计划”和“云·景”。
开启后，当设备检测出威胁时会进行抓包处理，并将抓包获取的威胁报文数据和威胁日志信息上送至云·
景，用户可以登录云·景进行查看和处置。

<!-- 来源页 2254 -->
a. 连接云平台：参阅“云平台服务器对接配置”章节。
b. 加入用户体验改进计划：在Cloud Server配置模式下，使用user-experience-improvement-plan
enable命令。
c. 启用云·景：在Cloud View配置模式下，使用enable命令。
d. 开启威胁日志上报：在Cloud View配置模式下，使用uptype-log threat-event命令。
4. 查看威胁证据信息。
当威胁流量经过设备时，设备会检测出威胁并进行抓包处理，用户可以在WebUI上查看或下载获取的威
胁报文数据信息。
对于僵尸网络防御中通过TCP协议检测或DNS域名检测所命中的威胁，用户还可以在WebUI上查看或下
载关联连接报文，以获取后续的业务交互数据，辅助威胁研判。
查看抓包缺失原因统计数据
该功能主要用于帮助用户诊断报文无法完整抓取的原因，评估威胁分析所依赖的数据完整性。
查看抓包缺失原因的统计数据，在任意模式下，使用以下命令：
show attack-forensics-statistic

<!-- 来源页 2255 -->
返回示例：
hostname# show attack-forensics-statistic
Attack forensics statistic:
no response count:181.
exceed time count:7.
exceed memory count:2.
exceed limit count:2.
dropped by speed control:1.
显示信息
统计的抓包缺失原因
说明
no response
count
超过2秒未收到响应报文
系统发送抓包请求后，若在2秒内未收到响应报文，则会
导致抓包数据缺失。
exceed time
count
距离取证开始超过5秒，
转为基础模式
扩展模式下，系统对每个session进行抓包时，从抓取到
第一个包开始计时。若超过5秒仍未完成抓包，系统将自
动切换至基础模式，从而导致抓包数据不完整。
exceed memory
count
当前占用的DP内存超过
总内存的1/10，转为基
础模式
扩展模式下，当抓包取证占用的DP（Data plane，数据
平面）内存超过系统总DP内存的10%时，系统会自动切
换至基础模式抓包，从而导致抓包数据不完整。
exceed limit
count
超出抓包上限，删除部分
报文
当系统抓取的单个连接取证报文量超过预设阈值时，将自
动删除超出部分的报文，从而造成抓包数据缺失。
dropped by
speed control
流量超速被限速丢包
当报文流量速率超出硬件处理能力上限时，限速机制将主
动丢弃部分报文，进而导致抓包数据缺失。
清除抓包缺失原因统计数据
在任何模式下，使用以下命令，清除抓包缺失原因统计数据：
show attack-forensics-statistic clear
将IPS模板绑定到安全域或策略规则上
开始之前
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。

<!-- 来源页 2256 -->
用户在完成IPS模板配置后，需要将指定IPS模板绑定到安全域或策略规则上，才可执行相应的安全防护能
力，从而抵御网络威胁对业务系统的侵害，避免网络威胁对客户造成损失。此外，根据用户需求，还可以将
IPS模板绑定到ZTNA策略，对与ZTNA策略相匹配的流量进行入侵防御检测和处理。相关配置请参阅配置
ZTNA策略。
前置条件
已创建IPS模板，并为该IPS模板配置相关的检测和防护规则，详见“"配置IPS入侵防御模板" 在第2182页”
章节。
基于安全域开启IPS入侵防御功能
在安全域上开启IPS入侵防御功能，并将指定IPS模板（IPS Profile）绑定到该安全域上。一个安全域只能绑
定一个IPS Profile。
在安全域配置模式下，使用以下命令，开启IPS入侵防御功能，并将指定IPS Profile绑定到安全域上：
ips enable {no-ips | predef_default | predef_loose | predef_critical | DMZ-server | Generalserver | web-server | Unix-like-server | Windows-server | profile-name} {egress | ingress |
bidirectional}
l
no-ips - 指定使用名为“no-ips”的预定义IPS Profile，含义为不做IPS检测。
l
predef_default - 指定使用名为“predef_default”的预定义IPS Profile，包含可信度为中和高的所
有IPS 特征，对威胁进行检测并执行规则默认动作。
l
predef_loose - 指定使用名为“predef_loose”的预定义IPS Profile，包含所有类型的IPS特征，对
威胁进行检测且处理行为默认为只记录日志。
l
predef_critical - 指定使用名为“predef_critical”的预定义IPS Profile，包含最新时段高危类型的
攻击检测，对检测效果要求严格，且处理行为默认为重置。
l
DMZ-server - 指定使用名为“DMZ-server”的预定义IPS Profile，包含除TFTP和NETBIOS协议之
外的所有攻击检测，对威胁进行检测且处理行为默认为只记录日志。
l
General-server - 指定使用名为“General-server”的预定义IPS Profile，包含针对漏洞扫描、拒绝
服务攻击和后门木马类的攻击检测规则，对威胁进行检测且处理行为默认为只记录日志。
l
web-server - 指定使用名为“web-server”的预定义IPS Profile，包含所有Web攻击类检测，以及
对SQL注入和XSS注入的通用检测，对威胁进行检测且处理行为默认为只记录日志。
l
Unix-like-server - 指定使用名为“Unix-like-server”的预定义IPS Profile，包含针对Linux、
Solaris系统攻击的检测规则，对威胁进行检测且处理行为默认为只记录日志。

<!-- 来源页 2257 -->
l
Windows-server - 指定使用名为“Windows-server”的预定义IPS Profile，包含针对Windows系
统攻击的检测规则，对威胁进行检测且处理行为默认为只记录日志。
l
profile-name - 指定绑定到安全域上的自定义IPS Profile的名称。指定后，该IPS Profile在安全域上
生效。
l
egress - 指定对出该安全域的流量进行IPS检测。
l
ingress - 指定对进入该安全域的流量进行IPS检测。
l
bidirectional - 指定对出入该安全域的流量都进行IPS检测。
在安全域配置模式下，使用以下命令，关闭安全域的IPS入侵防御功能：
no ips enable
［命令实例］
hostname(config)# zone trust
hostname(config-zone-trust)# ips enable test bidirectional
基于策略开启IPS入侵防御功能
在策略规则上开启IPS入侵防御功能，并将指定IPS模板（IPS Profile）绑定到该策略规则上。如果需要IPS
对HTTPS流量进行扫描，需要为此条策略启用SSL代理功能，详细说明请参阅“对HTTPS流量进行IPS检
测”。
在策略规则配置模式下，使用以下命令，开启IPS入侵防御功能，并将指定IPS Profile绑定到策略规则上：
ips {no-ips | predef_default | predef_loose | predef_critical | DMZ-server | General-server |
web-server | Unix-like-server | Windows-server | ips-profile-name}
l
no-ips - 指定使用名为“no-ips”的预定义IPS Profile，含义为不做IPS检测。
l
predef_default - 指定使用名为“predef_default”的预定义IPS Profile，包含可信度为中和高的所
有IPS 特征，对威胁进行检测并执行规则默认动作。
l
predef_loose - 指定使用名为“predef_loose”的预定义IPS Profile，包含所有类型的IPS特征，对
威胁进行检测且处理行为默认为只记录日志。
l
predef_critical - 指定使用名为“predef_critical”的预定义IPS Profile，包含最新时段高危类型的
攻击检测，对检测效果要求严格，且处理行为默认为重置。
l
DMZ-server - 指定使用名为“DMZ-server”的预定义IPS Profile，包含除TFTP和NETBIOS协议之
外的所有攻击检测，对威胁进行检测且处理行为默认为只记录日志。

<!-- 来源页 2258 -->
l
General-server - 指定使用名为“General-server”的预定义IPS Profile，包含针对漏洞扫描、拒绝
服务攻击和后门木马类的攻击检测规则，对威胁进行检测且处理行为默认为只记录日志。
l
web-server - 指定使用名为“web-server”的预定义IPS Profile，包含所有Web攻击类检测，以及
对SQL注入和XSS注入的通用检测，对威胁进行检测且处理行为默认为只记录日志。
l
Unix-like-server - 指定使用名为“Unix-like-server”的预定义IPS Profile，包含针对Linux、
Solaris系统攻击的检测规则，对威胁进行检测且处理行为默认为只记录日志。
l
Windows-server - 指定使用名为“Windows-server”的预定义IPS Profile，包含针对Windows系
统攻击的检测规则，对威胁进行检测且处理行为默认为只记录日志。
l
ips-profile-name - 指定绑定到策略上的自定义IPS Profile的名称。指定后，该IPS Profile在策略上
生效。
在策略规则配置模式下，使用以下命令，关闭策略上的IPS入侵防御功能：
no ips
［命令实例］
hostname(config)# policy-global
hostname(config-policy)# rule id test
hostname(config-policy-rule)# ips DMZ-server
配置入侵防御全局参数
开始之前
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。
入侵防御全局参数配置包括：
l 开启/关闭入侵防御功能
l 配置日志聚合类型和时间粒度
l 指定入侵防御工作模式
l 开启/关闭IPS防逃逸功能
l 配置保持时间

<!-- 来源页 2259 -->
开启/关闭入侵防御功能
系统支持开启/关闭系统的IPS功能。配置完成后，需要重启设备。
在执行模式下，使用以下命令，开启/关闭入侵防御功能。
l
开启：exec ips enable
l
关闭：exec ips disable
注意:
l
该命令仅在安装有IPS许可证的平台有效。
l
执行exec ips enable命令或者exec ips disable命令后，需要重启设备才能开启或者关闭
IPS功能。设备重启后，部分平台的最大并发连接数会根据IPS功能的开启或者关闭状态减少或
者恢复正常。关于系统最大并发连接数变化的详细信息，请参阅"调整系统最大并发连接数" 在
第894页。
l
非根VSYS不支持此命令。
［命令实例］
hostname# exec ips enable
配置日志聚合类型和时间粒度
用户通过配置日志聚合类型和日志聚合时间粒度，可以将符合聚合规则的日志信息进行聚合，还可以将同一
时间粒度内、同一类型的日志只存入数据库一次，从而减少日志数量，避免日志服务器接收冗余的日志信
息。若不进行配置，则按照默认聚合类型（相同源IP且相同目的IP）和默认时间粒度（10秒）进行日志聚
合。
注意:
l
系统仅支持聚合由IPS功能所产生的日志信息。
l
非根VSYS不支持此命令。
在全局配置模式下，使用以下命令，配置日志聚合类型和时间粒度：
ips log aggregation {by-src | by-dst | by-src-dst} [aggregation-time time-value]
l
by-src - 将相同源IP的日志进行聚合。
l
by-dst - 将相同目的IP的日志进行聚合。

<!-- 来源页 2260 -->
l
by-src-dst - 将相同源IP、相同目的IP的日志进行聚合。该选项为系统默认的日志聚合类型。
l
aggregation-time time-value - 指定入侵防御同类型（即指定的聚合类型）的威胁日志存入数据库
的时间粒度。指定后，系统将对同一时间粒度内、同一类型的日志只存入数据库一次，不再重复存入多
次。取值范围为10-600秒，默认值为10秒。
在全局配置模式下使用no ips log aggregation指定日志聚合类型为“不聚合”，即不聚合日志。每一条
入侵防御日志分别存入数据库，不进行日志聚合。
指定入侵防御工作模式
指定IPS工作模式。当前支持IPS模式和只记录日志模式。
在全局配置模式下，使用以下命令，指定IPS工作模式：
ips mode {ips | ips-logonly}
l
ips - 指定IPS工作模式为IPS模式，即在提供协议异常和网络攻击行为的告警、日志功能的同时，还对检
出攻击做重置和阻断操作。该模式为系统默认模式。
l
ips-logonly - 指定IPS工作模式为只记录日志模式，即提供协议异常和网络攻击行为的告警、日志功
能，不对检出攻击做重置和阻断操作。
注意: 非根VSYS不支持此命令。
开启/关闭IPS防逃逸功能
扫描攻击通常位于网络攻击的侦察阶段。在这个阶段，攻击者会使用各种工具和技术对目标网络进行扫描，
以识别开放的端口、运行的服务、操作系统类型等信息。这些信息帮助攻击者了解目标网络的布局和潜在的
漏洞，为后续的攻击做准备。
扫描攻击可能会在流量前端携带大量无效信息，导致系统无法在最大扫描长度中有效检测出扫描攻击。因
此，系统支持IPS防逃逸功能，当入侵防御功能或攻击防护功能检测出扫描攻击时，会将对应的攻击者IP记录
为风险IP，当相关的风险IP再次触发入侵防御检测时，系统将解除IPS最大扫描长度，完整扫描会话全部长度
的流量数据。IPS防逃逸功能默认为关闭状态。
注意:
l
系统最多支持记录1024个风险IP，达到上限后，会删除最早记录的风险IP。
l
风险IP最多保存6小时，系统将自动清除超时的风险IP。
l
系统重启后，将不会保留已记录的风险IP。

<!-- 来源页 2261 -->
开启/关闭IPS防逃逸功能，在全局配置模式下，使用以下命令：
开启：ips defense-evasion enable
关闭：ips defense-evasion disable
配置保持时间
保持时间是指在IPS特征库更新后，为新特征（包括新增和更新的特征）设置的监控观察期。在观察期内，
新特征仅记录日志，不执行阻断等防护动作，从而避免因新特征直接上线引发误报，提升IPS防护的稳定性
与可靠性。
提示: 该功能仅对IPS特征库3.0.284及之后版本中的新增或更新特征生效。由于默认保持时间与
IPS特征库发布周期一致，建议用户将此功能与在线升级IPS特征库功能结合使用，以获得最佳效
果。
l 开启/关闭保持时间功能
l 设置保持时间
l 手动清除保持时间
开启/关闭保持时间功能
该功能默认关闭。当功能未开启时，IPS特征库更新后的所有新特征会直接按照预设的防护动作执行防护策
略，无监控观察期。
开启或关闭功能的配置不会立即生效，将在下一次IPS特征库升级后生效。若关闭已启用的功能，对于已处
于观察期内的特征，仍需等待保持时间到期或手动清零后，方可恢复预设防护动作。
在全局配置模式下，使用以下命令，开启/关闭保持时间功能：
l
开启：ips hold-time enable
l
关闭：ips hold-time disable
设置保持时间
保持时间功能启用后，用户可根据实际需求自定义设置保持时间（即监控观察期），系统默认值为168小时
（7天），取值范围为1小时～168小时。
配置完成后，所有后续IPS特征库升级产生的新特征将自动进入监控观察期。在设定的保持时间内，这些新
特征只记录日志，不执行阻断等防护动作；待保持时间到期或手动清零后，自动恢复预设防护动作。
提示: 修改后的保持时间不会立即生效，将在下一次IPS特征库升级后开始应用。

<!-- 来源页 2262 -->
在全局配置模式下，使用以下命令，设置保持时间：
ips hold-time hour value
l
value - 指定保持时间时长，取值范围1小时～168小时。
手动清除保持时间
用户可手动清除特征的保持时间，使指定特征立即恢复预设的防护策略。
在执行模式下，使用以下命令，手动清除保持时间：
exec ips-hold-time clear {all | id signature-id}
l
all - 将当前所有处于观察期内的特征的保持时间清零。
l
id signature-id - 将指定特征的保持时间清零。
配置IPS HTTP多重解码功能
开始之前
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。
为了增强系统的检测和防护能力，系统支持配置IPS HTTP多重解码功能，可以对经过URL或Unicode方式编
码的HTTP协议报文进行多重解码，然后再对解码后的内容进行检测和防护。
URL编码和Unicode编码为HTTP协议常见的2种编码形式，用户可根据实际情况，选择开启对应的解码功
能。
具体配置流程如下：
1. 进入IPS HTTP多重解码配置模式
2. 开启/关闭URL解码功能
3. 开启/关闭Unicode解码功能
4. 配置HTTP多重解码的最大解码次数
进入IPS HTTP多重解码配置模式
进入IPS HTTP多重解码配置模式，在全局配置模式下使用以下命令：
ips http-multi-decode

<!-- 来源页 2263 -->
开启/关闭URL解码功能
启用该功能后，系统可以对经过URL方式编码的HTTP协议报文进行解码。默认情况下，该功能为开启状态。
在IPS HTTP多重解码配置模式下使用以下命令，开启和关闭URL解码功能：
l
开启URL解码功能：url-decode enable
l
关闭URL解码功能：url-decode disable
［命令实例］
hostname(config)# ips http-multi-decode
hostname(config-ips-http-decode)# url-decode disable
开启/关闭Unicode解码功能
启用该功能后，系统可以对经过Unicode方式编码的HTTP协议报文进行解码。默认情况下，该功能为开启
状态。
在IPS HTTP多重解码配置模式下使用以下命令，开启和关闭Unicode解码功能：
l
开启Unicode解码功能：unicode-decode enable
l
关闭Unicode解码功能：unicode-decode disable
［命令实例］
hostname(config)# ips http-multi-decode
hostname(config-ips-http-decode)# unicode-decode disable
配置HTTP多重解码的最大解码次数
同一条携带入侵攻击的HTTP协议报文可能经过多次编码，在开启URL解码或Unicode解码功能后，系统仅
会对一次编码的HTTP协议报文进行解码，二次及以上编码的HTTP协议报文则无法完全进行解码。用户可以
通过配置HTTP多重解码的最大解码次数，解决经过多次编码的HTTP协议报文无法完全进行解码的问题。
在IPS HTTP多重解码配置模式下使用以下命令，配置HTTP多重解码的最大解码次数：
multi-decode-limit number
l
number - 指定系统可解码的最大次数，取值范围为1-5，默认值为1。当HTTP报文经过编码的次数大
于指定的最大解码次数时，仅解码该报文对应编码次数的数据。例如：HTPP报文经过3次编码，最大解
码次数指定为2次，则仅解码该报文前两次编码的数据。
使用no命令，恢复默认值：

<!-- 来源页 2264 -->
no multi-decode-limit
［命令实例］
hostname(config)# ips http-multi-decode
hostname(config-ips-http-decode)# multi-decode-limit 3
配置IPS威胁数据相关功能
开始之前
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。
本章节包括如下内容：
l 开启/关闭抓取完整的威胁数据功能
l 配置IPS威胁日志携带攻击数据报文功能
开启/关闭抓取完整的威胁数据功能
型号说明：A系列带硬盘的设备（不包含A1600/A1800/A2200）、B系列带硬盘的设备、K系
列带硬盘的设备、X系列带硬盘的X8180/X20803/X20812设备、云·界支持抓取完整的威胁数
据。
对于入侵防御引擎检测出的威胁，系统支持抓取完整的威胁数据并通过威胁日志展示威胁发生的全过程。默
认情况下，该功能是开启的。开启后，用户可在WebUI 威胁日志详情页面“威胁数据”处查看威胁的ASCII
码和十六进制数据。若关闭该功能，威胁日志详情页面将不显示“威胁数据” 选项。
在全局配置模式下，使用以下命令，开启抓取完整的威胁数据功能：
ips buffer-capture enable
在全局配置模式下，使用以下命令，关闭抓取完整的威胁数据功能：
ips buffer-capture disable
配置IPS威胁日志携带攻击数据报文功能
开始之前

<!-- 来源页 2265 -->
l
如需将携带攻击数据报文的IPS威胁日志外发到日志服务器，需要先配置日志格式为“Default”或
“S6000”的日志服务器。具体的配置步骤，请参阅《StoneOS 命令行手册》中“监控> 日志> 配置
系统日志功能> 配置Syslog Server”章节。
默认情况下，系统生成的IPS威胁日志不会携带攻击数据报文（payload），这使得用户无法根据IPS威胁日
志进行攻击分析。因此，系统支持配置IPS威胁日志中是否携带攻击数据报文。用户可以根据实际需求开启
该功能，开启后，IPS威胁日志将会携带攻击数据报文进行展示或者外发到日志服务器，用户可根据这些攻
击数据报文进行攻击分析，从而更好地应对网络安全威胁。
配置IPS威胁日志携带攻击数据报文，在全局配置模式下模式下，使用以下命令：
l
开启：threat-syslog-send-payload on
l
关闭：threat-syslog-send-payload off
开启/关闭攻击数据报文的base64编码功能
注意: 关闭该功能可能会导致使用show logging threat查看威胁信息时出现乱码，请谨慎操作！
默认情况下，系统会对IPS威胁日志中携带的攻击数据报文进行base64编码。系统支持关闭攻击数据报文的
base64编码功能，关闭后，攻击数据报文将以明文报文进行展示和外发。
开启/关闭攻击数据报文的base64编码功能，在全局配置模式下，使用以下命令：
l
开启：threat-syslog-send-payload encode base64
l
关闭：no threat-syslog-send-payload encode
查看攻击数据报文相关功能启用状态
系统支持查看攻击数据报文相关功能的启用状态，包括IPS威胁日志携带攻击数据报文功能和攻击数据报文
的base64编码功能。
查看攻击数据报文相关功能的启用状态，在任何模式下，使用以下命令：
show security configurations
以下是一个返回结果示例：
hostname# show security configurations
threat-syslog-send-payload on（IPS威胁日志携带攻击数据报文功能为启用状态）
no threat-syslog-send-payload encode（攻击数据报文的base64编码功能为关闭状态）

<!-- 来源页 2266 -->
更新IPS特征库
开始之前
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。
IPS特征库更新配置
默认情况下，系统会每日自动更新IPS特征库，用户可以根据需要更改IPS特征库更新配置。系统提供两个默
认特征库更新服务器，分别是update1.hillstonenet.com和update2.hillstonenet.com。系统支持在线
更新和本地更新两种方式供用户进行选择。需要注意的是，非根VSYS不支持特征库更新。特征库更新配置，
请参阅下表：
配置
CLI
配置更新模式，默
认为自动
全局配置模式下使用以上命令：
l
指定方式：ips signature update mode {auto | manual}
l
恢复默认：no ips signature update mode
配置更新传输协
议，默认为HTTPS
在全局配置模式下，使用以下命令：
ips update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：
no ips update protocol HTTP
配置更新服务器
全局配置模式下使用以下命令：
l
指定服务器：ips signature update {server1 | server2 | server3} {ipaddress | domain-name} [vrouter vrouter-name] [src-interface srcinterface-name]
注意：服务器支持双栈协议，可配置IPv4地址和IPv6地址。
l
取消服务器的指定：no ips signature update {server1 | server2 |
server3}
指定更新时间
全局配置模式下使用以下命令，启用每日或每周更新，并指定更新的时间：
ips signature update schedule {daily | weekly {mon | tue | wed | thu | fri
| sat | sun} | monthly date} [HH:MM]
全局配置模式下使用以下命令，启用每小时更新，并指定更新的时间：
ips signature update schedule hourly minute

<!-- 来源页 2267 -->
配置
CLI
l
minute – 指定更新的时间，即，在每小时的第多少分钟进行更新。
立即更新
执行模式下使用以下命令：
exec ips signature update
本地更新
执行模式下使用以下命令：
import ips signature from {{ftp | ftps | sftp} server ip-address [user
user-namepassword password | vrouter vr-name] | tftp server ipaddress [vrouter vr-name]} file-name
显示特征库统计信
息
show ips signature info
显示特征库配置信
息
show ips signature update
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保特征库能够正常升级，需要在设备上指定代理服务器
的IP地址和端口号。
为入侵防御特征库升级指定代理服务器，在全局配置模式下，使用如下命令：
ips signature update proxy-server {main | backup} ip-address port-number
l
main | backup – 使用main参数指定主代理服务器，使用backup指定备份代理服务器。
l
ip-address port-number – 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no ips signature update proxy-server {main | backup}命令。
升级入侵防御全量特征库
由于设备之间的内存大小存在差异，部分设备默认加载的入侵防御特征库数量不完整。为了满足用户的安全
防护需求，用户可以手动将设备当前的入侵防御特征库升级为全量的入侵防御特征库，从而提升系统的安全
防护能力。
开始之前：
l
安装入侵防御许可证。关于安装许可证的详细信息，请参阅“系统管理> 许可证> 许可证管理”章节。
注意事项：

<!-- 来源页 2268 -->
l
系统默认不开启升级入侵防御全量特征库功能。
l
升级为入侵防御全量特征库可能会导致设备的吞吐性能最大下降20%，建议根据设备的实际负载情况进
行配置。
l
升级为入侵防御全量特征库后，如果关闭该功能，则会减少IPS特征库的数量，可能会影响已产生的威胁
事件的详细信息。
配置步骤：
升级IPS全量特征库，在全局配置模式下，使用以下命令：
ips signature update entire
在全局配置模式下，使用以上命令no的形式取消升级IPS全量特征库：
no ips signature update entire
配置IPS入侵防御白名单
开始之前
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。
系统实时对网路中的流量进行检测，当遇到威胁时，设备会产生告警或者阻断威胁。随着网络环境的复杂，
威胁的增多使设备产生的告警也会越来越多，过多的威胁告警使得用户无从下手，而且很多都存在误报的问
题。系统通过提供入侵防御白名单功能，对匹配到白名单的威胁不再上报告警或阻断，从而降低威胁的误报
率。入侵防御白名单由源地址、目的地址、特征ID和VRouter组成，用户至少选择一项进行配置，当配置多
条匹配条件时，只有所有都匹配成功的威胁，系统才会放行，并且不再上报告警或阻断流量。
创建IPS白名单
创建IPS白名单并进入IPS白名单配置模式。如果IPS白名单名称已存在，则直接进入IPS白名单配置模式。
在全局配置模式下，使用以下命令，创建IPS白名单并进入IPS白名单配置模式：
ips allowlist list-name
l
list-name - 指定白名单的名称，取值范围为1-255字符。
在全局配置模式下，使用以下命令，删除指定的IPS白名单。
no ips allowlist list-name
［命令实例］

<!-- 来源页 2269 -->
hostname(config)# ips allowlist allow1
hostname(config-ips-allowlist)#
指定源地址
指定IPS白名单的源IP地址。指定后，系统将对流经设备的所有流量的源IP地址进行匹配过滤。
在IPS白名单配置模式下，使用以下命令，指定IPS白名单的源IP地址：
src-ip {A.B.C.D | A.B.C.D/M | A:B:C:D::F/<0-128> }
l
A.B.C.D | A.B.C.D/M | A:B:C:D::F/<0-128> - 指定IPS白名单需匹配的源IP地址，可以为IPv4地址或
IPv6地址。
在IPS白名单配置模式下，使用以下命令，删除源IP地址的配置：
no src-ip
［命令实例］
hostname(config)# ips allowlist allow1
hostname(config-ips-allowlist)# src-ip 10.1.1.1
指定目的地址
指定IPS白名单的目的IP地址。指定后，系统将对流经设备的所有流量的目的IP地址进行匹配过滤。
在IPS白名单配置模式下，使用以下命令，指定IPS白名单的目的IP地址：
dst-ip {A.B.C.D | A.B.C.D/M | A:B:C:D::F/<0-128> }
l
A.B.C.D | A.B.C.D/M | A:B:C:D::F/<0-128> - 指定IPS白名单需匹配的目的IP地址，可以为IPv4地址
或IPv6地址。
在IPS白名单配置模式下，使用以下命令，删除目的IP地址的配置：
no dst-ip
［命令实例］
hostname(config)# ips allowlist allow1
hostname(config-ips-allowlist)# dst-ip 10.1.1.2
指定特征ID
指定IPS白名单的特征ID。一个白名单最多允许配置一个特征ID，不配置时表示特征ID可以任意，只根据源
地址或目的地址来进行过滤，当源地址和目的地址匹配成功，就对报文进行放行；若配置了特征ID，则须同

<!-- 来源页 2270 -->
时源地址、目的地址和特征ID都匹配成功，才能对报文进行放行。
在IPS白名单配置模式下，使用以下命令，指定IPS白名单的特征ID：
signature-id id
l
id - 指定IPS白名单需匹配的特征ID。
在IPS白名单配置模式下，使用以下命令，删除IPS白名单指定的特征ID：
no signature-id
［命令实例］
hostname(config)# ips allowlist allow1
hostname(config-ips-allowlist)# signature-id 105002
指定虚拟路由器
指定IPS白名单的VRouter。在IPS白名单配置模式下，使用以下命令，指定虚拟路由器：
vr vr-name
l
vr-name - 指定IPS白名单需匹配的VRouter的名称。
在IPS白名单配置模式下，使用以下命令，删除VRouter的配置：
no vr
［命令实例］
hostname(config)# ips allowlist allow1
hostname(config-ips-allowlist)# src-ip 10.1.1.1
hostname(config-ips-allowlist)# vr trust-vr
查看IPS相关配置信息
开始之前
l 阅读"入侵防御" 在第2178页介绍。
l 阅读"IPS入侵防御配置准备工作" 在第2179页。
l 阅读"IPS入侵防御配置流程和指导" 在第2179页。
本章节包括如下内容：

<!-- 来源页 2271 -->
l 查看IPS配置信息
l 查看IPS模板配置信息
l 查看IPS协议配置信息
l 查看CC防护认证相关信息
l 查看CC防护源IP的最大速率排名和总数排名
l 查看CC防护的总体信息、防护信息以及请求的URL排名
l 查看IPS的启用状态
l 查看安全域引用的IPS模板信息
查看IPS配置信息
在任何模式下使用以下命令，查看IPS功能的全部配置信息：
show ips configuration
注意: 非根VSYS不支持该功能。
［命令实例］
hostname# show ips configuration
IPS log aggregation by-src-dst agg_time 10
IPS log http proxy IP Enable
IPS working mode IPS
IPS hold-time : 24 hour
IPS stream-buffer-size : 4
IPS stream-expanded-buffer-size : 16
IPS max-http-transaction : 32
IPS buffer-capture Enable
IPS http multi decode:
Multi decode limit: 1
URL decode: Enable
Unicode decode: Enable

<!-- 来源页 2272 -->
查看IPS模板配置信息
在任何模式下使用以下命令，查看IPS模板（IPS Profile）配置的全部信息：
显示IPS Profile配置的全部信息：show ips profile [profile-name] [signature-class signatureclass-id]
l
profile-name - 指定需要显示的IPS Profile的名称。
l
signature-class-id - 指定需要显示的过滤规则或搜索规则的ID。
［命令实例］
hostname# show ips profile predef_default
IPS profile "predef_default" (ID 1)
Description Configured with attack detection of medium and high confidence levels,
this profile can be used to detect threats and perform the default rule action. The
profile is applicable to
the scenario of general deployment.
Pcap disable
suspicious user-agent detection is disable
suspicious user-agent action log-only
Password-Protect
password protect http username:
username;user;usrname;j_username;login
password protect http userpassword:
password;passwd;pass;pwd;j_password
password protect http success code:
200;302;201
password protect http custom success to login:
loginsuccess;login-success;OK=1;"successful":"true"
password protect http fail code:
200;302;201;303
password protect http custom fail to login:

<!-- 来源页 2273 -->
loginerror;login-error;loginerr;OK=0;"successful":"fail";"result"
http-plain-text-check is disable
IPS check-weakpassword is disable
check-weakpassword min length is 6
check-weakpassword min character type is 2
check-weakpassword equ-username-check is enable
check-weakpassword serial-char-check is enable
check-weakpassword ftp-anonymous-login-check is disable
check-weakpassword custom weak password ：
Sig-set count 22
default_dns default_ftp
default_http default_pop3
default_smtp default_telnet
default_other-tcp default_other-udp
default_imap default_finger
default_sunrpc default_nntp
default_tftp default_snmp
default_mysql default_mssql
default_oracle default_msrpc
default_netbios default_dhcp
default_ldap default_voip
IPS check reverse shell is disable
check reverse shell level is low
check reverse shell action is log-only
filter-class 1, action default, pcap disable
severity: Low; Medium; High; Critical;
confidence: Medium; High;

<!-- 来源页 2274 -->
查看IPS协议配置信息
在任何模式下使用以下命令，查看IPS协议配置的全部信息：
show ips sigset [sigset-name]
l
sigset-name - 指定需要显示的协议配置名称。
［命令实例］
hostname(config)# show ips sigset
Total count: 53
============================================================
IPS signature set dhcp
Default actions:
Attack-level Action Block Seconds
INFO log noblock 0
WARNING log noblock 0
CRITICAL log noblock 0
Max scan bytes per direction: 0(Unlimited)
Used by 1 IPS profiles:
test
-----------------------------------------------------------
查看CC防护认证相关信息
在任何模式下使用以下命令，查看CC防护认证相关信息：
show ips sigset sigset-name web-server server-name http-request-flood auth-ck
l
sigset-name - 指定需要显示的协议配置名称。
l
server-name - 指定需要显示的Web服务器的名称。
查看CC防护源IP的最大速率排名和总数排名
在任何模式下使用以下命令，查看CC防护源IP的最大速率排名和总数排名：
show ips sigset sigset-name web-server server-name http-request-flood ip-top {max-rate |
total}

<!-- 来源页 2275 -->
l
sigset-name - 指定需要显示的协议配置名称。
l
server-name - 指定需要显示的Web服务器的名称。
l
{max-rate | total} - 指定显示源IP的最大速率排名（max-rate）或者总数排名（total）。
查看CC防护的总体信息、防护信息以及请求的URL排名
在任何模式下使用以下命令，查看CC防护的总体信息、防护信息以及请求的URL排名：
show ips sigset sigset-name web-server server-name http-request-flood req-stat {overview
{by-day | by-hour | by-minute | by-second} | protect {by-day | by-hour | by-minute | bysecond} | top}
l
sigset-name - 指定需要显示的协议配置名称。
l
server-name - 指定需要显示的Web服务器的名称。
l
{overview {by-day | by-hour | by-minute | by-second} - 指定显示报文的总体信息，包括请求
数、不同请求方法（GET、POST）对应的请求数、应答数、不同状态码（4XX、5XX）对应的应答数。
可以按照天、小时、分钟和秒进行显示。
l
protect {by-day | by-hour | by-minute | by-second} - 指定显示报文的防护信息，包括请求数、
应答数、代理请求数限制丢弃数、非代理请求数限制丢弃数、认证应答数、认证丢弃数。可以按照天、
小时、分钟和秒进行显示。
l
top - 指定显示请求的URL排名。
注意: 执行http-request-flood statistics enable命令后，show ips sigset sigset-name
web-server server-name http-request-flood req-stat top 命令才会生效。
查看IPS的启用状态
在任何模式下使用以下命令，查看IPS功能的启用状态：
show ips status
查看安全域引用的IPS模板信息
在任何模式下使用以下命令，查看安全域中引用的IPS模板（IPS Profile）信息：
show ips zone-binding

<!-- 来源页 2276 -->
热点威胁情报
系统通过与山石云瞻平台对接，可定期从云端获取最近一周内互联网上最严峻的热点威胁情报信息，涵盖
IPS漏洞、AV病毒以及云沙箱检测到的威胁情报。依托云端与本地联动的云网协同能力，系统可有效解决热
点威胁防护响应滞后的问题，提升专项风险防护能力，助力用户精准掌握安全态势、快速调整防护策略，从
而高效应对各类网络风险。
用户可以在系统WebUI的iCenter页面中的<热点威胁情报>标签页，查看山石云瞻平台推送的热点威胁情报
详情；也可以根据热点威胁情报的防护状态，对相应的情报内容进行处置，从而对热点威胁进行防范。
热点威胁情报功能配置流程：
1. 配置热点威胁情报推送服务器
2. 开启热点威胁情报推送功能
3. 查看热点威胁情报（仅在WebUI上支持）
4. 热点威胁情报处置（仅在WebUI上支持）
注意:
l
非根VSYS下暂不支持通过CLI配置热点威胁情报。
l
获取热点威胁情报前，请先确保已安装并激活威胁情报许可证。否则，用户将无法进行威胁防
护处置。
l
山石云瞻平台威胁情报库每周更新一次。
配置热点威胁情报推送服务器
用户可在防火墙上将热点威胁情报推送服务器配置为山石云瞻平台，从而构建云网协同的威胁情报治理模
式，实现热点威胁情报的云端与网络侧联动。
系统提供默认的热点威胁情报推送服务器，即山石云瞻平台（ti.hillstonenet.com.cn）。同时用户也可以
根据需要配置其他的服务器来推送热点威胁情报。配置热点威胁情报推送服务器，在全局配置模式下，使用
以下命令：
threat-intelligence cloud-server {ip-address | domain-name} protocol {HTTP | HTTPS}
[vrouter vr-name] [src-interface interface-name]
l
cloud-server {ip-address | domain-name} – 指定热点威胁情报推送服务器的IP地址或域名，默认
为山石云瞻平台（ti.hillstonenet.com.cn）。取值范围为1-255个字符。

<!-- 来源页 2277 -->
l
protocol {HTTP | HTTPS} – 指定连接热点威胁情报推送服务器的请求协议类型，需要选择HTTPS或
HTTP协议，默认为HTTPS。
l
vrouter vr-name – 指定连接热点威胁情报推送服务器的VRouter，默认为trust-vr。
l
src-interface interface-name – 指定连接热点威胁情报推送服务器的源接口。
在全局配置模式下，使用no命令，恢复热点威胁情报推送服务器的默认配置：
no threat-intelligence cloud-server
开启/关闭热点威胁情报推送
热点威胁情报推送服务器配置完成后，用户需要开启热点威胁情报推送功能，确保系统能够接收服务器推送
的热点威胁情报。
该功能启用后，热点威胁情报推送服务器便会向系统推送最新的热点情报；系统接收后将自动更新威胁情报
列表。若不启用，热点威胁情报推送服务器将不再推送最新的热点情报。默认情况下，该功能为关闭状态。
开启/关闭热点威胁情报推送，在全局配置模式下，使用以下命令：
l
开启：threat-intelligence push enable
l
关闭：threat-intelligence push disable
配置每日更新时间
系统默认在每日00:00-04:00之间随机选择一个时间点自动触发热点威胁情报更新。同时用户也可以根据需
要配置每日更新热点威胁情报的时间点（取值范围为00:00-23:59）。配置完成后，系统将在每日设定的时
间，主动向热点威胁情报推送服务器请求获取威胁情报。若服务器存在新情报，系统将自动更新热点威胁情
报列表；若无新情报，则不做任何变更。
配置每日更新时间，在全局配置模式下，使用以下命令：
threat-intelligence update_time hour time-value minute time-value
l
hour time-value - 指定每日更新的小时数，取值范围为0-23。例如：2表示凌晨2点。
l
minute time-value - 指定每日更新的分钟数，取值范围为0-59。例如：30表示某小时的30分。
手动更新热点威胁情报
系统支持手动触发热点威胁情报更新，执行后，系统立即同步热点威胁情报推送服务器上的热点威胁情报，
并将最新的信息下载并更新到本地的热点威胁情报列表中。手动更新热点威胁情报，在任意模式下，使用以
下命令：

<!-- 来源页 2278 -->
exec threat-intelligence update
查看热点威胁情报推送服务器
查看热点威胁情报推送服务器的配置详情，在任意模式下，使用以下命令：
show threat-intelligence cloud-server
以下是一个返回结果示例：
hostname# show threat-intelligence cloud-server
The base information of threat-intelligence cloud server:
===============================================================
Server: ti.hillstonenet.com.cn
Port: 443
Protocol: HTTPS
Vrouter: trust-vr
Src interface: MGT0
--------------------------------------------------------------
Threat-intelligence daily update time: 2:44
===============================================================
查看热点威胁情报推送功能的启用状态
查看热点威胁情报推送功能的启用状态，在任意模式下，使用以下命令：
show threat-intelligence push
以下是一个返回结果示例：
hostname# show threat-intelligence push
The threat-intelligence push function: DISABLE

<!-- 来源页 2279 -->
IP地理库
IP地理库介绍
系统可以通过WebUI页面展示外部威胁地图，用户可以根据所选择的威胁或风险主机，查看该威胁的攻击主
机或该风险主机来源区域。使用该功能前，需要先更新IP地理库。
IP地理库更新配置
默认情况下，系统会每日自动更新IP地理库，用户可以根据需要更改IP地理库更新配置。IP地理库更新配置
包括：
l 配置IP地理库更新模式
l 配置更新传输协议
l 配置更新服务器
l 指定HTTP代理服务器
l 指定更新时间
l 立即更新
l 导入IP地理库文件
l 显示IP地理库信息
l 显示IP地理库更新配置信息
配置IP地理库更新模式
系统支持手动和自动两种更新方式。配置IP地理库更新方式，在全局配置模式下，使用以下命令：
geolocation-IP-signature update mode {auto | manual}
l
auto – 指定自动更新IP地理库。该方式为系统的默认更新方式。
l
manual – 指定手动更新IP地理库。
在全局配置模式下使用该命令no的形式恢复默认更新模式：
no geolocation-IP-signature update mode

<!-- 来源页 2280 -->
配置更新传输协议
系统支持通过HTTP和HTTPS对特征库进行更新，默认为HTTPS。配置特征库更新的传输协议为HTTP，在全
局配置模式下，使用以下命令：
geolocation-IP-signature update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：
no geolocation-IP-signature update protocol HTTP
配置更新服务器
系统提供默认的IP地理库更新服务器，即update1.hillstonenet.com和update2.hillstonenet.com，同
时用户也可以根据需要配置其它更新服务器下载最新IP地理信息。最多可配置3个。配置更新服务器，在全
局配置模式下，使用以下命令：
geolocation-IP-signature update {server1 | server2 | server3} {ip-address | domain-name}
[vrouter vrouter-name] [src-interface src-interface-name]
l
server1 | server2 | server3 – 指定将要配置的服务器，服务器支持双栈协议，可配置IPv4地址和IPv6
地址。server1的默认值为update1.hillstonenet.com，server2的默认值为
update2.hillstonenet.com。
l
ip-address | domain-name – 指定更新服务器的名称，可以是IP地址形式（ip-address）也可以是
域名形式（domain-name，例如update1.hillstonenet.com）。
l
vrouter vrouter-name - 指定更新服务器所属的VRouter。若不指定则默认是trust-vr。
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，IP地理库更新时将通过该源接口对更新服务器发起访问。若不指定，则默认使用管理口作为源接
口。
在全局配置模式下，使用该命令no的形式取消更新服务器的指定：
no geolocation-IP-signature update {server1 | server2 | server3}
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保特征库能够正常升级，需要在设备上指定代理服务器
的IP地址和端口号。
为IP地理库升级指定代理服务器，在全局配置模式下，使用如下命令：
geolocation-ip-signature update proxy-server {main | backup} ip-address port-number

<!-- 来源页 2281 -->
l
proxy-server {main | backup} – 使用main参数指定主代理服务器，使用backup指定备份代理服务
器。
l
ip-address port-number – 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no geolocation-ip-signature update proxy-server {main | backup}
命令。
指定更新时间
默认情况下，系统采用自动模式每日更新IP地理库，并且为避免服务器流量过大，每日更新时间是随机的。
用户可以根据需要指定IP地理库更新的频率和时间，在全局配置模式下，使用以下命令：
geolocation-IP-signature update schedule {daily | weekly {mon | tue | wed | thu | fri | sat |
sun} | monthly date} [HH:MM]
l
daily – 指定频率为每天更新。
l
weekly {mon | tue | wed | thu | fri | sat | sun} – 指定频率为每周更新。mon | tue | wed | thu | fri
| sat | sun用来指定每周更新的日期。
l
monthly date - 指定频率为每月更新。date用来指定每月更新的日期，取值范围为1到31。如果某月
不包含所指定的日期（比如2月没有30号），则该月不会自动升级。
l
HH:MM – 指定更新的时间，例如09：00。
立即更新
无论更新模式为手动还是自动，用户都可以随时使用以下命令更新IP地理库。立即更新IP地理库，在任何模
式下，使用以下命令：
exec geolocation-IP-signature update [full]
l
exec geolocation-IP-signature update – 仅对当前IP地理库与更新服务器最新发布IP地理库的不同
部分进行更新。
l
full – 强制升级当前IP地理库。
导入IP地理库文件
在某些情况下，用户设备可能无法连接到更新服务器对IP地理库进行更新，针对这一问题，系统提供IP地理
库文件导入功能，即通过FTP、TFTP服务器或者U盘将IP地理库文件导入到设备，从而更新设备的IP地理
库。导入IP地理库文件，在执行模式下，使用以下命令：

<!-- 来源页 2282 -->
import geolocation-IP-signature from {ftp server ip-address [user user-name password
password] | tftp server ip-address } [vrouter vr-name] file-name
l
ip-address – 指定FTP或者TFTP服务器的IP地址。
l
user user-name password password – 指定FTP服务器的用户名和密码。
l
vrouter vr-name – 指定FTP或者TFTP服务器所属的VRouter。
l
file-name – 指定导入的IP地理库文件的名称。
显示IP地理库信息
用户可以随时使用相应的show命令查看设备的IP地理库信息，包括IP地理库版本、发布日期等。查看IP地
理库信息，在任何模式下使用以下命令：
show geolocation-IP-signature info
显示IP地理库更新配置信息
用户可以随时使用相应的show命令查看设备上的IP地理库更新信息，包括更新服务器信息、更新模式、更
新频率及时间以及IP地理库更新状况等。查看IP地理库更新配置信息，在任何模式下使用以下命令：
show geolocation-IP-signature update

<!-- 来源页 2283 -->
威胁防护特征库
威胁防护特征库包括病毒过滤特征库、病毒过滤智能文件引擎库、入侵防御特征库、沙箱白名单、IP信誉特
征库、僵尸网络防御地址库、加密流量检测库、MITRE ATT&CK 知识库。默认情况下，设备会每日自动更新
威胁防护特征库，目前支持在线更新和本地更新两种方式。Hillstone提供两个默认特征库更新服务器，分
别是https://update1.hillstonenet.com和https://update2.hillstonenet.com。用户可以根据需要
更改特征库更新配置。需要注意的是，非根VSYS不支持特征库更新。
特征根据严重程度分为三个级别（安全级别），分别为严重（Critical）、警告（Warning）和信息
（Informational），各级别说明如下。用户可根据特征严重程度，设置系统对该特征攻击所将采取的行
为。
l 严重（Critical）：严重的攻击事件，例如缓冲区溢出。
l 警告（Warning）：具有一定攻击性的事件，例如超长的URL。
l 信息（Informational）：一般事件，例如登录失败。
通过CLI的方式更新特征库：
l 病毒特征库更新配置
l 病毒过滤智能文件引擎库更新配置
l 入侵防御特征库更新配置
l 沙箱白名单更新配置
l IP信誉特征库更新配置
l 僵尸网络防御地址库更新配置
l 加密流量检测库更新配置

<!-- 来源页 2284 -->
威胁分类库
威胁分类库介绍
威胁分类库用于存储不同级别的威胁分类数据，以确保系统可以准确地识别和分类各种威胁。
威胁分类库更新配置
默认情况下，系统会每日自动更新威胁分类库，用户可以根据需要更改威胁分类库更新配置。
提示: 目前仅支持通过CLI的方式更新威胁分类库。
威胁分类库更新配置包括：
l 配置威胁分类库更新模式
l 配置更新传输协议
l 配置更新服务器
l 指定HTTP代理服务器
l 指定更新时间
l 立即更新
l 导入威胁分类库文件
l 查看威胁分类库信息
l 查看威胁分类库更新配置信息
配置威胁分类库更新模式
系统支持手动和自动两种更新方式。配置威胁分类库更新方式，在全局配置模式下，使用以下命令：
threat-type update mode {auto | manual}
l
auto – 指定自动更新威胁分类库。该方式为系统的默认更新方式。
l
manual – 指定手动更新威胁分类库。
在全局配置模式下使用该命令no的形式恢复默认更新模式：
no threat-type update mode

<!-- 来源页 2285 -->
配置更新传输协议
系统支持通过HTTP和HTTPS对特征库进行更新，默认为HTTPS。配置特征库更新的传输协议为HTTP，在全
局配置模式下，使用以下命令：
threat-type update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：
no threat-type update protocol HTTP
配置更新服务器
系统提供默认的威胁分类库更新服务器，即update1.hillstonenet.com和update2.hillstonenet.com，
同时用户也可以根据需要配置其它更新服务器下载最新威胁分类信息。最多可配置3个。配置更新服务器，
在全局配置模式下，使用以下命令：
threat-type update {server1 | server2 | server3} {ip-address | domain-name} [vrouter
vrouter-name] [src-interface src-interface-name]
l
server1 | server2 | server3 – 指定将要配置的服务器，服务器支持双栈协议，可配置IPv4地址和IPv6
地址。server1的默认值为update1.hillstonenet.com，server2的默认值为
update2.hillstonenet.com。
l
ip-address | domain-name – 指定更新服务器的名称，可以是IP地址形式（ip-address）也可以是
域名形式（domain-name，例如update1.hillstonenet.com）。
l
vrouter vrouter-name - 指定更新服务器所属的VRouter。若不指定则默认是trust-vr。
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，威胁分类库更新时将通过该源接口对更新服务器发起访问。若不指定，则默认使用管理口作为源接
口。
在全局配置模式下，使用该命令no的形式取消更新服务器的指定：
no threat-type update {server1 | server2 | server3}
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保特征库能够正常升级，需要在设备上指定代理服务器
的IP地址和端口号。
为威胁分类库升级指定代理服务器，在全局配置模式下，使用如下命令：
threat-type update proxy-server {main | backup} ip-address port-number

<!-- 来源页 2286 -->
l
proxy-server {main | backup} – 使用main参数指定主代理服务器，使用backup指定备份代理服务
器。
l
ip-address port-number – 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no threat-type update proxy-server {main | backup}命令。
指定更新时间
默认情况下，系统采用自动模式每日更新威胁分类库，并且为避免服务器流量过大，每日更新时间是随机
的。用户可以根据需要指定威胁分类库更新的频率和时间，在全局配置模式下，使用以下命令：
threat-type update schedule {daily | weekly {mon | tue | wed | thu | fri | sat | sun} | monthly
date} [HH:MM]
l
daily – 指定频率为每天更新。
l
weekly {mon | tue | wed | thu | fri | sat | sun} – 指定频率为每周更新。mon | tue | wed | thu | fri
| sat | sun用来指定每周更新的日期。
l
monthly date - 指定频率为每月更新。date用来指定每月更新的日期，取值范围为1到31。如果某月
不包含所指定的日期（比如2月没有30号），则该月不会自动升级。
l
HH:MM – 指定更新的时间，例如09：00。
立即更新
无论更新模式为手动还是自动，用户都可以随时使用以下命令更新威胁分类库。立即更新威胁分类库，在任
何模式下，使用以下命令：
exec threat-type update
注意: 对当前威胁分类库与更新服务器最新发布威胁分类库的不同部分进行更新。
导入威胁分类库文件
在某些情况下，用户设备可能无法连接到更新服务器对威胁分类库进行更新，针对这一问题，系统提供威胁
分类库文件导入功能，即通过FTP/FTPS/SFTP/TFTP服务器将威胁分类库文件导入到设备，从而更新设备的
威胁分类库。导入威胁分类库文件，在执行模式下，使用以下命令：
import threat-type signature from {ftp server [ ip-address user user-name password
password ]| ftps server [ ip-address user user-name password password ]|sftp server [ ipaddress user user-name password password ]|tftp serverip-address} [vroutervr-name] filename

<!-- 来源页 2287 -->
l
ip-address – 指定FTP、FTPS、SFTP或者TFTP服务器的IP地址。
l
user user-name password password – 指定FTP、FTPS或者SFTP服务器的用户名和密码。
l
vrouter vr-name – 指定FTP、FTPS、SFTP或者TFTP服务器所属的VRouter。
l
file-name – 指定导入的威胁分类库文件的名称。
查看威胁分类库信息
用户可以随时使用相应的show命令查看设备的威胁分类库信息，包括威胁分类库版本、发布日期等。查看
威胁分类库信息，在任何模式下使用以下命令：
show threat-type info
以下是一个返回结果示例：
hostname# show threat-type info
Signature vendor: Hillstone Networks（显示威胁分类库所属公司。）
Current version: 1.0.241224（显示威胁分类库的当前版本。）
Release date: 2024/12/24 13:44:52（显示威胁分类库的发布日期。）
查看威胁分类库更新配置信息
用户可以随时使用相应的show命令查看设备上的威胁分类库更新信息，包括更新服务器信息、更新模式、
更新频率及时间以及威胁分类库更新状况等。查看威胁分类库更新配置信息，在任何模式下使用以下命令：
show threat-type update
以下是一个返回结果示例：
hostname# show threat-type update
THREAT_TYPE knowledge base signature update options:
protocol: HTTPS （显示威胁分类库更新的传输协议为HTTPS。）
server1: update1.hillstonenet.com, 443, trust-vr （显示威胁分类库更新服务器server1。）
server2: update2.hillstonenet.com, 443, trust-vr （显示威胁分类库更新服务器server2。）
server3: （显示威胁分类库更新服务器server3。）
proxy server status: disable （显示代理服务器的启用状态为未启用。）
main proxy server: （显示主代理服务器。）
backup proxy server: （显示备份代理服务器。）

<!-- 来源页 2288 -->
mode: auto （显示威胁分类库的更新模式为自动更新模式。）
schedule: daily 18:18 （显示威胁分类库的更新频率。）
current status: normal （显示威胁分类库的更新状态。）
last update result: success （上一次更新威胁分类库的结果。）
last update time: Tue Dec 24 18:18:27 2024（上一次更新威胁分类库的时间。）

<!-- 来源页 2289 -->
MITRE ATT&CK®知识库
MITRE ATT&CK®（Adversarial Tactics, Techniques, and Common Knowledge ）是一个攻击行为
知识库，将已知的攻击行为归纳为战术和技术，形成实用性强、清晰明了的体系框架。系统支持将检测到的
可疑行为与MITRE ATT&CK®模型进行映射，通过WebUI页面展示MITRE ATT&CK®战术和技术详情，帮助用
户更好地识别可疑行为。为确保检测时使用最新的MITRE ATT&CK®知识库，建议将MITRE ATT&CK®知识库
升级至最新版本。
MITRE ATT&CK®知识库更新配置
默认情况下，系统会每日自动更新MITRE ATT&CK®知识库，用户可以根据需要更改MITRE ATT&CK®知识库
更新配置。MITRE ATT&CK®知识库更新配置包括：
l 配置MITRE ATT&CK®知识库更新模式
l 配置更新传输协议
l 配置更新服务器
l 指定HTTP代理服务器
l 指定更新时间
l 立即更新
l 导入MITRE ATT&CK®知识库文件
l 显示MITRE ATT&CK®知识库信息
l 显示MITRE ATT&CK®知识库更新配置信息
配置MITRE ATT&CK®知识库更新模式
系统支持手动和自动两种更新方式。配置MITRE ATT&CK®知识库更新方式，在全局配置模式下，使用以下命
令：
ATT&CK update mode {auto | manual}
l
auto – 指定自动更新MITRE ATT&CK®知识库。该方式为系统的默认更新方式。
l
manual – 指定手动更新MITRE ATT&CK®知识库。
在全局配置模式下使用该命令no的形式恢复默认更新模式：
no ATT&CK update mode

<!-- 来源页 2290 -->
配置更新传输协议
系统支持通过HTTP和HTTPS对特征库进行更新，默认为HTTPS。配置特征库更新的传输协议为HTTP，在全
局配置模式下，使用以下命令：
ATT&CK update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：
no ATT&CK update protocol HTTP
配置更新服务器
系统提供默认的MITRE ATT&CK®知识库更新服务器，即update1.hillstonenet.com和
update2.hillstonenet.com，同时用户也可以根据需要配置其它更新服务器下载最新的MITRE ATT&CK®
知识库。最多可配置3个。配置更新服务器，在全局配置模式下，使用以下命令：
ATT&CK update {server1 | server2 | server3} {ip-address | domain-name} [vroutervroutername] [src-interface src-interface-name]
l
server1 | server2 | server3 – 指定将要配置的服务器，服务器支持双栈协议，可配置IPv4地址和IPv6
地址。server1的默认值为update1.hillstonenet.com，server2的默认值为
update2.hillstonenet.com。
l
ip-address | domain-name – 指定更新服务器的名称，可以是IP地址形式（ip-address）也可以是
域名形式（domain-name，例如update1.hillstonenet.com）。
l
vrouter vrouter-name– 指定更新服务器绑定的虚拟路由器。若不指定则默认是trust-vr。
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，MITRE ATT&CK®知识库更新时将通过该源接口对更新服务器发起访问。若不指定，则默认使用管理
口作为源接口。
在全局配置模式下，使用该命令no的形式取消更新服务器的指定：
no ATT&CK update {server1 | server2 | server3}
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保特征库能够正常升级，需要在设备上指定代理服务器
的IP地址和端口号。
为MITRE ATT&CK®知识库升级指定代理服务器，在全局配置模式下，使用如下命令：
ATT&CK update proxy-server {main | backup} ip-address port-number

<!-- 来源页 2291 -->
l
proxy-server {main | backup} – 使用main参数指定主代理服务器，使用backup指定备份代理服务
器。
l
ip-address port-number – 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no att&CK update proxy-server {main | backup}命令。
指定更新时间
默认情况下，系统采用自动模式每日更新MITRE ATT&CK®知识库，并且为避免服务器流量过大，每日更新时
间是随机的。用户可以根据需要指定MITRE ATT&CK®知识库更新的频率和时间，在全局配置模式下，使用以
下命令：
ATT&CK update schedule {daily | weekly {mon | tue | wed | thu | fri | sat | sun} | monthly date}
[HH:MM]
l
daily – 指定频率为每天更新。
l
weekly {mon | tue | wed | thu | fri | sat | sun} – 指定频率为每周更新。mon | tue | wed | thu | fri
| sat | sun用来指定每周更新的日期。
l
monthly date - 指定频率为每月更新。date用来指定每月更新的日期，取值范围为1到31。如果某月
不包含所指定的日期（比如2月没有30号），则该月不会自动升级。
l
HH:MM – 指定更新的时间，例如09：00。
立即更新
无论更新模式为手动还是自动，用户都可以随时使用以下命令更新MITRE ATT&CK®知识库。立即更新MITRE
ATT&CK®知识库，在任何模式下，使用以下命令：
exec ATT&CK update [full]
l
exec ATT&CK update – 仅对当前MITRE ATT&CK®知识库与更新服务器最新发布MITRE ATT&CK®知识
库的不同部分进行更新。
l
full – 强制升级当前MITRE ATT&CK®知识库。
导入MITRE ATT&CK®知识库文件
在某些情况下，用户设备可能无法连接到更新服务器对MITRE ATT&CK®知识库进行更新，针对这一问题，系
统提供MITRE ATT&CK®知识库文件导入功能，即通过FTP、TFTP服务器或者U盘将MITRE ATT&CK®知识库
文件导入到设备，从而更新设备的MITRE ATT&CK®知识库。导入MITRE ATT&CK®知识库文件，在执行模式
下，使用以下命令：

<!-- 来源页 2292 -->
import attck signature from {{ftp | ftps | sftp} server ip-address [vrouter vrouter-name] [user
user-name password password] | tftp server ip-address [vrouter vrouter-name]} file-name
l
ftp | ftps | sftp - 指定服务器的类型。
l
ip-address – 指定FTP、FTPS、SFTP或者TFTP服务器的IP地址。
l
vrouter vrouter-name – 指定FTP、FTPS、SFTP或者TFTP服务器所属的VRouter。
l
user user-name password password – 指定FTP/FTPS/SFTP服务器的用户名和密码。
l
file-name – 指定导入的MITRE ATT&CK®知识库文件的名称。
显示MITRE ATT&CK®知识库信息
用户可以使用相应的show命令查看设备的MITRE ATT&CK®知识库信息，包括MITRE ATT&CK®知识库版
本、发布日期等。查看MITRE ATT&CK®知识库信息，在任何模式下使用以下命令：
show ATT&CK info
例如：
hostname# show ATT&CK info
Signature vendor: Hillstone Networks（显示MITRE ATT&CK®知识库所属公司。）
Current version: 3.0.2（显示MITRE ATT&CK®知识库的当前版本。）
Release date: 2022/11/08 14:36:16（显示MITRE ATT&CK®知识库的发布日期。）
显示MITRE ATT&CK®知识库更新配置信息
用户可以使用相应的show命令查看设备上的MITRE ATT&CK®知识库更新信息，包括更新服务器信息、更新
模式、更新频率及时间以及MITRE ATT&CK®知识库更新状况等。查看MITRE ATT&CK®知识库更新配置信
息，在任何模式下使用以下命令：
show ATT&CK update
例如：
hostname# show ATT&CK update
ATT&CK knowledge base signature update options:
protocol: HTTPS（显示MITRE ATT&CK®知识库更新的传输协议为HTTPS。）
server1:
server2: update2.hillstonenet.com, 443, trust-vr（显示MITRE ATT&CK®知识库更新服务器信
息。）

<!-- 来源页 2293 -->
server3:
proxy server status: disable（显示未指定代理服务器。）
main proxy server:
backup proxy server:
mode: auto（显示MITRE ATT&CK®知识库更新模式为自动更新模式。）
schedule: daily 22:34（显示自动更新频率和时间。）
current status: normal（显示MITRE ATT&CK®知识库的更新状态为正常。）
last update result: not update yet from system up（显示MITRE ATT&CK®知识库上次更新的结
果。）

<!-- 来源页 2294 -->
僵尸网络防御
僵尸网络，是指采用一种或多种传播手段，使大量主机感染僵尸程序，从而在控制者和被感染主机之间所形
成的一个可一对多控制的网络，对用户的网络安全以及数据安全造成很大的威胁隐患。
系统的僵尸网络防御功能能够根据特征库中的地址及时发现用户内网的僵尸主机，并且根据配置对发现的僵
尸主机进行处理，从而避免发生进一步的威胁攻击。
系统支持基于安全域和基于策略的僵尸网络防御配置方式。为安全域配置僵尸网络防御规则后，系统将会对
以绑定安全域为源/目的安全域的流量根据僵尸网络防御规则配置进行僵尸网络检查。将僵尸网络防御规则绑
定到策略规则后，系统将会对与策略规则相匹配的流量根据规则配置进行僵尸网络检查。
DGA检测
DNS作为域名解析协议，用于地址和域名的双向解析，由于域名使用方便，被广泛应用，因此攻击者会采取
不同手段利用域名产生攻击。例如：一个IP地址可对应多个域名，服务器根据HTTP报文的Host字段来确定
目标网站，一些恶意软件会利用这一特性通过修改Host字段来伪装域名，产生恶意攻击行为；DGA
（Domain Generation Algorithm）即域名生成算法，该算法会生成大量的伪随机域名，并且会被恶意软
件所采用；运营商DNS劫持，将一些长期被恶意软件所采用的恶意域名加入其黑名单。
针对上述这些问题，设备支持启用DGA检测功能，对DNS响应报文进行检测，检测设备是否遭受DGA域名攻
击。若检测到DGA域名，系统将会根据僵尸网络防御规则的配置，对检测到的DGA域名执行指定的处理动作
（记录相关的威胁日志、重置连接和Sinkhole地址替换）。
DNS隧道检测
DNS隧道是隐蔽信道的一种，通过将其他协议封装在DNS协议中传输建立通信。但是大多数防火墙和检测设
备对DNS流量放行，而DNS隧道攻击正式利用了放行的特点，实现例如远程控制、文件传输等操作，对用户
的网络安全以及数据安全造成危害。因此，对DNS隧道的检测、告警和处理尤为重要。
系统提供了DNS隧道检测功能，通过对DNS请求报文的检测以及对DNS流量的监控，来实现对DNS隧道的特
征提取、综合分析，同时还可以对检测到的DNS隧道执行指定的处理动作（记录相关的威胁日志和重置连
接），从而阻止DNS隧道带来的威胁。
注意: 僵尸网络防御功能受许可证控制，DGA检测和DNS隧道检测均包含在僵尸网络防御功能中，
因此，为支持僵尸网络防御功能的设备安装僵尸网络防御许可证后，僵尸网络防御功能、DGA检测
功能以及DNS隧道检测才可使用。

<!-- 来源页 2295 -->
配置僵尸网络防御
僵尸网络防御配置准备工作
使用僵尸网络防御功能前，必须完成以下准备工作：
1. 确认系统版本支持僵尸网络防御功能。
2. 安装僵尸网络防御许可证，然后重启设备。设备成功重启后，僵尸网络防御功能即处于开启状态。
开启/关闭僵尸网络防御功能
用户可以通过show version命令查看僵尸网络防御功能是否开启。开启或者关闭僵尸网络防御功能，在任
何模式下使用以下命令：
exec botnet-c2-prevention {enable | disable}
l
enable – 开启系统的僵尸网络防御功能。
l
disable – 关闭系统的僵尸网络防御功能。
配置僵尸网络防御功能
实现系统的僵尸网络防御功能，用户需要按照以下步骤进行操作：
1. 开启僵尸网络防御功能。
2. 定义僵尸网络防御Profile，在Profile中指定外联威胁防护类型、扫描协议、系统发现僵尸网络后采取的动作、系
统检测到威胁时是否抓取相关证据报文。
3. 绑定僵尸网络防御Profile到适当的策略规则或者将僵尸网络防御Profile绑定到安全域。
注意: 初次使用僵尸网络防御功能，需要首先更新僵尸网络防御特征库。关于僵尸网络防御特征库
更新配置，请参阅“僵尸网络防御特征库更新配置”。为保证能够正常连接到默认更新服务器，请
在更新前为设备配置DNS服务器。
用户可使用系统默认的僵尸网络防御规则，也可自行创建规则。系统提供4个默认的僵尸网络防御规则
predef_critical、predef_default、predef_emergency和no-botnet-c2-prevention：
l predef_critical - 严格的僵尸网络防御检查策略。此规则扫描TCP/HTTP/DNS/TLS/ICMP协议流量，发现僵尸主
机后，重置恶意连接，并记录威胁日志。
l predef_default - 宽松的僵尸网络防御检查策略。此规则扫描TCP/HTTP/DNS/TLS/ICMP协议流量，发现僵尸主
机后，对流量放行，仅记录威胁日志。

<!-- 来源页 2296 -->
l predef_emergency - 重保模式模板，监控所有协议类型，一旦发现僵尸网络活动，立即执行重置操作。
l no-botnet-c2-prevention – 此规则不进行任何僵尸网络防御检查。
创建僵尸网络防御Profile
僵尸网络防御Profile中主要指定需要C&C检查的协议类型，以及系统发现僵尸主机后的动作。创建僵尸网络
防御Profile，在全局配置模式下使用以下命令：
botnet-c2-prevention profile profile-name
l
profile-name - 指定所创建的僵尸网络防御Profile的名称，并且进入该僵尸网络防御Profile的配置模
式。如果指定名称已存在，则直接进入僵尸网络防御Profile配置模式。
使用no botnet-c2-prevention profile-name删除指定的僵尸网络防御Profile。
指定外联威胁防护类型及控制动作
指定需要防护的外联威胁防护类型（即IOC标签类型）后，当流量命中预定义/自定义阻断名单或云查缓存黑
名单时，则会根据指定外联类型进行检测流量数据的IOC类型标签，并根据对应的动作进行处理；如果未指
定，则会根据通用类型的协议配置进行检测和处理。
注意:
l
进行TLS检测时，需要开启对应安全域下的应用识别功能，避免无法识别加密协议或者协议识
别错误。
l
TLS检测仅支持检测以下协议：HTTPS、FTPS、SMTPS、POP3S、IMAPS。
l
针对FTPS、SMTPS、POP3S、IMAPS协议的TLS检测，仅支持对协议的隐式加密处理进行检
测，不支持检测显式加密处理。
l
TLS检测仅支持抓取单个报文作为证据信息，不支持抓取双向报文或者多个报文。
l
开启未知域名云端查询功能后，如果未知域名上送云端后被检测为黑名单域名，则设备会在收
到响应报文后记录威胁日志，抓取响应报文，并执行防护动作。
l
当用户使用ping工具测试网络的连通性和时延时，如果开启了ICMP隧道检测，可能会影响
ICMP报文的转发速度，导致网络连通性测试结果不准确。
指定需要防护的外联威胁防护类型，并指定相应的处理动作。在僵尸网络防御Profile配置模式下，使用以下
命令：

<!-- 来源页 2297 -->
botnet-c2-prevention threat-type {APT | CnC | DDNS | Malware | Miner | Phishing | Proxy |
Ransomware | Trojan | DGA | Dns-tunnel | Icmp-tunnel} protocol {tcp | http | dns | tls |
icmp}action {reset| log-only | sinkhole-replace} [intelligent-algorithm {enable | disable}]
l
APT | CnC | DDNS | Malware | Miner | Phishing | Proxy | Ransomware | Trojan | DGA | Dnstunnel | Icmp-tunnel – 指定需要防护的外联威胁防护类型，包括APT检测（APT ）、CnC服务器检测
（ CnC ）、动态DNS域名检测（ DDNS）、恶意软件检测（ Malware）、挖矿检测（ Miner ）、网
络钓鱼检测（Phishing）、代理服务器检测（ Proxy）、勒索软件检测（ Ransomware）、木马检
测（ Trojan）、DGA检测（ DGA ）、DNS隧道检测（ Dns-tunnel ）、ICMP隧道检测（Icmptunnel）。
l
tcp | http | dns | tls | icmp – 指定对所选外联类型开启针对不同协议（TCP、HTTP、DNS、TLS、
ICMP）的扫描检测。
l
action { reset | log-only | sinkhole-replace} – 指定采取的动作。
l
reset – 指定该参数后，系统对应外联类型的威胁事件后，重置恶意连接，并记录威胁日志。
l
log-only – 指定该参数后，系统对应外联类型的威胁事件后，对流量放行，仅记录日志信息（威
胁日志），该选项采取的默认动作。
l
sinkhole-replace - 当协议类型为DNS，可以指定处理动作为“Sinkhole地址替换”。指定
后，若发现威胁后，系统会将DNS应答报文中的IP地址替换为已指定的Sinkhole IP地址。
l
intelligent-algorithm {enable | disable} – 开启（enable）/关闭（disable）本地智能算法。对
于“DGA检测（ DGA ）”、“DNS隧道检测（ Dns-tunnel ）”和“ICMP隧道检测（Icmptunnel）”类型，默认开启本地智能算法，能够采用该算法提高检测准确率并降低误报率。其中“ICMP
隧道检测（Icmp-tunnel）”只支持本地智能算法，关闭该算法后检测将不生效。
使用以上命令no的形式取消协议类型的指定：
no botnet-c2-prevention threat-type {APT | CnC | DDNS | Malware | Miner | Phishing | Proxy |
Ransomware | Trojan | DGA | Dns-tunnel | Icmp-tunnel} protocol {tcp | http | dns | tls | icmp}
指定协议类型及控制动作
注意:
l
进行TLS检测时，需要开启对应安全域下的应用识别功能，避免无法识别加密协议或者协议识
别错误。

<!-- 来源页 2298 -->
l
TLS检测仅支持检测以下协议：HTTPS、FTPS、SMTPS、POP3S、IMAPS。
l
针对FTPS、SMTPS、POP3S、IMAPS协议的TLS检测，仅支持对协议的隐式加密处理进行检
测，不支持检测显式加密处理。
l
TLS检测仅支持抓取单个报文作为证据信息，不支持抓取双向报文或者多个报文。
l
开启未知域名云端协同查询后，如果未知域名上送云端后被检测为黑名单域名，则设备会在收
到响应报文后记录威胁日志，抓取响应报文，并执行防护动作。
指定协议类型及控制动作，在僵尸网络防御Profile配置模式下，使用以下命令：
botnet-c2-prevention protocol {tcp | http | dns | tls} action {reset | log-only | sinkholereplace}
l
tcp – 指定对通过TCP协议传输的信息进行僵尸网络防御检查。
l
http – 指定对通过HTTP协议传输的信息进行僵尸网络防御检查。
l
dns – 指定对通过DNS协议传输的信息进行僵尸网络防御检查。
l
tls – 指定对通过TLS协议传输的信息进行僵尸网络防御检查。
l
action { reset | log-only | sinkhole-replace} – 指定采取的动作。
l
reset – 指定该参数后，系统发现威胁后，重置恶意连接，并记录威胁日志。
l
log-only – 指定该参数后，系统发现威胁后，对流量放行，仅记录日志信息（威胁日志），该选
项采取的默认动作。
l
sinkhole-replace - 当协议类型为DNS，可以指定处理动作为“Sinkhole地址替换”。指定
后，若发现威胁后，系统会将DNS应答报文中的IP地址替换为已指定的Sinkhole IP地址。
使用以上命令no的形式取消协议类型的指定：
no botnet-c2-prevention protocol {tcp | http | dns | tls}
指定日志聚合类型以及聚合时间间隔
系统可将具有相同属性的僵尸网络防御日志进行聚合，并指定日志聚合的时间间隔，从而减少日志数量，避
免日志服务器接受冗余的日志信息。指定日志聚合类型以及聚合时间间隔，在全局配置模式下，使用以下命
令：
botnet-c2-prevention agg-log enable [by-src | by-dst | by-src-dst | by-src-ioc | by-dst-ioc |
by-src-dst-ioc] [aggregation-time value]

<!-- 来源页 2299 -->
l
botnet-c2-prevention agg-log enable - 将按照默认聚合类型（同源IP且相同IOC）和默认时间间
隔（10秒）进行日志聚合。
l
by-src - 将相同源IP的日志进行聚合。
l
by-dst - 将相同目的IP的日志进行聚合。
l
by-src-dst - 将相同源IP且相同目的IP的日志进行聚合。
l
by-src-ioc - 将相同源IP且相同IOC的日志进行聚合。其中，IOC表示威胁情报，即僵尸网络防御功能
检测出的恶意域名、IP地址或URL。
l
by-dst-ioc - 将相同目的IP且相同IOC的日志进行聚合。其中，IOC表示威胁情报，即僵尸网络防御功
能检测出的恶意域名、IP地址或URL。
l
by-src-dst-ioc - 将相同源IP、相同目的IP且相同IOC的日志进行聚合。其中，IOC表示威胁情报，即
僵尸网络防御功能检测出的恶意域名、IP地址或URL。
l
value - 指定日志聚合的时间间隔。指定后，系统将对同一时间间隔内，同一聚合类型的日志只存入数
据库一次，不再重复存入多次。范围是10到600秒。如不指定，默认时间间隔为10秒。
在全局配置模式下使用no botnet-c2-prevention agg-log enable指定日志聚合类型为“不聚合”，即
不聚合日志。将每一条僵尸网络防御日志分别存入数据库，不进行日志聚合。
指定DNS隧道日志记录时间间隔
当系统检测到DNS隧道后，将会记录日志信息，用户可以指定记录日志信息的最小时间间隔，在全局配置模
式下，使用以下命令：
dns-tunnel-detect log-interval time-interval
l
time-interval - 指定记录日志信息的最小时间间隔，单位为秒。范围是1到3600秒。默认值是60秒。
在全局配置模式下使用no dns-tunnel-detect log-interval恢复时间间隔的默认值。
配置Sinkhole IP地址
用户可以选择系统预定义的Sinkhole IP地址或指定自定义的Sinkhole IP地址，用于替换DNS应答报文中IP
地址的Sinkhole IP地址。
配置Sinkhole IP地址，在全局配置模式下，使用以下命令：
botnet-c2-prevention sinkhole {ipv4 IPv4-address | ipv6 IPv6-address | predefined-sinkhole}
l
ipv4 IPv4-address - 指定自定义Sinkhole IPv4地址。如果仅配置了IPv4地址而没有配置IPv6地址，
当DNS服务器使用IPv6协议通信时，系统会自动则将配置的IPv4地址映射为相应的IPv6地址。

<!-- 来源页 2300 -->
l
ipv6 IPv6-address - 指定自定义Sinkhole IPv6地址。
l
predefined-sinkhole - 指定使用预定义的Sinkhole IP地址。
绑定僵尸网络防御Profile到安全域
将僵尸网络防御Profile绑定到安全域后，系统将会对以该安全域为目的安全域的流量按照Profile配置进行
僵尸网络防御检查。当策略规则已经绑定了僵尸网络防御Profile，同时策略规则的目的安全域也绑定了僵尸
网络防御Profile，策略规则绑定的僵尸网络防御Profile将会生效，而目的安全域绑定的僵尸网络防御
Profile无效。
绑定僵尸网络防御Profile到安全域，在安全域配置模式下，使用以下命令：
botnet-c2-prevention enable {profile-name | no-botnet-c2-prevention | predef_critical |
predef_default | predef_emergency}
l
profile-name – 指定绑定到安全域的僵尸网络防御Profile的名称。一个安全域只能绑定一个僵尸网络
防御Profile。
l
no-botnet-c2-prevention - 绑定名为no-botnet-c2-prevention的预定义僵尸网络防御Profile到
安全域。
l
predef_critical - 绑定名为predef_critical的预定义僵尸网络防御Profile到安全域。
l
predef_default - 绑定名为predef_default的预定义僵尸网络防御Profile到安全域。
l
predef_emergency - 绑定名为predef_emergency的预定义僵尸网络防御Profile到安全域。
在安全域配置模式下，使用该命令no的形式取消僵尸网络防御Profile的绑定：
no botnet-c2-prevention enable
绑定僵尸网络防御Profile到策略规则
将僵尸网络防御Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据Profile配置进行僵尸
网络防御检查。绑定僵尸网络防御Profile到策略规则，在策略规则配置模式下使用以下命令：
botnet-c2-prevention {profile-name | no-botnet-c2-prevention | predef_critical | predef_
default | predef_emergency}
l
profile-name – 指定绑定到策略规则的僵尸网络防御Profile的名称。
l
no-botnet-c2-prevention - 绑定名为no-botnet-c2-prevention的预定义僵尸网络防御Profile到
策略规则。
l
predef_critical - 绑定名为predef_critical的预定义僵尸网络防御Profile到策略规则。

<!-- 来源页 2301 -->
l
predef_default - 绑定名为predef_default的预定义僵尸网络防御Profile到策略规则。
l
predef_emergency - 绑定名为predef_emergency的预定义僵尸网络防御Profile到策略规则。
在策略规则配置模式下使用该命令no的形式取消僵尸网络防御Profile的绑定：no botnet-c2-prevention
显示僵尸网络防御profile信息
在任何模式下，输入以下命令显示僵尸网络防御profile信息：
show botnet-c2-prevention-profile profile-name
显示僵尸网络防御状态
在任何模式下，输入以下命令显示僵尸网络防御状态信息：
show botnet-c2-prevention status
显示僵尸网络防御日志聚合配置信息
在任何模式下，输入以下命令显示僵尸网络防御日志聚合配置信息：
show botnet-c2-prevention log aggregation
僵尸网络防御特征库更新配置
默认情况下，系统会每日自动更新僵尸网络防御特征库，用户可以根据需要更改僵尸网络防御特征库更新配
置。僵尸网络防御特征库更新配置包括：
l 配置僵尸网络防御特征库更新模式
l 配置更新传输协议
l 配置更新服务器
l 指定HTTP代理服务器
l 指定更新时间
l 立即更新
l 导入僵尸网络防御特征文件
l 显示僵尸网络防御特征信息
l 显示僵尸网络防御特征库加载状态
l 显示僵尸网络防御特征库更新配置信息

<!-- 来源页 2302 -->
配置僵尸网络防御特征库更新模式
系统支持手动和自动两种更新方式。配置僵尸网络防御特征库更新方式，在全局配置模式下，使用以下命
令：
botnet-c2-prevention signature update mode {auto | manual}
l
auto – 指定自动更新僵尸网络防御特征库。该方式为系统的默认更新方式。
l
manual – 指定手动更新僵尸网络防御特征库。
在全局配置模式下使用该命令no的形式恢复默认更新模式：
no botnet-c2-prevention signature update mode
配置更新传输协议
系统支持通过HTTP和HTTPS对特征库进行更新，默认为HTTPS。配置特征库更新的传输协议为HTTP，在全
局配置模式下，使用以下命令：
botnet-c2-prevention update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：
no botnet-c2-prevention update protocol HTTP
配置更新服务器
系统提供默认的僵尸网络防御特征库更新服务器，即update1.hillstonenet.com和
update2.hillstonenet.com，同时用户也可以根据需要配置其它更新服务器下载最新C&C防御特征。最多
可配置3个。配置更新服务器，在全局配置模式下，使用以下命令：
botnet-c2-prevention signature update {server1 | server2 | server3} {ip-address | domainname} [vrouter vrouter-name] [src-interface src-interface-name]
l
server1 | server2 | server3 – 指定将要配置的服务器，server1服务器支持双栈协议，可配置IPv4地
址和IPv6地址。。server1的默认值为update1.hillstonenet.com，server2的默认值为
update2.hillstonenet.com。
l
ip-address | domain-name – 指定更新服务器的名称，可以是IP地址形式（ip-address）也可以是
域名形式（domain-name，例如update1.hillstonenet.com）。
l
vrouter vrouter-name - 指定更新服务器所属的VRouter。若不指定则默认是trust-vr。
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，僵尸网络防御特征库更新时将通过该源接口对更新服务器发起访问。若不指定，则默认使用管理口
作为源接口。

<!-- 来源页 2303 -->
在全局配置模式下，使用该命令no的形式取消更新服务器的指定：
no botnet-c2-prevention signature update {server1 | server2 | server3}
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保特征库能够正常升级，需要在设备上指定代理服务器
的IP地址和端口号。
为僵尸网络防御特征库升级指定代理服务器，在全局配置模式下，使用如下命令：
botnet-c2-prevention signature update proxy-server {main | backup} ip-address portnumber
l
main | backup – 使用main参数指定主代理服务器，使用backup指定备份代理服务器。
l
ip-address port-number – 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no botnet-c2-prevention signature update proxy-server {main |
backup}命令。
指定更新时间
默认情况下，系统采用自动模式每日更新僵尸网络防御特征库，并且为避免服务器流量过大，每日更新时间
是随机的。用户可以根据需要指定僵尸网络防御特征库更新的频率和时间，在全局配置模式下，使用以下命
令：
botnet-c2-prevention signature update schedule { {daily | weekly {mon | tue | wed | thu | fri |
sat | sun} | monthly date} [HH:MM] | hourly MM }
l
daily – 指定频率为每天更新。
l
weekly {mon | tue | wed | thu | fri | sat | sun} – 指定频率为每周更新。mon | tue | wed | thu | fri
| sat | sun用来指定每周更新的日期。
l
monthly date - 指定频率为每月更新。date用来指定每月更新的日期，取值范围为1到31。如果某月
不包含所指定的日期（比如2月没有30号），则该月不会自动升级。
l
HH:MM – 指定更新的时间，例如09：00。
l
hourly MM– 指定频率为每小时更新。MM为分钟数。
立即更新
无论更新模式为手动还是自动，用户都可以随时使用以下命令更新僵尸网络防御特征库。立即更新僵尸网络
防御特征库，在任何模式下，使用以下命令：
exec botnet-c2-prevention signature update

<!-- 来源页 2304 -->
l
exec botnet-c2-prevention signature update – 仅对当前僵尸网络防御特征库与更新服务器最新
发布僵尸网络防御特征库的不同部分进行更新。
导入僵尸网络防御特征文件
在某些情况下，用户设备可能无法连接到更新服务器对僵尸网络防御特征库进行更新，针对这一问题，系统
提供僵尸网络防御特征文件导入功能，即通过FTP、TFTP服务器或者U盘将僵尸网络防御特征文件导入到设
备，从而更新设备的僵尸网络防御特征库。导入僵尸网络防御特征文件，在执行模式下，使用以下命令：
import botnet-c2-prevention signature from {ftp server ip-address [user user-name
password password] | tftp server ip-address | usb0 | usb1 } [vrouter vr-name] file-name
l
ip-address – 指定FTP或者TFTP服务器的IP地址。
l
user user-name password password – 指定FTP服务器的用户名和密码。
l
vrouter vr-name – 指定FTP或者TFTP服务器所属的VRouter。
l
file-name – 指定导入的僵尸网络防御特征文件的名称。
显示僵尸网络防御特征库信息
查看设备的僵尸网络防御特征库信息。在任何模式下使用以下命令：
show botnet-c2-prevention signature info
显示僵尸网络防御特征库加载状态
查看设备的僵尸网络防御特征库加载状态。在任何模式下使用以下命令：
show botnet-c2-prevention load-status
以下是返回结果示例：
hostname#show botnet-c2-prevention load-status
Botnet Prevention signature load status: completed
显示僵尸网络防御特征库更新配置信息
查看设备上的僵尸网络防御特征库更新信息，包括更新服务器信息、更新模式、更新频率及时间以及僵尸网
络防御特征库更新状况等。查看僵尸网络防御特征库更新配置信息，在任何模式下使用以下命令：
show botnet-c2-prevention signature update

<!-- 来源页 2305 -->
抓包取证
介绍
当威胁流量经过设备时，系统会抓取相关威胁报文，用户可以在对应的威胁日志中查看或下载抓取的报文。
同时可以结合连接云平台功能，将威胁报文数据上送至云端，助力用户快速完成威胁研判和处置。
使用限制和注意事项
通用
l 对于不带硬盘的设备和带硬盘的A1600/A1800/A2200设备，开启抓包取证功能时，需同时开启“加入用户体验
改进计划”并开启云·景的威胁日志上报，抓包取证功能才能生效。在该情况下，防火墙设备上将无法查看到抓
包取证的报文数据，系统会将抓包取证的报文数据和威胁日志信息上送至云·景，安全运营人员可以根据抓包取
证的证据信息对威胁日志信息进行分析研判。
抓包取证模式相关
l 抓包取证模式只对入侵检测和僵尸网络防御功能生效。
l 抓包取证模式为扩展模式时，最多支持抓取100个报文。
l 抓包取证模式为扩展模式时，若威胁报文数据超过了配置的“单次连接取证报文量上限”或超过100个报文，可
能会出现抓取的威胁报文数据不完整的情况。
l 若抓包取证功能占用的内存超过总DP（数据平面）内存的十分之一时，无论此时系统配置的抓包取证模式是基础
模式还是扩展模式，后续系统检测到威胁时采用的抓包取证模式均为基础模式。（可以使用show memory
detail命令查看系统DP内存使用情况）
入侵防御功能相关
l 反弹shell检测仅支持抓取检测出威胁的单个报文。
l 弱口令检测和HTTP明文密码检测不支持将证据报文上送至云端。
僵尸网络防御功能相关
l TCP协议检测和DNS域名检测支持抓取检测出威胁的单个报文，也支持抓取后续的业务交互报文。
l Sinkhole恶意IP日志不支持抓包取证。

<!-- 来源页 2306 -->
抓包取证配置步骤
1. 全局配置抓包取证模式。
抓包取证有基础和扩展两种模式，系统默认使用基础模式进行抓包取证。
l 基础模式：系统能够抓取检测到威胁时的报文。对于HTTP协议，系统会抓取请求和响应报文。
l 扩展模式：系统能够抓取检测到威胁时以及检测到威胁前的报文数据，抓取的报文数据量上限可以通过
“单个连接取证报文量”进行配置。对于僵尸网络检测功能中的HTTP协议以及入侵检测功能，系统会抓
取请求和响应报文。
配置抓包取证模式，在全局配置模式下，使用以下命令：
attack-forensics-mode {basic | extended limit value}
l basic - 指定使用基础模式进行抓包取证。
l extended limit value - 使用扩展模式进行抓包取证。使用扩展模式时，需要同时配置单个连接取证报文
量上限，达到上限后，对最早抓取的报文数据进行丢弃。范围是5-50KB，默认为5KB。
注意: 抓包取证模式只对入侵防御和僵尸网络防御功能生效。
2. 开启入侵防御/僵尸网络防御的抓包取证功能开关。
开启入侵防御/僵尸网络防御的抓包取证功能后，当系统检测到对应威胁时会抓取相关报文。用户可以在
对应的威胁日志中查看或下载抓取的报文。
l 开启僵尸网络防御的抓包取证功能，在僵尸网络防御Profile配置模式下，使用attack-forensic enable命
令。如需关闭此功能，可以在僵尸网络防御Profile配置模式下，使用attack-forensic disable命令。默认
情况下，默认情况下，僵尸网络防御的抓包取证功能为开启状态。
l 开启入侵防御的抓包取证功能，在IPS Profile配置模式下，使用pcap enable命令。如需关闭此功能，可
以在IPS Profile配置模式下，使用pcap disable命令。默认情况下，入侵防御的抓包取证功能为关闭状
态。
3. （可选）连接云平台，启用“加入用户体验改进计划”和“云·景”。
开启后，当设备检测出威胁时会进行抓包处理，并将抓包获取的威胁报文数据和威胁日志信息上送至云·
景，用户可以登录云·景进行查看和处置。
a. 连接云平台：参阅“云平台服务器对接配置”章节。
b. 加入用户体验改进计划：在Cloud Server配置模式下，使用user-experience-improvement-plan
enable命令。

<!-- 来源页 2307 -->
c. 启用云·景：在Cloud View配置模式下，使用enable命令。
d. 开启威胁日志上报：在Cloud View配置模式下，使用uptype-log threat-event命令。
4. 查看威胁证据信息。
当威胁流量经过设备时，设备会检测出威胁并进行抓包处理，用户可以在WebUI上查看或下载获取的威
胁报文数据信息。
对于僵尸网络防御中通过TCP协议检测或DNS域名检测所命中的威胁，用户还可以在WebUI上查看或下
载关联连接报文，以获取后续的业务交互数据，辅助威胁研判。
查看抓包缺失原因统计数据
该功能主要用于帮助用户诊断报文无法完整抓取的原因，评估威胁分析所依赖的数据完整性。
查看抓包缺失原因的统计数据，在任意模式下，使用以下命令：
show attack-forensics-statistic
返回示例：
hostname# show attack-forensics-statistic

<!-- 来源页 2308 -->
Attack forensics statistic:
no response count:181.
exceed time count:7.
exceed memory count:2.
exceed limit count:2.
dropped by speed control:1.
显示信息
统计的抓包缺失原因
说明
no response
count
超过2秒未收到响应报文
系统发送抓包请求后，若在2秒内未收到响应报文，则会
导致抓包数据缺失。
exceed time
count
距离取证开始超过5秒，
转为基础模式
扩展模式下，系统对每个session进行抓包时，从抓取到
第一个包开始计时。若超过5秒仍未完成抓包，系统将自
动切换至基础模式，从而导致抓包数据不完整。
exceed memory
count
当前占用的DP内存超过
总内存的1/10，转为基
础模式
扩展模式下，当抓包取证占用的DP（Data plane，数据
平面）内存超过系统总DP内存的10%时，系统会自动切
换至基础模式抓包，从而导致抓包数据不完整。
exceed limit
count
超出抓包上限，删除部分
报文
当系统抓取的单个连接取证报文量超过预设阈值时，将自
动删除超出部分的报文，从而造成抓包数据缺失。
dropped by
speed control
流量超速被限速丢包
当报文流量速率超出硬件处理能力上限时，限速机制将主
动丢弃部分报文，进而导致抓包数据缺失。
清除抓包缺失原因统计数据
在任何模式下，使用以下命令，清除抓包缺失原因统计数据：
show attack-forensics-statistic clear
僵尸网络防御地址库
僵尸网络防御地址库包括阻断名单和例外名单和云查缓存，其中阻断名单和例外名单包括预定义和自定义名
单，描述如下：
l 例外名单：当流量匹配到例外名单中的IP地址、域名或URL时，系统将不会对该流量进行僵尸网络防御功能控
制。预定义例外名单通过僵尸网络防御特征库自动获取；自定义例外名单通过用户手动添加IP地址、域名和
URL。
l 阻断名单：当流量匹配到阻断名单中的IP地址、域名和URL时，系统会对该流量进行僵尸网络防御功能控制。预
定义阻断名单通过僵尸网络防御特征库自动获取；自定义阻断名单通过用户手动添加IP地址、域名和URL。

<!-- 来源页 2309 -->
l 云查缓存：实时展示对于未知域名在云端的核查结果、云端自动推送的域名/IP/URL地址，用户可以通过指定IP/
域名/URL域名在云端缓存信息中精确查询详细的云查结果，并参考云查结果继续执行对应的操作。
注意:
l
系统对流量进行僵尸网络防御功能控制的匹配顺序为：自定义例外名单> 自定义阻断名单> 云
查缓存名单> 预定义例外名单> 预定义阻断名单。
l
云查缓存条目不会加入到僵尸网络防御地址库中，仅缓存在设备中。
配置例外名单
配置自定义例外名单
配置自定义例外名单特征条目，在全局配置模式下，使用以下命令：
botnet-c2-prevention allowlist {ip ip-address [port port-number | domain domain-name
[wildcard] | url url}
l
ip ip-address [port port-number] - 指定自定义地址库例外名单特征条目的IP地址及端口号。不输
入端口号，默认为任意端口。
l
domain domain-name [wildcard] - 指定自定义地址库例外名单特征条目的域名。wildcard指定域
名为通配符域名。
使用以上命令no的形式删除指定的自定义例外名单特征条目：
no botnet-c2-prevention allowlist {ip ip-address [port port-number | domain domain-name
[wildcard] | url url}
配置阻断名单
配置自定义阻断名单
配置自定义阻断名单特征条目，在全局配置模式下，使用以下命令：
botnet-c2-prevention signature {ip ip-address [port port-number] | domaindomain-name
[wildcard] | url url}
l
ip ip-address [port port-number - 指定自定义地址库阻断名单特征条目的IP地址及端口号。不输入
端口号，默认为任意端口。
l
domain domain-name [wildcard] - 指定自定义地址库阻断名单特征条目的域名。wildcard指定域
名为通配符域名。

<!-- 来源页 2310 -->
使用以上命令no的形式删除指定的自定义地址库阻断名单特征条目：
no botnet-c2-prevention signature {ip ip-address [port port-number] | domain domainname [wildcard] | urlurl}
查看自定义及预定义阻断名单
在任何模式下，输入以下命令显示所有或指定条件的自定义和预定义阻断名单：
show botnet-c2-prevention blocklist [ip ip-address [port port-number] | domain domainname [wildcard] | url url]
输出信息中：
l
entry：表示黑名单的具体IP地址、域名或URL。
l
type：表示黑名单的类型，1表示IP，2表示精确域名，3表示通配符域名，4表示IP+Port，5表示
URL。
l
define type：表示黑名单的定义类型，1表示预定义黑名单，2表示自定义黑名单。
l
tag：表示C&C库IOC（Indicator of Compromise）黑名单关联的恶意威胁标签，当有多个标签时，
只显示前5个。
l
malfare family：表示IOC对应的恶意家族名称。
l
APT group：表示IOC对应的攻击团伙名称。
示例：
hostname# show botnet-c2-prevention bl ip 118.0.0.2
Botnet Prevention blocklist
Total num: 0
==========================================
entry type define type tag malware family APT group
------------------------------------------------------------------------------------
==========================================
在任何模式下，输入以下命令显示所有或指定条件的自定义的预定义例外名单：
show botnet-c2-prevention allowlist [ip ip-address [port port-number] | domain domainname [wildcard] | url url]

<!-- 来源页 2311 -->
配置黑名单库
黑名单库是以文件形式保存的批量阻断名单条目，包含IP地址、域名或URL。系统支持手动导入/导出黑名单
库或从指定服务器自动更新黑名单库。
手动导入黑名单库文件，在执行模式下使用以下命令：
import botnet-c2-prevention blocklist-lib {add | cover} from {{ftp | ftps | sftp} server ipaddress [user user-name password password] | tftp server ip-address} [vrouter vroutername] file-name
l
add | cover - 指定黑名单库更新的方式，add表示增量导入，cover表示覆盖导入。
l
{ftp | ftps | sftp} server ip-address [user user-name password password] - 指定
FTP/FTPS/SFTP服务器的IP地址及账户名称密码。
l
tftp server ip-address - 指定TFTP服务器的IP地址。
l
[vrouter vrouter-name] - 指定FTP、FTPS、SFTP或者TFTP服务器所属的VRouter。
l
file-name – 指定黑名单库文件在FTP、FTPS、SFTP或者TFTP的路径。
导出所有黑名单库文件，在执行模式下使用以下命令：
export botnet-c2-prevention blocklist-lib to {{ftp | ftps | sftp} server ip-address [user username password password] | tftp server ip-address} [vrouter vrouter-name] file-name
l
{ftp | ftps | sftp} server ip-address [user user-name password password] - 指定
FTP/FTPS/SFTP服务器的IP地址及账户名称密码。
l
tftp server ip-address - 指定TFTP服务器的IP地址。
l
[vrouter vrouter-name] - 指定FTP、FTPS、SFTP或者TFTP服务器所属的VRouter。
l
file-name – 指定导出的黑名单库文件的名称。
配置导入黑名单库自动更新的导入模式、ip+文件名（或URL）、虚拟路由器、用户名和密码，在全局配置模
式下，使用以下命令：
botnet-c2-prevention block-lib auto-update {add | cover} from {{ ftp server ip-address [user
user-name password password] | tftp server ip-address} [vrouter vrouter-name] file-name |
{http | https} [vrouter vrouter-name] url url}
l
add | cover- 指定黑名单库更新的方式，add表示增量导入，cover表示覆盖导入。
l
ftp server ip-address [user user-name password password] - 指定FTP服务器的IP地址及账户
名称密码。

<!-- 来源页 2312 -->
l
tftp server ip-address - 指定TFTP服务器的IP地址。
l
[vrouter vrouter-name] - 指定FTP或者TFTP服务器所属的VRouter。
l
file-name – 指定黑名单库文件在FTP或者TFTP的路径。
l
http | https - 指定从HTTP或者HTTPS服务器更新黑名单库。
l
[vrouter vrouter-name] - 指定HTTP或者HTTPS服务器所属的VRouter。
l
url url - 指定HTTP或者HTTPS服务器的URL地址，范围是1-255个字符。HTTP服务器URL必须以
“http://”开头，HTTPS服务器URL必须以“https://”开头。HTTP/HTTPS服务器URL需以后缀
为.csv/.json/.stix2/.ioc/.xml/.sig的文件名结尾，例如
http://192.1.1.1:8080/chfs/shared/SERVER/ftp/test/score.csv。
配置黑名单库自动更新的频率和时间，在全局配置模式下，有以下三种方式：
o
指定频率为每天自动更新，使用以下命令：
o
botnet-c2-prevention block-lib auto-update schedule daily [HH:MM]
l
HH:MM - 指定每天更新的时间，取值范围为00:00到23:59。
o
指定频率为每周自动更新，使用以下命令：
o
botnet-c2-prevention block-lib auto-update schedule weekly {mon | tue | wed | thu | fri |
sat | sun} [HH:MM]
l
mon | tue | wed | thu | fri | sat | sun - 用来指定每周更新的日期。
l
HH:MM - 指定每周更新的时间，取值范围为00:00到23:59。
o
指定频率为按周期自动更新，使用以下命令：
o
botnet-c2-prevention block-lib auto-update schedule interval <1-10080>
l
interval <1-10080> - 指定按周期更新的时间间隔，单位为分钟，取值范围为1-10080分钟。
o
说明：配置自动更新的频率和时间之前，请先配置自动更新的导入模式，否则上述命令无法生效。
注意:
l
手动导入或自动更新的黑名单库文件支持CSV/STIX/OpenIOC格式的文件，文件后缀名包
含.csv/.json/.stix2/.ioc/.xml/.sig，其中仅.csv文件支持导入子域名。
l
.sig格式的黑名单文件仅支持覆盖导入。若选择增量导入，系统会提示导入失败。

<!-- 来源页 2313 -->
l
设备不会解析存储黑名单条目的描述信息，导入带有描述信息的黑名单库文件后再导出，会丢
失对应的描述信息。描述信息仅作为提示或备注，描述信息丢失并不影响黑名单库文件的重复
使用。
l
手动导入或自动更新的黑名单文件大小根据不同型号设备而有所差异，请以实际设备为准。
l
手动导入或自动更新黑名单库文件时会按导入先后顺序进行冗余检测。在无文件格式和内容问
题的前提下，不论是完全重合还是部分重合，黑名单库文件均导入成功，并在对应日志中显示
此次导入文件的黑名单条目总数量、实际导入的黑名单条目数和重复的黑名单条目数。
l
手动导入指定黑名单库文件时，若导入的黑名单条目超过设备僵尸网络防御黑白名单容量则该
文件无法导入；自动更新黑名单库文件时，若导入的黑名单条目超过设备僵尸网络防御黑白名
单总容量，则优先导入满足设备僵尸网络防御黑白名单总容量的条目数，剩余黑名单条目则不
导入。
l
SG-6000-A2200、SG-6000-A1800和SG-6000-A1600不支持黑名单库。
清除黑名单库自动更新的配置信息，在全局配置模式下，使用以下命令：
no botnet-c2-prevention block-lib auto-update
清空黑名单库文件，在任意配置模式下，使用以下命令：
clear botnet-c2-prevention blocklist lib
查看黑名单库自动更新配置信息，在任意配置模式下，使用以下命令：
show botnet-c2-prevention blocklist lib update
例如，查看从FTP服务器自动更新黑名单库的配置信息：
SG-6000# show botnet-c2-prevention blocklist lib update
Botnet blocklist lib update:
server ip: 10.182.201.11（显示FTP服务器的IP地址）
Vrouter: trust-vr（显示FTP服务器所属的VRouter）
update type: add（显示自动更新的导入模式为增量导入）
user: admin（显示登录FTP服务器的用户名）
password: $01010363$dLnWw8ijZ3zWr+5f+Ymt9iq/Bb8=（显示加密后的密码，该密码为登录FTP
服务器的用户名对应的密码）
file: /test/123.xml（显示自动更新的黑名单库文件在FTP服务器上的路径）
download mode ftp（显示从FTP服务器更新黑名单库）

<!-- 来源页 2314 -->
schedule: daily 12:34（显示自动更新的频率为每天，时间为12:34）
查看自定义白名单、自定义黑名单、导入黑名单的条目数和总容量，在任意配置模式下，使用以下命令：
show botnet-c2-prevention capacity
例如：
SG-6000# show botnet-c2-prevention capacity
Botnet allowlist and blocklist capacity:
total num: 7047/160000（显示截止当前查询时间自定义黑白名单条目总数和设备僵尸网络防御黑白名
单总容量）
custom allowlist num: 3518（显示自定义白名单条目数）
custom blocklist num: 3518（显示自定义黑名单条目数）
blocklist lib num: 11（显示导入的黑名单条目数）
云查缓存
设备连接山石云平台后，云端会不定时向设备推送域名/IP/URL地址，该数据连同未知域名云端核查的结果
一同存储在设备的“云查缓存”中，用于后续的僵尸网络防御的威胁检测。
用户可以在云查缓存中通过指定IP/域名/URL地址在云端缓存信息中查询详细结果，并参考云查结果继续执
行对应的操作。在任意模式下，使用以下命令：
show botnet-c2-prevention cache cache-information
l
cache-information - 指定需要查询的IP地址、域名或URL地址。
根据未知域名的云查结果，不同结果可执行不同的操作：
l
黑名单：当“result”为“block”时，携带该域名的流量会按照僵尸网络防御规则的配置进行处置。如
通过人工分析判断该域名为误报或流量可放行处理，可以通过配置自定义例外名单，将该条目加入到自
定义例外名单。当流量匹配到该IP地址、域名或URL时，系统将不会对该流量进行僵尸网络防御功能控
制。
l
白名单/未知：当“云查结果”为“allow”或者“grey”时，会默认对流量放行。
例如：查询域名hr.woqukaoqin.com，查询结果如下：
hostname#show botnet-c2-prevention cache hr.woqukaoqin.com
Botnet Prevention Cloud Cache Data
===================================================================

<!-- 来源页 2315 -->
name | type | | result | time | tags
------------------------------------------------------------------------------
hr.woqukaoqin.com | specific domain | | block | 0d 0h 1m 20s
===================================================================

<!-- 来源页 2316 -->
加密流量检测
加密流量是指经过加密技术处理的流量，恶意流量常采用SSL/TSL加密协议隐藏，检测难度大，易对网络安
全造成极大威胁。配置加密流量检测功能后，系统从加密流量中提取特征数据，并利用加密流量检测库中的
检测模型对其进行检测。若检测结果为异常加密流量，系统将记录威胁日志。
系统支持加密流量检测库的每日自动升级，也可以手动实时升级。
配置加密流量检测
设备的加密流量检测配置包括：
l 开启/关闭加密流量检测功能
l 启用/禁用预定义域名白名单
l 配置加密流量检测IP白名单
型号说明：
l
支持：A系列平台。
l
支持：SG-6000-K2680、K2380。
l
支持：云·界。
l
支持：B系列平台。
l
不支持：SG-6000-A7600、A6800、A2200、A2200-A、A1800、A1800-A、
A1600、A1600-A、A200、A200W、A200G4、A200WG4、A200-A、A200G4-A、
A200W-A、A200WG4-A以及A系列ASIC防火墙。
l
不支持：SG-6000-B600、B600W、B600G4、B600WG4
注意:
l
初次使用加密流量检测功能，需要首先更新加密流量检测库。关于加密流量检测库更新配置，
请参阅“加密流量检测库更新配置”。为保证能够正常连接到默认更新服务器，请在更新前为
设备配置DNS服务器。

<!-- 来源页 2317 -->
开启/关闭加密流量检测功能
开启或者关闭加密流量检测功能，需要在加密流量检测配置模式下进行。进入加密流量检测配置模式，在全
局模式下使用以下命令：
encrypted-traffic-detection
开启加密流量检测功能，在加密流量检测配置模式下，使用以下命令：
enable
在加密流量检测配置模式下，使用disable命令关闭加密流量检测功能。
启用/禁用预定义域名白名单
预定义域名白名单中包含10000个常见域名，当流量的来源是预定义域名白名单中的域名时，该流量被认为
是正常流量，不会被加密流量检测功能所检测。用户可以通过更新加密流量检测库来更新预定义域名白名
单。默认情况下，预定义域名白名单为启用状态。
禁用预定义域名白名单，在加密流量检测配置模式下，使用以下命令：
domain-allowlist-disable
在加密流量检测配置模式下，使用domain-allowlist-enable命令重新启用预定义域名白名单。
配置加密流量检测IP白名单
开启加密流量检测功能后，所有流量都会受到加密流量检测功能的检查。在实际应用中，用户可能不希望对
某些主机所发送的流量进行检查。针对这种情况，用户可以将特定的地址或地址范围（源地址或者目的地
址）添加到加密流量检测IP白名单，IP白名单支持IPv4地址和IPv6地址。白名单中的地址或地址范围不受加
密流量检测功能的检查。
配置攻击防护白名单，在加密流量检测配置模式下，使用以下命令：
allowlist [id id] {source-ip | destination-ip} {IPv4-address/M | IPv6-address/prefix }
l
id– 指定白名单条目的ID号，取值范围是1到64。如果不指定，系统将自动为其分配一个ID号。
l
source-ip | destination-ip– 指定添加到白名单中的地址类型，可以是源地址（source-ip）或者目
的地址（destination-ip）。
l
IPv4-address/M– 指定添加到白名单规则中的IPv4地址和网络掩码。
l
IPv6-address/prefix – 指定添加到白名单规则中的IPv6地址和前缀长度，取值范围为120到128。
使用no allowlist [id id] 命令删除指定的白名单规则。

<!-- 来源页 2318 -->
加密流量检测库更新配置
默认情况下，系统会每日自动更新加密流量检测库，用户可以根据需要更改加密流量检测库更新配置。加密
流量检测库更新配置包括：
l 配置加密流量检测库更新模式
l 配置更新传输协议
l 配置更新服务器
l 指定HTTP代理服务器
l 指定更新时间
l 立即更新
l 导入加密流量特征文件
l 显示加密流量检测库统计信息
l 显示加密流量检测库配置信息
配置加密流量检测库更新模式
系统支持手动和自动两种更新方式。配置加密流量检测库更新方式，在全局配置模式下，使用以下命令：
etd update mode {auto | manual}
l
auto – 指定自动加密流量检测库。该方式为系统的默认更新方式。
l
manual – 指定手动更新加密流量检测库。
在全局配置模式下使用该命令no的形式恢复默认更新模式：
no etd update mode
配置更新传输协议
系统支持通过HTTP和HTTPS对特征库进行更新，默认为HTTPS。配置加密流量检测库更新的传输协议为
HTTP，在全局配置模式下，使用以下命令：
etd update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：
no etd update protocol HTTP

<!-- 来源页 2319 -->
配置更新服务器
系统提供默认的加密流量检测库更新服务器，即update1.hillstonenet.com和
update2.hillstonenet.com，同时用户也可以根据需要配置其它更新服务器。最多可配置3个。配置更新
服务器，在全局配置模式下，使用以下命令：
etd update {server1 | server2 | server3} {ip-address | domain-name} [vrouter vrouter-name]
[src-interface src-interface-name]
l
server1 | server2 | server3– 指定将要配置的服务器，服务器支持双栈协议，可配置IPv4地址和IPv6
地址。server1的默认值为update1.hillstonenet.com，server2的默认值为
update2.hillstonenet.com。
l
ip-address | domain-name – 指定更新服务器的名称，可以是IP地址形式（ip-address）也可以是
域名形式（domain-name，例如update1.hillstonenet.com）。
l
vrouter vrouter-name - 指定更新服务器所属的VRouter。若不指定则默认是trust-vr。
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，加密流量检测库更新时将通过该源接口对更新服务器发起访问。若不指定，则默认使用管理口作为
源接口。
在全局配置模式下，使用该命令no的形式取消更新服务器的指定：
no etd update {server1 | server2 | server3}
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保加密流量检测库能够正常升级，需要在设备上指定代
理服务器的IP地址和端口号。
为加密流量检测库升级指定代理服务器，在全局配置模式下，使用如下命令：
etd update proxy-server {main | backup} ip-address port-number
l
main | backup– 使用main参数指定主代理服务器，使用backup指定备份代理服务器。
l
ip-address port-number– 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no etd update proxy-server {main | backup}命令。
指定更新时间
默认情况下，系统采用自动模式每日更新加密流量检测库，并且为避免服务器流量过大，每日更新时间是随
机的。用户可以根据需要指定加密流量检测库更新的频率和时间，在全局配置模式下，使用以下命令：

<!-- 来源页 2320 -->
etd update schedule {daily | weekly {mon | tue | wed | thu | fri | sat | sun} | monthly date}
[HH:MM]
l
daily – 指定频率为每天更新。
l
weekly {mon | tue | wed | thu | fri | sat | sun} – 指定频率为每周更新。mon | tue | wed | thu | fri
| sat | sun用来指定每周更新的日期。
l
monthly date - 指定频率为每月更新。date用来指定每月更新的日期，取值范围为1到31。如果某月
不包含所指定的日期（比如2月没有30号），则该月不会自动升级。
l
HH:MM – 指定更新的具体时间，例如09：00。
立即更新
无论更新模式为手动还是自动，用户都可以随时使用以下命令更新加密流量检测库。立即更新加密流量检测
库，在任何模式下，使用以下命令：
exec etd signature update
导入加密流量特征文件
在某些情况下，用户设备可能无法连接到更新服务器对加密流量特征库进行更新，针对这一问题，系统提供
加密流量特征文件导入功能，即通过FTP、FTPS、SFTP或者TFTP服务器将加密流量特征文件导入到设备，
从而更新设备的加密流量检测库。导入加密流量特征文件，在执行模式下，使用以下命令：
import etd signature from {{ftp server | ftps server | sftp server} ip-address [user user-name
password password] | tftp server ip-address } [vrouter vr-name] file-name
l
ip-address – 指定FTP、FTPS、SFTP或者TFTP服务器的IP地址。
l
user user-name password password– 指定FTP、FTPS、SFTP服务器的用户名和密码。
l
vrouter vr-name – 指定FTP、FTPS、SFTP或者TFTP服务器所属的VRouter。
l
file-name – 指定导入的加密流量特征文件的名称。
显示加密流量检测库信息
用户可以随时使用相应的show命令查看设备的加密流量检测库的信息，包括加密流量检测库版本、发布日
期等信息。查看加密流量检测库信息，在任何模式下使用以下命令：
show etd signature info
显示加密流量检测库更新配置信息
用户可以随时使用相应的show命令查看设备上的加密流量检测库更新信息，包括更新服务器信息、更新模
式、更新频率及时间等。查看加密流量检测库更新配置信息，在任何模式下使用以下命令：

<!-- 来源页 2321 -->
show etd signature update

<!-- 来源页 2322 -->
蜜罐诱捕
蜜罐诱捕功能介绍
山石网科智网欺骗诱捕系统，通过欺骗诱捕技术实现对攻击者流量的诱导，把攻击者引入蜜罐环境中，打乱
攻击者节奏、消耗攻击者时间、主动对抗攻击行为，为用户提供攻击捕获、攻击展示、绘制攻击者画像、攻
击回放、数据分析、溯源反制等多功能主动防御能力，力保用户最后一道防线。
系统支持蜜罐诱捕功能，将防火墙设备和山石网科智网欺骗诱捕系统（以下简称“蜜罐”或“蜜罐系统”）
进行联动，通过在防火墙设备中连接蜜罐系统并配置诱捕规则，将命中诱捕规则的攻击者IP引流到蜜罐系统
中进行封堵，避免用户的真实业务环境遭到攻击。同时，蜜罐系统会将诱捕到的攻击者信息进行威胁分析并
同步至防火墙设备进行展示，用户可按需将攻击者IP加入黑名单进行阻断。
配置蜜罐诱捕功能
配置蜜罐诱捕功能，请按照以下步骤进行操作：
1. 连接蜜罐
2. 配置诱捕规则
3. 查看蜜罐诱捕功能的相关配置信息
连接蜜罐
使用蜜罐诱捕功能前，防火墙需要与蜜罐系统（包括云蜜罐或本地蜜罐）进行连接认证，用户在连接前需要
先获取到蜜罐系统的以下信息：服务器IP地址或域名、端口号、租户ID和鉴权key。建立连接并成功认证
后，防火墙设备端会定期向蜜罐系统发送心跳报文检测连接状态。
连接蜜罐所需的配置包括以下各部分：
l 启用/禁用蜜罐诱捕功能
l 配置蜜罐系统的地址
l 配置蜜罐系统的端口号
l 配置心跳检测周期
l 配置蜜罐系统所属的虚拟路由器
l 配置蜜罐系统的租户ID
l 配置蜜罐系统的鉴权key

<!-- 来源页 2323 -->
l 配置诱捕规则的源地址
l 配置诱捕规则的伪装地址
进入蜜罐诱捕配置模式
连接蜜罐所需的配置和配置蜜罐诱捕规则均要在蜜罐诱捕配置模式下进行，进入蜜罐诱捕配置模式，在全局
配置模式下使用以下命令：
honeypot
启用/禁用蜜罐诱捕功能
默认情况下，蜜罐诱捕功能为关闭状态。启用/禁用蜜罐诱捕功能，在蜜罐诱捕配置模式下，使用以下命令：
l
启用：enable
l
禁用：disable
配置蜜罐系统的地址
配置蜜罐系统的地址，在蜜罐诱捕配置模式下，使用以下命令：
server {ip_address | ipv6_address | domain_name}
l
ip_address – 指定蜜罐系统的IPv4地址。
l
ipv6_address – 指定蜜罐系统的IPv6地址。
l
domain_name – 指定蜜罐系统的域名。范围是1到255个字符。
在蜜罐诱捕配置模式下，使用no rule命令删除已配置的蜜罐系统地址。
配置蜜罐系统的端口号
配置蜜罐系统的端口，在蜜罐诱捕配置模式下，使用以下命令：
auth-port port_number
l
port_number – 指定蜜罐系统的端口号。范围是0到65535，默认值为443。
在蜜罐诱捕配置模式下，使用no auth-port命令恢复端口号的默认值。
配置心跳检测周期
心跳检测周期用于定期检测防火墙与蜜罐系统的连接状态，在指定检测周期内，若防火墙未收到蜜罐系统返
回的心跳报文，则表示防火墙与蜜罐未连接。
配置心跳检测周期，在蜜罐诱捕配置模式下，使用以下命令：
track-interval time_value

<!-- 来源页 2324 -->
l
port_number – 指定心跳检测周期。范围是3到60秒，默认值为15秒。
在蜜罐诱捕配置模式下，使用no track-interval命令恢复心跳检测周期的默认值。
配置蜜罐系统所属的虚拟路由器
配置蜜罐系统所属的虚拟路由器，在蜜罐诱捕配置模式下，使用以下命令：
vrouter vrouter_name
l
vrouter_name – 指定蜜罐系统所属的虚拟路由器名称。
在蜜罐诱捕配置模式下，使用no vrouter命令删除已配置的虚拟路由器。
配置蜜罐系统的租户ID
配置蜜罐系统的租户ID，在蜜罐诱捕配置模式下，使用以下命令：
hf-id id_number
l
id_number – 指定蜜罐系统的租户ID。范围是1到63个字符。租户ID由蜜罐系统提供，请联系山石网科
工作人员获取。
在蜜罐诱捕配置模式下，使用no hf-id命令删除已配置的租户ID。
配置蜜罐系统的鉴权key
配置蜜罐系统的鉴权key，在蜜罐诱捕配置模式下，使用以下命令：
auth-key key_word
l
key_word – 指定蜜罐系统的鉴权key。范围是1到255个字符。鉴权key由蜜罐系统提供，请联系山石
网科工作人员获取。
在蜜罐诱捕配置模式下，使用no auth-key命令删除已配置的鉴权key。
配置诱捕规则
系统能够根据诱捕规则中配置的条件将攻击者的攻击流量引流到蜜罐的伪装业务中，从而保障真实业务的安
全。
诱捕规则的配置包括以下各部分：
l 创建诱捕规则并进入蜜罐诱捕规则配置模式
l 启用/禁用诱捕规则
l 配置诱捕规则名称

<!-- 来源页 2325 -->
l 配置蜜罐模板
l 配置诱捕规则所属的虚拟路由器
创建诱捕规则并进入蜜罐诱捕规则配置模式
配置诱捕规则前，用户需先创建诱捕规则并进入蜜罐诱捕规则配置模式。如果指定的ID或名称已存在，则直
接进入蜜罐诱捕规则配置模式。
创建诱捕规则并进入蜜罐诱捕规则配置模式，在蜜罐诱捕配置模式下，使用以下命令：
rule {id id | name name}
l
id – 指定诱捕规则的ID。范围是1到255。如果指定的ID已存在，则直接进入蜜罐诱捕规则配置模式。
l
name – 指定诱捕规则的名称。范围是1到127个字符。如果指定的名称已存在，则直接进入蜜罐诱捕规
则配置模式。
在蜜罐诱捕配置模式下，使用no rule {id id | name name}命令删除指定ID/名称的诱捕规则。
启用/禁用诱捕规则
启用/禁用诱捕规则，在蜜罐诱捕规则配置模式下，使用以下命令：
l
启用：enable
l
禁用：disable
注意: 诱捕规则创建后，默认为启用状态。
配置诱捕规则名称
配置诱捕规则名称，在蜜罐诱捕规则配置模式下，使用以下命令：
name name
l
name – 指定诱捕规则的名称。范围是1到127个字符。
在蜜罐诱捕规则配置模式下，使用no name命令删除已配置的诱捕规则名称。
配置诱捕规则的源地址
配置诱捕规则的源地址，即攻击者地址，在蜜罐诱捕规则配置模式下，使用以下命令：
src-ip {A.B.C.D/M | X:X:X:X::X/M}

<!-- 来源页 2326 -->
l
A.B.C.D/M – 指定IPv4类型的攻击者地址。
l
X:X:X:X::X/M – 指定IPv6类型的攻击者地址。
配置诱捕规则的伪装地址
当攻击者访问伪装地址时，表示命中该诱捕规则。命中诱捕规则的攻击者会被引流到蜜罐模板的伪装业务，
从而避免真实业务遭受攻击。
配置诱捕规则的伪装地址，在蜜罐诱捕规则配置模式下，使用以下命令：
disguised-ip {A.B.C.D/M | X:X:X:X::X/M}
l
A.B.C.D/M – 指定IPv4类型的伪装地址。
l
X:X:X:X::X/M – 指定IPv6类型的伪装地址。
配置蜜罐模板
防火墙与蜜罐系统建立连接后，蜜罐系统中的蜜罐模板将自动同步至防火墙，供用户选择使用。命中诱捕规
则的攻击者会被引流到蜜罐模板的伪装业务，从而避免真实业务遭受攻击。
配置蜜罐模板，在蜜罐诱捕规则配置模式下，使用以下命令：
profile id id
l
id – 指定蜜罐模板的ID。
在蜜罐诱捕规则配置模式下，使用no profile id命令删除已指定的蜜罐模板。
配置诱捕规则所属的虚拟路由器
配置虚拟路由器，在蜜罐诱捕规则配置模式下，使用以下命令：
vrouter vrouter_name
l
vrouter_name – 指定诱捕规则生效范围所属的虚拟路由器名称。如不指定，默认对全局生效。
在蜜罐诱捕规则配置模式下，使用no vrouter命令删除已配置的虚拟路由器。
查看蜜罐诱捕功能的相关配置信息
查看蜜罐诱捕功能的相关配置信息，在任意模式下，使用以下命令：
show honeypot {config | service-profiles | memory | rules}
l
config – 查看连接蜜罐的配置信息，包括启用状态、连接状态、蜜罐系统的服务器地址和端口号、租户
ID和鉴权key等。

<!-- 来源页 2327 -->
l
service-profiles – 查看蜜罐模板的配置信息，包括模板ID、模板名称、IP地址和端口号等。
l
memory – 查看蜜罐诱捕功能的内存占用情况，包括当前内存占用情况和历史最大内存占用情况等。
l
rules – 查看系统已创建的诱捕规则配置信息，包括启用状态、规则ID、规则名称、攻击者地址、伪装地
址和蜜罐模板等。

<!-- 来源页 2328 -->
重保模式
重保模式包含以下内容：
l "重保模式介绍与应用场景" 在第2326页
l "配置重保模式" 在第2326页
重保模式介绍与应用场景
国家级护网行动（HVV）及重大活动安全保障任务正逐步成为常态，特别是在每年7至8月的活动高峰期，网
络安全防护已成为各行各业不可忽视的重要议题。面对日益复杂多变的网络威胁和攻击手段，确保网络安全
稳定已成为用户最为关切的问题。为此，系统提供了重保模式，该模式通过执行最为严格的安全防护策略，
以及高频率更新的定制防护特征库，进一步强化了安全防护能力。同时，重保模式提供了简洁易用的操作方
式，使得用户能够迅速部署并启用，从而为各类活动的顺利开展以及信息安全提供了强有力的支撑和保障。
重保模式的典型应用场景包括：
l 重大活动安全保障：在重大活动期间，网络流量激增，潜在威胁也随之增加。使用“重保模式”能够显著提升防
火墙的防护效能，实施更为严密的安全策略，有效抵御各类网络攻击，确保活动期间的网络安全。
l 网络安全攻防演练：在攻防演练中，防火墙设备作为重要的防御工具，其性能和防护能力至关重要。使用“重保
模式”使防火墙能够更高效地识别和阻断各种攻击，满足用户对高检出率实战化防护的迫切需求，确保演练的顺
利成功进行。
l 高威胁网络环境应对：当网络环境面临频繁的网络攻击、恶意软件传播等高威胁情景时，使用“重保模式”能够
加强防火墙的防护力度，显著降低潜在的安全风险，确保网络环境的稳定与安全。
配置重保模式
前置条件
l 确认设备系统版本已升级至StoneOS 5.5R12及以上版本；
l 确保设备已安装病毒过滤（AV）许可证、入侵防御（IPS）许可证、云沙箱许可证、僵尸网络防御许可证；
l 确保特征库更新服务器可达。
配置重保模式
使用重保模式，可按照以下流程进行配置：

<!-- 来源页 2329 -->
1. 启用重保模式。
2. 启用全局防护模板，无需绑定策略或安全域，使用最严格的防护模板对全域进行防护。
3. 绑定威胁防护模板至全局防护模板。
4. （可选）升级特征库，及时获取到重保期间的定制威胁特征库。
5. 配置黑白名单，对恶意流量采取有效的应对措施。
开启/关闭重保模式
默认情况下，重保模式为关闭状态。开启/关闭重保模式，在全局配置模式下，使用以下命令：
l
开启：major-protect enable
l
关闭：major-protect disable
开启/关闭全局防护模板
全局防护模板是指具有最高优先级的防护规则集合。启用全局防护模板后，被指定的威胁防护规则防护机制
将自动覆盖所有安全域，无需用户进行额外的策略绑定或安全域绑定配置。相较于策略和安全域中绑定的其
他防护规则模板，全局防护模板将会优先生效。
默认情况下，全局防护模板为关闭状态。开启/关闭全局防护模板，在全局配置模式下，使用以下命令：
l
开启：major-protect profile enable
l
关闭：major-protect profile disable
绑定威胁防护模板至全局防护模板
为了更好地满足重保场景下的多样化安全需求，系统针对病毒过滤、入侵防御、僵尸网络防御、沙箱防护关
键威胁防护功能，均提供了默认的威胁防护模板“predef_emergency”，具体如下：
l
病毒过滤predef_emergency模板：全面扫描所有文件类型和协议类型，一旦发现威胁，立即执行重置
连接的防护动作；
l
入侵防御predef_emergency模板：全面启用大多数重点防护规则，对各类常见及潜在的入侵行为进行
精准监测和及时防御处置；
l
僵尸网络predef_emergency模板：监控所有协议类型，一旦发现僵尸网络活动，立即执行重置操作；
l
沙箱防护predef_emergency模板：全面检测所有文件类型和协议类型，发现恶意文件后，重置恶意链
接连接。
绑定威胁防护模板至全局防护模板，在全局配置模式下，使用以下命令：
major-protect profile {av | botnet-c2-prevention | ips | sandbox} profile-name

<!-- 来源页 2330 -->
l
av | botnet-c2-prevention | idp | sandbox – 指定威胁防护模板对应的检测引擎，包括病毒过滤
（av）、僵尸网络防御（botnet-c2-prevention）、入侵防御（ips）、沙箱防护（sandbox）。
l
profile-name – 指定绑定到全局防护模板的威胁防护模板Profile的名称。
下一步
l 更新特征库，及时获取到重保期间的定制威胁特征库。请参阅病毒特征库更新配置、入侵防御特征库更新配置、
IP信誉特征库更新配置、僵尸网络防御地址库更新配置。
l 配置黑白名单，对恶意流量采取有效的应对措施。请参阅黑名单全局配置、配置边界流量过滤黑名单库、配置IP
信誉过滤。

<!-- 来源页 2331 -->
云网协同DNS安全防御
DNS（Domain Name System，域名系统）是网络通信的关键，其安全性对于维护整个网络环境的安全至
关重要。攻击者常利用DNS的普遍存在和高流量特性来隐蔽其恶意行为，而据研究显示，高达80%的恶意软
件都使用DNS来启动命令与控制程序。鉴于此，实施有效的DNS安全检测不仅能够揭露潜在的网络威胁，也
是防止恶意软件传播和信息泄露的关键措施。
山石网科提供多种云网协同的DNS安全解决方案：
l 未知域名云端协同查询功能：与山石威胁情报云服务（云瞻）协同，借助云端海量威胁情报持续赋能，以实时云
端查询的方式核查未知风险域名的风险状态，结合僵尸网络防御功能，有效拦截互联网出口存在风险的DNS流
量。
l 云端DNS安全检测功能：与安全DNS SaaS服务进行对接，通过DoH（DNS over HTTPS）将内网出口的DNS流
量代理转发至云端进行域名解析，从而保证解析过程的完整性和机密性，同时云端也可以依托其海量威胁情报对
风险域名进行识别和拦截，有效保护内网主机安全。
未知域名云端协同查询功能
介绍
针对未包含在僵尸网络地址库、例外名单和阻断名单中的域名（即为该功能所述的“未知域名”），通过僵
尸网络防御功能出现无法管控防御的问题。
系统提供了未知域名云端协同查询功能（简称：云查），在保持原有网络部署环境下，以实时云端查询的方
式核查上述未知域名的风险状态，扩展僵尸网络防御功能的特征库，使得僵尸网络防御功能与山石威胁情报
云服务协同防御，增强对DNS流量的分析检测和恶意域名的管控能力，可在互联网出口有效拦截存在风险的
DNS流量，从而保护内网主机免受风险影响。
典型应用场景
防火墙设备作为网关部署在互联网边界出口，结合山石威胁情报云服务，将未知域名数据上送至云端进行核
查风险状态，协同僵尸网络防御功能的域名特征库分析出向DNS流量：
l 对于合规的域名请求流量，进行放行；
l 对于风险的域名请求流量，进行丢弃阻断。

<!-- 来源页 2332 -->
配置未知域名云端协同查询功能
注意: 未知域名云端协同查询（云查）功能受“僵尸网络防御许可证”控制，当“僵尸网络防御许
可证”过期后，该功能将不再生效。
开始之前：
l 阅读未知域名云端协同查询功能介绍
l 安装“僵尸网络防御许可证”
l 连接山石云平台
配置未知域名云端协同查询（云查）功能，包括以下内容：
l 开启/关闭未知域名云端协同查询
l 指定未知域名云端协同查询密钥
l 配置云查超时时间
l 查看云查缓存数据信息
l （可选）清除云查缓存数据信息
l 查看云查上送配置信息

<!-- 来源页 2333 -->
开启/关闭未知域名云端协同查询
默认情况下，该功能为关闭状态。开启/关闭未知域名云端协同查询，在云瞻配置模式下，使用以下命令：
l
开启：connect-vista enable
l
关闭：no connect-vista enable
指定未知域名云端协同查询密钥
使用“未知域名云端协同查询”功能时，需要指定密钥用于验证，云端基于输入的密钥提供可用的查询服
务，该密钥与连接云平台的山石云服务账号对应。
开始之前
请先请按照以下步骤获取密钥。
1.
点击“访问山石云瞻”，打开云瞻页面。
2.
点击页面右上角“登录”，跳转至山石云服务登录页面，使用山石云服务账号登录云平台。
3.
返回云瞻页面后，点击右上角用户名，在下拉菜单中选择“应用授权管理”。
4.
<山石云瞻授权管理>页面中展示的“API Key”即为密钥，复制使用即可。
指定未知域名云端协同查询密钥，在云瞻配置模式下，使用以下命令：
auth-token auth-token
l
auth-token - 指定获取的密钥值，密钥必须为64个字符。
在云瞻配置模式下，使用no auth-token命令删除指定的密钥值。
配置云查超时时间
开启未知域名云端协同查询功能后，系统会将僵尸网络防御功能的未知域名上传至云端进行进一步查询，再
依据核查结果对相应流量进行处置，且云端核查的结果可缓存在设备中（即云查缓存），所有云端核查结果
均用于后续的域名检测。
在上送域名查询期间，系统会暂停转发携带未知域名的报文，可暂停转发的最长时间即为云查超时时间，默
认值是500毫秒。
l
如果在云查超时时间内，云端返回了未知域名对应的风险状态，系统依据未知域名的云查结果（黑名单/
白名单/未知）执行对应的处置动作：
l
黑名单：按照僵尸网络防御规则配置的动作进行处置；
l
白名单/未知：携带未知域名的报文将被继续转发。

<!-- 来源页 2334 -->
l
如果在云查超时时间内，仍未返回云端查询结果，携带未知域名的报文将被放行处理。
开始之前
l
请先开启未知域名云端协同查询功能。
配置云查超时时间，在全局配置模式下，使用以下命令：
botnet-c2-prevention delay-time delay-time
l
delay-time - 指定云查超时时间最大值，默认值是500毫秒，范围是0-1000毫秒。
查询云查缓存数据信息
设备连接山石云平台后，云端会不定时向设备推送域名/IP/URL地址，该数据连同未知域名云端核查的结果
一同存储在设备的“云查缓存”中，用于后续的僵尸网络防御的威胁检测。
用户可以在云查缓存中通过指定IP/域名/URL地址在云端缓存信息中查询详细结果，并参考云查结果继续执
行对应的操作。在任意模式下，使用以下命令：
show botnet-c2-prevention cache cache-information
l
cache-information - 指定需要查询的IP地址、域名或URL地址。
根据未知域名的云查结果，不同结果可执行不同的操作：
l
黑名单：当“result”为“block”时，携带该域名的流量会按照僵尸网络防御规则的配置进行处置。如
通过人工分析判断该域名为误报或流量可放行处理，可以通过配置自定义例外名单，将该条目加入到自
定义例外名单。当流量匹配到该IP地址、域名或URL时，系统将不会对该流量进行僵尸网络防御功能控
制。
l
白名单/未知：当“云查结果”为“allow”或者“grey”时，会默认对流量放行。
例如：查询域名hr.woqukaoqin.com，查询结果如下：
hostname#show botnet-c2-prevention cache hr.woqukaoqin.com
Botnet Prevention Cloud Cache Data
===================================================================
name | type | | result | time | tags
------------------------------------------------------------------------------
hr.woqukaoqin.com | specific domain | | block | 0d 0h 1m 20s
===================================================================

<!-- 来源页 2335 -->
清除云查缓存数据信息
当设备重启后，云查缓存数据会自动清除。在某些使用场景下，例如需要释放设备内存或者当流量切换后，
如根据需要即刻清除当前设备中存储的所有云查缓存结果，在任意模式下，使用以下命令：
clear botnet-c2-prevention cache-data
查看云查上送配置信息
查看云查上送配置信息，在任意模式下，使用以下命令：
show botnet-c2-prevention cloud-search-config
云端DNS安全检测功能
介绍
传统DNS解析过程中，报文会通过不加密的DNS协议（例如UDP协议）直接进行传输，攻击者通常会利用中
间人手段篡改DNS流量，给企业组织带来严重的安全威胁。
系统提供了云端DNS安全监测功能，在保持原有网络部署环境的前提下，与安全DNS SaaS服务进行对接，
将内网出口的DNS流量使用DoH（DNS over HTTPS）代理转发至云端进行域名解析，从而保证解析过程的
完整性和机密性。同时，云端也可以依托其海量威胁情报对风险域名或IP进行识别和拦截，有效保护内网主
机安全。
典型应用场景
防火墙作为网关部署在互联网边界出口，与安全DNS SaaS服务进行对接后，将内网的DNS流量代理通过
DoH机密转发至云端。云端在进行域名解析的同时，借助海量威胁情报对风险域名或IP进行识别和拦截，将
合规的DNS响应报文返回给防火墙，将恶意域名进行丢弃。

<!-- 来源页 2336 -->
配置云端DNS安全检测功能
开始之前
l 阅读云端DNS安全检测功能介绍
l 前往sdns.360.cn申请云端安全DNS SaaS服务
配置云端DNS安全检测功能，包括以下内容：
l 开启/关闭云端DNS安全检测功能
l 进入指定服务商的Secure-DNS Profile配置模式
l 配置DoH服务器
l 开启/关闭发送客户端地址功能
l 配置健康检查周期
l 开启/关闭生成日志功能
l 查看云端DNS安全检测配置信息
开启/关闭云端DNS安全检测功能
默认情况下，云端DNS安全检测功能为关闭状态。开启云端DNS安全检测功能并指定DoH服务器厂商，在全
局配置模式下，使用以下命令：
secure-dns enable service-provider provider-name

<!-- 来源页 2337 -->
l
provider-name – 指定DoH服务器的厂商名称，目前仅支持360。
关闭云端DNS安全检测功能，在全局配置模式下，使用以下命令：
secure-dns disable
进入指定服务商的Secure-DNS Profile配置模式
配置云端DNS安全检测功能需要在指定服务商的Secure-DNS Profile配置模式下进行。进入指定服务商的
Secure-DNS Profile配置模式，在全局配置模式下，使用以下命令：
secure-dns profile service-provider provider-name
l
provider-name – 指定DoH服务器的厂商名称，目前仅支持360。
配置DoH服务器
配置DoH服务器的域名或IP地址，以及所属虚拟路由器，在指定服务商的Secure-DNS Profile配置模式
下，使用以下命令：
doh-server {domain | ip-address} [vrouter vr-name]
l
domain | ip-address – 指定DoH服务器的域名或IP地址，默认为doh.360.cn。
l
vr-name – 指定DoH服务器所属的虚拟路由器，默认为trust-vr。
在Secure-DNS Profile配置模式下，使用no doh-server命令恢复默认配置。
开启/关闭发送客户端地址功能
开启该功能后，用户通过DNS代理发起域名解析请求时，系统会将客户端IP地址上送至云端进行运维。默认
情况下，该功能为关闭状态。
开启/关闭发送客户端地址功能，在指定服务商的Secure-DNS Profile配置模式下，使用以下命令：
l
开启：send-client-ip enable
l
关闭：send-client-ip disable
配置健康检查周期
为避免由于DoH服务器出现异常，导致使用DoH协议解析域名失败的情况，系统支持定期向DoH服务器发送
DNS健康检测报文。当连续两次健康检测失败时，系统会将云端DNS安全检测功能切换至Inactive状态；处
于Inactive状态时，无法通过云端DNS安全检测功能使用DoH协议解析域名，但系统依然会定期发送健康检
测报文，一旦检测成功，立即切换为Active状态。
配置健康检查周期，在指定服务商的Secure-DNS Profile配置模式下，使用以下命令：
track-interval time-value

<!-- 来源页 2338 -->
l
time-value – 指定向DoH服务器发送DNS健康检测报文的时间间隔，范围是3-60秒，默认值是10秒。
在Secure-DNS Profile配置模式下，使用no track-interval命令恢复默认配置。
开启/关闭生成日志功能
开启该功能后，用户通过DNS代理请求具有威胁域名的解析时，将生成相应的威胁日志。默认情况下，该功
能为关闭状态。
开启/关闭生成日志功能，在指定服务商的Secure-DNS Profile配置模式下，使用以下命令：
l
开启：threat-log enable
l
关闭：threat-log disable
查看云端DNS安全检测配置信息
查看云端DNS安全检测功能的配置信息，在任意模式下，使用以下命令：
show secure-dns
以下是返回结果示例：
hostname(config)# show secure-dns
================================================================
Secure DNS: Enable（云端DNS安全检测功能已开启）
Service provider: 360（云端DNS安全检测功能提供厂商）
Service status: Active（云端DNS安全检测功能为可用状态）
------------------------------------------------------------------------------------------------
----------------------------------------
Profile 360:
Bootstrap server: 101.198.198.198 101.198.199.200（内置的360公网DoH服务器，用于解析DoH
服务器域名）
DoH server domain: hxr5.n.360.net（指定的DoH服务器域名）
DoH server IP: 36.110.234.252, TTL 241 s（通过Bootstrap解析出来的DoH服务器IP地址）
DoH server vrouter: trust-vr（指定DoH服务器所属的VRouter）
Send-client-addr: Enable（发送客户端地址功能开启状态）
Threat-log: Enable（生成日志功能开启状态）
Track interval: 10 s（健康检查周期）

<!-- 来源页 2339 -->
================================================================

<!-- 来源页 2340 -->
企业IT设备和IoT设备统一管理
随着数字化转型的深入，中小型企业的网络环境日益复杂，接入设备从传统IT 终端扩展到大量物联网
（IoT）设备。防火墙作为网络安全的核心基础设施，不再局限于边界防护，更承担着设备管理、资产可视化
的重要角色。随着企业内部IT设备、IoT设备的不断增多，带来的设备被威胁攻击、被僵尸网络控制、数据泄
露等一系列安全隐患问题。
l IT设备：IT设备指企业用于构建数字化基础设施的信息技术设备，涵盖数据处理、网络通信及业务应用的核心硬
件与软件系统，主要包括服务器、办公计算机、网络交换设备、存储系统及移动终端等。这类设备通常运行标准
化操作系统（如Windows、Linux），支持企业级协议（如SNMP、SSH），承载关键业务应用（ERP、数据库
等），并可通过集中管理工具实现安全策略部署、性能监控及漏洞修复，是支撑企业信息化运作与数据资产管理
的核心载体。
l IoT设备：物联网（Internet of Things）简称为IoT，是指将物理设备（例如网络视频监控设备、办公设备、生
产设备、楼宇设备等）实现互联互通的网络，可进行信息交换以实现智能化识别和管理。物联网技术在大中型企
业中已经应用的非常广泛，通常在大中型企业的园区物联网中包含大量各种类型的IoT设备，例如视频监控设
备、门禁系统、打卡机、人脸识别系统设备、电视、IP电话等。
型号说明：
l
目前支持识别以下厂商的IoT设备：海康威视、大华、宇视科技、格林威尔、世邦、联想、
天地伟业、霍尼韦尔、景阳、捷顺科技、江森自控、佳能、惠普、精工爱普生、三星、小
米、华为、JVC研诺、网路公司、苹果、沃科、工业富联、施耐德、山石网科等。
系统提供整体的设备管理功能，可实现对于企业内部设备的识别、安全管控和威胁治理，能够满足对企业设
备的安全保护、保护设备免受攻击、保障数据隐私等安全需求。
设备管理功能，包含以下5部分内容：
l 设备发现：系统支持通过安全域绑定设备发现规则，发现设备地址。
l 设备识别：发现设备后，系统支持通过基于流量的被动识别、云端设备识别服务识别、本地设备识别模块识别
（包括在设备系统Docker中部署设备识别系统和在虚拟机中部署设备识别系统）这三种方式识别网络内各类型的
设备信息，包括设备类型、厂商、型号等信息。
l 设备管理：对于识别出的设备进行实时监控，结合设备列表，对设备进行统一的管理。

<!-- 来源页 2341 -->
l 策略管控：支持配置基于设备分类的策略规则，通过分析流经设备的流量，根据设备的属性自动将其IP映射至设
备分类，实现安全策略自动、动态地管控设备的网络权限。
l 威胁治理：结合系统中的威胁防护功能、数据安全功能，对发现安全问题的设备，可进行相应的威胁治理。

<!-- 来源页 2342 -->
设备管理功能使用限制及注意事项
型号支持
型号说明：
l
不支持：SD-WAN系列平台。
注意事项
注意:
l
设备管理的云端设备识别功能、本地设备识别功能和IoT设备指纹库受许可证控制，请在使用功
能前先确认当前设备系统是否支持设备管理功能，并为设备安装IoT管控许可证，功能才可正常
使用。
l
云端设备识别与本地设备识别功能互斥，无法同时使用。
l
设备管理功能不支持识别处于NAT场景下的设备。
l
在使用设备管理功能的部署环境中，设备的DHCP流量需要经过防火墙设备或者将流量镜像到
防火墙设备。

<!-- 来源页 2343 -->
设备管理功能配置流程
使用设备管理功能，完整的配置流程如下，可依次完成以下配置：
注意: 设备管理的云端设备识别功能、本地设备识别功能和IoT设备指纹库受许可证控制，请在使用
功能前先确认当前设备系统是否支持设备管理功能，并为设备安装IoT管控许可证，功能才可正常
使用。
1. 更新IoT设备指纹库
a. 更新"设备指纹库" 在第2343页——升级IoT设备指纹库，提升识别IT设备和IoT设备信息的能力。
2. 设备发现
a. 配置设备发现规则——指定需要发现的设备的地址规则，为系统发现设备做好准备。
b. 配置安全域的设备发现功能——安全域下开启“设备发现”功能并且绑定设备发现规则，用于发现设备。
3. 选择设备识别方式，配置相关功能：
a. 云端设备识别：
1. 连接山石云平台并开启云景服务，完成与云平台服务器对接配置。
2. 开启云端设备识别功能
3. 配置校正后设备信息报文上送云端功能（可选）
b. 本地资产识别：
本地资产识别——内置Docker：
注意：仅支持A系列A2600及以上型号（A2600- A3810型号需要必配硬盘、A5100及以上型号可选配硬
盘）、B系列B3200及以上型号（需要必配硬盘）、云·界设备支持内置Docker识别方式。
1. 配置Docker——将资产识别系统部署到设备系统中。
2. 开启本地设备识别功能
3. 配置本地设备识别功能
本地资产识别——外置Docker：
l 在虚拟机中部署资产识别系统
c. 基于流量的被动识别：升级共享接入特征库，提升识别IT设备和IoT设备信息的能力。系统内置基于流量的
被动识别功能，无需用户手动配置即可自动启用。

<!-- 来源页 2344 -->
4. 设备管理
a. 配置区域——配置设备IP地址/IP范围与区域的对应关系，系统发现设备后，根据已配置的设备区域确定设
备的部署区域。
b. 设备自动同步到资产列表——开启自动同步设备至资产列表功能，将发现的设备或识别到对应设备类型的
设备自动同步到资产列表。
c. 设备监控——查看所有识别的设备的概览信息（TOP10厂商、TOP类型、TOP在线设备）以及设备列表信
息。在设备列表中可以查看设备的厂商、设备类型、型号、部署区域等信息，还可以校正设备信息以及将
设备添加到资产列表中。
d. 查看设备日志——当设备的在线/离线状态、厂商、设备类型等设备信息发生变化时，系统会生成相应的
设备日志。
5. 设备的策略管控
a. 配置设备分类——为设备指定归类维度，例如厂商、类型、设备型号、操作系统等，系统即可将识别的设
备信息与设备分类进行相应的映射。
b. 配置策略规则——在策略规则中配置源设备和目的设备，系统会通过策略规则对流量中的设备进行匹配过
滤。
6. 威胁治理
a. 结合威胁防护功能、数据安全功能，对发现安全问题的设备，可进行相应的威胁治理。
b. 配置数据上送智源——上送设备数据至智源，通过智源可实现进一步的资产管理、下发策略/阻断等威胁
事件响应处置。
c. 配置设备数据上送山石云平台——上送设备报表数据、设备列表数据至山石云平台，进行统一的分析统计
和管控。

<!-- 来源页 2345 -->
设备指纹库
IoT设备指纹库介绍
IoT设备指纹库是识别各类IT设备和IoT设备的关键，其持续更新的能力保证了识别准确性的不断提升。目
前，IoT设备指纹库支持在线更新和本地更新两种方式。Hillstone提供两个默认设备指纹库更新服务器，分
别是https://update1.hillstonenet.com和https://update2.hillstonenet.com。用户可以根据需要
更改设备指纹库更新配置。
注意: 非根VSYS不支持IoT设备指纹库更新。
IoT设备指纹库更新配置
IoT设备指纹库更新配置包括：
l 配置IoT设备指纹库更新模式
l 配置更新传输协议
l 配置更新服务器
l 指定HTTP代理服务器
l 指定更新时间
l 立即更新
l 导入IoT设备指纹库文件
l 显示IoT设备指纹库信息
l 显示IoT设备指纹库更新配置信息
配置IoT设备指纹库更新模式
系统支持手动和自动两种更新方式。配置IoT设备指纹库更新方式，在全局配置模式下，使用以下命令：
iot update mode {auto | manual}
l
auto – 指定自动更新IoT设备指纹库。该方式为系统的默认更新方式。
l
manual – 指定手动更新IoT设备指纹库。
在全局配置模式下使用该命令no的形式恢复默认更新模式：
no iot update mode

<!-- 来源页 2346 -->
配置更新传输协议
系统支持通过HTTP和HTTPS对IoT设备指纹库进行更新，默认为HTTPS。配置IoT设备指纹库更新的传输协
议为HTTP，在全局配置模式下，使用以下命令：
iot update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：
no iot update protocol HTTP
配置更新服务器
系统提供默认的IoT设备指纹库更新服务器，即update1.hillstonenet.com和
update2.hillstonenet.com，同时用户也可以根据需要配置其它更新服务器下载最新IoT设备指纹库。最
多可配置3个。配置更新服务器，在全局配置模式下，使用以下命令：
iot update {server1 | server2 | server3} {ip-address | domain-name} [vrouter vrouter-name]
[src-interface src-interface-name]
l
server1 | server2 | server3 – 指定将要配置的服务器，服务器支持双栈协议，可配置IPv4地址和IPv6
地址。server1的默认值为update1.hillstonenet.com，server2的默认值为
update2.hillstonenet.com。
l
ip-address | domain-name – 指定更新服务器的名称，可以是IP地址形式（ip-address）也可以是
域名形式（domain-name，例如update1.hillstonenet.com）。
l
vrouter vrouter-name - 指定更新服务器所属的VRouter。若不指定则默认是trust-vr。
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，IoT设备指纹库更新时将通过该源接口对更新服务器发起访问。若不指定，则默认使用管理口作为源
接口。
在全局配置模式下，使用该命令no的形式取消更新服务器的指定：
no iot update {server1 | server2 | server3}
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保IoT设备指纹库能够正常升级，需要在设备上指定代
理服务器的IP地址和端口号。
为IoT设备指纹库升级指定代理服务器，在全局配置模式下，使用如下命令：
iot update proxy-server {main | backup} ip-address port-number

<!-- 来源页 2347 -->
l
proxy-server {main | backup} – 使用main参数指定主代理服务器，使用backup指定备份代理服务
器。
l
ip-address port-number – 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no iot update proxy-server {main | backup}命令。
指定更新时间
默认情况下，系统采用自动模式每日更新IoT设备指纹库，并且为避免服务器流量过大，每日更新时间是随机
的。用户可以根据需要指定IoT设备指纹库更新的频率和时间，在全局配置模式下，使用以下命令：
iot update schedule {daily | weekly {mon | tue | wed | thu | fri | sat | sun} | monthly date}
[HH:MM]
l
daily – 指定频率为每天更新。
l
weekly {mon | tue | wed | thu | fri | sat | sun} – 指定频率为每周更新。mon | tue | wed | thu | fri
| sat | sun用来指定每周更新的日期。
l
monthly date - 指定频率为每月更新。date用来指定每月更新的日期，取值范围为1到31。如果某月
不包含所指定的日期（比如2月没有30号），则该月不会自动升级。
l
HH:MM – 指定更新的时间，例如09：00。
立即更新
无论更新模式为手动还是自动，用户都可以随时使用以下命令更新IoT设备指纹库。立即更新IoT设备指纹
库，在任何模式下，使用以下命令：
exec iot update [full]
l
exec iot update – 仅对当前IoT设备指纹库与更新服务器最新发布IoT设备指纹库的不同部分进行更
新。
l
full – 强制升级当前IoT设备指纹库。
导入IoT设备指纹库文件
在某些情况下，用户设备可能无法连接到更新服务器对IoT设备指纹库进行更新，针对这一问题，系统提供
IoT设备指纹库文件导入功能，即通过FTP、FTPS、SFTP、TFTP服务器将IoT设备指纹库文件导入到设备，
从而更新设备的IoT设备指纹库。导入IoT设备指纹库文件，在执行模式下，使用以下命令：
import iot signature from {{ftp | ftps |sftp} server A.B.C.D | X:X:X:X::X user user-name
password password[vrouter vrouter-name] | tftp serverip-address [vroutervrouter-name]}
file-name

<!-- 来源页 2348 -->
l
ftp | ftps |sftp - 指定服务器的类型。
l
A.B.C.D | X:X:X:X::X – 指定FTP、FTPS、SFTP或者TFTP服务器的IP地址。
l
user user-name password password – 指定FTP/FTPS/SFTP服务器的用户名和密码。
l
vrouter vrouter-name – 指定FTP、FTPS、SFTP或者TFTP服务器所属的VRouter。默认为trustvr。
l
file-name – 指定导入的IoT设备指纹库文件的名称。
显示IoT设备指纹库信息
用户可以随时使用相应的show命令查看设备的IoT设备指纹库信息，包括IoT设备指纹库版本、发布日期
等。查看IoT设备指纹库信息，在任何模式下使用以下命令：
show iot info
例如：
hostname# show iot info
Signature vendor: Hillstone Networks（显示IoT设备指纹库所属公司。）
Current version: 1.0.72（显示IoT设备指纹库的当前版本。）
Release date: 2024/08/27 11:05:40（显示IoT设备指纹库的发布日期。）
显示IoT设备指纹库更新配置信息
用户可以随时使用相应的show命令查看设备上的IoT设备指纹库更新信息，包括更新服务器信息、更新模
式、更新频率及时间以及IoT设备指纹库更新状况等。查看IoT设备指纹库更新配置信息，在任何模式下使用
以下命令：
show iot update
例如：
hostname# show iot update
IoT signature update options:
protocol: HTTPS（显示IoT设备指纹库更新的传输协议为HTTPS。）
server1: 10.XX.XX.100, 443, trust-vr（显示IoT设备指纹库更新服务器信息。）
server2: 10.XX.XX.100, 443, trust-vr
server3:
proxy server status: disable（显示未指定代理服务器。）

<!-- 来源页 2349 -->
main proxy server:
backup proxy server:
mode: auto（显示IoT设备指纹库更新模式为自动更新模式。）
schedule: daily 01:25（显示自动更新频率和时间。）
current status: normal（显示IoT设备指纹库的更新状态为正常。）
last update result: latest signature, needn't update（显示IoT设备指纹库最近一次更新的结
果。）
last update time: Tue Sep 10 01:25:59 2024（显示IoT设备指纹库最近一次更新时间。）

<!-- 来源页 2350 -->
设备发现
系统支持配置IP、MAC或IP/MAC类型的设备发现规则。对于开启设备发现功能且绑定设备发现规则的安全
域，系统可以对安全域下的流量进行设备发现。
当同时配置IP/MAC、IP和MAC类型的设备发现规则时，流量匹配的顺序为：IP/MAC > IP > MAC。
注意: 不同平台最多允许配置/导入的设备发现规则总数而不同，同时，允许添加至设备发现规则的
IP/MAC、IP和MAC类型地址个数也不同，请以实际为准。例如，当前设备最多允许配置/导入
1500个设备发现规则，那么最多允许添加至设备发现规则的IP/MAC、IP和MAC类型地址的比例
为：2:1:2，即IP/MAC类型最多600个、IP类型最多300个，MAC类型最多600个。
配置设备发现规则
创建设备发现规则
创建设备发现规则，并且进入设备发现规则配置模式，在全局配置模式下，使用以下命令：
device discover-rule rule-name
l
rule-name - 指定设备发现规则的名称，并且进入设备发现规则配置模式。如果指定名称已存在，则直
接进入设备发现规则配置模式。
在全局配置模式下，使用no device discover-rule rule-name删除指定的设备发现规则。
注意: 被绑定到安全域的设备发现规则只有在解除绑定后，才可以进行删除。
配置IP/MAC类型的设备发现规则条目
配置IP-MAC类型的设备发现规则条目
将设备的IPv4地址、MAC地址、用户名和密码添加到设备发现规则中，在设备发现规则配置模式下，使用以
下命令：
ip-mac ipv4-address mac-address [username username password password] [sync-toasset]
l
ipv4-address - 指定设备的IPv4地址。
l
mac-address - 指定与配置的IPv4地址对应的MAC地址。
l
username - 指定管理设备的用户名。

<!-- 来源页 2351 -->
l
password - 指定与用户名对应的密码。
l
sync-to-asset - 指定将发现的设备自动同步到资产列表。
在设备发现规则配置模式下，使用no ip-macipv4-address mac-address从设备发现规则中删除指定设
备的IPv4地址和MAC地址。
将允许通过的设备的IPv6地址、MAC地址、用户名和密码添加到设备发现规则中，在设备发现规则配置模式
下，使用以下命令：
ipv6-mac ipv6-address mac-address [username username password password] [sync-toasset]
l
ipv6-address - 指定设备的IPv6地址。
l
mac-address - 指定与配置的IPv6地址对应的MAC地址。
l
username - 指定管理设备的用户名。
l
password - 指定与用户名对应的密码。
l
sync-to-asset - 指定将发现的设备自动同步到资产列表。
在设备发现规则配置模式下，使用no ipv6-mac ipv6-address mac-address从设备发现规则中删除指定
设备的IPv6地址和MAC地址。
配置IP类型的设备发现规则条目
指定IP网段
将允许通过的设备所在IPv4网段、用户名和密码添加到设备发现规则中，在设备发现规则配置模式下，使用
以下命令：
ip network {ip-prefix/mask | ip-address mask} [username username password password]
[sync-to-asset]
l
ip-prefix/mask - 指定设备所在网段的IP地址和子网掩码，如1.1.1.1/24。
l
ip-address - 指定设备所在网段的IP地址，如1.1.1.1。
l
mask - 指定设备所在网段的网络掩码，如255.255.255.0。
l
username - 指定管理设备的用户名。
l
password - 指定与用户名对应的密码。
l
sync-to-asset - 指定将发现的设备自动同步到资产列表。

<!-- 来源页 2352 -->
在设备发现规则配置模式下，使用no ip network {ip-prefix/mask | ip-address mask}从设备发现规则
中删除指定设备所在的IPv4网段。
将允许通过的设备所在IPv6网段添加到设备发现规则中，在设备发现规则配置模式下，使用以下命令：
ipv6 prefix {ipv6-prefix / prefix-length} [username username password password] [sync-toasset]
l
ipv6-prefix / prefix-length –指定IPv6前缀以及前缀长度。取值范围为1到128。
l
username - 指定管理设备的用户名。
l
password - 指定与用户名对应的密码。
l
sync-to-asset - 指定将发现的设备自动同步到资产列表。
在设备发现规则配置模式下，使用no ipv6 prefix ipv6-prefix / prefix-length命令从设备发现规则中删
除指定设备所在的IPv6网段。
注意: 当配置的IP网段与已配置IP地址存在冲突时，系统会出现错误提示。
指定IP地址范围
将允许通过的设备所在IPv4地址范围、用户名和密码添加到设备发现规则中，在设备发现规则配置模式下，
使用以下命令：
ip range start-ip end-ip [username username password password] [sync-to-asset]
l
start-ip - 指定设备所在IP地址范围的起始IP地址。
l
end-ip - 指定设备所在IP地址范围的结束IP地址。
l
username - 指定管理设备的用户名。
l
password - 指定与用户名对应的密码。
l
sync-to-asset - 指定将发现的设备自动同步到资产列表。
在设备发现规则配置模式下，使用no ip rangestart-ip end-ip从设备发现规则中删除指定设备所在的
IPv4地址范围。
将允许通过的设备所在IPv6地址范围添加到设备发现规则中，在设备发现规则配置模式下，使用以下命令：
ipv6 range min-ipv6-address max-ipv6-address [username username password password]
[sync-to-asset]
l
min-ipv6-address – 指定IPv6地址范围的最小地址。
l
max-ipv6-address – 指定IPv6地址范围的最大地址。

<!-- 来源页 2353 -->
l
username - 指定管理设备的用户名。
l
password - 指定与用户名对应的密码。
l
sync-to-asset - 指定将发现的设备自动同步到资产列表。
在设备发现规则配置模式下，使用no ipv6 range min-ipv6-address max-ipv6-address从设备发现规
则中删除指定设备所在的IPv6地址范围。
注意: 当配置的IP范围与已配置IP地址存在冲突时，系统会出现错误提示。
配置MAC类型的设备发现规则条目
将允许通过的设备的MAC地址添加到设备发现规则中，在设备发现规则配置模式下，使用以下命令：
mac mac-address [sync-to-asset]
l
mac-address- 指定设备的MAC地址。
l
sync-to-asset - 指定将发现的设备自动同步到资产列表。
在设备发现规则配置模式下，使用no mac mac-address [sync-to-asset]从设备发现规则中删除指定设
备的MAC地址。
注意: 系统最多允许添加600个MAC地址至设备发现规则。
导入设备发现规则
用户可以通过FTP、TFTP、FTPS或SFTP服务器导入设备发现规则。从FTP、TFTP、FTPS或SFTP服务器导
入设备发现规则，在执行模式下使用以下命令：
import device discover-rule rule-name from {ftp server ip-address user user-name
password password [vrouter vrouter-name] | tftp server ip-address [vrouter vrouter-name] |
ftps server ip-address user user-name password password [vrouter vrouter-name] | sftp
server ip-address user user-name password password [vrouter vrouter-name]} file-name
l
rule-name- 指定导入的设备发现规则的名称。
l
ip-address- 指定FTP、TFTP、FTPS或SFTP服务器的IP地址。
l
user user-name password password - 指定FTP、FTPS或SFTP服务器的用户名和密码。
l
vrouter-name - 为指定的VRouter导入设备发现规则。如果不指定该参数，VRouter为trust-vr。
l
file-name - 指定FTP、TFTP、FTPS或SFTP服务器上设备发现规则文件的名称。

<!-- 来源页 2354 -->
显示设备发现规则信息
显示设备发现规则信息，在任何模式下，使用以下命令：
show device discover-rule rule-name [ip-entry | ip-mac-entrty | mac-entry]
l
rule-name - 显示指定名称的所有设备发现规则信息。
l
ip-entry - 显示IP类型的设备发现规则信息。
l
ip-mac-entrty - 显示IP/MAC类型的设备发现规则信息。
l
mac-entrty - 显示MAC类型的设备发现规则信息
配置安全域的设备发现功能
系统支持对安全域流量进行基于设备发现规则的设备发现，用户需要按照以下步骤进行操作：
1. 配置设备发现规则。
2. 开启安全域的设备发现功能，并绑定已创建的设备发现规则。
3. 开启引用流量中的MAC地址功能。（可选）
绑定设备发现规则到安全域和引用流量中的MAC地址功能，均需要在域配置模式下进行，在配置前请在全局
配置模式下，输入以下命令进入域配置模式：
zone zone-name
绑定设备发现规则到安全域
将已创建的设备发现规则绑定到安全域后，系统将会对经过安全域的流量根据设备发现规则进行设备发现。
在域配置模式下，使用以下命令将设备发现规则绑定到安全域：
device-discover enable name
l
name - 指定需要绑定到安全域的设备发现规则名称。一个安全域仅允许绑定一个设备发现规则。
在域配置模式下，使用该命令no的形式解除绑定设备发现规则到安全域：
no device-discover enable
开启/关闭引用流量中的MAC地址功能
由于从安全域流量中获取的MAC地址可能不是真实的设备MAC地址，有可能会造成设备的误发现。因此，引
用流量中的MAC地址功能是默认关闭的。如果用户在确信安全域流量中的MAC地址具有参考价值时（例如，
在二层网络直连部署的情况下），可以开启引用流量中的MAC地址功能，利用安全域流量分析获取的MAC地
址进行设备发现。
在域配置模式下，使用以下命令开启或关闭引用流量中的MAC地址功能。

<!-- 来源页 2355 -->
l
开启：device-discover mac-import
l
关闭：no device-discover mac-import

<!-- 来源页 2356 -->
设备识别
发现设备后，系统能够通过基于流量的被动识别、云端设备识别服务识别、本地设备识别模块识别（包括在
设备系统Docker中部署设备识别系统和在虚拟机中部署设备识别系统）这三种方式识别网络内各类型的设备
信息，包括设备类型、厂商、型号等信息。
系统内置基于流量的被动识别功能，无需用户手动配置即可自动启用。此外，用户可根据实际需求，灵活选
择启用云端设备识别或本地设备识别功能，进一步提升设备识别的准确性与效率。云端设备识别与本地设备
识别功能互斥，同一时间仅支持其中一种识别模式生效，以避免功能冲突。
设备识别典型部署场景
当系统通过设备发现规则发现设备时，需要通过设备识别功能，进一步识别出设备的厂商、设备类型、型号
等信息。
根据设备信息的识别方式的不同，典型的设备识别方式包含以下三种：
l 云端设备识别：通过云端设备识别服务识别设备信息。
l 本地设备识别：通过本地设备识别模块识别设备信息，分为内置和外置两种方式：
l 内置：使用防火墙系统的Docker管理功能，将资产识别系统部署在防火墙内部进行识别。
l 外置：在虚拟机上安装设备识别程序，使用部署在虚拟机中的设备识别系统识别。
l 基于流量的被动识别：系统可以对流经防火墙的流量，通过共享接入特征库识别设备详细信息。
型号说明：
本地资产识别的内置方式：
l
支持：A系列A2600及以上型号（A2600- A3810型号需要必配硬盘、A5100及以上型号
可选配硬盘）。
l
支持：B系列B3200及以上型号（需要必配硬盘）。
l
支持：云·界。
以下以识别IoT设备为例，介绍云端设备识别和本地设备识别两种部署场景。
云端设备识别典型部署
如下图所示，企业内部物联网中包含大量各种类型的IoT设备，例如视频监控设备、门禁系统、办公电脑、IP
电话、手机、对讲机等，企业中已部署防火墙（NGFW），将防火墙连接至山石云平台（山石云景），防火
墙系统从经过设备的流量中提取IoT设备指纹信息并上送至云端与山石云景交互，再使用山石云景提供的云端

<!-- 来源页 2357 -->
设备识别服务识别IoT设备详细信息，配合防火墙的设备管理功能，实现安全管控。同时，还部署了安全管理
平台（HSM）、安全运营平台（山石智源）等运维管理设备，可上送IoT设备数据信息进行进一步的安全管
控和威胁治理等。
本地设备识别典型部署
内置设备识别
如下图所示，企业内部物联网中包含大量各种类型的IoT设备，例如视频监控设备、门禁系统、办公电脑、IP
电话、手机、对讲机等。企业中已部署防火墙（NGFW），使用防火墙Docker管理功能将设备识别系统部署
到系统中，从而来识别IoT设备信息，配合防火墙的设备管理功能，实现安全管控。同时，还部署了安全管理
平台（HSM）、安全运营平台（山石智源）等运维管理设备，可上送IoT设备数据信息进行进一步的安全管
控和威胁治理等。

<!-- 来源页 2358 -->
外置设备识别
如下图所示，企业内部物联网中包含大量各种类型的IoT设备，例如视频监控设备、门禁系统、办公电脑、IP
电话、手机、对讲机等。企业中已部署防火墙（NGFW），并且在虚拟服务器上安装部署了设备识别系统，
来识别IoT设备信息，配合防火墙的设备管理功能，实现安全管控。同时，还部署了安全管理平台
（HSM）、安全运营平台（山石智源）等运维管理设备，可上送IoT设备信息进行进一步的安全管控和威胁
治理等。
部署设备识别系统到虚拟机
在使用外置本地设备识别方式时，用户可将设备识别系统部署到虚拟机中。
本章节介绍如何将设备识别系统部署到不同的环境中，包括VMware和OpenStack中。部署之前，根据不同
的部署场景，用户需要相应地熟悉VMware、OpenStack的组件及使用。
l 在VMware ESXi上部署设备识别系统
l 在OpenStack上部署设备识别系统
在VMware ESXi上部署设备识别系统
用户可以通过导入OVF+VMDK文件的方式将设备识别系统部署在任意一台支持VMware ESXi 虚拟机的X86
设备上。部署完成后，后续用户可使用通过Update Server自动更新识别引擎版本。
开始之前
在VMware ESXi服务器上部署设备识别系统，在开始之前请做到：

<!-- 来源页 2359 -->
l 要求您必须已经熟悉VMware的vSphere Hypervisor 架构、ESXi主机设置、VMware虚拟机部署等知识。
l 按照系统要求和限制准备好虚拟机环境，并设置好ESXi Server主机。
l 联系山石网科客服人员获取安装文件ZIP格式压缩包（包含ovf、vmdk、iso以及mf文件），解压后保存ovf、
vmdk文件至本地。
系统要求和限制
设备识别系统的使用要求和限制：
l VMware ESXi 的版本为7.0及以上。
l 虚拟机至少需要4个vCPU、4GB内存、20GB硬盘空间，并已安装网卡。
部署步骤
以下步骤示例使用的是VMware ESXi 7.0版本，供参考。
步骤一：访问登录VMware ESXi 平台
访问VMware ESXi 7.0平台，输入用户名和密码，点击“登录”。
第二步：创建虚拟机
1. 登录VMware ESXi 7.0平台后，点击左侧“虚拟机”节点，然后在右侧页面中点击“创建/注册虚拟机”。

<!-- 来源页 2360 -->
2. 选择创建的虚拟机类型。在<新建虚拟机>对话框中，点击“1 选择创建类型> 从OVF或OVA文件部署虚拟机”，
然后点击“下一页”。
3. 为要部署的虚拟机选择OVF+VMDK文件。输入虚拟机名称后，选择OVF+VMDK文件或直接将文件拖动至提示位
置，然后点击“下一页”。

<!-- 来源页 2361 -->
4. 选择存储类型和设备识别系统安装的硬盘位置，然后点击“下一页”。
注意：需选择大小在20G以上的硬盘。
5. 配置部署选项，根据网络环境选择“网络映射”，按照磁盘空间在“磁盘置备”处选择“精简”或“厚设备”，
勾选“自动打开电源”，然后点击“下一页”。
注意：“厚设备”占用的磁盘空间更多。

<!-- 来源页 2362 -->
6. 检查配置后，点击“完成”按钮，即开始部署。
7. 稍等片刻，待系统文件上载磁盘完成后，即可完成虚拟机创建。
注意: 部署过程可能需要等待较长时间，请勿刷新页面，并耐心等待部署完成。
第三步：登录虚拟机
1. 虚拟机创建完成后，会自动打开电源并启动。
2. 在左侧“导航器”下点击“虚拟机”标签页，然后在右侧列表中，选择上述步骤创建的虚拟机。

<!-- 来源页 2363 -->
3. 点击“控制台>打开浏览器控制台”或者直接单击控制台缩略图，打开控制台页面。
4. 输入默认的用户名和密码（hillstone/hillstone），登录虚拟机。
第四步：配置网卡信息
虚拟机部署完成后，用户需要根据当前环境地址，通过配置/etc/netplan下的配置文件进行修改网卡配置
信息。
1. 在控制台中，输入cat /etc/netplan/00-installer-config.yaml命令，查看当前配置文件信息。
2. 输入vi /etc/netplan/00-installer-config.yaml命令，打开该配置文件。
3. 光标移动至需要修改的位置，输入i进入编辑模式，可修改IP地址、网关地址等信息或者配置DHCP等。
注意：IP地址需保证防火墙设备、安装设备识别系统的PC机浏览器均可访问，此IP地址即作为本地设备识别虚拟
机的IP地址。（以10.182.197.172为示例）

<!-- 来源页 2364 -->
4. 编辑完成后，按“ESC”键，再输入:wq退出该配置文件并保存配置信息。
5. 重启虚拟机，以保证应用修改后的网卡信息。
第五步：安装设备识别程序
1. 打开浏览器，访问上述步骤中配置的IP地址，例如：https://10.182.197.172:22654
2. 由于使用了自签名证书，浏览器出现提示：您的连接不是专用链接。点击“高级> 继续访问”。

<!-- 来源页 2365 -->
3. 进入设备识别程序安装引导，选择识别模式，然后点击“下一步”，默认为“深度识别模式”以及默认开启“识
别引擎自动更新”。
4. 在“相关配置”步骤中，按需配置Update Server地址、主动探测超时时间、Docker端口号。如使用默认配置，
即使用山石网科提供的Update Server。

<!-- 来源页 2366 -->
5. 确认配置信息，点击“安装”按钮即可。
6. 安装完成后，设备识别程序将会自动启动。
至此，即可完成在VMware ESXi上部署设备识别系统。
在Openstack上部署设备识别系统
开始之前
在Openstack上部署设备识别系统，在开始之前请做到：
l 按照系统要求准备好宿主机环境。
l 联系山石网科客服人员获取设备识别系统qcow2格式的镜像文件保存在本地。
系统要求
在Openstack上部署设备识别系统，需要宿主机满足以下要求。
l 要求至少能够提供4个CPU、4GB内存。

<!-- 来源页 2367 -->
l 已经安装Openstack及其组件Horizon，Nova，Neutron，Glance和Cinder。
部署步骤
第一步：导入镜像文件
1. 登录OpenStack的Web管理界面，在左侧选择“项目> 计算> 镜像”。
2. 点击页面右上角的“创建镜像”按钮。
3. 在弹出的<创建镜像>对话框中，设置以下基本信息。
选项
说明
名称
指定镜像的名称，例如示意图中的“iot-identity-vm”。
镜像文件
点击“浏览”按钮，选择本地保存的设备识别系统qcow2格式的镜像文件。
镜像格式
在下拉菜单中选择“QCOW2-QEMU模拟器”格式。
4. 其他信息保持默认即可。
5. 点击右下角的“创建镜像”按钮，完成配置。
6. 稍等片刻，大约需要10分钟左右，新创建的镜像将会显示在镜像列表中。
第二步：创建实例类型
一般情况下，非管理员不能直接修改实例的属性参数（例如内核、内存等信息），只有通过将实例与一个实
例类型（Flavor）绑定，才能继承实例类型的属性。
创建实例类型，请按照以下步骤进行：

<!-- 来源页 2368 -->
1. 使用管理员帐户，登录OpenStack的Web管理界面。
2. 在左侧选择“管理员> 计算> 实例类型”，点击右上角“创建实例类型”按钮。
3. 在弹出的<创建实例类型>对话框，进行设置。
选项
说明
名称
指定实例类型名称，例如示意图中的“iot.normal”。
ID
ID号码由OpenStack自动生成。
VCPU数量
指定该主机的CPU虚拟内核的数量。推荐配置为4，最低配置推荐2。
内存（MB）
指定实例的内存大小。推荐配置为4096MB，最低配置推荐2048MB。
根磁盘（GB）
指定根磁盘分区所需容量，单位为GB。建议配置为20GB，最低配置推荐8GB。
4. 点击右下角“创建实例类型”按钮，完成配置。
第三步：创建网络
Openstack的网络服务为Openstack云部署提供了可扩展的网络连接服务，通过Openstack的WebUI界
面，就可以实现网络的创建和修改。
由于不同用户的组网需求不同，且创建网络属于Openstack的基础操作，本文档不再描述如何创建网络。

<!-- 来源页 2369 -->
一般情况下，OpenStack环境内基本会存在一个外部网络，例如“ext-net”，用户可以直接使用该外部网
络。
第四步：创建并启动实例
使用管理员帐户，创建实例，请按照以下步骤进行：
1. 选择“项目> 计算> 镜像”，点击第一步创建的镜像列表项后面的“启动”按钮。
2. 在弹出的<创建实例>对话框，进行设置。
3. 在<详情>标签页中，配置实例名称，例如示意图为“iot-identify-vm”。
4. 在<源>标签页中，配置“创建新卷”可选择“不”。
5. 在<实例类型>标签页中，选择第二步中配置的实例类型“iot.normal”，点击
按钮。
6. 在<网络>标签页中，选择网络“ext-net”，点击
按钮，使外部能够访问到该实例。
7. 其他配置保持默认即可。
8. 点击右下角“创建实例”按钮，完成配置。一般情况下，创建完成后，实例会自动启动。
9. 可以看到，实例创建完成后，会分配一个IP地址给实例，可以用此IP地址作为本地设备识别虚拟机的IP地址。
第五步：登录虚拟机
1. 登录OpenStack的Web管理界面。
2. 选择“项目> 计算> 实例”。
3. 在列表中，点击实例名称“iot-identify-vm”，跳转到实例详情界面中，点击<控制台>页签，即可在嵌入的命
令行界面中打开控制台页面。
4. 输入默认的用户名和密码（hillstone/hillstone），登录虚拟机。
第六步：配置网卡信息
虚拟机部署完成后，用户需要根据当前环境地址，通过配置/etc/netplan下的配置文件进行修改网卡配置
信息。

<!-- 来源页 2370 -->
1. 确认网卡名称。输入ip addr命令，查看当前的网卡名称。默认网卡名称为“ens160”。根据部署环境不同，自
动分配的网卡默认名称可能会不同。
2. 输入cat /etc/netplan/00-installer-config.yaml命令，查看当前配置文件信息。
3. 输入vi /etc/netplan/00-installer-config.yaml命令，打开该配置文件。
4. 光标移动至需要修改的位置，输入i进入编辑模式，可修改网卡名称、网卡数量等信息。
注意：网卡名称必须要与确认的网卡名称修改一致。
5. 编辑完成后，按“ESC”键，再输入:wq退出该配置文件并保存配置信息。
6. 重启虚拟机，以保证应用修改后的网卡信息。
第七步：安装设备识别程序
1. 打开浏览器，访问上述上述步骤中网卡信息中的IP地址，例如：https://10.182.237.89:22654
2. 由于使用了自签名证书，浏览器出现提示：您的连接不是专用链接。点击“高级> 继续访问”。
3. 进入设备识别程序安装引导，选择识别模式，然后点击“下一步”，默认为“深度识别模式”以及默认开启“识
别引擎自动更新”。

<!-- 来源页 2371 -->
4. 在“相关配置”步骤中，按需配置Update Server地址、主动探测超时时间、Docker端口号。如使用默认配置，
即使用山石网科提供的Update Server。
5. 确认配置信息，点击“安装”按钮即可。
6. 安装完成后，设备识别程序将会自动启动。

<!-- 来源页 2372 -->
至此，即可完成在OpenStack上部署设备识别系统。
云端设备识别配置
系统支持云端设备识别功能，开启该功能后，系统从经过设备的流量中提取设备信息并上送至云端，通过云
端设备识别服务识别IT设备和IoT设备的型号、厂商等信息。
云端设备识别配置包括：
l 开启/关闭云端设备识别功能
l 配置校正后设备信息报文上送云端功能
l 查看设备识别功能配置信息
l 配置重新识别间隔时间
前置条件
使用基于流量的被动识别、云端设备识别或本地设备识别前，需要先在安全域中开启应用识别。开启安全域
的应用识别功能，请参阅"应用识别" 在第126页。
开启/关闭云端设备识别功能
默认情况下，云端设备识别功能为关闭状态。在全局配置模式下，使用以下命令开启或关闭云端设备识别功
能。
l
开启：device cloud-detect enable
l
关闭：no device cloud-detect enable
配置校正后设备信息报文上送云端功能
用户可以根据需要，将设备中校正后的设备信息对应的报文上送至云端，云端用该报文进行自学习，从而更
大程度地提升识别能力。
进入设备校正报文上送云端配置模式
校正后设备信息报文上送云端功能需要在设备校正报文上送云端配置模式下进行。
进入设备校正报文上送云端配置模式，在全局配置模式下使用以下命令：
device training-upload
配置上送数量
配置校正后设备信息报文上送的数量，在设备校正报文上送云端配置模式下，使用以下命令：
collect-payload-num collect-payload-num

<!-- 来源页 2373 -->
l
collect-payload-num - 指定校正后设备指纹信息报文单次上送数量，范围是20至100个，默认值是
100。
在设备校正报文上送云端配置模式下使用no collect-payload-num恢复默认值。
配置上送时长
配置校正后设备信息报文上送的时长，在设备校正报文上送云端配置模式下，使用以下命令：
collect-time collect-time
l
collect-time - 指定校正后设备指纹信息报文收集时长，范围是60至600秒，默认时长为120秒。
在设备校正报文上送云端配置模式下使用no collect-time 恢复默认值。
查看校正后设备信息报文上送云端功能配置信息
查看校正后设备信息报文上送云端功能配置信息，在任意模式下，使用以下命令：
show device training-upload
示例：
SG-6000(config)# show device training-upload
Training_upload collect max time: 120 seconds（显示校正后设备信息报文上送至云端的时长为
120秒）
Training_upload collect number: 100（显示校正后设备信息报文上送至云端的单次上送数量为100
个）
查看设备识别功能配置信息
查看设备识别功能配置信息，在任意模式下，使用以下命令：
show device detect-config
示例：
SG-6000(config)# show device detect-config
------------------------------------------------------------------------------------------------
------
Device cloud-detect status:: enable（显示云端设备识别功能为开启状态）
------------------------------------------------------------------------------------------------
------

<!-- 来源页 2374 -->
Device docker-detect module environment: external docker（显示本地设备识别功能使用外置
方式，即使用部署在虚拟机中的设备识别系统识别）
Device docker-detect module ip: 10.182.192.187（显示部署设备识别系统的虚拟机IP地址）
Device docker-detect module port: 36000（显示设备识别系统的端口号）
Device docker-detect module vrouter: trust-vr（显示已部署设备识别系统的虚拟机所属VRouter
的名称）
Device docker-detect source interface: Not Configured（显示连接设备识别系统的源接口名
称。）
Device docker-detect action status: Disable（显示本地设备识别功能为关闭状态）
------------------------------------------------------------------------------------------------
------
device discover device abnormal detect status: enable（显示终端异常检测功能为开启状态）
------------------------------------------------------------------------------------------------
------
配置重新识别间隔时间
默认情况下，设备系统会每间隔20分钟（1200秒）重新进行一次设备识别，用户可以根据需求，调整重新
识别的间隔时间，在全局配置模式下，使用以下命令：
device identify-renew interval interval-value
l
interval-value - 指定重新识别的间隔时间，范围是10到1200秒，默认值是1200秒。
在全局配置模式下使用no device identify-renew interval 恢复默认值。
本地设备识别配置
本地设备识别功能是指通过部署在设备中的设备识别模块识别IT设备和IoT设备的型号、厂商等信息。
前置条件
使用基于流量的被动识别、云端设备识别或本地设备识别前，需要先在安全域中开启应用识别。开启安全域
的应用识别功能，请参阅"应用识别" 在第126页。
开启/关闭本地设备识别功能
默认情况下，本地设备识别功能为关闭状态。在全局配置模式下，使用以下命令开启或关闭本地设备识别功
能。

<!-- 来源页 2375 -->
l
开启：device docker-detect enable
l
关闭：no device docker-detect
注意: 若开启本地资产识别前，云端资产识别功能已开启，将会自动屏蔽云端资产识别功能。在本
地资产识别关闭后，则可继续使用云端资产识别。
配置本地设备识别功能
本地设备识别分为内置和外置两种方式：
l
内置：使用防火墙系统内置设备识别模块识别。使用该方式前，请先配置Docker管理功能将设备识别系
统部署到系统中。
l
外置：使用部署在虚拟机中的设备识别系统识别。使用该方式前，请先在虚拟机中部署设备识别系统。
型号说明：本地设备识别的内置方式，仅支持A系列A2600及以上型号（A2600- A3810型号
需要必配硬盘、A5100及以上型号可选配硬盘）、B系列B3200及以上型号（需要必配硬
盘）、云·界。
配置本地设备识别功能，在全局配置模式下，使用以下命令：
device docker-detect {local-docker | external-docker ip ip-address} port port-number
vrouter vr-name
l
local-docker - 指定使用防火墙系统内置设备识别模块识别，默认IP地址为127.0.0.1，无需配置和修
改。
l
external-docker ip ip-address - 指定部署在虚拟机中的设备识别系统识别，并指定已部署设备识别
系统的虚拟机IP地址。
l
port port-number - 指定设备识别模块的端口号。当指定为内置设备识别方式（local-docker）时，
该端口号为Docker的宿主机端口号，请与Docker配置（配置端口映射）中指定的宿主机端口号保持一
致，范围是1-65535。
l
vrouter vr-name - 指定已部署设备识别系统的虚拟机所属VRouter的名称。
在全局配置模式下，使用no device docker-detect {local-docker | external-docker}取消本地设备识
别功能配置。

<!-- 来源页 2376 -->
查看设备识别功能配置信息
查看设备识别功能配置信息，在任意模式下，使用以下命令：
show device detect-config
示例：
SG-6000(config)# show device detect-config
------------------------------------------------------------------------------------------------
------
Device cloud-detect status:: enable（显示云端设备识别功能为开启状态）
------------------------------------------------------------------------------------------------
------
Device docker-detect module environment: external docker（显示本地设备识别功能使用外置
方式，即使用部署在虚拟机中的设备识别系统识别）
Device docker-detect module ip: 10.182.192.187（显示部署设备识别系统的虚拟机IP地址）
Device docker-detect module port: 36000（显示设备识别系统的端口号）
Device docker-detect module vrouter: trust-vr（显示已部署设备识别系统的虚拟机所属VRouter
的名称）
Device docker-detect source interface: Not Configured（显示连接设备识别系统的源接口名
称。）
Device docker-detect action status: Disable（显示本地设备识别功能为关闭状态）
------------------------------------------------------------------------------------------------
------
device discover device abnormal detect status: enable（显示终端异常检测功能为开启状态）
------------------------------------------------------------------------------------------------
------
配置重新识别间隔时间
默认情况下，设备系统会每间隔20分钟（1200秒）重新进行一次设备识别，用户可以根据需求，调整重新
识别的间隔时间，在全局配置模式下，使用以下命令：
device identify-renew interval interval-value
l
interval-value - 指定重新识别的间隔时间，范围是10到1200秒，默认值是1200秒。
在全局配置模式下使用no device identify-renew interval 恢复默认值。

<!-- 来源页 2377 -->
开启终端异常行为检测功能
终端异常行为检测功能开启后，系统会从流经设备的流量中提取设备流量（traffic）信息，并将其上送至
IoT识别中心。识别中心会对设备的流量行为进行分析与监测，据此建立行为基线，从而发现异常行为。用
户可以通过查看设备日志来获取IoT设备异常行为信息，并对告警日志进行相应处置。若出现误报情况，可点
击“误报反馈”按钮，将处置意见反馈给识别中心。
在全局配置模式下，使用以下命令，开启/关闭终端异常行为检测功能：
l
开启：device device-abnormal-detect enable
l
关闭：no device device-abnormal-detect enable
配置MAC地址学习功能
在物联网跨三层网络部署环境中，IoT终端设备与防火墙分属不同网段。报文经由三层交换机时，IoT终端设
备原本的MAC地址会被替换为三层交换机的MAC地址，致使防火墙难以获取IoT终端设备的真实MAC地址。
而MAC地址作为IoT终端设备极为基础且稳定的属性，在判定设备厂商及终端识别方面发挥着关键作用。因
此，系统提供MAC地址学习功能，旨在解决跨网段场景下防火墙能够获取IoT终端设备真实MAC地址的难
题，为后续实现IoT终端设备的精准识别，以及强化物联网网络管理与安全保障夯实基础。
系统支持通过以下两种方式获取IoT设备的MAC地址信息，用户可按需任选其一，亦可同时选用多种方式。
当多种方式同时启用时，通过DHCP syslog获取MAC地址的方式优先级高于通过SNMP获取MAC地址的方
式。
l 通过DHCP syslog获取MAC地址
l 通过SNMP获取MAC地址
通过DHCP Syslog获取MAC地址
该方式依托DHCP Syslog主机外发日志数据的属性。当DHCP Syslog主机与防火墙设备成功建立通信连接
后，会主动将日志数据外发至防火墙。防火墙作为日志服务器，在接收到DHCP Syslog主机发送的日志数据
后，会立即对其进行解析，并从中提取出设备的真实MAC地址、IP地址等关键信息，以便后续用户对网络中
的设备资产进行管理，从而提高网络管理的效率，为网络安全监控提供重要保障。
通过DHCP Syslog获取MAC地址，可按照以下流程进行配置：
1. 进入DHCP Syslog主机配置模式
2. 配置DHCP Syslog主机参数
3. 开启接收日志功能
4. （可选）查看DHCP Syslog主机详情

<!-- 来源页 2378 -->
进入DHCP Syslog主机配置模式
创建指定名称的DHCP Syslog主机并进入DHCP Syslog主机配置模式。如果指定的名称已存在，则直接进
入DHCP Syslog主机配置模式。
在全局配置模式下，使用以下命令，创建DHCP Syslog主机并进入DHCP Syslog主机配置模式：
iot-monitor get-mac dhcp-syslog-host host-name
l
host-name - 指定DHCP Syslog主机的名称。系统最多支持新建8个DHCP Syslog主机。
在全局配置模式下，使用以下命令，删除指定名称的DHCP Syslog主机及其配置信息：
no iot-monitor get-mac dhcp-syslog-host host-name
配置DHCP Syslog主机参数
为确保防火墙与DHCP Syslog主机能够成功建立通信连接，用户需要配置DHCP Syslog主机的IP地址、协
议类型、DHCP服务类型等参数。
指定DHCP Syslog主机的IP地址
指定DHCP Syslog主机的IP地址，在DHCP Syslog主机配置模式下，使用以下命令：
address {ipv4-address | ipv6-address}
l
ipv4-address - 输入IPv4地址。
l
ipv6-address - 输入IPv6地址。
在DHCP Syslog主机配置模式下，使用以下命令，删除DHCP Syslog主机的IP地址配置：
no address
指定防火墙接收DHCP Syslog主机日志的端口号
指定防火墙接收DHCP Syslog主机日志的端口号，在DHCP Syslog主机配置模式下，使用以下命令：
port port_number
l
port_number - 指定端口号。取值范围是1到65535，默认为45514。
在DHCP Syslog主机配置模式下，使用以下命令，恢复默认配置：
no port
指定防火墙接收DHCP Syslog主机日志的接口
指定防火墙接收DHCP Syslog主机日志的接口，在DHCP Syslog主机配置模式下，使用以下命令：

<!-- 来源页 2379 -->
interface interface-name
l
interface-name - 指定防火墙接收DHCP Syslog主机日志的接口名称。
在DHCP Syslog主机配置模式下，使用以下命令，删除相关配置：
no interface
指定DHCP Syslog主机通信协议类型
指定防火墙与DHCP Syslog主机建立通信连接时所使用的协议类型，包括UDP、TCP和SSL协议。默认使用
UDP协议进行通信。
注意: 当使用SSL协议进行加密通信时，用户需要在DHCP Syslog主机上，为具备DHCP日志外发
功能的相关服务或程序，提前安装防火墙的CA证书以实现加密认证。防火墙的CA证书可前往“系
统> PKI > 信任域证书”页面导出，详见导入导出信任域的信息。
在DHCP Syslog主机配置模式下，使用以下命令，指定防火墙与DHCP Syslog主机建立通信连接时所使用
的协议类型：
connect-type {tcp | udp | ssl}
l
tcp - 指定TCP协议。
l
udp - 指定UDP协议。系统默认为该选项。
l
ssl - 指定SSL协议。
在DHCP Syslog主机配置模式下，使用以下命令，恢复默认配置：
no connect-type
指定DHCP服务类型
指定DHCP Syslog主机操作系统对应的DHCP服务类型。不同操作系统的DHCP服务类型支持的日志格式不
同，请根据需求进行配置。
注意: 系统支持的DHCP服务类型由IoT特征库控制，不同的IoT特征库版本，支持的DHCP服务类
型有所区别，请以当前实际版本为准。
在DHCP Syslog主机配置模式下，使用以下命令，指定DHCP服务类型：
type type-name
l
type-name - 指定DHCP服务类型的名称。

<!-- 来源页 2380 -->
在DHCP Syslog主机配置模式下，使用以下命令，删除DHCP服务类型配置：
no type
添加描述信息
添加DHCP Syslog主机的描述信息，在DHCP Syslog主机配置模式下，使用以下命令：
description description
l
description - 为DHCP Syslog主机添加相关的描述信息，取值范围是1到255个字符。
在DHCP Syslog主机配置模式下，使用以下命令，删除描述信息：
no description
开启/关闭接收日志功能
完成DHCP Syslog主机配置后，用户需要在防火墙设备上开启接收日志功能，以确保防火墙能够正常接收到
DHCP Syslog主机发送的日志信息。启用后，一旦防火墙与DHCP Syslog主机成功建立通信连接，防火墙
即可接收来自DHCP Syslog主机发送的日志信息。该功能默认为关闭状态。
在DHCP Syslog主机配置模式下，使用以下命令，开启/关闭接收日志功能：
l
开启：enable
l
关闭：no enable
查看DHCP Syslog主机详情
查看DHCP Syslog主机的详细信息，在任意模式下，使用以下命令：
show iot-monitor get-mac dhcp-syslog-host [host-name | detail | host-name detail]
l
show iot-monitor get-mac dhcp-syslog-host - 查看所有DHCP Syslog主机的配置信息。
l
host-name - 查看指定DHCP Syslog主机的配置信息。
l
detail - 查看所有DHCP Syslog主机的详细信息，包括DHCP Syslog主机的配置信息、DHCP Syslog
主机的连接次数等。
l
host-name detail - 查看单个DHCP Syslog主机的详细信息。
示例：
hostname(config)# show iot-monitor get-mac dhcp-syslog-host
IoT-monitor DHCP-Syslog-Host total num: 1
================================================

<!-- 来源页 2381 -->
DHCP Syslog Host name: server1 （显示DHCP Syslog主机的名称）
description: （显示DHCP Syslog主机的描述）
enable: on （显示接收日志功能的启用状态）
address: 10.1.1.1 （显示DHCP Syslog主机的IP地址）
type: CentOS-dhcpd （显示DHCP Syslog主机操作系统对应的DHCP服务类型）
connect-type: udp （显示防火墙与DHCP Syslog主机建立通信连接时所使用的协议类型）
port: 5144 （显示防火墙接收DHCP Syslog主机日志的端口号）
interface: MGT0 （显示防火墙接收DHCP Syslog主机日志的接口名称）
status: Connected （显示DHCP Syslog主机的连接状态）
dhcp-log-count: 0 （显示DHCP Syslog主机发送给防火墙的日志数量）
================================================
通过SNMP获取MAC地址
开始之前：
l
配置SNMP服务器
系统能够通过SNMP服务器获取设备相关的ARP信息，并根据IoT设备的IP地址查询对应的真实MAC地址。该
功能默认为关闭状态。
开启通过SNMP获取MAC地址功能，在全局配置模式下，使用以下命令：
iot-monitor get-mac snmp enable
关闭通过SNMP获取MAC地址功能，在全局配置模式下，使用以下命令：
no iot-monitor get-mac snmp enable
查看通过SNMP获取MAC地址功能的开启状态，在任意模式下，使用以下命令：
show iot-monitor get-mac snmp
以下是一个返回结果示例：
hostname# show iot-monitor get-mac snmp
IoT-monitor get MAC address from SNMP: enable（已开启通过SNMP获取MAC地址功能）

<!-- 来源页 2382 -->
设备管理
配置设备区域
用户可以配置设备IP地址/IP范围与区域的对应关系。系统发现设备后，根据已配置的设备区域确定设备的部
署区域。
创建区域以及子区域
创建区域，在全局配置模式下，使用以下命令：
device district id id name name
l
id id - 指定创建区域的id。范围是1到5000。
l
name name - 指定创建区域的名称。范围是1到31个字符。
执行该命令后，系统创建指定名称的区域，并且进入设备区域配置模式；如果指定的名称已存在，则直接进
入设备区域配置模式。在全局配置模式下，使用命令no device district id id 删除指定的区域。
用户可以为已存在的区域创建子区域。创建子区域，在设备区域配置模式下，使用以下命令：
member id id
l
id id - 指定创建子区域的id。范围是1到5000。说明：不能与区域的id重复。
在设备区域配置模式下，使用no member id id删除指定的子区域。
配置区域IP网段
配置区域所在的IPv4网段，在区域IP网段内的设备将自动加入该区域。在区域配置模式下，使用以下命令：
ip network ip-address / netmask
l
ip-address / netmask - 指定区域所在的IP地址和子网掩码。
在设备区域配置模式下，使用no ip network ip-address/netmask删除指定的区域所在的IPv4网段。
配置区域所在的IPv6网段，在区域IP网段内的设备将自动加入该区域。该命令仅当该版本为IPv6版本时可
配。在设备区域配置模式下，使用以下命令：
ipv6 prefix ipv6-prefix / prefix-length
l
ipv6-prefix / prefix-length - 指定IPv6前缀以及前缀长度。取值范围为1到128。
在设备区域配置模式下，使用no ip prefix ipv6-prefix / prefix-length删除指定的区域所在的IPv6网
段。

<!-- 来源页 2383 -->
配置区域IP地址范围
配置区域IPv4地址范围，在区域IP地址范围内的设备将自动加入该区域。在设备区域配置模式下，使用以下
命令：
ip range ip-min ip-max
l
ip-min - 指定区域对应的IP地址范围的最小值。
l
ip-max - 指定区域对应的IP地址范围的最大值。
在设备区域配置模式下，使用no ip range ip-min ip-max删除指定的区域所在的IPv4地址范围。
配置区域IPv6地址范围，在区域IP地址范围内的设备将自动加入该区域。该命令仅当该版本为IPv6版本时可
配。在设备区域配置模式下，使用以下命令：
ipv6 range ipv6-min ipv6-max
l
ipv6-min - 指定区域对应的IPv6地址范围的最小值。
l
ipv6-max - 指定区域对应的IPv6地址范围的最大值。
在设备区域配置模式下，使用no ipv6 range ipv6-min ipv6-max删除指定的区域所在的IPv6地址范围。
查看设备区域信息
查看设备区域信息，在任意模式下，使用以下命令：
show device district [ id ]
l
id - 显示指定id的设备区域信息。如不配置，则展示全部区域配置信息。
示例：
hostname#show device district
Device-district total num: 3
======================================
ID name & IP
--------------------------------------
1 test1
139.0.0.0/8
2 test2
140.0.0.0/9
3 test3

<!-- 来源页 2384 -->
141.0.0.0/8
======================================
启用/禁用自动同步设备至资产列表
型号说明：目前，支持自动同步设备到资产列表的防火墙包含：
l
安装有硬盘的SG-6000 A系列设备（不含SG-6000-A1600/A1800/A2200）。
l
安装有硬盘的SG-6000 B系列设备。
l
安装有硬盘的SG-6000 K系列设备。
l
安装有硬盘的SG-6000 X系列设备（不含SG-6000-X9180）。
l
安装有硬盘的SG-6000 云·界设备。
启用自动同步设备至资产列表，在全局配置模式下，使用以下命令：
device sync-asset type type-name
l
type-name - 指定设备类型名称。用户可通过在type参数后使用Tab键，查看设备类型名称列表，并
输入选择的设备类型名称。
注意：如果设备类型名称包含空格，需要使用英文双引号引住整个设备类型名称。
在全局配置模式下，使用device sync-asset type type-name 命令禁用指定设备类型的设备自动同步至
资产列表。
查看所有设备类型的设备同步至资产列表的启用状态
查看所有设备类型的设备同步至资产列表的启用状态，在任意模式下，使用以下命令：
show device sync-asset type
示例：
hostname#show device sync-asset type
=======================================================
type sync-asset
-------------------------------------------------------
IPC enable

<!-- 来源页 2385 -->
NVR enable
CVR disable
DVR disable
Video Server disable
Network Server disable
Server disable
Cloud Storage disable
PC disable
Door Control disable
Intercoms disable
Alarm Mainframe disable
Printer disable
Ipad disable
Firewall disable
Router disable
Gaming Console disable
Switch disable
Phone disable
Tablet disable
Monitoring Device disable
Video Conferencing disable
Projector disable
Thin Client disable
Scanner disable
Video Equipment disable
Voip Phone disable
Attendance Machine disable
Storage disable
=======================================================

<!-- 来源页 2386 -->
设备自动同步到资产列表
系统可以将发现的设备或识别到对应设备类型的设备自动同步到资产列表。
型号说明：目前，支持自动同步设备到资产列表的防火墙包含：
l
安装有硬盘的SG-6000 A系列设备（不含SG-6000-A1600/A1800/A2200）。
l
安装有硬盘的SG-6000 B系列设备。
l
安装有硬盘的SG-6000 K系列设备。
l
安装有硬盘的SG-6000 X系列设备（不含SG-6000-X9180）。
l
安装有硬盘的SG-6000 云·界设备。
将发现的设备自动同步至资产列表
启用将发现的设备自动同步至资产列表，在设备发现规则配置式下，使用以下命令:
sync-to-asset enable
在设备发现规则配置模式下，使用no sync-to-asset enable命令禁用发现的设备自动同步至资产列表。
提示: 在设备发现规则条目中也可以启用自动同步设备至资产列表，请参阅配置设备发现规则。
将识别出对应设备类型的设备自动同步至资产列表
启用将识别出对应设备类型的设备自动同步至资产列表，在全局配置模式下，使用以下命令：
device sync-asset type type-name
l
type-name - 指定设备类型名称。用户可通过在type参数后使用Tab键，查看设备类型名称列表，并
输入选择的设备类型名称。
注意：如果设备类型名称包含空格，需要使用英文双引号引住整个设备类型名称。
在全局配置模式下，使用no device sync-asset type type-name 命令禁用指定设备类型的设备自动同
步至资产列表。
查看所有设备类型的设备同步至资产列表的启用状态
查看所有设备类型的设备同步至资产列表的启用状态，在任意模式下，使用以下命令：
show device sync-asset type
示例：

<!-- 来源页 2387 -->
hostname#show device sync-asset type
=======================================================
type sync-asset
-------------------------------------------------------
IPC enable
NVR enable
CVR disable
DVR disable
Video Server disable
Network Server disable
Server disable
Cloud Storage disable
PC disable
Door Control disable
Intercoms disable
Alarm Mainframe disable
Printer disable
Ipad disable
Firewall disable
Router disable
Gaming Console disable
Switch disable
Phone disable
Tablet disable
Monitoring Device disable
Video Conferencing disable
Projector disable
Thin Client disable
Scanner disable

<!-- 来源页 2388 -->
Video Equipment disable
Voip Phone disable
Attendance Machine disable
Storage disable
=======================================================
设备监控
设备监控包括以下内容：
l 查看设备监控列表信息
l 修改设备监控列表条目
l 删除设备监控列表条目
查看设备监控列表信息
查看全部或指定设备监控列表信息，在任何模式下，使用以下命令：
show device-list [ip ip-address| ipv6 ipv6-address] [vrouter vr-name | vswitch vs-name]
[manufacturer manufacturer-name] [type type-name] [status {online | offline}]
l
ip ip-address - 显示指定IPv4地址的所有设备监控信息。
l
ipv6 ipv6-address - 显示指定IPv6地址的所有设备监控信息。
l
vr-name - 显示指定VRouter的设备监控列表条目信息。
l
vs-name - 显示指定VSwitch的设备监控列表条目信息。
l
manufacturer manufacturer-name - 显示指定厂商名称的设备监控列表条目信息。
l
type type-name- 显示指定设备类型的设备监控列表条目信息。
l
status {online | offline} - 显示指定状态的设备监控列表条目信息。其中，online为在线，offline为
离线。
修改设备监控列表条目
修改指定的设备监控列表条目，在任何模式下，使用以下命令：
exec device modify entry{ip ip-address| ipv6 ipv6-address} {vrouter vr-name | vswitch vsname} [manufacturer manufacturer-name] [type type-name] [model model-name] [osfamily family-name [os-version version-name]] [category {IT | IoT}]

<!-- 来源页 2389 -->
l
ip ip-address - 修改指定IPv4地址的设备监控列表条目。
l
ipv6 ipv6-address - 修改指定IPv6地址的设备监控列表条目。
l
vr-name - 指定IP地址所在的VRouter名称。
l
vs-name - 指定IP地址所在的VSwitch名称。
l
manufacturer manufacturer-name- 修改指定IP地址的设备监控列表条目的厂商。
l
type type-name- 修改指定IP地址的设备监控列表条目的设备类型。
l
model model-name- 修改指定IP地址的设备监控列表条目的设备型号。
l
os-family family-name - 修改指定IP地址的IoT监控列表条目的设备操作系统族。
l
os-version version-name - 修改指定IP地址的IoT监控列表条目的设备操作系统版本。
l
category {IT | IoT - 修改指定IP地址的设备监控列表条目的设备类别。
删除设备监控列表条目
删除全部或指定设备监控列表条目，在任何模式下，使用以下命令：
exec device delete entry [ip ip-address| ipv6 ipv6-address] [vrouter vr-name | vswitch vsname] [manufacturer manufacturer-name] [type type-name] [status {online | offline}]
l
ip ip-address - 删除指定IPv4地址的设备监控列表条目
l
ipv6 ipv6-address - 删除指定IPv6地址的设备监控列表条目。
l
vr-name - 删除指定VRouter的设备监控列表条目。
l
vs-name - 删除指定VSwitch的设备监控列表条目。
l
manufacturer manufacturer-name- 删除指定厂商的设备监控列表条目。
l
type type-name- 删除指定设备类型的设备监控列表条目。
l
status {online | offline} - 删除指定状态的设备监控列表条目。其中，online为在线，offline为离
线。
删除动态添加的自定义设备类型
在防火墙的设备管理功能中，设备类型包含预定义设备类型和自定义设备类型。预定义设备类型由系统内
置，适用于常见标准设备；自定义设备类型则为动态添加的设备类型，包括用户手动添加的设备类型、手工
校正已发现设备/设备自动识别且不在预定义列表中的设备类型。在设备接入和管理过程中，部分自定义设备
类型会逐渐变成冗余、无效或过时信息。此时，用户可通过删除动态添加的自定义设备类型功能，及时清理
这些陈旧数据，有效避免因陈旧或错误信息导致的系统误判，提升设备管理效率，同时释放系统资源，优化
防火墙性能。

<!-- 来源页 2390 -->
删除动态添加的自定义设备类型，在任意配置式下，使用以下命令:
exec device delete dynamic-attribute {manufacturer | type | model | os-family | os-version}
attribute-name
l
manufacturer | type | model | os-family | os-version - 指定需要删除的属性类别。
o
manufacturer - 设备厂商
o
type - 设备类型
o
model - 设备型号
o
os-family - 操作系统族
o
os-version -操作系统版本
l
attribute-name - 指定需要删除的具体属性值的名称。

<!-- 来源页 2391 -->
策略管控
设备分类
系统提供设备字典，包含已支持识别设备的厂商、类型、型号、操作系统族和操作系统版本信息。用户可以
按照设备的多种维度（包括设备厂商、类型、设备型号、操作系统等）将一个或多个设备归类成一个设备集
合，并为其指定设备分类名称。系统将识别的设备信息与设备分类属性进行相应的映射，进而可以通过安全
策略直接引用设备分类名称来实现对设备集合的管控。
注意: 设备字典包含在IoT设备指纹库中，用户可以通过升级IoT设备指纹库来更新设备字典。相关
操作参见“系统管理> 升级管理> 升级特征库”章节。
配置设备分类
用户可以对设备分类进行以下配置：
l 创建/删除设备分类
l 配置设备分类的设备类型
l 配置设备分类的厂商
l 配置设备的型号
l 配置设备分类的操作系统族
l 配置设备分类的操作系统版本
l 查看设备分类配置信息
l 查看设备映射IP地址
l 查看指定IP地址所属设备分类
创建/删除设备分类
创建设备分类，在全局配置模式下，使用以下命令：
device-group device-group-name
l
device-group-name – 指定设备分类的名称，范围是1到31个字符。
执行该命令后，系统创建指定名称的设备分类，并且进入设备分类配置模式。如果指定的名称已存在，则直
接进入设备分类配置模式。
在全局配置模式下，使用该命令no的形式删除设备分类：

<!-- 来源页 2392 -->
no device-group device-group-name
配置设备分类的设备类型
配置设备分类的设备类型，选择预定义设备类型或者指定自定义设备类型，在设备分类配置模式下，使用以
下命令：
type type-name
l
type-name– 设备分类的设备类型：
l
预定义：指定预定义操作系统族名称，用户可通过在type参数后使用Tab键，查看完整的预定义
设备类型列表。
l
自定义：如需指定自定义设备类型，直接输入设备类型名称，范围是1到63个字符。
在设备分类配置模式下，使用该命令no的形式删除指定的设备类型：
no type
配置设备分类的厂商
配置设备分类的厂商，选择预定义厂商名称或者指定自定义厂商名称，在设备分类配置模式下，使用以下命
令：
manufacturer manufacturer-name
l
manufacturer-name– 设备分类的厂商名称：
l
预定义：指定预定义厂商名称，用户可通过在manufacturer参数后使用Tab键，查看完整的预定
义厂商名称。
l
自定义：如需指定自定义厂商名称，直接输入厂商名称，范围是1到63个字符。
在设备分类配置模式下，使用该命令no的形式删除指定的厂商名称：
no manufacturer
配置设备型号
配置设备分类的设备型号，在设备分类配置模式下，使用以下命令：
model model-name
l
model-name – 指定设备分类的设备型号，范围是1到31个字符。
在设备分类配置模式下，使用该命令no的形式删除指定的设备型号：
no model

<!-- 来源页 2393 -->
配置设备分类的操作系统族
配置设备分类的操作系统族，选择预定义操作系统族名称或者指定自定义操作系统族名称，在设备分类配置
模式下，使用以下命令：
os-family os-family-name
l
os-family-name– 指定操作系统族名称：
l
预定义：指定预定义操作系统族名称，用户可通过在os-family参数后使用Tab键，查看完整的预
定义操作系统族列表。
l
自定义：如需指定自定义操作系统族名称，直接输入操作系统族名称，范围是1到63个字符。
在设备分类配置模式下，使用该命令no的形式删除指定的操作系统族：
no os-family
配置设备分类的操作系统版本
配置设备分类的操作系统版本，选择预定义操作系统版本或者指定自定义操作系统版本名称，在设备分类配
置模式下，使用以下命令：
os-version os-version-name
l
os-version-name– 指定操作系统版本名称：
l
预定义：指定预定义操作系统版本名称，用户可通过在os-version参数后使用Tab键，查看完整
的预定义操作系统版本列表。
l
自定义：如需指定自定义操作系统版本名称，直接输入操作系统版本名称，范围是1到127个字
符。
在设备分类配置模式下，使用该命令no的形式删除指定的操作系统版本：
no os-version
查看设备分类配置信息
用户可以在任何模式下使用以下命令查看设备分类配置信息：
show device-group device-group-name
l
show device-group – 显示所有设备分类的具体配置信息。
l
device-group-name – 显示指定名称的设备分类配置信息。

<!-- 来源页 2394 -->
查看设备映射IP地址
用户可以在任何模式下使用以下命令查看指定名称的设备分类的映射IP地址列表：
show device-group device-group-name ip-list
l
device-group-name – 指定查看映射IP地址的设备分类名称。
查看指定IP地址所属设备分类
用户可以在任何模式下使用以下命令查看指定的IP地址所属的设备分类：
show device-group mapping ip ipv4-address / ipv6-address
l
ipv4-address / ipv6-address – 指定查询所属设备分类的IPv4地址或IPv6地址。

<!-- 来源页 2395 -->
违规外联检测
在视频专网、电子政务和医疗物联网等应用场景中，内网终端可能因配备双网卡、连接其他WIFI/热点等情
况面临被黑客控制或非法向互联网传输数据的风险。而当其访问互联网时，其流量通常不经过防火墙，导致
防火墙无法检测出此风险行为。针对以上应用场景的问题，系统提供违规外联检测功能。该功能可对未经授
权访问互联网且流量不经过防火墙的终端设备、或未经授权访问互联网的网关设备的行为进行检测，达到有
效发现并阻断非法外联行为的效果，为网络安全提供坚实保障。
违规外联检测在CLI的配置包含：
l "网关违规外联检测" 在第2393页
l "终端违规外联检测" 在第2394页
l "查看违规外联检测配置和记录" 在第2399页
网关违规外联检测
开始之前
l 阅读"违规外联检测" 在第2393页介绍。
l 阅读"配置监测对象" 在第871页介绍。
网关违规外联检测功能主要用于识别防火墙在未经授权时是否能非法访问互联网，帮助用户及时阻断内网的
非法外联行为，确保网络安全。该功能通过指定监测对象，使防火墙按照监测对象中设定的周期自动向特定
目标（如IP或主机）发送网络请求，并通过对应协议报文是否成功触达监测目标来检测防火墙是否连接公
网，同时记录违规外联行为的事件日志。
前置条件
请提前"配置监测对象" 在第871页，以便在配置网关违规外联检测时可快速进行选择。
进入违规外联检测配置模式
在全局配置模式下，使用以下命令，进入违规外联检测配置模式。
violate-outreach-detect
开启/关闭网关违规外联检测
默认情况下，该功能为关闭状态。开启网关违规外联检测功能，在违规外联检测配置模式下，使用以下命
令：
gateway-detect enable track track-name

<!-- 来源页 2396 -->
l
track-name - 指定监测对象。仅支持指定类型为“HTTP/ICMP/ICMPv6/ARP/NDP/DNS/TCP”协
议的监测对象。
提示: 建议一个监测目标为一个监测对象，以保证网关违规外联检测的准确性和有效性。
在违规外联检测配置模式下，使用以下命令，关闭网关违规外联检测功能：
gateway-detect disable
终端违规外联检测
终端违规外联检测功能主要用于监控和识别内网终端设备（如IoT设备）在未经授权时，通过多网卡或WiFi
等途径非法访问互联网的行为，这一功能对于视频专网、电子政务和医疗物联网等关键应用场景至关重要，
它不仅有助于防止数据泄露和抵御黑客攻击，还能为网络安全管理提供重要的审计和追查手段。
该功能通过在山石云平台上部署公网服务器和违规外联管理平台，与防火墙协同工作，实现对内网终端设备
非法外联行为的有效检测。公网服务器负责接收防火墙触发终端发送的探测数据，而违规外联管理平台则用
于注册防火墙设备、激活违规外联功能和记录内网终端违规外联行为的详细信息。通常情况下，当内网终端
设备尝试访问互联网时，这些流量会绕过防火墙，使得防火墙无法直接进行检测。通过预置公网服务器，防
火墙能够触发内网终端设备访问这些服务器。一旦预置公网服务器接收到内网终端设备的访问请求，则表明
该终端存在违规外联行为，违规外联管理平台将记录该行为的详细信息，以便用户进行追查和处理。
终端违规外联检测功能分为主动探测和被动探测两种方式。
l 主动探测模式：防火墙会按照设定的周期主动向终端设备发送源地址为预置公网服务器的探测报文，如果预置公
网服务器接收到该探测报文，则表明该终端存在违规外联行为，同时违规外联管理平台将记录该行为的详细信
息。
该模式下，终端违规外联探测目标（即检测对象）包含两类来源：一是从网络会话流量中获取的源IP地
址，作为优先探测目标；二是从SNMP ARP-MIB表中获取的IP地址，作为次优先探测目标。系统以预先
配置的检测对象地址范围为筛选条件，从上述两类来源中提取符合范围的IP作为探测目标；当会话流量
中获取的IP数量未达到系统规格上限时，自动使用SNMP ARP-MIB表中符合范围的IP地址进行补充，以
实现探测覆盖范围最大化。
检测周期默认为30分钟，用户可根据需求自行配置。

<!-- 来源页 2397 -->
l 被动探测模式：防火墙在处理终端设备对内网服务器的访问请求时，会在其响应报文中添加预置公网服务器的地
址。终端设备接收到该响应报文后，会重定向访问预置公网服务器，如果预置公网服务器接收到访问请求，则表
明该终端存在违规外联行为，同时违规外联管理平台将记录该行为的详细信息。
被动探测模式下，同一个IP地址的终端在检测周期内只检测一次，且检测周期默认为1小时。如需修改该模式的
检测周期，仅限于通过CLI命令来执行，具体请使用endpoint-detect mode passive enable period timevalue命令重新调整指定周期。
注意: 在终端数量庞大的情况下，启用终端违规外联的被动探测模式可能会对系统性能产生一定的
影响，因此建议谨慎启用该功能。

<!-- 来源页 2398 -->
配置终端违规外联检测
开始之前
l 阅读"违规外联检测" 在第2393页介绍。
l 阅读"终端违规外联检测" 在第2394页介绍。
用户可以通过命令行接口（CLI）和Web界面（WebUI）两种方式配置终端违规外联检测功能。为实现终端
违规外联行为的检测，用户需要激活终端违规外联检测功能，并在防火墙设备上配置检测对象、探测模式等
参数。
使用终端违规外联检测，可按照以下流程进行配置：
1. 进入违规外联检测配置模式
2. 激活终端违规外联检测功能
3. 配置违规外联检测对象
4. 配置探测模式
进入违规外联检测配置模式
在全局配置模式下，使用以下命令，进入违规外联检测配置模式。
violate-outreach-detect
激活终端违规外联检测功能
在使用终端违规外联检测功能之前，必须先激活终端违规外联检测功能。用户可通过将防火墙设备注册至违
规外联管理平台，激活终端违规外联检测功能，以便违规外联管理平台能够有效监控并记录防火墙设备所在
网络中的终端违规外联事件。
激活终端违规外联检测功能流程如下：
1. 在防火墙上获取设备识别码
2. 从违规外联管理平台获取外联激活码
3. 在防火墙上配置激活码
在防火墙上获取设备识别码
在任意模式下，通过执行show violate-outreach-detect命令，在显示结果的Check Code字段中获取设
备识别码。详见"查看违规外联检测配置和记录" 在第2399页。

<!-- 来源页 2399 -->
从违规外联管理平台获取外联激活码
从违规外联管理平台获取外联激活码，请按照以下步骤进行操作：
1. 在浏览器中输入违规外联管理平台的访问地址，使用山石云平台账号，登录违规外联管理平台。
违规外联管理平台访问地址：https://vod.hillstonenet.com.cn
2. 将获取的设备识别码，粘贴至违规外联管理平台的“设备识别码”文本框中，然后输入验证码。
3. 点击“生成激活码”按钮，获取外联激活码。
配置激活码
在违规外联检测配置模式下，使用以下命令，配置激活码：
endpoint-detect activecode active-code
l
active-code - 填入外联激活码，该激活码由违规外联管理平台通过设备识别码生成，包括设备SN、预
置公网服务器IP和端口、请求URL、违规外联管理平台地址等。在将防火墙注册至违规外联管理平台
时，需使用该激活码进行认证。如何获取激活码，详见从违规外联管理平台获取外联激活码。
在违规外联检测配置模式下，使用以下命令，删除激活码配置：
no endpoint-detect activecode active-code
配置违规外联检测对象
在违规外联检测配置模式下，使用以下命令，配置违规外联检测对象：

<!-- 来源页 2400 -->
endpoint-detect {ip ip-address/netmask | ip-range min-ip-address max-ip-address |
address address-book}
l
ip ip-address/netmask | ip-range min-ip-address max-ip-address | address addressbook - 指定需要进行违规外联行为检测的目标对象地址，即内网终端设备的地址。可以为IP地址/掩
码、IP地址范围或地址簿。
l
ip ip-address/netmask - 表示为IP地址/掩码。
l
ip-range min-ip-address max-ip-address - 表示为IP地址范围。
l
address address-book - 表示为地址簿。
在违规外联检测配置模式下，使用以下命令，删除指定检测对象配置：
no endpoint-detect {ip ip-address/netmask | ip-range min-ip-address max-ip-address |
address address-book}
配置探测模式
终端违规外联检测功能分为主动探测和被动探测两种方式，用户可根据需求选择开启任意模式。系统支持同
时开启多种探测模式，以提高系统检测的效果和准确性。
注意: 在终端数量庞大的情况下，启用终端违规外联的被动探测模式可能会对系统性能产生一定的
影响，因此建议谨慎启用该功能。
开启/关闭主动探测模式
默认情况下，该功能为关闭状态。启用后，防火墙会按照设定的周期主动向终端设备发送源地址为预置公网
服务器的探测报文，如果预置公网服务器接收到该探测报文，则表明该终端存在违规外联行为，同时违规外
联管理平台将记录该行为的详细信息。该模式的检测周期默认为30分钟，可根据用户需求自行配置。
在违规外联检测配置模式下，使用以下命令，开启终端违规外联主动探测模式，并指定检测周期：
endpoint-detect mode active enable [period time-value]
l
periodtime-value - 指定防火墙定时向终端发送探测报文的周期，取值范围为1到120分钟。系统默认
为30分钟。
在违规外联检测配置模式下，使用以下命令，关闭终端违规外联主动探测模式：
endpoint-detect mode active disable

<!-- 来源页 2401 -->
开启/关闭被动探测模式
默认情况下，该功能为关闭状态。启用后，防火墙在处理终端设备对内网服务器的访问请求时，会在其响应
报文中添加预置公网服务器的地址。终端设备接收到该响应报文后，会重定向访问预置公网服务器，如果预
置公网服务器接收到访问请求，则表明该终端存在违规外联行为，同时违规外联管理平台将记录该行为的详
细信息。
提示: 被动探测模式下，同一个IP地址的终端在检测周期内只检测一次，且检测周期默认为1小
时。
在违规外联检测配置模式下，使用以下命令，开启终端违规外联被动探测模式，并指定检测周期：
endpoint-detect mode passive enable [period time-value]
l
period time-value - 指定防火墙对同一个IP地址的终端进行违规外联行为检测的周期，取值范围为
1~120分钟。系统默认为60分钟。
在违规外联检测配置模式下，使用以下命令，关闭终端违规外联被动探测模式：
endpoint-detect mode passive disable
查看违规外联检测配置和记录
在任意模式下，使用以下命令，查看违规外联检测配置和记录：
show violate-outreach-detect [endpoint [active | passive]]
l
show violate-outreach-detect - 查看网关违规外联检测和终端违规外联检测配置信息。
l
endpoint - 查看终端违规外联检测功能在主动和被动探测模式下，所探测的全部终端IP地址及其最近一
次探测时间。
l
active - 仅查看主动探测模式下的终端IP地址及其最近一次主动探测时间。
l
passive - 仅查看被动探测模式下的终端IP地址及其最近一次被动探测时间。
示例：
hostname# show violate-outreach-detect
Gateway Detection: Enable （显示网关违规外联检测功能的启用状态）
Gateway Detection Track: 2.2.22.2 （显示网关违规外联检测功能的监测对象）
Endpoint Active Detection: Enable （显示终端违规外联主动探测的启用状态）
Endpoint Active Detection Period: 30 minutes（显示终端违规外联主动探测的周期）

<!-- 来源页 2402 -->
Endpoint Passive Detection: Enable（显示终端违规外联被动探测的启用状态）
Endpoint Passive Detection Period: 60 minutes （显示终端违规外联被动探测的周期）
Check Code: xxx== （显示防火墙设备的识别码）
Active Code: xxx== （显示防火墙注册的激活码）
Detection Object Address: 1.1.1.1（显示终端违规外联检测的对象）
