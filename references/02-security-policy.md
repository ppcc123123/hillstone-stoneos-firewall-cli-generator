# 安全策略

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 5 安全策略
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 396 -->
5 安全策略
本章节包含以下内容：
l "策略介绍" 在第395页：介绍了安全策略的基本概念，配置策略规则、策略组、网页重定向，查看策略规则等。
l "共享接入" 在第451页：介绍了配置共享接入规则，配置共享接入特征库，共享接入日志等。
l "ARP防护介绍" 在第457页：介绍了如何配置ARP防护功能保护网络免受各种ARP攻击。
l "全局黑白名单" 在第466页：介绍了如何通过黑白名单对流量进行管控，包括边界流量过滤、域名管控、URL管
控等。

<!-- 来源页 397 -->
策略（Policy）
策略介绍
安全策略是网络安全设备的基本功能，控制安全域间/不同地址段间的流量转发。默认情况下，网络安全设备
会拒绝设备上所有安全域/地址段之间的信息传输。而安全策略则通过策略规则决定从一个（多个）安全域到
另一个（多个）安全域，以及从一个地址段到另一个地址段的哪些流量该被允许，哪些流量该被拒绝。
提示: 安全策略支持指定IPv4和IPv6格式的地址条目。如接口开启了IPv6功能，用户可根据需要配
置IPv6地址的策略规则。
策略规则的基本元素
策略规则允许或者拒绝从一个（多个）安全域到另一个（多个）安全域/从一个地址段到另一个地址段的流
量。流量的类型、流量的源安全域/源地址与目的安全域/目的地址以及行为构成策略规则的基本元素。
策略规则的基本元素包括：
l 流量的源安全域/源地址
l 流量的目的安全域/目的地址
l 流量的服务类型
l 设备在遇到指定类型流量时所做的行为，包括允许（Permit）、拒绝（Deny）、隧道（Tunnel）、是否来自隧
道（Fromtunnel）、Web认证以及Portal服务器六个行为
定义策略规则
一般来讲，策略规则分为两部分：过滤条件和行为。安全域间流量的源安全域/源地址、目的安全域/目的地
址、服务类型以及用户构成策略规则的过滤条件。策略规则都有其独有的ID号。策略规则ID会在定义规则时
自动生成，同时用户也可以按自己的需求为策略规则指定ID。整个系统的所有策略规则有特定的排列顺序。
在流量进入系统时，系统会对流量按照找到的第一条与过滤条件相匹配的策略规则进行处理。
提示: 不同设备平台支持的全局最大策略规则数不同。
配置策略规则
用户可以通过配置策略规则，对进入设备的流量进行控制。策略规则配置包括：

<!-- 来源页 398 -->
l 进入策略配置模式
l 切换多安全域模式
l 创建策略规则
l 编辑策略规则
l 启用/禁用策略规则
l 标记策略规则
l 配置服务
l 开启/关闭发送TCP重置报文功能
l 开启/关闭发送ICMP不可达报文功能
l 绑定终端标签
l 指定Policy缺省行为
l 修改规则排列顺序
l 策略规则的日志管理
l 启用/禁用记录策略配置变更
l 启用/禁用策略匹配信息的HA同步功能
l 配置策略匹配DNAT转换后的目的地址
l 配置策略规则的会话超时时间
l 开启/关闭延迟地址更新时间功能
l 开启/关闭策略匹配加速功能
l 开启/关闭策略流量统计功能
l 配置策略规则的开始时间
l 配置策略规则的过期时间
l 设置策略更新对CPU的占用率上限
l 查看策略规则信息
l 查看设备的当前策略配置信息
l 查看策略规则匹配次数
l 查看指定状态的策略规则
l 清除策略规则命中统计信息

<!-- 来源页 399 -->
l 查看长连接会话状态信息
l 查看包含指定服务关键字的策略规则
l 查看策略规则中资源使用情况
l 配置全局记录日志功能
进入策略配置模式
进入策略配置模式，在全局配置模式下使用以下命令：
policy-global
切换多安全域模式
系统支持多安全域模式和单安全域模式的切换。单安全域模式下，一条策略仅支持配置一个源安全域和一个
目的安全域；多安全域模式下，一条策略支持同时配置多个安全域，以减少系统中所需配置的策略数量，方
便用户对策略进行管理，一条策略支持最多配置16个源/目的安全域。默认情况下，系统使用单安全域模
式。在策略配置模式下，执行以下命令切换多安全域模式：
multi-zone-enable
在策略配置模式下，使用该命令no的形式，恢复单安全域模式。
no multi-zone-enable
注意: 仅当系统中没有配置多个安全域的策略时，可以使用该命令的no形式恢复至单安全域模式，
否则该命令会执行失败。
创建策略规则
在全局配置模式或者策略配置模式下，执行以下命令创建策略规则：
rule [id id] [name name] [config-mode create] [top | before {name rule-name | id} | after
{name rule-name | id} ] [role {UNKNOWN | role-name} | user aaa-server-name user-name |
user-group aaa-server-name user-group-name] [from {host host-name | range min-ip maxip | src-addr }] [to {host host-name | range min-ip max-ip | dst-addr }] [from-zone zonename to-zone zone-name] [service service-name ] [application app-name ] [permit | deny |
tunnel tunnel-name | fromtunnel tunnel-name | webauth | portal-server portal-server-url]
l
id id – 指定策略规则的ID。如果不指定，系统将会为策略规则自动分配一个ID。规则ID在整个系统中必
须是唯一的。
l
name name – 指定策略规则的名称。策略规则名称不允许和系统中已创建的策略规则名称重复。

