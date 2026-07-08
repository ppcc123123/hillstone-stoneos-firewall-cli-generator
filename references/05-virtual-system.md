# 虚拟系统

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 8 虚拟系统
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 925 -->
8 虚拟系统
虚拟系统（Virtual System），简称为VSYS，能够将一台设备在逻辑上划分成多个虚拟防火墙，每个虚拟
防火墙系统都可以被看成是一台完全独立的设备，拥有独立的系统资源，具备防火墙的大部分功能。每个虚
拟防火墙系统之间相互独立，不允许直接相互通信。
VSYS具有以下特征：
l 每个VSYS拥有独立的管理员；
l 每个VSYS拥有独立的虚拟路由器、安全域、地址簿、服务簿等；
l 每个VSYS可以拥有独立的物理接口或者逻辑接口；
l 每个VSYS拥有独立的安全策略。
l 每个VSYS拥有独立的日志。
型号说明：
l
不支持：A系列SG-6000-A1100、SG-6000-A1000、SG-6000-A200、SG-6000-
A200W、SG-6000-A200G4、SG-6000-A200WG4
l
不支持：SD-WAN系列全部型号
l
不支持：B系列SG-6000-B2000、SG-6000-B600、SG-6000-B600W、SG-6000-
B600G4、SG-6000-B600WG4
注意: 不同型号的设备支持的最大VSYS个数不同，如需增加支持的VSYS个数，请向销售人员购买
相应的许可证。
本章节包含以下内容：
l "虚拟系统管理员" 在第924页
l "VSYS对象" 在第925页
l 配置VSYS
l 导入/导出VSYS配置文件

<!-- 来源页 926 -->
虚拟系统管理员
每个VSYS都拥有自己独立的管理员。根VSYS中的管理员称为根系统管理员，非根VSYS中的管理员称为非根
系统管理员。其角色分为系统管理员（Administrator）、系统管理员（只读）（Administrator-readonly）、系统操作员（Operator）和系统审计员（Auditor）四种。关于如何配置管理员及管理员权限，
请参阅《系统管理》的“配置系统管理员”。
创建VSYS管理员并进行相关配置时，需要遵循以下原则：
l 管理员名称中不能包含“\”符号。
l 非根系统管理员可以通过两种方式创建：一种为非根系统系统管理员直接登录进行创建，另一种为由根系统管理
员登录后进入非根VSYS进行创建。
l 根系统管理员登录后，进入根VSYS，可以切换到非根VSYS并对该非根VSYS进行配置。
l 非根系统管理员登录后，进入到该非根VSYS，不能进入根VSYS。
l 每个VSYS的管理员名称仅在本VSYS中唯一，两个不同VSYS中可以有相同名称的管理员，登录时，必须在用户名
中指定所属VSYS，格式为“vsys_name\admin_name”，如果不指定所属VSYS，默认为根VSYS。
下表为VSYS管理员的详细权限列表。
功能
权限
根VSYS
系统管理
员
根VSYS
系统管理
员（只
读）
根VSYS
系统操作
员
根VSYS
系统审计
员
非根
VSYS系
统系统
管理员
非根
VSYS系
统管理
员（只
读）
非根
VSYS系
统操作
员
非根
VSYS系
统审计员
配置（包括保存配
置）
√
χ
√
χ
√
χ
√
χ
管理员配置
√
χ
χ
χ
√
χ
χ
χ
恢复出厂配置
√
χ
χ
χ
χ
χ
χ
χ
删除配置文件
√
χ
√
χ
√
χ
√
χ
回退起始配置信息
√
χ
√
χ
√
χ
√
χ
重启设备
√
χ
√
χ
χ
χ
χ
χ
查看配置信息
√
√
√
χ
只能查
看自己
当前
VSYS配
置信息
只能查
看自己
当前
VSYS配
置信息
只能查
看自己
当前
VSYS配
置信息
χ

<!-- 来源页 927 -->
功能
权限
根VSYS
系统管理
员
根VSYS
系统管理
员（只
读）
根VSYS
系统操作
员
根VSYS
系统审计
员
非根
VSYS系
统系统
管理员
非根
VSYS系
统管理
员（只
读）
非根
VSYS系
统操作
员
非根
VSYS系
统审计员
查看日志信息
√
√
χ
√
√
√
χ
√
修改当前管理员密
码
√
√
√
√
√
√
√
√
import命令
√
χ
√
χ
√
χ
√
χ
export命令
√
√
√
√
√
√
√
√
clear命令
√
√
√
√
√
√
√
√
ping/traceroute命
令
√
√
√
χ
√
√
√
χ
debug命令
√
√
√
χ
χ
χ
χ
χ
debug命令
√
χ
√
χ
χ
χ
χ
χ
exec命令
√
√
√
√
√
√
√
√
terminal width命
令
√
√
√
√
√
√
√
χ
VSYS对象
本节主要介绍VSYS的对象，包括根VSYS和非根VSYS、VRouter、VSwitch、安全域和接口。
根VSYS和非根VSYS
系统默认有一个根VSYS（Root VSYS），根VSYS不能被删除。安装虚拟系统许可证并重启设备后，用户可
以创建或者删除非根VSYS（Non-root VSYS）。
创建或者删除VSYS时，需要遵循以下原则：
l 只能在根VSYS中创建或者删除非根VSYS。
l 只有根VSYS系统管理员和根VSYS系统操作员才能创建或者删除VSYS。关于管理员权限的详细信息，请参阅"虚
拟系统管理员" 在第924页。
l 当创建一个非根VSYS时，系统自动创建与该VSYS相对应的下列对象：

<!-- 来源页 928 -->
l 一个非根VSYS系统管理员，名称为admin，密码为vsys_name-admin
l 一个VRouter，名称为vsys_name-vr
l 一个三层安全域，名称为vsys_name-trust
例如，创建vsys1时，系统自动创建一个非根VSYS系统管理员，该管理员的默认用户名为
vsys1\admin，默认密码为vsys1-admin；一个名称为vsys1-vr的默认VRouter、一个名称为vsys1-
trust的三层安全域，该安全域自动绑定到vsys1-vr上。
l 当删除一个非根VSYS时，VSYS中的所有对象均会被删除。
l 根VSYS拥有默认VSwitch，即VSwitch1，创建非根VSYS时，不会创建默认VSwitch，因此，在非根VSYS中创建
二层安全域时，需要先创建属于该VSYS的VSwitch。在非根VSYS中创建的第一个VSwitch即为该VSYS的默认
VSwitch，该VSYS中创建的二层安全域会自动绑定到该默认VSwitch。
VRouter、VSwitch、安全域和接口
VSYS中的VRouter、VSwitch、安全域和接口对象具有专有和共享属性。具有专有属性的对象称为专有对
象；将具有共享属性的对象经过相关配置后即成为共享对象。
专有对象和共享对象有如下特征：
l 专有对象：专有对象专属于某个VSYS，不可以被其它VSYS引用。根VSYS和非根VSYS中均可包含专有对象。
l 共享对象：共享对象可被多个VSYS共享。共享对象只能属于根VSYS，并且只能在根VSYS中进行配置；非根
VSYS只能引用共享对象，不能对其进行配置。共享对象的名称必须全局唯一，任何一个VSYS中的对象都不可以
与同类共享对象重名。
VSYS中专有及共享的VRouter、VSwitch、安全域和接口对象之间的引用关系如下图所示。
如上图所示，系统中包含三个VSYS：根VSYS（Root VSYS）、VSYS-A和VSYS-B。根VSYS中包含共享对
象和专有对象，共享对象包括共享VRouter（Shared VRouter）、共享VSwitch（Shared VSwitch）、
共享三层安全域（Shared L3-zone）、共享二层安全域（Shared L2-zone）和共享接口（Shared IF1
和Shared IF2）。

<!-- 来源页 929 -->
VSYS-A和VSYS-B中只包含专有对象，但其专有对象可以引用根VSYS中的共享对象。比如，VSYS-A中的安
全域A-zone2引用根VSYS中的Shared Vrouter；VSYS-B中的接口B-IF3引用根VSYS中的Shared L2-
zone。
l 共享VRouter：包含根VSYS中共享以及专有的三层域。将具有共享属性的三层域绑定到共享VRouter中，该域即
成为共享域。
l 共享VSwitch：包含根VSYS中共享以及专有的二层域。将具有共享属性的二层域绑定到共享VSwitch中，该域即
成为共享域。
l 共享域：共享域分为二层共享域和三层共享域，二层共享域需要将具有共享属性的域绑定到共享VSwitch，三层
共享域需要将具有共享属性的域绑定到共享VRouter。共享域可以包含根VSYS和非根VSYS中的接口。所有功能
域（如HA功能域）不可共享。
l 共享接口：将根VSYS中的接口绑定到共享域以后，该接口自动变为共享接口。
注意: 只有系统管理员或者系统操作员才能创建或者删除接口。接口及其子接口的创建和删除必须
在同一个VSYS下进行。
配置VSYS
VSYS配置包括：
l 创建非根VSYS
l 创建VSYS Profile
l 启用/禁用CPU资源配额
l 绑定Profile到VSYS
l 配置共享属性
l 导入/导出物理接口
l 分配逻辑接口
l 绑定监测对象
l 监测指定VSYS状态
l 回退配置信息（非根VSYS）
l 配置VSYS日志功能
l 配置跨VSYS流量转发功能

