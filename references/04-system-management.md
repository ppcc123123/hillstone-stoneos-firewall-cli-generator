# 系统管理

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 7 系统管理
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 670 -->
7 系统管理
本章节包含以下内容：
l "配置主机名称" 在第670页
l "通过WebUI免密登录命令行界面" 在第671页
l "配置管理员" 在第680页
l "许可证管理" 在第763页
l "配置可信主机" 在第693页
l "用户配置" 在第787页
l "配置管理接口" 在第696页
l "配置存储设备" 在第808页
l "配置文件管理" 在第731页
l "Docker管理操作" 在第906页
l
"密码卡管理" 在第813页
l "配置系统重启" 在第719页
l "StoneOS版本升级" 在第771页
l "配置SNMP" 在第822页
l "配置NETCONF" 在第835页
l "连接HSM" 在第839页
l "NTP介绍" 在第703页
l "配置时间表功能" 在第866页
l "配置监测对象" 在第871页
l "应用层强制检查" 在第883页
l "系统监控报警" 在第884页
l "CPU Cache Error监控" 在第887页
l "调整系统最大并发连接数" 在第894页
l "连接山石云平台配置" 在第857页

<!-- 来源页 671 -->
l "配置NetBIOS名字解析功能" 在第899页
l "配置WebUI登录时浏览器页签标题" 在第724页
l "配置系统信息显示语言" 在第729页
l "配置RESTful API上传文件的接口" 在第901页
l "清除指示灯告警提示" 在第902页
l "指定SSH访问时RSA密钥位数" 在第725页
l "配置设备作为SSH/Telnet客户端" 在第726页
l "Deny Session功能" 在第903页
l "切换SIOM模块工作模式" 在第914页
l
"配置下发的最长重试时间" 在第917页
l
"开启IP分片报文在IOM模块或SIOM模块的重组功能" 在第916页

<!-- 来源页 672 -->
配置主机名称
有些情况下，用户的网络环境中会配有一台以上设备，为区分这些设备，就需要为每一台设备指定不同的名
称。设备的默认名称是其平台名称。通过CLI配置设备名称，在全局配置模式输入以下命令：
hostname host-name
l
host-name - 指定设备名称。长度范围是1到63个字符。执行该命令后，命令行提示符也会变为新的
设备的名称。在全局配置模式下使用no hostname命令恢复设备的默认名称。
以下是配置设备名称的命令示例：
hostname# configure( 进入全局配置模式)
hostname(config)# hostname hillstone
hillstone(config)#
配置主机名称显示长度
用户可以配置系统可显示的主机名称长度，超过配置长度部分的主机名称用“~”来代替显示。配置主机名
称显示长度，在全局配置模式下，使用以下命令：
hostname-display-length length
l
length – 指定系统可显示的主机名称长度，取值范围为1到63个字符。默认值为16个字符，即当设备主
机名称长度超过16个字符时，超过16个字符部分的主机名称用“~”来代替显示。
在全局配置模式使用该命令no的形式恢复系统默认配置：
no hostname-display-length
查看主机名称显示长度
在任何模式下，使用以下命令查看主机名称显示长度
show hostname-display-length

<!-- 来源页 673 -->
通过WebUI免密登录命令行界面
为提高设备运维的便利性，系统支持通过WebUI免密登录命令行界面功能。当用户通过Web方式登录设备
后，可以点击系统右上角的命令行图标，弹出命令行界面。在弹出界面中，用户可以直接通过命令行对设备
进行配置，无需再输入用户名和密码。
注意: 使用该功能时：
l
推荐使用Microsoft Edge或者Chrome 110及更高版本浏览器访问设备的WebUI界面。
l
设备的管理口(部分设备有默认的MGT口)、可信主机、管理员需要开启HTTP或HTTPS服务。
l
如果用户为自定义角色管理员，需要开启管理员角色的CLI权限。如何开启管理员角色的CLI权
限，请参阅指定管理员角色的权限。
l
登录或退出令行界面，会产生相应的事件日志。
配置命令行窗口最大可连接数
用户可配置命令行窗口的最大可连接数，即对于同一台设备，可以同时打开命令行窗口的最大数量。进行该
配置，在全局配置模式下，使用以下命令：
webconsole max-clients number
l
number - 指定命令行窗口的最大可连接数量。不同平台可配置的命令行窗口最大可连接数量不同，请
以实际情况为准。默认情况下，命令行窗口最大可连接数量为可以配置的最大值。
在全局配置模式下，使用no webconsole max-clients命令取消命令行窗口最大可连接数量的配置并恢复
默认值。
查看命令行窗口配置信息
在任何模式下，使用以下命令查看通过WebUI免密登录命令行界面的配置信息，包括命令行窗口的当前已连
接数和最大可连接数量：
show webconsole

<!-- 来源页 674 -->
SD-WAN邮件开局
在SD-WAN场景下部署防火墙设备时，需要运维人员到现场完成设备的配置部署。当设备数量较多，分布较
广时，运维人员需要在每台设备上手动进行配置，会影响设备部署效率，也增加了设备运维成本。因此，系
统提供邮件开局功能，管理员在HSM上配置并发送开局邮件，开局人员通过访问开局邮件中的URL链接启动
开局流程，实现设备的免现场配置和部署，有效降低开局部署成本。
开始之前
l 管理员已在HSM端完成配置并发送开局邮件。关于如何配置开局邮件，请参阅《山石网科安全管理平台WebUI手
册》的“SD-WAN场景下的ZTP开局”章节。
l 开局人员确认已成功接收到开局邮件，并联系管理员获取邮件URL密钥。
l 开局人员确认设备已上架完毕并成功开机。
开局人员需按照以下步骤进行邮件开局：
1. 检查开局邮件中的设备SN与待开局的防火墙设备SN是否一致。如果一致，则继续进行后续步骤；如果不一致，
则需联系管理员重新发送开局邮件。
2. 使用以太网网线将PC机与防火墙设备的MGT口进行连接（若无，使用e0/0接口）。在PC机中，将以太网属性的
IP地址设置为与192.168.1.1/24同网段的IP地址，例如192.168.1.2/255.255.255.0。
对于A200W和A200WG4设备，也可以通过连接名称为“WIFI0/0_xxxxxx”的默认WLAN接入设备（“xxxxxx”
为防火墙设备SN号后六位），该WLAN安全模式为未加密，无需输入密钥。
3. 开局人员访问开局邮件中的URL链接，进入防火墙设备的登录页面。
4. 输入防火墙设备的用户名和密码（默认为hillstone/hillstone），然后点击“登录”，进入<邮件开局>页面。
5. 输入已获取的邮件URL密钥，然后点击“确定”，进入<配置信息>页面查看开局配置信息。开局配置信息主要包
括设备WAN口/LAN口配置、DNS配置、NTP配置、连接集中管理配置等。
6. 点击“确定”，防火墙设备会根据开局配置信息自动完成配置，并将设备注册到HSM上。

<!-- 来源页 675 -->
DHCP零配置开局
型号说明：
l
A系列所有型号设备
l
B系列所有型号设备
l
K系列部分型号设备：SG-6000-K3280/K2680/K2580/K2560/K2380
l
X系列部分型号设备：SG-6000-X8180
设备作为DHCP客户端时，系统支持DHCP零配置开局，即出厂设备或空配置设备在上电启动后，通过DHCP
方式自动获取指定的开局文件（包括配置文件、软件版本文件），并将其设置为设备启动时的开局文件，实
现设备的免现场配置和部署，提升部署效率。
进行DHCP零配置开局之前，需要先部署DHCP服务器和TFTP服务器，并在DHCP客户端和DHCP服务器上分
别配置相应的DHCP选项。出厂设备或空配置设备上电启动后，会自动进入DHCP零配置开局流程，通过
DHCP方式获取开局文件并重启完成自动部署。DHCP零配置开局流程如下：
1. 获取DHCP信息。
设备向DHCP服务器发送请求报文，DHCP服务器向设备返回应答报文。设备通过解析该应答报文获取IP地址、默
认网关等信息。
2. 解析应答报文并下载xml描述文件。
设备解析DHCP服务器的应答报文，获取xml描述文件所在的TFTP服务器地址和xml文件下载路径，然后从相应
的TFTP服务器中下载对应的xml描述文件。
3. 解析xml描述文件并下载开局文件。
设备解析下载的xml描述文件，获取开局文件所在的TFTP服务器地址和开局文件下载路径，然后从相应的TFTP服
务器中下载开局文件，包括配置文件和软件版本文件。其中，配置文件以设备SN号命名，例如
“5931844225000750.cfg”。
4. 自动重启设备。
开局文件下载成功后，系统将其设置为设备启动时的开局文件，设备自动重启完成后即可完成开局。

<!-- 来源页 676 -->
系统管理
介绍管理员、管理员角色、可信主机、管理接口、系统时间、NTP密钥、设置及操作、安全认证管理、存储
管理、密码重置管理。
l 管理员：设备的管理员根据角色的不同，对系统可执行的管理和配置权限不同。系统支持预定义管理员角色和自
定义管理员角色。
l 管理员角色：设备的管理员根据角色的不同，对系统可执行的管理和配置权限不同。系统支持预定义管理员角色
和自定义管理员角色。系统预定义的管理员角色不可被删除和编辑。用户可自定义管理员角色满足实际需求。
l 可信主机：设备使用可信主机来进一步保证系统安全。管理员可以通过指定IP地址/IP地址范围，或同时指定IP地
址/IP地址范围和MAC地址/MAC范围来匹配可信主机，即在指定范围内的主机为可信主机。只有可信主机才可以
对设备进行管理。
l 管理接口：设备支持Console、Telnet、SSH以及Web方式的访问。用户可以配置各种访问方式的超时时间、端
口号、HTTPS的PKI信任域以及证书认证信任域。使用Telnet、SSH、HTTP或者HTTPS方式登录设备时，如果在
一分钟内连续三次登录失败，系统会将登录失败的IP地址锁定两分钟。被锁定的IP地址在两分钟内不能建立与设
备的连接。
l 系统时间：介绍系统时间的配置，包括配置系统时间和通过NTP服务器同步系统时间。设备的系统时间影响到
VPN隧道的建立和时间表的时间，因此系统时间的精确性十分重要。为保证设备系统能够一直保持精确时间，设
备允许用户通过NTP来使系统时间与网络上的NTP服务器同步。
l 设置及操作：介绍系统相关设置，包括设置系统语言、配置管理员认证服务器、配置主机名称、设置密码策略、
重启设备和导出系统调试信息。
l 安全认证管理：启用安全认证管理功能，通过短信或邮箱二次认证的方式登录设备。
l 存储管理：存储管理功能通过限制各个功能占用磁盘空间的大小来管理系统存储空间。当系统存储比例或存储空
间达到指定的阈值时，系统将执行指定的动作，从而控制系统存储。用户还可以在该页面查看并设置报表、日志
等存储空间大小。
l 密码重置管理：通过密保问题重置管理员密码功能可以让用户修改密码时无需知道旧密码，从而更加便捷地重置
密码。若配置并启用了该功能，当管理员用户通过console口登录时，在输入正确的用户名，且连续三次输入错
误密码的情况下，系统会提示用户可以通过密保修改密码。

<!-- 来源页 677 -->
管理员权限
系统默认预定义如下四类管理员角色，这四类管理员角色不可被删除和编辑：
l 系统管理员（admin）：拥有读、执行和写权限，可以在任何模式下对设备所有功能模块进行配置，可通过
WebUI或命令行show命令查看当前或者历史配置信息、在执行模式下运行import、export和save等命令以及在
任何模式下对设备所有功能模块进行配置。。
l 系统操作员（Operator）：拥有读、执行和部分写权限，可以修改除管理员配置、重启设备、恢复出厂设置以及
升级版本以外的其他功能模块配置，可通过WebUI或通过show命令查看当前或者历史配置信息、但是不能查看
日志信息，以及在执行模式下运行部分执行命令。
l 系统审计员（Auditor）：只可以对日志信息进行操作，包括查看、导出和清除。
l 系统管理员（只读）（Administrator-read-only）：拥有读和部分执行权限，可通过WebUI或show命令查看
当前或者历史配置信息，可以在执行模式下运行export命令。
下表为管理员的详细权限列表：
功能
权限
系统管理员
系统管理员
（只读）
安全操作员
安全审计员
配置（包括保存配置）
√
χ
√
χ
管理员配置
√
χ
χ
χ
恢复出厂配置
√
χ
χ
χ
删除配置文件
√
χ
√
χ
回退起始配置信息
√
χ
√
χ
重启设备
√
χ
χ
χ
查看配置信息
√
√
√
χ
查看日志信息
√
√
χ
√
修改当前管理员密码
√
√
√
√
import命令
√
χ
√（除系统升级
外）
χ
export命令
√
√
√
√
clear命令
√
√
√
√
ping/traceroute命令
√
√
√
χ
debug命令
√
χ
√
χ

<!-- 来源页 678 -->
功能
权限
系统管理员
系统管理员
（只读）
安全操作员
安全审计员
debug命令
√
√
√
χ
exec命令
√
√
√
√
terminal width命令
√
√
√
√
对于A系列SG-6000-A2000-GM、SG-6000-A3000-GM设备，系统默认预定义如下三类管理员角色，这
三类管理员角色不可被删除和编辑：
l 系统管理员（admin）：主要负责维护系统运行，可配置的功能包括：配置与网络和系统的相关信息，以及创建
系统管理员子账号。默认用户名/密码为：“admin /Security@123”。
l 安全操作员（operator）：主要负责配置系统安全防护业务，可配置设备上所有的防护功能，如：配置安全策
略、威胁防护和攻击防护，以及创建安全操作员子账号等。默认用户名/密码为：operator /Security@123”
l 安全审计员（auditor）：主要负责对系统管理员和安全操作员的操作日志进行审查分析，可查看配置日志，以
及创建安全审计员子账号。默认用户名/密码为：“auditor /Security@123”。
注意:
l
设备拥有一个默认系统管理员“hillstone”，用户可以对系统管理员“hillstone”进行编
辑。
l
除了系统管理员，其他角色的管理员不能进行管理员配置，只能修改自身密码。
l
安全审计员可以管理一种或多种日志信息，管理日志类型需要系统管理员配置。
三类管理员在WebUI界面上的功能权限如下：
Web一级页面
Web二级页面
Web三级页面
系统管理员（admin）

<!-- 来源页 679 -->
Web一级页面
Web二级页面
Web三级页面
系统
系统信息
——
设备管理
管理员、系统时间、NTP密钥
配置文件管理
配置文件列表、当前系统配置
SNMP
SNMP代理、SNMP主机、Trap主机、V3用户组、V3用户
SNMP服务器
——
升级管理
版本升级、特征库升级
许可证
许可证
邮件服务器
——
HA
——
集中管理
——
PKI
密钥、信任域、信任域证书、可信根证书
诊断工具
测试工具
网络
安全域
——
MGT接口
——
接口
——
DNS
DNS服务器、DNS代理、解析配置、缓存、NBT缓存
DHCP
——
DDNS
——
Virtual Wire
——
虚拟路由器
虚拟路由
虚拟交换机
——
路由
目的路由、目的接口路由、源路由、源接口路由、策略路由、RIP、
OSPF
出站负载均衡
规则、模板
入站负载均衡
——
VPN
IPSEC VPN、SSL VPN、L2TP VPN
802.1X
802.1X、在线用户、全局配置
Web认证
Web认证、在线用户
应用层网关
——
全局网络参数
全局网络参数、防护模式
安全操作员（operator）
首页
——

<!-- 来源页 680 -->
Web一级页面
Web二级页面
Web三级页面
iCenter
——
监控
用户监控
概览、用户详情、地址簿详情、设置需要统计的地址簿
应用监控
概览、应用详情、应用组详情、设置需要统计的应用组
云应用监控
概览、云应用详情
共享接入监控
——
URL访问
概览、用户/IP、URL、URL类别
链路状态监控
链路状态、链路配置
管道监控
管道详情
系统监控
概览、在线IP数、会话列表
设备监控
概览、设备列表
关键字阻断
概览、网页关键字、邮件内容、Web外发信息、用户/IP
应用阻断
概览、应用、用户/IP
认证用户
——
监控配置
——
自定义监控
——
报表
报表汇总、自定义任务、快捷任务
日志
事件日志、网络日志、共享接入日志、威胁日志、会话日志、PBR
日志、NAT日志、URL日志、文件过滤日志、内容过滤日志、设备日
志、日志管理、日志配置
策略
安全策略
——
NAT
源NAT、目的NAT 、SLB服务器池状态、SLB服务器状态
iQoS
策略、配置
会话限制
——
共享接入
——
ARP防护
ARP绑定、ARP检查、DHCP监控、主机防御
SSL代理
——
黑白名单
边界流量过滤、域名管控、URL管控、全局检索、配置

<!-- 来源页 681 -->
Web一级页面
Web二级页面
Web三级页面
对象
地址簿
——
域名簿
——
服务簿
服务、服务组
应用簿
应用、应用组、应用过滤组、静态特征规则
SLB服务器池
——
时间表
——
AAA服务器
——
SSO Server
SSO Radius、AD Scripting
SSO Client
SSO Monitor、AD Polling
用户
本地用户、LDAP用户、Active Directory用户、用户绑定
角色
角色、角色映射、角色组合
监测对象
——
病毒过滤
模板、配置
入侵防御
模板、特征列表、配置、白名单
僵尸网络防御
模板、地址库、配置
URL过滤
模板、黑白名单分类
NetFlow
模板、配置
数据安全
文件过滤、内容过滤
访问控制
模板
网络
安全域
系统
设备管理
管理员、可信主机、管理接口、设置及操作、存储管理
安全审计员（auditor）
监控
日志
配置日志
系统
设备管理
管理员

<!-- 来源页 682 -->
配置管理员
设备的管理员根据角色的不同，对系统可执行的管理和配置权限不同。系统支持预定义管理员角色和自定义
管理员角色。用户可自定义管理员角色，指定管理员角色对CLI的权限。
本节包含以下内容：
l 新建管理员角色
l 指定管理员角色的权限
l 指定管理员角色的描述信息
l 创建管理员
l 配置管理员角色
l 配置管理员密码
l 配置管理员访问方式
l 配置管理员登录限制
l 配置默认管理员登录操作
l 显示管理员角色的配置
l 显示管理员配置
新建管理员角色
新建管理员角色，在全局配置模式下，使用如下命令：
admin role role-name
l
role-name – 指定管理员角色的名称。长度范围是4到95个字符。执行该命令后，系统创建指定名称的
管理员角色，并且进入管理员角色配置模式；如果指定的管理员角色名称已经存在，则直接进入管理员
配置模式。
使用no admin role role-name命令删除指定的管理员角色。
指定管理员角色的权限
指定管理员角色的CLI权限，在管理员角色配置模式下，使用如下命令：
cli-privilege all {rw | none}

<!-- 来源页 683 -->
l
rw | none – rw表示管理员角色对全部CLI具有读写权限；none表示管理员角色不具有CLI权限，不可使
用CLI命令。
指定管理员角色的描述信息
指定管理员角色的描述信息，在管理员角色配置模式下，使用如下命令：
description description
l
description – 指定描述信息标示此管理员角色。长度范围是0到255个字符。
使用no description命令删除描述信息。
创建管理员
创建管理员并进入管理员配置模式，请在全局配置模式下输入以下命令：
admin user user-name
l
user-name - 指定管理员名称。长度范围是4到31个字符。执行该命令后，系统创建指定名称的管理
员，并且进入管理员配置模式；如果指定的管理员名称已经存在，则直接进入管理员配置模式。
在全局配置模式下使用no admin user user-name命令删除指定的管理员。
在管理员配置模式下，用户可以配置管理员角色、管理员密码、访问方式和系统审计员可管理日志类型。
配置管理员角色
配置管理员角色，在管理员配置模式下输入以下命令：
role {admin | operator |auditor |admin-read-only}
l
admin - 指定管理员角色为系统管理员（Administrator）。
l
operator - 指定管理员角色为系统操作员（Operator）。
l
auditor - 指定管理员角色为系统审计员（Auditor）。
l
admin-read-only - 指定管理员角色为系统管理员（只读）（Administrator-read-only）。
配置管理员密码
设备具有密码策略。请为管理员指定符合密码策略的密码。指定管理员密码，在管理员配置模式下，输入以
下命令配置管理员的密码：
password password
l
password – 指定管理员的密码。范围是4到31个字符。

<!-- 来源页 684 -->
在管理员配置模式下使用no password命令取消管理员密码的配置。
系统允许当前登录的系统操作员、系统审计员或系统管理员（只读）修改自身密码，在任意模式下使用以下
命令：
exec admin user password update password
l
password – 指定管理员的新密码，为4到31个字符的字符串。
注意: 系统管理员可以修改所有管理员的密码。
配置管理员密码策略
管理员密码策略中可以配置管理员密码的复杂度。密码复杂度包括密码的总长度、密码中组成元素的长度以
及密码的有效期。其中组成元素包括以下4种类型：
l 大写字母（从A到Z）。
l 小写字母（从a到z）。
l 数字（从0到9）。
l 其他可见字符。例如：分号（；）、斜杠（/）等字符（仅支持半角字符）。
进入管理员密码策略配置模式
管理员密码策略的配置需要在管理员密码策略配置模式下进行。进入管理员密码策略配置模式，在全局配置
模式下，使用以下命令：
password-policy
开启/关闭管理员密码的复杂度检测功能
如果系统默认的管理员密码复杂度设置无法满足安全性的需求，用户可以自定义密码复杂度。自定义密码复
杂度前，用户必须先开启复杂度检测功能。
开启或关闭管理员密码的复杂度检测功能，在管理员密码策略配置模式下，使用以下命令：
admin complexity {enable | disable}
l
enable | disable – 开启或关闭管理员密码的复杂度检测功能。默认情况下，管理员密码的复杂度检测
功能为关闭状态。开启后，该功能默认要求密码中必须包含以下各项：1个大写字母、1个小写字母、1个
数字和1个特殊字符（例如“@”等）。2个大写字母、2个小写字母、2个数字和2个特殊字符（例如
“@”等）。

<!-- 来源页 685 -->
自定义密码组成元素长度
用户自定义密码组成元素长度，在管理员密码策略配置模式下，使用以下命令：
admin {capital-letters | non-alphanumeric-letters | numeric-characters | small-letters} value
l
capital-lettersvalue – 指定管理员密码中大写字母的最小长度。默认值是1个字符，范围是0到16。
l
non-alphanumeric-letters value – 指定管理员密码中其他可见字符（特殊字符）的最小长度。默认
值是1个字符，范围是0到16。
l
numeric-characters value – 指定管理员密码中数字的最小长度。默认值是1个字符，范围是0到16。
l
small-letters value – 指定管理员密码中小写字母的最小长度。默认值是1个字符，范围是0到16。
l
capital-letters value – 指定管理员密码中大写字母的最小长度。默认值是2个字符，范围是0到16。
l
non-alphanumeric-letters value – 指定管理员密码中其他可见字符（特殊字符）的最小长度。默认
值是2个字符，范围是0到16。
l
numeric-characters value – 指定管理员密码中数字的最小长度。默认值是2个字符，范围是0到16。
l
small-letters value – 指定管理员密码中小写字母的最小长度。默认值是2个字符，范围是0到16。
自定义管理员密码的最小长度
用户自定义管理员密码的最小长度，在管理员密码策略配置模式下，使用以下命令：
admin min-length length-value
l
min-length length-value – 指定管理员密码的最小长度。默认值是4个字符，范围是4到16个字符。
当开启管理员密码的复杂度检测功能后，最小长度的默认值为8个字符，范围是8到16个字符。
注意: 无论管理员密码的复杂度检测功能是否开启，用户都可以配置管理员密码的最小长度，以提
高密码的安全性。
自定义管理员密码的有效期
密码的有效期用来限制管理员密码的使用时间。当用户登录时，如果用户输入已经过期的密码，系统将提示
重新设置密码，回车后再次输入新密码。如果输入的新密码不符合密码复杂度要求，或连续两次输入的新密
码不一致，系统将要求用户重新输入。连续输入三次不符合要求的密码系统将会断开连接，用户重新登录时
系统仍要求用户设置新密码。用户设置的新密码可以和旧密码相同。用户自定义管理员密码的有效期，在管
理员密码策略配置模式下，使用以下命令：

<!-- 来源页 686 -->
admin password-expiration value
l
password-expiration value – 指定管理员密码的有效期。单位为天，范围是0到365天，默认值是
7。单位为天，范围是0到365天，默认值为0，表示不对有效期进行限制。在管理员密码策略配置模式
下，使用no admin complexity命令恢复管理员密码的复杂度检测功能的默认情况。
开启/关闭历史密码检查功能
开启或关闭历史密码检查功能，在管理员密码策略配置模式下，使用以下命令：
admin history-password-check {enable | disable}
l
enable | disable – 开启或关闭历史密码检查功能。默认情况下，历史密码检查功能为关闭状态。
配置历史密码检查功能
开启历史密码检查功能后，用户在修改密码时，系统将进行历史密码的校验，新密码不能与前n个历史密码
重复。配置历史密码检查功能，在管理员密码策略配置模式下，使用以下命令：
admin history-password-records count
l
count - 指定历史密码的检查个数。取值范围为3到8个，默认值是5，即新密码不能与前5个历史密码重
复。
开启/关闭用户名密码一致性检查功能
为增强账户的安全性，系统提供用户名密码一致性检查功能。开启该功能后，系统将不允许设置与用户名相
同的密码。当用户配置管理员的用户名密码时，系统会检查用户名与密码是否相同，只有在用户名与密码不
相同的情况下，才能配置成功。
开启或关闭用户名密码一致性检查功能，在管理员密码策略配置模式下，使用以下命令：
admin username-password-same-check {enable | disable}
l
enable | disable – 开启或关闭用户名密码一致性检查功能。默认情况下，该功能为关闭状态。
显示管理员密码策略信息
用户可以在任何模式下，随时使用show命令查看管理员密码策略信息：
show password-policy
配置通过密保问题重置管理员密码功能
通过密保问题重置管理员密码功能可以让用户修改密码时无需知道旧密码，从而更加便捷地重置密码。若配
置并启用了该功能，当用户通过console口登录时连续三次错误输入用户名或密码，系统会提示用户可以通

<!-- 来源页 687 -->
过密保修改密码。
配置密保问题，在全局配置模式下，使用以下命令：
admin reset-password question {custom value | predefined {question1 | question2 |
question3}}
l
question custom value–配置自定义密保问题，只支持英文字母、数字、英文特殊字符（”除外），
不支持中文。当输入字符串时，请用双引号引住整个密保问题字符串。取值范围为1-256个字符。
l
question predefined question1– 配置密保问题为系统预定义的问题1。question1指定的密保问题
为“What is your aspiration?”。
l
question predefined question2– 配置密保问题为系统预定义的问题2。question2指定的密保问题
为“What is your most impressed day?”。
l
question predefined question3– 配置密保问题为系统预定义的问题3。question3指定的密保问题
为“What do you like best?”。
配置密保问题答案，在全局配置模式下，使用以下命令：
admin reset-password answer value
l
answer value–配置密保问题答案，只支持英文字母、数字、英文特殊字符（”除外），不支持中文。
当输入字符串时，请用双引号引住整个密保问题答案字符串。取值范围为1-256个字符。
启用/禁用通过密保问题重置密码功能，在全局配置模式下，使用以下命令：
admin reset-password {enable | disable}
l
enable–启用通过密保问题重置密码功能。若要启用通过密保问题重置密码功能，用户需要先配置密保
问题以及密保问题答案。
l
disable–禁用通过密保问题重置密码功能。
删除密保问题以及密保问题答案，在全局配置模式下，使用以下命令：
no admin reset-password {question | answer}
l
question–同时删除密保问题以及密保问题答案。用户需要先禁用通过密保问题重置密码功能才能进行
删除。
l
answer–单独删除密保问题答案。用户需要先禁用通过密保问题重置密码功能才能进行删除。
查看通过密保问题重置管理员密码功能的信息，包括启用/禁用状态、密保问题以及密保问题答案。在任意模
式下，使用以下命令：
show admin reset-password

<!-- 来源页 688 -->
配置管理员访问方式
默认情况下，新建的管理员不可以访问Hillstone设备进行配置。用户需指定管理员的访问方式。系统只允
许系统管理员指定其他角色的管理员的访问方式。在管理员配置模式下，输入以下命令配置管理员的访问方
式：
access {console | http | https | ssh | telnet | netconf | webconsole | any}
l
console – 指定管理员通过Console访问。
l
http – 指定管理员通过HTTP访问。
l
https – 指定管理员通过HTTPS访问。
l
ssh – 指定管理员通过SSH访问。
l
telnet – 指定管理员通过Telnet访问。
l
netconf – 指定管理员通过NETCONF访问。
l
webconsole - 指定管理员通过WebConsole访问。
l
any – 指定管理员可以通过以上任何一种方式访问。
使用多条该命令为管理员指定多种访问方式。
使用no access {console | http | https | ssh | telnet | netconf
| webconsole | any}命令取消指定的
访问方式。
注意: 开启“Telnet”和“HTTP”访问方式时，系统会弹出安全提示。
配置管理员登录限制
管理员登录设备时，密码输入错误次数超过设定次数时，系统会在指定时间内禁止使用该用户IP或用户账号
登录设备。
基于用户IP地址指定禁止访问时长，在全局配置模式下，使用以下命令：
admin lockout-duration time
l
lockout-duration time – 指定禁止访问时长。单位为分钟。范围是1到65535。默认值是2分钟。
使用no admin lockout-duration命令恢复管理员登录时长默认配置。
基于用户账号指定禁止访问时长，在全局配置模式下，使用以下命令：
admin lockout-duration-user time

<!-- 来源页 689 -->
l
lockout-duration-user time – 指定禁止访问时长。单位为分钟。范围是1到65535。默认值是2分
钟。
使用no admin lockout-duration-user命令恢复管理员登录时长默认配置。
基于用户IP地址指定密码输入错误最大次数，在全局配置模式下，使用以下命令：
admin max-login-failure times
l
max-login-failure times – 指定管理员密码输入错误最大次数。默认值是3，范围是1到5。
使用no admin max-login-failure命令恢复管理员密码输入错误次数默认配置。
基于用户账号指定密码输入错误最大次数，在全局配置模式下，使用以下命令：
admin max-login-failure-user times
l
max-login-failure-user times – 指定管理员密码输入错误最大次数。默认值是3，范围是1到5。
使用no admin max-login-failure-user命令恢复管理员密码输入错误次数默认配置。
注意: 只允许系统管理员配置管理员登录限制。
配置管理员的最大数量
系统支持配置管理员的最大数量。配置后，系统支持创建的管理员的最大数量将为指定数值，用户可根据需
要进行调整。调整后，需将设备重启，指定值才能生效。配置管理员的最大数量，在全局配置模式下，使用
以下命令：
capacity management max-administrative-users capacity-num
l
capacity-num - 指定管理员最大数量的数值，取值范围为1-128。
使用no capacity management max-administrative-users命令恢复默认的管理员最大数量的数值。
不同平台的默认值不同，请以实际为准。
注意: 该命令为本地配置命令，不支持HA同步。在HA环境下，若主设备与备设备上设置的管理员
最大数量不同，HA状态显示正常，但系统会定时发出告警信息。
配置默认管理员登录操作
系统拥有一个默认管理员“hillstone”以及对应的默认密码“hillstone”，当管理员使用默认管理员和默
认密码登录设备时，可能会存在被破解的风险。针对该问题，系统将会在管理员使用默认管理员和密码初次

<!-- 来源页 690 -->
登录设备时提示用户修改默认密码。修改后，用户需要使用新的密码重新登录系统。用户可以按照提示进行
操作：
Administrator is logging in with default account and password:
Please change your password:
new password: ******（输入新密码）
Please input the new password again
new password: ****** （再次输入新密码）
注意: 在HA Active-Passive （A/P）模式下，备设备不支持该功能，可以使用默认用户直接登
录。
开启默认管理员Telnet及HTTP登录类型
系统默认管理员“hillstone”的Telnet和HTTP登录类型默认为关闭状态，开启Telnet和HTTP登录类型，
请见配置管理员访问方式。
显示管理员角色的配置
显示管理员角色的配置：show admin role [role-name]
显示管理员配置
用户可以在任何模式下，随时使用show命令查看管理员配置：
l
显示管理员信息：show admin user
l
显示管理员具体配置信息：show admin user user-name
l
显示管理员禁止访问时长配置信息：show admin lockout-duration
l
显示管理员密码输入错误最大次数配置信息：show admin max-login-failure
l
显示管理员的短信和邮箱认证的配置信息：show admin multiple-factor-auth
例如：
hostname(config)# show admin multiple-factor-auth
=============================================================
Multiple-factor-auth status: sms( 显示二次认证的状态，sms表示短信认证已开启，
email表示邮箱认证已开启)
Sender name:( 显示短信/邮件发送者名称)

<!-- 来源页 691 -->
Verify code timeout: 5 (minutes)( 显示短信/邮箱认证码的有效时间)
SMS config:( 显示短信认证的配置信息)
---------------------------------------------
SMS agent: gateway( 显示短信认证的方式)
SMS service provider: 11( 显示短信网关的服务商名称)
Email config:( 显示邮箱认证的配置信息)
---------------------------------------------
Email server name:( 显示邮箱服务器的名称)
=============================================================

<!-- 来源页 692 -->
配置系统审计员可管理日志类型
系统审计员只允许对日志信息进行查看、导出和清除，可管理的日志类型需要系统管理员来指定。在管理员
配置模式下，输入以下命令配置系统审计员可管理日志类型：
log {config | event | nbr | threat | sandbox | network | operation | iot-monitor | share-accessdetect | endpoint-tag| session | nat | urlfilter| pbr| dlp | cf | nbc | traffic | ips}
l
config – 指定系统审计员可管理配置日志信息。
l
event – 指定系统审计员可管理事件日志信息。
l
nbr – 指定系统审计员可管理NBR日志信息。
l
network – 指定系统审计员可管理网络日志信息。
l
iot-monitor – 指定系统审计员可管理IoT监控日志信息。
l
threat – 指定系统审计员可管理威胁日志信息。
l
sandbox – 指定系统审计员可管理沙箱日志信息。
l
share-access-detect – 指定系统审计员可管理共享接入日志信息。
l
operation – 指定系统审计员可管理操作日志信息。
l
endpoint-tag – 指定系统审计员可管理终端标签日志信息。
l
session – 指定系统审计员可管理会话日志信息。
l
nat – 指定系统审计员可管理NAT日志信息。
l
urlfilter – 指定系统审计员可管理URL过滤日志信息。
l
pbr – 指定系统审计员可管理沙箱PBR日志信息。
l
dlp – 指定系统审计员可管理DLP日志信息。
l
cf – 指定系统审计员可管理CF日志信息。
l
nbc - 指定系统审计员可管理NBC日志信息。
l
traffic - 指定系统审计员可管理流量日志信息。
l
ips - 指定系统审计员可管理IPS日志信息。
使用多条该命令为管理员指定多种可管理的日志类型。
使用no log {config | event | nbr | threat | sandbox | network | operation | iot-monitor | shareaccess-detect | endpoint-tag| session | nat | urlfilter| pbr| dlp | cf | nbc | traffic | ips}命令取消
指定的系统审计员可管理日志类型。

<!-- 来源页 693 -->
API Token
用户通过RESTful API登录设备时，可以通过用户名密码或者API Token的认证方式。支持创建指定管理员
的API Token，对API Token进行更新、续期、清除以及启用等操作。
注意: 开启短信或邮箱二次认证后，当管理员通过RESTful API登录设备时，只能使用API Token
的认证方式。
创建管理员的API Token
创建管理员的API Token，在管理员配置模式下，使用以下命令：
api-token create – 创建管理员的API Token。创建完默认是启用状态。
更改API Token的有效期
更改API Token的有效期，在管理员配置模式下，使用以下命令：
api-token expiration expiration-time
l
expiration-time – 更改API Token的有效期。范围是0-365天。默认是60天，如果配置为0，则表示
长期有效。
更新管理员的API Token
管理员可根据需要更新API Token的值，更新后原有的API Token立即失效，新生成的API Token根据当前
时间和有效期重新计算到期时间。更新管理员的API Token，在管理员配置模式下，使用以下命令：
api-token update
续期管理员的API Token
管理员可以对启用状态和过期状态的API Token进行续期操作。续期之后，API Token的值不发生改变。
API Token根据当前时间和有效期重新计算到期时间。例如：管理员“test”的API Token有效期为10天，
当前时间为2022年11月17日，到期时间为2022年11月25日，进行续期操作后，到期时间变更为2022年11
月27日。
api-token renewal
启用API Token
管理员可以对停用状态的API Token进行启用，启用时重新计算有效期，例如，API Token有效期原本设置
为30天，重新启用后，有效期重新变为30天。启用API Token，在管理员配置模式下，使用以下命令：
api-token enable

<!-- 来源页 694 -->
停用API Token
管理员可以对启用状态的API Token进行停用，停用之后如有需求通过api-token enable命令，下次可以
继续使用该API Token。停用API Token，在管理员配置模式下，使用以下命令：
api-token disable
删除管理员的API Token
管理员可以删除已创建的API Token，在管理员配置模式下，使用以下命令：
api-token delete
显示API Token的信息
用户可以在任何模式下，随时使用show命令查看指定管理员的API Token信息：
show admin api-token user-name
例如：
hostname(config)# show admin api-token test
================================================================
API Token:( 显示API Token的值用于登录RESTful API)
ewoJInR5cCI6CSJKV1QiLAoJImFsZyI6CSJTSEEyNTYiCn0=.ewoJInVzZXJuYW1lIjoJInRl
c3QiLAoJInZzeXNfaWQiOgkwCn0=.$020100rE$cmWWDXrSBhBtQvY+Pco1mSfmhmICNk7NKA
hxeS08wX/Kb08=
Begin Time: 2022-11-17 21:08:42( 显示API Token的生效时间)
Expiration: 60 days( 显示API Token的有效期)
Time To Expiration: 60 days( 显示API Token剩余的到期时间)
Current status: normal( 显示API Token当前的状态，normal表示当前是启用状态)
================================================================

<!-- 来源页 695 -->
配置可信主机
设备使用可信主机来进一步保证系统安全。管理员可以通过指定IP地址范围，或MAC地址/范围来匹配可信
主机，即在指定范围内的主机为可信主机。只有可信主机才可以对设备进行管理。
默认情况下，设备的可信主机范围是0.0.0.0/0，即所有主机都是可信主机。所有可信主机列表中可信主机
范围都是有效的。因此，建议用户在创建好合适的可信主机后，将系统原有的“0.0.0.0/0”可信主机范围
删除。
注意: 如果远程主机不能访问设备，请检查设备的可信主机配置。
配置可信主机
配置系统的可信主机，在全局配置模式下，使用以下命令：
admin host {range A.B.C.D A.B.C.D | A.B.C.D netmask | A.B.C.D/M | any} {http | https | ssh |
telnet | netconf | any }
l
range A.B.C.D A.B.C.D | A.B.C.D netmask | A.B.C.D/M | any – 指定可信主机的IP地址范围，例
如，range 1.1.1.1 255.255.0.0。any表示任何IP地址。
l
http | https | ssh | telnet | netconf | any – 指定可信主机的登录类型。any表示可以使用HTTP、
HTTPS、SSH、Telnet和NETCONF任意一种类型登录。
配置可信主机的IP地址范围和MAC地址或范围
配置可信主机的IP地址范围和MAC地址或范围，在全局配置模式下，使用以下命令：
admin host {range A.B.C.D A.B.C.D | A.B.C.D netmask | A.B.C.D/M | any} mac-host { range
H.H.H H.H.H | H.H.H | any} {http | https | ssh | telnet | netconf | any }
用户可以配置多条该命令添加多个可信主机范围。系统最多允许配置128条可信主机范围。
使用no admin host {range A.B.C.D A.B.C.D | A.B.C.D netmask | A.B.C.D/M | any} 命令取消对可
信主机IP地址范围的指定。
使用no admin host {range A.B.C.D A.B.C.D | A.B.C.D netmask | A.B.C.D/M | any} mac-host { 
range H.H.H H.H.H | H.H.H | any}命令取消对可信主机IP地址范围和MAC地址、范围的指定。
当使用指定的IP地址范围来匹配可信主机时，使用no admin host {range A.B.C.D A.B.C.D | A.B.C.D
netmask | A.B.C.D/M | any} {http | https | ssh | telnet| netconf | any }取消对可信主机特定登录类型
的指定。

<!-- 来源页 696 -->
当使用指定的IP地址范围和MAC地址范围来匹配可信主机时，使用no admin host {range A.B.C.D
A.B.C.D | A.B.C.D netmask | A.B.C.D/M | any} mac-host { range H.H.H H.H.H | H.H.H |
any} {http | https | ssh | telnet | netconf | any }取消对可信主机特定登录类型的指定。
配置IPv4可信主机描述信息
配置IPv4类型可信主机描述信息，在全局配置模式下，使用以下命令：
admin host {range A.B.C.D A.B.C.D | A.B.C.D netmask | A.B.C.D/M | any} [mac-host
{rangeH.H.H H.H.H | H.H.H | any}] description description
l
range A.B.C.D A.B.C.D | A.B.C.D netmask | A.B.C.D/M | any – 指定可信主机的IPv4地址范围，例
如，range 1.1.1.1 255.255.0.0。any表示任何IP地址。
l
mac-host {rangeH.H.H H.H.H | H.H.H | any} – 指定可信主机的MAC地址范围。any表示任何MAC
地址。指定后，可信主机的地址类型为IPv4&MAC。如不指定，则可信主机的地址类型为IPv4。
l
description – 指定可信主机的描述信息。范围是1到127个字符。
使用该命令no的形式取消可信主机的描述信息：
no admin host {range A.B.C.D A.B.C.D | A.B.C.D netmask | A.B.C.D/M | any} [mac-host
{rangeH.H.H H.H.H | H.H.H | any}] description
配置IPv6可信主机
管理员可以指定一个IPv6地址范围，在该指定范围内的主机为可信主机。
配置IPv6地址的可信主机，在全局配置模式下，使用以下命令：
admin ipv6-host {X:X:X:X::X/M | range X:X:X:X::X X:X:X:X::X | any} [mac-host {H.H.H | range
H.H.H H.H.H | any}] {http | https | ssh | telnet | netconf | any }[description description]
l
X:X:X:X::X/M | range X:X:X:X::X X:X:X:X::X | any – 指定可信主机的IPv6地址范围。any表示任
何IP地址。
l
mac-host {H.H.H | range H.H.H H.H.H | any} – 指定可信主机的MAC地址范围。any表示任何MAC
地址。指定后，可信主机的地址类型为IPv6&MAC。如不指定，则可信主机的地址类型为IPv6。
l
http | https | ssh | telnet | netconf | any – 指定可信主机的登录类型。any表示可以使用HTTP、
HTTPS、SSH、Telnet和NETCONF任意一种类型登录。
l
description description – 指定可信主机的描述信息。范围是1到127个字符。
用户可以配置多条该命令添加多个可信主机范围。系统最多允许配置128条可信主机范围。

<!-- 来源页 697 -->
使用no admin ipv6-host {X:X:X:X::X/M | range X:X:X:X::X X:X:X:X::X | any}命令取消地址类型为
IPv6的可信主机的配置。
使用no admin ipv6-host {X:X:X:X::X/M | range X:X:X:X::X X:X:X:X::X | any} mac-host {H.H.H |
range H.H.H H.H.H | any}命令取消地址类型为IPv6&MAC的可信主机的配置。
使用no admin ipv6-host {X:X:X:X::X/M | range X:X:X:X::X X:X:X:X::X | any} {http | https | ssh
| telnet | netconf}取消对IPv6类型可信主机的特定登录类型的指定。如果只配置了一种登录类型，只能通
过删除可信主机条目来删除登录类型。
使用no admin ipv6-host {X:X:X:X::X/M | range X:X:X:X::X X:X:X:X::X | any} mac-host {H.H.H |
range H.H.H H.H.H | any} {http | https | ssh | telnet | netconf}取消对IPv6&MAC类型可信主机的特
定登录类型的指定。如果只配置了一种登录类型，只能通过删除可信主机条目来删除登录类型。
配置IPv6可信主机描述信息
配置IPv6类型可信主机描述信息，在全局配置模式下，使用以下命令：
admin ipv6-host {X:X:X:X::X/M | range X:X:X:X::X X:X:X:X::X | any} [mac-host {H.H.H | range
H.H.H H.H.H | any}] descriptiondescription
l
X:X:X:X::X/M | range X:X:X:X::X X:X:X:X::X | any – 指定可信主机的IPv6地址范围。any表示任
何IP地址。
l
mac-host {H.H.H | range H.H.H H.H.H | any} – 指定可信主机的MAC地址范围。any表示任何MAC
地址。指定后，可信主机的地址类型为IPv6&MAC。如不指定，则可信主机的地址类型为IPv6。
l
description – 指定可信主机的描述信息。范围是1到127个字符。
使用该命令no的形式取消可信主机的描述信息：
no admin ipv6-host {X:X:X:X::X/M | rangeX:X:X:X::X X:X:X:X::X | any} [mac-host {H.H.H |
range H.H.H H.H.H | any}] description
显示可信主机配置
用户可以在任何模式下，随时使用show命令查看可信主机配置：
show admin host

<!-- 来源页 698 -->
配置管理接口
系统支持Console、Telnet、SSH以及WebUI方式的访问。用户可以配置各种访问方式的超时时间、端口号
以及HTTPS的PKI信任域。
使用Telnet、SSH、HTTP或者HTTPS方式登录设备时，如果在一分钟内连续三次登录失败，系统会将登录
失败的IP地址锁定两分钟。被锁定的IP地址在两分钟内不能建立与设备的连接。
配置Console管理接口
Console管理接口的配置包括波特率配置和超时时间配置。
配置波特率
在任何模式下，使用以下命令设置Console口的波特率：
exec console baudrate {9600 | 19200 | 38400 | 57600 | 115200}
l
9600 | 19200 | 38400 | 57600 | 115200 – 指定Console口波特率，单位为bps。
型号说明：
l
仅SG-6000-A2200/A1800/A1600/X20812/X20803/X9180-GS/X9180设备支持配置
波特率。
l
设备的默认波特率根据型号不同而不同。详见"搭建Console口配置环境" 在第14页。
注意: 完成波特率配置后，用户在通过Console口登录设备时需保证波特率与设备Console口所作
配置一致。
配置超时时间
如果在超时时间内未通过Console口进行任何配置，系统将断开此次Console连接。配置Console超时时
间，在全局配置模式下，使用以下命令：
console timeout timeout-value
l
timeout-value – 指定Console超时时间，单位为分钟。范围是0到60分钟，0表示无时间限制。默认
值是10分钟。
在全局配置模式下，使用该命令no的形式恢复Console超时默认值：
no console timeout

<!-- 来源页 699 -->
配置Telnet管理接口
用户可以配置Telnet的超时时间以及Telnet端口号。使用Telnet方式连接设备时，使用的端口号必须与此
处配置的端口号一致。同时，用户还可以配置Telnet最大登录次数。
如果已经建立的Telnet连接在超时时间内未发送Telnet请求，系统将断开此次Telnet连接。
配置Telnet超时时间
配置Telnet超时时间，在全局配置模式下，使用以下命令：
telnet timeout timeout-value
l
timeout-value – 指定Telnet超时时间，单位为分钟。范围是1到60分钟。默认值是10分钟。
在全局配置模式下，使用该命令no的形式恢复Telnet超时默认值：
no telnet timeout
配置Telnet最大会话数
配置Telnet最大会话数，在全局配置模式下，使用以下命令：
telnet max-session max-session
l
max-session – 指定Telnet最大会话数。范围是1到X，不同平台X的取值不同。默认值为X。
在全局配置模式下，使用该命令no的形式恢复Telnet默认会话数：
no telnet max-session
配置Telnet端口号
配置Telnet端口号，在全局配置模式下，使用以下命令：
telnet port port-number
l
port-number – 指定Telnet端口号。范围是1到65535。默认值是23。
在全局配置模式下，使用该命令no的形式恢复Telnet默认端口号：
no telnet port
配置Telnet最大登录次数
Telnet最大登录次数，是指允许用户连续失败登录的最大次数。如果连续登录失败次数超出该指定数值，系
统将断开此次Telnet连接。配置Telnet最大登录次数，在全局配置模式下，使用以下命令：
telnet authorization-try-count count-number

<!-- 来源页 700 -->
l
count-number – 指定最大连接次数。范围是1到10次。默认为3次。
在全局配置模式下，使用该命令no的形式恢复Telnet默认登录次数：
no telnet authorization-try-count
配置SSH管理接口
用户可以配置SSH超时时间以及端口号。并且可以指定SSH连接的间隔时间。
如果已经建立的SSH连接在超时时间内未发送SSH请求，系统将断开此次SSH连接。
配置SSH超时时间
配置SSH超时时间，在全局配置模式下，使用以下命令：
ssh timeout timeout-value
l
timeout-value – 指定SSH超时时间，单位为分钟。范围是1到60分钟。默认值是10分钟。
在全局配置模式下，使用该命令no的形式恢复SSH默认超时时间：
no ssh timeout
配置SSH最大会话数
配置SSH最大会话数，在全局配置模式下，使用以下命令：
ssh max-session max-session
l
max-session– 指定SSH最大会话数。范围是1到X，不同平台X的取值不同。默认值为X。
在全局配置模式下，使用该命令no的形式恢复SSH默认会话数：
no ssh max-session max-session
配置SSH端口号
配置SSH端口号，在全局配置模式下，使用以下命令：
ssh port port-number
l
port-number – 指定SSH端口号。范围是1到65535。默认值是22。
在全局配置模式下，使用该命令no的形式恢复SSH默认端口号：
no ssh port

<!-- 来源页 701 -->
配置SSH连接时间间隔
用户可以指定设备处理SSH连接的时间间隔。建立一个SSH连接后，在时间间隔过后，设备才接受下一个
SSH连接请求。配置SSH连接时间间隔，在全局配置模式下，使用以下命令：
ssh connection-interval interval-time
l
interval-time – 指定时间间隔，单位是秒。范围是2到3600秒。默认值是2秒。
在全局配置模式下，使用该命令no的形式恢复SSH连接默认端时间间隔：
no ssh connection-interval
配置WebUI管理接口
用户可以通过HTTP和HTTPS方式访问设备，进行配置。
配置WebUI超时时间
配置WebUI超时时间，在全局配置模式下，使用以下命令：
web timeout timeout-value
l
timeout-value – 指定WebUI超时时间，单位为分钟。范围是1到1440分钟。默认值是10分钟。
在全局配置模式下，使用该命令no的形式恢复WebUI超时默认值：
no web timeout
指定HTTP端口号
指定HTTP端口号，在全局配置模式下，使用以下命令：
http port port-number
l
port-number – 指定HTTP端口号。当使用HTTP方式访问设备时，浏览器的HTTP端口号必须与此处指
定的端口号一致。范围是1到65535。默认值是80。
在全局配置模式下，使用该命令no的形式，恢复默认HTTP端口号：
no http port
开启/关闭HTTP访问自动跳转HTTPS功能
开启HTTP访问自动跳转HTTPS功能后，当用户通过HTTP协议访问设备时，系统将自动跳转至HTTPS协议访
问。该功能默认为关闭状态。
开启/关闭HTTP访问自动跳转HTTPS功能，在全局配置模式下，使用以下命令：

<!-- 来源页 702 -->
l
开启：web redirect-http-to-https enable
l
关闭：web redirect-http-to-https disable
配置防跨站脚本攻击服务
配置防跨站脚本攻击（anti-xss）服务，在全局配置模式下，使用以下命令：
http anti-xss { disable | enable | mode {normal| strict}}
l
disable | enable– 启用和禁用防跨站脚本攻击服务。默认情况下，防跨站脚本攻击服务为启用状态。
l
mode {normal| strict}–指定防跨站脚本攻击服务模式。包括字符匹配模式（normal）和正则表达式
匹配模式（strict）。
在全局配置模式下，使用该命令no的形式，恢复防跨站脚本攻击（anti-xss）服务默认值：
no http anti-xss { disable | enable | mode {normal| strict}}
开启/关闭防点击劫持功能
点击劫持是一种视觉上的欺骗手段。攻击者使用一个透明的，不可见的iframe，覆盖在一个网页上，然后诱
导使用户在该网页上进行操作，此时用户将在不知情的情况下点击透明的iframe页面。为了防止攻击者的页
面被嵌入到防火墙的WebUI页面，用户可以开启防点击劫持功能，通过在响应中增加X-Frame-Options
sameorigin，保证防火墙的WebUI页面的所有内容来源于相同域名。防点击劫持功能默认为开启状态。
关闭防点击劫持功能，在全局配置模式下，使用以下命令：
http anti-click-jacking disable
开启防点击劫持功能，在全局配置模式下，使用以下命令：
http anti-click-jacking enable
配置内容安全策略
内容安全策略（CSP）可以控制用户代理能够为指定的页面加载哪些资源来防止跨站脚本攻击等，提高安全
性。
配置内容安全策略，在全局配置模式下，使用以下命令：
http content-security-policy {script-src-self | none}
l
script-src-self - 指定匹配当前域，允许内嵌脚本样式，且允许通过字符串动态创建脚本。
l
none - 不匹配任何内容。
启用/禁用国密HTTPS功能
用户通过HTTPS方式访问设备时，可以使用常规HTTPS方式或者国密HTTPS方式：

<!-- 来源页 703 -->
l
常规HTTPS方式：系统使用常规TLS/SSL协议与客户端（浏览器）建立通信连接；
l
国密HTTPS方式：系统使用国密TLS/SSL协议与客户端（国密浏览器）建立通信连接，SSL认证过程中
使用双证书，包括签名证书和加密证书。
启用或者禁用国密HTTPS功能，在全局配置模式下，使用以下命令：
https ssl-protocol-gm {enable | disable}
l
启用（enable）或者禁用（disable）国密HTTPS功能。
指定HTTPS端口号
指定HTTPS端口号，在全局配置模式下，使用以下命令：
https port port-number
l
port-number – 指定HTTPS端口号。当使用HTTPS方式访问设备时，浏览器的HTTPS端口号必须与此
处指定的端口号一致。范围是1到65535。默认值是443。
在全局配置模式下，使用该命令no形式恢复默认HTTPS端口号：
no https port
指定国密HTTPS PKI信任域
指定常规HTTPS方式访问时使用的PKI信任域，或者指定国密HTTPS访问方式时的签名证书信任域，在全局
配置模式下，使用以下命令：
https trust-domain trust-domain-name
l
trust-domain-name – 指定已配置的PKI信任域的名称。当使用常规HTTPS时，HTTPS服务器在SSL
认证过程中将使用指定PKI信任域中的证书；当使用国密HTTPS时，HTTPS服务器在国密SSL认证过程中
将使用指定PKI信任域中的证书作为签名证书。默认情况下，系统将使用缺省PKI信任域trust_domain_
default。
在全局配置模式下，使用该命令no的形式恢复默认PKI信任域：
no https trust-domain
指定国密HTTPS加密信任域
由于国密HTTPS使用双证书，开启国密HTTPS功能时，需要再指定加密信任域。指定加密信任域，在全局配
置模式下，使用以下命令：
https trust-domain-enc trust-domain-name

<!-- 来源页 704 -->
l
trust-domain-name– 指定已配置的PKI信任域的名称。HTTPS服务器在国密SSL认证过程中将使用指
定PKI信任域中的证书作为加密证书。默认情况下，系统将使用缺省PKI信任域trust_domain_
default。
在全局配置模式下，使用该命令no的形式恢复国密HTTPS默认加密信任域：
no https trust-domain-enc
显示管理接口配置
用户可以在任何模式下，随时使用show命令查看管理接口配置信息。命令如下：
l
显示Console配置：show console
l
显示Telnet配置：show telnet
l
显示SSH配置：show ssh
l
显示Web配置：show http

<!-- 来源页 705 -->
网络时间协议（Network Time Protocol）
NTP介绍
网络时间协议（Network Time Protocol），简称为NTP。NTP为整个网络传递统一、标准的时间。实现
方法是在网络上指定若干时钟源，为用户提供授时服务，并且这些时钟服务器间能够相互对比以提高准确
度。NTP协议采用UDP传输协议格式，使用专用端口123。
关于NTP确保时钟同步的精确性的算法，请参阅RFC1305规范。
Hillstone设备的时间影响到设备的许多功能模块，例如VPN隧道的建立、时间表功能的实现以及自签名证
书的使用等，因此系统时间的精确性十分重要。为保证Hillstone设备系统能够一直保持精确时间，
Hillstone设备允许用户通过NTP来使系统时间与网络上的NTP服务器同步。Hillstone设备支持两种设置时
间的方式，分别是手动设置和通过NTP与服务器同步。
注意: 为保证自签名证书时间的正确性，避免证书使用错误，初次使用设备时，请务必将设备时间
与PC时间同步。
配置NTP
手动配置时间
手动配置系统的时间，在全局配置模式下，使用以下命令：
clock time HH:MM:SS Month Day Year
l
HH:MM:SS Month Day Year - 指定系统时间。HH、MM和SS分别表示小时、分钟和秒，Month、
Day和Year分别表示月、日和年。
手动配置时区
系统提供多个预定义时区，同时，为实现更精确的时区配置，系统支持自定义时区配置，并且，用户可以为
自定义时区指定夏令时。
系统的默认时区是东8区。为系统指定时区，在全局配置模式下，使用以下命令：
clock zone {timezone-name | cus-timezone-name hours minutes}
l
timezone-name - 指定预定义时区名称。
l
cus-timezone-name - 指定自定义时区名称，范围是1到6个字符。
l
hours minutes – 为自定义时区指定相对UTC（Universal Time Coordinated，协调世界时）时间的
偏移量。hours的取值范围是-13到12；minutes的取值范围是0到59。

<!-- 来源页 706 -->
例如：
自定义时区为test，其相对UTC的偏移量是6小时30分：
hostname(config)# clock zone test 6 30
配置夏令时
夏令时（summer-time）是为节约能源而人为规定的地方时间制度。按国家法令，在夏季及其前后实施。
一般在天亮早的夏季人为将时间提前一小时，夏季结束再将时间调回一小时。用户可以为系统自定义时区指
定夏令时的绝对时间段和循环时间段。
为系统指定夏令时的绝对时间段，在全局配置模式下，使用以下命令：
clock summer-time cus-timezone-name date start-date start-time end-date end-time
[compensation-time]
l
cus-timezone-name – 指定自定义时区名称，范围是1到6个字符。
l
date – 指定夏令时的绝对时间段。
l
start-date – 指定夏令时起始日期。书写格式为“月/日/年”，例如7/20/2011。
l
start-time – 指定夏令时起始时间。书写格式为“小时：分钟”，例如10:30。
l
end-date – 指定夏令时终止日期。书写格式为“月/日/年”，例如7/20/2011。
l
end-time - 指定夏令时终止时间。书写格式为“小时：分钟”，例如10:30。
l
compensation-time – 指定夏令时生效时的时间补偿，默认值为0。例如夏令时开始时，某些地区时间
须调快1小时30分；夏令时结束时，时间须调慢1小时30分。“1小时30分”即为夏令时生效时的时间补
偿。书写格式为“小时：分钟”，例如1:30。
例如：
自定义时区test的夏令时从6/22/2011的10:30开始，到9/23/2011的10:00结束。夏令
时期间的时间将比非夏令时期间的时间快2小时30：
hostname（config）# clock summer-time test date 6/22/2011 10:30 9/23/2011 10:00
2:30
为系统指定夏令时的循环时间段，即在每年的指定时间段内，执行夏令时。在全局配置模式下，使用以下命
令：
clock summer-time cus-timezone-name recurring { [Mon] | […] | [Sun] }{after | before}startday start-month start-time { [Mon] | […] | [Sun]} {after | before}end-day end-month end-time
[compensation-time]

<!-- 来源页 707 -->
l
cus-timezone-name – 指定自定义时区名称，范围是1到6个字符。
l
recurring – 指定夏令时的循环时间段。
l
{ [Mon] | […] | [Sun] }{after | before}start-day start-month start-time – 指定夏令时循环时间段
的起始时间。例如命令关键字为Mon before 22 6 10:30，即夏令时起始时间为每年6月22日前的第一
个周一的10:30。
l
{ [Mon] | […] | [Sun]} {after | before}end-day end-month end-time– 指定夏令时循环时间段的
终止时间。例如命令关键字为Fri after 23 9 10:00，即夏令时终止时间为每年9月23日后的第一个周五
的10:00。
l
compensation-time – 指定夏令时生效时的时间补偿，默认值为0。例如夏令时开始时，某些地区时间
须调快1小时30分；夏令时结束时，时间须调慢1小时30分。“1小时30分”即为夏令时生效时的时间补
偿。书写格式为“小时：分钟”，例如1:30。
例如：
自定义时区test的夏令时在从每年的6月22日前的第一个周一的10:30开始，到9月23日后
的第一个周五的10:00结束。夏令时期间的时间将比非夏令时期间的时间快2小时30：
hostname（config）# clock summer-time test recurring Mon before 22 6 10:30 Fri
after 23 9 10:00 2:30
注意: 夏令时的配置会对日志和基于时间的功能模块产生影响。例如，当9/23/2011的10:00夏令
时结束时，系统时间将自动调慢2小时30分，恢复为非夏令时期间的7:30。这样，9/23/2011的
7:30到10:00在这一天会出现两次。
使用no clock summer-time cus-timezone-name {date |recurring}命令取消夏令时的配置。
查看系统时间配置信息
在CLI任何命令模式下使用show clock命令，查看当前的时区配置信息。
在CLI任何命令模式下使用show config命令，查看当前的夏令时配置信息。
配置设备作为NTP客户端
通过NTP客户端配置，可以使设备的系统时间与时钟服务器同步。在设备上可以做的NTP客户端配置有以下
各项：
l 开启/关闭NTP客户端
l 配置NTP服务器

<!-- 来源页 708 -->
l 配置最大调整时间
l 配置查询间隔
l 开启/关闭身份验证功能
l 配置NTP身份验证功能
开启/关闭NTP功能
默认情况下，系统的NTP功能是关闭的。在设备上开启或者关闭NTP功能，在全局配置模式下使用以下命
令：
l
启用：ntp enable
l
禁用：no ntp enable
配置NTP时钟服务器
用户最多可以指定3个时钟服务器，同时可以使用prefer关键字指定主时钟服务器（设备首先与主服务器进
行时间同步）；如果没有为服务器指定prefer关键字，设备会使用户最先配置的服务器做时间同步。配置
NTP时钟服务器，请在全局配置模式下输入以下命令：
ntp server {ip-address | host-name} [key number] [source interface-name] [prefer] [vrouter
vrouter-name]
l
ip-address | host-name – 指定时钟服务器的IP地址或主机名称。主机名称取值范围为1到127个字
符。
l
key number – 指定可以通过该服务器的验证密钥。如果要在配置的时钟服务器上使用NTP身份验证功
能，用户必须指定key参数值。
l
source interface-name – 指定设备上发送和接收NTP包的接口。
l
prefer – 如果指定了多个时钟服务器，该关键字用来指定该服务器为主时钟服务器。设备首先与主服务
器进行时间同步，如果失败，再查找下一个时钟服务器。
l
vrouter-name - 为指定的VRouter指定时钟服务器。
使用no ntp server {ip-address | host-name}命令取消指定时钟服务器的配置。
以下是时钟服务器配置示例：
hostname(config)# ntp server 10.160.64.5 prefer

<!-- 来源页 709 -->
配置最大调整时间
如果设备和NTP时钟服务器的时间差在最大调整时间之内，就能成功进行时间同步，否则同步不成功。配置
最大调整时间，在全局配置模式下，输入以下命令：
ntp max-adjustment time-value
l
time-value – 最大调整时间值。范围是0到3600秒，0表示没有时间限制。默认值是400秒。
使用no ntp max-adjustment命令恢复最大调整时间的默认值。
配置查询间隔
设备每隔一个查询间隔就与时钟服务器做一次同步，保证Hillstone设备系统时间的准确。配置查询间隔，
在全局配置模式下，输入以下命令：
ntp query-interval time-interval
l
time-interval – 查询间隔值。范围是1到60分钟。默认值是5分钟。
使用no ntp query-interval命令恢复查询间隔的默认值。
开启/关闭身份验证功能
默认情况下，系统的NTP身份验证功能是关闭的。在Hillstone设备上开启或者关闭NTP身份验证功能，在全
局配置模式下使用以下命令：
l
启用：ntp authentication
l
禁用：no ntp authentication
配置NTP身份验证功能
使用NTP身份验证功能，用户需要配置MD5身份验证密钥ID和密钥。启动该功能后，设备只会与通过验证的
服务器进行同步。配置NTP验证密钥ID和密钥，请在全局配置模式下，输入以下命令：
ntp authentication-key number md5 string
l
number - 验证密钥ID，范围是从1到65535；
l
string - MD5验证密钥，范围是1到31个字符。
在全局配置模式下，使用no ntp authentication-key number命令取消验证密钥的配置。

<!-- 来源页 710 -->
配置设备作为NTP服务端
通过NTP服务端配置，可以为其他客户端同步系统时间。一个设备可以同时作为服务端和客户端，且可以同
时为多个设备提供服务。设备通过其他NTP服务器同步时钟或指定本地时钟为主时钟时，设备本身的时钟处
于同步状态。此时，设备可作为NTP服务端为其他客户端提供同步时钟的服务。在设备上可以做的NTP服务
端配置有以下各项：
l 开启/关闭NTP服务端功能
l 配置侦听接口
l 配置本地时钟为主时钟
l 配置NTP服务器密钥
开启/关闭NTP服务端功能
默认情况下，系统的NTP服务端功能是关闭的。在设备上开启或者关闭NTP服务端功能，在全局配置模式下
使用以下命令：
l
启用：ntp server-service enable
l
禁用：no ntp server-service enable
配置侦听接口
侦听接口用于获取客户端发来的同步请求并为客户端提供同步服务。指定侦听接口，在全局配置模式下使用
以下命令：
ntp server-service listening-interface interface-name
l
interface-name - 指定设备上接受和发送NTP包的接口，最多可配置32个接口，仅支持三层接口。
在全局配置模式下，使用no ntp server-service listening-interface interface-name命令取消侦听接
口的配置。
配置本地时钟为主时钟
设备可以配置本地时间作为参考时钟为客户端提供同步服务，默认为关闭状态。指定本地时钟为主时钟，在
全局配置模式下使用以下命令：
ntp refclock local [stratum stratum-value]
l
stratum-value - 指定本地时间层数，取值范围是1到14，默认值为8。层数代表时钟精确度，层数越
小精度越高。当设备同时配置其他服务器作为时钟源时：

<!-- 来源页 711 -->
l
如果本地时钟的层数大于服务器提供的层数，那么设备使用时钟服务器作为参考；
l
如果本地时钟的层数小于服务器提供的层数，那么设备将使用本地时钟作为参考。
在全局配置模式下，使用no ntp refclock local 命令取消配置本地时钟为主时钟。
配置NTP服务器密钥
设备可以配置作为服务端的信任密钥，用于与其他客户端进行身份验证。指定NTP服务密钥，在全局配置模
式下使用以下命令：
ntp server-service key key-id
l
key-id - 指定NTP服务器密钥的ID。新建NTP密钥，请参考配置NTP身份验证功能。
在全局配置模式下，使用no ntp server-service key 命令取消配置NTP服务器密钥。
查看NTP状态
NTP配置完成后，在任何模式下运行show ntp status命令可以查看当前的NTP配置信息和NTP状态。
查看/清除发送NTP报文的统计信息
完成设备作为NTP服务端的配置后，在任何模式下运行show ntp server-service packets statistics命令
可以查看当前的设备发送/接收/处理/丢弃NTP报文的统计数量。
在任何模式下运行show ntp server-service packets statistics clear命令可以清除当前的设备发送/接
收/处理/丢弃NTP报文的统计数量。
NTP配置举例
NTP服务器的IP地址是10.10.10.10；身份验证密钥ID和MD5验证密钥分别是1和aaaa；查询间隔为3分
钟；最大调整时间为5秒。配置完成后开启设备的NTP身份验证功能和NTP功能。最后查看NTP配置信息和状
态。请参考以下配置命令：
hostname(config)# ntp authentication-key 1 md5 aaaa
hostname(config)# ntp server 10.10.10.10 key 1 prefer
hostname(config)# ntp query-interval 3
hostname(config)# ntp max-adjustment 5
hostname(config)# ntp authentication
hostname(config)# ntp enable
hostname(config)# show ntp status

<!-- 来源页 712 -->
ntp client is enabled, authentication is enabled
ntp query-interval is 3, max-adjustment time is 5
ntp server 10.10.10.10, key 1, prefer

<!-- 来源页 713 -->
配置存储管理
系统提供存储管理功能，帮助用户通过限制各个功能占用磁盘空间的大小来管理系统存储空间。同时，系统
为丢包统计、长期监控、报表及每个模块的日志划分了固定的存储空间，对于安装有硬盘的设备，用户配置
自定义的存储阈值。当各功能数据存储空间到达或超过配置的阈值时，会生成日志进行告警提示。
型号说明：
l
支持存储管理功能的设备型号包含：
l
SG-6000 A系列设备（不含SG-6000-A200/A200W/A200G4/A200WG4）
l
SG-6000 K系列所有设备
l
SG-6000 X系列设备X8180、X9180-GS、X20803、X20812
l
云·界
l
建议配置的自定义存储空间配置之和不超过整体阈值，否则部分数据存储将会无法达到设置
的阈值。
配置系统存储空间告警阈值
当系统存储比例达到指定的阈值时，系统将执行指定的动作，从而控制系统存储。
配置系统整体存储空间告警阈值，在全局配置模式下输入以下命令：
storage threshold percent percent-value
l
percent percent-value – 指定系统整体存储空间告警阈值，取值范围为0.01%-90%。
指定日志超过存储阈值处理动作
当日志达到指定的存储阈值时，系统将执行指定的动作，包括覆盖最早的日志和停止记录新的日志。
指定处理动作，在全局配置模式下输入以下命令：
storage threshold log {automatically-overwirte | stop-overwrite}
l
automatically-overwirte - 系统将覆盖最早的日志。对于安装有硬盘的SG-6000 K系列设备，如指定
该动作，可以继续配置FTP服务器，将被删除的日志转存至FTP服务器。配置方法参阅配置日志备份服务
器。
l
stop-overwrite - 系统将停止存储新的日志。

<!-- 来源页 714 -->
开启/关闭存储空间告警
当系统存储比例达到指定的阈值时，系统会向用户发送告警日志进行提示。默认情况下，存储空间告警是开
启的。
开启/关闭存储空间告警，在全局配置模式下输入以下命令：
开启：storage threshold alert-log enable
关闭：storage threshold alert-log disable
指定日志存储空间的管理方式
指定日志存储空间的管理方式，在全局配置模式下输入以下命令：
storage threshold log mode {global | by-log-type}
l
global - 指定存储阈值按总存储阈值管理。
l
by-log-type - 指定存储阈值按每个模块日志单独的存储空间管理。
说明：对于无硬盘的设备，仅支持以by-log-type的方式管理存储阈值，日志存储空间为系统预设固定值。
配置日志总存储阈值
对于安装有硬盘的设备，用户可以配置所有类型日志的总存储阈值。对于无硬盘的设备，日志存储阈值为系
统预设固定值，且不可配置。
配置所有类型日志的总存储阈值，在全局配置模式下输入以下命令：
storage threshold log percent percent-value
l
percent-value - 配置所有类型日志的总存储阈值。取值范围是0.01%-90%。
注意：日志总存储阈值配置在存储阈值计算方式为global时（可使用storage thresholdlog mode
global命令），才可生效。
配置各类型日志存储阈值
对于安装有硬盘的设备，用户可以根据需要自定义配置指定模块日志的存储阈值。对于无硬盘的设备，日志
存储阈值为系统预设固定值（事件日志7%、配置日志6%、网络日志6%），且不可配置。
配置各类型日志存储阈值，在全局配置模式下输入以下命令：
storage threshold log {configuration | endpoint-tag | event | network | sandbox | threat |
traffic {session | nat | urlfilter} } percent-value

<!-- 来源页 715 -->
l
{configuration | endpoint-tag| event | network | sandbox | threat | traffic {session | nat |
urlfilter} } percent-value - 配置指定模块的日志的存储阈值。取值范围是0.01%-90%。
注意：各类型日志存储阈值配置在存储阈值计算方式为by-log-type时（可使用storage thresholdlog
mode by-log-type命令），才可生效。
配置报表存储阈值
对于安装有硬盘的设备，用户可以根据需要自定义配置报表的存储阈值。对于无硬盘的设备，报表存储阈值
为系统预设固定值20%，且不可配置。
配置报表存储阈值，在全局配置模式下输入以下命令：
storage threshold log report percent-value
l
report percent-value - 配置报表的存储阈值。取值范围是0.01%-90%。
配置长期监控存储阈值
对于安装有硬盘的设备，用户可以根据需要自定义配置长期监控功能统计数据的存储阈值。对于无硬盘的设
备，不支持存储长期监控统计数据。
型号说明：支持长期监控功能的设备包含
l
安装有硬盘的SG-6000 A系列设备（不含SG-6000-A1600/A1800/A2200）。
l
安装有硬盘的SG-6000 K系列设备。
配置长期监控功能统计数据的存储阈值，在全局配置模式下，使用以下命令：
storage threshold statistics-long-term percent-value
l
percent-value - 配置长期监控功能统计数据的存储阈值。取值范围是0.01%-90%。系统为长期监控
功能统计数据分配的默认磁盘空间大小为10%。当存储空间达到指定的阈值时，系统将删除较早的统计
数据。
配置威胁证据数据存储阈值
入侵防御、病毒过滤、僵尸网络防御开启抓包取证功能后，系统会抓取威胁日志对应的报文并提取出威胁证
据信息，并在WebUI的威胁日志的详情页面中展示。
威胁证据数据包含威胁证据信息和威胁报文。系统为威胁证据数据的存储分配了默认的磁盘空间大小，用户
可以根据需要为威胁证据数据自定义配置磁盘空间大小。
当威胁证据数据达到指定的存储阈值时，系统将按照日志达到指定存储阈值的动作处理威胁证据数据。包括

<!-- 来源页 716 -->
覆盖最早的数据和停止记录。
如果删除威胁日志，对应的威胁报文和威胁证据信息也会一并被删除。
型号说明：支持威胁证据数据存储的设备包含：
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
配置威胁证据数据的存储阈值，在全局配置模式下，使用以下命令：
storage threshold forensic percent-value
l
percent-value - 配置威胁证据数据的存储阈值。取值范围是0.01%-90%。系统为威胁证据数据分配
的默认磁盘空间大小为10%。
配置丢包存储阈值
型号说明：对于安装有硬盘的SG-6000 A系列设备（不含SG-6000-
A1600/A1800/A2200），用户可以根据需要自定义配置丢包统计数据的存储阈值。对于无硬
盘的A系列设备，不支持存储丢包统计数据。
配置丢包统计数据的存储阈值，在全局配置模式下，使用以下命令：
storage threshold module-drop-counter percent-value
l
percent-value - 配置丢包统计数据的存储阈值。取值范围是0.1%-90%。系统为丢包统计数据分配的
默认磁盘空间大小为2%。当存储空间达到指定的阈值时，系统将删除较早的统计数据。
查看存储阈值配置
查看自定义的存储阈值配置、最大存储空间及已占用存储百分比，在任何模式下，使用以下命令：
show storage threshold
以下是返回结果示例：

<!-- 来源页 717 -->
hostname#show storage threshold
==============================================
State:on
Alert log is:on
Max storage percent:90%
Total:939Gb
Used:19Gb
==============================================
Storage for long term statistics:
Max storage percent:10%
Limit: 96129Mb
Used: <1 Mb
==============================================
Storage for module drop counter:
Max storage percent:2%
Limit: 19225Mb
Used: 84 Mb
==============================================
Storage for all logs: 961298Mb
Mode:by-log-type
Action: Automatically-overwrite
==================================================
Log Limit(MB) Used(MB)
--------------------------------------------------
event 1%(9612) 2
configuration 1%(9612) <1
network 1%(9612) <1
threat <1%(1922) 5
sandbox 1%(9612) <1

<!-- 来源页 718 -->
endpoint-tag 1%(9612) <1
traffic session <1%(4806) 3
traffic nat 10%(96129) <1
==================================================
日志自动清理
型号说明：不支持：SDW系列
对于带硬盘的设备，一旦硬盘达到设定的存储阈值，系统自动启动日志清理，且从较早的日志开始删除。此
操作旨在释放硬盘空间，以维持系统的基本功能与数据存储需求。用户无需干预，但可以根据自己的业务情
况，调整合适的整体存储比例阈值和日志存储阈值。
提示:
l
硬盘的存储阈值设置。需要在WebUI的“系统> 设备管理> 存储管理”页面，配置硬盘存储
阈值。
l
支持存储管理和清理的日志类型，包含事件日志、配置日志、网络日志、威胁日志、云沙箱日
志、会话日志、NAT日志等。部分日志类型，如URL日志、PBR日志等，无法存储到数据库，
所以不存在删除的情况。可在WebUI的“系统> 设备管理> 存储管理”页面查看，或者通过
show storage threshold命令查看。
不同日志的清理逻辑不同。下面以“防火墙设备版本为StoneOS V5.5R12，硬盘容量为100G，会话日志存
储阈值为85%的会话日志”为例，说明系统如何清理日志。用户可以在实际组网环境中根据日志量，及时调
整存储阈值。
用户在WebUI的“系统> 系统管理> 存储管理”页面中配置整体存储比例阈值为90%，会话日志存储阈值
为85%。用户组网中实际产生的会话日志量为88256M。
计算得到：会话日志分配存储，即会话日志告警阈值为100G*85%=87040M。
则当日志达到87040M时，系统产生告警，开始自动删除较早的会话日志。
系统需要删除的会话日志量：88256M-87040M+300M=1516M。

<!-- 来源页 719 -->
针对上例，计算参数罗列如下：
计算参数
举例
整体存储比例阈值
90%
会话日志存储阈值
85%
说明：StoneOS V5.5R11版本开始，如果在WebUI中开启“启用日志分类”或者在
CLI中配置storage threshold log mode by-log-type命令，每种日志类型可以
单独指定自身存储阈值，超过即产生告警。同时也受整体存储比例阈值约束，整机已
使用存储超过整机存储也会产生告警。
会话日志分配存储
（即，会话日志告警
100G*85%=85G，85G=87040M

<!-- 来源页 720 -->
计算参数
举例
阈值）
实际会话日志占用存
储
88256M
需要删除的会话日志
量
88256M-87040M+300M=1516M。
说明：如果需要删除的会话日志量大于10000M，则单次最多删除10300M。未删除
的会话日志在下个检测周期中达到告警阈值时，会继续删除。
所以，在by log模式下，当实际会话日志占用存储> 会话日志分配存储时：
需要删除的会话日志量=实际会话日志占用存储-会话日志告警阈值+实际会话日志占用存储*10%
如果会话日志删除后，系统仍然提示“存储空间已达阈值”或者产生“日志超出存储阈值”的事件日志，系
统会根据硬盘超限大小，按比例对每种日志继续进行删除。
说明：“实际会话日志占用存储*10%”表示多删除一张日志表的存储。当“实际会话日志占用存储*10%”
大于300M，则取300M。

<!-- 来源页 721 -->
配置系统重启
在设备运行过程中，用户可能因为多种原因需要重启设备或者扩展模块。对于设备重启，用户可以选择直接
下电再重新上电的方式，也可以通过CLI或者WebUI的方式进行重启操作。对于扩展模块重启，用户可以通
过CLI的方式进行重启操作。
重启设备
重启设备，请在执行模式下使用reboot命令。请参阅以下示例：
hostname# reboot
System configuration has been modified. Save? [y]/n ( 键入字母“y”或者敲回车键，系
统将保存配置；键入字母“n”，系统将不保存配置；默认操作为“y”)
Building configuration..
Saving configuration is finished
System reboot, are you sure? y/[n] ( 键入字母“y”，系统将重启；键入字母“n”或者敲回
车键，系统将返回到执行模式)
执行reboot命令时，系统首先会提示用户是否保存先前所做的配置。请谨慎使用reboot命令，因为执行该
命令会导致网络工作在短时间内中断。
重启扩展模块
对于多扩展模块设备，用户可以对单个模块进行重启。重启扩展模块，请在执行模式下使用reboot slot
{slot-number}命令。请参阅以下示例：
hostname# reboot slot slot8
Reboot slot8, are you sure? y/[n]: ( 键入字母“y”，Slot8将重启；键入字母“n”或者敲
回车键，系统将返回到执行模式)

<!-- 来源页 722 -->
离线模式
离线模式的核心价值在于为设备提供软件形式的隔离能力，适用于系统升级、设备配件更换、设备状态异常
等软硬件维护场景。通过这一功能，设备可直接以软件形式从网络中隔离，无需用户进行手动拔线等物理操
作。开启离线模式后，只有MGT接口（若设备没有MGT接口，则为绑定至mgt安全域上的物理接口）和HA
链路可以收发报文，其余接口将无法收发报文（但接口状态不会改变），以此避免在维护时对网络中的其他
设备造成影响。离线模式默认为关闭状态。
离线模式下并不影响HA协商，系统仍会进行HA配置同步和HA会话同步。在关闭离线模式后，建议用户手动
进行一次HA同步。
注意:
l
开启离线模式时必须使用MGT接口作为管理接口，如果设备没有MGT接口，需要将绑定至mgt
安全域上的物理接口作为管理接口。并且在HA场景下管理接口需要关闭HA同步或者配置管理
IP。
l
在公有云平台HA部署场景下，如果防火墙只能通过trust-vr和云平台控制中心进行交互，则不
支持使用离线模式。
l
在设备处于离线模式下，执行系统升级、重启等维护操作，不会改变离线模式的状态。
开启/关闭离线模式
离线模式默认为关闭状态。开启/关闭离线模式，在全局配置模式下，使用以下命令：
l
开启离线模式：offline enable
l
关闭离线模式：offline disable
开启离线模式后，命令行将显示offline标记：

<!-- 来源页 723 -->
切换数据库
设备支持使用MySQL数据库和国产数据库PolarDB两种数据库，用户可以根据实际情况自行切换使用的数据
库类型，默认为MySQL数据库。切换数据库后，需要重启设备使配置生效。
注意:
l
仅K系列设备（K9180除外）支持使用国产数据库PolarDB。
l
PolarDB数据库受许可证控制，安装国产数据库许可证后才可切换至PolarDB数据库。
l
在K3280、K2580和K2560平台上使用国产数据库时，建议将VSYS数量设置为小于等于5。如
果VSYS数量超过5，则可能引发与硬盘读写相关的业务异常问题。例如：在查询威胁日志时，
出现响应缓慢的情况；在打开iCenter页面时，页面loading时间增长等。
l
切换数据库功能不支持HA同步，需要在主备设备上分别进行数据库切换。若主备设备使用不同
的数据库，也并不影响HA协商和HA配置同步。
l
切换数据库后，将读取不到冻结数据库的相关数据，但可以在WebUI“设备管理> 存储管理”
中查看冻结数据库数据占用的存储空间大小。
l
系统会将生成的报表文件存储在设备上，将报表文件的生成记录和文件路径信息存储在数据库
中。在报表汇总页面查询的数据是数据库中保存的记录信息。切换数据库后，由于查询不到切
换前数据库中的记录，会导致用户无法管理（查看/删除）设备上之前生成的报表文件。这些残
留的报表文件会占用存储空间，影响后续的报表生成，并且只能通过清除报表文件进行清除。
因此建议用户在删除冻结数据库数据后，也同步清除报表文件中的数据。
切换至PolarDB数据库，在任意模式下，使用以下命令：
exec database domestic-db enable
切换至MySQL数据库，在任意模式下，使用以下命令：
exec database domestic-db disable
删除冻结数据库数据
冻结数据库指当前为非运行状态的数据库，用户可以删除冻结数据库中的全部数据。
删除冻结数据库数据，在任意模式下，使用以下命令：
exec database remove-frozen-data

<!-- 来源页 724 -->
登录WebUI的二次认证功能(安全认证）
管理员可以通过短信、邮箱二次认证的方式登录WebUI。
开启短信/邮箱二次认证
配置短信/邮箱认证功能，在全局配置模式下，使用以下命令：
admin {sms-auth [gateway provider-name | modem] | email-auth [smtp smtp-name] |
verification-timeout timeout | auth-sender sender-name}
l
sms-auth– 开启短信认证功能。开启短信认证后，未配置手机号码的管理员将无法登录设备。
l
gateway provider-name– 指定短信认证的方式为短信网关。
l
modem – 指定短信认证的方式为短信猫。
l
email-auth– 开启邮箱认证功能。开启邮箱认证后，未配置邮箱地址的管理员将无法登录设备。
l
smtp smtp-name – 指定邮箱服务器。
l
verification-timeout timeout– 指定短信/邮箱认证码的有效时间，取值范围是1到30分钟。默认是5
分钟。如果用户在有效时间内没有输入短信/邮箱认证码，将无法登录设备。
l
auth-sender sender-name– 指定短信/邮件发送者名称以显示在短信内容或邮件中。取值范围是1到
64字符。
在全局配置模式下，使用no admin sms-auth关闭短信认证功能。
在全局配置模式下，使用no admin email-auth关闭邮箱认证功能。
注意: 短信/邮箱认证和第三方平台单点登录设备的功能无法同时开启。
配置管理员的手机号码
当开启短信认证功能后，管理员可以通过手机验证码进行二次验证。未配置手机号码的管理员将无法登录设
备的WebUI页面。配置管理员的手机号码，在管理员配置模式下，使用以下命令：
phone phone-number
l
phone-number – 指定管理员的手机号码。
配置管理员的邮箱地址
当开启邮箱认证功能后，管理员可以通过邮箱验证码进行二次验证。未配置邮箱地址的管理员将无法登录设
备的WebUI页面。配置管理员的手机号码，在管理员配置模式下，使用以下命令：

<!-- 来源页 725 -->
email email
l
email – 指定管理员的邮箱地址。

<!-- 来源页 726 -->
配置WebUI登录时浏览器页签标题
通过WebUI登录设备时，浏览器页签标题默认为“Hillstone Networks”。
用户可以配置该标题为设备的主机名称、设备型号、管理地址中的一项或多项。配置将在下一次通过WebUI
登录设备时生效。
配置页签标题
配置WebUI登录时的浏览器页签标题，在全局配置模式下，使用以下命令：
webui-title-display-mode [hostname] [platform] [manage-address]
l
hostname - 指定设备的主机名称为页签标题。
l
platform - 指定设备型号为页签标题。
l
manage-address - 指定设备的管理地址为页签标题。
如果执行该命令时未设置任意一项，或者删除页签标题设置，浏览器仍将显示默认的页签标题。设置多项
时，各项不限制排列顺序。实际的页签标题在显示时，各项的排列顺序与配置的顺序一致。
删除页签标题设置
删除页签标题设置，在全局配置模式下，使用以下命令：
no webui-title-display-mode
查看页签标题设置
查看页签标题设置，在任意模式下，使用以下命令：
show webui-title-display-mode

<!-- 来源页 727 -->
指定SSH访问时RSA密钥位数
用户使用SSH方式访问设备时，客户端需要通过算法来验证服务器的真实性，RSA算法就是其中一种。
系统支持指定RSA算法生成的密钥位数，如不指定，系统默认生成1024位的RSA密钥。指定RSA算法生成的
密钥位数，在任意模式下，使用以下命令：
exec ssh generate-host-key rsa modulus {1024 | 2048 | 4096}

<!-- 来源页 728 -->
配置设备作为SSH/Telnet客户端
防火墙设备可以作为SSH或者Telnet客户端，连接并登录其它SSH或者Telnet服务器设备。
配置设备作为SSH客户端
设备作为SSH客户端连接并登录其它SSH服务器设备时，支持3种认证方式，包括密码认证、密钥认证以及密
码密钥认证。配置设备作为SSH客户端连接并登录其它SSH服务器设备，在执行模式下，使用以下命令：
ssh user user-name ip {A.B.C.D | X:X:X:X::X} [port port] [publickey publickey_name] [vrouter
vrouter-name]
l
user user-name - 指定登录SSH服务器的用户名。
l
ip {A.B.C.D | X:X:X:X::X} - 指定登录的SSH服务器的IPv4（A.B.C.D）或者IPv6（X:X:X:X::X）地
址。
l
port port - 指定建立SSH连接的目的端口号。取值范围为1至65535，默认值为22。
l
publickey publickey_name - 指定SSH密钥对名称。配置该参数后，如果SSH服务器端的认证方式为
密钥认证，防火墙可以直接登录SSH服务器；如果SSH服务器端的认证方式为密码密钥认证，输入正确
的登录密码后才可以登录SSH服务器。如果不配置该参数，防火墙将通过密码认证的方式登录SSH服务
器，输入正确的登录密码即可登录。注意：为保证成功进行密钥认证或者密码密钥认证，SSH服务器端
需要配置密钥对的SSH格式公钥。关于如何获取密钥对的SSH格式公钥信息，请参阅显示PKI配置信息。
l
vrouter vrouter-name - 指定建立SSH连接时使用的VRouter。默认为当前VSYS中的默认VRouter。
注意: 对于X系列设备及SG-6000-K9180设备，在双主控（SCM）HA场景中，仅支持在主用主控
模块中进行上述命令配置。
配置设备作为Telnet客户端
设备作为Telnet客户端连接并登录其它Telnet服务器设备时，支持密码认证方式。配置设备作为Telnet客
户端连接并登录其它Telnet服务器设备，在执行模式下，使用以下命令：
telnet ip {A.B.C.D | X:X:X:X::X} [port port] [vrouter vrouter-name]
l
ip {A.B.C.D | X:X:X:X::X} - 指定登录的Telnet服务器的IPv4（A.B.C.D）或者IPv6（X:X:X:X::X）
地址。
l
port port - 指定建立Telnet连接的目的端口号。取值范围为1至65535，默认值为23。

<!-- 来源页 729 -->
l
vrouter vrouter-name - 指定建立Telnet连接时使用的VRouter。默认为当前VSYS中的默认
VRouter。
注意: 对于X系列设备及SG-6000-K9180设备，在双主控（SCM）HA场景中，仅支持在主用主控
模块中进行上述命令配置。

<!-- 来源页 730 -->
配置Banner功能
Banner用于显示登录后的声明信息，用户可以自定义Banner信息内容。
在全局配置模式下，使用以下命令配置Banner功能：
admin login-banner Banner-content
l
Banner-content – 指定Banner信息内容，长度范围是1到4096个字符。执行该命令后，系统创建指
定内容的Banner信息；如果已存在Banner信息，则将Banner信息内容修改为指定内容。
使用no admin login-banner命令删除Banner信息内容，显示为空。
注意:
l
在编辑Banner信息内容时，如果需要换行，需输入“\n”;需要空格，需输入双引号“”。
l
仅支持在使用SSH、Telnet或者Console方式登录设备时显示Banner信息。

<!-- 来源页 731 -->
配置系统信息显示语言
系统信息包括日志信息、错误信息和提示信息。设备支持简体中文和英文两种系统信息显示语言，在全局配
置模式下，使用以下命令设置显示语言：
language {en | zh_CN}
l
en – 设置系统信息显示语言为英文。默认情况下，系统信息显示语言为英文。
l
zh_CN – 设置系统信息显示语言为简体中文。
在全局配置模式下使用no language命令恢复显示语言为默认情况。
需要注意的是，该命令的设置不会影响Web管理界面的语言。

<!-- 来源页 732 -->
配置设备所在国家/地区
用户可根据实际业务部署情况，为每一台防火墙设备指定其所在国家/地区，以便于运维管理。
为当前设备指定其所在国家/地区，在全局配置模式，输入以下命令：
location country country-name [province province-name]
l country-name - 指定当前设备所在国家的名称。取值范围为1到31个字符。
l province province-name -指定当前设备所在地区的名称。取值范围为1~31个字符。
在全局配置模式下，使用以下命令，删除当前设备所在国家/地区的相关配置：
no location

<!-- 来源页 733 -->
配置文件
该功能在不同平台上的呈现方式有所差异，请以实际页面为准。
系统的配置信息都被保存在系统的配置文件中。用户通过运行相应的命令或者访问相应的WebUI页面查看系
统的各种配置信息，例如系统的初始配置信息和当前配置信息等。配置文件中保存的用来初始化设备的配置
信息称作起始配置信息，设备通过读取起始配置信息进行启动时的初始化工作；如果找不到起始配置信息，
则使用设备的缺省参数初始化。与起始配置信息相对应，设备运行过程中正在生效的配置称为当前配置信
息。
系统起始配置信息包括系统的当前起始配置信息（系统启动时使用的配置信息）和系统的备份起始信息。系
统记录最近十次保存的配置信息，最近一次保存的配置信息会记录为系统的当前起始配置信息，当前系统配
置信息以“Startup”作为标记。前九次的配置信息按照保存时间的先后以数字0到8作为标记。
配置文件以命令行的格式保存配置信息，并且也以这种格式显示配置信息。用户可以导出、恢复、删除已创
建的系统配置文件，也可以导出当前的系统配置。
注意: 如果已回退到已保存的指定的起始配置信息，那么该配置信息将会以“startup”作为标
记。
配置文件管理
配置Hillstone设备配置信息
用户可以查看和保存系统的配置信息，也可以导出和导入配置信息。
查看配置信息
配置文件中保存的用来初始化系统的配置信息称作起始配置信息，系统通过读取起始配置信息进行启动时的
初始化工作；如果找不到起始配置信息，系统则使用系统的缺省参数初始化。与起始配置信息相对应，系统
运行过程中正在生效的配置称为当前配置信息。
系统起始配置信息包括系统的当前起始配置信息（系统启动时使用的配置信息），和系统的备份起始信息。
系统纪录最近十次保存的配置信息，最近一次保存的配置信息会纪录为系统的当前起始配置信息，当前系统
起始配置信息以“startup”作为标记。前九次的配置信息按照保存时间的先后以数字0到8作为标记。
注意: 如果已回退到已保存的指定的起始配置信息，那么该配置信息将会以“startup”作为标
记。

<!-- 来源页 734 -->
查看系统的当前起始配置信息
查看系统的当前起始配置信息，在任何命令模式下输入以下命令：show configuration [startup]
查看设备的备份起始信息
查看设备的备份起始信息，在任何命令模式下使用以下命令：
show configuration backup number
l
number - 备份起始信息的数字标记。
查看设备的当前配置信息
查看设备的当前配置信息，在任何命令模式下输入以下命令：
show configuration
查看设备的当前配置锁定状态
型号说明：仅云·界平台支持该功能。
“配置锁定状态”用于实时显示系统配置是否被锁定，包含“未锁定”和“已锁定”两种状态。状态为“未
锁定”时，可正常登录设备，查看及修改系统配置；状态为“已锁定”时，仅可正常登录和查看配置，无法
进行修改操作。触发“已锁定”状态通常有三类场景：设备平台试用许可证到期未续期、虚拟CPU订阅过期
未续订，或是管理员通过API锁定配置。
查看设备的当前配置锁定状态，在任何命令模式下输入以下命令：
show config-status
以下为回显示例：
hostname(config)# show config-status
=====================================
config status: Locked
manual-lock: Locked
//表示当前锁定状态是设备通过API 接口手动下发指令锁定
hostname(config)# show config-status
=====================================
config status: Locked

<!-- 来源页 735 -->
platform-license：License does not match the
platform
//表示当前锁定是因为系统安装的许可证与当前设备平台不一
致触发
hostname(config)# show config-status
=====================================
config status: Locked
platform-license：License not activated or not
installed
//表示当前锁定状态是因为平台试用许可证未激活或未安装触
发
hostname(config)# show config-status
=====================================
config status: Locked
vcore-license：Expired
//表示当前锁定状态是因为虚拟CPU 订阅许可证过期
比较设备的当前配置信息与当前/备份起始配置信息的差异
用户可以比较设备的当前配置信息与当前起始配置信息(startup配置文件)的差异，以便决定是否将当前的配
置信息保存到startup配置文件和新的备份配置文件中，或者当用户准备将某一个备份起始信息（backup配
置文件）作为下一次系统启动的配置文件时，可以先比较当前配置信息与指定backup配置文件的差异。在
任何命令模式下输入以下命令：
show configuration difference {startup | backup number} [current-line current-line-number |
saved-line saved-line-number]
l
startup – 指定比较设备的当前配置信息与当前起始配置信息的差异。
l
backup number – 指定比较设备的当前配置信息与某一个备份起始配置信息的差异。
l
current-line current-line-number – 指定从设备当前配置信息的第current-line-number行和
startup/backup配置文件的第一行开始比较差异。如不指定，则均从第一行开始比较。
l
saved-line saved-line-number – 指定从设备当前配置信息的第一行和startup/backup配置文件的
第saved-line-number行开始比较差异。如不指定，则均从第一行开始比较。
例如：
hostname#show configuration difference startup current-line 3（从系统当前配置信息的第三
行和startup配置文件的第一行开始比较差异）
--- current.config（-表示当前配置信息独有的内容）
+++ startup.config（+表示startup/backup配置文件独有的内容）

<!-- 来源页 736 -->
@@ -1,5 +1,9 @@（从系统当前配置信息的第三行和startup配置文件的第一行开始比较时，当前配置信
息的第三行将作为起始行，往下数5行与startup配置文件的第一行往下数9行，之间内容对比有差异）
-# global configuration version: 194（-表示当前配置信息独有的内容）
-# configuration sequence number: 383
+# Generated by autosave at 2023-09-11 15:54:37（+表示startup配置文件独有的内容）
+# Size is 11876 bytes
+# Software Version 5.5 SG6000-MX_MAIN-7x-V6-r0828.bin 2023/08/28 21:01:28
+
+# global configuration version: 192
+# configuration sequence number: 381
# PREVIOUS CONFIGERATION START（无-或+表示两者内容相同）
sandbox cloud-server-check enable
# END OF PREVIOUS CONFIGERATION
查看设备的当前接口配置信息
查看设备的当前接口配置信息，在任何命令模式下输入以下命令：
show configuration interface [interface-name | last number]
l
interface-name – 指定显示配置信息的接口名称。
l
last number – 指定显示配置信息的接口条目数。显示从倒数指定数值的条目开始到最后条目的接口配
置信息。如果指定数值大于所有接口条目数，则显示所有接口配置信息。
查看设备的备份起始信息记录
查看设备的备份起始信息记录，在任何命令模式下输入以下命令：
show configuration record
查看设备的当前运行的配置信息记录
查看设备的当前运行的配置信息记录，在任何命令模式下输入以下命令：
show configuration running

<!-- 来源页 737 -->
查看设备的当前地址簿配置信息
查看设备的当前地址簿配置信息，在任何命令模式下输入以下命令：
show configuration [ ipv4 | ipv6 ] address [ lastnumber | address-name ]
l
[ipv4 | ipv6] - 指定显示IPv4（ipv4）或者IPv6（ipv6）地址簿条目配置信息，包括地址条目名称、类
型（预定义或者自定义）和地址成员。如不指定，显示所有IPv4和IPv6地址簿条目的配置信息。
l
last number – 指定显示配置信息的地址簿条目数。显示从倒数指定数值的条目开始到最后条目的地址
簿配置信息。如果指定数值大于所有地址簿条目数，则显示所有地址簿配置信息。
l
address-name– 显示指定名称的地址簿条目配置信息，包括地址条目名称、类型（预定义或者自定
义）和地址成员。
查看设备的当前策略配置信息
查看设备的当前策略配置信息，在任何命令模式下输入以下命令：
show configuration policy [ last number]
l
last number – 指定显示配置信息的策略条目数。显示从倒数指定数值的条目开始到最后条目的策略配
置信息。如果指定数值大于所有策略条目数，则显示所有策略配置信息。
查看设备的当前路由配置信息
查看设备的当前路由配置信息，在任何命令模式下输入以下命令：
show configuration vrouter [last number]
l
last number – 指定显示配置信息的路由条目数。显示从倒数指定数值的条目开始到最后条目的路由配
置信息。如果指定数值大于所有路由条目数，则显示所有路由配置信息。
查看设备当前的HA配置信息
查看设备当前的HA配置信息，在任何命令模式下输入以下命令：
show configuration ha
以xml方式输出当前配置信息
以xml方式输出当前配置信息，在任何命令模式下输入以下命令：
show configuration xml

<!-- 来源页 738 -->
回退配置信息
回退配置信息，系统支持以下两种方式：
在执行模式下，使用以下命令回退起始配置信息。系统能够纪录最近十次保存的起始配置信息，用户可以根
据需要回退到已保存的指定的起始配置信息。
回退配置文件时支持开启新配置立即生效功能，该功能支持回退配置即时生效且无需重启设备。开启后，系
统将只对范围内的配置执行检查与回退操作，范围外的功能将保持不变。具体规则如下：
l
对于范围内的功能，系统会自动检查当前配置与待回退配置文件的差异，仅回退存在差异的配置，回退
后配置立即生效，无需重启设备。
l
对于范围外的功能，系统不执行任何配置差异检查，也不会进行配置回退操作，该部分配置保持不变。
l
范围内的功能：安全策略、NAT、地址簿、域名簿、服务簿、时间表、监测对象、安全域、路由（不包
含OSPF和BGP）、本地用户以及应用簿（不包含应用特征规则）。
注意: 如需开启新配置立即生效功能，请注意以下事项：
l
待恢复的系统配置文件版本需要与当前的系统版本保持一致。
l
若待恢复的系统配置文件与当前的系统配置文件差异过大（存在差异的命令行超过10000
行），则无法使新配置立即生效，需要重启设备使之生效。
rollback configuration backup number [loading-immediately]
l
number – 备份起始配置信息的数字标记。
l
loading-immediately - 指定回退配置立即生效且无需重启设备。指定后，系统将按照相应规则进行
配置文件回退，回退的配置将立即生效且不需重启设备；若不指定，则系统将回退全部配置，且需重启
设备使回退的配置生效。
在配置回滚模式下，使用以下命令回退配置信息并退出配置回滚模式。用户不需要重启设备，该配置直接生
效。
exec configuration rollback
注意: 在执行模式下，使用exec configuration start进入配置回滚模式。
示例：
hostname# exec configuration start（进入配置回滚模式）
hostname[TRN]# configure （进入全局配置模式）

<!-- 来源页 739 -->
…… （进行任意配置，且所做配置即时生效）
hostname[TRN](config)# exec configuration rollback （回退配置并退出配置回滚模式）
hostname#
退出配置回滚模式
直接退出配置回滚模式，系统支持以下两种方式：
在配置回滚模式下，使用以下命令直接退出配置回滚模式：
exec configuration commit
例如：
hostname# exec configuration start （进入配置回滚模式）
hostname[TRN]# configure （进入全局配置模式）
…… （进行任意配置，且所做配置即时生效）
hostname[TRN](config)# exec configuration commit （直接退出配置回滚模式）
hostname#
在配置回滚模式下，使用exit命令直接退出登录终端，从而退出配置回滚模式。
l
当不同用户同时登录设备时，先进入配置回滚模式的用户可以继续配置操作，其他用户无法进行配置操
作。
l
当相同用户通过不同访问方式登录设备时，先进入配置回滚模式的某访问方式的用户可以继续配置操
作，其他访问方式的用户无法进行配置操作，但其可以使用exec configuration commit或者exec
configuration rollback命令强制进入配置回滚模式的某访问方式的用户退出配置回滚模式。
配置退出配置回滚模式的动作
当使用exit命令退出配置回滚模式时，默认情况下，系统会直接退出配置回滚模式。回退配置后退出配置回
滚模式，在全局配置模式下，使用以下命令：
cli-exit-action rollback
恢复直接退出配置回滚模式，在全局配置模式下，使用以下命令：
cli-exit-action commit
删除配置文件
用户可以删除设备的起始配置信息。删除起始配置信息，在执行模式下，使用以下命令：
delete configuration {startup | backup number}

<!-- 来源页 740 -->
l
startup – 删除当前起始配置信息。
l
backup number – 删除指定的备份起始配置信息，number为备份起始配置信息的数字标记。
保存配置信息
用户可以保存系统的当前配置信息使其成为系统下次启动时的起始配置。保存系统的当前配置信息，在任何
命令模式下输入以下命令：
save [string]
l
string - 对所保存配置信息的描述。如果不使用string对保存的配置文件进行描述，系统会直接覆盖原
有配置文件。
自动备份配置文件
用户可以通过配置自动备份配置文件功能，能够实现设备定期检查配置文件，在当前配置文件发生变化时，
系统会自动将当前的配置文件上传到FTP、TFTP、SFTP或FTPS服务器上。
指定自动备份配置文件到FTP服务器
指定自动备份配置文件到FTP服务器，在全局配置模式下，使用以下命令：
configuration auto-backup ftp ip-address [user user-name password password] [vrouter
vrouter-name] path path [interval time-value] [cpu-threshold threshold-value]
l
ip-address - 指定FTP服务器的IP地址。
l
user user-name password password – 指定访问FTP服务器的用户名和密码。
l
vrouter vrouter-name – 指定VRouter的名称。
l
path path – 指定配置文件的上传路径。
l
interval time-value – 指定自动备份配置文件的时间间隔。单位为小时，默认值是1小时。范围是1到
7*24小时。如果不指定该参数，系统将每1小时检查配置文件，在发生变化时，自动备份到FTP服务器
上。
l
cpu-threshold threshold-value - 指定向FTP服务器自动备份配置文件的CPU阈值，范围是1到99，
默认为无限制。指定阈值后，当CPU占用率超过阈值时，该周期内不向FTP服务器发送配置文件，等待下
个周期再次尝试发送。
在全局配置模式下，使用no configuration auto-backup ftp取消自动备份配置文件到FTP服务器。

<!-- 来源页 741 -->
指定自动备份配置文件到TFTP服务器
指定自动备份配置文件到TFTP服务器，在全局配置模式下，使用以下命令：
configuration auto-backup tftp ip-address [vrouter vrouter-name] path path [interval timevalue]
在全局配置模式下，使用no configuration auto-backup tftp取消自动备份配置文件到TFTP服务器。
指定自动备份配置文件到SFTP服务器
指定自动备份配置文件到SFTP服务器，在全局配置模式下，使用以下命令：
configuration auto-backup sftp ip-address [user user-name password password] [vrouter
vrouter-name] path path [interval time-value]
在全局配置模式下，使用no configuration auto-backup sftp取消自动备份配置文件到SFTP服务器。
指定自动备份配置文件到FTPS服务器
指定自动备份配置文件到FTPS服务器，在全局配置模式下，使用以下命令：
configuration auto-backup ftps ip-address [user user-name password password] [vrouter
vrouter-name] path path [interval time-value]
在全局配置模式下，使用no configuration auto-backup ftps取消自动备份配置文件到FTPS服务器。
查看自动备份配置文件信息
查看自动备份配置文件功能的信息，在任何命令模式下输入以下命令：
show configuration auto-backup
导出配置信息
用户可以导出系统的当前起始配置信息、备份配置信息及所有VSYS起始配置信息到FTP服务器、TFTP服务
器、SFTP服务器、FTPS服务器或者U盘。
导出系统配置信息到FTP服务器
导出系统配置信息到FTP服务器，在执行模式下使用以下命令：
export configuration {startup [config-filetype zip [zip-password zip-password] ] | backup
number| all-vsys} to ftp server ip-address [vrouter vrouter-name][ user user-name
password password] [file-name]

<!-- 来源页 742 -->
l
startup | backup number| all-vsys– 指定导出的配置信息。startup为导出当前起始配置信
息；number 为导出以number为标识的备份配置信息; all-vsys为导出所有VSYS当前起始配置信息。
l
config-filetype zip [zip-password zip-password] - 导出当前的起始配置信息时，支持导出加密
和不加密的ZIP文件。zip-password指定ZIP文件的压缩密码。
l
ip-address – 指定FTP服务器的IP地址。
l
vrouter-name - 导出指定VRouter的配置信息。
l
user user-name password password – 指定访问FTP服务器的用户名和密码。
l
file-name – 指定导出的配置信息文件的名称。
导出系统配置信息到TFTP服务器
导出系统配置信息到TFTP服务器，在执行模式下使用以下命令：
export configuration {startup [config-filetype zip [zip-password zip-password] ] | backup
number | all-vsys} to tftp server ip-address [vrouter vrouter-name] [file-name]
导出系统配置信息到SFTP服务器
导出系统配置信息到SFTP服务器，在执行模式下使用以下命令：
export configuration {startup [config-filetype zip [zip-password zip-password] ] | backup
number | all-vsys} to sftp server ip-address [vrouter vrouter-name][user user-name
password password] [file-name]
导出系统配置信息到FTPS服务器
导出系统配置信息到FTPS服务器，在执行模式下使用以下命令：
export configuration {startup [config-filetype zip [zip-password zip-password] ] | backup
number | all-vsys} to ftps server ip-address [vrouter vrouter-name][user user-name
password password] [file-name]
导出系统配置信息到U盘
导出系统配置信息到U盘，在执行模式下使用以下命令：
export configuration {startup [config-filetype zip [zip-password zip-password] ] | backup
number | all-vsys} to {usb0 | usb1} [vrouter vrouter-name] [file-name]

<!-- 来源页 743 -->
导入配置信息
用户可以通过FTP、TFTP服务器、SFTP服务器或FTPS服务器导入配置信息，也可以将配置信息放入U盘
中，通过设备的USB口导入配置信息。
注意: 导入配置信息文件后，需重启生效。
从FTP服务器导入配置信息
从FTP服务器导入配置信息，在执行模式下使用以下命令：
import configuration [all-vsys | config-filetype zip [zip-password zip-password] ] from ftp
server ip-address user user-name password password [vrouter vrouter-name] file-name
l
all-vsys – 导入所有VSYS配置信息。
l
config-filetype zip [zip-password zip-password] - 指定导入的配置文件类型为ZIP，如果是加密
文件，需输入压缩密码。
l
ip-address – 指定FTP服务器的IP地址。
l
user user-name password password – 指定FTP服务器的用户名和密码。
l
vrouter-name - 为指定的VRouter导入配置信息。
l
file-name – 指定导入的配置信息文件的名称。
从TFTP服务器导入配置信息
从TFTP服务器导入配置信息，在执行模式下使用以下命令：
import configuration [all-vsys | config-filetype zip [zip-password zip-password] ] from tftp
server ip-address [vrouter vrouter-name] file-name
从SFTP服务器导入配置信息
从SFTP服务器导入配置信息，在执行模式下使用以下命令：
import configuration [all-vsys | config-filetype zip [zip-password zip-password] ] from sftp
server
ip-address [vrouter vrouter-name] [user user-name password password] [filename]

<!-- 来源页 744 -->
从SFTP服务器导入配置信息
从SFTP服务器导入配置信息，在执行模式下使用以下命令：
import configuration [all-vsys | config-filetype zip [zip-password zip-password] ] from sftp
server ip-address [vrouter vrouter-name] [user user-name password password] [file-name]
从U盘导入配置信息
从U盘导入配置信息，在执行模式下使用以下命令：
import configuration [all-vsys | config-filetype zip [zip-password zip-password] ] from
{usb0 | usb1} [vrouter vrouter-name] file-name
启用/禁用自动导入USB中配置文件功能
默认情况下，当设备系统启动时，将会自动导入USB中的配置文件，即替换设备中已存在的所有配置文件，
包括预定义配置文件和增量配置文件（在预定义配置信息基础上增加的配置信息），用户可以通过命令禁用
该功能，不会自动导入配置文件。禁用或启用该功能，在全局配置模式下，使用以下命令：
l
禁用：configuration load-by-usb disable
l
启用：configuration load-by-usb enable
自动导入USB中的配置文件时请注意：
l
导入的预定义配置文件名称格式为“sn_XXX.config”，其中“sn”表示为设备SN号，“XXX”表示为
用户自定义字段，由英文字符、数字或下划线组成，最多不能超过128字节。自动导入后，将会在USB的
根目录中记录导入日志信息。如果USB中存在多个设备SN号相同的配置文件，用户可以将配置文件的名
称格式修改为“sn_时间戳.config”或者“sn_时间戳_XXX.config”，系统会导入时间戳最新的配置
文件作为系统启动文件。其中“时间戳”的格式为“YYYYMMDDHHMMSS”（Y为年，M为月，D为
日，H为时，采用24小时制，M为分，S为秒），例如20220521143030。
l
导入的增量配置文件名格式为“sn-inject_XXX.config”，其中“sn”表示为设备SN号，“XXX”表
示为用户自定义字段，由英文字符、数字或下划线组成，最多不能超过128字节。自动导入后，将会在
USB的根目录中记录导入日志信息。如果USB中存在多个设备SN号相同的配置文件，用户可以将配置文
件的名称格式修改为“sn-inject_时间戳.config”或者“sn-inject_时间戳_XXX.config”，系统会导
入时间戳最新的配置文件作为系统启动文件。其中“时间戳”的格式为“YYYYMMDDHHMMSS”（Y为
年，M为月，D为日，H为时，采用24小时制，M为分，S为秒），例如20220521143030。

<!-- 来源页 745 -->
l
自动导入的配置文件必须是UTF-8编码文件且最大不能超过16M。
l
自动导入的配置文件需存放在USB的根目录下。
配置文件签名校验
为保障配置文件的数据机密性与完整性，系统支持在导出配置文件时添加数字签名，及导入配置文件时进行
签名校验。
l
配置文件导出阶段：系统根据配置文件的完整内容计算生成对应的数字签名，并将该签名写入配置文件
的头部区域。
l
配置文件导入阶段：系统读取待导入配置文件头部的数字签名信息，通过签名校验机制验证配置文件的
完整性与合法性。如校验失败，用户也可选择继续进行导入，否则导入失败。
对配置文件进行签名校验，在全局配置模式下使用以下命令：
configuration signature-verification SM2 key-pair key-pair-name
l
key-pair-name - 指定签名校验使用的密钥对，新建密钥对，请参考创建PKI密钥对。
在全局配置模式下，使用no configuration signature-verification取消配置文件的签名校验功能。
注意:
l
通过HSM/云景/ZTP开局等对设备进行配置的导入导出时不支持数字签名校验功能。
l
子VSYS的签名校验功能与根VSYS的配置保持一致。
l
重新生成的密钥与之前的密钥即使命名相同也是不同的密钥，无法进行校验。将设备恢复出厂
设置后，默认密钥会重新生成，因此设备恢复出厂设置后，导入的配置文件校验失败。
查看配置文件签名校验功能的相关信息，在任何模式下使用以下命令：
show configuration signature-verification
hostname# show configuration signature-verification
===================================================
Status: enable
Signature_algorithm: SM2
Signature_keypair_name: Default-Key-SM2
===================================================

<!-- 来源页 746 -->
恢复出厂配置
注意: 执行该命令后，设备的所有配置将被清除。请谨慎使用！
用户除使用设备上的CLR按键使系统恢复到出厂配置外，也可以使用命令恢复。
恢复出厂配置，请在任何模式下使用unset all命令，请参阅以下示例：
hostname# unset all
Remove all the configuration(back to factory default), are you sure? y/[n]: （键入字母
“y”，系统将恢复到出厂配置；键入字母“n”或者敲回车键，系统将返回到执行模式）
使用replace-config命令批量修改配置
replace-config命令用于对设备配置文本进行全局匹配与批量替换。系统管理员（admin）可通过该命令
快速完成大规模配置的批量修改，从而显著提升设备运维效率。
该命令提供3种匹配模式和3种替换模式，两者相互组合可形成9种配置方案，能够灵活满足不同运维场景下
的配置变更需求。
注意:
l
该命令为全局配置替换，替换行数最多不能超过一万行。
l
使用该命令完成配置替换后，新配置会立即生效，无需重启设备。
l
仅以下功能模块支持通过该命令进行配置替换：安全策略、NAT、地址簿、域名簿、服务簿、
时间表、监测对象、安全域、路由（不包含OSPF和BGP）、本地用户以及应用簿（不包含应用
特征规则）。
l
执行配置替换时，该命令会自动忽略不支持的功能模块，即匹配到不支持模块的配置项时，不
影响命令的整体执行。
l
若待替换的配置项已被其他功能模块引用，请先解除引用关系，再执行该命令，否则可能导致
执行失败。
匹配模式介绍
该命令支持以下3种匹配模式，用于定位待替换的配置文本。

<!-- 来源页 747 -->
l 精确匹配
l 包含匹配
l 正则匹配
精确匹配
精确匹配采用完全匹配机制，仅当目标内容与待查找的字符串完全一致时才能匹配成功。
匹配规则：
l 字符顺序、大小写和长度必须一致。
l 不支持通配符、模糊匹配或部分匹配。
适用场景与示例：
该模式适用于明确知道完整配置项名称或参数值的场景，定位精准，无歧义。
待查找的字符串
目标内容
匹配结果
admin
admin
√匹配
字符完全一致
admin
admin@1
× 不匹配
字符长度不一致
admin
Admin
× 不匹配
大小写不一致
包含匹配
包含匹配采用关键字包含匹配机制，只要待查找的关键字按原有顺序、连续不间断地出现在目标内容的任意
位置（开头、中间或末尾），即视为匹配成功。
匹配规则：
l 严格区分大小写。
l 不支持通配符或正则表达式。
l 同一目标内容中，首次匹配到关键字即执行，后续内容不再匹配。
l 关键字必须连续出现，不得有字符间隔。
适用场景与示例：
该模式适用于只知道部分关键字、需模糊定位配置项的场景，匹配范围较广。
待查找的关键字
目标内容
匹配结果
hello
helloWorld
√匹配

<!-- 来源页 748 -->
待查找的关键字
目标内容
匹配结果
关键字连续完整地出现在开头位置
hello
HelloWorld
× 不匹配
严格区分大小写，H与h不匹配
hello
heelloworld
× 不匹配
关键字要求作为完整的连续序列进行匹配，但目标内容中的e为连续
重复（如ee），不满足单字符匹配条件，因此匹配失败。
正则匹配
正则匹配采用正则表达式模式匹配机制，通过预定义的元字符、量词和分组等语法规则构建匹配模式，对目
标内容进行结构化匹配。
匹配规则：
l 采用贪婪匹配策略，即在保证整体匹配成功的前提下，尽可能多地匹配字符。
l 遵循标准正则表达式语法（如^匹配行首，\d匹配数字，[0-9]匹配数字范围等），具体匹配范围由表达式自身的
逻辑结构决定。
l 严格区分大小写。
l 正则表达式中包含空格时，需确保整个表达式正确包含在英文双引号内。
以下为通用正则表达式标准下的常用语法对照表，供您查阅。
元字符
功能含义
说明
|
或
匹配管道符| 左侧或右侧的子表达式，左侧优先。按从左到右依次尝试匹配各个
分支，最终选择能使整个正则表达式匹配成功的那一个。
例如：cat | dog，可以匹配“cat” 或“dog”。
[ ]
字符组
匹配该字符组内任意一个字符。支持使用连字符（-）定义范围。
例如：[0-9]，可以匹配任意一个数字字符；[A-Za-z]，可以匹配任意一个大小
写字母字符。
[^]
[!]
否定字符组
匹配该字符组内未列出的任意一个字符，即排除该字符组内的所有字符。
例如：[^0-9]或者[!0-9]，可以匹配任意非数字字符（如a、&等）。
*
量词（零次或多次）
匹配前一个元素零次或任意次数。
例如：a*，可以匹配“a”、“aa”、“aaa”等。
?
量词（零次或一次）
匹配前一个元素零次或一次。
例如：a?c，可以匹配“ac”或“c”。
+
量词（一次或多次）
匹配前一个元素一次或多次。
例如：a+，可以匹配“a”、“aa”、“aaa” 等，但不可以匹配空字符串。
{n}
量词（n次）
匹配前一个元素恰好n次。

<!-- 来源页 749 -->
元字符
功能含义
说明
例如：[0-9]{4}，可以匹配任意4位数字，如2026、8080等。
{n,}
量词（至少n次）
匹配前一个元素至少n次。
例如：[0-9]{3,}，可以匹配3位及以上的任意数字，如123、4567等。
{n,m}
量词（n到m次）
匹配前一个元素n到m次（含两端）。
例如：[0-9]{2,5}，可以匹配2位到5位的任意数字，如“12”、“12345”等。
.
通配符
匹配除换行符（\n）以外的任意单个字符。
例如：a.c，可以匹配“abc”、“a1c”、“a-c”等。
^
位置锚定
匹配字符串的起始位置。
例如：^host，可以匹配以host开头的字符串，如hostname。
$
位置锚定
匹配字符串的结束位置。
例如：enable$，可以匹配以enable结尾的字符串，如disenable。
\
转义字符
取消后续元字符的特殊含义，将其解析为字面值字符。
例如：\.，可以匹配点号（.）；\\，可以匹配反斜杠（\）。
( )
捕获分组
将括号内的多个元素组合为一个整体，支持对该整体应用量词。匹配的内容会
按左括号出现的顺序自动编号（\1、\2…），以便后续通过反向引用方式再次
调用。
例如：(ab)+，可以匹配“ab”、“abab”、“ababab”等。
适用场景与示例：
该模式适用于需要进行模糊匹配、范围匹配或符合特定规则的批量定位场景，灵活性最高，但需用户具备正
则表达式编写能力。
正则表达式
目标内容
匹配结果
[A-Za-z]+_[0-9]+
abc_123
√匹配
字母、下划线、数字三项要求均匹配
[A-Za-z]+_[0-9]+
abc123
× 不匹配
缺少下划线分隔符
[A-Za-z]+_[0-9]+
abc_
× 不匹配
下划线后缺少数字
[A-Za-z]+_[0-9]+
abc_12a
× 不匹配
数字部分包含字母，不符合[0-9]的数字限定
^192\.168\.[0-9]{1,3}\.[0-9]
{1,3}$
192.168.1.2
√匹配
所有内容均匹配，格式正确
^192\.168\.[0-9]{1,3}\.[0-9]
{1,3}$
192.168.1000.1
× 不匹配
1000为4位数字，超出{1,3}允许的3位上限
^192\.168\.[0-9]{1,3}\.[0-9]
{1,3}$
192.168.1.a
× 不匹配
末尾部分包含字母a，不符合[0-9]的数字限定

<!-- 来源页 750 -->
替换模式介绍
该命令支持以下3种替换模式，用于指定匹配成功后的处理方式。
l 直接替换：指将匹配到的原始内容直接替换为新的目标值，适用于需要将指定配置项完整修改为新值的场景。
l 追加前缀替换：在匹配到的内容前面追加指定字符串，适用于需要为配置项统一添加分类标识或作用域前缀的场
景。
l 追加后缀替换：在匹配到的内容后面追加指定字符串，适用于需要为配置项统一添加版本号、环境标识或备注后
缀的场景。
replace-config命令配置
使用replace-config命令批量修改配置，在全局配置模式下，使用以下命令：
replace-config mode {exact | contain | regex} "pattern" {with | prefix | suffix} "replacement"
l
{exact | contain | regex} - 指定配置文本的匹配模式。exact表示精确匹配，contain表示包含匹配，
regex表示正则匹配。
l
"pattern" - 输入待匹配的字符串或表达式，且必须使用英文双引号（"）将其包裹。取值范围1-1023个
字符。
l
{with | prefix | suffix} - 指定配置文本的替换模式。with表示直接替换，prefix表示追加前缀替换，
suffix表示追加后缀替换。
l
"replacement" - 输入用于替换的目标字符串，且必须使用英文双引号（"）将其包裹。取值范围1-
1023个字符。
执行该命令后，系统将在CLI界面展示即将执行的配置变更，并提示用户确认是否执行替换操作。此时，用户
需按照以下步骤进行操作：

<!-- 来源页 751 -->
1.
预览配置差异：查看配置变更差异对比（参照上图中“-/+”标识），确认变更范围与预期一致。
2.
确认执行替换操作：在提示符“Replace configuration, are you sure? [y]/n:”后，输入“y”，执
行替换操作。
若无需替换配置，可在提示符后输入“n”或按“Enter”键，取消操作。
3.
选择是否备份配置文件：确认替换后，系统进一步提示是否备份当前配置文件。如需备份，可在提示符
后输入“y”；如无需备份，则可在提示符后输入“n”或按“Enter”键。
4.
执行下发：确认备份选项后，可根据CLI打印信息，依次按“Enter”键下发配置变更，直至系统返回执
行结果。
替换操作执行成功后，新配置将立即生效，无需重启设备。
提示: 有关匹配模式与替换模式的完整规则及使用约束，请参阅本章的“匹配模式介绍”及“替换
模式介绍”两节。

<!-- 来源页 752 -->
许可证
许可证（license）用来授权用户使用一些功能、服务，或者用来扩展性能。对于基于许可证的功能、服务
和性能来说，如果没有购买和安装相应的许可证，该功能和服务就无法使用，或不能达到更高的性能。对于
虚拟化产品-云·界的性能，由许可证的控制。只有购买并安装了相应的许可证，才能使产品达到其标称的数
值。购买许可证，请与销售人员联系。
许可证种类
许可证的种类和规则如下：
注意: 功能类和服务类试用许可证可以在申请该许可证时选择使用时长，最长不能超过90天。多个
试用许可证可以叠加使用时长。
平台许可证
说明
许可证过期
是否重启设备
支持平
台
平台试用许可
证（Platform
Trial）
平台许可证是其他许可证运行的基础，如果平台许可证
无效，其他许可证均不生效。设备出厂时已预装15天的
试用许可证，支持功能同正式许可证。
过期后，已
有的配置不
能修改，若
设备重启，
原有的配置
保留但不能
修改。
不需要重启。
A、
K、
X、
B、
SDW
平台正式许可
证
（Platform）
设备正式销售后，可以安装平台正式许可证。该许可证
提供基础防火墙功能和VPN功能。
过期后，设
备仍可正常
使用，但不
能升级到期
后的OS版
本。
不需要重启。
A、
K、
X、
B、
SDW
功能许可证
说明
许可证过期
是否重启设备
支持平
台
虚拟系统许可
证
授权VSYS的最大可用数量。
无过期。
每次安装都需要
重启。
A、
K、
X、B
SSL VPN许可证
授权SSL VPN的接入数量。多个SSL VPN许可证可以叠
加允许接入用户的数量。
无过期
除以下版本外，
其他版本在每
次安装后均需
重启。不需要
A、
K、
X、B

<!-- 来源页 753 -->
重启的版
本：5.5R6P21
及其以后P版
本、5.5R8P7 及
其以后P版本、
5.5R9及其以后
版本。
SSL VPN试用许
可证
授权SSL VPN的最大接入数量（平台允许的SSL VPN用
户最大接入数量），但是使用期限较短。
过期后，允
许接入设备
的SSL VPN
用户数恢复
为之前的数
量。
不需要重启。
A、
K、
X、B
ZTNA正式许可
证
授权ZTNA的最大接入数量。生效优先级高于试用许可
证。多个ZTNA许可证可以叠加允许接入用户的最大数
量。SCVPN授权数量不足时，可以借用ZTNA许可证，
ZTNA登录方式不能借用SCVPN许可证。
无过期
不需要重启。
A、
K、
X、
B、
SDW
ZTNA升级许可
证
转换指定个数的SSL VPN许可证为ZTNA许可证，不限
制SSL许可证类型。多个ZTNA升级许可证可叠加，转换
的总个数不超过SSL VPN授权数量。如果被转换的SSL
VPN许可证是非永久的，到期后，升级后的ZTNA授权
数量将清零。
无过期
不需要重启。
A、
K、
X、
B、
SDW
ZTNA试用许可
证
提供ZTNA试用。授权数量和可用时间可叠加。
过期后，只
能使用系统
默认提供的
8个ZTNA并
发用户授
权。
不需要重启。
A、
K、
X、
B、
SDW
QoS/iQoS许可
证
开启QoS功能。
无过期。
不需要重启。
A、
K、
X、
B、
SDW
QoS/iQoS试用
许可证
提供QoS功能试用。安装QoS试用许可证后，系统支持
的QoS功能与正式许可证相同，但是使用期限较短。
过期后，已
有的配置失
效，无法继
续使用QoS
功能。
不需要重启。
A、
K、
X、
B、
SDW
国家商用密码
IPSec VPN支持使用国家商用密码算法。对于支持该算
无过期。
-
K、X

<!-- 来源页 754 -->
IPSec VPN许可
证
法的设备，从StoneOS 5.5R6版本开始，系统不需安装
国家商用密码IPSec VPN许可证即可使用国密算法。
云沙箱防护许
可证
提供云沙箱防护功能，授权每天允许上传到云沙箱的可
疑文件样本数目，并且提供域名白名单的升级。分为以
下四种许可证：Cloud sandbox-200、Cloud
sandbox-300、Cloud sandbox-500和Cloud
sandbox-1000，不同许可证每天允许上传的文件数不
同。
有效期包括
1年、2年、
3年。过期
后，云端分
析功能无法
使用，不能
升级域名白
名单。仅可
根据本地数
据库缓存结
果使用沙箱
防护功能，
重启设备之
后，功能不
可用。
首次安装需要重
启设备，之后续
费不需要重启。
A、
K、
X、B
Twin-mode许
可证
开启孪生模式功能，控制系统孪生模式相关功能的可见
性和可配置性。
无过期。
不需要重启。
Twin-mode试
用许可证
开启孪生模式功能，控制系统孪生模式相关功能的可见
性和可配置性。安装Twin-mode试用许可证后，系统
支持的孪生模式相关功能与正式许可证相同，但是使用
期限较短。
过期后，无
法使用孪生
模式的功能
升级和维护
服务。
不需要重启。
国产数据库许
可证
开启国产数据库功能，可以切换使用国产数据库
PolarDB。
注意：仅K系列设备（K9180除外）支持国产数据库功
能。
无过期。
不需要重启。
K
扩展功能试用
许可证
打包提供SSL VPN、QoS以及VSYS功能试用。安装扩展
功能试用许可证后，系统支持的功能与单独的正式许可
证相同，但是使用期限较短。
注意: SDW系列不支持SSL VPN和QoS试
用，安装扩展功能试用许可证后，仅对
VSYS功能生效。
过期后，
SSL VPN、
QoS功能请
参考单独的
试用许可证
策
略；VSYS
功能无法配
置，重启
后，VSYS
的相关配置
资源将被删
除。
安装后，SSL
VPN、QoS功能
不需要重启设
备；VSYS功能
在首次安装时需
要重启设备才能
生效。
A、
K、
X、
B、
SDW

<!-- 来源页 755 -->
服务许可证
说明
许可证过期
是否重启设备
支持平
台
病毒过滤
（AV）许可证
提供病毒过滤功能，以及病毒特征库和病毒过滤智能文
件引擎库的升级。
型号说明：智能文件引擎检测功能及
病毒过滤智能文件引擎库仅支持如下
型号：
l
A系列：除SG-6000-
A2200/A1800/A1600/A1600-
A
/A200/A200W/A200G4
/A200WG4/A200-A/A200G4-
A/A200W-A/A200WG4-A之外
的其它设备。
l
B系列：除SG-6000-
B600/B600W/B600G4
/B600WG4之外的其它设备。
l
K系列：K系列所有设备。
l
X系列：SG-6000-
X20812/X20803/X9180-
GS/X8180。
l
云·界：部署在X86架构或者ARM
架构服务器上的云·界。
过期后，不
能升级病毒
特征库和病
毒过滤智能
文件引擎
库，病毒过
滤功能和智
能文件引擎
检测功能正
常使用。
未安装过正式或
试用许可证：首
次安装需要重启
设备。
已安装正式许可
证：后续安装试
用/正式许可证
不需要重启。
已安装试用许可
证：
l 若在生效时
间内安装试
用/正式许
可证，不需
要重启。
l 若在设备使
用过程中过
期，在设备
重启前安装
试用/正式
许可证，不
需要重启。
l 若在设备启
动后就是过
期状态，安
装试用/正
式许可证，
需要重启。
A、
K、
X、B
病毒过滤
（AV）试用许
可证
提供病毒过滤功能试用，以及病毒特征库和病毒过滤智
能文件引擎库的升级。
安装病毒过滤试用许可证后，系统支持的病毒过滤功能
与正式许可证相同，但是使用时间较短。可以在申请该
许可证时选择使用时间，最长不能超过90天。多个病毒
过滤试用许可证可以叠加使用时间。
过期后，无
法继续使用
病毒过滤功
能，不能升
级病毒特征
库和病毒过
滤智能文件
引擎库。
A、
K、
X、B
入侵防御
提供入侵防御功能和IPS特征库升级。
过期后，不
未安装过正式或
A、

<!-- 来源页 756 -->
（IPS）许可证
能升级IPS
特征库，入
侵防御功能
正常使用。
试用许可证：首
次安装需要重启
设备。
已安装正式许可
证：后续安装试
用/正式许可证
不需要重启。
已安装试用许可
证：
l 若在生效时
间内安装试
用/正式许
可证，不需
要重启。
l 若在设备使
用过程中过
期，在设备
重启前安装
试用/正式
许可证，不
需要重启。
l 若在设备启
动后就是过
期状态，安
装试用/正
式许可证，
需要重启。
K、
X、B
入侵防御
（IPS）试用许
可证
提供入侵防御功能试用和IPS特征库升级。
安装入侵防御试用许可证后，系统支持的入侵防御功能
与正式许可证相同，但是使用时间较短。
过期后，无
法继续使用
入侵防御功
能，不能升
级IPS特征
库。
A、
K、
X、B
URL DB 许可证
提供URL分类库和URL分类库的在线查询功能。
过期后，不
能提供URL
分类库的在
线查询功
能，自定义
URL和URL
过滤功能仍
正常使用。
首次安装需要重
启设备，之后续
费不需要重启。
A、
K、
X、
B、
SDW

<!-- 来源页 757 -->
URL DB 试用许
可证
提供URL分类库和URL分类库的在线查询功能试用。安
装URL DB 试用许可证后，系统支持的URL DB 相关功能
与正式许可证相同，但是使用期限较短。
过期后，不
能提供URL
分类库的在
线查询功
能，自定义
URL和URL
过滤功能仍
正常使用。
首次安装需要重
启设备，之后续
费不需要重启。
A、
K、
X、
B、
SDW
应用特征库许
可证
提供应用特征库升级功能。应用特征库许可证不需要单
独申请，随平台许可证一同发放，有效期也同平台许可
证。
过期后不能
升级APP特
征库。
不需要重启。
A、
K、
X、
B、
SDW
应用特征库试
用许可证
安装应用特征库试用许可证后，系统支持的应用特征库
相关功能与正式许可证相同，但是使用期限较短。
过期后不能
升级APP特
征库。
不需要重启。
A、
K、
X、
B、
SDW
威胁防护
（TP）许可证
打包提供AV、IPS及威胁情报功能，和相应特征库的升
级。
过期后，不
能提供其包
含的特征库
的升级，功
能仍可使
用。
是否重启，请参
考AV、IPS及威
胁情报单独许可
证的重启策略。
A、
K、
X、B
IP信誉库许可证
提供基于IP信誉库的边界流量过滤（PTF）功能和IP信誉
特征库升级。从StoneOS 5.5R6及以后版本，原先的预
定义黑名单边界流量过滤功能（由PTF许可证提供）不
再支持，而是升级为IP信誉库功能，用户可购买该IP信
誉库许可证进行升级。
过期后，IP
信誉特征库
无法升级，
基于IP信誉
库的边界流
量过滤功能
仍可继续使
用。
首次安装需要重
启设备，之后续
费不需要重启。
A、
K、
X、B
IP信誉库试用
许可证
提供基于IP信誉库的边界流量过滤（PTF）功能和IP信誉
特征库升级。系统支持的IP信誉库相关功能与正式许可
证相同，但是使用期限较短。
过期后，IP
信誉特征库
无法升级，
基于IP信誉
库的边界流
量过滤功能
仍可继续使
用。
首次安装需要重
启设备，之后续
费不需要重启。
A、
K、
X、B

<!-- 来源页 758 -->
僵尸网络防御
许可证
提供僵尸网络防御功能和僵尸网络防御特征库的升级。
过期后，不
能提供其包
含的特征库
的升级，功
能仍可使
用。
未安装过正式或
试用许可证：首
次安装需要重启
设备。
已安装正式许可
证：后续安装试
用/正式许可证
不需要重启。
已安装试用许可
证：
l 若在生效时
间内安装试
用/正式许
可证，不需
要重启。
l 若在设备使
用过程中过
期，在设备
重启前安装
试用/正式
许可证，不
需要重启。
l 若在设备启
动后就是过
期状态，安
装试用/正
式许可证，
需要重启。
A、
K、
X、B
僵尸网络防御
试用许可证
提供僵尸网络防御功能试用和僵尸网络防御特征库的升
级。
安装僵尸网络防御试用许可证后，系统支持的僵尸网络
防御功能与正式许可证相同，但是使用时间较短。
过期后，无
法继续使用
僵尸网络防
御功能，不
能升级僵尸
网络防御特
征库。
A、
K、
X、B
IoT管控许可证
提供IT和IoT设备的云端设备识别和本地设备识别功能，
以及IoT设备指纹库的升级。
无过期。
不需要重启。
A、
K、
X、B
IoT管控试用许
可证
提供IT和IoT设备的云端设备识别和本地设备识别功能试
用，以及IoT设备指纹库的升级。安装IoT管控试用许可
证后，系统支持的设备识别功能与正式许可证相同，但
是使用期限较短。
过期后，无
法使用设备
识别功能，
不需要重启。
A、
K、
X、B

<!-- 来源页 759 -->
不能升级
IoT设备指
纹库。系统
重启后，设
备识别功能
配置不丢
失，但是不
生效。
威胁情报许可
证
提供威胁情报功能。
过期后，无
法继续向云
平台上传数
据及从云平
台获取情
报。
不需要重启。
A、
K、
X、
B、
SDW
威胁情报试用
许可证
提供威胁情报功能试用。安装威胁情报试用许可证后，
系统支持的威胁情报功能与正式许可证相同，但是使用
期限较短。
过期后，无
法继续向云
平台上传数
据及从云平
台获取情
报。
不需要重启。
A、
K、
X、
B、
SDW
Bundle许可证
1（ BDL1）
打包提供IPS、AV、威胁情报、QoS以及URL DB功能，
和相应特征库的升级。
过期请参考
相应单独的
许可证策
略。
是否重启，请参
考IPS、AV、威
胁情报、QoS以
及URL DB单独
许可证的重启策
略。
A、
X、B
Bundle许可证
3（ BDL3）
打包提供IPS、AV、威胁情报、QoS、URL DB、僵尸网
络、IP信誉库以及云沙箱功能，和相应特征库的升级。
过期请参考
相应单独的
许可证策
略。
是否重启，请参
考IPS、AV、威
胁情报、QoS、
URL DB、僵尸
网络、IP信誉库
以及云沙箱单独
许可证的重启策
略。
A、B
扩展模块许可
证
说明
许可证过期
是否重启设备
板卡许可证
板卡许可证为X系列设备和部分K系列设备（K9180、
K20803）提供扩展模块的维保服务到期时间。
说明：维保服务是指基本系统软件升级及硬件保修服
务。
到期后不影
响正常使
用。
不需要重启。
K、X

<!-- 来源页 760 -->
许可证（云·界）
许可证机制
虚拟化防火墙的许可证分为平台类许可证、订阅类许可证和功能服务类许可证。平台许可证是功能服务类许
可证运行的基础。用户可通过SN号申请各类许可证（即旧版许可证）。若重新安装虚拟化防火墙，由于SN
号发生改变，需重新申请许可证。
从5.5R5版本开始，云·界许可证升级为最新版本许可证，许可证机制与之前略有不同。新版平台许可证安装
后，设备的SN号将进行变更，即变为虚拟SN（简称“vSN”）。若用户想继续获取功能服务类或订阅类许
可证，可通过该vSN号进行申请。云·界系统重新安装后，由于新版许可证不依赖于原系统的SN号，故原先
申请的新版许可证仍可继续使用。同时，Hillstone提供公网和局域网LMS许可证服务器，对新版许可证进
行校验及许可证的管理，保证许可证的安全。
注意: 如果您在公有云平台上购买的防火墙是内置许可证的版本，那么您无需额外购买许可证，也
无需安装许可证，即可获得以下许可证所代表的所有功能。
平台类许可证
云·界系统初始预装有一个免费的默认许可证（default license），无需申请。用户可通过SN号申请的平台
许可证（即旧版平台许可证）或直接申请新版许可证。旧版平台许可证分为平台正式许可证和平台试用许可
证。新版平台许可证分为平台正式许可证和平台订阅许可证。
l 默认许可证（Default）
虚拟化防火墙预装了一个免费的默认许可证（default license），无需申请。装有默认许可证的系统支持所有
的功能，例如平台功能、SSL VPN、iQoS和IPS等，但是性能受限，例如系统仅支持创建2条IPSec VPN 隧道，仅
支持2个SSL VPN用户等等。该许可证的有效期为30天。到期后，系统的所有功能将不能使用，且系统版本和所
有的特征库将不能升级。该许可证为出厂自带，不需要导入及重启设备。
l 平台试用许可证（Platform Trial）
安装平台试用许可证后，系统支持的功能和性能与正式许可证相同，但是使用期限较短。具体可用时长，根据申
请时协议决定，该可用时长指的是相对时间，例如一个月。到期后，已有的配置不能修改；重启后，原有的配置
保留，但不能修改，且仅平台的功能可用，但性能受限。安装许可证后不需要重启设备。
l 平台订阅许可证（Platform Sub ）
安装平台订阅许可证后，系统支持的功能和性能与正式许可证相同，但是使用期限较短。具体使用时间，根据申
请时协议决定，该使用时间指的是绝对时间，例如2017年3月1日到2017年3月31日。到期后，已有的配置不能

<!-- 来源页 761 -->
修改；重启后，原有的配置保留，但不能修改，且仅平台的功能可用，但性能受限。首次安装需要重启设备，之
后续费不需要重启。
l 平台正式许可证（Platform ）
产品正式销售后，可以安装平台正式许可证。正式许可证提供基础防火墙功能，并且防火墙性能可达到标称数
值。到期后，系统仍可正常使用，但不能升级到到期后的系统版本。首次安装需要重启设备，之后续费不需要重
启。
注意:
l
新版的平台许可证过期时，系统安装的订阅许可证和功能服务类许可证仍然有效，但不能升级
到到期后的系统版本。
l
如果卸载了新版的平台许可证，系统重启后，系统的vSN号将恢复为初始的设备SN号，通过原
先vSN号申请的订阅类和功能服务类许可证将无法使用。
订阅类许可证
订阅类许可证能够控制相关功能是否开启及其使用期限。
l SSL VPN订阅许可证
开启SSL VPN功能且授权SSL VPN的接入数量。多个SSL订阅许可证可以叠加允许接入用户的数量。过期后，
SSL VPN的所有连接将断开，SSL VPN将不可配置。系统重启前，SSL VPN的所有配置不会丢失。安装许可证后
不需要重启设备。
l ZTNA订阅许可证
开启ZTNA功能且授权ZTNA的最大接入数量，生效优先级低于ZTNA正式许可证，高于ZTNA试用许可证。多个
ZTNA订阅许可证可叠加，授权数量和使用时间可叠加，时间范围取最佳。过期后，只能使用系统默认提供的8个
ZTNA并发用户授权。
l ZTNA订阅许可证
开启ZTNA功能且授权ZTNA的最大接入数量，生效优先级低于ZTNA正式许可证，高于ZTNA试用许可证。多个
ZTNA订阅许可证可叠加，授权数量和使用时间可叠加，时间范围取最佳。过期后，只能使用系统默认提供的8个
ZTNA并发用户授权。
l IPSEC VPN 订阅许可证
开启IPSec VPN功能且授权IPSec VPN的最大接入数量。多个IPSEC VPN订阅许可证可以叠加允许接入用户的最

<!-- 来源页 762 -->
大数量。过期后，IPSec VPN的所有连接将断开，IPSec VPN将不可配置。系统重启前，IPSec VPN的所有配置
不会丢失。安装许可证后不需要重启设备。
l iQoS订阅许可证
开启iQoS功能。许可证过期后，系统重启前iQoS的所有配置不会丢失。安装许可证后不需要重启设备。
l 虚拟CPU正式许可证
授权CloudEdge虚拟防火墙可配置的vCPU的最大数量。无过期。规格变更后，需重启设备。不同型号的云·界所
要求的vCPU及内存不同，请注意申请对应数量的许可证，具体如下：
产品型号
最低配置
硬盘最低配置
SG-6000-VM01/VM01-KL
2个vCPU，4G内存
10G
SG-6000-VM02/VM02-KL
2个vCPU，8G内存
10G
SG-6000-VM04/VM04-KL
4个vCPU，8G内存
10G
SG-6000-VM08/VM08-KL
8个vCPU，16G内存
10G
l 虚拟CPU订阅许可证
授权CloudEdge虚拟防火墙可配置的vCPU的最大数量。过期后，系统将会重启，重启后将恢复到最低型号SG-
6000-VM01的配置，即2vCPU。规格变更后，需重启设备。
功能服务类许可证
只有购买并安装了各个功能服务类许可证，用户才能使用相应的功能，并能够获取特征库更新。
l ZTNA 许可证
提供ZTNA功能，包括：
a. ZTNA正式许可证：永久有效，优先级最高。多个ZTNA许可证可以叠加允许接入用户的最大数量。SCVPN授
权数量不足时，可以借用ZTNA许可证，ZTNA登录方式不能借用SCVPN许可证。
b. ZTNA试用许可证：提供ZTNA试用。授权数量和可用时间可叠加。到期后，只能使用系统默认提供的8个
ZTNA并发用户授权。
c. ZTNA升级许可证：转换指定个数的SSL VPN许可证为ZTNA许可证，不限制SSL VPN许可证的类
型。ZTNA升级许可证可叠加，转换的总个数不超过SSL VPN授权数量。如果被转换的SSL VPN许可
证是非永久的，到期后，升级后的ZTNA授权数量将清零。
l 入侵防御（IPS）许可证
提供入侵防御功能和IPS特征库升级。具有单独的使用期限。过期后，不能升级IPS特征库，入侵防御功能正常使
用。

<!-- 来源页 763 -->
未安装过试用/正式许可证，首次安装需要重启设备。已安装正式许可证，之后续费安装试用/正式许可证不需要
重启。
l 入侵防御（IPS）试用许可证
提供入侵防御功能试用和IPS特征库升级。具有单独的使用期限，可以在申请该许可证时选择使用期限，最长不
能超过90天。多个入侵防御试用许可证可以叠加使用期限。过期后，无法继续使用入侵防御功能，不能升级IPS
特征库。
未安装过试用/正式许可证，首次安装需要重启设备。已安装试用许可证，若在生效时间内续费安装试用/正式许
可证，不需要重启；若在设备使用过程中过期，在设备重启前安装试用/正式许可证，不需要重启；若在设备启
动后就是过期状态，需要重启设备。
l 病毒过滤（AV）许可证
提供病毒过滤功能，以及病毒特征库和病毒过滤智能文件引擎库的升级。具有单独的使用期限。过期后，不能升
级病毒特征库和病毒过滤智能文件引擎库，病毒过滤功能和智能文件引擎检测功能正常使用。
未安装过试用/正式许可证，首次安装需要重启设备。已安装正式许可证，之后续费安装试用/正式许可证不需要
重启。
说明：仅部署在X86架构或者ARM架构服务器上的云·界支持病毒过滤智能文件引擎库。
l 病毒过滤（AV）试用许可证
提供病毒过滤功能试用，以及病毒特征库和病毒过滤智能文件引擎库的升级。具有单独的使用期限，可以在申请
该许可证时选择使用期限，最长不能超过90天。多个病毒过滤试用许可证可以叠加使用期限。过期后，无法继续
使用病毒过滤功能，不能升级病毒特征库和病毒过滤智能文件引擎库。
未安装过试用/正式许可证，首次安装需要重启设备。已安装试用许可证，若在生效时间内续费安装试用/正式许
可证，不需要重启；若在设备使用过程中过期，在设备重启前安装试用/正式许可证，不需要重启；若在设备启
动后就是过期状态，需要重启设备。
l 僵尸网络防御许可证
提供僵尸网络防御功能和僵尸网络防御特征库的升级。具有单独的使用期限过期后，不能升级僵尸网络防御特征
库，僵尸网络防御功能正常使用。
未安装过试用/正式许可证，首次安装需要重启设备。已安装正式许可证，之后续费安装试用/正式许可证不需要
重启。
l 僵尸网络防御试用许可证
提供僵尸网络防御功能试用和僵尸网络防御特征库的升级。具有单独的使用期限，可以在申请该许可证时选择使
用期限，最长不能超过90天。多个僵尸网络防御试用许可证可以叠加使用期限。过期后，无法继续使用僵尸网络

<!-- 来源页 764 -->
防御功能，不能升级僵尸网络防御特征库。
未安装过试用/正式许可证，首次安装需要重启设备。已安装试用许可证，若在生效时间内续费安装试用/正式许
可证，不需要重启；若在设备使用过程中过期，在设备重启前安装试用/正式许可证，不需要重启；若在设备启
动后就是过期状态，需要重启设备。
l 云沙箱（Sandbox）许可证
提供沙箱防护功能，授权每天允许上传到云沙箱的可疑文件样本数目，并提供域名白名单升级。具有单独的使用
期限。过期后，云端分析功能失效，且域名白名单无法升级，但是如果仍有可疑流量符合本地缓存中的分析条
目，则沙箱功能仍然可用，系统重启后，沙箱防护功能将不能使用。首次安装需要重启设备，之后续费不需要重
启。
l URL DB 许可证
提供URL 过滤功能和URL库升级功能。具有单独的使用期限。过期后，不能升级URL库，URL 过滤功能正常使
用。首次安装需要重启设备，之后续费不需要重启。
l URL DB 试用许可证
提供URL 过滤功能和URL库升级功能。具有单独的使用期限，可以在申请该许可证时选择使用期限，最长不能超
过90天。过期后，不能升级URL库，URL 过滤功能正常使用。首次安装需要重启设备，之后续费不需要重启。
l 应用特征库许可证
提供应用特征库升级功能。应用特征库许可证不需要单独申请，随平台许可证一同发放，有效期也同平台类许可
证。过期后，不能升级APP特征库。
l 应用特征库试用许可证
提供应用特征库升级功能。具有单独的使用期限，可以在申请该许可证时选择使用期限，最长不能超过90天。应
用特征库许可证不需要单独申请，随平台许可证一同发放，具有单独的使用期限。过期后，不能升级APP特征
库。
l 威胁情报许可证
提供威胁情报功能。到期后，无法继续向云平台上传数据及从云平台获取情报。
l 威胁情报试用许可证
提供威胁情报功能。具有单独的使用期限，可以在申请该许可证时选择使用期限，最长不能超过90天。到期后，
无法继续向云平台上传数据及从云平台获取情报。
l IP信誉库许可证
提供基于IP信誉库的边界流量过滤（PTF）功能和IP信誉特征库升级。从StoneOS 5.5R6及以后版本，原先的预
定义黑名单边界流量过滤功能（由PTF许可证提供）不再支持，而是升级为IP信誉库功能，用户可购买该IP信誉

<!-- 来源页 765 -->
库许可证进行升级。到期后，IP信誉特征库无法升级，基于IP信誉库的边界流量过滤功能仍可继续使用。首次安
装需要重启设备，之后续费不需要重启。
l IP信誉库试用许可证
提供基于IP信誉库的边界流量过滤（PTF）功能和IP信誉特征库升级，功能与正式许可证相同。具有单独的使用
期限，可以在申请该许可证时选择使用期限，最长不能超过90天。到期后，IP信誉特征库无法升级，基于IP信誉
库的边界流量过滤功能仍可继续使用。首次安装需要重启设备，之后续费不需要重启。
l SR-IOV吞吐控制正式/试用许可证
提供对云·界上SR-IOV类型网卡的吞吐量进行提升。初始未安装该许可证时，SR-IOV卡将以默认的吞吐量运行，
安装后，吞吐量可进行提升。正式许可证一经安装，永久有效；试用许可证过期后，网卡吞吐量将恢复为默认
值。不同的平台型号的SR-IOV网卡默认吞吐量不同，安装许可证后提升的幅度也不同，具体如下：
平台型号
VM01
VM02
VM04
VM08
网卡默认吞吐量
2Gbps
4Gbps
8Gbps
16Gbps
安装许可证后吞吐量
10Gbps
20Gbps
40Gbps
80Gbps
注意:
l
除了上面列出的许可证外，硬件防火墙所支持的其他许可证，包括提供高级威胁防护和异常行
为分析的StoneShield许可证，云·界暂不支持。
许可证管理
申请许可证
请遵循以下流程申请许可证：
生成申请许可证所需的许可证请求，将生成的请求发送给Hillstone代理商，由其获取许可证再返回。
在任何模式下使用以下命令生成许可证请求：
exec license apply applicant string
l
string – 申请人名称。
安装许可证
云·界非国产系列平台支持安装V2和对应型号的V3版本许可证。云·界国产系列平台仅支持安装对应型号的
V3版本许可证。
若为云·界安装非对应型号的V3版本许可证，用户需要根据实际情况，执行对应操作。

<!-- 来源页 766 -->
l
在低规格的云·界平台上安装高规格的云·界平台型号的V3版本许可证，系统可正常使用。
l
在高规格的云·界平台上安装低规格的云·界平台型号的V3版本许可证，用户无法在WebUI页面和CLI的
全局配置模式下进行配置操作。用户需要使用exec license uninstall license-name命令，卸载对应
低规格型号的许可证，然后再重新安装对应型号的V3版本许可证。
注意: 云·界非国产系列平台和国产系列平台许可证不能互相安装。
许可证为一串字符串。获得许可证后，用户需要将许可证安装到相应的设备。
获得许可证后，用户可在任何模式下通过使用以下命令安装许可证：
exec license install license-string
l
license-string – 要安装的许可证字符串。
安装部分许可证后，需要输入命令reboot使系统重启。
提示: 以下许可证将在重启后生效，其他许可证直接生效。
l
首次安装以下许可证后，需要重启系统：平台订阅许可证（Platform sub）、平台正式许可证
（Platform）、病毒过滤（AV）许可证、病毒过滤（AV）试用许可证、入侵防御（IPS）许
可证、入侵防御（IPS）试用许可证、、僵尸网络防御许可证、僵尸网络防御试用许可证、
StoneShield许可证、URL DB许可证、沙箱防护许可证、虚拟CPU正式许可证、链路负载均
衡许可证（LLB）、IP信誉库许可证。
l
每次安装以下许可证后，需要重启系统：AEL 许可证、虚拟系统许可证。
卸载许可证
卸载许可证，在任何模式下使用以下命令：
exec license uninstall [slot slot-id] license-name
l
slot slot-id – 指定要卸载的扩展模块许可证所在的槽位号。仅X系列设备和部分K系列设备
（K20803、K9180）支持该参数。
l
license-name – 指定要卸载的许可证名称。
注意: StoneOS允许用户卸载已安装的许可证。但是强烈建议用户不要对许可证进行卸载。

<!-- 来源页 767 -->
查看许可证信息
查看系统中已安装的许可证信息，包括许可证版本、客户名称、许可证类型、许可证到期时间等，在任意模
式下，输入以下命令：
show license [slot slot-id] license-name
l
slot slot-id – 指定要查看的扩展模块许可证所在的槽位号。仅X系列设备和部分K系列设备（K20803、
K9180）支持该参数。
l
license-name – 指定要查看的许可证名称。
查看许可证汇总信息
在任何模式下，输入以下命令，查看系统中所有许可证的汇总信息，包括所有受许可证控制的功能名称、许
可证状态、许可证类型、过期时间及可用资源数：
show license summary
例如：
hostname# show license summary
===============================================
Feature State Type Expiration Resource
----------------------------------------------------------------------------------------------
URL DB Authorized Service license 2020/03/05(Upgrade effective time expired) 1
APP signature Authorized Service license 2020/03/05(Upgrade effective time expired)
NULL
IPS Authorized Service license 2020/03/05(Upgrade effective time expired) 1
AntiVirus Authorized Service license 2020/03/05(Upgrade effective time expired) NULL
VSYS Authorized Permanent license Permanent 5
Cloud sandbox Authorized Service license 2020/03/05(Upgrade effective time expired) 1
Platform Authorized Service license 2030/10/02(Upgrade effective time) NULL
QoS Expired Trial license 0 days left NULL
Host route No License NULL NULL NULL
SCVPN No License NULL NULL NULL
IP Reputation No License NULL NULL NULL

<!-- 来源页 768 -->
Twin mode No License NULL NULL NULL
Botnet C&C Prevention No License NULL NULL NULL
Threat intelligence No License NULL NULL NULL
===============================================
以上命令显示结果中参数解释如下：
l
Feature：显示系统中受许可证控制的所有功能名称。
l
State：显示许可证的安装或者生效状态，包括已过期（Expired）、已授权（Authorized）、待生
效（To be effective）及未安装许可证（No License）。
l
Type ：显示许可证的种类，包括永久许可证（Permanent license）、服务许可证（Service
license）、订阅许可证（Subscribe license）及试用许可证（Trial license）。
l
Expiration ：显示许可证过期时间，不同类型许可证过期时间显示不同：
l
永久许可证（Permanent license）：“Permanent”表示无过期时间。
l
服务许可证（Service license）：“Upgrade effective time expired”表示功能可用，但是
特征库升级有效期已过，无法升级特征库；“Upgrade effective time”表示在特征库升级有效
期内。
l
订阅许可证（Subscribe license）：“2021/08/30 to 2021/09/28 (29 days left)”表示在
时间区间内还可以使用29天，如果打点时间为0，则表示已过期，对应状态为Expired。
l
试用许可证（Trial license）：“2 days left”表示还可以使用2天；“0 days left”则表示已
过期。
l
Resource：显示该功能可用资源数量，如SCVPN的用户数量或者IPSec VPN的隧道数量等。
许可证生效机制优先级为：永久许可证> 服务许可证> 订阅许可证> 试用许可证> 默认许可证。例如：设
备同时安装了150个隧道数量的IPSec VPN订阅许可证和30个隧道数量的IPSec VPN永久许可证，则永久许
可证生效，隧道资源数量为30个。如果卸载永久许可证，则订阅许可证生效，隧道资源数量为150个。
校验许可证
若虚拟化防火墙云·界产品安装VSN许可证，则需要连接到LMS（许可证管理系统），进行合法性校验，以防
止许可证被克隆盗版。若虚拟化防火墙云·界产品安装SN许可证，则无需进行合法性校验。
目前系统支持两种校验方式，分别是通过互联网连接到公网LMS进行校验和通过局域网连接到内网LMS进行
校验，用户可根据需要选择其中的一种方式。

<!-- 来源页 769 -->
l
互联网：适用于小型私有云或公有云场景。云·界连接到公网LMS后，公网LMS服务器将提供许可证的合
法性校验（目前公网LMS暂不提供许可证的分发和管理）。若发现克隆许可证的行为，克隆设备（安装
许可证较晚的设备）将会立即被重启。
l
局域网：适用于大型私有云或行业云场景。云·界连接到内网LMS后，内网LMS不仅能提供许可证的校
验，还可提供许可证的自动分发和管理。若发现克隆许可证的行为，克隆设备（安装许可证较晚的设
备）上的许可证将会被卸载，同时设备也将立即被重启。
在任何模式下使用以下命令：
exec lms enable { public | private ip {A.B.C.D| X:X:X:X::X} port port-number} vrouter vroutername
l
public – 指定云•界通过公网LMS进行许可证校验。
l
private ip {A.B.C.D | X:X:X:X::X} – 指定云•界通过内网LMS进行许可证校验，并指定内网LMS的IP地
址，可以是IPv4地址或者IPv6地址。注意：若实际部署为通过代理服务器连接到License服务器，此处
需指定为代理服务器的地址和端口。
l
port port-number – 指定连接内网LMS的端口号，取值范围为1到65535，默认为8001。
l
vrouter vrouter-name – 指定VRouter的名称。
许可证将在设备重启后生效，若此前未重启过，连接LMS成功后，可输入命令reboot重启设备。
断开与LMS的连接，在任何模式下使用以下命令：
exec lms disable
注意:
l
安装5.5R7及以上版本的云·界连接的LMS 的版本必须是3.0及以上。
l
若用户环境中的云·界所安装的软件版本既有5.5R7又有之前的旧版本时，当LMS发现许可证克
隆行为时，安装有5.5R7以前旧版本的云·界上的许可证将被判定为克隆设备。
l
建议先升级LMS至3.0及以上版本，然后再将云·界升级到5.5R7及其以后版本，再连接到
LMS。
l
通过公网LMS进行许可证验证时，请保证连接公网LMS的接口在trust-vr安全域内并且通过
trust-vr安全域可以访问互联网。
l
关于LMS（许可证管理系统）的更多资料，请访问文档中心参阅《许可证管理系统(LMS)使用
手册》。

<!-- 来源页 770 -->
配置HA备设备通过主设备与LMS进行通信
该功能仅虚拟化产品-云·界支持。在虚拟化环境中，当云·界以HA的方式进行部署时，若没有足够公网IP提
供给备设备来连接公网LMS时，可以配置通过主设备连接公网LMS进行通信，进而完成许可证的校验。此
时，主设备将作为备设备的代理，备设备与公网LMS的认证请求，将通过主备之间的HA链路转发给主设备，
最终由主设备发送到公网LMS服务器上。该功能默认情况下为关闭状态。开启通过主设备连接LMS，在主设
备的全局配置模式下，使用以下命令：
lms master-auth-proxy { enable | disable }
l
enable - 开启通过主设备连接LMS。开启后，主设备将作为备设备的代理，备设备与公网LMS的认证请
求，将通过HA链路转发给主设备，最终通过主设备发送到公网LMS服务器上。
l
disable - 关闭通过主设备连接LMS的功能。当备设备本身能够与LMS连接时，可关闭该功能。
更换云·界与LMS连接使用的数字证书
云·界与LMS进行连接时支持使用数字证书进行认证（认证连接使用双向认证，分发连接使用单向认证），认
证通过后，云·界和LMS成功连接。在云·界中创建信任域存储CA证书、本地证书和私钥，以供云·界与LMS
连接时进行认证使用。导入新的CA证书、本地证书以及私钥后，用户可以更换数字证书。创建信任域、配置
证书和私钥，请参阅PKI配置章节。
LMS引用已配置的信任域来获取新证书，在全局配置模式下，使用以下命令：
lms trust-domain trust-domain-name
l
trust-domain-name– 指定系统中已配置的存储了新证书和私钥的信任域名称。若不配置该项，则使
用默认的内置证书。
显示云·界与LMS的连接信息
在任意模式下，使用以下命令查看云·界与LMS的连接信息：
show lms
例如：
hostname(config)# show lms
==================================================================
Server IP: 10.182.21.12( 显示LMS服务器IP地址)
Server Port: 8001( 显示LMS服务器端口)
VR: trust-vr( 显示LMS服务器所属的虚拟服务器)
Master Auth Proxy status: Disable( 显示备设备是否通过主设备连接LMS)
Trust-domain:( 显示云·界配置的PKI信任域)

<!-- 来源页 771 -->
Lock Time: Locked( 显示云·界与LMS是否失联)
Authentication Connection Status: Disconnected and waiting for
reconnection(The network is unreachable)( 显示云·界与LMS的认证连接状态)
Distribution Connection Status: Disconnected and waiting for reconnection
(The network is unreachable)( 显示云·界与LMS的分发连接状态)
==================================================================
注意: Lock Time有四种状态：
l
当云·界与LMS正常连接时，Lock Time显示为Do not lock。
l
当云·界与LMS失联在30天内，Lock Time显示为After time hours。time为剩余小时数，剩
余小时数为0 时会锁定配置。
l
当云·界与LMS失联超过30天，Lock Time显示为Locked，用户无法配置在WebUI页面进行配
置操作，并且无法进入命令行的全局配置模式进行操作。请检查系统配置和网络，重连LMS成
功后才能取消配置锁定。
l
当云·界与LMS失联超过30天，对设备进行重启。重启后，Lock Time显示为Temporary
unlocking，用户可以在8小时内对设备进行操作，8小时后如果连接未恢复，仍会锁定配置。
许可证灌装
许可证灌装方法适用于需要给大批设备安装许可证的情况。使用许可证灌装可以简化大批量设备安装许可证
的操作步骤，减少错误的发生。
许可证灌装操作
许可证灌装操作步骤如下：
1. 拥有大批量设备的用户提供设备序列号以及需要的许可证类型。具体许可证信息请咨询当地代理商。
2. Hillstone山石网科获得许可证信息后，生成相应的许可证文件，并将许可证文件通过适当的方式发送给客户，例
如通过邮件。
3. 用户获得许可证文件后，将许可证文件拷贝到格式为FAT32的U盘中，拷贝路径为“\license”。目录名称
“license”区分大小写（必须为全部小写）且不可更改。拷贝许可证文件时不可修改许可证书写格式，否则将
无法安装许可证。
4. 用户利用存有许可证文件的U盘为所有设备安装许可证。具体安装步骤请参考下节内容。

<!-- 来源页 772 -->
利用U盘安装
用户将许可证文件拷贝到U盘的正确位置后，将U盘插入设备的USB口，设备将自动扫描U盘并安装许可证。
用户可以根据指示灯状态判断许可证安装状态。具体步骤如下：
1. 启动设备，进入运行状态（出现“login”提示符）。
2. 将存有许可证文件的U盘插入设备的USB口。
3. 设备扫描U盘信息，寻找与其序列号相同的许可证，找到后自动安装相应的许可证。通过设备的ALM指示
灯可判断许可证安装状态，指示灯闪烁方式以及含义如下表所示：
设备说明
ALM指示灯状态
设备从U盘的“license”目录下中发现匹配的许可证
绿色闪烁持续到许可证安装完成
许可证安装完成
恢复之前状态
设备未从U盘的“license”目录下中发现匹配的许可证
红色闪烁保持10秒后恢复之前状态
设备未从U盘中找到“license”目录
保证原状态不变
4. 许可证安装完毕取出U盘，然后用同样的方法为其他设备安装许可证。
5. U盘中所有和设备相匹配的许可证都会被自动安装到设备上，同时已经安装的许可证将被自动移动到U盘
的“license_installed”目录（自动创建）下，避免重新插入U盘后再次扫描并安装重复的许可证。
6. 重启设备，使许可证生效。

<!-- 来源页 773 -->
StoneOS版本升级
用户在使用设备的过程中，有时需要升级设备的系统固件StoneOS的版本。本节介绍设备的启动系统以及
StoneOS的升级方法。本节包含：
l "通过命令行升级StoneOS" 在第771页
l "通过Sysloader升级StoneOS" 在第775页
l "热补丁升级" 在第784页
通过命令行升级StoneOS
用户可以在CLI中通过FTP服务器、TFTP服务器、FTPS服务器、SFTP服务器或者U盘升级StoneOS。
通过FTP服务器升级StoneOS
1.
登录进入CLI后，在执行模式下，使用以下命令通过FTP服务器导入需要升级的版本文件：
import image from ftp server ip-address [user user-name password password ] [vrouter
vrouter-name] file-name
l
ip-address – 指定FTP服务器的IP地址。
l
user user-name password password– 指定FTP服务器的用户名和密码。
l
vrouter-name - 指定用于访问FTP服务器的设备接口对应的Vrouter。
l
file-name – 指定待升级的版本文件名称。如果该版本文件在FTP服务器的根目录下，则直接输入
版本文件名称；如果该版本文件在FTP服务器的多级目录下，需要填写为“多级目录+版本文件名
称”。例如：SG6000-ADNV-MX_MAIN-r0422.img在FTP服务器的test/5.5R11路径下，则
file-name填写为test/5.5R11/SG6000-ADNV-MX_MAIN-r0422.img。
2.
导入版本文件后，按照如下操作提示保存待升级的版本文件：
Save this image? [y]/n: y ( 选择y保存当前待升级的版本文件，选择n会退出升
级)
2 image can be saved, please remove ( 设备的Flash中最多可以储存两个版
本文件。如果Flash中已经保存了两个版本文件，请根据提示对储存的版本文件进行删
除。)
1: SG6000-ADNV-MX_MAIN-r0305(Active) ( 删除系统当前版本文件)

<!-- 来源页 774 -->
2: SG6000-ADNV-MX_MAIN-V6-t0301(Backup) ( 删除当前已备份的版本文件)
3: remove all ( 删除除待升级版本之外的所有版本文件)
4: cancel ( 不做删除操作，选择4会退出升级)
Which one do you select: 2
Are you sure? [y]/n: y
Remove SG6000-ADNV-MX_MAIN-V6-t0301...
Saving ...
Set SG6000-ADNV-MX_MAIN-r0422 as active boot image
3.
在执行模式下，输入reboot命令重启系统使新的StoneOS生效。按照如下提示进行操作：
System configuration has been modified. Save? [y]/n: y( 系统中有配置
变更，选择y将系统当前配置保存至startup文件中)
Building configuration.
Saving configuration is finished
System reboot, are you sure? y/[n]: y
2 configuration in system, please choose one to be loaded.
==================================================================
====
Name Version Save Time Size (bytes)
------------------------------------------------------------------
----
[a]: Startup 5.5R11 2024-04-23 18:50:18 33099
[b]: Backup 0 5.5R11 2024-04-23 18:50:18 33099
==================================================================
====
Press enter to use system current setting
Please choose one: a
4.
升级过程中需要等待一段时间，期间请勿执行任何操作。升级完成后，登录进入CLI，输入show
version命令验证系统是否已经成功升级到新版本。

<!-- 来源页 775 -->
通过TFTP服务器升级StoneOS
1.
登录进入CLI后，在执行模式下，使用以下命令通过TFTP服务器升级StoneOS：
import image from tftp server ip-address [vrouter vrouter-name] file-name
l
ip-address – 指定TFTP服务器的IP地址。
l
vrouter-name - 指定用于访问TFTP服务器的设备接口对应的Vrouter。
l
file-name – 指定待升级的版本文件名称。如果该版本文件在TFTP服务器的根目录下，则直接输
入版本文件名称；如果该版本文件在TFTP服务器的多级目录下，需要输入“多级目录+版本文件名
称”。例如：SG6000-ADNV-MX_MAIN-r0401.img在TFTP服务器的test/5.5R11路径下，则
file-name填写为test/5.5R11/SG6000-ADNV-MX_MAIN-r0401.img。
2.
导入待升级的版本文件后，根据CLI界面中的提示保存待升级的版本文件，以及按需删除之前的版本文
件。可参考通过FTP服务器升级STONEOS的步骤2进行操作。
3.
在执行模式下，输入reboot命令重启系统使新的StoneOS生效。可参考通过FTP服务器升级STONEOS
的步骤3进行操作。
4.
升级过程中需要等待一段时间，期间请勿执行任何操作。升级完成后，登录进入CLI，输入show
version命令验证系统是否已经成功升级到新版本。
通过FTPS服务器升级StoneOS
1.
登录进入CLI后，在执行模式下，使用以下命令通过FTPS服务器升级StoneOS：
import image from ftps server ip-address [user user-name password password ] [vrouter
vrouter-name] file-name
l
ip-address – 指定FTPS服务器的IP地址。
l
user user-name password password– 指定FTPS服务器的用户名和密码。
l
vrouter-name - 指定用于访问FTPS服务器的设备接口对应的Vrouter。
l
file-name – 指定待升级的版本文件名称。如果该版本文件在FTPS服务器的根目录下，则直接输
入版本文件名称；如果该版本文件在FTPS服务器的多级路目录下，需要填写为“多级目录+版本文
件名称”。例如：SG6000-ADNV-MX_MAIN-r0401.img在FTPS服务器的test/5.5R11路径
下，则file-name填写为test/5.5R11/SG6000-ADNV-MX_MAIN-r0401.img。
2.
导入待升级的版本文件后，根据CLI界面中的提示保存待升级的版本文件，以及按需删除之前的版本文
件。可参考通过FTP服务器升级STONEOS的步骤2进行操作。

<!-- 来源页 776 -->
3.
在执行模式下，输入reboot命令重启系统使新的StoneOS生效。可参考通过FTP服务器升级STONEOS
的步骤3进行操作。
4.
升级过程中需要等待一段时间，期间请勿执行任何操作。升级完成后，登录进入CLI，输入show
version命令验证系统是否已经成功升级到新版本。
通过SFTP服务器升级StoneOS
1.
登录进入CLI后，在执行模式下，使用以下命令通过FTPS服务器升级StoneOS：
import image from sftp server ip-address [user user-name password password ]
[vrouter vrouter-name] file-name
l
ip-address – 指定SFTP服务器的IP地址。
l
user user-name password password– 指定SFTP服务器的用户名和密码。
l
vrouter-name - 指定用于访问SFTP服务器的设备接口对应的Vrouter。
l
file-name – 指定待升级的版本文件名称。如果该版本文件在SFTP服务器的根目录下，则直接输
入版本文件名称；如果该版本文件在SFTP服务器的多级目录下，需要填写为“多级目录+版本文件
名称”。例如：SG6000-ADNV-MX_MAIN-r0401.img在SFTP服务器的test/5.5R11路径下，
则file-name填写为test/5.5R11/SG6000-ADNV-MX_MAIN-r0401.img。
2.
导入待升级的版本文件后，根据CLI界面中的提示保存待升级的版本文件，以及按需删除之前的版本文
件。可参考通过FTP服务器升级STONEOS的步骤2进行操作。
3.
在执行模式下，输入reboot命令重启系统使新的StoneOS生效。可参考通过FTP服务器升级STONEOS
的步骤3进行操作。
4.
升级过程中需要等待一段时间，期间请勿执行任何操作。升级完成后，登录进入CLI，输入show
version命令验证系统是否已经成功升级到新版本。
通过U盘升级StoneOS
注意: 通过U盘升级StoneOS时，需要将待升级的版本文件保存在U盘的根目录下。
1.
将待升级的版本文件拷贝到U盘的根目录下。
2.
将U盘插入设备的USB接口中。
3.
登录进入CLI后，在执行模式下，使用以下命令通过U盘升级StoneOS：
import image from {usb0 | usb1} file-name

<!-- 来源页 777 -->
l
usb0 | usb1 – 指定用于升级的设备USB接口。
l
file-name– 指定待升级的版本文件名称。例如：SG6000-ADNV-MX_MAIN-r0401.img。
4.
导入待升级的版本文件后，根据CLI界面中的提示保存待升级的版本文件，以及按需删除之前的版本文
件。可参考通过FTP服务器升级STONEOS的步骤2进行操作。
5.
在执行模式下，输入reboot命令重启系统使新的StoneOS生效。可参考通过FTP服务器升级STONEOS
的步骤3进行操作。
6.
升级过程中需要等待一段时间，期间请勿执行任何操作。升级完成后，登录进入CLI，输入show
version命令验证系统是否已经成功升级到新版本。
7.
升级完成后请及时拔出U盘。
通过Sysloader升级StoneOS
当设备发生故障，导致无法进入StoneOS系统时，用户可以在Sysloader中通过FTP服务器、TFTP服务器或
者U盘升级StoneOS。
启动系统介绍
山石网科防火墙设备的启动系统分为三个部分，分别是Bootloader、Sysloader和StoneOS。部分设备的
启动系统只包含Sysloader和StoneOS。它们各自的作用如下：
l Bootloader – 设备上电后最先运行的程序。Bootloader装载执行StoneOS或者Sysloader。
l Sysloader - 升级StoneOS。
l StoneOS – 设备的操作系统软件。
用户在设备启动时根据提示按下“ESC”键后，Bootloader尝试启动Sysloader。StoneOS是设备的操作
系统软件。Sysloader实现StoneOS的更新和选择，支持FTP、TFTP以及直接通过USB Host接口升级。
设备启动时，部分设备需要键入“Ctrl+W”然后进入Sysloader，进入Sysloader时可能需要输入密码或用
户名+密码。请以实际设备为准。如果需要用户名、密码，请咨询400-693-0555获取。
注意: 仅A200、A200W、A200G4、A200WG4、A1600、A1800、A2200、X8180和SDW系列
设备需要通过Bootloader进入Sysloader。
对设备物理连接的要求
通过Sysloader升级StoneOS时，PC需要通过Console口直连防火墙，也可以通过串口服务器连接防火
墙。

<!-- 来源页 778 -->
PC通过Console口直连防火墙
升级人员在机房环境中，可以将防火墙的Console口通过RS-232电缆直接连接PC，从而进行升级操作。
PC通过串口服务器连接防火墙
如果机房中设有串口服务器，且串口服务器的串口已通过RS-232电缆与防火墙的Console口连接，则升级
人员可以不在机房现场，通过远程访问串口服务器来连接防火墙，从而进行升级操作。
在用户PC上运行终端仿真程序，通过串口服务器连接防火墙，输入如下命令：
telnet ip-address port
l ip-address – 指定串口服务器的IP地址。
l port – 指定串口服务器连接防火墙的服务器端口号。
升级操作
在Sysloader中可以通过FTP服务器、TFTP服务器、FTPS服务器、SFTP服务器或者U盘升级StoneOS。
注意: 通过Sysloader升级StoneOS前，请先完成以下操作：
1.
防火墙的Console口（CON口）已通过标准的RS-232电缆与PC的串口连接。如果防火墙已连
接串口服务器，用户PC可以通过远程访问串口服务器来连接防火墙。
2.
请提前获取防火墙Console口的波特率。在PC上运行终端仿真程序与防火墙建立连接时，需保
证终端仿真程序上的波特率与设备的波特率一致。使用show console命令查看设备Console
口的波特率。如果设备未修改波特率，可参阅《硬件参考指南》获取设备的默认波特率。
3.
使用设备的MGT口连接FTP/TFTP服务器。设备如无MGT口，请使用eth0/0接口。
4.
以上操作完成后，重启设备，然后进入设备的启动系统。
在Sysloader中通过TFTP服务器升级StoneOS
Sysloader可以从TFTP服务器获取待升级的版本文件，从而保证用户能够通过网络迅速升级StoneOS。请
按照以下步骤进行操作：
1. 设备的CON口通过RS-232电缆与PC的串口连接好后，重启设备，重启过程中进入Sysloader（如果通过上下箭
头无法选择Sysloader，请先键入“Ctrl+W”然后进入Sysloader。例如SG-6000-K6580设备需要键入
“Ctrl+W”然后进入Sysloader）。不同设备回显信息可能存在差异，请以设备实际显示内容为准。
例如，SG-6000-X20803请参照以下操作提示：
GNU GRUB version 2.02

<!-- 来源页 779 -->
SG6000-XN-5.5R12F2B5-v6
SG6000-XN-5.5R12F2B8-v6
*SYSLOADER( 通过上下箭头选中Sysloader并按回车键，进入Sysloader)
Loading Sysloader
[  7.253642]
[  7.255125] Arbitrating
[  7.373235] -> Master
Sysloader 2.0.4 Jul 19 2023 - 11:40:32
Enter the password to stop autoboot: 3( 请在倒计时5秒内输入登录
Sysloder的密码，并按回车键。密码请咨询400-693-0555获取。)
sysloader(M)#
1 Load firmware via TFTP
2 Load firmware via FTP
3 Load firmware from USB disks (not available)
4 Select backup firmware as active
5 Show on-board firmware
6 Reset
7 Reset Administrator password
8 Load sysloader via TFTP
例如，SG-6000-A2000请参照以下操作提示：
                      GNU GRUB version 2.02
SG6000-ADNV-MX_MAIN-V6-t0419
SG6000-ADNV-MX_MAIN-r0420
*SYSLOADER( 通过上下箭头选中Sysloader并按回车键，进入Sysloader)
Sysloader 1.0.5 Sep 23 2020 - 16:09:24
sysloader#
1 Load firmware via TFTP
2 Load firmware via FTP

<!-- 来源页 780 -->
3 Load firmware from USB disks (available)
4 Select backup firmware as active
5 Show on-board firmware
6 Reset
7 Reset Administrator password
8 Load sysloader via TFTP
例如，需要通过Bootloader进入Sysloader的设备，请参照以下操作提示（以SG-6000-A200为
例）：
Press ESC to stop autoboot: 2( 键入“ESC”进入Bootloader的交互模式)
load sysloader from USB? [y]/n: n( 是否通过USB升级Sysloader，键入字母
“n”)
Run on-board sysloader? [y]/n: y( 键入字母“y”进入Sysloader)
Loading: #
Starting kernel ...
Sysloader 8.0.10 Feb 2 2023 - 09:16:23
sysloader#
1 Load firmware via TFTP
2 Load firmware via FTP
3 Load firmware from USB disks (not available)
4 Select backup firmware as active
5 Show on-board firmware
6 Reset
7 Reset Administrator password
例如，SG-6000-K6580键入“Ctrl+W”然后选择Sysloader，请参照以下操作提示：
                      GNU GRUB version 2.06
SG6000-HYGON-MX_MAIN-V6-r0420
SG6000-HYGON-R10_F-V6-r0409
*SYSLOADER( 通过上下箭头选中Sysloader并按回车键，进入Sysloader)

<!-- 来源页 781 -->
Enter username:(输入登录Sysloder的用户名，并按回车键。用户名请咨询400-
693-0555获取。)
Enter password:(输入登录Sysloder的密码，并按回车键。密码请咨询400-693-
0555获取。)
Loading Sysloader
▒
Sysloader 8.0.12 May 22 2023 - 01:52:42
sysloader#
1 Load firmware via TFTP
2 Load firmware via FTP
3 Load firmware from USB disks (not available)
4 Select backup firmware as active
5 Show on-board firmware
6 Reset
7 Reset Administrator password
8 Clear button
9 Load sysloader via FTP
2. 从Sysloader的操作选择菜单选择通过TFTP升级StoneOS。参照以下操作提示（以SG-6000-A2000为例）：
说明：各平台的Sysloader启动项略有差别，请参考Sysloader菜单介绍。
Sysloader 1.0.5 Sep 23 2020 - 16:09:24
sysloader#
1 Load firmware via TFTP
2 Load firmware via FTP
3 Load firmware from USB disks (available)
4 Select backup firmware as active
5 Show on-board firmware
6 Reset
7 Reset Administrator password

<!-- 来源页 782 -->
8 Load sysloader via TFTP
sysloader# 1( 在此处键入“1”并敲回车键)
3. 依次配置Sysloader的IP地址、TFTP服务器的IP地址、网关IP地址以及待升级的版本文件名称。参照以下操作提
示（以SG-6000-A2000为例）：
Local ip address [  ]: 192.168.1.1/16( 输入Sysloader的IP地址并敲回车键)
Server ip address [  ]: 192.168.1.20( 输入TFTP服务器的IP地址并敲回车键)
Gateway ip address [  ]: 192.168.1.2( 如果Sysloader与TFTP服务器的IP地址不属于
同一个网段，输入网关的IP地址并敲回车键；否则直接敲回车键)
File name : SG6000-ADNV-MX_MAIN-r0401.img( 输入待升级的版本文件名称并敲回
车键，系统开始通过TFTP获取需要升级的版本文件。如果版本文件不在TFTP服务器的
根目录下，则需要输入“多级目录+版本文件名称”。例如：SG6000-ADNV-MX_MAINr0401.img在TFTP服务器的test/5.5R12F2路径下，则file-name填写为
test/5.5R12F2/SG6000-ADNV-MX_MAIN-r0401.img。)
SG6000-ADNV-MX_MAIN- 100% |*******************************| 327M
0:00:00 ETA
4. 保存待升级的版本文件。参照以下操作提示（以SG-6000-A2000为例）：
Save this image? [y]/n: y( 键入字母“y”或者敲回车键，保存获得的版本文件)
Only 2 image can be saved, please remove( 设备的Flash中最多可以储存两
个版本文件。如果Flash中已经保存了两个版本文件，请根据提示对储存的版本文件进
行删除。)
1: SG6000-ADNV-MX_MAIN-r0420(Backup)( 删除当前已备份的版本文件)
2: SG6000-ADNV-MX_MAIN-V6-t0419(Active)( 删除系统当前版本文件)
3: remove all( 删除除待升级版本之外的所有版本文件)
4: cancel( 不做删除操作，选择4会退出升级)
Which one do you select: 2
Are you sure? [y]/n: y
Remove SG6000-ADNV-MX_MAIN-V6-t0419...
Saving
............................................................
Checking saved firmware

<!-- 来源页 783 -->
................................................ OK
Set SG6000-ADNV-MX_MAIN-r0401 as active boot image
5. 重启。系统将使用新的版本文件启动。参照以下操作提示（以SG-6000-A2000为例）：
1 Load firmware via TFTP
2 Load firmware via FTP
3 Load firmware from USB disks (not available)
4 Select backup firmware as active
5 Show on-board firmware
6 Reset
7 Reset Administrator password
8 Load sysloader via TFTP
sysloader# 6( 在此处键入“6”并敲回车键，系统开始重启)
6. 升级过程中需要等待一段时间，期间请勿执行任何操作。升级完成后，登录进入CLI，输入show version命令验
证系统是否已经成功升级到新版本。
在Sysloader中通过FTP服务器升级StoneOS
设备支持从FTP服务器获取待升级的版本文件，请按照以下步骤在Sysloader中通过FTP升级StoneOS：
1. 进入Sysloader后，从Sysloader的操作选择菜单中选择“2”并敲回车键。进入Sysloader的操作提示可参考在
Sysloader中通过TFTP服务器升级StoneOS的步骤1进行操作。
2. 配置Sysloader的IP地址。在“Local ip address [  ]:”后输入为Sysloader配置的IP地址。敲回车键。
3. 配置FTP服务器的IP地址。在“Server ip address [  ]:”后输入FTP服务器的IP地址。敲回车键。
4. 如果Sysloader与FTP服务器的IP地址不属于同一个网段，请配置Sysloader的网关IP地址。在“Gateway ip
address [  ]:”后输入网关的IP地址。敲回车键。
5. 在“User Name [anonymous ]:”后输入FTP用户名。敲回车键。
6. 在“Password :”后输入用户名对应的密码。敲回车键。
7. 在“File name :”后输入待升级的版本文件名称。敲回车键。系统开始通过FTP获取指定的StoneOS。如果版本
文件不在FTP服务器的根目录下，则需要输入“多级目录+版本文件名称”。例如：SG6000-ADNV-MX_MAINr0401.img在FTP服务器的test/5.5R12F2路径下，则file-name填写为test/5.5R12F2/SG6000-ADNV-MX_
MAIN-r0401.img。

<!-- 来源页 784 -->
8. 版本文件传输完成后，系统将会询问是否保存该版本文件。键入字母“y”，系统将把该版本文件保存到设备的
Flash中。
说明：设备的Flash中最多可以储存两个版本文件。如果Flash中已经保存了两个版本文件，请根据提示对储存的
版本文件进行删除。
9. 保存成功后，敲回车键，系统再次出现Sysloader的操作选择菜单，选择“6”并敲回车键。系统开始使用新的版
本文件重新启动。
10. 升级过程中需要等待一段时间，期间请勿执行任何操作。升级完成后，登录进入CLI，输入show version命令验
证系统是否已经成功升级到新版本。
提示: 对于匿名FTP服务器，在“User Name [anonymous ]:”和“Password :”后直接敲回
车键（第5步和第6步）。
在Sysloader中通过设备USB口升级StoneOS
用户还可以将待升级的版本文件放入U盘，通过设备的USB Host接口进行升级。
注意: 通过U盘升级StoneOS时，需要将待升级的版本文件保存在U盘的根目录下。
请按照以下步骤进行操作：
1. 将待升级的版本文件拷贝到U盘的根目录下。
2. 将U盘插入设备的USB接口中。
3. 进入Sysloader后，从Sysloader操作选择菜单中选择“3”并敲回车键。
4. 在待升级的版本文件后输入“y”，系统开始从U盘获取版本文件。不同设备回显信息可能存在差异，请以设备实
际显示内容为准。请按照以下提示操作：
sysloader# 3( 在此处键入“3”并敲回车键)
Please select firmware
1 SG6000-ADNV-MX_MAIN-r0401.img (usb0) [y]/n: n
2 SG6000-ADNV-MX_MAIN-V6-t0422.img (usb0) [y]/n: y
说明：如果设备插入了两个U盘，待升级的版本文件在USB1上，请先对USB0中的版本文件键入字母“n”。
5. 版本文件传输完成后，系统将会询问是否保存该版本文件。键入字母“y”，系统将把该版本文件保存到设备的
Flash中。

<!-- 来源页 785 -->
说明：设备的Flash中最多可以储存两个版本文件。如果Flash中已经保存了两个版本文件，请根据提示对储存的
版本文件进行删除。
6. 保存成功后，敲回车键，系统再次出现Sysloader的操作选择菜单，选择“6”并敲回车键。系统开始使用新的版
本文件重新启动。
7. 升级过程中需要等待一段时间，期间请勿执行任何操作。升级完成后，登录进入CLI，输入show version命令验
证系统是否已经成功升级到新版本。
8. 升级完成后请及时拔出U盘。
Sysloader菜单介绍
Sysloader使用菜单提示的方式帮助用户完成指定的操作。本节介绍Sysloader中各菜单项的功能。关于
Sysloader的菜单选项和功能，请参阅下表：
菜单选项
功能
1 Load firmware via TFTP
通过TFTP升级StoneOS。
2 Load firmware via FTP
通过FTP升级StoneOS。
3 Load firmware from USB disks
通过U盘升级StoneOS。
4 Select backup firmware as active
选择系统中保存的备份版本文件作为当前的StoneOS启
动系统。
5 Show on-board firmware
显示系统中保存的版本文件名称和状态。
6 Reset
重新启动系统。
7 Clear button
删除所有配置，恢复到出厂设置。
说明：SG-6000 A/X/K9180平台不支持该选项。部分设
备菜单该选项序号不同，请与实际对应为准。
7 Reset administrator password
重置默认管理员（hillstone）的密码。重置的密码为随
机生成的密码，仅首次重启时生效。首次重启后请及时
修改密码。
说明：部分设备菜单该选项序号不同，请与实际对应为
准。
8 Load sysloader via TFTP
通过TFTP升级Sysloader。
说明：SG-6000 A/X/K平台支持该选项。SG-6000-
A200/A200W/A200G4/A200WG4还支持通过USB升级
Sysloader。进入Bootloader交互模式后，在“load
sysloader from USB? ”提示后键入字母“y”，即可通
过USB升级Sysloader。
9 Load sysloader via FTP
通过FTP升级Sysloader。
说明：SG-6000-K6580支持该选项。
按照菜单提示，在“sysloader#”后键入菜单选项相对应的数字，然后按回车键。

<!-- 来源页 786 -->
热补丁升级
系统支持在保证业务不中断的情况下，对设备当前软件版本问题进行修复。用户可以通过FTP服务器、TFTP
服务器、FTPS服务器、SFTP服务器上传补丁文件，将补丁加载至进程中后，激活/运行补丁使之生效。
注意:
l
补丁升级只能通过CLI方式实现。
l
导入后的补丁文件默认是未加载（UNLOAD）状态，需要先加载到系统中再进行激活/运行操
作。
l
exec patch patch-name {activate | run}命令中activate和run的区别：activate是激活
已加载的补丁文件使之生效，被激活的补丁48小时后，会自动变为RUNNING状态。run是直
接运行已加载的补丁文件，设备重启后补丁依旧是运行状态。如果对补丁状态为ACTIVE的设备
进行重启，补丁会回退到未加载（UNLOAD）状态。
l
补丁升级不需要重启设备即可生效。
l
补丁与软件版本有配套关系。已运行有补丁的设备，进行版本升级操作后，该补丁将失效，变
为invalid状态。
热补丁升级步骤如下：
1. 将FTP/TFTP/FTPS/SFTP服务器上的补丁文件导入到设备中。请参阅导入补丁文件进行操作。
2. 使用exec patch patch-name load命令将导入到设备中的补丁文件加载到StoneOS系统中。请参阅加载/激活/
运行/删除补丁进行操作。
3. 使用exec patch patch-name {activate | run}命令激活或运行补丁文件，即可升级补丁文件成功。请参阅加载/
激活/运行/删除补丁进行操作。
4. 使用show patch命令查看补丁状态。根据步骤3的配置显示为ACTIVE或RUNNING状态。请参阅查看补丁状态进
行操作。
热补丁删除步骤如下：
1. 使用exec patch patch-name unload命令卸载已激活/运行的补丁文件。
2. 使用show patch命令查看补丁的状态，显示为UNLOAD。
3. 使用exec patch patch-name delete命令删除设备中的补丁文件。只有处于UNLOAD状态的补丁才能被删除。

<!-- 来源页 787 -->
导入补丁文件
通过FTP服务器将补丁文件导入到系统中，在执行模式下使用以下命令：
import patch from ftp server ip-address [vrouter vrouter-name] [user user-namepassword
password] filename
l
ip-address – 指定FTP服务器的IP地址。
l
user user-name password password – 指定FTP服务器的用户名和密码。
l
vrouter-name - 指定用于访问FTP服务器的设备接口对应的Vrouter。
l
filename – 指定需要导入到系统中的补丁文件的名称。如果该补丁文件在FTP服务器的根目录下，则直
接输入版本文件名称；如果该补丁文件在FTP服务器的多级目录下，需要填写为“多级目录+版本文件名
称”。例如：K5680-r0426.patch在FTP服务器的patch/5.5R11路径下，则file-name填写为
patch/5.5R11/K5680-r0426.patch。
通过TFTP服务器将补丁文件导入到系统中，在执行模式下使用以下命令：
import patch from tftp server ip-address [vrouter vrouter] [filename]
l
ip-address – 指定TFTP服务器的IP地址。
l
vrouter-name - 指定用于访问TFTP服务器的设备接口对应的Vrouter。
l
filename – 指定需要导入到系统中的补丁文件的名称。如果该补丁文件在TFTP服务器的根目录下，则
直接输入版本文件名称；如果该补丁文件在TFTP服务器的多级目录下，需要填写为“多级目录+版本文
件名称”。例如：K5680-r0426.patch在TFTP服务器的patch/5.5R12F2路径下，则file-name填写
为patch/5.5R12F2/K5680-r0426.patch。
通过FTPS服务器将补丁文件导入到系统中，在执行模式下使用以下命令：
import patch from ftps server ip-address [user user-name password password] [vrouter
vrouter-name] file-name
l
ip-address – 指定FTPS服务器的IP地址。
l
user user-name password password– 指定FTPS服务器的用户名和密码。
l
vrouter-name - 指定用于访问FTPS服务器的设备接口对应的Vrouter。
l
filename – 指定需要导入到系统中的补丁文件的名称。如果该补丁文件在FTPS服务器的根目录下，则
直接输入版本文件名称；如果该补丁文件在FTPS服务器的多级目录下，需要填写为“多级目录+版本文

<!-- 来源页 788 -->
件名称”。例如：K5680-r0426.patch在FTPS服务器的patch/5.5R12F2路径下，则file-name填写
为patch/5.5R12F2/K5680-r0426.patch。
通过SFTP服务器将补丁文件导入到系统中，在执行模式下使用以下命令：
import patch from sftp server ip-address [user user-name password password ]
[vrouter vrouter-name] file-name
l
ip-address – 指定FTPS服务器的IP地址。
l
user user-name password password– 指定FTPS服务器的用户名和密码。
l
vrouter-name - 指定用于访问SFTP服务器的设备接口对应的Vrouter。
l
filename – 指定需要导入到系统中的补丁文件的名称。如果该补丁文件在SFTP服务器的根目录下，则
直接输入版本文件名称；如果该补丁文件在SFTP服务器的多级目录下，需要填写为“多级目录+版本文
件名称”。例如：K5680-r0426.patch在FTPS服务器的patch/5.5R12F2路径下，则file-name填写
为patch/5.5R12F2/K5680-r0426.patch。
加载/激活/运行/删除补丁
用户可以对补丁进行删除、加载、激活、运行等操作，可在任何模式下，使用以下命令：
exec patch patch-name {delete | load | unload | activate | deactivate | run}
l
patch-name – 指定需要进行操作的补丁文件的名称。
l
delete – 删除指定名称的补丁文件。只有处于UNLOAD状态的补丁才能被删除。
l
load– 加载指定名称的补丁文件。
l
unload – 卸载指定名称的补丁文件。
l
activate – 激活指定名称的补丁文件使之生效。设备重启后，补丁状态将回退到未加载（UNLOAD）状
态。
l
deactivate – 将指定补丁状态回退到去激活状态。
l
run – 运行指定名称的补丁文件。设备重启后，补丁的状态仍然是运行状态。
查看补丁状态
加载/激活/运行/删除补丁后可以查看当前补丁的状态。
查看补丁状态，在任何模式下，使用以下命令：
show patch

<!-- 来源页 789 -->
系统用户管理
用户介绍
系统中的用户（User）是指使用设备提供的功能、服务、被设备认证、管理的用户。被设备认证的用户有本
地和外部两种。本地用户（Local User）由系统管理员创建，分属于不同的本地认证服务器，储存在系统的
配置文件中；外部用户（External User）储存在外部服务器上，例如AD服务器、LDAP服务器。为方便管
理用户，系统支持用户组功能，属于同一本地认证服务器的用户可以划分到不同的用户组中，并且同一个用
户可以同时属于不同的用户组，属于同一个本地认证服务器的用户组可以划分到不同的用户组中，并且同一
个用户组可以同时属于不同的用户组。下图以缺省本地AAA认证服务器“Local”的用户配置说明用户以及
用户组关系：
如上图所示，用户User1、User2和User3均属于用户组UserGroup1，而User3又同时属于用户组
UserGroup2，UserGroup2中还包含User4、User5以及用户组UserGroup1。
用户配置
本节包含以下内容：
l 配置用户
l 配置用户组
l 导出和导入用户列表
关联主题："查看用户/用户组/在线用户信息" 在第2660页
配置用户
用户的配置包括静态绑定用户的配置和系统认证用户的配置。

<!-- 来源页 790 -->
配置静态绑定用户
在全局配置模式下，使用以下命令将IP地址或MAC地址绑定到用户：
user-binding aaa-server-name user-name {ip {ipv4-address | ipv6-address} [auth-checkonly | vrouter vr-name] | mac mac-address}
l
aaa-server-name – 指定用户所属的AAA服务器名称。
l
user-name – 指定用户名称。
l
ip{ipv4-address | ipv6-address} - 指定IP地址, 支持IPv4地址和IPv6地址。
l
auth-check-only – 配置了该参数后，系统在对用户进行认证之前将会先检查该用户IP地址的合法性，
即检查是否与该用户绑定的IP地址一致。如果一致，则允许对用户进行认证。
l
vrouter vr-name – 指定IP地址或MAC地址所属的VRouter的名称。默认为缺省VR，即trust-vr。
l
mac mac-address - 指定MAC地址。
在全局配置模式下，使用该命令no的形式取消将IP地址或MAC地址绑定到用户：
no user-binding aaa-server-name user-name {ip {ipv4-address | ipv6-address} [auth-checkonly] | mac mac-address} [vrouter vr-name]
配置认证用户
用户可以为不同的本地AAA服务器配置用户或者用户组。进入本地AAA认证服务器配置模式，在全局配置模
式下使用aaa-server aaa-server-name type local命令。创建本地用户，在本地AAA服务器配置模式
下，使用以下命令：
user user-name
l
user-name – 指定用户名称。长度范围是1到63个字符。
执行该命令后，系统创建指定名称的用户并且进入用户配置模式；如果指定的用户名称已存在，则直接进入
用户配置模式。在本地AAA服务器配置模式下，使用该命令no的形式删除指定用户：
no user user-name
用户配置可分三类，分别是
l
用户基本配置：用户密码配置、用户过期时间配置、用户描述以及用户组配置。
l
拨号VPN相关配置：IKE ID配置
l
PnPVPN相关配置：DNS服务器配置、WINS服务器配置、DHCP地址池IP地址配置、DHCP地址池网络
掩码配置、DHCP地址池网关配置以及隧道路由配置。具体配置命令，请参阅《防火墙》的“网络参
数”。

<!-- 来源页 791 -->
指定用户密码
指定用户密码，在用户配置模式下，使用以下命令：
password [ irreversible-cipher ] password
l
irreversible-cipher - 指定用户密码的加密方式为不可逆加密算法。若不指定，即加密方式为可逆加
密算法。
l
可逆：表示系统将使用AES可逆加密算法对用户密码进行加密，在某些认证场景，系统可对密码进
行解密后使用。
l
不可逆：表示系统将使用SHA不可逆加密算法对用户密码进行加密，密码将无法被解密。此时通
过CHAP（挑战握手认证协议）方式将无法进行认证（L2TP VPN和802.1X功能也将无法使用）。
l
password – 指定用户的密码。长度范围是1到31个字符。
在用户配置模式下使用该命令no的形式取消密码的配置：
no password
指定用户有效期
超过有效期的用户不可以通过设备的认证，因此不可以在系统中继续使用。默认情况下，用户没有有效期限
制。指定用户的有效期，在用户配置模式下，使用以下命令：
expire Month/day/year HH:MM
l
Month/day/year HH:MM – 指定用户有效期时间，格式为“月/日/年小时:分钟”。例如命令expire
02/12/2010 12:00表示用户将在2010年2月12日的12：00过期。
在用户配置模式下使用该命令no的形式取消用户有效期配置：
no expire
配置用户描述信息
为用户提供描述信息，在用户配置模式下，使用以下命令：
desc string
l
string – 指定描述信息，范围是1到31个字符。
在用户配置模式下，使用该命令no的形式取消用户描述信息的指定：
no desc

<!-- 来源页 792 -->
指定用户组
用户可以根据不同类别组织到不同的用户组中。同一个用户可以同时属于多个用户组。为用户指定用户组，
在用户配置模式下，使用以下命令：
group user-group-name
l
user-group-name – 指定系统中已配置的用户组的名称。长度范围是1到127个字符。
配置多条该命令为同一用户指定多个用户组。注意：当一个用户加入的用户组个数超过256时，按照加入的
顺序，只有前256个生效。该原则适用于外部认证服务器上配置的用户组。
在用户配置模式下使用该命令no的形式取消用户组的指定：
no group user-group-name
关于如何配置用户组，请参阅下一节“用户组配置”。
配置用户组
用户可以为不同的本地AAA服务器配置用户或者用户组。
进入AAA认证服务器配置模式
进入本地AAA认证服务器配置模式，在全局配置模式下使用aaa-server aaa-server-name type local命
令。
创建本地用户组
创建本地用户组，在本地AAA服务器配置模式下，使用以下命令：
user-group user-group-name
l
user-group-name – 指定用户组名称。
执行该命令后，系统创建指定名称的用户组并且进入用户组配置模式；如果指定的用户组名称已存在，则直
接进入用户组配置模式。在本地AAA服务器配置模式下，使用该命令no的形式删除指定用户：
no user-group user-group-name
为用户组添加成员
在用户组配置模式下，使用以下命令为用户组添加成员，用户组成员可以是用户或者其它的用户组：
member {user user-name | group user-group-name}

<!-- 来源页 793 -->
l
user-name – 指定用户的名称。
l
user-group-name – 指定用户组的名称。系统支持的用户组的嵌套层数最多为5层，并且不支持回环
嵌套，用户组不可以再嵌套它所属的用户组。
配置多条该命令为用户组添加多个成员。
在用户组配置模式下，使用该命令no的形式将成员从用户组中删除：
no member {user user-name | group user-group-name}
导出和导入用户列表
为防止恢复配置时误将用户信息重置，用户可以将用户信息以文件格式从设备端导出或者导入。系统支持导
入带BOM的UTF-8编码格式的.txt格式和带BOM的UTF-8编码格式的.csv格式的用户列表文件。导入时，系
统将会对整个文件进行合法性和用户密码复杂度检查，检查成功后完成导入，若检查失败，则导入失败。系
统导出的用户列表文件为.csv格式，内容为系统当前保存的用户列表信息。
下图为.csv格式的用户列表文件及参数描述示例：
下图为文本格式的用户列表文件及参数描述实例：
注意: 在导入用户列表文件前，请仔细阅读上图中的批注文字，并且将用户信息按照格式要求填
写。

<!-- 来源页 794 -->
导出用户列表
导出用户列表，在执行模式下使用以下命令：
export aaa user to {tftp server ip-address | ftp server ip-address [user user-name]} filename
l
ip-address – 指定FTP或者TFTP服务器的IP地址。
l
user user-name – 指定FTP服务器的用户名。
l
file-name – 指定导出的用户列表文件名称。
导入用户列表
导入用户列表，在执行模式下使用以下命令：
import aaa user from { tftp server ip-address | ftp server ip-address [user user-name]} filename
l
ip-address – 指定FTP或者TFTP服务器的IP地址。
l
user user-name – 指定FTP服务器的用户名。
l
file-name – 指定导入的用户列表文件名称。
导入用户信息的原则是：
l
如果用户列表文件中的用户信息在系统中已经存在，则将用户列表文件的此用户信息更新到系统中。
l
如果用户列表文件中的用户未在系统中存在，则新建此用户信息到系统中。
注意:
l
导入用户列表文件后，配置立即生效。
l
导入用户列表文件后，系统会在CLI中提示导入成功的用户数目。
l
导入的用户列表文件中，“用户名称”参数不能包含斜线、逗号、双引号、问号、
“@”；“用户组名称”参数不能包含逗号、双引号、问号。
l
导入的用户列表文件中，“账号到期日”参数需符合DD/MM/YYYY HH:SS格式。
l
如果导入的用户列表文件格式为文本文件，应注意以下几点：
l
文件中的每个参数需用半角逗号隔开。
l
若某个参数不存在，则直接以半角逗号代替。例如：“123123,,local”。

<!-- 来源页 795 -->
l
第一行参数的顺序固定，不区分大小写。例
如：“Servername,userName,pAssWord”。
l
文件不能包含空行和乱码行，否则将会导入失败。
l
若某个参数低于或超过其长度限制，则导入失败。
用户名称的长度范围为1-63字符。
密码的长度范围为1-31字符。
手机号码的长度范围为6-15字符。
邮箱的长度范围是1-127字符。
描述的长度范围为0-127字符。
角色
角色拥有某些特定的权限，例如某角色可以访问某指定网络资源或者某角色可以独享一定带宽等。在系统
中，用户与权限并不直接关联，而是需要通过角色把二者联系起来。角色映射规则定义角色和用户的对应关
系，功能配置中，为不同的角色指定不同的服务，由此，角色对应的用户即可拥有其角色的服务。系统支持
角色组合，即通过对角色进行“与”、“或”逻辑运算，将角色进行组合。被不同功能模块引用的角色对应
的用户将是经过运算后的角色对应的用户。设备支持角色黑名单功能，通过将角色加入角色黑名单来控制映
射到该角色的用户能否认证登录成功。当用户进行认证登录时，若用户通过角色映射获取到的角色信息在角
色黑名单中则认证登录失败，用户将无法访问网络。
系统支持以下基于角色的功能：
l 基于角色的策略规则：实现不同用户的访问控制。
l 基于角色的QoS：实现不同用户的带宽控制。
l 基于角色的统计集：统计不同用户的带宽、会话数以及新建会话速率。
l 基于角色的会话限制：实现对特定用户的会话数限制。
l SCVPN基于角色的主机安全检测：实现不同用户对特定资源的访问控制。
l 基于角色的策略路由：实现根据不同源用户选择路由。
l SSL VPN/ZTNA/WebAuth/L2TP/802.1X/IPSec VPN（UserGroup）基于角色的访问限制：通过角色黑名单实
现仅特定用户能对网络进行访问。
相关内容：
l 配置角色

<!-- 来源页 796 -->
角色配置
角色配置包括：
l 创建角色
l 配置角色映射规则
l 配置角色组合
l 配置角色黑名单
创建角色
创建角色，在全局配置模式下使用以下命令：
role role-name
l
role-name – 指定角色名称。长度范围是1到31个字符。
在全局配置模式下使用该命令no的形式删除指定的角色：
no role role-name
配置角色映射规则
角色映射规则表达式指定角色与用户或者用户组的映射关系。系统最多支持64条角色映射规则，每个规则中
最多可以包含256条映射条目。
当SCVPN用户以USB Key证书认证方式登录并通过认证时，系统可以根据USB Key数字证书中的证书名称
（证书CN字段）、组织机构（证书OU字段）或者证书DN为用户映射相应的角色。关于如何只用USB Key证
书进行认证的详细信息，请参阅《VPN》的“配置客户端USB Key证书认证”。
进入角色映射规则配置模式
配置角色映射规则，需要首先进入角色映射规则配置模式，在全局配置模式下，使用以下命令：
role-mapping-rule rule-name
l
rule-name – 指定角色映射规则的名称。长度范围是1到31个字符。执行该命令后，系统创建指定名称
的角色映射规则，并且进入角色映射规则配置模式。如果指定的名称已存在，则直接进入角色映射规则
配置模式。
在全局配置模式下使用该命令no的形式删除指定的角色映射规则：
no role-mapping-rule rule-name

<!-- 来源页 797 -->
配置角色映射条目
在角色映射规则配置模式下，使用以下命令配置角色映射条目：
match {any | user user-name | user-group user-group-name | cn cn-field | ou ou-field | userattribute user-attribute-name | certificate-dn dn-field} role role-name
l
any | user user-name | user-group user-group-name | cn cn-field | ou ou-field | userattribute user-attribute-name | certificate-dn dn-field – 指定映射条目中的用户、用户组、证
书名称、组织机构、用户属性或者证书DN。any表示系统中任何用户、用户组、证书名称、组织机构、
用户属性或者证书DN。关于用户属性配置，参见配置用户属性实例。
l
role role-name – 指定用户、用户组、证书名称、组织机构、用户属性或者证书DN相对应的角色名
称。
配置多条该命令添加多个映射条目。
在角色映射规则配置模式下使用该命令no的形式删除指定的映射条目：
no match {any | user user-name | user-group user-group-name | cn cn-field | ou ou-field |
user-attribute user-attribute-name | certificate-dn dn-field} role role-name
配置用户属性实例
配置用户属性实例，需要首先进入用户属性实例配置模式，在全局配置模式下，使用以下命令：
role-mapping-source user-attribute user-attribute-name protocol-type {radius | ad/ldap}
l
user-attribute-name - 指定用户属性实例名称。
l
protocol-type {radius | ad/ldap} - 指定协议类型，可以是RADIUS（radius）或者AD/LDAP
（ad/ldap）。
执行该命令后，系统创建指定名称及协议类型的用户属性实例，并且进入用户属性实例配置模式。如果指定
的名称已存在，则直接进入用户属性实例配置模式。
注意: 系统最多允许配置64个用户属性实例。
在全局配置模式下，使用no role-mapping-source user-attribute user-attribute-name命令删除已
配置的用户属性实例。
配置过滤条件
为用户属性实例配置过滤条件，在用户属性实例配置模式下，使用以下命令：

<!-- 来源页 798 -->
attribute attribute-value {contain | end-with | equal-to | greater-than | less-than | same-as |
start-with} value
l
attribute-value - 指定用户属性名称，可以为自定义名称或者常用用户属性名称。
l
contain | end-with | equal-to | greater-than | less-than | same-as | start-with - 指定映射条
件，可以是包含（contain）、终止于（end-with）、等于（equal-to）、大于（greater-than）、
小于（less-than）、一致（same-as）或者起始于（start-with）。
l
value - 指定用户属性的映射值。
注意:
l
每个用户属性实例中最多允许配置8条过滤条件；
l
当协议类型为RADIUS时，字符串类型的用户属性对应的映射条件只能为contain（包含）、
start-with（起始于）、end-with（终止于）或者same-as（一致）；数字类型的用户属性
对应的映射条件只能为equal-to（等于）、greater-than（大于）或者less-than（小
于）；
l
当映射条件为contain（包含）、start-with（起始于）、end-with（终止于）、或者
same-as（一致）时，映射值可以为字符串或者数字；当映射条件为equal-to（等于）、
greater-than（大于）或者less-than（小于）时，映射值只能为数字。
在用户属性实例配置模式下，使用该命令no的形式删除已配置的用户属性实例过滤条件：
no attribute attribute-value {contain | end-with | equal-to | greater-than | less-than | sameas | start-with} value
配置命中方式
为用户属性实例配置命中方式，在用户属性实例配置模式下，使用以下命令：
match {once | all}
l
once | all - 指定用户属性实例的命中方式，一种方式为如果用户满足用户属性实例中的任意一条过滤条
件，该用户就会匹配到用户属性实例映射到的角色（once），另一种为仅当用户满足用户属性实例中的
全部过滤条件，该用户才会匹配到用户属性实例映射到的角色（all）。
在用户属性实例配置模式下，使用no match命令取消用户属性实例命中方式的指定。

<!-- 来源页 799 -->
配置角色组合
Hillstone设备支持角色组合，即通过逻辑运算重新组合已有角色。配置角色组合，在全局配置模式下使用
以下命令：
role-expression [not] r1 [{and | or} [not] r2] roler3
l
[not] r1 – 指定表达式中的第一个角色。not表示“非”；r1为系统中已创建的角色名称。例如，not
testrole1表示的结果为非testrole1以外的所有角色。
l
and | or – 指定运算符符号。and表示“和”；or表示“或”。
l
[not] r2 – 指定表达式中的第二个角色。not表示“非”；r2为系统中已创建的角色名称。
l
roler3 – 指定角色运算的结果角色。role关键字为推导符，r3为结果角色名称。
在全局配置模式下使用该命令no的形式删除指定的角色表示式：
no role-expression [not] r1 [{and | or} [not] r2] roler3
配置角色黑名单
系统支持角色黑名单功能，通过将角色加入角色黑名单来控制映射到该角色的用户能否认证登录成功。当用
户进行认证登录时，若用户通过角色映射获取到的角色信息在角色黑名单中则认证登录失败，用户将无法访
问网络。
配置角色黑名单，在全局配置模式下使用以下命令：
role-block-list role-name
l
role-name - 指定加入角色黑名单中的角色名称。取值范围是1到31个字符。
说明：系统仅支持将已创建好的角色名称加入角色黑名单，若要创建新的角色，在全局配模式下使用
rolerole-name命令。
在全局配置模式下使用no role-block-list role-name命令删除角色黑名单中指定的角色。
查看角色信息
用户可以在任何模式下使用show命令查看角色信息。
l
查看角色信息：show role
l
查看角色映射信息：show role-mapping-rule [rule-name]
l
查看角色组合信息：show role-expression
l
查看角色黑名单信息：show role-block-list

<!-- 来源页 800 -->
用户下线告警
系统支持用户下线告警功能，可以实现对用户下线情况的监控。当在指定时间内，下线用户数达到指定阈值
时，系统将会生成相应的事件日志进行告警。同时，系统还可以通过SNMP Trap主机、短信、邮件三种方式
将告警信息及时通知到相关人员，以便及时进行后续的响应处理。
配置用户下线告警功能，请按照以下步骤进行操作：
1. 创建用户下线告警模板。
2. 配置L2TP VPN实例，引用用户下线告警模板。
注意:
l
系统最多支持创建4个用户下线告警模板。
l
一分钟内最多发送一次告警信息给指定的Trap主机/邮箱/手机号码。
创建用户下线告警模板
创建用户下线告警模板，在全局配置模式下，使用以下命令：
user-logout-alarm profile profile_name
l
profile_name – 指定用户下线告警模板的名称。执行该命令后，系统将创建指定名称的用户下线告警
模板，并进入用户下线告警配置模式，如果指定的名称已存在，则直接进入用户下线告警配置模式。范
围是1到31个字符，最多支持创建4个用户下线告警模板。
在全局配置模式下，使用no user-logout-alarm profile profile_name命令删除指定的用户下线告警模
板。
配置用户下线告警阈值
系统支持配置用户下线告警的阈值，当在一定时间内，下线用户数达到阈值则进行相应告警。如不配置，默
认在60秒内，发生50次用户下线则会进行告警。
配置用户下线告警阈值，在用户下线告警配置模式下，使用以下命令：
logout-threshold times interval time-value
l
times – 指定用户下线的次数阈值。范围是10到500次，默认50次。
l
interval time-value – 指定用户下线的时间阈值。范围是10到300秒，默认60秒。
在用户下线告警配置模式下，使用no logout-threshold命令恢复用户下线告警阈值的默认值。

<!-- 来源页 801 -->
配置用户下线告警方式
产生用户下线告警信息后，系统支持通过SNMP Trap主机、短信、邮件三种方式进行告警，将告警信息发送
给相关人员，以便及时进行后续的响应处理。
注意: 一分钟内最多发送一次告警信息给指定的Trap主机/邮箱/手机号码。
用户下线告警方式的配置包括：
l
开启/关闭SNMP Trap告警功能
l
开启/关闭短信告警功能
l
指定短信告警方式
l
指定短信网关
l
指定接收告警短信的手机号码
l
开启/关闭邮件告警功能
l
指定邮件服务器
l
指定接收告警邮件的邮箱
开启/关闭SNMP Trap告警功能
系统支持通过SNMP Trap主机告警，开启SNMP Trap告警功能后，当系统产生告警信息时，将会发送告警
Trap报文给系统中已配置的Trap主机。
开启/关闭SNMP Trap告警功能，在用户下线告警配置模式下，使用以下命令：
snmp-trap {enable | disable}
l
enable – 开启SNMP Trap告警功能。
l
disable – 关闭SNMP Trap告警功能。
注意: 使用SNMP Trap告警功能前，请先配置Trap主机。关于Trap主机的配置方法，请参阅配置
trap报文目标主机地址。
开启/关闭短信告警功能
系统支持通过短信告警，开启短信告警功能后，当系统产生告警信息时，将会发送告警通知短信给指定的手
机号码。
开启/关闭短信告警功能，在用户下线告警配置模式下，使用以下命令：

<!-- 来源页 802 -->
sms {enable | disable}
l
enable – 开启短信告警功能。
l
disable – 关闭短信告警功能。
指定短信告警方式
使用短信进行告警时，系统支持指定短信告警方式，产生告警信息后将通过短信猫或短信网关自动向指定的
手机号码发送告警短信。如不指定，默认的短信告警方式为“短信网关”。
配置短信告警方式，在用户下线告警配置模式下，使用以下命令：
sms type {modem | service-provider}
l
modem – 指定短信告警方式为“短信猫”。说明：云·界不支持指定该参数。
l
service-provider – 指定短信告警方式为“短信网关”。
在用户下线告警配置模式下，使用no sms type命令恢复默认的短信告警方式。
注意: 由于云·界不支持指定短信告警方式为“短信猫”，因此配置no sms type命令将无法生
效。
指定短信网关
当用户指定短信告警方式为“短信网关”时，需同时指定系统中已配置的短信网关。
指定短信网关，在用户下线告警配置模式下，使用以下命令：
sms service-provider provider_name
l
provider_name – 指定系统中已配置的短信网关。
在用户下线告警配置模式下，使用no sms service-provider命令取消短信网关的指定。
注意: 使用短信告警功能前，请先配置短信网关。关于短信网关的配置方法，请参阅配置短信网
关。
指定接收告警短信的手机号码
指定接收告警短信的手机号码，在用户下线告警配置模式下，使用以下命令：
phone phone_number
l
phone_number – 指定接收告警短信的手机号码。范围是6到15个字符。

<!-- 来源页 803 -->
重复配置以上命令可以指定多个手机号码，最多支持指定3个手机号码。
在用户下线告警配置模式下，使用no phone phone_number命令删除指定的手机号码。
开启/关闭邮件告警功能
系统支持通过邮件告警，开启邮件告警功能后，当系统产生告警信息时，将会发送告警通知邮件给指定的邮
箱。
开启/关闭邮件告警功能，在用户下线告警配置模式下，使用以下命令：
email {enable | disable}
l
enable – 开启邮件告警功能。
l
disable – 关闭邮件告警功能。
指定邮件服务器
使用邮件进行告警时，需同时指定系统中已配置的邮件服务器。
指定邮件服务器，在用户下线告警配置模式下，使用以下命令：
smtp-server server_name
l
server_name – 指定系统中已配置的邮件服务器。
在用户下线告警配置模式下，使用no smtp-server命令取消邮件服务器的指定。
注意: 使用邮件告警功能前，请先配置邮件服务器。关于邮件服务器的配置方法，请参阅配置
SMTP服务器实例。
指定接收告警邮件的邮箱
指定接收告警邮件的邮箱，在用户下线告警配置模式下，使用以下命令：
email email_address
l
email_address – 指定接收告警邮件的邮箱。范围是1到127个字符。
重复配置以上命令可以指定多个邮箱，最多支持指定3个邮箱。
在用户下线告警配置模式下，使用no email email_address 命令删除指定的邮箱。
查看用户下线告警模板
查看系统中已创建的用户下线告警模板，包括模板名称、告警阈值、告警方式。在任意模式下，使用以下命
令：
show user-logout-alarm profile [profile_name]

<!-- 来源页 804 -->
l
profile_name – 指定用户下线告警模板名称。如不指定，默认展示系统中所有已创建的用户下线告警
模板。

<!-- 来源页 805 -->
硬盘热插拔
型号说明：
l
支持：SG-6000-A系列ASIC防火墙。
l
支持：SG-6000-K系列ASIC防火墙。
设备支持通知式硬盘热插拔，在热拔硬盘前需要先执行卸载命令，让系统停止对该硬盘的读写操作、解除业
务挂载，再执行物理拔硬盘的操作；在热插硬盘后需要执行挂载命令，让系统识别硬盘、恢复业务挂载。
双硬盘设备支持组建RAID1阵列使两块硬盘相互备份，当其中一块硬盘损坏时，能够通过热插拔的方式更换
硬盘，保障设备在数据不丢失、系统不重启的状态下完成硬盘更换。
注意: 不允许在硬盘挂载时（硬盘槽位为非unmounted状态）热拔硬盘，否则可能导致数据丢
失、日志记录异常等情况。
硬盘槽位状态
硬盘槽位分为以下6种状态：
状态
说明
absent
当前槽位未插入硬盘/未检测到硬盘在位。
unmounted
当前槽位已插入硬盘，且硬盘未挂载。
mounted
当前槽位已插入硬盘，且硬盘已挂载，工作在非RAID1模式。
raid1(active sync)
当前槽位已插入硬盘，且硬盘已挂载，工作在RAID1模式，数据同步正常。
raid1(rebuilding)
当前槽位已插入硬盘，且硬盘已挂载，工作在RAID1模式，数据同步重建中。
raid1(faulty)
当前槽位已插入硬盘，且硬盘已挂载，工作在RAID1模式，检测到硬盘已损坏。

<!-- 来源页 806 -->
单硬盘槽位设备/双硬盘槽位设备（非RAID1）状态示意图如下：
说明：
①插入硬盘
②拔出硬盘
③卸载硬盘
④挂载硬盘
⑤硬盘挂载时直接拔出硬盘
（违规操作，可能导致设备
异常）
双硬盘槽位设备（RAID1）状态示意图如下：
说明：
①插入硬盘
②拔出硬盘
③组建RAID1
④删除RAID1
⑤RAID1模式
下检测到硬盘损
坏
⑥卸载损坏硬盘
⑦卸载硬盘
⑧拔出硬盘
⑨插入硬盘
⑩挂载硬盘
⑪硬盘数据同
步

<!-- 来源页 807 -->
配置硬盘热插拔
开始之前
l 阅读"硬盘热插拔" 在第803页介绍。
挂载/卸载硬盘
对于非RAID1模式的设备，仅支持对disk 0执行挂载/卸载硬盘操作，不支持对disk 1执行。在该场景下：
l
挂载硬盘：挂载硬盘后无需手动执行重置数据库操作，可以直接使用硬盘。
l
卸载硬盘：卸载硬盘时将选择是否重置数据库。若后续继续使用该硬盘，且硬盘数据不变，则可以不重
置数据库；若后续不需要使用该硬盘或替换硬盘，则需重置数据库。
注意:
l
卸载硬盘时若未重置数据库，在重新挂载前可能提示数据库报错，该现象为正常情况。
l
卸载硬盘时若未重置数据库，但后续需要挂载其他硬盘时，则需要在挂载新硬盘后执行exec
database reset命令手动重置数据库。
对于RAID1模式的设备，在挂载硬盘时，待挂载的硬盘容量必须大于等于RAID1阵列的容量（即show disk
命令显示的total容量）。
注意: RAID1模式下支持卸载所有硬盘，并保留RAID1模式。但由于加入RAID1阵列必须对原有硬
盘进行格式化，因此在重新挂载硬盘后，将无法恢复原有的硬盘数据，请谨慎操作。
挂载/卸载硬盘，在任意模式下，使用以下命令：
exec disk {0 | 1} {online | offline}
l
disk {0 | 1} - 对指定槽位的硬盘进行挂载/卸载。单硬盘槽位设备不需配置槽位号。
l
online - 挂载硬盘。
l
offline - 卸载硬盘。
组建RAID1
双硬盘设备支持组建RAID1阵列使两块硬盘相互备份，当其中一块硬盘损坏时，能够通过热插拔的方式更换
硬盘，保障设备在数据不丢失、系统不重启的状态下完成硬盘更换。

<!-- 来源页 808 -->
注意:
l
组建RAID1阵列时会对硬盘进行格式化。
l
支持不同容量硬盘组建RAID1阵列，组建后RAID1阵列的可用容量为两块硬盘中的最小容量。
该场景下若将两块硬盘全部卸载，然后先挂载容量较大的硬盘，则RAID1阵列的可用容量为容
量较大的硬盘的容量，此时将无法再挂载容量较小的硬盘。因此如需将两块硬盘重新组建
RAID1，则可以先删除RAID1阵列，再重新组建RAID1阵列；或者卸载两块硬盘，然后先挂载
小容量硬盘，再挂载大容量硬盘。
l
对于暂时只有一块硬盘但后续会加装硬盘的场景，支持以一块硬盘组建RAID1，后续可以用挂
载硬盘方式将新硬盘加入RAID1阵列。
组建RAID1阵列，在任意模式下，使用以下命令：
exec raid1 {active | inactive}
l
active - 组建RAID1阵列。该操作会自动重置数据库。
l
inactive - 删除RAID1阵列。该操作会自动重置数据库。
查看硬盘信息
用户可以查看硬盘信息，包括硬盘槽位状态、硬盘S/N号、硬盘厂商、硬盘容量等。
查看硬盘信息，在任意模式下，使用以下命令：
show disk
以下是返回结果示例：
SG-6000# show disk
------------ Data disk 0 -------------
Status: mounted
S/N: XXXXXXXXX
Manufacturer: XXX
--------------------------------------
The percentage of data disk utilization: 5.8%
total(KB) used(KB) free(KB)
1007998627 58148364 949850263
硬盘热插拔典型配置方案
开始之前

<!-- 来源页 809 -->
l 阅读"硬盘热插拔" 在第803页介绍。
单硬盘槽位设备更换硬盘
单硬盘槽位设备更换硬盘，请按照以下步骤进行操作：
1. 执行exec disk offline命令卸载硬盘。由于需要更换其他硬盘，此时需选择重置数据库。完成后硬盘槽位状态由
mounted变为unmounted。
2. 拔出硬盘。硬盘槽位状态变为absent。
3. 插入新硬盘。硬盘槽位状态变为unmounted。
4. 执行exec disk online命令挂载硬盘。完成后硬盘槽位状态变为mounted。
双硬盘RAID1阵列下更换损坏硬盘
双硬盘RAID1阵列下更换损坏硬盘，请按照以下步骤进行操作：
1. 执行show disk命令查看损坏硬盘。损坏硬盘的槽位状态为raid1(faulty)。
2. 执行exec disk offline命令卸载硬盘。完成后硬盘槽位状态变为unmounted。
3. 拔出损坏硬盘，硬盘槽位状态变为absent。
4. 插入新硬盘。需确保新插入的硬盘容量大于等于RAID1阵列的容量（即show disk命令显示的total容量）。硬盘
槽位状态变为unmounted。
5. 执行exec disk online命令挂载硬盘。完成后硬盘槽位状态变为raid1(rebuilding)。
6. 待硬盘数据同步完成，硬盘槽位状态变为raid1(active sync)。
双硬盘RAID1阵列下替换大容量硬盘
双硬盘RAID1阵列下替换大容量硬盘，请按照以下步骤进行操作：
1. 执行exec raid1 inactive命令删除RAID1阵列。两个硬盘槽位状态变为unmounted。
2. 拔出两块硬盘。两个硬盘槽位状态变为absent。
3. 插入两块大容量硬盘。两个硬盘槽位状态变为unmounted。
4. 执行exec raid1 active命令组建RAID1阵列，组建时会对硬盘进行格式化。组建完成后两个硬盘槽位状态变为
raid1(active sync)。

<!-- 来源页 810 -->
配置存储设备
系统提供许可证控制的网络行为控制功能。该功能在对用户的网络访问行为进行控制和管理的同时，也对用
户的网络行为进行全面记录，记录到的日志信息可以以数据库文件的方式保存到本地数据库中。
提示: 能够保存本地数据库的存储设备包括SD存储卡、U盘和Hillstone山石网科提供的存储扩展
模块。目前只有部分型号的Hillstone设备配有SD卡槽、USB接口或支持存储扩展模块的扩展槽。
格式化存储设备
当存储设备不能正常运行、Hillstone设备不支持存储设备的磁盘文件系统或存储设备未被格式化时，用户
可以通过格式化存储设备的方法修复存储设备的故障、更改磁盘文件系统和格式化存储设备。
注意: 格式化操作会删除存储设备上的所有数据，请自行备份重要文件。
格式化存储设备，请在任何模式下输入以下命令：
exec format [sd0 | usb0 | usb1 | storage X]
l
sd0 – 对SD卡槽内插入的SD存储卡进行格式化操作。
l
usb0 | usb1 – 对与指定USB口相连的存储设备进行格式化操作。
l
storageX – 对指定的存储扩展模块进行格式化操作。X为插入存储扩展模块的扩展槽号，不同平台X的
取值范围不同。
安全删除存储设备
如果用户在信息传输的过程中强行拔下或弹出存储设备，可能会造成数据丢失，导致日志信息存储不全。为
了保证数据传输的完整性，请在任何模式下输入以下命令，安全删除存储设备：
exec detach [sd0 | usb0 | usb1 | storage X]
l
sd0 – 安全删除SD卡槽内插入的SD存储卡。
l
usb0 | usb1 – 安全删除指定USB口相连的存储设备。
l
storageX – 安全删除指定的存储扩展模块。X为插入存储扩展模块的扩展槽号，不同平台X的取值范围
不同。

<!-- 来源页 811 -->
数据库修复
当数据库不能进行正常的操作时，请在全局配置模式下输入以下命令，修复数据库表项：
exec database repair
如果数据库表项修复未按预期修复数据库至正常状态，请在全局配置模式下输入以下命令，修复数据库关键
字：
exec database reset
注意: 执行该命令会导致原有的数据库表丢失。
数据库数据升级
当用户对系统版本进行升级后，系统的新旧版本数据同时存在于数据库中，例如日志、报表文件、监控数据
等，由于新旧版本数据格式不一致，导致系统页面可能无法正常显示旧版本数据信息。为保证系统功能的正
常显示与使用，用户需及时将数据库中的旧版本数据升级至符合当前版本的数据格式，若用户不需要旧版本
数据也可以选择将旧版本数据删除。系统仅支持手动升级数据库数据。
升级数据库数据，在任何模式下，使用以下命令：
exec database data {upgrade | delete}
l
upgrade - 将与系统当前版本数据格式不一致的旧版本数据升级至符合当前系统版本的数据格式。若系
统版本降级后，当数据状态处于“待升级”时，可将数据库的数据降级至符合当前版本的数据格式。
l
delete - 将与系统当前版本数据格式不一致的旧版本数据删除。
查看数据库数据升级状态
型号说明：SG-6000-A2200/A1800/A1600不支持升级数据库数据。
系统数据库中数据的升级状态共有三种，分别是“Upgrade not started（待升级）”、“Upgrading
（升级中）”和“No database files need to be upgraded.（已是最新，无需升级）”。查看数据库
数据升级状态，在任何模式下，使用以下命令：
show mysql data operate
以下是状态为“待升级”的返回结果示例：

<!-- 来源页 812 -->
hostname#show mysql data operate
Mysql database progress:
============================================
State Percentage
----------------------------------------------------------------------
Upgrade not started.
============================================

<!-- 来源页 813 -->
删除模块扩展槽配置信息
在部分设备（X系列设备、SG-6000-K20803/K9180/K7680/K7280/K6680/K6580设备）运行过程中，
由于各种原因，用户需要更换扩展模块或者拔出扩展模块。Hillstone设备支持模块卡的热插拔操作，可以
保证整个系统不间断运行。
由于模块扩展槽配置信息的依赖关系比较复杂，对于IOM/SIOM模块，执行热插拔操作时，用户需要使用
exec unset slot {number}命令检查并删除模块扩展槽的配置信息，使模块正常初始化。
删除模块扩展槽的配置信息，在执行模式下，使用以下命令：
exec unset slot slot-number
l
slot-number – 指定IOM/SIOM模块所在的槽位号。取值范围为1-128。
执行该命令后，根据具体情况，系统会出现不同的提示信息。用户可根据提示信息的描述选择下一步操作。
注意:
l
如果模块扩展槽存在接口配置依赖关系，用户必须先手动删除接口配置依赖关系后，再执行该
命令删除模块扩展槽的配置信息。
l
SCM模块、SSM模块或QSM模块进行热插拔操作时，则无需执行该命令。

<!-- 来源页 814 -->
删除虚拟网卡配置信息
型号说明：云·界
对于虚拟化安全产品云·界，如果用户在信息传输的过程中强行移除虚拟网卡，可能会造成数据丢失或其他异
常情况。为了保证数据传输的完整性，删除虚拟网卡时，请按照以下步骤进行:
l
首先，在任何模式下输入以下命令，关闭网卡：
exec detach-port port port-number
l
port-number – 指定的需要关闭的虚拟网卡的接口号。即用户在设备上查看接口信息时，
Etherent0/X的“X”的值。
执行完成上述命令后，相应的接口的物理/协议/连接等状态将变为Down状态（通过show interface命
令查看）。
l
然后，在虚拟管理器上移除虚拟网卡。
l
最后，在执行模式下，使用以下命令删除虚拟网卡的配置信息，使模块正常初始化：exec unset-port
port port-number
l
port-number – 指定需要删除配置信息的虚拟网卡的接口号。即用户在设备上查看接口信息时，
Etherent0/X的“X”的值。此处X数值需与exec detach-port port命令的端口号保持一致。
执行完上述命令后，用户即安全删除完成虚拟网卡。
注意:
l
禁止删除接口ethernet0/0，否则将导致产品的许可证失效。
l
云·界最多可支持10块虚拟网卡，虚拟网卡对应的接口号将按照插入顺序递增，直到达到10个
接口。当用户在接口之间删除一个接口，即产生一个空位后，若再新插入一块虚拟网卡，新网
卡的接口号将继承原空位上的接口号。

<!-- 来源页 815 -->
密码卡管理
型号说明：
l
支持：SG-6000-A2000-GM、SG-6000-A3000-GM
l
支持：SG-6000-K5680-A-GM、K2680-A-GM、K2380-A-GM
SG-6000-A2000-GM/A3000-GM/K5680-A-GM/K2680-A-GM/K2380-A-GM内置密码卡。该卡提供国
家商用密码算法，可以满足系统数据的签名/验证、加密/解密的要求，保证传输数据的机密性、完整性和有
效性。密码卡需要使用USBKey激活后才能使用。山石网科为这些设备随箱提供两种USBKey，共计4个，分
别是3个管理员USBKey和1个操作员USBKey。用户通过在设备上插入USBKey来激活密码卡。使用不同的
USBKey激活，密码卡功能的支持情况有所差异。“备份/恢复密钥信息”功能仅当用户通过管理员USBKey
激活密码卡后支持使用。
注意: “密码卡管理”功能仅当用户通过“安全操作员（operator）”角色登录设备时支持配置。
密码卡管理包括以下内容：
l 激活密码卡
l 取消激活密码卡
l 算法即时自检
l 算法周期性自检
l 备份密钥信息
l 恢复密钥信息
l 修改PIN口令
l 重置PIN口令
l 查看密码卡状态
进入密码卡配置模式
密码卡管理功能需要在密码卡配置模式下进行，在全局配置模式下，使用以下命令进入密码卡配置模式：
crypto-global

<!-- 来源页 816 -->
激活密码卡
SG-6000-A2000-GM/A3000-GM激活密码卡需使用1个操作员USBKey或2个管理员USBKey。
SG-6000-K5680-A-GM/K2680-A-GM/K2380-A-GM激活密码卡需使用1个操作员USBKey或1个管理员
USBKey。
注意:
l
SG-6000-A2000-GM/A3000-GM的USBKey初始PIN口令为12345678。
l
SG-6000-K5680-A-GM/K2680-A-GM/K2380-A-GM的USBKey初始PIN口令为
1234567812345678。
l
SG-6000-K5680-A-GM/K2680-A-GM/K2380-A-GM激活密码卡时，连续输错8次PIN码将
导致USBKey被锁定。如有其他未被锁定的USBKey，可用其重新激活密码卡。若4个USBKey
均被锁定，则设备需返送厂家解锁。
l
激活成功后，拔出USBKey不影响功能正常使用。
l
插入下一个USBKey前，请先拔出上一个USBKey。密码卡管理中的所有功能如有涉及插入
USBKey的操作，均要遵循该原则进行。
l
设备重启后，国密卡为未激活状态，系统会自动执行国密算法开机自检，并记录“SM1算法自
检失败”事件日志，同时向用户发出“尽快主动激活国密卡”的提示。用户需在设备重启后重
新激活国密卡，以确保其恢复正常工作状态；若未及时激活，将导致配置了SM1算法的业务功
能（如IPSec等）无法正常使用。
激活密码卡，在密码卡配置模式下，使用以下命令：
crypto-card enable
根据系统提示，在设备USB接口上依次插入1个操作员USBKey或2个管理员USBKey并输入相应的PIN口令
来激活密码卡。
取消激活密码卡
取消激活密码卡，在密码卡配置模式下，使用以下命令：
crypto-card disable
在“Are you sure to deactivate the cryptographic card ？[Y/N]”后输入字母Y，并按回车键，即可
取消激活密码卡。

<!-- 来源页 817 -->
算法即时自检
系统支持对国密系列算法的可用性进行即时检测，包括SM1、SM2、SM3、SM4、随机数算法。对于SG-
6000-K5680-A-GM/K2680-A-GM/K2380-A-GM设备，若国密卡未激活，则SM1算法不可用，即检测失
败。
进行算法即时自检，在密码卡配置模式下，使用以下命令：
crypto-card self-check
算法周期性自检
除即时自检外，系统还支持对国密系列算法进行周期性检测并配置检测时间间隔。默认情况下，算法周期性
自检功能为关闭状态。
开启算法周期性自检功能
开启算法周期性自检功能，在密码卡配置模式下，使用以下命令：
random-self-check enable
在密码卡配置模式下，使用no random-self-check enable命令关闭算法周期性自检功能。
配置算法周期性自检时间间隔
配置算法自检时间间隔，在密码卡配置模式下，使用以下命令：
random-self-check interval times
l
times – 指定算法周期性自检的时间间隔。取值范围为1到600，单位为分钟。默认值为600分钟。
在密码卡配置模式下，使用no random-self-check interval命令恢复默认值。
备份密钥信息
对于SG-6000-A2000-GM及SG-6000-A3000-GM设备，用户可使用3个管理员USBKey来备份密码卡的密
钥信息。
对于SG-6000-K5680-A-GM/K2680-A-GM/K2380-A-GM设备，用户可通过输入8个任意字符的口令来备
份密码卡的密钥信息。
备份密钥信息，在密码卡配置模式下，使用以下命令：
crypto-card backup

<!-- 来源页 818 -->
l
SG-6000-A2000-GM及SG-6000-A3000-GM设备：根据系统提示，在设备USB接口上依次插入3个管
理员USBKey并输入对应的PIN口令，按回车键，即可成功备份密钥信息。
l
SG-6000-K5680-A-GM/K2680-A-GM/K2380-A-GM设备：根据系统提示，输入8个任意字符的口
令，按回车键，即可成功备份密钥信息。
恢复密钥信息
对于SG-6000-A2000-GM及SG-6000-A3000-GM设备，密钥备份成功并生成密钥文件后，如需恢复密钥
信息，可以使用2个管理员USBKey来恢复密码卡的密钥信息。
对于SG-6000-K5680-A-GM/K2680-A-GM/K2380-A-GM设备，密钥备份成功并生成密钥文件后，如需
恢复密钥信息，必须输入与备份时相同的口令才能成功恢复。
恢复密钥信息，在密码卡配置模式下，使用以下命令：
crypto-card restore
l
SG-6000-A2000-GM及SG-6000-A3000-GM设备：根据系统提示，在设备USB接口上依次插入2个管
理员USBKey并输入对应的PIN口令，按回车键，即可成功恢复密钥信息。
l
SG-6000-K5680-A-GM/K2680-A-GM/K2380-A-GM设备：根据系统提示，输入备份密钥信息时填
写的口令，按回车键，即可成功恢复密钥信息。
注意: “备份密钥信息”和“恢复密钥信息”功能仅当用户通过管理员USBKey激活密码卡后支持
配置。
修改PIN口令
系统支持修改当前设备中插入的USBKey的PIN口令。
修改口令，在密码卡配置模式下，使用以下命令：
crypto-card change
根据系统提示，依次输入旧口令、新口令以及确认新口令，并按回车键，即可成功修改PIN口令。
注意: SG-6000-A2000-GM及SG-6000-A3000-GM设备PIN口令长度必须为8个字符；SG-
6000-K5680-A-GM/K2680-A-GM/K2380-A-GM设备PIN口令长度必须为16个字符。

<!-- 来源页 819 -->
重置PIN口令
系统支持将当前设备中插入的USBKey的PIN口令重置为初始口令。
重置口令，在密码卡配置模式下，使用以下命令：
crypto-card reset
根据系统提示，输入当前该USBKey的PIN口令，并按回车键，即可成功重置PIN口令。
查看密码卡状态
系统支持查看密码卡的状态，包括密码卡在线状态和激活状态。
查看密码卡状态，有以下两种方式：
方式一：在任意模式下，使用show pki crypto-card命令。
以下是返回结果示例：
hostname#show pki crypto-card
===============================================================
=============
Item Info
----------------------------------------------------------------------------
hardware online（密码卡在线）
permission operator（仅使用操作员USBKey激活密码卡）
===============================================================
=============
状态说明如下表：
字段
状态
说明
hardware
online
密码卡在线
offline
密码卡离线
permission
administrator
仅使用管理员USBKey激活密码卡
operator
仅使用操作员USBKey激活密码卡
administrator & operator
使用管理员USBKey和操作员USBKey激
活密码卡
NULL
密码卡未激活
方式二：在任意模式下，使用show version命令。

<!-- 来源页 820 -->
以下是返回结果示例：
hostname#show version
Hillstone Networks StoneOS software, Version 5.5
Copyright (c) 2009-2023 by Hillstone Networks
......
cryptographic card status: online（operator activated）（密码卡在线，仅使用操作员
USBKey激活密码卡）
......
状态说明如下表：
字段
密码卡状态
说明
cryptographic
card status
offline
离线
online（administrator activated）
在线（管理员已激活）
online（operator activated）
在线（操作员已激活）
online（administrator and
operator activated）
在线（管理员、操作员已激活）
online（unactivated）
在线（未激活）

<!-- 来源页 821 -->
同步系统固件
型号说明：X系列设备、SG-6000-K9180/K20803支持该功能。
当为设备配置两个主控模块时，需要将系统固件从主用主控模块同步到备用主控模块。默认情况下，系统启
动时会自动进行同步。如果自动同步出现问题（如启动备用主控模块失败），在执行模式下，使用以下命令
手动同步系统固件：
exec image sync

<!-- 来源页 822 -->
简单网络管理协议（SNMP）
简单网络管理协议（SNMP，Simple Network Management Protocol）是应用层协议，它通过标准框
架、公共语言和相对应的安全机制来监控和管理网络设备。SNMP的体系结构包括网络管理平台、SNMP代
理、网络管理协议和管理信息库（MIB，Management Information Base）四部分。
l 网络管理平台：是一个通过网络管理软件（如adventnet、solarwinds等）向SNMP代理发出Get和Set报文并接
收代理的应答，以达到管理和监控网络设备目的的系统。
l SNMP代理：是运行在被管理网络设备上的一个软件模块，用来维护被管理设备的信息数据并在需要时把管理数
据发送给网络管理平台。
l 网络管理协议：网络管理平台和SNMP代理之间是通过网络管理协议连接的，通过SNMP报文的形式来交换信
息。协议主要支持Get、Set和Trap三种功能，Get用于管理平台获取代理的MIB对象值，Set用于管理平台去设置
代理的MIB对象值，Trap用于代理向管理平台通告重要事件。
l 管理信息库（MIB）：是由SNMP代理维护的有关网络设备的信息数据库，信息库里的内容可供网络管理平台查
询或设置其中变量的值。
相关链接：
SNMP在CLI的配置包含：
l "Hillstone设备的SNMP功能" 在第820页
l "配置SNMP" 在第822页
l "SNMP配置示例" 在第831页
Hillstone设备的SNMP功能
Hillstone设备拥有SNMP代理功能，该SNMP代理功能能够接受网络管理平台的操作请求并反馈网络和设备
的相应信息。下图为SNMP管理框架在Hillstone设备中实现的示意图：

<!-- 来源页 823 -->
SNMP版本
Hillstone设备支持以下版本的SNMP：
l SNMPv1协议，具体描述请参阅RFC-1157，A Simple Network Management Protocol。
l SNMPv2协议，具体描述请参阅RFC-1901，Introduction to Community-based SNMPv2；RFC-1905，
Protocol Operations for Version 2 of the Simple Network Management Protocol；RFC-1906，Transport
Mappings for Version 2 of the Simple Network Management Protocol。
l SNMPv3协议，具体描述请参阅RFC2263，SNMPv3 Applications；RFC2264，User-based Security Model
(USM) for version 3 of the Simple Network Management Protocol (SNMPv3)；RFC2265，View-based
Access Control Model (VACM) for the Simple Network Management Protocol (SNMP)。
SNMPv1和SNMPv2c都使用了团体字的认证方式，可以限制网络管理平台获取设备信息。SNMPv3引入了
基于用户的安全模型用于保证消息安全及基于视图的访问控制模型用于访问控制。
MIB信息库
Hillstone设备支持RFC-1213中定义的管理信息库组相关MIB（Management Information Base for
Network Management of TCP/IP-based Internets: MIB-II）、RFC-2233中定义的使用SMIv2的接口
组MIB（The Interfaces Group MIB using SMIv2：IF-MIB）、RFC-2574中定义的SNMPv3安全模块相
关MIB（User-based Security Model：USM）以及RFC-2575中定义的SNMPv3用户访问控制模块相关
MIB（View-based Access Control Model：VACM）。此外，StoneOS提供一个私有MIB库，MIB库中
包含Hillstone设备的系统信息、IPSec VPN信息以及系统统计信息，用户可以将其导入到管理主机的MIB浏
览器，进行使用。

<!-- 来源页 824 -->
Trap报文信息
Hillstone设备的SNMP代理功能在设备发生异常情况时，会主动向网络管理平台发送Trap报文报告所发生
的事件。Hillstone设备的SNMP代理可以生成以下各种trap信息：
l 热启动trap
l SNMP验证失败trap
l 端口状态改变trap
l VPN SA协商状态改变trap
l HA状态改变trap
l 系统状态改变trap，如CPU使用率超过80%的trap、风扇状态改变trap、内存过低trap等
l 网络攻击trap，如ARP欺骗攻击trap、IP地址欺骗攻击trap、SYN Flood攻击trap等
l 配置改变trap
配置SNMP
Hillstone设备的SNMP的配置包括以下各项：
l 开启或者关闭SNMP代理功能
l 配置SNMP代理设备端口号
l 配置SNMP引擎ID
l 创建SNMPv3用户组
l 创建SNMPv3用户
l 配置管理主机地址
l 配置trap报文目标主机地址
l 配置管理员的标识及联系方法
l 配置Hillstone设备位置
l 指定启用SNMP功能的虚拟路由器
l 配置SNMP服务器
l 清除SNMP服务器的ARP表项信息
l 显示SNMP信息
l 显示SNMP服务器信息
l 开启或者关闭SNMP OID统计功能

<!-- 来源页 825 -->
l 显示SNMP OID统计信息
l 清除SNMP OID统计信息
l 导出SNMP MIB文件
开启或者关闭SNMP代理功能
默认情况下，系统的SNMP代理功能是关闭的。开启Hillstone设备的SNMP代理功能，请在全局配置模式下
使用以下命令。用该命令no的形式关闭SNMP代理功能。
l
snmp-server manager
l
no snmp-server manager
配置SNMP代理设备端口号
配置SNMP代理设备端口号，在全局配置模式下，使用以下命令：
snmp-server port port-number
l
port-number – 指定SNMP代理设备的端口号。范围为1到65535。默认值为161。
配置SNMP引擎ID
SNMP引擎ID唯一标识一个引擎，SNMP引擎是SNMP实体（网络管理平台或者被管理网络设备）的重要组
成部分，完成SNMP消息的收发、验证、提取PDU、组装消息与SNMP应用程序通信等功能。配置本地设备
的SNMP引擎ID，在全局配置模式下使用以下命令：
snmp-server engineID string
l
string – 指定引擎ID号。取值范围为1到23个字符。
创建SNMPv3用户组
配置SNMPv3用户组，请在全局配置模式下使用以下命令：
snmp-server group group-name v3 {noauth | auth | auth-enc} [read-view {mib2 | privmib |
vacm | usm}] [write-view usm]
l
group-name – 指定用户组的名称。取值范围为1到31个字符。
l
noauth | auth | auth-enc – 指定用户组的安全级别。可以为noAuth、Auth或者Auth-Enc。安全级
别决定了在处理一个SNMP数据包时所采用的安全机制。noAuth即无认证和加密；Auth提供基于MD5
或SHA算法的认证；Auth-Enc提供基于MD5或SHA算法的认证和基于AES和DES的报文加密。

<!-- 来源页 826 -->
l
read-view {mib2 | privmib | vacm | usm} – 指定该用户组的可读MIB视图名，用户组能够对指定的
MIB进行读操作，包括RFC-1213以及RFC-2233中定义的公有MIB（mib2）、山石网科的私有MIB库
（privmib）、RFC-2574中定义的SNMPv3安全模块相关MIB（usm）以及RFC-2575中定义的
SNMPv3用户访问控制模块相关MIB（vacm）。如不指定该参数，默认能够对所有MIB进行读操作。
l
write-view usm –指定该用户组的可写MIB视图名，用户组能够对指定的MIB进行写操作，包括RFC-
2574中定义的SNMPv3安全模块相关MIB（usm）。如不指定该参数，默认能够对所有MIB（USM
MIB）进行写操作。
系统最多允许配置5个用户组，且每个用户组最多可包含5个用户。在全局配置模式下使用no snmp-server
group group-name命令删除指定的用户组。
创建SNMPv3用户
配置SNMPv3用户，请在全局配置模式下使用以下命令：
snmp-server user user-name group group-name v3 remote A.B.C.D/M [auth-protocol {md5 |
sha } auth-pass [enc-protocol {des | aes } enc-pass]]
l
user user-name – 指定用户名称。取值范围为1到31个字符。
l
group group-name – 为所创建的用户指定已经配置好的用户组。
l
remote A.B.C.D/M – 指定远程管理主机的IP地址以及掩码。
l
auth-protocol {md5 | sha } – 指定用户安全级别为需要认证且认证协议可以为MD5、SHA算法。如
不输入此参数，则默认是无认证，无加密模式。
l
auth-pass – 指定认证密码。取值范围为8到40个字符。
l
enc-protocol {des | aes } – 指定用户安全级别为加密且加密协议为DES、AES。
l
enc-pass – 指定加密密码。取值范围为8到40个字符。
系统最多允许配置25个用户。在全局配置模式下使用no snmp-server user user-name命令删除指定的
用户。
配置管理主机地址
配置管理主机地址，请在全局配置模式下使用以下命令：
snmp-server host { ip-address | ip-address/mask | range start-ip end-ip} {version [1 | 2c]
community string [ro | rw] | version 3}

<!-- 来源页 827 -->
l
ip-address | ip-address/mask | range start-ip end-ip – 指定管理主机的IP地址或IP地址范围。
l
version [1 | 2c] – 指定SNMP的版本为SNMPv1或者SNMPv2C。
l
community string –团体字是管理进程和代理进程之间的口令，因此与设备认可的团体字不符的SNMP
报文将被丢弃。该参数指定主机的团体字，取值范围为一个最多31位的字符串，且仅当SNMP为v1和
v2C版本时有效。
l
ro | rw – 指定该团体字的读写权限。ro为只读，此类团体字只可读取MIB中的信息；rw为可读可写，此
类团体字不仅可以读取MIB中的信息，还可以对信息进行修改。此项为可选，默认情况下，团体字的访问
权限为只读。
l
version 3 –指定SNMP的版本为SNMPv3。
全局配置模式下使用no snmp-server host {host-name | ip-address | ip-address/mask | range
start-ip end-ip}命令删除指定的管理主机。
配置trap报文目标主机地址
用户可以配置接收SNMP trap报文的主机。配置SNMP trap报文目标主机地址，请在全局配置模式下使用
以下命令：
snmp-server trap-host host-ip [source-ip ip-address] {version {1 | 2c } community string |
version 3 user user-name engineID string } [port port-number]
l
host-ip - 指定接收trap报文目标主机的IP地址。
l
source-ip ip-address – 指定发送trap报文的源地址。
l
port port-number – 指定接收trap报文的目标主机端口号。取值范围为1到65535，默认值为162。
l
version {1 | 2c} – 指定使用SNMPv1或者SNMPv2C发送trap报文。
l
community string – 指定SNMPv1或者SNMPv2C的团体字。
l
version 3 – 指定使用SNMPv3发送trap报文。
l
user string – 指定已配置的SNMPv3用户名。
l
engineID string – 指定trap报文目标主机的引擎ID号。
l
port port-number – 指定接收trap报文的目标主机端口号。取值范围为1到65535，默认值为162。
在全局配置模式下使用no snmp-server trap-host host-ip [source-ip]命令删除指定的trap报文目标主
机。

<!-- 来源页 828 -->
注意: 在HA环境中，主设备上配置的发送Trap报文的源IP地址（source-ip）不会同步到备设
备，用户可以在备设备中使用snmp-server trap-host host-ip source-ip ip-address命令，
为已添加的Trap主机指定发送Trap报文的源IP地址。
配置管理员的标识及联系方法
sysContact即系统联络，是MIB II中系统组的一个管理变量，内容为被管理设备（此处为Hillstone设备）
相关人员的标识及联系方法。用户可以通过配置此参数，将重要信息存储在Hillstone设备中，以便出现紧
急问题时查询使用。配置管理员的标识及联系方法，请在全局配置模式下使用以下命令：
snmp-server contact string
l
string – 描述系统联络信息的字符串。取值范围为1到255个字符。
在全局配置模式下使用no snmp-server contact命令该系统联系信息。
配置Hillstone设备位置
sysLocation是MIB中系统组的一个管理变量，用于表示被管理设备（此处为Hillstone设备）的位置。指定
Hillstone设备的位置，请在全局配置模式下使用以下命令：
snmp-server location string
l
string – 描述Hillstone设备位置的字符串。取值范围为1到255个字符。
在全局配置模式下使用no snmp-server location命令删除系统位置信息。
指定启用SNMP功能的VRouter
用户可以指定启用SNMP功能的VRouter。指定启用SNMP功能的VRouter，请在全局配置模式下使用以下
命令：
snmp-server vrouter vrouter-name
l
vrouter-name –指定VRouter的名称。
在全局配置模式下使用no snmp-server vrouter命令关闭指定VRouter的SNMP功能。
配置SNMP服务器
用户可以配置SNMP服务器，从而通过SNMP协议来获取相关的ARP信息。
配置SNMP服务器，在全局配置模式下，使用以下命令：
arp-mib-query server ip-address community string [vrouter vrouter-name ] [source
interface-name ] [ port port-number ] [interval value]

<!-- 来源页 829 -->
l
ip-address – 指定SNMP服务器的IP地址。
l
community string – 指定SNMPv1或者SNMPv2C的团体字，取值范围为一个最多31位的字符串。
l
vrouter vrouter-name – 指定VRouter的名称。
l
source interface-name – 指定连接SNMP服务器的源接口。防火墙会通过指定接口收发SNMP消息。
l
port port-number – 指定SNMP服务器的端口号。范围为1到65535。默认值为161。
l
interval value – 指定防火墙向SNMP服务器发送请求消息的间隔时间。防火墙会定期向SNMP服务器
发送请求消息，获取相关的ARP信息。在文本框中输入间隔时间，取值范围为5到1800秒，默认为60
秒。
在全局配置模式下使用no arp-mib-query server ip-address命令删除指定的SNMP服务器。
清除SNMP服务器的ARP表项信息
用户可以在任何模式下通过以下命令清除SNMP服务器的ARP表项信息：
clear arp-mib-query
显示SNMP信息
用户可以在任何模式下通过以下命令查看SNMP的相关配置信息：
l
显示Hillstone设备的SNMP配置信息：show snmp-server
l
显示Hillstone设备的SNMPv3用户组信息：show snmp-group
l
显示Hillstone设备的SNMPv3用户信息：show snmp-user
显示SNMP服务器信息
用户可以在任何模式下通过以下命令查看SNMP服务器的相关信息：
l
显示SNMP服务器状态信息：show arp-mib-query status
l
显示SNMP服务器的ARP表项信息：show arp-mib-query table [ip-address]
l
显示SNMP服务器配置信息：show configuration arp-mib-query
进入SNMP代理配置模式
进入SNMP代理配置模式，在全局配置模式下使用以下命令：
snmp-agent

<!-- 来源页 830 -->
开启或者关闭SNMP OID统计功能
OID（对象标识符）是SNMP代理提供的具有唯一标识的键值，一般用一串数字表示，例
如：.1.3.6.1.4.1.28557.2.2.1.32。SNMP协议将设备的各类参数按树形结构进行分组，从树的根部开
始，每一层级节点对应一个编码，并将各层级编码用小数点（.）分隔，然后将层级编码拼接后形成的一串编
码称为OID（对象标识符）。
SNMP OID统计功能通过统计SNMP代理OID的基本信息，有效帮助用户快速定位SNMP问题。系统提供3种
SNMP OID统计功能，分别为：OID的基本信息统计功能、基于监控IP所有OID的详细信息统计功能、以及
最近所有监控IP对应的OID详细信息统计功能，用户可以同时开启这3种SNMP OID统计功能。
默认情况下，系统的SNMP OID统计功能是关闭的。开启指定SNMP OID统计功能，请在SNMP代理配置模
式下使用以下命令：
snmp-agent statistics {generic | monitor-ip | recently}
l
generic - 开启OID的基本信息统计功能。
l
monitor-ip - 开启基于监控IP所有OID的详细信息统计功能。
l
recently - 开启最近所有监控IP对应的OID详细信息统计功能。
在SNMP代理配置模式下，使用以下命令，关闭指定SNMP OID统计功能：
no snmp-agent statistics [generic | monitor-ip | recently]
l
generic - 关闭OID的基本信息统计功能。
l
monitor-ip - 关闭基于监控IP所有OID进行详细信息统计功能。
l
recently - 关闭最近所有监控IP对应的OID详细信息统计功能。
l
若不指定generic | monitor-ip | recently参数，则关闭全部SNMP OID统计功能。
显示SNMP OID统计信息
当OID的基本信息统计功能开启后，用户可以在任何模式下，使用以下命令，查看所有OID和指定OID的基本
统计信息：
l
查看所有OID的基本统计信息：show snmp-agent statistics generic
例如：
hostname# show snmp-agent statistics generic
10.160.25.181
==================================================
Messages delivered to the SNMP entity 3 ( 表示SNMP实体传递了3次消息)

<!-- 来源页 831 -->
SNMP PDUs which had noError 3 ( 表示SNMP PDUs总共有3次未出错的操作)
GetRequest-PDU accepted and processed 0 ( 表示Get请求次数为0，GetRequest-PDU
表示SNMP PDU的操作名称，0表示操作的次数)
GetNextRequest-PDU accepted and processed 0 ( 表示Get Next请求次数为0)
GetBulkRequest-PDU accepted and processed 0 ( 表示Get Bulk请求次数为0)
Set-PDU accepted and processed 0 ( 表示Set次数为0)
Trap-PDU sent 0 ( 表示Trap版本1发送了0次)
Trap2-PDU sent 3 ( 表示Trap版本2发送了3次)
查看指定OID的基本统计信息：show snmp-agent statistics oid oid-string generic
o oid-string - 指定需要查看的OID字符串的值，字符串长度的取值范围是2到256。例
如：.1.3.6.1.4.1.28557.2.2.1.32。
例如：
hostname# show snmp-agent statistics oid .1.3.6.1.4.1.28557.3.19 generic
.1.3.6.1.4.1.28557.3.19
===================================================
Messages delivered to the SNMP entity 4 ( 表示SNMP实体传递了4次消息)
SNMP PDUs which had noError 4 ( 表示SNMP PDUs总共有4次未出错的操作)
当基于监控IP所有OID的详细信息统计功能开启后，用户可以在任何模式下，使用以下命令，查看指定监控
IP下所有OID的详细统计信息：
show snmp-agent statistics ip ip-address
l ip-address - 指定需要查看的目标IP地址。该IP地址需通过Tab键联想得到，联想后的IP地址至少经过1次SNMP
基本操作，如Set、Get等。如果用户输入任意的IP地址，则出现“该IP无法识别”的错误。
例如：
hostname# show snmp-agent statistics ip ?
10.160.25.181 SNMP detail statistics monitor-ip ( 显示连接过设备的SNMP服务器
的IP地址)
10.160.28.169 SNMP detail statistics monitor-ip
hostname# show snmp-agent statistics ip 10.160.28.169
OID Type Time(ms) Result

<!-- 来源页 832 -->
( 对象标识符
类型
时间
结果)
===================================================
.1.3.6.1.4.1.28557.2.26.1.2.1.5.4 getnext 0 NOERROR
.1.3.6.1.4.1.28557.2.26.1.2.1.5.4 getnext 0 NOERROR
.1.3.6.1.4.1.28557.2.27.1.1.0 getnext 0 NOERROR
.1.3.6.1.4.1.28557.2.27.1.1.0 getnext 0 NOERROR
.1.3.6.1.4.1.28557.2.27.1.1.0 getnext 0 NOERROR
当最近所有监控IP对应的OID详细信息统计功能开启后，用户可以在任何模式下，使用以下命令，查看最近
所有监控IP对应的OID的详细信息：
show snmp-agent statistics recently-detail
例如：
hostname# show snmp-agent statistics recently-detail
OID ADDR Type Time(ms) Result
( 对象标识符
监控IP 类型
时间( 毫秒)
结果)
=====================================================
.1.3.6.1.4.1.28557.2.2.1.4.0 10.160.28.169 getnext 18 NOERROR
.1.3.6.1.4.1.28557.2.2.1.4.0 10.160.28.169 getnext 0 NOERROR
.1.3.6.1.4.1.28557.2.2.1.6.0 10.160.28.169 getnext 0 NOERROR
.1.3.6.1.4.1.28557.2.2.1.7.0 10.160.28.169 getnext 18 NOERROR
用户可以在任何模式下，使用以下命令，查看SNMP OID的统计状态：
show snmp-agent statistics status
例如：
hostname# show snmp-agent statistics status
SNMP generic statistics is off ( OID的基本信息统计功能已关闭)
SNMP detail recently statistics is off ( 基于监控IP所有OID的详细信息统计功能已
关闭)
SNMP detail monitor-ip statistics is on ( 最近所有监控IP对应的OID的详细信息统
计功能已开启)

<!-- 来源页 833 -->
清除SNMP OID统计信息
用户可以在任何模式下，使用以下命令，清除SNMP OID的全部统计信息：
clear snmp-agent statistics
导出SNMP MIB文件
导出SNMP MIB文件到FTP/FTPS/SFTP服务器，在执行模式使用以下命令：
export snmp mib to {ftp | ftps | sftp} server ip-address [vrouter vrouter-name] [user username password password] [file-name]
l
ip-address - 指定FTP/FTPS/SFTP服务器的IP地址。
l
vrouter-name - 指定虚拟路由器的名称。
l
user user-name password password - 指定访问FTP/FTPS/SFTP服务器的用户名和密码。
l
file-name - 指定导出的SNMP MIB文件的名称。
导出SNMP MIB文件到TFTP服务器，在执行模式下使用以下命令：
export snmp mib to tftp server ip-address [vrouter vrouter-name] [file-name]
SNMP配置示例
为方便用户更好的理解和使用Hillstone设备的SNMP功能，本节介绍两个典型的SNMP配置示例。
组网要求
网络管理平台与Hillstone设备通过以太网相连，网络管理平台的IP地址为10.160.64.193，Hillstone设备
以太网口IP地址为10.160.64.194。请看以下示意图：
l 示例一：通过SNMPv2C实现IP地址为10.160.64.193的PC对Hillstone设备的管理，使用团体字public。另外，
允许向网络管理平台10.160.64.193发送trap报文，使用团体字private。
l 示例二：通过SNMPv3实现IP地址为10.160.64.193的PC对Hillstone设备的管理。安全级别为需要认证和加密，
指定认证协议为MD5、认证密码为password1，指定加密协议为DES、加密密码为password2。同时，PC只能
读取MIB-II信息库的内容并且只能对usm信息库的内容进行设置。另外，允许向Hillstone设备发送trap报文。

<!-- 来源页 834 -->
示例一配置步骤
第一步：配置Hillstone设备：
进入全局配置模式
hostname# configure
启动Hillstone设备接口的SNMP功能
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# manage snmp
启动SNMP功能
hostname(config)# snmp-server manager
配置团体字和访问权限
hostname(config)# snmp-server host 10.160.64.193 version 2c community public ro
配置管理员标识、联系方法以及Hillstone设备物理位置
hostname(config)# snmp-server contact cindy-Tel:218
hostname(config)# snmp-server location Hostname-Network
允许向网络管理平台10.160.64.193发送trap报文，使用的团体字为private
hostname(config)# snmp-server trap-host 10.160.64.193 version 2c community
private
第二步：配置网络管理平台。
示例二配置步骤
第一步：配置Hillstone设备：
进入全局配置模式
hostname# configure
启动Hillstone设备接口的SNMP功能
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# manage snmp
启动SNMP功能
hostname(config)# snmp-server manager
配置本地引擎ID

<!-- 来源页 835 -->
hostname(config)# snmp-server engineID hillstone
配置用户组，网络管理平台只能读取MIB-II信息库的内容并且可以对usm信息库的内容进
行设置
hostname(config)# snmp-server group group1 v3 auth-enc read-view mib2 writeview usm
配置用户，认证协议为MD5，密码为password1；加密协议为DES，密码为password2
hostname(config)# snmp-server user user1 group group1 v3 remote 10.160.64.193
auth md5 password1 enc des password2
配置管理主机地址
hostname(config)# snmp-server host 10.160.64.193 version 3
配置trap报文目标主机地址，允许向网络管理平台10.160.64.193发送trap报文
hostname(config)# snmp-server trap-host 10.160.64.193 version 3 user user1
engineID remote-engineid
配置管理员标识、联系方法以及Hillstone设备物理位置
hostname(config)# snmp-server contact cindy-Tel:218
hostname(config)# snmp-server location Hostname-Network
第二步：配置网络管理平台。

<!-- 来源页 836 -->
网络配置协议（NETCONF）
网络配置协议NETCONF（Network Configuration Protocol）提供一套管理网络设备的机制，用户可以
使用这套机制增加、修改和删除网络设备的配置，获取网络设备的配置和状态信息。通过NETCONF协议，
网络设备可以提供规范的应用编程接口API（Application Programming Interface），应用程序可直接
使用这些API，向网络设备发送和获取配置。
NETCONF与SNMP对比：
特性
SNMP
NETCONF
配置管理
SNMP在进行设备数据操作
时，SNMP没有锁定保护机
制。
NETCONF提供保护锁定机制，防止多用户操作产生冲突。
查询
SNMP能够对某个表的某个或
多个节点进行操作，查询需要
多次交互才能完成。
NETCONF可直接对整个系统的配置数据进行操作。
扩展性
扩展性差。
扩展性好。NETCONF采取分层定义，各层之间相互独立，当
对NETCONF中的某一层进行扩展时，能最大限度不影响到其
上层协议。NETCONF采用了XML编码，使得协议在管理能力
和系统兼容性方面也有一定的可扩展性。
安全性
以目前最新的SNMPv3为例，
SNMPv3全部自己定义，难以
扩展。
NETCONF利用现有的安全协议提供安全保证，不与具体的安
全协议绑定。在使用中，NETCONF比SNMP更灵活。
说明：NETCONF传输层首选SSH协议，XML信息通过SSH协
议承载。
用户通过NETCONF客户端，可以对Hillstone设备实现配置修改、获取配置及状态信息。用户可以通过
NETCONF客户端对以下功能模块进行配置：
l 对象模块：新建/删除/编辑地址簿和域名簿时，支持通过NETCONF进行配置。
l 网络模块：新建/删除/编辑安全域、接口、DNS服务器、DNS代理、DHCP、目的路由、源路由、策略路由、
OSPF、BGP、IPsec VPN和SSL VPN时，支持通过NETCONF进行配置。
l 策略模块：新建/删除/编辑策略、SNAT和DNAT时，支持通过NETCONF进行配置。
注意:
l
开启NETCONF功能时，需要设置系统管理员和可信主机的接入方式为NETCONF、接口的管理
方式为NETCONF。建议先设置这三项，再开启NETCONF代理服务。

<!-- 来源页 837 -->
l
当根VSYS已开启NETCONF功能，如果非根VSYS需要开启NETCONF功能，只需配置非根
VSYS的系统管理员的接入方式为NETCONF，即可开启。
配置NETCONF
开启/关闭NETCONF代理功能
默认情况下，系统的NETCONF代理功能是关闭的。
开启Hillstone设备的NETCONF代理功能，在全局配置模式下使用以下命令：
netconf-manager enable
在全局配置模式下，用该命令no的形式关闭NETCONF代理功能：
no netconf-manager enable
开启/关闭NETCONF candidate功能
当用户需要修改当前设备配置，但不想立即替换当前配置影响现行业务流量，可以开启NETCONF
candidate功能。用户可以修改candidate配置，用candidate配置替换当前设备配置，并即时生效。默认
情况下，系统的NETCONF candidate功能是关闭的。
开启NETCONF candidate功能，在全局配置模式下使用以下命令：
netconf-manager candidate
在全局配置模式下，用该命令no的形式关闭NETCONF candidate功能：
no netconf-manager candidate
配置NETCONF超时时间
NETCONF客户端用户对Hillstone设备进行下发配置等操作，如果NETCONF客户端用户在超时时间内未对
设备进行操作，则需重新登录进行后续操作。配置超时时间，在全局配置模式下，使用以下命令：
netconf-manager timeout value
l
value – 指定超时时间。单位为分钟，取值范围是5到30分钟。默认值是10分钟。
显示NETCONF代理配置
用户可以在任何模式下使用show命令查看设备上NETCONF代理的配置信息：
show netconf-manager

<!-- 来源页 838 -->
AI运维助手介绍
防火墙AI运维助手是一种集成了人工智能技术的智能工具，旨在提升网络安全运维的效率和效果。它能够利
用大模型服务平台，理解并解释复杂的网络安全数据，帮助运维人员快速识别和响应各种安全威胁、快速回
答运维人员的查询，提供产品使用和安全防护的指导。
山石AI运维助手，支持：
l 通用类知识问答：利用大模型丰富的知识库，解答用户咨询的通用性安全知识问题。如：防火墙是什么；防火墙
的工作原理是什么
l 山石网科防火墙产品的知识问答：集成山石网科防火墙产品的各类配置使用指南，解答用户提出的产品问题。包
括并不限于产品的硬件知识、WebUI功能的配置使用、CLI命令行的配置、典型配置案例指导、常规的故障排
查，以及常见问题及解答。如：SG-6000-A2700具备什么类型的接口；策略不生效怎么办；我应该如何实现对
用户流量的监控
l 威胁分析问答：协助用户了解系统所检测到的威胁和漏洞是什么含义。当防火墙扫描到某病毒时，AI运维助手借
助第三方专业平台查询相关的信息，结合大模型能力，解答用户对于威胁分析的疑问。如：CVE-2018-18778是
什么漏洞；上级通报防护漏洞CVE-2023-4863，做什么来防护这个漏洞
提示: 因系统软件与知识问答存在多个版本，且版本之间存在功能支持的差异。在使用AI运维助手
时，如果需要查询与当前系统版本不一致的问题，请提问时增加设备版本信息（如：在StoneOS
5.5R10P4版本中如何查看CPU利用率），以便能获取到准确的答案。
典型场景
AI运维助手支持多种使用场景，以下举例供参考：
l 设备初始上线配置
l 威胁日志运维分析
l 设备故障排查
配置AI运维助手
进入AI运维助手配置模式
进入AI运维助手配置模式，在全局配置模式下，使用以下命令：
ai-assistant

<!-- 来源页 839 -->
开启/关闭AI运维助手连接本地大模型服务平台
开启/关闭AI运维助手连接本地大模型服务平台，在AI运维助手配置模式下，使用以下命令：
l
开启：llm-server enable
l
关闭：no llm-server enable
开启/关闭AI运维助手连接山石云平台
开启/关闭AI运维助手连接山石云平台，在AI运维助手配置模式下，使用以下命令：
l
开启：cloud-server enable
l
关闭：no cloud-server enable
开启/关闭数据查询授权功能
开启数据查询授权功能，即代表授权同意大模型获取对设备存储的日志、事件、流量数据等关键信息的访问
权限。该功能默认为关闭状态。
开启/关闭数据查询授权功能，在AI运维助手配置模式下，使用以下命令：
l
开启：llm-access enable
l
关闭：no llm-access enable

<!-- 来源页 840 -->
连接安全管理平台（HSM）
Hillstone安全管理平台（Hillstone Security Management，简称HSM）为软硬件一体化的多设备安全
集中管理产品。该产品基于WEB2.0和RIA（Rich Internet Application）技术，支持可视化的策略配置管
理、设备状态监控、设备流量监控、设备安全事件监控以及设备实时告警功能；同时，为方便用户掌握设备
状态、分析网络情况，该产品提供丰富的报表功能以及设备日志审计功能。
HSM系统分为三部分，即HSM代理、HSM服务器和HSM客户端。将这三部分合理部署到网络中，并且实现
安全连接后，用户可以通过客户端程序，查看被管理安全设备的日志信息、统计信息、设备属性等，实时监
控被管理设备的运行状态和流量信息。
每台设备运行的系统都包含HSM代理模块，在设备上正确配置了HSM代理功能后，就可以实现设备与HSM
服务器的连接，进而实现服务器对设备的管理与控制。连接后，需要保持连接状态，如果断开连接超过一段
时间，所有的配置都不能下发。当设备与HSM服务器断开连接时，系统右上角的通知图标会新增SDWAN控
制器已断开连接的通知，点击通知图标，展开系统当前所有的通知信息，然后再点击<SDWAN控制器已断开
连接>后的“处理”，跳转至扩展服务页面重新连接HSM。
另外，防火墙还支持向HSM设备上送以下信息：
l 接口信息，包含接口延时、抖动、丢包率等等。
l 接口上的应用数据信息，包含应用的延时、抖动、上行丢包率、下行丢包率等等。
注意: 关于HSM的详细信息，请参阅《山石网科安全管理平台用户手册》。
HSM应用场景
HSM的主要应用场景有两种，分别是公网应用场景和内网应用场景。描述如下：
l 公网应用场景：HSM系统与被管理设备通过Internet相连，只要HSM系统与被管理设备之间具有可达路由，用户
就可以通过HSM系统对属于不同网段的设备进行管理，参见下图：

<!-- 来源页 841 -->
l 内网应用场景：HSM系统与被管理设备处于同一内网中，用户通过HSM系统对内网的不同设备进行管理，参见下
图：
连接HSM
开始之前
l 阅读"连接安全管理平台（HSM）" 在第838页介绍。
用户可以通过命令行接口（CLI）和Web界面（WebUI）两种方式为Hillstone安全设备配置HSM代理功
能。为实现设备与HSM的连接，用户需要在设备上启用HSM代理功能并配置HSM服务器的IP地址、连接端
口号等参数。连接HSM功能配置主要包括以下各项：
l 配置HSM服务器管理参数
l 指定信任域
l 更换数字证书
l 开启/关闭HSM代理功能
l 显示HSM代理配置
配置HSM服务器管理参数
为实现设备与HSM服务器的连接，使服务器能够对设备进行管理，用户需要在设备上配置服务器的IP地址、
连接端口号、设备注册模式、访问密码及启用HSM代理功能的VRouter、连接HSM服务器的源接口。
配置HSM服务器的IP地址
配置HSM服务器的IP地址，在全局配置模式下，使用以下命令：
network-manager host ip-address
l
ip-address – 指定HSM服务器的IP地址。此IP地址不能为“0.0.0.0”、“255.255.255.255”以及组
播地址。

<!-- 来源页 842 -->
配置HSM服务器的连接端口号
配置HSM服务器的连接端口号，在全局配置模式下，使用以下命令：
network-manager host port port-number
l
port-number – 指定HSM服务器的连接端口号。范围是1到65535。默认值是9091。
指定HSM服务器的设备注册模式
指定HSM服务器的设备注册模式为普通模式（即非加密模式），在全局配置模式下，使用以下命令：
network-manager host plain
在全局配置模式下，用该命令no的形式指定为加密模式：
no network-manager host plain
配置HSM服务器的访问密码
配置HSM服务器的访问密码，在全局配置模式下，使用以下命令：
network-manager host password password
l
password – 指定HSM服务器的访问密码。服务器通过该密码对设备进行认证。范围是1到31个字符。
配置启用HSM代理功能的VRouter
配置启用HSM代理功能的VRouter，在全局配置模式下，使用以下命令：
network-manager host vrouter vrouter-name
l
vrouter-name –指定VRouter的名称。
指定连接HSM服务器的源接口
指定连接HSM服务器的源接口，在全局配置模式下，使用以下命令：
network-manager host source interface-name
l
source interface-name – 指定连接HSM服务器的源接口。
取消对HSM服务器管理参数的配置
在全局配置模式下，使用以下命令取消对HSM服务器管理参数的配置：
no network-manager host

<!-- 来源页 843 -->
配置服务器的IP地址和端口号
为保证设备与HSM服务器在NAT环境下能够正常通信，系统支持用户在设备上配置FTP服务器、FTPS服务
器、HTTPS服务器和日志服务器的IP地址和端口号。默认情况下，FTP服务器、FTPS服务器、HTTPS服务器
的IP地址为HSM服务器的IP地址，端口号为21；日志服务器的IP地址为HSM服务器的IP地址，端口号为
514。
配置FTP服务器的IP地址和端口号
配置FTP服务器的IP地址和端口号，在全局配置模式下，使用以下命令：
network-manager host ftp-server ip-address [port port-number]
l
ip-address – 指定FTP服务器的IP地址。
l
port-number – 指定FTP服务器的端口号。
在全局配置模式下，使用以下命令恢复FTP服务器默认IP地址和端口号：
no network-manager host ftp-server [port]
配置FTPS服务器的IP地址和端口号
配置FTPS服务器的IP地址和端口号，实现数据的加密传输，在全局配置模式下，使用以下命令：
network-manager host ftps-serverip-address [portport-number]
l
ip-address – 指定FTPS服务器的IP地址。
l
port-number – 指定FTPS服务器的端口号。
在全局配置模式下，使用以下命令恢复FTPS服务器默认IP地址和端口号：
no network-manager host ftps-server [port]
配置HTTPS服务器的IP地址和端口号
配置HTTPS服务器的IP地址和端口号，实现数据的加密传输，在全局配置模式下，使用以下命令：
network-manager host https-server ip-address [https-port port-number]
l
ip-address – 指定HTTPS服务器的IP地址。
l
port-number – 指定HTTPS服务器的端口号。
在全局配置模式下，使用以下命令恢复HTTPS服务器默认IP地址和端口号：
no network-manager host https-server [https-port]

<!-- 来源页 844 -->
配置日志服务器的IP地址和端口号
配置日志服务器的IP地址和端口号，在全局配置模式下，使用以下命令：
network-manager host syslog-server ip-address [secure-tcp] [port port-number]
l
ip-address – 指定日志服务器的IP地址。
l
secure-tcp – 指定该参数后，安全设备和HSM服务器在日志传输时，日志信息将被加密传输。
l
port-number – 指定日志服务器的端口号。
在全局配置模式下，使用以下命令恢复日志服务器默认IP地址和端口号：
no network-manager host syslog-server [secure-tcp] [port]
更换数字证书
设备和HSM服务器进行连接时支持使用数字证书进行双向认证，双向认证通过后，设备和HSM服务器成功连
接。在系统中创建信任域存储CA证书，设备用该证书验证HSM服务器提供的证书；创建另一个信任域存储本
地证书和私钥，以便提供证书给HSM服务器进行认证。若没有配置本地证书和私钥，则设备连接HSM服务器
时只进行单向认证，即设备认证HSM服务器提供的证书。导入新的CA证书、本地证书以及私钥后，用户可以
更换数字证书。创建信任域、配置证书和私钥，请参阅PKI配置一节。
引用已有的信任域来获取新的CA证书，在全局配置模式下，使用以下命令：
network-manager host trust-domain trust-domain-name
l
trust-domain-name–指定系统中已有的存储了新的CA证书的信任域名称。若不配置该项，则使用默
认的内置CA证书。
引用已有的信任域来获取新的本地证书和私钥，在全局配置模式下，使用以下命令：
network-manager agent trust-domain trust-domain-name
l
trust-domain-name–指定系统中已有的存储了新的本地证书和私钥的信任域名称。若不配置该项，则
不提供本地证书和私钥给HSM服务器认证，只使用CA证书对HSM服务器单向认证。
注意: 当HSM服务器不支持双向认证时，设备向HSM服务器提供本地证书后，HSM服务器将默认
设备认证通过。
开启/关闭HSM代理功能
HSM服务器管理参数以及信任域配置完成以后，用户需要开启设备的HSM代理功能以实现设备与服务器的正
常连接。默认情况下，设备的HSM代理功能是关闭的，启用此功能，在全局配置模式下，使用以下命令：

<!-- 来源页 845 -->
network-manager enable
在全局配置模式下，用该命令no的形式关闭此功能：
no network-manager enable
显示HSM代理配置
用户可以在任何模式下使用show命令查看设备上HSM代理的配置信息：
show network-manager
查看从HSM同步的认证用户信息
用户可以查看从HSM同步的认证用户信息，包括用户名、IP、端口范围、服务器、在线时长等。
查看从HSM同步的认证用户信息，在任意模式下，使用以下命令：
l
查看系统控制层面的用户认证信息：show auth-user sso-hsm
l
查看系统数据层面的用户认证信息：show dp-auth-user sso-hsm
查看从HSM同步的用户映射信息
查看从HSM同步的用户和IP的映射信息，在任意模式下，使用以下命令：
show user-mapping user-sso sso-hsm default
踢出从HSM同步的认证用户
当防火墙和HSM失去连接并且没有自动删除从HSM同步的用户信息时，用户可以手动踢出用户并删除用户和
IP的映射信息。
踢出从HSM同步的用户映射信息，在任意模式下，使用以下命令：
exec user-mapping user-sso sso-hsm kickout {ip ip-address vrouter vrouter-name |
username user-name auth-server server-name}
l
ip ip-address vrouter vrouter-name - 踢出指定IP和虚拟路由器的用户。
l
username user-name auth-server server-name - 踢出指定用户名和认证服务器的用户。
开启/关闭从HSM同步认证用户的调试功能
开启从HSM同步认证用户的调试功能，在任意模式下，使用以下命令：
debug usersso hsm [basic | error | success]

<!-- 来源页 846 -->
l
basic - 开启从HSM同步认证用户的基本信息调试功能。
l
error - 开启从HSM同步认证用户的错误信息调试功能。
l
success - 开启从HSM同步认证用户的成功信息调试功能。
关闭从HSM同步认证用户的调试功能，在任意模式下，使用以下命令：
undebug usersso hsm [basic | error | success]

<!-- 来源页 847 -->
连接山石智铠统一终端安全管理系统（EDR）
连接山石智铠是系统用来连接山石网科的智铠统一终端安全管理系统（以下简称“智铠”）。
山石智铠统一终端安全管理系统（EDR），是面向政府、金融、医疗、教育、互联网等企事业单位推出的终
端管理、等保基线检查、漏洞扫描与修复、病毒威胁检测与响应、微隔离、安全接入的一体化安全防护方
案，在安全能力方面集成了病毒查杀、实时防护、行为事件检测与响应等功能，实现事前的运维管控和合规
检查，事中异常行为检测和病毒威胁防护，事后追踪溯源、响应处置和安全审计。
在设备上启用连接智铠统一终端安全管理平台，正确配置了智铠服务器的IP/域名、连接端口和虚拟路由器
后，就可以实现设备与智铠的连接，进而实现设备与智铠的数据交互和策略协同。注意确保防火墙设备与智
铠之间通信网络正常。连接后，智铠能够自动将其管理的终端信息同步至防火墙设备上，以便用户对终端设
备进行集中管理和监控。同时，结合智铠的安全能力，用户可通过终端标签安全策略实现动态权限控制，进
一步提升整体安全防护能力。
注意:
l
关于智铠的详细信息，请参阅《山石网科智铠统一终端安全管理系统WebUI手册》。
l
非根VSYS不支持连接智铠统一终端安全管理平台。
智铠系统构成
在系统构成方面，智铠主要由管理中心和终端探针两部分组成：
l 管理中心（Controller）：作为智铠的核心大脑，以软件形态部署在虚拟环境、裸金属服务器、云平台和国产化
服务器版操作系统中，实现对终端探针的全面集中管控。其功能涵盖终端资产管理、实时防护、病毒查杀、外设
管控、弱密码检测、微隔离、漏洞管理、数据检索、行为事件检测、响应处置及安全运维等。
l 终端探针（Agent）：作为守护每一台终端的安全软件，部署在受保护的终端上，与管理中心进行交互，实现安
全防护。终端探针可以安装在主流Windows操作系统、Linux操作系统、macOS操作系统以及国产化操作系统
终端中。
注意: 关于智铠的部署信息，请参阅《山石网科智铠统一终端安全管理系统部署手册》。
连接智铠（EDR）
开始之前
l 阅读"连接山石智铠统一终端安全管理系统（EDR）" 在第845页介绍。

<!-- 来源页 848 -->
用户可以通过命令行接口（CLI）和Web界面（WebUI）两种方式连接智铠（EDR）平台。为实现设备与智
铠（EDR）平台的连接，用户需要在设备上启用连接智铠（EDR）功能并配置智铠服务器的IP地址、
VRouter、连接端口号等参数。
连接智铠（EDR）功能的配置流程如下：
1. 进入EDR Server配置模式
2. 配置智铠（EDR）连接参数
3. 启用连接智铠（EDR）功能
4. 查看连接智铠（EDR）平台配置
进入EDR Server配置模式
进入EDR Server配置模式，在全局配置模式下，使用以下命令：
edr server
配置智铠（EDR）连接参数
为实现设备与智铠服务器的连接，用户还需要在设备上配置智铠服务器的IP地址、连接端口号等参数。
配置智铠服务器的IP地址
配置智铠服务器的IP地址，在EDR Server配置模式下，使用以下命令：
address {A.B.C.D | domain}
l
A.B.C.D | domain – 指定智铠服务器的IPv4地址或域名。
在EDR Server配置模式下，使用以下命令，删除智铠服务器的IPv4地址或域名配置：
no address
配置智铠服务器的连接端口号
配置智铠服务器的连接端口号，在EDR Server配置模式下，使用以下命令：
port port-number
l
port-number – 指定智铠服务器的连接端口号。范围是1到65535。默认值是7443。
在EDR Server配置模式下，使用以下命令，恢复默认值：
no port
指定连接智铠服务器的VRouter
指定连接智铠服务器的VRouter，在EDR Server配置模式下，使用以下命令：

<!-- 来源页 849 -->
vrouter vrouter-name
l
vrouter-name –指定VRouter的名称，默认为trust-vr。
在EDR Server配置模式下，使用以下命令，恢复默认值：
no vrouter
指定连接智铠服务器的源接口
指定连接智铠服务器的源接口，在EDR Server配置模式下，使用以下命令：
interface interface-name
l
interface-name – 指定连接智铠服务器的源接口。
在EDR Server配置模式下，使用以下命令，删除源接口配置：
no interface
启用连接智铠（EDR）功能
开启连接智铠（EDR）平台功能，在EDR Server配置模式下，使用以下命令：
connection enable
在EDR Serve配置模式下，使用该命令no的形式关闭此功能：
no connection enable
更换数字证书
设备和智铠（EDR）服务器连接时需要使用数字证书进行双向认证，双向认证通过后，设备和智铠服务器成
功连接。在系统中创建信任域存储CA证书，设备用该证书验证智铠服务器提供的证书；创建另一个信任域存
储本地证书和私钥，以便提供证书给智铠服务器进行认证。导入新的CA证书、本地证书以及私钥后，用户可
以更换数字证书。创建信任域、配置证书和私钥，请参阅PKI配置一节。
引用已有的信任域来获取新的CA证书，在EDR Server配置模式下，使用以下命令：
server-trust-domain trust-domain-name
l
trust-domain-name - 指定系统中已有的存储了新的CA证书的信任域名称。若不配置该项，则使用默
认的内置CA证书。
引用已有的信任域来获取新的本地证书和私钥，在EDR Server配置模式下，使用以下命令：
agent-trust-domain trust-domain-name

<!-- 来源页 850 -->
l
trust-domain-name - 指定系统中已有的存储了新的本地证书和私钥的信任域名称。若不配置该项，
则使用默认的本地证书和私钥。
查看连接智铠（EDR）平台配置
用户可以在任何模式下使用show命令查看设备上HSM代理的配置信息：
show edr server
示例：
hostname(config-edr-server)# show edr server
=======================================================================
server: 10.11.10.1（显示智铠服务器的IP地址或域名）
server port: 7443（显示智铠服务器的连接端口号）
vrouter: trust-vr（显示连接智铠服务器的虚拟路由器）
interface: ethernet0/2（显示连接智铠服务器的源接口）
connection: enable（显示连接智铠平台功能已开启）
status: online（显示设备与智铠的连接状态）
agent trust-domain: （显示存储本地证书和私钥的信任域名称）
server trust-domain: （显示存储CA证书的信任域名称）
connection time: 2025/02/17 15:00:14（显示该设备与智铠平台上一次建立通信连接的时间）
connection duration: 0 days 6 hours 0 minutes 6 seconds（显示该设备与智铠平台成功建立通信
连接的时长）
=======================================================================

<!-- 来源页 851 -->
连接安全运营平台（智源）
连接安全运营平台是系统用来连接山石网科的智源智能安全运营管理系统。
智源智能安全运营管理系统，是全息数据驱动的AI分析运营系统，由分析平台与丰富的探针共同构成，可为
各行业客户提供网络威胁分析、态势呈现与溯源等功能，解决客户监控盲区，潜在安全隐患、运维低效等问
题。智源具备全息数据采集的能力，通过多种类型的数据探针采集数据，基于海量网络流量、威胁事件和终
端日志等进行智能数据挖掘及分析，呈现全局网络安全及威胁态势，并支持多维度投屏展示、联动响应、工
单响应等核心功能，让企业安全运营尽在掌握之中。
在设备上启用连接安全运营平台，正确配置了智源的IP/域名、端口和虚拟路由器后，就可以实现设备与智源
的连接，进而实现智源对设备信息的接收和进一步分析。防火墙设备作为网络设备与智源连接后，支持将威
胁日志及证据报文上送至智源进行分析。
注意: 关于智源的详细信息，请参阅《山石网科智源智能安全运营管理系统WebUI手册》。
智源典型部署
智源的典型部署主要包含智源安全运营平台（iSource Security Operation Platform，简称智源平台）、
流量探针、威胁探针、威胁溯源插件四部分。典型部署包含单机部署和集群部署两种方式。
单机部署
智源平台（单机）、网络安全设备、NDR、EDR、CWPP部署在用户内网环境中，威胁溯源插件部署在用户
服务器或终端上。部署完成后，智源平台可以接收来自网络安全设备、NDR、EDR、CWPP的信息（Meta
Data、Syslog、NetFlow、Linux、Sysmon、威胁信息、资产信息、风险行为信息），从而对全网进行
监控和分析。
单机部署场景参见下图：

<!-- 来源页 852 -->
集群部署
随着用户数据量的增加，单台智源平台可能无法满足用户的需求。针对这一问题，智源平台支持集群部署，
即用户可以部署多台智源平台，进而缓解单台智源平台的数据量压力。
智源平台集群将默认支持高可靠性（HA），能够在设备产生故障时提供备用方案。当集群中一台智源平台发
生故障不可用时，集群中其他智源平台将会继续接收以及处理数据，从而保证数据通信的不间断，有效增强
网络的可靠性。
参考如下集群部署拓扑图，智源平台（集群）、网络安全设备、NDR、EDR、CWPP部署在用户内网环境
中，威胁溯源插件部署在用户服务器和终端上。集群中所有智源平台都部署在同一个二层网络中，第一、
二、三台部署的智源作为Master节点，第四、五及更多的智源作为Secondary节点。部署完成后，智源平
台可以接收来自网络安全设备、NDR、EDR、CWPP的信息（Meta Data、Syslog、NetFlow、Linux、
Sysmon、威胁信息、资产信息、风险行为信息）。
集群部署场景参见下图：

<!-- 来源页 853 -->
连接智源
用户可以通过命令行接口（CLI）和Web界面（WebUI）两种方式连接智源平台。为实现设备与智源平台的
连接，用户需要在设备上启用连接智源功能并配置智源平台的IP地址、VRouter，还可以配置发送至智源平
台的数据类型。连接智源功能配置主要包括以下各项：
l 进入iSource配置模式
l 启用连接智源功能
l 配置智源平台的IP地址
l 配置智源平台的VRouter
l 配置上送到智源平台的数据类型
进入iSource配置模式
进入iSource配置模式，在全局配置模式下，使用以下命令：
cloud server isource
开启连接智源平台
开启连接智源平台功能，在iSource配置模式下，使用以下命令：
enable
在iSource配置模式下，使用no enable命令关闭连接智源平台功能。

<!-- 来源页 854 -->
配置智源平台的IP地址
配置智源平台的IP地址，在iSource配置模式下，使用以下命令：
address {A.B.C.D | domain}
l
A.B.C.D | domain – 指定智源平台的IP地址或域名。
在iSource配置模式下，使用no address命令取消智源平台地址或域名的指定。
配置智源平台的VRouter
配置智源平台的VRouter，在iSource配置模式下，使用以下命令：
vrouter {trust-vr| mgt-vr}
l
trust-vr | mgt-vr–指定VRouter的名称。
在iSource配置模式下，使用no vrouter命令取消智源平台虚拟服务器的指定。
配置发送至智源平台的数据类型
配置发送至智源平台的数据类型，在iSource配置模式下，使用以下命令：
upload-type {all | forensic-pcap | threat-event | device-monitor-property}
l
all–指定将所有类型的数据发送至智源平台。
l
forensic-pcap–指定将设备抓取的威胁相关的证据报文发送至智源平台。
l
threat-event–指定将设备的威胁日志发送至智源平台。
l
device-monitor-property–将防火墙中已识别的设备列表信息发送至智源平台。
在iSource配置模式下，使用no upload-type {all | forensic-pcap | threat-event | device-monitorproperty}命令取消上送到智源平台的数据类型的指定。

<!-- 来源页 855 -->
型号说明：仅以下平台支持上送证据报文。
l
支持：安装有硬盘的A系列平台
l
支持：安装有硬盘的B系列平台
l
支持：安装有硬盘的K系列平台
l
支持：安装有硬盘的X系列平台
l
支持：云·界
显示连接智源平台配置
用户可以在任何模式下使用show命令查看设备连接智源平台的配置信息：
show cloud server isource

<!-- 来源页 856 -->
大模型服务平台介绍
连接大模型服务平台是指连接山石网科云平台或本地部署的大模型一体机，例如山石网科灵岩大模型一体
机。用户可以根据实际需求自由选择通过云平台或者本地大模型来使用AI运维助手，从而适配更多的应用场
景，满足不同环境下的运维需求。
在设备上启用AI运维助手，并正确配置山石云平台的地址、虚拟路由器或本地大模型的IP/域名、端口和虚拟
路由器后，就可以实现设备与山石云平台或本地大模型的连接。
山石网科云平台
山石网科云平台是移动互联时代的云安全服务平台，主要提供山石云服务功能。山石云服务是山石网科的云
端能力中心、云网融合的大脑。启用山石云服务后设备将与山石云端互联，借此将获得更广的威胁情报，提
升设备的防护能力，随时随地在云端进行设备和流量的实时监控、巡检、报表获取等。这些山石云应用将极
大地提升网络安全性、可视性、易用性。
提示: 关于山石云平台的详细信息，请参阅连接山石云平台章节。
山石网科灵岩大模型
山石网科灵岩大模型（简称为山石灵岩）是山石网科推出的新一代智能安全与AI大模型融合解决方案，集高
性能硬件、基础大模型与行业知识中枢于一体，为企业提供“AI+安全+知识管理”的全栈能力。产品深度融
合DeepSeek大语言模型与山石网科全栈安全技术，通过开箱即用的智能服务、动态知识引擎及多维度安全
分析能力，助力企业实现智能化运维、精准化决策与敏捷化知识运营，实现安全闭环与业务价值提升，打造
下一代智能基础设施。
提示: 关于山石灵岩的详细信息，请参阅《山石灵岩大模型软件功能使用手册》。
连接本地大模型服务平台
开始之前
l 阅读"大模型服务平台介绍" 在第854页。
用户可以通过命令行（CLI）和Web界面（WebUI）两种方式连接本地大模型服务平台。连接本地大模型服
务平台主要包含以下各项配置：

<!-- 来源页 857 -->
l 进入本地大模型服务平台配置模式
l 配置本地大模型服务平台连接参数
l 查看本地大模型服务平台的连接信息
进入本地大模型服务平台配置模式
进入本地大模型服务平台配置模式，在全局配置模式下，使用以下命令：
cloud server llm-server
配置本地大模型服务平台连接参数
为实现设备与本地大模型服务平台的连接，用户还需要在设备上配置本地大模型服务平台的IP地址、连接端
口号等参数。
配置本地大模型服务平台的地址
配置本地大模型服务平台的地址，在本地大模型服务平台配置模式下，使用以下命令：
address {A.B.C.D | domain}
l
A.B.C.D | domain - 指定本地大模型服务平台的IP地址或域名，仅支持IPv4地址类型。
删除本地大模型服务平台的IP地址或域名配置，在本地大模型服务平台配置模式下，使用以下命令：
no address
配置本地大模型服务平台的端口号
配置本地大模型服务平台的端口号，在本地大模型服务平台配置模式下，使用以下命令：
port port-number
l
port-number – 指定本地大模型服务平台的端口号。取值范围为1-65535，默认为4433。
恢复默认端口号，在本地大模型服务平台配置模式下，使用以下命令：
no port
指定连接本地大模型服务平台的VRouter
指定连接本地大模型服务平台的VRouter，在本地大模型服务平台配置模式下，使用以下命令：
vrouter vrouter-name
l
vrouter-name –指定VRouter的名称，默认为trust-vr。
恢复默认的VRouter，在本地大模型服务平台配置模式下，使用以下命令：

<!-- 来源页 858 -->
no vrouter
查看本地大模型服务平台的连接信息
查看本地大模型服务平台的连接信息，在任意模式下，使用以下命令：
show cloud server llm-server
以下是一个返回结果示例：
hostname(config)# show cloud server llm-server
Large Languaguage Model Integrated Machine parameters:
=============================================================
server: 10.182.223.151（显示本地大模型服务平台的IP地址或域名）
server port: 4433（显示本地大模型服务平台的端口号）
vrouter: trust-vr（显示本地大模型服务平台的虚拟路由器）
connection status: Online（显示设备与本地大模型服务平台已连接）
ai-assistant enable（显示AI运维助手功能已开启）
llm-access disable（显示数据查询授权功能未开启）
=============================================================

<!-- 来源页 859 -->
连接山石云平台
山石云平台是移动互联时代的云安全服务平台，主要提供山石云服务功能。山石云服务是山石的云端能力中
心、云网融合的大脑。启用山石云服务后设备将与山石云端互联，借此您将获得更广的威胁情报，提升设备
的防护能力，随时随地在云端进行设备和流量的实时监控、巡检、报表获取等。这些山石云应用将极大地提
升网络安全性、可视性、易用性。
山石云平台提供的云服务应用包括：
l 云景（CloudView）：是一款安全领域的SaaS产品，部署在公有云上，为用户提供在线按需服务。Hillstone设
备注册到云平台，将设备信息、流量数据、威胁事件、系统日志等上传到云平台，由云景提供可视化的展示。用
户通过Web方式或者手机APP方式远程监控设备状态信息、获取报表并进行威胁分析。另外，用户还可以从云景
向设备下发配置。关于云景（CloudView），请参阅“山石云景-云端安全运营与管理平台WebUI手册”手册。
l 云·影（Cloud Sandbox）：是系统进行沙箱防护的一种技术。将可疑文件上传到云平台，云沙箱可以分析文
件，搜集可疑文件的动态行为，判断文件合法性，将分析结果反馈给系统，并根据系统设置的动作对恶意文件进
行处理。关于云沙箱的具体配置方法，参考“威胁防护>沙箱防护”。
l 云瞻（CloudVista）：山石云瞻威胁情报中心作为能力中心，设备与云端系统联动，通过云端威助情报的收集、
处理和分析，可为用户提供及时准确的威胁情报数据，辅助管理员分析界定威胁检测结果。用户可以通过威胁情
报中心查看元素相关的威胁情报详情。
连接山石云平台配置
在Hillstone设备端，连接山石云平台配置包括以下内容：
l 云平台服务器对接配置
l 更换数字证书
l 配置HTTP代理服务器
l 配置山石云景服务功能
l 配置山石云瞻服务功能
l 加入用户体验改进计划服务
l 显示云平台服务器配置
注意: 山石云·影的相关配置，请见“威胁防护>沙箱防护”。

<!-- 来源页 860 -->
云平台服务器对接配置
在设备上启用连接云平台功能之后，用户需要获取云平台服务器的地址、用户名及密码，并且需要在设备中
指定获取的信息用于云平台的对接。当用户名密码验证通过后，才能正确连接至山石云平台。
启用连接云平台功能，并指定云平台服务器的地址、用户名/密码、虚拟服务器均需要在Cloud Server配置
模式下进行。
进入Cloud Server配置模式
进入Cloud Server配置模式，在全局配置模式下，使用以下命令：
cloud server cloud-platform
启用连接云平台功能
启用连接云平台功能，在Cloud Server配置模式下，使用以下命令：
enable
在Cloud Server配置模式下，使用no enable命令关闭连接云平台功能。
指定云平台服务器地址
指定云平台服务器地址，在Cloud Server配置模式下，使用以下命令：
address {A.B.C.D | X:X:X:X::X | domain}
l
A.B.C.D | X:X:X:X::X | domain– 指定云平台服务器的IPv4地址、IPv6地址或域名，系统默认地址为
“cloud.hillstonenet.com.cn”。
在Cloud Server配置模式下，使用no address命令取消云平台服务器地址或域名的指定。
指定云平台服务器的用户名及密码
指定云平台服务器的用户名及密码，在Cloud Server配置模式下，使用以下命令：
username user-name password pass-word
l
username user-name – 指定云平台账号用户名，即可将设备注册到公有云指定的用户名下。
l
password pass-word – 指定对应用户的密码。
在Cloud Server配置模式下，使用no username命令取消云平台服务器的用户名及密码的指定。
指定云平台服务器的虚拟路由器
指定云平台服务器的虚拟路由器，在Cloud Server配置模式下，使用以下命令：
vrouter vr-name

<!-- 来源页 861 -->
l
vr-name – 指定虚拟路由器名称。
在Cloud Server配置模式下，使用no vrouter命令取消云平台服务器的虚拟路由器的指定。
更换数字证书
设备和云平台连接时需要使用数字证书进行双向认证，双向认证通过后，设备和云平台成功连接。在系统中
创建信任域存储CA证书，设备用该证书验证云平台提供的证书；创建另一个信任域存储本地证书和私钥，以
便提供证书给云平台认证。导入新的CA证书、本地证书以及私钥后，用户可以更换数字证书。创建信任域、
配置证书和私钥，请参阅PKI配置一节。
引用已有的信任域来获取新的CA证书，在Cloud Server配置模式下，使用以下命令：
server-trust-domain trust-domain-name
l
trust-domain-name–指定系统中已有的存储了新的CA证书的信任域名称。若不配置该项，则使用默
认的内置CA证书。
引用已有的信任域来获取新的本地证书和私钥，在Cloud Server配置模式下，使用以下命令：
agent-trust-domain trust-domain-name
l
trust-domain-name–指定系统中已有的存储了新的本地证书和私钥的信任域名称。若不配置该项，则
使用默认的本地证书和私钥。
配置HTTP代理服务器
在无法直接连接外网的情况下，用户可以通过HTTP代理服务器功能，连接上山石云平台，从而使用AI运维助
手等功能。
注意:
l
HTTP代理服务器仅支持连接山石云平台，不支持连接本地大模型服务平台。
l
HTTP代理服务器仅支持云·景和AI运维助手功能，不支持云·影和云瞻。
l
开启HTTP代理服务器后会存在网络延迟情况，一般会延迟5s左右。
l
A2200/A1800/A1600/X9180/X7180不支持HTTP代理服务器功能。
配置HTTP代理服务器，在Cloud Server配置模式下，使用以下命令：
proxy-server address ip-address port number [username username password password]

<!-- 来源页 862 -->
l
address ip-address – 指定HTTP代理服务器的IP地址，仅支持IPv4类型的IP地址。
l
port number – 指定HTTP代理服务器的端口号，取值范围为1-65535。
l
username username password password – 指定用于登录HTTP代理服务器的用户名和密码。
在Cloud Server配置模式下，使用no proxy-server清除HTTP代理服务器相关信息并关闭此功能。
配置山石云景服务功能
山石云景是一款安全领域的SaaS产品，部署在公有云上，为用户提供在线按需服务。Hillstone设备注册到
云平台，将设备信息、流量数据、威胁事件、系统日志等上传到云平台，由云景提供可视化的展示。用户通
过Web方式或者手机APP方式远程监控设备状态信息、获取报表并进行威胁分析。另外，用户可以通过云景
向设备下发配置。在防火墙上开启配置下发功能后，防火墙将对云景下发的配置进行处理。
在Hillstone设备端，云景相关配置包括以下内容：
l 启用云景
l 开启信息上传
l 开启日志上报
l 开启监控数据上传
l 开启配置下发
l 开启云端资产识别功能
l 开启/关闭资产一键断网功能
启用云景
启用云景需要在Cloud View配置模式下进行。进入Cloud View配置模式，在Cloud Server配置模式下，
使用以下命令：
cloud-view
启用云景，在Cloud View配置模式下，使用以下命令：
enable
在Cloud View配置模式下，使用no enable命令关闭云景。
开启信息上传
将设备运行过程中产生的信息上传到云平台，包括设备基础信息、设备报表数据以及设备列表数据。在
Cloud View配置模式下，使用以下命令：
upload-type {all | device-property | device-report }

<!-- 来源页 863 -->
l
all - 指定将设备的上述所有信息上传到云平台。
l
device-property - 指定将设备的设备列表数据上传到云平台。
l
device-report - 指定将设备的设备报表数据上传到云平台。
在Cloud View配置模式下，使用以下命令取消信息上传：
no upload-type {all | device-property | device-report }
开启日志上报
将设备的日志数据上传到云平台，在Cloud View配置模式下，使用以下命令：
uptype-log {all | log-cf | log-config | log-dlp | log-event | log-device | log-nat | log-nbr |
log-network | log-operat | log-sandbox| log-session | threat-event}
l
log-cf -指定将设备的内容过滤日志上传到云平台。
l
log-config - 指定将设备的配置日志上传到云平台。
l
log-dlp - 指定将设备的文件过滤日志上传到云平台。
l
log-event - 指定将设备的事件日志上传到云平台，上传间隔默认为10分钟。开启该功能前，请先确保
设备已开启事件日志功能（logging event on）。
l
log-device - 指定将设备的IT和IoT日志上传到云平台。
l
log-nat - 指定将设备的NAT日志上传到云平台。
l
log-nbr - 指定将设备的上网行为审计日志上传到云平台。
l
log-network - 指定将设备的网络日志上传到云平台。
l
log-operat - 指定将设备的操作日志上传到云平台。
l
log-sandbox - 指定将设备的云沙箱日志上传到云平台。
l
log-session - 指定将设备的会话日志上传到云平台。
l
threat-event - 指定将设备的威胁事件上传到云平台，上传间隔默认为60分钟。
l
all - 指定将设备的上述所有监控数据上传到云平台。
在Cloud View配置模式下，使用以下命令取消监控数据上传类型的指定：
no uptype-log {all | log-cf | log-config | log-dlp | log-event | log-device | log-nat | log-nbr |
log-network | log-operat | log-sandbox| log-session | threat-event}

<!-- 来源页 864 -->
注意: 高级版云景支持查看上送的所有类型日志。如使用基础版云景，仅支持在云景查看上送的事
件日志和威胁日志。
开启监控数据上传
将设备的监控数据上传到云平台，在Cloud View配置模式下，使用以下命令：
uptype-detect {all | traffic-rank | stats-session | stats-url-rank | stats-device | scvpn-user |
stats-interface}
l
traffic-rank -指定将设备的流量排名数据上传到云平台。
l
stats-session - 指定将设备的会话排名数据上传到云平台。
l
stats-url-rank - 指定将设备的URL排名数据上传到云平台。
l
stats-device -指定将设备的设备信息数据上传到云平台。
l
scvpn-user - 指定将设备的VPN统计数据上传到云平台。
l
stats-interface - 指定将设备的接口统计信息上报至云平台，包括各个接口的上行最大速率、下行最大
速率、上行平均速率和下行平均速率。
l
all - 指定将设备的上述所有监控数据上传到云平台。
在Cloud View配置模式下，使用以下命令取消监控数据上传类型的指定：
no uptype-detect {all | traffic-rank | stats-session | stats-url-rank | stats-device | scvpn-user
| stats-interface}
开启云巡检
在设备端启用云巡检功能后，系统能够接收并执行云端的巡检指令，并且将收集的巡检数据信息上传到云平
台，从而实现随时随地在云端进行设备和流量的实时监控和运维管理。
启用云巡检功能，在Cloud View配置模式下，使用以下命令：
inspection enable
在Cloud View配置模式下，使用no inspection enable命令关闭云巡检功能。
开启下发配置
允许云景下发配置到设备，在Cloud View配置模式下，使用以下命令：
load-config enable
在Cloud View配置模式下，使用no load-config enable命令关闭云景配置下发功能。

<!-- 来源页 865 -->
开启云景配置下发功能后，设备支持加载云景实时下发的以下配置：
l
PTF动态IP黑名单：用户可以在云景上向设备的根VSYS下发新建和删除PTF动态IP黑名单，支持IPv4和
IPv6，并且可以指定生效的虚拟路由器和IP黑名单的阻断时长。设备在接收到云景的配置任务后，会生
成相应的动态IP黑名单条目，同时会生成相应的配置日志和操作日志。
开启/关闭资产一键断网功能
型号说明：
l
支持：安装有硬盘的A/K/X/B系列平台。
l
支持：云·界。
l
不支持：A1600、A1800、A2200。
l
不支持：X9180。
开启资产一键断网功能后，用户可以通过云景对系统中的资产进行一键断网，实现紧急情况下的快速响应。
该功能默认为关闭状态。
开启/关闭资产一键断网功能，在Cloud View配置模式下，使用以下命令：
l
开启：upload-type critical-asset-management
l
关闭：no upload-type critical-asset-management
配置山石云瞻服务功能
山石云瞻服务功能包括以下内容：
l 进入云瞻配置模式
l 开启/关闭IOC详情云端协同查询
l 配置未知域名云端协同查询（云查）功能
开始之前
l IOC详情云端协同查询功能受“威胁情报许可证”控制，请先安装“威胁情报许可证”之后才能使用。
l 未知域名云端协同查询（云查）功能受“僵尸网络防御许可证”控制，请先安装“僵尸网络防御许可证”之后才
能使用。
l 连接山石云平台。

<!-- 来源页 866 -->
进入云瞻配置模式
开启/关闭IOC详情云端协同查询功能、未知域名云端协同查询（云查）功能、配置云查密钥值均需要在云瞻
配置模式下进行配置，在开始配置之前，请先使用以下命令进入云瞻配置模式。
进入云瞻配置模式，在Cloud Server配置模式下，使用以下命令：
cloud-vista
开启/关闭IOC详情云端协同查询
IOC即指威胁情报，IOC详情云端协同查询功能用于向云端服务查询威胁信息的详细内容，辅助管理员分析界
定威胁检测结果。
注意: IOC详情云端协同查询功能受许可证控制，安装“威胁情报许可证”之后才能使用。
默认情况下，该功能为关闭状态。开启该功能后，在重启设备后，该功能依旧保持启用状态。
开启/关闭IOC详情云端协同查询，在云瞻配置模式下，使用以下命令：
l
开启：query-ioc enable
l
关闭：no query-ioc enable
加入用户体验改进计划服务
加入用户体验改进计划服务，设备的威胁数据、UDP类型的DNS流量将会被上传到云端，被用于内部的数据
研究以减少用户设备的误报并实现更好的防护效果。加入用户体验改进计划服务，在Cloud Server配置模式
下，使用以下命令：
user-experience-improvement-plan enable
在Cloud Server配置模式下，使用no user-experience-improvement-plan enable命令，取消加入用
户体验改进计划服务。
注意：抓取UDP DNS流量当满足容量（占用最多176K内存）、数量（最多抓取20个DNS报文）、周期（每
分钟）三者其中一个条件时就会停止抓包并上传至云端。上送失败的UDP DNS流量在之后周期会被新的
UDP DNS流量覆盖，不会被上传至云端。X系列设备、K20803/K9180/K7680/K7280/K6680/K6580设
备不支持将UDP类型的DNS流量上传至云端。
显示云平台服务器配置
显示云平台服务器的配置，在任意模式下，使用以下命令：
show cloud server cloud-platform [all-uptype | cloud-view | cloud-vista | user-experienceimprovement-plan]

<!-- 来源页 867 -->
l
all-uptype - 查看防火墙设备上传到云平台的所有数据信息。
l
cloud-view - 查看云景状态及相关配置信息。
l
cloud-vista - 查看云瞻状态及相关配置信息。
l
user-experience-improvement-plan - 查看用户体验改进计划服务状态。
hostname(config)# show cloud server cloud-platform
cloud-platform parameters:
=============================================================
server: 1.1.2.2 (显示云平台服务器的地址)
username: test （显示云平台服务器的用户名）
password: **********（显示云平台服务器的密码）
security: encrypt （显示数据传输时为加密状态）
server port: 443 （显示云平台服务器的连接端口号）
vrouter: trust-vr （显示云平台服务器的虚拟路由器）
agent trust-domain: （显示存储本地证书和私钥的信任域名称）
server trust-domain: （显示存储CA证书的信任域名称）
server status: enable （显示云平台的启用状态）
connection status: Online （显示云平台的连接状态）
------------------------------------------------------------
service status:
CLOUD-VIEW enable （显示山石云景服务的启用状态）
SANDBOX disable （显示山石云·影服务的启用状态）
VISTA-IOC disable （显示山石云瞻服务的启用状态）
USER-EXPERIENCE-PLAN disable （显示用户体验改进计划服务的启用状态）
VISTA-QUERY disable （显示未知域名云端协同查询（云查）功能的启用状态）
=============================================================

<!-- 来源页 868 -->
配置时间表功能
设备支持时间表（Schedule）功能。时间表功能可以使策略规则、NAT规则在指定的时间生效，也可以控
制PPPoE接口与因特网的连接时间。时间表包含绝对计划和周期计划。周期计划通过周期条目指定时间表的
时间点或者时间段；而绝对计划决定周期计划的生效时间。每个周期计划最多可以拥有16条周期条目。
创建时间表
创建一个时间表，在全局配置模式下，使用以下命令：
schedule schedule-name
l
schedule-name – 指定时间表的名称。范围是1到95个字符。
执行该命令后，系统创建指定名称的时间表并且进入时间表配置模式；如果指定的名称已存在，则直接进入
时间表配置模式。在时间表配置模式下，用户可以配置时间表的周期和绝对时间。
使用no schedule schedule-name命令删除指定的时间表。删除时间表之前，请从其它模块中取消对该时
间表的引用。
指定绝对计划
绝对计划是一个时间范围，指定的周期计划会在绝对计划的时间范围内生效。同时，用户也可以不启用绝对
计划功能，此时周期计划会在被应用到系统中某项功能上时，立即生效。指定绝对计划，在时间表配置模式
下，使用以下命令：
absolute {[start start-date start-time] [end end-date end-time]}
l
start start-date start-time – 指定绝对计划的开始时间点，包括日期和具体时间。start-date为开始
的日期，书写格式为“月/日/年”，例如10/23/2007；start-time为开始的具体时间，书写格式为
“小时:分钟:秒钟”，例如15:30:20。如果不指定该参数的值，开始时间为当前时间。
l
end end-date end-time – 指定绝对计划的结束时间点，包括日期和具体时间。end-date为结束的
日期，书写格式为“月/日/年”，例如11/05/2007；end-time为结束的具体时间，书写格式为“小
时:分钟:秒钟”，例如09:00:00。如果不指定该参数的值，则无结束时间，周期会从开始时间起，一直
有效。
使用no absolute命令关闭绝对计划功能，使周期计划能够即时生效。

<!-- 来源页 869 -->
指定周期计划
周期计划的时间是该周期计划中周期条目的总和。一个周期计划中最多可以添加16个条周期条目。用户可以
配置以下五种类型的周期条目：
l 每天：将在每一天的指定时间生效。例如每天的9:00:30到18:00:20。
l 每周的某几天：将在选择的每周固定几天的指定时间生效。例如每周一、周二和周六的9:00:15到13:30:45。
l 每周一段时间：将在每周的某一段连续时间内生效，例如连续几天或几周。例如从周一早上9:30:30到周三下午
15:00:05。
l 每月的某几天：将在选择的每月固定几天的指定时间生效。例如每月10号、20号的9:00:30到18:00:20。
l 每月一段时间：将在每月的某一段连续时间内生效。例如，某企业为了确保财务人员能够及时处理报账流程，规
定报账系统每月1到20号全天可进行报账，自21号开始，每日上午8:00:00到下午18:00:00期间可以进行报账，
以避免下班时间的报账问题无法及时处理。在该场景下，用户需要创建以下两个周期条目：每月1号到20号的
00:00:00到23:59:59、每月21号到31号的8:00:00到18:00:00。
配置“每天”类型的周期计划
配置“每天”类型的周期计划条目，在时间表配置模式下，使用以下命令：
periodic daily start-time to end-time
l
start-time – 开始时间。书写格式为“小时:分钟:秒钟”，例如09:00:00。
l
end-time – 结束时间。书写格式为“小时:分钟:秒钟”，例如16:30:30。
使用多条该命令添加多个“每天”类型的周期计划条目。
使用no periodic daily start-timetoend-time命令删除指定的周期计划条目。
配置“每周的某几天”类型的周期计划
配置“每周的某几天”类型的周期计划条目，在时间表配置模式下，使用以下命令：
periodic {weekdays | weekend | [monday] […] [sunday]} start-time to end-time
l
weekdays – 工作日（周一到周五）。
l
weekend – 周末（周六到周日）。
l
[monday] […] [sunday] – 选择需要的日期。例如选择周二、周三和周六，命令关键字为tuesday
wednesday saturday。

<!-- 来源页 870 -->
l
start-time – 开始时间。书写格式为“小时:分钟:秒钟”，例如09:00:00。
l
end-time – 结束时间。书写格式为“小时:分钟:秒钟”，例如16:30:30。
使用多条该命令添加多个“每周的某几天”类型的周期计划条目。
使用no periodic {weekdays | weekend | [monday] […] [sunday]} start-time to end-time命令删
除指定的周期计划条目。
配置“每周一段时间”类型的周期计划
配置“每周一段时间”类型的周期计划条目，在时间表配置模式下，使用以下命令：
periodic {[monday] | […] | [sunday]} start-time to {[monday] | […] | [sunday]} end-time
l
[monday] | […] | [sunday] – 开始日期，可以是周一到周日的任意一天。
l
start-time – 开始时间。书写格式为“小时:分钟:秒钟”，例如09:00:00。
l
[monday] | […] | [sunday] – 结束日期，与开始日期相同或者晚于开始日期。
l
end-time – 结束时间。书写格式为“小时:分钟:秒钟”，例如16:30:30。
使用多条该命令添加多条“每周一段时间”类型的周期计划条目。
使用no periodic {[monday] | […] | [sunday]} start-time to {[monday] | […] | [sunday]} end-time
命令删除指定的周期计划条目。
配置“每月的某几天”类型的周期计划
配置“每月的某几天”类型的周期计划条目，在时间表配置模式下，使用以下命令：
periodic day-in-month date start-time to end-time
l
date - 指定日期，可以是每月的任意一天或几天。指定任意几天时，日期需用英文逗号进行分隔，例如
“3,6,9”表示每月的3号、6号、9号。
l
start-time – 开始时间。书写格式为“小时:分钟:秒钟”，例如09:00:00。
l
end-time – 结束时间。书写格式为“小时:分钟:秒钟”，例如16:30:30。
例如：periodic day-in-month 3,6,9 9:00:00 to 18:00:00，表示周期计划为每月3号、6号、9号的
9:00:00到18:00:00。
使用多条该命令添加多条“每月的某几天”类型的周期计划条目。
使用no periodic day-in-month day start-time to end-time命令删除指定的周期计划条目。

<!-- 来源页 871 -->
配置“每月一段时间”类型的周期计划
配置“每月一段时间”类型的周期计划条目，在时间表配置模式下，使用以下命令：
periodic day-range start-day start-time to end-day end-time
l
start-date - 开始日期，可以是每月的任意一天。
l
start-time – 开始时间。书写格式为“小时:分钟:秒钟”，例如09:00:00。
l
end-date - 结束日期，与开始日期相同或者晚于开始日期。
l
end-time – 结束时间。书写格式为“小时:分钟:秒钟”，例如16:30:30。
例如：periodic day-range 15 9:00:00 to 20 18:00:00，表示周期计划为每月5号的9:00:00到20号的
18:00:00。
使用多条该命令添加多条“每月一段时间”类型的周期计划条目。
使用no periodic day-range start-day start-time to end-day end-time命令删除指定的周期计划条
目。
注意: 在周期计划和绝对计划中，时间表的开始时间和结束时间的时间间隔不能小于1分钟。
添加描述信息
为指定时间表添加相关的描述信息，在时间表配置模式下，使用以下命令：
description information
l
information – 指定该时间表的描述信息。范围是1到255个字符。
使用no description命令删除指定时间表的描述信息。
查看指定状态的时间表信息
系统支持查看指定状态的时间表信息。根据时间表的周期计划和绝对计划配置，时间表可以分为以下三种状
态：
l
生效：时间表当前时间为生效状态。
l
失效：时间表当前时间不生效，但之后的时间可能会生效。例如，配置了周期计划的起始时间，且当前
时间早于起始时间。
l
过期：时间表当前不生效，以后也不会生效。例如，配置了绝对计划，且当前时间晚于结束时间。
查看指定状态的时间表信息，在任意模式下，使用以下命令：

<!-- 来源页 872 -->
show schedule status {valid | invalid | expired}
l
valid - 查看处于生效状态的时间表。
l
invalid - 查看处于失效状态的时间表。
l
expired - 查看处于过期状态的时间表。
以下是一个返回结果示例：

<!-- 来源页 873 -->
配置监测对象
系统的监测功能能够监测指定的目标（IP地址或者主机）是否可达或者接口的链路是否连通，以及监测目标
或接口链路是否出现拥塞。如果监测目标不可达或接口链路没有连通，系统会直接判断监测失败；如果监测
目标可达或接口链路连通，系统可以继续根据报文延时和接口流量判断监测目标或链路是否出现拥塞。监测
功能主要用在HA、策略路由、链路负载均衡等场景，用户可以通过配置监控功能确保系统始终选择相对健康
的链路。
注意:
l
监测对象失败的条件是所有失败的监测成员的权重值（weight）总和大于等于监测对象配置的
警戒值（threshold）。
l
监测失败后，系统会断开到监测对象的所有会话。
l
出现拥塞后，系统仍会保留到监测对象的所有会话，但不允许新建会话。
配置监测对象
配置监测功能，首先需配置监测对象，在全局配置模式下，使用以下命令：
track track-object-name [local]
l
track-object-name – 指定监测对象名称。范围是1到31个字符。
l
local – 若指定该参数，系统将不向备份设备同步该监测对象的相关配置信息。默认情况下，不指定该参
数。
执行该命令后，系统创建指定名称的监测对象，并且进入监测对象配置模式；如果指定的名称已存在，则直
接进入监测对象的配置模式。使用该命令no的形式删除指定的监测对象：
no track track-object-name
系统支持通过ICMP报文、HTTP报文、ARP报文、DNS报文、TCP报文和BFD（Bidirectional
Forwarding Detection，双向转发检测）六种方式对目标进行主动监测，还支持通过统计指定接口的流量
信息对目标进行被动监测。
注意: 目前仅HA场景支持通过BFD进行监测。

<!-- 来源页 874 -->
配置监测对象警戒值
警戒值用于判断整个监测对象失败或出现拥塞。当监测对象中失败的监测条目的权重值的总和大于等于一定
值，系统就判断整个监测对象失败。该值即为监测对象的警戒值。
指定监测对象的警戒值，在监测对象配置模式下使用以下命令：
thresholdvalue
l
value – 指定监测对象警戒值的大小。范围是1到255。默认值是255。
在监测对象配置模式使用该命令no的形式恢复警戒值的默认值：
no threshold
查看监测对象
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

<!-- 来源页 875 -->
开启）; hold notify: disable（监测对象异常时，不通知使用该监测对象的模块）
track interface:（监测接口的链路状态）
------------------------------------------------------------------------------------------------
-----------------------------------------------------------------
Track interface weight status（被监测接口的名称该条监测失败对整个监测对象失败贡献的权重值接
口的链路状态）
------------------------------------------------------------------------------------------------
-----------------------------------------------------------------
ethernet0/1 255 unknown
- - More - -
协议监测
ICMP报文监测
通过ICMP报文对目标进行监测，在监测对象配置模式下使用以下命令：
icmp {A.B.C.D | host host-name} interface interface-name [interval value] [threshold value]
[weight value] [src-interface interface-name [prior-used-srcip]]
l
A.B.C.D | host host-name – 指定监测目标的IP地址或者主机名称。主机名称范围是1到63个字符。
l
interface interface-name – 指定发送Ping检测报文的出接口。
l
interval value – 指定发送Ping报文的时间间隔，单位为秒。范围是1到255秒。默认值是3秒。
l
threshold value – 指定判断监测失败的警戒值。如果系统连续未收到该参数指定个数的响应报文，就
判断为监测失败，即目标不可达。取值范围是1到255。默认值是3。
l
weight value – 指定该条监测失败对整个监测对象失败贡献的权重值。取值范围是1到255。默认值是
255。
l
src-interface interface-name – 指定Ping检测报文的源接口。
l
prior-used-srcip – 若源接口上已配置多个IP，将其中一个IP指定为prior-used-srcip后，系统将使
用此IP发送track报文；若没有指定该参数，则使用默认的源接口主IP发送track报文。
icmp6 { ipv6-address | host host-name} interface interface-name [interval value] [threshold
value] [weight value] [src-interface interface-name [prior-used-srcip ipv6-address]]

<!-- 来源页 876 -->
l
ipv6-address | host host-name – 指定监测目标的IPv6地址或者主机名称。主机名称范围是1到63
个字符。
l
interface interface-name – 指定发送Ping检测报文的出接口。
l
interval value – 指定发送Ping报文的时间间隔，单位为秒。范围是1到255秒。默认值是3秒。
l
threshold value – 指定判断监测失败的警戒值。如果系统连续未收到该参数指定个数的响应报文，就
判断为监测失败，即目标不可达。取值范围是1到255。默认值是3。
l
weight value – 指定该条监测失败对整个监测对象失败贡献的权重值。取值范围是1到255。默认值是
255。
l
src-interface interface-name – 指定Ping检测报文的源接口。
l
prior-used-srcip ipv6-address – 若源接口上已配置多个IPv6地址，将其中一个IP指定为priorused-srcip后，系统将使用此IP发送track报文；若没有指定该参数，则使用默认的源接口主IP发送
track报文。
用户可以配置多条该命令为监测对象指定多个监测条目。使用该命令no的形式删除指定的监测条目：
no icmp {A.B.C.D | host host-name} interface interface-name [delay]
no icmp6 {ipv6-address | host host-name} interface interface-name [delay]
ICMP监测报文动态ID
通过ICMP报文对目标进行监测时，同一个监测对象发送的ICMP报文的ID为固定值，ICMP报文可能会被中间
设备误作为DoS攻击而被拦截，导致监测失败。为解决该问题，系统支持配置Ping报文动态ID功能，使同一
个监测对象发送的ICMP报文的ID为动态随机值。配置Ping报文动态ID功能，在测对象配置模式下使用以下
命令：
dynamic-ping-msg-id {enable | disable}
l
enable - 开启Ping报文动态ID功能。开启后，同一个监测对象发送的ICMP报文的ID为动态随机值。
l
disable - 关闭Ping报文动态ID功能。关闭后，同一个监测对象发送的ICMP报文的ID为固定值。
HTTP报文监测
通过HTTP报文对目标进行监测，在监测对象配置模式下使用以下命令：
http {A.B.C.D | host host-name} interface interface-name [interval value] [threshold value]
[weight value] [src-interface interface-name]

<!-- 来源页 877 -->
l
A.B.C.D | host host-name – 指定监测目标的IP地址或者主机名称。主机名称范围是1到63个字符。
l
interface interface-name – 指定发送HTTP检测报文的出接口。
l
interval value – 指定发送HTTP报文的时间间隔，单位为秒。范围是1到255秒。默认值是3秒。
l
threshold value – 指定判断监测失败的警戒值。如果系统连续未收到该参数指定个数的响应报文，就
判断为监测失败，即目标不可达。取值范围是1到255。默认值是3。
l
weight value – 指定该条监测失败对整个监测对象失败贡献的权重值。取值范围是1到255。默认值是
255。
l
src-interface interface-name – 指定HTTP检测报文的源接口。
用户可以配置多条该命令为监测对象指定多个监测条目。使用该命令no的形式删除指定的监测条目：
no http {A.B.C.D | host host-name} interface interface-name [delay]
ARP报文监测
通过ARP报文对目标进行监测，在监测对象配置模式下使用以下命令：
arp {A.B.C.D} interface interface-name [interval value] [threshold value] [weight value]
l
A.B.C.D – 指定监测目标的IP地址。
l
interface interface-name – 指定发送ARP检测报文的出接口。
l
interval value – 指定发送ARP报文的时间间隔，单位为秒。范围是1到255秒。默认值是3秒。
l
threshold value – 指定判断监测失败的警戒值。如果系统连续未收到该参数指定个数的响应报文，就
判断为监测失败，即目标不可达。取值范围是1到255。默认值是3。
l
weight value – 指定该条监测失败对整个监测对象失败贡献的权重值。取值范围是1到255。默认值是
255。
用户可以配置多条该命令为监测对象指定多个监测条目。使用该命令no的形式删除指定的监测条目：
no arp {A.B.C.D} interface interface-name
DNS报文监测
通过DNS报文对目标进行监测，在监测对象配置模式下使用以下命令：
dns A.B.C.D interface interface-name [interval value] [threshold value] [weight value] [srcinterface interface-name]

<!-- 来源页 878 -->
l
A.B.C.D – 指定监测目标的IP地址。
l
interface interface-name – 指定发送DNS检测报文的出接口。
l
interval value – 指定发送DNS报文的时间间隔，单位为秒。范围是1到255秒。默认值是3秒。
l
threshold value – 指定判断监测失败的警戒值。如果系统连续未收到该参数指定个数的响应报文，就
判断为监测失败，即目标不可达。取值范围是1到255。默认值是3。
l
weight value – 指定该条监测失败对整个监测对象失败贡献的权重值。取值范围是1到255。默认值是
255。
l
src-interface interface-name – 指定DNS检测报文的源接口。
用户可以配置多条该命令为监测对象指定多个监测条目。使用该命令no的形式删除指定的监测条目：
no dns A.B.C.D interface interface-name [delay]
TCP报文监测
通过TCP报文对目标端口进行监测，在监测对象配置模式下使用以下命令：
tcp {A.B.C.D | host host-name} port port-number interface interface-name [interval value]
[threshold value] [weight value] [src-interface interface-name]
l
A.B.C.D | host host-name – 指定监测目标的IP地址或者主机名称。主机名称范围是1到63个字符。
l
port port-number – 指定监测目标的目的端口号。取值范围为0到65535。
l
interface interface-name – 指定发送TCP检测报文的出接口。
l
interval value – 指定发送TCP报文的时间间隔，单位为秒。范围是1到255秒。默认值是3秒。
l
threshold value – 指定判断监测失败的警戒值。如果系统连续未收到该参数指定个数的响应报文，就
判断为监测失败，即目标不可达。取值范围是1到255。默认值是3。
l
weight value – 指定该条监测失败对整个监测对象失败贡献的权重值。取值范围是1到255。默认值是
255。
l
src-interface interface-name – 指定TCP检测报文的源接口。
用户可以配置多条该命令为监测对象指定多个监测条目。对于同一个监测对象，不能同时配置对同一目标主
机的HTTP监测和对端口80（port 80）的TCP监测。使用该命令no的形式删除指定的监测条目：
no tcp {A.B.C.D | host host-name} port port-number interface interface-name [delay]

<!-- 来源页 879 -->
BFD监测
BFD（Bidirectional Forwarding Detection，双向转发检测）能够快速检测网络中链路或者IP路由的转
发连通状况。
HA场景下，系统可以通过BFD监测设备的工作状态，如果监测对象出现故障不能正常工作，BFD可以快速检
测到问题并通知系统进行主备切换。相较于其他监测方式，BFD可以实现毫秒级的主备切换，从而保证数据
通信的畅通，有效增强网络的可靠性。
配置BFD监测，在监测对象配置模式下，使用以下命令：
bfd {ipv6 X:X:X:X::X | A.B.C.D} interface interface_name prior-used-srcip {X:X:X:X::X |
A.B.C.D} [bfd-template bfd_template_name] [weight value]
l
{ipv6 X:X:X:X::X | A.B.C.D}– 指定监测对象的IPv6地址或IPv4地址。
l
interface interface_name – 指定发送BFD监测报文的出接口。
l
prior-used-srcip {X:X:X:X::X | A.B.C.D}– 指定出接口的IPv6地址或IPv4地址。该地址需配置为备设
备的管理IP地址，避免备设备无法发送BFD监测报文，导致BFD会话建立失败。
l
bfd-template bfd_template_name – 当使用BFD多跳检测方式时，需指定BFD多跳检测模板名称以
绑定该模板。如不指定该参数，则表示使用BFD单跳检测方式。关于BFD单跳/多跳检测定义以及如何创
建BFD多跳检测模板，请参阅配置BFD多跳检测。
l
weight value– 指定该条监测失败对整个监测对象失败贡献的权重值。取值范围是1到255。如不指
定，默认值是255。
在监测对象配置模式下，使用该命令no的形式删除指定的监测条目：
no bfd {ipv6 X:X:X:X::X | A.B.C.D} interface interface_name prior-used-srcip {X:X:X:X::X |
A.B.C.D} [bfd-template bfd_template_name]
注意:
l
目前系统仅支持配置一条BFD监测条目，且仅HA功能支持通过BFD监测设备的工作状态。
l
配置BFD监测条目后，将无法配置其他类型的监测条目。
接口链路状态监测
配置监测接口的链路状态，在监测对象配置模式下使用以下命令：
interface interface-name [weight value]

<!-- 来源页 880 -->
l
interface-name – 指定被监测接口的名称。
l
weight value – 指定该条监测失败对整个监测对象失败贡献的权重值。取值范围是1到255。默认值是
255。
用户可以配置多条该命令为监测对象指定多个监测条目。使用该命令no的形式删除指定的监测条目：
no interface interface-name
接口带宽监测
配置监测接口带宽，在监测对象配置模式下使用以下命令：
bandwidth interface interface-name direction {in | out | both} [high-watermark value lowwatermark value] [interval value] [threshold value] [weight value]
l
interface-name – 指定被监测接口的名称。
l
direction {in | out | both} – 指定监测的流量方向。in指流入方向，out指流出方向，both指双方向。
默认为流出方向（out）。
l
high-watermark value low-watermark value – 指定接口流量的高水位线和低水位线，单位为
kbps。取值范围是1到100000000kbps。接口流量小于指定的高水位线，系统会判断链路为正常状
态；接口流量大于或等于指定的高水位下，系统会判断出现链路拥塞；出现链路拥塞后，只有在接口流
量小于或等于指定的低水位线后系统才会判断链路恢复正常状态。这种高低水位线的设计可以有效的防
范链路在正常与拥塞状态之间频繁切换。
l
interval value – 指定监控接口流量的间隔时间，单位为秒。取值范围是1到255秒。默认值是1秒。
l
threshold value – 指定判断该条监测出现拥塞的警戒值。如果系统连续检测到参数指定次数的链路过
载情况，就判断该条监测出现拥塞。取值范围是1到255。默认值是3。
l
weight value – 指定该条监测出现拥塞对整个监测对象出现拥塞贡献的权重值。取值范围是1到255。
默认值是255。
用户可以配置多条该命令为监测对象指定多个监测条目。使用该命令no的形式删除指定的监测条目：
no bandwidth interface interface-name
接口链路质量监测
通过统计指定接口的采样流量信息，系统可以监测该接口的链路状态。配置接口链路对象监测，在监测对象
配置模式下使用以下命令：

<!-- 来源页 881 -->
traffic-condition [ ipv6 ]interface interface-name [interval value] [threshold value] [weight
value] [condition-threshold low-watermark high-watermark]
l
ipv6 – 指定为IPv6类型的接口链路监测对象。如果不指定该参数，默认指定为IPv4类型的接口链路监测
对象。
l
interface-name – 指定被监测接口的名称。
l
interval value– 指定每个监测周期的持续时间，单位为秒。取值范围是1到255秒。默认值是3秒。每
个监测周期结束后，系统会重置探测到的新建会话相关数值。
l
threshold value – 指定判断监测失败的警戒值。如果系统连续检测到参数指定次数的监测失败情况，
就判断该条监测失败。取值范围是1到255。默认值是3。
l
weight value – 指定该条监测失败对整个监测对象失败贡献的权重值。取值范围是1到255。默认值是
255。
l
condition-threshold low-watermark high-watermark – 指定每个监测周期的新建会话成功率阈
值。默认情况下，失败界定阈值为30，成功界定阈值为50。取值范围是0到100。在某个监测周期内，
当新建会话成功率小于指定的失败界定阈值时，判断为监测失败；当新建会话成功率大于指定的成功界
定阈值时，判断为监测成功；当新建会话成功率大于等于失败界定阈值且小于等于成功界定阈值时，系
统保持原来的监测状态。
用户可以配置多条该命令为监测对象指定多个监测条目。使用该命令no的形式删除指定的监测条目：
no traffic-condition [ ipv6 ] interface interface-name
系统资源监测
系统支持对设备的CPU利用率和内存利用率进行监测，并基于监测结果来控制接口的自动关闭。如果达到监
测对象配置的警戒值，系统会强制关闭指定接口，从而在一定程度上提升网络通信的稳定性和可靠性。
l
CPU利用率监测
l
内存利用率监测
注意: “系统资源”类型的监测对象仅支持在自动关闭接口时以及在HA中引用。关于如何配置接口
的自动关闭功能，请参阅“强制关闭接口”章节。
CPU利用率监测
监测CPU利用率，在监测对象配置模式下，使用以下命令：
cpu {any | cpu_name} [threshold value] [recover-threshold value] [weight value]

<!-- 来源页 882 -->
l
any | cpu_name – 指定需要进行监测的CPU名称。当指定为“Any”时，表示监测设备SIOM模块和
SSM模块上的所有CPU。如果SIOM模块和SSM模块上任意一个CPU的CPU利用率达到监测值，则判断为
监测成员失败。
型号说明：仅部分设备（X系列、K20803、K9180、K7680、K7280、K6680、K6580）
支持配置该参数。
l
threshold value – 指定判断监测失败的警戒值。如果CPU利用率达到监测警戒值，则判断为监测成员
失败。取值范围是1到100，默认值是85。
l
recover-threshold value - 指定监测成员的恢复阈值。当CPU利用率小于恢复阈值时，监测成员将自
动恢复为成功状态。取值范围是1到100。默认值为空，即未配置恢复阈值时，监测成员不会进行自动恢
复。
l
weight value – 指定该监测成员失败对整个监测对象失败贡献的权重值。如果同一监测对象下所有失败
的监测成员贡献的权重值总和达到监测对象配置的警戒值，则判断为监测对象失败。取值范围是1到
255。默认值是255。
内存利用率监测
监测内存利用率，在监测对象配置模式下，使用以下命令：
memory {any | cpu_name} [threshold value] [recover-threshold value] [weight value]
l
any | cpu_name – 指定需要进行监测的CPU名称。当指定为“Any”时，表示监测设备SIOM模块和
SSM模块上的所有CPU。如果SIOM模块和SSM模块上任意一个CPU的内存利用率达到监测值，则判断为
监测成员失败。
型号说明：仅部分设备（X系列、K20803、K9180、K7680、K7280、K6680、K6580）
支持配置该参数。
l
threshold value – 指定判断监测成员失败的警戒值。如果内存利用率达到监测警戒值，则判断为监测
成员失败。取值范围是1到100，默认值是95。

<!-- 来源页 883 -->
l
recover-threshold value - 指定监测成员的恢复阈值。当内存利用率小于恢复阈值时，监测成员将自
动恢复为成功状态。取值范围是1到100。默认值为空，即未配置恢复阈值时，监测成员不会进行自动恢
复。
l
weight value – 指定该监测成员失败对整个监测对象失败贡献的权重值。如果同一监测对象下的所有监
测成员贡献的权重值总和达到监测对象配置的警戒值，则判断为监测对象失败。取值范围是1到255。默
认值是255。
动态路由监测
系统支持对动态路由的邻居状态进行监测，并基于监测结果切换HA设备的主备状态。系统支持监测以下动态
路由：
l OSPF动态路由监测
l BGP动态路由监测
注意: “动态路由”类型的监测对象仅支持被HA引用。
OSPF动态路由监测
配置OSPF动态路由监测，在监测对象配置模式下，使用以下命令：
ospf [ipv6] local-process-id process-id neighbor A.B.C.D vrouter vr-name [first-check-delay
[delay-minutes]] [weight value]
l
ipv6 - 指定监测IPv6类型的OSPF动态路由，若不配置，则为监测IPv4类型的OSPF动态路由。
l
local-process-id process-id - 指定被监测的OSPF动态路由的进程ID。取值范围为1-65535。
l
neighbor A.B.C.D - 指定被监测的OSPF动态路由的邻居ID，即动态路由对应邻居的IP地址。当查询所
配置的邻居IP地址不存在时，该监测成员为失败状态。
l
vrouter vr-name - 指定被监测的OSPF动态路由所属的虚拟路由器。
l
first-check-delay delay-minutes - 指定被监测动态路由的首次监测延后生效时间。考虑到创建动态
路由需要时间，为避免查询时由于路由未创建而导致监测失败，用户可以调整首次监控动态路由邻居状
态的延后生效时间。取值范围为0-30分钟，默认为10分钟。
l
weight value - 指定该成员监测失败对整个监测对象失败贡献的权重值。取值范围是1-255。默认值是
255。
删除OSPF动态路由监测成员，在监测对象配置模式下，使用以下命令：

<!-- 来源页 884 -->
no ospf [ipv6] local-process-id process-id neighbor A.B.C.D vrouter vr-name
BGP动态路由监测
配置BGP动态路由监测，在监测对象配置模式下，使用以下命令：
bgp [ipv6] neighbor A.B.C.D vrouter vr-name [first-check-delay [delay-minutes]] [weight
value]
l
ipv6 - 指定监测IPv6类型的BGP动态路由，若不配置，则为监测IPv4类型的BGP动态路由。
l
neighbor A.B.C.D - 指定被监测的BGP动态路由的邻居ID，即动态路由对应邻居的IP地址。当查询所
配置的邻居IP地址不存在时，该监测成员为失败状态。
l
vrouter vr-name - 指定被监测的BGP动态路由所属的虚拟路由器。
l
first-check-delay delay-minutes - 指定被监测动态路由的首次监测延后生效时间。考虑到创建动态
路由需要时间，为避免查询时由于路由未创建而导致监测失败，用户可以调整首次监控动态路由邻居状
态的延后生效时间。取值范围为0-30分钟，默认为10分钟。
l
weight value - 指定该成员监测失败对整个监测对象失败贡献的权重值。取值范围是1-255。默认值是
255。
删除BGP动态路由监测成员，在监测对象配置模式下，使用以下命令：
no bgp [ipv6] neighbor A.B.C.D vrouter vr-name

<!-- 来源页 885 -->
应用层强制检查
系统支持应用层强制检查功能。开启该功能后，系统将对应用层入侵防御、病毒过滤、内容过滤以及网页关
键字过滤、应用层行为控制进行强制检查。若关闭该功能，当系统资源过低（例如设备的CPU使用率过高、
内存、数据包缓存剩余容量不足）时，系统将对数据包放行处理，来控制应用层功能对设备的资源利用，从
而不会影响到其他功能模块。默认情况下，该功能为关闭状态。
开启/关闭应用层强制检查功能
用户可在全局配置模式下，使用以下命令开启应用层强制检查：
fail-close enable
在全局配置模式下，使用该命令no的形式关闭该功能：
no fail-close enable
注意: 不支持应用层强制检查功能有：FTP的应用行为控制、Web surfing、IPS的
MSRPC/SUNRPC/DNS(UDP）检测。
查看应用层强制检查启用状态
在任何模式下运行show fail-close命令可以查看当前的应用层强制检查功能的启用状态。
开启/关闭应用层安全Bypass功能
系统支持对应用层的功能一键Bypass，包括入侵防御，病毒过滤，URL过滤、数据安全、沙箱防护、病毒过
滤、僵尸网络。在全局配置模式下，使用以下命令开启应用层一键Bypass功能：
app-security-bypass
在全局配置模式下，使用该命令no的形式关闭该功能：
no app-security-bypass
注意: 当应用层安全Bypass功能与应用层强制检查功能同时配置时，应用层安全Bypass功能的优
先级更高。
查看应用层安全Bypass启用状态
在任何模式下运行show app-security-bypass命令可以查看当前的应用层安全Bypass功能的启用状态。

<!-- 来源页 886 -->
系统监控报警
StoneOS的系统监控报警功能能够监控系统资源的使用状况，并根据配置发出报警信息。当前版本支持的报
警方式为日志信息和SNMP Trap信息。
进入监控配置模式
配置系统监控报警功能，首先要进入监控配置模式。进入监控配置模式，在全局配置模式下，使用以下命
令：
monitor
配置监控规则
进入监控配置模式后，用户可以根据需要监控的系统资源对象，设置相应的监控规则：
{cpu | memory utilization | interface-bandwidth interface-name utilization | log-buffer { 
config | event | ips | network | security | traffic{session | nat | urlfilter}} utilization | policy
utilization | session utilization | snat-resource utilization} interval interval-value absolute
rising-threshold threshold-value sample-period period-value [count count-value] {log
[snmp-trap] | snmp-trap}
l
cpu | memory utilization | interface-bandwidth interface-name utilization | log-buffer { 
config | event | ips | nbc | network | security | traffic {session | nat | urlfilter}} utilization |
policy utilization | session utilization | snat-resource utilization – 指定监控对象，可以为系统
CPU（cpu）、内存（memory）、接口带宽（interface-bandwidth）、日志容量（logbuffer）、策略数（policy）、会话（session）和SNAT转换后的IP地址端口资源（snatresource）。当用户设备为X平台时，选择CPU监控对象后，需要继续选择对应的板卡。
l
interface-name – 指定监控的接口名称。
l
config | event | ips | network | security | traffic {session | nat | urlfilter} – 指定具体的日
志类型。
l
utilization – 指定监控值为各对象的利用率。CPU（cpu）的监控值默认为利用率，不需要指
定。
l
interval interval-value – 指定监控间隔，即系统在报警计算时间段（sample-period periodvalue）内，每次取值后等待的时间间隔。取值范围为3到10秒。

<!-- 来源页 887 -->
l
absolute – 指定监控值为绝对值。
l
rising-threshold threshold-value – 指定上升阈值，即实际监控值超过该阈值满足报警条件的百分
比。取值范围为1到99。
l
sample-period period-value – 指定报警计算时间段。取值范围为30到3600秒。
l
count count-value – 指定在报警计算时间段（sample-period）内，监控对象的实际监控数值超过
阈值（rising-threshold）的次数。取值范围为1到1000。如果配置该参数，在监控时间段内，若监控
对象值超过阈值的次数大于该count值，则发出警告；如果不配置该参数，在监控时间段内，若监控对
象值的平均值大于阈值（rising-threshold），则发出警告。
l
log [snmp-trap] | snmp-trap – 指定报警方式。可以使用日志（log）或者SNMP Trap报文
（snmp-trap），也可以同时使用这两种报警方式。
例如：
配置CPU峰值监控：
hostname(config)# monitor
hostname(config-monitor)# cpu interval 5 absolute rising-threshold 65 sampleperiod 600 count 50 log
完成该配置后，在600秒内，如果CPU利用率超过了阈值65%，且发生过最少50次，则发出
报警日志
配置会话均值监控：
hostname(config)# monitor
hostname(config-monitor)# session utilization interval 8 absolute rising-threshold 90
sample-period 600 log
完成该配置后，在600秒内，如果会话平均利用率超过了阈值90%，则发出报警日志
在监控配置模式下使用该命令no的形式删除指定的监控规则：
no {cpu | memory utilization | interface-bandwidth interface-name utilization | log-buffer { 
config | event | ips | network | security | traffic {session | nat | urlfilter}} utilization | policy
utilization | session utilization | snat-resource utilization}

<!-- 来源页 888 -->
注意:
l
不支持对SNAT转换后地址为出接口IP地址（eif-ip）的端口资源的监控报警；
l
对于每种监控对象，只有最后配置的一条监控规则生效。
查看系统监控报警配置
查看系统监控报警配置，在任意模式下，使用以下命令：
show monitor

<!-- 来源页 889 -->
CPU Cache Error监控
型号说明：SG-6000-A2200/A1800/A1600支持该功能。
为尽量避免CPU Cache Error报错导致设备工作异常的问题，用户可以配置CPU Cache Error监控功能。
配置该功能后，当系统的CPU Cache Error报错次数达到指定的阈值时，设备会重启或者不重启。
配置CPU Cache Error监控功能
为尽量避免CPU Cache Error报错导致设备工作异常的问题，用户可以配置CPU Cache Error监控功能。
配置该功能后，用户可以分别配置CPU Cache Error的告警阈值和重启阈值，两个阈值相互独立。当达到告
警阈值时，设备会生成告警日志；当达到重启阈值时，设备可以选择重启、不重启两个动作。
配置CPU Cache Error监控功能，首先要进入监控配置模式。进入监控配置模式，在全局配置模式下，使用
以下命令：
monitor
配置CPU Cache Error监控功能的告警阈值，在监控配置模式下，使用以下命令：
cache-error-config threshold-num num alarm
l
threshold-numnum - 指定告警阈值，当CPU Cache Error的报错次数达到告警阈值时，设备会发出
告警并生成日志。取值范围为100至500。
l
alarm- 指定CPU Cache Error的报错次数达到指定阈值后设备的动作，即告警（alarm）。
配置CPU Cache Error监控功能的重启阈值，在监控配置模式下，使用以下命令：
cache-error-config threshold-num numreboot {enable | disable}
l
threshold-num num - 指定重启阈值，当CPU Cache Error的报错次数达到重启阈值时，设备会根据
配置重启或者不重启。取值范围为500至5000。
l
{reboot enable | reboot disable}- 指定CPU Cache Error的报错次数达到指定阈值后设备的动作，
可以为重启（enable）或者不重启（disable）。
例如：
hostname(config)# monitor
hostname(config-monitor)# cache-error-config threshold-num 1000 reboot enable

<!-- 来源页 890 -->
完成该配置后，如果系统的CPU Cache Error报错次数达到了1000次，则重启设备。
在监控配置模式下，使用no cache-error-config命令取消CPU Cache Error监控配置。
查看CPU Cache Error监控配置信息
查看CPU Cache Error监控配置信息，在任意模式下，使用以下命令：
show cache-error-reboot-config
l
cache-error-reboot-config- 显示当前配置的CPU Cache Error的重启阈值。

<!-- 来源页 891 -->
系统最大并发连接数变化
在部分平台上开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防护、僵尸网络防御、NetFlow等功能
后，或者使用IPv6版本系统软件，系统的最大并发连接数会发生变化。下表列出设备平台型号、系统文件版
本以及相应的系统最大并发连接数的变化情况。
平台/模块
系统文件
最大并发连接数变化
SG-6000 A系列设备
SG-6000 B系列设备
StoneOS IPv4版本
开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防护、
僵尸网络防御、NetFlow功能后，系统最大并发连接数无变
化。
StoneOS IPv6版本
l IPv6版本原始的最大并发连接数与IPv4版本一致；
l 开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防
护、僵尸网络防御、NetFlow等功能后，系统最大并发
连接数无变化。
SG-6000 K系列设备（不
含K20803/K9180）
StoneOS IPv4版本
开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防护、
僵尸网络防御、NetFlow功能后，系统最大并发连接数无变
化。
StoneOS IPv6版本
l IPv6版本原始的最大并发连接数与IPv4版本一致；
l 开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防
护、僵尸网络防御、NetFlow等功能后，系统最大并发
连接数无变化。
QSM模块
StoneOS IPv4版本
l 开启多VR：最大并发连接数减少15%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15)”；
l 开启病毒过滤/入侵防御/URL特征库/沙箱防护/僵尸网
络防御中的一个或者多个：最大并发连接数减少50%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.5)”；
l 开启多VR的同时开启病毒过滤/入侵防御/URL特征库/沙
箱防护/僵尸网络防御中的一个或者多个：最大并发连接
数在已经减少的基础上再减少50%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15)*(1-0.5)”；

<!-- 来源页 892 -->
平台/模块
系统文件
最大并发连接数变化
l 开启Netflow功能：最大并发连接数减少25%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.25)”；
l 开启多VR的同时开启NetFlow和病毒过滤/入侵防御
/URL特征库/沙箱防护/僵尸网络防御中的一个或者多
个：最大并发连接数在已经减少的基础上再减少。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15）*(1-0.25)*(1-0.5)”。
StoneOS IPv6版本
l IPv6版本原始的最大并发连接数为IPv4版本的50%；
l 开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防
护、僵尸网络防御、NetFlow等功能后，最大并发连接
数变化情况与IPv4版本一致。
SSM-300
StoneOS IPv4版本
l 开启多VR：最大并发连接数减少15%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15)”；
l 开启病毒过滤/入侵防御/URL特征库/沙箱防护/僵尸网
络防御中的一个或者多个：最大并发连接数减少50%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.5)”；
l 开启多VR的同时开启病毒过滤/入侵防御/URL特征库/沙
箱防护/僵尸网络防御中的一个或者多个：最大并发连接
数在已经减少的基础上再减少50%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15)*(1-0.5)”；
l 开启Netflow功能：最大并发连接数减少25%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.25)”；
l 开启多VR的同时开启NetFlow和病毒过滤/入侵防御
/URL特征库/沙箱防护/僵尸网络防御中的一个或者多

<!-- 来源页 893 -->
平台/模块
系统文件
最大并发连接数变化
个：最大并发连接数在已经减少的基础上再减少。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15）*(1-0.25)*(1-0.5)”。
StoneOS IPv6版本
l 对于X9180，IPv6版本原始的最大并发连接数为IPv4版
本的2/3；
l 开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防
护、僵尸网络防御、NetFlow等功能后，最大并发连接
数变化情况与IPv4版本一致。
SSM-200
SSM-100
StoneOS IPv4版本
l 开启多VR：最大并发连接数减少15%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15)”；
l 开启病毒过滤/入侵防御/URL特征库/沙箱防护/僵尸网
络防御中的一个或者多个：最大并发连接数减少50%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.5)”；
l 开启多VR的同时开启病毒过滤/入侵防御/URL特征库/沙
箱防护/僵尸网络防御中的一个或者多个：最大并发连接
数在已经减少的基础上再减少50%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15)*(1-0.5)”；
l 开启Netflow功能：最大并发连接数减少25%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.25)”；
l 开启多VR的同时开启NetFlow和病毒过滤/入侵防御
/URL特征库/沙箱防护/僵尸网络防御中的一个或者多
个：最大并发连接数在已经减少的基础上再减少。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15）*(1-0.25)*(1-0.5)”。
StoneOS IPv6版本
l IPv6版本原始的最大并发连接数为IPv4版本的2/3；

<!-- 来源页 894 -->
平台/模块
系统文件
最大并发连接数变化
l 开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防
护、僵尸网络防御、NetFlow等功能后，最大并发连接
数变化情况与IPv4版本一致。
SIOM
（X/K20803/K9180）
StoneOS IPv4版本
l 开启多VR：最大并发连接数减少15%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15)”；
l 开启病毒过滤/入侵防御/URL特征库/沙箱防护/僵尸网
络防御中的一个或者多个：最大并发连接数减少50%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.5)”；
l 开启多VR的同时开启病毒过滤/入侵防御/URL特征库/沙
箱防护/僵尸网络防御中的一个或者多个：最大并发连接
数在已经减少的基础上再减少50%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15)*(1-0.5)”；
l 开启Netflow功能：最大并发连接数减少25%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.25)”；
l 开启多VR的同时开启NetFlow和病毒过滤/入侵防御
/URL特征库/沙箱防护/僵尸网络防御中的一个或者多
个：最大并发连接数在已经减少的基础上再减少。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15）*(1-0.25)*(1-0.5)”。
StoneOS IPv6版本
l IPv6版本原始的最大并发连接数与IPv4版本一致；
l 开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防
护、僵尸网络防御、NetFlow等功能后，最大并发连接
数变化情况与IPv4版本一致。
IOM-P100-300
IOM-P40-300
StoneOS IPv4版本
l 开启多VR：最大并发连接数减少15%。
计算公式为“实际最大并发连接数=原始最大并发连接数

<!-- 来源页 895 -->
平台/模块
系统文件
最大并发连接数变化
*(1-0.15)”；
l 开启病毒过滤/入侵防御/URL特征库/沙箱防护/僵尸网
络防御中的一个或者多个：最大并发连接数减少50%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.5)”；
l 开启多VR的同时开启病毒过滤/入侵防御/URL特征库/沙
箱防护/僵尸网络防御中的一个或者多个：最大并发连接
数在已经减少的基础上再减少50%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15)*(1-0.5)”；
l 开启Netflow功能：最大并发连接数减少25%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.25)”；
l 开启多VR的同时开启NetFlow和病毒过滤/入侵防御
/URL特征库/沙箱防护/僵尸网络防御中的一个或者多
个：最大并发连接数在已经减少的基础上再减少。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.15）*(1-0.25)*(1-0.5)”。
StoneOS IPv6版本
l 对于X9180，IPv6版本原始的最大并发连接数为IPv4版
本的88.3%；
l 开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防
护、僵尸网络防御、NetFlow等功能后，最大并发连接
数变化情况与IPv4版本一致。
IOM-8SFP+
StoneOS IPv4版本
开启NetFlow功能：最大并发连接数减少25%。
计算公式为“实际最大并发连接数=原始最大并发连接数*(1-
0.25)”。
注意：其它未列出功能对最大并发连接数无影响。
StoneOS IPv6版本
l IPv6版本原始的最大并发连接数为IPv4版本的2/3；
l 开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防
护、僵尸网络防御、NetFlow等功能后，最大并发连接

<!-- 来源页 896 -->
平台/模块
系统文件
最大并发连接数变化
数变化情况与IPv4版本一致。
IOM-200
IOM-100
StoneOS IPv4版本
开启NetFlow功能：最大并发连接数减少25%。
计算公式为“实际最大并发连接数=原始最大并发连接数*(1-
0.25)”。
注意：其它未列出功能对最大并发连接数无影响。
StoneOS IPv6版本
l IPv6版本原始的最大并发连接数为IPv4版本的67.5%；
l 开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防
护、僵尸网络防御、NetFlow等功能后，最大并发连接
数变化情况与IPv4版本一致。
IOM-80
IOM-20
StoneOS IPv4版本
l 开启IOM卡快转功能：最大并发连接数减少60% 。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.6)”；
l 开启NetFlow功能：最大并发连接数减少25%。
计算公式为“实际最大并发连接数=原始最大并发连接数
*(1-0.25)”。
StoneOS IPv6版本
l IPv6版本原始的最大并发连接数为IPv4版本的50%；
l 开启多VR、病毒过滤、入侵防御、URL特征库、沙箱防
护、僵尸网络防御、NetFlow等功能后，最大并发连接
数变化情况与IPv4版本一致。
调整系统最大并发连接数
注意: 调整最大并发连接数可能会影响部分功能的正常使用，操作之前请联系山石网科工作人员。
用户可以根据需要调整部分A系列、K系列设备的IPv4最大并发连接数。调整最大并发连接数，在全局配置模
式下，使用以下命令：
exec session-adjust [vssm] value
l
value - 指定设备IPv4最大并发连接数。取值范围请参考下表。
l
vssm - 仅K7680/K7280/K6680支持配置该参数。由于硬件结构差异，因此调整
K7680/K7280/K6680设备的IPv4最大并发连接数时需配置该参数。

<!-- 来源页 897 -->
型号
取值范围
A200-A/A200G4-
A/A200WA/A200WG4-A
360,000 - 2,000,000
A1000
120,000 - 600,000
A1100
120,000 - 600,000
A1600-A
360,000 - 2,000,000
A1600
360,000 - 2000,000
A1800
360,000 - 2000,000
A1800-A
360,000 - 2,000,000
A2000
400,000 - 2,000,000
A2200
400,000 - 2000,000
A2200-A
400,000 - 2000,000
A2600
400,000 - 2,000,000
A2700
440,000 - 2,200,000
A2710
1,500,000 - 2,200,000
A2800
500,000 - 2,500,000
A2810
1,800,000 - 2,500,000
A3000
700,000 - 3,500,000
A3600
960,000 - 4,800,000
A3610
3,000,000 - 4,800,000
A3700
2,000,000 - 10,000,000
A3800
2,000,000 - 10,000,000
A3810
8,000,000 - 10,000,000
A5200
3,000,000 - 15,000,000
A5500
3,600,000 - 18,000,000
A5600
5,000,000 - 25,000,000
A5800
6,000,000 - 30,000,000
A6800
7,000,000 - 35,000,000
A7600
8,400,000 - 42,000,000
A5800-B
30,000,000 - 38,000,000
A5600-B
20,000,000 - 25,000,000
A5500-B
18,000,000 - 23,000,000

<!-- 来源页 898 -->
型号
取值范围
A5200-B
16,000,000 - 20,000,000
A5100-B
9,000,000 - 10,000,000
A3800-B
8,000,000 - 10,000,000
A3700-B
8,000,000 - 10,000,000
K1280
400,000 - 4,800,000
K2580
2,000,000 - 10,000,000
K2780-A
1,400,000 - 7,000,000
K3280
3,000,000 - 15,000,000
K5180-A/K3280-
A
1,800,000 - 9,000,000
K5280-A
5,200,000 - 20,000,000
K5680-A/K5680-
A-GM
5,200,000 - 26,000,000
K6280-A
5,200,000 - 31,000,000
K6580
8,400,000 - 42,000,000
K2680-A/K2680-
A-GM
960,000 - 4,800,000
K2580-A
960,000 - 4,800,000
K2560-A
960,000 - 4,800,000
K2380-A/K2380-
A-GM
960,000 - 4,800,000
K1280-A
960,000 - 4,800,000
K6680
400,000 - 50,000,000
K7280
400,000 - 50,000,000
K7680
400,000 - 50,000,000
K7280-B
84,000,000 - 105,000,000
K6680-B
70,000,000 - 88,000,000
K6560-B
42,000,000 - 52,000,000
K6360-B/K6280-
B
20,000,000 - 25,000,000
K5680-B
18,000,000 - 23,000,000
K5280-B
9,000,000 - 12,000,000
K5180-B
16,000,000 - 20,000,000

<!-- 来源页 899 -->
型号
取值范围
K5160-B
9,000,000 - 12,000,000
注意: 对于K7680/K7280/K6680设备，由于其存在2个vSSM模块，使用exec session-adjust
vssm命令会同时调整2个vSSM模块的IPv4最大并发连接数，因此于K7680/K7280/KK6680设备
的IPv4最大并发连接数实际为100,000,000。
通过降低最大并发连接数优化内存分配
型号说明：
l
A系列设备所有型号
l
B系列设备所有型号
l
K系列部分设备（除K20803/K9180）
注意: 该功能涉及内存分配，可能会影响业务的正常运行，建议在山石网科技术支持人员的指导下
进行配置。
在防火墙系统中，CP(Control plane，控制平面)内存用于存储系统配置和管理产生的数据，DP(Data
plane，数据平面)内存用于存储系统流量转发和业务产生的数据。
如果在设备中开启过多的安全功能（如IPS、AV等）或者新建过多统计集，可能会占用大量CP内存。针对一
些内存较小的设备，可能就会由于CP内存不足而影响设备的正常启动和运行。为此，当该类设备处于业务低
峰期时，可以通过降低最大并发连接数来优化内存分配。降低最大并发连接数会释放出部分DP内存，释放出
的这部分DP内存将会分配给CP内存，从而提升CP内存，以避免因CP内存不足而导致的设备问题。
通过降低最大并发连接数优化内存分配，在任意模式下，使用以下命令：
exec session-adjust value cp
l
value - 将设备的最大并发连接数降低到指定值从而释放出部分DP内存，该部分DP内存将会分配给CP
内存。不同设备的最大并发连接数取值范围不同，用户可通过输入exec session-adjust命令后敲Tab
键，查看当前设备的最大并发连接数取值范围。
对于已经调整过内存分配的设备，如果遇到业务高峰期，为避免影响业务的正常运行，可以使用exec
session-adjust reset命令，恢复最大并发连接数默认值，此时CP内存大小也会恢复为默认值。

<!-- 来源页 900 -->
注意: 重启设备后，配置才能生效。

<!-- 来源页 901 -->
配置NetBIOS名字解析功能
StoneOS支持NetBIOS名字解析功能。开启该功能后，系统将自动获取设备所管理网络的所有主机注册的
NetBIOS主机名，并将其记录在设备缓存中，用于为设备其他功能模块提供IP地址到NetBIOS主机名的查询
服务。
当前版本，系统仅为流量日志的查询提供该功能。开启NetBIOS名字解析功能是流量日志中主机名称显示的
前提条件。如何使流量日志中显示主机名称，请参考《监控》的“设置流量日志的主机名称/用户名称的显示
状态”。
配置NetBIOS名字解析功能，请按照以下步骤进行操作：
1. 开启安全域的NetBIOS主机名查询功能。该安全域不能为连接WAN网的安全域。
2. 根据统计集统计的信息（IP地址）系统将自动进行NetBIOS查询。
查询过程可能会持续一段时间，查询结果将添加到NetBIOS缓存表中。系统每隔一段时间会重新进行一次查
询并更新查询结果。
注意: 只有开启了NetBIOS设置的PC才可以被查询到其主机名称。请参阅PC操作系统的详细说明
来获得开启NetBIOS功能的方法。
开启NetBIOS主机名查询功能
开启安全域的NetBIOS主机名查询功能，在安全域配置模式下，使用以下命令：
nbt-cache enable
在安全域配置模式下使用该命令no的形式关闭该功能：
no nbt-cache enable
使用zone zone-name命令进入安全域配置模式。
查询指定IP的NetBIOS主机名
用户可以通过指定主机的IP地址，实时查看该主机的NetBIOS主机名称和MAC地址。在全局配置模式下，使
用以下命令：
nbtstat ip2name ip-address [vrouter vrouter-name]

<!-- 来源页 902 -->
l
ip-address – 指定被查询的主机的IP地址。
l
vrouter vrouter-name – 指定被查询的主机所属的VR名称。如果没有指定VR，系统使用默认VR，即
trust-vr。
清除NetBIOS缓存数据
清除NetBIOS缓存数据，在全局配置模式下，使用以下命令：
clear nbt-cache [ip-address][vrouter vrouter-name]
l
ip-address – 指定IP地址。配置该参数，系统将清除与指定IP地址相关的NetBIOS缓存数据。如果不配
置该参数，系统将清除所有NetBIOS缓存数据。
l
vrouter vrouter-name – 指定VR名称。配置该参数，系统将清除属于指定VR的NetBIOS缓存数据。
如果没有指定VR，系统将清除所有VR下的NetBIOS缓存数据。
查看NetBIOS缓存数据
在任何模式下，使用以下命令查看NetBIOS缓存数据，包括IP地址、主机名称、MAC地址以及VR信息：
show nbt-cache [ip-address][vrouter vrouter-name]
l
ip-address – 指定IP地址。配置该参数，系统将显示与指定IP地址相关的NetBIOS缓存数据。如果不配
置该参数，系统将显示所有NetBIOS缓存数据。
l
vrouter vrouter-name – 显示属于指定VR的NetBIOS缓存数据。如果没有指定VR，系统将显示所有
VR下的NetBIOS缓存数据。

<!-- 来源页 903 -->
配置RESTful API上传文件的接口
系统支持配置使用/rest/file接口上传文件，在全局配置模式下，使用以下命令：
restful-api-control /rest/file {enable | disable}[version 5.5R4]
l
enable - 开启后，可以使用/rest/file接口上传文件，不对文件的后缀及大小进行检查，仅检查后缀与
实际文件是否匹配。
l
disable- 关闭后，无法使用/rest/file接口，上传文件将直接返回错误。默认情况下为关闭状态。
l
version 5.5R4 - 兼容5.5R4版本RESTful API的部分格式，具体请参考5.5R8P6及以上版本的
《RESTful API手册》。

<!-- 来源页 904 -->
清除指示灯告警提示
当设备前面板的PWR（电源指示灯）、STA（状态指示灯）以及ALM（告警指示灯）处于红色常亮告警状态
时，用户可以在设备恢复正常状态后，通过配置，手动清除指示灯的告警提示。
手动清除指示灯的告警提示，请在全局配置模式下使用以下命令：
clear led {PWR | STA | ALM}
l
PWR | STA | ALM - 指定清除电源指示灯（PWR）、状态指示灯（STA）以及告警指示灯（ALM）的告
警提示。
注意: K6580/K6280-GS设备仅支持通过clear led ALM命令清除告警指示灯的告警提示，不支持
清除电源指示灯和状态指示灯的告警提示。
自动清除ALM灯告警提示
当由于以下原因导致设备前面板ALM指示灯变成红色告警状态时，用户可以通过配置，使设备在恢复正常状
态时，自动清除ALM指示灯告警提示。
l
缺少电源模块
l
设备温度超过正常范围
l
风扇损坏
配置自动清除ALM灯告警提示功能，请在全局配置模式下使用以下命令：
led-alarm-autoclear
在全局配置模式下，使用no led-alarm-autoclear命令取消自动清除ALM灯告警提示功能配置。
注意: K6580/K6280-GS设备不支持自动清除ALM灯告警提示。

<!-- 来源页 905 -->
Deny Session功能
Deny Session功能能够在系统受到攻击时显著提高系统性能。正常情况下，系统尝试建立一个会话前，需
要进行很多相关处理，例如AD处理、SNAT/DNAT处理、策略规则匹配以及应用类别识别等（参考"数据包
处理流程" 在第22页），进行这些相关处理工作需要耗费大量的系统CPU资源，从而导致系统性能下降，同
时也给攻击者攻击设备系统提供了机会。针对这一问题，StoneOS提供Deny Session功能。
Deny Session的工作原理如下：配置Deny Session功能后，系统会为由于某些原因本不能建立会话的数
据包建立Deny Session，之后，当与已建立的Deny Session具有相同五元组的数据包进入设备后，会直
接与相应的Deny Session相匹配，系统进而会丢弃这些数据包。因此，通过使用Deny Session，系统性
能可以得到显著提高。
系统可以在以下情况下建立Deny Session：
l 未能通过AD（二层和三层IP地址欺骗攻击防护）检查。
l 未能找到匹配的策略规则。
l 未能找到匹配的转发或者逆向路由。
l 到设备本身的数据包被拒绝时。
l 当超出会话限制时。
在以下情况下，Deny Session将会被删除：
l Deny Session自行老化。建立的Deny Session不能够更新，因此一段时间以后会自行老化进而被删除。用户可
以指定该老化时间。
l 如果系统允许Deny Session的逆向流量建立正常会话，相应的Deny Session将会被删除。
配置Deny Session功能
Deny Session的配置需要在Flow配置模式下进行。进入Flow配置模式，在全局配置模式下，使用flow命
令。
指定Deny Session的类型
用户可以指定在何种情况下建立Deny Session。在Flow配置模式下使用以下命令：
deny-session deny-type {all | ad | policy | route | self | session-limit}
l all – 系统支持的五种情况下均建立Deny Session。
l ad – 当数据包未通过AD（二层和三层IP地址欺骗攻击防护）检查时建立Deny Session。

<!-- 来源页 906 -->
l policy – 当数据包未找到相匹配的策略规则或者匹配“拒绝”策略规则时建立Deny Session。
l route – 当数据包未找到相匹配的转发或者逆向路由时建立Deny Session。
l self – 当到设备自身的数据包被拒绝时建立Deny Session。
l session-limit – 当数据包超出设备配置的会话限制时建立Deny Session。
在Flow配置模式下使用该命令no的形式取消Deny Session类型的指定：
no deny-session deny-type {all | ad | policy | route | self | session-limit}
指定最大Deny Session
最大Deny Session数是指系统支持的可以建立的最大Deny Session的个数。指定最大Deny Session数，
在Flow配置模式下使用以下命令：
deny-session percentage number
l number – 指定Deny Session数占系统最大Session数的百分比。范围是0到10。0表示关闭Deny Session功
能。默认值是2，即默认最多可建立占总会话数2%的Deny Session。
在Flow配置模式下使用该命令no的形式恢复默认最大Deny Session数：
no deny-session percentage
指定超时时间
超时时间是指已建立的Deny Session的老化时间，即到达超时时间的Deny Session会自动从系统中删
除。指定Deny Session的超时时间，在Flow配置模式下，使用以下命令：
deny-session timeout time
l time – 指定超时时间，单位为秒。取值范围为1到3秒。默认为3秒。
在Flow配置模式下，使用该命令no的形式恢复默认超时时间：
no deny-session timeout
显示Deny Session配置信息
Deny Session配置信息包括Deny Session的类型、最大Deny Session数以及超时时间。查看Deny
Session的配置信息，在任何模式下使用以下命令：
show flow deny-session
显示Deny Session信息
查看系统中存在的Deny Session的具体信息，在任何模式下使用以下命令：

<!-- 来源页 907 -->
show session deny

<!-- 来源页 908 -->
Docker管理
型号说明：
l
支持：SG-6000-A系列平台。
l
支持：SG-6000-B系列平台。
l
支持：CloudEdge（云·界软件版本为StoneOS 5.5R10F6及其以后F版本、5.5R11P1及
其以后P版本、5.5R12及其以后版本）。
l
不支持：A2200、A1800、A1600-A、A1600、A200-A、A200G4-A、A200W-A、
A200WG4-A、A200、A200G4、A200W、A200WG4。
l
不支持：B600、B600G4、B600W、B600WG4。
Docker是一种开源的容器化平台，它可以将应用程序封装成一个独立的可移植的容器，使应用程序可以在不
同的环境中快速部署和运行。
StoneOS支持Docker管理功能，通过该功能，用户可以在系统中创建Docker，为Docker分配系统资源，
导入Docker镜像文件，并基于Docker运行容器应用。
注意: 当云·界安装有一块硬盘时，若从5.5R10F6之前版本升级至5.5R10F6及其以后版本，则不
支持Docker管理功能。如需使用该功能，请选择以下任一方法：
l
重新部署5.5R10F6及其以后版本的云·界，具体操作请参阅《云·界部署手册》。
l
为云·界再安装一块硬盘，具体操作请参阅《云·界部署手册》。建议在安装硬盘前，先备份系
统数据，以防止数据丢失。
Docker管理操作
用户可进行的Docker管理操作包括：
l 新建Docker
l Docker资源分配
l 指定访问接口
l 管理镜像文件

<!-- 来源页 909 -->
l 管理容器
l Docker全局配置
l 查看Docker信息
l 查看Docker全局配置信息
l 查看Docker占用存储信息
新建Docker
新建Docker，在全局配置模式下使用以下命令：
docker docker-name
l
docker-name - 指定需要创建的Docker名称，为2到31个字母或者数字的字符串。
执行该命令后，系统创建指定名称的Docker，并进入Docker配置模式。如果指定的名称已存在，则直接进
入Docker配置模式。在全局配置模式下使用no docker docker-name命令删除指定的Docker。删除
Docker时，会将Docker中的容器和镜像文件一起删除。
注意: 不同平台可以创建的Docker数量不同：
l
SG-6000-A5100及以上型号设备最多支持创建3个Docker，SG-6000-A5100以下型号设备
最多支持创建1个Docker，SG-6000-
A2200/A1800/A1600/A200/A200G4/A200W/A200WG4不支持创建Docker。
l
SG-6000-B600/B600G4/B600W/B600WG4不支持创建Docker，其它SG-6000-B系列型
号设备最多支持创建1个Docker。
l
SG-6000-VM04及以上型号设备最多支持创建3个Docker，SG-6000-VM04以下型号设备最
多支持创建1个Docker。
Docker资源分配
StoneOS中所有Docker共享系统的CPU、内存和端口资源。用户可以为每个Docker分配CPU、内存和端口
资源。
注意: 为了不影响系统中其它功能的正常运行，请根据系统的资源使用情况为Docker分配系统CPU
和内存资源。

<!-- 来源页 910 -->
分配CPU资源
配置Docker绑定的CPU核，在Docker配置模式下使用以下命令：
cpu cpu-number
l
cpu-number - 指定Docker绑定的CPU核。例如，如果cpu-number配置为2，则表示Docker和
Core2绑定。Docker默认绑定Core0。
多次执行以上命令将Docker绑定到多个CPU核。在Docker配置模式下使用no cpu cpu-number命令取消
Docker与指定CPU核的绑定。
注意: 默认情况下，新创建的Docker会绑定Core0。为防止容器运行导致Core0处于高负荷运行状
态，可以使用flow-core-num number命令释放系统数据层面占用的CPU核，供Docker使用。
例如，如果设备的CPU总核数为8核（Core0~Core7），通过配置flow-core-num 4命令指定系
统数据层面占用4个CPU核（Core0~Core3），剩下的Core4~Core7就为Docker可以绑定的CPU
核。对于仅包含2个CPU核的设备，由于系统不支持flow-core-num number命令，所以Docker
只能绑定Core0。
分配内存资源
配置Docker可以使用的最大内存，在Docker配置模式下使用以下命令：
memory memory-size
l
memory-size - 指定Docker可以使用的最大内存。可以使用的最大内存默认为256 MB。可以使用的
最大内存的配置上限为控制层面内存的50%，用户可以使用show memory de命令查看控制层面内存大
小及使用情况。
在Docker配置模式下使用no memory命令恢复默认内存上限。
配置端口映射
Docker通信需要配置端口映射。配置Docker端口映射，在Docker配置模式下使用以下命令：
port-map {tcp | udp} host-port port-number docker-port port-number
l
tcp | udp - 指定端口的协议类型，可以为TCP或者UDP。
l
host-port port-number - 指定Docker的宿主机端口号。取值范围为36000至36008。
l
docker-port port-number - 指定Docker端口号。取值范围为0至65535。

<!-- 来源页 911 -->
在Docker配置模式下使用no port-map {tcp | udp} host-port port-number取消Docker的端口映射配
置。
指定访问接口
用户可以指定用来访问Docker的接口，在Docker配置模式下使用以下命令：
access-interface interface-name
l
interface-name- 指定访问Docker的接口名称，MGT接口和HA接口除外。
如需指定多个接口，重复配置该命令，最多可以允许指定3个接口。
在Docker配置模式下使用no access-interface interface-name取消Docker的访问接口配置。
管理镜像文件
用户可以对Docker镜像文件进行管理，包括导入镜像文件，还可以删除镜像文件或者将镜像文件设置为启动
首选。
导入镜像文件
用户可以通过FTP、TFTP服务器、SFTP服务器或FTPS服务器将Docker镜像文件导入到Docker中。
注意: 每个Docker中最多允许导入3个镜像文件。
从FTP服务器导入Docker镜像文件
从FTP服务器导入Docker镜像文件，在执行模式下使用以下命令：
import docker-image-file docker-name from ftp server ip-address user user-name
password password [vrouter vrouter-name] file-name
l
docker-name - 指定导入镜像文件的Docker名称。
l
ip-address – 指定FTP服务器的IP地址。
l
user user-name password password – 指定FTP服务器的用户名和密码。
l
vrouter-name - 为指定的VRouter导入Docker镜像文件。
l
file-name – 指定导入的镜像文件的名称。
从TFTP服务器导入Docker镜像文件
从TFTP服务器导入Docker镜像文件，在执行模式下使用以下命令：

<!-- 来源页 912 -->
import docker-image-file docker-name from tftp server ip-address [vrouter vrouter-name]
file-name
从SFTP服务器导入Docker镜像文件
从SFTP服务器导入Docker镜像文件，在执行模式下使用以下命令：
import docker-image-file docker-name from sftp server
ip-address [vrouter vrouter-name]
[user user-name password password] [file-name]
从FTPS服务器导入Docker镜像文件
从FTPS服务器导入Docker镜像文件，在执行模式下使用以下命令：
import docker-image-file docker-name from sftp server ip-address [vrouter vrouter-name]
[user user-name password password] [file-name]
删除镜像文件或者设置启动首选
删除镜像文件或者设置启动首选，在执行模式下使用以下命令：
exec docker docker-name {delete | set-start-first} file-name
l
docker-name - 指定Docker名称。
l
delete | set-start-first - 指定操作类型，包括删除（delete）镜像文件或者将镜像文件设置为启动首
选（set-start-first）。系统中正在运行的镜像文件不可以被删除。将镜像文件设置为启动首选后，设
备重启时优先选择启动首选镜像文件加载镜像。
l
file-name - 指定镜像文件名称。
管理容器
用户可以对Docker中运行的容器进行管理，包括运行、重载、停止、启动、重启或者移除容器。
运行/重载容器
运行或者重载容器，在执行模式下使用以下命令：
exec docker docker-name { run | reload-run} file-name
l
docker-name - 指定Docker名称。
l
run | reload-run - 指定操作类型，包括运行（run）或者重载（reload-run）容器。在没有创建容器
的情况下，使用运行容器命令，加载镜像文件并运行容器；在已经创建了容器的情况下，使用重载命

<!-- 来源页 913 -->
令，删除已有容器，然后加载镜像文件并运行容器。
l
file-name - 指定镜像文件名称。
停止/启动/重启/移除容器
停止、启动、重启或者移除容器，在执行模式下使用以下命令：
exec docker docker-name {stop | start | restart | remove}
l
docker-name - 指定Docker名称。
l
stop | start | restart | remove - 指定操作类型，包括停止（stop）、启动（start）、重启
（restart）或者移除（remove）容器。
Docker全局配置
Docker全局配置包括Docker网络的网段地址配置。Docker通过网桥连接容器网络和宿主机网络，用户需
要配置Docker网络的网段地址，该网段内的可用IP地址将会用于宿主机网络内部接口和容器内部接口。如果
未配置该网段地址，Docker无法正常使用。
配置Docker网络的网段地址，在全局配置模式下，使用以下命令：
docker-config network {ipv4-address/mask | ipv4-address netmask | ipv6 ipv6-
address/prefix }
l
ipv4-address/mask | ipv4-address netmask - 指定Docker网络的网段IPv4地址和子网掩码。
l
ipv6 ipv6-address/prefix- 指定Docker网络的网段IPv6地址和前缀长度。配置IPv6网段地址后，
容器内部将会支持IPv6地址。
在全局配置模式下使用no docker-config network [ ipv6 ]取消Docker网络的网段地址配置。
注意:
l
为保证Docker正常使用，请必须配置网段IPv4地址和子网掩码。
l
指定的网段地址不能和trust-vr下的接口地址冲突。
查看Docker信息
在任何模式下，使用以下命令查看Docker信息：
show docker docker-name
l
docker-name - 指定需要查看的Docker名称。

<!-- 来源页 914 -->
示例：
hostname# show docker test
------------------------------------------------------------
name : test ( Docker名称)
memory limit : 256M ( Docker的内存限制)
cpu : core0 ( Docker绑定的CPU核)
port map : ( 端口映射信息，以下参数分别为：协议类型
宿主机端口:Docker端口)
tcp 36001:10
Image file(D: default; S: start first; L loaded by docker) ( 镜像文件，
D为默认镜像文件；S为启动首选镜像文件；L为当前加载的镜像文件)
------------------------------------------------------------
busybox_latest.dat
busybox_1.1.1.tar SL
------------------------------------------------------------
Status : exited ( 容器的状态，init为初始化完成；running为运行中；exited为已
创建，未运行)
Image name : busybox ( 镜像名称)
Image version : 1.1.1 ( 镜像版本)
Start at : 2023-08-08 14:45:18 ( 容器启动时间)
Finish at : 2023-08-08 14:45:46 ( 容器停止时间)
==============================
查看Docker全局配置信息
在任何模式下，使用以下命令查看Docker全局配置信息：
show docker-config
示例：
hostname# show docker-config
Subnet of docker network: 1.1.2.0/28 ( Docker网络的IPv4网段地址)
IPv6 subnet of docker network: 2001:0db8:85a3:08d3::1/64 ( Docker网络
的IPv6网段地址)

<!-- 来源页 915 -->
查看Docker占用存储信息
当Docker文件占用的内存超过阈值后，设备将停止容器的运行。在任何模式下，使用以下命令查看Docker
占用设备存储的相关信息：
show docker-info
示例：
hostname# show docker-info
Storage Limit of containers:
threshold : 1374MB ( 设备的存储阈值)
current used : 0MB(0.0%) ( Docker当前使用的存储空间大小及百分比)
Total size of user imported image files: 0MB ( Docker导入的所有镜像文件
的大小)

<!-- 来源页 916 -->
切换SIOM模块工作模式
型号说明：X系列，K系列设备支持该功能：
l
X系列所有型号设备
l
K系列部分型号设备：SG-6000-K20803/K9180
SIOM模块有两种工作模式，分别为SIOM模式和IOM模式，默认工作在SIOM模式。SIOM模式下，SIOM模
块既可以收发报文，也可以进行业务处理；IOM模式下，SIOM模块仅收发报文，不进行业务处理。针对不同
的业务场景，用户可以灵活切换SIOM模块的工作模式，以提升设备性能。
切换SIOM模块工作模式为IOM模式，在全局配置模式下，使用以下命令：
siom-switch-to-iom slot slot-number
l slot-number - 指定SIOM模块所在的槽位号。用户可通过在slot参数后使用Tab键，查看已安装SIOM模块的槽
位号。
在全局配置模式下，使用no siom-switch-to-iom slot slot-number命令切换SIOM模块工作模式为
SIOM模式。
注意:
l
切换SIOM模块的工作模式后，需要重启设备使配置生效。
l
若设备上仅插入一个SIOM模块，该SIOM模块的工作模式将无法切换为IOM模式，即必须确保
设备上至少有一个SIOM模块工作在SIOM模式下。
l
无论SIOM模块工作在SIOM模式还是IOM模式，均不支持与IOM模块/SSM模块混插。
l
SIOM模块热插入设备槽位后，工作模式会自动变为该槽位已配置的工作模式，无需重启设备或
重新配置。
l
该功能与session-schedule-mode local-slot命令互斥，二者不能同时配置。

<!-- 来源页 917 -->
上电或下电SIOM模块
型号说明：
l
X系列所有型号设备
l
K系列部分设备：SG-6000-K20803/K9180
下电SIOM模块
设备正常运行至少需要一个SIOM模块。当SIOM模块存在冗余，且业务空闲时，用户可以通过以下两种方式
给指定SIOM模块进行下电，以达到节约能源的目的。
l
手动拔出SIOM模块：SIOM模块支持热插拔。用户可以在不影响业务的情况下拔出SIOM模块，拔出后的
SIOM模块会自动下电。
l
使用命令：与手动拔出SIOM模块相比，该方式可以免去人力操作的繁琐，实现机房的远程便捷运维。配
置流程如下：
1.
使用show module命令，查看设备已插入的SIOM模块状态。允许使用命令进行下电的SIOM模块
需处于Booting、Loading或Online状态。
2.
在任意模式下，使用power off slot slot-id命令，执行SIOM模块下电操作。下电后，SIOM模
块的状态显示为PowerDown。
上电SIOM模块
如需重新启用已下电的SIOM模块，可以通过以下两种方式重新上电。上电后，SIOM模块进入启动流程，正
常情况下，经过一段时间后状态会显示为Online。
l
重新插入SIOM模块：将已下电的SIOM模块从设备插槽中拔出，然后再重新插入，SIOM模块会自动上
电。
l
使用命令：在任意模式下，使用power on slot slot-id命令，即可使处于PowerDown状态的SIOM模
块重新上电。

<!-- 来源页 918 -->
开启IP分片报文在IOM模块或SIOM模块的重组功能
型号说明：X系列，K系列设备支持该功能：
l
X系列所有型号设备
l
K9180
对于使用IOM/SIOM模块的设备，默认情况下，进入设备的数据包IP分片报文会在IOM/SIOM模块中进行重
组和转发。当IP分片报文的首片报文和非首片报文从不同的IOM/SIOM模块进入设备时，由于非首片报文重
组依赖于首片报文，因此在报文传输过程中，可能会出现非首片报文的丢包，从而造成流量转发失败。
为了避免该问题，保证流量可以正常转发，系统支持开启或关闭IP分片报文在IOM/SIOM模块的重组功能。
开启后，IP分片报文不会在IOM模块/SIOM模块进行重组，而是直接将IP分片报文上送至SSM业务模块进行
处理。
开启/关闭IP分片报文在IOM模块或SIOM模块的重组功能，在全局配置模式下，使用以下命令：
l
开启：fragment centralized-mode
l
关闭：no fragment centralized-mode
默认情况下，该功能为关闭状态，即IP分片报文会在IOM/SIOM模块进行重组。

<!-- 来源页 919 -->
配置下发的最长重试时间
针对系统部分功能配置，当执行配置命令后将会自动暂时将配置锁住，可能会导致后续功能配置命令下发执
行失败的情况。针对此类情况，系统支持指定配置下发的最长重试时间，在该时间内将持续重新下发配置，
超过该时间后，如果配置仍下发失败，则返回错误信息。如不指定，系统默认在5秒内持续重新下发配置。
指定配置下发的最长重试时间，在任意模式下，使用以下命令：
exec retrytime times
l
times – 指定最长重试时间。范围是0到3600秒。重试时间指定为0时，表示不重新下发配置，立即返回
错误信息。
配置PHP-FPM子进程个数
PHP-FPM（FastCGI Process Manager）是一个用于管理PHP进程的FastCGI管理器，其子进程在Web应
用程序中发挥着重要作用。在高流量的Web环境中，当多个用户同时发起请求时，PHP-FPM子进程可以并
发地处理这些请求，确保网站的响应速度和稳定性。同时每个子进程相互独立运行，一个子进程出现问题不
会影响其他子进程的正常工作。
例如：当查询的日志数量过大时，系统页面会长时间停留在查询阶段，可能会导致其他用户登录系统后无法
操作系统页面。为了避免这一情况，用户可以配置双进程来同时处理日志查询和页面操作。
配置PHP-FPM子进程个数，在全局配置模式下，使用以下命令：
php worker-num number
l
number – 指定PHP-FPM子进程的个数，取值范围为1-2个，默认为1个。
恢复默认PHP-FPM子进程个数，在全局配置模式下，使用以下命令：
no php worker-num

<!-- 来源页 920 -->
管理SSH算法
SSH连接在协商阶段会使用多种SSH算法进行协商。为了防范潜在的安全风险，当某个SSH算法存在安全漏
洞时，用户可以主动选择关闭该算法，从而避免其对业务造成不良影响。OpenSSH库默认会禁用一些不安
全的算法，这是为了在默认配置下就提供一个较为安全的连接环境。已手动关闭或默认禁用的SSH算法在密
钥协商阶段将不会被使用，后续如果漏洞得到修复，用户也可以根据需要重新启用这些SSH算法。目前系统
支持管理的SSH算法类型包括：密钥交换算法（kex algorithms）、服务器主机密钥算法（server host
key algorithms）、报文加密算法（encryption algorithms）、完整性校验算法（mac
algorithms）。用户可以根据实际需求管理上述SSH算法，提高SSH连接过程的安全性和稳定性。
管理SSH算法包括：
l 关闭指定SSH算法
l 重新启用SSH算法
l 查看已关闭的SSH算法
关闭指定SSH算法
关闭指定的SSH算法，在全局配置模式下，使用以下命令：
no ssh server algorithms type {encryption | kex | mac | server-host -key} algorithm-name
l
algorithm-name - 指定需要关闭的SSH算法的具体名称。用户可通过在{encryption | kex | mac |
server-host -key} 参数后使用Tab键，查看当前类型下包含的所有SSH算法名称。
重新启用SSH算法
注意: OpenSSH库默认禁用的算法存在一定安全风险，如果用户自行启用这些算法，则可能导致
SSH连接出现风险，请谨慎操作！
重新启用SSH算法，在全局配置模式下，使用以下命令：
ssh server algorithms type {encryption | kex | mac | server-host -key} algorithm-name
l
algorithm-name - 指定需要重新启用的SSH算法的具体名称。用户可通过在{encryption | kex |
mac | server-host -key} 参数后使用Tab键，查看当前类型下可以重新启用的SSH算法名称。

<!-- 来源页 921 -->
查看已关闭的SSH算法
查看已关闭的SSH算法，在任意模式下，使用以下命令：
show ssh server algorithms disable
以下是返回结果示例：
hostname#show ssh server algorithms disable
kex_algroithms: diffie-hellman-group14-sha256
server_host_key_algorithms: rsa-sha2-512
encryption_algorithms: aes128-ctr
mac_algorithms: umac-64-etm@openssh.com

<!-- 来源页 922 -->
调整设备规格容量
当业务临近上线节点发现设备规格不足时，用户可根据业务需求，动态调整设备各功能模块的规格参数（如
策略数量、地址簿容量等），快速补足规格缺口，使设备即时满足上线要求，有效保障业务按时投产运行，
进而规避因规格瓶颈导致的延期风险。在调整设备规格容量后，需立即重启设备以确保更改生效。若进行规
格调整的设备与其他设备互为主备时，两台设备均需重启。
当设备在规格调整后未及时重启时，系统将每隔十五分钟生成一条事件日志，以提示用户需要重启设备以应
用新的规格设置。
各功能模块的规格容量最大支持调整为系统默认规格的2倍，不同平台支持调整的功能模块类型及其默认规
格可能存在差异，具体可调整的范围请以各平台的实际情况为准。例如某平台地址簿默认规格为10万条，系
统最大可将地址簿容量调整为20万条。
提示: 随着设备功能规格的扩展，其在运行过程中的内存占用率及CPU使用率均会有所增长。具体
的增长幅度受设备的具体配置、所启用的功能类型、处理的数据流量规模等多种因素的共同影响，
因此难以提供准确的量化评估。请谨慎使用该功能，以免因内存不足或CPU使用率过高导致业务无
法正常运行。如有疑问，请及时联系山石网科技术支持人员。建议用户结合实际使用场景观察设备
运行状态，以便更直观地了解性能变化情况。
调整设备规格容量，请按照以下步骤进行配置：
1. 修改设备规格容量：
在全局配置模式下，使用capacity capacity-name number命令，修改指定规格参数的容量。
l
capacity-name - 指定需要修改的规格参数名称。用户在进行配置时，可通过Tab键补全或查看
所有支持调整的规格参数名称。
l
number - 指定该规格参数调整后的容量大小。
注意:
l
在进行规格调整时，调整的规格值需大于设备当前已使用的规格容量。例如：某设备地
址簿功能当前已配置使用了10万条，若对该设备地址簿规格进行调整，调整后的规格值
则必须大于10万。
l
为保障设备正常运行，不建议在同一台设备上对多种规格进行调整。

<!-- 来源页 923 -->
l
当VSYS中存在资源配额时，如需调整设备规格容量，调整的规格值需大于等于所有
VSYS配额中的最大值。
l
当设备故障需切换至同配置备用设备时，在导入配置文件后，必须将备用设备的规格容
量手动调整至切换前的配置值，以确保业务连续性。
在全局配置模式下，使用no capacity capacity-name命令，恢复默认规格。
配置示例（调整策略数量）：
hostname(config)# capacity max_policy_num
<1-120000> The modified number
hostname(config)# capacity max_policy_num 120000
The capacity has been modified, please reboot the system
2. （可选）配置设备重启异常应对机制：为避免因调整后的规格过大引发内存不足等问题，从而导致设备
反复重启的情况发生，请在重启设备之前，配置设备重启异常应对机制。系统默认为回退到默认规格，
即设备在规格调整后重启异常时，系统会自动将设备规格恢复到默认规格并重启设备。
在全局配置模式下，使用以下命令，配置设备重启异常应用机制：
capacity restore-method {default | last-modify}
l
default - 回退到默认规格。该选项为系统默认配置。
l
last-modify - 回退到上一次成功启动配置。当设备在规格调整后重启异常时，系统会自动将设
备规格恢复至最近一次成功启动的规格配置。如果无法成功回退到该配置，系统将自动回退至默认
规格，以确保设备能够正常运行。此机制适用于设备至少有一次规格调整成功的场景。
3. 重启设备：在执行模式下，使用reboot命令，重启设备。或者登录防火墙WebUI管理界面，选择“系统> 设备
管理> 设置及操作> 系统操作”，然后点击“重启设备”。
4. 查看规格修改项，并验证修改后的规格是否生效：
在任意模式下，使用show capacity dynamic命令，查看当前系统已修改的规格参数，并验证修改后
的规格是否生效。
示例：
hostname# show capacity dynamic
capacity will restore to the state of the last successful boot when device break down
Capacity name             Description                   Value       Need reboot        Reboot
value          Used value

<!-- 来源页 924 -->
=================================================================
max_policy_num:       Max policy
entries        60000              Y                       120000                         4;
显示信息
说明
Capacity name
显示调整的规格参数名称。
Description
显示对应的规格描述。
Value
显示设备当前的规格大小。
Need reboot
显示是否需要重启设备。
l Y：表示需要重启设备，即该规格参数调整未生效。
l N：表示无需重启设备，即该规格参数调整已生效。
Reboot value
显示重启后的设备规格大小。
Used value
显示设备当前已使用的规格大小。