<!-- 来源页 400 -->
l
config-mode create – 指定该参数后，若当前所配置的策略的ID或名称与已创建策略重复，则当前策
略将配置失败，系统会提示该策略已存在，防止用户在创建新策略时误修改已有策略。
l
top | before {name rule-name | id} | after {name rule-name | id} – 指定策略规则的位置。默认
情况下，系统会将新创建的策略规则放到所有规则的末尾。
l
top - 指定策略规则的位置为所有规则的首位。
l
before {name rule-name | id} – 指定策略规则的位置为某个规则ID或者名称之前。
l
after {name rule-name | id – 指定策略规则的位置为某个规则ID或者名称之后。
l
role {UNKNOWN | role-name} | user aaa-server-name user-name | user-group aaaserver-name user-group-name – 指定策略规则的角色/用户/用户组。
l
role {UNKNOWN | role-name} – 指定角色名称，其中UNKNOWN是系统预留的角色，是既没
有经过系统认证也没有静态绑定的角色，最多支持配置8个。
l
user aaa-server-name user-name – 指定用户。aaa-server-name为用户所属的AAA服务
器名称，user-name为用户名称。
l
user-group aaa-server-name user-group-name – 指定用户组。aaa-server-name为用
户组所属的AAA服务器名称，user-group-name为用户组名称。
l
from {host host-name | range min-ip max-ip | src-addr } – 指定策略规则的源地址。
l
host host-name - 为地址簿中定义的主机类型的源地址条目。
l
range min-ip max-ip – 为地址簿中定义的IP地址段类型的源地址条目。
l
src-addr – 为地址簿中定义的地址条目。
l
to {host host-name | range min-ip max-ip | dst-addr } – 指定策略规则的目的地址。
l
host host-name – 为地址簿中定义的主机类型的目的地址条目。
l
range min-ip max-ip – 为地址簿中定义的IP地址段类型的目的地址条目。
l
dst-addr - 为地址簿中定义的地址条目。
l
from-zone zone-name – 指定策略规则的源安全域。
l
to-zone zone-name – 指定策略规则的目的安全域。
l
service service-name – 指定策略规则的服务名称。service-name为服务簿中定义的服务。
l
application app-name – 指定策略规则的应用名称。app-name为应用簿中定义的应用。
l
permit | deny | tunnel tunnel-name | fromtunnel tunnel-name | webauth | portal-server
portal-server-url – 指定对匹配策略规则的流量所采取的行为。

<!-- 来源页 401 -->
l
permit - 允许流量通过。
l
deny - 拒绝流量通过。
l
tunnel - 当流量为从本地到对端时，使用该行为使流量通过VPN隧道。
l
fromtunnel - 当流量为从对端到本地时，如果使用该行为，系统将会首先判断流量是否来自隧
道，只有来自隧道的流量才会被允许通过。
l
webauth - 对符合条件的流量进行Web认证。
l
portal-server portal-server-url – 对符合条件的流量进行Portal认证。portal-server-url
指定Portal认证服务器地址，范围为1到63个字符。URL地址格式为“www.abc.com”或
“https://www.abc.com”。
切换至多安全域模式后，重复配置以上命令可以添加多个源/目的安全域，每条策略最多支持配置16个源/目
的安全域。若安全域选定Any，则不可再添加其他安全域。
例如，创建允许从任意地址到任意地址的ICMP服务的策略规则，请输入以下命令：
hostname(config)# policy-global
hostname(config-policy)# rule from any to any service icmp permit
Rule id 5 is created.
删除策略规则，在全局配置模式或者策略配置模式下，使用以下命令：
no rule {id id | name name}
l
id id – 删除指定ID的策略规则。
l
name name – 删除指定名称的策略规则。
关于如何配置其它策略相关参数，请参考下一节“编辑策略规则”。
编辑策略规则
创建好的策略规则可以进行编辑来修改不合适的参数值，但是修改工作必须在规则配置模式下进行。
提示:
配置策略中的域名有两种方式：策略规则中的源/目的地址中的“主机名称”，和“域名”
（domain）。策略规则中配置域名/域名簿/外部动态列表类型的域名时，目的地址需要指定为
any。

<!-- 来源页 402 -->
l
当策略规则中源/目的地址配置为主机名称时，系统先对主机名称做DNS解析，解析成IP地址。
流量匹配策略时，对于源/目的地址实际是匹配相应的IP地址。
l
当策略规则中配置域名（domain）时，策略会对报文中的域名字符串（例如abc.com）做匹
配。
在CLI中进入策略规则配置模式，请在全局配置模式或策略配置模式下输入以下命令：
rule [id id] [namename] [config-mode create] [top | before {name name | id} | after {name
name | id}]
l
id id – 指定策略规则的ID。如果不指定，系统将会为策略规则自动分配一个ID。规则ID在整个系统中必
须是唯一的。
l
name name – 指定策略规则的名称。策略规则名称不允许和系统中已创建的策略规则名称重复。
l
config-mode create – 指定该参数后，若当前所配置的策略的ID或名称与已创建策略重复，则当前策
略将配置失败，系统会提示该策略已存在，防止用户在创建新策略时误修改已有策略。
l
top | before {name name | id} | after {name name | id} – 指定策略规则的位置。默认情况下，系
统会将新创建的策略规则放到所有规则的末尾。
l
top - 指定策略规则的位置为所有规则的首位。
l
before {name name | id} – 指定策略规则的位置为某个规则ID或者名称之前。
l
after {name name | id }– 指定策略规则的位置为某个规则ID或者名称之后。
进入策略规则配置模式后，可使用的编辑策略规则的命令如下：
l
命名/重新命名策略规则：name policy-name
l
单安全域模式下指定/修改/删除安全域：
l
指定/修改源安全域：src-zone src-zone
l
删除源安全域：no src-zone（执行该命令后，策略规则无源安全域限制）
l
指定/修改目的安全域：dst-zone dst-zone
l
删除目的安全域：no dst-zone（执行该命令后，策略规则无目的安全域限制）
l
多安全域模式下指定/修改/删除安全域：
l
指定/修改源安全域：src-zone src-zone（切换至多安全域配置模式后，当源安全域不是Any
时，重复该命令可配置多个安全域，最多配置16个）

<!-- 来源页 403 -->
l
删除源安全域：no src-zone [src-zone]（重复执行该命令，可以删除指定安全域。若不指定具
体的安全域，则会删除全部安全域，此时表示策略规则无源安全域限制）
l
指定/修改目的安全域：dst-zone dst-zone（切换至多安全域配置模式后，当源安全域不是Any
时，重复该命令可配置多个安全域，最多配置16个）
l
删除目的安全域：no dst-zone [dst-zone]（重复执行该命令，可以删除指定安全域。若不指定
具体的安全域，则会删除全部安全域，此时表示策略规则无源安全域限制）
l
添加地址簿条目类型源地址：src-addr src-addr
l
删除地址簿条目类型源地址：no src-addr src-addr
l
添加IP成员类型源地址：src-ip ip/netmask
l
删除IP成员类型源地址：no src-ip ip/netmask
l
添加主机成员类型源地址：src-host host-name
l
删除主机成员类型源地址：no src-host host-name
l
添加IP地址范围类型源地址：src-range min-ip [max-ip]
l
删除IP地址范围类型源地址：no src-range min-ip [max-ip]
l
添加源设备：src-device-group device-name
l
删除源设备：no src-device-group device-name
l
添加地址簿条目类型目的地址：dst-addr dst-addr
l
删除地址簿条目类型目的地址：no dst-addr dst-addr
l
添加IP成员类型目的地址：dst-ip {ip/netmask | ip-address netmask}
l
删除IP成员类型目的地址：no dst-ip {ip/netmask | ip-address netmask}
l
添加主机成员类型目的地址：dst-host host-name
l
删除主机成员类型目的地址：no dst-host host-name
l
添加IP地址范围类型目的地址：dst-range min-ip [max-ip]
l
删除IP地址范围类型目的地址：no dst-range min-ip [max-ip]
l
添加目的设备：dst-device-group device-name
l
删除目的设备：no dst-device-group device-name
l
添加域名：domain domain-name（domain-name取值范围1到255个字符，最多可添加1024个域
名。）

<!-- 来源页 404 -->
l
删除域名：no domain domain-name
l
指定域名簿：domain-book domain-book-name（最多可指定8个域名簿。）
l
删除域名簿：no domain-book domain-book-name
l
添加服务类型：service service-name
l
删除服务类型：no service service-name
l
添加/删除服务规则：服务规则包括服务的协议类型和端口号，可以根据需要的协议和端口号，配置服务
规则并在策略中添加该服务规则。关于如何添加/删除服务规则，请参阅配置服务规则。
l
添加应用类型：application application-name
l
删除应用类型：no application application-name
l
指定角色：role {UNKNOWN | role-name}
l
删除角色：no role {UNKNOWN | role-name}
l
指定用户：user aaa-server-name user-name
l
删除用户：no user aaa-server-name user-name
l
指定用户组：user-group aaa-server-name user-group-name
l
删除用户组：no user-group aaa-server-name user-group-name
l
修改处理行为：action {permit | deny | tunnel | fromtunnel | webauth | portal-server portalserver-url}
o
permit - 允许流量通过。
o
deny - 拒绝流量通过。
o
tunnel - 当流量为从本地到对端时，使用该行为使流量通过VPN隧道。
o
fromtunnel - 当流量为从对端到本地时，如果使用该行为，系统将会首先判断流量是否来自隧
道，只有来自隧道的流量才会被允许通过。
o
webauth - 对符合条件的流量进行Web认证。
o
portal-server portal-server-url – 对符合条件的流量进行Portal认证。portal-server-url
指定Portal认证服务器地址，范围为1到63个字符。URL地址格式为“www.abc.com”或
“https://www.abc.com”。
l
配置VLAN ID：vlan-id vlan-id
l
删除VLAN ID：no vlan-id vlan-id
l
配置时间表：schedule schedule-name

<!-- 来源页 405 -->
l
删除时间表：no schedule schedule-name
提示: 默认情况下，配置的策略规则会即时生效，而当为策略规则配置时间表功能后，策略规则就
只在时间表所指定的时间内生效。用户最多可以为一条策略规则配置8个时间表，策略规则的生效
时间为所有被配置到该策略规则的时间表的时间的总和。关于如何配置时间表，请参阅“系统管
理”的“配置时间表”部分。
l
添加描述：description description（description的取值范围是1到255字节）
l
删除描述：no description description
l
添加规则的QoS标签：policy-qos-tag tag（tag的取值范围是1到1024）
l
删除规则的QoS标签：no policy-qos-tag tag
提示: 用户可以为策略中允许通过的流量添加QoS标签。关于QoS配置，请参阅《流量管理》。
l
绑定病毒过滤Profile：av {av-profile-name | no-av}（no-av参数表示绑定系统预定义的名为“noav”的病毒过滤Profile，含义为不做病毒过滤检测）
l
取消病毒过滤Profile的绑定：no av
l
绑定IPS Profile：ips {no-ips | predef_default | predef_loose | predef_critical | DMZ-server |
General-server | web-server | Unix-like-server | Windows-server | ips-profile-name}（noips参数表示绑定系统预定义的名为“no-ips”的IPS Profile，含义为不做IPS检测；ips-profilename表示绑定系统自定义的IPS Profile）
l
取消IPS Profile的绑定：no ips
l
绑定行为Profile：behavior {behavior-profile-name | no-behavior}（no-behavior参数表示绑
定系统预定义的名为“no-behavior”的行为Profile，含义为不做行为控制）
l
取消行为Profile的绑定：no behavior
l
绑定内容过滤Profile：contentfilter {contentfilter-profile-name | no-contentfilter}（nocontentfilter参数表示绑定系统预定义的名为“no-contentfilter”的内容过滤Profile，含义为不做
内容过滤）
l
取消内容过滤Profile的绑定：no contentfilter
l
绑定邮件过滤Profile：mail {mail-profile-name | no-mail}（no-mail参数表示绑定系统预定义的
名为“no-mail”的邮件过滤Profile，含义为不做邮件过滤）

<!-- 来源页 406 -->
l
取消邮件过滤Profile的绑定：no mail
l
绑定网络聊天Profile：im {im-profile-name | no-im}（no-im参数表示绑定系统预定义的名为
“no-im”的网络聊天Profile，含义为不做网络聊天监控）
l
取消网络聊天Profile的绑定：no im
l
绑定Web外发信息Profile: webpost {webpost-profile-name | no-webpost}（no-webpost参数
表示绑定系统预定义的名为“no-webpost”的Profile，含义为不做Web外发信息检测）
l
取消Webpost Profile的绑定：no webpost
l
绑定URL过滤Profile: url {url-profile-name | no-url}（no-url参数表示绑定系统预定义的名为
“no-url”的Profile，含义为不做URL过滤检测）
l
取消URL过滤Profile的绑定：no url
l
绑定GTP Profile：gtp-profile profile-name
l
取消GTP Profile的绑定：no gtp-profile
l
绑定ACL Profile：acl acl-profile-name
l
取消ACL Profile的绑定：no acl
启用/禁用策略规则
默认情况下，配置好的策略规则会在系统中立即起效。用户可以通过命令禁用某条策略规则，使其不对流量
进行控制。禁用或者启用某条策略规则，在策略规则配置模式下，使用以下命令：
l
禁用：disable
l
启用：enable
为策略规则添加标记
为策略规则添加标记，在规则配置模式下，使用以下命令：
tag name name
l
name–指定标签的名称。取值范围是1到63个字符。单条策略最多可添加8个标签。
在规则配置模式下，使用no tag name name删除已添加的标签。
配置服务
在配置策略规则的服务时，可以添加服务簿中已配置好的预定义服务或者自定义服务。当所需要的服务在服
务簿中不存在时，管理员可以通过配置服务规则，直接指定服务的协议类型以及端口号等信息，从而简化策
略的配置步骤。

<!-- 来源页 407 -->
配置TCP或者UDP类型服务规则，在策略规则配置模式下，使用以下命令：
service-rule {tcp | udp} dst-port min-port [max-port] [src-port min-port [max-port]]
l
tcp | udp - 指定服务规则的协议类型：TCP或者UDP。
l
dst-port min-port [max-port] – 指定服务规则的目的端口号。如果目的端口号为一个范围，minport为最小目的端口号，max-port为最大目的端口号；如果不配置max-port，系统将使用min-port
作为单一目的端口号。目的端口号的范围是0到65535。
l
src-port min-port [max-port] – 指定服务规则的源端口号。如果源端口号为一个范围，min-port为
最小源端口号，max-port为最大源端口号；如果不配置max-port，系统将使用min-port作为单一源
端口号。源端口号的范围是0到65535。
配置ICMP类型服务规则，在策略规则配置模式下，使用以下命令：
service-rule icmp type type-value [code min-code [max-code]]
l
type-value – 指定服务规则的ICMP type值。取值范围是0-255，详情请参阅附表：ICMP Type以及
Code值对照表。
l
code min-code [max-code] – 指定服务规则的ICMP code值。如果ICMP code值为一个范围，
min-code为最小code值，max-code为最大code值；如果不配置max-code，系统将使用mincode作为单一code值。取值范围是0到255。默认值是min-code为0、max-code为255。
配置ICMPv6类型服务规则，在策略规则配置模式下，使用以下命令：
service-rule icmpv6 type type-value [code min-code [max-code]]
l
type-value – 指定服务规则的ICMPv6 type值。取值范围为0-255，详情请参阅附表：ICMPv6 Type
以及Code值对照表。
l
code min-code [max-code] – 指定服务规则的ICMPv6 code值。如果ICMPv6 code值为一个范
围，min-code为最小code值，max-code为最大code值；如果不配置max-code，系统将使用mincode作为单一code值。取值范围是0到255。默认值是min-code为0、max-code为255。
配置SCTP类型服务规则，在策略规则配置模式下，使用以下命令：
service-rule sctp dst-port min-port [max-port] [src-port min-port [max-port]]
l
dst-port min-port [max-port] – 指定服务规则的目的端口号。如果目的端口号为一个范围，minport为最小目的端口号，max-port为最大目的端口号；如果不配置max-port，系统将使用min-port
作为单一目的端口号。目的端口号的范围是0到65535。

<!-- 来源页 408 -->
l
src-port min-port [max-port] – 指定服务规则的源端口号。如果源端口号为一个范围，min-port为
最小源端口号，max-port为最大源端口号；如果不配置max-port，系统将使用min-port作为单一源
端口号。源端口号的范围是0到65535。
配置其它类型服务规则，在策略规则配置模式下输入以下命令：
service-rule protocol protocol-number
l
protocol-number – 指定服务规则的协议号。范围是1到255。
使用以上命令no的形式可以删除对应服务规则。
l
no service-rule{tcp | udp} dst-port min-port [max-port] [src-port min-port [max-port]]
l
no service-rule icmp type type-value [code min-code [max-code]]
l
no service-rule icmpv6 type type-value [code min-code [max-code]]
l
no service-rule sctp dst-port min-port [max-port] [src-port min-port [max-port]]
l
no service-rule protocol protocol-number
开启/关闭发送TCP重置报文功能
开启发送TCP重置报文功能后，当策略阻断流量时，系统会向对应的TCP报文发送端返回重置报文，从而快
速断开连接。该功能默认为关闭状态。
注意:
l
该功能仅在策略动作为“拒绝”时生效。
l
该功能仅适用于新建会话场景。
开启发送TCP重置报文，在策略规则配置模式下，使用以下命令：
send-deny-packet reset
关闭发送TCP重置报文，在策略规则配置模式下，使用以下命令：
no send-deny-packet reset
开启/关闭发送ICMP不可达报文功能
开启发送ICMP不可达报文功能后，当策略阻断流量时，系统会向对应的UDP/ICMP报文发送端返回ICMP不
可达报文，从而快速断开连接。该功能默认为关闭状态。

<!-- 来源页 409 -->
注意:
l
该功能仅在策略动作为“拒绝”时生效。
l
该功能仅适用于新建会话场景。
开启发送ICMP不可达报文功能，在策略规则配置模式下，使用以下命令：
send-deny-packet icmp-destination-unreachable
关闭发送ICMP不可达报文功能，在策略规则配置模式下，使用以下命令：
no send-deny-packet icmp-destination-unreachable
配置策略的硬件快转功能
型号说明：
l
支持：SG-6000-A7600、A6800以及A系列ASIC防火墙。
l
支持：SG-6000-K20803、K7680、K7280、K6680以及K系列ASIC防火墙。
开启策略的硬件快转功能后，将由专门的硬件芯片转发命中该策略的流量，从而降低CPU负载，提升大流量
场景下的转发性能。
配置策略的硬件快转功能，在策略规则配置模式下，使用以下命令：
hardware-fast-forward {use-global-config | enable | disable}
l
use-global-config - 指定该策略的硬件快转功能的启用状态和全局硬件快转功能保持一致。该配置为
默认配置。配置全局硬件快转功能参见“防火墙> 硬件快转”章节。
l
enable - 指定单独开启该策略的硬件快转功能，不受全局硬件快转功能状态影响。
l
disable - 指定单独关闭该策略的硬件快转功能，不受全局硬件快转功能状态影响。
绑定终端标签
在防火墙与智铠（EDR）联动管控场景，或者基于ZTNA的内网安全改造场景下，用户可以通过指定策略规
则的终端标签，对匹配终端标签的流量进行访问控制。
每条安全策略可以绑定最多10个终端标签，多个终端标签之间是逻辑“或”的关系，用户匹配其中的任何一
个终端标签，即认为命中了该条策略的终端标签维度。当策略中不绑定任何终端标签时，表示所有终端标签
都可以匹配。
将指定终端标签与安全策略绑定，在策略配置模式下，使用以下命令：

<!-- 来源页 410 -->
endpoint-tag {UNKNOWN-DEVICE | tag-name}
l
UNKNOWN-DEVICE - 系统预留的终端标签，表示未安装EDR和ZTNA客户端的设备，无法进行终端信
息收集与合规性检查。
l
tag-name - 指定需要绑定的终端标签名称。
取消安全策略与指定终端标签的绑定，在策略配置模式下，使用以下命令：
no endpoint-tag tag-name
指定Policy缺省行为
用户可以为未匹配到任何已配置策略规则的流量指定缺省行为，系统将按照指定的缺省行为对此类流量进行
处理。默认情况下，系统会拒绝未匹配到任何已配置策略规则的流量通过。指定缺省行为为允许，在策略配
置模式下，使用以下命令：
default-action permit
在策略配置模式下，使用该命令no的形式，恢复缺省行为为“拒绝”：
no default-action permit
修改规则排列顺序
每一条策略规则都有唯一一个ID号和名称。流量进入Hillstone设备时，Hillstone设备对策略规则进行顺序
查找，然后按照查找到的相匹配的第一条规则对流量进行处理。但是，策略规则ID的大小顺序并不是规则查
找时的匹配顺序。使用show policy命令列出的规则顺序才是规则匹配顺序（系统将由上到下进行查找）。
用户在创建策略规则时可以指定该规则的排列位置，也可以在策略配置模式下修改其位置。策略规则的排列
位置可以是绝对位置，即处在首位（Top）或者处在末位（Bottom），也可以是相对位置，即位于某个ID
或者名称的前后。修改规则排列顺序，在策略配置模式下使用以下命令：
move {name name | id} {top | bottom | before {name rule-name | id} | after {name rule-name
| id} }
l
name name | id – 指定需要修改排列顺序的策略规则ID或者名称。
l
top – 指定策略规则修改后的位置为所有规则的首位。
l
before {name rule-name | id} – 指定策略规则修改后的位置为某个规则ID或者名称之前。
l
after {name rule-name | id} – 指定策略规则修改后的位置为某个规则ID或者名称之后。

<!-- 来源页 411 -->
策略规则的日志管理
l
对于permit类型的策略规则，可以记录两种情况，分别是符合策略规则的流量建立会话时生成日志信息
和结束会话时生成日志信息。
l
对于deny类型的策略规则，可以记录的情况为：符合策略规则的流量被deny时生成日志信息。
使用该功能前，必须保证系统的流量日志功能是开启的，即在全局配置模式下，执行logging traffic on命
令。配置规则的日志管理，在策略规则配置模式下，使用以下命令：
log {policy-deny | session-start | session-end}
l
policy-deny – 适用于deny类型的策略规则。使系统生成规则拒绝流量的日志信息。
l
session-start – 适用于permit类型的策略规则。使系统生成会话建立的日志信息。
l
session-end – 适用于permit类型的策略规则。使系统生成会话结束的日志信息。
使用no log {policy-deny | session-start | session-end}命令取消策略规则日志管理功能的配置。
另外，对于从指定源安全域到目的安全域的未匹配到策略规则的流量，用户可以指定是否为其生成日志信
息。默认情况下，系统不为此类流量生成日志信息。生成日志信息，在策略配置模式下，使用以下命令：
log policy-default
在策略配置模式下，使用该命令no的形式恢复默认值：
no log policy-default
启用/禁用记录策略配置变更
默认情况下，当策略规则配置信息发生变更时，系统自动将配置变更记录在事件日志中；当微型策略配置信
息发生变更时，系统将不会记录配置变更记录在事件日志中。
禁用或者启用记录微型策略或者策略规则配置变更的日志信息，在策略配置模式下，使用以下命令：
modification-log { mini-policy | policy } {enable | disable}
l
mini-policy - 指定启用/禁用记录微型策略配置变更日志信息。
l
policy - 指定启用/禁用记录策略规则配置变更日志信息。
l
enable - 启用记录配置变更日志信息。
l
disable - 禁用记录配置变更日志信息。
启用/禁用策略匹配信息的HA同步功能
默认情况下，在HA环境中，微型策略和策略规则的匹配信息会在主备设备之间自动同步。禁用或启用微型策
略和策略规则的匹配信息的HA同步功能，在策略配置模式下，使用以下命令：

<!-- 来源页 412 -->
l
启用：hit-info-ha-sync
l
禁用：no hit-info-ha-sync
配置策略匹配DNAT转换后的目的地址
系统支持策略匹配DNAT转换前的目的地址，或者匹配DNAT转换后的目的地址。默认情况下，策略匹配
DNAT转换前的目的地址。
配置策略匹配DNAT转换后的目的地址，在策略配置模式下，使用以下命令：
match-after-dnat
在策略配置模式下，使用该命令的no形式恢复策略匹配DNAT转换前的目的地址。
no match-after-dnat
开启/关闭延迟地址更新时间功能
系统支持开启延迟地址更新时间功能，即用户在批量修改地址簿中的地址条目后，系统不会立即将修改后的
地址条目同步给引用该地址簿的策略，而是在指定的延迟时间结束后进行同步，可以避免由于策略引用的地
址簿成员频繁变更而造成配置下发缓慢的情况。默认情况下，延迟地址更新时间功能为关闭状态。
开启延迟地址更新时间功能，在策略配置模式下，使用以下命令：
delay-address-update-time time_value
l
time_value – 指定延迟时间，范围是1到3秒。指定后，如果策略引用的地址簿中的地址条目发生变
更，系统不会立即将变更后的地址条目同步给策略，而是在指定的延迟时间结束后进行同步。
在策略配置模式下，使用no delay-address-update-time命令关闭延迟地址更新时间功能。
开启/关闭策略匹配加速功能
当在极限情况下，系统中存在大量策略时，用户可以开启策略匹配加速功能。功能生效后，系统会生成两份
策略索引，在策略变更（包括新建/修改/删除策略）时更新其中一份索引。在新索引更新完成之前，系统会
使用原索引进行策略匹配，从而防止由于策略变更导致策略匹配中断，保证较高的处理效率，但是变更后的
策略不会立即生效。用户还可以配置匹配备份延迟时间，系统会在策略变更后的指定延迟时间后，使用新索
引进行策略匹配。该功能默认为关闭状态。
用户可以根据实际情况选择是否开启策略匹配加速功能：
l
当策略数量较多或策略配置变更频繁时，为了保证策略变更时的策略匹配速率，可以开启策略匹配加速
功能。但开启该功能后，将会占用更多内存，并且新的策略配置会延迟生效。
l
当策略数量较少时，可以关闭策略匹配加速功能。

<!-- 来源页 413 -->
注意:
l
策略匹配加速功能不支持VSYS。
l
配置策略匹配加速功能后，需重启系统使配置生效。
开启策略匹配加速功能，在策略配置模式下，使用以下命令：
policy-match-accelerate [delay delay-time]
l
policy-match-accelerate - 开启策略匹配加速功能。
l
delay delay-time - 指定匹配备份延迟时间，取值范围为1-43200秒，默认为60秒。
关闭策略匹配加速功能，在策略配置模式下，使用以下命令：
no policy-match-accelerate
查看策略匹配加速功能，在策略配置模式下，使用以下命令：
show policy
开启/关闭会话重匹配策略功能
默认情况下，会话重匹配策略功能为开启状态。当用户添加、修改或删除策略时，已存在的会话所匹配的策
略可能会发生变化，系统会根据会话重匹配策略功能的配置做出不同的操作：
l
若会话重匹配策略功能为开启状态，则系统会为已存在的会话重新匹配策略，并且删除匹配的策略发生
变化的会话。
l
若会话重匹配策略功能为关闭状态，则系统不会为已存在的会话重新匹配策略，原有会话会继续保持直
到超时。
开启/关闭会话重匹配策略功能，在策略配置模式下，使用以下命令关闭：
l
关闭：session-rematch off
l
开启：no session-rematch off
开启/关闭策略流量统计功能
策略流量统计功能能够统计命中策略规则的系统流量的信息，包括上行报文数、下行报文数、上行字节数、
下行字节数。默认情况下，策略流量统计功能为关闭状态。开启策略流量统计功能，在策略配置模式下，使
用以下命令：
policy-traffic-statistic
在策略配置模式下，使用no policy-traffic-statistic命令关闭策略流量统计功能。

<!-- 来源页 414 -->
查看策略流量统计功能状态
查看策略流量统计功能是开启还是关闭状态，在任意模式下，使用以下命令：
show policy traffic-statistic-status
配置策略规则的起始时间
系统支持为策略规则配置起始时间，即当系统时间运行到该起始时间时，策略规则才会生效。配置策略规则
的起始时间，在策略规则配置模式下，使用以下命令：
start-time time_value
l
time_value - 指定策略规则的起始时间，格式为“MM/DD/YYYY HH:MM:SS”例如：06/07/2024
17:49:32。
配置策略规则的过期时间
系统支持为策略规则配置过期时间，即当系统时间运行到该过期时间时，策略规则将会失效。配置策略规则
的过期时间，在策略规则配置模式下，使用以下命令：
expire-time time_value
l
time_value - 指定策略规则的过期时间，格式为“MM/DD/YYYY HH:MM:SS”例如：06/07/2024
17:49:32
设置策略更新对CPU的占用率上限
用户可以通过设置策略更新占用的CPU上限，来达到对CPU占用率的有效控制和调节，从而防止在大量更新
策略时设备的CPU占用率过高，影响业务运行。
注意: 该功能只适用于策略更新场景，比如因为地址簿、服务簿引发的策略更新。并且该功能只能
够控制策略更新占用的CPU，不能直接控制最终整体的CPU占用率。如果更新策略时有其他进程在
占用CPU，则最终的CPU占用率可能会高于设置的上限。
设置策略更新对CPU的占用率上限，在策略配置模式下，使用以下命令：
policy-update-cpu-control number
l
numer - 指定策略更新对CPU的占用率上限，取值范围为10-90。
取消设置策略更新对CPU的占用率上限，在策略配置模式下，使用以下命令：
no policy-update-cpu-control
查看策略更新对CPU的占用率上限，在任意模式下，使用以下命令：

<!-- 来源页 415 -->
show policy
查看包含指定服务关键字的策略规则
服务包含协议类型、端口号等信息，当策略规则调用服务时，用户可以将服务信息作为关键字进行模糊搜
索，从而筛选出所有包含指定服务关键字的策略规则。
查看包含指定服务关键字的策略规则，在任意模式下，使用以下命令：
show policy service keyword string
l
string – 指定关键字，范围是1到95个字符。
查看策略规则中资源使用情况
查看策略规则中源地址、目的地址和服务的资源使用情况，即查看策略规则中配置的源地址、目的地址和服
务数量占总可配数量的比例，在任何命令模式下输入以下命令：
show policy resource
例如：
hostname(config)# show policy resource
Resource usage:
address: 2%(10000 of 480000; src-addr usage: 5000; dst-addr usage: 5000; current
available: 470000)
service: 4%(10000 of 240000; current available: 230000)
以上策略规则中已配置的源地址为5000条，已配置目的地址为5000条，已配置的源地址和目的地址占系
统可配置地址总数的2%，系统当前剩余可用地址为470000条；策略规则中已配置的服务为1000个，占系
统可配置服务总数的4%。
查看策略规则信息
用户可以在任何模式下，通过show命令查看策略规则的具体信息，可以查看所有或者某条策略规则的具体
信息，也可以查看符合五元组过滤条件的策略规则的具体信息，五元组指策略规则的源IP地址、目的IP地
址、协议、源端口、目的端口。具体命令如下：
show policy [id id] [tag name][from src-zone] [to dst-zone] [src-addr src-addr] [dst-addr
dst-addr] [src-device-group [name device-name | ip ip-address]] [dst-device-group [name
device-name | ip ip-address]] [protocol | service service-name] [application applicationname] [description description] [name name] [name-filter filter-name] [user {filter-fuzzy
filter-name | filter-precise aaa-server-name filter-name}] [user-group {filter-fuzzy filter-

<!-- 来源页 416 -->
name | filter-precise aaa-server-name filter-name}] [role filter-fuzzy filter-name] [family
{ipv4 | ipv6}] [schedule-name schedule-name] [schedule-name-filter filter-schedule-name]
l
id id – 查看指定ID规则的详细信息。
l
tag name - 查看指定标签规则的详细信息。
l
from src-zone – 查看源安全域为指定域的规则的详细信息。
l
to dst-zone – 查看目标安全域为指定域的规则的详细信息。
l
src-addr src-addr – 查看指定地址簿条目类型源地址的规则的详细信息。
l
dst-addr dst-addr – 查看指定地址簿条目类型目的地址的规则的详细信息。
l
src-device-group [name device-name | ip ip-address] – 查看指定源设备（name devicename）或者指定源设备分类映射IP地址（ip ip-address）的规则的详细信息。
l
dst-device-group [name device-name | ip ip-address] – 查看指定目的设备（name devicename）或者指定目的设备分类映射IP地址（ip ip-address）的规则的详细信息。
l
protocol | service service-name - 查看指定协议（protocol）或者服务（service servicename）的规则详细信息。
l
service service-name – 查看指定服务类型的规则详细信息。
l
application application-name – 查看指定应用类型的规则详细信息。
l
description description – 查看指定描述信息的规则详细信息。
l
name name – 查看指定名称的规则详细信息。
l
name-filter filter-name – 查看名称包含指定关键字的所有规则详细信息。
l
user – 显示指定用户名称的所有规则信息。
l
user-group – 显示指定用户组名称的所有规则信息。
l
role – 显示指定角色名称的所有规则信息。
l
filter-fuzzy filter-name | filter-precise aaa-server-name filter-name – 指定使用模糊查询
（filter-fuzzy）或精准查询（filter-precise）的方式进行策略规则筛选。
l
filter-fuzzy filter-name – 指定查询方式为模糊查询。模糊查询基于指定用户/用户组/角色名
称关键字，对于输入关键字进行模糊字符串匹配，可以筛选出用户/用户组/角色维度中包含该关
键字的所有策略规则。
l
filter-precise aaa-server-name filter-name – 指定查询方式为精准查询。精准查询基于指
定用户/用户组名称，对于输入的用户/用户组名称进行精准匹配，可以筛选出用户/用户组维度中

<!-- 来源页 417 -->
与该名称相同的所有策略规则。当某一策略规则中的用户组包含所指定的用户/用户组时，该策略
规则也将被筛选出来。
l
family {ipv4 | ipv6 } – 查看仅IPv4地址、仅IPv6地址类型的规则详细信息。说明：该关键字仅当系统
版本为IPv6版本时可配。
l
schedule-name schedule-name – 查看指定时间表名称的规则详细信息。
l
schedule-name-filter filter-schedule-name – 查看时间表名称包含指定关键字的所有规则详细信
息。
注意:
l
模糊查询和精准查询是互斥的，不可同时选择。
l
将“用户”过滤条件和其他过滤条件进行“与”操作时，“用户”过滤条件需置于最后。
查看TCP或者UDP协议类型对应的策略规则，在任何模式下，使用以下命令：
show policy protocol {tcp | udp} [dst-port {port-number | range min-port max-port}] [ srcport {port-number | range min-port max-port} ]
l
tcp | udp – 指定查看TCP或者UDP协议类型的规则详细信息。
l
dst-port{ port-number | range min-port max-port} – 查看指定目的端口号规则详细信息。portnumber为单一目的端口号，如果目的端口号为一个范围，min-port为最小目的端口号，max-port为
最大目的端口号，范围是0到65535。
l
src-port {port-number | range min-port max-port} - 查看指定源端口号的规则详细信息。portnumber为单一源端口号，如果源端口号为一个范围，min-port为最小源端口号，max-port为最大源
端口号，范围是0到65535。
注意: min-port必须小于等于max-port，当min-port等于max-port时，表示指定为单一端口
号。
查看ICMP或者ICMPv6协议类型对应的策略规则，在任何模式下，使用以下命令：
show policy protocol {icmp | icmpv6} [type type-number [code {code-number | range mincode max-code}] ]
l
icmp | icmpv6 – 指定查看ICMP或者ICMPv6协议类型的规则详细信息。
l
type type-number – 查看指定ICMP type值或者ICMPv6 type值的规则详细信息。

<!-- 来源页 418 -->
l
code {code-number | range min-code max-code} - 查看指定ICMP code值或者ICMPv6 code值
的规则详细信息。code-number为单一code值，如果code值为一个范围，min-code为最小code
值，max- code为最大code值。ICMP协议类型对应的Code值取值范围为0到15，ICMPv6协议类型对
应的Code值取值范围为0到255。
注意: min-code必须小于等于max- code，当min-code等于max- code时，表示指定为单一
code值。
查看SCTP协议类型对应的策略规则，在任何模式下，使用以下命令：
show policy protocol sctp [dst-port {port-number | range min-port max-port}] [ src-port
{port-number | range min-port max-port} ]
l
[dst-port {port-number | range min-port max-port}] – 查看指定目的端口号规则详细信息。
port-number为单一目的端口号，如果目的端口号为一个范围，min-port为最小目的端口号，maxport为最大目的端口号，范围是0到65535。
l
[ src-port {port-number | range min-port max-port} ] – 查看指定源端口号的规则详细信息。
port-number为单一源端口号，如果源端口号为一个范围，min-port为最小源端口号，max-port为
最大源端口号，范围是0到65535。
注意: min-port必须小于等于max-port，当min-port等于max-port时，表示指定为单一端口
号。
查看其他指定协议类型对应的策略规则，在任何模式下，使用以下命令：
show policy protocol protocol-number
l
protocol-number – 查看指定协议号的规则详细信息。取值范围为1到255。
查看设备的当前策略配置信息
查看设备的当前策略配置信息，在任何命令模式下输入以下命令：
show configuration policy [name name | id id | by-line | last last-number]
l
name name – 单行显示指定名称的策略规则配置信息。
l
id id – 单行显示指定ID的策略规则配置信息。
l
by-line – 单行显示所有策略规则配置信息。

<!-- 来源页 419 -->
l
last last-number - 显示指定数量的策略规则配置信息，取值范围为1到2147483647。例如：若指定
last-number数值为3，则表示查看该设备配置时间最近的3个ID的策略规则配置信息。
查看策略规则匹配次数
为方便用户对策略规则的管理和维护，Hillstone设备支持策略规则匹配次数统计功能。该功能能够对系统
流量与策略规则的匹配次数进行统计，即每当进入系统的流量与某条策略规则相匹配时，该策略规则的匹配
次数会自动加1。用户可以在任何模式下通过以下命令查看策略规则匹配次数统计信息：
show policy hit-count [id id | name name | [unlimited] [from src-zone] [to dst-zone] top {10 |
20 | 50 | all }]
l
id id – 显示指定ID规则的匹配次数统计信息。
l
name name – 显示指定名称规则的匹配次数统计信息。
l
unlimited – 显示完整的策略名称和匹配次数。若不指定，系统最多显示16个字符的策略名称以及99亿
次匹配次数。
l
from src-zone – 显示源安全域为指定域的规则的匹配次数统计信息。
l
top {10 | 20 | 50 | all } – 显示匹配次数位于前10、20、50位的规则的匹配次数统计信息或者按降序方
式显示所有规则的匹配次数统计信息。
例如：
查看所有规则的匹配次数统计信息
hostname(config)# show policy hit-count
Most hit policy rules:
==============================================================================
No. Id Src-zone Dst-zone Src-addr Dst-addr Service Applica~ Action Hit-count
------------------------------------------------------------------------------
1 14 trust trust Any Any Any PERMIT 0
2 4 untrust trust Any Any Any PERMIT 1
3 3 trust untrust Any Any Any PERMIT 761697
4 1 Any Any Any Any Any PERMIT 64203455
==============================================================================
查看指定ID规则的匹配次数统计信息
hostname(config)# show policy hit-count id 1

<!-- 来源页 420 -->
Policy id 1 is hit 342424 times
查看指定名称规则的匹配次数统计信息
SG-6000(config)# show policy hit-count name a
Policy "a" is hit 0 times
查看匹配次数位于前10位的规则的匹配次数统计信息
hostname(config)# show policy hit-count top 10
Most hit policy rules:
=====================================================================
No. Id Src-zone Dst-zone Src-addr Dst-addr Service Action Hit-count
---------------------------------------------------------------------
1 4 trust trust any any http permit 40029
2 6 zone2 untrust addr1 any any deny 7487
3 3 zone2 untrust s1 d1 ftp permit 3834
4 29 trust untrust any any any permit 2899
5 14 zone1 zone2 s2 any pop3 permit 2046
按降序方式查看所有规则的匹配次数统计信息
hostname(config)# show policy hit-count top all
Most hit policy rules:
==============================================================================
No. Id Src-zone Dst-zone Src-addr Dst-addr Service Applica~ Action Hit-count
------------------------------------------------------------------------------
1 1 Any Any Any Any Any PERMIT 64212319
2 3 trust untrust Any Any Any PERMIT 762070
3 4 untrust trust Any Any Any PERMIT 1
4 14 trust trust Any Any Any PERMIT 0
==============================================================================

<!-- 来源页 421 -->
查看指定状态的策略规则
系统支持查看指定时间有效性状态的策略规则。根据策略配置的起始时间、过期时间以及时间表，策略可以
分为以下三种状态：
l
生效：策略规则当前时间为生效状态。例如，配置了处于生效状态的时间表。
l
失效：策略规则当前时间不生效，但之后的时间可能会生效。例如，配置了起始时间，且当前时间早于
开始时间。
l
过期：策略规则当前不生效，以后也不会生效。例如，配置了过期时间，且当前时间晚于过期时间。
查看指定时间有效性状态的策略规则，在任意模式下，使用以下命令：
show policy time-validity {valid | invalid | expired}
l
valid - 查看处于生效状态的策略规则。
l
invalid - 查看处于失效状态的策略规则。
l
expired - 查看处于过期状态的策略规则。
以下是一个返回结果示例：
查看策略规则命中统计信息
在CLI的任何模式下，用户可以使用相应的show命令，查看策略规则的命中统计信息，包括策略规则ID、命
中数、首次命中时间、最近一次命中时间、最近未命中天数、策略规则创建时间以及策略规则状态（启用/禁
用）。
查看所有策略规则的命中统计信息:
show policy statistic-info
查看指定ID的策略规则命中统计信息：
show policy statistic-info id id
l
id id - 指定策略规则ID。
查看创建时间距现在的天数大于指定天数的策略规则命中统计信息：

<!-- 来源页 422 -->
show policy statistic-info days-since-created value
l
days-since-created value - 指定天数。取值范围为1到3650天。
查看首次命中时间距现在的天数大于指定天数的策略规则命中统计信息：
show policy statistic-info days-since-first-hitted value
l
days-since-first-hitted value - 指定天数。取值范围为1到3650天。
查看最近一次命中时间距现在的天数大于指定天数的策略规则命中统计信息：
show policy statistic-info days-since-last-hitted value
l
days-since-last-hitted value - 指定天数。取值范围为1到3650天。
查看组合过滤条件下的策略规则命中统计信息，过滤条件包括最近一次命中时间距现在的天数大于指定天
数、首次命中时间距现在的天数大于指定天数、创建时间距现在的天数大于指定天数：
show policy statistic-info [days-since-last-hitted value] [days-since-first-hitted value]
[days-since-created value]
l
days-since-last-hitted value - 指定天数。取值范围为1到3650天。查看最近一次命中时间距现在的
天数大于指定天数的策略规则命中统计信息。
l
days-since-first-hitted value - 指定天数。取值范围为1到3650天。查看首次命中时间距现在的天
数大于指定天数的策略规则命中统计信息。
l
days-since-created value - 指定天数。取值范围为1到3650天。查看创建时间距现在的天数大于指
定天数的策略规则命中统计信息。
查看按照所有策略规则ID升序或者降序排列后的策略规则命中统计信息：
show policy statistic-info sorted-by id {ascending | descending}
l
id {ascending | descending} - 指定按照策略规则ID升序（ascending）或者降序（descending）
排列。
查看按照所有策略规则命中数升序或者降序排列后的策略规则命中统计信息：
show policy statistic-info sorted-by hit-count {ascending | descending}
l
hit-count {ascending | descending} - 指定按照策略规则命中数升序（ascending）或者降序
（descending）排列。
查看按照所有策略规则创建时间升序或者降序排列后的策略规则命中统计信息：
show policy statistic-info sorted-by created-time {ascending | descending}

<!-- 来源页 423 -->
l
created-time {ascending | descending} - 指定按照策略规则创建时间升序（ascending）或者降
序（descending）排列。
查看按照所有策略规则首次命中时间升序或者降序排列后的策略规则命中统计信息：
show policy statistic-info sorted-by first-hitted-time {ascending | descending}
l
first-hitted-time {ascending | descending} - 指定按照策略规则首次命中时间升序
（ascending）或者降序（descending）排列。
查看按照所有策略规则最近未命中天数升序或者降序排列后的策略规则命中统计信息：
show policy statistic-info sorted-by last-hitted-days {ascending | descending}
l
last-hitted-days {ascending | descending} - 指定按照策略规则最近未命中天数升序
（ascending）或者降序（descending）排列。
查看按照所有策略规则最近一次命中时间升序或者降序排列后的策略规则命中统计信息：
show policy statistic-info sorted-by last-hitted-time {ascending | descending}
l
last-hitted-time {ascending | descending} - 指定按照策略规则最近一次命中时间升序
（ascending）或者降序（descending）排列。
清除策略规则命中统计信息
在CLI的任何模式下，使用以下命令清除策略规则命中统计信息：
clear policy statistic-info {all | id id}
l
all | id id - 清除所有策略规则（all）或者指定ID（id id）的策略规则命中统计信息。
配置策略规则的会话超时时间
会话超时时间是指策略规则的会话的老化时间，超出超时时间后，连接将断开。配置策略规则的会话超时时
间，在策略配置模式下使用以下命令：
session-timeout {day day_value | second second_value}
l
day day_value – 指定超时时间。单位为天，取值范围1-1000。
l
second second_value – 指定超时时间。单位为秒，取值范围1-65535。
查看长连接会话状态信息
超时时间大于或等于1天的会话即为长连接会话。查看长连接会话的状态信息，在任意模式下，使用以下命
令：

<!-- 来源页 424 -->
show session long-time
配置全局记录日志功能
开始之前：
l
使用该功能前，必须保证系统的流量日志功能是开启的，即在全局配置模式下，执行logging traffic
on命令。
系统可以通过单条策略中的记录日志功能来记录流量对策略规则的匹配状况，但这会出现由于人工遗漏等问
题导致部分策略未开启或未关闭记录日志功能的情况。为了避免这种情况的发生，系统支持全局记录日志功
能，该功能可以对所有策略的记录日志功能统一进行开启或关闭。默认情况下，全局记录日志功能为关闭状
态。
配置全局记录日志功能，在策略规则配置模式下，使用以下命令：
global-policy-log {session-start | session-end | policy-deny} {on | off}
l
session-start – 适用于permit类型的策略规则。使系统生成会话建立的日志信息。
l
session-end – 适用于permit类型的策略规则。使系统生成会话结束的日志信息。
l
policy-deny – 适用于deny类型的策略规则。使系统生成规则拒绝流量的日志信息。
l
on – 指定全局记录日志功能为记录日志模式。
l
off – 指定全局记录日志功能为不记录日志模式。
使用no global-policy-log {session-start | session-end | policy-deny} 命令取消全局记录日志功能
的配置。
注意: 全局记录日志功能的优先级高于单一策略和微型策略中的记录日志功能，即开启全局记录日
志功能后，单一策略和微型策略中对应的记录日志配置将不生效。
例如：在单条策略中启用了“session-start”记录日志功能，并且在全局记录日志功能中启用了
对应功能并设置为不记录日志模式，那么此时该条策略的“session-start”记录日志配置将不会
生效，系统不会记录对应的日志信息。
配置策略组
用户可以将一些策略规则组织到一起便组成了策略组。用户可以直接将对策略组进行配置，这样便简化了管
理。
用户可以通过CLI对策略组进行以下配置：

<!-- 来源页 425 -->
l 新建/删除策略组
l 启用/禁用策略组
l 添加/删除策略组描述信息
l 添加/删除策略规则成员
l 策略组重命名
l 配置VSYS Profile策略组
l 查看策略组配置信息
新建/删除策略组
新建策略组，请在全局配置模式下，输入以下命令：
policy-group group-name
l
group-name – 指定策略组名称。范围是1到95个字符。
运行该命令后，系统进入策略组配置模式。
删除策略组，请在全局配置模式下，输入以下命令：
no policy-group group-name
启用/禁用策略组
默认情况下，策略组为启用状态。启用/禁用策略组，在策略组配置模式下，使用以下命令：
l
启用：enable
l
禁用：disable
注意:
l
启用/禁用策略组后，策略组中的策略规则成员启用状态同时被修改。
l
策略规则在被引用时，不允许启用或者禁用。
添加/删除策略组描述信息
在策略组配置模式下，用户可以通过使用以下命令为策略组添加描述信息。
description description
l
description – 指定策略组名称。范围是1到95个字符。
在策略组配置模式下，使用以下命令删除策略组的描述信息。

<!-- 来源页 426 -->
no description
添加/删除策略规则成员
在策略组配置模式下，用户可以通过使用以下命令为策略组添加策略规则成员。
rule id
l
id – 指定策略规则ID。
在策略组配置模式下，使用以下命令删除策略组的策略规则成员。
no rule id
注意: 一条策略规则只能添加到一个策略组中。
策略组重命名
在全局配置模式下，用户可以通过使用以下命令为策略组重命名。
rename policy-group old-name new-name
l
old-name – 指定策略组的旧名称。
l
new-name – 指定策略组的新名称。
配置VSYS Profile策略组
在VSYS Profile配置模式下，用户可以通过使用以下命令为VSYS Profile配置策略组。
policy-group max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中策略组的最大配额（max max-num）和预留
配额（reserve reserve-num）。最大配额和预留配额根据不同平台取值范围不同。预留配额不能超过
最大配额。
查看策略组配置信息
查看策略组配置信息，在任何模式下，使用以下命令：
show policy-group [name]
l
name – 查看指定策略组名称的配置信息。

<!-- 来源页 427 -->
配置规则冗余检测
为保证策略规则的有效性，系统可对策略规则进行冗余检测，即检查是否存在冗余策略或冲突策略。系统把
策略规则的源安全域、源地址、目的安全域、目的地址、服务、应用和VLAN ID作为冗余检测项，将高优先
级的策略依次与低优先级的策略进行比较分析，并在冗余检测列表列出分析结果，以便用户进一步处理，帮
助用户实现精简策略的目的。
注意: 冗余检测功能仅对动作配置为“允许”或“拒绝”的策略规则生效。
指定冗余检测的问题类型
进行冗余检测前，需要先指定冗余检测的问题类型，包括四种类型：完全冲突（completely-conflict）、
完全冗余（completely-redundancy）、部分冲突（partly-conflict）、部分冗余（partlyredundancy）。
四种问题类型的定义如下：
l
完全冗余：策略A的冗余检测项被策略B完全覆盖，当策略A优先级低于策略B，且动作相同时，策略A会
被检测为完全冗余。
l
部分冗余：两条策略规则的每一个冗余检测项均有部分重叠，且动作相同时，低优先级的策略规则会被
检测为部分冗余。
l
完全冲突：策略A的冗余检测项被策略B完全覆盖，当策略A优先级低于策略B，且动作冲突时，策略A会
被检测为完全冲突。
l
部分冲突：两条策略规则的每一个冗余检测项均有部分重叠，且动作冲突时，低优先级的策略规则会被
检测为部分冲突。
指定冗余检测的问题类型，在策略配置模式下，使用以下命令：
redundancy-check-type {[completely-conflict] [completely-redundancy] [partly-conflict]
[partly-redundancy]}
l
[completely-conflict] [completely-redundancy] [partly-conflict] [partly-redundancy] – 指
定冗余检测的问题类型，可以同时指定多个问题类型，不同问题类型间用空格隔开。
如不指定，冗余检测的默认问题类型为完全冲突和完全冗余。
在策略配置模式下，使用no redundancy-check-type命令恢复默认问题类型。
查看冗余检测的问题类型
查看当前冗余检测的问题类型，在任意模式下，使用以下命令：

<!-- 来源页 428 -->
show policy redundancy-check-type
开始冗余检测
开始策略规则的冗余检测，在任意模式下，使用以下命令：
exec policy redundancy-check start
停止冗余检测
停止策略规则的冗余检测，在任意模式下，使用以下命令：
exec policy redundancy-check stop
查看冗余检测结果
查看策略规则的冗余检测结果，包括策略ID、策略名称、问题类型、策略状态，在任意模式下，使用以下命
令：
show policy redundancy-check-result [[id id] [name name] [type type]]
l
id id – 查看指定策略ID的冗余检测结果。范围是1到4000。
l
name name – 查看指定策略名称的冗余检测结果。范围是1到95个字符。
l
type type – 查看指定问题类型的冗余检测结果。问题类型包括四种：完全冲突（completelyconflict）、完全冗余（completely-redundancy）、部分冲突（partly-conflict）、部分冗余
（partly-redundancy）。
查看策略规则的覆盖情况
查看冗余检测结果中策略规则的覆盖情况，包括策略ID和被覆盖的策略ID，在任意模式下，使用以下命令：
show policy redundancy-check
清除冗余检测结果
清除策略规则的冗余检测结果，在任意模式下，使用以下命令：
exec policy redundancy-check clear
配置策略的忽略时间
用户可以忽略策略，并为其指定忽略时间。在忽略时间内，系统将不再检测该策略的冗余情况。系统支持按
天数或时间戳两种方式配置忽略时间。

<!-- 来源页 429 -->
注意: 同一条策略若使用两种方式配置忽略时间，仅后配置的忽略时间生效。建议用户按“忽略天
数”的方式进行配置。
按天数配置忽略时间，在策略规则配置模式下，使用以下命令：
redundancy-ignore-days {time_value | forever}
l
time_value – 指定忽略时间，范围是1到3650天。
l
forever - 指定永久忽略。
按时间戳配置忽略时间，在策略规则配置模式下，使用以下命令：
redundancy-expire-time time_value
l
time_value – 指定忽略的到期时间戳。指定后，在到期时间前，系统将不再检测该策略规则的冗余情
况。取值范围是-1到9223372036854775807，指定为-1时，表示永久忽略该策略。时间戳是指从格
林威治时间1970年01月01日00时00分00秒（北京时间1970年01月01日08时00分00秒）起，到指定
时间点经过的总秒数。例如：指定时间戳为1782201600，表示到期时间为北京时间2026-06-23
16:00:00。
解除策略的忽略状态
在策略规则配置模式下，使用no redundancy-ignore-days命令或no redundancy-expire-time命令
解除策略的忽略状态。
查看已忽略的策略
查看已忽略的策略，包括策略ID、策略名称、到期时间，在任意模式下，使用以下命令：
show policy redundancy-ignore
配置策略助手
为了提高用户配置安全策略的完整性、准确性和快速性，系统提供策略助手功能。策略助手能够提取命中指
定策略ID的流量作为流量数据分析源，并根据用户设置的聚合规则聚合数据流量列表，最后自动生成符合用
户期望的安全策略规则。
提示: 通过WebUI可以进行策略助手完整的配置，详细配置指导请参阅《StoneOS WebUI手
册》“配置策略助手”小节。

<!-- 来源页 430 -->
开启/关闭策略助手
启用策略助手功能，在策略规则配置模式下，使用以下命令：
assistant enable
注意: 根VSYS最多支持开启4个策略规则ID的策略助手功能；非根VSYS最多支持开启1个策略规则
ID的策略助手功能。
关闭策略助手功能，在策略规则配置模式下，使用以下命令：
assistant disable
示例：
hostname(config)# policy-global
hostname(config-policy)# rule id 2
hostname(config-policy-rule)# assistant enable
查看开启策略助手的策略
查看已开启策略助手功能的策略的详细信息，在任意模式下，使用以下命令：
show policy assistant-enable
开启策略助手流量统计功能
策略助手流量统计功能能够统计通过策略助手提取到的流量的信息，包括命中数、上行报文数、下行报文
数、上行字节数及下行字节数。默认情况下，策略助手流量统计功能为关闭状态。开启策略助手流量统计功
能，在策略配置模式下，使用以下命令：
policy-assistant-traffic-statistic
在策略配置模式下，使用no policy-assistant-traffic-statistic命令关闭策略助手流量统计功能。
查看策略助手流量统计功能状态
查看策略助手流量统计功能是开启还是关闭状态，在任意模式下，使用以下命令：
show policy assistant-traffic-statistic-status
配置微型策略
微型策略配置包括：

<!-- 来源页 431 -->
l 启用/禁用微型策略
l 创建/删除微型策略
l 编辑微型策略
l 微型策略的日志管理
l 查看微型策略信息
l 查看微型策略命中信息
启用/禁用微型策略
默认情况下，配置好的微型策略会在系统中立即起效。管理员可以通过命令禁用微型策略，使其不对流量进
行控制。禁用或者启用某条微型策略，在微型策略配置模式下，使用以下命令：
l
禁用：disable
l
启用：enable
注意: 管理员也可在创建微型策略时，指定disable参数直接禁用配置的微型策略。请参阅上一节
“创建/删除微型策略”。
创建/删除微型策略
创建微型策略，在全局配置模式或者策略配置模式下，使用以下命令：
mini-rule [id id] [src-zone zone-name] [dst-zone dst-zone] src-ip {src-ipv4-address | srcipv6-address}dst-ip {dst-ipv4-address | dst-ipv6-address} protocol protocol-number [dstport port-number] action {permit | deny} [description description] [log-start] [log-end] [logdeny] [disable]
l
id id – 指定微型策略的ID。如果不指定，系统将会为微型策略自动分配一个ID。规则ID在整个系统中必
须是唯一的。微型策略的起始ID为1000001，ID范围根据不同设备平台而不同。
l
src-zone zone-name – 指定微型策略的源安全域，如果不指定则默认指定为any。该参数为可选配
置。
l
dst-zone dst-zone – 指定微型策略的目的安全域，如果不指定则默认指定为any。该参数为可选配
置。
l
src-ip {src-ipv4-address | src-ipv6-address} – 指定微型策略的源地址，可指定为IPv4地址或IPv6
地址。

<!-- 来源页 432 -->
l
dst-ip {dst-ipv4-address | dst-ipv6-address} – 指定微型策略的目的地址，可指定为IPv4地址或
IPv6地址。
l
protocol protocol-number – 指定微型策略的协议号，取值范围是1-255。
l
dst-port port-number – 指定微型策略的目的端口号，取值范围是1-65535。当协议号为6
（TCP）、17（UDP）时，则必须指定目的端口号，其他协议号时则不支持配置。
l
action {permit | deny} – 指定微型策略的处理行为。
l
permit - 允许流量通过。
l
deny - 拒绝流量通过。
l
description description – 指定微型策略的描述信息，范围是1到31个字符。
l
log-start – 开启记录会话建立日志信息。
l
log-end – 开启记录会话结束日志信息。
l
log-deny – 开启记录会话拒绝日志信息。
l
disable – 禁用微型策略。
删除微型策略，在全局配置模式或者策略配置模式下，使用以下命令：
no mini-rule id id
l
id - 删除指定ID的微型策略。
编辑微型策略
已创建好的微型策略可以进行编辑来修改不合适的参数值，编辑微型策略包括以下内容：
l 启用/禁用微型策略
l 修改微型策略的过滤条件
l 修改微型策略处理行为
l 修改微型策略描述信息
编辑微型策略必须在微型策略配置模式下进行，在全局配置模式或策略配置模式下，使用以下命令进入微型
策略配置模式：
mini-rule id id
l id - 指定已创建的微型策略ID。该ID必须指定为已存在的微型策略ID，若指定的ID不存在，将会显示错误提示信
息。微型策略的起始ID为1000001，ID范围根据不同设备平台而不同。

<!-- 来源页 433 -->
修改微型策略的过滤条件
修改微型策略的过滤条件（源/目的地址、协议、目的端口或源/目的安全域），在微型策略配置模式下，使
用以下命令：
[src-zone zone-name] [dst-zone dst-zone] src-ip {src-ipv4-address | src-ipv6-address} dstip {dst-ipv4-address | dst-ipv6-address} protocol protocol-number [dst-port port-number]
l
src-zone zone-name – 指定微型策略的源安全域，如果不指定则默认指定为any。该参数为可选配
置。
l
dst-zone dst-zone – 指定微型策略的目的安全域，如果不指定则默认指定为any。该参数为可选配
置。
l
src-ip {src-ipv4-address | src-ipv6-address} – 指定微型策略的源地址，可指定为IPv4地址或IPv6
地址。
l
dst-ip {dst-ipv4-address | dst-ipv6-address} – 指定微型策略的目的地址，可指定为IPv4地址或
IPv6地址。
l
protocol protocol-number – 指定微型策略的协议号，取值范围是1-255。
l
dst-port port-number – 指定微型策略的目的端口号，取值范围是1-65535。当协议号为6
（TCP）、17（UDP）时，则必须指定目的端口号，其他协议号时则不支持配置。
修改微型策略处理行为
修改微型策略处理行为（允许或拒绝），在微型策略配置模式下，使用以下命令：
action {permit | deny}
l
permit - 允许流量通过。
l
deny - 拒绝流量通过。
修改微型策略描述信息
修改微型策略描述信息，在微型策略配置模式下，使用以下命令：
description description
l
description - 指定微型策略的描述信息，范围是1到31个字符。
使用no description description命令取消微型策略描述信息的配置。

<!-- 来源页 434 -->
微型策略的日志管理
l
对于permit类型的微型策略，可以记录两种情况，分别是符合微型策略的流量建立会话时生成日志信息
和结束会话时生成日志信息。
l
对于deny类型的微型策略，可以记录的情况为：符合微型策略的流量被deny时生成日志信息。
使用该功能前，必须保证系统的流量日志功能是开启的，即在全局配置模式下，执行logging traffic on命
令。配置微型策略的日志管理，在微型策略配置模式下，使用以下命令：
log {deny | start | end}
l
deny – 适用于deny类型的微型策略。使系统生成微型策略拒绝流量的日志信息。
l
start – 适用于permit类型的微型策略。使系统生成会话建立的日志信息。
l
end – 适用于permit类型的微型策略。使系统生成会话结束的日志信息。
使用no log {deny | start | end}命令取消微型策略日志管理功能的配置。
查看微型策略信息
查看指定ID的微型策略信息，在任何模式下，使用以下命令：
show mini-policy id id
l
id - 查看指定ID的微型策略信息。
查看所有微型策略信息，在任何模式下，使用以下命令：
show mini-policy
查看符合指定条件的微型策略信息，在任何模式下，使用以下命令：
show mini-policy [src-zone zone-name] [dst-zone dst-zone] [src-ip {src-ipv4-address | srcipv6-address}] [dst-ip {dst-ipv4-address | dst-ipv6-address}] [protocol protocol-number]
[dst-port port-number] [description description] [family{ ipv4 | ipv6 }]
l
src-zone zone-name – 查看符合指定源安全域的微型策略信息。
l
dst-zone dst-zone – 查看符合指定目的安全域的微型策略信息。
l
src-ip {src-ipv4-address | src-ipv6-address} – 查看符合指定源地址的微型策略信息，可指定为
IPv4地址或IPv6地址。
l
如该源地址指定为精确IP地址，系统将会对该IP地址进行精确匹配，查询到该源地址对应的微型策
略信息。

<!-- 来源页 435 -->
l
如该源地址指定为不完整的IP地址，系统将会对该IP地址进行模糊匹配，查询到相匹配的源地址对
应的微型策略信息。例如，当该源地址指定为“192.168”时，系统将会查询到所有包含
“192.168”字符串的源地址（192.168.1.2、192.168.1.50等）对应的微型策略信息。
l
dst-ip {dst-ipv4-address | dst-ipv6-address} – 查看符合指定目的地址的微型策略信息，可指定为
IPv4地址或IPv6地址。
l
如该目的地址指定为精确IP地址，系统将会对该IP地址进行精确匹配，查询到该目的地址对应的微
型策略信息。
l
如该目的地址指定为不完整的IP地址，系统将会对该IP地址进行模糊匹配，查询到相匹配的目的地
址对应的微型策略信息。例如，当该目的地址指定为“192.168”时，系统将会查询到所有包含
“192.168”字符串的目的地址（192.168.1.2、192.168.1.50等）对应的微型策略信息。
l
protocol protocol-number – 查看符合指定协议号的微型策略信息，取值范围是1-255。
l
dst-port port-number – 查看符合指定目的端口号的微型策略信息。
l
description description – 查看符合指定描述信息的微型策略信息，范围是1到31个字符。
l
family{ ipv4| ipv6 } - 查看IPv4类型或IPv6类型的微型策略信息。
查看微型策略命中信息
为方便用户对微型策略的管理和维护，设备支持微型策略命中次数统计功能。该功能能够对系统流量与微型
策略的命中次数进行统计，即每当进入系统的流量与某条微型策略相匹配时，该微型策略的命中时间会进行
刷新，命中次数会自动加1。管理员可以在任何模式下通过以下命令查看微型策略命中信息：
show mini-policy hit-info [top {10 | 20 | 50 | all }]
l
top {10 | 20 | 50 | all} – 显示命中次数位于前10、20、50位的微型策略的命中信息，或者按命中数降
序方式显示所有微型策略的命中信息。
配置策略自定义属性
为方便策略查询和管理，用户可以为策略规则配置自定义属性，并基于自定义属性对策略规则进行过滤查
看。
自定义属性可以极大的方便管理员去过滤、分类、查询策略。例如，某企业网管部署了上千条策略，对于某
些策略的使用情况不是很了解。通过自定义属性，可以简单明了的查看当前策略的使用人、到期时间等等。
配置策略自定义属性为“使用人”，将策略规则的“使用人”配置为“张三”。配置完成后，将“张三”作
为过滤条件进行策略筛选，可以快速查找到使用人为“张三”的策略规则。
请按照以下步骤进行策略自定义属性配置：

<!-- 来源页 436 -->
l 配置自定义属性映射
l 为策略规则配置自定义属性内容
l 查看自定义属性信息
配置自定义属性映射
配置策略自定义属性映射，指定不同ID的自定义属性和属性名称之间的对应关系。系统最多允许配置8个策
略自定义属性，每个属性都对应一个ID，用户可以根据需要配置属性名称。
配置策略自定义属性映射，在全局配置模式下，使用以下命令：
user-defined-attribute policy attribute-index id attribute-name name
l
attribute-index id - 指定策略自定义属性的ID。取值范围为1到8。
l
attribute-name name - 指定策略自定义属性的名称。取值范围为1到31个字符。
在全局配置模式下，使用no user-defined-attribute policy attribute-index id命令删除已配置的策略
自定义属性映射。
为策略规则配置自定义属性内容
为策略配置自定义属性，在策略规则配置模式下，使用以下命令：
user-defined-attribute {attribute-index id | attribute-name name} content content
l
attribute-index id - 指定已配置的策略自定义属性ID。
l
attribute-name name - 指定已配置的策略自定义属性名称。
l
content content - 指定自定义属性的内容。取值范围为1到31个字符。
在策略规则配置模式下，使用no user-defined-attribute {attribute-index id | attribute-name
name}命令删除已配置的自定义属性内容。
查看自定义属性信息
在任何模式下，使用以下命令查看策略自定义属性映射信息，包括属性ID、属性名称以及该属性被策略规则
使用的次数。
show user-defined-attribute policy
在任何模式下，使用以下命令查看包含指定自定义属性内容的策略规则信息。
show policy user-defined-attribute {attribute-index id | attribute-name name} content
content [accurate]

<!-- 来源页 437 -->
l
attribute-index id - 指定已配置的策略自定义属性ID。
l
attribute-name name - 指定已配置的策略自定义属性名称。
l
content content - 指定需要查看的自定义属性所包含的内容。取值范围为1到31个字符。
l
accurate - 指定按照精确匹配的方式查找符合自定义属性内容的策略规则。如不指定，默认按照模糊匹
配的方式进行查找。
在策略中使用外部动态列表
为简化配置过程并提高管理效率，用户可以在策略规则中引用外部动态列表。可以将IP类型的外部动态列表
作为策略规则的源地址或者目的地址；或者将域名类型的外部动态列表作为策略规则的域名。有关外部动态
列表的详细信息，请参阅"外部动态列表介绍" 在第144页。
以下是如何在策略规则中引用IP类型的外部动态列表作为目的地址，以阻止访问恶意IP地址的示例。
企业要将上级监管单位发布的恶意IP地址列表快速同步到内部的多台防火墙中，以阻止公司对这些恶意IP地
址的访问，从而提升网络安全防护能力。则可以创建一个包含这些恶意IP地址的外部动态列表，然后在防火
墙策略规则的目的地址中引用该外部动态列表，并将规则动作设置为拒绝（Deny）。这样，所有匹配这些IP
地址的流量都会被自动阻断，从而迅速实施对这些恶意IP的访问限制。管理员只需更新服务器上的IP列表文
件，所有与该文件相关联的防火墙会自动同步这些更改，并应用在安全策略中，大大减少了手动更新每台防
火墙配置的工作量。
在策略中引用外部动态列表，可以进行以下配置：
l 为策略规则添加外部动态列表类型的源地址
l 为策略规则添加外部动态列表类型的目的地址
l 为策略规则添加外部动态列表类型的域名
l 查看引用外部动态列表的策略规则信息
前置条件
在策略中使用外部动态列表前，请先完成"配置外部动态列表" 在第147页。
为策略规则添加外部动态列表类型的源地址
为策略规则添加外部动态列表类型的源地址，在策略规则配置模式下，使用以下命令：
src-ip-external-dynamic-list name name
l
name - 指定外部动态列表的名称。仅支持指定IP类型的外部动态列表。

<!-- 来源页 438 -->
在策略规则配置模式下，使用no src-ip-external-dynamic-list name name命令删除已配置的外部动
态列表类型的源地址。
为策略规则添加外部动态列表类型的目的地址
为策略规则添加外部动态列表类型的目的地址，在策略规则配置模式下，使用以下命令：
dst-ip-external-dynamic-list name name
l
name - 指定外部动态列表的名称。仅支持指定IP类型的外部动态列表。
在策略规则配置模式下，使用no dst-ip-external-dynamic-list name name命令删除已配置的外部动
态列表类型的目的地址。
为策略规则添加外部动态列表类型的域名
为策略规则添加外部动态列表类型的域名，在策略规则配置模式下，使用以下命令：
dst-host-external-dynamic-list name name
l
name - 指定外部动态列表的名称。仅支持指定域名类型的外部动态列表。
在策略规则配置模式下，使用no dst-host-external-dynamic-list name name命令删除已配置的外部
动态列表类型的域名。
查看引用外部动态列表的策略规则信息
用户可以在任何模式下，通过show命令查看引用外部动态列表的策略规则详细信息。具体命令如下：
show policy [src-addr src-addr] [dst-addr dst-addr]
l
src-addr src-addr – 查看指定外部动态列表类型源地址的规则的详细信息。
l
dst-addr dst-addr – 查看指定外部动态列表类型目的地址的规则的详细信息。
在策略中启用前向纠错（FEC）功能
开始之前
l 阅读"前向纠错（FEC）介绍" 在第165页。
l 阅读"前向纠错（FEC）技术应用场景" 在第165页介绍。
l 阅读"前向纠错（FEC）技术实现原理" 在第166页介绍。
l 阅读"前向纠错（FEC）使用限制和注意事项" 在第167页。
l 阅读"IPSec VPN隧道前向纠错（FEC）配置流程" 在第167页。
在策略中开启前向纠错（FEC）功能，需先进入策略规则配置模式。

<!-- 来源页 439 -->
开启/关闭前向纠错（FEC）功能
用户需根据业务规划需求，在指定策略中开启前向纠错（FEC）功能。启用该功能后，系统会根据该策略规
则的相关配置过滤出需要进行FEC处理的原始数据包。策略中的前向纠错（FEC）功能默认为关闭状态。
注意: 用户需在IPSec VPN隧道两端设备的策略中均启用前向纠错（FEC）功能，以确保此功能正
常运行。
开启/关闭前向纠错（FEC）功能，在策略规则配置模式下，使用以下命令：
l
开启：fec-enable
l
关闭：no fec-enable
示例：
hostname(config)# rule id 3
hostname(config-policy-rule)# fec-enable
hostname(config-policy-rule)# exit
下一步
在策略中启用前向纠错（FEC）功能后，请根据业务规划需求，逐项核查配置步骤的完成情况。待所有配置
完成后，可使用show ipsec sa id或show fec statistic sa id命令，进一步验证前向纠错（FEC）功能是
否生效。
注意: 为确保验证结果的准确性，建议在实施验证前确认已有业务流量符合策略规则的匹配条件。
l show ipsec sa id（查看IPSec VPN监控信息）：使用该命令验证时，当show信息中的Fec instance显示为
“enable”时，则说明前向纠错（FEC）功能已实际生效；若Fec instance显示为“disable”，则说明前向纠
错（FEC）功能暂未生效。

<!-- 来源页 440 -->
l show fec statistic sa id（查看前向纠错（FEC）统计数据）：使用该命令验证时，当show信息中FEC编解码的
统计数据增加，则说明前向纠错（FEC）功能已实际生效；若FEC编解码的统计数据为0，则说明前向纠错
（FEC）功能暂未生效。
聚合策略
用户可以根据场景需要，创建聚合策略并且将一些具有相同作用或者相同属性的策略规则加入聚合策略，管
理员调整聚合策略的优先级后，所有聚合策略成员的优先级将会一起调整，实现对策略规则的批量管理。
聚合策略的配置包括：
l 创建聚合策略
l 添加聚合策略成员
l 移出聚合策略成员
l 删除聚合策略
l 调整优先级
l 启用/禁用聚合策略
l 添加/删除聚合策略描述信息
创建聚合策略
创建聚合策略，需进行如下两步操作：

<!-- 来源页 441 -->
1.
创建一条包含名称的策略规则。
2.
进入该策略规则配置模式后，将新创建的策略规则指定为聚合策略。
注意: 如需要将之前已存在的策略规则指定为聚合策略，策略规则的配置需满足以下要求，否则无
法指定为聚合策略：
l
必须包含名称的配置。
l
可包含启用状态或描述配置，并且除名称、启用状态或描述配置外，不包含其他配置。
创建策略规则并进入该策略规则的配置模式，在全局配置模式下，使用以下命令：
rule [id id ] { name name}
l
id id - 指定策略的ID。如果不指定，系统将会为策略规则自动分配一个ID。规则ID在整个系统中必须是
唯一的。
l
name name - 指定聚合策略的名称。范围是1到95个字符，该名称为必配项。
指定为聚合策略，在策略规则配置模式下，使用以下命令：
aggregate-type
添加聚合策略成员
当聚合策略创建完成后，管理员可以将策略规则添加到聚合策略中成为聚合策略成员。首先，使用rule idid
进入要被添加的策略规则的配置模式，然后，使用以下命令：
aggregate-rule {name name | id}
l
name name | id - 指定需要加入到的聚合策略名称或规则ID。
注意:
l
一条策略规则只能添加到一个聚合策略中。
l
如果一条策略规则已经被添加到聚合策略中，执行该命令后，将会加入到新指定的聚合策略
中。
l
聚合策略不能作为聚合策略成员加入到另一个聚合策略中。
l
策略组中的策略成员不能被添加到聚合策略中。

<!-- 来源页 442 -->
移出聚合策略成员
从聚合策略中移出某个聚合策略成员，使用rule idid进入要被移出的聚合策略成员的配置模式，然后使用以
下命令：
no aggregate-rule
注意:
l
当top位置的聚合策略成员被移出聚合策略后，将会被排列到该聚合策略之前。
l
当非top位置的聚合策略成员被移出聚合策略后，将会被排列到该聚合策略之后。
删除聚合策略
删除聚合策略并移出其中的聚合策略成员，在全局配置模式或者策略配置模式下，使用以下命令：
no rule {id id | name name}
l
id id – 删除指定ID的聚合策略。
l
name name – 删除指定名称的聚合策略。
删除聚合策略及其聚合策略成员，即删除聚合策略的同时，将其中的聚合策略成员一并删除，在全局配置模
式或者策略配置模式下，使用以下命令：
no rule {id id | name name} include-member
调整优先级
调整聚合策略或其中聚合策略成员的优先级，修改其排列顺序，在策略配置模式下使用以下命令：
move {name name | id} {top | bottom | before {name rule-name | id} | after {name rule-name
| id} }
l
name name | id – 指定需要调整优先级的聚合策略或其中成员ID或者名称。
l
top – 如果移动的是聚合策略，指定该聚合策略移动到所有策略规则的首位；如果移动的是聚合策略成
员，指定该聚合策略成员移动到其所属聚合策略中所有成员的首位。
l
bottom - 如果移动的是聚合策略，指定该聚合策略移动到所有策略规则的末尾；如果移动的是聚合策略
成员，指定该聚合策略成员移动到其所属聚合策略中所有成员的末尾。
l
before {name rule-name | id} – 指定聚合策略移动到某个规则ID或者名称之前。如果移动的是聚合
策略成员，rule-name或id仅可指定为所属聚合策略中的其他成员的ID或名称。

<!-- 来源页 443 -->
l
after {name rule-name | id} – 指定聚合策略移动到某个规则ID或者名称之后。如果移动的是聚合策
略成员，rule-name或id仅可指定为所属聚合策略中的其他成员的ID或名称。
注意:
l
用户调整聚合策略的优先级后，所有聚合策略成员的优先级将会一起调整。
l
不支持通过调整策略规则的优先级实现添加到聚合策略或者从聚合策略中移出。
启用/禁用聚合策略
默认情况下，配置好的聚合策略会在系统中立即起效。管理员可以通过命令禁用某条聚合策略，使其不对流
量进行控制。禁用或者启用某条聚合策略，在聚合策略的配置模式下，使用以下命令：
l
禁用：disable
l
启用：enable
注意:
l
禁用聚合策略后，聚合策略中的聚合策略成员同时被禁用。
l
启用聚合策略后，聚合策略中的聚合策略成员状态将会保持原有启用/禁用状态。例如，某个聚
合策略成员原有状态为禁用，那么当启用其所属的聚合策略后，该聚合策略成员状态依旧保持
禁用状态。
添加/删除聚合策略描述信息
在聚合策略的配置模式下，管理员可以通过使用以下命令为聚合策略添加描述信息。
description description
l
description – 指定聚合策略描述信息。范围是1到95个字符。
在聚合策略的配置模式下，使用以下命令删除聚合策略的描述信息。
no description
策略审计
系统支持策略审计功能，当用户新建、修改策略规则配置时，可以使用该功能，为策略规则添加策略审计注
释内容，来说明策略规则的创建/修改原因，以便用户了解策略规则配置的变更理由、变更历史记录。

<!-- 来源页 444 -->
型号说明：
l
支持：安装有硬盘的SG-6000 A系列设备（不含SG-6000-A1600/A1800/A2200）。
l
支持：安装有硬盘的SG-6000 B系列设备（不含SG-6000-
B600/B600W/B600G4/B600WG4）。
l
支持：安装有硬盘的SG-6000 K系列设备。
l
支持：安装有硬盘的SG-6000 X系列设备（不含SG-6000-X9180）。
l
支持：安装有硬盘的SG-6000 云·界设备。
启用/禁用策略审计
默认情况下，策略审计功能为关闭状态。启用策略审计功能，在全局配置模式下，使用以下命令：
audit-comment-enable
在全局配置模式下，使用该命令no的形式禁用策略审计功能：
no audit-comment-enable
添加审计注释
为策略规则添加策略审计注释内容，在任意模式下，使用以下命令：
audit-comment rule id id comment comment
l
rule id id - 指定需要添加审计注释的策略规则ID。
l
comment comment - 指定审计注释内容。范围是1-255个字符。
查看策略审计启用状态
显示策略审计功能启用状态，在任何模式下使用以下命令：
show audit-comment-status
注意:
l
策略审计注释为可选配置，在用户新建、修改策略规则配置时，可以根据需求为策略规则添加
策略审计注释内容。

<!-- 来源页 445 -->
l
关于查看策略规则的审计历史信息，仅支持通过WebUI方式查看，具体方法请参阅《StoneOS
WebUI用户手册》。
策略访问控制
策略访问控制功能，即通过将策略规则与ACL Profile相结合，在策略规则控制的基础上，进一步对报文进
行细粒度的访问控制，如源/目的MAC地址、DSCP等。只有将ACL Profile绑定到策略规则上，该功能才能
在设备上起作用。
配置策略访问控制
创建ACL Profile
ACL Profile的配置需要在ACL Profile配置模式下进行。进入ACL Profile配置模式，在全局配置模式下，
使用以下命令：
acl-profile acl-profile-name
l
acl-profile-name – 指定ACL Profile的名称。执行该命令后，系统创建指定名称的ACL Profile，并
且进入该ACL Profile配置模式；如果指定的名称已存在，则直接进入ACL Profile配置模式。最多只能
创建64个ACL Profile。
在全局配置模式下，使用no acl-profile acl-profile-name命令删除指定的ACL Profile。
配置策略访问控制规则
配置IPv4策略访问控制规则以及控制动作，在ACL Profile配置模式下，使用以下命令：
sequence id {drop | pass} [both | forward | backward] [src-mac src-mac-address] [dst-mac
dst-mac-address] [dscp dscp-value]
l
id – 指定策略访问控制规则的ID。范围是1-32。
l
drop | pass – 指定采取的控制动作，丢弃或允许通过。
l
both | forward | backward – 指定策略规则访问控制的流量方向，forward指上行方向，
backward指下行方向，both指双方向。默认为双方向。
l
src-mac src-mac-address – 指定访问控制规则的源MAC地址。
l
dst-mac dst-mac-address – 指定访问控制规则的目的MAC地址。
l
dscp dscp-value – 指定DSCP的值。范围是0-63。
在ACL Profile配置模式下，使用no sequence id命令删除指定的策略访问控制规则。

<!-- 来源页 446 -->
注意: 若要配置IPv6策略访问控制规则以及控制动作，请参阅IPv6策略访问控制部分。
配置默认控制动作
当未命中任何访问控制规则时，系统将采取指定的默认访问控制动作。配置默认控制动作，在ACL Profile
配置模式下，使用以下命令：
default-action {drop | pass}
l
drop | pass– 指定采取的默认控制动作，丢弃或允许通过。若不配置，系统采取的默认控制动作为允许
通过。
在ACL Profile配置模式下，使用no default-action命令恢复默认访问控制动作为允许通过。
查看ACL Profile信息
用户可以在任何模式下随时使用show命令查看ACL Profile的配置信息。
show acl-profile [acl-profile-name]
l
acl-profile-name – 显示指定名称的ACL Profile的信息。如果不指定该参数，则显示系统中所有ACL
Profile的信息。
配置MAC地址获取顺序
在跨三层网络部署环境中，报文经过三层交换机时，其MAC地址会被替换为三层交换机的MAC地址。此时如
果系统直接从报文中读取MAC地址进行访问控制匹配，可能会导致匹配结果不准确，从而影响访问控制策略
的有效性。为了解决这一问题，系统提供了如下两种MAC地址获取方式，以满足不同网络环境下的精准访问
控制需求。
l
报文获取：直接从报文中读取MAC地址。该方式简单快速，适用于二层网络部署环境，但在跨三层网络
部署环境中，由于报文中的MAC地址会被替换，可能导致匹配结果不准确。
l
SNMP Server获取：通过SNMP Server获取设备的真实MAC地址。该方式能够有效解决跨三层网络部
署环境中的MAC地址获取问题，确保访问控制的精准性。
为保障访问控制策略的准确性，系统支持用户根据实际网络部署环境灵活调整MAC地址的获取顺序。在二层
网络部署环境中，可以直接使用报文获取方式；而在跨三层网络部署环境中，建议优先使用SNMP Server获
取方式，以避免因MAC地址替换而导致的匹配错误。通过合理配置MAC地址获取顺序，用户可以在不同部署
场景下实现精准的访问控制，确保访问控制策略的有效执行。
配置MAC地址获取顺序，在全局配置模式下，使用以下命令：
acl-match mac-fetch-order { 1 | 2 }

<!-- 来源页 447 -->
l
{ 1 | 2 } - 指定MAC地址获取顺序的排列方式。1：表示优先通过报文获取MAC地址，如果报文中获取不
到，则继续使用SNMP Server获取；2：表示优先通过SNMP Server获取MAC地址，如果报文中获取不
到，则继续使用报文获取。
查看设备当前的MAC地址获取顺序
查看设备当前的MAC地址获取顺序，在任意模式下，使用以下命令：
show acl-match mac-fetch-order
以下是返回结果示例：
hostname #show acl-match mac-fetch-order
acl mac fetch order as below: 0--first, 1--second
acl mac fetch from packet:0
acl mac fetch from snmp server:1
（以上返回结果表示：当前系统优先通过报文获取MAC地址，如果报文中获取不到，则继续使用SNMP
Server获取）
方案介绍：防火墙支持跨三层设备做MAC访问控制
在跨三层网络部署环境中，报文经过三层交换机时，其MAC地址会被替换为三层交换机的MAC地址。此时如
果系统直接从报文中读取MAC地址进行访问控制匹配，可能会导致匹配结果不准确，从而影响访问控制策略
的有效性。
为此防火墙新增支持跨三层设备做MAC访问控制。系统可以通过SNMP Server获取设备的真实MAC地址。
该方式能够有效解决跨三层网络部署环境中的MAC地址获取问题，确保访问控制的精准性。
方案介绍
某企业将防火墙部署于互联网出口，并在核心交换机上开启了DHCP功能来为资产分配IP。该企业现在想对
资产进行访问控制，但遇到了以下问题：
l 基于IP的策略控制会因DHCP重新分配IP而失效。
l 基于MAC的策略控制会因跨三层设备难以获取真实MAC地址而失效。
在此情况下，用户便可以通过SNMP Server联动三层交换机来获取资产的真实MAC地址，从而对资产进行
访问控制。
用户价值：该方案无需增加其它产品，降低建设成本。适用于同样存在DHCP分配IP，同时又希望做精细化
访问控制的中小企业场景。

<!-- 来源页 448 -->
工作流程
第一步：SNMP联动
首先用户需要在防火墙上配置SNMP服务器，联动三层交换机。系统将通过SNMP协议来获取相关的ARP信
息。
hostname(config)# snmp-server manager
hostname(config)# arp-mib-query server 192.168.8.2 community hillstone
第二步：定期同步ARP表
三层交换机会定期向防火墙同步ARP表项。
ARP Table
192.168.1.1
1111.1111.1111
192.168.2.1
2222.2222.2222
......
......
第三步：将ARP表存入arp-mib
防火墙会将三层交换机同步过来的ARP表项存入arp-mib。用户可以通过命令行查看ARP表项信息。

<!-- 来源页 449 -->
以下是返回结果示例：
hostname# show arp-mib-query table
Total arp mib count:4
================ALL ARP MIB================
ip:192.168.1.1 mac:1111.1111.1111
ip:192.168.2.1 mac:2222.2222.2222
第四步：配置MAC地址获取顺序
默认情况下，系统优先通过报文获取MAC地址。用户需要调整MAC地址获取顺序，使系统优先通过SNMP
Server获取MAC地址。
hostname(config)# acl-match mac-fetch-order 2
第五步：制定访问控制策略
用户根据资产的MAC地址，制定访问控制策略，阻止PC1的流量通过。
hostname(config)# acl-profile test
hostname(config-acl-profile)# default-action pass
hostname(config-acl-profile)# sequence 1 drop both src-mac 1111.1111.1111
第六步：放行或阻断流量
防火墙将根据制定的访问控制策略，放行或阻断流量。
Web重定向
Web重定向（即“网页重定向”）是指当客户端发送HTTP或HTTPS网页访问请求后，系统自动将该请求重
新定向到指定的通知页面。StoneOS提供基于策略的网页重定向功能。配置该功能后，当用户使用HTTP或
HTTPS访问网络时，页面会直接跳转到指定的通知页面。若用户需要继续访问目标URL地址，请重新在Web
浏览器中输入该地址。此外，管理员可启用强制重定向功能，直接阻断HTTP或HTTPS连接请求，禁止用户
访问目标网络。
使用Web重定向功能，请按照以下流程进行操作：
1. 配置Web重定向功能参数。
2. 创建策略规则，定义做Web重定向的流量以及该流量可访问的网络资源。
3. 开启Web重定向功能并配置重定向的URL地址。
配置Web重定向功能参数
Web重定向功能参数配置包括以下内容：

<!-- 来源页 450 -->
l 配置重定向时间间隔
l 开启/关闭强制重定向功能
在配置Web重定向功能参数之前需先进入重定向配置模式。
进入重定向配置模式
进入重定向配置模式，在全局配置模式下，使用以下命令：
web-redirect
配置重定向时间间隔
重定向时间间隔指用户触发Web重定向后，等待重定向的间隔时间。当超过该时间阈值时：
l
若该主机用户未发起其他Web访问请求，系统将直接清除该重定向主机信息，且该主机用户再次访问时
系统将重新进行Web重定向。
l
若该主机用户存在其他Web访问请求，系统会先清除该主机用户之前的会话信息，待会话信息成功清除
后，再清除该主机信息。此后该主机用户再次访问时需要重新完成重定向流程。
配置重定向时间间隔，在重定向配置模式下，使用以下命令：
interval time-value
l
time-value – 指定重定向时间间隔，单位为分钟。取值范围是0到1440分钟。默认值为30分钟。
在重定向配置模式下，使用该命令no的形式，恢复默认值：
no interval
开启/关闭强制重定向
开启强制重定向功能后，当用户首次通过HTTP/HTTPS访问网络时，系统会自动将其重定向至指定页面；当
用户再次访问时，系统将直接阻断该HTTP/HTTPS连接请求，禁止访问目标网络。该功能默认为关闭状态。
开启强制重定向功能，在重定向配置模式下，使用以下命令：
force-redirect enable
关闭强制重定向功能，在重定向配置模式下，使用以下命令：
no force-redirect enable
配置重定向URL
开始之前

<!-- 来源页 451 -->
用户需要根据策略配置，选择需要启用Web重定向功能的策略并进入对应的策略规则配置模式。关于如何进
入策略规则配置模式，请参阅“创建策略规则”章节。所选策略规则需满足以下配置：
l
服务：HTTP/HTTPS
l
动作：Permit
注意: Web重定向功能只在允许HTTP、HTTPS流量时生效。
开启Web重定向功能并配置重定向的URL地址，在策略规则配置模式下输入以下命令：
web-redirect [url]
l
url – 指定重定向的URL地址，取值范围为1到127个字符。URL地址格式为“http://www.abc.com”
或“https://www.abc.com”。若不指定该项参数，网页将会定向到用户起始输入的URL地址的页
面。
在策略规则配置模式下，使用该命令no的形式取消指定重定向URL：
no web-redirect
清除Web重定向主机信息
用户可以在任何模式下，使用以下命令，清除重定向用户信息：
exec webredirect-user kickout {all | ip ip-address}
l
all – 清除所有重定向主机的相关信息。清理期间系统将暂停新主机的接入。此操作将占用部分性能资
源，建议谨慎执行。
l
ip ip-address – 清除指定IP的重定向主机信息。
查看Web重定向功能配置信息
用户可以在任何模式下，使用以下命令查看Web重定向功能的配置信息：
show web-redirect
示例：
hostname# show web-redirect
==============================================================
interval: 3 minutes （显示重定向时间间隔）
force-redirect: disable（显示强制重定向功能的启用状态）

<!-- 来源页 452 -->
==============================================================
查看Web重定向主机列表信息
用户在首次使用HTTP或HTTPS访问网络并触发Web重定向功能时，该用户的主机IP将被加入Web重定向主
机列表中。用户可以在任何模式下，使用以下命令查看Web重定向主机的详细信息：
show web-redirect-user
示例：
hostname# show web-redirect-user
Total count: 1
==============================================================================
==
IP（IP地址）    Interface（源接口名称）     Expire(s)（过期时间）
--------------------------------------------------------------------------------
1.1.1.1                       ethernet0/4                            100
==============================================================================
==
注意:
l
当列表内主机的过期时间不为0时，如果该主机再次通过HTTP或HTTPS访问网站，将直接进入
访问网站，不会再跳转到重定向页面。如果开启了强制重定向功能，则系统会直接阻断HTTP或
HTTPS访问，不会再跳转到重定向页面。
l
当列表内主机的过期时间为0时，主机将从Web重定向IP列表中移除，该主机再次通过HTTP或
HTTPS访问网站时，会重新跳转到重定向页面。

<!-- 来源页 453 -->
共享接入
共享接入，即多个用户终端通过同一个IP地址接入到网络。系统的共享接入功能可以防范未知设备的接入，
消除潜在的安全风险，并能够帮助用户合理分配带宽，限制多用户共享带宽，保证用户的上网体验。
共享接入规则
用户可以根据需要更改共享接入规则。共享接入更新配置包括：
l 创建共享接入规则
l 配置共享接入规则
l 查看共享接入规则
创建共享接入规则
创建共享接入规则名称并进入到共享接入规则的配置模式，在全局模式下，使用以下命令：
share-access-detect rule rule-name [ipv6]
l
rule-name –指定共享接入规则的名称，并且进入共享接入规则配置模式。如果指定名称已存在，则直
接进入共享接入规则配置模式。进入IPv6类型的共享接入规则配置模式时，需指定ipv6参数。
l
ipv6 - 指定创建的共享接入规则为IPv6类型。若不指定该参数，则默认为IPv4类型的共享接入规则。
在全局配置模式下，使用该命令no的形式删除共享接入规则：
no share-access-detect rule rule-name
配置共享接入规则
进入到共享接入的配置模式后，用户可以配置共享接入规则。在共享接入配置模式下，使用以下命令：
l
指定需要监控的源安全域：src-zone zone-name
l
删除源安全域：no src-zone
l
指定需要监控的源IP地址（IPv4/IPv6）：src-ip{ipv4-address |ipv4 / netmask}/ src-ip {ipv6
prefix/ prefix length}
l
删除源IP地址（IPv4/IPv6）：no src-ip{ipv4-address |ipv4/netmask}/ no src-ip {ipv6 prefix/
prefix length}
l
指定需要监控的源IP地址范围（IPv4/IPv6）：src-range begin-ipv4 end-ipv4/ src-range
begin-ipv6 end-ipv6

<!-- 来源页 454 -->
l
删除源IP地址范围（IPv4/IPv6）：no src-range begin-ipv4 end-ipv6/ no src-range beginipv6 end-ipv6
l
指定需要监控的源IP地址簿（IPv4/IPv6）：src-addr ipv4-addr/ src-addr ipv6-addr
l
删除源IP地址簿（IPv4/IPv6）：no src-addr ipv4-addr/ no src-addr ipv6-addr
l
启用/禁用共享接入规则：enable | disable（默认为启用）
l
指定监控时间表：schedule schedule-name（共享接入规则在时间表所指定的时间周期内生效。如
果不配置，那么共享接入规则会一直生效）
l
删除时间表：no schedule
l
指定系统允许共享接入的最大终端数：access-limit limit-num（取值范围是1-15，默认值为2）
l
恢复系统默认允许共享接入的终端数：no access-limit
l
指定超限动作：当共享接入同一个IP地址的终端数超出系统允许共享接入的最大终端数后，将按指定的
动作处理该超限终端的IP地址。超限动作包括：阻断并记录日志、只记录日志、警告并记录日志，默认
动作为只记录日志。
action {block | log-only | warning}
l
block – 指定超限动作为阻断，当共享接入终端数超出最大终端数后，系统在指定的持续时间内将
对超限终端的IP地址进行阻断并记录日志信息。
l
log-only – 指定超限动作为只记录日志，当共享接入终端数超出最大终端数后，系统将对超限终
端的IP仅进行记录日志信息，而不影响接入终端的正常上网。
l
warning – 指定该超限动作为警告，当共享接入终端数超出最大终端数后，系统将在指定的持续
时间内，对超限终端发送警告信息页面并记录日志信息。
l
恢复系统默认的超限动作（只记录日志）：no action
l
指定阻断或警告的持续时间：control-duration duration（取值范围是60-3600秒，默认值为60秒，
持续时间结束后，系统将会重新检测接入终端数是否超限）
l
恢复系统默认的持续时间：no control-duration
l
指定终端的超时时间：detected-endpoint-timeout time（超过超时时间后，当终端未再使用该IP访
问网络时，系统将清除终端信息。取值范围是300-86400s，默认值为600s）
l
恢复系统默认的终端超时时间：no detected-endpoint-timeout

<!-- 来源页 455 -->
l
指定共享接入规则的序列号：sequence {first | last | seq-id}
l
first – 指定共享接入规则的序列号为第一。
l
last – 指定共享接入规则的序列号为最后。
l
seq-id – 指定共享接入规则的序列号。取值范围是1-8，数值越小，优先级越高。
l
指定警告信息页面的自定义告警内容：warning-info string
l
删除警告信息页面的自定义告警内容：no warning-info
查看共享接入规则
用户可以在任何模式下使用以下命令查看共享接入规则信息：
show share-access-detect rule [rule-name]
l
rule-name – 指定共享接入规则的名称。如果不配置规则名称，系统默认显示所有规则的配置信息。
共享接入特征库配置
用户可以根据需要更改共享接入规则特征库更新配置。共享接入特征库更新配置包括：
l 配置共享接入特征库
l 立即更新
l 导入共享接入特征库文件
l 查看共享接入特征库升级信息
l 查看共享接入特征库信息
提示: 非根VSYS也支持配置共享接入功能，但不支持共享接入特征库的更新配置。
配置共享接入特征库
升级共享接入特征库，在全局配置模式下，使用以下命令：
share-access-detect signature update [mode {auto | manual} | proxy-server {main | backup}
proxy-ip proxy-port | schedule {daily | weekly {sun | mon | tue | wed | thu | fri | sat} | monthly
date} [HH:MM] } | server1 {domain | ip} [vrouter vrouter-name] [src-interfacesrc-interfacename] | server2 {domain | ip} [vrouter vrouter-name] [src-interfacesrc-interface-name] |
server3 {domain | ip} [vrouter vrouter-name] [src-interfacesrc-interface-name] | protocol
HTTP]

