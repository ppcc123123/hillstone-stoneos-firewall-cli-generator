# 零信任网络访问(ZTNA)

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 13 零信任网络访问（ZTNA）
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 1764 -->
13 零信任网络访问（ZTNA）
介绍
相比于传统的VPN接入方式允许接入内网的终端访问任意资源，零信任网络访问（简称为ZTNA），是以不
信任企业边界内部和外部的任何实体为核心思想而提出的一种安全网络连接概念。只有对访问用户的身份、
使用的设备以及访问时间等其他环境属性进行验证后，ZTNA才会授予用户最小范围内的最可控的访问权
限，用户可以从任何地点、通过任何设备安全地访问云上和数据中心的私有应用。
ZTNA需要安装许可证使用，设备默认提供8个ZTNA并发用户授权（X系列所有型号和K系列
K20803/K9180默认128个）。不同型号的Hillstone设备支持的最大ZTNA并发用户数不同。如需增加授权
数量，请向代理商购买许可证。
ZTNA与SSL VPN共用Hillstone Secure Connect客户端，如需访问ZTNA服务，请下载和安装最新版本的
客户端，升级后的客户端支持ZTNA接入，也支持SSL VPN接入。目前，ZTNA远程访问解决方案支持
Windows、macOS、Linux、iOS、Android和国产操作系统终端接入，ZTNA内网接入解决方案支持
Windows、macOS、Linux和国产操作系统终端接入，接入时需登录相应的客户端，安装和使用方法请参
阅对应客户端。
ZTNA典型场景
ZTNA的典型应用场景主要包含远程访问及内网接入两种。
远程访问
随着移动办公的普及，远程访问内网资源的需求日益增长。为了满足这种需求，同时确保内网资源的安全，
Hillstone提供ZTNA远程访问方案。该方案支持基于远程用户身份、终端设备的状态、访问时间等维度对访
问流量进行管控，通过细粒度控制策略使之只能访问特定的授权应用，并持续监控终端状态变化，灵活调整
用户可访问的授权应用范围。
ZTNA远程访问方案的用户登录流程如下：

<!-- 来源页 1765 -->
1. ZTNA用户在客户端输入服务器地址、端口、认证方式（用户名/密码、用户名/密码+数字证书、仅数字证书和第
三方应用登录）等，请求验证。如果配置了二次认证，则需要完成二次认证。
2. 认证通过后，服务端向客户端下发终端信息收集的命令，为客户端分配私网IP，服务端和客户端建立安全隧道。
3. 客户端执行命令，收集主机信息，例如操作系统版本、是否安装防火墙、防病毒软件、IE浏览器安全级别、是否
运行某些进程等等，并上报给服务端。
4. 服务端解析主机信息，获取终端标签，将用户名和终端标签发送给认证模块，请求创建认证用户。
5. 认证模块创建认证用户，关联终端标签，获取用户组信息。
6. 服务端根据用户名、用户组和终端标签等信息匹配ZTNA策略，确定允许客户端访问的应用资源列表。
7. ZTNA客户端弹出Portal页面，展示用户有权限和无权限访问的应用资源，并展示应用资源名称和URL地址。
内网接入
传统的网络安全观念认为企业内网一般是安全的，安全威胁主要来自外界。但是，许多重大安全威胁往往发
生在内网中，例如内网员工在上网过程中可能无意间下载恶意软件，给整个内网带来严重安全风险。此外，
内网中的非法接入和非授权访问，可能导致业务受损和信息泄露。针对该问题，Hillstone提供ZTNA内网接
入方案。该方案支持基于内网用户身份、终端设备的状态、访问时间等维度对访问流量进行管控，通过细粒
度控制策略使之只能访问特定的授权应用，并持续监控终端状态变化，灵活调整用户可访问的授权应用范
围。
与远程访问方案相比，ZTNA内网接入方案中设备不用进行流量的加密和解密，因此无需建立隧道。ZTNA内
网接入方案的用户登录流程如下：
1. ZTNA用户在客户端输入服务器地址、端口、认证方式（用户名/密码、用户名/密码+数字证书、仅数字证书和第
三方应用登录）等，请求验证。如果配置了二次认证，则需要完成二次认证。
2. 认证通过后，服务端向客户端下发终端信息收集的命令。
3. 客户端执行命令，收集主机信息，例如操作系统版本、是否安装防火墙、防病毒软件、IE浏览器安全级别、是否
运行某些进程等等，并上报给服务端。
4. 服务端解析主机信息，获取终端标签，将用户名和终端标签发送给认证模块，请求创建认证用户。
5. 认证模块创建认证用户，关联终端标签，获取用户组信息。

<!-- 来源页 1766 -->
6. 服务端根据用户名、用户组和终端标签等信息匹配ZTNA策略，确定允许客户端访问的应用资源列表。
7. ZTNA客户端弹出Portal页面，展示用户有权限和无权限访问的应用资源，并展示应用资源名称和URL地址。

<!-- 来源页 1767 -->
ZTNA服务端配置
ZTNA在CLI的配置包含：
l "配置应用资源/应用资源组" 在第1802页
l "配置终端信息项" 在第1770页
l "管理终端标签日志" 在第1908页
l "终端标签配置" 在第1765页
l "配置接入地址池" 在第1491页
l "配置ZTNA策略" 在第1817页
l "ZTNA实例配置" 在第1841页
l "配置二次认证功能" 在第1876页
l "配置单包授权（SPA）" 在第1906页
l "查看ZTNA信息" 在第1910页
终端标签
介绍
终端标签用于标识用户的终端状态信息，系统会根据用户携带的终端信息为其打上相应的终端标签，这些标
签会被用作策略（包括安全策略和ZTNA策略）的匹配条件。带有特定标签的用户只能获取指定资源的访问
权限，从而实现对用户访问权限的检查和控制。
终端标签由一个或多个条件组构成，条件组由一个或多个条件构成。每条终端标签最多可以包含16个条件组
和最多16个条件。系统支持配置最多1024个终端标签，每个VSYS不超过128个。
l 条件组之间是逻辑“或”关系，用户携带的终端标签匹配终端标签中的任意一个条件组，即认为是匹配了这条终
端标签。
l 每个条件组内的各个条件之间是逻辑“与”关系，用户携带的终端标签同时匹配了某一条件组中的所有条件，才
认为是匹配了这个条件组。
此外，系统提供了一个预定义的终端标签“UNKNOWN-DEVICE”，该终端标签仅适用于防火墙与智铠
（EDR）联动管控场景，用于标识未能匹配任何自定义终端标签的终端设备。
终端标签配置
终端标签配置包括：

<!-- 来源页 1768 -->
l 创建终端标签
l 配置条件组
l 配置条件
l 配置提示信息
l 配置中英文提示信息
创建终端标签
创建一个终端标签并进入该终端标签的配置模式，在全局配置模式下，使用以下命令：
endpoint-tag tag-name [id]
l
tag-name - 指定终端标签名称，取值范围为1至95个字符。如果指定的名称已存在，将进入该终端标
签的配置模式。同一个VSYS中终端标签名称不能重复，不同VSYS中终端标签名称可以相同。
l
id - 指定终端标签ID，取值范围为1至128。如不指定，系统将为该终端标签生成一个ID。同一个VSYS
中终端标签ID不能重复，不同VSYS中终端标签ID可以相同。
在全局配置模式下，使用以下命令可以删除指定的终端标签：
no endpoint-tag tag-name
修改终端标签的名称，在终端标签配置模式下，使用以下命令：
name tag-name
l
tag-name - 指定终端标签的新名称，取值范围为1至95个字符。
配置终端标签的描述信息，在终端标签配置模式下，使用以下命令：
description description
l
description - 指定终端标签的描述信息，取值范围为1至255个字符。
在终端标签配置模式下，使用以下命令可以删除终端标签的描述信息：
no description
配置条件组
配置终端标签的条件组并进入条件组配置模式，在终端标签配置模式下，使用以下命令：
criteria-set[ id]
l
id - 指定终端标签条件组ID，取值范围为1至16。如不指定，系统将为该条件组生成一个ID。如果指定
的ID已存在，将直接进入该条件组的配置模式。

<!-- 来源页 1769 -->
在终端标签配置模式下，使用以下命令可以删除指定的终端标签条件组：
no criteria-set id
配置条件
终端标签的条件由两部分组成：
l
操作系统类型，支持Windows、macOS、Linux、国产操作系统、iOS、Android、HarmonyOS
PC、HarmonyOS Mobile(5.0+)。
l
终端状态，是一个由“key-name operator key-value”组成的字符串。
配置终端标签的条件，在终端标签条件组配置模式下，使用以下命令：
criteria [id ] os-type {windows | macOS | Linux | iOS | Android | ChineseOS| HarmonyOS-PC |
HarmonyOS-Mobile} key key-name operator key-value
l
id - 指定终端标签的条件ID，取值范围为1至16。如不指定，系统将为该条件生成一个ID。
l
os-type {windows | macOS | Linux | iOS | Android | ChineseOS | HarmonyOS-PC |
HarmonyOS-Mobile} - 指定终端的操作系统类型。
l
key key-name operator key-value- 指定需要匹配的终端信息项和对应的取值。key-name表示终
端信息项的名称；operator表示关系运算符；key-value表示终端信息项的取值。示例：key iesecurity-level >= low。关于系统支持的终端信息项和取值的详细信息，参考管理终端信息项。
注意: 对于Windows和Linux操作系统类型，部分终端信息项由智铠（EDR）平台提供，这些
信息需要与智铠平台联动才能生效，即设备必须与智铠平台建立稳定的通信连接，才能使配置
了这些信息的终端标签生效。设备如何与智铠平台建立通信连接，详见"连接智铠（EDR）" 在
第845页。
在终端标签条件组配置模式下，使用以下命令可以删除指定的终端标签条件：
no criteria id
配置提示信息
对于因为不匹配终端标签而无权限访问的应用资源，用户可以配置提示信息展示在ZTNA Portal上，使终端
用户了解不能访问的原因，从而通过更新自己的终端配置来获得访问应用资源的权限。默认的提示信息是
“无法访问！请联系IT管理员！”。
当一条ZTNA策略绑定多个终端标签时：

<!-- 来源页 1770 -->
l
如果用户匹配任意一个终端标签且具有应用资源的访问权限，ZTNA Portal上对应应用资源将不展示任
何提示信息。
l
如果用户因为不匹配任意一个终端标签而无法访问应用资源，ZTNA Portal上对应应用资源将汇总展示
所有终端标签的提示信息。如果所有终端标签都未配置提示信息，则展示默认提示信息。
为终端标签配置不匹配时的提示信息，在终端标签配置模式下，使用以下命令：
tips message
l
message - 指定需要展示的提示信息，取值范围是1到511个字符。提示信息中支持包含URL地址，展
示在ZTNA Portal上时将显示为超链接。
删除提示信息配置，在终端标签配置模式下，使用以下命令：
no tips
配置中英文提示信息
对于因为不匹配终端标签而无权限访问的应用资源，用户可自定义ZTNA Portal的中英文提示信息。配置完
成后，当用户终端环境不满足终端标签规则要求时，ZTNA Portal页面将根据浏览器语言设置自动匹配并显
示对应语言的提示内容。若未配置中英文提示信息，则默认显示提示信息的配置内容。
注意:
l
仅当设备的系统语言为中文时，支持配置该选项。
l
如果浏览器语言既不是中文也不是英文，ZTNA Portal页面将默认显示英文的应用资源名称。
配置中英文提示信息，在终端标签配置模式下，使用以下命令：
{zh-cn-tips | en-tips} message
l
zh-cn-tips - 配置中文提示信息。
l
en-tips - 配置英文提示信息。
l
message - 输入对应语言的具体提示内容，取值范围是1到511个字符。提示信息中支持包含URL地
址，展示在ZTNA Portal上时将显示为超链接。
删除中英文提示信息配置，在终端标签配置模式下，使用以下命令：
no {zh-cn-tips | en-tips}
查看终端标签配置信息
查看指定终端标签的配置信息和ZTNA策略引用次数，在任意模式下，使用以下命令：

<!-- 来源页 1771 -->
show endpoint-tag name tag-name
l
tag-name - 指定终端标签的名称。
查看符合指定过滤条件的终端标签配置信息、ZTNA策略引用次数和命中计数，在任意模式下，使用以下命
令：
show endpoint-tag filter {name tag-name | description description}
l
name tag-name - 查看指定名称的终端标签配置信息、ZTNA策略引用次数和命中计数。
l
description description - 查看配置有指定描述信息的终端标签配置信息、ZTNA策略引用次数和命中
计数。
查看所有终端标签配置信息、ZTNA策略引用次数和命中计数，在任意模式下，使用以下命令：
show endpoint-tag
管理终端信息项
介绍
终端信息项是零信任网络访问（ZTNA）架构的核心要素，由ZTNA客户端从终端设备收集关键属性数据，作
为防火墙执行终端标签规则判断的依据。管理员可在终端标签规则中灵活引用终端信息项作为判断条件，并
通过将终端标签与访问控制策略相关联，最终实现基于终端安全状态的精细化访问控制。
系统提供以下两类终端信息项：
l 预定义信息项：系统内置丰富多样的终端信息项（如操作系统版本、已安装软件、终端风险等级等），开箱即用
且不支持编辑，保障基础数据收集的稳定与可靠，为ZTNA通用安全校验提供标准化数据支撑。
l 自定义信息项：用户可根据业务需求，灵活添加需要收集的自定义信息项（每种最多可添加5条），例如通过指
定特定文件、注册表项等收集内容，实现深度定制化的数据采集，为精细化权限控制提供数据支撑。
基于终端信息项的访问控制策略配置流程如下图所示：

<!-- 来源页 1772 -->
终端信息项管理实现终端信息采集配置、终端信息收集脚本的生成和下发，以及终端状态的持续性监控。在
客户端登录成功后和访问应用资源期间，服务端会持续监控终端状态，并根据终端信息的变化，调整用户允
许访问的应用资源范围，其工作流程如下：
1. 信息采集与上报：ZTNA客户端根据终端信息收集脚本，定期收集终端上的预定义和自定义信息项，并上报给服
务端。客户端默认每20分钟收集和上报一次终端信息，管理员可根据需求，通过endpoint-informationmonitor命令自行调整该上报周期。
2. 策略重匹配：服务端解析终端信息，若发现关键信息项发生变更，则立即根据最新获取的终端信息项，重新匹配
访问控制策略，调整用户允许访问的应用资源范围，并根据session-rematch命令的配置，对该用户的已有会话
进行处理，确保ZTNA访问策略立即生效。
配置终端信息项
系统支持以下操作系统的终端信息管理：
l Windows终端信息管理
l macOS终端信息管理
l Linux终端信息管理
l iOS终端信息管理
l Android终端信息管理
l ChineseOS终端信息管理
l HarmonyOS PC终端信息管理
l HarmonyOS Mobile(5.0+)终端信息管理
Windows终端信息管理
注意: Windows终端信息项中，下列使用*号标识的终端信息项由智铠（EDR）平台提供，这些信
息需要与智铠平台联动才能生效，即设备必须与智铠平台建立稳定的通信连接，才能使配置了这些
信息的终端标签生效。设备如何与智铠平台建立通信连接，详见"连接智铠（EDR）" 在第845页。
系统内置的预定义Windows终端信息项如下表所示。
预定义Windows终端信息项
终端信息项名称
详细描述
关系运算符
取值
os-version
Windows终端的操作系统
版本
is、is-not
windows-7/8.1/10/11；
windows-server-2008-

<!-- 来源页 1773 -->
预定义Windows终端信息项
终端信息项名称
详细描述
关系运算符
取值
R2/2012/2012-
R2/2016/2019/2022
anti-virus
Windows终端防病毒软件
状态（安装/运行/更新）
is、is-not
installed、enabled、
updated
firewall
Windows终端防火墙状态
（安装/运行）
is、is-not
installed、enabled
anti-spyware
Windows终端反间谍软件
状态（安装/运行/更新）
is、is-not
installed、enabled、
updated
windows-update
Windows更新服务状态
is、is-not
enabled
ie-version
Windows终端上安装的IE
浏览器版本
=、!=、>、<、>=、<=
IE7 ~ IE11
ie-security-level
Windows终端上IE浏览器
的安全级别
=、!=、>、<、>=、<=
custom-define、low、
medium-low、medium、
medium-high、high
non-allowlistedsoftware
Windows终端中非白名单
软件的安装信息
is、is-not
exist
risk-level
Windows终端的风险等级
=、!=、>、<、>=、<=
normal、low、medium、
high、critical
edr-agent-status
Windows终端上智铠
（EDR）客户端的在线状
态
is、is-not
online
edr-user-bindingstatus
Windows终端上智铠
（EDR）与用户账号的绑
定状态
is、is-not
bound
wlan-autoconfig*
WLAN AutoConfig服务
（无线网络自动配置服
务）的启用状态
is、is-not
enabled
remote-desktopservice*
Windows远程桌面服务的
启用状态
is、is-not
enabled
server*
Windows文件共享服务
（Server服务）的启用状
态
is、is-not
enabled
print-spooler-service*
Windows打印后台处理程
序（Print Spooler服务）
的启用状态
is、is-not
enabled

<!-- 来源页 1774 -->
预定义Windows终端信息项
终端信息项名称
详细描述
关系运算符
取值
remote-managementservice*
Windows远程管理服务的
启用状态
is、is-not
enabled
remote-registryservice*
Windows远程注册表服务
的启用状态
is、is-not
enabled
default-sharing*
Windows文件夹默认共享
功能的启用状态
is、is-not
enabled
auto-login*
检查Windows终端是否启
用了账号自动登录功能
is、is-not
enabled
clone-account *
Windows终端内的克隆账
户
is、is-not
exist
guest-account*
Guest来宾账户功能的启
用状态
is、is-not
enabled
weak-pwd*
Windows终端内的弱密码
is、is-not
exist
telnet-service*
Telnet服务的启用状态
is、is-not
enabled
系统支持对如下表格所示的自定义Windows信息项进行配置，以用于终端信息采集和终端标签规则引用。
自定义Windows终端信息项
终端信息项名称
详细描述
关系运算符
取值
process
Windows终端中指定
进程的运行状态
exist、not-exist
指定的进程的别名
service-installed
Windows终端中指定
服务的安装状态
exist、not-exist
指定的服务的别名
service-running
Windows终端中指定
服务的运行状态
exist、not-exist
指定的服务的别名
registry-key
Windows终端内指定
注册表项的存在状态
exist、not-exist
指定的注册表项的别名
file
Windows终端内指定
文件的存在状态
exist、not-exist
指定的文件的别名
hotfix
Windows终端内指定
热补丁包的安装信息
exist、not-exist
指定的热补丁包的别名
edr-agent-version
Windows终端上安装
的智铠（EDR）客户端
版本
=、!=、>、<、>=、<=
指定的EDR客户端版本的别名
hostname
Windows终端所使用
的主机名称的匹配状
is、is-not、contain、notcontain
指定的主机的别名

<!-- 来源页 1775 -->
自定义Windows终端信息项
终端信息项名称
详细描述
关系运算符
取值
态
mac
Windows终端所在
MAC地址的匹配状态
is、is-not、contain、notcontain
指定的MAC地址的别名
group*
Windows终端所属分
组的匹配状态
is、is-not
指定的终端所属分组的别名
ad-domain
Windows终端所属AD
域的匹配状态
is、is-not
指定的AD域名的别名
进入自定义Windows终端信息项配置模式
配置自定义Windows终端信息项，需在全局配置模式下，使用以下命令进入endpoint-informationwindows-profile配置模式：
endpoint-information-windows-profile
自定义注册表项作为Windows终端信息项
用户可以配置防火墙检查Windows终端是否存在指定的注册表项。
自定义需要收集的注册表项信息，在endpoint-information-windows-profile配置模式下，使用以下命
令：
registry-key alias alias-name value registry-key-name
l
alias alias-name - 指定注册表项的别名，取值范围为1至31个字符。
l
value registry-key-name - 指定注册表项的名称，取值范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的注册表项信息。
在endpoint-information-windows-profile配置模式下，使用以下命令可以删除指定的注册表信息项配
置：
no registry-key alias alias-name
自定义运行进程作为Windows终端信息项
用户可以配置防火墙检查Windows终端是否正在运行指定的进程。
自定义需要收集的运行进程信息，在endpoint-information-windows-profile配置模式下，使用以下命
令：
process alias alias-name value process-name

<!-- 来源页 1776 -->
l
alias alias-name - 指定进程的别名，范围为1至31个字符。
l
value process-name - 指定进程的实际名称，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的运行进程信息。
在endpoint-information-windows-profile配置模式下，使用以下命令可以删除指定的运行进程信息项
配置：
no process alias alias-name
自定义运行服务作为Windows终端信息项
用户可以配置防火墙检查Windows终端是否正在运行指定的服务。
自定义需要收集的运行服务信息，在endpoint-information-windows-profile配置模式下，使用以下命
令：
service-running alias alias-name value service-name
l
alias alias-name - 指定服务的别名，范围为1至31个字符。
l
value service-name - 指定服务的实际名称，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的运行服务信息。
在endpoint-information-windows-profile配置模式下，使用以下命令可以删除指定的运行服务信息项
配置：
no service-running alias alias-name
自定义已安装服务作为Windows终端信息项
用户可以配置防火墙检查Windows终端是否安装了指定的服务。
自定义需要收集的已安装服务信息，在endpoint-information-windows-profile配置模式下，使用以下
命令：
service-installed alias alias-name value service-name
l
alias alias-name - 指定服务的别名，范围为1至31个字符。
l
value service-name - 指定服务的实际名称，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的已安装服务信息。
在endpoint-information-windows-profile配置模式下，使用以下命令可以删除指定的已安装服务信息
项配置：
no service-installed alias alias-name

<!-- 来源页 1777 -->
自定义文件作为Windows终端信息项
用户可以配置防火墙检查Windows终端是否存在指定的文件。
自定义需要收集的文件信息，在endpoint-information-windows-profile配置模式下，使用以下命令：
file alias alias-name value file-name
l
alias alias-name - 指定文件的别名，范围为1至31个字符。
l
value file-name - 指定文件的绝对路径，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的文件信息。
在endpoint-information-windows-profile配置模式下，使用以下命令可以删除指定的文件信息项配
置：
no file alias alias-name
自定义已安装热补丁包作为Windows终端信息项
用户可以配置防火墙检查Windows终端是否安装了指定的热补丁包。
自定义需要收集的已安装热补丁包信息，在endpoint-information-windows-profile配置模式下，使用
以下命令：
hotfix alias alias-name value hot-patch-name
l
alias alias-name - 指定热补丁包的别名，范围为1至31个字符。
l
value hot-patch-name - 指定热补丁包的实际名称，长度1至255个字符。
重复该命令可以自定义最多5条需要收集的已安装热补丁包信息。
在endpoint-information-windows-profile配置模式下，使用以下命令可以删除指定的已安装热补丁包
信息项配置：
no hotfix alias alias-name
自定义EDR客户端版本作为Windows终端信息项
用户可以配置EDR客户端版本作为Windows终端信息项，ZTNA客户端会定期收集并上报EDR客户端版本信
息给防火墙端，防火墙端来检查Windows终端是否安装了指定的EDR客户端版本，根据检查结果更新终端
标签以及终端允许访问的应用资源。
自定义需要收集的EDR客户端版本信息，在endpoint-information-windows-profile配置模式下，使用
以下命令：
edr-agent-version alias alias-name value edr-agent-version-name

<!-- 来源页 1778 -->
l
alias alias-name - 指定EDR客户端版本的别名，范围为1至31个字符。
l
value edr-agent-version-name - 指定EDR客户端的实际版本号，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的EDR客户端版本信息。
在endpoint-information-windows-profile配置模式下，使用以下命令可以删除指定的EDR客户端版本
信息项配置：
no edr-agent-version alias alias-name
自定义主机名作为Windows终端信息项
用户可以配置防火墙检查Windows终端所使用的主机名称是否与指定的主机名称一致。
自定义需要收集的主机名称信息，在endpoint-information-windows-profile配置模式下，使用以下命
令：
hostname alias alias-name value hostname
l
alias-name - 指定主机的别名，范围是1至31个字符。
l
hostname - 指定主机的实际名称，范围是1至255个字符。
重复该命令可以自定义最多5个需要收集的主机名信息。
在endpoint-information-windows-profile配置模式下，使用以下命令可以删除指定的主机名信息项配
置：
no hostname alias alias-name
自定义终端所属分组作为Windows终端信息项
用户可以配置防火墙检查Windows终端所属的分组是否与指定的终端所属分组一致。
自定义需要收集的终端所属分组信息，在endpoint-information-windows-profile配置模式下，使用以
下命令：
group alias alias-name value group-name
l
alias-name - 指定终端所属分组的别名，范围是1至31个字符。
l
group-name - 指定终端所属分组的实际名称，范围是1至255个字符。
重复该命令可以自定义最多5条需要收集的终端所属分组信息。
在endpoint-information-windows-profile配置模式下，使用以下命令可以删除指定的终端所属分组信
息项配置：
no group alias alias-name

<!-- 来源页 1779 -->
自定义MAC地址作为Windows终端信息项
用户可以配置防火墙检查Windows终端所在的MAC地址与指定的MAC地址是否一致。
自定义需要收集的MAC地址信息，在endpoint-information-windows-profile配置模式下，使用以下命
令：
mac alias alias-name value mac-address
l
alias-name - 指定终端MAC地址的别名，范围是1至31个字符。
l
mac-address - 指定输入终端实际的MAC地址。
重复该命令可以自定义最多5个需要收集的MAC地址信息。
在endpoint-information-windows-profile配置模式下，使用以下命令可以删除指定的MAC地址信息项
配置：
no mac alias alias-name
配置AD域名作为Windows终端信息采集项
用户可根据需求，配置终端所属AD域的域名作为Windows终端信息采集项。
配置AD域名，在ztna-endpoint-information-windows-profile配置模式下，使用以下命令：
ad-domain alias alias-name value domain-name
l
alias alias-name - 指定AD域名的别名，取值范围为1至31个字符。
l
value domain-name - 指定AD域名，取值范围为1至255个字符，且不区分大小写。
重复该命令，可以自定义添加最多5条AD域名配置。
在ztna-endpoint-information-windows-profile配置模式下，使用以下命令可以删除指定的AD域名信
息项配置：
no ad-domain alias alias-name
查看Windows终端信息项配置
查看系统支持的预定义和自定义Windows终端信息项，在任意模式下，使用以下命令：
show endpoint-information-windows-profile
查看指定的Windows终端信息项配置信息，在任意模式下，使用以下命令：
show endpoint-information-windows-profile key-name
l
key-name - 指定Windows终端信息项的名称，支持预定义和自定义项。

<!-- 来源页 1780 -->
macOS终端信息管理
系统内置的预定义macOS终端信息项如下表所示。
预定义macOS终端信息项
终端信息项名称
详细描述
关系运算符
取值
os-version
macOS终端的操作系统
版本
is、is-not
10.13/10.14/10.15/11/12/13
filevault
macOS终端上FileVault
功能的启用状态
is、is-not
enabled
non-allowlistedsoftware
macOS终端中非白名单
软件的安装信息
is、is-not
exist
risk-level
macOS终端的风险等级
=、!=、>、<、>=、<=
normal、low、medium、
high、critical
edr-agent-status
macOS终端上智铠
（EDR）客户端的在线
状态
is、is-not
online
edr-user-bindingstatus
macOS终端上智铠
（EDR）与用户账号的
绑定状态
is、is-not
bound
系统支持对如下表格所示的自定义macOS终端信息项进行配置，以用于终端信息采集和终端标签规则引用。
自定义macOS终端信息项
终端信息项名称
详细描述
关系运算符
取值
ad-domain
macOS终端所属AD域的匹
配状态
is、is-not
指定的AD域名的别名
process
macOS终端中指定进程的
运行状态
exist、not-exist
指定的进程的别名
service-running
macOS终端中指定服务的
运行状态
exist、not-exist
指定的服务的别名
service-installed
macOS终端中指定服务的
安装状态
exist、not-exist
指定的服务的别名
file
macOS终端内指定文件的
存在状态
exist、not-exist
指定的文件的别名
edr-agent-version
macOS终端上安装的智铠
（EDR）客户端版本
=、!=、>、<、>=、<=
指定的EDR客户端版本的别
名

<!-- 来源页 1781 -->
进入自定义macOS终端信息项配置模式
配置自定义Android终端信息项，需在全局配置模式下，使用以下命令进入endpoint-informationmacos-profile配置模式：
endpoint-information-macos-profile
配置AD域名作为macOS终端信息项
用户可根据需求，配置终端所属AD域的域名作为macOS终端信息采集项。
配置AD域名，在endpoint-information-macos-profile配置模式下，使用以下命令：
ad-domain alias alias-name value domain-name
l
alias alias-name - 指定AD域名的别名，取值范围为1至31个字符。
l
value domain-name - 指定AD域名，取值范围为1至255个字符。，且不区分大小写
重复该命令，可以自定义添加最多5条需要收集的AD域名信息。
在endpoint-information-macos-profile配置模式下，使用以下命令可以删除指定的AD域名信息项配
置：
no ad-domain alias alias-name
自定义运行进程作为macOS终端信息项
用户可以配置防火墙检查macOS终端是否正在运行指定的进程。
自定义需要收集的运行进程信息，在endpoint-information-macos-profile配置模式下，使用以下命
令：
process alias alias-name value process-name
l
alias alias-name - 指定进程的别名，范围为1至31个字符。
l
value process-name - 指定进程的实际名称，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的运行进程信息。
在endpoint-information-macos-profile配置模式下，使用以下命令可以删除指定的运行进程信息项配
置：
no process alias alias-name
自定义运行服务作为macOS终端信息项
用户可以配置防火墙检查macOS终端是否正在运行指定的服务。

<!-- 来源页 1782 -->
自定义需要收集的运行服务信息，在endpoint-information-macos-profile配置模式下，使用以下命
令：
service-running alias alias-name value service-name
l
aliasalias-name - 指定服务的别名，范围为1至31个字符。
l
value service-name - 指定服务的实际名称，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的运行服务信息。
在endpoint-information-macos-profile配置模式下，使用以下命令可以删除指定的运行服务信息项配
置：
no service-running alias alias-name
自定义已安装服务作为macOS终端信息项
用户可以配置防火墙检查macOS终端是否安装了指定的服务。
自定义需要收集的已安装服务信息，在endpoint-information-macos-profile配置模式下，使用以下命
令：
service-installed alias alias-name value service-name
l
alias alias-name - 指定服务的别名，范围为1至31个字符。
l
value service-name - 指定服务的实际名称，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的已安装服务信息。
在endpoint-information-macos-profile配置模式下，使用以下命令可以删除指定的已安装服务信息项
配置：
no service-installed alias alias-name
自定义文件作为macOS终端信息项
用户可以配置防火墙检查macOS终端是否存在指定的文件。
自定义需要收集的文件信息，在endpoint-information-macos-profile配置模式下，使用以下命令：
file alias alias-name value file-name
l
alias alias-name - 指定文件的别名，范围为1至31个字符。
l
value file-name - 指定文件的绝对路径，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的文件信息。

<!-- 来源页 1783 -->
在endpoint-information-macos-profile配置模式下，使用以下命令可以删除指定的文件信息项配置：
no file alias alias-name
自定义EDR客户端版本作为macOS终端信息项
用户可以配置EDR客户端版本作为macOS终端信息项，ZTNA客户端会定期收集并上报EDR客户端版本信息
给防火墙端，防火墙端来检查macOS终端是否安装了指定的EDR客户端版本，根据检查结果更新终端标签以
及终端允许访问的应用资源。
自定义需要收集的EDR客户端版本信息，在endpoint-information-macos-profile配置模式下，使用以
下命令：
edr-agent-version alias alias-name value edr-agent-version-name
l
alias alias-name - 指定EDR客户端版本的别名，范围为1至31个字符。
l
value edr-agent-version-name - 指定EDR客户端的实际版本号，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的EDR客户端版本信息。
在endpoint-information-macos-profile配置模式下，使用以下命令可以删除指定的EDR客户端版本信
息项配置：
no edr-agent-version alias alias-name
查看macOS终端信息项配置
查看系统支持的预定义和自定义macOS终端信息项，在任意模式下，使用以下命令：
show endpoint-information-macos-profile
查看指定的macOS终端信息项配置信息，在任意模式下，使用以下命令：
show endpoint-information-macos-profile key-name
l
key-name - 指定macOS终端信息项的名称，支持预定义和自定义项。
Linux终端信息管理
注意: Linux终端信息项中，下列使用*号标识的终端信息项由智铠（EDR）平台提供，这些信息需
要与智铠平台联动才能生效，即设备必须与智铠平台建立稳定的通信连接，才能使配置了这些信息
的终端标签生效。设备如何与智铠平台建立通信连接，详见"连接智铠（EDR）" 在第845页。
系统内置的预定义Linux终端信息项如下表所示。

<!-- 来源页 1784 -->
预定义Linux终端信息项
终端信息项名称
详细描述
关系运算符
取值
os-version
Linux终端的操作系统版
本
is、is-not
CentOS
7.6/7.7/7.8/7.9/8.0
/8.1/8.2/8.3/8.4/8.5;
Ubuntu
18.04/18.10/19.04/19.10
/20.04/20.10/21.04;
Ubuntu Kylin 18.04/20.04
anti-virus*
Linux终端防病毒软件的
安装状态
is、is-not
installed
risk-level*
Linux终端的风险等级
=、!=、>、<、>=、<=
normal、low、medium、
high、critical
edr-agent-status*
Linux终端上智铠
（EDR）客户端的在线状
态
is、is-not
online、offline
weak-pwd*
Linux终端内的弱密码
is、is-not
exist
telnet-service*
Telnet服务的启用状态
is、is-not
enabled
super-user-otherthan-root*
Root之外的超级用户功能
的启用状态
is、is-not
enabled
only-wheel-usersu-to-root*
Linux系统只允许wheel
组用户使用su命令切换到
Root功能的启用状态
is、is-not
enabled
ftp-service*
FTP服务的启用状态
is、is-not
enabled
rlogin-service*
Linux远程登录服务
（rlogin服务）的启用状
态
is、is-not
enabled
smbd-service*
Linux文件打印和共享服
务（smbd服务）的启用
状态
is、is-not
enabled
ssh-use-non-22-
port *
Linux系统内使用非默认
22端口进行SSH连接
is、is-not
exist
ssh-disable-root*
Linux系统禁止root用户
通过SSH方式登录功能的
启用状态
is、is-not
enabled
ssh-disablepassword*
SSH关闭密码认证登录
（即SSH服务不允许使用
密码进行身份验证和登
is、is-not
enabled

<!-- 来源页 1785 -->
预定义Linux终端信息项
终端信息项名称
详细描述
关系运算符
取值
录）功能的启用状态
ssh-with-rsa*
SSH服务允许使用RSA认
证方式登录功能的启用状
态
is、is-not
enabled
ssh-permit-login*
SSH服务允许特定用户登
录功能的启用状态
is、is-not
enabled
ssh-permit-ip*
SSH服务允许特定IP登录
功能的启用状态
is、is-not
enabled
系统支持对如下表格所示的自定义Linux终端信息项进行配置，以用于终端信息采集和终端标签规则引用。
自定义Linux终端信息项
终端信息项名称
详细描述
关系运算符
取值
process
Linux终端中指定进程的运
行状态
exist、not-exist
指定的进程的别名
service-running
Linux终端中指定服务的运
行状态
exist、not-exist
指定的服务的别名
service-installed
Linux终端中指定服务的安
装状态
exist、not-exist
指定的服务的别名
file
Windows终端内指定文件
的存在状态
exist、not-exist
指定的文件的别名
hostname
Linux终端所使用的主机名
称的匹配状态
is、is-not、contain、
not-contain
指定的主机的别名
edr-agent-version
Linux终端上安装的智铠
（EDR）客户端版本
=、!=、>、<、>=、<=
指定的EDR客户端版本的别
名
mac
Linux终端所在MAC地址的
匹配状态
is、is-not、contain、
not-contain
指定的MAC地址的别名
group*
Linux终端所属分组的匹配
状态
is、is-not
指定的终端所属分组的别名
进入自定义Linux终端信息项配置模式
配置自定义Linux终端信息项，需在全局配置模式下，使用以下命令进入endpoint-information-linuxprofile配置模式：
endpoint-information-linux-profile

<!-- 来源页 1786 -->
自定义运行进程作为Linux终端信息项
用户可以配置防火墙检查Linux终端是否正在运行指定的进程。
自定义需要收集的运行进程信息，在endpoint-information-linux-profile配置模式下，使用以下命令：
process alias alias-name value process-name
l
alias alias-name - 指定进程的别名，范围为1至31个字符。
l
value process-name - 指定进程的实际名称，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的运行进程信息。
在endpoint-information-linux-profile配置模式下，使用以下命令可以删除指定的运行进程信息项配
置：
no process alias alias-name
自定义运行服务作为Linux终端信息项
用户可以配置防火墙检查Linux终端是否正在运行指定的服务。
自定义需要收集的运行服务信息，在endpoint-information-linuxs-profile配置模式下，使用以下命
令：
service-running alias alias-name value service-name
l
alias alias-name - 指定服务的别名，范围为1至31个字符。
l
value service-name - 指定服务的实际名称，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的运行服务信息。
在endpoint-information-linux-profile配置模式下，使用以下命令可以删除指定的运行服务信息项配
置：
no service-running alias alias-name
自定义已安装服务作为Linux终端信息项
用户可以配置防火墙检查Linux终端是否安装了指定的进程。
自定义需要收集的已安装服务信息，在endpoint-information-linux-profile配置模式下，使用以下命
令：
service-installed alias alias-name value service-name

<!-- 来源页 1787 -->
l
alias alias-name - 指定服务的别名，范围为1至31个字符。
l
value service-name - 指定服务的实际名称，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的已安装服务信息。
在endpoint-information-linux-profile配置模式下，使用以下命令可以删除指定的已安装服务信息项配
置：
no service-installed alias alias-name
自定义文件作为Linux终端信息项
用户可以配置防火墙检查Linux终端是否存在指定的文件。
自定义需要收集的文件信息，在endpoint-information-linux-profile配置模式下，使用以下命令：
file alias alias-name value file-name
l
alias alias-name - 指定文件的别名，范围为1至31个字符。
l
value file-name - 指定文件的绝对路径，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的文件信息。
在endpoint-information-linux-profile配置模式下，使用以下命令可以删除指定的文件信息项配置：
no file alias alias-name
自定义EDR客户端版本作为Linux终端信息项
用户可以配置EDR客户端版本作为Linux终端信息项，ZTNA客户端会定期收集并上报EDR客户端版本信息给
防火墙端，防火墙端来检查Linux终端是否安装了指定的EDR客户端版本，根据检查结果更新终端标签以及
终端允许访问的应用资源。
自定义需要收集的EDR客户端版本信息，在endpoint-information-linux-profile配置模式下，使用以下
命令：
edr-agent-version alias alias-name value edr-agent-version-name
l
alias alias-name - 指定EDR客户端版本的别名，范围为1至31个字符。
l
value edr-agent-version-name - 指定EDR客户端的实际版本号，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的EDR客户端版本信息。
在endpoint-information-linux-profile配置模式下，使用以下命令可以删除指定的EDR客户端版本信息
项配置：
no edr-agent-version alias alias-name

<!-- 来源页 1788 -->
自定义主机名作为Linux终端信息项
用户可以配置防火墙检查Linux终端所使用的主机名称是否与指定的主机名称一致。
自定义需要收集的主机名称信息，在endpoint-information-linux-profile配置模式下，使用以下命令：
hostname alias alias-name value hostname
l
alias-name - 指定主机的别名，范围是1至31个字符。
l
hostname - 指定主机的实际名称，范围是1至255个字符。
重复该命令可以自定义最多5个需要收集的主机名信息。
在endpoint-information-linux-profile配置模式下，使用以下命令可以删除指定的主机名信息项配置：
no hostname alias alias-name
自定义终端所属分组作为Linux终端信息项
用户可以配置防火墙检查Linux终端所属的分组是否与指定的终端所属分组一致。
自定义需要收集的终端所属分组信息，在endpoint-information-linux-profile配置模式下，使用以下命
令：
group alias alias-name value group-name
l
alias-name - 指定终端所属分组的别名，范围是1至31个字符。
l
group-name - 指定终端所属分组的实际名称，范围是1至255个字符。
重复该命令可以自定义最多5条需要收集的终端所属分组信息。
在endpoint-information-linux-profile配置模式下，使用以下命令可以删除指定的终端所属分组信息项
配置：
no group alias alias-name
自定义MAC地址作为Linux终端信息项
用户可以配置防火墙检查Linux终端所在的MAC地址与指定的MAC地址是否一致。
自定义需要收集的MAC地址信息，在endpoint-information-linux-profile配置模式下，使用以下命令：
mac alias alias-name value mac-address
l
alias-name - 指定终端MAC地址的别名，范围是1至31个字符。
l
mac-address - 指定输入终端实际的MAC地址。
重复该命令可以自定义最多5个需要收集的MAC地址信息。

<!-- 来源页 1789 -->
在endpoint-information-linux-profile配置模式下，使用以下命令可以删除指定的MAC地址信息项配
置：
no mac alias alias-name
查看Linux终端信息项配置
查看系统支持的预定义和自定义Linux终端信息项，在任意模式下，使用以下命令：
show endpoint-information-linux-profile
查看指定的Linux终端信息项配置信息，在任意模式下，使用以下命令：
show endpoint-information-linux-profile key-name
l
key-name - 指定Linux终端信息项的名称，支持预定义和自定义项。
iOS终端信息管理
系统内置的预定义iOS终端信息项如下表所示。
预定义iOS终端信息项
终端信息项名称
详细描述
关系运算符
取值
os-version
iOS终端的操作系统版本
is、is-not
iOS 12/13/14/15/16
系统支持对如下表格所示的自定义iOS终端信息项进行配置，以用于终端信息采集和终端标签规则引用。
自定义iOS终端信息项
终端信息项名称
详细描述
关系运算符
取值
device-model
iOS终端的设备型号
is、is-not
指定的设备型号的别名
wifi-ssid
iOS终端所连接的WiFi的
SSID
is、is-not
指定的WiFi SSID的别名
client-version
iOS终端使用的ZTNA客户
端版本
is、is-not
指定的ZTNA客户端版本的别
名
进入自定义iOS终端信息项配置模式
配置自定义iOS终端信息项，需在全局配置模式下，使用以下命令进入endpoint-information-iosprofile配置模式：
endpoint-information-ios-profile
自定义设备型号作为iOS终端信息项
用户可以配置防火墙检查iOS终端的设备型号。

<!-- 来源页 1790 -->
自定义需要收集的iOS终端设备型号信息，在endpoint-information-ios-profile配置模式下，使用以下
命令：
device-model alias alias-name value device-model-number
l
alias alias-name - 指定iOS终端设备型号的别名，取值范围为1至31个字符。
l
value device-model-number - 指定iOS终端设备的型号，取值范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的iOS终端设备型号信息。
在endpoint-information-ios-profile配置模式下，使用以下命令可以删除指定的iOS终端设备型号信息
项配置：
no device-model alias alias-name
自定义WiFi SSID作为iOS终端信息项
用户可以配置防火墙检查iOS终端连接的WiFi SSID。
自定义需要收集的WiFi SSID信息，在endpoint-information-ios-profile配置模式下，使用以下命令：
wifi-ssid alias alias-name value wifi-ssid
l
alias alias-name - 指定iOS终端设备使用的WiFi SSID的别名，取值范围为1至31个字符。
l
value wifi-ssid - 指定WiFi SSID，取值范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的WiFi SSID信息。
在endpoint-information-ios-profile配置模式下，使用以下命令可以删除指定的WiFi SSID信息项配
置：
no wifi-ssid alias alias-name
自定义ZTNA客户端版本作为iOS终端信息项
用户可以配置防火墙检查iOS终端使用的ZTNA客户端版本。
自定义需要收集的ZTNA客户端版本信息，在endpoint-information-ios-profile配置模式下，使用以下
命令：
client-version alias alias-name value client-version
l
client-version alias alias-name - 指定ZTNA客户端版本的别名，取值范围为1至31个字符。
l
value client-version - 指定ZTNA客户端版本，取值范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的ZTNA客户端版本信息。

<!-- 来源页 1791 -->
在endpoint-information-ios-profile配置模式下，使用以下命令可以删除指定的ZTNA客户端版本信息
项配置：
no client-version alias alias-name
查看iOS终端信息项配置
查看系统支持的预定义和自定义iOS终端信息项，在任意模式下，使用以下命令：
show endpoint-information-ios-profile
查看指定的iOS终端信息项配置信息，在任意模式下，使用以下命令：
show endpoint-information-ios-profile key-name
l
key-name - 指定iOS终端信息项的名称，支持预定义和自定义项。
Android终端信息管理
系统内置的预定义Android终端信息项如下表所示。
预定义Android终端信息项
终端信息项名称
详细描述
关系运算符
取值
os-version
检查Android终端的操作
系统版本
is、is-not
Android 8/9/10/11/12/13
系统支持对如下表格所示的自定义Android终端信息项进行配置，以用于终端信息采集和终端标签规则引
用。
自定义Android终端信息项
终端信息项名称
详细描述
关系运算符
取值
device-model
Android终端的设备型号
is、is-not
指定的设备型号的别名
wifi-ssid
Android终端所连接的Wifi
SSID
is、is-not
指定的Wifi SSID的别名
client-version
Android终端使用的ZTNA
客户端版本
is、is-not
指定的ZTNA客户端版本的别
名
进入自定义Android终端信息项配置模式
配置自定义Android终端信息项，需在全局配置模式下，使用以下命令进入endpoint-informationandroid-profile配置模式：
endpoint-information-android-profile

<!-- 来源页 1792 -->
自定义设备型号作为Android终端信息项
用户可以配置防火墙检查Android终端的设备型号。
自定义需要收集的Android终端设备型号信息，在endpoint-information-android-profile配置模式
下，使用以下命令：
device-model alias alias-name value device-model-number
l
alias alias-name - 指定Android终端设备型号的别名，取值范围为1至31个字符。
l
value device-model-number - 指定Android终端设备的型号，取值范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的Android终端设备型号信息。
在endpoint-information-android-profile配置模式下，使用以下命令可以删除指定的Android终端设
备型号信息项配置：
no device-model alias alias-name
自定义WiFi名称作为Android终端信息项
用户可以配置防火墙检查Android终端连接的WiFi SSID。
自定义需要收集的WiFi SSID信息，在endpoint-information-android-profile配置模式下，使用以下命
令：
wifi-ssid alias alias-name value wifi-ssid
l
alias alias-name - 指定WiFi SSID的别名，取值范围为1至31个字符。
l
value wifi-ssid - 指定WiFi SSID，取值范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的WiFi SSID信息。
在endpoint-information-android-profile配置模式下，使用以下命令可以删除指定的WiFi SSID信息项
配置：
no wifi-ssid alias alias-name
自定义ZTNA客户端版本作为Android终端信息项
用户可以配置防火墙检查Android终端使用的ZTNA客户端版本。
自定义需要收集的ZTNA客户端版本信息，在endpoint-information-android-profile配置模式下，使用
以下命令：
client-version alias alias-name value client-version

<!-- 来源页 1793 -->
l
client-version alias alias-name - 指定ZTNA客户端版本的别名，取值范围为1至31个字符。
l
value client-version - 指定ZTNA客户端版本，取值范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的ZTNA客户端版本信息。
在endpoint-information-android-profile配置模式下，使用以下命令可以删除指定的ZTNA客户端版本
信息项配置：
no client-version alias alias-name
查看Android终端信息项配置
查看系统支持的预定义和自定义Android终端信息项，在任意模式下，使用以下命令：
show endpoint-information-ios-profile
查看指定的Android终端信息项配置信息，在任意模式下，使用以下命令：
show endpoint-information-ios-profile key-name
l
key-name - 指定Android终端信息项的名称，支持预定义和自定义项。
ChineseOS终端信息管理
系统内置的预定义ChineseOS终端信息项如下表所示。
预定义ChineseOS终端信息项
终端信息项名称
详细描述
关系运算符
取值
os-version
ChineseOS终端的操作系统
版本
is、is-not
KylinV10 ;
UOS20
系统支持对如下表格所示的自定义ChineseOS终端信息项进行配置，以用于终端信息采集和终端标签规则引
用。
自定义ChineseOS终端信息项
终端信息项名称
详细描述
关系运算符
取值
process
ChineseOS终端中指定进程
的运行状态
exist、not-exist
指定的进程的别名
service-running
ChineseOS终端中指定服务
的运行状态
exist、not-exist
指定的服务的别名
service-installed
ChineseOS终端中指定服务
的安装状态
exist、not-exist
指定的服务的别名
file
ChineseOS终端内指定文件
的存在状态
exist、not-exist
指定的文件的别名

<!-- 来源页 1794 -->
进入自定义ChineseOS终端信息项配置模式
配置自定义ChineseOS终端信息项，需在全局配置模式下，使用以下命令进入endpoint-informationchineseos-profile配置模式：
endpoint-information-chineseos-profile
自定义运行进程作为ChineseOS终端信息项
用户可以配置防火墙检查ChineseOS终端是否正在运行指定的进程。
自定义需要收集的运行进程信息，在endpoint-information-chineseos-profile配置模式下，使用以下
命令：
process alias alias-name value process-name
l
alias alias-name - 指定进程的别名，范围为1至31个字符。
l
value process-name - 指定进程的实际名称，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的运行进程信息。
在endpoint-information-chineseos-profile配置模式下，使用以下命令可以删除指定的运行进程信息
项配置：
no process alias alias-name
自定义运行服务作为ChineseOS终端信息项
用户可以配置防火墙检查ChineseOS终端是否正在运行指定的服务。
自定义需要收集的运行服务信息，在endpoint-information-chineseos-profile配置模式下，使用以下
命令：
service-running alias alias-name value service-name
l
alias alias-name - 指定服务的别名，范围为1至31个字符。
l
value service-name - 指定服务的实际名称，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的运行服务信息。
在endpoint-information-chineseos-profile配置模式下，使用以下命令可以删除指定的运行服务信息
项配置：
no service-running alias alias-name

<!-- 来源页 1795 -->
自定义已安装服务作为ChineseOS终端信息项
用户可以配置防火墙检查ChineseOS终端是否安装了指定的进程。
自定义需要收集的已安装服务信息，在endpoint-information-chineseos-profile配置模式下，使用以
下命令：
service-installed alias alias-name value service-name
l
alias alias-name - 指定服务的别名，范围为1至31个字符。
l
value service-name - 指定服务的实际名称，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的已安装服务信息。
在endpoint-information-chineseos-profile配置模式下，使用以下命令可以删除指定的已安装服务信
息项配置：
no service-installed alias alias-name
自定义文件作为ChineseOS终端信息项
用户可以配置防火墙检查ChineseOS终端是否存在指定的文件。
自定义需要收集的文件信息，在endpoint-information-chineseos-profile配置模式下，使用以下命
令：
file alias alias-name value file-name
l
alias alias-name - 指定文件的别名，范围为1至31个字符。
l
value file-name - 指定文件的绝对路径，范围为1至255个字符。
重复该命令可以自定义最多5条需要收集的文件信息。
在endpoint-information-chineseos-profile配置模式下，使用以下命令可以删除指定的文件信息项配
置：
no file alias alias-name
查看ChineseOS终端信息项配置
查看系统支持的预定义和自定义ChineseOS终端信息项，在任意模式下，使用以下命令：
show endpoint-information-chineseos-profile
查看指定的ChineseOS终端信息项配置信息，在任意模式下，使用以下命令：
show endpoint-information-chineseos-profile key-name

<!-- 来源页 1796 -->
l
key-name - 指定ChineseOS终端信息项的名称，支持预定义和自定义项。
例如：
hostname(config)# show endpoint-information-chineseos-profile
Total ZTNA endpoint information key: 5（ChineseOS终端信息项数量）
=====================================================
Key name ID Data type Support custom（ChineseOS终端信息项名称、ChineseOS终端信息项
ID、数据类型、是否允许自定义）
-----------------------------------------------------
file 10 string Yes
os-version 1 string No
process 20 string Yes
service-installed 40 string Yes
service-running 30 string Yes
=====================================================
HarmonyOS PC终端信息管理
系统支持对如下表格所示的自定义HarmonyOS PC终端信息项进行配置，以用于终端信息采集和终端标签
规则引用。
自定义HarmonyOS PC终端信息项
终端信息项名称
详细描述
关系运算符
取值
os-version
HarmonyOS PC终端的操作
系统版本
=、!=、>、<、>=、<=
指定操作系统版本的别名。
device-model
HarmonyOS PC终端设备的
型号
is、is-not
指定的设备型号的别名
wifi-ssid
HarmonyOS PC终端所连接
WiFi的SSID信息
is、is-not
指定的WiFi SSID的别名
client-version
HarmonyOS PC终端使用的
Hillstone Secure Connect
客户端（ZTNA客户端）版
本
is、is-not
指定的ZTNA客户端版本的
别名

<!-- 来源页 1797 -->
进入自定义HarmonyOS PC终端信息项配置模式
配置自定义HarmonyOS PC终端信息项，需在全局配置模式下，使用以下命令进入自定义HarmonyOS PC
终端信息项配置模式：
ztna-endpoint-information-harmonyos-pc-profile
配置OS版本作为HarmonyOS PC终端信息采集项
用户可根据需求，配置终端设备的操作系统版本作为HarmonyOS PC终端信息采集项。
配置OS版本信息，在自定义HarmonyOS PC终端信息项配置模式下，使用以下命令：
os-version alias alias-name value os-version-number
l
alias alias-name - 指定HarmonyOS PC终端的OS版本的别名，取值范围为1至31个字符。
l
value
os-version-number - 指定HarmonyOS PC终端的OS版本，取值范围为1至255个字符。
重复该命令，可以自定义添加最多5条OS版本信息配置。
在自定义HarmonyOS PC终端信息项配置模式下，使用以下命令可以删除指定HarmonyOS PC终端的OS
版本信息项配置：
no os-version alias alias-name
配置设备型号作为HarmonyOS PC终端信息采集项
用户可根据需求，配置终端设备型号作为HarmonyOS PC终端信息采集项。
配置终端设备型号信息，在自定义HarmonyOS PC终端信息项配置模式下，使用以下命令：
device-model alias alias-name value device-model-number
l
alias alias-name - 指定HarmonyOS PC终端设备型号的别名，取值范围为1至31个字符。
l
value device-model-number - 指定HarmonyOS PC终端设备的型号，取值范围为1至255个字
符。
重复该命令，可以自定义添加最多5条设备型号配置。
在自定义HarmonyOS PC终端信息项配置模式下，使用以下命令可以删除指定的HarmonyOS PC终端设备
型号信息项配置：
no device-model alias alias-name
配置WiFi SSID作为HarmonyOS PC终端信息采集项
用户可根据需求，配置终端连接WiFi的SSID信息作为HarmonyOS PC终端信息采集项。

<!-- 来源页 1798 -->
配置WiFi SSID信息，在自定义HarmonyOS PC终端信息项配置模式下，使用以下命令：
wifi-ssid alias alias-name value wifi-ssid
l
alias alias-name - 指定HarmonyOS PC终端设备使用的WiFi SSID的别名，取值范围为1至31个字
符。
l
value wifi-ssid - 指定WiFi SSID，取值范围为1至255个字符。
重复该命令，可以自定义添加最多5条WiFi SSID信息配置。
在自定义HarmonyOS PC终端信息项配置模式下，使用以下命令可以删除指定的WiFi SSID信息项配置：
no wifi-ssid alias alias-name
配置ZTNA客户端版本作为HarmonyOS PC终端信息采集项
用户可根据需求，配置ZTNA客户端版本作为HarmonyOS PC终端信息采集项。
配置ZTNA客户端版本信息，在自定义HarmonyOS PC终端信息项配置模式下，使用以下命令：
client-version alias alias-name value client-version
l
client-version alias alias-name - 指定ZTNA客户端版本的别名，取值范围为1至31个字符。
l
value client-version - 指定ZTNA客户端版本，取值范围为1至255个字符。
重复该命令，可以自定义添加最多5条ZTNA客户端版本信息配置。
在自定义HarmonyOS PC终端信息项配置模式下，使用以下命令可以删除指定的ZTNA客户端版本信息项配
置：
no client-version alias alias-name
查看HarmonyOS PC终端信息项配置
查看系统支持的HarmonyOS PC终端信息项，在任意模式下，使用以下命令：
show ztna-endpoint-information-harmonyos-pc-profile
以下是返回结果示例：
hostname(config)# show ztna-endpoint-information-harmonyos-pc-profile
Total ZTNA endpoint information key: 4（终端信息项数量）
=====================================================
Key name ID Data type Support custom（终端信息项名称、终端信息项ID、数据类型、是否允许自
定义）

<!-- 来源页 1799 -->
-----------------------------------------------------
os-version 1 version Yes
device-model 30 string Yes
wifi-ssid 50 string Yes
client-version 60 string Yes
=====================================================
查看指定的HarmonyOS PC终端信息项配置信息，在任意模式下，使用以下命令：
show ztna-endpoint-information-harmonyos-pc-profile key-name
l
key-name - 指定HarmonyOS PC终端信息项的名称。
以下是查询OS版本信息的返回结果示例：
hostname(config)# show ztna-endpoint-information-harmonyos-pc-profileos-version
endpoint information key basic information:
Name : os-version
ID : 1
Display name en : OS Version
Display name cn : OS版本
Data type : version
Support custom : Yes
Operator : < <= = != >= >
Total ZTNA endpoint information key value: 1
==================================================================
Custom alias name | String value
------------------------------------------------------------------
version 5.0.0
==================================================================
HarmonyOS Mobile(5.0+)终端信息管理
注意: 仅支持OS版本为5.0及以上版本的HarmonyOS Mobile终端。

<!-- 来源页 1800 -->
系统支持对如下表格所示的自定义HarmonyOS Mobile(5.0+)终端信息项进行配置，以用于终端信息采集
和终端标签规则引用。
自定义HarmonyOS Mobile(5.0+)终端信息项
终端信息项名称
详细描述
关系运算符
取值
os-version
HarmonyOS Mobile(5.0+)
终端的操作系统版本
=、!=、>、<、>=、<=
指定操作系统版本的别名。
device-model
HarmonyOS Mobile(5.0+)
终端设备的型号
is、is-not
指定的设备型号的别名
wifi-ssid
HarmonyOS Mobile(5.0+)
终端所连接WiFi的SSID信息
is、is-not
指定的WiFi SSID的别名
client-version
HarmonyOS Mobile(5.0+)
终端使用的Hillstone
Secure Connect客户端
（ZTNA客户端）版本
is、is-not
指定的ZTNA客户端版本的
别名
进入自定义HarmonyOS Mobile(5.0+)终端信息项配置模式
配置自定义HarmonyOS Mobile(5.0+)终端信息项，需在全局配置模式下，使用以下命令进入自定义
HarmonyOS Mobile(5.0+)终端信息项配置模式：
ztna-endpoint-information-harmonyos-mobile-profile
配置OS版本作为HarmonyOS Mobile(5.0+)终端信息采集项
用户可根据需求，配置终端设备的操作系统版本作为HarmonyOS Mobile(5.0+)终端信息采集项。
配置OS版本信息，在自定义HarmonyOS Mobile(5.0+)终端信息项配置模式下，使用以下命令：
os-version alias alias-name value os-version-number
l
alias alias-name - 指定HarmonyOS Mobile(5.0+)终端的OS版本的别名，取值范围为1至31个字
符。
l
value
os-version-number - 指定HarmonyOS Mobile(5.0+)终端的OS版本，取值范围为1至255
个字符。
重复该命令，可以自定义添加最多5条OS版本信息配置。
在自定义HarmonyOS Mobile(5.0+)终端信息项配置模式下，使用以下命令可以删除指定HarmonyOS
Mobile(5.0+)终端的OS版本信息项配置：
no os-version alias alias-name

<!-- 来源页 1801 -->
配置设备型号作为HarmonyOS Mobile(5.0+)终端信息采集项
用户可根据需求，配置终端设备型号作为HarmonyOS Mobile(5.0+)终端信息采集项。
配置终端设备型号信息，在自定义HarmonyOS Mobile(5.0+)终端信息项配置模式下，使用以下命令：
device-model alias alias-name value device-model-number
l
alias alias-name - 指定HarmonyOS Mobile(5.0+)终端设备型号的别名，取值范围为1至31个字
符。
l
value device-model-number - 指定HarmonyOS Mobile(5.0+)终端设备的型号，取值范围为1至
255个字符。
重复该命令，可以自定义添加最多5条设备型号配置。
在自定义HarmonyOS Mobile(5.0+)终端信息项配置模式下，使用以下命令可以删除指定的HarmonyOS
Mobile(5.0+)终端设备型号信息项配置：
no device-model alias alias-name
配置WiFi SSID作为HarmonyOS Mobile(5.0+)终端信息项
用户可根据需求，配置终端连接WiFi的SSID信息作为HarmonyOS Mobile(5.0+)终端信息采集项。
配置WiFi SSID信息，在自定义HarmonyOS Mobile(5.0+)终端信息项配置模式下，使用以下命令：
wifi-ssid alias alias-name value wifi-ssid
l
alias alias-name - 指定HarmonyOS Mobile(5.0+)终端设备使用的WiFi SSID的别名，取值范围为
1至31个字符。
l
value wifi-ssid - 指定WiFi SSID，取值范围为1至255个字符。
重复该命令，可以自定义添加最多5条WiFi SSID信息配置。
在自定义HarmonyOS Mobile(5.0+)终端信息项配置模式下，使用以下命令可以删除指定的WiFi SSID信息
项配置：
no wifi-ssid alias alias-name
配置ZTNA客户端版本作为HarmonyOS Mobile(5.0+)终端信息采集项
用户可根据需求，配置ZTNA客户端版本作为HarmonyOS Mobile(5.0+)终端信息采集项。
配置ZTNA客户端版本信息，在自定义HarmonyOS Mobile(5.0+)终端信息项配置模式下，使用以下命令：
client-version alias alias-name value client-version

<!-- 来源页 1802 -->
l
client-version alias alias-name - 指定ZTNA客户端版本的别名，取值范围为1至31个字符。
l
value client-version - 指定ZTNA客户端版本，取值范围为1至255个字符。
重复该命令，可以自定义添加最多5条ZTNA客户端版本信息配置。
在自定义HarmonyOS Mobile(5.0+)终端信息项配置模式下，使用以下命令可以删除指定的ZTNA客户端版
本信息项配置：
no client-version alias alias-name
查看HarmonyOS Mobile(5.0+)终端信息项配置
查看系统支持的HarmonyOS Mobile(5.0+)终端信息项，在任意模式下，使用以下命令：
show ztna-endpoint-information-harmonyos-mobile-profile
以下是返回结果示例：
hostname(config)# show ztna-endpoint-information-harmonyos-mobile-profile
Total ZTNA endpoint information key: 4（终端信息项数量）
=====================================================
Key name ID Data type Support custom（终端信息项名称、终端信息项ID、数据类型、是否允许自
定义）
-----------------------------------------------------
os-version 1 version Yes
device-model 30 string Yes
wifi-ssid 50 string Yes
client-version 60 string Yes
=====================================================
查看指定的HarmonyOS Mobile(5.0+)终端信息项配置信息，在任意模式下，使用以下命令：
show ztna-endpoint-information-harmonyos-mobile-profile key-name
l
key-name - 指定HarmonyOS Mobile(5.0+)终端信息项的名称。
以下是查询OS版本信息的返回结果示例：
hostname(config)# show ztna-endpoint-information-harmonyos-mobile-profile osversion
endpoint information key basic information:

<!-- 来源页 1803 -->
Name : os-version
ID : 1
Display name en : OS Version
Display name cn : OS版本
Data type : version
Support custom : Yes
Operator : < <= = != >= >
Total ZTNA endpoint information key value: 1
==================================================================
Custom alias name | String value
------------------------------------------------------------------
版本A 6.0
==================================================================
配置终端监控周期
在用户认证成功后，系统会持续监控终端状态，实时调整用户可访问的资源权限。系统支持配置终端监控周
期，如果在监控周期内信息收集失败，且连续失败的次数达到指定的阈值，系统会清除该用户的终端标签并
重新匹配策略（包括安全策略和ZTNA策略）。
配置终端监控周期，在全局配置模式下，使用以下命令：
endpoint-information-monitor {edr | ztna} { interval interval-value [threshold thresholdvalue] | threshold threshold-value}
l
edr | ztna - 指定终端监控信息的来源，edr表示智铠（EDR）服务器，ztna表示安装了ZTNA客户端的
PC终端。
l
interval interval-value - 指定终端信息的上报周期，单位为分钟，取值范围为10至65535，默认为
20。
l
threshold threshold-value - 指定终端信息上报的连续失败次数阈值，取值范围为2至65535，默认
为2。
查看终端监控配置信息
查看终端信息监控配置信息，在任意配置模式下，使用以下命令：
show endpoint-information-monitor

<!-- 来源页 1804 -->
查看终端信息库
查看系统的终端信息库，在任意配置模式下，使用以下命令：
show endpoint-information-database
执行该命令后，系统将显示终端信息库的版本信息、支持的终端操作系统和关系运算符。
查看终端列表
查看系统所有终端设备的详细信息，包括终端设备的IP地址、主机名、来源、终端状态、操作系统、风险等
级等内容。
在任意配置模式下，使用以下命令，查看终端列表：
show endpoint information [filter value | ip ip-address]
l
filter value - 指定搜索关键字。指定后，可通过关键字模糊搜索符合条件的终端设备列表。
l
ip ip-address - 指定终端IP地址。指定后，可查看指定IP的终端设备详情。
应用资源/应用资源组
应用资源用于定义用户需要访问的应用、内容、服务等资源，用户需要通过配置地址、协议、端口等来指定
一个应用资源条目。应用资源组用于定义一组应用资源。系统支持配置最多256个应用资源，64个应用资源
组。
系统支持以下方式配置应用资源条目：
l 基于IP地址、协议、端口
l 基于IP范围、协议、端口
l 基于域名、协议、端口
配置应用资源/应用资源组
创建应用资源
创建应用资源并进入此应用资源的配置模式，在全局配置模式下，使用以下命令：
application-resource application-resource-name [id id]
l
application-resource-name - 指定应用资源的名称，取值不区分大小写，范围为1到95个字符。如
果指定的名称已存在，将直接进入该应用资源的配置模式。
l
id id - 指定应用资源的ID，取值范围为1到256，如不指定，系统会分配一个ID。
删除指定的应用资源，在全局配置模式下，使用以下命令：

<!-- 来源页 1805 -->
no application-resource application-resource-name
配置应用资源的中英文显示名称
系统支持为应用资源自定义中文和英文名称。配置生效后，ZTNA Portal页面将根据浏览器语言设置自动匹
配并显示对应语言的应用资源名称。若未配置中英文名称，则默认显示应用资源创建时的原始名称。
注意:
l
仅当设备的系统语言为中文时，支持配置该选项。
l
如果浏览器语言既不是中文也不是英文，ZTNA Portal页面将默认显示英文的应用资源名称。
配置应用资源的中英文显示名称，在应用资源配置模式下，使用以下命令：
{zh-cn-name | en-name} application-resource-name
l
zh-cn-name - 配置中文名称。
l
en-name - 配置英文名称。
l
application-resource-name - 输入对应语言的名称。取值范围为1-95个字符。
删除中英文名称配置，在应用资源配置模式下，使用以下命令：
no {zh-cn-name | en-name}
配置应用资源图标
为提升ZTNA Portal页面的可辨识性与操作效率，用户在配置应用资源时，可为每个应用单独设置展示图
标。该图标将展示在ZTNA Portal页面，辅助用户快速定位并启动对应应用。
系统内置丰富的预定义图标库，可直接选用；若预定义图标无法满足业务需求，用户还可上传本地自定义图
标。若未配置任何应用资源图标，系统默认使用网站图标
作为其展示图标。
以下是系统所有预定义图标的详细说明。
图标名称
图标
说明
application.svg
通用应用。可作为各类业务系统及内部工具的入口图标。
call.svg
通话。适用于电话会议、语音通话、呼叫中心等通信类应
用。
compile.svg
编译。适用于代码编译、构建部署、开发工具等研发类应
用。
customer-service.svg
客服。适用于客服系统、工单管理、在线支持等服务类应
用。

<!-- 来源页 1806 -->
图标名称
图标
说明
data-dashboard.svg
数据仪表盘。适用于数据看板、BI分析、实时监控大屏等
可视化应用。
data.svg
数据。适用于数据处理、数据集成、数据库管理等数据类
应用。
default.svg
网站。可作为各类网页应用的入口图标。当应用资源未指
定任何图标时，系统默认使用该图标作为其展示图标。
document.svg
文档。适用于文档管理系统、知识库、云盘等内容管理类
应用。
download.svg
下载。适用于文件下载、数据导出、客户端获取等传输类
应用。
experiment.svg
实验。适用于测试环境、实验室系统、试运行项目等。
file.svg
文件。适用于文件管理、附件上传等功能入口。
folder.svg
文件夹。适用于目录结构、归档存储、文件归类等场景。
meter.svg
仪表。适用于性能监控、资源用量、指标检测等监控类应
用。
multimedia.svg
多媒体。适用于图片管理、音视频处理、内容编辑等媒体
类应用。
oa.svg
OA（办公自动化）。适用于审批流转、公文管理、考勤
打卡等办公类应用。
phone.svg
电话。适用于通讯录、总机服务、客服热线等通信类应
用。
pie-chart.svg
饼图。适用于统计报表、数据可视化、图表分析等数据呈
现类应用。
play.svg
播放。适用于视频/音频播放器、演示文稿放映等多媒体
展示类场景。
project.svg
项目。适用于项目管理、任务跟踪及团队协作类应用。
self-servicepassword.svg
自助密码。适用于AD/LDAP密码修改、账号自助服务等
场景。
specification-listmanagement.svg
规格清单管理。适用于物料清单、产品规格、标准文档管
理等场景。
video-demo.svg
视频演示。适用于产品演示、教学录像、宣传视频等场
景。
video.svg
视频。适用于视频点播、监控回放、在线课程等播放类应

<!-- 来源页 1807 -->
图标名称
图标
说明
用。
warehousing.svg
仓储。适用于仓库管理、库存系统、物流配送等供应链类
应用。
为应用资源配置预定义图标，在应用资源配置模式下，使用以下命令：
icon predefined icon-name
l
icon-name - 指定所需图标的名称。用户可通过Tab键浏览完整列表，然后手动输入目标名称以完成配
置。
为应用资源上传自定义图标，在应用资源配置模式下，使用以下命令：
icon icon-string
l
icon-string - 输入目标图片的Data URL格式字符串（以data:image/...;base64,开头），它包含了
图片格式声明和Base64编码后的图片数据。取值范围是1-4499个字符。
删除该应用资源的图标配置，并恢复系统默认信息，在应用资源配置模式下，使用以下命令：
no icon
配置基于IP地址的应用资源条目
配置基于IP地址的应用资源条目，在应用资源配置模式下，使用以下命令：
ip ip-address protocol {{tcp | udp} port port-number [maximum-port-number] | {icmp |
icmpv6} [type type-value [code min-code [max-code]]]} [timeout timeout-value |
timeouthour timeout-value | timeoutday timeout-value]
l
ip ip-address - 指定应用资源的IP地址，可以是IPv4/IPv6地址、IPv4地址/掩码、IPv6地址/前缀长
度，前缀长度的取值范围为1到128。
l
protocol {tcp | udp} port port-number [maximum-port-number] - 指定应用资源的传输层协议
类型为TCP或UDP，并指定应用资源的端口号或端口范围，取值范围为1到65535。
l
如果指定端口号，可以只配置port-number 。
l
如果指定端口范围，最小端口port-number 不能大于最大端口maximum-port-number。
说明：如果最小端口port-number 和最大端口maximum-port-number配置一致，则为指定端口
号。
l
protocol {icmp | icmpv6} [type type-value [code min-code [max-code]]] - 指定应用资源的传
输层协议类型为ICMP或ICMPv6，并指定ICMP/ICMPv6 type值和ICMP/ICMPv6 code值。

<!-- 来源页 1808 -->
说明：当IP地址配置为IPv4类型时，应用资源的传输层协议类型仅支持指定为ICMP类型；当IP地址配置
为IPv6类型时，则仅支持指定为ICMPv6类型。
l
type type-value - 指定应用资源的ICMP type值或ICMPv6 type值。ICMP type和ICMPv6
type取值范围都是0-255，详情请参阅"附表：ICMP/ICMPv6 Type以及Code值对照表" 在第
1186页。
l
code min-code [max-code] - 指定应用资源的ICMP code值或ICMPv6 code值。如果
ICMP/ICMPv6 code值为一个范围，min-code为最小code值，max-code为最大code值；如
果不配置max-code，系统将使用min-code作为单一code值。ICMP code和ICMPv6 code取
值范围都是0到255，默认值是min-code为0、max-code为255。
l
timeout timeout-value | timeouthour timeout-value |timeoutday timeout-value - 指定用户
访问应用资源时创建的ZTNA会话的超时时间，到达超时时间后，会话将结束。timeout timeoutvalue指定的超时时间单位为秒，取值范围是1到65535；timeouthour timeout-value 指定的超时时
间单位为小时，取值范围是1到24000；timeoutday timeout-value指定的超时时间单位为天，取值
范围是1到1000。如不设置timeout/timeouthour/timeouday参数，TCP/ICMP类型的ZTNA会话有
效时间默认为1800秒，UDP类型的ZTNA会话有效时间默认为60秒。
注意: 当新增一条基于IP地址的应用资源条目时，如果仅有超时项的配置与已有应用资源条目不
同，已有配置会被覆盖。
删除基于IP地址的应用资源条目，在应用资源配置模式下，使用以下命令：
no ip ip-address protocol {{tcp | udp} port port-number [maximum-port-number] | {icmp |
icmpv6} [type type-value [code min-code [max-code]]]}
配置基于IP范围的应用资源条目
配置基于IP范围的应用资源条目，在应用资源配置模式下，使用以下命令：
range min-ip max-ip protocol {{tcp | udp} port port-number [maximum-port-number] |
{icmp | icmpv6} [type type-value [code min-code [max-code]]]} [timeout timeout-value |
timeouthour timeout-value | timeoutday timeout-value]
l
range min-ip max-ip - 指定应用资源的IP范围，min-ip为最小IP地址，max-ip为最大IP地址。IP
范围内最多可以包含65535个IP地址。
l
protocol {tcp | udp} port port-number [maximum-port-number] - 指定应用资源的传输层协议
类型为TCP或UDP，并指定应用资源的端口号或端口范围，取值范围为1到65535。

<!-- 来源页 1809 -->
l
如果指定端口号，可以只配置port-number 。
l
如果指定端口范围，最小端口port-number 不能大于最大端口maximum-port-number。
说明：如果最小端口port-number 和最大端口maximum-port-number配置一致，则为指定端口
号。
l
protocol {icmp | icmpv6} [type type-value [code min-code [max-code]]] - 指定应用资源的传
输层协议类型为ICMP或ICMPv6，并指定ICMP/ICMPv6 type值和ICMP/ICMPv6 code值。
说明：当IP范围配置为IPv4类型时，应用资源的传输层协议类型仅支持指定为ICMP类型；当IP范围配置
为IPv6类型时，则仅支持指定为ICMPv6类型。
l
type type-value - 指定应用资源的ICMP type值或ICMPv6 type值。ICMP type和ICMPv6
type取值范围都是0-255，详情请参阅"附表：ICMP/ICMPv6 Type以及Code值对照表" 在第
1186页。
l
code min-code [max-code] - 指定应用资源的ICMP code值或ICMPv6 code值。如果
ICMP/ICMPv6 code值为一个范围，min-code为最小code值，max-code为最大code值；如
果不配置max-code，系统将使用min-code作为单一code值。ICMP code和ICMPv6 code取
值范围都是0到255，默认值是min-code为0、max-code为255。
l
timeout timeout-value | timeouthour timeout-value |timeoutday timeout-value - 指定用户
访问应用资源时创建的ZTNA会话的超时时间，到达超时时间后，会话将结束。timeout timeoutvalue指定的超时时间单位为秒，取值范围是1到65535；timeouthour timeout-value 指定的超时时
间单位为小时，取值范围是1到24000；timeoutday timeout-value指定的超时时间单位为天，取值
范围是1到1000。如不设置timeout/timeouthour/timeouday参数，TCP/ICMP类型的ZTNA会话有
效时间默认为1800秒，UDP类型的ZTNA会话有效时间默认为60秒。
注意: 当新增一条基于IP范围的应用资源条目时，如果仅有超时项的配置与已有应用资源条目不
同，已有配置会被覆盖。
删除基于IP范围的应用资源条目，在应用资源配置模式下，使用以下命令：
no range min-ip max-ip protocol {{tcp | udp} port port-number [maximum-port-number] |
{icmp | icmpv6} [type type-value [code min-code [max-code]]]}
配置基于域名的应用资源条目
配置基于域名的应用资源条目，在应用资源配置模式下，使用以下命令：

<!-- 来源页 1810 -->
domain string protocol {http | https} port port-number [maximum-port-number] [timeout
timeout-value | timeouthour timeout-value | timeoutday timeout-value]
l
domain string - 指定应用资源的域名，取值范围是1到255个字符，且在两个点号（.）之间最多可以
有63个字符。支持设置精确域名和以“*”作为第一个字符的通配域名。
l
protocol {http | https} - 指定应用资源的应用层协议类型为HTTP或HTTPS。
l
port port-number [maximum-port-number] - 指定应用资源的端口号或端口范围，取值范围为1
到65535。
l
如果指定端口号，可以只配置port-number 。
l
如果指定端口范围，最小端口port-number 不能大于最大端口maximum-port-number。
说明：如果最小端口port-number 和最大端口maximum-port-number配置一致，则为指定端口
号。
l
timeout timeout-value | timeouthour timeout-value |timeoutday timeout-value - 指定用户
访问应用资源时创建的ZTNA会话的超时时间，到达超时时间后，会话将结束。timeout timeoutvalue指定的超时时间单位为秒，取值范围是1到65535；timeouthour timeout-value 指定的超时时
间单位为小时，取值范围是1到24000；timeoutday timeout-value指定的超时时间单位为天，取值
范围是1到1000。如不设置timeout/timeouthour/timeouday参数，TCP/ICMP类型的ZTNA会话有
效时间默认为1800秒，UDP类型的ZTNA会话有效时间默认为60秒。
注意: 当新增一条基于域名的应用资源条目时，如果仅有超时项的配置与已有应用资源条目不同，
已有配置会被覆盖。
删除基于域名的应用资源条目，在应用资源配置模式下，使用以下命令：
no domain string protocol {http | https} port port-number [maximum-port-number]
配置超链接
在用户登录后展示的ZTNA Portal页面上，配置了超链接的应用资源，用户可以复制链接到浏览器访问，也
可以直接点击图标实现快速访问（需确保链接有效）。不配置超链接的应用资源不会展示在Portal页面上。
Portal页面上展示用户有权限和无权限访问的应用资源。对于无权限访问的应用资源，用户在调整终端配置
后，可以获得访问权限。禁止访问的应用资源不在Portal页面上展示，如果用户被禁止访问任何应用资源，
Portal页面将展示“无可用的Web服务资源”。关闭Portal页面后，用户可以通过客户端菜单的“应用资源
列表”选项重新打开最新的Portal页面查看应用资源的访问权限。
配置超链接，在应用资源配置模式下，使用以下命令：
hyperlink hyperlink

<!-- 来源页 1811 -->
l
hyperlink - 指定超链接，取值范围是1到2047个字符，如果超链接中不指定协议类型，默认使用
HTTP。
删除超链接，在应用资源配置模式下，使用以下命令：
no hyperlink
配置应用资源的描述信息
配置应用资源的描述信息，在应用资源配置模式下，使用以下命令：
description description
l
description - 指定应用资源的描述信息，取值范围为1到255个字符。当应用资源已存在描述信息时，
输入新的描述信息会修改已有配置。
删除应用资源的描述信息，在应用资源配置模式下，使用以下命令：
no description
重命名应用资源
修改应用资源的名称，在应用资源配置模式下，使用以下命令：
rename application-resource-name
l
application-resource-name - 指定应用资源的新名称，取值不区分大小写，范围为1到95个字符。
也可以在全局配置模式下，使用以下命令修改应用资源的名称：
rename application-resource original-application-resource-name new-applicationresource-name
l
original-application-resource-name - 指定应用资源的原名称。
l
new-application-resource-name - 指定应用资源的新名称，取值不区分大小写，范围为1到95个字
符。
配置应用资源分类
随着应用资源数量的增加，用户在ZTNA Portal界面查找特定应用资源时可能会感到不便。为了提升用户体
验和操作便利性，系统支持对应用资源进行分组展示。通过将应用资源按照类别进行分组，不仅可以让用户
更快捷地找到所需的应用资源，也能使ZTNA Portal界面看起来更加整洁和有序。
应用资源分类的相关配置，包括以下内容：
l 新增应用资源分类
l 重命名应用资源分类

<!-- 来源页 1812 -->
l 为应用资源设置所属分类
l 查看应用资源分类的配置信息
新增应用资源分类
新增应用资源分类，在全局配置模式下，使用以下命令：
application-resource-category category-name
l
category-name - 指定应用资源分类的名称，取值不区分大小写，范围为1到95个字符。
删除指定的应用资源分类，在全局配置模式下，使用以下命令：
no application-resource-category category-name
重命名应用资源分类
修改应用资源分类的名称，在全局配置模式下，使用以下命令：
rename application-resource-category original-category-name new-category-name
l
original-category-name - 指定应用资源分类的原名称。
l
new-category-name - 指定应用资源分类的新名称，取值不区分大小写，范围为1到95个字符。
为应用资源设置所属分类
为应用资源设置所属分类，在应用资源配置模式下，使用以下命令：
category category-name
l
category-name - 指定应用资源所属的分类名称。
删除为应用资源设置的分类，在应用资源配置模式下，使用以下命令：
no category
查看应用资源分类的配置信息
查看应用资源分类的配置信息，在任意模式下，使用以下命令：
show application-resource-category [name category-name]
l
name category-name - 指定需要查看配置信息的应用资源分类名称。如不指定，则表示查看所有应
用资源分类的配置信息。
以下是一个返回结果示例：

<!-- 来源页 1813 -->
hostname#show application-resource-category
Total count: 4（应用资源分类总数）
==================================================================
Name App-Resource-Count（应用资源分类名称成员数量）
------------------------------------------------------------------------------------------
分类0 1
分类1 2
分类2 3
==================================================================
hostname#show application-resource-category name 分类0
Name:分类0
Application resource count: 1（表示该分类下有一个应用资源）
|_appres1
查看应用资源配置信息
查看指定应用资源的配置信息，在任意模式下，使用以下命令：
show application-resource {name application-resource-name | id id}
l
name application-resource-name | id id - 指定应用资源的名称或ID。
查看所有应用资源的配置信息，在任意模式下，使用以下命令：
show application-resource
查看符合过滤条件的应用资源配置信息
查看符合指定过滤条件的应用资源配置信息，在任意模式下，使用以下命令：
show application-resource filter { [name application-resource-name] [ip ip-address]
[domain string] [protocol {tcp | udp | http | https | {icmp | icmpv6} type type-value code mincode max-code} ] [port port-number] [description description] [hyperlink hyperlink]
[referenced | unreferenced] [zh-cn-name application-resource-name | en-name
application-resource-name]}
l
name application-resource-name - 显示配置了指定应用资源名称的应用资源配置信息，支持部分
和全部匹配。

<!-- 来源页 1814 -->
l
ip ip-address - 显示配置了指定IP地址的应用资源配置信息，可以为IPv4/IPv6地址，IPv4地址/掩
码、IPv6地址/前缀长度。
l
domain string - 显示配置了指定域名的应用资源配置信息，支持部分和全部匹配。
l
protocol {tcp | udp | http | https | {icmp | icmpv6} type type-value code min-code maxcode} - 显示配置了指定协议类型的应用资源配置信息。过滤基于IP定义的应用资源时，协议类型支持
TCP、UDP、ICMP、ICMPv6；过滤基于域名定义的应用资源时，协议类型支持HTTP、HTTPS。
l
port port-number - 显示配置了指定端口号的应用资源配置信息。
l
description description - 显示配置了指定描述信息的应用资源配置信息，支持部分和全部匹配。
l
hyperlink hyperlink - 显示配置了指定超链接的应用资源配置信息，支持部分和全部匹配。
l
referenced | unreferenced - 显示被引用或未被引用的应用资源配置信息。
l
zh-cn-name application-resource-name | en-name application-resource-name - 显示配置
了指定中英文名称的应用资源配置信息，支持模糊和精确匹配。
查看应用资源的引用信息
当用户流量命中ZTNA策略时，将被允许或禁止访问策略中引用的应用资源。
查看指定应用资源的ZTNA策略引用信息，在任意模式下，使用以下命令：
show reference application-resource application-resource-name
l
application-resource-name - 指定应用资源名称。
创建应用资源组
应用资源组由一个或多个应用资源组成。创建应用资源组并进入此应用资源组的配置模式，在全局配置模式
下，使用以下命令：
application-resource-group application-resource-group-name [id id]
l
application-resource-group-name - 指定应用资源组的名称，取值不区分大小写，范围为1到95个
字符。如果指定的应用资源组名称已存在，则直接进入此应用资源组的配置模式。
l
id id - 指定应用资源组的ID，取值范围为1到64，如不指定，系统会分配一个ID。
删除指定的应用资源组，在全局配置模式下，使用以下命令：
no application-resource-group group-name
配置应用资源组成员
每个应用资源组包含1个或最多16个应用资源。

<!-- 来源页 1815 -->
配置应用资源组成员，在应用资源组配置模式下，使用以下命令：
application-resource application-resource-name
l
application-resource-name - 指定已存在的应用资源名称。
删除应用资源组的指定成员，在应用资源组配置模式下，使用以下命令：
no application-resource application-resource-name
配置应用资源组描述信息
配置应用资源组的描述信息，在应用资源组配置模式下，使用以下命令：
description description
l
description - 指定应用资源组的描述信息，取值范围为1到255个字符。当应用资源组已存在描述信息
时，输入新的描述信息会修改已有配置。
删除应用资源组的描述信息，在应用资源组配置模式下，使用以下命令：
no description
重命名应用资源组
修改应用资源组的名称，在应用资源组配置模式下，使用以下命令：
rename application-resource-group-name
l
application-resource-group-name - 指定应用资源组的新名称，取值不区分大小写，范围为1到95
个字符。
也可以在全局配置模式下，使用以下命令修改应用资源组的名称：
rename application-resource-group original-application-resource-group-name newapplication-resource-group-name
l
original-application-resource-group-name - 指定应用资源组的原名称。
l
new-application-resource-group-name - 指定应用资源组的新名称，取值不区分大小写，范围为
1到95个字符。
查看应用资源组配置信息
查看指定应用资源组的配置信息，在任意配置模式下，使用以下命令：
show application-resource-group {name application-resource-group-name | id id}
l
name application-resource-group-name | id id - 指定应用资源组的名称或ID。

<!-- 来源页 1816 -->
查看所有应用资源组的配置信息，在任意配置模式下，使用以下命令：
show application-resource-group
查看应用资源组的引用信息
当用户流量命中ZTNA策略时，将被允许或禁止访问策略中引用的应用资源组。
查看指定应用资源组的引用信息，在任意配置模式下，使用以下命令：
show reference application-resource-group group-name
l
group-name - 指定应用资源组的名称。
ZTNA策略
零信任网络访问（ZTNA）策略是一种以“永不信任、始终验证”为原则的网络安全策略，它要求对每个用
户和设备进行严格的身份验证和授权，确保只有经过授权且符合安全策略的实体才能访问指定的网络资源。
ZTNA策略分为ZTNA授权策略和自定义配置的ZTNA策略。系统支持配置最多2000条ZTNA策略（即ZTNA
授权策略和自定义配置的ZTNA策略之和）。
l ZTNA授权策略：在ZTNA场景中，当用户通过Radius服务器进行认证且认证成功后，Radius服务器会根据服务
器中用户的配置，为该认证用户创建一条或多条包含终端标签、应用资源以及行为的ZTNA策略，该策略被称为
ZTNA授权策略。若认证用户需要在不中断ZTNA连接的情况下调整ZTNA授权策略，只需在Radius服务器中修改
或添加相应的配置，这样，Radius服务器就能够发送CoA请求消息，从而动态地调整或下发新的ZTNA授权策
略。Radius服务器为认证用户创建的ZTNA授权策略会展示在<ZTNA策略>页面的列表最后面（不支持修调整授
权策略的顺序），用户可在该页面查看ZTNA授权策略详情。ZTNA授权策略不允许被编辑，但可以被删除。系统
支持在<ZTNA策略>页面手动删除ZTNA授权策略，也可以在认证用户断开ZTNA连接后，自动删除对应的ZTNA
授权策略。Radius服务器最多可以为每个认证用户创建16条ZTNA授权策略。
注意: 如需启用ZTNA授权策略，请关注以下内容：
l
请确保Radius服务器中用户配置信息里包含了ZTNA策略字符串，且该字符串所指定的
终端标签和应用资源，已提前在防火墙中配置成功。ZTNA策略字符串配置格式说明详见
“ZTNA策略字符串格式”章节。
l
ZTNA用户认证使用的Radius服务器必须已启用“授权策略”功能，详情请参阅“"AAA
（认证、授权与计费）" 在第1195页> 配置Radius服务器”章节。

<!-- 来源页 1817 -->
l
若认证用户需要在不中断ZTNA连接的情况下调整ZTNA授权策略，必须确保已开启
Radius动态授权功能，详情请参阅“"AAA（认证、授权与计费）" 在第1195页> 配置
Radius动态授权”章节。
l
在配置ZTNA网关时，需要在“接入用户”选项中引用已开启“授权策略”功能的
Radius服务器，详情请参阅“配置ZTNA网关”章节。
l 自定义配置的ZTNA策略：指用户在<ZTNA策略>页面手动创建的ZTNA策略。用户可对手动创建的ZTNA策略进
行编辑和删除等操作。
ZTNA策略中需要指定匹配条件和控制动作，ZTNA策略支持以下维度作为匹配条件：
l 用户/用户组/角色：当用户的用户名/用户组/角色和ZTNA策略中绑定的用户名/用户组/角色匹配时，即命中了
该维度。
l 终端标签：当用户携带的终端标签和ZTNA策略中绑定的终端标签匹配时，即命中了该维度。
l 应用资源/应用资源组：当用户请求访问的应用资源/应用资源组和ZTNA策略中绑定的应用资源匹配时，即命中
了该维度。
l 时间表：当用户的访问时间和ZTNA策略中绑定的时间表匹配时，即命中了该维度。
在一条ZTNA策略中，可以配置一个或多个上述维度作为匹配条件。当配置多个维度时，需要同时匹配所有
维度，才会命中ZTNA策略并按照ZTNA策略规定的控制动作处理流量。当某个维度未配置时，表示该维度可
以匹配任意对象。ZTNA策略的控制动作包括两种（必须配置一种）：
l permit：当流量匹配指定的ZTNA策略时，允许访问ZTNA策略中绑定的应用资源。
l deny：当流量匹配指定的ZTNA策略时，拒绝访问ZTNA策略中绑定的应用资源。
如果流量未匹配到任何ZTNA策略，会命中ZTNA默认策略，按照ZTNA默认策略里配置的控制动作处理。
ZTNA策略匹配说明
对于外网接入场景，通过为ZTNA实例指定策略模式，流量会按照以下方式进行匹配：
l 当选择ZTNA策略模式时，会进行ZTNA策略匹配。
l 当选择混合模式时，从ZTNA隧道接口进入的流量，且根据路由查找到的流量出接口的安全域服务类型不为WAN
安全域，会进行ZTNA策略匹配。其它流量会进行防火墙安全策略匹配。
对于内网接入场景，通过为ZTNA实例指定策略模式，流量会按照以下方式进行匹配：

<!-- 来源页 1818 -->
l 当选择安全策略模式时，会进行防火墙安全策略匹配。
l 当选择混合模式时，流量入接口的安全域服务类型为ZTNA安全域，且根据路由查找到的流量出接口的安全域服
务类型不为WAN安全域，或根据路由查找到的流量出接口的安全域服务类型为ZTNA安全域，会进行ZTNA策略
匹配。
关于配置安全域服务类型的详细信息，请参阅“指定安全域的服务类型”。
ZTNA策略字符串格式
Radius服务器中用户配置ZTNA策略字符串或发送CoA请求消息中ZTNA策略字符串的格式如下：
ztna-rule rule-name {permit | deny} [endpoint-tag tag-name] [app-resource resourcename] [app-resource-group group-name] [log {policy-deny | session-start | session-end |
policy-deny session-start | policy-deny session-end | session-start session-end | policydeny session-start session-end}] [Description dsecription]
l ztna-rule - 固定前缀，用于区分普通策略和ZTNA策略。
l rule-name - 指定ZTNA策略的名称，唯一标识一条ZTNA策略。取值范围是1~95个字符。
l permit | deny - 指定ZTNA策略的控制动作。permit表示允许访问ZTNA策略中绑定的应用资源；deny表示拒绝
访问ZTNA策略中绑定的应用资源。
l [endpoint-tag tag-name] - 指定终端标签名称，取值范围是1~95个字符。可以填多个但最多不超过10个。当
需要填写多个时，使用空格隔开。例如：endpoint-tag tag1 tag2
l [app-resource resource-name] - 指定应用资源名称，取值范围是1~95个字符。可以填多个但最多不超过10
个。当需要填写多个时，使用空格隔开。例如：app-resource res1 res2 res3
l [app-resource-group group-name] - 指定应用资源组名称，取值范围是1~95个字符。可以填多个但最多不超
过10个。当需要填写多个时，使用空格隔开。例如：app-resource-group group1 group2
l [log {policy-deny | session-start | session-end | policy-deny session-start | policy-deny session-end |
session-start session-end | policy-deny session-start session-end}] - 指定需要记录日志的场景。
o policy-deny - 表示记录ZTNA策略拒绝流量的日志信息；
o session-start - 表示记录ZTNA会话建立的日志信息；
o session-end - 表示记录ZTNA会话结束的日志信息；
o policy-deny session-start - 表示记录ZTNA策略拒绝流量以及ZTNA会话建立的日志信息；
o policy-deny session-end - 表示记录记录ZTNA策略拒绝流量以及ZTNA会话结束的日志信息；
o session-start session-end - 表示记录ZTNA会话建立以及会话结束的日志信息；

<!-- 来源页 1819 -->
o policy-deny session-start session-end - 表示记录ZTNA策略拒绝流量、ZTNA会话建立以及ZTNA会话
结束的日志信息。
l [Description dsecription] - 指定ZTNA策略的描述信息，取值范围为1到255个字符。
注意:
l
单个ZTNA策略字符串的大小不能超过255字节。
l
单个Radius报文的大小不能超过4096字节。
以下是Radius服务器中用户配置信息里包含的ZTNA策略字符串示例：
配置ZTNA策略
ZTNA策略配置包括：
l 创建ZTNA策略
l 配置ZTNA策略名称
l 绑定应用资源/应用资源组
l 绑定终端标签
l 绑定用户/用户组
l 配置时间表
l 指定控制动作
l 配置策略审计
l 启用/禁用ZTNA策略
l 配置策略描述信息
l ZTNA策略日志管理
l 绑定病毒过滤Profile
l 绑定沙箱防护Profile
l 绑定入侵防御Profile
l 绑定文件过滤Profile
l 绑定文件内容过滤Profile

<!-- 来源页 1820 -->
l 进入全局ZTNA策略配置模式
l 清除ZTNA策略统计信息
创建ZTNA策略
新建ZTNA策略并进入ZTNA策略配置模式，在全局配置模式下，使用以下命令：
ztna-rule [name rule-name | id id] [top | before {name rule-name | id} | after {name rulename | id} ]
l
name rule-name - 指定ZTNA策略名称，取值范围是1到95个字符。
l
id id - 指定ZTNA策略ID，取值范围为1至2000。如果指定ID的ZTNA策略已存在，则直接进入ZTNA策
略配置模式。如果在新建ZTNA策略时不指定ID，系统会分配一个。
l
top | before {name rule-name | id} | after {name rule-name | id} - 指定ZTNA策略的位置。默
认情况下，系统会将新创建的ZTNA策略放到所有策略的末尾。
l
top - 指定ZTNA策略的位置为所有策略的首位。
l
before {name rule-name | id} - 指定ZTNA策略的位置为某个策略名称或ID之前。
l
after {name rule-name | id} - 指定ZTNA策略的位置为某个策略名称或ID之后。
删除指定的ZTNA策略，在全局配置模式下，使用以下命令：
no ztna-rule {name rule-name | id id}
配置ZTNA策略名称
对于已存在的ZTNA策略，设置或修改策略名称，在ZTNA策略配置模式下，使用以下命令：
name name
l
name - 指定ZTNA策略名称，取值范围是1到95个字符。
删除ZTNA策略的名称，在ZTNA策略配置模式下，使用以下命令：
no name
绑定应用资源/应用资源组
每条ZTNA策略可以绑定最多10个应用资源和10个应用资源组。策略中绑定的多个应用资源或应用资源组之
间是逻辑“或”关系，用户访问其中的任何一个应用资源，即认为命中了这条策略的应用资源维度。当策略
中不绑定应用资源时，可以匹配所有应用资源。
将指定的应用资源绑定到ZTNA策略，在ZTNA策略配置模式下，使用以下命令：
application-resource application-resource-name

<!-- 来源页 1821 -->
l
application-resource-name - 指定已存在的应用资源名称。
取消ZTNA策略与指定应用资源的绑定，在ZTNA策略配置模式下，使用以下命令：
no application-resource application-resource-name
将指定的应用资源组绑定到ZTNA策略，在ZTNA策略配置模式下，使用以下命令：
application-resource-group group-name
l
group-name - 指定已存在的应用资源组名称。
取消ZTNA策略与指定应用资源组的绑定，在ZTNA策略配置模式下，使用以下命令：
no application-resource-group group-name
绑定终端标签
每条ZTNA策略可以绑定最多10个终端标签，多个终端标签之间是逻辑“或”的关系，用户匹配其中的任何
一个终端标签，即认为命中了该条策略的终端标签维度。当策略中不绑定任何终端标签时，表示所有终端标
签都可以匹配。
将指定终端标签与ZTNA策略绑定，在ZTNA策略配置模式下，使用以下命令：
endpoint-tag tag-name
取消ZTNA策略与指定终端标签的绑定，在ZTNA策略配置模式下，使用以下命令：
no endpoint-tag tag-name
绑定用户/用户组/角色
每条ZTNA策略可以绑定最多8个用户/用户组/角色，多个用户/用户组/角色之间是逻辑“或”的关系，其中
的任何一个用户访问时，即认为匹配了该条策略的用户/用户组/角色维度。当策略中不绑定用户/用户组/角
色时，表示所有用户/用户组/角色都可以匹配。
将指定用户与ZTNA策略绑定，在ZTNA策略配置模式下，使用以下命令：
user aaa-server-name user-name
l
aaa-server-name - 指定用户所属的AAA服务器名称。
l
user-name - 指定用户名称。
取消ZTNA策略与指定用户的绑定，在ZTNA策略配置模式下，使用以下命令：
no user aaa-server-name user-name
将指定用户组与ZTNA策略绑定，在ZTNA策略配置模式下，使用以下命令：
user-group aaa-server-name user-group-name

<!-- 来源页 1822 -->
l
aaa-server-name - 指定用户组所属的AAA服务器名称。
l
user-group-name - 指定用户组名称。
取消ZTNA策略与指定用户组的绑定，在ZTNA策略配置模式下，使用以下命令：
no user-group aaa-server-name user-group-name
将指定角色与ZTNA策略绑定，在ZTNA策略配置模式下，使用以下命令：
role role-name
l
role-name - 指定角色名称。
取消ZTNA策略与指定角色的绑定，在ZTNA策略配置模式下，使用以下命令：
no role role-name
配置时间表
默认情况下，配置的ZTNA策略会即时生效，并一直生效。而当为ZTNA策略配置时间表功能后，ZTNA策略
就只在时间表所指定的时间内生效。用户最多可以为一条ZTNA策略配置10个时间表，ZTNA策略的生效时
间为所有被配置到该策略规则的时间表的时间的总和。多个时间表之间是逻辑“或”关系，匹配其中的任何
一个时间表，即认为命中了该条策略的时间表维度。策略中不绑定任何时间表时，表示所有时间都匹配。关
于如何配置时间表，请参阅系统管理的配置时间表部分。
配置时间表，在ZTNA策略配置模式下，使用以下命令：
schedule schedule-name
l
schedule-name - 指定时间表名称。为避免产生不可预知的问题，建议用户不要配置时间重叠的时间
表。
删除指定的时间表，在ZTNA策略配置模式下，使用以下命令：
no schedule schedule-name
指定控制动作
如果不为ZTNA策略指定控制动作，该策略不会生效。
指定对命中策略的流量的控制动作，在ZTNA策略配置模式下，使用以下命令：
action {permit | deny}
l
permit | deny - 为命中策略的流量指定控制动作，允许访问或拒绝访问策略中绑定的应用资源/应用资
源组。

<!-- 来源页 1823 -->
配置审计注释
为策略规则添加策略审计注释内容，来说明策略规则的创建/删除/粘贴/移动/启用/禁用等操作的原因，以
便用户了解策略规则配置的变更理由、变更历史记录。添加策略审计注释内容，在任意模式下，使用以下命
令：
audit-comment ztna-rule id id comment comment
l
rule id id - 指定需要添加审计注释的策略规则ID。
l
comment comment - 指定审计注释内容。范围是1-255个字符。
注意:
l
当audit-comment-enable时，必须配置策略审计内容才能下发ZTNA策略。
l
策略审计功能的平台支持情况如下：
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
启用/禁用ZTNA策略
默认情况下，配置好的ZTNA策略会立即生效。用户可以通过命令禁用某条ZTNA策略，使其不对流量进行控
制。禁用或者启用某条ZTNA策略，在ZTNA策略配置模式下，使用以下命令：
l
禁用：disable
l
启用：enable
配置策略描述信息
配置策略描述信息，在ZTNA策略配置模式下，使用以下命令：
description description
l
description - 指定ZTNA策略的描述信息，取值范围为1到255个字符。当ZTNA策略已存在描述信息
时，输入新的描述信息会修改已有配置。
删除策略描述信息，在ZTNA策略配置模式下，使用以下命令：

<!-- 来源页 1824 -->
no description
ZTNA策略日志管理
系统支持ZTNA策略的日志管理功能。默认情况下，该功能为关闭状态。
l
对于permit类型的ZTNA策略，可以记录两种情况，分别是匹配ZTNA策略的流量建立会话时生成日志信
息和结束会话时生成日志信息。
l
对于deny类型的ZTNA策略，可以记录的情况为：匹配ZTNA策略的流量被deny时生成日志信息。
使用该功能前，必须保证系统的流量日志功能是开启的，即在全局配置模式下，执行logging traffic
session on命令。配置ZTNA策略的日志管理，在ZTNA策略配置模式下，使用以下命令：
log {policy-deny | session-start | session-end}
l
policy-deny – 适用于动作类型为deny的ZTNA策略。使系统生成ZTNA策略拒绝流量的日志信息。
l
session-start – 适用于动作类型为permit的ZTNA策略。使系统生成ZTNA会话建立的日志信息。
l
session-end – 适用于动作类型为permit的ZTNA策略。使系统生成ZTNA会话结束的日志信息。
取消ZTNA策略日志管理功能的配置，在ZTNA策略配置模式下，使用以下命令：
no log {policy-deny | session-start | session-end}
绑定病毒过滤Profile
当系统安装了病毒过滤许可证时，可以为ZTNA策略绑定病毒过滤Profile，对匹配ZTNA策略的流量实现多
种病毒威胁的探测，并根据病毒过滤Profile的配置对发现的病毒进行处理。关于病毒过滤的详细信息，请参
阅病毒过滤。
绑定病毒过滤Profile，在ZTNA策略配置模式下，使用以下命令：
av profile-name
l
profile-name - 指定病毒过滤Profile的名称。
取消ZTNA策略与病毒过滤Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no av
绑定沙箱防护Profile
当系统安装了沙箱防护许可证时，可以为ZTNA策略绑定沙箱防护Profile，对匹配ZTNA策略的流量实现基
于Profile的沙箱防护检查。通过云·影或智影，对可疑文件进行分析，搜集可疑文件的动态行为，判断文件
合法性，将分析结果反馈给系统，并根据沙箱防护Profile的配置对恶意文件进行处理。关于沙箱防护的详细
信息，请参阅沙箱防护。
绑定沙箱防护Profile，在ZTNA策略配置模式下，使用以下命令：

<!-- 来源页 1825 -->
sandbox profile-name
l
profile-name - 指定沙箱防护Profile的名称，支持自定义和预定义类型的沙箱防护Profile。
取消ZTNA策略与沙箱防护Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no sandbox
绑定入侵防御Profile
当系统安装了入侵防御许可证时，可以为ZTNA策略绑定入侵防御Profile，对匹配ZTNA策略的流量实现多
种网络攻击的探测，并根据入侵防御Profile的配置对网络攻击执行阻断等操作。关于入侵防御的详细信息，
请参阅入侵防御系统。
绑定入侵防御Profile，在ZTNA策略配置模式下，使用以下命令：
ips profile-name
l
profile-name - 指定入侵防御Profile的名称，支持自定义和预定义类型的入侵防御Profile。
取消ZTNA策略与入侵防御Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no ips
绑定僵尸网络防御Profile
当系统安装了僵尸防御许可证时，可以为ZTNA策略绑定僵尸网络防御Profile，对匹配ZTNA策略的流量实
现多种网络攻击的探测，并根据僵尸网络防御Profile的配置对网络攻击执行阻断等操作。关于僵尸网络防御
的详细信息，请参阅僵尸网络防御。
绑定僵尸网络防御Profile，在ZTNA策略配置模式下，使用以下命令：
botnet-c2-prevention profile-name
l
profile-name - 指定僵尸网络防御Profile的名称，支持自定义和预定义类型的僵尸网络防御Profile。
取消ZTNA策略与僵尸网络防御Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no botnet-c2-prevention
绑定垃圾邮件过滤Profile
当系统安装了垃圾邮件过滤许可证时，可以为ZTNA策略绑定垃圾邮件过滤Profile，对匹配ZTNA策略的流
量实现多种网络攻击的探测，并根据垃圾邮件过滤Profile的配置对网络攻击执行阻断等操作。关于垃圾邮件
过滤的详细信息，请参阅垃圾邮件过滤。
绑定垃圾邮件过滤Profile，在ZTNA策略配置模式下，使用以下命令：
antispam profile-name

<!-- 来源页 1826 -->
l
profile-name - 指定垃圾邮件过滤Profile的名称，支持自定义和预定义类型的垃圾邮件过滤Profile。
取消ZTNA策略与垃圾邮件过滤Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no antispam
绑定URL过滤Profile
将URL过滤Profile绑定到ZTNA策略后，系统将会对与ZTNA策略相匹配的流量进行URL检测，并根据URL
过滤Profile的配置对符合过滤条件的URL访问行为进行控制。关于URL过滤的详细信息，请参阅URL过滤。
绑定URL过滤Profile，在ZTNA策略配置模式下，使用以下命令：
url profile-name
l
profile-name - 指定URL过滤Profile的名称。
取消ZTNA策略与URL过滤Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no url
绑定文件过滤Profile
将文件过滤Profile绑定到ZTNA策略后，系统将会对与ZTNA策略相匹配的流量进行传输文件检测，并根据
文件过滤Profile的配置对符合过滤条件的文件进行控制。关于文件过滤的详细信息，请参阅文件过滤。
绑定文件过滤Profile，在ZTNA策略配置模式下，使用以下命令：
dlp profile-name
l
profile-name - 指定文件过滤Profile的名称。
取消ZTNA策略与文件过滤Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no dlp
绑定文件内容过滤Profile
将文件内容过滤Profile绑定到ZTNA策略后，系统将会对与ZTNA策略相匹配的流量进行文件内容检测，并
根据文件内容过滤Profile的配置执行记录日志或者阻断动作。关于文件内容过滤的详细信息，请参阅文件内
容过滤。
绑定文件内容过滤Profile，在ZTNA策略配置模式下，使用以下命令：
file-contentfilter profile-name
l
profile-name - 指定文件内容过滤Profile的名称。
取消ZTNA策略与文件内容过滤Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no file-contentfilter

<!-- 来源页 1827 -->
绑定网页关键字Profile
将网页关键字Profile绑定到ZTNA策略后，系统将会对与ZTNA策略相匹配的流量进行网页关键字检测，并
根据网页关键字Profile的配置执行记录日志或者阻断动作。关于网页关键字的详细信息，请参阅网页关键
字。
绑定网页关键字Profile，在ZTNA策略配置模式下，使用以下命令：
contentfilter profile-name
l
profile-name - 指定内容过滤Profile的名称。
取消ZTNA策略与网页关键字Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no contentfilter
绑定Web外发信息Profile
将Web外发信息Profile绑定到ZTNA策略后，系统将会对与ZTNA策略相匹配的流量进行Web外发信息检
测，并根据Web外发信息Profile的配置执行记录日志或者阻断动作。关于Web外发信息的详细信息，请参
阅Web外发信息。
绑定Web外发信息Profile，在ZTNA策略配置模式下，使用以下命令：
webpost profile-name
l
profile-name - 指定Web外发信息Profile的名称。
取消ZTNA策略与Web外发信息Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no webpost
绑定邮件过滤Profile
将邮件过滤Profile绑定到ZTNA策略后，系统将会对与ZTNA策略相匹配的流量进行邮件过滤检测，并根据
邮件过滤Profile的配置执行记录日志或者阻断动作。关于邮件过滤的详细信息，请参阅邮件过滤。
绑定邮件过滤Profile，在ZTNA策略配置模式下，使用以下命令：
mail profile-name
l
profile-name - 指定邮件过滤Profile的名称。
取消ZTNA策略与邮件过滤Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no mail

<!-- 来源页 1828 -->
绑定应用行为控制Profile
将应用行为控制Profile绑定到ZTNA策略后，系统将会对与ZTNA策略相匹配的流量进行应用行为控制检
测，并根据应用行为控制Profile的配置执行记录日志或者阻断动作。关于应用行为控制的详细信息，请参阅
应用行为控制。
绑定应用行为控制Profile，在ZTNA策略配置模式下，使用以下命令：
behavior profile-name
l
profile-name - 指定应用行为控制Profile的名称。
取消ZTNA策略与应用行为控制Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no behavior
绑定上网行为审计Profile
将上网行为审计Profile绑定到ZTNA策略后，系统将会对与ZTNA策略相匹配的流量进行上网行为审计检
测，并根据上网行为审计Profile的配置执行记录日志或者阻断动作。关于上网行为审计的详细信息，请参阅
上网行为审计。
绑定应用行为控制Profile，在ZTNA策略配置模式下，使用以下命令：
nbr profile-name
l
profile-name - 指定上网行为审计Profile的名称。
取消ZTNA策略与上网行为审计Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no nbr
绑定访问控制Profile
将访问控制Profile绑定到ZTNA策略后，通过ZTNA策略和访问控制规则相结合，在策略规则控制的基础
上，进一步对报文进行细粒度的访问控制，如源/目的MAC地址、DSCP等。关于访问控制的详细信息，请参
阅访问控制。
绑定访问控制Profile，在ZTNA策略配置模式下，使用以下命令：
acl profile-name
l
profile-name - 指定访问控制Profile的名称。
取消ZTNA策略与访问控制Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no acl

<!-- 来源页 1829 -->
绑定SSL代理Profile
将SSL代理Profile绑定到ZTNA策略后，通过ZTNA策略与SSL代理Profile相结合，能够使设备控制并解密
HTTPS流量。关于SSL代理的详细信息，请参阅SSL代理。
绑定SSL代理Profile，在ZTNA策略配置模式下，使用以下命令：
sslproxy profile-name
l
profile-name - 指定SSL代理Profile的名称。
取消ZTNA策略与SSL代理Profile的绑定，在ZTNA策略配置模式下，使用以下命令：
no sslproxy
进入全局ZTNA策略配置模式
ZTNA策略包含一些全局配置，需要在全局ZTNA策略配置模式下完成。进入全局ZTNA策略配置模式，在系
统的全局配置模式下，使用以下命令：
ztna-policy-global
在全局ZTNA策略配置模式下的配置包括：
l
配置默认策略动作
l
开启/关闭ZTNA会话重匹配
l
ZTNA默认策略日志管理
l
修改ZTNA策略排列顺序
配置默认策略动作
用户可以为未匹配到任何已配置ZTNA策略的流量指定缺省的控制动作，系统将按照指定的缺省的控制动作
对此类流量进行处理。默认情况下，系统会拒绝未匹配到任何已配置ZTNA策略的流量访问。
配置ZTNA默认动作，在全局ZTNA策略配置模式下，使用以下命令：
default-action {permit | deny}
l
permit | deny - 指定默认的控制动作，允许访问或拒绝访问
开启/关闭ZTNA会话重匹配
默认情况下，ZTNA会话重匹配功能是开启的。当用户添加、修改或删除ZTNA策略时，已存在的ZTNA会话
匹配的策略可能会发生变化，系统会根据ZTNA会话重匹配功能的配置做出不同的操作：

<!-- 来源页 1830 -->
l
若ZTNA会话重匹配功能为开启状态，系统会为已存在的ZTNA会话重新匹配策略，并且删除匹配的策略
发生变化的会话。
l
若ZTNA会话重匹配功能为关闭状态，系统不会为已存在的ZTNA会话重新匹配策略，原有会话会继续保
持直到超时。
在全局ZTNA策略配置模式下，使用以下命令关闭和开启ZTNA会话重匹配：
l
关闭：session-rematch off
l
开启：no session-rematch off
ZTNA默认策略日志管理
对于命中默认ZTNA策略的流量，用户可以指定是否为其生成日志信息。默认情况下，系统不为此类流量生
成日志信息。生成日志信息，在全局ZTNA策略配置模式下，使用以下命令：
log ztna-policy-default
在全局ZTNA策略配置模式下，使用该命令no的形式恢复默认值：
no log ztna-policy-default
修改ZTNA策略排列顺序
改变ZTNA策略的排列顺序，在全局ZTNA策略配置模式下，使用以下命令：
注意: 不支持修改授权策略的位置。
move {name rule-name | id} {top | bottom | before {name rule-name | id} | after {name rulename | id} }
l
name rule-name | id id – 指定需要修改排列顺序的ZTNA策略ID或者名称。
l
top – 将ZTNA策略移动到所有策略之首。
l
bottom - 将ZTNA策略移动到所有策略的末尾。
l
before {name rule-name | id id} – 将ZTNA策略移动到某个策略ID或名称之前。
l
after {name rule-name | id id} – 将ZTNA策略移动到某个策略ID或名称之后。
查看ZTNA策略配置信息
查看指定ZTNA策略的配置信息，在任意模式下，使用以下命令：
show ztna-policy {name rule-name | id id}

<!-- 来源页 1831 -->
l
name rule-name - 指定ZTNA策略名称。
l
id id - 指定ZTNA策略ID。
查看符合指定过滤条件的ZTNA策略配置信息，在任意模式下，使用以下命令：
show ztna-policy filter { [application-resource application-resource-name] [applicationresource-group application-resource-group-name] [description description] [endpoint-tag
tag-name] [name rule-name] [user user-name] [user-group user-group-name] }
l
application-resource application-resource-name - 显示配置有指定应用资源名称的ZTNA策略
配置信息。
l
application-resource-group application-resource-group-name - 显示配置有指定应用资源组
名称的ZTNA策略配置信息。
l
description description - 显示配置有指定描述信息的ZTNA策略配置信息。
l
endpoint-tag tag-name - 显示配置有指定终端标签名称的ZTNA策略配置信息。
l
name rule-name - 显示配置有指定名称的ZTNA策略配置信息。
l
user user-name - 显示配置有指定用户名的ZTNA策略配置信息。
l
user-group user-group-name - 显示配置有指定用户组的ZTNA策略配置信息。
查看所有ZTNA策略配置信息，在任意模式下，使用以下命令：
show ztna-policy
查看ZTNA策略统计信息
查看命中数排名前10、前20、前50的ZTNA策略统计信息，在任意模式下，使用以下命令：
show ztna-policy statistics-information top {10 | 20 | 50 | all}
l
top {10 | 20 | 50 | all} - 按命中数排名查看ZTNA策略统计信息，包括排名前10、前20和前50。all表
示对所有策略统计信息按照命中数从高到低排名。
查看所有ZTNA策略的统计信息，使用以下命令：
show ztna-policy statistics-information
清除ZTNA策略统计信息
清除指定ZTNA策略的统计信息，在任意模式下，使用以下命令：
clear ztna-policy statistics-information {name rule-name | id id}

<!-- 来源页 1832 -->
l
name rule-name - 指定ZTNA策略名称。
l
id id - 指定ZTNA策略ID。
清除全部ZTNA策略统计信息，使用以下命令：
clear ztna-policy statistics-information all
清除ZTNA默认策略统计信息，使用以下命令：
clear ztna-policy statistics-information default-action
接入地址池
服务端通过地址池给客户端分配IP地址。当客户端连接服务端成功后，服务端会从地址池里取出一个IP地址
与其它相关参数（如DNS服务器地址与WINS服务器地址等）一起分配给客户端。
服务端通过创建和执行IP地址绑定规则来满足客户端的固定IP地址需求。IP地址绑定规则包括IP用户绑定规
则和IP角色绑定规则。IP用户绑定规则将客户端用户与已配置地址池中的某个固定IP地址绑定，当客户端连
接成功后，服务端会将绑定的IP地址分配给客户端；IP角色绑定规则是将角色与已配置地址池中的某一IP地
址范围绑定，当此客户端连接成功后，服务端会从绑定的地址范围中取出一个IP地址分配给客户端。
当服务端通过地址池给客户端分配IP地址时，系统会按照一定的顺序对客户端的IP地址绑定规则进行检查，
决定如何为客户端分配IP地址。
l 检查是否已为客户端用户配置IP用户绑定规则，如果是，则将绑定的IP地址分配给客户端；否则，从非绑定地址
范围中取出一个未被占用的IP分配给客户端。
l 检查是否已为客户端用户配置IP角色绑定规则，如果是，则从绑定的地址范围中取出一个IP地址分配给客户端；
否则，从非绑定地址范围中取出一个未被占用的IP分配给客户端。
注意: IP用户绑定规则中的IP地址和IP角色绑定规则中的IP地址不能重叠。
配置接入地址池
系统支持配置IPv4和IPv6两种类型的接入地址池。
IPv4接入地址池配置
服务端通过地址池给客户端分配IP地址。当客户端连接服务端成功后，服务端会从地址池里取出一个IP地址
与其它相关参数（如DNS服务器地址与WINS服务器地址等）一起分配给客户端。在全局配置模式，使用以
下命令创建地址池：
access-address-pool pool-name

<!-- 来源页 1833 -->
l
pool-name – 指定地址池的名称，取值范围是1到31个字符。
执行该命令后，系统创建指定名称的地址池，并且进入IPv4接入地址池配置模式；如果指定的名称已存在，
则直接进入IPv4接入地址池配置模式。
在全局配置模式下，使用该命令no的形式删除指定的地址池：
no access-address-pool pool-name
在IPv4接入地址池配置模式下可进行如下配置：
l 配置地址池地址范围和网络掩码
l 配置保留地址池
l 配置IP地址绑定规则
l 配置DNS服务器
l 配置WINS服务器
l 配置IP租期功能
l 开启/关闭IP抢占功能
配置地址池地址范围
为地址池配置地址范围和网络掩码，在IPv4接入地址池配置模式下使用以下命令：
address start-ip end-ip netmask A.B.C.D
l
start-ip – 指定IP范围的起始IP地址。
l
end-ip – 指定IP范围的结束IP地址。
l
netmask A.B.C.D – 指定地址池IP范围的网络掩码。
在IPv4接入地址池配置模式下使用该命令no的形式删除配置的IP地址范围：
no address
配置保留地址池
保留地址池中的IP地址为地址池中的部分IP地址，当服务端从地址池里取出IP地址分配给客户端时，需要保
留已经被占用的部分IP地址（如网关、FTP服务器等），不进行分配。配置保留地址池，在IPv4接入地址池
配置模式下使用以下命令：
exclude address start-ip end-ip

<!-- 来源页 1834 -->
l
start-ip – 指定保留地址池的起始IP地址。
l
end-ip – 指定保留地址池的结束IP地址。
在IPv4接入地址池配置模式下，使用该命令no的形式取消保留地址池的配置：
no exclude
配置IP用户绑定规则
配置IP用户绑定规则，在IPv4接入地址池配置模式下使用以下命令：
ip-binding user user-name ip ip-address
l
user user-name – 指定客户端用户名。
l
ip ip-address – 指定绑定的IP地址。此地址必须为地址池中可以分配的地址。
在IPv4接入地址池配置模式下，使用该命令no的形式取消对特定用户IP用户绑定规则的配置：
no ip-binding user user-name
配置IP角色绑定规则
配置IP角色绑定规则，在IPv4接入地址池配置模式下使用以下命令：
ip-binding role role-name ip_range start-ip end-ip
l
role role-name – 指定角色名称。
l
ip_range start-ip end-ip – 指定绑定的IP范围的起始IP地址start-ip和结束IP地址end-ip。此地址
范围必须为地址池中可以分配的地址范围。
在IPv4接入地址池配置模式下，使用该命令no的形式取消对特定角色的IP角色绑定规则的配置：
no ip-binding role role-name
修改IP角色绑定规则排列顺序
一个用户可以绑定到一个或者多个角色，不同角色可以配置不同的IP角色绑定规则。对于绑定到多个角色且
多个角色有相应的IP角色绑定规则的用户，Hillstone设备会对IP角色绑定规则进行顺序查找，然后按照查找
到的相匹配的第一条规则为用户分配地址。默认情况下，系统会将新创建的规则放到所有规则的末尾，管理
员可以移动已有的IP角色绑定规则从而改变规则的排列顺序。改变规则的排列顺序，在IPv4接入地址池配置
模式下使用以下命令：
move role-name1 {before role-name2 | after role-name2 | top | bottom}

<!-- 来源页 1835 -->
l
role–name1 – 指定被移动的IP角色绑定规则的角色名称。
l
before role-name2 – 将IP角色绑定规则移动到某个IP角色绑定规则(角色名称为role-name2的规
则)之前。
l
after role-name2 – 将IP角色绑定规则移动到某个IP角色绑定规则(角色名称为role-name2的规则)
之后。
l
top – 将IP角色绑定规则移动到所有IP角色绑定规则之首。
l
bottom – 将IP角色绑定规则移动到所有IP角色绑定规则的末尾。
配置DNS服务器
配置DNS服务器，在IPv4接入地址池配置模式下使用以下命令：
dns address1 [address2] [address3] [address4]
l
address1 – 指定DNS服务器IP地址。用户最多可配置4个DNS服务器。
在接入地址池配置模式下使用该命令no的形式取消对DNS服务器的指定：
no dns
配置WINS服务器
配置WINS服务器，在IPv4接入地址池配置模式下使用以下命令：
wins address1[ address2]
l
address1 – 指定WINS服务器IP地址。用户最多可配置两个WINS服务器。
在接入地址池配置模式下使用该命令no的形式取消对WINS服务器的指定：
no wins
显示IPv4地址池信息
显示IPv4地址池信息，在任何模式下使用以下命令：
show access-address-pool [pool-name]
l
pool-name – 指定IPv4地址池名称以显示指定的地址池信息。如果不指定该参数值，系统将显示所有
已配置的地址池信息。
以下是显示IPv4地址池具体信息的命令示例：
hostname(config)# show access-address-pool pool_test1
Name: pool_test1

<!-- 来源页 1836 -->
Address range: 3.3.3.1 - 3.3.3.10 （地址池IP地址范围）
Exclude range: 3.3.3.1 - 3.3.3.2 （保留地址池地址范围）
Netmask: 255.255.255.0 （地址池网络掩码）
Wins server: （WINS服务器信息）
wins1: 10.1.1.1
Dns server: （DNS服务器信息）
dns1: 10.10.209.1
IP Lease: enable （IP租期功能：启用）
IP Lease Term: 1 hour(s) （IP租期时间：1小时）
IP Preempt: enable （IP抢占功能：开启）
IP Binding User: （IP用户绑定信息）
test 3.3.3.8
IP Binding Role: （IP角色绑定信息）
role1 3.3.3.3 3.3.3.7
显示IPv4地址池统计信息
显示IPv4地址池统计信息，在任何模式下使用以下命令：
show access-address-pool pool-name statistics
l
pool-name – 指定IPv4地址池名称以显示指定的地址池统计信息。
以下是显示IPv4地址池统计信息的命令示例：
hostname(config)# show access-address-pool pool_test1 statistics
Total Ip Num 10 （地址池中IP地址总数）
Exclude Ip Num 2 （保留IP地址个数）
Fixed Ip Num 6 （绑定IP地址个数）
Used Ip Num 2 （已分配IP地址个数）
Fixed Used Ip Num 0 （已分配绑定IP地址个数）
Free Ip Num 6 （可用地址个数）
====================================
Total Lease IP Num 4 （地址池中处于租期内的IP地址总数）

<!-- 来源页 1837 -->
------------------------------------
Active(In use) IP Num 1 （当前已分配给在线用户、且处于租期内的IP地址个数）
Inactive IP Num 3 （当前可用且处于租期内的IP地址个数）
====================================
IPv6接入地址池配置
IPv6服务端通过地址池给客户端分配IPv6地址。当客户端连接IPv6服务端成功后，服务端会从地址池里取出
一个IPv6地址与其它相关参数（如DNS服务器地址等）一起分配给客户端。在全局配置模式，使用以下命令
创建IPv6地址池：
access-address-pool-ipv6 pool-name
l
pool-name – 指定IPv6地址池的名称，取值范围是1到31个字符。
执行该命令后，系统创建指定名称的IPv6地址池，并且进入IPv6接入地址池配置模式；如果指定的名称已存
在，则直接进入IPv6接入地址池配置模式。在全局配置模式下，使用该命令no的形式删除指定的IPv6地址
池：
no access-address-pool-ipv6 pool-name
在IPv6接入地址池配置模式下可进行如下配置：
l 配置地址池地址范围和前缀长度
l 配置保留地址池
l 配置IP地址绑定规则
l 配置DNS服务器
l 配置IP租期功能
l 开启/关闭IP抢占功能
配置IPv6地址池地址范围
为IPv6地址池配置地址范围和前缀长度，在IPv6接入地址池配置模式下使用以下命令：
address start-ipv6-address end-ipv6-address prefix-len prefix-length
l
start-ipv6-address – 指定IPv6地址范围的起始IPv6地址。
l
end-ipv6-address – 指定IPv6地址范围的结束IPv6地址。
l
prefix-len prefix-length – 指定IPv6地址池IPv6地址范围的前缀长度。取值范围是111到128。
在IPv6接入地址池配置模式下使用该命令no的形式删除配置的IPv6地址范围：

<!-- 来源页 1838 -->
no address
配置保留地址池
保留地址池中的IPv6地址为地址池中的部分IPv6地址，当服务端从地址池里取出IPv6地址分配给客户端时，
需要保留已经被占用的部分IPv6地址（如网关、FTP服务器等），不进行分配。配置保留地址池，在IPv6接
入地址池配置模式下使用以下命令：
exclude address start-ipv6-address end-ipv6-address
l
start-ipv6-address – 指定保留地址池的起始IPv6地址。
l
end-ipv6-address – 指定保留地址池的结束IPv6地址。
在IPv6接入地址池配置模式下使用该命令no的形式取消保留地址池的配置：
no exclude
配置IP用户绑定规则
配置IP用户绑定规则，在IPv6接入地址池配置模式下使用以下命令：
ip-binding user user-name ip ipv6-address
l
user user-name – 指定客户端用户名。
l
ip ipv6-address – 指定绑定的IPv6地址。此地址必须为IPv6地址池可以分配的地址。
在IPv6接入地址池配置模式下使用该命令no的形式取消对特定用户IP用户绑定规则的配置：
no ip-binding user user-name
配置IP角色绑定规则
配置IP角色绑定规则，在IPv6接入地址池配置模式下使用以下命令：
ip-binding role role-name ip_range start-ipv6-address end-ipv6-address
l
role role -name – 指定角色名称。
l
ip_range start-ipv6-address end-ipv6-address – 指定绑定的IPv6地址范围的起始IPv6地址
start-ipv6-address和结束IPv6地址end-ipv6-address。此地址范围必须为IPv6地址池中可以分配
的地址范围。
在IPv6接入地址池配置模式下使用该命令no的形式取消对特定角色的IP角色绑定规则的配置：
no ip-binding role role-name

<!-- 来源页 1839 -->
修改IP角色绑定规则排列顺序
一个用户可以绑定到一个或者多个角色，不同角色可以配置不同的IP角色绑定规则。对于绑定到多个角色且
多个角色有相应的IP角色绑定规则的用户，设备会对IP角色绑定规则进行顺序查找，然后按照查找到的相匹
配的第一条规则为用户分配地址。默认情况下，系统会将新创建的规则放到所有规则的末尾，管理员可以移
动已有的IP角色绑定规则从而改变规则的排列顺序。改变规则的排列顺序，在IPv6接入地址池配置模式下使
用以下命令：
move role-name1 {before role-name2 | after role-name2| top | bottom}
l
role-name1 – 指定被移动的IP角色绑定规则的角色名称。
l
before role-name2 – 将IP角色绑定规则移动到某个IP角色绑定规则(角色名称为role-name2的规
则)之前。
l
after role-name2 – 将IP角色绑定规则移动到某个IP角色绑定规则(角色名称为role-name2的规则)
之后。
l
top – 将IP角色绑定规则移动到所有IP角色绑定规则之首。
l
bottom – 将IP角色绑定规则移动到所有IP角色绑定规则的末尾。
配置DNS服务器
配置DNS服务器，在IPv6接入地址池配置模式下使用以下命令：
dns ipv6-address1 [ipv6-address2] [ipv6-address3] [ipv6-address4]
l
ipv6-address1 – 指定DNS服务器IP地址。用户最多可配置4个DNS服务器。
在IPv6接入地址池配置模式下使用该命令no的形式取消对DNS服务器的指定：
no dns
显示IPv6地址池信息
显示IPv6地址池信息，在任何模式下使用以下命令：
show access-address-pool-ipv6 [pool-name]
l
pool-name – 指定IPv6地址池名称以显示指定的地址池信息。如果不指定该参数值，系统将显示所有
已配置的IPv6地址池信息。
以下是显示IPv6地址池具体信息的命令示例：
hostname(config)# show access-address-pool-ipv6
===============================================================

<!-- 来源页 1840 -->
Name Address range Prefix length
-----------------------------------------------------------------------
1-ipv6-pool 1000:5678:2222~ - 1000:5678:2222~112
2-ipv6-pool 1001:5678:2222~ - 1001:5678:2222~112
3-ipv6-pool 1002:5678:2222~ - 1002:5678:2222~112
4-ipv6-pool 1003:5678:2222~ - 1003:5678:2222~112
5-ipv6-pool 1004:5678:2222~ - 1004:5678:2222~112
6-ipv6-pool 1005:5678:2222~ - 1005:5678:2222~112
===============================================================
hostname(config)# show access-address-pool 2-ipv6-pool
Name: 2-ipv6-pool
Address range: 1001:5678:2222:3333:5555:ABCD:EFAB:1000 -
1001:5678:2222:3333:5555:ABCD:EFAB:3000 （IPv6地址池IPv6地址范围）
Exclude range: 1001:5678:2222:3333:5555:ABCD:EFAB:1000 -
1001:5678:2222:3333:5555:ABCD:EFAB:2000 （保留IPv6池地范围）
prefix length: 112（地址池前缀长度）
Dns server: （DNS服务器信息）
IP Lease: enable （IP租期功能：启用）
IP Lease Term: 1 hour(s) （IP租期时间：1小时）
IP Preempt: enable （IP抢占功能：开启）
IP Binding User:
IP Binding Role:
显示IPv6地址池统计信息
显示IPv6地址池统计信息，在任何模式下使用以下命令：
show access-address-pool pool-name statistics
l
pool-name – 指定IPv6地址池名称以显示指定的地址池统计信息。
以下是显示地址池统计信息的命令示例：
hostname(config)# show access-address-pool 2-ipv6-pool statistics

<!-- 来源页 1841 -->
Total Ip Num 10 （地址池中IPv6地址总数）
Exclude Ip Num 2 （保留IPv6地址个数）
Fixed Ip Num 6 （绑定IPv6地址个数）
Used Ip Num 2 （已分配IPv6地址个数）
Fixed Used Ip Num 0 （已分配绑定IPv6地址个数）
Free Ip Num 6 （可用IPv6地址个数）
====================================
Total Lease IP Num 4 （地址池中处于租期内的IP地址总数）
------------------------------------
Active(In use) IP Num 1 （当前已分配给在线用户、且处于租期内的IP地址个数）
Inactive IP Num 3 （当前可用且处于租期内的IP地址个数）
====================================
配置IP租期功能
IP租期功能可为用户分配固定的私网IP，确保同一用户在租期内每次上线均获得相同的私网IP地址。该功能
适用于需要保持IP连续性、基于IP进行行为审计的场景，如运维人员远程办公时的操作日志追踪。
该功能默认处于禁用状态。功能禁用时，用户注销SSL VPN/ZTNA登录后（即用户下线后），系统会立即回
收并重新分配其占用的IP地址。
若开启该功能并配置租期时长，用户下线后，系统不会立即回收其占用的IP地址，而是按配置时长予以保
留。保留期内，同一用户再次登录SSL VPN/ZTNA，系统会优先分配相同的IP地址；超过保留期后，该IP地
址才被释放，供其他用户使用。
开启/关闭IP租期功能，在IPv4或IPv6接入地址池配置模式下使用以下命令：
l
开启：ip-lease enable
l
关闭：ip-lease disable
开启IP租期功能后，若不配置租期时长，系统将默认设置为1小时。
配置租期时长，在IPv4或IPv6接入地址池配置模式下使用以下命令：
ip-lease term {day time-value | hour time-value}
l
day time-value – 以“天”为单位设置租期时长，取值范围为1-365天。
l
hour time-value - 以“小时”为单位设置租期时长，取值范围为1-8760小时。

<!-- 来源页 1842 -->
开启/关闭IP抢占功能
开启IP租期功能后，用户可选择同时开启IP抢占功能，以提高网络接入的优先性。
启用IP抢占功能后，当新用户登录SSL VPN/ZTNA时，系统会优先分配空闲IP地址；若无空闲IP，则会抢占
已被注销但仍处于保留期内的IP地址。抢占时，优先选择保留期剩余时间最短的IP。该功能默认关闭。
开启/关闭IP抢占功能，在IPv4或IPv6接入地址池配置模式下使用以下命令：
l
开启：ip-preempt enable
l
关闭：ip-preempt disable
查看用户与IP映射关系
用户可查看指定地址池中用户与IP的映射关系，包括用户名、分配的IP地址以及用户最后一次注销SSL
VPN/ZTNA登录的时间。通过查看该信息，用户可判断IP是否处于租期保留状态，也可判断用户重新登录
SSL VPN/ZTNA时能否重新获得相同的IP。
用户可在任意模式下，执行以下命令，查看用户与IP的映射关系表：
show {access-address-pool | access-address-pool-ipv6} pool-name ip-lease
l
access-address-pool - 用于查看用户与IPv4地址的映射关系表。
l
access-address-pool-ipv6 - 用于查看用户与IPv6地址的映射关系表。
l
pool-name - 指定IPv4或IPv6地址池的名称。
返回示例：
hostname# show access-address-pool test ip-lease
total number: 1
=============================================
User Name       User IP(v4)             Logout Time
-------------------------------------------------------
User1                 17.1.1.2               2026-06-08 15:04
=============================================
显示信息
说明
User Name
登录SSL VPN/ZTNA的用户名称。
User IP(v4)/User
IP(v6)
系统从指定地址池中分配给该用户的私网IP地址。

<!-- 来源页 1843 -->
显示信息
说明
Logout Time
用户最近一次注销SSL VPN/ZTNA登录的时间（即用户最近一次下线的时间）。若
用户当前已登录SSL VPN/ZTNA（在线），该字段显示为“/”；若当前用户已下
线，该字段则显示为上次下线的时间。
ZTNA实例配置
创建ZTNA实例，在全局配置模式下，使用以下命令：
tunnel ztna instance-name [intranet | remote]
l
instance-name - 指定ZTNA实例的名称，取值范围是1到31个字符。
l
intranet | remote - 指定ZTNA实例类型，可以为内网接入（intranet）或者远程访问（remote）。
默认为远程访问（remote）。
执行该命令后，系统创建指定名称的ZTNA实例，并且进入相应的实例配置模式，包括内网接入ZTNA实例配
置模式或者远程访问ZTNA实例配置模式；如果指定的名称已存在，则直接进入此ZTNA实例的配置模式。在
全局配置模式下，使用该命令no的形式删除指定的ZTNA实例：
no tunnel ztna instance-name {intranet | remote}
注意: 不同平台支持创建的ZTNA实例数量不同，请以实际平台为准。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，用户可以进行如下配置：
l 启用/禁用ZTNA实例
l 指定服务类型
l 指定策略模式
l 指定接入地址池（仅适用于远程访问ZTNA实例）
l 指定服务端接口
l 指定SSL协议
l 指定PKI信任域
l 指定加密信任域
l 指定隧道密码套件（仅适用于远程访问ZTNA实例）
l 指定AAA服务器
l 指定SSL端口号

<!-- 来源页 1844 -->
l 配置传输协议（仅适用于远程访问ZTNA实例）
l 配置ZTNA隧道路由（仅适用于远程访问ZTNA实例）
l 配置防重放功能（仅适用于远程访问ZTNA实例）
l 配置分片功能（仅适用于远程访问ZTNA实例）
l 配置强制超时时间（仅适用于内网接入ZTNA实例）
l 配置空闲时间（仅适用于远程访问ZTNA实例）
l 配置强制下线时间表
l 配置用户同名登录功能
l 配置多网关地址
l 配置URL重定向功能
l 开启/关闭允许浏览器下载客户端功能
l 绑定远程访问ZTNA实例到隧道接口（仅适用于远程访问ZTNA实例）
l 配置客户端USB Key证书认证
l 配置ZTNA Portal页面标题
l 配置ZTNA Portal页面的中英文标题
l 开启/关闭ZTNA Portal页面智能弹窗功能
启用/禁用ZTNA实例
ZTNA实例处于启用状态且配置完整的情况下，客户端可以正常接入。若客户端已接入到ZTNA，禁用ZTNA
实例，已连接的客户端用户将会被下线。
启用或禁用ZTNA实例，在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用以下命
令：
启用：enable
禁用：disable
指定服务类型
指定ZTNA实例的服务类型，包括IPv4、IPv6或双栈。仅远程访问ZTNA实例支持配置为双栈类型。IPv6和
双栈类型仅当系统版本为IPv6版本时可配，默认情况下，ZTNA实例的服务类型为IPv4。在内网接入ZTNA
实例配置模式或者远程访问ZTNA实例配置模式下，使用以下命令：
service-type {ipv4 | ipv6 | dual-stack}

<!-- 来源页 1845 -->
l
ipv4 | ipv6 | dual-stack –指定ZTNA实例的服务类型，包括IPv4、IPv6或双栈。
相关概念：
双栈是一种网络技术，它允许在一个网络设备上同时运行IPv4和IPv6两种网络协议栈，使得网络设备能
够在IPv4和IPv6网络间进行无缝切换和通信。
指定策略模式
指定ZTNA实例的策略模式，在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用以下
命令：
policy-match {gateway-config-enable {security-policy | ztna-policy} | global-config-enable}
l
gateway-config-enable security-policy - 指定ZTNA实例的策略模式为安全策略模式。在安全策
略模式下，该网关的ZTNA用户发起的流量仅匹配安全策略。
l
gateway-config-enable ztna-policy - 指定ZTNA实例的策略模式为ZTNA策略模式。在ZTNA策略
模式下，该网关的ZTNA用户发起的流量仅匹配ZTNA策略。
l
global-config-enable - 指定ZTNA实例的策略模式为全局配置模式。在全局配置模式下，对于该网
关的ZTNA用户发起的流量，若目的安全域为WAN安全域则匹配安全策略，其他流量则匹配ZTNA策略。
默认为全局配置模式。
指定接入地址池
该配置项仅适用于远程访问ZTNA实例。
绑定IPv4地址池，在远程访问ZTNA实例配置模式下，使用以下命令：
access-address-pool pool-name
l
pool-name - 指定已配置的IPv4地址池名称。
在远程访问ZTNA实例配置模式下，使用该命令no的形式解绑指定的IPv4地址池：
no access-address-pool
绑定IPv6地址池，在远程访问ZTNA实例配置模式下，使用以下命令：
access-address-pool-ipv6 pool-name
l
pool-name - 指定已配置的IPv6地址池名称。
在远程访问ZTNA实例配置模式下，使用该命令no的形式解绑指定的IPv6地址池：
no access-address-pool-ipv6

<!-- 来源页 1846 -->
注意:
l
仅可以为IPv4服务类型的ZTNA实例指定IPv4地址池。
l
仅可以为IPv6服务类型的ZTNA实例指定IPv6地址池。
指定服务端接口
客户端通过HTTPS协议访问服务端接口，每个ZTNA实例可以绑定最多8个接口。绑定服务端ZTNA接口，在
内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用以下命令：
interface interface-name
l
interface-name - 指定服务端接口名称。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用该命令no的形式解绑指定的出接
口：
no interface interface-name
指定SSL协议
为ZTNA实例指定SSL协议，在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用以下
命令：
ssl-protocol { tlsv1 | tlsv1.2 | tlsv1.3 | gmssl | any}
l
tlsv1 – 指定使用TLSv1协议。
l
tlsv1.2 – 指定使用TLSv1.2协议。此为系统默认配置。
l
tlsv1.3 – 指定使用TLSv1.3协议。
l
gmssl – 指定使用国密GMSSLv1.0协议。当协议为此选项时，PKI信任域和加密信任域必须选择配置含
有SM2类型密钥的信任域，加密算法建议优先选择SM4，Hash算法建议优先选择SM3。
l
any – 指定使用TLSv1、TLSv1.1、TLSv1.2或者TLSv1.3任何一种协议。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用该命令no的形式恢复SSL协议的默
认值：
no ssl-protocol
如果服务端指定的SSL协议类型为tlsv1.2或者any，在客户端进行数字证书认证前，需要用户将要导入到浏
览器中的软证书或者USB Key中的.pfx格式证书进行处理，使得证书能够支持tlsv1.2协议，以便用户在使用
“用户名/密码+数字证书”或者“数字证书”认证方式进行认证时，能够连接成功。处理证书前，请先准备
一台安装了OpenSSL1.0.1版本及以上的PC（Windows或Linux系统均可）。以文件名称为oldcert.pfx的
证书为例，处理步骤如下：

<!-- 来源页 1847 -->
1.
在OpenSSL软件界面中，输入以下命令将.pfx格式的证书转换为.pem格式的证书。openssl pkcs12 –
in oldcert.pfx –out cert.pem
2.
继续输入下面的命令将.pem格式的证书转换为支持tlsv1.2的.pfx格式证书。openssl pkcs12 –
export–in cert.pem –out newcert.pfx –CSP “Microsoft Enhanced RSA and AES
Cryptographic Provider”
3.
将新生成的.pfx格式证书导入到浏览器或者USB Key。
指定PKI信任域
此处指定的PKI信任域用于HTTPS访问认证。为ZTNA指定PKI信任域，在内网接入ZTNA实例配置模式或者
远程访问ZTNA实例配置模式下，使用以下命令：
trust-domain trust-domain-name
l
trust-domain-name – 指定系统中已配置的PKI信任域的名称。默认信任域为trust_domain_
default。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用该命令no的形式恢复信任域的默
认配置：
no trust-domain
关于如何创建PKI信任域，请参阅PKI配置部分。
指定加密信任域
此处为ZTNA指定加密信任域，加密信任域用于国密SSL协商。在内网接入ZTNA实例配置模式或者远程访问
ZTNA实例配置模式下，使用以下命令：
trust-domain-enc trust-domain-name
l
trust-domain-name – 指定系统预定义的用于国密SSL协商的加密信任域的名称。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用该命令no的形式删除加密信任域
的配置：
no trust-domain-enc
指定隧道密码套件
该配置项仅适用于远程访问ZTNA实例。隧道密码套件包括加密算法、验证算法和压缩算法。为ZTNA指定隧
道密码套件，在远程访问ZTNA实例配置模式下，使用以下命令：

<!-- 来源页 1848 -->
tunnel-cipher encryption {null | des | 3des | aes | aes192 | aes256 | sm4} hash {null | md5 |
sha | sha256 |sha384 | sha512 | sm3} [compression defl]
l
encryption {null | des | 3des | aes | aes192 | aes256 | sm4} – 指定加密算法。默认加密算法为
AES。null表示不使用加密功能。关于加密算法的详细描述，请参阅加密算法。
l
hash {null | md5 | sha | sha256 | sha384 | sha512| sm3} – 指定验证算法。默认验证算法为
MD5。null表示不使用验证功能。关于验证算法的详细描述，请参阅验证算法。
l
compression defl – 指定DEFLATE压缩算法。默认无压缩算法。关于压缩算法的详细描述，请参阅压
缩算法。
在远程访问ZTNA实例配置模式下，使用该命令no的形式恢复隧道密码套件的默认配置：
no tunnel-cipher
指定AAA服务器
此处指定的AAA服务器为进行客户端用户身份认证的AAA服务器。指定AAA服务器，在内网接入ZTNA实例
配置模式或者远程访问ZTNA实例配置模式下，使用以下命令：
aaa-server aaa-server-name [domain domain-name] [keep-domain-name]
l
aaa-server-name – 指定AAA服务器的名称。
l
domain domain-name – 为AAA服务器指定域名以区分不同的AAA服务器，取值范围是1到31个字
符。
l
keep-domain-name – 指定该参数后，用于身份认证的用户名将验证域名。
注意: 仅Windows/macOS/Linux/国产操作系统的Hillstone Secure Connect客户端支持
OAuth2认证方式。OAuth2服务器不支持用户域名验证功能（keep-domain-name）。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用该命令no的形式取消对AAA服务
器的指定：
no aaa-server aaa-server-name [domain domain-name]
指定SSL端口号
SSL端口号用于客户端访问服务端时使用。指定SSL端口号，在内网接入ZTNA实例配置模式或者远程访问
ZTNA实例配置模式下，使用以下命令：
ssl-port port-number

<!-- 来源页 1849 -->
l
port-number – 指定SSL端口号。取值范围是1到65535。绑定到同一个接口的ZTNA实例需配置不同
的SSL端口号，并避免与其他服务使用的SSL端口号重复。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用该命令no的形式删除SSL端口号：
no ssl-port
配置传输协议
该配置项仅适用于远程访问ZTNA实例。系统支持通过TCP或UDP协议进行ZTNA数据传输，默认使用UDP协
议，端口为4433。配置传输协议及端口，在远程访问ZTNA实例配置模式下，使用以下命令：
transport-service {tcp | udp} port-number
l
tcp | udp - 指定使用TCP或UDP协议进行数据传输。
l
port-number –指定数据通道使用的端口号。取值范围是1到65535。
在远程访问ZTNA实例配置模式下，使用该命令no的形式删除传输协议和端口配置：
no transport-service {tcp | udp}
配置ZTNA隧道路由
ZTNA隧道路由相关配置仅适用于远程访问ZTNA实例。ZTNA隧道路由是指通过IPv4/IPv6类型的ZTNA隧
道到指定网段/域名的路由。客户端接收到指定网段后，生成到达指定网段的路由条目；接收到指定域名后，
根据域名解析结果，生成到达域名所在地址的路由条目。
注意: 当配置双栈类型的ZTNA时，需指定IPv4和IPv6 ZTNA隧道路由。
配置到指定IPv4网段的ZTNA隧道路由
仅可以为IPv4或双栈服务类型的ZTNA实例配置IPv4 ZTNA隧道路由。使用网段方式配置IPv4 ZTNA隧道路
由，在远程访问ZTNA实例配置模式下，使用以下命令：
split-tunnel-route ip-address/netmask [metric metric-number] [user-group aaa-server_
name group_name | role role_name]
l
ip-address/netmask – 指定目的地址和掩码。
l
metric metric-number – 指定路由的度量值。默认值是35。取值范围是1到9999。
l
user-group aaa-server_name group_name – 指定用户组所属的认证服务器名称和用户组名称。
指定后，仅该用户组里的用户可以访问隧道路由中的指定网段。说明：指定该参数前请先创建用户组，
具体方法请参阅“用户组配置”（系统管理> 系统用户管理> 用户组配置）。

<!-- 来源页 1850 -->
l
role role_name] – 指定角色名称。指定后，仅该角色对应的用户可以访问隧道路由中的指定网段。说
明：指定该参数前请先创建角色，具体方法请参阅“角色配置”（系统管理> 系统用户管理> 角色配
置）。
用户可以配置多条该命令添加多条路由。
在远程访问ZTNA实例配置模式下，使用该命令no的形式删除指定的IPv4路由：
no split-tunnel-route ip-address/netmask [metric metric-number]
配置到指定IPv6网段的ZTNA隧道路由
仅可以为IPv6或双栈服务类型的ZTNA实例配置IPv6 ZTNA隧道路由。使用网段方式配置IPv6 ZTNA隧道路
由，在远程访问ZTNA实例配置模式下，使用以下命令：
split-tunnel-route-ipv6 ipv6-address/prefix [metric metric-number] [user-group aaaserver_name group_name | role role_name]
l
ipv6-address/prefix – 指定IPv6类型的目的地址和前缀长度。
l
metric metric-number – 指定路由的度量值。默认值是35。取值范围是1到9999。
l
user-group aaa-server_name group_name – 指定用户组所属的认证服务器名称和用户组名称。
指定后，仅该用户组里的用户可以访问隧道路由中的指定网段。说明：指定该参数前请先创建用户组，
具体方法请参阅“用户组配置”（系统管理> 系统用户管理> 用户组配置）。
l
role role_name] – 指定角色名称。指定后，仅该角色对应的用户可以访问隧道路由中的指定网段。说
明：指定该参数前请先创建角色，具体方法请参阅“角色配置”（系统管理> 系统用户管理> 角色配
置）。
用户可以配置多条该命令添加多条IPv6路由。
在远程访问ZTNA实例配置模式模式下，使用该命令no的形式删除指定的IPv6路由：
no split-tunnel-route-ipv6 ipv6-address/prefix [metric metric-number]
配置到指定域名的ZTNA隧道路由
使用域名方式配置IPv4和IPv6 ZTNA隧道路由后，系统将域名下发给客户端。客户端根据域名解析结果，生
成到达域名所在地址的路由条目。配置到指定域名的ZTNA隧道路由，在远程访问ZTNA实例配置模式下，使
用以下命令：
domain-route {disable | enable | max-entries value | url}
l
disable – 不下发域名到客户端。此为系统默认设置。
l
enable – 下发域名到客户端。

<!-- 来源页 1851 -->
l
max-entries value – 指定客户端可以根据域名解析后地址所生成的最大路由条目数。默认值是
1000，取值范围是1到10000。
l
url – 指定域名。每次可添加一个，支持最多64个域名。每个域名的字符串长度不得超过63个字符。域
名末尾不能为“.”，不支持通配符，且不支持过于宽泛的URL，比如：“.com”、“com”。
在远程访问ZTNA实例配置模式下，使用该命令no的形式删除指定的路由：
no domain-route url
注意: 域名下发功能和ZTNA专线功能互斥，不能同时使用。关于如何配置ZTNA专线功能，请参阅
启用ZTNA专线。
启用ZTNA专线
系统支持ZTNA专线功能，该功能默认关闭。启用该功能后，用户在成功登录ZTNA后仅能访问隧道路由中指
定网段的内网资源，不能访问互联网资源。
注意:
l
支持ZTNA专线功能的客户端版本包括：Windows系统ZTNA客户端最新版本、macOS系统
ZTNA客户端最新版本、Linux系统ZTNA客户端最新版本。
l
ZTNA专线功能和域名下发功能互斥，不能同时使用。关于如何配置域名下发功能，请参阅配
置到指定域名的ZTNA隧道路由。
l
启用ZTNA专线功能后，建议不要在隧道路由中配置默认路由。
启用或者禁用ZTNA专线功能，在远程访问ZTNA实例配置模式下，使用以下命令：
dedicated-tunnel {enable | disable}
l
enable - 启用ZTNA专线功能。
l
disable -禁用ZTNA专线功能。
配置防重放功能
该配置项仅适用于远程访问ZTNA实例。防重放（Anti-Replay）指防止恶意用户通过重复发送捕获到的数
据包所进行的攻击，即接收方会拒绝旧的或重复的数据包。配置防重放功能，在远程访问ZTNA实例配置模
式下，使用以下命令：
anti-replay {32 | 64 | 128 | 256 | 512}

<!-- 来源页 1852 -->
l
32 – 指定防重放的窗口为32。该数值为系统的默认数值。
l
64 – 指定防重放的窗口为64。
l
128 – 指定防重放的窗口为128。
l
256 – 指定防重放的窗口为256。
l
512 – 指定防重放的窗口为512。
在网络状况较差时，例如存在严重乱序现象等，请选择较大的窗口。
在远程访问ZTNA实例配置模式下，使用该命令no的形式恢复默认防重放窗口：
no anti-replay
配置分片功能
该配置项仅适用于远程访问ZTNA实例。用户可以指定是否允许转发设备将包进行分片处理。配置分片功
能，在远程访问ZTNA实例配置模式下，使用以下命令：
df-bit {copy | clear | set}
l
copy – 直接从发包端拷贝IP包的DF选项。该选项为系统默认选项。
l
clear – 允许转发设备对包做分片处理。
l
set – 不允许转发设备对包做分片处理。
在远程访问ZTNA实例配置模式下，使用该命令no的形式恢复系统的默认设置：
no df-bit
配置强制超时时间（内网接入）
ZTNA客户端接入内网成功后，当用户在线时长达到配置的强制超时时间时，系统会踢出用户，强制用户下
线。
配置强制超时时间，在内网接入ZTNA实例配置模式下，使用以下命令：
force-timeout time-value
l
time-value – 指定强制超时时间，单位为分钟。默认值是10080分钟。取值范围是10到10080分钟。
在内网访问实例配置模式下，使用该命令no的形式恢复默认值：
no force-timeout

<!-- 来源页 1853 -->
配置强制超时时间（远程访问）
强制超时时间指当ZTNA客户端在持续访问受保护资源的过程中，系统允许其保持连接的最长时间。当连接
时长达到设定值，系统会自动断开连接，需重新登录才能继续访问资源。它的主要作用是避免客户端长时间
保持连接带来的潜在安全风险，满足“非闲时自动断连”的合规要求。
配置强制超时时间，在远程访问ZTNA实例配置模式下，使用以下命令：
force-kickout {enable | disable | time time-value}
l
enable - 启用强制超时时间。
l
disable - 禁用强制超时时间。系统默认为该配置项。
l
time time-value – 指定强制超时时间值。配置前，需先启用强制超时时间，设置的超时值才会生效。
单位为分钟。默认值是10080分钟。取值范围是10到10080分钟。
配置空闲时间
该配置项仅适用于远程访问ZTNA实例。空闲时间指客户端与服务端在无流量状态下能够保持连接状态的最
长时间，超出空闲时间后，服务端将断开与客户端的连接。配置空闲时间，在远程访问ZTNA实例配置模式
下，使用以下命令：
idle-time time-value
l
time-value – 指定空闲时间，单位为分钟。默认值是30分钟。取值范围是1到1500分钟。
在远程访问ZTNA实例配置模式下，使用该命令no的形式恢复空闲时间的默认值：
no idle-time
配置强制下线时间表
为ZTNA实例指定强制下线时间表，时间表生效后，系统将按照时间表周期计划或绝对计划的起始时间强制
在线用户下线。配置强制下线时间表，在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，
使用以下命令：
kickout-all-user schedule schedule-name
l
schedule-name - 指定时间表名称。系统将在时间表的起始时间强制用户在线。
注意:
l
起始时间与结束时间不能相同，否则时间表无法生效。
l
时间表生效后再上线的用户会在时间表下一次生效时被强制下线。

<!-- 来源页 1854 -->
配置用户同名登录功能
用户同名登录功能指允许同一个用户在多个地点同时登录认证。开启用户同名登录功能，在内网接入ZTNA
实例配置模式或者远程访问ZTNA实例配置模式下，使用以下命令：
allow-multi-logon
执行该命令后，开启用户同名登录功能，并且不对同一用户名的同时登录个数做限制。用户可以在内网接入
ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，通过使用以下命令指定用户同名登录个数：
allow-multi-logon number number
l
number – 指定用户同名登录个数。范围是1到99999999。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用以下命令no的形式关闭用户同名
登录功能：
no allow-multi-logon
配置多网关地址
ZTNA支持配置备选网关供客户端选择建立ZTNA连接时的最优网关，ZTNA服务端配置了备选网关时，
ZTNA客户端可以开启网关探测功能选择需要连接的ZTNA网关。
开启网关探测功能后，用户登录时ZTNA客户端会向登录的网关获取备选网关列表，并对备选网关进行链路
探测，然后选择与链路质量最优的网关建立连接。建立连接后，ZTNA客户端会每隔30分钟更新一次链路质
量探测结果。如果发生连接中断或用户登录失败，客户端会自动切换到链路质量最优的备选网关重新建立连
接。
配置备选网关，在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用以下命令：
gateway gateway-name {ipv4 ipv4-address | ipv6 ipv6-address | domain string}
l
gateway-name - 指定备选网关的名称。取值范围是1到31个字符。
l
ipv4 ipv4-address - 指定备选网关的IPv4地址。
l
ipv6 ipv6-address - 指定备选网关的IPv6地址。
l
domain string - 指定备选网关的域名。取值范围是1到255个字符，但是在两个句点（.）之间，最多
可以有63个字符。
重复执行该命令可以配置多个备选网关。
删除指定的备选网关，在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用以下命令：
no gateway gateway-name

<!-- 来源页 1855 -->
注意: 备选网关上的ZTNA配置需要和主网关上的保持一致。
配置URL重定向功能
URL重定向功能是指在ZTNA服务端配置重定向的URL，客户端认证成功后将自动跳转到指定URL的页面。默
认情况下，URL重定向功能是关闭的。配置URL重定向功能，在内网接入ZTNA实例配置模式或者远程访问
ZTNA实例配置模式下，使用以下命令：
redirect-url url title name
l
url – 指定认证成功后，客户端自动跳转页面的URL，取值范围为1到255字符。系统支持HTTP
（http://）和HTTPS（https://）两种类型的URL。
l
title name – 指定重定向URL的描述信息，范围为1到31字符。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用该命令no的形式取消URL重定向
功能：
no redirect-url
URL内容格式
根据重定向页面类型的不同，StoneOS支持内容符合下列格式的URL输入，以HTTP类型URL为例：
l UTF-8编码格式的页面：输入“URL”+“username=$USER&password=$PWD”。比如，
“http://www.abc.com/oa/login.do?username=$USER&password=$PWD”。
l GB2312编码格式的页面：输入“URL”+“username=$GBUSER&password=$PWD”。比如，
“http://www.abc.com/oa/login.do?username=$GBUSER&password=$PWD”。
l 其它页面：直接输入URL。比如，“http://www.abc.com”。
开启/关闭允许浏览器下载客户端功能
浏览器下载功能指通过浏览器Web页面的方式下载ZTNA客户端，默认情况下，该功能为开启状态。当关闭
该功能后，用户可通过山石网科官网下载ZTNA客户端。
开启允许浏览器下载客户端功能，在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用
以下命令：
client-download-page enable
关闭允许浏览器下载客户端功能，在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用
以下命令：
client-download-page disable

<!-- 来源页 1856 -->
绑定远程访问ZTNA实例到隧道接口
该配置项仅适用于远程访问ZTNA实例。配置好的远程访问ZTNA实例需要绑定到隧道接口，才能够生效。绑
定远程访问ZTNA实例到隧道接口，在隧道接口配置模式下，使用以下命令：
tunnel ztna instance-name
l
instance-name – 指定系统中已配置的远程访问ZTNA实例的名称。一个隧道接口最多只能绑定一个远
程访问ZTNA实例。
在隧道接口配置模式下使用该命令no的形式取消隧道接口与远程访问ZTNA实例的绑定：
no tunnel ztna instance-name
配置客户端USB Key证书认证
Hillstone设备支持客户端USB Key证书认证。只要用户持有的USB Key支持标准的Windows SDK
（Certificate Store Functions），并且存储合法的证书，就能通过认证进而实现网络连通的目的。
USB Key证书认证功能支持以下两种认证方式：
l 用户名/密码+ USB Key：ZTNA用户需要持有存储正确数字证书的USB Key，并且在登录时输入正确的用户名、
密码和USB Key用户口令，才能通过认证；
l 只用USB Key：ZTNA用户需要持有存储正确数字证书的USB Key，并且在登录时输入正确的USB Key用户口
令，即可通过认证，无需输入用户名和密码。
注意: 当认证方式为“只用USB Key”时，
l
系统可以根据USB Key数字证书中的证书名称（证书CN字段）或者组织机构（证书OU字段）
为认证成功的用户映射相应的角色。关于如何进行证书名称或者组织机构的角色映射，请参阅
系统管理的配置角色映射规则部分。
l
系统不支持允许本地用户修改密码。
l
系统不支持配置短信口令认证功能。
l
如果移除USB Key，客户端不会自动重连。
实现USB Key证书认证功能，用户需在服务端配置以下功能：
l 开启USB Key证书认证功能
l 导入USB Key证书相应CA证书到信任域
l 配置USB Key证书相应CA证书的信任域

<!-- 来源页 1857 -->
开启USB Key证书认证功能
默认情况下，服务端的USB Key证书认证功能为关闭状态，用户可以在内网接入ZTNA实例配置模式或者远
程访问ZTNA实例配置模式下，使用以下命令开启USB Key证书认证功能：
client-cert-authentication [usbkey-only]
l
usbkey-only – 指定USB Key证书认证方式为“只用USB Key”。如不指定该参数，认证方式为“用户
名/密码+ USB Key”。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用该命令no的形式关闭USB Key证
书认证功能：
no client-cert-authentication [usbkey-only]
导入USB Key证书相应CA证书到信任域
用户可以通过多种方式（FTP、TFTP和USB）实现CA证书到信任域的导入，在执行模式下使用以下命令：
import pki trust-domain trust-domain-name cacert from {ftp server ip-address [user username password password] | tftp server ip-address | usb0 | usb1} file-name
l
trust-domain-name – 指定PKI信任域的名称。
l
ftp server ip-address [user user-name password password] – 指定FTP服务器的IP地址以及访
问服务器使用的用户名和密码。当不输入用户名和密码时表示采用匿名登录方式。
l
tftp server ip-address – 指定TFTP服务器的IP地址。
l
usb0 | usb1 – 指定通过USB方式从usb0或者usb1插槽所对应的U盘根目录导入CA证书。
l
file-name – 指定要导入的CA证书的文件名。
配置USB Key证书相应CA证书的信任域
服务端开启客户端USB Key证书认证功能后，还需要指定用户证书相应的CA（Certification Authority）
的信任域。客户端所提交的证书匹配到其中任意一个信任域的CA证书，都会认证成功。在内网接入ZTNA实
例配置模式或者远程访问ZTNA实例配置模式下，使用以下命令：
client-auth-trust-domain trust-domain
l
trust-domain – 指定CA证书所在的PKI信任域，该信任域需已经创建。
如果需要配置多个信任域，需重复使用本命令。系统最多可以支持10个信任域。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用该命令no的形式取消对PKI信任域
的指定：
no client-auth-trust-domain trust-domain

<!-- 来源页 1858 -->
注意: 关于如何创建PKI信任域，请参阅PKI配置部分。
配置ZTNA Portal页面标题
系统支持自定义ZTNA Portal页面的标题，在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式
下，使用以下命令：
resource-portal title title-name
l
title-name - 指定ZTNA Portal页面的标题名称，默认为“ZTNA Portal”。取值范围为1-63个字
符。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用no命令恢复默认配置：
no resource-portal title
配置ZTNA Portal页面的中英文标题
为满足跨国企业各地员工在远程办公时访问不同语言门户页面（即ZTNA Portal页面）的需求，系统支持为
该页面同时配置中英文标题。配置完成后，ZTNA Portal页面标题将根据浏览器语言设置自动匹配并显示对
应语言的标题，用户也可以在ZTNA Portal页面右上角手动切换中英文显示。若未配置中英文标题，则默认
显示ZTNA Portal页面标题配置内容。
注意:
l
仅当设备的系统语言为中文时，支持配置中英文标题。
l
使用Hillstone Secure Connect 5.7.0以上版本（不含5.7.0）的客户端登录ZTNA网关后，
其Portal页面标题支持中英文显示。
l
如果浏览器语言既不是中文也不是英文，ZTNA Portal页面将默认显示英文的应用资源名称。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用以下命令：
resource-portal {zh-cn-title | en-title} title-name
l
zh-cn-title - 配置中文标题。
l
en-title - 配置英文标题。
l
title-name - 输入对应语言的标题名称。取值范围为1-63个字符。
在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用no命令删除中英文标题配置：
no resource-portal {zh-cn-title | en-title}

<!-- 来源页 1859 -->
开启/关闭ZTNA Portal页面弹窗功能
为提升用户使用体验，系统支持开启或关闭ZTNA Portal页面弹窗功能。启用后，系统将根据ZTNA实例中
应用资源的超链接配置，自动判断是否向终端用户弹出Portal页面：
l
存在任一应用资源配置了超链接：用户登录成功后，将正常弹出ZTNA Portal页面。
l
所有资源均未配置超链接：用户登录成功后，不自动弹出ZTNA Portal页面，用户可在ZTNA客户端中点
击“应用资源列表”手动打开。
关闭该功能后，ZTNA Portal页面将不再自动弹出，且ZTNA客户端中的“应用资源列表”菜单将被隐藏，
用户无法通过客户端打开ZTNA Portal页面。该功能默认为开启状态。
注意: 该功能需使用5.7.0及之后版本的ZTNA客户端（即Hillstone Secure Connect客户端）方
可生效。若使用低于5.7.0版本的客户端，则始终会弹出Portal页面。
开启/关闭ZTNA Portal页面弹窗功能，在内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式
下，使用以下命令：
l
开启：resource-portal enable
l
关闭：resource-portal disable
复用隧道源地址
介绍
复用隧道源地址功能主要用于解决业务系统禁止私网IP访问、多网络环境IP地址不一致等网络通信问题，其
核心价值在于“通过IP地址转换适配业务需求，同时保持内部网络的私网隔离特性”。在SSL VPN或ZTNA
远程接入场景中，该功能允许服务端在转发客户端主机的业务访问流量时，自动将该流量的源地址替换成服
务端接收到的封装报文的源地址。这样，当流量经过SSL VPN或ZTNA网关（防火墙）时，系统会自动将原
始私网IP地址或内部网络地址转换为一个合法的公网IP地址或隧道外指定的IP地址。这不仅解决了因私网IP
限制导致的访问障碍，更确保了网络通信中的源地址能被目标业务系统（如OA、CRM等）所在服务器精准
识别，全面满足业务对IP地址的合规性与兼容性要求，进而显著提升网络访问的安全性。
典型应用场景
该功能适用于业务场景中明确规定不能使用私网IP进行访问的情况，具体包括但不限于以下场景：
l 政务外网“一机两用”：政务人员使用同一台终端设备（如电脑、笔记本等）同时处理政务外网业务和互联网访
问时，通过复用隧道源地址功能，可将远程接入政务外网业务流量的源IP地址转换为符合要求的IP，从而隐藏终
端设备真实IP地址，实现网络隔离与身份伪装，避免因直接跨网络切换访问而导致敏感数据泄露或横向渗透，确

<!-- 来源页 1860 -->
保政务外网的安全性和数据保密性。
l 企业分支用户访问总部资源场景：企业分支机构下的用户与总部通过VPN连接，部分业务系统要求使用指定IP地
址访问，复用隧道源地址功能就能将流量的源地址转换为符合要求的IP地址，使分支机构设备访问总部业务时符
合其IP地址规范，确保用户能够正常访问业务系统。
配置复用隧道源地址功能
开始之前
l 阅读"复用隧道源地址" 在第1857页功能介绍。
注意: 仅IPv4类型的SSL VPN及ZTNA远程访问实例支持该功能。
在SSL VPN或ZTNA远程访问场景下，开启复用隧道源地址功能的完整配置流程如下，可依次完成以下配
置：
1. 配置SSL VPN或ZTNA远程访问实例
l SSL VPN远程访问实例配置的详细操作步骤，请参阅配置SSL VPN实例章节。
l ZTNA远程访问实例配置的详细操作步骤，请参阅配置ZTNA实例章节。
2. 开启复用隧道源地址功能
3. （可选）配置访问策略与资源权限
l SSL VPN远程访问：用户可根据使用场景，配置主机检测策略规则，确保授权用户可访问指定资源。
l ZTNA远程访问：用户可根据使用场景，配置应用资源/应用资源组、终端信息、终端标签、ZTNA策略等
信息，确保授权终端可访问指定应用资源。
若在开启复用隧道源地址功能之前，已完成相关访问策略与资源权限配置，可跳过该步骤。
4. 用户验证：完成上述配置后，用户在PC上通过SSL VPN/ZTNA客户端可正常接入SSL VPN/ZTNA服务，并访问指
定授权资源。
以接入ZTNA服务为例
5. 查看复用隧道源地址的地址转换条目

<!-- 来源页 1861 -->
开启/关闭复用隧道源地址功能
默认情况下，该功能为关闭状态。该功能启用后，SSL VPN/ZTNA服务端在转发客户端主机业务流量时，会
将该流量的源地址替换成服务端接收到的封装报文的源地址。
开启或关闭复用隧道源地址功能，在远程访问SSL VPN/ZTNA实例配置模式下，使用以下命令：
l
开启：reuse-tunnel-src-ip enable
l
关闭：reuse-tunnel-src-ip disable
查看复用隧道源地址的地址转换条目
开启复用隧道源地址功能后，管理员可通过查看地址转换条目功能，快速获取私网地址转换后的IP地址信
息。
查看复用隧道源地址的地址转换条目，在任意模式下，使用以下命令：
show dp-scvpn-snat-info
hostname# show dp-scvpn-snat-info
=========================================
vr_id src_ip trans_to_ip
(虚拟路由ID 源IP地址SNAT转换后的IP地址)
----------------------------------------------------------------------------------------
1 33.1.1.2 11.1.1.2 （显示私网地址33.1.1.2转换后的IP地址为11.1.1.2）
1 66.6.6.4 10.1.1.2
==========================================
隧道路由监测
介绍
注意: 该功能仅适用于PC端的SSL VPN/ZTNA客户端远程接入场景。
隧道路由监测功能是SSL VPN或ZTNA远程接入场景中的一项重要安全机制，通过“自动检测- 立即清除-
持续监控”的闭环管理，实现对客户端主机路由的动态管控，有效防止因主机路由与隧道路由冲突或PC的主
机路由被篡改而导致的网络连接异常，确保远程接入的安全性和稳定性。客户端在连接过程中，会自动检测
PC上的主机路由列表，一旦发现与隧道路由存在冲突的主机路由，将立即清除这些冲突路由，并准确下发隧
道路由，从而确保隧道路由的有效性和优先级。客户端连接成功后，会持续监测PC上的主机路由状态。如果

<!-- 来源页 1862 -->
主机路由发生变化且与隧道路由冲突，服务端会自动断开客户端连接，并及时向用户发出提示，从而有效防
御路由篡改攻击，保障远程接入场景下的网络通信安全。
在SSL VPN/ZTNA客户端（即Hillstone Secure Connect客户端）与服务端连接断开的情况下，客户端会
自动将PC上的主机路由恢复到连接服务端之前的状态。
应用场景
隧道路由监测功能特别适用于需要防止路由被篡改，保障网络通信安全的应用场景。
l SSL VPN专线/ZTNA专线：专线网络常被用于传输敏感数据（如财务信息、客户隐私），攻击者可能通过植入恶
意程序篡改终端路由，试图窃取专线流量或渗透至企业内网。隧道路由监测功能可持续监控主机路由的状态，一
旦检测到未经授权的路由修改（如通过ARP 欺骗、路由劫持攻击），会立即断开连接，防止攻击者利用路由篡改
渗透专线网络，强化专线场景下的终端安全防护能力。
l 多网络环境下的路由隔离：终端同时连接Wi-Fi（本地网络）和VPN隧道时，隧道路由监测功能可确保流量严格
遵循隧道路由，避免因路由优先级混乱导致的访问失败或安全风险。
l 企业远程办公安全：当员工远程办公时，可能因误操作或恶意软件修改本地路由，导致流量绕过VPN隧道。隧道
路由监测功能可及时阻断异常路由，保障企业内网资源访问安全。
l 高安全需求环境：在对安全性要求较高的环境中，如政务外网或金融行业，隧道路由监测功能可以防止恶意路由
篡改，保障网络连接的安全性。
工作原理
启用隧道路由监测功能后，用户在PC上通过SSL VPN/ZTNA客户端发起远程接入请求后，SSL VPN/ZTNA
服务端会通知客户端在连接过程中及连接成功后全程监测并管理PC的主机路由。客户端在收到通知后，会进
行如下处理：
1. 在连接过程中，客户端会自动检查PC上的主机路由（除默认路由、直连路由以外的所有主机路由）是否与隧道路
由冲突。
l 若存在冲突，客户端会立即清除这些与隧道路由冲突的主机路由，并在清除成功后准确下发隧道路由。
l 若无冲突，客户端直接建立隧道连接。
2. 连接成功后，客户端会持续监测PC上的主机路由状态。如果主机路由发生变化并与隧道路由冲突，服务端将自动
断开客户端连接，并及时向用户提示“路由发生变化，与当前隧道路由存在冲突，断开连接”。用户可以查看PC
的路由表项，找出冲突的主机路由条目，并根据实际情况进行调整或处理。
3. 连接断开后，客户端会自动恢复之前因冲突而删除的主机路由。用户可以查看PC的路由表项，确认这些已恢复的
主机路由。

<!-- 来源页 1863 -->
隧道路由监测功能注意事项
注意:
l
仅IPv4类型的SSL VPN及ZTNA远程访问实例支持该功能。
l
不支持同时开启隧道路由监测与域名路由下发功能。
l
桌面端Hillstone Secure Connect客户端版本和运行环境需满足以下要求，隧道路由监测功
能才能生效。
客户端版本
运行环境
v5.7.0及以上版
本
l
Window系统
l
Linux系统
l
MacOS系统
l
国产操作系统：统信UOS 20（CPU飞腾/CPU兆芯）、银河麒麟
Kylin V10 SP1（CPU飞腾/CPU兆芯）
开启隧道路由监测功能后，若在上述Window系统和国产操作系统下使用
5.5.0及以下版本的客户端接入SSL VPN/ZTNA服务时，系统会提示“当
前客户端与防火墙版本不兼容，请升级到最新版本”。此时，用户需将客
户端版本升级至已发布的最新版本。
l
开启隧道路由监测功能后，若在移动端上使用Hillstone Secure Connect客户端接入SSL
VPN/ZTNA服务时，可成功接入SSL VPN/ZTNA服务，但隧道路由监测功能不生效。
配置隧道路由监测功能
开始之前
l 阅读隧道路由监测功能"介绍" 在第1859页。
l 阅读"隧道路由监测功能注意事项" 在第1861页。
在SSL VPN或ZTNA远程访问场景下，开启隧道路由监测功能的完整配置流程如下，可依次完成以下配置：
1. 配置SSL VPN或ZTNA远程访问实例
l SSL VPN远程访问实例配置的详细操作步骤，请参阅配置SSL VPN实例章节。
l ZTNA远程访问实例配置的详细操作步骤，请参阅配置ZTNA实例章节。
2. 开启隧道路由监测功能

<!-- 来源页 1864 -->
在远程访问SSL VPN/ZTNA实例配置模式下，使用tunnel-route-snoop enable命令，开启隧道路由
监测功能。启用后，SSL VPN/ZTNA服务端会通知客户端在连接过程中及连接成功后全程监测并管理PC
的主机路由，详细说明请参阅该功能的"工作原理" 在第1860页章节。
如需关闭该功能，可在远程访问SSL VPN/ZTNA实例配置模式下，使用tunnel-route-snoop disable
命令。默认情况下，该功能为关闭状态。
3. （可选）配置访问策略与资源权限
l SSL VPN远程访问：用户可根据使用场景，配置主机检测策略规则，确保授权用户可访问指定资源。
l ZTNA远程访问：用户可根据使用场景，配置应用资源/应用资源组、终端信息、终端标签、ZTNA策略等
信息，确保授权终端可访问指定应用资源。
若在开启隧道路由监测功能之前，已完成相关访问策略与资源权限配置，可跳过该步骤。
4. 用户验证：可选择以下任一方式，验证隧道路由监测功能是否生效。
以下是针对配置了隧道路由为192.168.0.0/16的SSL VPN/ZTNA实例的验证步骤说明。
方式一：通过比对SSL VPN/ZTNA客户端连接前和连接后，PC上的路由表进行验证。
不同操作系统的PC查看路由表项的命令有所不同，具体操作请根据实际情况进行调整。下面以
Windows操作系统的PC为例进行说明：
a. SSL VPN/ZTNA客户端连接之前，在PC上使用Win+R按键，打开运行窗口，输入cmd，回车打开命令提
示符（cmd）窗口。
b. 在命令提示符（cmd）窗口，输入route print -4命令，查看该PC上的所有IPv4路由表项，并检查该路由
表项中是否存在与隧道路由冲突的主机路由。如下图所示，“192.168.2.0 /24” 及“ 192.168.3.0
/24”两条主机路由与隧道路由“192.168.0.0/16 33.1.1.1”冲突。

<!-- 来源页 1865 -->
c. 在PC上打开SSL VPN/ZTNA客户端，输入相关认证信息并连接到服务器。
d. 客户端成功建立连接后，在PC上的命令提示符（cmd）窗口，再次输入route print -4命令，查看当前PC
上的所有IPv4路由表项，并检查与隧道路由冲突的主机路由是否已被删除。若路由表中与隧道路由冲突的
主机路由成功被删除，且存在一条成功下发的隧道路由，则说明隧道路由监测功能生效；反之，则未生
效，用户需检查SSL VPN/ZTNA客户端版本、运行系统以及服务端的相关配置，并在问题解决后重新进行
验证。
如下图所示，“192.168.2.0 /24” 及“ 192.168.3.0 /24”两条主机路由已被删除，且下发了
“192.168.0.0/16 33.1.1.1”的隧道路由。

<!-- 来源页 1866 -->
e. 退出/断开客户端连接后，查看PC的路由表项，之前被删除的主机路由已恢复。

<!-- 来源页 1867 -->
方式二：SSL VPN/ZTNA客户端连接成功后，通过在PC上添加一个与隧道路由冲突的主机路由进行验
证。
不同操作系统的PC添加路由表项的命令有所不同，具体操作请根据实际情况进行调整。下面以
Windows操作系统的PC为例进行说明：
a. 在PC上打开SSL VPN/ZTNA客户端，输入相关认证信息并连接到服务器。
b. 客户端成功建立连接后，在PC上，使用Win+R按键，打开运行窗口，输入cmd，回车打开命令提示符
（cmd）窗口。
c. 在命令提示符（cmd）窗口，输入route add dst-network-address mask mask-address gateway
metric value if interface index命令，添加一个与隧道路由冲突的路由。如在PC上添加
“192.168.5.0/24 10.1.1.1”的路由，该路由与“192.168.0.0/16 33.1.1.1”的隧道路由冲突。
l dst-network-address - 输入需要访问的目的网络地址，即数据包发送的目标网络地址。
l mask-address - 输入子网掩码地址。
l gateway - 输入网关地址，即数据包转发的下一跳地址。
l metric value - 指定路由的优先级，数值越低优先级越高，当存在多条到目标网络的路由时，系统
会优先选择优先级高（metric 值低）的路由。
l if interface index - 指定该路由所使用的网络接口的唯一数字标识符（即接口索引）。
d. 成功在PC上添加路由后，若客户端连接断开，并提示“路由发生变化，与当前路由存在冲突，断开连
接”，则说明隧道路由功能生效；若客户端连接无影响，则说明隧道路由功能未生效。
清理TCP连接
介绍
清理TCP连接功能是指在SSL VPN或ZTNA客户端成功建立连接后，系统会自动识别并清除终端上所有目标
IP匹配隧道路由配置范围的现有TCP连接，强制相关流量必须通过加密隧道传输，从而有效阻断非法流量绕
过安全通道的潜在路径，消除数据传输过程中的泄密风险。同时，该功能通过清除可能产生冲突的既有TCP
连接，规避新旧TCP连接之间的会话干扰，确保网络通信的连续性与可靠性，显著提升整体网络安全防护能
力，最大限度降低因非授权连接引发的安全风险。

<!-- 来源页 1868 -->
应用场景
该功能作为SSL VPN/ZTNA解决方案中的一项重要安全机制，特别适用于以下使用场景：
l 远程办公：在远程办公场景中，员工通过SSL VPN或ZTNA客户端连接到企业内网。启用清理TCP连接功能可以确
保所有业务流量通过安全隧道传输，防止数据泄露。
l 多网络环境：在多网络环境下，终端设备可能同时连接到多个网络。清理TCP连接功能可以防止流量在不同网络
之间冲突，确保流量正确地通过隧道传输。
l 高安全需求环境：在安全性要求较高的环境中，如政务外网或金融行业，清理TCP连接功能可以确保所有流量均
通过安全隧道，满足合规要求。
l 防止会话劫持：在可能存在会话劫持风险的环境中，清理TCP连接功能可以清除潜在的恶意连接，防止会话被劫
持。
l 动态网络环境：在动态网络环境中，终端设备的网络连接可能会频繁变化。清理TCP连接功能可以确保每次连接
时，所有流量都通过最新的安全隧道传输。
清理TCP连接功能注意事项
注意:
l
仅IPv4类型的SSL VPN及ZTNA远程访问实例支持该功能。
l
若SSL VPN及ZTNA远程访问实例已配置默认路由，则不建议开启清理TCP连接功能。如果开
启该功能，系统会清除所有TCP连接，从而导致远程桌面（RDP）、SSH等连接中断，影响通
信的稳定性。
l
桌面端Hillstone Secure Connect客户端版本和运行环境需满足以下要求，清理TCP连接功
能才能生效。
运行环境
客户端版本
Window系统
建议使用5.7.0及以上版本的客户端。
开启清理TCP连接功能后，若在Window系统下使用5.5.0及以下版本的客
户端接入SSL VPN/ZTNA服务时，系统会提示“当前客户端与防火墙版本
不兼容，请升级到最新版本”。此时，用户需将客户端版本升级至已发布
的最新版本。
除Window系统
之外的其他操作
系统
客户端版本无要求。除Window系统之外的其他操作系统天然适配该功
能。

<!-- 来源页 1869 -->
l
开启清理TCP连接功能后，若在移动端上使用Hillstone Secure Connect客户端接入SSL
VPN/ZTNA服务时，可成功接入SSL VPN/ZTNA服务，但清理TCP连接功能不生效。
配置清理TCP连接功能
开始之前
l 阅读"清理TCP连接" 在第1865页功能介绍。
l 阅读"清理TCP连接功能注意事项" 在第1866页。
在SSL VPN或ZTNA远程访问场景下，开启清理TCP连接功能的完整配置流程如下，可依次完成以下配置：
1. 配置SSL VPN或ZTNA远程访问实例
l SSL VPN远程访问实例配置的详细操作步骤，请参阅配置SSL VPN实例章节。
l ZTNA远程访问实例配置的详细操作步骤，请参阅配置ZTNA实例章节。
2. 开启清理TCP连接功能
在远程访问SSL VPN/ZTNA实例配置模式下，使用clear-tcp-connection enable命令，开启清理
TCP连接功能。启用后，当SSL VPN/ZTNA客户端成功建立连接时，系统会识别终端上已存在的所有
TCP会话，并自动清除目标IP属于隧道路由配置范围的所有TCP会话。如需关闭该功能，可在远程访问
SSL VPN/ZTNA实例配置模式下，使用clear-tcp-connection disable 命令。默认情况下，该功能为
关闭状态。
3. （可选）配置访问策略与资源权限
l SSL VPN远程访问：用户可根据使用场景，配置主机检测策略规则，确保授权用户可访问指定资源。
l ZTNA远程访问：用户可根据使用场景，配置应用资源/应用资源组、终端信息、终端标签、ZTNA策略等
信息，确保授权终端可访问指定应用资源。
若在开启清理TCP连接功能之前，已完成相关访问策略与资源权限配置，可跳过该步骤。
4. 用户验证：通过对比SSL VPN/ZTNA客户端连接前后终端上的TCP连接表，即可验证清理TCP连接功能是否生
效。
不同操作系统的终端查看TCP连接表的命令有所不同，具体操作请根据实际情况进行调整。下面以
Windows操作系统终端为例，详细介绍清理TCP连接功能验证的具体操作步骤：
a. SSL VPN/ZTNA客户端连接之前，在PC上建立一些TCP连接会话。这些TCP连接会话中，需确保至少有一
个会话的目标IP地址能够匹配上隧道路由（即会话的目标IP地址在隧道路由配置范围内），方便后续进行
验证。以PC上存在的目标IP地址为10.18.24.37的TCP连接会话举例（该会话可匹配上10.18.24.0/24的隧

<!-- 来源页 1870 -->
道路由）。
b. 在PC上，使用Win+R按键，打开运行窗口，输入cmd，回车打开命令提示符（cmd）窗口。
c. 在命令提示符（cmd）窗口，输入netstat -ano | findstr "TCP"命令，查看当前TCP连接表。如下图所
示，TCP连接表中发现目标IP地址为10.18.24.37的TCP连接会话。
d. 在PC上打开SSL VPN/ZTNA客户端，输入相关认证信息并连接到服务器。
e. 客户端成功建立连接后，重复步骤b~c，再次查看当前TCP连接表，并确认原会话是否已被清理。
若TCP连接表中原会话（目标IP地址为10.18.24.37的TCP连接会话）已被清除，则说明清理TCP连接功能
生效；反之，则未生效，用户需检查SSL VPN/ZTNA服务端的相关配置，并在问题解决后重新进行验证。
免二次认证
介绍
注意: 该功能目前仅支持在零信任网络访问（ZTNA）场景下使用。
免二次认证功能可有效解决网络切换、设备休眠唤醒等场景下的重复二次认证问题，显著提升企业员工移动
办公效率。该功能通过预置持续时间阈值和网络区域条件等规则，对符合安全规则要求的办公终端（办公电
脑PC/移动设备）实施“首次认证+持续可信”的智能验证机制：在指定时间范围内，员工只需完成首次连接
的二次认证，后续访问即可免除二次认证，自动保持认证状态，既严格遵循零信任安全架构，又显著减少认
证操作频次，实现安全性与用户体验的双重提升，同时降低运维成本。
应用场景
该功能适用于需要频繁切换办公地点、使用多种网络环境的企业员工群体，在保障安全的前提下最大限度减
少认证干扰，提升工作效率。

<!-- 来源页 1871 -->
l 跨网络切换场景：员工在办公区Wi-Fi/有线网络、家庭网络、4G/5G移动网络之间切换时，保持持续访问状态，
避免每次网络切换都触发重新二次认证。
l 设备休眠唤醒场景：员工在公司内网使用办公电脑接入ZTNA，电脑处于休眠/锁屏后重新唤醒时，无需重新二次
认证即可自动恢复原有会话连接，提升办公效率。
l 跨地域办公场景：员工在全国不同分支机构间移动办公时，只要处于企业预设的可信网络区域内，即可免除二次
认证，提升办公效率。
l 移动办公场景：用户在移动设备上通过ZTNA访问企业资源时，可在确保网络安全的前提下，使用免二次认证功
能减少重复认证的步骤，提供便捷的访问体验。
工作原理
当客户端完成登录操作并成功通过首次认证之后，系统将根据客户端类型、网络区域条件、持续时间等条
件，进一步判断后续客户端登录是否可以免除二次认证，详细判断流程如下图所示：

<!-- 来源页 1872 -->
免二次认证功能配置注意事项
注意:
l
当二次认证类型为“令牌口令认证”时，不支持该功能。
l
非根VSYS不支持该功能。

<!-- 来源页 1873 -->
l
使用该功能后，用户首次连接ZTNA，或在超出免二次认证的持续时间连接ZTNA时，都需要重
新进行二次认证。
l
当系统无法识别客户端类型（例如安装鸿蒙系统的终端设备等），则默认将其识别为桌面端，
并自动应用免二次认证功能中桌面端对应的网络区域条件。
l
使用该功能后，若ZTNA接入客户端的IP地址发生变化（如终端网络切换），防火墙会强制断
开该客户端连接。随后，客户端会自动发起重新连接请求。若客户端IP地址变更后，仍符合免
二次认证功能所配置的持续时间及网络区域条件，则可免于二次认证，直接登录ZTNA；若不
符合，则需手动按照流程完成二次认证后，方可登录ZTNA。
l
为确保免二次认证功能的网络区域条件全面生效，建议仅双栈类型的ZTNA实例引用同时配置
IPv4和IPv6网段的网络区域。IPv4或IPv6单栈类型的ZTNA实例引用此类网络区域时，部分条
件将不生效，因其仅支持对应类型的IP地址接入。
l
当用户重启设备或对ZTNA实例执行禁用后重新启用的操作时，需在连接ZTNA服务时重新完成
二次认证流程。
免二次认证功能配置流程
在零信任网络访问（ZTNA）场景下，免二次认证功能的完整配置流程如下，可依次完成以下配置：
1. 配置ZTNA实例，并开启二次认证功能（二次认证的类型需为短信口令认证或邮箱口令认证），确保用户通过短
信或邮箱进行二次认证后，能够正常访问授权资源。
2. 配置网络区域，以便在配置免二次认证功能时能够直接引用。
3. 为指定ZTNA实例配置免二次认证功能，以满足用户在指定网络区域及时长内再次接入可以免除二次认证。
4. 完成上述配置后，用户需要验证免二次功能是否生效。
网络区域
在零信任网络访问（ZTNA）场景中，网络区域是指用户或设备所处的网络环境的分类，通常基于网络位置
（如企业内网、分支机构网络）、连接类型（如有线、无线、VPN）、地理位置、设备类型等条件因素来定
义。通过对网络区域的划分，可以帮助系统根据用户所在的网络环境的安全性和可靠性，灵活地调整访问控
制策略。例如，如果用户处于企业内网等安全网络区域，系统可以允许用户免于二次认证即可访问资源；而
如果用户处于外网等风险较高的网络区域，系统则可以要求用户进行二次认证，以确保访问的安全性。通过
这种方式，系统能够在保障安全的同时，优化用户体验，实现灵活且高效的访问管理。
注意: 非根VSYS不支持该功能。

<!-- 来源页 1874 -->
配置网络区域
网络区域配置主要包括以下各项：
l 创建网络区域并进入网络区域配置模式
l 配置描述信息
l 配置网络区域条件
l 查看网络区域配置
创建网络区域并进入网络区域配置模式
创建指定名称的网络区域并进入网络区域配置模式。如果指定的名称已存在，则直接进入网络区域配置模
式。
在全局配置模式下，使用以下命令，创建网络区域并进入网络区域配置模式：
network-area network-area-name
l
network-area-name - 指定网络区域的名称，取值范围为1到95个字符。系统最多支持配置64个网络
区域。
在全局配置模式下，使用以下命令，删除指定名称的网络区域：
no network-area network-area-name
注意: 当网络区域已被ZTNA实例引用时，不能直接删除。如需删除被ZTNA引用的网络区域，需在
免二次认证配置模式下，使用no {pc | mobile} network-areanetwork-area-name命令先解
除其引用关系，再执行删除操作。
配置描述信息
为指定网络区域添加相关的描述信息，在网络区域配置模式下，使用以下命令：
description description
l
description - 为指定网络区域添加相关的描述信息，取值范围为1到255个字符。
在网络区域配置模式下，使用以下命令，删除指定网络区域的相关描述信息：
no description

<!-- 来源页 1875 -->
配置网络区域条件
网络区域条件用于判断用户是否属于某一个网络区域。它通过多维度属性识别终端身份，确保只有符合条件
的终端用户被纳入目标区域，并应用相应的访问策略（目前仅应用于免二次认证功能）。当前，网络区域条
件仅支持配置客户端IP属性。
在网络区域配置模式下，使用以下命令，配置网络区域条件：
client-ip in ip-address/prefix
l
ip-address/prefix - 指定客户端IP所在网段，如192.168.1.0/24。若客户端与ZTNA网关之间存在
SNAT设备，网段需设置为SNAT转换后IP所在网段。
重复上述命令，可在同一网络区域中，添加多条网络区域条件。如需删除指定网络区域条件，可在网络区域
配置模式下，使用以下命令：
no client-ip in ip-address/prefix
注意:
l
一个网络区域，最多可配置16条网络区域条件。
l
在同一网络区域中，可以同时配置IPv4网段和IPv6网段的网络区域条件。
查看网络区域配置
在任意模式下，使用以下命令，查看所有网络区域或指定网络区域的详细配置信息：
show network-area [network-area-name]
l
show network-area - 查看所有网络区域的配置信息。
l
network-area-name - 查看指定网络区域的详细配置信息。
示例：
hostname# show network-area （查看所有网络区域的配置信息）
===============================================================
Name Condition
（网络区域名称网络区域条件）
------------------------------------------------------------------------------------------------
----
1 client-ip in 1.1.1.0/24

<!-- 来源页 1876 -->
test client-ip in 10.1.0.0/16
test-area client-ip in 10.1.1.0/24
===============================================================
hostname# show network-area test （查看指定网络区域的配置信息）
------------------------------------------------------------------------------------------------
----
Name: test （显示网络区域名称）
Description: （显示网络区域的相关描述信息）
Condition: client-ip in 10.1.0.0/16 or （显示网络区域条件）
client-ip in 2.2.2.0/24
================================================================
下一步
完成网络区域配置后，用户需要将该配置引用到相关的业务功能上使其生效。目前仅ZTNA实例可引用网络
区域配置。
配置免二次认证功能
开始之前
l 阅读免二次认证功能"介绍" 在第1868页。
l 阅读"免二次认证功能配置注意事项" 在第1870页。
l 阅读"免二次认证功能配置流程" 在第1871页。
前置条件
l 请提前配置ZTNA实例，并开启二次认证功能（二次认证的类型需为短信口令认证或邮箱口令认证），确保用户
通过短信或邮箱进行二次认证后，能够正常访问授权资源。
o ZTNA实例的配置步骤及说明请参阅"ZTNA实例配置" 在第1841页。
o 二次认证功能配置步骤及说明请参阅"配置二次认证功能" 在第1876页。
l 请提前配置好网络区域条件，以便在配置免二次认证功能时能够直接引用。网络区域条件配置步骤及说明请参阅
"网络区域" 在第1871页配置。

<!-- 来源页 1877 -->
配置免二次认证功能
免二次功能配置包括持续时间、以及桌面端/移动端用户对应的网路区域条件设置。用户需先进入免二次认证
配置模式，才能进行免二次认证功能的相关配置。
进入自适应认证配置模式
进入免二次认证配置模式之前，需先进入自适应认证配置模式。在内网接入ZTNA实例配置模式或者远程访
问ZTNA实例配置模式下，使用以下命令：
adaptive-verification
进入免二次认证配置模式
在自适应认证配置模式下，使用以下命令，进入免二次认证配置模式：
skip-two-step-verification
配置免二次认证持续时间
持续时间是指用户在完成二次认证后，系统保持其信任状态，并允许用户无需重复进行二次认证即可访问资
源的有效时长。若当前认证时间与最近一次认证时间的差值超过设定的阈值，用户需要重新进行二次认证。
在免二次认证配置模式下，使用以下命令，配置免二次认证的持续时间：
duration days
l
days - 指定用户免除二次认证的持续时间，取值范围1到30天，默认为1天。
指定免二次认证的网络区域条件
指定桌面端和移动端用户所属的网络区域，即为桌面端和移动端用户指定免除二次认证时需匹配的网络区域
条件。指定后，符合该网络区域条件的个人电脑（PC）或移动设备（如手机等）用户在登录ZTNA时，首次
连接需执行二次认证流程；此后，在规定的持续时间范围内，用户可免除二次认证。对于不符合所设定网络
区域条件的个人电脑（PC）或移动设备（如手机等）用户在登录ZTNA时，则每次连接或重新连接都需要进
行二次认证。
在免二次认证配置模式下，使用以下命令，指定免二次认证的网路区域条件：
{pc | mobile} network-area network-area-name
l
pc | mobile - 指定客户端类型。pc为桌面端，mobile为移动端。
l
network-area-name - 指定网络区域的名称。

<!-- 来源页 1878 -->
注意: 如需为同一客户端类型添加多个网络区域，需重复执行上述命令。桌面端与移动端合计最多
可选择16个网络区域，且多个网络区域之间为“或（or）”的关系。
在免二次认证配置模式下，使用以下命令，删除免二次认证的网络区域条件配置：
no {pc | mobile} network-area network-area-name
下一步
完成免二次认证功能配置后，用户需进一步验证该配置是否生效。免二次认证功能验证，请按照以下步骤进
行操作：
1. 在满足所设定网络区域条件的个人电脑（PC）或移动设备（手机）上，启动ZTNA客户端。
2. 找到目标ZTNA连接会话，点击“连接”，在弹出的页面填写用户账号密码。
3. 点击“登录”，按照提示完成短信/邮箱认证，登录ZTNA网关。
说明：用户在进行该功能验证时，需确保以上操作为该功能配置完成后的首次登录。
4. 在所设定的持续时间范围内，先断开ZTNA连接，然后再重新登录ZTNA。重新登录时，若无需进行二次认证，则
说明该功能已生效；反之，则不生效，用户需检查ZTNA网关相关配置信息，并在问题解决后重新进行验证。
5. 在超出持续时间后，用户登录ZTNA时，需要重新进行二次认证。
配置二次认证功能
二次认证功能是指ZTNA用户使用用户名/密码或用户名/密码+数字证书方式登录时，收到登录请求的山石网
科设备通过短信口令、令牌口令、邮件口令的方式进行二次认证，用户输入收到的认证码后，才可以通过认
证，进而访问内网资源。
l "配置令牌口令认证" 在第1878页
l "配置短信口令认证" 在第1878页
l "配置邮件口令认证" 在第1903页
开启/关闭二次认证功能
默认情况下，系统的二次认证功能为关闭状态。开启/关闭二次认证功能，在ZTNA实例配置模式下，使用以
下命令：
开启：two-step verification enable
关闭：two-step verification disable

<!-- 来源页 1879 -->
指定认证类型
指定二次认证的类型，在ZTNA实例配置模式下，使用以下命令：
two-step verification type {token | sms modem | sms service-provider | email }
l
token- 指定通过令牌口令对用户进行二次认证。
l
sms modem - 指定通过短信猫发送短信口令对用户进行二次认证。
l
sms service-provider - 指定通过短信网关发送短信口令对用户进行二次认证。
l
email - 指定通过邮件口令对用户进行二次认证。

<!-- 来源页 1880 -->
配置令牌口令认证
当用户登录时，通过绑定的令牌口令进行认证，并支持用户自定义令牌口令认证的提示信息。
配置提示信息
配置令牌口令认证的提示信息，在ZTNA实例配置模式下，使用以下命令：
token-auth prompt-message message
l
prompt-message message- 指定提示信息，为1到255个字符长度的字符串。
配置短信口令认证
短信口令认证功能是指ZTNA用户使用用户名和密码登录时，收到登录请求的山石网科设备通过短信猫或短
信网关自动向该用户的手机号码发送一条包含随机认证码的短信，用户输入收到的认证码后，才可以通过认
证，进而访问内网资源。
注意: 山石网科设备的部分平台支持短信口令认证功能。
短信猫认证
山石网科设备采用外置GSM短信猫或CDMA短信猫。配置短信口令认证功能前，请准备一张手机SIM卡和一
个GSM短信猫或CDMA短信猫，并将短信猫正确连接到网关设备上。连接短信猫和山石网科设备，首先，将
SIM卡正确插入短信猫内；然后，通过USB数据线将短信猫与山石网科设备的USB接口连接起来。我们推荐
用户使用以下型号的短信猫：
型号
类型
接口
金笛4G全网通MODEM M1806-NC5
LTE(FDD)
LTE(TDD)
WCDMA
TD-SCOMA
GSM/GPRS/EDGE
CDMA2000
USB接口
金笛GSM MODEM （M1206B、M1206B-FT）
GSM
USB接口
短信猫的状态共包括三种：“短信猫存在”、“短信猫不存在”和“无SIM卡”。
短信猫认证配置
短信口令认证功能的服务端配置包括：

<!-- 来源页 1881 -->
l 设置短信认证手机号码
l 配置短信认证码有效时间
l 配置短信认证码长度
l 配置短信验证内容
l 配置短信最大发送数量
l 发送测试短信
设置短信认证手机号码
ZTNA本地用户和AD用户均可使用短信口令认证功能。管理员可以为每个本地用户和AD用户设置一个手机
号码。开启短信口令认证功能后，系统会向已指定的登录用户手机号码发送认证码短信。
为本地用户设置手机号码，在用户配置模式下，使用以下命令：
phone phone-number
l
phone-number – 指定本地用户手机号码。
在用户配置模式下使用该命令no的形式取消用户手机号码的指定：
no phone
为AD用户设置手机号码，需要在AD服务器的“mobile”属性中配置手机号码。
配置短信认证码有效时间
每条短信认证码都有一个有效时间，如果用户在有效时间内没有输入短信认证码也没有重新申请认证码，
ZTNA服务端将自动断开连接。配置短信认证码有效时间，在ZTNA实例配置模式下，使用以下命令：
sms-auth expiration expiration
l
expiration – 指定短信认证码有效时间。默认为10分钟，范围为1-10分钟。
在ZTNA实例配置模式下使用该命令no的形式恢复系统默认有效时间：
no sms-auth expiration
配置短信认证码长度
配置短信认证码长度，在ZTNA实例配置模式下，使用以下命令：
sms-auth verification-code-length length
l
length – 指定短信认证码长度。取值范围为4至8个字符。默认为8个字符。

<!-- 来源页 1882 -->
在ZTNA实例配置模式下，使用该命令no的形式恢复默认短信认证码长度。
no sms-auth verification-code-length
配置短信验证内容
配置认证码短信的验证内容，在ZTNA实例配置模式下，使用以下命令：
sms-auth message-content content
l
content – 指定认证码短信的验证内容，内容必须包含“＄VRFYCODE”（用于获取认证码），可以包
含“＄USERNAME”和“＄EXPIRATION”（“＄USERNAME”用于获取用户
名；“＄EXPIRATION”用于获取认证码有效期）。短信验证内容长度的取值范围为9至500个字符。若
未配置短信验证内容，将使用默认短信验证内容，默认短信验证内容为“Your num sms authing
message is vrfycode”(num为认证次数，vrfycode为认证码。)
在ZTNA实例配置模式下，使用该命令no的形式恢复默认验证内容。
no sms-auth message-content
注意: 仅ACC、XUANWU、CAS和HTTP(S)协议的短信网关支持配置短信验证内容。
配置短信最大发送数量
管理员可以配置短信猫每小时或者每天最多发送的短信数量。对超出数量限制的短信，系统将自动丢弃并记
录日志信息。配置短信最大发送数量，在全局配置模式下，使用以下命令：
sms modem {num-per-hour | num-per-day} number
l
{num-per-hour | num-per-day} number– 指定短信猫每小时（num-per-hour）或者每天
（num-per-day）最多发送的短信数量。范围为1-1000条。
在全局配置模式下使用该命令no的形式不限制短信最大发送数量：
no sms modem {num-per-hour | num-per-day}
发送测试短信
为验证设备能否正常发送短信，管理员可以向指定手机号码发送测试短信。发送测试短信，在任意模式下，
使用以下命令：
exec sms sp sp-name tunnel-name sendtest-message to phone-number [test-msgcontentcontent ]

<!-- 来源页 1883 -->
l
phone-number – 指定接收测试短信的手机号。
l
tunnel-name – 指定绑定该SP实例的隧道的名称。
l
content–指定测试短信的内容。默认值为“这是一条测试短信，请不要回复！”，取值范围为1至64个
字符。
如果测试短信发送成功，指定手机号码会收到系统发送的测试短信；如果测试短信发送失败，系统会记录日
志并描述失败原因。
显示短信猫配置信息
在任意模式下，使用以下命令查看短信猫的配置信息，包括存在状态和短信最大发送数量：
show sms modem

<!-- 来源页 1884 -->
短信网关认证配置
山石网科安全设备可通过运营商的短信网关或者其代理服务器向用户发送短消息。配置该功能前，用户需先
向运营商索要短信网关的地址、发送短消息的设备ID等相关信息。
短信网关认证的配置包括：
1. 创建Service Provider（SP）实例，并根据需要，配置SP实例。
2. 绑定SP实例到已创建的ZTNA实例，开启短信网关认证功能。
注意: 此为华为云短信网关本身的限制条件。如需配置华为云短信网关，请仔细阅读该限制条件。
l
任意1分钟内，华为云短信网关最多向同一个手机号码发送2次短信。
l
任意24小时内，华为云短信网关最多向同一个手机号码发送50次短信。
前置条件
在通过华为云短信网关和阿里云短信网关向指定手机号码发送短信之前，请校准系统的时间和时区。如何配
置系统时间，详情请参阅系统时间或配置NTP章节。
指定短信网关协议类型
设备支持的短信网关协议类型包括SGIP、UMS、ACC、ALIYUNSMS、XUANWU、CAS、BEIKE、HTTP(S)
和HTTP(S)-Plus等。
用户可以在全局配置模式下，使用以下命令指定短信网关的协议类型：
sms service-provider default-protocol {sgip | ums | acc | aliyunsms| xuanwu | cas | beike |
http(s) | http(s)-plus}
sms service-provider {provider-name protocol | default-protocol} {sgip | ums | acc |
aliyunsms| xuanwu | cas | beike | http(s) | http(s)-plus}
l
sgip | ums | acc | aliyunsms| xuanwu | cas | beike | http(s) | http(s)-plus - 指定短信网关的协
议类型。sgip表示联通的SGIP协议，ums表示使用联通企业信息平台，acc表示使用电信的ACC协议，
aliyunsms表示使用阿里云短信服务平台，xuanwu表示使用玄武科技短信服务平台，cas表示使用
12302短信服务平台，beike表示贝壳的短信网关，http(s)表示HTTP/HTTPS协议，http(s)-plus表示
对接特殊格式的短信网关，可根据短信网关的接口要求，灵活规划1至5步请求与响应链路，适合复杂接
口场景。

<!-- 来源页 1885 -->
在全局配置模式下，使用no sms service-provider default-protocol命令取消短信网关的协议类型的指
定。
提示: HTTP(S)-Plus对接类型，拥有高度的自定义能力。配置方式请参阅配置HTTPS-Plus类型短
信网关。
创建SP实例名称
创建SP实例，在全局配置模式下，使用以下命令：
sms service-provider sp-name [protocol {sgip | ums | acc | aliyunsms| xuanwu | cas | beike |
http(s) | http(s)-plus}]
l
sp-name - 指定SP实例的名称，取值范围为1至31个字符。
l
protocol {sgip | ums | acc | aliyunsms| xuanwu | cas | beike | http(s)} - 指定SP实例运行的短信
网关协议。指定SP实例运行的短信网关协议。sgip表示联通的SGIP协议，ums表示使用联通企业信息平
台，acc表示使用电信的ACC协议，aliyunsms表示使用阿里云短信服务平台，xuanwu表示使用玄武
科技短信服务平台，cas表示使用12302短信服务平台，beike表示贝壳的短信网关，http(s)表示
HTTP/HTTPS协议，http(s)-plus表示对接特殊格式的短信网关，可根据短信网关的接口要求，灵活规
划1至5步请求与响应链路，适合复杂接口场景。
执行该命令后，系统创建指定名称的SP实例，并且进入SP实例配置模式；如果指定的名称已存在，则直接进
入SP实例配置模式。对于每种协议类型的SP实例，系统最多可配置8个SP实例。
在全局配置模式下，使用该命令no的形式删除指定的SP实例：
no sms service-provider sp-name
配置SP实例介绍
在SP实例配置模式下，可以进行以下配置：
l 指定VRouter
l 指定发送方式
l 指定HTTP（S）报文的内容类型
l 指定编码格式
l 指定UMS/ACC/BEIKE/ALIYUNSMS/BEIKE协议
l 配置URL地址

<!-- 来源页 1886 -->
l 配置来源号码
l 配置平台编号
l 配置平台密码
l 配置平台子系统编号
l 配置模板ID
l 配置成功标识
l 配置根节点
l 配置属性
l 配置协议子类型
l 指定短信网关的地址和端口号
l 指定模板参数
l 设置发送认证短信的号码
l 指定设备ID
l 指定用户名和密码
l 配置短信最大发送数量
l 开启/关闭发送校验码功能
l 指定企业编码
l 指定AccessKeyId
l 指定AccessKeySecret
l 指定请求类型
l 指定机构子码
l 指定短信业务类型
l 指定交易码
l 指定渠道码
l 配置HTTP(S)-Plus类型短信网关
l 发送测试短信
l 指定短信网关实例
l 指定发送方名称或者签名

<!-- 来源页 1887 -->
l 指定模板CODE
指定VRouter
系统有一个默认VRouter，即trust-vr，同时系统支持多VR。指定SP所属的VRouter，在SP实例配置模式
下，使用以下命令：
vrouter {trust-vr | vr-name}
l
trust-vr - 指定SP所属VR为默认VR。
l
vr-name – 指定已创建的VR名称。
在SP实例配置模式下使用该命令no的形式恢复为默认VR：
no vrouter
指定发送方式
当SP实例使用HTTP(S)协议类型时，指定系统向短信网关发送HTTP(S)请求时使用的方法，默认为POST方
式。指定发送方式，在SP实例配置模式下，使用以下命令：
request-type [get | post]
l
get –指定使用GET方式来发送HTTP(S)请求。
l
post –指定使用POST方式来发送HTTP(S)请求。
使用no request-type恢复默认发送方式。
指定HTTP（S）报文的内容类型
当SP实例使用HTTP(S)协议类型时，用户可指定系统向短信网关发送HTTP POST请求报文的内容类型
（Content-type），默认为URL-ENCODE。指定HTTP POST请求报文的内容类型，在SP实例配置模式
下，使用以下命令：
content-type {  url-encode | json | xml}
l
url-encode-表示系统向短信网关发送的HTTP POST请求报文的内容类型为application/x-wwwfrom-urlencode。
l
json - 表示系统向短信网关发送的HTTP POST请求报文的内容类型为application/json。
l
xml - 表示系统向短信网关发送的HTTP POST请求报文的内容类型为XML格式。
使用no content-type系统将恢复HTTP POST请求报文的内容类型为默认值URL-ENCODE。

<!-- 来源页 1888 -->
指定编码格式
当SP实例使用HTTP(S)协议类型时，指定认证短信内容的编码格式，默认为UTF-8编码格式。指定编码格
式，在SP实例配置模式下，使用以下命令：
charset [utf-8 | gbk]
l
utf-8–指定使用UTF-8编码格式对认证短信的内容进行编码。
l
gbk–指定使用GBK编码格式对认证短信的内容进行编码。
使用no charset 恢复默认的编码格式。
指定UMS/ACC/BEIKE/ALIYUNSMS/CAS协议
指定UMS、ACC、ALIYUNSMS、BEIKE或者CAS的协议，在SP实例配置模式下，使用以下命令：
protocol {http | https}
l
http | https – 指定UMS、ACC、ALIYUNSMS、BEIKE或者CAS的协议为HTTP或者HTTPS。UMS、
BEIKE及CAS的默认协议为HTTPS，ACC及ALIYUNSMS的默认协议为HTTP。
在SP实例配置模式下，使用该命令no的形式恢复默认协议：
no protocol
配置URL地址
当SP实例使用HTTP(S)协议类型时，指定短信网关的URL地址，需要输入完整的访问路径。系统根据指定的
URL地址向短信网关请求通信。配置URL地址，在SP实例配置模式下，使用以下命令：
url url string
l
url string–指定短信网关的URL地址，例如"http(s)://1.1.1.1"。取值范围为1至255个字符。
使用nourl删除指定的短信网关URL地址。
配置来源号码
当SP实例使用ChinaMobileMusic协议类型时，指定发送验证码短信的号码，即手机终端收到验证码短信后
显示的号码。配置来源号码，在SP实例配置模式下，使用以下命令：
source-addr phone-number
l
phone-number - 指定发送验证码短信的号码。取值范围为8至21位数字。
在SP实例配置模式下，使用no source-addr命令删除指定的来源号码。

<!-- 来源页 1889 -->
配置平台编号
当SP实例使用ChinaMobileMusic协议类型时，指定中国移动音乐短信服务平台的编号，该编号由中国移动
音乐短信服务平台提供。配置平台编号，在SP实例配置模式下，使用以下命令：
device-id id
l
id - 指定中国移动音乐短信服务平台编号。该编号由中国移动音乐短信服务平台提供，为4位数字。
在SP实例配置模式下，使用no device-id命令删除指定的平台编号。
配置平台密码
当SP实例使用ChinaMobileMusic协议类型时，指定中国移动音乐短信服务平台的密码，该密码由中国移动
音乐短信服务平台提供。配置平台密码，在SP实例配置模式下，使用以下命令：
device-pwd password
l
password - 指定中国移动音乐短信服务平台密码。该密码由中国移动音乐短信服务平台提供，为1至
64个字符。
在SP实例配置模式下，使用no device-pwd命令删除指定的平台密码。
配置平台子系统编号
当SP实例使用ChinaMobileMusic协议类型时，指定中国移动音乐短信服务平台子系统的编号，该编号由中
国移动音乐短信服务平台提供。配置平台子系统编号，在SP实例配置模式下，使用以下命令：
access-platform-id id
l
id - 指定中国移动音乐短信服务平台子系统编号。该编号由中国移动音乐短信服务平台提供，为3位或者
7位数字。
在SP实例配置模式下，使用no access-platform-id命令删除指定的平台子系统编号。
配置模板ID
当SP实例使用ChinaMobileMusic协议类型时，指定验证码短信的模板ID，该ID由中国移动音乐短信服务
平台提供。配置模板ID，在SP实例配置模式下，使用以下命令：
templet-id id
l
id - 指定短信模板ID。该ID由中国移动音乐短信服务平台提供，为1至21位数字。
在SP实例配置模式下，使用no templet-id命令删除指定的模板ID。

<!-- 来源页 1890 -->
配置成功标识
当SP实例使用HTTP(S)协议类型时，成功标识用于判断短信网关短信是否发送成功。系统与短信网关交互时
将手机号码、短信内容以及其他参数发送给短信网关。短信网关向收到的手机号码发送认证短信，完成后发
送包含状态码的报文给系统，系统通过报文中是否包含指定的成功标识来判断认证短信是否发送成功。例
如：某短信网关成功发送短信时返回的状态码为“OK:325689”，发送短信失败时返回的状态码为
“ERROR:eUser”，此时用户可以将成功标识设置为“OK”，系统收到短信网关发送的报文后判断其中是
否包含“OK”字符串，有则表示短信发送成功，没有表示发送失败。
配置成功标识，在SP实例配置模式下，使用以下命令：
success-code string
l
string–指定成功标识的内容。取值范围为1至50个字符。不同短信网关返回的状态码不同，指定成功标
识时需要参考使用的短信网关对应的使用手册中给出的状态码。
使用no success-code删除指定的成功标识。
配置根节点
当SP实例使用HTTP(S)协议类型、POST请求方式以及XML内容类型时，指定系统向短信网关发送XML报文
的根节点名称。
配置根节点，在SP实例配置模式下，使用以下命令：
xml-root value
l
value–指定根节点的名称。取值范围为1至20个字符。
使用no xml-root删除指定的根节点。
配置属性
当SP实例使用HTTP(S)协议类型时，不同短信网关的属性不同，系统通过配置的属性参数和短信网关进行交
互。常用的属性包括手机号码字段的参数名称、短信内容字段的参数名称、用户密码以及用户名等，最多可
以配置32条。其中手机号码字段的参数名称、短信内容字段的参数名称为默认属性，必须配置，密码字段和
其他自定义的用户字段均为可选属性。
注意:
l
仅当“发送方式”为“POST”、“内容类型”为“JSON”、参数类型默认为“HTTP DATA”
时，才支持配置节点名称和数组对象。

<!-- 来源页 1891 -->
l
同一个节点名称的属性字段，数组对象配置需保持一致。
配置手机号码字段的参数名称和认证短信内容字段的参数名称
配置手机号码字段的参数名称和认证短信内容字段的参数名称。在SP实例配置模式下，使用以下命令：
default-attribute {phone-attr-name phone-attr-name | msg-content-attr-name msgcontent-name} [ node node-name] [add-to-array ]
l
phone-attr-name phone-attr-name–指定手机号码字段的参数名称，例如phone。此项为默认属
性，取值范围为1至20个字符。
l
msg-content-attr-name msg-content-name–指定短信内容字段的参数名称，例如msg。此项为
默认属性，取值范围为1至20个字符。
l
node node-name - 指定手机号码字段或短信内容字段的节点名称，仅支持输入字母、数字和下划
线，范围是1至20个字符。指定后系统在发送短信时会将JSON或XML格式的HTTP报文中属于同一个节
点名称的属性组合在一起。最多允许配置10个不同的节点名称。
l
add-to-array- 指定将手机号码字段或短信内容字段配置为数组对象，指定该参数后，参数值以数组形
式存储。
短信网关与系统交互时，从系统中获取手机号码和短信内容的参数值。使用no default-attribute
{phone-attr-name | msg-content-attr-name}删除指定的手机号字段的参数名称和短信内容字段的参
数名称。
指定登录短信网关的密码字段参数
指定登录短信网关的密码字段参数，此项为可选属性。在SP实例配置模式下，使用以下命令：
password-attribute {password-name password-value} [ node node-name] [add-to-array ]
l
password-name–指定密码字段的参数名称，例如password。取值范围为1至20个字符。
l
password-value–指定密码字段的参数值，例如123456。取值范围为1至255个字符。
l
node node-name - 指定密码字段的节点名称，仅支持输入字母、数字和下划线，范围是1至20个字
符。指定后系统在发送短信时会将JSON格式的HTTP报文中属于同一个节点名称的属性组合在一起。最
多允许配置10个不同的节点名称。
l
add-to-array- 指定将密码字段配置为数组对象，指定该参数后，密码字段值以数组形式存储。
使用no password-attribute删除指定的密码字段。
指定登录短信网关的自定义用户属性
指定登录短信网关的自定义用户属性，此项为可选属性。在SP实例配置模式下，使用以下命令：

<!-- 来源页 1892 -->
user-attribute {parameter-name value} [ add-to-header | [node node-name] [add-to-array ]
]
l
parameter-name–指定自定义用户属性的参数名称，例如username。取值范围为1至20个字符。
l
value–指定自定义用户属性的参数值，例如user1。取值范围为1至255个字符。
l
add-to-header–表示自定义用户属性参数将被加入到HTTP的头部，若不指定，则该参数将作为HTTP
报文的数据内容（HTTP DATA）。
l
node node-name - 指定自定义用户属性的节点名称，仅支持输入字母、数字和下划线，范围是1至20
个字符。指定后系统在发送短信时会将JSON或XML格式的HTTP报文中属于同一个节点名称的属性组合
在一起。最多允许配置10个不同的节点名称。
l
add-to-array - 指定将自定义用户属性字段配置为数组对象，指定该参数后，参数值以数组形式存
储。
使用no user-attribute {parameter-name } [ add-to-header ]删除指定的自定义用户属性，如配置用
户属性时指定了add-to-header，删除该用户属性时需指定add-to-header。
配置协议子类型
当SP实例使用HTTP(S)协议类型时，可以配置MAS、EMAY、ZGC、ESB、HW或ALIYUN-GLOBE协议子类
型，实现山石网科设备与移动云MAS、亿美短信平台、中关村短信网关平台、ESB短信平台、华为云短信平
台或阿里云国际短信平台对接。配置协议子类型，在SP实例配置模式下，使用以下命令：
subtype { mas | emay | zgc | esb | hw | aliyun-globe}
在SP实例配置模式下，使用no subtype 命令删除MAS、EMAY、ZGC、ESB、HW或ALIYUN-GLOBE协议
子类型的配置。
指定MAS协议子类型时，需要进行下列属性配置。如何进行属性配置，请参阅配置属性：
l
mobiles：在SP实例配置模式下，使用default-attribute phone-attr-name mobiles 命令，指定
手机号码字段的参数名称为“mobiles”。此项必须配置。
l
content：在SP实例配置模式下，使用default-attribute msg-content-attr-name content 命
令，指定短信内容字段的参数名称为“content”。此项必须配置。
l
secretKey：在SP实例配置模式下，使用password-attribute secretKey password-value 命令，
指定登录短信网关的用户密码字段的参数名称为“secretKey”；参数值password-value的取值范围
为1至255个字符。此项必须配置。

<!-- 来源页 1893 -->
l
apId：在SP实例配置模式下，使用user-attribute apId value命令，指定登录短信网关的用户名的
参数名称为“apId”；参数值“ value”的取值范围为1至255个字符；参数类型默认为“HTTP
DATA”。此项必须配置。
l
ecName：在SP实例配置模式下，使用user-attribute ecName value命令，指定企业名称的参数名
称为“ecName”；参数值“ value”的取值范围为1至255个字符；参数类型默认为“HTTP
DATA”。此项必须配置。
l
sign：在SP实例配置模式下，使用user-attribute sign value命令，指定签名编码的参数名称为
“sign”；参数值“ value”由中国移动云MAS短信平台提供；参数类型默认为“HTTP DATA”。此
项必须配置。
l
addSerial：在SP实例配置模式下，使用user-attribute addSerial value命令，指定扩展码的参数
名称为“addSerial”；参数值“ value”由中国移动云MAS短信平台提供；参数类型默认为“HTTP
DATA”。此项为可选配置。
指定ESB协议子类型时，需要进行下列属性配置。如何进行属性配置，请参阅配置属性：
l
MOBILE：在SP实例配置模式下，使用default-attribute phone-attr-name MOBILE 命令，指定手
机号码字段的参数名称为“MOBILE”。此项必须配置。
l
MSG：在SP实例配置模式下，使用default-attribute msg-content-attr-name MSG 命令，指定短
信内容字段的参数名称为“MSG”。此项必须配置。
l
密码字段：在SP实例配置模式下，使用password-attribute password-name password-value
命令，指定ESB短信平台的密码字段的参数名称和参数值。参数名称password-name可自定义配置；
参数值password-value由ESB短信平台提供。此项为可选配置。
l
CHANNEL_CODE：在SP实例配置模式下，使用user-attribute CHANNEL_CODE value命令，指定
渠道名称的参数名称“CHANNEL_CODE”；参数值value由ESB短信平台提供；参数类型默认为
“HTTP DATA”。此项必须配置。
l
SYS_HEAD：在SP实例配置模式下，使用user-attribute {parameter-name value} [node SYS_
HEAD]命令，指定系统向ESB短信平台发送XML报文必须包含的节点名称“SYS_HEAD”，以及属于该
节点名称的属性的参数名称、参数值和参数类型。属性的参数名称parameter-name由ESB短信平台提
供且在配置时必须大写；参数值value根据需求填写；参数类型默认为“HTTP DATA”。此项必须配
置。
l
BODY：在SP实例配置模式下，使用user-attribute {parameter-name value} [node BODY]命
令，指定系统向ESB短信平台发送XML报文必须包含的节点名称“BODY”，以及属于该节点名称的属性

<!-- 来源页 1894 -->
的参数名称、参数值和参数类型。属性的参数名称parameter-name由ESB短信平台提供且在配置时必
须大写；参数值value根据需求填写；参数类型默认为“HTTP DATA”。此项必须配置。
指定HW协议子类型时，需要进行下列属性配置。如何进行属性配置，请参阅配置属性：
l
手机号码字段：在SP实例配置模式下，使用default-attribute phone-attr-name phone-attrname命令，指定手机号码字段的参数名称。参数名称phone-attr-name可自定义配置。此项必须配
置。
l
短信内容字段：在SP实例配置模式下，使用default-attribute msg-content-attr-name msgcontent-name命令，指定短信内容字段的参数名称。参数名称msg-content-name可自定义配置。
此项必须配置。
l
APP_Secret：在SP实例配置模式下，使用password-attribute APP_Secret password-value 命
令，指定登录短信网关的用户密码字段的参数名称为“APP_Secret”；参数值password-value由华
为云短信平台提供。此项必须配置。
l
APP_Key：在SP实例配置模式下，使用user-attribute APP_Key value命令，指定登录短信网关的用
户名的参数名称为“APP_Key”；参数值value由华为云短信平台提供；参数类型默认为“HTTP
DATA”。此项必须配置。
l
sender：在SP实例配置模式下，使用user-attribute sender value命令，指定签名通道号的参数名
称为“sender”；参数值value由华为云短信平台提供；参数类型为“HTTP DATA”。此项必须配
置。
l
templateId：在SP实例配置模式下，使用user-attribute templateId value命令，指定短信模板ID
的参数名称为“templateId”；参数值value由华为云短信平台提供；参数类型为“HTTP DATA”。
此项必须配置。
指定ALIYUN-GLOBE协议子类型时，需要进行下列属性配置。如何进行属性配置，请参阅配置属性：
l
手机号码字段：在SP实例配置模式下，使用default-attribute phone-attr-name phone-attrname命令，指定手机号码字段的参数名称。参数名称phone-attr-name可自定义配置。此项必须配
置。
l
短信内容字段：在SP实例配置模式下，使用default-attribute msg-content-attr-name msgcontent-name命令，指定短信内容字段的参数名称。参数名称msg-content-name可自定义配置。
此项必须配置。

<!-- 来源页 1895 -->
l
Accesskeysecret：在SP实例配置模式下，使用password-attribute Accesskeysecret
password-value 命令，指定山石网科设备和阿里云国际短信网关之间相互认证时，密码字段的参数名
称为“Accesskeysecret”；参数值password-value由阿里云国际短信平台提供。此项必须配置。
l
Accesskeyid：在SP实例配置模式下，使用user-attribute Accesskeyid value命令，指定山石网科
设备和阿里云国际短信网关之间相互认证时，用户名的参数名称为“Accesskeyid”；参数值value由
阿里云国际短信平台提供；参数类型默认为“HTTP DATA”。此项必须配置。
l
From：在SP实例配置模式下，使用user-attribute From value命令，指定短信签名（即短信发送方
的标识）的参数名称为“From”；参数值value由阿里云国际短信平台提供；参数类型为“HTTP
DATA”。此项必须配置。
l
Type：在SP实例配置模式下，使用user-attribute Type {OTP | NOTIFY | MKT}命令，指定短信模板
类型的参数名称为“Type”；参数值为“OTP ”（验证码）、“NOTIFY ”（短信通知）或“ MKT”
（推广短信）；参数类型为“HTTP DATA”。此项必须配置。
注意:
l
指定MAS协议子类型时，为实现山石网科设备与移动云MAS短信平台对接成功，“发送方式”
需设置为“POST”，“内容类型”需设置为“JSON”，“编码格式”需设置为“UTF-8”。
l
指定EMAY协议子类型时，为实现山石网科设备与亿美短信平台对接成功，“发送方式”需设
置为“POST”，“内容类型”需设置为“JSON”。
l
指定ESB协议子类型时，为实现山石网科设备与ESB短信平台对接成功，“发送方式”需设置
为“POST”；“内容类型”需设置为“XML”。
l
指定HW协议子类型时，为实现山石网科设备与华为云短信平台对接成功，“发送方式”需设
置为“POST”。
l
指定ALIYUN-GLOBE协议子类型时，为实现山石网科设备与阿里云国际短信平台对接成功，
“发送方式”需设置为“POST”；“内容类型”需设置为“URL-ENCODE”。
指定短信网关的地址和端口号
指定短信网关的地址和端口号，在SP实例配置模式下，使用以下命令：
gateway {hosthostname | ip ip-address} [port port-number]

<!-- 来源页 1896 -->
l
host hostname - 指定短信网关的主机名称，名称范围为1至31个字符。
l
ip ip-address - 指定短信网关的IP地址。
l
port port-number - 指定短信网关的端口号。当协议类型指定为“SGIP”时，默认端口号为8801；
当协议类型指定为“UMS”时，默认端口号为9600；当协议类型指定为“XUANWU”或“CAS”时，
默认端口号为8080。
多次执行此命令，最新一次执行的命令生效。
在SP实例配置模式下使用该命令no的形式删除短信网关的地址和端口号：
no gateway {hosthostname | ip ip-address}
指定模板参数
指定贝壳短信网关的模板参数，在SP实例配置模式下，使用以下命令：
template value
l
value – 指定贝壳短信网关的模板参数，取值长度为1至64个字符。
在SP实例配置模式下使用该命令no的形式删除贝壳短信网关的模板参数：
no template
设置发送认证短信的号码
当SP实例使用SGIP类型的短信网关时，在开启短信口令认证功能后，系统会向已指定的用户手机号码发送认
证码短信。在SP实例配置模式下，使用以下命令设置手机号码：
source-number phone-number
l
phone-number – 指定用户的手机号码，取值范围为1至21个字符。
在SP实例配置模式下使用该命令no的形式取消用户手机号码的指定：
no source-number
指定设备ID
当SP实例使用SGIP类型的短信网关时，在配置短信网关前，用户需向运营商索取允许发送短信的设备ID。
在SP实例配置模式下，使用以下命令在服务端指定ID：
device-code code-number
l
code-number - 指定设备的ID，取值范围为1至4294967295。

<!-- 来源页 1897 -->
在SP实例配置模式下使用该命令no的形式取消ID号码的指定：
no device-code
指定用户名和密码
指定登录短信网关的用户名称及密码，在SP实例配置模式下，使用以下命令：
user username password password
l
username –指定登录短信网关的用户名称。当协议类型指定为SGIP、UMS或CAS时，名称范围是1至
31个字符；当协议类型指定为XUANWU时，名称范围是1至6个字符。
l
password – 指定登录密码。当协议类型指定为SGIP、UMS或CAS时，取值范围是1至31个字符；当协
议类型指定为XUANWU时，取值范围是1至6个字符。
在SP实例配置模式下使用该命令no的形式取消用户名和密码的指定：
no user
配置短信最大发送数量
当SP实例使用SGIP或UMS类型的短信网关时，管理员可以配置短信网关每小时或者每天最多发送的短信数
量。对超出数量限制的短信，系统将自动丢弃并记录日志信息。配置短信最大发送数量，在SP实例配置模式
下，使用以下命令：
{num-per-hour | num-per-day} number
l
number – 指定短信网关每小时（num-per-hour）或者每天（num-per-day）最多发送的短信数
量。范围为0-65535条。
在SP实例配置模式下使用该命令no的形式取消短信最大发送数量的指定：
no {num-per-hour | num-per-day}
开启/关闭发送校验码功能
开启发送校验码功能后，ACC短信网关向ACC服务器发送请求时会增加校验码字段，从而防止短信内容被篡
改。在SP实例配置模式下，使用以下命令开启发送校验码功能：
sign enable
在SP实例配置模式下使用该命令no的形式关闭发送校验码功能：
no sign enable

<!-- 来源页 1898 -->
指定企业编码
当SP实例使用UMS协议类型时，用户可以指定在UMS平台上注册的企业编码，在SP实例配置模式下，使用
以下命令：
spcode spcode-number
l
spcode-number - 指定企业编码，取值范围为1至31位数字。
在SP实例配置模式下使用该命令no的形式取消企业编码的指定：
no spcode
指定AccessKeyId
当SP实例运行的短信网关协议为ALIYUNSMS时，用户需要指定在阿里云短信服务中申请的AccessKeyId，
作为山石网科设备和阿里云短信网关之间相互认证时的用户名。指定AccessKeyId，在SP实例配置模式下，
使用以下命令：
accesskeyid word
l
word - 指定AccessKeyId，取值范围为1至64个字符。该参数需与在阿里云短信服务中申请的模板
AccessKeyId保持一致。
在SP实例配置模式下，使用no accesskeyid命令取消AccessKeyId的指定。
指定AccessKeySecret
当SP实例运行的短信网关协议为ALIYUNSMS时，用户需要指定在阿里云短信服务中申请的
AccessKeySecret，作为山石网科设备和阿里云短信网关之间相互认证时的密码。指定
AccessKeySecret，在SP实例配置模式下，使用以下命令：
accesskeysecret word
l
word - 指定AccessKeySecret，取值范围为1至63个字符。该参数需与在阿里云短信服务中申请的模
板AccessKeySecret保持一致。
在SP实例配置模式下，使用no accesskeysecret命令取消AccessKeySecret的指定。
指定请求类型
当SP实例运行的短信网关协议为CAS时，用户可向12302短信服务平台索取请求类型，然后进行指定。指定
请求类型，在SP实例配置模式下，使用以下命令：
post_type post_type

<!-- 来源页 1899 -->
l
post_type –指定请求类型，取值范围是1至6个字符。
在SP实例配置模式下，使用no post_type命令取消请求类型的指定。
指定机构子码
当SP实例运行的短信网关协议为CAS时，用户可向12302短信服务平台索取机构子码，然后进行指定。指定
机构子码，在SP实例配置模式下，使用以下命令：
orgcode orgcode
l
orgcode –指定机构子码，取值范围是1至31个字符。
在SP实例配置模式下，使用no orgcode命令取消机构子码的指定。
指定短信业务类型
当SP实例运行的短信网关协议为CAS时，用户可向12302短信服务平台索取短信业务类型，然后进行指定。
指定短信业务类型，在SP实例配置模式下，使用以下命令：
smstype smstype
l
smstype –指定短信业务类型，取值范围是1至31个字符。
在SP实例配置模式下，使用no smstype命令取消短信业务类型的指定。
指定交易码
当SP实例运行的短信网关协议为XUANWU时，用户须向玄武科技短信服务平台索取交易码。指定交易码，
在SP实例配置模式下，使用以下命令：
trading_code trading-code
l
trading-code –指定交易码，取值范围是1至7个字符。
在SP实例配置模式下，使用no trading_code命令取消交易码的指定。
指定渠道码
当SP实例运行的短信网关协议为XUANWU时，用户须向玄武科技短信服务平台索取渠道码。指定渠道码，
在SP实例配置模式下，使用以下命令：
channel channel-value
l
channel-value –指定渠道码，取值范围是a至z。

<!-- 来源页 1900 -->
在SP实例配置模式下，使用no channel命令取消渠道码的指定。
配置HTTP(S)-Plus类型短信网关
山石网科设备支持多种短信网关对接类型，包括联通SGIP协议、电信ACC协议、阿里云短信服务
（ALIYUNSMS）、HTTP(S)协议等，可满足不同运营商、第三方平台及企业自有网关的对接需求。为满足
复杂的接口场景需求，系统支持HTTP(S)-Plus对接类型，支持通过最多5步可自定义的请求与响应流程，实
现与各类短信网关（如企业自研网关、特殊协议第三方平台）的对接。
与设备支持的其他短信网关类型（如SGIP、HTTPS等）相比，HTTP(S)-Plus的差异在于交互流程的灵活性
与场景适配性更强。像传统的HTTP(S)对接类型，仅支持“单步请求- 响应”交互方式，请求参数的字段名
已被系统设定且格式固化，仅能够完成“发送短信并接收结果”的基础需求。当不同厂商短信网关对参数命
名、接口逻辑有差异时，难以快速适配。而HTTP(S)-Plus则具备高度自定义的能力。它基于HTTP(S)协议、
可根据对接的短信网关的接口要求，灵活规划1至5步请求与响应内容。每一步的请求参数（如字段名称、格
式）、交互地址（URL）、请求方式（GET/POST）、响应内容的解析规则、成功条件的判定，均支持自定
义配置。
例如在某高校的实际对接中，高校内部已部署自有短信网关，要求先进行权限校验后才能发送短信。通过
HTTP(S)-Plus，可配置“身份认证→短信模板分类获取→短信模板内容获取→短信发送→状态验证”
5步流程，并可根据需要，将上一步请求的响应结果（如Token、模板ID）作为下一步请求的输入参数。在
流程执行中某一步请求失败，系统会终止整个流程并返回失败提示。这样既保障了多步流程的连贯执行，又
能通过“一步一验证”的方式完成多次有效性校验（如5步流程即完成5次有效性校验）。关于此对接场景的
具体配置，可查阅《StoneOS WebUI手册》的“例：对接第三方短信网关实现SSL VPN二次认证”章节。
提示: 为避免配置过程中遗漏信息或操作出错，建议提前准备并确认以下两类关键信息：
l
在短信网关官方文档中查询获取标准化配置规则，包括：对应接口的路径、请求方法
（GET/POST）、URL参数/请求头/请求体的字段名称及数据格式，以及Content-Type的具
体取值（如application/json，用于指定请求体格式）等。
l
从网关管理员处获取环境信息，包括：短信网关的IP地址或域名、通信端口，以及接口认证所
需的动态信息（如Token令牌、AppKey等）。
配置HTTP(S)-Plus对接类型的短信网关，请参考下表的命令进行配置：
命令行
解释
新增短信网关协议类型
sms service-provider spname protocol http(s)-plus
在全局配置模式下，指定短信网关协议类型为HTTP(S)-Plus。执行该命令
后，系统创建指定名称的SP实例，并且进入SP实例配置模式；如果指定的
名称已存在，则直接进入SP实例配置模式。

<!-- 来源页 1901 -->
命令行
解释
指定五步自定义请求与响应流程
request-round {1 | 2 | 3 | 4 | 5} 指定五步自定义请求与响应流程中当前要配置的步骤。如参数为1，表示配
置第一步请求与响应。
在SP 实例配置模式下，需先通过该命令指定当前步骤（取值1 至5，最多
支持五步）。执行该命令后，进入SP HTTP 请求配置模式，用于配置该步
骤与短信网关单个接口的请求及响应参数，每一步对应一次完整的请求- 响
应交互。
配置请求参数与脚本
address url
配置请求接口地址。
在SP HTTP请求配置模式下，输入该步对应接口的完整访问地址（如
https://sms-gateway.example.com/api/v1/auth）。
type {get | post}
配置请求方法。
在SP HTTP 请求配置模式下，选择当前接口的请求方法（支持GET 或
POST）。
header arg-name value
arg-value
配置请求头参数。
在SP HTTP 请求配置模式下，配置当前请求的HTTP(S) 请求头参数（如
Content-Type: application/json）。
url-arg url-arg-name value
url-arg-value
配置URL 参数。
在SP HTTP 请求配置模式下，配置URL查询参数（如认证Key、Token
等），指定参数名（url-arg-name）与参数值（url-arg-value），确保请
求参数符合网关接口要求。
body string
配置请求体（仅POST 请求生效）。
在SP HTTP 请求配置模式下，配置POST 请求的请求体内容，string参数
需经Base64编码处理后输入。
script-switch turn-on
启用Http Request请求脚本功能。
在SP HTTP 请求配置模式下，启用当前请求的PHP 脚本功能，用于自定义
处理请求参数或格式等。使用no script-switch turn-on命令关闭该功能。
script string
配置请求脚本内容。
在SP HTTP 请求配置模式下，使用该命令配置PHP 脚本，string参数需经
Base64编码处理后输入。
配置响应参数与脚本
rsp-arg arg-name value
arg-value
配置响应参数。
在SP HTTP 请求配置模式下，配置网关响应的参数名称和本地变量，需严
格匹配短信网关该接口的响应结构。arg-name用于指定短信网关该接口响
应数据中实际包含的字段名，以确保系统能够准确获取并解析所需的响应信
息；arg-value用于指定该字段在当前系统中的自定义变量名。
rsp-script-switch turn-on
启用响应脚本功能。

<!-- 来源页 1902 -->
命令行
解释
在SP HTTP 请求配置模式下，启用当前响应的PHP 脚本功能，用于自定义
解析响应内容。使用no rsp-script-switch turn-on命令关闭该功能。
rsp-script string
在SP HTTP 请求配置模式下，通过PHP 脚本对响应数据进行过滤、转换等
处理（如从响应中提取ID 和成功状态），将网关返回的原始响应转换为设
备可识别的格式。string参数需经Base64编码处理后输入。
配置当前步骤响应成功的判定
规则
success-condition-key keyname
配置响应成功条件参数名称。
在SP HTTP 请求配置模式下，指定判定网关响应是否成功的字段名（如短
信网关文档定义参数值为status，参数值1表示返回成功。那么参数值keyname指定为“status”，类型为“等于”，参数值填写为“1”。）。
success-condition-operate { 
equal | unequal | include |
exclude | exist | nonexistent }
配置响应成功条件类型，包含equal（等于）、unequal（不等于）、
include（包含）、exclude（不包含）、exist（存在）、nonexistent
（不存在），用于定义响应字段与成功条件参数值的判定逻辑。
success-condition-value
value
配置响应成功条件参数值。
在SP HTTP 请求配置模式下，输入参数值value。
发送测试短信
为验证设备能否正常发送短信，管理员可以向指定手机号码发送测试短信。发送测试短信，在任意模式下，
使用以下命令：
exec sms sp sp-name send test-message to phone-number [test-msg-content content]
l
sp-name - 指定SP实例的名称。
l
phone-number – 指定接收测试短信的手机号码。
l
content–指定测试短信的内容。默认值为“这是一条测试短信，请不要回复！”，取值范围为1至64个
字符。
注意: 当通过华为云短信网关向指定手机号码发送测试短信时，需执行exec sms sp spname send test-message to phone-number命令。
如果测试短信发送成功，指定手机号码会收到系统发送的测试短信；如果测试短信发送失败，系统会记录日
志并描述失败原因。

<!-- 来源页 1903 -->
指定短信网关实例
配置好的SP实例需要绑定到ZTNA实例才能生效。在ZTNA实例配置模式下，使用以下命令指定短信网关实
例：
sms-auth enable servicer-provider sp-name
l
sp-name – 指定SP实例的名称，该名称须是已创建的SP实例名称。取值范围为1至31个字符。
指定发送方名称或者签名
当绑定到ZTNA隧道的SP实例的协议类型为SGIP、USM或者ACC时，用户可以指定短信发送方名称以显示在
短信内容中；当绑定到ZTNA隧道的SP实例的协议类型为ALIYUNSMS时，用户需要输入在阿里云短信服务
中申请的短信签名，以显示在短信内容中。指定发送方名称或者短信签名，在ZTNA实例配置模式下，使用
以下命令：
sms-auth sms-sender-name sender-name [without-auto-bracket]
l
sender-name – 指定发送方名称或者签名。取值范围是1到63字符。该签名需要与在阿里云短信服务
中申请的签名保持一致。
l
without-auto-bracket– 关闭发送方名称自动添加尖括号功能。例如，当短信网关名称指定为SGIP或
UMS服务商名称，且用户配置了发送方名称时，如果不配置该参数，验证短信中的发送方名称将会自动
添加尖括号。如果配置该参数，验证短信中的发送方名称不会自动添加尖括号。
在ZTNA实例配置模式下，使用该命令no的形式取消发送方名称或者签名的指定：
no sms-auth sms-sender-name
注意:
l
由于UMS企业信息平台限制，当使用短信网关认证时，发送方名称将会显示在UMS企业信息平
台注册的名称。
l
发送方名称自动添加尖括号功能对针对默认短信验证内容有效，若用户自定义配置了短信验证
内容，发送方名称自动添加尖括号功能将失效。如需要，用户可以在配置短信验证内容时，直
接在短信模板内容末尾处手动添加带尖括号的发送方名称。配置短信验证内容，请参阅配置短
信验证内容。

<!-- 来源页 1904 -->
指定模板CODE
当绑定到ZTNA实例的SP实例的协议类型为ALIYUNSMS时，用户需要指定在阿里云短信服务中申请的短信
内容模板对应的CODE（代码）。指定模板CODE，在ZTNA实例配置模式下，使用以下命令：
sms-auth sms-msg-templatecode word
l
word - 指定模板CODE，取值范围为1至30个字符。该参数需与在阿里云短信服务中申请的模板CODE
保持一致。
在ZTNA实例配置模式下，使用no sms-auth sms-msg-templatecode命令取消模板CODE的指定。
显示短信网关配置信息
在任意模式下，使用以下命令查看短信网关的配置信息：
show sms service-provider [sp-name]
l
sp-name – 指定已创建的SP实例。如不指定，则默认显示所有已创建的SP实例的配置信息。
显示短信统计信息
在任意模式下，使用以下命令查看短信网关发送短信成功或失败的计数信息：
show tunnel ztna ztna-name smsp-statistice [clear]
l
ztna-name– 指定已创建的ZTNA实例名称。
l
clear– 清除所有的计数信息。

<!-- 来源页 1905 -->
配置邮件口令认证
邮件口令认证功能是指ZTNA用户使用用户名/密码或用户名/密码+数字证书方式登录时，收到登录请求的山
石网科设备通过邮件服务器自动向该用户的邮箱发送一条包含随机认证码的邮件，用户输入收到的认证码
后，才可以通过认证，进而访问内网资源。
邮件口令认证功能的服务端配置包括：
l 配置接收认证码邮箱
l 指定邮件服务器
l 配置认证码长度
l 配置认证码有效时间
l 配置发送方名称
l 配置邮件验证内容
配置接收认证码邮箱
用户可以通过本地认证服务器和Radius认证服务器中配置的邮箱接收认证码。
当通过本地认证服务器中配置的邮箱接收认证码时，需要在本地认证服务器的用户配置模式下，使用以下命
令指定邮箱：
email email-address
l
email-address – 指定当用户通过本地认证服务器中配置的邮箱接收认证码时，用于接收认证码的邮
箱。取值范围为1至127个字符。
在用户配置模式下，使用no email命令取消用户邮箱的指定。
当通过Radius认证服务器中配置的邮箱接收认证码时，需要在Radius服务器中指定用户的邮箱。以下以
FreeRadius为例
“test1” Cleartext-Password：=“123456”
Login-LAT-Group="radiusgroup1",
Hillstone-user-type=16,
Hillstone-user-vsys-id=0,
Hillstone-user-login-type=63,
Hillstone-user-admin-privilege=4294967295,
Hillstone-user-email=user-test@hillstonenet.com ( 在

<!-- 来源页 1906 -->
“etc/freeradius/users”中添加Hillstone-user-email属性值)
指定邮件服务器
指定邮件服务器，该服务器上配有用于发送认证码的邮箱地址，在ZTNA实例配置模式下，使用以下命令：
email-auth smtp-server smtp-server-name
l
smtp-server--name – 指定邮件服务器，该服务器为系统中已配置的邮件服务器。取值范围为1至31
个字符。
在ZTNA实例配置模式下，使用no email-auth smtp-server命令取消邮件服务器的指定。
配置认证码长度
配置邮件认证码长度，在ZTNA实例配置模式下，使用以下命令：
email-auth verification-code-length length
l
length – 指定邮件认证码长度。取值范围为4至8个字符。默认为8个字符。
在ZTNA实例配置模式下，使用no email-auth verification-code-length恢复默认认证码长度。
配置认证码有效时间
每个邮件认证码都有一个有效时间，如果用户在有效时间内没有输入认证码也没有重新申请认证码，ZTNA
服务端将自动断开连接。配置邮件认证码的有效时间，在ZTNA实例配置模式下，使用以下命令：
email-auth expiration value
l
value – 指定邮件认证码的有效时间。取值范围为1至10分钟。默认为10分钟。
在ZTNA实例配置模式下，使用no email-auth expiration恢复默认有效时间。
配置发送方名称
配置认证码的发送方名称以显示在邮件内容中，在ZTNA实例配置模式下，使用以下命令：
email-auth sender-name name
l
name – 指定认证码的发送方名称。取值范围为1至63个字符。为防止认证码邮件被认定为垃圾邮件，
建议用户进行认证码邮件发送方名称的配置。
在ZTNA实例配置模式下，使用no email-auth sender-name恢复默认发送方名称。
配置邮件验证内容
配置认证码邮件的验证内容，在ZTNA实例配置模式下，使用以下命令：
email-auth message-content content

<!-- 来源页 1907 -->
l
content – 指定认证码邮件的验证内容，内容必须包含“＄USERNAME”和“＄VRFYCODE”
（“＄USERNAME”用于获取用名；“＄VRFYCODE”用于获取认证码）。取值范围为18至128个字
符。默认内容为“ZTNA user <＄USERNAME> email verification code: ＄VRFYCODE. Do not
reveal to anyone! If you did not request this, please ignore it.”。
在ZTNA实例配置模式下，使用no email-auth message-content恢复默认验证内容。
单包授权（SPA）
介绍
SPA（Single Packet Authorization，单包授权）是一种网络安全技术，它通过在单个加密的数据包中封
装所有必要的认证信息，并在建立网络连接之前验证用户和设备的身份，确保只有携带正确认证信息的数据
包才能访问特定的服务地址和端口。SPA技术通过隐藏服务端口，降低服务被发现和攻击的风险，从而增强
网络安全。简而言之，SPA允许网络服务在不暴露的情况下进行安全通信，有效防止未授权访问和网络攻
击。
应用场景
SPA适用于最小化网络暴露和保护服务不被恶意扫描的环境，通常应用在需要高安全性的场景。目前，该功
能仅支持在部署零信任网络访问（ZTNA）的场景下使用。
SPA工作原理
启用SPA功能后，客户端将发送一个加密的UDP数据包至服务端的敲门端口以发起连接请求。成功敲门后，
服务端依据配置的隐藏地址（包括隐藏IP和端口）和源IP，生成对应的放行表项。当客户端发出连接请求

<!-- 来源页 1908 -->
时，服务端将核查请求的IP和端口是否与放行表项匹配。匹配成功则允许建立安全连接，若无匹配的放行表
项则拒绝请求并丢弃该数据包。
下面以在ZTNA远程访问场景下开启SPA功能为例，详细介绍ZTNA用户通过客户端登录时SPA的工作流程。
1. 客户端将时间戳、随机值、目的端口等信息通过数据加密封装成一个UDP包发送给ZTNA服务端进行敲门（该动
作称之为“SPA敲门”，目的端口即为敲门端口）。为防止UDP丢包，客户端会将该UDP包连续发送3次。
2. ZTNA服务端接收到敲门报文后，会对该报文进行校验。若校验通过，则说明敲门成功，ZTNA服务端会根据配置
的隐藏地址（包括隐藏IP和端口）和源IP，生成对应的放行表项；反之，敲门失败并丢弃该报文。
3. 客户端发送ZTNA连接请求。
4. ZTNA服务端检查连接请求的IP和端口是否为隐藏IP和端口。如果是隐藏IP和端口，则查询是否存在匹配的放行表
项。如果存在，则允许建立ZTNA连接。如果不存在会丢弃报文。
注意: 放行表项的老化时间为30秒，如果客户端在30秒内未与服务端建立连接，那么对应的放行表
项会被删除。
配置单包授权（SPA）
开始之前
l 阅读单包授权（SPA）介绍
开启单包授权（SPA）功能，可按照以下流程进行配置：

<!-- 来源页 1909 -->
1. 配置ZTNA实例
2. 配置单包授权（SPA）功能
3. 配置应用资源/应用资源组
4. 配置终端信息
5. 配置终端标签
6. 配置ZTNA策略
配置单包授权（SPA）
开启/关闭SPA功能
SPA功能默认为关闭状态。
开启/关闭SPA功能，在全局配置模式下，使用以下命令：
l
开启：spa enable
l
关闭：no spa enable
配置本地敲门端口
本地敲门端口是ZTNA服务端接收敲门报文的端口号，默认为60001。
配置本地敲门端口，在全局配置模式下，使用以下命令：
spa knock-port port-number
l
port-number - 指定本地敲门端口号，取值范围是1025到65535，默认值是60001。
在全局配置模式下，使用以下命令将本地敲门端口号恢复为默认值：
no spa knock-port
配置隐藏的IP和端口
在开启SPA功能时，需配置隐藏的IP和端口，SPA功能才会生效。当服务端关闭SPA或开启了SPA但未配置
隐藏IP和端口时，无论客户端是否开启SPA，服务端都不会对客户端进行SPA校验。
配置隐藏IP和端口，在全局配置模式下，使用以下命令：
spa hide service-ip ip-address port port-number vrouter vrouter-name [description
description]

<!-- 来源页 1910 -->
l
ip-address - 指定需要隐藏的IPv4地址。
l
port-number - 指定需要隐藏的端口号，取值范围是1到65535。
l
vrouter-name - 指定隐藏IP所在接口绑定的虚拟路由器名称。
l
description - 指定描述信息，取值范围是1到63个字符。
可以重复配置该命令添加多条需要隐藏的IP和端口。
删除指定的隐藏IP和端口设置，在全局配置模式下，使用以下命令：
no spa hide service-ip ip-address port port-number vrouter vrouter-name
查看SPA配置信息
查看SPA配置信息，在任意模式下，使用以下命令：
show spa
查看SPA放行表项
查看SPA放行表项，在任意模式下，使用以下命令：
show spa-entry
管理终端标签日志
系统支持配置终端标签日志功能对终端标签日志单独管理。
开启/关闭终端标签日志功能
终端标签日志功能默认为开启。
开启/关闭终端标签日志功能，在全局配置模式下，使用以下命令：
l
开启：logging endpoint-tag on
l
关闭：no logging endpoint-tag on
清除终端标签日志
清除终端标签日志，在全局配置模式下，使用以下命令：
clear logging endpoint-tag
输出终端标签日志
开启终端标签日志功能后，系统会默认将终端标签日志输出到内存缓存。用户可以根据需要将终端标签日志
输出到其他目的地，可以配置多个输出目的地。
配置设备将终端标签日志输出到指定目的地，在全局配置模式下使用以下命令：

<!-- 来源页 1911 -->
logging endpoint-tag to {console | syslog | localdb | buffer [size buffer-size] }
l
console - 输出终端标签日志到console口。
l
syslog - 输出终端标签日志到Syslog服务器。关于Syslog服务器的配置说明，请参阅配置Syslog
Server。
l
localdb - 输出终端标签日志到设备硬盘，仅在A（不含A2200、A1800和A1600）和K（不含
K9180）系列带硬盘的设备及X8180、X20812带硬盘的主控模块上支持。
l
buffer - 输出终端标签日志到内存缓存。
l
size buffer-size - 指定内存缓存的大小，单位是字节，取值范围是4096到2097152。默认的缓存大
小是2097152。
取消输出终端标签日志到指定的目的地，在全局配置模式下使用以下命令：
no logging endpoint-tag to {console | syslog | localdb | buffer}
配置硬盘存储空间阈值
在配置了将终端标签日志输出到硬盘时，可以配置终端标签日志占用的硬盘存储空间阈值。在全局配置模式
下，使用以下命令：
storage threshold log endpoint-tag percent
l
percent - 指定终端标签日志占用的硬盘存储空间阈值。取值范围是0.01到90，单位为百分比。默认值
为1。当终端标签日志占用的硬盘空间超过指定的阈值时，将根据storage threshold percent命令的
配置覆盖早期日志或停止在硬盘中记录日志。
设置终端标签日志的缓存配额
在配置了将终端标签日志输出到内存缓存时，根系统管理员可以通过Profile为VSYS设置终端标签日志占用
内存缓存的预留配额和最大配额。预留配额即系统为每个VSYS的终端标签日志预留的日志缓存值；最大配额
即每个VSYS的终端标签日志可获得的最大日志缓存值。如果VSYS中终端标签日志的容量超过其最大配额，
那么新增加的终端标签日志将覆盖掉缓存中最早的日志。
设置VSYS中终端标签日志的缓存配额，在VSYS Profile配置模式下使用以下命令：
log endpoint-tag buffer-size max max-num reserve reserve-num
l
max max-num reserve reserve-num – 指定VSYS中终端标签日志的最大配额（max max-num）
和预留配额（reserve reserve-num），单位是字节。最大配额和预留配额在不同平台上的取值范围不
同，请以实际为准。预留配额不能超过最大配额。
关于VSYS Profile的配置说明，请参阅创建VSYS Profile。

<!-- 来源页 1912 -->
查看终端标签日志
查看终端标签日志，在任意模式下，使用以下命令：
show logging endpoint-tag
ZTNA Portal
ZTNA用户登录成功后，用户终端会通过默认浏览器弹出ZTNA Portal页面，展示用户有权限和无权限访问
的应用资源。
l 有权限访问：当用户的认证信息和终端标签匹配动作类型为Permit的ZTNA策略时，用户有权限访问策略中绑定
的应用资源。
l 无权限访问：当用户的认证信息匹配ZTNA策略，但终端标签不匹配ZTNA策略时，用户无权限访问策略中绑定的
应用资源。
对于有权限访问的应用资源，用户可以通过点击应用资源图标跳转到相应的URL地址，或者复制URL地址到
浏览器访问。对于无权限访问的应用资源，用户可以查看提示信息了解无权限访问的原因。
ZTNA Portal页面不展示以下应用资源：
l 禁止用户访问的应用资源
l 允许用户访问，但未指定超链接的应用资源
在ZTNA Portal页面关闭后，用户可以通过ZTNA客户端的“应用资源列表”菜单重新获取ZTNA Portal页
面。
注意: 当关闭ZTNA Portal页面弹窗功能时，用户将无法通过ZTNA客户端的“应用资源列表”菜
单打开ZTNA Portal页面。
查看ZTNA信息
显示ZTNA信息
用户可以通过show命令查看系统ZTNA信息。
l
显示ZTNA实例信息：
show tunnel ztna [ztna-instance-name]

<!-- 来源页 1913 -->
l
显示ZTNA认证用户的信息：
show auth-user ztna [interface interface-name | groupname group-name | vrouter
vrouter-name | endpoint-tag endpoint-tag-name]
l
显示客户端信息：
show secure-connect client-info
l
显示ZTNA用户信息：
show ztna-user ztna-instance-name [user user-name]
l
显示ZTNA许可证的授权用户数量：
show secure-connect user capacity
l
显示客户端升级URL：
show secure-connect update-url
l
显示客户端下载页面的定制标题：
show secure-connect download-web-page-title

<!-- 来源页 1914 -->
ZTNA客户端
ZTNA与SSL VPN共用Hillstone Secure Connect客户端，如需访问ZTNA服务，请下载和安装最新版本的
客户端，升级后的客户端支持ZTNA接入，也支持SSL VPN接入。目前，ZTNA远程访问解决方案支持
Windows、macOS、Linux、iOS、Android和国产操作系统终端接入，ZTNA内网接入解决方案支持
Windows、macOS、Linux和国产操作系统终端接入，接入时需登录相应的客户端，安装和使用方法请参
阅对应客户端。
l "Hillstone Secure Connect客户端for Windows" 在第1921页
l "Hillstone Secure Connect客户端for macOS" 在第1944页
l "Hillstone Secure Connect客户端for Linux" 在第1953页
l "Hillstone Secure Connect客户端for iOS" 在第1938页
l "Hillstone Secure Connect客户端for Android" 在第1933页
l "Hillstone Secure Connect客户端for ChineseOS" 在第1964页

<!-- 来源页 1915 -->
Secure Connect客户端
终端用户可以通过以下地址下载Secure Connect客户端：
l 访问服务端提供的客户端下载地址https://IP-Address:Port-Number。其中“IP-Address”和“PortNumber”分别为SSL VPN或ZTNA实例中指定的接口的IP地址和HTTPS端口号。
l 访问山石网科官方提供的客户端下载地址https://www.hillstonenet.com.cn/support-andtraining/hillstone-secure-connect/。
l 国产操作系统的客户端请在操作系统自带的软件应用商店搜索“Hillstone Secure Connect”，进行下载安装。
默认情况下，服务端和山石网科官网两个地址的客户端下载源相同，下载到的Secure Connect客户端也是
相同的。
客户端通用配置
以下配置属于ZTNA和SSL VPN通用配置，配置后对ZTNA和SSL VPN都生效。
l 配置SSL加密套件
l 允许本地用户修改密码
l 强制断开客户端SSL VPN连接
l 配置客户端修改密码URL
l 配置客户端忘记密码URL
l 配置客户端自动重连
l 配置允许接入的客户端类型
l 查看Secure Connect客户端信息
l 配置客户端升级URL
配置SSL加密套件
配置SSL密码套件，在全局配置模式下使用以下命令：
secure-connect ssl-cipher-list string
l
string - 指定SSL密码套件列表，取值为1至511个字符。默认值为
“ALL:!EXPORT:!LOW:!aNULL:!eNULL:!SSLv2:!RC4"。
在全局配置模式下，使用该命令no的形式恢复默认的SSL密码套件：
no secure-connect ssl-cipher-list

<!-- 来源页 1916 -->
允许本地用户修改密码
Hillstone设备支持本地用户成功通过SSL VPN或ZTNA认证后，在客户端修改自己的用户密码。默认情况
下，该功能为关闭状态。在密码控制配置模式下，使用以下命令开启或关闭允许本地用户修改登录密码功
能：
l
开启：allow-pwd-change
l
关闭：no allow-pwd-change
注意: Secure Connect客户端1.2.0.1106（Hillstone Secure Connect 1.2.0.1106）及后续
版本支持允许本地用户修改密码功能。为避免出错，建议用户使用最新版本的Secure Connect客
户端。
开启该功能并成功通过SSL VPN或ZTNA认证后，本地用户可通过以下步骤修改登录密码：
1. 右键单击系统任务栏通知区域的Hillstone Secure Connect绿色图标，系统弹出客户端菜单，如下图所示：
2. 点击<修改密码>，系统弹出<修改密码>对话框。在<当前密码>文本框中输入正确的旧密码，在<新密码>文本框
中输入新密码并在<确认新密码>处再次输入相同的新密码。如下图所示：

<!-- 来源页 1917 -->
3. 点击『确定』按钮，系统显示提示信息“修改密码成功”。
强制断开客户端用户连接
强制断开SSL VPN客户端用户连接
服务端可以通过命令强制断开某个客户端用户与服务端的连接。强制断开SSL VPN客户端用户连接，在执行
模式使用以下命令：
exec scvpn instance-name {kickout user-name | kickout-all-user }
l
instance-name – 指定SSL VPN实例的名称。
l
user-name – 指定被强制断开连接的用户名称。
l
kickout-all-user - 指定断开该实例的所有在线用户。
强制断开ZTNA客户端用户连接
服务端可以通过命令强制断开某个客户端用户与服务端的连接。强制断开ZTNA客户端用户连接，在任意模
式使用以下命令：
exec ztna instance-name kickout user-name
l
instance-name – 指定ZTNA实例的名称。
l
user-name – 指定被强制断开连接的用户名称。
强制断开所有ZTNA客户端用户与设备的连接，在任意模式下使用以下命令：
exec ztna instance-name kickout-all-user
l
instance-name - 指定ZTNA实例的名称。

<!-- 来源页 1918 -->
配置客户端修改密码URL
系统支持客户端通过配置的URL跳转到指定的页面修改密码。
配置修改密码URL，在SSL VPN实例模式、内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式
下，执行以下命令：
change-password-urlurl
l
url – 配置修改密码需要跳转的URL地址，长度取值范围1-255字符。
在SSL VPN实例模式、内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用no changepassword-url命令取消修改密码URL的配置。
配置客户端忘记密码URL
系统支持客户端通过配置的URL跳转到指定的页面重新配置密码。
配置忘记密码URL，在SSL VPN实例模式、内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式
下，执行以下命令：
forgot-password-urlurl
l
url – 配置重新配置密码需要跳转的URL地址，长度取值范围1-255字符。
在SSL VPN实例模式、内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用no forgotpassword-url命令取消忘记密码URL的配置。
配置客户端自动重连
系统支持客户端在网络连接断开时自动重连。
配置客户端自动重连，在SSL VPN实例模式、内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式
下，执行以下命令：
client-auto-connect count {number | unlimited}
l
number | unlimited - 指定客户端的自动重连次数。number指定具体的次数，取值范围为0至
1024。unlimited表示不自动重连。默认为unlimited。
在SSL VPN实例模式、内网接入ZTNA实例配置模式或者远程访问ZTNA实例配置模式下，使用no clientauto-connect命令将客户端自动重连次数恢复为默认值。
no client-auto-connect

<!-- 来源页 1919 -->
配置允许接入的客户端类型
配置允许接入的SSL VPN客户端类型
默认情况下，系统允许8种类型的SSL VPN客户端接入，分别为Windows系统客户端、Android系统客户
端、iOS系统客户端、macOS系统客户端、Linux系统客户端、国产操作系统客户端、HarmonyOS PC系统
客户端和HarmonyOS Mobile(5.0+)系统客户端。用户可以根据需要，配置仅允许指定类型的SSL VPN客
户端接入。
配置允许接入的客户端类型，在SSL VPN实例配置模式下执行以下命令：
allowed-client-type {Android | iOS | Linux | macOS | Windows | ChineseOS | HarmonyOS-PC |
HarmonyOS-Mobile}
l
Android | iOS | Linux | macOS | Windows | ChineseOS | HarmonyOS-PC | HarmonyOSMobile - 指定允许接入的SSL VPN客户端类型，可以为Windows系统客户端（Windows）、
Android系统客户端（Android）、iOS系统客户端（iOS）、macOS系统客户端（macOS ）、Linux
系统客户端（Linux）、国产操作系统客户端（ChineseOS）、HarmonyOS PC系统客户端
（HarmonyOS-PC）或HarmonyOS Mobile(5.0+)系统客户端（HarmonyOS-Mobile）。
多次执行该命令，允许多种类型的SSL VPN客户端接入。
在SSL VPN实例配置模式下使用no allowed-client-type {Android | iOS | Linux | macOS | Windows |
ChineseOS | HarmonyOS-PC | HarmonyOS-Mobile}命令，禁止指定类型的SSL VPN客户端接入。
配置允许接入的ZTNA客户端类型
默认情况下，系统允许8种类型的ZTNA客户端接入，分别为Windows系统客户端、Android系统客户端、
iOS系统客户端、macOS系统客户端、Linux系统客户端、国产操作系统客户端、HarmonyOS PC系统客户
端和HarmonyOS Mobile(5.0+)系统客户端。用户可以根据需要，配置仅允许指定类型的ZTNA客户端接
入。
配置允许接入的客户端类型，在ZTNA实例配置模式下，执行以下命令：
allowed-client-type {Android | iOS | Linux | macOS | Windows | ChineseOS | HarmonyOS-PC |
HarmonyOS-Mobile}
l
Android | iOS | Linux | macOS | Windows| ChineseOS | HarmonyOS-PC | HarmonyOS-Mobile
- 指定允许接入的ZTNA客户端类型，可以为Windows系统客户端（Windows）、Android系统客户端
（Android）、iOS系统客户端（iOS）、macOS系统客户端（macOS ）、Linux系统客户端

<!-- 来源页 1920 -->
（Linux）、国产操作系统客户端（ChineseOS）、HarmonyOS PC系统客户端（HarmonyOS-PC）
或HarmonyOS Mobile(5.0+)系统客户端（HarmonyOS-Mobile）。
多次执行该命令，允许多种类型的ZTNA客户端接入。
在ZTNA实例配置模式下，使用no allowed-client-type {Android | iOS | Linux | macOS | Windows |
ChineseOS | HarmonyOS-PC | HarmonyOS-Mobile}命令，禁止指定类型的ZTNA客户端接入。
查看Secure Connect客户端信息
在任意模式下，使用以下命令查看系统内保存的Secure Connect客户端信息：
show secure-connect client-info [windows | linux | macos]
配置Windows/Linux/macOS类型客户端的升级URL
Windows/Linux/macOS类型客户端通过配置的URL进行新版本检查及下载升级。系统默认已经存在指向
官方升级服务器的URL，且此URL不可删除。Window/Linux/macOS类型的客户端会通过此官方升级服务
器的URL进行新版本检查以及下载升级。配置升级URL，在全局配置模式下执行以下命令：
secure-connect update-url url
l
url – 如果需要使用内网服务器进行客户端新版本的检查以及下载升级，则输入内网服务器URL。用户需
要自行在此服务器部署客户端新版本。
在全局配置模式下，使用该命令no的形式恢复默认的官方升级服务器的URL：
no secure-connect update-url
查看升级服务器的URL，在任意模式下使用以下命令：
show secure-connect update-url
注意:
l
当客户端版本为1.4.4.1199或更低版本且StoneOS版本为5.5R1或更高版本，推荐卸载旧版客
户端并重新登陆Web下载安装。
l
如需用户下载系统镜像里自带的Windows类型客户端，配置该命令为secure-connect
update-url localhost。
l
通过import secure-connect client命令导入Windows/Linux/macOS类型客户端后，
secure-connect update-url配置将不生效。

<!-- 来源页 1921 -->
自定义客户端
l 定制客户端下载源
l 定制客户端下载页面背景图
l 定制客户端下载页面标题
定制客户端下载源
从服务器导入客户端文件
从服务器导入客户端文件，在执行模式下使用以下命令：
import secure-connect client {windows | linux | macos} from { {ftp | ftps | sftp} server ipaddress [vrouter vrouter-name] [user user-name password password] | tftp server ipaddress | usb0 | usb1} file-name
l
{ftp | ftps | sftp} server ip-address [vrouter vrouter-name] [user user-name password
password] –指定从FTP/FTPS/SFTP服务器获取客户端文件，并指定FTP服务器的IP地址、虚拟路由器
名称以及访问服务器使用的用户名和密码。当不输入用户名和密码时表示采用匿名登录方式。
l
tftp server ip-address - 指定从TFTP服务器导入客户端文件，并指定TFTP服务器的IP地址。
l
usb0 | usb1 - 指定通过USB方式从USB0或者USB1插槽所对应的U盘根目录导入客户端文件。
l
file-name – 指定客户端文件。系统会对导入的文件进行校验，建议导入下载自山石网科官网的客户端
文件，且未修改过文件名，否则会导入失败。
删除导入的客户端
系统支持删除导入的客户端，删除后，客户端下载源将恢复为默认下载源。在执行模式下使用以下命令删除
导入的客户端：
exec secure-connect client {windows | linux | macos} delete
定制客户端下载页面背景图
设备支持用户自行定制客户端下载页面。默认情况下，配置ZTNA认证功能后，其下载页面如下图所示：

<!-- 来源页 1922 -->
用户可以通过改变下载页面上的背景图片自行定制下载页面。从服务器导入背景图片，在执行模式下使用以
下命令：
import customize secure-connect download-webpage-background-picture from { {ftp | ftps
| sftp} server ip-address [vrouter vrouter-name] [user user-name password password] | tftp
server ip-address | usb0 | usb1} file-name
l
{ftp | ftps | sftp} server ip-address [vrouter vrouter-name] [user user-name password
password] – 指定从FTP/FTPS/SFTP服务器获取图片，并指定FTP/FTPS/SFTP服务器的IP地址、虚拟
路由器名称以及访问服务器使用的用户名和密码。当不输入用户名和密码时表示采用匿名登录方式。
l
tftp server ip-address – 指定从TFTP服务器获取图片，并指定TFTP服务器的IP地址。
l
usb0 | usb1 – 指定通过USB方式从USB0或者USB1插槽所对应的U盘根目录获取图片。
l
file-name – 指定图片名称、图片格式。图片须为PNG格式，分辨率建议为1920px*1080px，并且图
片大小须小于2MB。
恢复默认背景图片，在任意模式下，使用以下命令：
exec customize secure-connect download-webpage-background-picture default
定制客户端下载页面标题
默认情况下，客户端下载页面的标题为“Hillstone Secure Connect”。
定制客户端下载页面的标题，在全局配置模式下使用以下命令：
secure-connect download-web-page-title title

<!-- 来源页 1923 -->
l
title - 指定客户端下载页面的标题，取值范围为1至63个字符。
在全局配置模式下，使用该命令no的形式删除定制标题，删除后下载页面将不显示任何标题：
no secure-connect download-web-page-title
查看客户端下载页面的定制标题，在任意模式下，使用以下命令：
show secure-connect download-web-page-title
Hillstone Secure Connect客户端for Windows
型号说明：v5.4.0及以上版本的Secure Connect Windows客户端支持接入双栈类型的SSL
VPN/ZTNA实例。
支持Windows系统的SSL VPN/ZTNA客户端工具为Hillstone Secure Connect，建议在以下操作系统中
运行：
l Windows7 SP1、Windows8.1、Windows10、Windows11
l Windows server 2008 R2、Windows server 2012、Windows server 2012 R2、Windows server 2016、
Windows server 2019、Windows server 2022
通过客户端与服务端的连接，即可实现数据的加密通信。该客户端的主要作用包括：
l 从服务端获得虚拟IP和路由信息；
l 显示与连接状态、数据流统计数据以及接口和路由信息；
l 显示应用程序日志信息；
l 调用客户端更新程序进行客户端更新；
l 解析从服务端接收到的资源列表信息；
l 采集和上报终端状态信息。
本节主要介绍Secure Connect Windows客户端的下载、安装和启动等。服务端对客户端支持以下四种认
证方式：
l 用户名/密码
l 用户名/密码+ 数字证书（包括USB Key证书和软证书）
l 只用数字证书（包括USB Key证书和软证书）
l 第三方应用登录（OAuth2认证、企业微信认证和钉钉认证）

<!-- 来源页 1924 -->
下载与安装
可以通过以下方法下载Secure Connect Windows客户端：
l 访问Hillstone官网客户端下载页面https://www.hillstonenet.com.cn/support-and-training/hillstonesecure-connect/。
l 在浏览器的地址栏输入以下URL访问服务端下载和安装：https://IP-Address:Port-Number。其中“IPAddress”和“Port-Number”分别为服务端SSL VPN或ZTNA实例中指定的接口的IP地址和HTTPS端口号。
成功安装Secure Connect Windows客户端后，将有一个虚拟网卡安装到PC上。该虚拟网卡用来实现客户
端与服务端信息的安全加密传输。
启动与连接
客户端安装成功后，按照以下步骤启动和登录客户端：
1. 双击桌面的Secure Connect Windows客户端快捷方式，或者点击“开始菜单”中的“所有程序> Hillstone
Secure Connect > Hillstone Secure Connect”，系统弹出客户端页面。
2. 点击“添加连接”按钮，系统弹出下图所示对话框。
输入连接信息。
选项
说明
TLS/SSL
选择该页签，表示使用TLS/SSL加密协议。

<!-- 来源页 1925 -->
选项
说明
国密SSL
选择该页签，表示使用国密SSL协议。
连接名称
填写连接名称。
服务器
填写SSL VPN或ZTNA服务端的服务IP地址。
端口
填写SSL VPN或ZTNA服务端的HTTPS端口号。
高级配置：默认是折叠状态。点击
按钮，配置如下功能。
最优通道
设置是否开启最优路径检测功能。该功能用于SSL VPN访问场景。当服务端和客户端同
时开启最优路径检测功能后，不同ISP线路接入的客户端可以自动选择最快线路连接到
SSL VPN服务端。默认为关闭。
网关探测
设置是否开启网关探测功能。该功能用于ZTNA访问场景。当ZTNA服务端配置了备选网
关时，ZTNA客户端可以开启网关探测功能。用户登录时，ZTNA客户端会先获取备选网
关列表，探测每个备选网关的链路质量，并选择链路质量最优的网关建立ZTNA连接。建
立连接后，客户端会每隔30分钟更新一次备选网关的链路质量。如果发生连接中断或用
户登录失败，客户端会自动切换到链路质量最优的备选网关重新建立连接。默认为开
启。
最优网关
开启网关探测后，ZTNA客户端会在用户登录时获取到备选网关列表，此时用户可以手动
选择最优网关。最优网关默认不指定。如果指定了最优网关，用户再次登录时，ZTNA客
户端将优先向最优网关地址发起连接请求，若连接失败，则自动切换到链路质量最优的
备选网关重新建立连接。
单包授权
设置是否开启单包授权（SPA）功能。该功能用于ZTNA访问场景。如果ZTNA服务端开
启了SPA并配置了隐藏IP和端口，ZTNA客户端也需要开启SPA。用户通过ZTNA客户端
登录时，需要先通过SPA敲门认证后才能建立到ZTNA服务的连接。当ZTNA服务端关闭
SPA或开启了SPA但未配置隐藏IP和端口时，无论客户端是否开启SPA，服务端都不会对
客户端进行SPA认证。
l 开：开启时，客户端需要手动指定SPA的敲门端口。
l 关：客户端登录时不会敲门。
l 自动：无论ZTNA服务端是否开启SPA功能，客户端均认为服务器已开启SPA功
能，并通过默认端口敲门。该选项为默认设置。
通信稳定性优化
设置是否使用TCP协议传输数据，默认为关闭。启用该功能时需要服务端配置TCP端
口。
验证服务器证书
点击“启用”按钮，在建立连接时，对服务器进行证书验证。添加可信证书，请参考通
用设置。
3. 连接信息填写完成后，点击“确定”按钮，客户端将填写的连接信息保存为一条登录信息条目。如需要，可重复
以上步骤添加多个登录信息条目。

<!-- 来源页 1926 -->
4. 点击登录信息条目中的“连接”按钮，客户端弹出连接页面，其将呈现服务端配置的认证方式。选择相应的认证
方式并登录，客户端将建立到服务端的连接。
认证方式包含用户名/密码、用户名/密码+数字证书、仅数字证书和第三方应用登录。
如果服务端“接入用户”选择了OAuth2服务器、企业微信服务器或钉钉服务器时，可通过第三方应用登录方式
进行认证。当客户端选择OAuth2认证、企业微信认证或钉钉认证时，将跳转至浏览器进行认证。点击所选认证
方式对应的图标，进入相应的授权页面，授权和认证完成后浏览器返回认证结果，同时客户端返回登录状态。
选项
说明
用户名
当认证类型包含“用户名/密码”时，需填写客户端用户名和密码。
密码
填写与用户名相对应的密码。如果服务端采用本地认证服务器进行用户认证，此处的用
户名和密码为设备中配置的用户及其相应的密码。
数字证书
当认证类型设置为“用户名/密码+数字证书”或“仅数字证书”时，点击此项进入
“选择证书”对话框选择认证所用的证书。
选择证书
当加密协议为TLS/SSL时，“选择数字证书”对话框各选项说明如下：
l 默认系统证书：选中该单选按钮时，Hillstone设备采用Hillstone UKey证书作为
默认系统证书。该选项为系统默认选项。
l USB Key证书：选中该单选按钮，并在“证书列表”中选择USB Key证书，需提
前将USB Key插入PC的USB接口。用户可以通过USB Key批量部署工具将第三方
USB Key证书设置为默认系统证书。关于USB Key批量部署工具的详细信息，请
参阅USB Key批量部署。

<!-- 来源页 1927 -->
选项
说明
l 软证书：选中该单选按钮，并在“证书列表”中选择软证书，需提前将软证书导
入系统。
l 证书列表：显示系统中已有的证书。点击“刷新”图标刷新证书列表。
选择证书
当加密协议为国密SSL时，“选择数字证书”对话框各选项说明如下：
l 设备名称：在下拉菜单中选择当前USB Token设备名称。需提前将USB Token插
入PC的USB接口。
l 应用名称：应用是包含容器、设备认证密钥以及文件的一种结构。在下拉菜单选
择指定的应用名称。
l 容器名称：容器是USB Token设备中用于保存密钥所划分的唯一性存储空间。用
来存储加密密钥对、与加密密钥对所对应的加密证书、签名密钥对、与签名密钥
对所对应的签名证书。在下拉菜单选择指定的容器名称。
l 签名证书：显示指定容器内的SM2签名证书名称。
l 加密证书：显示指定容器内的SM2加密证书名称。
PIN码
当认证类型设置为“用户名/密码+数字证书”或“仅数字证书”时，需填写数字证书对
应的PIN码。
记住PIN码
勾选后，客户端在下一次建立连接时，无需用户再次输入PIN码。
记住密码
开启后，客户端在下一次建立连接时，无需用户再次输入密码。
记住认证类型
开启后，下次连接时直接使用上一次的认证方式连接服务端。默认是开启状态。如果关
闭“记住认证类型”功能，下次连接时需要重新选择认证方式进行连接。
注意：当服务端上的认证类型发生改变时，如果记住的认证类型不包含在改变后的认证
类型中，下次连接时会提示认证类型和服务端不一致，需要重新选择认证方式进行连
接。

<!-- 来源页 1928 -->
5. 如果服务端开启短信口令认证功能，客户端会弹出短信口令认证对话框（如下图所示）。输入短信认证码，并点
击“验证”按钮。如果用户在1分钟内没收到认证码短信，可以重新申请认证码。
6. 如果服务端开启令牌口令认证功能，客户端将转到令牌口令认证对话框，用户需通过令牌口令认证。
7. 如果服务端开启邮件口令认证功能，客户端会弹出邮件口令认证对话框，用户需通过邮件口令认证。
l 通过用户名和密码验证后，用户最多可以输入3次认证码。如果连续3次输入错误，服务端将自动断开连
接。
l 用户最多能重新申请3次认证码，重新申请认证码的时间间隔为1分钟。重新申请认证码后，旧认证码信息
失效，用户必须输入最新认证码才能认证成功。
8. 连接成功后，在系统任务栏的通知区域将会显示绿色的图标。
提示:
l
如果服务端配置了密码控制功能及允许修改密码功能，系统将按照密码控制功能的配置进行提
示用户，例如：在密码过期前提醒用户及时修改密码，密码过期后提示用户进行密码修改，并
校验新密码不能与历史密码重复等。配置密码控制功能，请参考配置本地AAA服务器。
l
浏览器显示OAuth2认证成功后，SSL VPN/ZTNA客户端不一定登录成功，可能的原因有主机
检测不通过等。请在客户端查看失败原因进行处理。
l
如果服务端开启二次认证，且支持OAuth2认证，那么客户端使用第三方应用登录方式进行连
接时将不会进行二次认证。
l
选择第三方应用登录时，弹出浏览器后如果不进行认证操作，10分钟后客户端会提示认证超
时。

<!-- 来源页 1929 -->
l
如果需要回退客户端版本，需要先卸载当前版本再安装旧版本，不能直接覆盖安装，否则会出
现连接配置信息错误，无法连接成功。
l
客户端自动重连时需要重新进行OAuth2认证。
l
客户端连接支持OAuth2认证的服务端（R10F4及以后F版本，R11及以后版本）时，客户端页
面返回服务端配置的认证方式。例如服务端配置用户名/密码和OAuth2认证，则客户端的<连
接>页面，显示用户名/密码和第三方应用登录方式。
l
客户端连接不支持OAuth2认证的服务端（R10F4之前版本）时，客户端的连接页面默认显示3
种认证方式，需要选择服务端配置的认证方式才能连接成功。例如服务端配置了仅证书的认证
方式，则在客户端页面需要选择数字证书的方式才能连接成功。如下图所示：
编辑和删除登录信息条目
当连接为断开状态时，将光标指向登录信息条目，点击
图标编辑登录信息条目；点击
图标删除登录
信息条目。

<!-- 来源页 1930 -->
查看连接和统计信息
在客户端页面，点击“统计”页签，查看连接和统计信息。
地址信息:显示IP地址信息。
服务器
显示客户端连接到的服务端的IP地址。
客户端
显示当前客户端的IP地址。
加密信息:显示服务端使用的加密与验证算法以及SSL版本信息。
密码套件
依次显示服务端使用的加密算法和验证算法。
密码版本
显示服务端使用的SSL协议版本。
连接状态:
状态
显示客户端与服务端的当前连接状态。
IP压缩
算法
显示客户端所使用的数据压缩算法。
隧道包统计
发送
显示通过隧道发送的数据包数。
接收
显示通过隧道接收的数据包数。
隧道字节统计
发送
显示通过隧道发送的数据字节数。
接收
显示通过隧道接收的数据字节数。
连接时长
持续
显示客户端与服务端保持连接的时间。
压缩率
发送
显示通过压缩算法处理后的发送数据长度百分比。
接收
显示通过压缩算法处理后的接收数据长度百分比。

<!-- 来源页 1931 -->
查看接口和路由信息
在客户端页面，点击“接口”页签，查看接口信息。在客户端页面，点击“路由> IPv4路由”或“路由>
IPv6路由”页签，查看IPv4或IPv6路由信息。
选项
说明
接口名称
显示客户端传送加密信息的接口的名称。
接口类型
显示客户端传送加密信息的接口的类型。
接口状态
显示客户端传送加密信息的接口的状态。
IP地址类型
显示客户端传送加密信息的接口IP地址的类型。
当客户端用户接入IPv4或双栈类型的服务端时，会显示以下信息：
IPv4网络地址
显示客户端传送加密信息的接口的IPv4地址（由服务端自动分配）。
IPv4子网掩码
显示客户端传送加密信息的接口的IPv4网络掩码。
IPv4 DNS服务器地址
显示服务端下发给客户端使用的DNS服务器地址，该地址为IPv4类型。
IPv4 WINS地址
显示服务端下发给客户端使用的WINS服务器地址，该地址为IPv4类型。
当客户端用户接入IPv6或双栈类型的服务端时，会显示以下信息：
IPv6网络地址
显示客户端传送加密信息的接口的IPv6地址（由服务端自动分配）。
IPv6前缀长度
显示客户端传送加密信息的接口的IPv6前缀长度。
IPv6 DNS服务器地址
显示服务端下发给客户端使用的DNS服务器地址，该地址为IPv6类型。
查看日志
在客户端页面，点击“日志”页签，查看日志信息。点击“导出”，导出日志信息到本地文件。点击“清
除”，清除客户端日志。

<!-- 来源页 1932 -->
点击
，选择“日志级别”，设置需要显示的日志的级别。
配置检查更新
在客户端页面，点击
，选择“检查更新”，当有可用更新时，在弹出的提示框中，进行如下操作：
l 选择“立即更新”，立即开始下载客户端，下载完成后自动进入客户端安装页面。
l 选择“下次启动时更新”，将安装包下载到本地，在下次启动客户端时进行安装。
l 选择“不再提醒”，下次启动客户端时，将不再出现自动更新提示。
USB Key批量部署
Hillstone设备采用Hillstone UKey证书作为默认系统证书。使用默认系统证书进行认证时，Secure
Connect Windows客户端会自动选择默认系统证书传送至服务端，服务端对收到的数字证书进行认证，整
个认证过程对用户来说是透明的，不需要用户手动进行证书选择。针对用户使用第三方USB Key进行
Secure Connect Windows客户端认证的情况，Hillstone提供USB Key批量部署工具SelectUSBKey。通
过SelectUSBKey，用户能够将第三方USB Key证书设置为默认系统证书，从而简化认证时的操作过程。
通过SelectUSBKey将第三方USB Key证书设置为默认系统证书，用户首先要将USB Key的CSP Name信息
以注册表文件的格式导出，然后将文件中的信息添加进客户端PC注册表。
请按照以下步骤导出USB Key的CSP Name信息：
1. 在PC中安装第三方USB Key驱动程序。
2. 插入第三方USB Key。

<!-- 来源页 1933 -->
3. 双击SelectUSBKey.exe，系统弹出<Select Default Certificate>对话框。如下图所示：
Export：将USB Key的CSP Name以注册表文件（.reg）格式导出到本地目录。
Update：刷新证书列表。
Close：关闭对话框。
4. 在<Certificate List>中选中所需证书，点击『Export』按钮，将USB Key的CSP Name信息以注册表文件
（.reg）格式导出到本地目录。如下图所示:
导出USB Key的CSP Name信息后，用户将信息文件存放在客户端PC目录中并双击该文件，将文件中的信
息添加进客户端PC注册表。添加完成后，当用户通过该USB Key进行SSL VPN客户端认证时，客户端会自
动选择USB Key中的数字证书传送至服务端，不需要用户手动选择证书。

<!-- 来源页 1934 -->
客户端菜单
右键单击系统任务栏通知区域的Secure Connect Windows客户端的绿色图标，系统弹出客户端菜单，菜
单项的作用如下：
l 修改密码：弹出<修改密码>对话框输入密码信息。
l 重定向URL：服务端配置重定向URL时，点击此菜单可以快速跳转至该地址。
l 资源列表：当用户访问SCVPN服务时，连接成功后点击此菜单项将弹出浏览器页面，用户可以点击页面里的资源
条目访问内网资源。
l 应用资源列表：当用户使用Secure Connect Windows客户端访问ZTNA服务时，连接成功后可以看到此菜单
项。用户登录成功后弹出的Portal页面关闭后，可以点击该菜单打开最新的Portal页面查看应用资源的访问权
限。Portal页面上展示用户有权限和无权限访问的应用资源。对于无权限访问的应用资源，用户在调整终端配置
后，可以获得访问权限。禁止访问的应用资源不在Portal页面上展示，如果用户被禁止访问任何应用资源，
Portal页面将展示“无可用的Web服务资源”。
l 显示主页面：当客户端界面处于最小化状态时，点击此项可以显示客户端主页面。
l 退出：退出Secure Connect Windows客户端程序。
通用设置
在客户端页面，点击“设置”。
l 开机自动运行：开启后，客户端将在PC系统启动时自动启动。
l 自动重连：开启后，客户端将在连接中断时进行自动重连。
l 自动登录：开启后，客户端将在启动时使用上一次登录成功的连接信息进行自动登录。
l 连接最小化：开启后，客户端将在连接成功后自动缩小到托盘。
l 导入服务端可信证书：在建立连接时开启“验证服务器证书”功能后，点击
按钮，在<可信证书>页面点击

<!-- 来源页 1935 -->
“导入”按钮，导入对服务器进行认证的证书。点击“删除”按钮，删除列表中的可信证书。
l 状态通知：当客户端连接成功或失败时，出现相应的状态弹窗通知。
客户端的卸载
从PC上卸载Secure Connect Windows客户端，从“开始菜单”点击“所有程序> Hillstone Secure
Connect > Hillstone Secure Connect”，右键点击“Hillstone Secure Connect”，在菜单中选择
“卸载”。
Hillstone Secure Connect客户端for Android
型号说明：v5.2.0及以上版本的Secure Connect Android客户端支持接入双栈类型的SSL
VPN/ZTNA实例。
支持Android系统的SSL VPN/ZTNA客户端工具为Hillstone Secure Connect，可在Android
8.x/Android 9.x/Android 10.x/Android 11.x/Android 12.x/Android 13.x及鸿蒙2.0系统环境中运
行。Hillstone Secure Connect主要作用包括：
l 从所在Android系统中获得接口信息；
l 显示与服务端连接状态、数据流统计以及接口和路由信息；
l 显示应用程序日志信息。
l 收集和上报终端状态信息。
下载与安装
下载和安装Secure Connect Android客户端，参照如下步骤：
1. 访问Hillstone官网客户端下载页面https://www.hillstonenet.com.cn/support-and-training/hillstonesecure-connect/；或者访问服务端的客户端下载地址https://IP-Address:Port-Number。其中“IPAddress”和“Port-Number”分别为服务端SSL VPN或ZTNA实例中指定的接口的IP地址和HTTPS端口号。
2. 找到Android客户端二维码，用Android设备扫描。
3. 通过二维码扫描结果打开下载链接并下载安装文件Hillstone-Secure-Connect-Versione_Number.apk到手
机。
4. 下载完成后，在手机存储器中找到该安装文件。
5. 点击该安装文件。弹出程序安装界面。

<!-- 来源页 1936 -->
6. 阅读权限需求。
7. 点击“安装”按钮。
安装成功后会在Android系统中出现程序图标，如下图所示：
启动与连接
客户端安装成功后，按照以下步骤启动和登录客户端：
1. 点击Android系统桌面上的Hillstone Secure Connect图标，进入客户端界面。
2. 在“首页”页签，点击“+”，进入“添加连接”页面。

<!-- 来源页 1937 -->
选项
说明
认证方式
选择认证方式，包括“用户名/密码”，“用户名/密码+数字证书”和“数字证
书”。
连接名称
填写连接名称。
服务器地址
填写SSL VPN或ZTNA服务端的服务IP地址。
端口
填写SSL VPN或ZTNA服务端的HTTPS端口号。
用户名
当认证类型包含“用户名/密码”时，需填写客户端用户名和密码。
密码
填写与用户名相对应的密码。如果服务端采用本地认证服务器进行用户认证，此
处的用户名和密码为设备中配置的用户及其相应的密码。
PIN码
当认证类型设置为“用户名/密码+数字证书”或“数字证书”时，需填写数字证
书对应的PIN码。
密码标准
选择使用哪种加密协议建立连接。
l
TLS/SSL：表示使用TLS/SSL协议。
l
国密SSL：表示使用国密SSL协议。
选择证书
当认证类型设置为“用户名/密码+数字证书”或“数字证书”时，点击此项选择
TLS/SSL证书或国密证书，需提前将证书导入Android系统。客户端会将证书传
送到服务端进行认证。
网关探测
设置是否开启网关探测。该功能用于ZTNA访问场景。当ZTNA服务端配置了备选
网关时，ZTNA客户端可以开启网关探测功能。用户登录时，ZTNA客户端会先获
取备选网关列表，探测每个备选网关的链路质量，并选择链路质量最优的网关建
立ZTNA连接。建立连接后，客户端会每隔30分钟更新一次备选网关的链路质
量。如果发生连接中断或用户登录失败，客户端会自动切换到链路质量最优的备
选网关重新建立连接。
最优网关
开启网关探测后，ZTNA客户端会在用户登录时获取到备选网关列表，此时用户可
以手动选择最优网关。最优网关默认不指定。如果指定了最优网关，用户再次登
录时，ZTNA客户端将优先向最优网关地址发起连接请求，若连接失败，则自动切
换到链路质量最优的备选网关重新建立连接。
单包授权
设置是否开启单包授权（SPA）功能。该功能用于ZTNA访问场景。如果ZTNA服
务端开启了SPA并配置了隐藏IP和端口，ZTNA客户端也需要开启SPA。用户通过
ZTNA客户端登录时，需要先通过SPA敲门认证后才能建立到ZTNA服务的连接。
当ZTNA服务端关闭SPA或开启了SPA但未配置隐藏IP和端口时，无论客户端是否
开启SPA，服务端都不会对客户端进行SPA认证。
l
开启：开启时，客户端需要手动指定SPA的敲门端口。默认为开启。
l
关闭：客户端登录时不会敲门。
l
AUTO：无论ZTNA服务端是否开启SPA功能，客户端均认为服务器已开启

<!-- 来源页 1938 -->
选项
说明
SPA功能，并通过默认端口敲门。该选项为默认设置。
通信稳定性优化
设置是否使用TCP协议传输数据，默认为关闭。启用该功能时需要服务端配置
TCP端口。
3. 连接信息填写完成后，点击“确定”按钮，系统将添加一条登录信息条目。如需要，可重复以上步骤添加多个登
录信息条目。
4. 返回客户端主界面，选择刚刚添加的登录信息条目，打开“连接状态”开关。
5. 如果服务端开启短信口令、令牌口令或邮件口令认证功能，需输入相应的认证码完成认证。
6. 连接成功后，此时就可以实现客户端与服务端之间的加密通信。
编辑和删除登录信息条目
点击需要编辑的登录信息条目，点击
图标，可以编辑登录信息条目。
按住需要删除的登录信息条目，向右拖拽，可以删除登录信息条目。

<!-- 来源页 1939 -->
查看连接信息
点击客户端界面下方的“连接信息”页签，可查看连接统计、接口和路由信息。
连接统计信息：

<!-- 来源页 1940 -->
选项
说明
服务器地址
显示当前连接的服务端IP地址或域名。
端口
显示当前连接的服务器端口号。
用户名
显示当前连接的登录用户名。
连接时长
显示客户端与服务端保持连接的时间。
接收字节
显示通过加密隧道接收的数据字节数。
发送字节
显示通过加密隧道发送的数据字节数。
接收数据包
显示通过加密隧道接收的数据包个数。
发送数据包
显示通过加密隧道发送的数据包个数。
接收压缩率
显示通过压缩算法处理后的接收数据长度百分比。
发送压缩率
显示通过压缩算法处理后的发送数据长度百分比。
接口统计信息：
选项
说明
接口名称
显示客户端传送加密信息的接口的名称。
接口类型
显示客户端传送加密信息的接口的类型。
物理地址
显示客户端传送加密信息的接口的MAC地址。
IP地址类型
显示客户端传送加密信息的接口IP地址的类型。
当客户端用户接入IPv4或双栈类型的服务端时，会显示以下信息：
IPv4 网络地址
显示客户端传送加密信息的接口的IPv4地址（由服务端自动分配）。
IPv4 子网掩码
显示客户端传送加密信息的接口的IPv4网络掩码。
IPv4 DNS地址
显示服务端下发给客户端使用的DNS服务器地址，该地址为IPv4类型。
当客户端用户接入IPv6或双栈类型的服务端时，会显示以下信息：
IPv6 网络地址
显示客户端传送加密信息的接口的IPv6地址（由服务端自动分配）。
IPv6 前缀长度
显示客户端传送加密信息的接口的IPv6前缀长度。
IPv6 DNS地址
显示服务端下发给客户端使用的DNS服务器地址，该地址为IPv6类型。
Hillstone Secure Connect客户端for iOS
型号说明：v5.2.0及以上版本的Secure Connect iOS客户端支持接入双栈类型的SSL
VPN/ZTNA实例。

<!-- 来源页 1941 -->
支持iOS系统的SSL VPN/ZTNA客户端工具为Hillstone Secure Client(beta)，可在iOS 12.x/iOS
13.x/iOS 14.x/iOS 15.x/iOS 16.x系统环境中运行。iOS客户端的主要作用包括：
l 简化与服务端建立隧道的过程；
l 显示与服务端连接状态；
l 显示日志信息。
l 采集和上报终端状态信息。
下载与安装
可以通过以下方法下载Secure Connect iOS客户端：
l 从App Store搜索应用Hillstone Secure Connect下载和安装。
l 访问Hillstone官网客户端下载页面https://www.hillstonenet.com.cn/support-and-training/hillstonesecure-connect/，找到iOS客户端二维码，用iOS设备扫描二维码后，跳转到App Store进行下载和安装。
l 在浏览器的地址栏输入以下URL访问服务端下载和安装：https://IP-Address:Port-Number。其中“IPAddress”和“Port-Number”分别为服务端SSL VPN或ZTNA实例中指定的接口的IP地址和HTTPS端口号。
启动与连接
客户端安装成功后，如果是首次登录，需要按照以下步骤启动和登录客户端：

<!-- 来源页 1942 -->
1. 点击iOS系统桌面上的HSAccess图标，进入客户端界面。
2. 点击“+”，进入“添加连接”页面。
选项
说明
连接名称
填写连接名称。
服务器地址
填写SSL VPN或ZTNA服务端的服务IP地址。
端口
填写SSL VPN或ZTNA服务端的HTTPS端口号。
用户名
填写客户端用户名。
密码
填写与用户名相对应的密码。如果服务端采用本地认证服务器进行用户认证，此
处的用户名和密码为设备中配置的用户及其相应的密码。
密码标准
选择加密连接的密码标准。
l
TLS/SSL：表示使用TLS加密。
l
国密SSL：表示使用国密SSL加密。
网关探测
设置是否开启网关探测。该功能用于ZTNA访问场景。当ZTNA服务端配置了备选
网关时，ZTNA客户端可以开启网关探测功能。用户登录时，ZTNA客户端会先获
取备选网关列表，探测每个备选网关的链路质量，并选择链路质量最优的网关建
立ZTNA连接。建立连接后，客户端会每隔30分钟更新一次备选网关的链路质
量。如果发生连接中断或用户登录失败，客户端会自动切换到链路质量最优的备

<!-- 来源页 1943 -->
选项
说明
选网关重新建立连接。
最优网关
开启网关探测后，ZTNA客户端会在用户登录时获取到备选网关列表，此时用户可
以手动选择最优网关。最优网关默认不指定。如果指定了最优网关，用户再次登
录时，ZTNA客户端将优先向最优网关地址发起连接请求，若连接失败，则自动切
换到链路质量最优的备选网关重新建立连接。
单包授权
设置是否开启单包授权（SPA）功能。该功能用于ZTNA访问场景。如果ZTNA服
务端开启了SPA并配置了隐藏IP和端口，ZTNA客户端也需要开启SPA。用户通过
ZTNA客户端登录时，需要先通过SPA敲门认证后才能建立到ZTNA服务的连接。
当ZTNA服务端关闭SPA或开启了SPA但未配置隐藏IP和端口时，无论客户端是否
开启SPA，服务端都不会对客户端进行SPA认证。
l
开启：开启时，客户端需要手动指定SPA的敲门端口。默认为开启。
l
关闭：客户端登录时不会敲门。
l
AUTO：无论ZTNA服务端是否开启SPA功能，客户端均认为服务器已开启
SPA功能，并通过默认端口敲门。该选项为默认设置。
通信稳定性优化
设置是否使用TCP协议传输数据，默认为关闭。启用该功能时需要服务端配置
TCP端口。
3. 连接信息填写完成后，点击“确定”按钮，系统将添加一条登录信息条目。如需要，可重复以上步骤添加多个登
录信息条目。
4. 返回客户端主界面，选择刚刚添加的登录信息条目，打开“连接状态”开关。
5. 如果服务端开启短信口令、令牌口令或邮件认证功能，需输入相应的认证码。
6. 登录成功后，客户端与服务端成功建立连接。
7. 在<允许安装VPN配置文件>对话框中，点击“允许”按钮。
8. 在<输入密码>页面中，输入iOS锁屏密码。密码输入正确后，iOS开始下发VPN配置文件。
9. 下发完成后，打开iOS设备的设置功能，点击“通用>VPN”。在<选择配置>列表中，选中需要连接的VPN名称，
即在VPN配置中设置的连接名称。
10. 打开VPN开关。iOS设备进行VPN连接。
11. 连接成功后，就可以实现客户端与服务端之间的加密通信。
注意: 如果不是首次登录，将不会进行VPN配置文件的安装。只需要登录客户端与服务端进行连
接，并在iOS系统中完成VPN的连接，即可对客户端与服务端之间传输的数据进行加密。

<!-- 来源页 1944 -->
编辑和删除登录信息条目
点击需要编辑的登录信息条目，点击
图标，可以编辑登录信息条目。
按住需要删除的登录信息条目，向右拖拽，可以删除登录信息条目。

<!-- 来源页 1945 -->
查看连接信息
点击客户端界面下方的“连接信息”页签，可查看连接统计、接口和路由信息。
连接统计信息：

<!-- 来源页 1946 -->
选项
说明
服务器地址
显示当前连接的服务端IP地址或域名。
端口
显示当前连接的服务器端口号。
用户名
显示当前连接的登录用户名。
连接时长
显示客户端与服务端保持连接的时间。
接收字节
显示通过加密隧道接收的数据字节数。
发送字节
显示通过加密隧道发送的数据字节数。
接收数据包
显示通过加密隧道接收的数据包个数。
发送数据包
显示通过加密隧道发送的数据包个数。
接收压缩率
显示通过压缩算法处理后的接收数据长度百分比。
发送压缩率
显示通过压缩算法处理后的发送数据长度百分比。
接口统计信息：
选项
说明
接口名称
显示客户端传送加密信息的接口的名称。
接口类型
显示客户端传送加密信息的接口的类型。
物理地址
显示客户端传送加密信息的接口的MAC地址。
IP地址类型
显示客户端传送加密信息的接口IP地址的类型。
当客户端用户接入IPv4或双栈类型的服务端时，会显示以下信息：
IPv4 网络地址
显示客户端传送加密信息的接口的IPv4地址（由服务端自动分配）。
IPv4 子网掩码
显示客户端传送加密信息的接口的IPv4网络掩码。
IPv4 DNS地址
显示服务端下发给客户端使用的DNS服务器地址，该地址为IPv4类型。
当客户端用户接入IPv6或双栈类型的服务端时，会显示以下信息：
IPv6 网络地址
显示客户端传送加密信息的接口的IPv6地址（由服务端自动分配）。
IPv6 前缀长度
显示客户端传送加密信息的接口的IPv6前缀长度。
IPv6 DNS地址
显示服务端下发给客户端使用的DNS服务器地址，该地址为IPv6类型。
Hillstone Secure Connect客户端for macOS
型号说明：v5.4.0及以上版本的Secure Connect macOS客户端支持接入双栈类型的SSL
VPN/ZTNA实例。

<!-- 来源页 1947 -->
支持macOS系统的SSL VPN/ZTNA客户端工具为Hillstone Secure Connect，建议在macOS 10.13、
macOS 10.14、macOS 10.15、macOS 11、macOS 12、macOS 13系统环境中运行。
通过客户端与服务端的连接，即可实现数据的加密通信。客户端的主要作用包括：
l 与服务端建立安全连接；
l 显示与服务端的连接状态、数据流统计数据以及路由信息；
l 显示应用程序日志信息；
l 采集和上报终端状态信息。
本节主要介绍Secure Connect macOS客户端的下载、安装和启动等。服务端对客户端支持以下四种认证
方式：
l 用户名/密码
l 用户名/密码+ 数字证书
l 只用数字证书
l 第三方应用登录（OAuth2认证、企业微信认证和钉钉认证）
下载与安装
下载和安装Secure Connect macOS客户端，参照如下步骤：
1. 访问Hillstone官网客户端下载页面https://www.hillstonenet.com.cn/support-and-training/hillstonesecure-connect/；或者访问服务端的客户端下载地址https://IP-Address:Port-Number。其中“IPAddress”和“Port-Number”分别为服务端SSL VPN或ZTNA实例中指定的接口的IP地址和HTTPS端口号。
2. 下载完成后，双击安装程序，在弹出窗口中将Secure Connect macOS客户端拖拽到Applications中即可完成安
装。
|

<!-- 来源页 1948 -->
注意: 需要符合如下条件才可打开客户端安装程序：
l
需要管理员权限才可以打开客户端安装程序。
l
在系统偏好设置的“安全性与隐私”中，将“允许从以下位置下载的应用”设置为“任何来
源”，才可以打开客户端安装程序。
启动与连接
客户端安装成功后，按照以下步骤启动和登录客户端：
1. 在macOS Launchpad中单击Hillstone Secure Connect图标，启动客户端。
2. 点击“添加连接”按钮，系统弹出下图所示对话框。
输入连接信息。
选项
说明
TLS/SSL
选择该页签，表示使用TLS/SSL加密协议。
国密SSL
选择该页签，表示使用国密SSL协议。
连接名称
填写连接名称。
服务器
填写SSL VPN或ZTNA服务端的服务IP地址。
端口
填写SSL VPN或ZTNA服务端的HTTPS端口号。
高级配置：默认是折叠状态。点击
按钮，配置如下功能。

<!-- 来源页 1949 -->
选项
说明
网关探测
设置是否开启网关探测功能。该功能用于ZTNA访问场景。当ZTNA服务端配置了备选网
关时，ZTNA客户端可以开启网关探测功能。用户登录时，ZTNA客户端会先获取备选网
关列表，探测每个备选网关的链路质量，并选择链路质量最优的网关建立ZTNA连接。建
立连接后，客户端会每隔30分钟更新一次备选网关的链路质量。如果发生连接中断或用
户登录失败，客户端会自动切换到链路质量最优的备选网关重新建立连接。默认为开
启。
最优网关
开启网关探测后，ZTNA客户端会在用户登录时获取到备选网关列表，此时用户可以手动
选择最优网关。最优网关默认不指定。如果指定了最优网关，用户再次登录时，ZTNA客
户端将优先向最优网关地址发起连接请求，若连接失败，则自动切换到链路质量最优的
备选网关重新建立连接。
单包授权
设置是否开启单包授权（SPA）功能。该功能用于ZTNA访问场景。如果ZTNA服务端开
启了SPA并配置了隐藏IP和端口，ZTNA客户端也需要开启SPA。用户通过ZTNA客户端
登录时，需要先通过SPA敲门认证后才能建立到ZTNA服务的连接。当ZTNA服务端关闭
SPA或开启了SPA但未配置隐藏IP和端口时，无论客户端是否开启SPA，服务端都不会对
客户端进行SPA认证。
l 开：开启时，客户端需要手动指定SPA的敲门端口。
l 关：客户端登录时不会敲门。
l 自动：无论ZTNA服务端是否开启SPA功能，客户端均认为服务器已开启SPA功
能，并通过默认端口敲门。该选项为默认设置。
通信稳定性优化
设置是否使用TCP协议传输数据，默认为关闭。启用该功能时需要服务端配置TCP端
口。
验证服务器证书
点击“启用”按钮，在建立连接时，对服务器进行证书验证。添加可信证书，请参考通
用设置。
3. 连接信息填写完成后，点击“确定”按钮，客户端将填写的连接信息保存为一条登录信息条目。如需要，可重复
以上步骤添加多个登录信息条目。
4. 点击登录信息条目中的“连接”按钮，客户端弹出连接页面，其将呈现服务端配置的认证方式。选择相应的认证
方式并登录，客户端将建立到服务端的连接。
认证方式包含用户名/密码、用户名/密码+数字证书、仅数字证书和第三方应用登录。
如果服务端“接入用户”选择了OAuth2服务器、企业微信服务器或钉钉服务器时，可通过第三方应用登录方式
进行认证。当客户端选择OAuth2认证、企业微信认证或钉钉认证时，将跳转至浏览器进行认证。点击所选认证
方式对应的图标，进入相应的授权页面，授权和认证完成后浏览器返回认证结果，同时客户端返回登录状态。

<!-- 来源页 1950 -->
选项
说明
用户名
当认证类型包含“用户名/密码”时，需填写客户端用户名和密码。
密码
填写与用户名相对应的密码。如果服务端采用本地认证服务器进行用户认证，此处的用
户名和密码为设备中配置的用户及其相应的密码。
选择证书
点击
按钮，在弹出的页面中点击证书名称就可以选中需要的证书。如无证书，点击
页面下方的“导入”按钮，可以导入指定TLS/SSL或国密SSL协议的证书。也可以在选择
证书前，先在客户端管理证书页面导入证书，关于如何导入证书，请参阅通用设置。
记住密码
开启后，客户端在下一次建立连接时，无需用户再次输入密码。
记住认证类型
开启后，下次连接时直接使用上一次的认证方式连接服务端。默认是开启状态。如果关
闭“记住认证类型”功能，下次连接时需要重新选择认证方式进行连接。
注意：当服务端上的认证类型发生改变时，如果记住的认证类型不包含在改变后的认证
类型中，下次连接时会提示认证类型和服务端不一致，需要重新选择认证方式进行连
接。
5. 如果服务端开启短信口令、令牌口令或邮件口令认证功能，需输入相应的认证码完成二次认证。
6. 连接成功后，就可以实现客户端与服务端之间的加密通信。
提示:
l
如果服务端配置了密码控制功能及允许修改密码功能，系统将按照密码控制功能的配置进行提
示用户，例如：在密码过期前提醒用户及时修改密码，密码过期后提示用户进行密码修改，并
校验新密码不能与历史密码重复等。配置密码控制功能，请参考配置本地AAA服务器。

<!-- 来源页 1951 -->
l
浏览器显示OAuth2认证成功后，SSL VPN/ZTNA客户端不一定登录成功，可能的原因有主机
检测不通过等。请在客户端查看失败原因进行处理。
l
如果服务端开启二次认证，且支持OAuth2认证，那么客户端使用第三方应用登录方式进行连
接时将不会进行二次认证。
l
选择第三方应用登录时，弹出浏览器后如果不进行认证操作，10分钟后客户端会提示认证超
时。
l
如果需要回退客户端版本，需要先卸载当前版本再安装旧版本，不能直接覆盖安装，否则会出
现连接配置信息错误，无法连接成功。
l
客户端自动重连时需要重新进行OAuth2认证。
l
客户端连接支持OAuth2认证的服务端（R10F4及以后F版本，R11及以后版本）时，客户端页
面返回服务端配置的认证方式。例如服务端配置用户名/密码和OAuth2认证，则客户端的<连
接>页面，显示用户名/密码和第三方应用登录方式。
l
客户端连接不支持OAuth2认证的服务端（R10F4之前版本）时，客户端的连接页面默认显示3
种认证方式，需要选择服务端配置的认证方式才能连接成功。例如服务端配置了仅证书的认证
方式，则在客户端页面需要选择数字证书的方式才能连接成功。如下图所示：
编辑和删除登录信息条目
当连接为断开状态时，将光标指向登录信息条目，点击
图标编辑登录信息条目；点击
图标删除登录
信息条目。

<!-- 来源页 1952 -->
查看连接和统计信息
在客户端页面，点击“统计”页签，查看连接和统计信息。
地址信息:显示IP地址信息。
服务器
显示客户端连接到的服务端的IP地址。
客户端
显示当前客户端的IP地址。
加密信息:显示服务端使用的加密与验证算法以及SSL版本信息。
密码套件
依次显示服务端使用的加密算法和验证算法。
密码版本
显示服务端使用的SSL协议版本。
连接状态:
状态
显示客户端与服务端的当前连接状态。
IP压缩
算法
显示客户端所使用的数据压缩算法。
隧道包统计
发送
显示通过隧道发送的数据包数。
接收
显示通过隧道接收的数据包数。
隧道字节统计
发送
显示通过隧道发送的数据字节数。
接收
显示通过隧道接收的数据字节数。
连接时长
持续
显示客户端与服务端保持连接的时间。
压缩率
发送
显示通过压缩算法处理后的发送数据长度百分比。
接收
显示通过压缩算法处理后的接收数据长度百分比。

<!-- 来源页 1953 -->
查看接口和路由信息
在客户端页面，点击“接口”页签，查看接口信息。在客户端页面，点击“路由> IPv4路由”或“路由>
IPv6路由”页签，查看IPv4或IPv6路由信息。
选项
说明
接口名称
显示客户端传送加密信息的接口的名称。
接口类型
显示客户端传送加密信息的接口的类型。
接口状态
显示客户端传送加密信息的接口的状态。
IP地址类型
显示客户端传送加密信息的接口IP地址的类型。
当客户端用户接入IPv4或双栈类型的服务端时，会显示以下信息：
IPv4网络地址
显示客户端传送加密信息的接口的IPv4地址（由服务端自动分配）。
IPv4子网掩码
显示客户端传送加密信息的接口的IPv4网络掩码。
IPv4 DNS服务器地址
显示服务端下发给客户端使用的DNS服务器地址，该地址为IPv4类型。
IPv4 WINS地址
显示服务端下发给客户端使用的WINS服务器地址，该地址为IPv4类型。
当客户端用户接入IPv6或双栈类型的服务端时，会显示以下信息：
IPv6网络地址
显示客户端传送加密信息的接口的IPv6地址（由服务端自动分配）。
IPv6前缀长度
显示客户端传送加密信息的接口的IPv6前缀长度。
IPv6 DNS服务器地址
显示服务端下发给客户端使用的DNS服务器地址，该地址为IPv6类型。
查看日志
在客户端页面，点击“日志”页签，查看日志信息。点击“导出日志”，导出日志信息到本地文件。点击
“清除日志”，清除客户端日志。

<!-- 来源页 1954 -->
点击
，选择“日志级别”，设置需要显示的日志的级别。
配置检查更新
在客户端页面，点击
，选择“检查更新”，当有可用更新时，在弹出的提示框中，进行如下操作：
l 选择“立即更新”，立即开始下载客户端，下载完成后自动进入客户端安装页面。
l 选择“下次启动时更新”，将安装包下载到本地，在下次启动客户端时进行安装。
l 选择“不再提醒”，下次启动客户端时，将不再出现自动更新提示。
通用设置
在客户端页面，点击“设置”。
l 自动重连：开启后，客户端将在连接中断时进行自动重连。
l 自动登录：开启后，客户端将在启动时使用上一次登录成功的连接信息进行自动登录。
l 连接最小化：开启后，客户端将在连接成功后自动缩小到托盘。
l 可信服务器证书管理：在建立连接时开启“验证服务器证书”功能后，点击
按钮，在<可信证书>页面点击
“导入”按钮，导入对服务器进行认证的证书。点击“删除”按钮，删除列表中的可信证书。

<!-- 来源页 1955 -->
l 客户端证书管理：点击
按钮，在<客户端证书管理>页面点击“导入”按钮，导入登录认证需要的证书，证
书为PKCS#12格式，可以导入国密、非国密证书。最多可以导入16个证书文件。点击“删除”按钮，删除列表
中的证书。
l 状态通知：当客户端连接成功或失败时，出现相应的状态弹窗通知。
客户端菜单
右键单击系统任务栏通知区域的Secure Connect macOS客户端的绿色图标，系统弹出客户端菜单，菜单
项的作用如下：
l 重定向URL：服务端配置重定向URL时，点击此菜单可以快速跳转至该地址。
l 资源列表：当用户访问SCVPN服务时，连接成功后点击此菜单项将弹出浏览器页面，用户可以点击页面里的资源
条目访问内网资源。
l 应用资源列表：当用户使用Secure Connect macOS客户端访问ZTNA服务时，连接成功后可以看到此菜单项。
用户登录成功后弹出的Portal页面关闭后，可以点击该菜单打开最新的Portal页面查看应用资源的访问权限。
Portal页面上展示用户有权限和无权限访问的应用资源。对于无权限访问的应用资源，用户在调整终端配置后，
可以获得访问权限。禁止访问的应用资源不在Portal页面上展示，如果用户被禁止访问任何应用资源，Portal页
面将展示“无可用的Web服务资源”。
l 显示主页面：当客户端界面处于最小化状态时，点击此项可以显示客户端主页面。
l 退出：退出Secure Connect macOS客户端程序。
卸载客户端
卸载客户端，右击客户端图标，从下拉菜单中选择“移到废纸篓”。
Hillstone Secure Connect客户端for Linux
型号说明：v5.4.0及以上版本的Secure Connect Linux客户端支持接入双栈类型的SSL
VPN/ZTNA实例。
支持Linux系统的SSL VPN/ZTNA客户端工具为Hillstone Secure Connect，建议在以下操作系统中运
行：

<!-- 来源页 1956 -->
l CentOS 7.6/7.7/7.8/7.9/8.0/8.1/8.2/8.3/8.4/8.5
l Ubuntu 18.04/18.10/19.04/19.10/20.04/20.10/21.04
l Ubuntu Kylin 18.04/20.04
通过客户端与服务端的连接，即可实现数据的加密通信。该客户端的主要作用包括：
l 从所在系统获得接口和路由信息。
l 显示与SSL VPN/ZTNA服务端的连接状态、数据流统计数据以及接口和路由信息。
l 显示应用程序日志信息。
l 采集和上报终端状态信息。
本节主要介绍Secure Connect Linux客户端的下载、安装和启动等。服务端对客户端支持以下四种认证方
式：
l 用户名/密码
l 用户名/密码+ 数字证书
l 只用数字证书
l 第三方应用登录（OAuth2认证、企业微信认证和钉钉认证）
下面以CentOS 7.6为例介绍客户端的下载与安装、启动与连接、升级与卸载、客户端GUI和菜单，其他系统
配置方法类似。
下载与安装
下载和安装Secure Connect Linux客户端，按照以下步骤进行操作：
1. 访问Hillstone官网客户端下载页面https://www.hillstonenet.com.cn/support-and-training/hillstonesecure-connect/；或者访问服务端的客户端下载地址https://IP-Address:Port-Number。其中“IPAddress”和“Port-Number”分别为服务端SSL VPN或ZTNA实例中指定的接口的IP地址和HTTPS端口号。

<!-- 来源页 1957 -->
2. 下载完成后，使用鼠标右击图标并选择“属性”，进入属性页面。
3. 在属性页面，点击“权限”标签页，勾选“允许作为程序执行文件”，点击“关闭”。
4. 双击安装程序，并按照设置向导完成安装。
启动与连接
客户端安装成功后，按照以下步骤启动和登录客户端：
1. 双击Linux系统桌面上的客户端图标，系统进入超级用户身份认证页面，输入超级用户密码，并点击“授权”，
进入客户端主界面。

<!-- 来源页 1958 -->
2. 在主界面，点击“添加连接”按钮，系统弹出下图所示对话框。
输入连接信息。
选项
说明
TLS/SSL
选择该页签，表示使用TLS/SSL加密协议。
国密SSL
选择该页签，表示使用国密SSL协议。
连接名称
填写连接名称。
服务器
填写SSL VPN或ZTNA服务端的服务IP地址。
端口
填写SSL VPN或ZTNA服务端的HTTPS端口号。
高级配置：默认是折叠状态。点击
按钮，配置如下功能。
网关探测
设置是否开启网关探测功能。该功能用于ZTNA访问场景。当ZTNA服务端配置了备选网
关时，ZTNA客户端可以开启网关探测功能。用户登录时，ZTNA客户端会先获取备选网
关列表，探测每个备选网关的链路质量，并选择链路质量最优的网关建立ZTNA连接。建
立连接后，客户端会每隔30分钟更新一次备选网关的链路质量。如果发生连接中断或用
户登录失败，客户端会自动切换到链路质量最优的备选网关重新建立连接。默认为开
启。
最优网关
开启网关探测后，ZTNA客户端会在用户登录时获取到备选网关列表，此时用户可以手动
选择最优网关。最优网关默认不指定。如果指定了最优网关，用户再次登录时，ZTNA客
户端将优先向最优网关地址发起连接请求，若连接失败，则自动切换到链路质量最优的
备选网关重新建立连接。
单包授权
设置是否开启单包授权（SPA）功能。该功能用于ZTNA访问场景。如果ZTNA服务端开

<!-- 来源页 1959 -->
选项
说明
启了SPA并配置了隐藏IP和端口，ZTNA客户端也需要开启SPA。用户通过ZTNA客户端
登录时，需要先通过SPA敲门认证后才能建立到ZTNA服务的连接。当ZTNA服务端关闭
SPA或开启了SPA但未配置隐藏IP和端口时，无论客户端是否开启SPA，服务端都不会对
客户端进行SPA认证。
l 开：开启时，客户端需要手动指定SPA的敲门端口。
l 关：客户端登录时不会敲门。
l 自动：无论ZTNA服务端是否开启SPA功能，客户端均认为服务器已开启SPA功
能，并通过默认端口敲门。该选项为默认设置。
通信稳定性优化
设置是否使用TCP协议传输数据，默认为关闭。启用该功能时需要服务端配置TCP端
口。
验证服务器证书
点击“启用”按钮，在建立连接时，对服务器进行证书验证。添加可信证书，请参考通
用设置。
3. 连接信息填写完成后，点击“确定”按钮，客户端将填写的连接信息保存为一条登录信息条目。如需要，可重复
以上步骤添加多个登录信息条目。
4. 点击登录信息条目中的“连接”按钮，客户端弹出连接页面，其将呈现服务端配置的认证方式。选择相应的认证
方式并登录，客户端将建立到服务端的连接。
认证方式包含用户名/密码、用户名/密码+数字证书、仅数字证书和第三方应用登录。
如果服务端“接入用户”选择了OAuth2服务器、企业微信服务器或钉钉服务器时，可通过第三方应用登录方式
进行认证。当客户端选择OAuth2认证、企业微信认证或钉钉认证时，将跳转至浏览器进行认证。点击所选认证
方式对应的图标，进入相应的授权页面，授权和认证完成后浏览器返回认证结果，同时客户端返回登录状态。

<!-- 来源页 1960 -->
选项
说明
用户名
当认证类型包含“用户名/密码”时，需填写客户端用户名和密码。
密码
填写与用户名相对应的密码。如果服务端采用本地认证服务器进行用户认证，此处的用
户名和密码为设备中配置的用户及其相应的密码。
选择证书
点击
按钮，在弹出的页面中点击证书名称就可以选中需要的证书。如无证书，点击
页面下方的“导入”按钮，可以导入指定TLS/SSL或国密SSL协议的证书。也可以在选择
证书前，先在客户端管理证书页面导入证书，关于如何导入证书，请参阅通用设置。
记住密码
开启后，客户端在下一次建立连接时，无需用户再次输入密码。
记住认证类型
开启后，下次连接时直接使用上一次的认证方式连接服务端。默认是开启状态。如果关
闭“记住认证类型”功能，下次连接时需要重新选择认证方式进行连接。
注意：当服务端上的认证类型发生改变时，如果记住的认证类型不包含在改变后的认证
类型中，下次连接时会提示认证类型和服务端不一致，需要重新选择认证方式进行连
接。
5. 如果服务端开启短信口令、令牌口令或邮件口令认证功能，需输入相应的认证码完成二次认证。
6. 连接成功后，即可以实现客户端与服务端之间的加密通信。

<!-- 来源页 1961 -->
提示:
l
如果服务端配置了密码控制功能及允许修改密码功能，系统将按照密码控制功能的配置进行提
示用户，例如：在密码过期前提醒用户及时修改密码，密码过期后提示用户进行密码修改，并
校验新密码不能与历史密码重复等。配置密码控制功能，请参考配置本地AAA服务器。
l
浏览器显示OAuth2认证成功后，SSL VPN/ZTNA客户端不一定登录成功，可能的原因有主机
检测不通过等。请在客户端查看失败原因进行处理。
l
如果服务端开启二次认证，且支持OAuth2认证，那么客户端使用第三方应用登录方式进行连
接时将不会进行二次认证。
l
选择第三方应用登录时，弹出浏览器后如果不进行认证操作，10分钟后客户端会提示认证超
时。
l
如果需要回退客户端版本，需要先卸载当前版本再安装旧版本，不能直接覆盖安装，否则会出
现连接配置信息错误，无法连接成功。
l
客户端自动重连时需要重新进行OAuth2认证。
l
客户端连接支持OAuth2认证的服务端（R10F4及以后F版本，R11及以后版本）时，客户端页
面返回服务端配置的认证方式。例如服务端配置用户名/密码和OAuth2认证，则客户端的<连
接>页面，显示用户名/密码和第三方应用登录方式。
l
客户端连接不支持OAuth2认证的服务端（R10F4之前版本）时，客户端的连接页面默认显示3
种认证方式，需要选择服务端配置的认证方式才能连接成功。例如服务端配置了仅证书的认证
方式，则在客户端页面需要选择数字证书的方式才能连接成功。如下图所示：
编辑和删除登录信息条目
当连接为断开状态时，将光标指向登录信息条目，点击
图标编辑登录信息条目；点击
图标删除登录
信息条目。

<!-- 来源页 1962 -->
查看连接和统计信息
在客户端页面，点击“统计”页签，查看连接和统计信息。
地址信息:显示IP地址信息。
服务器
显示客户端连接到的服务端的IP地址。
客户端
显示当前客户端的IP地址。
加密信息:显示服务端使用的加密与验证算法以及SSL版本信息。
密码套件
依次显示服务端使用的加密算法和验证算法。
密码版本
显示服务端使用的SSL协议版本。
连接状态:
状态
显示客户端与服务端的当前连接状态。
IP压缩
算法
显示客户端所使用的数据压缩算法。
隧道包统计
发送
显示通过隧道发送的数据包数。
接收
显示通过隧道接收的数据包数。
隧道字节统计
发送
显示通过隧道发送的数据字节数。
接收
显示通过隧道接收的数据字节数。
连接时长
持续
显示客户端与服务端保持连接的时间。
压缩率
发送
显示通过压缩算法处理后的发送数据长度百分比。
接收
显示通过压缩算法处理后的接收数据长度百分比。

<!-- 来源页 1963 -->
查看接口和路由信息
在客户端页面，点击“接口”页签，查看接口信息。在客户端页面，点击“路由> IPv4路由”或“路由>
IPv6路由”页签，查看IPv4或IPv6路由信息。
选项
说明
接口名称
显示客户端传送加密信息的接口的名称。
接口类型
显示客户端传送加密信息的接口的类型。
接口状态
显示客户端传送加密信息的接口的状态。
IP地址类型
显示客户端传送加密信息的接口IP地址的类型。
当客户端用户接入IPv4或双栈类型的服务端时，会显示以下信息：
IPv4网络地址
显示客户端传送加密信息的接口的IPv4地址（由服务端自动分配）。
IPv4子网掩码
显示客户端传送加密信息的接口的IPv4网络掩码。
IPv4 DNS服务器地址
显示服务端下发给客户端使用的DNS服务器地址，该地址为IPv4类型。
IPv4 WINS地址
显示服务端下发给客户端使用的WINS服务器地址，该地址为IPv4类型。
当客户端用户接入IPv6或双栈类型的服务端时，会显示以下信息：
IPv6网络地址
显示客户端传送加密信息的接口的IPv6地址（由服务端自动分配）。
IPv6前缀长度
显示客户端传送加密信息的接口的IPv6前缀长度。
IPv6 DNS服务器地址
显示服务端下发给客户端使用的DNS服务器地址，该地址为IPv6类型。
查看日志
在客户端页面，点击“日志”页签，查看日志信息。点击“导出日志”，导出日志信息到本地文件。点击
“清除日志”，清除客户端日志。

<!-- 来源页 1964 -->
点击
，选择“日志级别”，设置需要显示的日志的级别。
配置检查更新
在客户端页面，点击
，选择“检查更新”，当有可用更新时，在弹出的提示框中，进行如下操作：
l 选择“立即更新”，立即开始下载客户端，下载完成后自动进入客户端安装页面。
l 选择“下次启动时更新”，将安装包下载到本地，在下次启动客户端时进行安装。
l 选择“不再提醒”，下次启动客户端时，将不再出现自动更新提示。
通用设置
在客户端页面，点击“设置”。
l 自动重连：开启后，客户端将在连接中断时进行自动重连。
l 自动登录：开启后，客户端将在启动时使用上一次登录成功的连接信息进行自动登录。
l 连接最小化：开启后，客户端将在连接成功后自动缩小到托盘。
l 可信服务器证书管理：在建立连接时开启“验证服务器证书”功能后，点击
按钮，在<可信证书>页面点击
“导入”按钮，导入对服务器进行认证的证书。点击“删除”按钮，删除列表中的可信证书。

<!-- 来源页 1965 -->
l 客户端证书管理：点击
按钮，在<客户端证书管理>页面点击“导入”按钮，导入登录认证需要的证书，证
书为PKCS#12格式，可以导入国密、非国密证书。最多可以导入16个证书文件。点击“删除”按钮，删除列表
中的证书。
l 状态通知：当客户端连接成功或失败时，出现相应的状态弹窗通知。
客户端菜单
右键单击系统任务栏通知区域的Secure Connect Linux客户端的绿色图标，系统弹出客户端菜单，菜单项
的作用如下：
l 修改密码：弹出<修改密码>对话框输入密码信息。
l 重定向URL：服务端配置重定向URL时，点击此菜单可以快速跳转至该地址。
l 资源列表：当用户访问SCVPN服务时，连接成功后点击此菜单项将弹出浏览器页面，用户可以点击页面里的资源
条目访问内网资源。
l 应用资源列表：当用户使用Secure Connect Linux客户端访问ZTNA服务时，连接成功后可以看到此菜单项。用
户登录成功后弹出的Portal页面关闭后，可以点击该菜单打开最新的Portal页面查看应用资源的访问权限。
Portal页面上展示用户有权限和无权限访问的应用资源。对于无权限访问的应用资源，用户在调整终端配置后，
可以获得访问权限。禁止访问的应用资源不在Portal页面上展示，如果用户被禁止访问任何应用资源，Portal页
面将展示“无可用的Web服务资源”。
l 显示主页面：当客户端界面处于最小化状态时，点击此项可以显示客户端主页面。
l 退出：退出Secure Connect Linux客户端程序。
客户端的卸载
从Linux上卸载客户端：
l 若客户端版本低于5.4.0，在目录“/opt/apps/HillstoneSecureConnect”下点击“MaintenanceTool”组
件，根据提示进行卸载。
l 若客户端版本为5.4.0及以上，在目录“/opt/HillstoneSecureConnect”下点击“MaintenanceTool”组件，
根据提示进行卸载。

<!-- 来源页 1966 -->
Hillstone Secure Connect客户端for ChineseOS
型号说明：v5.4.0及以上版本的Secure Connect ChineseOS客户端支持接入双栈类型的SSL
VPN/ZTNA实例。
支持国产操作系统的SSL VPN/ZTNA客户端工具为Hillstone Secure Connect，建议在以下操作系统中运
行：
l 操作系统：统信UOS 20（CPU海思麒麟）、银河麒麟Kylin V10（CPU兆芯）、统信UOS 20（CPU飞腾）、
银河麒麟Kylin V10（CPU海思麒麟）、银河麒麟Kylin V10（CPU龙芯）、统信UOS 20（CPU龙芯）、银河麒
麟Kylin V10（CPU飞腾）、统信UOS 20（CPU兆芯）
通过客户端与服务端的连接，即可实现数据的加密通信。该客户端的主要作用包括：
l 从所在系统获得接口和路由信息。
l 显示与SSL VPN/ZTNA服务端的连接状态、数据流统计数据以及接口和路由信息。
l 显示应用程序日志信息。
l 采集和上报终端状态信息。
本节主要介绍Secure Connect ChineseOS客户端的下载、安装和启动等。服务端对客户端支持以下四种
认证方式：
l 用户名/密码
l 用户名/密码+ 数字证书
l 只用数字证书
l 第三方应用登录（OAuth2认证、企业微信认证和钉钉认证）
下面以UOS 20 为例介绍客户端的下载与安装、启动与连接、升级与卸载、客户端GUI和菜单，其他系统配
置方法类似。
下载与安装
下载和安装Secure Connect ChineseOS客户端，按照以下步骤进行操作：
1. 访问国产操作系统自带的软件应用商店，搜索Hillstone，搜索到Hillstone Secure Connect客户端。

<!-- 来源页 1967 -->
2. 点击“安装”按钮，安装Hillstone Secure Connect客户端。安装完成后显示为“打开”按钮。点击“打开”按
钮可直接启动客户端。
启动与连接
客户端安装成功后，按照以下步骤启动和登录客户端：
1. 在“开始”菜单栏中找到“Hillstone Secure Connect”，点击客户端，进入客户端主界面。也可以右键点击
“Hillstone Secure Connect”，在菜单中选择桌面添加快捷方式或固定到任务栏。

<!-- 来源页 1968 -->
2. 在主界面，点击“添加连接”按钮，系统弹出下图所示对话框。
输入连接信息。
选项
说明
TLS/SSL
选择该页签，表示使用TLS/SSL加密协议。
国密SSL
选择该页签，表示使用国密SSL协议。
连接名称
填写连接名称。
服务器
填写SSL VPN或ZTNA服务端的服务IP地址。
端口
填写SSL VPN或ZTNA服务端的HTTPS端口号。
高级配置：默认是折叠状态。点击
按钮，配置如下功能。
网关探测
设置是否开启网关探测功能。该功能用于ZTNA访问场景。当ZTNA服务端配置了备选网
关时，ZTNA客户端可以开启网关探测功能。用户登录时，ZTNA客户端会先获取备选网
关列表，探测每个备选网关的链路质量，并选择链路质量最优的网关建立ZTNA连接。建
立连接后，客户端会每隔30分钟更新一次备选网关的链路质量。如果发生连接中断或用
户登录失败，客户端会自动切换到链路质量最优的备选网关重新建立连接。默认为开
启。
最优网关
开启网关探测后，ZTNA客户端会在用户登录时获取到备选网关列表，此时用户可以手动
选择最优网关。最优网关默认不指定。如果指定了最优网关，用户再次登录时，ZTNA客
户端将优先向最优网关地址发起连接请求，若连接失败，则自动切换到链路质量最优的
备选网关重新建立连接。
单包授权
设置是否开启单包授权（SPA）功能。该功能用于ZTNA访问场景。如果ZTNA服务端开

<!-- 来源页 1969 -->
选项
说明
启了SPA并配置了隐藏IP和端口，ZTNA客户端也需要开启SPA。用户通过ZTNA客户端
登录时，需要先通过SPA敲门认证后才能建立到ZTNA服务的连接。当ZTNA服务端关闭
SPA或开启了SPA但未配置隐藏IP和端口时，无论客户端是否开启SPA，服务端都不会对
客户端进行SPA认证。
l 开：开启时，客户端需要手动指定SPA的敲门端口。
l 关：客户端登录时不会敲门。
l 自动：无论ZTNA服务端是否开启SPA功能，客户端均认为服务器已开启SPA功
能，并通过默认端口敲门。该选项为默认设置。
通信稳定性优化
设置是否使用TCP协议传输数据，默认为关闭。启用该功能时需要服务端配置TCP端
口。
验证服务器证书
点击“启用”按钮，在建立连接时，对服务器进行证书验证。添加可信证书，请参阅通
用设置。
3. 连接信息填写完成后，点击“确定”按钮，客户端将填写的连接信息保存为一条登录信息条目。如需要，可重复
以上步骤添加多个登录信息条目。
4. 点击登录信息条目中的“连接”按钮，客户端弹出连接页面，其将呈现服务端配置的认证方式。选择相应的认证
方式并登录，客户端将建立到服务端的连接。
认证方式包含用户名/密码、用户名/密码+数字证书、仅数字证书和第三方应用登录。
如果服务端“接入用户”选择了OAuth2服务器、企业微信服务器或钉钉服务器时，可通过第三方应用登录方式
进行认证。当客户端选择OAuth2认证、企业微信认证或钉钉认证时，将跳转至浏览器进行认证。点击所选认证
方式对应的图标，进入相应的授权页面，授权和认证完成后浏览器返回认证结果，同时客户端返回登录状态。

<!-- 来源页 1970 -->
选项
说明
用户名
当认证类型包含“用户名/密码”时，需填写客户端用户名和密码。
密码
填写与用户名相对应的密码。如果服务端采用本地认证服务器进行用户认证，此处的用
户名和密码为设备中配置的用户及其相应的密码。
选择证书
点击
按钮，在弹出的页面中点击证书名称就可以选中需要的证书。如无证书，点击
页面下方的“导入”按钮，可以导入指定TLS/SSL或国密SSL协议的证书。也可以在选择
证书前，先在客户端管理证书页面导入证书，关于如何导入证书，请参阅通用设置。
记住密码
开启后，客户端在下一次建立连接时，无需用户再次输入密码。
记住认证类型
开启后，下次连接时直接使用上一次的认证方式连接服务端。默认是开启状态。如果关
闭“记住认证类型”功能，下次连接时需要重新选择认证方式进行连接。
注意：当服务端上的认证类型发生改变时，如果记住的认证类型不包含在改变后的认证
类型中，下次连接时会提示认证类型和服务端不一致，需要重新选择认证方式进行连
接。
5. 如果服务端开启短信口令、令牌口令或邮件口令认证功能，需输入相应的认证码完成二次认证。
6. 连接成功后，即可以实现客户端与服务端之间的加密通信。
提示:
l
如果服务端配置了密码控制功能及允许修改密码功能，系统将按照密码控制功能的配置进行提
示用户，例如：在密码过期前提醒用户及时修改密码，密码过期后提示用户进行密码修改，并
校验新密码不能与历史密码重复等。配置密码控制功能，请参考配置本地AAA服务器。
l
浏览器显示OAuth2认证成功后，SSL VPN/ZTNA客户端不一定登录成功，可能的原因有主机
检测不通过等。请在客户端查看失败原因进行处理。
l
如果服务端开启二次认证，且支持OAuth2认证，那么客户端使用第三方应用登录方式进行连
接时将不会进行二次认证。
l
选择第三方应用登录时，弹出浏览器后如果不进行认证操作，10分钟后客户端会提示认证超
时。
l
如果需要回退客户端版本，需要先卸载当前版本再安装旧版本，不能直接覆盖安装，否则会出
现连接配置信息错误，无法连接成功。
l
客户端自动重连时需要重新进行OAuth2认证。

<!-- 来源页 1971 -->
l
客户端连接支持OAuth2认证的服务端（R10F4及以后F版本，R11及以后版本）时，客户端页
面返回服务端配置的认证方式。例如服务端配置用户名/密码和OAuth2认证，则客户端的<连
接>页面，显示用户名/密码和第三方应用登录方式。
l
客户端连接不支持OAuth2认证的服务端（R10F4之前版本）时，客户端的连接页面默认显示3
种认证方式，需要选择服务端配置的认证方式才能连接成功。例如服务端配置了仅证书的认证
方式，则在客户端页面需要选择数字证书的方式才能连接成功。如下图所示：
编辑和删除登录信息条目
当连接为断开状态时，将光标指向登录信息条目，点击
图标编辑登录信息条目；点击
图标删除登录
信息条目。
查看连接和统计信息
在客户端页面，点击“统计”页签，查看连接和统计信息。

<!-- 来源页 1972 -->
地址信息:显示IP地址信息。
服务器
显示客户端连接到的服务端的IP地址。
客户端
显示当前客户端的IP地址。
加密信息:显示服务端使用的加密与验证算法以及SSL版本信息。
密码套件
依次显示服务端使用的加密算法和验证算法。
密码版本
显示服务端使用的SSL协议版本。
连接状态:
状态
显示客户端与服务端的当前连接状态。
IP压缩
算法
显示客户端所使用的数据压缩算法。
隧道包统计
发送
显示通过隧道发送的数据包数。
接收
显示通过隧道接收的数据包数。
隧道字节统计
发送
显示通过隧道发送的数据字节数。
接收
显示通过隧道接收的数据字节数。
连接时长
持续
显示客户端与服务端保持连接的时间。
压缩率
发送
显示通过压缩算法处理后的发送数据长度百分比。
接收
显示通过压缩算法处理后的接收数据长度百分比。
查看接口和路由信息
在客户端页面，点击“接口”页签，查看接口信息。在客户端页面，点击“路由> IPv4路由”或“路由>
IPv6路由”页签，查看IPv4或IPv6路由信息。

<!-- 来源页 1973 -->
选项
说明
接口名称
显示客户端传送加密信息的接口的名称。
接口类型
显示客户端传送加密信息的接口的类型。
接口状态
显示客户端传送加密信息的接口的状态。
IP地址类型
显示客户端传送加密信息的接口IP地址的类型。
当客户端用户接入IPv4或双栈类型的服务端时，会显示以下信息：
IPv4网络地址
显示客户端传送加密信息的接口的IPv4地址（由服务端自动分配）。
IPv4子网掩码
显示客户端传送加密信息的接口的IPv4网络掩码。
IPv4 DNS服务器地址
显示服务端下发给客户端使用的DNS服务器地址，该地址为IPv4类型。
IPv4 WINS地址
显示服务端下发给客户端使用的WINS服务器地址，该地址为IPv4类型。
当客户端用户接入IPv6或双栈类型的服务端时，会显示以下信息：
IPv6网络地址
显示客户端传送加密信息的接口的IPv6地址（由服务端自动分配）。
IPv6前缀长度
显示客户端传送加密信息的接口的IPv6前缀长度。
IPv6 DNS服务器地址
显示服务端下发给客户端使用的DNS服务器地址，该地址为IPv6类型。
查看日志
在客户端页面，点击“日志”页签，查看日志信息。点击“导出日志”，导出日志信息到本地文件。点击
“清除日志”，清除客户端日志。
点击
，选择“日志级别”，设置需要显示的日志的级别。
配置检查更新
客户端支持自动更新检测和手动更新检测。手动更新检测操作是在客户端页面，点击
，选择“检查更
新”。当有可用更新时，在弹出的提示框中，进行如下操作：
l 选择“确认”，用户可前往国产操作系统自带的软件应用商店下载安装最新的客户端。
l 选择“不再提醒”，下次启动客户端时，将不再出现自动更新提示。

<!-- 来源页 1974 -->
通用设置
在客户端页面，点击“设置”。
l 自动重连：开启后，客户端将在连接中断时进行自动重连。
l 自动登录：开启后，客户端将在启动时使用上一次登录成功的连接信息进行自动登录。
l 连接最小化：开启后，客户端将在连接成功后自动缩小到托盘。
l 可信服务器证书管理：在建立连接时开启“验证服务器证书”功能后，点击
按钮，在<可信证书>页面点击
“导入”按钮，导入对服务器进行认证的证书。点击“删除”按钮，删除列表中的可信证书。
l 客户端证书管理：点击
按钮，在<客户端证书管理>页面点击“导入”按钮，导入登录认证需要的证书，证
书为PKCS#12格式，可以导入国密、非国密证书。最多可以导入16个证书文件。点击“删除”按钮，删除列表
中的证书。
l 状态通知：当客户端连接成功或失败时，出现相应的状态弹窗通知。
客户端菜单
右键单击系统任务栏通知区域的Secure Connect ChineseOS客户端的绿色图标，系统弹出客户端菜单，
菜单项的作用如下：
l 修改密码：弹出<修改密码>对话框输入密码信息。
l 重定向URL：服务端配置重定向URL时，点击此菜单可以快速跳转至该地址。
l 资源列表：当用户访问SCVPN服务时，连接成功后点击此菜单项将弹出浏览器页面，用户可以点击页面里的资源
条目访问内网资源。
l 应用资源列表：当用户使用Secure Connect ChineseOS客户端访问ZTNA服务时，连接成功后可以看到此菜单
项。用户登录成功后弹出的Portal页面关闭后，可以点击该菜单打开最新的Portal页面查看应用资源的访问权
限。Portal页面上展示用户有权限和无权限访问的应用资源。对于无权限访问的应用资源，用户在调整终端配置

<!-- 来源页 1975 -->
后，可以获得访问权限。禁止访问的应用资源不在Portal页面上展示，如果用户被禁止访问任何应用资源，
Portal页面将展示“无可用的Web服务资源”。
l 显示主页面：当客户端界面处于最小化状态时，点击此项可以显示客户端主页面。
l 退出：退出Secure Connect ChineseOS客户端程序。
客户端的卸载
从PC上卸载Secure Connect ChineseOS客户端，从“开始”菜单栏中找到“Hillstone Secure
Connect”，右键点击“Hillstone Secure Connect”，在菜单中选择“卸载”。