<!-- 来源页 930 -->
l 显示VSYS信息
l 显示VSYS Profile信息
创建非根VSYS
根系统管理员能够创建非根VSYS。创建非根VSYS，在根VSYS的全局配置模式下使用以下命令：
vsys vsys-name
l
vsys-name – 指定需要创建的VSYS实名，为1到23个字符的字符串，名称不能为root（root为保留名
称），且不能包含“\”字符。
执行该命令后，系统创建指定名称的非根VSYS，并且进入该VSYS的配置模式。如果指定的名称已存在，则
直接进入该VSYS的配置模式。在根VSYS的全局配置模式下使用no vsys vsys-name命令删除指定的
VSYS。
配置非根VSYS的别名
由于系统不允许修改非根VSYS的实名，导致用户需要变更非根VSYS的实名时，会产生较大的工作量并且对
用户业务造成影响。为了解决这一问题，系统提供配置非根VSYS别名的功能，从而满足了用户变更非根
VSYS名称的需求，也避免了对非根VSYS承载业务的影响。
默认情况下，非根VSYS的别名为空。用户可根据需要，为非根VSYS配置别名或修改别名。在非根VSYS的配
置模式下，使用以下命令：
alias alias_name
l
alias_name - 指定该非根VSYS的别名。该别名应为1到127个字符的字符串，可以包含小写字母a-z、
大写字母A-Z、数字0-9、连字符‘-’和下划线‘_’，且必须以英文字母或数字开头。名称不能为root
（root为保留名称）。
在非根VSYS的配置模式下，使用该命令no的形式删除该非根VSYS的别名：
no alias
注意:
l
创建非根VSYS时，指定的实名不能与其他非根VSYS别名或实名重复。
l
配置非根VSYS别名时，指定的别名不能与其他非根VSYS别名或实名重复。
配置非根VSYS的描述信息
用户可根据需要，为非根VSYS配置描述信息。在非根VSYS的配置模式下，使用以下命名：

<!-- 来源页 931 -->
description string
l
string – 指定描述信息内容。
在非根VSYS的配置模式下，使用该命令no的形式取消描述信息的指定：
no description
创建VSYS Profile
StoneOS中的每个VSYS在功能上相互独立，但共享系统资源，如共享CPU、会话数、安全域数、策略数、
SNAT规则数、DNAT规则数、会话限制规则数、缓存、URL资源和IPS资源等。根系统管理员可以创建VSYS
Profile，并通过Profile设置VSYS中各项系统资源的预留配额和最大配额。预留配额即系统为每个VSYS预
留的资源值；最大配额即每个VSYS可获得的最大资源值。所有VSYS分配的每种资源预留配额总和不能超过
系统的整体限制（Capacity），且所有VSYS实际分配的每种资源总和不能超过系统的整体限制
（Capacity）。
创建VSYS Profile，在根VSYS全局配置模式下使用以下命令：
vsys-profile vsys-profile-name
l
vsys-profile-name – 指定需要创建的VSYS Profile名称，为1到31个字符的字符串。
执行该命令后，系统创建指定名称的VSYS Profile，并且进入VSYS Profile配置模式；如果指定的名称已存
在，则直接进入VSYS Profile配置模式。在根VSYS全局配置模式下使用该命令no的形式删除指定的VSYS
Profile：
no vsys-profile vsys-profile-name
注意:
l
系统允许最多创建128个VSYS Profile。
l
根VSYS的默认Profile（root-vsys-profile）和非根VSYS的默认Profile（default-vsysprofile）都不可以被删除和编辑。
l
删除VSYS Profile之前必须删除所有引用该Profile的VSYS。
设置资源配额
用户可对VSYS资源的最大配额和预留配置进行配置。资源配额包括VSYS中CPU（cpu）、会话数
（session）、安全域个数（zone）、关键字数（keyword）、关键字类别（keyword-category）、策
略数（policy）、SNAT规则数（snat）、DNAT规则数（dnat）、会话数（session）、会话限制规则数
（session-limit）、统计集（statistic-set）、新建连接速率（cps）和IPSec VPN隧道数（tunnel-

<!-- 来源页 932 -->
ipsec）。
设置资源配额，在VSYS Profile配置模式下使用以下命令：
{cpu | session | zone | keyword {simple | regexp} | keyword-category | policy | snat | dnat |
session | session-limit | statistic-set {non-session-based | session-based} | tunnel-ipsec | cps
| scvpn-user} max max-num [reserve reserve-num] [alarm alarm-num]
l
{simple | regexp} - 该关键字为keyword专用，simple用来指定完全匹配类型的关键字，regexp用
来指定正则匹配类型的关键字。
l
max max-num – 指定VSYS资源的最大资源配额。最大配额和预留配额根据不同平台取值范围不同。
预留配额不能超过最大配额。各资源的最大配额取值范围以及预留配额的最小值请参见下表。
l
reserve reserve-num - 指定VSYS资源的预留配额。
l
alarm alarm-num – 该参数为CPU专用。配置该参数后，当CPU使用率超过指定百分比时，系统产生
报警日志。取值范围为50到99。
系统资源
最大配额（max max-num）取值范围
预留配额（reserve
res-num）最小值
CPU利用率（1秒内使用
CPU的资源）
1 – 10000
0
会话数
min (max-num①, 256) – max-num①
0
安全域数
（max-num①-res-num③）– maxnum①
0
每个关键字类别中可添加的
关键字数
l
完全匹配类型：0 – max-num①
l
正则匹配类型：0 – 10
0
关键字类别数
0 – max-num①
0
策略数
0 – max-num①
0
SNAT规则数
0 – max-num1②
0
DNAT规则数
0 – max-num1②
0
会话限制规则数
l
根VSYS Profile：固定值128
l
非根VSYS Profile：0 – 118
l
根VSYS Profile：
固定值10
l
非根VSYS
Profile：0

<!-- 来源页 933 -->
系统资源
最大配额（max max-num）取值范围
预留配额（reserve
res-num）最小值
统计集
0 – 32
0
IPSec隧道数
0 – max-num①
0
新建连接速率
10-50000000
--
SCVPN用户数
0 – max-num①
0
max-num①: 为该模块的整体Capacity限制。
max-num1②: 为该模块每个VSYS下的Capacity限制。
res-num③：为该模块的预留配额。
在VSYS Profile配置模式下使用该命令no的形式恢复默认配额：
no {cpu | session | zone | keyword {simple | regexp} | keyword-category | policy | snat | dnat |
session | session-limit | statistic-set {non-session-based | session-based} | tunnel-ipsec | cps
| scvpn-user} max max-num [reserve reserve-num] [alarm alarm-num]
设置日志的缓存配额
配置将日志信息输出到内存缓存后，根系统管理员可以通过Profile为VSYS设置各类日志占用内存缓存的预
留配额和最大配额。预留配额即系统为每个VSYS的各类型日志预留的日志缓存值；最大配额即每个VSYS的
各类型日志可获得的最大日志缓存值。如果VSYS中日志的容量超过其最大配额，那么新增加的日志将覆盖掉
缓存中最早的日志。
设置VSYS中日志的缓存配额，在VSYS Profile配置模式下使用以下命令：
log {configuration | operation | event | network | threat | traffic {session | nat | websurf} |
data-security {cf | dlp | nbr} | sandbox} buffer-size max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中配置日志、操作日志、事件日志、网络日志、
威胁日志、流量日志（会话日志、NAT日志和上网日志）、数据安全日志（内容过滤日志、文件过滤日
志和上网行为审计日志）、云沙箱日志的最大配额（max max-num）和预留配额（reserve reservenum）。最大配额和预留配额根据不同平台取值范围不同。预留配额不能超过最大配额。
配置URL过滤
根系统管理员可以通过VSYS Profile来配置是否开启URL过滤功能，然后将其绑定到VSYS，从而控制非根
VSYS是否支持URL过滤功能。StoneOS中的每个VSYS共享URL、URL类别和URL过滤Profile等URL资源，
管理员可以配置各资源的最大配额和预留配额。