<!-- 来源页 456 -->
l
mode {auto | manual} – 指定升级共享接入特征库的方式，分为自动升级和手动升级。不配置默认为
自动升级。
l
proxy-server {main | backup} proxy-ip proxy-port – 指定升级共享接入特征库的代理服务器。
l
schedule {daily | weekly {sun | mon | tue | wed | thu | fri | sat} | monthly date} – 指定自动升
级共享接入特征库的升级周期。
l
server1 {domain | ip} [vrouter vrouter-name] – 指定升级服务器1的域名、IP地址以及所属的
VRouter。
l
server2 {domain | ip} [vrouter vrouter-name] – 指定升级服务器2的域名、IP地址以及所属的
VRouter。
l
server3 {domain | ip} [vrouter vrouter-name] – 指定升级服务器3的域名、IP地址以及所属的
VRouter。
l
protocol HTTP - 指定升级的传输协议为HTTP，默认为HTTPS。
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，共享接入特征库更新时将通过该源接口对更新服务器发起访问。若不指定，则默认使用管理口作为
源接口。
立即更新
用户可以立即升级共享接入特征库。在执行模式下，使用以下命令：
exec share-access-detect signature update
导入共享接入特征库文件
在某些情况下，用户设备可能无法连接到更新服务器对共享接入特征库进行更新，针对这一问题，StoneOS
提供共享接入特征库文件导入功能。用户可以通过FTP或者TFTP方式导入共享接入特征库，从而更新设备的
特征库。导入共享接入特征库文件，在执行模式下，使用以下命令：
import share-access-detect signature from {ftp server { A.B.C.D | X:X:X:X::X } [vrouter
vrouter-name] [user username password string] | tftp server { A.B.C.D | X:X:X:X::X }[vrouter
vrouter-name]} file-name
l
ftp server { A.B.C.D | X:X:X:X::X } [vrouter vrouter-name] [user user-name password
password] – 指定从FTP服务器获取共享接入特征库文件，并指定FTP服务器的IP地址、FTP服务器所属
的VRouter以及访问服务器使用的用户名和密码。当不输入用户名和密码时表示采用匿名登录方式。