<!-- 来源页 934 -->
在VSYS Profile中开启URL过滤功能或配置URL资源，需要首先进入URL过滤配置模式，请在VSYS Profile
配置模式下使用以下命令：
urlfilter
开启或关闭URL过滤功能，在URL过滤配置模式下使用以下命令：
l
开启：enable
l
关闭：no enable
设置VSYS中URL资源的配额，在URL过滤配置模式下使用以下命令：
{url | url-category | url-profile} max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中URL总数量、自定义URL类别数量和URL过滤
Profile数量的最大配额（max max-num）和预留配额（reserve reserve-num）。最大配额和预留
配额根据不同平台取值范围不同。预留配额不能超过最大配额。最大配额的默认值为Capacity，预留配
额的默认值为0。
系统资源
最大配额（max max-num）取值范围
预留配额（reserve reserve-num）最
小值
URL
0 – Capacity
0
自定义URL类别
0 – 26
0
URL过滤Profile
0 – 32
0
配置入侵防御
根系统管理员可以通过VSYS Profile来配置是否开启入侵防御功能，然后将其绑定到VSYS，从而控制非根
VSYS是否支持入侵防御功能。StoneOS中的每个VSYS共享IPS Profile资源，管理员可以配置各VSYS的最
大配额和预留配额。
在VSYS Profile中开启入侵防御功能或配置IPS Profile资源，需要首先进入入侵防御配置模式，请在VSYS
Profile配置模式下使用以下命令：
ips
开启或关闭入侵防御功能，在入侵防御配置模式下使用以下命令：
l
开启：enable
l
关闭：no enable
设置VSYS中IPS Profile资源的配额，在入侵防御配置模式下使用以下命令：
profile max max-num reserve reserve-num

<!-- 来源页 935 -->
l
max max-num reserve reserve-num – 指定VSYS中IPS Profile数量的最大配额（max maxnum）和预留配额（reserve reserve-num）。每个非根VSYS中可以创建最多4个自定义IPS
Profile，即最大配额的取值范围为0到4，默认值为4。预留配额不能超过最大配额。最大配额和预留配
额的默认值都为0，即非根VSYS只能使用预定义的IPS Profile。
配置病毒过滤
根系统管理员可以通过VSYS Profile来配置是否开启病毒过滤功能，然后将其绑定到VSYS，从而控制非根
VSYS是否支持病毒过滤功能。StoneOS中的每个VSYS共享病毒过滤Profile资源，管理员可以配置各VSYS
的最大配额和预留配额。
在VSYS Profile中开启病毒过滤功能或配置病毒过滤Profile资源，需要首先进入病毒过滤配置模式，请在
VSYS Profile配置模式下使用以下命令：
av
默认情况下，病毒过滤功能是关闭的。开启或关闭病毒过滤功能，在病毒过滤配置模式下使用以下命令：
l
开启：enable
l
关闭：no enable
设置VSYS中病毒过滤Profile资源的配额，在病毒过滤配置模式下使用以下命令：
profile max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中AV Profile数量的最大配额（maxmaxnum）和预留配额（reserve reserve-num）。最大配额的取值范围为0～32，预留配额不能超过最大
配额。最大配额的默认值为32、预留配额的默认值为0。
配置黑白名单
根系统管理员可以通过VSYS Profile来配置是否开启黑白名单功能，然后将其绑定到VSYS，从而控制非根
VSYS是否支持黑白名单功能。StoneOS中的每个VSYS共享自定义黑白名单资源，管理员可以配置各VSYS
的最大配额和预留配额。
在VSYS Profile中开启黑白名单功能或配置自定义黑白名单资源，需要首先进入边界流量过滤配置模式，请
在VSYS Profile配置模式下使用以下命令：
perimeter-traffic-filtering
开启或关闭黑白名单功能，在边界流量过滤配置模式下使用以下命令：
l
开启：enable
l
关闭：no enable

<!-- 来源页 936 -->
设置VSYS中静态IP黑名单资源的配额，在边界流量过滤配置模式下使用以下命令：
blocklist-ip max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中静态IP黑名单总数量的最大配额（max maxnum）和预留配额（reserve reserve-num）。
设置VSYS中静态Service黑名单资源的配额，在边界流量过滤配置模式下使用以下命令：
blocklist-service max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中静态Service黑名单总数量的最大配额（max
max-num）和预留配额（reserve reserve-num）。
设置VSYS中IP白名单资源的配额，在边界流量过滤配置模式下使用以下命令：
allowlist-ip max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中IP白名单总数量的最大配额（max maxnum）和预留配额（reserve reserve-num）。
设置VSYS中MAC黑名单资源的配额，在边界流量过滤配置模式下使用以下命令：
blocklist-mac max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中MAC黑名单总数量的最大配额（max maxnum）和预留配额（reserve reserve-num）。
设置VSYS中域名/URL黑白名单资源的配额，在边界流量过滤配置模式下使用以下命令：
static-domain-url max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中域名/URL黑白名单总数量的最大配额（max
max-num）和预留配额（reserve reserve-num）。该配置仅对静态黑名单以及白名单生效。
配置QoS
根系统RXW管理员可以通过VSYS Profile来配置是否开启QoS功能，然后将其绑定到VSYS，从而控制非根
VSYS是否支持QoS功能。管理员还可以配置根管道的最大配额和预留配额。
VSYS Profile中的QoS功能需要在VSYS Profile Qos 模式下进行配置。进入VSYS Profile Qos 模式，在
VSYS Profile配置模式下使用以下命令：
iqos
在VSYS Profile Qos配置模式下，使用以下命令在VSYS Profile中开启或关闭QoS功能：

<!-- 来源页 937 -->
l
开启：enable
l
关闭：no enable
设置VSYS Profile中根管道的配额，请在VSYS Profile Qos配置模式下使用以下命令：
root-pipe max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS Profile中根管道数的最大配额（max maxnum）和预留配额（reserve reserve-num）。最大配额的取值范围为0～20。预留配额不能超过最大
配额。
配置僵尸网络防御
根系统管理员可以通过VSYS Profile来配置是否开启僵尸网络防御功能，然后将其绑定到VSYS，从而控制
非根VSYS是否支持僵尸网络防御功能。StoneOS中的每个VSYS共享僵尸网络防御Profile资源，管理员可
以配置各VSYS的最大配额和预留配额。
进入僵尸网络防御配置模式
在VSYS Profile中开启僵尸网络防御功能或配置僵尸网络防御Profile资源，需要首先进入僵尸网络防御配
置模式。进入僵尸网络防御配置模式，请在VSYS Profile配置模式下使用以下命令：
botnet-c2-prevention
开启或关闭僵尸网络防御功能
默认情况下，僵尸网络防御功能是关闭的。开启或关闭僵尸网络防御功能，在僵尸网络防御配置模式下使用
以下命令：
l
开启：enable
l
关闭：no enable
设置VSYS中僵尸网络防御Profile资源的配额
设置VSYS中僵尸网络防御Profile资源的配额，在僵尸网络防御配置模式下使用以下命令：
profile max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中僵尸网络防御Profile数量的最大配额（max
max-num）和预留配额（reserve reserve-num）。最大配额的取值范围为0～33，预留配额不能超
过最大配额。最大配额的默认值为33，预留配额的默认值为0。
注意: 系统允许在根VSYS和非根VSYS中最多共配置29个自定义僵尸网络防御Profile。

<!-- 来源页 938 -->
配置沙箱防护
根系统管理员可以通过VSYS Profile来配置是否开启沙箱防护功能，然后将其绑定到VSYS，从而控制非根
VSYS是否支持沙箱防护功能。StoneOS中的每个VSYS共享沙箱防护Profile资源，管理员可以配置各VSYS
的最大配额和预留配额。
进入沙箱防护Profile配置模式
在VSYS Profile中开启沙箱防护功能或配置沙箱防护Profile资源，需要首先进入沙箱防护Profile配置模
式。进入沙箱防护Profile配置模式，请在VSYS Profile配置模式下使用以下命令：
sandbox
开启或关闭沙箱防护功能
默认情况下，沙箱防护功能是关闭的。开启或关闭沙箱防护功能，在沙箱防护Profile配置模式下使用以下命
令：
l
开启：enable
l
关闭：disable
设置VSYS中沙箱防护Profile资源的配额
设置VSYS中沙箱防护Profile资源的配额，在沙箱防护Profile配置模式下使用以下命令：
profile max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中沙箱防护Profile数量的最大配额（max maxnum）和预留配额（reserve reserve-num）。最大配额的取值范围为0～33，预留配额不能超过最大
配额。最大配额的默认值为33，预留配额的默认值为0。
配置文件过滤
根系统管理员可以通过VSYS Profile来配置是否开启文件过滤功能，然后将其绑定到VSYS，从而控制非根
VSYS是否支持文件过滤功能。StoneOS中的每个VSYS共享文件过滤Profile资源，管理员可以配置各VSYS
的最大配额和预留配额。
进入文件过滤Profile配置模式
在VSYS Profile中开启文件过滤功能或配置文件过滤Profile资源，需要首先进入文件过滤Profile配置模
式。进入文件过滤Profile配置模式，请在VSYS Profile配置模式下使用以下命令：
dlp