<!-- 来源页 457 -->
l
tftp server { A.B.C.D | X:X:X:X::X } [vrouter vrouter-name] – 指定从TFTP服务器获取共享接入特
征库文件，并指定TFTP服务器的IP地址以及所属的VRouter。
l
file-name – 指定导入的共享接入特征库文件的名称。
查看共享接入特征库升级信息
用户可以在任何模式下使用以下命令查看共享接入特征库升级信息：
show share-access-detect signature update
查看共享接入特征库信息
用户可以在任何模式下使用以下命令查看共享接入特征库信息：
show share-access-detect signature info
查看共享接入统计信息
用户可以在任何模式下使用以下命令查看共享接入统计信息：
show share-access-detect statistics [rule rule-name] [src-ip ip-address] [src-zone zonename] [status {blocking | normal | logging | warning}] [endpoint-num {gt | lt | eq} number]
l
rule rule-name – 显示指定共享接入规则下的终端统计信息。
l
src-ip ip-address – 显示指定源IP地址下的终端统计信息。
l
src-zone zone-name – 显示指定源安全域下的终端统计信息。
l
status {normal | logging | warning} – 显示终端IP地址为指定状态下的接入终端统计信息。
l
blocking – 显示终端IP地址为阻断状态下的接入终端统计信息。
l
normal – 显示终端IP地址为正常状态下的接入终端统计信息。
l
logging –显示终端IP地址为记录日志状态下的接入终端统计信息。
l
warning -显示终端IP地址为告警状态下的接入终端统计信息。
l
endpoint-num {gt | lt | eq} number – 显示指定条件的终端数量的终端统计信息。
l
gt – 显示终端数量为大于某数值（该值为用户指定的number的数值）的终端统计信息。
l
lt -显示终端数量为小于某数值（该值为用户指定的number的数值）的终端统计信息。
l
eq -显示终端数量为等于某数值（该值为用户指定的number的数值）的终端统计信息。
l
number – 指定的终端的数量。

<!-- 来源页 458 -->
共享接入日志
用户可以根据需要更改共享接入日志信息。共享接入日志更新配置包括：
l
配置共享接入日志的状态
l
配置共享接入日志信息输出目的地
l
查看共享接入日志信息
配置共享接入日志的状态
开启共享接入日志的功能，在全局配置模式下，使用以下命令，默认开启该功能：
logging share-access-detect on
在全局配置模式下，使用该命令no的形式关闭共享接入日志功能：
no logging share-access-detect on
配置共享接入日志信息输出目的地
用户可以根据需要指定共享接入日志信息的输出目的地，可以是Syslog服务器、内存缓存和Console。默认
输出到内存缓存。在全局配置模式下，使用以下命令：
logging share-access-detect to { syslog | buffer [size buffer-size] | console}
l
syslog – 指定将日志信息输出到系统日志服务器，此时需要在该服务器上指定记录共享接入检测日志的
信息。
l
buffer [size buffer-size] –指定将日志信息输出到内存缓存，并指定缓存的大小。范围是4096到
524288字节。默认值为524288。
l
console –指定将日志信息输出到Console。
在全局配置模式下，使用该命令no的形式，取消将共享接入日志信息输出到目的地：
no logging share-access-detect to { syslog | buffer [size buffer-size] | console}
查看共享接入日志信息
用户可以在任何模式下使用以下命令查看共享接入日志信息：
show logging share-access-detect

<!-- 来源页 459 -->
ARP防护
ARP防护介绍
系统提供一系列功能进行ARP防护，保护网络免受各种ARP攻击。这些ARP防护功能包括：
l ARP学习：设备通过ARP学习过程获得内网中的IP-MAC的绑定信息，并将绑定信息添加到系统ARP表中。默认情
况下，设备的ARP学习功能是开启的，设备会一直进行ARP学习，并将学到的IP-MAC绑定信息添加到系统ARP表
中。在ARP学习过程中，如果IP或者MAC地址发生变化，设备会将更新的IP-MAC绑定信息添加到系统ARP表中。
关闭ARP学习功能，只有已经在系统ARP表中的IP地址可以访问Internet。
l MAC学习：设备通过MAC学习过程获得内网中的MAC-端口绑定信息，并将其添加到系统MAC表中。默认情况
下，设备的MAC学习功能是开启的，设备会一直进行MAC学习，并将学到的MAC-端口绑定信息添加到系统MAC
表中。在MAC学习过程中，如果MAC地址或者端口发生变化，设备会将更新的MAC-端口绑定信息添加到MAC表
中。
l IP-MAC-端口绑定：IP-MAC、MAC-端口以及IP-MAC-端口绑定后，与绑定列表中不一致的数据包将会被丢弃，
保证系统免受ARP欺骗攻击或者MAC地址表攻击。结合ARP/MAC学习功能，实现“实时扫描+静态绑定”，使防
护配置更加简单有效。
l ARP检查：系统会对通过接口的所有ARP包进行检查，将ARP包的IP地址与系统ARP表中的静态表项以及DHCP监
控列表中的IP-MAC绑定表项进行对比。
l DHCP监控：DHCP监控通过分析DHCP客户端与DHCP服务器之间的DHCP报文建立DHCP客户端的MAC地址和被
分配的IP地址的对应关系。
l 主机防御：设备代替不同主机发送免费ARP包，保护被代理主机免受ARP攻击。
ARP绑定
为加强网络安全控制，设备支持IP-MAC地址绑定、MAC-端口绑定以及IP-MAC-端口绑定。这些绑定信息分
为静态和动态两种。通过ARP学习功能、ARP扫描功能以及MAC学习功能获得绑定信息为动态绑定信息；而
手工配置的绑定信息为静态信息。同时，设备还具有ARP检查功能。
静态绑定
用户可以添加静态IP-MAC绑定条目和MAC-端口绑定条目；还可以限制IP-MAC地址动态学习到的主机不能
上网，仅IP-MAC静态绑定的主机可以上网。
添加静态IP-MAC绑定条目
添加静态IP-MAC绑定条目，在全局模式下，使用以下命令：

<!-- 来源页 460 -->
arp ip-address mac-address [vrouter vrouter-name]
l
ip-address – 指定静态绑定的IP地址。
l
mac-address – 指定静态绑定的MAC地址。
l
vrouter vrouter-name – 添加静态IP-MAC绑定条目到指定VR。用vrouter-name参数指定VR名称。
如不指定该参数，配置的静态IP-MAC绑定条目将属于缺省VR——trust-vr。
在全局配置模式下，使用以下命令删除静态IP-MAC绑定条目：
no arp {all | ip-address} [vrouter vrouter-name]
l
all – 指定删除系统中所有静态IP-MAC绑定条目。
l
ip-address – 删除指定IP地址的IP-MAC绑定条目。
l
vrouter vrouter-name – 删除指定VR的静态IP-MAC绑定条目。用vrouter-name参数指定VR名称。
如不指定该参数，系统将删除缺省VR中的全部或者指定IP地址的静态IP-MAC绑定条目。
添加静态MAC-端口绑定条目
添加静态MAC-端口绑定条目，在全局配置模式下，使用以下命令：
mac-address-static mac-address interface interface-name
l
mac-address – 指定静态绑定的MAC地址。
l
interface interface-name – 指定静态绑定的端口。
在全局配置模式下，使用以下命令删除MAC-端口绑定条目：
l
删除系统中所有静态MAC-端口绑定条目：
no mac-address-static all
l
删除指定接口的所有静态MAC-端口绑定条目：
no mac-address-static interface interface-name
l
删除指定的MAC-端口绑定条目：
no mac-address-static mac-address {interface interface-name | vid vlan-id}
仅允许IP-MAC静态绑定主机上网
默认情况下，系统允许ARP动态学习到的主机上网。如果仅允许IP-MAC静态绑定的主机上网，在接口配置
模式下，输入以下命令：
arp-disable-dynamic-entry
使用该命令的no形式关闭该功能：

<!-- 来源页 461 -->
no arp-disable-dynamic-entry
动态IP-MAC-端口绑定
设备可以通过以下两种方式获得动态IP-MAC-端口绑定信息：
l ARP学习功能
l MAC学习功能
ARP学习功能
设备通过ARP学习过程获得内网中的IP-MAC的绑定信息，并将绑定信息添加到系统ARP表中。默认情况
下，设备的ARP学习功能是开启的，设备会一直进行ARP学习，并将学到的IP-MAC绑定信息添加到系统
ARP表中。在ARP学习过程中，如果IP或者MAC地址发生变化，设备会将更新的IP-MAC绑定信息添加到系
统ARP表中。关闭ARP学习功能，只有已经在系统ARP表中的IP地址可以访问Internet。
配置ARP学习功能，在接口配置模式下，使用以下命令：
l
开启ARP学习功能：arp-learning
l
关闭ARP学习功能：no arp-learning
透明模式下的ARP功能
在透明模式下，设备默认没有启用ARP学习功能。用户可以手动开启或关闭ARP学习，以获得IP-MAC的绑
定信息。开启或关闭ARP功能，在VSwitch配置模式下，使用以下命令：
l
开启：arp-l2mode
l
关闭：no arp-l2mode
ARP学习限制功能
开启ARP学习功能后，当一个接口接入的某个用户主机发起ARP攻击时，可能会出现耗尽ARP表项资源的情
况，导致其他接口无法进行ARP学习。为避免上述问题，系统支持开启ARP学习限制功能，并指定该接口允
许学习的最大数量。指定后，如果一个接口达到了允许学习的最大数量，将不再允许该接口继续进行ARP学
习。
开启ARP学习限制功能并指定最大限制数量，在接口配置模式下，使用以下命令：
arp-learning-limit number
l
number - 指定一个接口允许学习的IP-MAC绑定信息的最大数量。取值范围是1到Capacity。不同设备
平台的限制（Capacity）不同，请以实际为准。
在接口配置模式下使用no arp-learning-limit命令关闭ARP学习限制功能。