<!-- 来源页 939 -->
开启或关闭文件过滤功能
默认情况下，文件过滤功能是关闭的。开启或关闭文件过滤功能，在文件过滤Profile配置模式下使用以下命
令：
l
开启：enable
l
关闭：disable
设置VSYS中文件过滤Profile资源的配额
设置VSYS中文件过滤Profile资源的配额，在文件过滤Profile配置模式下使用以下命令：
profile max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中文件过滤Profile数量的最大配额（max maxnum）和预留配额（reserve reserve-num）。最大配额的取值范围为0～32，预留配额不能超过最大
配额。最大配额的默认值为32，预留配额的默认值为0。
配置文件内容过滤
根系统管理员可以通过VSYS Profile来配置是否开启文件内容过滤功能，然后将其绑定到VSYS，从而控制
非根VSYS是否支持文件内容过滤功能。StoneOS中的每个VSYS共享文件内容过滤Profile资源，管理员可
以配置各VSYS的最大配额和预留配额。
进入文件内容过滤Profile配置模式
在VSYS Profile中开启文件内容过滤功能或配置文件内容过滤Profile资源，需要首先进入文件内容过滤
Profile配置模式。进入文件内容过滤Profile配置模式，请在VSYS Profile配置模式下使用以下命令：
file-contentfilter
开启或关闭文件内容过滤功能
默认情况下，文件内容过滤功能是关闭的。开启或关闭文件内容过滤功能，在文件内容过滤Profile配置模式
下使用以下命令：
l
开启：enable
l
关闭：disable
设置VSYS中文件内容过滤Profile资源的配额
设置VSYS中文件内容过滤Profile资源的配额，在文件内容过滤Profile配置模式下使用以下命令：
profile max max-num reserve reserve-num

<!-- 来源页 940 -->
l
max max-num reserve reserve-num – 指定VSYS中文件内容过滤Profile数量的最大配额（max
max-num）和预留配额（reserve reserve-num）。最大配额的取值范围为0～32，预留配额不能超
过最大配额。最大配额的默认值为32，预留配额的默认值为0。
配置网页关键字
根系统管理员可以通过VSYS Profile来配置是否开启网页关键字功能，然后将其绑定到VSYS，从而控制非
根VSYS是否支持网页关键字功能。StoneOS中的每个VSYS共享网页关键字Profile资源，管理员可以配置
各VSYS的最大配额和预留配额。
进入网页关键字Profile配置模式
在VSYS Profile中开启网页关键字功能或配置网页关键字Profile资源，需要首先进入网页关键字Profile配
置模式。进入网页关键字Profile配置模式，请在VSYS Profile配置模式下使用以下命令：
contentfilter
开启或关闭网页关键字功能
默认情况下，网页关键字功能是关闭的。开启或关闭网页关键字功能，在网页关键字Profile配置模式下使用
以下命令：
l
开启：enable
l
关闭：disable
设置VSYS中网页关键字Profile资源的配额
设置VSYS中网页关键字Profile资源的配额，在网页关键字Profile配置模式下使用以下命令：
profile max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中网页关键字Profile数量的最大配额（max
max-num）和预留配额（reserve reserve-num）。最大配额的取值范围为0～32，预留配额不能超
过最大配额。最大配额的默认值为32，预留配额的默认值为0。
配置Web外发信息
根系统管理员可以通过VSYS Profile来配置是否开启Web外发信息功能，然后将其绑定到VSYS，从而控制
非根VSYS是否支持Web外发信息功能。StoneOS中的每个VSYS共享Web外发信息Profile资源，管理员可
以配置各VSYS的最大配额和预留配额。

<!-- 来源页 941 -->
进入Web外发信息Profile配置模式
在VSYS Profile中开启Web外发信息功能或配置Web外发信息Profile资源，需要首先进入Web外发信息
Profile配置模式。进入Web外发信息Profile配置模式，请在VSYS Profile配置模式下使用以下命令：
webpost
开启或关闭Web外发信息功能
默认情况下，Web外发信息功能是关闭的。开启或关闭Web外发信息功能，在Web外发信息Profile配置模
式下使用以下命令：
l
开启：enable
l
关闭：disable
设置VSYS中Web外发信息Profile资源的配额
设置VSYS中Web外发信息Profile资源的配额，在Web外发信息Profile配置模式下使用以下命令：
profile max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中Web外发信息Profile数量的最大配额（max
max-num）和预留配额（reserve reserve-num）。最大配额的取值范围为0～32，预留配额不能超
过最大配额。最大配额的默认值为32，预留配额的默认值为0。
配置邮件过滤
根系统管理员可以通过VSYS Profile来配置是否开启邮件过滤功能，然后将其绑定到VSYS，从而控制非根
VSYS是否支持邮件过滤功能。StoneOS中的每个VSYS共享邮件过滤Profile资源，管理员可以配置各VSYS
的最大配额和预留配额。
进入邮件过滤Profile配置模式
在VSYS Profile中开启邮件过滤功能或配置邮件过滤Profile资源，需要首先进入邮件过滤Profile配置模
式。进入邮件过滤Profile配置模式，请在VSYS Profile配置模式下使用以下命令：
mail
开启或关闭邮件过滤功能
默认情况下，邮件过滤功能是关闭的。开启或关闭邮件过滤功能，在邮件过滤Profile配置模式下使用以下命
令：
l
开启：enable
l
关闭：disable

<!-- 来源页 942 -->
设置VSYS中邮件过滤Profile资源的配额
设置VSYS中邮件过滤Profile资源的配额，在邮件过滤Profile配置模式下使用以下命令：
profile max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中邮件过滤Profile数量的最大配额（max maxnum）和预留配额（reserve reserve-num）。最大配额的取值范围为0～32，预留配额不能超过最大
配额。最大配额的默认值为32，预留配额的默认值为0。
配置应用行为控制
根系统管理员可以通过VSYS Profile来配置是否开启应用行为控制功能，然后将其绑定到VSYS，从而控制
非根VSYS是否支持应用行为控制功能。StoneOS中的每个VSYS共享应用行为控制Profile资源，管理员可
以配置各VSYS的最大配额和预留配额。
进入应用行为控制Profile配置模式
在VSYS Profile中开启应用行为控制功能或配置应用行为控制Profile资源，需要首先进入应用行为控制
Profile配置模式。进入应用行为控制Profile配置模式，请在VSYS Profile配置模式下使用以下命令：
behavior
开启或关闭应用行为控制功能
默认情况下，应用行为控制功能是关闭的。开启或关闭应用行为控制功能，在应用行为控制Profile配置模式
下使用以下命令：
l
开启：enable
l
关闭：disable
设置VSYS中应用行为控制Profile资源的配额
设置VSYS中应用行为控制Profile资源的配额，在应用行为控制Profile配置模式下使用以下命令：
profile max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中应用行为控制Profile数量的最大配额（max
max-num）和预留配额（reserve reserve-num）。最大配额的取值范围为0～32，预留配额不能超
过最大配额。最大配额的默认值为32，预留配额的默认值为0。
配置上网行为审计
根系统管理员可以通过VSYS Profile来配置是否开启上网行为审计功能，然后将其绑定到VSYS，从而控制
非根VSYS是否支持上网行为审计功能。StoneOS中的每个VSYS共享上网行为审计Profile资源，管理员可
以配置各VSYS的最大配额和预留配额。

<!-- 来源页 943 -->
进入上网行为审计Profile配置模式
在VSYS Profile中开启上网行为审计功能或配置上网行为审计Profile资源，需要首先进入上网行为审计
Profile配置模式。进入上网行为审计Profile配置模式，请在VSYS Profile配置模式下使用以下命令：
nbr
开启或关闭上网行为审计功能
默认情况下，上网行为审计功能是关闭的。开启或关闭上网行为审计功能，在上网行为审计Profile配置模式
下使用以下命令：
l
开启：enable
l
关闭：disable
设置VSYS中上网行为审计Profile资源的配额
设置VSYS中上网行为审计Profile资源的配额，在上网行为审计Profile配置模式下使用以下命令：
profile max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中上网行为审计Profile数量的最大配额（max
max-num）和预留配额（reserve reserve-num）。最大配额的取值范围为0～32，预留配额不能超
过最大配额。最大配额的默认值为32，预留配额的默认值为0。
启用/禁用CPU资源配额
默认情况下，配置完成的CPU资源配额会在系统中立即生效。用户可以通过命令关闭VSYS CPU资源的检
查，也就是已配置的CPU资源配额不生效，每个VSYS来抢占系统中CPU的资源值。禁用或者启用CPU资源配
额，在根VSYS全局配置模式下，使用以下命令：
l
禁用：vsys-resource cpu disable
l
启用：vsys-resource cpu enable
型号说明：对于部分HIllstone设备（X9180、K9180），不支持启用或者禁用已配置的CPU
资源配额。
绑定Profile到VSYS
将已经创建的VSYS Profile绑定到VSYS，在VSYS配置模式下使用以下命令：
profile vsys-profile-name

<!-- 来源页 944 -->
l
vsys-profile-name – 指定绑定的VSYS Profile名称。
在VSYS配置模式下使用no profile命令恢复默认绑定。
注意:
l
当将一个Profile绑定到VSYS时，如果所有VSYS的预留配额之和超过当前系统Capacity，则
绑定失败。
l
被绑定的VSYS Profile只有在解除绑定后，才可以进行删除。
配置共享属性
为根VSYS的VRouter、VSwitch或者安全域对象配置共享属性，分别在根VSYS的VRouter配置模式、
VSwitch配置模式或者安全域配置模式下使用以下命令：
vsys-shared
在根VSYS的VRouter配置模式、VSwitch配置模式或者安全域配置模式下，使用no vsys-shared命令取消
共享属性配置。
型号说明：仅K9180、K6280-GS、K6580、K5680、K3680-GS、K3280、K2580、
K2560、K1280、K2680、K2380和X9180支持该功能。
导入/导出物理接口
所有物理接口都默认属于根VSYS。根系统管理员可以将根VSYS中的物理接口导入到非根VSYS，也可以将非
根VSYS中的物理接口导出到根VSYS。导入或者导出的物理接口不能属于安全域，不能为BGroup接口、集
聚接口、PPPoE接口，VSwitch接口和冗余接口成员，且无子接口。导入到非根VSYS中的物理接口的相关
接口（如子接口）只能在该非根VSYS中使用。
通过非根VSYS实名将物理接口导入到非根VSYS，在接口配置模式下使用以下命令：
export-to vsys-name
l
vsys-name – 指定物理接口导入到的非根VSYS实名。
通过非根VSYS别名将物理接口导入到非根VSYS，在接口配置模式下使用以下命令：
export-to alias alias_name
l
alias alias_name – 指定物理接口导入到的非根VSYS别名。

<!-- 来源页 945 -->
在接口配置模式下，使用no export-to命令将非根VSYS中的物理接口导出到根VSYS。
分配逻辑接口
根系统管理员可以将根VSYS中的逻辑接口分配给非根VSYS，也可以将已分配的逻辑接口恢复到根VSYS。
通过非根VSYS实名将逻辑接口分配到非根VSYS，在接口配置模式下使用以下命令：
vsys vsys-name
l
vsys-name – 指定将接口分配到的非根VSYS实名。
通过非根VSYS别名将逻辑接口分配到非根VSYS，在接口配置模式下使用以下命令：
vsys alias alias_name
l
alias alias_name – 指定将接口分配到的非根VSYS别名。
在接口配置模式下，使用no vsys命令将已分配的逻辑接口恢复到根VSYS。
绑定监测对象
用户可以将非根VSYS绑定一个监测对象，来监控该非根VSYS的状态。配置非根VSYS绑定监测对象，在指定
非根VSYS配置模式下，使用以下命令：
vsys-track-status track track-name
l
track-name – 指定在此非根VSYS中已配置的监测对象的名称。
通过非根VSYS实名将已配置的监测对象绑定到非根VSYS，在监测对象配置模式下，使用以下命令：
vsys vsys_name
l
vsys-name – 指定该监测对象绑定的非根VSYS的实名。
通过非根VSYS别名将已配置的监测对象绑定到非根VSYS，在监测对象配置模式下，使用以下命令：
vsys alias alias_name
l
alias alias_name – 指定该监测对象绑定的非根VSYS的别名。
在指定非根VSYS配置模式下使用该命令no的形式解除绑定监测对象：
no vsys-track-status track track-name

<!-- 来源页 946 -->
注意:
l
被绑定的监测对象只有在解除绑定后，才可以进行删除。
l
关于如何配置监测对象，请参阅《系统管理》的“配置监测对象”部分。
监测指定VSYS状态
在根VSYS下可以监测指定VSYS的状态，根据被监测的VSYS状态改变，采取相应的措施。监测指定的VSYS
状态，在根VSYS的监测对象的配置模式下，使用以下命令：
vsys vsys-name weight value
l
vsys-name – 指定被监测的VSYS名称。
l
weight value – 指定该条监测失败对整个监测对象失败贡献的权重值。取值范围是1到255。默认值是
255。
回退配置信息
系统可对根VSYS和非根VSYS回退配置信息，支持以下两种方式：
第一种：在执行模式下，使用以下命令回退起始配置信息。系统能够纪录最近十次保存的起始配置信息，用
户可以根据需要回退到已保存的指定的起始配置信息。系统将在重启后使用指定的起始配置信息。
rollback configuration backup number
l
number – 备份起始配置信息的数字标记。
第二种：在配置回滚模式下，使用以下命令回退配置信息并退出配置回滚模式。用户不需要重启设备，该配
置直接生效。
exec configuration rollback
注意:
l
在执行模式下，使用exec configuration start进入配置回滚模式。
l
开启配置回滚模式后和结束之前，用户无法切换VSYS。
l
每个VSYS可以独立的开启和结束回滚模式，互不影响。
l
每个VSYS同一时刻只允许一个用户开启配置回滚模式，并且仅该用户可以结束配置回滚模式。
l
根VSYS开启配置回滚模式后，系统将无法执行：切换HA状态、切换主备设备、创建或删除HA
Cluster、创建或删除VSYS、修改VSYS资源配额。

<!-- 来源页 947 -->
示例：
hostname# exec configuration start( 进入配置回滚模式)
hostname[TRN]# configure ( 进入全局配置模式)
…… ( 进行任意配置，且所做配置即时生效)
hostname[TRN](config)# exec configuration rollback ( 回退配置并退出配置回滚模式)
hostname#
退出配置回滚模式
直接退出配置回滚模式，系统支持以下两种方式：
第一种：在配置回滚模式下，使用以下命令直接退出配置回滚模式：
exec configuration commit
示例：
hostname# exec configuration start ( 进入配置回滚模式)
hostname[TRN]# configure ( 进入全局配置模式)
…… ( 进行任意配置，且所做配置即时生效)
hostname[TRN](config)# exec configuration commit ( 直接退出配置回滚模式)
hostname#
第二种：在配置回滚模式下，使用exit命令直接退出登录终端，从而退出配置回滚模式。
l
当不同用户同时登录设备时，先进入配置回滚模式的用户可以继续配置操作，其他用户无法进行配置操
作。
l
当相同用户通过不同访问方式登录设备时，先进入配置回滚模式的某访问方式的用户可以继续配置操
作，其他访问方式的用户无法进行配置操作，但其可以使用exec configuration commit或者exec
configuration rollback命令强制使进入配置回滚模式的某用户退出配置回滚模式。
配置退出配置回滚模式的动作
当使用exit命令退出配置回滚模式时，默认情况下，系统会直接退出配置回滚模式。回退配置后退出配置回
滚模式，在全局配置模式下，使用以下命令：
cli-exit-action rollback
恢复直接退出配置回滚模式，在全局配置模式下，使用以下命令：
cli-exit-action commit

<!-- 来源页 948 -->
注意: 每个VSYS可以独立使用该命令，指定自己的退出配置回滚模式的动作。
配置VSYS日志功能
目前系统支持对VSYS中的AAA、NAT/NAT444、策略、路由、攻击防护、接口、DNS、服务、DHCP和系
统管理事件生成日志。有关配置和查看日志的更多详细信息，请参考《监控》的“日志”。
注意: 在非根VSYS中，系统不支持生成调试、IPS和数据安全类型日志。
配置跨VSYS转发功能
为了实现设备的跨VSYS转发功能，系统引入了Simple-Switch的概念，即一种特殊的VSwitch，仅进行
MAC地址学习、转发已知单播包或者泛洪。用户通过新建VWANIF接口，并且分配给指定的VSYS，不同的
VSYS即可通过VWANIF接口进行相互通信，从而实现在设备内部直接转发跨越不同VSYS之间流量数据包。
通常情况下，配置跨VSYS转发功能，需要以下步骤：
1. 开启跨VSYS转发功能。
2. 配置Simple-Switch。
包括创建Simple-Switch、二层安全域以及绑定该二层安全域到Simple-Switch。
3. 创建VWANIF接口和VPort接口。
创建新的VWANIF接口后，需要再创建一个配对的VPort接口。
4. 配置VPort接口。
将VPort接口绑定到已加入Simple-Switch的二层安全域。
5. 配置VWANIF接口。
将VWANIF接口导入到自定义VSYS，并配置所属的三层安全域和IP地址。
开启跨VSYS转发功能
默认情况下，该功能是关闭的。开启跨VSYS转发功能，在全局配置模式下，使用以下命令：
vsys-switch-mode
使用no vsys-switch-mode关闭跨VSYS转发功能。
配置Simple-Switch
Simple-Switch，即一种特殊的VSwitch，仅进行MAC地址学习、转发已知单播包或者泛洪。可以创建多
个Simple-Switch，每一个Simple-Switch都是一个独立的广播域。