<!-- 来源页 462 -->
MAC学习功能
设备通过MAC学习过程获得内网中的MAC-端口绑定信息，并将其添加到系统MAC表中。默认情况下，设备
的MAC学习功能是开启的，设备会一直进行MAC学习，并将学到的MAC-端口绑定信息添加到系统MAC表
中。在MAC学习过程中，如果MAC地址或者端口发生变化，设备会将更新的MAC-端口绑定信息添加到MAC
表中。
配置MAC学习功能，在VSwitch接口的接口配置模式下，使用以下命令：
l
开启MAC学习功能：mac-learning
l
关闭MAC学习功能：no mac-learning
显示IP-MAC-端口绑定信息
用户可以通过以下命令查看系统的IP-MAC绑定信息（静态与动态）和MAC-端口绑定信息（静态与动态）。
l
IP-MAC绑定信息：show arp [vrouter vrouter-name]
l
MAC-端口绑定信息：show mac
清除ARP绑定信息
用户可以通过以下命令清除系统中的ARP绑定信息（动态）：
clear arp [interface interface-name [A.B.C.D] | vrouter vrouter-name]
l
interface interface-name – 清除指定接口的ARP绑定信息，使用interface-name参数指定接口名
称。
l
A.B.C.D - 清除接口上指定IP地址的ARP绑定信息。
l
vrouter vrouter-name – 删除指定VRouter的ARP绑定信息，使用vrouter-name参数知道VRouter
的名称。如果不指定该参数，将清除缺省VRouter——trust-vr的ARP绑定信息。
强制绑定动态MAC-端口绑定信息
用户可以将系统通过MAC学习得到的动态MAC-端口绑定信息进行强制绑定。配置强制绑定功能，在任何模
式下，使用以下命令：
exec mac-address dynamic-to-static
配置超时探测次数
系统默认对老化后的ARP表项进行自动探测，对于指定探测次数内未收到应答的表项进行删除。用户可以对
探测次数进行配置，当设置0时，表示关闭自动探测。关闭后，ARP表项到达老化时间后将直接被删除。

<!-- 来源页 463 -->
注意:
l
配置后，对所有接口的ARP表项都生效。
l
非根VSYS会同步根VSYS下的配置，但不支持在非根VSYS下配置该功能。
配置ARP自动探测次数，在全局模式下，使用以下命令：
arp timeout-probe timestimes
l
times - 指定ARP自动探测的次数，取值范围是0到50次，默认值是33，0次表示关闭ARP自动探测。
在全局配置模式下，使用以下命令恢复ARP自动探测的默认值：
no arp timeout-probe times
显示ARP自动探测次数
用户可以在任何模式下通过以下命令查看当前ARP自动探测次数：
show arp timeout-probe times
ARP检查
设备支持接口的ARP检查功能。开启该功能后，系统会对通过接口的所有ARP包进行检查，将ARP包的IP地
址与系统ARP表中的静态表项以及DHCP监控列表中的IP-MAC绑定表项进行对比：
l 如果IP地址在ARP表中，并且与表中记录的MAC地址相同，则继续转发该ARP包；
l 如果IP地址在ARP表中，但是与表中记录的MAC地址不一致，系统将丢弃该ARP包；
l 如果IP地址不在ARP表中，则继续检查该IP地址是否在DHCP监控列表中；
l 如果IP地址在DHCP监控列表中，并且与表中记录的MAC地址相同，则继续转发该ARP包；
l 如果IP地址在DHCP监控列表中，但是与表中记录的MAC地址不一致，系统将丢弃该ARP包；
l 如果IP地址不在DHCP监控列表中，则根据配置进行丢弃或者转发。
开启/关闭ARP检查功能
系统的BGroup接口、VSwitch接口以及VLAN均支持ARP检查功能。默认情况下，该功能是关闭的。
开启BGroup或者VSwitch接口的ARP检查功能
开启BGroup或者VSwitch接口的ARP检查功能，在BGroup或者VSwitch接口的接口配置模式下，使用以
下命令：
arp-inspection {drop | forward}

<!-- 来源页 464 -->
l
drop – 丢弃IP地址不在ARP表中的ARP包。
l
forward – 转发IP地址不在ARP表中的ARP包。
在BGroup或者VSwitch接口的接口配置模式下，使用该命令no的形式关闭接口的ARP检查功能：
no arp-inspection
开启VLAN的ARP检查功能
开启VLAN的ARP检查功能，在全局配置模式下，使用以下命令：
arp-inspection vlanvlan-list {drop | forward}
l
vlan-list – 指定开启ARP检查功能的VLAN编号。取值范围为1到4094，可以为1、2-4、1，2，5等。
系统为BGroup保留32个VLAN编号（从VLAN224到VLAN255）。
在全局配置模式下，使用该命令no的形式关闭VLAN的ARP检查功能：
no arp-inspection vlanvlan-list
配置可信接口
用户可以设置设备的接口(BGroup或者VSwitch接口中的物理接口)为可信接口，通过可信接口的数据包将
不会受到ARP检查。默认情况下，设备所有的接口都是不可信的。配置设备的某个接口为可信接口，在接口
配置模式下，使用以下命令：
arp-inspection trust
在接口配置模式下，使用该命令no的形式取消可信接口的配置：
no arp-inspection trust
配置ARP包速率限制
配置接收ARP包的速率限制，在接口配置模式下，使用以下命令：
arp-inspection rate-limitnumber
l
number – 指定接口每秒钟接收ARP包的个数。当每秒钟接收ARP包的个数超过该指定值时，系统将丢
弃超出的ARP包。范围是0到10000。默认值是0，即无速率限制。
在接口配置模式下，使用该命令no的形式取消速率限制的配置：
no arp-inspection rate-limit
注意: 只能在绑定到二层域的物理接口上配置ARP包速率检查。

<!-- 来源页 465 -->
DHCP监控
DHCP为动态主机配置协议（Dynamic Host Configuration Protocol），它能够自动为子网分配适当的
IP地址以及其它网络参数。DHCP监控通过分析DHCP客户端与DHCP服务器之间的DHCP报文建立DHCP客
户端的MAC地址和被分配的IP地址的对应关系。在启动ARP检查功能后，将检查经过设备的ARP包是否与该
表的内容匹配，如果不匹配则丢弃该ARP包。在用DHCP获取地址的网络中，可以通过启用ARP检查和DHCP
监控功能来防止ARP欺骗。
由于DHCP服务的客户端是以广播的方式寻找服务器，并且只接收第一个到达的服务器提供的网络配置参
数，因此，如果网络中存在非授权的DHCP服务器，就有可能引发DHCP服务器欺骗。设备可以通过在相应端
口上设置丢弃DHCP响应报文来防止DHCP服务器欺骗。
另外，一些恶意攻击者通过伪造不同的MAC地址不断地向DHCP服务器发送DHCP请求，从而耗尽服务器的
IP地址资源，最终导致合法用户不能获得IP地址。这种攻击也即网络上常见的DHCP Starvation Attack。
设备可以通过在相应端口上设置丢弃请求报文、设置DHCP包速率限制或者打开合法性检查功能来防止该类
攻击。
开启/关闭DHCP监控功能
系统的BGroup接口、VSwitch接口以及VLAN均支持DHCP监控功能。默认情况下，该功能是关闭的。
开启BGroup或者VSwitch接口的DHCP监控功能
开启BGroup或者VSwitch接口的DHCP监控功能，在BGroup或者VSwitch接口的接口配置模式下，使用以
下命令：
dhcp-snooping
在BGroup或者VSwitch接口的接口配置模式下，使用该命令no的形式关闭接口的DHCP监控功能：
no dhcp-snooping
开启VLAN的DHCP监控功能
开启VLAN的DHCP监控功能，在全局配置模式下，使用以下命令：
dhcp-snooping vlanvlan-list
l
vlan-list – 指定开启DHCP监控功能的VLAN编号。取值范围为1到4094，可以为1、2-4、1，2，5
等。系统为BGroup保留32个VLAN编号（从VLAN224到VLAN255）。
在全局配置模式下，使用该命令no的形式关闭VLAN的DHCP监控功能：
no dhcp-snooping vlanvlan-list

<!-- 来源页 466 -->
配置DHCP检查功能
用户可以配置设备的DHCP检查功能，包括配置对DHCP请求报文和响应报文的处理方式以及有效性检查。默
认情况下，所有的DHCP请求和响应报文都是允许的，并且无有效性检查。配置DHCP检查功能，在以太网接
口（BGroup或者VSwitch接口中的物理接口）配置模式下，使用以下命令：
dhcp-snooping {deny-request | deny-response | validity-check}
l
deny-request – 丢弃从客户端发送到服务器端的所有请求报文。
l
deny-response – 丢弃从服务器端发送到客户端的所有响应报文。
l
validity-check – 检查DHCP包的客户端MAC地址与以太网包的源MAC地址是否一致，如不一致，则丢
弃。
在接口配置模式下，使用该命令no的形式关闭DHCP检查功能：
no dhcp-snooping {deny-request | deny-response | validity-check}
配置DHCP包速率限制
配置接收DHCP包的速率限制，在以太网接口（BGroup或者VSwitch接口中的物理接口）配置模式下，使用
以下命令：
dhcp-snooping rate-limitnumber
l
number – 指定接口每秒钟接收DHCP包的个数。当每秒钟接收DHCP包的个数超过该指定值时，系统将
丢弃超出的DHCP包。范围是0到10000。默认值是0，即无速率限制。
在接口配置模式下，使用该命令no的形式取消速率限制的配置：
no dhcp-snooping rate-limit
显示DHCP监控配置信息
用户可以在任何模式下通过以下命令查看DHCP监控功能的配置信息：
show dhcp-snooping configuration
DHCP监控列表
启用DHCP监控功能后，系统会对通过接口的所有DHCP包进行检查，并在此过程中建立并维护一个包含IPMAC绑定信息的DHCP监控列表。另外，当系统的BGroup接口、VSwitch接口以及其它三层物理接口配置
为DHCP服务器时，不用开启DHCP监控功能，系统也会自动建立IP-MAC绑定信息并将它们添加到DHCP监
控列表中。列表中的绑定条目包含合法用户的MAC 地址、所获IP地址、设备接口、VLAN编号、租约期限等
信息。用户可以在任何模式下通过以下命令查看DHCP监控列表信息：
show dhcp-snooping binding

<!-- 来源页 467 -->
在任何模式下，用户可以使用以下命令删除所有的或者指定的DHCP监控列表条目：
clear dhcp-snooping binding [interfaceinterface-name [A.B.C.D]]
l
clear dhcp-snooping binding – 删除DHCP监控列表中所有的绑定条目。
l
interfaceinterface-name – 指定接口名称，删除指定接口的绑定条目。
l
interfaceinterface-name [A.B.C.D] – 指定某个接口下的IP地址，删除此接口下特定IP的绑定条目。
主机防御
设备的主机防御功能即设备代替不同主机发送免费ARP包，保护被代理主机免受ARP攻击。
配置主机防御功能，在全局配置模式下，使用以下命令：
gratuitous-arp-send ip ip-address mac mac-address switch-interface interface-name
except-interface interface-name rate rate-value
l
ip ip-address – 指定被代理主机的IP地址。
l
mac mac-address – 指定被代理主机的MAC地址。
l
switch-interface interface-name – 指定发送ARP广播包的接口。可以是VSwitch接口或者BGroup
接口。
l
except-interface interface-name – 指定排除接口，即不发送免费ARP包的接口。通常为连接被代
理主机的接口。
l
rate rate-value - 指定设备发送免费ARP包的速率。单位为个/每秒。默认值为1个。取值范围是1到
10个。
配置多条该命令代理多台主机发送免费ARP包。设备最多可代理16台主机发送免费ARP包。
在全局配置模式下，使用以下命令取消代理指定主机发送免费ARP包功能：
no gratuitous-arp-send ip ip-address switch-interface interface-name
ARP防御
通过使用ARP学习、MAC学习以及ARP检查功能，系统能够很好的防御ARP欺骗攻击。并且，系统能够对
ARP欺骗攻击进行统计。显示ARP欺骗攻击统计信息，任何模式下，使用以下命令：
show arp-spoofing-statistics [number]
l
number – 显示统计数最高的前number条记录。
清除系统中的ARP欺骗攻击统计信息，在执行模式下，使用以下命令：
clear arp-spoofing-statistics

<!-- 来源页 468 -->
全局黑白名单
全局黑白名单功能包含以下内容：
l 全局黑白名单介绍
l 边界流量过滤
l 域名管控
l URL管控
l 黑名单全局配置
l 查看黑白名单
型号说明：仅以下型号支持全局黑白名单功能：
l
A/B系列所有型号
l
K系列所有型号
l
X系列所有型号
l
云·界
全局黑白名单介绍与应用场景
在当前环境下，挖矿、勒索、恶意文件传播等是用户主要面临的网络风险。面对这些风险，通过威胁情报辅
助构建的IP、域名以及URL管控，已经逐渐成为网络边界防护的基本措施之一，同时也是应对威胁的快速处
置手段。全局黑白名单功能整合了多种管控方式，在方便用户使用的同时，也能够为用户提供全面有效的安
全防护。
全局黑白名单功能包含以下内容：
功能
说明
使用场景
边界流量过滤
基于已知的风险IP、MAC或服务等对流量
进行过滤，并对命中风险IP、MAC或服务
的恶意流量采取阻断、记录日志等措施进
行处理。
在企业网络边界或网络安全防护的关键节点，为防止
外部已知风险源对内部网络造成威胁，需要对进出网
络的流量进行过滤。
例如：当企业得知某些特定IP地址频繁发起恶意攻
击，或者某些MAC地址关联的设备存在异常网络行
为，又或者某些服务被证实为恶意软件传播的途径
时，就可以使用此功能。

<!-- 来源页 469 -->
功能
说明
使用场景
域名管控
基于域名对流量进行管控。当检测到命中
风险域名的流量时，系统会采取阻断措
施，从而有效避免用户访问恶意网站，保
障网络环境安全。
在网络访问过程中，部分域名可能被用于恶意活动，
如钓鱼网站、恶意软件下载站点等。企业为保护员工
免受这些恶意域名的侵害，确保内部网络安全，以及
防止企业数据泄露至恶意域名服务器，需要对域名访
问进行管控。
URL管控
基于URL对流量进行管控。当检测到命中
风险URL的流量时，系统会采取阻断措
施，确保用户不会访问到存在安全隐患的
网页，降低安全风险。
随着互联网应用的丰富，部分URL可能隐藏着安全风
险，如包含恶意脚本的网页链接、诱导用户下载恶意
软件的URL等。
在企业办公环境中，为防止员工误点击这些风险
URL，导致企业网络遭受攻击或数据泄露，需要对URL
进行管控。
全局检索
支持查询指定IP、域名或URL的黑白名单
条目信息。通过输入目标IP、域名或
URL，系统能够快速检索并展示相应的黑
白名单详细信息。
网络安全管理人员在进行日常安全维护、调查安全事
件或规划网络访问策略时，可能需要快速了解指定
IP、域名或URL在黑白名单中的相关信息。
全局配置
黑名单全局配置，包括记录日志、会话重
匹配以及IP黑名单TCP重置。
为了统一且高效地管理黑名单，确保整个网络在面对
恶意流量时能采取一致且有效的应对措施，需要进行
黑名单全局配置。
边界流量过滤
边界流量过滤配置包含以下内容：
l 边界流量过滤介绍
l IP黑名单
l Service黑名单
l MAC黑名单
l IP信誉过滤
l IP白名单
边界流量过滤介绍与应用场景
基于已知的风险IP、MAC或服务等对流量进行过滤。当检测到命中风险IP、MAC或服务的恶意流量时，系统
将采取阻断措施，防止恶意流量进入或流出内部网络，同时记录日志信息，以便后续进行安全事件分析与溯
源。
边界流量过滤功能包含以下内容：

<!-- 来源页 470 -->
功能
说明
使用场景
IP黑名单
基于已知的风险IP对流量进行过滤，并对
命中风险IP的恶意流量采取阻断、记录日
志等措施进行处理。同时可以对列入黑名
单的用户进行网络访问管控，在预设时间
段内，被列入黑名单的用户将无法连接网
络。
在企业网络边界防护中，常常会面临来自外部的各种
恶意网络攻击。
例如，企业可能遭受过来自特定IP地址的持续DDoS
攻击，导致网络服务中断，影响业务正常开展。对于
这些已知的风险IP，就需要通过IP黑名单功能来进行
防范。
Service黑名单
将服务添加到黑名单后，系统将对涉及该
黑名单服务的流量进行阻断，直到阻断时
间结束。
企业内部网络中，某些服务可能存在安全漏洞，容易
成为黑客攻击的目标。
例如，某些未授权的远程控制服务，可能被不法分子
用于非法获取企业内部数据。为了防止这些潜在的风
险，就可以使用Service黑名单功能。
MAC黑名单
将主机的MAC地址添加到黑名单中，并通
过绑定时间表的方式，实现对列入黑名单
主机的网络访问管控。在预设时间段内，
被列入黑名单的主机将无法连接网络。
在企业办公网络环境中，可能会存在一些违反网络使
用规定的内部主机。
例如，某些员工私自将个人设备接入办公网络，且该
设备携带病毒，可能对整个网络造成威胁；或者某些
离职员工的设备仍在网络中进行异常活动。针对这些
情况，就可以使用MAC黑名单功能。
IP信誉过滤
通过更新IP信誉特征库，系统能够从云端
同步符合僵尸主机、垃圾邮件、Tor节
点、失陷主机、代理服务（器）、扫描、
暴力破解、DDos攻击者等特征的风险IP
地址。对于命中风险IP的流量，系统会采
取相应的处理措施，如丢弃、阻断、记录
日志。
随着网络威胁的不断变化和复杂化，新的恶意IP层出
不穷。企业和网络安全运营者很难及时掌握所有的风
险IP信息。
此时，通过IP信誉过滤功能，借助云端强大的情报资
源，能够及时获取最新的风险IP信息，有效应对不断
变化的网络威胁。
IP白名单
将IP地址添加至IP白名单列表后，系统将
不对白名单中的IP地址做阻断限制，从而
确保关键的网络连接和业务通信不受影
响。
在企业网络中，有些特定的IP地址是企业正常业务运
行所必需的。这些IP地址需要确保能够始终与企业内
部网络进行顺畅的通信，不受其他安全策略的干扰。
注意:
l
使用IP信誉功能前，用户需要首先更新IP信誉特征库。默认情况下，系统会每日自动更新特征
库，用户可以根据需要更改边界流量过滤特征库更新配置。升级方式请参阅升级管理。
l
若需升级IP信誉库，请先安装IP信誉库许可证，然后重启设备。设备成功重启后，升级IP信誉
库功能才可使用。

<!-- 来源页 471 -->
IP黑名单
IP黑名单包含以下内容：
l 配置静态IP黑名单
l 配置动态IP黑名单
l 配置真实IP黑名单
l 配置黑名单库
l IP黑名单命中统计
配置静态IP黑名单
静态IP黑名单能够对指定IP的恶意流量进行过滤阻断。此外，也可以对列入黑名单的用户进行网络访问管
控，在预设时间段内，被列入黑名单的用户将无法连接网络。
进入边界流量过滤配置模式
进入边界流量过滤配置模式，在全局配置模式下，使用以下命令：
perimeter-traffic-filtering
创建静态IP黑名单
创建静态IP黑名单，在边界流量过滤配置模式下，使用以下命令：
blocklist ip [id id] {address {external-dynamic-list external-dynamic-list-name | addressbook address-book | start-ip end-ip | ip-prefix/mask} [direct {both | src | dst}] | user {{user |
group} server-name | role} user-name} [vrouter vrouter-name | zone zone-name] [schedule
schedule-name] [tag tag-name] {enable | disable}
l
id id - 指定静态IP黑名单规则的ID。
l
external-dynamic-list external-dynamic-list-name - 指定添加到静态IP黑名单的外部动态列
表。
l
address-book address-book - 指定添加到静态IP黑名单的地址簿。
l
start-ip end-ip - 指定添加到静态IP黑名单的地址范围。支持配置IPv4或IPv6地址。
l
ip-prefix/mask - 指定添加到静态IP黑名单的网段的IP地址和子网掩码。
l
direct{both | src | dst} - 指定静态IP黑名单的封堵方向，需指定源目的地址、源地址或目的地址。系
统会对指定方向的流量进行阻断。默认封堵方向为源目的地址。

<!-- 来源页 472 -->
l
user {user | group | role}- 指定添加到静态IP黑名单的用户类型，用户、用户组或者角色。
l
server-name - 指定添加到静态IP黑名单的用户所属AAA服务器名称。
l
user-name - 指定添加到静态IP黑名单的用户名称。
l
vrouter vrouter-name | zone zone-name - 指定静态IP黑名单生效的虚拟路由器或安全域。如不
指定，则该黑名单条目在全域生效。
l
schedule schedule-name - 指定系统中已经配置的时间表名称。如果指定该参数，系统将在时间表
指定的时间范围内禁止主机访问网络；如果不指定该参数，系统将永久禁止主机访问网络。关于如何创
建时间表，请参阅《系统管理》的“配置时间表功能”部分。
l
tag tag-name - 指定静态IP黑名单条目的标签，用于区分不同的静态IP黑名单条目，从而满足复杂架
构下的精细化配置需求，降低误操作概率。
l
enable | disable – 启用或禁用该静态IP黑名单条目。
在边界流量过滤配置模式下，使用该命令no的形式删除指定ID的黑名单地址条目：
no blocklist ip id id
查看静态IP黑名单条目，在任意模式下，使用以下命令：
show perimeter-traffic-filtering blocklist ip
配置静态IP黑名单冗余检查
系统可对黑名单条目进行冗余检测，即检查IP地址的覆盖情况，帮助用户排除由于IP地址覆盖导致的匹配问
题。
配置静态IP黑名单冗余检查，在任意模式下，使用以下命令：
exec perimeter-traffic-filtering blocklist-ip redundancy-check start
停止静态IP黑名单冗余检查
停止静态IP黑名单冗余检查，在任意模式下，使用以下命令：
exec perimeter-traffic-filtering blocklist-ip redundancy-check stop
查看静态IP黑名单冗余检查结果
查看静态IP黑名单冗余检查结果，在任意模式下，使用以下命令：
show perimeter-traffic-filtering blocklist-ip redundancy

<!-- 来源页 473 -->
清除静态IP黑名单冗余检查结果
清除静态IP黑名单冗余检查结果，在任意模式下，使用以下命令：
exec perimeter-traffic-filtering blocklist-ip redundancy-check clear
配置动态IP黑名单
动态IP黑名单既可以由威胁引擎基于实时检测动态加入黑名单条目，也可以通过用户手动进行添加。系统将
对黑名单中的IP或用户名执行阻断操作，直到阻断时间结束，确保在面对各种突发的网络威胁时，能够迅速
做出响应并有效防范。
支持加入动态IP黑名单的方式如下：
l 命中入侵防御检测：当开启入侵防御检测并且其模板动作为阻断IP时，命中的IP会被添加到动态IP黑名单中。
l 超出共享接入上限：当配置的共享接入规则的超限动作为阻断时，超出上限的终端IP会被添加到动态IP黑名单
中。
l 命中IP信誉过滤：当开启IP信誉过滤且处理动作为阻断时，命中的IP会被添加到动态IP黑名单中。
l 资产一键断网：当通过云景或防火墙本地对资产进行断网时，系统会将对应资产的IP添加到动态IP黑名单中。
l 命中蜜罐诱捕（仅WebUI支持）：蜜罐系统会将诱捕到的攻击者信息进行威胁分析并同步至防火墙进行展示，用
户可以在“策略> 蜜罐诱捕>威胁信息”页面查看攻击者的威胁信息，并根据需要将攻击者IP加入动态IP黑名
单。
l 用户监控页面手动加入（仅WebUI支持）：用户可以在“监控> 用户监控> 概览”页面的用户流量排名TOP 10
和用户并发连接排名TOP 10中，通过点击“添加到黑名单”，将对应IP加入动态IP黑名单。
l 首页/用户监控页面手动加入（仅WebUI支持）：用户可以在“首页”或者“监控> 用户监控> 概览”页面的用
户流量排名TOP 10和用户并发连接排名TOP 10中，通过点击“添加到黑名单”，将对应IP加入动态IP黑名单。
l 与云景联动：防火墙连接云景并开启云配置功能后，云景支持将阻断IP下发到动态IP黑名单中。
l 与其他设备联动：通过与其他设备联动，自动将黑名单条目下发到动态IP黑名单中，如BDS联动防火墙等。
l 手动添加动态IP黑名单。
创建动态IP黑名单
创建动态IP黑名单条目，在任意模式下，使用以下命令：
exec block-ip add {{ip | ipv6} ip-address [direct {both | src | dst}] | user {{user | group} servername | role} user-name} [vrouter vrouter-name] [timeout timeout-value]