<!-- 来源页 949 -->
创建Simple-Switch
创建Simple-Switch，在全局配置模式下，使用以下命令：
vswitch vswitchNumber [simple-switch]
l
Number – 指定VSwitch的数字标识。Number的取值范围根据平台不同而不同。不可指定为
VSwitch1。
l
simple-switch – 指定该参数，创建Simple-Switch，并且进入Simple-Switch配置模式。
在全局配置模式下，使用以上命令no的形式删除指定的Simple-Switch：
no vswitch vswitch Number
绑定二层安全域到Simple-Switch
绑定二层安全域到Simple-Switch需要进行两步配置。
首先，创建二层安全域，在全局配置模式下，使用以下命令：
zone zone-name l2
l
zone-name - 创建域的名称。
l
l2 – 指定所创建域为二层域。
然后，在安全域配置模式下，输入以下命令将该二层安全域绑定到Simple-Switch：
bind vswitch-name
l
vswitch-name - 指定将二层域绑定到的Simple-Switch所属的VSwitch名称。
创建VWANIF接口
注意: 非根VSYS不支持新建VWANIF接口。
VWANIF接口是三层接口，每新建一个VWANIF接口，需要再创建一个配对的VPort接口，通过VWANIF接
口和VPort接口可以实现不同VSYS的互通。
创建VWANIF接口，在全局配置模式下，使用以下命令：
interface vwanif id
l
id – 指定将要创建的VWANIF接口的编号。如果指定编号的VWANIF接口不存在，则创建VWANIF接口
并进入VWANIF接口配置模式；如果指定编号的VWANIF接口已存在，则直接进入VWANIF接口配置模
式。

<!-- 来源页 950 -->
在全局配置模式下使用no interface vwanif id命令删除指定的VWANIF接口。
创建VPort接口
注意: 非根VSYS不支持新建VPort接口。
创建VPort接口，在全局配置模式下，使用以下命令：
interface vport id
l
id – 指定将要创建的VPort接口的编号，该编号需要与配对的VWANIF接口编号相同。如果指定编号的
VPort接口不存在，则创建VPort接口并进入VPort接口配置模式；如果指定编号的VPort接口已存在，
则直接进入VPort接口配置模式。
在全局配置模式下使用no interface vport id命令删除指定的VPort接口。
创建VPort接口之后，同时需要将VPort接口绑定到已加入Simple-Switch的二层安全域。在VPort接口配
置模式下，使用以下命令：
zone zone-name
l
zone -name – 指定将接口绑定到已加入Simple-Switch的二层安全域名称。
配置VWANIF接口
为了实现不同VSYS的三层互通，用户还需要将VWANIF接口导入到自定义VSYS，并配置所属的三层安全域
和IP地址（IPv4 或IPv6）。
注意: 关于配置VWANIF接口配所属安全域以及IP地址（IPv4 或IPv6），请参阅“配置接口”章
节。
分配VWANIF接口
创建VWANIF接口之后，需要将VWANIF接口接口分配到非根VSYS，在接口配置模式下使用以下命令：
vsys vsys-name
l
vsys-name – 指定将接口分配到的VSYS名称。
显示跨VSYS转发功能信息
查看设备是否开启了跨VSYS转发功能，在任意模式使用以下命令：
show vsys-switch-mode

<!-- 来源页 951 -->
显示VWANIF接口配置信息
显示指定VWANIF接口信息，在任意模式下，使用以下命令：
show interface vwanif id
显示VWANIF接口IPv6配置信息
显示指定VWANIF接口IPv6配置信息，在任意模式下，使用以下命令：
show ipv6 interface vwanif id
显示VSYS信息
通过非根VSYS实名显示系统中非根VSYS信息，在根VSYS任意模式使用以下命令：
show vsys [vsys-name]
l
vsys-name – 指定需要查看的非根VSYS的实名。若不指定，则显示系统所有非根VSYS的信息。
通过非根VSYS别名显示系统中非根VSYS信息，在根VSYS任意模式使用以下命令：
show vsys alias alias_name
l
alias alias_name – 指定需要查看的非根VSYS的别名。
显示VSYS Profile信息
显示系统中VSYS Profile信息，在根VSYS任意模式使用以下命令：
show vsys-profile [vsys-profile-name]
l
vsys-profile-name – 指定需要查看的VSYS Profile的名称。若不指定，则显示系统所有VSYS
Profile的信息。
进入VSYS
进入根VSYS，请按照以下步骤进行操作：
1.
在本地PC上启动一个终端仿真程序，输入设备的管理IP和端口号后与系统建立连接。
2.
根据提示输入用户名和密码后进入根VSYS，可以是根系统管理员或者根系统中配置的认证服务器（本地
服务器/Radius服务器/TACACS+服务器）用户的用户名和密码。
进入非根VSYS，可以通过以下三种方式：
方式一：直接通过管理IP访问非根VSYS，请按照以下步骤进行操作：

<!-- 来源页 952 -->
1.
进入根VSYS。
2.
在根VSYS全局配置模式下，使用vsys vsys-name命令创建非根VSYS。关于创建非根VSYS的详细信
息，请见创建非根VSYS。
3.
在本地PC上启动一个终端仿真程序，输入设备的管理IP和端口号后与系统建立连接。
4.
按以下格式输入用户名和密码：vsys_name\username。其中vsys_name为虚拟系统名称，
username为非根VSYS管理员的用户名。
l
非根VSYS默认管理员的用户名为admin，初始密码为vsys_name-admin。修改初始密码后，
可直接使用新密码登录，密码中不需携带vsys_name-前缀。
l
自定义管理员直接使用创建时设置的密码即可。
注意: 若通过以上方式直接进入非根VSYS，用户将无法使用exit-vsys命令返回根VSYS，需退出设
备后，再次进入根VSYS。
方式二：通过实名从根VSYS进入非根VSYS（仅根系统管理员具有该权限），并对该非根VSYS进行配置，在
根VSYS执行模式或者全局配置模式下使用以下命令：
enter-vsys vsys-name
l
vsys-name – 指定进入的非根VSYS实名。
通过别名从根VSYS进入非根VSYS（仅根系统管理员具有该权限），并对该非根VSYS进行配置。在根VSYS
执行模式或者全局配置模式下使用以下命令：
enter-vsys alias alias-name
l
alias alias-name – 指定进入的非根VSYS别名。
在非根VSYS执行模式或者全局配置模式下，使用exit-vsys命令退出当前的非根VSYS，进入根VSYS对应的
执行模式或者全局配置模式。
方式三：在非根VSYS中配置认证服务器，用户通过认证服务器登录非根VSYS。按照以下步骤进行操作：
1.
通过上述任意方式进入非根VSYS。
2.
在非根VSYS全局配置模式下，使用aaa-server aaa-server-name [type] {local | radius |
tacacs+}命令创建AAA服务器（本地服务器/Radius服务器/TACACS+服务器）并进行服务器参数配
置。关于AAA服务器的详细信息，请见"配置本地服务器认证参数" 在第1197页章节。
3.
在非根VSYS全局配置模式下，使用admin auth-server server-name命令指定系统管理员认证服务
器。关于指定系统管理员认证服务器的详细信息，请见"配置服务器认证与授权" 在第1270页章节。

<!-- 来源页 953 -->
4.
在本地PC上启动一个终端仿真程序，输入设备的管理IP和端口号后与系统建立连接。
5.
根据提示输入认证服务器中配置的用户名和密码后进入非根VSYS。

<!-- 来源页 954 -->
VSYS配置举例
本节介绍VSYS的四个典型配置示例，分别为：
l 例：VSYS在三层流量转发中的应用（通过单一VSYS）
l 例：VSYS在三层流量转发中的应用（通过共享VRouter）
l 例：VSYS在二层流量转发中的应用（通过共享VSwitch)
l 例：跨VSYS的流量转发（通过Simple-Switch）
型号说明：云•界、X8180和A系列平台不支持例2与例3所示的配置。
例：VSYS在三层流量转发中的应用（通过单一VSYS）
提示: 本示例所展示的操作步骤，基于StoneOS 5.5R11版本进行配置。若有变动，请以实际页面
为准。
组网需求
Hillstone设备为某企业提供服务。现需要进行VSYS配置，使部门A能够通过ethernet0/0和ethernet0/3
访问企业内部某服务器。组网图如下：
通过创建单一VSYS和相应的安全策略实现三层流量转发，逻辑示意图如下：

<!-- 来源页 955 -->
配置步骤
第一步：创建VSYS-a。
hostname(config)# vsys vsys-a
hostname(config-vsys)# exit
hostname(config)#
第二步：将eth0/0和eth0/3导入到VSYS-a（导入操作可以由Root VSYS中的根系统管理员执行）。
hostname(config)# interface ethernet0/0
hostname (config-if-eth0/0)# export-to vsys-a
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/3
hostname (config-if-eth0/3)# export-to vsys-a
hostname(config-if-eth0/3)# exit
hostname(config)#
第三步：进入VSYS-a并配置eth0/0、eth0/3和策略。
hostname(config)# enter-vsys vsys-a
hostname(vsys-a)(config)# zone vsys-a-trust
hostname(vsys-a)(config-zone-vsys-a-trust)# exit
hostname(vsys-a)(config)# interface ethernet0/0
hostname(vsys-a)(config-if-eth0/0)# zone vsys-a-trust
hostname(vsys-a)(config-if-eth0/0)# ip address 192.168.1.1/24
hostname(vsys-a)(config-if-eth0/0)# exit
hostname(vsys-a)(config)# zone vsys-a-untrust

<!-- 来源页 956 -->
hostname(vsys-a)(config-zone-vsys-a-untrust)# exit
hostname(vsys-a)(config)# interface ethernet0/3
hostname(vsys-a)(config-if-eth0/3)# zone vsys-a-untrust
hostname(vsys-a)(config-if-eth0/3)# ip address 10.160.65.203/21
hostname(vsys-a)(config-if-eth0/3)# exit
hostname(vsys-a)(config)# policy-global
hostname(vsys-a)(config-policy)# rule
hostname(vsys-a)(config-policy-rule)# src-zone vsys-a-trust
hostname(vsys-a)(config-policy-rule)# dst-zone vsys-a-untrust
hostname(vsys-a)(config-policy-rule)# src-addr any
hostname(vsys-a)(config-policy-rule)# dst-addr any
hostname(vsys-a)(config-policy-rule)# service any
hostname(vsys-a)(config-policy-rule)# action permit
hostname(vsys-a)(config-policy-rule)# exit
hostname(vsys-a)(config-policy)# exit
hostname(vsys-a)(config)# exit-vsys
hostname(config)#
例：VSYS在三层流量转发中的应用（通过共享VRouter）
提示: 本示例所展示的操作步骤，基于StoneOS 5.5R11版本进行配置。若有变动，请以实际页面
为准。
组网需求
Hillstone设备为企业A和企业B提供服务。其中，企业A使用VSYS-a，企业B使用VSYS-b。端口
ethernet0/0为VSYS-a的专有接口，端口ethernet0/7为VSYS-b的专有接口。企业A和企业B共享端口
ethernet0/3，并通过该接口访问外网。
注意: 仅K9180、K6280-GS、K6580、K5680、K3680-GS、K3280、K2580、K2560、
K1280、K2680、K2380和X9180支持该案例。

<!-- 来源页 957 -->
组网图如下：
通过创建共享VRouter和相应的路由、SNAT规则、安全策略实现三层流量转发，逻辑示意图如下：
配置步骤
第一步：Root VSYS的配置。
创建vsys-a和vsys-b
hostname(config)# vsys vsys-a
hostname(config-vsys)# exit
hostname(config)# vsys vsys-b
hostname(config-vsys)# exit
hostname(config)#
配置端口ethernet0/3、路由、SNAT规则和DNS服务器

<!-- 来源页 958 -->
hostname(config)# interface ethernet0/3
hostname(config -if-eth0/3)# zone untrust
hostname(config -if-eth0/3)# ip address 10.160.65.203/21
hostname(config -if-eth0/3)# exit
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 0.0.0.0/0 10.160.64.1
hostname(config-vrouter)# snatrule from any to any eif ethernet0/3 trans-to eif-ip
mode dynamicport
rule ID=3
hostname(config-vrouter)# exit
hostname(config)# ip name-server 202.106.0.20
hostname(config)#
配置Root VSYS的trust-vr为共享VR
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# vsys-shared
hostname(config-vrouter)# exit
hostname(config)#
配置Root VSYS的untrust zone为共享安全域
hostname(config)# zone untrust
hostname(config-zone-untrust)# vsys-shared
hostname(config-zone-untrust)# exit
hostname(config)#
第二步：VSYS-a的配置。
将eth0/0导入到VSYS-a( 导入操作可以由Root VSYS中的根系统管理员执行)
hostname(config)# interface ethernet0/0
hostname (config-if-eth0/0)# export-to vsys-a
hostname(config-if-eth0/0)# exit
hostname(config)#
进入VSYS-a并配置eth0/0、策略和跨VR路由

<!-- 来源页 959 -->
hostname(config)# enter-vsys vsys-a
hostname(vsys-a)(config)# interface ethernet0/0
hostname(vsys-a)(config-if-eth0/0)# zone vsys-a-trust
hostname(vsys-a)(config-if-eth0/0)# ip address 192.168.1.1/24
hostname(vsys-a)(config-if-eth0/0)# exit
hostname(vsys-a)(config)# policy-global
hostname(vsys-a)(config-policy)# rule
hostname(vsys-a)(config-policy-rule)# src-zone vsys-a-trust
hostname(vsys-a)(config-policy-rule)# dst-zone untrust
hostname(vsys-a)(config-policy-rule)# src-addr any
hostname(vsys-a)(config-policy-rule)# dst-addr any
hostname(vsys-a)(config-policy-rule)# service any
hostname(vsys-a)(config-policy-rule)# action permit
hostname(vsys-a)(config-policy-rule)# exit
hostname(vsys-a)(config)# ip vrouter vsys-a-vr
hostname(vsys-a)(config-vrouter)# ip route 0.0.0.0/0 vrouter trust-vr
hostname(vsys-a)(config-vrouter)# exit
hostname(vsys-a)(config)# exit-vsys
hostname(config)#
第三步：VSYS-b的配置。
将eth0/7导入到VSYS-b( 导入操作可以由Root VSYS中的根系统管理员执行)
hostname(config)# interface ethernet0/7
hostname (config-if-eth0/7)# export-to vsys-b
hostname(config-if-eth0/7)# exit
hostname(config)#
进入VSYS-b并配置eth0/7、策略和跨VR路由
hostname(config)# enter-vsys vsys-b
hostname(vsys-b)(config)# interface ethernet0/7

<!-- 来源页 960 -->
hostname(vsys-b)(config-if-eth0/7)# zone vsys-b-trust
hostname(vsys-b)(config-if-eth0/7)# ip address 192.169.1.1/24
hostname(vsys-b)(config-if-eth0/7)# exit
hostname(vsys-b)(config)# policy-global
hostname(vsys-b)(config-policy)# rule
hostname(vsys-b)(config-policy-rule)# src-zone vsys-b-trust
hostname(vsys-b)(config-policy-rule)# dst-zone untrust
hostname(vsys-b)(config-policy-rule)# src-addr any
hostname(vsys-b)(config-policy-rule)# dst-addr any
hostname(vsys-b)(config-policy-rule)# service any
hostname(vsys-b)(config-policy-rule)# action permit
hostname(vsys-b)(config-policy-rule)# exit
hostname(vsys-b)(config)# ip vrouter vsys-b-vr
hostname(vsys-b)(config-vrouter)# ip route 0.0.0.0/0 vrouter trust-vr
hostname(vsys-b)(config-vrouter)# exit
hostname(vsys-b)(config)# exit-vsys
hostname(config)#
例：VSYS在二层流量转发中的应用（通过共享VSwitch）
提示: 本示例所展示的操作步骤，基于StoneOS 5.5R11版本进行配置。若有变动，请以实际页面
为准。
组网需求
Hillstone设备为某企业提供服务。其中，部门A使用VSYS-a，部门B使用VSYS-b。端口ethernet0/0为
VSYS-a的专有接口，端口ethernet0/7为VSYS-b的专有接口。部门A和部门B共享端口ethernet0/3，并
通过该接口访问企业内部某服务器。组网图如下：

<!-- 来源页 961 -->
通过创建共享VSwitch和相应的安全策略实现二层流量转发，逻辑示意图如下：
注意: 仅K9180、K6280-GS、K6580、K5680、K3680-GS、K3280、K2580、K2560、
K1280、K2680、K2380和X9180支持该案例。
配置步骤
第一步：Root VSYS的配置。
创建vsys-a和vsys-b
hostname(config)# vsys vsys-a
hostname(config-vsys)# exit
hostname(config)# vsys vsys-b
hostname(config-vsys)# exit