<!-- 来源页 474 -->
l
{ip | ipv6} ip-address - 指定被阻断的IP地址。支持配置IPv4或IPv6地址。
l
direct {both | src | dst} - 指定动态IP黑名单的封堵方向，需指定源目的地址、源地址或目的地址。系
统会对指定方向的流量进行阻断。默认封堵方向为源目的地址。
l
user {user | group | role} - 指定被阻断的用户类型，用户、用户组或者角色。
l
server-name - 指定被阻断的用户所属AAA服务器名称。
l
user-name - 指定被阻断的用户名称。
l
vrouter vrouter-name - 指定被阻断IP所属的虚拟路由器。如不指定，则该黑名单条目在全域生效。
l
timeout timeout-value - 指定黑名单的阻断时长，取值范围是60到1296000秒。当不配置阻断时
长，默认为永久阻断。
删除动态IP黑名单条目，在任意模式下，使用以下命令：
exec block-ip remove {all | {{ip | ipv6} ip-address [direct {both | src | dst}] | user {{user |
group} server-name | role} user-name} [vrouter vrouter-name] [timeout timeout-value]}
查看动态IP黑名单条目，在任意模式下，使用以下命令：
show block-ip [{ip | ipv6} ip-address]
配置真实IP黑名单
一般情况下用户可以通过查看HTTP数据包判断客户端IP地址，如果客户端进行了代理设置，HTTP数据包中
查看到的源IP地址将会是代理服务器的IP地址，不是真实的客户端IP地址。系统发现攻击后，进行阻断时将
会阻断代理服务器的IP地址，导致所有业务不可用。为了解决上述问题，用户可通过解析HTTP数据包中的
X-Forwarded-For字段和X-Real-IP字段来判断真实的客户端IP地址。其中，X-Forwarded-For字段用于
记录真实客户端IP地址和每一级代理服务器的地址，X-Real-IP字段仅用于记录真实客户端IP地址。
注意: 开启入侵防御功能和防护模式后，真实IP黑名单功能才会生效。开启入侵防御功能参见"IPS
入侵防御配置流程和指导" 在第2179页章节，开启防护模式参见WebUI手册“网络连接> 全局网
络参数> 配置防护模式”章节。
将解析出的真实客户端IP地址加入真实IP黑名单后，系统将对黑名单中的IP执行阻断操作，直到阻断时间结
束。
支持加入真实IP黑名单的方式如下：
l 命中入侵防御检测：当开启入侵防御检测并且其模板中开启了CC防护功能，同时CC防护功能中开启了X-Real-IP
和访问限速，且访问限速动作为阻断时，命中的IP会被添加到真实IP黑名单中。
l 手动添加真实IP黑名单。

<!-- 来源页 475 -->
创建真实IP黑名单
创建真实IP黑名单条目，在任意模式下，使用以下命令：
exec block-real-ip add {ip | ipv6} ip-address [vrouter vrouter-name] [timeout timeout-value]
l
{ip | ipv6} ip-address - 指定被阻断的IP地址。支持配置IPv4或IPv6地址，仅当系统版本为IPv6版本
时可指定IPv6地址。
l
vrouter vrouter-name - 指定被阻断IP所属的虚拟路由器。
l
timeout timeout-value - 指定黑名单的阻断时长，取值范围是60到1296000秒。当不配置阻断时
长，默认为永久阻断。
删除真实IP黑名单条目，在任意模式下，使用以下命令：
exec block-real-ip remove {all | {ip | ipv6} ip-address [vrouter vrouter-name] }
查看真实IP黑名单条目
查看真实IP黑名单条目，在任意模式下，使用以下命令：
show block-real-ip [{ip | ipv6} ip-address]
l
{ip | ipv6} ip-address - 显示指定IP地址的真实IP黑名单条目。支持指定IPv4（ip）或IPv6（ipv6）
地址，仅当系统版本为IPv6版本时可指定IPv6地址。如不指定，则展示所有真实IP黑名单条目。
配置黑名单库
系统支持导入/导出黑名单库文件或从指定服务器更新黑名单文件，并指定黑名单库的策略。
配置黑名单库
配置黑名单库，在边界流量过滤配置模式下，使用以下命令：
blocklist lib [direct {both | src | dst}] [vrouter vrouter-name | zone zone-name] {enable |
disable}
l
direct {both | src | dst} - 指定黑名单库的封堵方向，需指定源目的地址、源地址或目的地址。系统会
对指定方向的流量进行阻断。默认封堵方向为源目的地址。
l
vrouter vrouter-name | zone zone-name - 指定黑名单库生效的虚拟路由器或安全域。如不指
定，则该黑名单库在全域生效。
l
enable | disable – 启用或禁用黑名单库。

<!-- 来源页 476 -->
导入黑名单库文件
导入黑名单库文件，在执行模式下，使用以下命令：
import blocklist-lib {add | cover} from {{ftp | ftps | sftp} server ip-address [user user-name
password password] | tftp server ip-address} [vrouter vrouter-name] file-name
l
add | cover - 指定黑名单库更新的方式，add表示增量覆盖，cover表示全量覆盖。
l
{ftp | ftps | sftp} server ip-address [user user-name password password] - 指定
FTP/FTPS/SFTP服务器的IP地址及账户名称密码。
l
tftp server ip-address - 指定TFTP服务器的IP地址。
l
vrouter vrouter-name] - 指定FTP、FTPS、SFTP或者TFTP服务器所属的VRouter。
l
file-name – 指定导入的黑名单库文件的名称。
导出黑名单库文件
导出黑名单库文件，在执行模式下，使用以下命令：
export blocklist-lib to {{ftp | ftps | sftp} server ip-address [user user-name password
password] | tftp server ip-address} [vrouter vrouter-name] file-name
l
{ftp | ftps | sftp} server ip-address [user user-name password password] - 指定
FTP/FTPS/SFTP服务器的IP地址及账户名称密码。
l
tftp server ip-address - 指定TFTP服务器的IP地址。
l
vrouter vrouter-name] - 指定FTP、FTPS、SFTP或者TFTP服务器所属的VRouter。
l
file-name – 指定导出的黑名单库文件的名称。
配置黑名单库自动更新服务器
配置黑名单库自动更新服务器，在边界流量过滤配置模式下，使用以下命令：
blocklist lib update {add | cover} from { {ftp server ip-address [user user-name password
password] | tftp server ip-address} file-name | {http | https} url url} [vrouter vrouter-name]
l
add | cover - 指定黑名单库自动更新的方式，add代表增量覆盖，cover代表全量覆盖。
l
ftp server ip-address [user user-name password password] - 指定FTP服务器的IP地址及账户
名称密码。
l
tftp server ip-address - 指定TFTP服务器的IP地址。

<!-- 来源页 477 -->
l
vrouter vrouter-name] - 指定FTP、TFTP、HTTP或者HTTPS服务器所属的VRouter。
l
file-name – 指定从FTP或者TFTP服务器导入的黑名单库文件的名称。
l
http | https – 指定从HTTP或者HTTPS服务器更新黑名单库。
l
url url– 指定HTTP或者HTTPS服务器的URL地址，范围是1-255个字符。HTTP服务器URL必须以
“http://”开头，HTTPS服务器URL必须以“https://”开头。
在边界流量过滤配置模式下，使用no blocklist lib update命令关闭黑名单库自动更新功能。
注意:
l
导入或自动更新的黑名单库文件仅支持TXT和CSV格式（仅对FTP或TFTP类型服务器生效）。
l
导入或自动更新的黑名单文件大小不能大于40M。
l
导入或自动更新的黑名单库文件时会按导入先后顺序进行冗余检测，后导入的条目若被先导入
的条目完全覆盖则导入失败。
配置黑名单库自动更新的频率和时间
配置黑名单库自动更新的频率和时间，在边界流量过滤配置模式下，使用以下命令：
blocklist lib update schedule {daily [HH:MM] | weekly {mon | tue | wed | thu | fri | sat | sun}
[HH:MM] | interval time-value}
l
daily – 指定频率为每天更新。
l
weekly {mon | tue | wed | thu | fri | sat | sun} – 指定频率为每周更新。mon | tue | wed | thu | fri
| sat | sun用来指定每周更新的日期。
l
HH:MM – 指定更新的时间，例如09：00。
l
interval – 指定频率为按周期更新。
l
time-value – 指定更新周期时间，单位为分钟。取值范围为1-10080分钟。
清空当前黑名单库文件以及内存中加载的当前VSYS的黑名单库
清空当前黑名单库文件以及内存中加载的当前VSYS的黑名单库，在任意模式下，使用以下命令：
clear perimeter-traffic-filtering blocklist lib
查看黑名单库配置信息
查看黑名单库配置信息，在任意模式下，输入以下命令：

<!-- 来源页 478 -->
show perimeter-traffic-filtering blocklist lib
查看黑名单库自动更新配置信息
查看黑名单库自动更新配置信息，在任意模式下，输入以下命令：
show perimeter-traffic-filtering blocklist lib update
IP黑名单命中统计
系统支持对IP黑名单命中情况进行统计，用户可以查询所有命中的IP黑名单条目的的详细信息，包括IP地
址、封堵方向、作用域、首次命中时间、最近一次命中时间及命中数。
查询IP黑名单命中统计
在任意模式下，输入以下命令查询IP黑名单命中统计信息：
show perimeter-traffic-filtering blocklist hit-info {all | top top-number | {ip | ipv6} ipaddress [direct {both | src | dst}] [vrouter vrouter-name | zone zone-name]}
l
all - 查询所有的IP黑名单的命中统计信息。
l
top top-number - 查询前指定数量的IP黑名单的命中统计信息。
l
{ip | ipv6} ip-address - 查询指定IP地址的IP黑名单命中统计信息。
l
direct {both | src | dst} - 查询指定封堵方向的IP黑名单命中统计信息。
l
vrouter vrouter-name - 查询指定虚拟路由器的IP黑名单命中统计信息。
l
zone zone-name - 查询指定安全域的IP黑名单命中统计信息。
清除IP黑名单命中统计
在任意模式下，输入以下命令清除IP黑名单命中统计信息：
clear perimeter-traffic-filtering blocklist hit-info {all | ip ip-address [direct {both | src | dst}]
[vrouter vrouter-name | zone zone-name]}
l
all - 清除所有的IP黑名单的命中统计信息。
l
top top-number - 清除前指定数量的IP黑名单的命中统计信息。
l
ipip-address - 清除指定IP地址的IP黑名单命中统计信息。
l
direct {both | src | dst} - 清除指定封堵方向的IP黑名单命中统计信息。
l
vrouter vrouter-name - 清除指定虚拟路由器的IP黑名单命中统计信息。
l
zone zone-name - 清除指定安全域的IP黑名单命中统计信息。

<!-- 来源页 479 -->
配置IP黑名单命中统计数据的缓存时间
由于系统默认的IP黑名单命中统计数据存储时间较短，导致用户无法查看更长时间的统计数据。为满足用户
需求，系统支持配置IP黑名单命中统计数据的缓存时间。默认情况下，系统会将IP黑名单命中统计数据存储6
个小时。
配置IP黑名单命中统计数据的缓存时间，在边界流量过滤配置模式下，使用以下命令：
blocklist ip hit-age-period time-value
l
time-value - 指定IP黑名单命中统计数据的缓存时间，取值范围1~72小时，默认为6小时。
恢复系统默认的缓存时间，在边界流量过滤配置模式下，使用以下命令：
no blocklist ip hit-age-period
Service黑名单
Service黑名单包含以下内容：
l 配置静态Service黑名单
l 配置动态Service黑名单
配置静态Service黑名单
静态Service黑名单通过配置IP掩码、IP前缀、IP范围或地址簿类型的IP地址，在指定时间范围对黑名单中的
条目进行阻断，有效防范因服务漏洞带来的安全风险和网络资源消耗问题。
创建静态Service黑名单
创建静态Service黑名单条目，在边界流量过滤配置模式下，使用以下命令：
blocklist service [id id] src-ip {min-ipv4-address max-ipv4-address | ipv4-address/Mask |
min-ipv6-address max-ipv6-address | ipv6/Mask | address-book address-name} dst-ip
{ipv4-address | ipv6-address} drt-port port-number prot {tcp | udp} [schedule schedulename| vrouter vrouter-name] {enable | disable}
l
id id - 为静态Service黑名单指定ID号，取值范围是1到3000。
l
src-ip {min-ipv4-address max-ipv4-address | ipv4-address/Mask | min-ipv6-address
max-ipv6-address | ipv6/Mask | address-book address-name} - 指定被阻断服务的源地址，
支持配置IPv4地址范围、IPv4地址/掩码、IPv6地址范围、IPv6地址/掩码或地址簿。
l
dst-ip {ipv4-address | ipv6-address} - 指定被阻断服务的目的IP。支持配置IPv4或IPv6地址。
l
vrouter vrouter-name - 指定被阻断IP所属的虚拟路由器。

<!-- 来源页 480 -->
l
drt-port port-number - 指定被阻断服务的目的端口。取值范围是1到65535。
l
prot {tcp | udp} - 指定被阻断服务的协议，包括TCP或UDP协议。
l
schedule schedule-name - 指定黑名单条目生效的时间表。不指定时，默认全时间段内有效。
l
enable | disable - 指定黑名单条目的启用状态。
删除静态Service黑名单条目，在边界流量过滤配置模式下，使用以下命令：
no blocklist service id id
查看静态Service黑名单条目
查看静态Service黑名单条目，在任意模式下，使用以下命令：
show perimeter-traffic-filtering blocklist service
配置动态Service黑名单
动态Service黑名单既可以由威胁引擎基于实时检测动态加入黑名单条目，也可以通过用户手动进行添加。
系统将对黑名单中的服务执行阻断操作，直到阻断时间结束，确保在面对各种突发的网络威胁时，能够迅速
做出响应并有效防范。
支持加入动态Service黑名单的方式如下：
l 与其他设备联动：通过与其他设备联动，自动将黑名单条目下发到动态Service黑名单中，如BDS联动防火墙
等。
l 手动添加动态Service黑名单。
创建动态Service黑名单
创建动态Service黑名单条目，在任意模式下，使用以下命令：
exec block-service add {src-ip src-ip dst-ip dst-ip | src-ipv6 src-ipv6 dst-ipv6 dst-ipv6}
[vrouter vrouter-name] drt-port port-number proto protocol [timeout timeout-value]
l
src-ip src-ip dst-ip dst-ip | src-ipv6 src-ipv6 dst-ipv6 dst-ipv6 - 指定被阻断服务的源IP和目
的IP。支持配置IPv4或IPv6地址。
l
vrouter vrouter-name - 指定被阻断IP所属的虚拟路由器。
l
drt-port port-number - 指定被阻断服务的目的端口。取值范围是1到65535。
l
proto protocol - 指定被阻断服务的协议。

<!-- 来源页 481 -->
l
timeout timeout-value - 指定黑名单的阻断时长，取值范围是60到1296000秒。当不配置阻断时
长，默认为永久阻断。
删除动态Service黑名单条目，在任意模式下，使用以下命令：
exec block-service remove {all | {src-ip src-ip dst-ip dst-ip| src-ipv6 src-ipv6 dst-ipv6 dstipv6} [vrouter vrouter-name] drt-port port-number proto protocol}
查看动态Service黑名单条目
查看动态Service黑名单条目，在任意模式下，使用以下命令：
show block-service [ip ip-address] [ipv6 ipv6-address] [vrouter vrouter-name]
配置MAC黑名单
将主机的MAC地址添加到黑名单中，并通过绑定时间表的方式，实现对列入黑名单主机的网络访问管控。在
预设时间段内，被列入黑名单的主机将无法连接网络。
创建MAC黑名单条目
创建MAC黑名单条目，在边界流量过滤配置模式下，使用以下命令：
blocklist mac [id id] address address [schedule schedule-name] {enable | disable}
l
id id - 指定MAC黑名单规则的ID，不同设备的ID取值范围不同，请以实际设备为准。
l
address address - 指定添加到MAC黑名单的主机的MAC地址。
l
schedule schedule-name - 指定系统中已经配置的时间表名称。如果指定该参数，系统将在时间表
指定的时间范围内禁止主机访问网络；如果不指定该参数，系统将永久禁止主机访问网络。关于如何创
建时间表，请参阅《系统管理》的“配置时间表功能”部分。
l
enable | disable – 启用或禁用该MAC黑名单条目。
在边界流量过滤配置模式下，使用该命令no的形式删除指定ID的黑名单地址条目：
no blocklist mac id id
注意: 不支持配置组播MAC地址和广播MAC地址。
查看MAC黑名单条目
查看MAC黑名单条目，在任意模式下，使用以下命令：
show perimeter-traffic-filtering blocklist mac

<!-- 来源页 482 -->
配置IP信誉过滤
默认情况下，StoneOS会每日自动更新IP信誉特征库，用户可以根据需要更改IP信誉特征库更新配置。IP信
誉过滤配置包括：
l 开启IP信誉过滤功能
l 配置IP信誉特征库更新模式
l 配置更新传输协议
l 配置更新服务器
l 指定更新时间
l 立即更新
l 导入IP信誉特征文件
l 显示IP信誉特征信息
l 显示IP信誉特征库的IP信誉的类别
l 显示IP信誉特征库更新配置信息
注意: 若需升级IP信誉库，请先安装IP信誉库许可证，然后重启设备。设备成功重启后，升级IP信
誉库功能才可使用。
开启IP信誉过滤功能
开启IP信誉过滤功能并进入IP信誉过滤模式，在边界流量过滤配置模式下，使用以下命令：
ip-reputation
配置各类风险IP信誉过滤功能以及指定命中后的处理动作，在IP信誉过滤模式下，使用以下命令：
category category-type action {drop | log-only | block-ip timeout}
l
category-type – 指定IP信誉的类别，包括僵尸主机（bot）、暴力破解（brute-forcer）、失陷主机
（compromised）、DDos攻击者（ddos-attacker）、代理（proxy）、扫描（scanner）、垃圾邮
件（spam）、Tor节点（tornode）、攻防演练（ioc）（该分类适用于攻防演练期间的IP黑名单）。
l
action {drop | log-only | block-ip timeout}- 指定系统命中IP信誉分类的恶意流量后的处理动作。
l
drop – 系统命中IP信誉分类的恶意流量后丢弃数据包。
l
log-only– 系统命中IP信誉分类的恶意流量后仅记录日志信息。该选项为系统默认处理行为。

<!-- 来源页 483 -->
l
block-ip timeout – 系统命中IP信誉分类的恶意流量后阻断IP一定的时间，timeout为阻断的时
长，单位为秒，范围是60到1296000秒。
在IP信誉过滤模式下，使用以上命令no的形式关闭IP信誉过滤功能：
no category category-type
配置IP信誉特征库更新模式
系统支持手动和自动两种更新方式。配置IP信誉特征库更新方式，在全局配置模式下，使用以下命令：
ip-reputation update mode {auto | manual}
l
auto – 指定自动更新IP信誉特征库。该方式为系统的默认更新方式。
l
manual – 指定手动更新IP信誉特征库。
在全局配置模式下使用该命令no的形式恢复默认更新模式：
no ip-reputation update mode
配置更新传输协议
系统支持通过HTTP和HTTPS对特征库进行更新，默认为HTTPS。配置特征库更新的传输协议为HTTP，在全
局配置模式下，使用以下命令：
ip-reputation update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：
no ip-reputation update protocol HTTP
配置更新服务器
系统提供默认的IP信誉特征库更新服务器，即update1.hillstonenet.com和
update2.hillstonenet.com，同时用户也可以根据需要配置其它更新服务器下载最新IP信誉特征。最多可
配置3个。配置更新服务器，在全局配置模式下，使用以下命令：
ip-reputation update {server1 | server2 | server3} {ip-address | domain-name} [vrouter
vrouter-name] [src-interface src-interface-name]
l
server1 | server2 | server3 – 指定将要配置的服务器, 服务器支持双栈协议，可配置IPv4地址和IPv6
地址。server1的默认值为update1.hillstonenet.com，server2的默认值为
update2.hillstonenet.com。
l
ip-address | domain-name – 指定更新服务器的名称，可以是IP地址形式（ip-address）也可以是
域名形式（domain-name，例如update1.hillstonenet.com）。

<!-- 来源页 484 -->
l
vrouter vrouter-name– 指定更新服务器绑定的虚拟路由器。若不指定则默认是trust-vr。
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，IP信誉特征库更新时将通过该源接口对更新服务器发起访问。若不指定，则默认使用管理口作为源
接口。
在全局配置模式下，使用该命令no的形式取消更新服务器的指定：
no ip-reputation signature update {server1 | server2 | server3}
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保特征库能够正常升级，需要在设备上指定代理服务器
的IP地址和端口号。
为IP信誉特征库升级指定代理服务器，在全局配置模式下，使用如下命令：
ip-reputation update proxy-server {main | backup} ip-address port-number
l
main | backup – 使用main参数指定主代理服务器，使用backup指定备份代理服务器。
l
ip-address port-number – 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no perimeter-traffic-filter update proxy-server {main | backup}命
令。
指定更新时间
默认情况下，系统采用自动模式每日更新IP信誉特征库，并且为避免服务器流量过大，每日更新时间是随机
的。用户可以根据需要指定IP信誉特征库更新的频率和时间，在全局配置模式下，使用以下命令：
ip-reputation update schedule {daily [HH:MM] | weekly {mon | tue | wed | thu | fri | sat | sun}
[HH:MM] | hourly minute | monthly date [HH:MM]}
l
daily [HH:MM] – 指定频率为每天更新，HH:MM 用来指定更新的时间，例如09：00。不指定更新时间
将按照系统默认的更新时间进行更新。
l
weekly {mon | tue | wed | thu | fri | sat | sun} – 指定频率为每周更新。mon | tue | wed | thu | fri
| sat | sun用来指定每周更新的日期。
l
hourly minute – 指定频率为每小时更新，minute用来指定每小时更新的具体分钟时刻。
l
monthly date – 指定频率为每月更新。date用来指定每月更新的日期，取值范围为1到31。如果某月
不包含所指定的日期（比如2月没有30号），则该月不会自动升级。
l
HH:MM – 指定更新的时间，例如09：00。