<!-- 来源页 962 -->
hostname(config)#
配置Root VSYS的VSwitch1为共享VSwitch
hostname(config)# vswitch vswitch1
hostname(config-vswitch)# vsys-shared
hostname(config-vswitch)# exit
配置Root VSYS的L2-trust安全域为共享安全域
hostname(config)# zone l2-trust
hostname(config-zone-l2-tru~)# vsys-shared
hostname(config-zone-l2-tru~)# exit
hostname(config)#
配置端口ethernet0/3
hostname(config)# interface ethernet0/3
hostname(config -if-eth0/3)# zone l2-trust
hostname(config -if-eth0/3)# exit
hostname(config)#
第二步：VSYS-a的配置。
将eth0/0导入到VSYS-a( 导入操作可以由Root VSYS中的根系统管理员执行)
hostname(config)# interface ethernet0/0
hostname (config-if-eth0/0)# export-to vsys-a
hostname(config-if-eth0/0)# exit
hostname(config)#
进入VSYS-a，创建VSwitch和L2安全域，并将该安全域绑定到共享的VSwitch1上
hostname(config)# enter-vsys vsys-a
hostname(vsys-a)(config)# zone a-l2 l2
hostname(vsys-a)( config-zone-a-l2)# bind vswitch1
hostname(vsys-a)( config-zone-a-l2)# exit
hostname(vsys-a)(config)#
配置接口eth0/0和策略

<!-- 来源页 963 -->
hostname(vsys-a)(config)# interface ethernet0/0
hostname(vsys-a)(config-if-eth0/0)# zone a-l2
hostname(vsys-a)(config-if-eth0/0)# exit
hostname(vsys-a)(config)# policy-global
hostname(vsys-a)(config-policy)# rule
hostname(vsys-a)(config-policy-rule)# src-zone a-l2
第三步：VSYS-b的配置。
将eth0/7导入到VSYS-b( 导入操作可以由Root VSYS中的根系统管理员执行)
hostname(config)# interface ethernet0/7
hostname (config-if-eth0/7)# export-to vsys-b
hostname(config-if-eth0/7)# exit
hostname(config)#
进入VSYS-b，创建VSwitch和L2安全域，并将该安全域绑定到共享的VSwitch1上
hostname(config)# enter-vsys vsys-b
hostname(vsys-b)(config)# zone b-l2 l2
hostname(vsys-b)( config-zone-b-l2)# bind vswitch1
hostname(vsys-b)( config-zone-b-l2)# exit
hostname(vsys-b)(config)#
配置接口eth0/7和策略
hostname(vsys-b)(config)# interface ethernet0/7
hostname(vsys-b)(config-if-eth0/7)# zone b-l2
hostname(vsys-b)(config-if-eth0/7)# exit
hostname(vsys-b)(config)# policy-global
hostname(vsys-b)(config-policy)# rule
hostname(vsys-b)(config-policy-rule)# src-zone b-l2
hostname(vsys-b)(config-policy-rule)# dst-zone l2-trust
hostname(vsys-b)(config-policy-rule)# src-addr any
hostname(vsys-b)(config-policy-rule)# dst-addr any

<!-- 来源页 964 -->
hostname(vsys-b)(config-policy-rule)# service any
hostname(vsys-b)(config-policy-rule)# action permit
hostname(vsys-b)(config-policy-rule)# exit
hostname(vsys-b)(config)# exit-vsys
hostname(config)#
例：跨VSYS的流量转发（通过Simple-Switch）
提示: 本示例所展示的操作步骤，基于StoneOS 5.5R11版本进行配置。若有变动，请以实际页面
为准。
组网需求
设备为某企业提供服务，现需要进行VSYS配置，部门A使用VSYS-v1，部门B使用VSYS-v2。端口
ethernet0/0为VSYS-v1的专有接口，端口ethernet0/2为VSYS-v2的专有接口。使部门A和部门B分属不
同的两个vsys，且能够通过ethernet0/0和ethernet0/2完成互相访问。组网图如下：
通过创建Simple-Switch、VWANIF接口、VPort接口和相应的路由、安全策略实现流量转发，逻辑示意图
如下：

<!-- 来源页 965 -->
配置步骤
第一步：Root VSYS的配置。
创建vsys-v1和vsys-v2
hostname(config)# vsys vsys-v1
hostname(config-vsys)# exit
hostname(config)# vsys vsys-v2
hostname(config-vsys)# exit
hostname(config)#
配置Root VSYS的VSwitch2为Simple-Switch
hostname(config)# vsys-switch-mode
hostname(config)# vswitch vswitch2 simple-switch
hostname(config-vswitch)# exit
配置Root VSYS的L2-simple安全域为二层安全域
hostname(config)# zone l2-simple l2

<!-- 来源页 966 -->
hostname(config-zone-l2-sim~)# bind vswitch2
hostname(config-zone-l2-sim~)# exit
hostname(config)#
配置端口vwanif1、vport1
hostname(config)# interface vwanif1
hostname(config -if-vwa1)# vsys vsys-v1
hostname(config -if-vwa1)# exit
hostname(config)#interface vport1
hostname(config -if-vpo1)# zone l2-simple
hostname(config -if-vpo1)# exit
hostname(config)#
配置端口vwanif2、vport2
hostname(config)# interface vwanif2
hostname(config -if-vwa1)# vsys vsys-v2
hostname(config -if-vwa1)# exit
hostname(config)#interface vport2
hostname(config -if-vpo1)# zone l2-simple
hostname(config -if-vpo1)# exit
hostname(config)#
配置端口ethernet0/0
hostname(config)# interface ethernet0/0
hostname(config -if-eth0/0)# vsys vsys-v1
hostname(config -if-eth0/0)# exit
hostname(config)#
配置端口ethernet0/2
hostname(config)# interface ethernet0/2
hostname(config -if-eth0/2)# vsys vsys-v2
hostname(config -if-eth0/2)# exit
hostname(config)#

<!-- 来源页 967 -->
第二步：VSYS-v1的配置。
hostname(config)# enter-vsys vsys-v1
hostname(vsys-v1)(config)# interface vwanif1
hostname(vsys-v1)(config-if-vwa1)# zone vsys-v1-trust
hostname(vsys-v1)(config-if-vwa1)# ipv6 enable
hostname(vsys-v1)(config-if-vwa1)# ipv6 address 6666::1/64
hostname(vsys-v1)(config-if-vwa1)# exit
hostname(vsys-v1)(config)# interface ethernet0/0
hostname(vsys-v1)(config-if-eth0/0)# zone vsys-v1-trust
hostname(vsys-v1)(config-if-eth0/0)# ipv6 enable
hostname(vsys-v1)(config-if-eth0/0)# ipv6 address 2222::1/64
hostname(vsys-v1)(config-if-eth0/0)# exit
hostname(config)#
为VSYS-v1配置路由
hostname(vsys-v1)(config)# ip vrouter vsys-v1-vr
hostname(vsys-v1)(config-vrouter)# ipv6 route 3333::1/64 6666::2
hostname(vsys-v1)(config-vrouter)# exit
hostname(vsys-v1)(config)# policy-global
hostname(vsys-v1)(config-policy)# default-action permit
hostname(vsys-v1)(config-policy)# exit
hostname(vsys-v1)(config)# exit-vsys
hostname(config)#
第三步：VSYS-v2的配置。
hostname(config)# enter-vsys vsys-v2
hostname(vsys-v2)(config)# interface vwanif2
hostname(vsys-v2)(config-if-vwa2)# zone vsys-v2-trust
hostname(vsys-v2)(config-if-vwa2)# ipv6 enable
hostname(vsys-v2)(config-if-vwa2)# ipv6 address 6666::2/64

<!-- 来源页 968 -->
hostname(vsys-v2)(config-if-vwa2)# exit
hostname(vsys-v2)(config)# interface ethernet0/2
hostname(vsys-v2)(config-if-eth0/2)# zone vsys-v2-trust
hostname(vsys-v2)(config-if-eth0/2)# ipv6 enable
hostname(vsys-v2)(config-if-eth0/2)# ipv6 address 3333::1/64
hostname(vsys-v2)(config-if-eth0/2)# exit
hostname(config)#
为VSYS-v2配置路由
hostname(vsys-v2)(config)# ip vrouter vsys-v2-vr
hostname(vsys-v2)(config-vrouter)# ipv6 route 2222::1/64 6666::1
hostname(vsys-v2)(config-vrouter)# exit
hostname(vsys-v2)(config)# policy-global
hostname(vsys-v2)(config-policy)# default-action permit
hostname(vsys-v2)(config-policy)# exit
hostname(vsys-v2)(config)# exit-vsys
hostname(config)#