<!-- 来源页 485 -->
导入IP信誉特征文件
在某些情况下，用户设备可能无法连接到更新服务器对IP信誉特征库进行更新，针对这一问题，StoneOS提
供IP信誉特征文件导入功能，即通过FTP、TFTP服务器或者U盘将IP信誉特征文件导入到设备，从而更新设
备的IP信誉特征库。导入IP信誉特征文件，在执行模式下，使用以下命令：
import ip-reputation from {ftp server ip-address [user user-name password password] | tftp
server ip-address } [vrouter vr-name] file-name
l
ip-address – 指定FTP或者TFTP服务器的IP地址。
l
user user-name password password – 指定FTP服务器的用户名和密码。
l
vrouter vr-name – 指定FTP或者TFTP服务器所属的VRouter。
l
file-name – 指定导入的IP信誉特征文件的名称。
查看IP信誉特征库信息
用户可以随时使用相应的show命令查看设备的IP信誉特征库信息，包括IP信誉特征库版本、发布日期以及
IP信誉特征个数等。查看IP信誉特征库信息，在任意模式下，使用以下命令：
show ip-reputation info
查看IP信誉特征库的IP信誉的类别
查看设备的IP信誉特征库包含的IP信誉类别，在任意模式下，使用以下命令：
show perimeter-traffic-filtering ip-reputation category
以下为查看IP信誉类别的命令示例：
hostname(config-ptf-iprep-scope)# show perimeter-traffic-filtering ip-reputation
category
IP-reputation config table, total num: 10
=======================================================
ID                           NAME
-----------------------------------------------------------------
0                           bot（僵尸主机）
1                           spam（垃圾邮件）
2                           tornode （Tor节点）
3                           compromised （失陷主机）
4                           proxy （代理）

<!-- 来源页 486 -->
5                           scanner （扫描）
6                           brute-forcer （暴力破解）
7                           ddos-attacker （DDos攻击者）
8                           ioc （攻防演练）
========================================================
查看IP信誉特征库更新配置信息
用户可以随时使用相应的show命令查看设备上的IP信誉特征库更新信息，包括更新服务器信息、更新模
式、更新频率及时间以及IP信誉特征库更新状况等。查看IP信誉特征库更新配置信息，在任意模式下，使用
以下命令：
show ip-reputation update
配置IP白名单
系统支持全局白名单和边界流量过滤白名单。全局白名单作用于全局，对于在全局白名单中的IP地址，系统
不做任何安全检测，直接放行。边界流量过滤白名单作用于边界流量过滤功能，对于在边界流量过滤白名单
中的IP地址，系统不做边界流量过滤检测，不进行阻断。
注意:
l
NAT转换和流量配额功能不受全局白名单影响。
l
配置NAT转换后，由于系统在NAT转换前后各进行一次边界流量过滤检测，若转换前后的IP地
址并未都设置为全局白名单，则流量可能被黑名单拦截。
l
X系列设备部分攻击防护类型不受全局白名单影响。不受全局白名单影响的攻击防护类型
有：Teardrop、IP Option、IP Fragment、WinNuke、Ping-of-Death、Huge ICMP
Packet、UDP Flood，DNS Flood。
创建IP白名单
创建IP白名单条目，在边界流量过滤配置模式下，使用以下命令：
allowlist [id id] { ip ip-address} [vrouter vrouter-name | zone zone-name | global ]
l
id id–指定白名单规则的ID，不同设备的ID取值范围不同，请以实际设备为准。
l
ip ip-address–指定添加到白名单的IP地址和子网掩码，支持IPv4地址和IPv6地址。
l
[vrouter vrouter-name | zone zone-name | global ]–指定白名单生效的范围：虚拟路由器、安全
域或全局。若不指定，则该条白名单条目在全域生效（即在所有的安全域及虚拟路由器中生效）。

<!-- 来源页 487 -->
域名管控
域名管控包含以下内容：
l 域名管控介绍
l 域名黑名单
l 域名白名单
域名管控介绍与应用场景
在网络访问过程中，部分域名可能被用于恶意活动，如钓鱼网站、恶意软件下载站点等。企业为保护员工免
受这些恶意域名的侵害，确保内部网络安全，以及防止企业数据泄露至恶意域名服务器，需要对域名访问进
行管控。
域名管控功能基于域名对流量进行管控。当检测到命中风险域名的流量时，系统会采取阻断措施，从而有效
避免用户访问恶意网站，保障网络环境安全。
域名管控功能包含以下内容：
功能
说明
使用场景
域名黑名单
域名黑名单功能基于已知的风险域名对流
量进行管控。当流量中出现试图访问这些
风险域名的请求时，系统能够迅速识别并
采取阻断措施，从而维护网络环境的安全
与健康。
钓鱼网站通常模仿正规企业的网站域名，以骗取用户
的账号、密码等敏感信息。当员工尝试访问这些域名
时，系统检测到流量命中风险域名，立即阻断该流
量，防止恶意软件进入企业网络，保护企业内部设备
和数据安全。
域名白名单
域名白名单功能允许用户将指定域名添加
至白名单列表。系统在对流量进行检测和
管理时，不会对白名单域名的流量做阻断
限制，保证重要域名的正常访问。
企业日常办公依赖于一些特定的域名，如企业官方网
站、企业邮箱域名、办公软件在线服务域名等。将这
些与业务紧密相关的域名添加到域名白名单后，系统
不会对这些域名进行阻断限制，确保各项业务能够正
常开展。
域名黑名单
域名黑名单包含以下内容：
l 配置静态域名黑名单
l 配置动态域名黑名单
l 域名黑名单命中统计

<!-- 来源页 488 -->
配置静态域名黑名单
静态域名黑名单能够对指定域名的恶意流量进行阻断，从而有效保护网络内用户和设备的安全，维护网络环
境的健康和合规。
进入域名管控配置模式
进入域名管控配置模式，在全局配置模式下，使用以下命令：
domain-control
创建静态域名黑名单
创建静态域名黑名单，在域名管控配置模式下，使用以下命令：
blocklist-domain [id id] {external-dynamic-list external-dynamic-list-name | domain
domain-name [wildcard]} [vrouter vrouter-name | zone zone-name] [schedule schedulename] [tag tag-name] {enable | disable}
l
id id - 指定静态域名黑名单规则的ID。
l
external-dynamic-list external-dynamic-list-name - 指定添加到静态域名黑名单的外部动态列
表。
l
domain domain-name - 指定添加到静态域名黑名单的域名名称。
l
wildcard - 指定该静态域名黑名单是否作用于子域名。指定后，不仅主域名被列入域名黑名单，其所有
子域名也会被阻止访问。
l
vrouter vrouter-name | zone zone-name - 指定静态域名黑名单生效的虚拟路由器或安全域。如
不指定，则该黑名单条目在全域生效。
l
schedule schedule-name - 指定系统中已经配置的时间表名称。如果指定该参数，系统将在时间表
指定的时间范围内禁止主机访问网络；如果不指定该参数，系统将永久禁止主机访问网络。关于如何创
建时间表，请参阅《系统管理》的“配置时间表功能”部分。
l
tag tag-name - 指定静态域名黑名单条目的标签，用于区分不同的静态域名黑名单条目，从而满足复
杂架构下的精细化配置需求，降低误操作概率。
l
enable | disable – 启用或禁用该静态域名黑名单条目。
在域名管控配置模式下，使用该命令no的形式删除指定ID的域名黑名单条目：
no blocklist-domain id id
查看静态域名黑名单条目，在任意模式下，使用以下命令：

<!-- 来源页 489 -->
show domain-control blocklist-domain
配置动态域名黑名单
用户可以手动添加动态域名黑名单。系统将对黑名单中的域名执行阻断操作，直到阻断时间结束，确保在面
对各种突发的网络威胁时，能够迅速做出响应并有效防范。
创建动态域名黑名单
创建动态域名黑名单条目，在任意模式下，使用以下命令：
exec block-domain add domain domain-name [wildcard] [vrouter vrouter-name] [timeout
time]
l
domain domain-name - 指定被阻断的域名。
l
wildcard - 指定该动态域名黑名单是否作用于子域名。指定后，不仅主域名被列入域名黑名单，其所有
子域名也会被阻止访问。
l
vrouter vrouter-name - 指定动态域名黑名单生效的虚拟路由器或安全域。如不指定，则该黑名单条
目在全域生效。
l
timeout time - 指定黑名单的阻断时长，取值范围是60到1296000秒。若不配置阻断时长，默认为永
久阻断。
删除动态域名黑名单条目，在任意模式下，使用以下命令：
exec block-domain remove {all | domain domain-name [vrouter vrouter-name]}
查看动态域名黑名单条目，在任意模式下，使用以下命令：
show block-domain [domain domain-name]
域名黑名单命中统计
系统支持对域名黑名单命中情况进行统计，用户可以查询所有命中的域名黑名单条目的详细信息，包括域
名、类型、作用域、首次命中时间、最近一次命中时间及命中数。
查询域名黑名单命中统计
在任意模式下，输入以下命令查询域名黑名单的命中统计信息：
show domain-control blocklist hit-info {all | top top-number | domain domain-name
[wildcard [vrouter vrouter-name | zone zone-name] | vrouter vrouter-name | zone zonename]}

<!-- 来源页 490 -->
l
all - 查询所有的域名黑名单的命中统计信息。
l
top top-number - 查询前指定数量的域名黑名单的命中统计信息。
l
domain domain-name - 查询指定域名的域名黑名单命中统计信息。
l
wildcard - 查询作用于子域名的域名黑名单命中统计信息。
l
vrouter vrouter-name - 查询指定虚拟路由器的域名黑名单命中统计信息。
l
zone zone-name - 查询指定安全域的域名黑名单命中统计信息。
清除域名黑名单命中统计
在任意模式下，输入以下命令清除域名黑名单的命中统计信息：
clear domain-control blocklist hit-info {all | domain domain-name [wildcard [vrouter
vrouter-name | zone zone-name] | vrouter vrouter-name | zone zone-name]}
l
all - 清除所有域名黑名单的命中统计信息。
l
domain domain-name - 清除指定域名的域名黑名单命中统计信息。
l
wildcard - 清除作用于子域名的域名黑名单命中统计信息。
l
vrouter vrouter-name - 清除指定虚拟路由器的域名黑名单命中统计信息。
l
zone zone-name - 清除指定安全域的域名黑名单命中统计信息。
配置域名白名单
域名白名单功能允许用户将指定域名添加至白名单列表。系统在对流量进行检测和管理时，不会对白名单域
名的流量做阻断限制，保证重要域名的正常访问。
创建域名白名单
创建域名白名单条目，在域名管控配置模式下，使用以下命令：
allowlist-domain [id id] domain domain-name [wildcard] [vrouter vrouter-name | zone
zone-name]
l
id id–指定域名白名单条目的ID。
l
domain domain-name – 指定添加到域名白名单的域名名称。
l
wildcard – 指定该域名白名单是否作用于子域名。指定后，指定域名及其所有的子域名都将被列入域名
白名单。若不指定，默认不作用于子域名。

<!-- 来源页 491 -->
l
[vrouter vrouter-name | zone zone-name]–指定域名白名单生效的范围：指定虚拟路由器或指定
安全域。若不指定，则该条域名白名单条目在全域生效（即在所有的安全域及虚拟路由器中生效）。
查询域名白名单条目，在任意模式下，使用以下命令：
show domain-control allowlist-domain
URL管控
URL管控包含以下内容：
l URL管控介绍
l URL黑名单
l URL白名单
URL管控介绍与应用场景
随着互联网应用的丰富，部分URL可能隐藏着安全风险，如包含恶意脚本的网页链接、诱导用户下载恶意软
件的URL等。在企业办公环境中，为防止员工误点击这些风险URL，导致企业网络遭受攻击或数据泄露，需
要对URL进行管控。
URL管控功能基于URL对流量进行管控。当检测到命中风险URL的流量时，系统会采取阻断措施，确保用户
不会访问到存在安全隐患的网页，降低安全风险。
URL管控功能包含以下内容：
功能
说明
使用场景
URL黑名单
URL黑名单功能基于已知的风险URL对流
量进行管控。一旦检测到流量中包含命中
风险URL 的恶意流量，系统能够立刻进
行阻断，从而维护网络环境的安全与健
康。
企业员工日常工作频繁接触网络，可能因点击邮件中
的恶意链接、访问伪装成正规网站的恶意网址等，导
致恶意软件或病毒入侵企业网络。将相关URL加入
URL黑名单，可以有效防范相关风险。
URL白名单
URL白名单功能允许用户将指定URL添加
至白名单列表。系统在对流量进行检测和
管理时，不会对白名单URL的流量做阻断
限制，保证正常业务不受影响。
企业日常运营依赖众多核心业务系统，这些系统各自
对应特定的URL。为确保员工能够顺畅、高效地访问
这些系统进行日常工作，企业可以将这些核心业务系
统的URL添加到URL白名单。
URL黑名单
URL黑名单包含以下内容：

<!-- 来源页 492 -->
l 配置静态URL黑名单
l 配置动态URL黑名单
l URL黑名单命中统计
配置静态URL黑名单
静态URL黑名单能够对指定URL的恶意流量进行阻断，从而有效保护网络内用户和设备的安全，维护网络环
境的健康和合规。
进入URL管控配置模式
进入URL管控配置模式，在全局配置模式下，使用以下命令：
url-control
创建静态URL黑名单
创建静态URL黑名单，在URL管控配置模式下，使用以下命令：
blocklist-url [id id] {external-dynamic-list external-dynamic-list-name | url url-string}
[vrouter vrouter-name | zone zone-name] [schedule schedule-name] [tag tag-name]
{enable | disable}
l
id id - 指定静态URL黑名单条目的ID。
l
external-dynamic-list external-dynamic-list-name - 指定添加到静态URL黑名单的外部动态列
表。
l
url url-string - 指定添加到静态URL黑名单的URL名称
l
vrouter vrouter-name | zone zone-name - 指定静态URL黑名单生效的虚拟路由器或安全域。如
不指定，则该黑名单条目在全域生效。
l
schedule schedule-name - 指定系统中已经配置的时间表名称。如果指定该参数，系统将在时间表
指定的时间范围内禁止主机访问网络；如果不指定该参数，系统将永久禁止主机访问网络。关于如何创
建时间表，请参阅《系统管理》的“配置时间表功能”部分。
l
tag tag-name - 指定静态URL黑名单条目的标签，用于区分不同的静态URL黑名单条目，从而满足复
杂架构下的精细化配置需求，降低误操作概率。
l
enable | disable – 启用或禁用该静态URL黑名单条目。
在URL管控配置模式下，使用该命令no的形式删除指定ID的URL黑名单条目：
no blocklist-url id id

<!-- 来源页 493 -->
查看静态URL黑名单条目，在任意模式下，使用以下命令：
show url-control blocklist-url
配置动态URL黑名单
用户可以手动添加动态URL黑名单。系统将对黑名单中的URL执行阻断操作，直到阻断时间结束，确保在面
对各种突发的网络威胁时，能够迅速做出响应并有效防范。
创建动态URL黑名单
创建动态URL黑名单，在任意模式下，使用以下命令：
exec block-url add url url-string [vrouter vrouter-name] [timeout time]
l
url url-string - 指定添加到动态URL黑名单的URL地址。
l
vrouter vrouter-name - 指定动态URL黑名单生效的虚拟路由器或安全域。如不指定，则该黑名单条
目在全域生效。
l
timeout time - 指定黑名单的阻断时长，取值范围是60到1296000秒。若不配置阻断时长，默认为永
久阻断。
删除动态URL黑名单，在任意模式下，使用以下命令：
exec block-url remove {all | url url-string [vrouter vrouter-name]}
查看动态URL黑名单，在任意模式下，使用以下命令：
show block-url [url url-string]
URL黑名单命中统计
系统支持对URL黑名单命中情况进行统计，用户可以查询所有命中的URL黑名单条目的详细信息，包括URL
地址、作用域、首次命中时间、最近一次命中时间及命中数。
查询URL黑名单命中统计
在任意模式下，输入以下命令查询URL黑名单的命中统计信息：
show url-control blocklist hit-info {all | top top-number | url url-string [vrouter vroutername | zone zone-name]}
l
all - 查询所有URL黑名单的命中统计信息。
l
top top-number - 查询前指定数量的URL黑名单的命中统计信息。
l
url url-string - 查询指定URL地址的URL黑名单的命中统计信息。

<!-- 来源页 494 -->
l
vrouter vrouter-name - 查询指定虚拟路由器的URL黑名单的命中统计信息。
l
zone zone-name - 查询指定安全域的URL黑名单的命中统计信息。
清除URL黑名单命中统计
在任意模式下，输入以下命令清除URL黑名单的命中统计信息：
clear url-control blocklist hit-info {all | url url-string [vrouter vrouter-name | zone zonename]}
l
all - 清除所有URL黑名单的命中统计信息。
l
url url-string - 清除指定URL地址的URL黑名单命中统计信息。
l
vrouter vrouter-name - 清除指定虚拟路由器的URL黑名单命中统计信息。
l
zone zone-name - 清除指定安全域的URL黑名单命中统计信息。
配置URL白名单
域名白名单功能允许用户将指定域名添加至白名单列表。系统在对流量进行检测和管理时，不会对白名单域
名的流量做阻断限制，保证重要域名的正常访问。
创建URL白名单
创建URL白名单条目，在URL管控配置模式下，使用以下命令：
allowlist-url [id id] url url-string [vrouter vrouter-name | zone zone-name]
l
id id–指定URL白名单条目的ID。
l
url url-string – 指定添加到URL白名单的URL地址
l
[vrouter vrouter-name | zone zone-name]–指定URL白名单生效的范围：指定虚拟路由器或指定安
全域。若不指定，则该条URL白名单条目在全域生效（即在所有的安全域及虚拟路由器中生效）。
查询URL白名单条目，在任意模式下，使用以下命令：
show url-control allowlist-url
黑名单全局配置
配置黑名单日志记录功能
配置黑名单的日志记录功能，在边界流量过滤配置模式下，使用以下命令：

<!-- 来源页 495 -->
l
开启：log enable
l
关闭：log disable
配置黑名单会话重匹配
开启会话重匹配功能后，当用户添加或者修改黑名单时，会话会重新匹配黑名单。
配置黑名单会话重匹配功能，在边界流量过滤配置模式下，使用以下命令：
l
开启：session rematch ptf enable
l
关闭：session rematch ptf disable
开启/关闭IP黑名单TCP重置
开启IP黑名单TCP重置功能后，系统会向命中黑名单的TCP流量IP地址发送TCP-RST报文，从而阻断该IP地
址。
开启IP黑名单TCP重置功能，在边界流量过滤配置模式下，使用以下命令：
blocklist ip tcp-reset enable
在边界流量过滤配置模式下，使用该命令no的形式关闭IP黑名单TCP重置功能：
no blocklist ip tcp-reset enable
开启/关闭真实IP检测功能
一般情况下用户可以通过查看HTTP数据包判断客户端IP地址，如果客户端进行了代理设置，HTTP数据包中
查看到的源IP地址将会是代理服务器的IP地址，不是真实的客户端IP地址。系统发现攻击后，进行阻断时将
会阻断代理服务器的IP地址，导致所有业务不可用。
为此，系统支持真实IP检测功能。开启该功能后，静态IP黑名单、动态IP黑名单以及黑名单库将检测真实
IP，通过解析HTTP/HTTPS流量中的X-Forwarded-For、X-Real-IP、CDN-SRC-IP字段来判断真实的客
户端IP地址。其中，X-Forwarded-For字段用于记录真实客户端IP地址和每一级代理服务器的地址，XReal-IP字段仅用于记录真实客户端IP地址，CDN-SRC-IP字段用于记录访问CDN节点的源客户端IP。该功
能默认为关闭状态。
开启/关闭真实IP检测功能，在边界流量过滤配置模式下，使用以下命令：
l
开启：blocklist ip check-real-ip enable
l
关闭：blocklist ip check-real-ip disable
查询黑名单日志记录功能的启用状态
在任意模式下，输入以下命令查询黑名单日志记录功能的启用状态：

<!-- 来源页 496 -->
show perimeter-traffic-filtering log
查询IP黑名单TCP重置状态
在任意模式下，输入以下命令查询IP黑名单TCP重置功能状态：
show perimeter-traffic-filtering blocklist ip tcp-reset
查看真实IP检测功能的启用状态
查看真实IP检测功能的启用状态，在任意模式下，使用以下命令：
show perimeter-traffic-filtering blocklist ip check-real-ip
以下是返回结果示例：
hostname# show perimeter-traffic-filtering blocklist ip check-real-ip
Perimeter traffic filtering:
blocklist ip check_real_ip status: enable
查看黑白名单
查看静态IP黑名单
查看静态IP黑名单条目，在任意模式下，使用以下命令：
show perimeter-traffic-filtering blocklist ip
查看静态IP黑名单冗余检查结果
查看静态IP黑名单冗余检查结果，在任意模式下，使用以下命令：
show perimeter-traffic-filtering blocklist-ip redundancy
查看动态IP黑名单
查看动态IP黑名单条目，在任意模式下，使用以下命令：
show block-ip [{ip | ipv6} ip-address]
l
{ip | ipv6} ip-address - 显示指定IP地址的动态IP黑名单条目。支持指定IPv4（ip）或IPv6（ipv6）
地址，仅当系统版本为IPv6版本时可指定IPv6地址。如不指定，则展示所有动态IP黑名单条目。
查看真实IP黑名单
查看真实IP黑名单条目，在任意模式下，使用以下命令：
show block-real-ip [{ip | ipv6} ip-address]

<!-- 来源页 497 -->
l
{ip | ipv6} ip-address - 显示指定IP地址的真实IP黑名单条目。支持指定IPv4（ip）或IPv6（ipv6）
地址，仅当系统版本为IPv6版本时可指定IPv6地址。如不指定，则展示所有真实IP黑名单条目。
查看黑名单库配置信息
查看黑名单库配置信息，在任意模式下，输入以下命令：
show perimeter-traffic-filtering blocklist lib
查看黑名单库自动更新配置信息
查看黑名单库自动更新配置信息，在任意模式下，输入以下命令：
show perimeter-traffic-filtering blocklist lib update
查看静态Service黑名单
查看静态Service黑名单条目，在任意模式下，使用以下命令：
show perimeter-traffic-filtering blocklist service
查看动态Service黑名单
查看动态Service黑名单条目，在任意模式下，使用以下命令：
show block-service [ip ip-address] [ipv6 ipv6-address] [vrouter vrouter-name]
查看MAC黑名单
查看MAC黑名单条目，在任意模式下，使用以下命令：
show perimeter-traffic-filtering blocklist mac
查看静态域名黑名单
查看静态域名黑名单条目，在任意模式下，使用以下命令：
show domain-control blocklist-domain
查看动态域名黑名单
查看动态域名黑名单条目，在任意模式下，使用以下命令：
show block-domain [domain domain-name]
查看域名白名单
查看域名白名单条目，在任意模式下，使用以下命令：
show domain-control allowlist-domain

<!-- 来源页 498 -->
查看静态URL黑名单
查看静态URL黑名单条目，在任意模式下，使用以下命令：
show url-control blocklist-url
查看动态URL黑名单
查看动态URL黑名单条目，在任意模式下，使用以下命令：
show block-url [url url-string]
查看URL白名单
查看URL白名单条目，在任意模式下，使用以下命令：
show url-control allowlist-url
