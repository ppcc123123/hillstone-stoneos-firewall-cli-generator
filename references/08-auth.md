# 用户认证

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 11 用户认证
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 1195 -->
11 用户认证
介绍
对用户和主机进行识别，即为“认证”，认证是产品的一个重要功能。开启了认证功能的网络能够允许或拒
绝用户和主机对网络进行访问。从用户的角度出发，认证可以分为：
l 位于企业内网的用户通过认证访问互联网。该方式下的认证支持以下几种：
l "Web认证" 在第1278页
l "单点登录介绍" 在第1298页
l "802.1X认证" 在第1331页
l "Portal认证" 在第1329页（仅支持通过CLI配置）
l "PKI" 在第1339页
l 位于互联网的用户访问内网的资源（通常使用VPN）
l "SSL VPN" 在第1490页
l "IPSec VPN" 在第1392页（IPSec VPN （radius服务器）+Xauth）
l "L2TP VPN" 在第1703页（L2TP over IPsec VPN）
用户认证流程
用户通过终端与防火墙建立连接，防火墙基于存储在AAA服务器上的用户信息来认证用户。
l 认证用户（User）：认证请求者。用户发起认证给认证系统，并输入用户名和口令。
l 认证系统（Firewall）：接收用户名和密码，并向认证服务器发送认证请求。认证系统在认证用户和认证服务器
之间充当代理角色。
l 认证服务器（AAA Server）：判断认证请求。该服务器可以存储用户的相关信息，如用户名称、用户口令等。
它收到合法请求后，判断用户是否有权使用网络资源，并向认证系统返回认证结果。有关认证服务器的信息，请
参考"AAA（认证、授权与计费）" 在第1195页。认证服务器分为以下六种：

<!-- 来源页 1196 -->
l 本地服务器
l Radius服务器
l LDAP服务器
l AD服务器
l TACACS+服务器
l OAuth2服务器

<!-- 来源页 1197 -->
AAA（认证、授权与计费）
AAA概念简介
AAA是Authentication（认证）、Authorization（授权）和Accounting（计费）的简称。具体内容如
下：
l 认证：验证用户身份。
l 授权：根据配置对用户授予一定权限。
l 计费：记录用户使用网络资源应付的费用。
设备支持以下认证方式：
l 本地认证：将用户信息（包括用户名称、密码和各种属性）配置在Hillstone设备上。本地认证速度快，可以降低
运营成本，但是存储信息量受设备硬件条件的限制。默认情况下，Hillstone设备使用本地认证的方式对用户进行
认证。
l 外部认证：支持通过RADIUS、LDAP、AD、TACACS+和OAuth2协议进行外部认证。将用户信息储存在外部
RADIUS、LDAP、AD、TACACS+和OAuth2服务器上，通过外部服务器对Hillstone设备的用户进行认证。
系统支持以下授权方式：
l 本地授权：根据Hillstone设备上为本地用户帐号配置的相关属性进行授权。
l 外部服务器认证成功后授权：RADIUS/LDAP/AD/TACACS+协议的认证和授权绑定在一起。
系统支持以下计费方式：
l 不计费：不记录用户使用网络资源的费用。
l 外部服务器计费：使用RADIUS服务器对通过认证的用户进行计费。
AAA服务器介绍
AAA服务器是认证服务器，存储用户信息（包括用户名称、密码和各种属性），在用户请求访问网络时，提
供认证功能。有关认证的工作流程，请参考"用户认证" 在第1193页。
AAA服务器包括以下六种：
l 本地服务器：Local服务器即设备本身。将用户信息存储在防火墙上。本地认证速度快，可以降低运营成本，但
是存储信息量受设备硬件条件的限制。

<!-- 来源页 1198 -->
l 外部服务器，包括：
l Radius服务器
l LDAP服务器
l Active-Directory 服务器
l TACACS+服务器
l OAuth2服务器
根据认证类型的不同，选择不同的AAA服务器。
l 802.1x认证：只能选择Local和Radius服务器。
l IPSec-XAUTH：可选择Local、Radius、LDAP、AD、Tacacs+服务器。
配置AAA
AAA的配置主要包括：
l 创建AAA服务器
l 配置本地服务器认证参数
l 配置RADIUS服务器认证参数
l 配置Active-Directory服务器认证参数
l 配置TACACS+服务器认证参数
l 配置LDAP服务器认证参数
l 配置OAuth2服务器认证参数
l 配置企业微信服务器认证参数
l 配置钉钉服务器认证参数
l 配置中孚服务器认证参数
l 配置SAML服务器认证参数
l 配置RADIUS服务器的计费功能
l 配置服务器认证与授权
l 认证与授权的显示与调试
l 配置防暴力破解功能
l 配置信任域/证书链

<!-- 来源页 1199 -->
创建AAA服务器
对AAA的各项配置需要在AAA服务配置模式下进行。在全局配置模式下使用以下命令创建AAA服务器：
aaa-server aaa-server-name [type] {local | radius | active-directory | ldap | tacacs+ | oauth|
wecom | dingtalk | saml | zhongfu}
l
aaa-server-name – 指定AAA服务实例的名称，为1到31个字符的字符串，区分大小写。
l
type {local | radius | active-directory | ldap | tacacs+ | oauth | wecom | dingtalk | saml |
zhongfu} – 指定所创建AAA服务器的类型，可以是本地（local）、RADIUS（radius）、ActiveDirectory（active-directory）、LDAP（ldap）、TACACS+、OAuth2、企业微信、钉钉、SAML或
者中孚类型的服务器。
执行该命令后，系统创建指定名称的AAA服务实例，并且进入AAA服务配置模式；如果指定的名称已存在，
则直接进入AAA服务配置模式。在全局配置模式下使用该命令no的形式删除指定的AAA服务器：
no aaa-server aaa-server-name
配置本地服务器认证参数
在全局配置模式下执行aaa-server aaa-server-name type local命令可以进入指定名称的本地服务器配
置模式。用户可配置的本地服务器认证参数包括：
l 配置账户控制
l 配置密码控制
l 指定用户名格式
l 配置角色映射规则
l 配置用户黑名单
l 配置备份认证服务器
l 配置认证码控制
配置账户控制
为了提高用户账户的安全性，系统提供账户控制功能，用户可以在账户控制功能中开启并配置账户到期提
醒。账户到期提醒默认关闭，开启该功能后，系统会检查用户账户在本地服务器中的状态，即检查账户是否
过期，并对即将过期的账号进行剩余有效天数提醒。
开启并配置账户到期提醒功能，在本地服务器配置模式下，使用以下命令：
alert-before-account-expire alert-day

<!-- 来源页 1200 -->
l
alert-day – 指定在账户到期时间前提醒用户账户即将到期。取值范围是1-30天，例如在账户到期前10
天提醒用户账户即将到期，默认值是7。关于如何配置用户账户到期时间，请参阅指定用户有效期。
使用no alert-before-account-expire关闭账户到期提醒功能。
注意: 开启并配置账户到期提醒功能后，
l
如果开启了Web认证功能并且认证服务器为本地服务器，当账户即将到期的用户进行Web认证
时，Web认证登录页面会提示账户的剩余有效天数。
l
如果系统采用本地认证服务器进行SSL VPN/ZTNA客户端用户身份认证，当账户即将到期的用
户通过客户端登录SSL VPN/ZTNA时，客户端会弹出窗口提示账户的剩余有效天数。支持弹窗
提示账户剩余有效天数的客户端版本包括Windows客户端v5.0.1.10328及之后版本、
Android客户端v5.0.1.10331及之后版本、iOS客户端v5.0.1及之后版本、macOS客户端
v5.0.1.10331及之后版本、Linux客户端v5.0.1.10331及之后版本，其它客户端版本无弹窗
提示。
配置密码控制
为了提高用户密码的安全性以防止出现安全问题，系统提供密码控制功能。对于密码控制功能的配置，必须
在密码控制配置模式下进行。进入密码控制配置模式，在本地服务器配置模式下，使用以下命令：
password-control
系统支持的密码控制功能包括：
l
允许本地用户修改密码
l
配置首次登录修改密码
l
配置密码过期时间及密码到期提醒功能
l
配置历史密码检查功能
l
配置密码复杂度
l
开启/关闭首次登录强制修改密码功能
允许本地用户修改密码
系统支持本地用户通过Web认证后，在认证登录成功页面修改自己的用户密码。具体配置方法，请参阅“用
户认证>用户识别>Web认证>允许本地用户修改密码。

<!-- 来源页 1201 -->
系统支持本地用户成功通过SSL VPN认证后，在客户端修改自己的用户密码。具体配置方法，请参阅
“VPN>SSL VPN>SSL VPN设备端配置>Secure Connect客户端管理>Secure Connect客户端管理配置>
允许本地用户修改密码。
配置首次登录修改密码
默认情况下，首次登录修改密码功能为关闭状态。配置首次登录修改密码功能，在密码控制配置模式下，使
用以下命令：
first-login-check [ mode { compatibility | enforcement }]
l
compatibility – 指定首次登录修改密码为兼容模式。下发命令first-login-check也指定首次登录修改
密码为兼容模式。兼容模式分为两种情况：①若SSL VPN客户端版本不支持该功能，用户首次登录SSL
VPN客户端时，无需修改密码，可立即使用；②若SSL VPN客户端版本支持该功能，用户首次登录SSL
VPN客户端时，需立即修改登录密码后才可使用。
l
enforcement – 指定首次登录修改密码为强制模式。首次登录SSL VPN客户端时，需立即修改登录密码
才可使用。
注意:
l
配置强制模式后，若SSL VPN客户端不支持该功能，客户端将无法正常使用。建议升级客户端
版本或切换至兼容模式。
l
支持首次登录修改密码的SSL VPN客户端版本：SSL VPN Window 客户端1.4.9.1274及之
后版本、Linux 1.4.0及之后版本、Android 4.5及之后版本、iOS2.0.6及之后版本。
l
SSL VPNWindows客户端（非管理员）1.5.x版本不支持首次登录修改密码。
配置密码过期时间及密码到期提醒功能
配置密码的过期时间并配置密码到期提醒功能，即在过期前n天提醒用户修改密码。还可以配置历史密码检
查功能，新密码不能与前n次历史密码重复。
配置密码的过期时间及密码到期提醒，在密码控制配置模式下，使用以下命令：
aging aging-day [alert-before-expire alert-day]
l
aging-day – 指定密码的过期时间。取值范围是1-365天，默认值是90。
l
alert-day–指定在密码过期前提醒用户修改密码的天数。取值范围是1-30天，例如在密码前15天提醒
用户修改密码，默认值是7。
使用no aging取消密码过期时间及密码到期提醒的配置。

<!-- 来源页 1202 -->
配置历史密码检查功能
配置历史密码检查功能，在修改密码时，进行历史密码的校验，新密码不能与前n次历史密码重复，在密码
控制配置模式下，使用以下命令：
history-check count
l
count – 指定新密码不能与前n次历史密码重复。取值范围是1-5，默认值是3。
使用no history-check取消历史密码检查的配置。
配置密码复杂度
密码的复杂度越低，其被破解的可能性就越大，比如包含用户名、密码长度短等。出于安全性的考虑，用户
可以开启密码复杂度的配置功能并配置密码复杂度的要求，以确保用户的密码具有较高的复杂度。
开启密码复杂度配置功能，在密码控制配置模式下，使用以下命令：
complexity enable
使用no complexity enable命令关闭密码复杂度配置功能。
配置密码复杂度，在密码控制配置模式下，使用以下命令：
complexity {capital-letters letters | small-letters length | min-length length | no-includeusername | non-alphanumeric-letters length | numeric-characters length}
l
capital-letters letters - 指定密码包含的大写字母的最小长度，范围是0-16，默认值是0。
l
small-letters length - 指定密码包含的小写字母的最小长度，范围是0-16，默认值是0。
l
min-length length - 指定密码最小长度，范围是1-16，默认值是1。
l
no-include-username - 指定密码不能包含用户名。
l
non-alphanumeric-letters length - 指定密码包含特殊字符（即非数字的字符）的最小长度，范围
是0-16，默认值是0。
l
numeric-characters length - 指定密码包含的数字的最小长度，范围是0-16，默认值是0。
使用no complexity {capital-letters | small-letters | min-length | no-include-username | nonalphanumeric-letters | numeric-characters}命令恢复密码复杂度的默认值。
指定用户名格式
用户认证时，系统会根据配置的认证用户名格式，对用户名进行提取（不满足格式时，使用原始用户名）。
最终使用提取后的用户名进行认证。指定认证用户名格式，在本地服务器配置模式下，使用以下命令：
extract-username-format authenticate { [domain\username ] [ username@domain] }

<!-- 来源页 1203 -->
删除认证用户名格式配置，在本地服务器配置模式下，使用以下命令：
no extract-username-format authenticate { [domain\username ] [username@domain] }
在基于用户/用户组进行策略控制时，系统会根据配置的用户名格式在本地存储的组织机构中查找用户名所属
的用户组。指定查找用户组时支持的用户名格式，在本地服务器配置模式下，使用以下命令：
extract-username-format search-usergroup { [domain\username ] [ username@domain] }
删除查找用户组时的用户名格式配置，在本地服务器配置模式下，使用以下命令：
no extract-username-format search-usergroup { [domain\username ] [username@domain] }
配置角色映射规则
为本地服务器指定角色映射规则后，系统将会为通过该服务器认证的用户按照指定角色映射规则分配角色。
为本地服务器指定角色映射规则，在本地服务器配置模式下，使用以下命令：
role-mapping-rule rule-name
l
rule-name – 指定系统中已经配置的角色映射规则的名称。
在本地服务器配置模式下，使用该命令no的形式取消角色映射规则的指定：
no role-mapping-rule
配置用户黑名单
为本地服务器配置用户黑名单后，系统将会禁止通过该服务器认证的黑名单用户访问任何网络资源。配置用
户黑名单，在本地服务器配置模式下，使用以下命令：
user-block-list username user-name
l
user-name – 指定黑名单中的用户名。取值范围是1到63个字符。
在本地服务器配置模式下，使用该命令no的形式删除黑名单用户：
no user-block-list username user-name
配置备份认证服务器
为本地服务器配置备份认证服务器后，当主服务器出现问题或者用户在主服务器认证失败时，备份认证服务
器发挥身份认证的作用。备份认证服务器可以与主服务器为不同类型。系统中已配置的本地、ActiveDirectory、RADIUS或者LDAP服务器均可作为备份认证服务器。为本地服务器配置备份认证服务器，在本
地服务器配置模式下，使用以下命令：
backup-aaa-server aaa-server-name
l
aaa-server-name – 指定系统中已经配置的AAA服务器的名称。
在本地服务器配置模式下，使用该命令no的形式取消备份认证服务器的配置：

<!-- 来源页 1204 -->
no backup-aaa-server
注意:
l
备份认证服务器和主认证服务器必须处于相同VSYS。关于VSYS的详细信息，请参阅虚拟系
统。
l
备份认证服务器不能嵌套备份认证服务器。
l
删除AAA服务器之前，请确保该服务器未被指定为备份认证服务器。
配置认证码控制
当用户通过Hillstone Secure Connect客户端接入SSL VPN或ZTNA时忘记连接密码，用户可以自行通过
短信认证码或邮件认证码的方式找回密码，而不用反馈给管理员进行处理。对于认证码控制功能的配置，必
须在认证码控制配置模式下进行。
注意:
l
仅Windows、Linux、macOS端的Hillstone Secure Connect客户端支持找回密码功能。
l
仅v5.5.0.11806版本、v5.5.7版本及其之后版本的Hillstone Secure Connect客户端支持找
回密码功能。
l
该功能不支持非根VSYS。
进入认证码控制配置模式，在本地服务器配置模式下，使用以下命令：
verify-code-control
系统支持的认证码控制功能包括：
l
短信认证码
l
邮件认证码
短信认证码
短信认证码功能是指用户通过Hillstone Secure Connect客户端找回密码时，收到请求的山石网科设备通
过短信猫或短信网关自动向该用户的手机号码发送一条包含随机认证码的短信，用户输入收到的认证码后，
才可以通过认证，设置新的密码。配置短信认证码功能前，请用户预先连接短信猫或配置短信网关实例。
指定短信认证类型
指定短信认证类型，在认证码控制配置模式下，使用以下命令：
sms verify-type {modem | service-provider}

<!-- 来源页 1205 -->
l
modem - 指定短信认证类型为短信猫。
l
service-provider - 指定短信认证类型为短信网关。
注意: 云·界、X系列设备、K20803、K9180、K7680、K7280、K6680、K6580不支持短信猫。
配置短信认证码长度
配置短信认证码长度，在认证码控制配置模式下，使用以下命令：
sms verify-code-length number
l
number – 指定短信认证码长度。取值范围为4-8个字符，默认为8个字符。
在认证码控制配置模式下使用no sms verify-code-length命令恢复默认短信认证码长度。
配置短信认证码有效时间
配置短信认证码有效时间，在认证码控制配置模式下，使用以下命令：
sms verify-code-timeout number
l
number – 指定短信认证码有效时间。取值范围为1-10分钟，默认为1分钟。
在认证码控制配置模式下使用no sms verify-code-timeout命令恢复默认短信认证码有效时间。
指定短信网关实例
当短信认证类型为短信网关时，还需指定短信网关实例。
指定短信网关实例，在认证码控制配置模式下，使用以下命令：
sms service-provider sp-name
l
sp-name – 指定短信网关实例，该实例必须是系统中已创建的短信网关实例。
在认证码控制配置模式下使用no sms service-provider命令取消指定短信网关实例。
指定签名
用户可以指定显示在短信内容中的签名。
注意: 当使用短信网关认证时，如果该短信网关实例的协议类型为ALIYUNSMS（即使用阿里云短
信服务平台），则用户必须指定签名，并且该签名需要与在阿里云短信服务中申请的签名保持一
致。
指定签名，在认证码控制配置模式下，使用以下命令：
sms sender-name sender-name

<!-- 来源页 1206 -->
l
sender-name – 指定签名，取值范围为1到63个字符。
在认证码控制配置模式下使用no sms sender-name命令取消指定签名。
指定模板CODE
当使用短信网关认证时，如果该短信网关实例的协议类型为ALIYUNSMS（即使用阿里云短信服务平台），
则用户必须指定模板CODE，并且该CODE需要与在阿里云短信服务中申请的模板CODE保持一致。
指定模板CODE，在认证码控制配置模式下，使用以下命令：
sms template-code string
l
string – 指定模板CODE，取值范围为1到30个字符。该参数需与在阿里云短信服务中申请的模板CODE
保持一致。
在认证码控制配置模式下使用no sms template-code命令取消指定模板CODE。
邮件认证码
邮件认证码功能是指用户通过Hillstone Secure Connect客户端找回密码时，收到请求的山石网科设备通
过邮件服务器自动向该用户的邮箱发送一条包含随机认证码的邮件，用户输入收到的认证码后，才可以通过
认证，设置新的密码。配置邮件认证码功能前，请用户预先配置邮件服务器。
指定邮件服务器
指定邮件服务器，在认证码控制配置模式下，使用以下命令：
email smtp-server smtp-server-name
l
smtp-server-name – 指定邮件服务器，该服务器必须为系统中已配置的邮件服务器。
在认证码控制配置模式下使用no email smtp-server命令取消指定邮件服务器。
配置邮件认证码长度
配置邮件认证码长度，在认证码控制配置模式下，使用以下命令：
email verify-code-length number
l
number – 指定邮件认证码长度。取值范围为4-8个字符，默认为8个字符。
在认证码控制配置模式下使用no email verify-code-length命令恢复默认的邮件认证码长度。
配置邮件认证码有效时间
配置邮件认证码有效时间，在认证码控制配置模式下，使用以下命令：
email verify-code-timeout number

<!-- 来源页 1207 -->
l
number – 指定邮件认证码有效时间。取值范围为1-10分钟，默认为10分钟。
在认证码控制配置模式下使用no email verify-code-timeout命令恢复默认的邮件认证码有效时间。
配置发送方名称
配置认证码的发送方名称以显示在邮件内容中，在认证码控制配置模式下，使用以下命令：
email sender-name sender-name
l
sender-name – 指定认证码的发送方名称。取值范围为1到63个字符。为防止认证码邮件被认定为垃
圾邮件，建议用户进行认证码邮件发送方名称的配置。
在认证码控制配置模式下使用no email sender-name命令取消配置发送方名称。
配置RADIUS服务器认证参数
在全局配置模式下执行aaa-server aaa-server-name type radius命令可以进入指定名称的RADIUS服
务器配置模式。用户可配置的RADIUS服务器认证参数包括：
l 配置RADIUS认证的源IP地址
l 配置认证主服务器的IP地址或域名
l 配置备份服务器1的IP地址或域名
l 配置备份服务器2的IP地址或域名
l 配置RADIUS服务器端口号
l 配置RADIUS服务器的共享密钥
l 配置重试次数
l 配置超时时间
l 指定用户名格式
l 配置角色映射规则
l 配置用户黑名单
l 配置备份认证服务器
l 配置防暴力破解功能
l 启用/禁用授权策略
l 添加授权策略到聚合策略
l 配置SM4国密加密算法

<!-- 来源页 1208 -->
配置RADIUS认证的源IP地址
当使用RADIUS服务器服务器进行认证时，用户可按需指定LOCAL NAS（Network Access Server）IP地
址。指定LOCAL NAS IP地址，在RADIUS服务器配置模式下，使用以下命令：
local-nas-ip ip-address
l
ip-address – 指定LOCAL NAS（Network Access Server）IP地址（当前仅支持IPv4地址。）指定
后，RADIUS认证、计费报文中的源地址以及认证报文中的“nas-ip-address”都将变更为该指定地
址，从而保证保证复杂网络环境下，RADIUS服务器返回的报文能被当前设备正常接收到。指定时，需保
证LOCAL NAS IP 需为本设备上的接口IP，否则可能无法正常发送RADIUS认证或计费报文。
在RADIUS服务器配置模式下，使用该命令no的形式删除认证LOCAL NAS IP地址：
no local-nas-ip ip-address
注意:
l
在HA环境下，本地认证源IP的配置不会被同步到备设备上，所以用户需在主、备设备上进行分
别配置。
l
需保证RADIUS服务器上与当前设备是路由可达的。
配置认证主服务器的IP地址或域名
配置认证主服务器的IP地址或域名以及所属的VRouter，在RADIUS服务器配置模式下，使用以下命令：
host {ip-address | host-name }[vrouter vrouter-name]
l
ip-address | host-name – 指定认证主服务器的IP地址（IPv4地址或IPv6地址）或者域名。
l
vrouter vrouter-name – 指定认证主服务器所属的VRouter。默认为系统缺省VR即trust-vr。
在RADIUS服务器配置模式下，使用该命令no的形式取消认证主服务器的IP地址或者域名配置：
no host
配置备份服务器1的IP地址或域名
该参数为可选配置。备份服务器是与主服务器相同类型服务器。在当通过主服务器进行认证失败时，依次启
用备份服务器1和2进行认证。配置备份服务器1的IP地址或域名以及所属的VRouter，在RADIUS服务器配
置模式下，使用以下命令：
backup1 {ip-address | host-name }[vrouter vrouter-name]

<!-- 来源页 1209 -->
l
ip-address | host-name – 指定备份服务器1的IP地址（IPv4地址或IPv6地址）或者域名。
l
vrouter vrouter-name – 指定认证主服务器所属的VRouter。默认为系统缺省VR即trust-vr。
在RADIUS服务器配置模式下，使用该命令no的形式取消备份服务器1的IP地址或者域名配置：
no backup1
配置备份服务器2的IP地址或域名
该参数为可选配置。备份服务器是与主服务器相同类型服务器。在当通过主服务器进行认证失败时，依次启
用备份服务器1和2进行认证。配置备份服务器2的IP地址或域名以及所属的VRouter，在RADIUS服务器配
置模式下，使用以下命令：
backup2 {ip-address | host-name }[vrouter vrouter-name]
l
ip-address | host-name – 指定备份服务器2的IP地址（IPv4地址或IPv6地址）或者域名。
l
vrouter vrouter-name – 指定备份服务器所属的VRouter。默认为系统缺省VR即trust-vr。
在RADIUS服务器配置模式下，使用该命令no的形式取消备份服务器2的IP地址或者域名配置：
no backup2
配置RADIUS服务器端口号
配置RADIUS服务器端口号，在RADIUS服务器配置模式下，使用以下命令：
port port-number
l
port-number – 指定RADIUS服务器的端口号。默认值是1812。取值范围是1024到65535。
在RADIUS服务器配置模式下，使用该命令no的形式恢复端口号的默认值：
no port
配置RADIUS服务器的共享密钥
配置RADIUS服务器的共享密钥，在RADIUS服务器配置下，使用以下命令：
secret secret
l
secret – 指定RADIUS服务器的共享密钥字符串。字符串范围为1到31个字符。
在RADIUS服务器配置模式下，使用该命令no的形式取消对RADIUS服务器共享密钥的配置：
no secret

<!-- 来源页 1210 -->
配置重试次数
重试次数指Hillstone设备向AAA服务器在没有收到服务器回应时重新发送认证报文的次数。配置重试次
数，在RADIUS服务器配置模式下，使用以下命令：
retries times
l
times – 指定重传次数。取值范围是1到10次。默认为3次。
在RADIUS服务器配置模式下使用该命令no的形式恢复重传次数的默认值：
no retries
配置超时时间
超时时间指AAA服务器的应答超时时间。如果在超时时间结束时Hillstone设备仍未收到服务器的应答，则
会重新发送认证报文。重新发送报文的次数由retries times命令配置。配置超时时间，在RADIUS服务器配
置模式下，使用以下命令：
timeout time-value
l
time-value – 指定超时时间，单位为秒。取值范围是1到30秒。默认为3秒。
在RADIUS服务器配置模式下使用该命令no的形式恢复超时时间的默认值：
no timeout
指定用户名格式
用户认证时，系统会根据配置的认证用户名格式，对用户名进行提取（不满足格式时，使用原始用户名）。
最终使用提取后的用户名进行认证。指定认证用户名格式，在RADIUS服务器配置模式下，使用以下命令：
extract-username-format authenticate { [domain\username ] [ username@domain] }
删除认证用户名格式配置，在RADIUS服务器配置模式下，使用以下命令：
no extract-username-format authenticate { [domain\username ] [username@domain] }
在基于用户/用户组进行策略控制时，系统会根据配置的用户名格式在本地存储的组织机构中查找用户名所属
的用户组。指定查找用户组时支持的用户名格式，在RADIUS服务器配置模式下，使用以下命令：
extract-username-format search-usergroup { [domain\username ] [ username@domain] }
删除查找用户组时的用户名格式配置，在RADIUS服务器配置模式下，使用以下命令：
no extract-username-format search-usergroup { [domain\username ] [username@domain] }
指定角色映射规则
为RADIUS服务器指定角色映射规则后，系统将会为通过该服务器认证的用户按照指定角色映射规则分配角
色。为RADIUS服务器指定角色映射规则，在RADIUS服务器配置模式下，使用以下命令：

<!-- 来源页 1211 -->
role-mapping-rule rule-name
l
rule-name – 指定系统中已配置的映射规则的名称。
在RADIUS服务器配置模式下，使用该命令no的形式取消角色映射规则的指定：
no role-mapping-rule
配置用户黑名单
为RADIUS服务器配置用户黑名单后，系统将会禁止通过该服务器认证的黑名单用户访问任何网络资源。配
置用户黑名单，在RADIUS服务器配置模式下，使用以下命令：
user-block-list username user-name
l
user-name – 指定黑名单中的用户名。取值范围是1到63个字符。
在RADIUS服务器配置模式下，使用该命令no的形式删除黑名单用户：
no user-block-list username user-name
配置备份认证服务器
为RADIUS服务器配置备份认证服务器后，当主服务器出现问题或者用户在主服务器认证失败时，备份认证
服务器发挥身份认证的作用。备份认证服务器可以与主服务器为不同类型。系统中已配置的本地、ActiveDirectory、RADIUS或者LDAP服务器均可作为备份认证服务器。为RADIUS服务器配置备份认证服务器，
在RADIUS服务器配置模式下，使用以下命令：
backup-aaa-server aaa-server-name
l
aaa-server-name – 指定系统中已经配置的AAA服务器的名称。
在RADIUS服务器配置模式下，使用该命令no的形式取消备份认证服务器的配置：
no backup-aaa-server
注意:
l
备份认证服务器和主认证服务器必须处于相同VSYS。关于VSYS的详细信息，请参阅虚拟系统
章节。
l
备份认证服务器不能嵌套备份认证服务器。
l
删除AAA服务器之前，请确保该服务器未被指定为备份认证服务器。
l
如果为同一RADIUS服务器配置了备份服务器1（backup1）、备份服务器2（backup2）和
备份认证服务器（backup-aaa-server），当用户在主服务器认证无响应时，系统会先通过

<!-- 来源页 1212 -->
备份服务器1和2进行认证，如果备份服务器1和2认证无响应，再通过备份认证服务器对该用户
再次进行认证；但当用户在主服务器、备份服务器1或者备份服务器2认证失败时，系统会直接
通过备份认证服务器对该用户再次进行认证。
添加字典文件
对于Radius服务器来说，厂商的属性以字典文件的方式来定义。山石防火墙的字典文件名为
dictionary.hillstone。RARIUS服务器管理员通过修改服务器的主字典文件的方式，将
dictionary.hillstone文件引用进来。
dictionary.hillstone字典文件定义了以下属性：
属性
说明
Hillstone-user-type
用户类型。admin type=16 PnPVPN=4 all=31 其他类型用户不检查此
值。
Hillstone-user-vsys-id
VSYS ID值。管理员必须配置此参数。目前仅支持ID等于0。
Hillstone-user-login-type
管理员登录类型。
telnet＝2
SSH＝4
CONSOLE＝1
HTTP＝8
HTTPS＝16
all＝31
任意组合等于数值相加的值（如telnet+SSH＝6）。
Hillstone-user-role-name
管理员角色类型。
admin=系统管理员
operator=系统操作员
auditor=系统审计员
admin-read-only=系统管理员（只读）
role-name=自定义管理员角色
Hillstone-user-policy-dstip-begin
授权区域的起始IP地址。请输入IPv4地址。
Hillstone-user-policy-dstip-end
授权区域的终止IP地址。请输入IPv4地址。
Hillstone-User-Data-Filter
RADIUS服务器通过该属性将策略规则下发给认证用户。
属性格式为：
rule number {permit|deny} [ dst ip-address ] [ protocol [ dstport port ] ]

<!-- 来源页 1213 -->
属性
说明
l
number：Radius服务器中策略的编号。
l
permit|deny：策略规则动作，permit表示允许访问，deny表示拒
绝访问。
l
dst ip-address：目的地址。可配置多个，之间请使用空格分隔。
l
protocol：协议类型，可指定为TCP或者UDP。
l
dst-port port ]：目的端口号。可配置多个，之间请使用空格分隔。
配置防暴力破解功能
为了防止非法用户通过暴力方法获取用户名和密码，可以通过配置基于用户名或基于IP地址的防暴力破解功
能，即在指定时间内，若用户连续输错指定次数的用户名和密码，系统将会按照指定的锁定时间锁定该用户
或IP地址。防暴力破解功能的配置包括：
l 开启或关闭防暴力破解功能
l 配置尝试次数
l 配置锁定时间
开启或关闭防暴力破解功能
防暴力破解功能默认情况下是关闭的。开启防暴力破解功能，请在RADIUS服务器配置模式下使用以下命
令：
l
启用：lockout {ip | user} enable
l
关闭：lockout {ip | user} disable
配置尝试次数
配置尝试次数，即在指定时间内，允许用户连续输错用户名和密码的次数，请在RADIUS服务器配置模式下
使用以下命令：
lockout {ip | user} failed-attempts number interval interval
l
failed-attempts number – 指定时间内允许输错用户名和密码的次数，基于用户名配置时，取值范围
是1-32，默认值是5次；基于IP地址配置时，取值范围是1-2048，默认值是64次。
l
interval interval – 指定连续输错用户名和密码的时间范围，单位是秒，取值范围是1-180秒，默认值
是60秒。

<!-- 来源页 1214 -->
配置锁定时间
在指定时间内，若用户连续输错指定次数的用户名和密码，系统将会按照指定的锁定时间锁定该用户或IP地
址。配置锁定时间，请在RADIUS服务器配置模式下使用以下命令：
lockout {ip | user} lockout-time time
l
lockout-time time – 指定锁定时间，单位是秒，取值范围是30-1800秒，基于用户名配置时，默认值
是600秒；基于IP地址配置时，默认值是60秒。
查看锁定列表信息
查看被锁定的用户信息、被锁定的IP地址信息，在任何模式下，使用以下命令：
show aaa-server aaa-server-name lockout {user [username] | ip [ip-address vr_id number]}
l
aaa-server-name - 指定AAA服务器名称。
l
user [username] - 查看指定名称的锁定用户信息。
l
ip [ip-address vr_id number] - 查看指定IP地址和VRouter ID的锁定IP信息。
解除用户/IP地址的锁定
解除对指定用户/IP地址的锁定并且从锁定列表中删除，在任何模式下，使用以下命令：
exec aaa aaa-server aaa-server-name lockout delete {user [username] | ip [ip-address vr_id
number]}
l
aaa-server-name - 指定AAA服务器名称。
l
user [username] - 解除对指定名称的用户的锁定。
l
ip [ip-address vr_id number] - 解除对指定IP地址和VRouter ID的锁定。
启用/禁用授权策略
用户通过Radius服务器认证时，当用户认证成功后，Radius服务器会为认证用户创建一条包含目的网段、
目的端口、协议以及行为的安全策略，该策略被称为授权策略。系统支持“认证时授权策略”和“动态授权
策略”两种授权策略，用户可以启用授权策略功能，使系统能够从Radius服务器获取该授权策略，并加入到
系统的策略列表中，使其生效。当认证用户断开连接后，授权策略将会被自动删除。
默认情况下，授权策略为禁用状态。启用或禁用授权策略，在RADIUS服务器配置模式下，使用以下命令：
l
启用：authorization-policy enable
l
禁用：authorization-policy disable

<!-- 来源页 1215 -->
注意: 如果需要获取通过Radius CoA报文动态修改后的动态授权策略，请先配置Radius动态授权
功能。关于Radius动态授权功能的配置方法，请参阅“"配置Radius动态授权" 在第1276页”。
添加授权策略到聚合策略
启用Radius服务器的授权策略后，用户可以指定将获取到的授权策略添加到系统已创建的聚合策略中，作为
聚合策略成员排列在聚合策略的末尾，更便于用户统一管理授权策略。如果未添加到聚合策略，授权策略将
会默认加入到系统策略列表的末尾。
添加授权策略到聚合策略，在RADIUS服务器配置模式下，使用以下命令：
authorization-policy associated-aggregate-rule rule-name
l
rule-name- 指定需要添加到的聚合策略名称。
在RADIUS服务器配置模式下，使用该命令no的形式取消添加：
no authorization-policy associated-aggregate-rule
配置SM4国密加密算法
Radius服务器支持使用SM4国密加密算法对密码进行加密存储以及加密传输。为Radius服务器配置SM4国
密加密算法，需要在扩展配置模式下使用相关命令进行配置。
进入扩展配置模式，在RADIUS服务器配置模式下，使用以下命令：
extend-option
为Radius服务器配置SM4国密加密算法，在扩展配置模式下，使用以下命令：
encryption-algorithm SM4
l
SM4- 指定SM4国密加密算法。SM4不区分大小写。
在扩展配置模式下，使用no encryption-algorithm命令删除国密加密算法的配置。
配置Active-Directory服务器认证参数
在全局配置模式下执行aaa-server aaa-server-name type active-directory命令可以进入指定名称的
Active-Directory服务器配置模式。用户可配置的Active-Directory服务器认证参数包括：
l 配置认证主服务器的IP地址或域名
l 配置备份服务器1的IP地址或域名
l 配置备份服务器2的IP地址或域名
l 配置服务器端口号

<!-- 来源页 1216 -->
l 配置服务器认证或同步方法
l 指定Base-DN
l 指定同步Base-DN
l 指定同步对象
l 指定认证Base-DN
l 指定登录DN
l 指定sAMAccountName属性值
l 指定登录密码
l 指定手机号码属性名称
l 指定邮箱属性名称
l 启用/禁用SSL加密连接
l 启用/禁用SSL证书校验
l 指定用户名格式
l 配置角色映射规则
l 配置用户黑名单
l 配置AD用户
l 指定用户有效期
l 配置用户同步功能
l 指定用户名属性
l 指定组类别
l 指定用户类别
l 配置用户过滤功能
l 配置同步的工作模式
l 配置备份认证服务器
l 配置仅同步Base-DN下用户组
l 配置防暴力破解功能
l 启用/禁用简化认证功能

<!-- 来源页 1217 -->
配置认证主服务器的IP地址或域名
配置认证主服务器的IP地址或域名以及所属的VRouter，在Active-Directory服务器配置模式下，使用以下
命令：
host {ip-address | host-name }[vrouter vrouter-name]
l
ip-address | host-name – 指定认证主服务器的IP地址（IPv4地址或IPv6地址）或者域名。
l
vrouter vrouter-name – 指定认证主服务器所属的VRouter。默认为系统缺省VR即trust-vr。
在Active-Directory服务器配置模式下，使用该命令no的形式取消认证主服务器的IP地址或者域名配置：
no host
配置备份服务器1的IP地址或域名
该参数为可选配置。备份服务器是与主服务器相同类型服务器。在当通过主服务器进行认证失败时，依次启
用备份服务器1和2进行认证。配置备份服务器1的IP地址或域名以及所属的VRouter，在Active-Directory
服务器配置模式下，使用以下命令：
backup1 {ip-address | host-name }[vrouter vrouter-name]
l
ip-address | host-name – 指定备份服务器1的IP地址（IPv4地址或IPv6地址）或者域名。
l
vrouter vrouter-name – 指定认证主服务器所属的VRouter。默认为系统缺省VR即trust-vr。
在Active-Directory服务器配置模式下，使用该命令no的形式取消备份服务器1的IP地址或者域名配置：
no backup1
配置备份服务器2的IP地址或域名
该参数为可选配置。备份服务器是与主服务器相同类型服务器。在当通过主服务器进行认证失败时，依次启
用备份服务器1和2进行认证。配置备份服务器2的IP地址或域名以及所属的VRouter，在Active-Directory
服务器配置模式下，使用以下命令：
backup2 {ip-address | host-name }[vrouter vrouter-name]
l
ip-address | host-name – 指定备份服务器2的IP地址（IPv4地址或IPv6地址）或者域名。
l
vrouter vrouter-name – 指定认证主服务器所属的VRouter。默认为系统缺省VR即trust-vr。
在Active-Directory服务器配置模式下，使用该命令no的形式取消备份服务器2的IP地址或者域名配置：
no backup2
配置服务器端口号
配置Active-Directory服务器端口号，在Active-Directory服务器配置模式下，使用以下命令：

<!-- 来源页 1218 -->
port port-number
l
port-number – 指定Active-Directory服务器的端口号。默认值是389。取值范围是1到65535。
在Active-Directory服务配置模式下，使用该命令no的形式恢复端口号的默认值：
no port
配置服务器认证或同步方法
Active-Directory服务器和系统之间可以使用明文和MD5摘要两种方法进行用户认证或用户同步。配置
Active-Directory服务器认证或同步方法，在Active-Directory服务器配置模式下，使用以下命令：
auth-method {plain | digest-md5}
l
plain – 指定使用明文的方法来认证或同步用户。
l
digest-md5 – 指定使用MD5摘要的方法来认证或同步用户。该方法为系统默认认证方法。
在Active-Directory服务配置模式下，使用该命令no的形式恢复默认认证或同步方法：
no auth-method
注意: 如果指定使用MD5摘要方法后没有配置sAMAccountName属性值，那么从服务器同步用户
的过程中将使用明文方法，认证用户的过程中将使用MD5摘要方法。
指定Base-DN
指定Base-DN，Base-DN是指当Active-Directory服务器收到一个认证请求时，目录查询的起始点。在
Active-Directory服务器配置模式下，使用以下命令：
base-dn string
l
string – 指定Base-DN的具体内容，如dc=hillstonenet。
在Active-Directory服务配置模式下，使用该命令no的形式取消Base-DN的指定：
no base-dn
指定同步Base-DN
同步Base-DN是指系统从Active Directory服务器同步用户和用户组时的路径起点。指定同步Base-DN
后，该Base-DN路径下的所有用户及用户组将同步到本地。指定同步Base-DN，在Active-Directory服务
器配置模式下，使用以下命令：
sync-base-dn string
l
string – 指定从Active Directory服务器同步用户和用户组时的路径起点，如OU=test，dc=com。

<!-- 来源页 1219 -->
重复执行该命令可以配置多条需要同步的路径。
在Active-Directory服务配置模式下，使用该命令no的形式删除指定的同步Base-DN配置：
no sync-base-dn string
指定同步对象
当指定了同步Base-DN后，该同步Base-DN路径下的所有用户及用户组将会同步到本地。若没有指定同步
Base-DN，则将Base-DN路径下的所有用户及用户组同步到本地。指定同步对象为用户或用户组后，筛选
同步到本地的信息并将指定对象的信息保留。指定同步对象，在Active-Directory服务器配置模式下，使用
以下命令：
sync-object {user | group}
l
user –指定同步对象为用户，仅保留同步的用户信息。
l
group –指定同步对象为用户组，仅保留同步的用户组信息。
在Active-Directory服务配置模式下，使用该命令no的形式取消同步对象的指定：
no sync-object {user | group}
指定认证Base-DN
Base-DN是指Active-Directory服务器目录查询的起始点。指定认证Base-DN后，该Base-DN路径下的
所有用户（包括用户组中的直属用户）将允许通过认证。指定认证Base-DN，在Active-Directory服务器
配置模式下，使用以下命令：
auth-base-dn string
l
string – 指定认证Base-DN的具体内容，如OU=A，dc=hillstonenet。
在Active-Directory服务配置模式下，使用该命令no的形式取消认证Base-DN的指定：
no auth-base-dn
指定登录DN
如果使用明文方法来认证或同步用户，系统会使用登录DN和登录密码到服务器进行认证，从而能够连接服务
器进行用户认证或同步。指定登录DN（通常为AD服务器预设的具有查询权限的用户账号），在ActiveDirectory服务器配置模式下，使用以下命令：
login-dn string
l
string – 指定登录DN的具体内容，为1到255个字符的字符串，不区分大小写。
在Active-Directory服务配置模式下，使用该命令no的形式取消登录DN的指定：
no login-dn

<!-- 来源页 1220 -->
指定sAMAccountName属性值
如果使用MD5摘要方法来认证或同步用户，系统会使用sAMAccountName属性值和登录密码到服务器进行
认证，从而能够连接服务器进行用户认证或同步。配置sAMAccountName属性值，在Active-Directory服
务器配置模式下，使用以下命令：
login-dn sAMAccountName string
l
string – 指定sAMAccountName的值，为1到63个字符的字符串，区分大小写。
在Active-Directory服务配置模式下，使用该命令no的形式取消sAMAccountName的指定：
no login-dn sAMAccountName
指定登录密码
指定登录密码，此处的登录密码即为登录DN所对应的密码。在Active-Directory服务器配置模式下，使用
以下命令：
login-password string
l
string – 指定登录密码的具体内容。
在Active-Directory服务配置模式下，使用该命令no的形式取消登录密码的指定：
no login-password
指定手机号码属性名称
指定用户的手机号码属性名称，系统可以通过该属性获取用户的手机号码，用于短信口令二次认证场景。例
如，在SSL VPN短信口令认证场景中，系统可以通过该属性获取用户的手机号码。当用户登录SSL VPN时，
系统会将短信验证码发送至该号码。指定手机号码属性名称，在Active-Directory服务器配置模式下，使用
以下命令：
mobile-attribute string
l
string - 指定手机号码属性名称，默认为mobile，取值范围是1-63个字符，不区分大小写。
使用no mobile-attribute恢复手机号码属性名称的默认值。
指定邮箱属性名称
指定用户的邮箱属性名称，系统可以通过该属性获取用户的邮箱地址，用于邮箱口令二次认证场景。例如，
在SSL VPN邮箱口令认证场景中，系统可以通过该属性获取用户的邮箱地址，当用户登录SSL VPN时，系统
会将验证码发送至该邮箱。指定邮箱属性名称，在Active-Directory服务器配置模式下，使用以下命令：
email-attribute string
l
string - 指定邮箱属性名称，默认为mail，取值范围是1-63个字符，不区分大小写。

<!-- 来源页 1221 -->
使用no email-attribute恢复邮箱属性名称的默认值。
启用/禁用SSL加密连接
开启SSL加密连接功能后，系统通过SSL加密方式连接Active Directory认证服务器，从而保证系统与
Active Directory认证服务器之间的数据传输安全。启用/禁用SSL加密连接功能，在Active-Directory服
务器配置模式下，使用以下命令：
connect-through-SSL {enable | disable}
l
enable | disable - 启用（enable）或者禁用（disable）SSL加密连接功能。
启用/禁用SSL证书校验
当防火墙通过SSL加密的方式连接Active Directory认证服务器时，需要将Active Directory服务器的证书
导入到防火墙系统进行验证。然而，有时用户可能无法获取服务器证书，导致无法使用SSL加密连接。为解
决该问题，系统允许用户配置是否启用SSL证书校验。如果禁用SSL证书校验，当防火墙通过SSL加密的方式
连接Active Directory认证服务器时，无需导入服务器证书也可以成功连接。
默认情况下，SSL证书校验功能为开启状态。启用/禁用SSL证书校验功能，在Active Directory服务器配置
模式下，使用以下命令：
verify-certificate {enable | disable}
l
enable | disable - 启用（enable）或者禁用（disable）SSL证书校验功能。
注意: 启用SSL加密连接功能后，SSL证书校验功能才会生效。
指定用户名格式
用户认证时，系统会根据配置的认证用户名格式，对用户名进行提取（不满足格式时，使用原始用户名）。
最终使用提取后的用户名进行认证。指定认证用户名格式，在Active-Directory服务器配置模式下，使用以
下命令：
extract-username-format authenticate { [domain\username ] [username@domain] }
删除认证用户名格式配置，在Active-Directory服务器配置模式下，使用以下命令：
no extract-username-format authenticate { [domain\username ] [username@domain] }
在基于用户/用户组进行策略控制时，系统会根据配置的用户名格式在本地存储的组织机构中查找用户名所属
的用户组。指定查找用户组时支持的用户名格式，在Active-Directory服务器配置模式下，使用以下命令：
extract-username-format search-usergroup { [domain\username ] [username@domain] }
删除查找用户组时的用户名格式配置，在Active-Directory服务器配置模式下，使用以下命令：
no extract-username-format search-usergroup { [domain\username ] [username@domain] }

<!-- 来源页 1222 -->
指定角色映射规则
为Active-Directory服务器指定角色映射规则后，系统将会为通过该服务器认证的用户按照指定角色映射规
则分配角色。为Active-Directory服务器指定角色映射规则，在Active-Directory服务器配置模式下，使
用以下命令：
role-mapping-rule rule-name
l
rule-name – 指定系统中已配置的映射规则的名称。
在Active-Directory服务器配置模式下，使用该命令no的形式取消角色映射规则的指定：
no role-mapping-rule
配置用户黑名单
为Active-Directory服务器配置用户黑名单后，系统将会禁止通过该服务器认证的黑名单用户访问任何网络
资源。配置用户黑名单，在Active-Directory服务器配置模式下，使用以下命令：
user-block-list username user-name
l
user-name – 指定黑名单中的用户名。取值范围是1到63个字符。
在Active-Directory服务器配置模式下，使用该命令no的形式删除黑名单用户：
no user-block-list username user-name
配置AD用户
用户可以为不同的AD服务器配置用户。创建AD用户，在Active-Directory服务器配置模式下，使用以下命
令：
user user-name
l
user-name – 指定用户名称。长度范围是1到63个字符。
执行该命令后，系统创建指定名称的用户并且进入用户配置模式；如果指定的用户名称已存在，则直接进入
用户配置模式。在Active-Directory服务器配置模式下，使用该命令no的形式删除指定用户：
no user user-name
指定用户有效期
超过有效期的用户不可以通过设备的认证，因此不可以在系统中继续使用。默认情况下，用户没有有效期限
制。指定用户的有效期，在用户配置模式下，使用以下命令：
expire Month/day/year HH:MM

<!-- 来源页 1223 -->
l
Month/day/year HH:MM – 指定用户有效期时间，格式为“月/日/年小时:分钟”。例如命令
expire 02/12/2022 12:00表示用户将在2022年2月12日的12：00过期。
在用户配置模式下使用该命令no的形式取消用户有效期配置：
no expire
配置用户同步功能
用户同步指的是完成Active-Directory服务器配置后，系统将认证服务器上的用户信息同步到本地的功能，
默认情况下系统每隔30分钟同步一次。
启用/禁用用户同步功能
在进行用户同步前，需要先启用用户同步功能。默认情况下，用户同步功能是启用的。启用或禁用用户同步
功能，在Active-Directory服务器配置模式下，使用以下命令：
l
启用：sync enable
l
禁用：sync disable
配置用户同步方式
系统支持多种用户同步方式，包括手动同步和自动同步。
手动同步
更新Active-Directory服务器连接，手动同步用户信息。在Active-Directory服务器配置模式下，使用以
下命令：
manual-sync
执行一次该命令即进行一次同步，如果同步过程中再次执行该命令，系统将清除原有用户同步信息，重新进
行同步。
自动同步
自动同步方式包括三种：按时间间隔同步、每天同步和一次性同步。配置自动同步方式，在ActiveDirectory服务器配置模式下，使用以下命令：
auto-sync {periodically interval | daily HH:MM | once}
l
interval – 指定为按时间间隔同步，并配置自动同步的间隔时间。取值范围为30到1440，单位为分钟，
默认值为30。
l
HH:MM – 指定为每天同步，并配置每天执行自动同步的时间点。HH和MM分别代表小时和分钟。

<!-- 来源页 1224 -->
l
once – 指定为一次性同步，当Active-Directory服务器配置信息有更改时，系统将会自动同步。首次
配置该命令后，系统会执行一次同步。
恢复默认自动同步方式，即每隔30分钟进行一次同步。在Active-Directory服务器配置模式下，使用以下命
令：
no auto-sync
指定用户名属性
指定用户名属性的值。当系统同步用户信息到本地时，可以通过该属性获取用户名；当系统进行用户认证
时，可以通过该属性来识别用户。在Active-Directory服务器配置模式下，使用以下命令来指定用户名属
性：
naming-attribute string
l
string – 指定用户名属性的值，为1到63个字符的字符串。该字符串通常为cn（Common Name）、
name或者sAMAccountName，默认值为sAMAccountName。
在Active-Directory服务配置模式下，使用该命令no的形式恢复默认情况：
no naming-attribute
指定组类别
指定用户组对象类别objectClass的值。当系统同步Active-Directory用户信息到本地时，会根据组类别对
用户信息进行过滤，符合条件的用户信息才会同步至系统。指定组类别，在Active-Directory服务器配置模
式下，使用以下命令：
group-class string
l
string – 指定用户组对象类别objectClass的值，为1到63个字符的字符串，默认值为group。
多次使用上述命令配置多个组类别。系统最多允许配置8个组类别，多个组类别之间为“或”的关系，即只
要满足一个组类别即可以同步至系统。
在Active-Directory服务配置模式下，使用no group-class string命令删除指定的组类别。删除所有的组
类别后，会恢复默认组类别。
指定用户类别
指定用户对象类别objectClass的值。当系统同步Active-Directory用户信息到本地时，会根据用户类别对
用户信息进行过滤，符合条件的用户信息才会同步至系统。指定用户类别，在Active-Directory服务器配置
模式下，使用以下命令：
user-class string

<!-- 来源页 1225 -->
l
string – 指定用户对象类别objectClass的值，为1到63个字符的字符串，默认值为person。
多次使用上述命令配置多个用户类别。系统最多允许配置8个用户类别，多个用户类别之间为“或”的关
系，即只要满足一个用户类别即可以同步至系统。
在Active-Directory服务配置模式下，使用no user-class string命令删除指定的用户类别。删除所有的用
户类别后，会恢复默认用户类别。
配置用户过滤功能
在配置Active-Directory服务器认证参数时，通过指定用户过滤条件，使得在同步Active-Directory服务
器上的用户时只有符合过滤条件的用户信息才被同步到设备中，或者只允许上述用户在登录时进行认证。配
置用户过滤功能，必须先进入AAA认证服务器配置模式。在全局配置模式下执行aaa-server aaa-servername type active-directory命令可以进入指定名称的Active-Directory服务器配置模式。
配置用户过滤功能，在Active-Directory服务器配置模式下，使用以下命令：
user-filter filter-string
l
filter-string – 指定用户过滤条件，为0到120个字符的字符串。例如，配置Active-Directory服务器
时，filter-string设置为“memberOf=CN=Admin,DC=test,DC=com”，表明只同步或认证DN为
“CN=Admin,DC=test,DC=com”的Group中的用户。
常用的操作符如下：
操作符
描述
=
相等
&
条件与
|
条件或
！
条件非
*
通配符，代替0个或多个字符
～=
类似（用于模糊查询）
>=
字典序大于等于
<=
字典序小于等于
注意:
l
Hillstone设备支持Active-Directory服务器支持的所有操作符。
l
如果用户输入的格式不符合Active-Directory服务器的规定，可能会导致用户同步或认证失
败。

<!-- 来源页 1226 -->
l
删除AAA服务器之前，请确保该服务器未被指定为备份认证服务器。
l
如果为同一Active-Directory服务器配置了备份服务器1（backup1）、备份服务器2
（backup2）和备份认证服务器（backup-aaa-server），当用户在主服务器认证无响应
时，系统会先通过备份服务器1和2进行认证，如果备份服务器1和2认证无响应，再通过备份认
证服务器对该用户再次进行认证；但当用户在主服务器、备份服务器1或者备份服务器2认证失
败时，系统会直接通过备份认证服务器对该用户再次进行认证。
在Active-Directory服务器配置模式下，使用no user-filter命令取消用户过滤功能，即同步所有的用户，
并且对所有的用户进行认证。
配置同步的工作模式
系统支持通过两种工作模式从Active-Directory服务器同步组织结构和用户信息到本地：按OU
(OrganizationUnit)同步和按Group同步，从而管理员可以通过OU和Group类型的用户组进行安全策略控
制。默认情况下，系统会按Group同步用户信息到本地。
配置用户同步的工作模式，在Active-Directory服务器配置模式下，使用以下命令：
sync-type {ou | group}
l
ou – 指定按OU组织结构同步用户到本地。
l
group – 指定按Group同步用户到本地。
如果以OU模式来同步用户信息，可以配置要同步的OU组织结构的最大深度。在Active-Directory服务器配
置模式下，使用以下命令：
sync-ou-depth depth-value
l
depth-value – 指定同步OU组织结构的最大深度。取值范围为1到12，默认值为12。超过最大深度的
OU组织结构不会被同步，但是超过最大深度的所有用户会被同步，并且被同步到其所属最大限制深度的
OU中。需要注意的是，如果各层级OU的名称总长度（包括“OU=”和标点符号）大于128个字符，那
么超过此长度的OU信息将不会被同步。
配置备份认证服务器
为Active-Directory服务器配置备份认证服务器后，当主服务器出现问题或者用户在主服务器认证失败时，
备份认证服务器发挥身份认证的作用。备份认证服务器可以与主服务器为不同类型。系统中已配置的本地、
Active-Directory、RADIUS或者LDAP服务器均可作为备份认证服务器。为Active-Directory服务器配置
备份认证服务器，在Active-Directory服务器配置模式下，使用以下命令：
backup-aaa-server aaa-server-name

<!-- 来源页 1227 -->
l
aaa-server-name – 指定系统中已经配置的AAA服务器的名称。
在Active-Directory服务器配置模式下，使用该命令no的形式取消备份认证服务器的配置：
no backup-aaa-server
注意:
l
备份认证服务器和主认证服务器必须处于相同VSYS。关于VSYS的详细信息，请参阅虚拟系
统。
l
备份认证服务器不能嵌套备份认证服务器。
l
删除AAA服务器之前，请确保该服务器未被指定为备份认证服务器。
l
如果为同一Active-Directory服务器配置了备份服务器1（backup1）、备份服务器2
（backup2）和备份认证服务器（backup-aaa-server），当用户在主服务器认证无响应
时，系统会按照这样的顺序对该用户再次进行认证：备份服务器1→备份服务器2→备份认证服
务器；当用户在主服务器认证失败时，系统会先通过备份服务器进行认证，如果备份服务器认
证失败再通过备份认证服务器对该用户再次进行认证。
配置仅同步Base-DN下用户组
在同步AD服务器用户时，可以根据需要，启用或禁用仅同步Base-DN下的用户组功能，在ActiveDirectory服务器配置模式下，使用以下命令：
l
启用：sync-group-under-basedn enable
l
禁用：no sync-group-under-basedn enable
配置防暴力破解功能
为了防止非法用户通过暴力方法获取用户名和密码，可以通过配置基于用户名或基于IP地址的防暴力破解功
能，即在指定时间内，若用户连续输错指定次数的用户名和密码，系统将会按照指定的锁定时间锁定该用户
或IP地址。防暴力破解功能的配置包括：
l 开启或关闭防暴力破解功能
l 配置尝试次数
l 配置锁定时间
l 查看锁定列表信息
l 解除用户/IP地址的锁定

<!-- 来源页 1228 -->
开启或关闭防暴力破解功能
防暴力破解功能默认情况下是关闭的。开启防暴力破解功能，请在Active-Directory服务器配置模式下使用
以下命令：
l
启用：lockout {ip | user} enable
l
关闭：lockout {ip | user} disable
配置尝试次数
配置尝试次数，即在指定时间内，允许用户连续输错用户名和密码的次数，请在Active-Directory服务器配
置模式下使用以下命令：
lockout {ip | user} failed-attempts number interval interval
l
failed-attempts number – 指定时间内允许输错用户名和密码的次数，基于用户名配置时，取值范围
是1-32，默认值是5次；基于IP地址配置时，取值范围是1-2048，默认值是64次。
l
interval interval – 指定连续输错用户名和密码的时间范围，单位是秒，取值范围是1-180秒，默认值
是60秒。
配置锁定时间
在指定时间内，若用户连续输错指定次数的用户名和密码，系统将会按照指定的锁定时间锁定该用户或IP地
址。配置锁定时间，请在Active-Directory服务器配置模式下使用以下命令：
lockout {ip | user} lockout-time time
l
lockout-time time – 指定锁定时间，单位是秒，取值范围是30-1800秒，基于用户名配置时，默认值
是600秒；基于IP地址配置时，默认值是60秒。
查看锁定列表信息
查看被锁定的用户信息、被锁定的IP地址信息，在任何模式下，使用以下命令：
show aaa-server aaa-server-name lockout {user [username] | ip [ip-address vr_id number]}
l
aaa-server-name - 指定AAA服务器名称。
l
user [username] - 查看指定名称的锁定用户信息。
l
ip [ip-addressvr_idnumber] - 查看指定IP地址和VRouter ID的锁定IP信息。

<!-- 来源页 1229 -->
解除用户/IP地址的锁定
解除对指定用户/IP地址的锁定并且从锁定列表中删除，在任何模式下，使用以下命令：
exec aaa aaa-serveraaa-server-namelockout delete {user [username] | ip [ip-addressvr_
idnumber]}
l
aaa-server-name - 指定AAA服务器名称。
l
user [username] - 解除对指定名称的用户的锁定。
l
ip [ip-addressvr_idnumber] - 解除对指定IP地址和VRouter ID的锁定。
启用/禁用简化认证功能
系统和Active-Directory服务器建立连接之前，需要进行连接认证。在连接认证的过程中，系统会首先发送
请求，查询Active-Directory服务器的加密方式，然后通过查询到的加密方式与服务器建立连接。某些场景
下，服务器会禁止响应加密方式的查询，导致系统和Active-Directory服务器的连接认证失败。为解决该问
题，系统支持简化认证功能，启用该功能后，系统会直接使用设备中配置的认证方式（通过命令行authmethod {plain | digest-md5}配置）与Active-Directory服务器进行连接，不再查询服务器的加密方
式。
默认情况下，简化认证功能为禁用状态。开启/禁用简化认证功能，在Active-Directory服务器配置模式
下，使用以下命令：
simplified-authentication {enable | disable}
l
enable - 开启简化认证功能。
l
disable - 禁用简化认证功能。
注意: 开启简化认证功能后，如果Active-Directory服务器与系统之间使用MD5摘要的方法进行认
证（通过命令行auth-method digest-md5 配置），用户需要指定认证服务器的域名（服务器系
统全名，例如“WIN-S3VE2GEH3CK.addomain.com”，而不是IP地址），并通过DNS获取域
名和IP地址之间的映射关系（建议配置DNS静态缓存，将认证服务器的域名映射到IP地址），才能
认证成功。
配置LDAP服务器认证参数
在全局配置模式下执行aaa-server aaa-server-name type ldap命令可以进入指定名称的LDAP服务器
配置模式。用户可配置的LDAP服务器认证参数包括：
l 配置认证主服务器的IP地址或域名
l 配置备份服务器1的IP地址或域名

<!-- 来源页 1230 -->
l 配置备份服务器2的IP地址或域名
l 配置服务器端口号
l 配置服务器认证或同步方法
l 指定Base-DN
l 指定同步Base-DN
l 指定同步对象
l 指定登录DN
l 指定Authid属性值
l 指定登录密码
l 启用/禁用SSL加密连接
l 启用/禁用SSL证书校验
l 指定用户名属性
l 指定用户组名称属性
l 指定组类别
l 指定用户类别
l 指定成员属性名
l 指定手机号码属性名称
l 指定邮箱属性名称
l 指定用户名格式
l 配置角色映射规则
l 配置用户黑名单
l 配置LDAP用户
l 指定用户有效期
l 配置用户同步功能
l 配置用户过滤功能
l 配置同步的工作模式
l 配置备份认证服务器
l 配置防暴力破解功能

<!-- 来源页 1231 -->
l 启用/禁用简化认证功能
配置认证主服务器的IP地址或域名
配置认证主服务器的IP地址或域名以及所属的VRouter，在LDAP服务器配置模式下，使用以下命令：
host {ip-address | host-name }[vrouter vrouter-name]
l
ip-address | host-name – 指定认证主服务器的IP地址（IPv4地址或IPv6地址）或者域名。
l
vrouter vrouter-name – 指定认证主服务器所属的VRouter。默认为系统缺省VR即trust-vr。
在LDAP服务器配置模式下，使用该命令no的形式取消认证主服务器的IP地址或者域名配置：
no host
配置备份服务器1的IP地址或域名
该参数为可选配置。备份服务器是与主服务器相同类型服务器。在当通过主服务器进行认证失败时，依次启
用备份服务器1和2进行认证。配置备份服务器1的IP地址或域名以及所属的VRouter，在LDAP服务器配置模
式下，使用以下命令：
backup1 {ip-address | host-name }[vrouter vrouter-name]
l
ip-address | host-name – 指定备份服务器1的IP地址（IPv4地址或IPv6地址）或者域名。
l
vrouter vrouter-name – 指定认证主服务器所属的VRouter。默认为系统缺省VR即trust-vr。
在LDAP服务器配置模式下，使用该命令no的形式取消备份服务器1的IP地址或者域名配置：
no backup1
配置备份服务器2的IP地址或域名
该参数为可选配置。备份服务器是与主服务器相同类型服务器。在当通过主服务器进行认证失败时，依次启
用备份服务器1和2进行认证。配置备份服务器2的IP地址或域名以及所属的VRouter，在LDAP服务器配置模
式下，使用以下命令：
backup2 {ip-address | host-name }[vrouter vrouter-name]
l
ip-address | host-name – 指定备份服务器2的IP地址（IPv4地址或IPv6地址）或者域名。
l
vrouter vrouter-name – 指定认证主服务器所属的VRouter。默认为系统缺省VR即trust-vr。
在LDAP服务器配置模式下，使用该命令no的形式取消备份服务器2的IP地址或者域名配置：
no backup2
配置服务器端口号
配置LDAP服务器端口号，在LDAP服务器配置模式下，使用以下命令：

<!-- 来源页 1232 -->
port port-number
l
port-number – 指定LDAP服务器的端口号。默认值是389。取值范围是1到65535。
在LDAP服务配置模式下，使用该命令no的形式恢复端口号的默认值：
no port
配置服务器认证或同步方法
LDAP服务器和系统之间可以使用明文和MD5摘要两种方法进行用户认证或用户同步。配置LDAP服务器认证
或同步方法，在LDAP服务器配置模式下，使用以下命令：
auth-method {plain | digest-md5}
l
plain – 指定使用明文的方法来认证或同步用户。
l
digest-md5 – 指定使用MD5摘要的方法来认证或同步用户。该方法为系统默认认证方法。
在LDAP服务配置模式下，使用该命令no的形式恢复默认认证或同步方法：
no auth-method
注意: 如果指定使用MD5摘要方法后没有配置Authid属性值，那么从服务器同步用户的过程中将
使用明文方法，认证用户的过程中将使用MD5摘要方法。
指定Base-DN
指定Base-DN，Base-DN是指当LDAP服务器收到一个认证请求时，目录查询的起始点。在LDAP服务器配
置模式下，使用以下命令：
base-dn string
l
string – 指定Base-DN的具体内容，如dc=hillstonenet。
在LDAP服务配置模式下，使用该命令no的形式取消Base-DN的指定：
no base-dn
指定认证Base-DN
Base-DN是指LDAP服务器目录查询的起始点。指定认证Base-DN后，该Base-DN路径下的所有用户（包
括用户组中的直属用户）将允许通过认证。指定认证Base-DN，在LDAP服务器配置模式下，使用以下命
令：
auth-base-dn string
l
string–指定认证Base-DN的具体内容，如OU=A，dc=hillstonenet，dc=com。

<!-- 来源页 1233 -->
在LDAP服务配置模式下，使用该命令no的形式取消认证Base-DN的指定：
no auth-base-dn
指定同步Base-DN
同步Base-DN是指系统从LDAP服务器同步用户和用户组时的路径起点。指定同步Base-DN后，该BaseDN路径下的所有用户及用户组将同步到本地。指定同步Base-DN，在LDAP服务器配置模式下，使用以下命
令：
sync-base-dn string
l
string – 指定同步Base-DN的具体内容，如OU=A，dc=hillstonenet，dc=com。
重复执行该命令可以配置多条需要同步的路径。
在LDAP服务配置模式下，使用该命令no的形式删除指定的同步Base-DN配置：
no sync-base-dn
指定同步对象
当指定了同步Base-DN后，该同步Base-DN路径下的所有用户及用户组将会同步到本地。若没有指定同步
Base-DN，则将Base-DN路径下的所有用户及用户组同步到本地。指定同步对象为用户或用户组后，筛选
同步到本地的信息并将指定对象的信息保留。指定同步对象，在LDAP服务器配置模式下，使用以下命令：
sync-object {user | group}
l
user–指定同步对象为用户，仅保留同步的用户信息。
l
group–指定同步对象为用户组，仅保留同步的用户组信息。
在LDAP服务配置模式下，使用该命令no的形式取消同步对象的指定：
no sync-object {user | group}
指定登录DN
如果使用明文方法来认证或同步用户，系统会使用登录DN和登录密码到服务器进行认证，从而能够连接服务
器进行用户认证或同步。指定登录DN（通常为LDAP服务器预设的具有查询权限的用户账号），在LDAP服
务器配置模式下，使用以下命令：
login-dn string
l
string – 指定登录DN的具体内容，为1到255个字符的字符串，不区分大小写。
在LDAP服务配置模式下，使用该命令no的形式取消登录DN的指定：
no login-dn

<!-- 来源页 1234 -->
指定Authid属性值
如果使用MD5摘要方法来认证或同步用户，系统会使用Authid属性值和登录密码到服务器进行认证，从而
能够连接服务器进行用户认证或同步。配置Authid属性值，在LDAP服务器配置模式下，使用以下命令：
login-dn authid string
l
string – 指定Authid的值，为1到63个字符的字符串，区分大小写。
在LDAP服务配置模式下，使用该命令no的形式取消Authid的指定：
no login-dn Authid
指定登录密码
指定登录密码，此处的登录密码即为登录DN所对应的密码。在LDAP服务器配置模式下，使用以下命令：
login-password string
l
string – 指定登录密码的具体内容。
在LDAP服务配置模式下，使用该命令no的形式取消登录密码的指定：
no login-password
指定用户名属性
指定用户名属性的值。当系统同步用户信息到本地时，可以通过该属性获取用户名；当系统进行用户认证
时，可以通过该属性来识别用户。在LDAP服务器配置模式下，使用以下命令来指定用户名属性：
naming-attribute string
l
string – 指定用户名属性的值，为1到63个字符的字符串。该字符串通常为uid（User ID）或cn
（Common Name），默认值为uid。
在LDAP服务配置模式下，使用该命令no的形式恢复默认情况：
no naming-attribute
启用/禁用SSL加密连接
开启SSL加密连接功能后，系统通过SSL加密方式连接LDAP认证服务器，从而保证系统与LDAP认证服务器
之间的数据传输安全。启用/禁用SSL加密连接功能，在LDAP服务器配置模式下，使用以下命令：
connect-through-SSL {enable | disable}
l
enable | disable - 启用（enable）或者禁用（disable）SSL加密连接功能。

<!-- 来源页 1235 -->
启用/禁用SSL证书校验
当防火墙通过SSL加密的方式连接LDAP认证服务器时，需要将LDAP服务器的证书导入到防火墙系统进行验
证。然而，有时用户可能无法获取服务器证书，导致无法使用SSL加密连接。为解决该问题，系统允许用户
配置是否启用SSL证书校验。如果禁用SSL证书校验，当防火墙通过SSL加密的方式连接LDAP认证服务器
时，无需导入服务器证书也可以成功连接。
默认情况下，SSL证书校验功能为开启状态。启用/禁用SSL证书校验功能，在LDAP服务器配置模式下，使
用以下命令：
verify-certificate {enable | disable}
l
enable | disable - 启用（enable）或者禁用（disable）SSL证书校验功能。
注意: 启用SSL加密连接功能后，SSL证书校验功能才会生效。
指定用户组名称属性
指定用户组名称属性的值。当系统同步用户信息到本地时，可以通过该属性获取用户组；当系统进行用户认
证时，可以通过该属性来识别用户组。在LDAP服务器配置模式下，使用以下命令来指定用户组名称属性：
group-naming-attribute string
l
string – 指定用户组名称属性的值，为1到63个字符的字符串。该字符串通常为uid（User ID）或cn
（Common Name），默认值为uid。
在LDAP服务配置模式下，使用该命令no的形式恢复默认情况：
no group-naming-attribute
指定组类别
指定用户组对象类别objectClass的值。当系统同步LDAP用户信息到本地时，会根据组类别对用户信息进行
过滤，符合条件的用户信息才会同步至系统。指定组类别，在LDAP服务器配置模式下，使用以下命令：
group-class string
l
string – 指定用户组对象类别objectClass的值，为1到63个字符的字符串，默认值为
groupOfUniqueNames。
多次使用上述命令配置多个组类别。系统最多允许配置8个组类别，多个组类别之间为“或”的关系，即只
要满足一个组类别即可以同步至系统。
在LDAP服务配置模式下，使用no group-class string命令删除指定的组类别。删除所有的组类别后，会
恢复默认组类别。

<!-- 来源页 1236 -->
指定用户类别
指定用户对象类别objectClass的值。当系统同步LDAP用户信息到本地时，会根据用户类别对用户信息进行
过滤，符合条件的用户信息才会同步至系统。指定用户类别，在LDAP服务器配置模式下，使用以下命令：
user-class string
l
string – 指定用户对象类别objectClass的值，为1到63个字符的字符串，默认值为inetOrgPerson、
uidObject或者person。
多次使用上述命令配置多个用户类别。系统最多允许配置8个用户类别，多个用户类别之间为“或”的关
系，即只要满足一个用户类别即可以同步至系统。
在LDAP服务配置模式下，使用no user-class string命令删除指定的用户类别。删除所有的用户类别后，
会恢复默认用户类别。
指定成员属性名
指定组对象中成员属性的名称，在LDAP服务器配置模式下，使用以下命令：
member-attribute string
l
string – 指定成员属性名的具体内容，为1到63个字符的字符串，默认值为uniqueMember。
在LDAP服务配置模式下，使用该命令no的形式恢复默认情况：
no member-attribute
指定手机号码属性名称
指定用户的手机号码属性名称，系统可以通过该属性获取用户的手机号码，用于短信口令二次认证场景。例
如，在SSL VPN短信口令认证场景中，系统可以通过该属性获取用户的手机号码。当用户登录SSL VPN时，
系统会将短信验证码发送至该号码。指定手机号码属性名称，在LDAP服务器配置模式下，使用以下命令：
mobile-attribute string
l
string - 指定手机号码属性名称，默认为mobile，取值范围是1-63个字符，不区分大小写。
使用no mobile-attribute恢复手机号码属性名称的默认值。
指定邮箱属性名称
指定用户的邮箱属性名称，系统可以通过该属性获取用户的邮箱地址，用于邮箱口令二次认证场景。例如，
在SSL VPN邮箱口令认证场景中，系统可以通过该属性获取用户的邮箱地址，当用户登录SSL VPN时，系统
会将验证码发送至该邮箱。指定邮箱属性名称，在LDAP服务器配置模式下，使用以下命令：
email-attribute string

<!-- 来源页 1237 -->
l
string - 指定邮箱属性名称，默认为mail，取值范围是1-63个字符，不区分大小写。
使用no email-attribute恢复邮箱属性名称的默认值。
指定用户名格式
用户认证时，系统会根据配置的认证用户名格式，对用户名进行提取（不满足格式时，使用原始用户名）。
最终使用提取后的用户名进行认证。指定认证用户名格式，在LDAP服务器配置模式下，使用以下命令：
extract-username-format authenticate { [domain\username ] [ username@domain] }
删除认证用户名格式配置，在LDAP服务器配置模式下，使用以下命令：
no extract-username-format authenticate { [domain\username ] [username@domain] }
在基于用户/用户组进行策略控制时，系统会根据配置的用户名格式在本地存储的组织机构中查找用户名所属
的用户组。指定查找用户组时支持的用户名格式，在LDAP服务器配置模式下，使用以下命令：
extract-username-format search-usergroup { [domain\username ] [ username@domain] }
删除查找用户组时的用户名格式配置，在LDAP服务器配置模式下，使用以下命令：
no extract-username-format search-usergroup { [domain\username ] [username@domain] }
指定角色映射规则
为LDAP服务器指定角色映射规则后，系统将会为通过该服务器认证的用户按照指定角色映射规则分配角
色。为LDAP服务器指定角色映射规则，在LDAP服务器配置模式下，使用以下命令：
role-mapping-rule rule-name
l
rule-name – 指定系统中已配置的映射规则的名称。
在LDAP服务器配置模式下，使用该命令no的形式取消角色映射规则的指定：
no role-mapping-rule
配置用户黑名单
为LDAP服务器配置用户黑名单后，系统将会禁止通过该服务器认证的黑名单用户访问任何网络资源。配置
用户黑名单，在LDAP服务器配置模式下，使用以下命令：
user-block-list username user-name
l
user-name – 指定黑名单中的用户名。取值范围是1到63个字符。
在LDAP服务器配置模式下，使用该命令no的形式删除黑名单用户：
no user-block-list username user-name

<!-- 来源页 1238 -->
配置LDAP用户
用户可以为不同的LDAP服务器配置用户。创建LDAP用户，在LDAP服务器配置模式下，使用以下命令：
user user-name
l
user-name – 指定用户名称。长度范围是1到63个字符。
执行该命令后，系统创建指定名称的用户并且进入用户配置模式；如果指定的用户名称已存在，则直接进入
用户配置模式。在LDAP服务器配置模式下，使用该命令no的形式删除指定用户：
no user user-name
指定用户有效期
超过有效期的用户不可以通过设备的认证，因此不可以在系统中继续使用。默认情况下，用户没有有效期限
制。指定用户的有效期，在用户配置模式下，使用以下命令：
expire Month/day/year HH:MM
l
Month/day/year HH:MM – 指定用户有效期时间，格式为“月/日/年小时:分钟”。例如命令
expire 02/12/2022 12:00表示用户将在2022年2月12日的12：00过期。
在用户配置模式下使用该命令no的形式取消用户有效期配置：
no expire
配置用户同步功能
用户同步指的是完成LDAP服务器配置后，系统将认证服务器上的用户信息同步到本地的功能，默认情况下
系统每隔30分钟同步一次。
启用/禁用用户同步功能
在进行用户同步前，需要先启用用户同步功能。默认情况下，用户同步功能是启用的。启用或禁用用户同步
功能，在LDAP服务器配置模式下，使用以下命令：
l
启用：sync enable
l
禁用：sync disable
配置用户同步方式
系统支持多种用户同步方式，包括手动同步和自动同步。
手动同步
更新LDAP服务器连接，手动同步用户信息。在LDAP服务器配置模式下，使用以下命令：

<!-- 来源页 1239 -->
manual-sync
执行一次该命令即进行一次同步，如果同步过程中再次执行该命令，系统将清除原有用户同步信息，重新进
行同步。
自动同步
自动同步方式包括三种：按时间间隔同步、每天同步和一次性同步。配置自动同步方式，在LDAP服务器配
置模式下，使用以下命令：
auto-sync {periodically interval | daily HH:MM | once}
l
interval – 指定为按时间间隔同步，并配置自动同步的间隔时间。取值范围为30到1440，单位为分钟，
默认值为30。
l
HH:MM – 指定为每天同步，并配置每天执行自动同步的时间点。HH和MM分别代表小时和分钟。
l
once – 指定为一次性同步，当LDAP服务器配置信息有更改时，系统将会自动同步。首次配置该命令
后，系统会执行一次同步。
恢复默认自动同步方式，即每隔30分钟进行一次同步。在LDAP服务器配置模式下，使用以下命令：
no auto-sync
配置用户过滤功能
在配置LDAP服务器认证参数时，通过指定用户过滤条件，使得在同步LDAP服务器上的用户时只有符合过滤
条件的用户信息才被同步到设备中，或者只允许上述用户在登录时进行认证。配置用户过滤功能，必须先进
入AAA认证服务器配置模式。在全局配置模式下执行aaa-server aaa-server-name type ldap命令可以
进入指定名称的LDAP服务器配置模式。
配置用户过滤功能，在LDAP服务器配置模式下，使用以下命令：
user-filter filter-string
l
filter-string – 指定用户过滤条件，为0到120个字符的字符串。例如，配置LDAP服务器时，filterstring设置为“（|（objectclass=inetOrgperson）（objectclass=person））”，表明只同步或
认证所有被定义为inetOrgperson或者person的用户。
常用的操作符如下：
操作符
描述
=
相等
&
条件与
|
条件或

<!-- 来源页 1240 -->
操作符
描述
！
条件非
*
通配符，代替0个或多个字符
～=
类似（用于模糊查询）
>=
字典序大于等于
<=
字典序小于等于
注意:
l
Hillstone设备支持LDAP服务器支持的所有操作符。
l
如果用户输入的格式不符合LDAP服务器的规定，可能会导致用户同步或认证失败。
在LDAP服务器配置模式下，使用no user-filter命令取消用户过滤功能，即同步所有的用户，并且对所有的
用户进行认证。
配置同步的工作模式
系统支持通过两种工作模式从LDAP服务器同步组织结构和用户信息到本地：按OU(OrganizationUnit)同
步和按Group同步，从而管理员可以通过OU和Group类型的用户组进行安全策略控制。默认情况下，系统
会按Group同步用户信息到本地。
配置用户同步的工作模式，在LDAP服务器配置模式下，使用以下命令：
sync-type {ou | group}
l
ou – 指定按OU组织结构同步用户到本地。
l
group – 指定按Group同步用户到本地。
如果以OU模式来同步用户信息，可以配置要同步的OU组织结构的最大深度。在LDAP服务器配置模式下，
使用以下命令：
sync-ou-depth depth-value
l
depth-value – 指定同步OU组织结构的最大深度。取值范围为1到12，默认值为12。超过最大深度的
OU组织结构不会被同步，但是超过最大深度的所有用户会被同步，并且被同步到其所属最大限制深度的
OU中。需要注意的是，如果各层级OU的名称总长度（包括“OU=”和标点符号）大于128个字符，那
么超过此长度的OU信息将不会被同步。

<!-- 来源页 1241 -->
配置备份认证服务器
为LDAP服务器配置备份认证服务器后，当主服务器出现问题或者用户在主服务器认证失败时，备份认证服
务器发挥身份认证的作用。备份认证服务器可以与主服务器为不同类型。系统中已配置的本地、ActiveDirectory、RADIUS或者LDAP服务器均可作为备份认证服务器。为LDAP服务器配置备份认证服务器，在
LDAP服务器配置模式下，使用以下命令：
backup-aaa-server aaa-server-name
l
aaa-server-name – 指定系统中已经配置的AAA服务器的名称。
在LDAP服务器配置模式下，使用该命令no的形式取消备份认证服务器的配置：
no backup-aaa-server
注意:
l
备份认证服务器和主认证服务器必须处于相同VSYS。关于VSYS的详细信息，请参阅虚拟系统
章节。
l
备份认证服务器不能嵌套备份认证服务器。
l
删除AAA服务器之前，请确保该服务器未被指定为备份认证服务器。
l
如果为同一LDAP服务器配置了备份服务器1（backup1）、备份服务器2（backup2）和备份
认证服务器（backup-aaa-server），当用户在主服务器认证无响应时，系统会按照这样的
顺序对该用户再次进行认证：备份服务器1→备份服务器2→备份认证服务器；当用户在主服务
器认证失败时，系统会先通过备份服务器进行认证，如果备份服务器认证失败再通过备份认证
服务器对该用户再次进行认证
配置防暴力破解功能
为了防止非法用户通过暴力方法获取用户名和密码，可以通过配置基于用户名或基于IP地址的防暴力破解功
能，即在指定时间内，若用户连续输错指定次数的用户名和密码，系统将会按照指定的锁定时间锁定该用户
或IP地址。防暴力破解功能的配置包括：
l 开启或关闭防暴力破解功能
l 配置尝试次数
l 配置锁定时间
开启或关闭防暴力破解功能
防暴力破解功能默认情况下是关闭的。开启防暴力破解功能，请在LDAP服务器配置模式下使用以下命令：

<!-- 来源页 1242 -->
l
启用：lockout {ip | user} enable
l
关闭：lockout {ip | user} disable
配置尝试次数
配置尝试次数，即在指定时间内，允许用户连续输错用户名和密码的次数，请在LDAP服务器配置模式下使
用以下命令：
lockout {ip | user} failed-attempts number interval interval
l
failed-attempts number – 指定时间内允许输错用户名和密码的次数，基于用户名配置时，取值范围
是1-32，默认值是5次；基于IP地址配置时，取值范围是1-2048，默认值是64次。
l
interval interval – 指定连续输错用户名和密码的时间范围，单位是秒，取值范围是1-180秒，默认值
是60秒。
配置锁定时间
在指定时间内，若用户连续输错指定次数的用户名和密码，系统将会按照指定的锁定时间锁定该用户或IP地
址。配置锁定时间，请在LDAP服务器配置模式下使用以下命令：
lockout {ip | user} lockout-time time
l
lockout-time time – 指定锁定时间，单位是秒，取值范围是30-1800秒，基于用户名配置时，默认值
是600秒；基于IP地址配置时，默认值是60秒。
查看锁定列表信息
查看被锁定的用户信息、被锁定的IP地址信息，在任何模式下，使用以下命令：
show aaa-serveraaa-server-namelockout {user [username] | ip [ip-addressvr_idnumber]}
l
aaa-server-name - 指定AAA服务器名称。
l
user [username] - 查看指定名称的锁定用户信息。
l
ip [ip-addressvr_idnumber] - 查看指定IP地址和VRouter ID的锁定IP信息。
解除用户/IP地址的锁定
解除对指定用户/IP地址的锁定并且从锁定列表中删除，在任何模式下，使用以下命令：
exec aaa aaa-serveraaa-server-namelockout delete {user [username] | ip [ip-addressvr_
idnumber]}

<!-- 来源页 1243 -->
l
aaa-server-name - 指定AAA服务器名称。
l
user [username] - 解除对指定名称的用户的锁定。
l
ip [ip-addressvr_idnumber] - 解除对指定IP地址和VRouter ID的锁定。
启用/禁用简化认证功能
系统和LDAP服务器建立连接之前，需要进行连接认证。在连接认证的过程中，系统会首先发送请求，查询
LDAP服务器的加密方式，然后通过查询到的加密方式与服务器建立连接。某些场景下，服务器会禁止响应
加密方式的查询，导致系统和LDAP服务器的连接认证失败。为解决该问题，系统支持简化认证功能，启用
该功能后，系统会直接使用设备中配置的认证方式（通过命令行auth-method {plain | digest-md5}配
置）与LDAP服务器进行连接，不再查询服务器的加密方式。
默认情况下，简化认证功能为禁用状态。开启/禁用简化认证功能，在LDAP服务器配置模式下，使用以下命
令：
simplified-authentication {enable | disable}
l
enable - 开启简化认证功能。
l
disable - 禁用简化认证功能。
配置TACACS+服务器认证参数
在全局配置模式下执行aaa-server aaa-server-name type tacacs+命令可以进入指定名称的TACACS+
服务器配置模式。用户可配置的TACACS+服务器认证参数包括：
l 配置认证主服务器的IP地址或域名
l 配置备份服务器1的IP地址或域名
l 配置备份服务器2的IP地址或域名
l 配置TACACS+服务器端口号
l 配置TACACS+服务器的共享密钥
l 指定用户名格式
l 配置角色映射规则
l 配置防暴力破解功能
l 配置命令行授权功能
l 开启/关闭命令行审计功能
配置认证主服务器的IP地址或域名
配置认证主服务器的IP地址或域名以及所属的VRouter，在TACACS+服务器配置模式下，使用以下命令：

<!-- 来源页 1244 -->
host {ipv4-address | ipv6-address | host-name} [vrouter vrouter-name]
l
ipv4-address | ipv6-address | host-name – 指定认证主服务器的IPv4地址、IPv6地址或者域名。
l
vrouter vrouter-name – 指定认证主服务器所属的VRouter。默认为系统缺省VR即trust-vr。
在TACACS+服务器配置模式下，使用该命令no的形式取消认证主服务器的IP地址或者域名配置：
no host
配置备份服务器1的IP地址或域名
该参数为可选配置。备份服务器是与主服务器相同类型服务器。在当通过主服务器进行认证失败时，依次启
用备份服务器1和2进行认证。配置备份服务器1的IP地址或域名以及所属的VRouter，在TACACS+服务器配
置模式下，使用以下命令：
backup1 {ipv4-address | ipv6-address | host-name} [vrouter vrouter-name]
l
ipv4-address | ipv6-address | host-name – 指定备份服务器1的IPv4地址、IPv6地址或者域名。
l
vrouter vrouter-name – 指定备份服务器1所属的VRouter。默认为系统缺省VR即trust-vr。
在TACACS+服务器配置模式下，使用该命令no的形式取消备份服务器1的IP地址或者域名配置：
no backup1
配置备份服务器2的IP地址或域名
该参数为可选配置。备份服务器是与主服务器相同类型服务器。在当通过主服务器进行认证失败时，依次启
用备份服务器1和2进行认证。配置备份服务器2的IP地址或域名以及所属的VRouter，在TACACS+服务器配
置模式下，使用以下命令：
backup2 {ipv4-address | ipv6-address | host-name} [vrouter vrouter-name]
l
ipv4-address | ipv6-address | host-name – 指定备份服务器2的IPv4地址、IPv6地址或者域名。
l
vrouter vrouter-name – 指定备份服务器2所属的VRouter。默认为系统缺省VR即trust-vr。
在TACACS+服务器配置模式下，使用该命令no的形式取消备份服务器2的IP地址或者域名配置：
no backup2
配置TACACS+服务器端口号
配置TACACS+服务器端口号，在TACACS+服务器配置模式下，使用以下命令：
port port-number
l
port-number – 指定TACACS+服务器的端口号。默认值是49。
在TACACS+服务器配置模式下，使用该命令no的形式恢复端口号的默认值：

<!-- 来源页 1245 -->
no port
配置TACACS+服务器的共享密钥
配置TACACS+服务器的共享密钥，在TACACS+服务器配置下，使用以下命令：
secret secret
l
secret – 指定TACACS+服务器的共享密钥字符串。字符串范围为1到31个字符。
在TACACS+服务器配置模式下，使用该命令no的形式取消对TACACS+服务器共享密钥的配置：
no secret
指定用户名格式
用户认证时，系统会根据配置的认证用户名格式，对用户名进行提取（不满足格式时，使用原始用户名）。
最终使用提取后的用户名进行认证。指定认证用户名格式，在TACACS+服务器配置模式下，使用以下命令：
extract-username-format authenticate { [domain\username ] [ username@domain] }
删除认证用户名格式配置，在TACACS+服务器配置模式下，使用以下命令：
no extract-username-format authenticate { [domain\username ] [username@domain] }
在基于用户/用户组进行策略控制时，系统会根据配置的用户名格式在本地存储的组织机构中查找用户名所属
的用户组。指定查找用户组时支持的用户名格式，在TACACS+服务器配置模式下，使用以下命令：
extract-username-format search-usergroup { [domain\username ] [ username@domain] }
删除查找用户组时的用户名格式配置，在TACACS+服务器配置模式下，使用以下命令：
no extract-username-format search-usergroup { [domain\username ] [username@domain] }
指定角色映射规则
为TACACS+服务器指定角色映射规则后，系统将会为通过该服务器认证的用户按照指定角色映射规则分配角
色。为TACACS+服务器指定角色映射规则，在TACACS+服务器配置模式下，使用以下命令：
role-mapping-rule rule-name
l
rule-name – 指定系统中已配置的映射规则的名称。
在TACACS+服务器配置模式下，使用该命令no的形式取消角色映射规则的指定：
no role-mapping-rule
配置TACACS+服务器
通过山石设备与TACACS+服务器通信实现认证，需要在TACACS+服务器端修改自定义属性。
目前支持的TACACS+服务器的版本为：

<!-- 来源页 1246 -->
l Linux系统的tac_plus
在服务器上修改tac_plus配置文件，增加hillstone相关的字段，见下表。
l 思科的acs 4.2及以上版本
新建名为hillstone的服务，并自定义服务的属性，添加hillstone相关的字段，见下表。
属性
说明
user-type
用户类型。
admin type=16
all=31
其他类型用户不检查此值。
user-vsys-id
vSYS ID值。
管理员必须配置此参数。目前仅支持ID等于0。
user-admin-privilege
读写权限。
读写=4294967295
只读=0
user-admin-role
管理员角色的权限。
admin=系统管理员，拥有读、执行和写权限，可以在任何模式下对设备所有功
能模块进行配置，可查看当前或者历史配置信息。
operator=系统操作员，拥有读、执行和部分写权限，可以修改除管理员配置以
外的其他功能模块配置，可查看当前或者历史配置信息，但是不能查看日志信
息。
auditor=系统审计员，只可以对日志信息进行操作，包括查看、导出和清除。
admin-read-only＝系统管理员（只读），拥有读和部分执行权限，可查看当
前或者历史配置信息。
注意:
该属性优先级高于user-admin-privilege，如果二者同时配置，user-adminrole生效。建议用户直接使用user-admin-role字段。
user-login-type
管理员登录类型。
telnet＝2
SSH＝4
CONSOLE＝1
HTTP＝8
HTTPS＝16
all＝31
任意组合等于数值相加的值（如telnet+SSH＝6）。
user-group
此项为可选项，指定user所属的user-group，便于在设备上进行基于usergroup的策略控制。

<!-- 来源页 1247 -->
配置防暴力破解功能
为了防止非法用户通过暴力方法获取用户名和密码，可以通过配置基于用户名或基于IP地址的防暴力破解功
能，即在指定时间内，若用户连续输错指定次数的用户名和密码，系统将会按照指定的锁定时间锁定该用户
或IP地址。防暴力破解功能的配置包括：
l 开启或关闭防暴力破解功能
l 配置尝试次数
l 配置锁定时间
开启或关闭防暴力破解功能
防暴力破解功能默认情况下是关闭的。开启防暴力破解功能，请在TACACS+服务器配置模式下使用以下命
令：
l
启用：lockout {ip | user} enable
l
关闭：lockout {ip | user} disable
配置尝试次数
配置尝试次数，即在指定时间内，允许用户连续输错用户名和密码的次数，请在TACACS+服务器配置模式下
使用以下命令：
lockout {ip | user} failed-attempts number interval interval
l
failed-attempts number – 指定时间内允许输错用户名和密码的次数，基于用户名配置时，取值范围
是1-32，默认值是5次；基于IP地址配置时，取值范围是1-2048，默认值是64次。
l
interval interval – 指定连续输错用户名和密码的时间范围，单位是秒，取值范围是1-180秒，默认值
是60秒。
配置锁定时间
在指定时间内，若用户连续输错指定次数的用户名和密码，系统将会按照指定的锁定时间锁定该用户或IP地
址。配置锁定时间，请在TACACS+服务器配置模式下使用以下命令：
lockout {ip | user} lockout-time time
l
lockout-time time – 指定锁定时间，单位是秒，取值范围是30-1800秒，基于用户名配置时，默认值
是600秒；基于IP地址配置时，默认值是60秒。

<!-- 来源页 1248 -->
查看锁定列表信息
查看被锁定的用户信息、被锁定的IP地址信息，在任何模式下，使用以下命令：
show aaa-server aaa-server-name lockout {user [username] | ip [ip-address vr_id number]}
l
aaa-server-name - 指定AAA服务器名称。
l
user [username] - 查看指定名称的锁定用户信息。
l
ip [ip-address vr_id number] - 查看指定IP地址和VRouter ID的锁定IP信息。
解除用户/IP地址的锁定
解除对指定用户/IP地址的锁定并且从锁定列表中删除，在任何模式下，使用以下命令：
exec aaa aaa-server aaa-server-name lockout delete {user [username] | ip [ip-address vr_id
number]}
l
aaa-server-name - 指定AAA服务器名称。
l
user [username] - 解除对指定名称的用户的锁定。
l
ip [ip-address vr_id number] - 解除对指定IP地址和VRouter ID的锁定。
配置命令行授权功能
为了提高命令行操作的安全性，加强对用户操作的限制，可以配置命令行授权功能。开启该功能后，对于通
过TACACS+服务器认证登录的用户，其输入的每一条命令都需要对应的TACACS+服务器进行授权。只有
TACACS+服务器授权通过，命令才可以被执行，否则不能执行该命令。命令行授权功能的配置包括：
l 开启/关闭命令行授权功能
l 配置逃生模式时间
开启/关闭命令行授权功能
命令行授权功能默认为关闭状态。开启/关闭命令行授权功能，在TACACS+服务器配置模式下，使用以下命
令：
l
开启：authentication-cmd enable
l
关闭：no authentication-cmd enable

<!-- 来源页 1249 -->
配置逃生模式时间
当TACACS+服务器因网络问题、服务器故障或其他原因无法响应授权请求时，系统进入逃生模式。在此模式
下，系统会设置一个计时器（逃生模式时间），从用户首次尝试执行命令且服务器不可达的那一刻开始计
时。用户输入的命令在逃生模式时间内无需经过TACACS+服务器的授权即可直接执行，从而避免因授权服务
中断而导致的操作停滞。逃生模式时间耗尽后系统会恢复正常授权流程，若服务器仍不可达则重新进入逃生
模式，直至服务器恢复或问题解决。
配置逃生模式时间，在TACACS+服务器配置模式下，使用以下命令：
authentication-cmd-escape-mode-time time
l
time – 指定逃生模式时间，取值范围是0-3600秒，默认值是0秒，表示关闭逃生模式。
开启/关闭命令行审计功能
注意: 命令行审计功能只对通过TACACS+服务器认证登录的用户生效。
用户在使用命令行对设备进行配置时，可能会因为错误的操作引起网络故障。开启命令行审计功能后，系统
会将用户执行的命令信息发送到对应的TACACS+服务器，用户可以通过查看这些命令信息来帮助定位网络故
障。默认情况下，该功能为关闭状态。
开启/关闭命令行审计功能，在TACACS+服务器配置模式下，使用以下命令：
l
开启：accounting-cmd enable
l
关闭：no accounting-cmd enable
配置OAuth2服务器认证参数
在全局配置模式下执行aaa-server aaa-server-name type oauth命令可以进入指定名称的OAuth2服
务器配置模式。用户需要按如下步骤进行OAuth2服务器认证参数配置：
1. OAuth2服务器基础配置
2. OAuth2服务器授权码请求配置
3. OAuth2服务器访问令牌请求配置
4. OAuth2服务器用户信息请求配置
注意:
l
整机下最多配置5个OAuth2服务器，单个VSYS下最多配置3个OAuth2服务器。

<!-- 来源页 1250 -->
OAuth2服务器基础配置
当使用OAuth2服务器进行认证时，用户需要指定组织来源服务器、虚拟路由器以及用户认证页面中
OAuth2认证图标的提示信息。
指定组织来源服务器
指定认证用户所属的组织来源服务器，在OAuth服务器配置模式下，使用以下命令：
organization-source aaa-server-name
l
aaa-server-name – 指定选择认证用户所属的AAA服务器。系统支持选择已配置的Local、AD或者
LDAP类型的服务器。选择AAA服务器后，系统可以在引用的AAA服务器上查询在线用户的用户名对应的
用户组和角色信息，从而实现基于用户组和角色的策略控制。
在OAuth服务器配置模式下使用该命令no的形式取消对组织来源服务器的指定：
no organization-source
指定OAuth2服务器所属的虚拟路由器
指定OAuth2服务器所属的虚拟路由器，在OAuth服务器配置模式下，使用以下命令：
vrouter vrouter-name
l
aaa-server-name – 指定认证服务器所属的虚拟路由器（VRouter）。
在OAuth服务器配置模式下使用该命令no的形式取消对虚拟路由器的指定：
no vrouter
指定OAuth2认证图标的名称
指定OAuth2认证图标的名称，在OAuth服务器配置模式下，使用以下命令：
authentication-icon-name name
l
name – 指定OAuth2认证图标的名称。在用户认证页面中，当用户将鼠标悬浮在认证图标上时，显示
OAuth2服务器的提示信息。例如：提示“使用山石用户中心认证”。
在OAuth服务器配置模式下使用该命令no的形式取消对OAuth2认证图标的名称的指定：
no authentication-icon-name
OAuth2服务器授权码请求配置
当使用OAuth2服务器进行认证时，用户需要配置授权码请求相关的内容，包括授权码请求的OAuth2服务器
地址、请求参数、响应参数。

<!-- 来源页 1251 -->
进入授权码请求配置模式
对于授权码请求的OAuth2服务器地址、请求参数、响应参数，都需要在授权码请求配置模式下进行。进入
授权码请求配置模式，在OAuth服务器配置模式，使用以下命令：
authorization-code-request
配置授权码请求的OAuth2服务器地址
配置授权码请求的OAuth2服务器地址，在授权码请求配置模式下，使用以下命令：
request-url request-url
l
request-url – 指定系统请求授权码的认证服务器地址。如
https://passport.hillsonenet.com/OAuth/Authorize。
在授权码请求配置模式下使用该命令no的形式取消对授权码请求的OAuth2服务器地址的指定：
no request-url
配置授权码请求的请求url参数
用户最多可以配置16个请求url参数。配置系统申请授权码的请求url参数，在授权码请求配置模式下，使用
以下命令：
request-parameter name value
l
name – 指定请求url参数的参数名称。取值范围为1-31个字符。
l
value – 指定请求url参数的参数值。取值范围为1-511个字符。
在授权码请求配置模式下使用该命令no的形式取消配置系统申请授权码的请求url参数：
no request-parameter name
配置授权码响应参数
配置系统申请授权码的响应参数，包括参数名称和本地变量。授权码请求成功后，需要解析响应报文中的指
定参数字段并保存到本地变量中，用于下一步的访问令牌请求。最多可以配置5个响应参数。
配置授权码响应参数，在授权码请求配置模式下，使用以下命令：
response-parameter attribute_name mapping local_value
l
attribute_name – 指定授权码响应参数中的参数名称。取值范围为1-31个字符。
l
local_value – 指定授权码响应参数中的本地变量。取值范围为1-31个字符。
在授权码请求配置模式下使用该命令no的形式取消对授权码响应参数的指定：

<!-- 来源页 1252 -->
no response-parameter attribute_name
OAuth2服务器访问令牌请求配置
当使用OAuth2服务器进行认证时，用户需要配置访问令牌请求相关的内容，包括访问令牌请求的OAuth2服
务器地址、请求参数、响应参数。
进入访问令牌请求配置模式
对于访问令牌请求的OAuth2服务器地址、请求参数、响应参数，都需要在访问令牌请求配置模式下进行。
进入访问令牌请求配置模式，在OAuth服务器配置模式，使用以下命令：
access-token-request
开启/关闭请求访问令牌功能
请求访问令牌功能默认为开启状态。开启/关闭请求访问令牌功能，在访问令牌请求配置模式下，使用以下命
令：
l
开启：enable
l
关闭：disable
配置访问令牌请求的OAuth2服务器地址
配置访问令牌请求的OAuth2服务器地址，在访问令牌请求配置模式下，使用以下命令：
request-url request-url
l
request-url – 指定系统请求访问令牌的认证服务器地址。如
https://passort.hillstonenet.com/OAuth/Token。
在访问令牌请求配置模式下使用该命令no的形式取消对访问令牌请求的OAuth2服务器地址的指定：
no request-url
配置访问令牌请求的请求方法
配置访问令牌请求的请求方法，在访问令牌请求配置模式下，使用以下命令：
request-type {get | post}
l
get – 指定请求方法为“GET”。默认为“GET”。
l
post – 指定请求方法为“POST”。
在访问令牌请求配置模式下使用该命令no的形式恢复默认的请求方法：

<!-- 来源页 1253 -->
no request-type
配置访问令牌请求的请求参数
配置访问令牌请求的请求参数（URL参数和请求头），在访问令牌请求配置模式下，使用以下命令：
request-parameter name value [add-to-header]
l
name – 指定访问令牌请求参数中的参数名称。取值范围为1-31个字符。
l
value – 指定访问令牌请求参数中的参数值。取值范围为1-511个字符。
l
add-to-header – 指定在请求头中加入该请求参数。如不指定，则默认加入URL参数中。请求头和URL
参数分别最多可配置16个请求参数。
在访问令牌请求配置模式下使用该命令no的形式删除指定的请求参数：
no request-parameter name [add-to-header]
配置访问令牌请求的请求体
注意:
l
请求体支持URL Encode和JSON两种格式，默认为URL Encode格式。使用JSON格式时，需
要在请求头中配置参数名称为Content-Type，参数值为application/json。
l
通过WebUI配置请求体时，仅支持明文配置；通过CLI配置请求体时，仅支持配置base64编码
后的请求体参数。
配置访问令牌请求的请求体，在访问令牌请求配置模式下，使用以下命令：
request-body text
l
text – 指定访问令牌请求参数中的请求体，根据具体的OAuth2服务器进行配置。取值范围为1-2048个
字符。
在访问令牌请求配置模式下使用该命令no的形式删除配置的请求体：
no request-body
配置访问令牌请求的响应参数
配置系统申请访问令牌的响应参数，包括参数名称和本地变量。访问令牌请求成功后，需要解析响应报文中
的指定参数字段并保存到本地变量中，用于下一步的用户信息请求。最多可以配置5个响应参数。
配置访问令牌请求的响应参数，在访问令牌请求配置模式下，使用以下命令：

<!-- 来源页 1254 -->
response-parameter attribute_name mapping local_value
l
attribute_name – 指定访问令牌响应参数中的参数名称。取值范围为1-31个字符。
l
local_value – 指定访问令牌响应参数中的本地变量。取值范围为1-31个字符。
在访问令牌请求配置模式下使用该命令no的形式取消对访问令牌请求参数中响应参数的指定：
no response-parameter attribute_name
配置访问令牌请求的成功条件
配置系统申请访问令牌的成功条件，包括参数名称、类型、参数值。系统将检查响应报文中指定参数的值是
否满足成功条件，若满足则继续进行认证，若不满足则中断认证。
配置访问令牌请求的成功条件，在访问令牌请求配置模式下，使用以下命令：
response-validate-parameter name {{contains | does-not-contain | equals | does-not-equal}
value | exists | does-not-exist }
l
name – 指定成功条件的参数名称。取值范围为1-31个字符。
l
contains | does-not-contain | equals | does-not-equal | exists | does-not-exist – 指定成功
条件的匹配关系，包括包含（contains）、不包含（does-not-contain）、等于（equals）、不等于
（does-not-equal）、为空（does-not-exist）、不为空（exists）。
l
value – 指定成功条件的参数值。取值范围为1-511个字符。
在访问令牌请求配置模式下使用该命令no的形式删除访问令牌请求的成功条件：
no response-validate-parameter name
OAuth2服务器用户信息请求配置
当使用OAuth2服务器进行认证时，用户需要配置用户信息请求相关的内容，包括用户信息请求的OAuth2服
务器地址、请求参数、响应参数。
进入用户信息请求配置模式
对于用户信息请求的OAuth2服务器地址、请求参数、响应参数，都需要在用户信息请求配置模式下进行。
进入用户信息请求配置模式，在OAuth服务器配置模式，使用以下命令：
user-info-request number
l
number – 指定进入第number次用户信息请求配置模式。取值范围为1-5。
在OAuth服务器配置模式下使用该命令no的形式删除用户信息请求：

<!-- 来源页 1255 -->
no user-info-request number
注意: 删除时需要从最后一次请求开始倒序依次删除。
配置用户信息请求的OAuth2服务器地址
配置用户信息请求的OAuth2服务器地址，在访问令牌请求配置模式下，使用以下命令：
request-url request-url
l
request-url – 指定系统请求用户信息的认证服务器地址。如
https://passport.hillstonenet.com/API/Resource/UserInfo。
在用户信息请求配置模式下使用该命令no的形式取消对用户信息请求的OAuth2服务器地址的指定：
no request-url
配置用户信息请求的请求方法
配置用户信息请求的请求方法，在用户信息请求配置模式下，使用以下命令：
request-type {get | post}
l
get – 指定请求方法为“GET”。默认为“GET”。
l
post – 指定请求方法为“POST”。
在用户信息请求配置模式下使用该命令no的形式恢复默认的请求方法：
no request-type
配置用户信息请求的请求参数
配置用户信息请求的请求参数（URL参数和请求头），在用户信息请求配置模式下，使用以下命令：
request-parameter name value [add-to-header]
l
name – 指定用户信息请求参数中的参数名称。取值范围为1-31个字符。
l
value – 指定用户信息请求参数中的参数值。取值范围为1-511个字符。
l
add-to-header – 指定在请求头中加入该请求参数。如不指定，则默认加入URL参数中。请求头和URL
参数分别最多可配置16个请求参数。
在用户信息请求配置模式下使用该命令no的形式删除指定的请求参数：
no request-parameter name [add-to-header]

<!-- 来源页 1256 -->
配置用户信息请求的请求体
注意:
l
请求体支持URL Encode和JSON两种格式，默认为URL Encode格式。使用JSON格式时，需
要在请求头中配置参数名称为Content-Type，参数值为application/json。
l
通过WebUI配置请求体时，仅支持明文配置；通过CLI配置请求体时，仅支持配置base64编码
后的请求体参数。
配置用户信息请求的请求体，在用户信息请求配置模式下，使用以下命令：
request-body text
l
text – 指定用户信息请求参数中的参数体，根据具体的OAuth2服务器进行配置。取值范围为1-2048个
字符。
在用户信息请求配置模式下使用该命令no的形式删除配置的请求体：
no request-body
配置用户信息请求的响应参数
配置系统申请用户信息的响应参数，包括参数名称和本地变量。用户信息请求成功后，需要解析响应报文中
的指定参数字段并保存到本地变量中，用于认证用户的用户名展示。最多可以配置5个响应参数。
配置用户信息请求的响应参数，在用户信息请求配置模式下，使用以下命令：
response-parameter attribute_name mapping local_value
l
attribute_name – 指定用户信息响应参数中的参数名称。取值范围为1-31个字符。
l
local_value – 指定用户信息响应参数中的本地变量。取值范围为1-31个字符。
在用户信息请求配置模式下使用该命令no的形式取消对用户信息请求参数中的响应参数的指定：
no response-parameter attribute_name
配置用户信息请求的成功条件
配置系统申请用户信息的成功条件，包括参数名称、类型、参数值。系统将检查响应报文中指定参数的值是
否满足成功条件，若满足则继续进行认证，若不满足则中断认证。
配置用户信息请求的成功条件，在用户信息请求配置模式下，使用以下命令：

<!-- 来源页 1257 -->
response-validate-parameter name {{contains | does-not-contain | equals | does-not-equal}
value | exists | does-not-exist }
l
name – 指定成功条件的参数名称。取值范围为1-31个字符。
l
contains | does-not-contain | equals | does-not-equal | exists | does-not-exist – 指定成功
条件的匹配关系，包括包含（contains）、不包含（does-not-contain）、等于（equals）、不等于
（does-not-equal）、为空（does-not-exist）、不为空（exists）。
l
value – 指定成功条件的参数值。取值范围为1-511个字符。
在用户信息请求配置模式下使用该命令no的形式删除访问令牌请求的成功条件：
no response-validate-parameter name
查看OAuth2服务器配置信息
show aaa-server aaa-server-name
l
aaa-server-name – 指定OAuth2服务器。每个VSYS下只有一个OAuth2服务器。
例如：
hostname(config)# show aaa-server oauth-server
==============================================================
aaa-server: oauth-server（显示OAuth2服务器名称）
type: oauth（显示AAA服务器类型为OAuth2服务器）
vrouter: trust-vr（显示OAuth2服务器所属的虚拟路由器）
organization source: local（显示认证用户所属的组织来源服务器）
authentication icon name: test（显示OAuth2认证图标的名称）
--------------------------------------------------------------
authorization code:（显示OAuth2服务器的授权码请求配置信息）
request type: get
request url: http://www.example.com
request:
query parameters:
redirect_uri: https://host:17443/login/oauth
client_id: AAA

<!-- 来源页 1258 -->
response:
mapping parameters:
code: $code
--------------------------------------------------------------
access token:（显示OAuth2服务器的访问令牌请求配置信息）
enabled
request type: get
request url: http://www.example.com
request:
query parameters:
redirect_uri: https://host:17443/login/oauth
code: code
response:
validation parameters:
msg equals success
mapping parameters:
access_token: $access_token
--------------------------------------------------------------
user information:（显示OAuth2服务器的用户信息请求配置信息）
*****************************
step no: 1（显示第一次用户信息请求配置信息）
request type: get
request url: http://www.example.com
request:
header parameters:
Authorization: Bearer $access_token
response:
validation parameters:
msg equals success

<!-- 来源页 1259 -->
mapping parameters:
username: $username1
*****************************
step no: 2（显示第二次用户信息请求配置信息）
request type: get
request url: http://www.example.com
request:
header parameters:
Authorization: Bearer $access_token
response:
validation parameters:
msg equals success
mapping parameters:
username: $username
==============================================================
配置企业微信服务器认证参数
在全局配置模式下执行aaa-server aaa-server-name type wecom命令可以进入指定名称的企业微信服
务器配置模式。用户可配置的企业微信服务器认证参数包括：
l 配置认证服务器所属的VRouter
l 配置角色映射规则
l 配置CorpID
l 配置AgentID
l 配置AppSecret
l 配置重定向URL
l 配置用户同步功能
配置认证服务器所属的VRouter
配置认证服务器所属的VRouter，在企业微信服务器配置模式下，使用以下命令：
vrouter vrouter-name

<!-- 来源页 1260 -->
l
vrouter-name – 指定认证服务器所属的VRouter。默认为系统缺省VR即trust-vr。
在企业微信服务器配置模式下，使用该命令no的形式取消认证主服务器的IP地址或者域名配置：
no vrouter
指定角色映射规则
为企业微信服务器指定角色映射规则后，系统将会为通过该服务器认证的用户按照指定角色映射规则分配角
色。为企业微信服务器指定角色映射规则，在企业微信服务器配置模式下，使用以下命令：
role-mapping-rule rule-name
l
rule-name – 指定系统中已配置的映射规则的名称。
在企业微信服务器配置模式下，使用该命令no的形式取消角色映射规则的指定：
no role-mapping-rule
配置企业微信服务器的CorpID
CorpID，即企业ID，用于区分不同的企业、标识企业微信的主体，确保所有操作都属于特定的企业。在与服
务器进行认证连接的过程中，CorpID是获取Access Token（访问令牌）的必要参数。Access Token是调
用企业微信API的凭证。配置企业微信服务器的CorpID，在企业微信服务器配置模式下，使用以下命令：
CorpID id-number
l
id-number – 指定企业微信服务器的企业ID。
在企业微信服务器配置模式下，使用该命令no的形式删除配置：
no CorpID
配置企业微信服务器的AgentID
指定应用ID，企业微信中应用的唯一标识，用于区分企业微信内的不同应用，指定操作属于特定的应用。用
户需要在企业微信服务器上创建一个应用，用于与防火墙设备进行认证连接。配置企业微信服务器的
AgentID，在企业微信服务器配置下，使用以下命令：
AgentID id-number
l
id-number– 指定企业微信服务器的应用ID。
在企业微信服务器配置模式下，使用该命令no的形式删除配置：
no AgentID

<!-- 来源页 1261 -->
配置企业微信服务器的AppSecret
AppSecret，即应用的密钥，用于与CorpID一起生成Access Token。Access Token是调用企业微信API
的凭证。配置企业微信服务器的AppSecret，在企业微信服务器配置下，使用以下命令：
AppSecret secret
l
secret– 指定企业微信服务器的应用密钥。
在企业微信服务器配置模式下，使用该命令no的形式删除配置：
no AppSecret
配置企业微信服务器的重定向URL
指定企业微信服务器成功授权后返回的地址，在企业微信服务器配置下，使用以下命令：
redirect-uri url
l
url– 指定企业微信服务器的重定向URL。
在企业微信服务器配置模式下，使用该命令no的形式删除配置：
no redirect-uri
配置用户同步功能
用户同步指的是完成企业微信服务器配置后，系统将认证服务器上的用户信息同步到本地的功能，默认情况
下系统每隔30分钟同步一次。
启用/禁用用户同步功能
在进行用户同步前，需要先启用用户同步功能。默认情况下，用户同步功能是启用的。启用或禁用用户同步
功能，在企业微信服务器配置模式下，使用以下命令：
l
启用：sync enable
l
禁用：sync disable
配置用户同步方式
系统支持多种用户同步方式，包括手动同步和自动同步。
手动同步
更新企业微信服务器连接，手动同步用户信息。在企业微信服务器配置模式下，使用以下命令：
manual-sync

<!-- 来源页 1262 -->
执行一次该命令即进行一次同步，如果同步过程中再次执行该命令，系统将清除原有用户同步信息，重新进
行同步。
周期自动同步
周期自动同步方式包括：按时间间隔同步和每天同步。周期自动同步配置流程如下：
1.
启用周期自动同步功能：在企业微信服务器配置模式下，使用auto-sync enable命令，开启周期自动
同步。
2.
配置周期自动同步方式：在企业微信服务器配置模式下，使用auto-sync {periodically interval |
daily HH:MM}命令，指定周期自动同步方式。
l
interval – 指定为按时间间隔同步，并配置自动同步的间隔时间。取值范围为60到1440，单位为
分钟，默认值为720。
l
HH:MM – 指定为每天同步，并配置每天执行自动同步的时间点。HH和MM分别代表小时和分钟。
如需恢复系统默认同步方式，即每隔30分钟进行一次同步，可在企业微信服务器配置模式下，使用以下命
令，关闭周期自动同步功能：
auto-sync disable
配置钉钉服务器认证参数
在全局配置模式下执行aaa-server aaa-server-name type dingtalk命令可以进入指定名称的服务器配
置模式。用户可配置的钉钉服务器认证参数包括：
l 配置认证服务器所属的VRouter
l 配置角色映射规则
l 配置用户名属性
l 配置APPKey
l 配置AppSecret
l 配置重定向URL
l 配置用户同步功能
配置认证服务器所属的VRouter
配置认证服务器所属的VRouter，在钉钉服务器配置模式下，使用以下命令：
vrouter vrouter-name
l
vrouter-name – 指定认证服务器所属的VRouter。默认为系统缺省VR即trust-vr。

<!-- 来源页 1263 -->
在钉钉服务器配置模式下，使用该命令no的形式取消认证主服务器所属的VRouter配置：
no vrouter
指定角色映射规则
为钉钉服务器指定角色映射规则后，系统将会为通过该服务器认证的用户按照指定角色映射规则分配角色。
为钉钉服务器指定角色映射规则，在钉钉服务器配置模式下，使用以下命令：
role-mapping-rule rule-name
l
rule-name – 指定系统中已配置的映射规则的名称。
在钉钉服务器配置模式下，使用该命令no的形式取消角色映射规则的指定：
no role-mapping-rule
指定用户名属性
指定用户名属性的值。当系统同步用户信息到本地时，可以通过该属性获取用户名；当系统进行用户认证
时，可以通过该属性来识别用户。在钉钉服务器配置模式下，使用以下命令来指定用户名属性：
naming-attribute string
l
string – 指定用户名属性的值，为1到63个字符的字符串。该字符串通常为name或userid，默认值为
name。
在钉钉服务配置模式下，使用该命令no的形式恢复默认情况：
no naming-attribute
配置钉钉服务器的APPKey
指定应用Key，钉钉开放平台为每个应用分配的唯一标识，用于标识应用的身份。用户需要在钉钉服务器上
创建一个应用，用于与防火墙设备进行认证连接。在认证连接的过程中，应用Key用于向钉钉服务器发起认
证请求时，表明是哪个应用在请求认证。配置钉钉服务器的APPKey，在钉钉服务器配置模式下，使用以下
命令：
APPKey key
l
key – 指定钉钉服务器的应用Key。
在钉钉服务器配置模式下，使用该命令no的形式删除配置：
no APPKey

<!-- 来源页 1264 -->
配置钉钉服务器的AppSecret
AppSecret是与应用Key配对的密钥，用于确保应用的身份验证和授权的安全性。配置钉钉服务器的
AppSecret，在钉钉服务器配置下，使用以下命令：
AppSecret secret
l
secret– 指定钉钉服务器的应用密钥。
在钉钉服务器配置模式下，使用该命令no的形式删除配置：
no AppSecret
配置钉钉服务器的重定向URL
指定钉钉服务器成功授权后返回的地址，在钉钉服务器配置下，使用以下命令：
redirect-uri url
l
url– 指定钉钉服务器的重定向URL。
在钉钉服务器配置模式下，使用该命令no的形式删除配置：
no redirect-uri
配置用户同步功能
用户同步指的是完成钉钉服务器配置后，系统将认证服务器上的用户信息同步到本地的功能，默认情况下系
统每隔30分钟同步一次。
启用/禁用用户同步功能
在进行用户同步前，需要先启用用户同步功能。默认情况下，用户同步功能是启用的。启用或禁用用户同步
功能，在钉钉服务器配置模式下，使用以下命令：
l
启用：sync enable
l
禁用：sync disable
配置用户同步方式
系统支持多种用户同步方式，包括手动同步和自动同步。
手动同步
更新钉钉服务器连接，手动同步用户信息。在钉钉服务器配置模式下，使用以下命令：
manual-sync

<!-- 来源页 1265 -->
执行一次该命令即进行一次同步，如果同步过程中再次执行该命令，系统将清除原有用户同步信息，重新进
行同步。
周期自动同步
周期自动同步方式包括：按时间间隔同步和每天同步。周期自动同步配置流程如下：
1.
启用周期自动同步功能：在钉钉服务器配置模式下，使用auto-sync enable命令，开启周期自动同
步。
2.
配置周期自动同步方式：在钉钉服务器配置模式下，使用auto-sync {periodically interval | daily
HH:MM }命令，指定周期自动同步方式。
l
interval – 指定为按时间间隔同步，并配置自动同步的间隔时间。取值范围为60到1440，单位为
分钟，默认值为720。
l
HH:MM – 指定为每天同步，并配置每天执行自动同步的时间点。HH和MM分别代表小时和分钟。
如需恢复系统默认同步方式，即每隔30分钟进行一次同步，可在钉钉服务器配置模式下，使用以下命令，关
闭周期自动同步功能：
auto-sync disable
配置中孚服务器认证参数
在全局配置模式下执行aaa-server aaa-server-name type zhongfu命令可以进入指定名称的中孚服务
器配置模式。用户可配置的中孚服务器认证参数包括：
l 配置认证服务器的地址和所属VRouter
l 配置认证服务器的端口号
l 配置角色映射规则
l 配置授权密码
l 配置用户同步功能
配置认证服务器的地址和所属VRouter
配置认证服务器的地址和所属VRouter，在中孚服务器配置模式下，使用以下命令：
host host-name [vrouter vrouter-name]
l
host-name - 指定认证服务器的IPv4地址、IPv6地址或者域名。
l
vrouter-name – 指定认证服务器所属的VRouter。默认为系统缺省VR即trust-vr。
在中孚服务器配置模式下，使用该命令no的形式取消认证服务器的地址和所属虚拟路由器配置：

<!-- 来源页 1266 -->
no host
配置认证服务器的端口号
配置认证服务器的端口号，在中孚服务器配置模式下，使用以下命令：
port port-number
l
id-number – 指定中孚服务器的端口号，取值范围是1到65535。
在中孚服务器配置模式下，使用该命令no的形式删除配置：
no port
指定角色映射规则
为中孚服务器指定角色映射规则后，系统将会为通过该服务器认证的用户按照指定角色映射规则分配角色。
为中孚服务器指定角色映射规则，在中孚服务器配置模式下，使用以下命令：
role-mapping-rule rule-name
l
rule-name – 指定系统中已配置的映射规则的名称。
在中孚服务器配置模式下，使用该命令no的形式取消角色映射规则的指定：
no role-mapping-rule
配置授权密码
指定应用授权密码，中孚沙箱中应用的唯一身份标识，用于区分中孚沙箱内的不同应用。该密码由中孚沙箱
提供，主要用于防火墙设备与中孚服务器进行安全认证连接。用户需提前登录中孚沙箱，在“安全沙箱> 系
统管理> 应用系统授权”页面获取应用授权密码；或者联系中孚相关人员获取应用授权密码。
配置授权密码，在中孚服务器配置下，使用以下命令：
token token-value
l
token-value – 指定应用授权密码。取值范围是1到127个字符。
在中孚服务器配置模式下，使用该命令no的形式删除配置：
no token
配置用户同步功能
用户同步指的是完成中孚服务器配置后，系统将认证服务器上的用户信息同步到本地的功能，默认情况下系
统每隔30分钟同步一次。

<!-- 来源页 1267 -->
启用/禁用用户同步功能
在进行用户同步前，需要先启用用户同步功能。默认情况下，用户同步功能是启用的。启用或禁用用户同步
功能，在中孚服务器配置模式下，使用以下命令：
l
启用：sync enable
l
禁用：sync disable
配置用户同步方式
系统支持多种用户同步方式，包括手动同步和周期自动同步。
手动同步
更新中孚服务器连接，手动同步用户信息。在中孚服务器配置模式下，使用以下命令：
manual-sync
执行一次该命令即进行一次同步，如果同步过程中再次执行该命令，系统将清除原有用户同步信息，重新进
行同步。
周期自动同步
周期自动同步方式包括：按时间间隔同步和每天同步。周期自动同步配置流程如下：
1.
启用周期自动同步功能：在中孚服务器配置模式下，使用auto-sync enable命令，开启周期自动同
步。
2.
配置周期自动同步方式：在中孚服务器配置模式下，使用auto-sync {periodically interval | daily
HH:MM }命令，指定周期自动同步方式。
l
interval – 指定为按时间间隔同步，并配置自动同步的间隔时间。取值范围为60到1440，单位为
分钟，默认值为720。
l
HH:MM – 指定为每天同步，并配置每天执行自动同步的时间点。HH和MM分别代表小时和分钟。
如需恢复系统默认同步方式，即每隔30分钟进行一次同步，可在中孚服务器配置模式下，使用以下命令，关
闭周期自动同步功能：
auto-sync disable
配置SAML服务器认证参数
在全局配置模式下执行aaa-server aaa-server-name type saml命令可以进入指定名称的SAML服务器
配置模式。用户可配置的SAML服务器认证参数包括：

<!-- 来源页 1268 -->
l 服务提供者参数
l 身份提供者参数
l 用户名属性
配置服务提供者参数
服务提供者（Service provider）：简称SP。SP 是指为用户提供各种服务的业务系统。它依赖于身份提供
者（Identity provider）来对用户进行身份认证，并根据身份提供者提供的身份信息来授权用户访问其系
统。防火墙即为服务提供者（SP）。
配置服务提供者的实体ID
配置SP的实体ID，在SAML服务器配置模式下，使用以下命令：
sp-entity-id id-name
l
id-name - 指定SP的实体ID。该ID是SP的标识符，用于在SAML交互中被IDP识别。取值范围为1-255
个字符。
取消配置SP的实体ID，在SAML服务器配置模式下，使用以下命令：
no sp-entity-id
配置服务提供者的单点登录URL
配置SP的单点登录URL，在SAML服务器配置模式下，使用以下命令：
sp-single-sign-on-url url
l
url - 指定SP的单点登录URL，用于接收并解析IDP返回的SAML断言以完成登录。一般为防火墙的IP地
址，取值范围为1-255个字符。例如：https://1.1.1.1:80/samlLogin
取消配置SP的单点登录URL，在SAML服务器配置模式下，使用以下命令：
no sp-single-sign-on-url
配置服务提供者的信任域
SP信任域主要用于在SP向IDP发送认证请求时进行数字签名，并且能够对SP接收到的认证响应进行解密，确
保消息的真实性、完整性与保密性。当IDP有证书验证要求，或对通信保密性有较高需求时，用户可根据实
际情况配置SP信任域。信任域配置参见“用户认证> PKI > 配置PKI”章节。
配置SP的信任域，在SAML服务器配置模式下，使用以下命令：
sp-trust-domain trust-domain-name

<!-- 来源页 1269 -->
l
trust-domain-name - 指定系统中已创建的信任域。
取消配置SP的信任域，在SAML服务器配置模式下，使用以下命令：
no sp-trust-domain
配置服务提供者的名称
配置SP的名称，在SAML服务器配置模式下，使用以下命令：
sp-provider-name name
l
name - 指定SP的名称。取值范围为1-63个字符。
no sp-provider-name
配置身份提供者参数
身份提供者（Identity provider）：简称IDP。IDP是用于提供用户身份认证的服务器。它保存着用户的身
份信息，如用户名、密码、用户角色等，并通过一定的认证机制对用户进行身份验证。IDP提供认证界面验
证用户凭证（如账号密码），生成包含用户身份和权限信息的断言，并将断言返回给SP。
配置身份提供者的实体ID
配置IDP的实体ID，在SAML服务器配置模式下，使用以下命令：
idp-entity-id id-name
l
id-name - 指定IDP的实体ID。该ID是IDP的标识符，用于保证在SAML交互中SP能够准确地与指定IDP
进行交互。取值范围为1-255个字符。
取消配置IDP的实体ID，在SAML服务器配置模式下，使用以下命令：
no idp-entity-id
配置身份提供者的单点登录URL
配置IDP的单点登录URL，在SAML服务器配置模式下，使用以下命令：
idp-single-sign-on-url url
l
url - 指定IDP的单点登录URL，即IDP登录界面，用于验证用户凭证。取值范围为1-255个字符。例
如：https://idp.example.com/saml2/sso
取消配置IDP的单点登录URL，在SAML服务器配置模式下，使用以下命令：
no idp-single-sign-on-url

<!-- 来源页 1270 -->
配置身份提供者的证书
在SAML认证过程中，当IDP向SP发送认证响应时，IDP证书用于对该认证响应进行数字签名和加密，确保
SP接收到的消息真实、完整且保密。若IDP需要对认证响应进行加密，则用户需预先在信任域中配置相关证
书才能对认证响应进行解密。
配置IDP证书，在SAML服务器配置模式下，使用以下命令：
idp-cert value
l
value - 指定IDP证书。取值范围为1-2047个字符。
取消配置IDP证书，在SAML服务器配置模式下，使用以下命令：
no idp-cert
配置用户名属性
配置用户名属性，在SAML服务器配置模式下，使用以下命令：
user-name-attribute name
l
name - 指定在SAML断言中用于标识用户名的属性名称。若不指定，默认为NameID。取值范围为1-
31个字符。
恢复默认的用户名属性，在SAML服务器配置模式下，使用以下命令：
no user-name-attribute
查看SAML服务器配置信息
查看SAML服务器配置信息，在任意模式下，使用以下命令：
show aaa-server aaa-server-name
l
aaa-server-name - 指定SAML服务器。
以下是返回结果示例：
hostname(config)# show aaa-server saml-server
==============================================================
aaa-server: saml-server
type: saml
user-name-attribute: NameID
sp-entity-id: SP

<!-- 来源页 1271 -->
sp-single-sign-on-url: https://1.1.1.1:80/samlLogin
sp-trust-domain: trust_domain_default
sp-provider-name: SP-test
idp-entity-id: IDP
idp-single-sign-on-url: https://idp.example.com/saml2/sso
idp-cert: MIIEDIBAgIVAMM6IbzwzCCAnegAwYcV26MA0GCSqPSYG8HoxoIj5eE2.......
==============================================================
配置RADIUS服务器的计费功能
系统支持对使用RADIUS服务器认证的用户进行计费。在全局配置模式下执行aaa-server aaa-servername type radius命令可以进入指定名称的RADIUS服务器配置模式。用户可配置的RADIUS服务器计费功
能的参数包括：
l 开启或关闭计费功能
l 配置计费主/备份服务器的IP地址或域名
l 配置计费服务器的端口号
l 配置计费服务器的共享密钥
开启或关闭计费功能
在RADIUS服务器配置模式下，输入以下命令开启或关闭该RADIUS服务器的计费功能：
l
开启：accounting enable
l
关闭：no accounting enable
当计费功能开启后，用户可以继续对计费功能的其他参数进行配置。
配置计费主/备份服务器的IP地址或域名
配置计费主/备份服务器的IP地址或域名，在RADIUS服务器配置模式下，使用以下命令：
accounting {host {ip-address | host-name} | backup1 {ip-address | host-name} | backup2 {ipaddress | host-name}}
l
host {ip-address | host-name} – 指定主服务器的IP地址或者域名。
l
backup1 {ip-address | host-name} – 指定备份服务器1的IP地址或者域名。
l
backup2 {ip-address | host-name} – 指定备份服务器2的IP地址或者域名。

<!-- 来源页 1272 -->
在RADIUS服务器配置模式下，使用该命令no的形式取消计费主/备份服务器的IP地址或者域名配置：
no accounting {host | backup1 | backup2}
配置计费服务器端口号
配置计费服务器端口号，在RADIUS服务器配置模式下，使用以下命令：
accounting port port-number
l
port-number – 指定计费服务器的端口号。默认值是1813。取值范围是1024到65535。
在RADIUS服务器配置模式下，使用该命令no的形式恢复端口号的默认值：
no accounting port
配置计费服务器的共享密钥
配置计费服务器的共享密钥，在RADIUS服务器配置下，使用以下命令：
accounting secret secret
l
secret – 指定计费服务器的共享密钥字符串。字符串范围为1到31个字符。
在RADIUS服务器配置模式下，使用该命令no的形式取消对计费服务器共享密钥的配置：
no accounting secret
开启/关闭计费用户下线管理功能
开启计费用户下线管理功能后，系统可以根据获取Radius服务器上的计费用户下线信息（包括指定下线用户
名称、用户IP地址、用户计费ID等），断开指定下线用户的连接并结束计费。默认情况下，该功能是关闭
的。
开启计费用户下线管理功能，在RADIUS服务器配置下，使用以下命令：
unsolicited-message enable
关闭计费用户下线管理功能，在RADIUS服务器配置下，使用以下命令：
no unsolicited-message enable
配置服务器认证与授权
AAA认证服务器的认证参数配置完成后，用户需要指定某个服务器作为Hillstone设备系统管理员使用的认
证服务器。默认情况下，系统使用“Local”作为系统管理员认证服务器。用户不可以删除“Local”。
配置认证服务器授权
配置认证服务器授权，在全局配置模式下输入以下命令：
admin authorization-mode {local | aaa-server server-name [disable-retry-local]}

<!-- 来源页 1273 -->
l
local - 指定本地服务器授权。
l
aaa-server server-name [disable-retry-local] - 指定外部服务器授权。
l
server-name - 指定认证服务器的名称。支持RADIUS（radius）或TACACS+类型的服务器。
l
disable-retry-local - 关闭本地密码重试功能。默认情况下，如果所配置的外部服务器不可达或
返回密码错误，系统会使用本地服务器“Local”进行系统管理员认证。用户可以选择关闭本地密
码重试功能，即关闭“Local”服务器认证，当指定的外部服务器返回密码错误时，无法使用
“Local”进行系统管理员认证。服务器不可达不受disable-retry-local配置影响。
使用no admin authorization-mode命令恢复使用默认系统认证服务器“Local”。
用户可以根据需要，指定优先使用本地服务器对Console方式访问的管理员进行认证，如果所配置的本地服
务器不可达或认证服务器不可用时，系统会使用默认Radius服务器进行系统管理员认证。指定Console方式
访问的管理员优先使用本地服务器认证，在全局配置模式下，使用以下命令：
admin console local-auth-prior
使用no admin console local-auth-prior命令取消优先使用本地认证服务器“Local”。
显示认证服务器的授权信息
显示认证服务器的授权信息，在任意模式下，使用以下命令：
show admin authorization-mode
显示优先使用本地服务器认证启用状态
显示优先使用本地服务器认证功能启用状态，在任何模式下使用以下命令：
show admin console local-auth-prior
配置管理员用户的服务器认证
如果选择本地服务器授权，需要配置管理员及认证信息。配置服务器认证，在管理员配置模式下输入以下命
令：
authentication-server {local | aaa-server server-name [retry-local]}
l
local - 指定本地服务器认证。
l
aaa-server server-name [retry-local] - 指定外部服务器认证。
l
server-name - 指定认证服务器的名称。支持RADIUS（radius）、Active-Directory
（active-directory）、LDAP（ldap）或者TACACS+类型的服务器。

<!-- 来源页 1274 -->
l
retry-local - 开启逃生模式。外部服务器不可达时，如果开启逃生模式，系统会使用本地服务器
“Local”进行系统管理员认证，如果未开启逃生模式，无法使用“Local”进行系统管理员认
证。外部服务器返回密码错误时，直接认证失败，不受retry-local配置影响。
认证与授权的显示与调试
配置完毕，在任何模式下执行show命令可以查看配置后的运行情况，用户可以通过查看显示信息验证配置
的效果。在任何模式下执行debug aaa命令可以对AAA进行调试。
查看AAA服务器的配置信息，请输入以下命令:
show aaa-server [server-name]
显示用户黑名单的配置信息，请输入以下命令：
show user-block-list
显示AAA的调试信息，请输入以下命令:
debug aaa [accounting | authentication | authorization | internal | radius | ldap | user]
l
accounting - 显示AAA计费的调试信息。
l
authentication - 显示AAA认证的调试信息。
l
authorization - 显示AAA授权的调试信息。
l
internal - 显示本地用户通过AAA本地认证方式访问设备时的调试信息。
l
radius - 显示RADIUS认证的调试信息。
l
ldap - 显示LDAP（包括Active-Directory服务器和LDAP服务器）认证的调试信息。
l
user – 显示本地用户属性变化时的调试信息。
配置防暴力破解功能
为了防止非法用户通过暴力方法获取用户名和密码，可以通过配置基于用户名或基于IP地址的防暴力破解功
能，即在指定时间内，若用户连续输错指定次数的用户名和密码，系统将会按照指定的锁定时间锁定该用户
或IP地址。防暴力破解功能的配置包括：
l 开启或关闭防暴力破解功能
l 配置尝试次数
l 配置锁定时间
l 查看锁定列表信息
l 解除用户/IP地址的锁定

<!-- 来源页 1275 -->
开启或关闭防暴力破解功能
防暴力破解功能默认情况下是关闭的。开启防暴力破解功能，请在本地服务器配置模式下使用以下命令：
l
启用：lockout {ip | user} enable
l
关闭：lockout {ip | user} disable
配置尝试次数
配置尝试次数，即在指定时间内，允许用户连续输错用户名和密码的次数，请在本地服务器配置模式下使用
以下命令：
lockout {ip | user} failed-attempts number interval interval
l
failed-attempts number – 指定时间内允许输错用户名和密码的次数，基于用户名配置时，取值范围
是1-32，默认值是5次；基于IP地址配置时，取值范围是1-2048，默认值是64次。
l
interval interval – 指定连续输错用户名和密码的时间范围，单位是秒，取值范围是1-180秒，默认值
是60秒。
配置锁定时间
在指定时间内，若用户连续输错指定次数的用户名和密码，系统将会按照指定的锁定时间锁定该用户或IP地
址。配置锁定时间，请在本地服务器配置模式下使用以下命令：
lockout {ip | user} lockout-time time
l
lockout-time time – 指定锁定时间，单位是秒，取值范围是30-1800秒，基于用户名配置时，默认值
是600秒；基于IP地址配置时，默认值是60秒。
查看锁定列表信息
查看被锁定的用户信息、被锁定的IP地址信息，在任何模式下，使用以下命令：
show aaa-server aaa-server-name lockout {user [username] | ip [ip-address vr_id number]}
l
aaa-server-name - 指定AAA服务器名称。
l
user [username] - 查看指定名称的锁定用户信息。
l
ip [ip-address vr_id number] - 查看指定IP地址和VRouter ID的锁定IP信息。
解除用户/IP地址的锁定
解除对指定用户/IP地址的锁定并且从锁定列表中删除，在任何模式下，使用以下命令：
exec aaa aaa-server aaa-server-name lockout delete {user [username] | ip [ip-address vr_id
number]}

<!-- 来源页 1276 -->
l
aaa-server-name - 指定AAA服务器名称。
l
user [username] - 解除对指定名称的用户的锁定。
l
ip [ip-address vr_id number] - 解除对指定IP地址和VRouter ID的锁定。
配置信任域/证书链
在SSL VPN双栈组网场景中，用户通过OAuth2.0/企业微信/钉钉服务器认证登录时，浏览器可能出现“网
站不安全”的告警提示，影响正常登录。其根本原因是企业商用证书为三级证书（根证书→中间证书→服务
器证书），需要完整证书链方能通过浏览器合法性校验。然而在实际证书验证中，浏览器从上述认证服务器
中获取授权码并重定向至防火墙进行TLS握手时，防火墙提供的证书缺少中间证书，导致浏览器无法构建完
整的信任链路，从而触发安全告警。针对此问题，系统支持为OAuth2.0、企业微信和钉钉认证服务统一配
置信任域或证书链，补全证书信任路径，使浏览器能够正常完成合法性校验，消除登录告警，保障SSL VPN
双栈场景下统一身份认证登录的安全、稳定与顺畅。
为OAuth2.0、企业微信和钉钉认证服务配置信任域或证书链的流程如下：
1. 创建信任域或证书链
2. 进入OAuth信任域/证书链配置模式
3. 配置信任域或证书链
4. 查看OAuth信任域/证书链的配置信息
注意:
l
信任域与证书链为互斥配置，二者只能任选其一。
l
在OAuth信任域/证书链配置模式下设置的信任域或证书链，仅适用于通过OAuth2.0服务器、
企业微信服务器或钉钉服务器进行认证的场景。
进入OAuth信任域/证书链配置模式
进入OAuth信任域/证书链配置模式，在全局配置模式下，使用以下命令：
oauth-https
配置信任域
在配置信任域之前，请确保系统当前未配置证书链；若已配置，需先执行no cert-chain命令，删除证书链
配置。若信任域和证书链均未配置，系统默认使用内置信任域“trust_domain_default”进行证书验证。
配置信任域，在OAuth信任域/证书链配置模式下，使用以下命令：
trust-domain trust-domain-name

<!-- 来源页 1277 -->
l
trust-domain-name - 指定信任域的名称。
在OAuth信任域/证书链配置模式下，使用no命令恢复默认信任域配置：
no trust-domain
配置证书链
在配置证书链之前，请确保系统当前未指定非默认信任域；若已指定，需先执行no trust-domain命令恢复
默认配置。
提示: 证书链的优先级高于默认信任域。
配置证书链，在OAuth信任域/证书链配置模式下，使用以下命令：
cert-chain cert-chain-name
l
cert-chain-name - 输入指定证书链的名称。
在OAuth信任域/证书链配置模式下，使用no命令删除证书链配置：
no cert-chain
查看信任域/证书链配置信息
查看信任域/证书链配置信息，在任意模式下，使用以下命令：
show oauth-https
返回示例：
hostname# show oauth-https
==================================
trust-domain: trust_domain_default
==================================

<!-- 来源页 1278 -->
Radius动态授权
Radius 动态授权功能，包含以下两点内容：
l 当用户认证成功后，Radius服务器可以发送Radius CoA（Change of Authorization）请求消息将认证用户的
权限下发到设备，设备自动生成该用户的安全策略规则，当该用户下线时，设备将会自动删除该用户的安全策略
规则。
l 当SCVPN用户认证成功后，Radius服务器可以发送Radius DM（Disconnect Messages）请求消息，将该计费
用户信息（包括用户名称、用户IP地址、用户计费ID等）下发到设备，设备能够断开指定SCVPN认证用户的连接
并结束计费。
配置Radius动态授权
开启/关闭Radius动态授权功能
默认情况下，Radius动态授权功能是关闭的。开启或关闭Radius动态授权功能，在全局配置模式下，使用
以下命令：
l
开启：radius-server dynamic-authorization enable
l
关闭：no radius-server dynamic-authorization enable
注意: 如果需要使用Radius动态授权功能，请先开启并配置Radius服务器的计费功能。具体配置
方法，请参阅“"配置RADIUS服务器的计费功能" 在第1269页”。
配置Radius动态授权服务器
配置用来发送动态授权请求的Radius授权服务器信息，在全局配置模式下，使用以下命令：
radius-server dynamic-authorization {server-ip ip-address [destination-ip destination-ip]}
{secret key-string}
l
server-ip ip-address- 指定Radius授权服务器的IP地址（IPv4地址或IPv6地址）。
l
destination-ip destination-ip - 指定授权请求的目的IP地址，该选项为选配项。
l
secret key-string - 指定Radius授权服务器的共享密钥，字符串范围为1到31个字符。
在全局配置模式下，使用该命令no的形式删除Radius授权服务器配置：
no radius-server dynamic-authorization server-ip ip-address

<!-- 来源页 1279 -->
配置动态授权端口号
配置动态授权的端口号，在全局配置模式下，使用以下命令：
radius-server dynamic-authorization port port-number
l
port-number- 指定动态授权的端口号，默认值是3799。取值范围是1024到65535。
在全局配置模式下，使用该命令no的形式恢复端口号的默认值：
no radius-server dynamic-authorization port
查看Radius授权服务器配置信息
查看Radius授权服务器配置信息，在任意模式下，使用以下命令：
show radius-server dynamic-authorization

<!-- 来源页 1280 -->
Web认证
Web认证功能用来对通过设备访问Internet的用户进行身份认证。配置Web认证功能后，打开浏览器访问互
联网页面会被重定向到Web认证登录页面，根据认证方式的不同，用户需要在该页面提供正确的认证信
息；Web认证成功后，系统会按照策略配置给IP地址分配角色，从而实现设备对不同用户的访问控制。
Web认证是指通过打开认证界面进行认证的方式。包括多种认证方式：口令认证、短信认证、NTLM认证、
OAuth2认证。
l 口令认证：通过用户名和密码的方式实现Web认证。
l 短信认证：通过短信认证的方式实现Web认证。用户需要在登录页面输入用于接收验证码的手机号码，然后再输
入收到的手机短信验证码，才可以通过认证。
l NTLM认证：认证过程为安全设备自动获取用户本地PC端的登录用户信息，验证用户身份。
l OAuth2认证：用户需要在Web认证登录页面点击Oauth2认证图标，跳转至Oauth2服务器登录页面，输入
Oauth2服务器的用户名和密码，才可以通过认证。
HTTPS协议方式触发认证仅支持单边SSL代理。客户端进行认证时，系统启动SSL连接，认证通过后，SSL代
理不再工作，客户端与服务器之间直接交互。
另外，系统支持自行指定Web认证页面功能，具体信息请参考“定制认证登录页面”。
注意: NTLM认证模式仅支持Windows server 2008之前版本的Active-Directory服务器。
相关链接：
Web认证在CLI的配置包含：
l "配置Web认证" 在第1278页
配置Web认证
进入Web认证配置模式
进入Web认证配置模式，在全局配置模式下使用以下命令：
webauth
开启/关闭Web认证功能
默认情况下，系统的Web认证功能是关闭的。在Web认证配置模式下，使用以下命令开启系统的Web认证
功能：

<!-- 来源页 1281 -->
开启Web认证：enable
在Web认证配置模式下，使用以下命令关闭系统的Web认证功能：
disable
指定Web认证模式
Web认证包括口令认证、短信认证、NTLM认证三种认证模式。
Web认证模式根据组合方式又可以分为单一认证模式以及组合认证模式。OAuth2认证支持在短信认证、口
令认证、口令认证/短信认证三种认证模式中组合使用。
指定单一认证模式
指定Web认证模式，在Web认证配置模式下，使用以下命令：
mode { password | sms | ntlm}
l
password – 指定口令认证模式。
l
sms – 指定短信认证模式。
l
ntlm – 指定NTLM认证模式。
指定组合认证模式
用户可以指定Web认证组合认证模式。

<!-- 来源页 1282 -->
l
通过口令认证方式或者短信认证方式进行Web认证，如下图所示：
指定Web认证组合认证模式，在Web认证配置模式下，使用以下命令：
mode password-sms
l
password-sms – 指定可以在Web认证登录页面选择通过口令认证方式或者短信认证方式进行认证。
在Web认证配置模式下，使用以上两个命令no的形式恢复默认口令认证方式：
no mode
指定认证协议类型
Web认证协议类型包括HTTP和HTTPS。HTTP模式更为快捷，而HTTPS模式更为安全。指定认证协议类型，
在Web认证配置模式下，使用以下命令：
protocol {http | https}
l
http | https – 指定HTTP或者HTTPS认证协议类型。
在Web认证配置模式下，使用命令no的形式恢复默认认证协议类型HTTP：
no protocol

<!-- 来源页 1283 -->
指定接口的Web认证全局默认配置
开启Web认证功能后，所有接口的Web认证功能是默认关闭的。指定所有接口的Web认证全局默认配置，
在Web认证配置模式下，使用以下命令：
interface global-default {enable | disable}
l
enable – 指定所有接口默认开启Web认证功能。
l
disable – 指定所有接口默认关闭Web认证功能
配置指定接口的Web认证功能，参见开启/关闭指定接口的Web认证功能。
配置认证服务器端口号
用户可以指定认证服务器的HTTP和HTTPS的端口号。在Web认证配置模式下，使用以下命令：
http-port port-number
l
port-number – 指定认证服务器的HTTP端口号。取值范围是1到65535。默认值是8181。
https-port port-number
l
port-number – 指定认证服务器的HTTPS端口号。取值范围是1到65535。默认值是44433。
使用以上两个命令no的形式恢复HTTP或者HTTPS的默认端口号：
no http-port
no https-port
注意: HTTP与HTTPS的端口号不能相同。
配置HTTP代理服务器端口号
开启Web认证后，设备默认只对用户发起的目的端口为80端口的HTTP请求进行Web认证。当用户通过浏览
器访问网络的流量需要发送给HTTP代理服务器进行代理时，需要在设备上设置HTTP代理服务器端口号，使
得发送给HTTP代理服务器的流量也进行Web认证。
配置HTTP代理服务器端口号，在Web认证配置模式下，使用以下命令：
proxy-port port-number
l
port-number – 指定HTTP代理服务器用来代理HTTP请求的端口号。取值范围是1到65535。
使用no proxy-port命令取消HTTP代理服务器端口号设置，设备将不对80端口外的任何端口的流量进行
Web认证。

<!-- 来源页 1284 -->
在使用此功能的同时，为了使用户能够进行Web认证，需要在用户浏览器中将设备的IP地址加入到浏览器
“代理服务器设置”的“例外情况”列表中。
指定HTTPS信任域
指定HTTPS信任域的名称。在Web认证配置模式下，使用以下命令：
https-trust-domain trust-domain-name
l
trust-domain-name – 指定HTTPS信任域的名称。此PKI信任域已经建立，并且已经导入从国际CA认
证中心购买的证书。
在Web认证配置模式下，使用no https-trust-domain命令恢复默认指定的信任域trust_domain_
default。
指定HTTPS证书链
Web认证功能支持配置HTTPS证书链，配置后，当通过HTTPS流量触发Web认证时，防火墙会向客户端返
回证书链中证书的数字签名，该证书与客户端安装的证书链根CA证书组成一条完整的证书信任链。如果整个
证书信任链上的各个证书都有效，客户端浏览器就会认定当前用户的证书是有效和受信任的，不会弹出“你
的链接不是私密链接”的告警提示信息。
指定HTTPS证书链的名称。在Web认证配置模式下，使用以下命令：
https-cert-chain cert-chain-name
l
cert-chain-name - 指定HTTPS证书链的名称，此证书链为系统中已经配置完成的证书链。关于如何
配置证书链，请参阅配置证书链。
在Web认证配置模式下，使用no https-cert-chain命令删除指定的证书链。
注意: 如果指定了HTTPS证书链，请注意如下事项：
l
防火墙端和客户端构成的证书链等级必需连续。例如，对于一个3级证书链，如果防火墙端配
置的证书链等级为2级和3级，客户端则需要安装1级证书链。
l
客户端需要安装证书链的根CA证书。
l
配置HTTPS证书链之前如果已经配置了HTTPS信任域，需要先取消HTTPS信任域的配置。
l
HTTPS证书链的优先级高于默认信任域。
l
防火墙端配置的证书链的证书中要包含“使用者可选名称”项，该项内容为开启了Web认证功
能的接口的IP地址或者域名。

<!-- 来源页 1285 -->
指定地址类型
默认情况下，认证用户的地址类型为IP。指定认证用户的地址类型为IP或MAC，在Web认证配置模式下，使
用以下命令：
address-type {ip | mac}
l
ip – 指定认证用户的地址类型为IP。
l
mac – 指定认证用户的地址类型为MAC。设备需与客户端部署在同一个二层网络环境中，否则系统获取
客户端的MAC地址失败或者获取到的MAC地址错误。
在Web认证配置模式下，使用no address-type命令恢复默认地址类型。
配置Web认证用户同名登录功能
用户同名登录功能指允许同一个用户在多个客户端同时登录。系统默认状态不开启此功能。开启Web认证用
户同名登录功能，允许同一用户在不同的客户端上登录，在Web认证配置模式下，输入以下命令：
multi-logon
执行该命令后，用户同名登录功能开启，用户可以对同一用户名的登录个数做限制。在Web认证配置模式下
通过使用以下命令指定用户同名登录个数：
multi-logon number
l
number – 指定用户同名登录个数。范围是2到1000。
在Web认证配置模式下使用该命令no的形式关闭用户同名登录功能：
no multi-logon
配置拒绝同名登录功能
拒绝同名登录功能指只允许同一用户在一个客户端登录。当同一用户再次登录时，可以根据配置踢出已登录
用户或者禁止同名用户再次登录。
踢出已登录用户，即当同一用户再次登录的信息会替换掉已登录的信息，系统自动断开已登录用户的连接。
在Web认证配置模式下，输入以下命令：
auto-kickout
禁止同名用户再次登录，在Web认证配置模式下，输入以下命令：
no auto-kickout

<!-- 来源页 1286 -->
开启/关闭Web主动认证
用户可以在设备的三层接口下开启Web主动认证功能。开启后，用户可通过访问Web认证地址主动发起认证
请求，然后在认证登录页面填写正确的用户名和密码即可进行认证。Web认证地址为该接口的IP地址+认证
服务器的HTTP或HTTPS的端口号，如接口的IP地址为192.168.3.1，认证服务器HTTP和HTTPS的端口号被
分别配置为8182、44434，则认证服务器配置为HTTP模式时，Web认证地址为：http://
192.168.3.1:8182；认证服务器配置为HTTPS模式时, Web认证地址为https:// 192.168.3.1:44434。
在设备的接口模式下，使用以下命令开启Web主动认证：
webauth aaa-server aaa-server-name
l
aaa-server-name – 指定系统中已经配置的AAA服务器的名称。
在设备接口模式下，使用该命令no的形式关闭Web主动认证：
no webauth aaa-server
注意:
l
在接口下开启Web主动认证功能时，需保证系统的Web认证功能开启，否则该功能不生效。
l
若认证服务器的HTTP和HTTPS的端口号为协议的默认端口80和443，则认证地址的端口号可
以省略。
l
主动认证只支持口令认证和短信认证模式，若系统已配置为NTLM认证模式，则主动认证将以
口令认证的方式生效。
开启/关闭指定接口的Web认证功能
开启Web认证功能后，该设备所有接口的Web认证功能默认是关闭的。开启指定接口的Web认证功能，在
接口配置模式下，使用以下命令：
webauth enable
关闭指定接口的Web认证功能，在接口配置模式下，使用以下命令：
webauth disable
指定接口Web认证功能使用全局默认配置，在接口配置模式下，使用以下命令：
webauth global-default
l
建议在开启Web认证功能后使用该命令，否则该配置无效。
l
关于Web认证功能全局默认配置，参见指定接口的Web认证全局默认配置。

<!-- 来源页 1287 -->
配置Web认证地址的域名
为Web认证地址配置域名后（即为接口IP配置对应的域名），访问服务时弹出的Web认证页面（被动认证）
的URL将显示为域名形式。配置该功能前，需先开启Web认证功能。
配置Web认证地址的域名，在接口配置模式下，使用以下命令：
webauth domain domain-name
l
domain-name - 指定Web认证地址的域名，取值范围是1到255个字符。
删除Web认证地址的域名配置，在接口配置模式下，使用以下命令：
no webauth domain
强制断开用户连接
系统可以通过命令强制断开某个用户与认证系统的连接。强制断开用户连接，在任何模式下，使用以下命
令：
exec user-mapping webauth kickout {{ip ip-address| mac mac-address} vrouter vroutername | username username { auth-server auth-server-name}}
l
ip-address – 指定Web认证用户的IP地址。
l
mac-address – 指定Web认证用户的MAC地址。
l
vrouter -name– 指定Web认证用户的VRouter。
l
username – 指定Web认证用户的用户名。
l
auth-server-name – 指定Web认证用户的认证服务器名称。
注意: 为避免强制断开过多同名用户与认证系统的连接，需指定VRouter或者认证服务器。
允许本地用户修改密码
系统支持本地用户通过Web认证后，在认证登录成功页面修改自己的用户密码。默认情况下，该功能为关闭
状态。在密码控制配置模式下，使用以下命令开启或关闭允许本地用户修改登录密码功能：
l
开启：allow-pwd-change
l
关闭：no allow-pwd-change
开启该功能并成功配置Web认证后，本地用户可通过以下步骤修改登录密码：

<!-- 来源页 1288 -->
1. 进行Web认证。在Web认证页面输入正确的用户名和密码，点击<登录>按钮。
2. 成功登录后，点击Web认证页面上的<修改密码>按钮，如下图所示：
3. 修改密码。在<旧密码>文本框中输入正确的旧密码，在<新密码>文本框中输入新密码并在<确认新密码>
处再次输入相同的新密码。如下图所示：

<!-- 来源页 1289 -->
4. 点击<确定>按钮，系统显示提示信息“修改密码成功”。
配置Web认证策略规则
触发系统的Web认证功能，需要配置相应的策略规则。在策略规则配置模式下，使用以下命令配置策略规则
Web认证相关参数：
指定角色：role unknown
指定Web认证行为和认证服务器：
action webauth aaa-server-name
l
aaa-server-name – 指定认证服务器，为系统中配置的AAA认证服务器。
关于如何配置策略规则，请参阅《安全策略》。

<!-- 来源页 1290 -->
定制认证登录页面
Hillstone设备支持用户自行定制Web认证登录页面。默认情况下，配置Web认证功能后，其认证登录页面
如下图所示：
定制登录页面
用户可以通过下载压缩包并修改其源文件，自行定制Web认证登录页面。引入修改后的压缩包文件到系统，
请在执行模式下使用以下命令：
import customize webauth from {ftp server ip-address [vrouter vrouter-name] [user username password password] | tftp server ip-address [vrouter vrouter-name]} file-name
l
ftp server ip-address [vrouter vrouter-name] [user user-name password password] – 指
定从FTP服务器获取压缩包文件，并指定FTP服务器的IP地址、FTP服务器所属的VRouter以及访问服务
器使用的用户名和密码。当不输入用户名和密码时表示采用匿名登录方式。
l
tftp server ip-address [vrouter vrouter-name] – 指定从TFTP服务器获取压缩包文件，并指定
TFTP服务器的IP地址以及所属的VRouter。
l
file-name – 指定压缩包名称。
恢复Web认证登录页面至默认页面，在任意模式下使用以下命令：

<!-- 来源页 1291 -->
exec customize webauth default
注意:
l
用户从以前版本升级至5.5R6版本后，以前版本中上传的Web认证登录页面不再生效，并且恢
复到系统默认页面，请在版本升级后重新下载模板进行登录页面定制。
l
用户升级版本后，请重新下载模板修改源文件后再上传自定义页面压缩包，如果上传的压缩包
与当前系统版本不一致，定制登录页面的功能会无法正常使用。
l
上传的自定义页面的压缩包需要符合以下要求：文件数量不能超过50个；上传文件格式为
zip；压缩包最大为1M；源文件中必须包含“index.html”文件。
l
系统仅保留一份默认模板页面和一份自定义页面文件，成功上传新的自定义页面后会覆盖之前
的文件，建议管理员先进行本地调试并备份之前的文件。
l
修改源文件的方法，请参阅“readme_cn.md”或“readme_en.md”文件。
导出Web认证登录页面
导出默认的Web认证登录页面的压缩包，在执行模式下使用以下命令：
export webauth default-page to {ftp server ip-address [vrouter vrouter-name] [user username password password] | tftp server ip-address [vrouter vrouter-name]} file-name
l
ftp server ip-address [vrouter vrouter-name] [user user-name password password] – 指
定导出压缩包文件到FTP服务器，并指定FTP服务器的IP地址、FTP服务器所属的VRouter以及访问服务
器使用的用户名和密码。当不输入用户名和密码时表示采用匿名登录方式。
l
tftp server ip-address [vrouter vrouter-name] – 指定导出压缩包文件到FTP服务器，并指定TFTP
服务器的IP地址以及所属的VRouter。
l
file-name – 指定压缩包名称。
口令认证
开启口令认证模式，在Web认证配置模式下，使用以下命令：
mode password
配置用户重新认证时间间隔
当用户认证成功并访问网络后，系统可以对用户进行重认证。默认情况下，系统不对用户进行重认证。在
Web认证配置模式下，使用以下命令配置用户重认证的时间间隔：
password reauth-interval {time | disable}

<!-- 来源页 1292 -->
l
time – 指定用户进行重认证的时间间隔，单位为分钟。范围为10到60*24分钟。
l
disable – 关闭重认证功能，即系统不对用户进行重认证。
在Web认证配置模式下，使用该命令no的形式恢复默认值：
no password reauth-interval
配置重定向URL功能
重定向URL功能是指用户在认证成功并返回认证页面后，弹出的新页面将会重定向到指定的URL页面。如果
没有配置该功能，新弹出页面将返回用户输入的地址页面。该功能的正确执行需要浏览器关闭弹出窗口阻止
程序。如果浏览器阻止弹出窗口，新弹出的页面将被阻止，需要手工确认才能打开。配置重定向URL，在
Web认证配置模式下，使用以下命令：
password popup-url url
l
url – 指定重定向URL的地址。范围为1到127个字符。
在Web认证配置模式下，使用该命令no的形式取消指定的重定向URL：
no password popup-url
注意:
l
系统可以通过在URL地址中指定用户名和密码，当用户指定的弹窗URL页面为内网中需认证的
应用系统页面时，无需再次认证便可以正常访问应用系统。
l
对应的关键字为$USER，$PWD或$HASHPWD参数(通常$PWD和$HASHPWD参数二选一即
可)。URL格式为“URL”+“username=$USER&password=$PWD”。
l
使用CLI指定重定向URL的地址时，如果URL地址中如果包含“？”，请用双引号引住整个
URL地址。例
如：”http://192.10.5.201/oa/login.do?username=$USER&password=$HASHPW
D”。
配置强制超时时间
系统可以通过设置强制超时时间，使用户在指定的时间过后必须重新登录。默认情况下，系统不强制用户重
新登录。在Web认证配置模式下，使用以下命令配置强制超时时间：
password force-timeout {timeout-value | disable}

<!-- 来源页 1293 -->
l
timeout-value - 指定强制超时时间，单位为分钟。范围为10到60*24*100分钟。
l
disable – 关闭强制超时时间功能，即系统不强制用户重新登录。
在Web认证配置模式下，使用该命令no的形式恢复默认值：
no password force-timeout
配置空闲超时时间
空闲超时时间指认证成功页面在无流量状态下能够保持连接状态的最长时间，超出空闲超时时间后，将会断
开连接。默认情况下，认证成功页面在无流量状态下能够持续保持连接状态。配置空闲超时时间，在Web认
证配置模式下，使用以下命令：
password idle-timeout {timeout | disable}
l
timeout – 指定空闲超时时间，单位为分钟。取值范围是1到60*24分钟。
l
disable – 关闭空闲超时时间功能，即认证成功页面在无流量状态下能够持续保持连接状态。
在Web认证配置模式下使用该命令no的形式恢复默认值：
no password idle-timeout
注意:
l
用户如果使用（iOS/Android）系统下的手机终端通过Web认证，为保证手机终端在有流量时
始终在线，请开启该功能，指定空闲超时时间。
l
SG6000-K20803/K9180/K7680/K7280/K6680/K6580和X系列设备不支持配置空闲超时
时间。
配置心跳超时时间
认证成功后，系统会在心跳超时时间结束前对认证成功页面进行自动刷新，确认登录信息。如果同时配置了
空闲超时时间和心跳超时时间，用户会在两者中的最小时间点下线。配置心跳超时时间，在Web认证配置模
式下，使用以下命令：
password heartbeat-timeout {interval | disable}
l
interval – 指定超时时间，单位为分钟。取值范围是1到60*24*100分钟。默认为10分钟。
l
disable – 关闭心跳超时时间功能。
在Web认证配置模式下，使用该命令no的形式恢复默认心跳超时时间：
no password heartbeat-timeout

<!-- 来源页 1294 -->
短信认证
系统支持通过短信认证的方式实现Web认证。配置短信认证功能后，打开浏览器访问互联网页面会被重定向
到Web认证登录页面，用户需要在登录页面输入用于接收验证码的手机号码，然后再输入收到的手机短信验
证码，才可以通过认证。
开启Web短信认证模式，在Web认证配置模式下，使用以下命令：
mode sms
配置强制超时时间
短信认证成功后，系统会在超时时间结束前对用户进行重新认证。配置超时时间，在Web认证配置模式下，
使用以下命令：
sms force-timeout {timeout-value | disable}
l
timeout-value – 指定强制超时时间，单位为分钟。取值范围是10到60*24*100分钟。默认为60分
钟。
l
disable – 关闭强制超时时间功能，即系统不强制用户重新认证。
在Web认证配置模式下，使用该命令no的形式恢复默认超时时间：
no sms force-timeout
配置空闲超时时间
空闲超时时间指短信认证成功页面在无流量状态下能够保持连接状态的最长时间，超出空闲超时时间后，将
会断开连接。默认情况下，认证成功页面在无流量状态下能够持续保持连接状态。配置短信认证空闲超时时
间，在Web认证配置模式下，使用以下命令：
sms idle-timeout {timeout | disable}
l
timeout – 指定短信认证空闲超时时间，单位为分钟。取值范围是1到60*24分钟。
l
disable – 关闭短信认证空闲超时时间，即认证成功页面在无流量状态下能够持续保持连接状态。
在Web认证配置模式下使用该命令no的形式恢复默认值：
no sms idle-timeout
配置短信验证码超时时间
用户使用Web短信认证时，需要使用手机收到的短信验证码，验证码在超时时间结束前生效。在超过超时时
间后，如果验证码没有使用，用户需要重新获取新的短信验证码。配置短信验证码超时时间，在全局配置模
式下，使用以下命令：
webauth sms-verify-code-timeout timeout-value

<!-- 来源页 1295 -->
l
timeout-value – 指定验证码超时时间，单位为分钟。取值范围是1到10分钟。默认为1分钟。
在全局配置模式下，使用该命令no的形式恢复验证码默认超时时间：
no webauth sms-verify-code-timeout
指定发送方名称或者签名
当短信网关的协议类型为SGIP或USM时，用户可以指定短信发送方名称以显示在短信内容中；当短信网关的
协议类型为ALIYUNSMS时, 用户需要输入在阿里云短信服务中申请的短信签名，以显示在短信内容中。指定
发送方名称或者短信签名，在Web认证配置模式下，使用以下命令：
sms sender-name sender-name
l
sender-name – 指定发送方名称或者签名。取值范围是1到63字符。
在Web认证配置模式下，使用该命令no的形式删除发送方名称或者签名的指定：
no sms sender-name
注意:
由于UMS企业信息平台限制，当使用短信网关发送认证短信时，发送方名称将会显示在UMS企业
信息平台注册的名称。
配置认证码长度
配置短信认证码的长度，在Web认证配置模式下，使用以下命令：
sms verification-code-length length
l
length – 指定短信认证码长度。取值范围为4至8个字符。默认为6个字符。
在Web认证配置模式下，使用no sms verification-code-length恢复默认认证码长度。
指定模板CODE
当通过阿里云短信网关发送认证短信时，用户需要指定在阿里云短信服务中申请的短信内容模板对应的
CODE（代码）。指定模板CODE，在Web认证配置模式下，使用以下命令：
sms templatecode word
l
word - 指定模板CODE，取值范围为1至30个字符。该参数需与在阿里云短信服务中申请的模板CODE
保持一致。
在Web认证配置模式下，使用no sms templatecode命令取消模板CODE的指定。

<!-- 来源页 1296 -->
指定通过短信猫发送短信
指定通过短信猫发送认证短信，在Web认证配置模式下，使用以下命令：
sms agent modem
指定通过短信网关发送短信
指定通过短信网关发送认证短信，在Web认证配置模式下，使用以下命令：
sms agent gateway sp-name
l
sp-name – 指定SP实例的名称，该名称须是已创建的SP实例名称。取值范围为1至31个字符。
NTLM认证
开启NTLM认证模式，在Web认证配置模式下，使用以下命令：
mode ntlm
注意:
l
对于IE浏览器，用户需要配置自动使用当前用户名和密码登录才可以自动完成Web认证过程。
l
对于非IE浏览器，用户每次访问网络资源时都需要在弹出的提示框中输入用户名和密码。
l
NTM认证模式仅支持Windows server 2008之前版本的Active-Directory服务。
配置强制超时时间
认证只会在用户完成Active Directory服务器认证后有限的时间内生效，超时后用户仍需在Web认证页面输
入有效的用户名和密码重新登录才可以继续访问网络资源。配置NTLM认证重新登录时间，在Web认证配置
模式下，使用以下命令：
ntlm force-timeout {timeout-value | disable}
l
timeout-value - 指定强制超时时间，单位为分钟。范围为10到60*24*100分钟。默认值为600分钟。
l
disable – 关闭强制超时时间，即系统不强制用户重新登录。
使用该命令no的形式恢复默认值：
no ntlm force-timeout
配置认证模式兼容
由于NTLM认证仅适用Windows系统用户，为了保证全部用户进行身份验证，可开启设备认证模式兼容功
能。认证模式兼容功能是指在启用NTLM认证后，当用户认证失败时，可指定认证模式为用户名/密码认证。
默认情况下，NTLM认证失败后系统不执行任何操作，即认为认证失败。在Web认证配置模式下，使用以下

<!-- 来源页 1297 -->
命令：
ntlm fallback-to-webform
在Web认证配置模式下，使用以下命令恢复默认设置：
no ntlm fallback-to-webform
配置NTLM认证空闲超时时间
空闲超时时间指认证成功页面在无流量状态下能够保持连接状态的最长时间，超出空闲超时时间后，将会断
开连接。默认情况下，认证成功页面在无流量状态下能够持续保持连接状态。配置NTLM认证空闲超时时
间，在Web认证配置模式下，使用以下命令：
ntlm idle-timeout {timeout | disable}
l
timeout – 指定短信认证空闲超时时间，单位为分钟。取值范围是1到60*24分钟。
l
disable – 关闭空闲超时时间功能，即认证成功页面在无流量状态下能够持续保持连接状态。
在Web认证配置模式下使用该命令no的形式恢复默认值：
no ntlm idle-timeout
OAuth2认证
系统支持通过OAuth2认证的方式实现Web认证。配置OAuth2认证功能后，打开浏览器访问互联网页面会
被重定向到Web认证登录页面，用户需要在登录页面点击OAuth2认证图标，跳转至OAuth2服务器登录页
面，输入OAuth2服务器的用户名和密码，才可以通过认证。
启用/禁用OAuth2认证模式
默认情况下，OAuth2认证是禁用状态。启用/禁用OAuth2认证模式，在Web认证配置模式下，使用以下命
令：
oauth {enable | disable}
l
enable– 启用OAuth2认证。
l
disable– 禁用OAuth2认证。
绑定OAuth2服务器
启用OAuth2认证时，需要同时绑定OAuth2服务器，OAuth2认证才能生效。绑定OAuth2服务器，在Web
认证配置模式下，使用以下命令：
oauth server aaa-server-name
l
aaa-server-name– 指定需要绑定的OAuth2服务器。最多绑定3个OAuth2服务器。

<!-- 来源页 1298 -->
在Web认证配置模式下，使用该命令no的形式取消对OAuth2服务器的绑定：
no oauth server aaa-server-name
配置OAuth2认证强制超时时间
系统可以通过设置强制超时时间，使用户在指定的时间过后必须重新登录。默认情况下，系统不强制用户重
新登录。配置OAuth2认证强制超时时间，在Web认证配置模式下，使用以下命令：
oauth force-timeout {timeout-value | disable}
l
timeout-value – 指定强制超时时间，单位为分钟。取值范围是10到60*24*100分钟。
l
disable – 关闭强制超时时间功能，即系统不强制用户重新登录。
在Web认证配置模式下，使用该命令no的形式恢复默认超时时间：
no oauth force-timeout
配置OAuth2认证心跳超时时间
认证成功后，系统会在心跳超时时间结束前对认证成功页面进行自动刷新，确认登录信息。如果同时配置了
空闲超时时间和心跳超时时间，用户会在两者中的最小时间点下线。配置OAuth2认证心跳超时时间，在
Web认证配置模式下，使用以下命令：
oauth heartbeat-timeout {timeout-value | disable}
l
timeout-value – 指定心跳超时时间，单位为分钟。取值范围是1到60*24分钟。默认为10分钟。
l
disable – 关闭心跳超时时间功能。
在Web认证配置模式下，使用该命令no的形式恢复默认心跳超时时间：
no oauth heartbeat-timeout
配置OAuth2认证空闲超时时间
空闲超时时间指认证成功页面在无流量状态下能够保持连接状态的最长时间，超出空闲超时时间后，将会断
开连接。默认情况下，认证成功页面在无流量状态下能够持续保持连接状态。配置OAuth2认证空闲超时时
间，在Web认证配置模式下，使用以下命令：
oauth idle-timeout {timeout | disable}
l
timeout – 指定空闲超时时间，单位为分钟。取值范围是1到60*24分钟。
l
disable – 关闭空闲超时时间功能，即认证成功页面在无流量状态下能够持续保持连接状态。默认是关
闭空闲超时时间功能。
在Web认证配置模式下，使用该命令no的形式恢复默认心跳超时时间：

<!-- 来源页 1299 -->
no oauth idle-timeout
显示Web认证配置信息
在任意模式下，使用以下命令查看当前Web认证配置信息：
show webauth
在任意模式下，使用以下命令查看所有Web认证配置信息：
show webauth detail
显示在线Web认证用户信息
在任意模式下，使用以下两条命令查看在线的Web认证用户信息：
show auth-user {webauth-ntlm | webauth-password | webauth-sms | webauth-oauth}
[interface interface-name | vrouter vrouter-name]
show user-mapping webauth [ip ip-address | mac mac-address] [vrouter vrouter-name]

<!-- 来源页 1300 -->
单点登录
单点登录介绍
单点登录（SSO，Single Sign-On）指用户通过一次认证之后，系统通过某种方式获取其认证信息，之后
该用户不需要再次在设备上进行认证，即用户可以实现“免认证”上网。
单点登录有多种实现方式，互相独立，均可实现“免输入”（不输入用户名、密码）认证。实现方式如下表
所示：
实现方式
安装软件或脚本
描述
SSO Radius
---
启用SSO Radius功能后，系统可接收基于Radius标准协议的计费报
文，并根据报文内容获取用户认证信息、更新在线用户信息以及对用户
进行上下线操作。
SSO Web
---
启用SSO Web功能后，SSO Web客户端（第三方认证系统）可以通过
HTTP(S) RESTful API请求向StoneOS系统发送用户上下线报文和用户
信息更新报文，StoneOS系统根据报文内容获取用户认证信息，进行在
线用户信息更新及用户上下线操作，实现单点登录以及基于用户组和角
色的策略控制。
SSO Monitor
---
启用SSO Monitor功能后，StoneOS系统通过SSO-Monitor协议与第三
方认证服务器建立连接并获取用户在线状态及所属用户组信息，并实时
更新用户名和IP的映射关系。
AD Scripting
脚本文件
Logonscript.exe
在AD服务器上安装脚本文件“Logonscript.exe”，通过脚本文件将上
线用户发送给StoneOS系统。
AD Polling
---
启用AD Polling功能后，StoneOS系统定时查询并获取AD服务器上的
上线用户信息，并定时探测在线用户是否下线。
Radius
Snooping
---
Radius为远程认证拨入用户服务，是用于NAS和AAA服务器间通信的
一种协议。Radius Snooping通过解析镜像到设备上的Radius报文，
系统将自动获取认证用户的用户名和IP地址对应关系，用于为设备日志
功能模块提供对认证用户的审计功能。
Agile
Controller
---
启用Agile Controller功能后，系统可接收Agile Controller服务器发送
的用户上下线报文和用户信息更新报文，根据报文内容获取用户认证信
息，并进行在线用户上下线及在线用户信息更新操作。
TS Agent
软件Hillstone Terminal
Service Agent
在Windows服务器上安装并运行Hillstone Terminal Service Agent软
件。启用TS Agent功能后，当用户通过远程桌面服务登录Windows服
务器时，Hillstone Terminal Service Agent为用户分配端口段，并将
端口段和用户信息发送给设备，设备创建基于流量IP、端口段和用户的
映射信息，实现用户的“免登录”。

<!-- 来源页 1301 -->
实现方式
安装软件或脚本
描述
SAML
---
SAML单点登录是一种基于XML标准的身份验证机制，允许用户通过一
次登录访问多个相互信任的应用系统，无需重复输入凭证。启用并配置
SAML单点登录方案后，用户可以在防火墙登录界面使用SAML方式进
行登录。
云·界单点登录方案
仅虚拟化产品云·界支持该功能。开启该功能并配置第三方平台对应的单点登录方案后，用户可在登录第三方
平台后，直接访问云·界而无需输入用户名和密码。
SSO Radius单点登录
接收Radius计费报文
设备可接收符合Radius标准协议的计费报文，并根据报文内容，生成对应的用户认证信息并加入认证用户
表、重置用户保活定时器以及删除已认证用户。
使设备接收Radius计费报文、分析报文内容以及采取相应动作，需要进行如下配置：
在全局配置模式下，使用如下命令，进入SSO-Radius配置模式：
user-sso server sso-radius default
在sso-radius配置模式下，使用如下命令：
enable
关闭设备接收Radius计费报文功能，在SSO-Radius配置模式下，使用no enable。
注意: 执行开启操作后，必须间隔5秒以上才能执行关闭操作。同理，执行关闭操作后，必须间隔5
秒以上才能执行开启操作。如果当前业务量较大，间隔时间可能会延长。
指定AAA服务器
指定用户所属的AAA服务器。指定AAA服务器，在SSO-Radius配置模式下，使用以下命令：
aaa-server aaa-server-name
l
aaa-server-name – 指定AAA服务器的名称。AAA服务器支持选择Local、AD或者LDAP类型的服务
器。选择AAA服务器后，系统可以在引用的AAA服务器上查询在线用户的用户名对应的用户组和角色信
息，从而实现基于用户组和角色的策略控制。
在SSO-Radius配置模式下使用该命令no的形式取消对AAA服务器的指定：

<!-- 来源页 1302 -->
no aaa-server
指定设备接收Radius报文的端口号
指定设备接收Radius报文的端口号（不可在非根VSYS中配置端口），在SSO-Radius配置模式下，使用如
下命令：
port port
l
port – 指定端口号。取值范围1~65535。默认端口号1813。
使用no port命令恢复默认端口号。
配置Radius客户端
指定Radius客户端的IP地址。最多支持指定8条记录。指定IP地址后，进入SSO Radius客户端配置模式。
指定SSO Radius客户端的IP地址并进入SSO Radius客户端配置模式，在SSO-Radius配置模式下，使用如
下命令：
client {any | A.B.C.D| X:X:X:X::X}
l
any – 接收任意SSO Radius客户端发送的报文。
l
A.B.C.D – 接收指定IP地址的SSO Radius客户端发送的报文。
l
X:X:X:X::X –接收指定IPv6地址的SSO Radius客户端发送的报文。仅当系统版本为IPv6版本时可指
定。
删除所设置的SSO Radius客户端，在全局配置模式下，使用no client {any | A.B.C.D| X:X:X:X::X} 命
令。
配置共享密钥
设备使用共享密钥校验报文，校验成功后，才会对报文进行解析，否则丢弃报文。SSO Radius客户端需要
配置与设备相同的共享密钥，或者SSO Radius客户端和设备都不配置共享密钥，报文才能通过校验。配置
共享密钥，在SSO Radius客户端配置模式下，使用如下命令：
shared-secret key-value
l
key-value – 指定共享密钥。长度1-31个字符。
清除共享秘钥，使用no shared-secret命令。
配置心跳超时时间
心跳超时时间用来设置Radius报文中的用户认证信息在设备中的存活时间。如果在心跳超时时间内未收到此
用户相关更新或删除报文，设备将删除用户认证信息。

<!-- 来源页 1303 -->
在SSO Radius客户端配置模式下，使用如下命令配置心跳超时时间：
heartbeat-timeout time
l
time – 指定心跳超时时间。单位分钟。取值范围是0-1440。默认值为30。如果设置为0，则代表永不超
时。
恢复默认心跳超时时间，在SSO Radius客户端配置模式下，使用no heartbeat-timeout命令。
禁用心跳超时时间，在SSO Radius客户端配置模式下，使用heartbeat-timeout disable命令。
指定空闲超时时间
空闲超时时间指认证用户在无流量状态下保持认证状态的最长时间。超出空闲超时时间后，设备删除用户认
证信息。
指定空闲超时时间，在SSO Radius客户端配置模式下，使用以下命令：
idle-timeout time
l
time– 指定空闲超时时间，单位为分钟。取值范围是0-1440，默认值为0。如果设置为0，则关闭该功
能，认证用户在无流量状态下永不超时。
恢复空闲超时时间的默认值，在SSO Radius客户端配置模式下，使用no idle-timeout命令。
禁用空闲超时时间，在SSO Radius客户端配置模式下，使用idle-timeout disable命令。
指定强制超时时间
当用户在线时长超过配置的强制超时时间后，系统会强制用户下线。
指定强制超时时间，在SSO Radius客户端配置模式下，使用以下命令：
force-timeout time
l
time– 指定强制超时时间。单位为分钟。取值范围是0-1440，默认值为0。如果设置为0或输入
disable，则关闭该功能。
恢复强制超时时间的默认值，在SSO Radius客户端配置模式下，使用no force-timeout命令。
禁用强制超时时间，在SSO Radius客户端配置模式下，使用force-timeout disable命令。
显示SSO Radius配置信息
显示SSO Radius配置信息，在任意模式下，使用如下命令：
show user-sso server sso-radius default

<!-- 来源页 1304 -->
查看用户映射信息
查看SSO Radius的用户名和IP映射信息。在任意模式下，使用以下命令：
show user-mapping user-sso sso-radius default
查看认证用户表
设备生成的用户认证信息保存在用户认证表。在任意模式下，使用以下命令：
show auth-user sso-radius
踢出用户映射信息
踢出某指定IP的用户和IP的映射信息。在任意模式下，使用以下命令：
exec user-mappping user-sso sso-radius kickout ip ip-address vrouter vrouter-name
SSO Web单点登录
防火墙支持通过SSO Web功能，与第三方认证系统（如盈高认证系统）对接，实现单点登录以及基于用户组
和角色的策略控制，主要包括：
l 防火墙设备与第三方认证系统进行对接，第三方认证系统通过HTTP(S) RESTful API请求向防火墙发送用户上下
线报文和用户信息更新报文，防火墙根据报文内容获取用户认证信息。
l 当认证用户访问防火墙设备时，根据同步的认证用户信息，进行在线用户信息更新及用户上下线操作，实现单点
登录以及基于用户组和角色的策略控制。
SSO Web单点登录典型场景
SSO Web单点登录典型场景如下说明：
1. 用户通过第三方认证系统进行身份认证。
2. 第三方认证系统通过HTTP(S) RESTful API请求将用户认证信息发送给防火墙。
根据发送的用户认证消息以及防火墙中AD服务器配置的不同，防火墙获取用户的用户组或者角色信息的方法不

<!-- 来源页 1305 -->
同，分为以下四种情况：
l 如果发送给防火墙的用户认证信息中包含用户的用户组或者角色信息，防火墙直接获取到用户的用户组或
者角色信息；
l 如果发送给防火墙的用户认证信息中不包含用户组信息，且防火墙中AD服务器的同步对象配置为用户和
用户组，防火墙可以从AD服务器同步的数据中查找用户所属的用户组；
l 如果发送给防火墙的用户认证信息中不包含用户组信息，且防火墙中AD服务器的同步对象配置为仅同步
用户、仅同步用户组或者用户和用户组均不同步时，防火墙可以通过AD服务器查询用户所属的用户组；
l 如果发送给防火墙的用户认证信息中不包含角色信息，且防火墙中AD服务器配置了角色映射规则，防火
墙可以根据角色映射规则为用户映射角色。
3. 防火墙基于用户组或者角色对用户进行网络访问控制，且用户进行网络访问时，无需再次进行认证。
配置SSO Web单点登录
配置SSO Web单点登录，可按照以下流程进行配置：
1. 配置SSO Web引用的AAA服务器：Local、Active-Directory或者LDAP类型的服务器。
2. 在防火墙设备中配置SSO Web功能。
3. 在第三方认证系统中构建HTTP(S) RESTful API请求。
4. 查看SSO Web配置/认证用户信息/用户映射信息
5. （可选）踢出SSO Web用户
配置SSO Web功能
进入SSO Web配置模式
进入SSO Web配置模式，在全局配置模式下，使用以下命令：
user-sso server sso-web default
开启/关闭SSO Web功能
默认情况下，系统的SSO Web功能是关闭的。开启或者关闭SSO Web功能，在SSO Web配置模式下，使用
以下命令：
l
启用：enable
l
关闭：no enable

<!-- 来源页 1306 -->
指定AAA服务器
指定用户所属的AAA服务器，在SSO Web配置模式下，使用以下命令：
aaa-server aaa-server-name
l
aaa-server-name – 指定AAA服务器的名称。AAA服务器支持选择已配置的Local、AD或者LDAP类
型的服务器。选择AAA服务器后，系统可以在引用的AAA服务器上查询在线用户的用户名对应的用户组
和角色信息，从而实现基于用户组和角色的策略控制。默认为本地服务器local。
在SSO Web配置模式下使用该命令no的形式恢复默认本地服务器local：
no aaa-server
指定强制超时时间
指定强制超时时间，在SSO Web配置模式下，使用以下命令：
force-timeout time
l
time - 指定强制超时时间。用户上线后，如果系统在强制超时时间内没有收到用户的信息更新请求，会
踢出用户，强制用户下线。取值范围是0到1440分钟。默认值为0，即永不强制用户下线。
在SSO Web配置模式下，使用该命令no的形式恢复默认值：
no force-timeout
指定可信客户端地址范围
指定可信客户端地址范围，在SSO Web配置模式下，使用以下命令：
trust-client-address address-book
l
address-book- 指定可信客户端地址范围。仅可信地址范围内的SSO Web客户端可以通过HTTP(S)
RESTful API请求向StoneOS系统发送用户上下线报文和用户信息更新报文。可以指定系统中已创建的
IPv4或者IPv6地址簿条目，默认值为Any，即任意IPv4地址的SSO Web客户端都可以通过HTTP(S)
RESTful API请求向StoneOS系统发送用户上下线报文和用户信息更新报文。
在SSO Web配置模式下，使用该命令no的形式恢复默认值：
no trust-client-address

<!-- 来源页 1307 -->
在第三方认证系统中构建HTTP(S) RESTful API请求
注意:
l
与第三方认证系统通信的防火墙接口需要开启HTTP或HTTPS服务。
l
第三方认证系统IP地址需要在防火墙可信主机范围内。
第三方认证系统的运维人员使用开发工具在第三方认证系统代码中构建HTTP(S) RESTful API请求。第三方认证系统
对用户认证成功后，将用户认证信息同步给防火墙。
RESTful API请求的格式如下：
l 用户上线请求：http(s)://防火墙IP/rest/api/sso-web-user?opr=login&info=USERINFO
l 用户下线请求：http(s)://防火墙IP/rest/api/sso-web-user?opr=logout&info=USERINFO
参数说明：
l 防火墙IP：接受用户认证信息的防火墙设备IP地址。
l opr：仅支持上线（login）和下线（logout）两种消息类型
l info=USERINFO：上线或下线的用户信息。USERINFO为认证用户的UserIP、UserName、Group、Role信息的
base64编码，需在第三方认证系统代码中按照格式自行转换生成。UserIP和UserName为必填项，Group和
Role为可选项，支持多个Group，仅支持一个Role。USERINFO编码前格式如下：
认证用户内容
USERINFO编码前格式
只包含用户IP、用户名
UserIP/UserName//
包含用户IP、用户名和Group
UserIP/UserName//Group
包含用户IP、用户名和Role
UserIP/UserName////role=Role
包含用户IP、用户名、Group、Role
UserIP/UserName//Group//role=Role
包含用户IP、用户名、多个Group、Role
UserIP/UserName//Group1//Group2//role=Role
例如：UserIP=120.1.1.163，UserName=qa_user1，Group=QA_Group，Role=RnD-Group，防火
墙的IP地址为10.182.12.34，所以USERINFO为"120.1.1.163/qa_user1//QA_Group//role=RnDGroup"，第三方系统进行base64编码后的结果是
MTIwLjEuMS4xNjMvcWFfdXNlcjEvL1FBX0dyb3VwLy9yb2xlPVJuRC1Hcm91cA==
因此，第三方系统下发的该用户上线/下线请求如下：
l 上线请求：http(s)://10.182.12.34/rest/api/sso-webuser?opr=login&info=MTIwLjEuMS4xNjMvcWFfdXNlcjEvL1FBX0dyb3VwLy9yb2xlPVJuRC1Hcm91cA==

<!-- 来源页 1308 -->
l 下线请求：http(s)://10.182.12.34/rest/api/sso-webuser?opr=logout&info=MTIwLjEuMS4xNjMvcWFfdXNlcjEvL1FBX0dyb3VwLy9yb2xlPVJuRC1Hcm91cA==
查看SSO Web配置/认证用户信息/用户映射信息
查看SSO Web配置
查看SSO Web配置，包括启用状态、强制超时时间、AAA服务器、可信客户端地址范围。在任意模式下，
使用以下命令：
show user-sso server sso-web default
查看SSO Web认证用户信息
查看SSO Web用户认证信息。在任意模式下，使用以下命令：
l
查看系统控制层面的SSO Web用户认证信息：show auth-user sso-web
l
查看系统数据层面的SSO Web用户认证信息：show dp-auth-user sso-web
查看SSO Web用户映射信息
查看SSO Web的用户映射关系。在任意模式下，使用以下命令：
show user-mapping user-sso sso-web
踢出SSO Web用户
踢出SSO Web用户并删除用户和IP映射关系，支持踢出指定IP的用户，以及踢出指定用户名的用户。在任意
模式下，使用以下命令：
exec user-mappping user-sso sso-web kickout {ip ip-address vrouter vrouter-name |
username user-name auth-server server-name}
SSO Monitor单点登录
SSO Monitor单点登录可以将外部服务器上保存的用户在线状态通过SSO Monitor规定的协议报文同步至防
火墙，在防火墙上生成认证用户，并实时更新在线用户的用户名与IP（可以为IPv4地址或者IPv6地址）绑定
关系，而且支持提取报文中的用户所属用户组信息，使用户免于二次登录。
StoneOS并不限制外部服务器形式和类型，只要它能在SSO Monitor协议中充当TCP连接的服务端，向防火
墙同步用户信息，即可将其视作可以对接的外部服务器，例如AD Agent软件。

<!-- 来源页 1309 -->
注意: 在StoneOS 5.5R10之前的版本上，在需要使用AD Agent软件获取用户信息时，可以通过
SSO Monitor对接AD Agent软件，也可以通过在Active Directory服务器配置模式下配置AD服
务监控功能。从StoneOS 5.5R10版本开始，系统不再支持配置AD服务监控功能。在版本升级到
StoneOS 5.5R10后，系统中已配置的AD服务监控功能会自动转换成SSO Monitor功能对接AD
Agent软件配置。可通过“show user-sso client sso-monitor[ profile-name]”查看配置，
转换后的SSO Monitor Profile名称与AD服务器名称相同。
创建SSO Monitor Profile
创建SSO Monitor profile并进入SSO-Monitor配置模式，在全局配置模式下，输入以下命令：
user-sso client sso-monitor profile-name
l
profile-name - 指定所创建的SSO Monitor profile的名称。执行该命令后，系统将创建指定名称的
SSO Monitor profile，并进入SSO-Monitor配置模式；如果指定的SSO Monitor profile名称已存
在，则直接进入SSO-Monitor配置模式。
在全局配置模式下使用该命令的no形式删除指定的SSO Monitor profile：
no user-sso client sso-monitor name
开启/关闭SSO Monitor功能
启用SSO Monitor功能后，系统通过SSO-Monitor协议与外部服务器建立连接并获取用户在线状态及所属
用户组信息（可选），并实时更新在线用户的用户名/IP绑定信息。
开启SSO Monitor功能，在SSO-Monitor配置模式下，使用以下命令：
enable
关闭SSO Monitor功能，在SSO-Monitor配置模式下，使用以下命令：
no enable
配置用户地址范围
用户可以关联已配置的地址簿，在生成认证用户时，只生成在IP范围内的用户。指定用户地址范围，在SSOMonitor配置模式下，使用以下命令：
user-address address-entry
l
address-entry - 指定地址簿中已配置的地址条目的名称。
在SSO-Monitor配置模式下，使用no user-address命令删除关联的地址簿条目。

<!-- 来源页 1310 -->
配置用户虚拟路由器
指定生成的认证用户所属的虚拟路由器。若不配置，则认证用户所属的虚拟路由器和外部服务器的虚拟路由
器保持一致。
配置用户虚拟路由器，在SSO-Monitor配置模式下，使用以下命令：
user-vrouter vrouter-name
l
vrouter-name - 指定虚拟路由器名称。
在SSO-Monitor配置模式下，使用no user-vrouter命令取消配置用户虚拟路由器。
指定外部服务器
外部服务器需要支持将用户在线状态通过SSO-Monitor协议报文发送到防火墙。用户需至少配置一个外部服
务器host1、host2或host3，当配置多于一个时，其他外部服务器地址用于冗余备份。当某一个地址无法连
接时，系统将尝试连接下一个地址。建议按照1、2、3的顺序配置。
指定外部服务器，在SSO-Monitor配置模式下，使用以下命令：
host1 {ipv4-address | ipv6-address | host-name} [vrouter vrouter-name]
host2 {ipv4-address | ipv6-address | host-name} [vrouter vrouter-name]
host3 {ipv4-address | ipv6-address | host-name} [vrouter vrouter-name]
l
ipv4-address | ipv6-address | host-name - 指定外部服务器的IPv4地址、IPv6地址或者域名，取
值范围是1到255个字符。
l
vrouter-name - 指定防火墙与外部服务器的通信接口所属的虚拟路由器名称。
在SSO-Monitor配置模式下，使用以下命令删除指定的外部服务器:
no host {1 | 2 | 3}
注意: 从StoneOS 5.5R10版本开始，SSO Monitor支持对接多个外部服务器实现冗余备份。因
此，在版本升级到StoneOS 5.5R10后，系统中已配置的SSO Monitor的“host x.x.x.x”会自动
转换成“host1 x.x.x.x”配置。可通过“show user-sso client sso-monitor[ profilename”查看转换后的配置，转换后的SSO Monitor Profile名称与AD服务器名称相同。
指定AAA服务器
在防火墙的认证用户架构中，所有认证用户及其用户组不能独立存在，需关联于一个AAA服务器。SSO
Monitor用户是从外部服务器同步而来的。通过在防火墙上指定AAA服务器，可以将SSO Monitor用户与其
关联。

<!-- 来源页 1311 -->
指定SSO Monitor关联的AAA服务器，在SSO-Monitor配置模式下，使用以下命令：
aaa-server server-name
l
server-name - 指定SSO Monitor关联的AAA服务器的名称。AAA服务器支持选择Local、AD或者
LDAP类型的服务器。
在SSO-Monitor配置模式下，使用该命令no的形式删除SSO Monitor与AAA服务器的关联：
no aaa-server
指定端口
指定外部服务器的端口号，系统通过该端口号获取认证用户信息。默认为6666。在SSO-Monitor配置模式
下，使用以下命令：
port number
l
number – 指定外部服务器的端口号，系统通过该端口号获取认证用户信息。默认为6666，取值范围为
1024到65535。
在SSO-Monitor配置模式下，使用该命令no的形式恢复默认端口号：
no port
指定组织同步模式
指定组织同步模式，在SSO-Monitor配置模式下，使用以下命令：
org-source [aaa-server | message]
l
aaa-server –指定组织同步模式为AAA服务器。系统采用AAA服务器中的用户组织结构作为用户所属
组，一般用于用户组织结构保存在AAA服务器的场景。
l
message -指定组织同步模式为消息。系统采用外部服务器向防火墙同步用户时的SSO Monitor协议报
文中的用户组作为用户所属组，该用户组也将关联到所配置的AAA服务器上。
默认情况下，组织同步模式为消息。在SSO-Monitor配置模式下，恢复默认情况，使用以下命令：
no org-source
注意: 在使用AD Agent软件获取用户信息的应用场景，如果配置了AD服务监控功能，那么当版本
升级到StoneOS 5.5R10后，系统中已配置的AD服务监控功能会自动转换成SSO Monitor功能对
接AD Agent软件配置。转换后的组织同步模式为AAA服务器。可通过“show user-sso client

<!-- 来源页 1312 -->
sso-monitor[ profile-name”查看转换后的配置，转换后的SSO Monitor Profile名称与AD服
务器名称相同。
指定重连超时时间
指定连接超时时间，在SSO-Monitor配置模式下，使用以下命令：
disconn-del-timeout timeout
l
timeout - 设置连接超时时间。系统和外部服务器超时断开后，系统等待连接超时时间，如果超时时间
内仍然连接失败，则删除在线用户。范围是0到14400秒，默认值为300。0表示用户认证信息永不超
时。
在SSO Monitor配置模式下，使用该命令no的形式恢复SSO-Monitor重连超时时间为默认值：
no disconn-del-timeout
指定SSO Monitor强制超时时间
为了控制认证用户的在线时间，用户可以配置SSO Monitor强制超时时间使超时用户下线。
指定SSO Monitor强制超时时间，在SSO-Monitor配置模式下，使用以下命令：
force-timeout timeout
l
timeout - 设置强制超时时间。取值范围是0到6000分钟，默认值为0，表示认证用户永不超时。
在SSO Monitor配置模式下，使用该命令no的形式恢复SSO Monitor强制超时时间为默认值：
no force-timeout
提示: 在SSO Monitor对接AD Agent的应用场景，SSO Monitor强制超时时间建议大于或等于
AD Agent软件上的用户在线时长同时配置。
查看SSO Monitor配置
查看系统所有或者指定名称的SSO Monitor配置，包括名称、状态、AAA服务器，客户端探测间隔等。在任
意模式下，使用以下命令：
show user-sso client sso-monitor [profile-name]
l
profile-name – 指定SSO Monitor profile的名称。此时显示指定SSO Monitor的配置信息。
查看用户映射信息
查看SSO Monitor的用户名和IP映射关系。在任意模式下，使用以下命令：

<!-- 来源页 1313 -->
show user-mapping user-sso sso-monitor profile-name
查看认证用户表
设备生成的用户认证信息保存在认证用户表。在任意模式下，使用以下命令查看认证用户表：
show auth-user sso-monitor
踢出SSO Monitor用户
踢出SSO Monitor用户并删除用户和IP的映射信息。在任意模式下，使用以下命令：
exec user-mappping user-sso sso-monitor kickout ip ip-address vrouter vrouter-name
踢出AD- Script上线用户
系统支持将AD- Script功能与SSO Monitor功能结合使用，实现更快速的响应。先使用AD- Script单点登
录上线，为用户提供基础上网权限。同时，使用SSO Monitor功能提供更精确的上网权限。在ADScripting配置模式下，使用以下命令，在SSO Monitor用户上线后，踢出AD- Script上线用户：
kickout-by sso-monitor
默认情况下，不可踢出AD- Script上线用户。在AD-Scripting配置模式下使用该命令no的形式恢复默认情
况：
no kickout-by sso-monitor
AD Scripting单点登录
AD Scripting单点登录使用户通过Active-Directory服务器认证的同时，即可自动通过设备认证。目前只
支持Active-Directory服务器的AD Scripting功能。
Hillstone提供脚本程序”Logonscript.exe”，用户只需将脚本文件添加到Active-Directory服务器的登
录/注销脚本中即可实现AD Scripting功能。
注意: 将脚本程序” Logonscript.exe”添加到AD服务器的方法，请参考AD Scripting单点登录
配置举例。
进入AD Scripting配置模式
进入AD Scripting配置模式，在全局配置模式下，使用以下命令：
user-sso server ad-scripting default

<!-- 来源页 1314 -->
开启/关闭AD Scripting功能
默认情况下，系统的AD Scripting功能是关闭的。在防火墙上开启或者关闭AD Scripting功能，在ADScripting配置模式下，使用以下命令：
l
启用：enable
l
关闭：no enable
指定AAA服务器
指定用户所属的AAA服务器，在AD-Scripting配置模式下，使用以下命令：
aaa-server aaa-server-name
l
aaa-server-name – 指定AAA服务器的名称。AAA服务器支持选择Local、AD或者LDAP类型的服务
器。选择AAA服务器后，系统可以在引用的AAA服务器上查询在线用户的用户名对应的用户组和角色信
息，从而实现基于用户组和角色的策略控制。
在AD-Scripting配置模式下使用该命令no的形式取消对AAA服务器的指定：
no aaa-server
配置空闲超时时间
空闲超时时间指认证用户在无流量状态下保持认证状态的最长时间，超出空闲超时时间后，设备删除用户认
证信息。配置空闲超时时间，在AD-Scripting配置模式下，使用以下命令：
idle-timeout timeout
l
timeout – 指定空闲超时时间，单位为分钟。取值范围是1到60*24分钟。
默认情况下，在无流量状态下认证用户永不超时。在AD-Scripting配置模式下使用该命令no的形式恢复空
闲超时时间的默认值：
no idle-timeout
注意: SG6000-K20803/K9180/K7680/K7280/K6680/K6580和X系列设备不支持配置空闲超
时时间。
拒绝同名用户登录
AD-Scripting的用户同名登录功能为关闭状态时，如果开启拒绝同名用户登录功能，同一用户再次登录的信
息会替换掉已登录的信息，系统自动断开已登录的连接。如果关闭拒绝同名用户登录功能，则系统允许同一
用户再次登录。在AD-Scripting配置模式下，输入以下命令开启此功能：

<!-- 来源页 1315 -->
l
开启拒绝同名用户登录（默认设置）：auto-kickout
l
关闭拒绝同名用户登录：no auto-kickout
显示AD Scripting配置信息
在任意模式下，使用以下命令查看AD Scripting配置信息：
show user-sso server ad-scripting default
查看用户映射信息
查看AD Scripting的用户名和IP映射信息。在任意模式下，使用以下命令：
show user-mapping user-sso ad-scripting default
查看认证用户表
设备生成的用户认证信息保存在用户认证表。在任意模式下，使用以下命令：
show auth-user ad-scripting
踢出用户映射信息
踢出某指定IP的用户和IP的映射信息。在任意模式下，使用以下命令：
exec user-mappping user-sso ad-scripting kickout ip ip-address vrouter vrouter-name
AD Polling单点登录
创建AD Polling Profile
创建AD Polling profile并进入AD-Polling配置模式，在全局配置模式下，输入以下命令：
user-sso client ad-polling profile-name
l
profile-name - 指定所创建的AD Polling profile的名称。执行该命令后，系统将创建指定名称的AD
Polling profile，并进入AD-Polling配置模式；如果指定的名称已存在，则直接进入AD-Polling配置
模式。
在全局配置模式下使用该命令的no形式删除指定的AD Polling profile：
no user-sso client ad-polling name
开启/关闭AD Polling功能
启用AD Polling功能后，系统定时查询并获取AD服务器上的上线用户信息，并定时探测在线用户是否下
线。开启AD Polling功能，在AD-Polling配置模式下，使用以下命令：

<!-- 来源页 1316 -->
enable
关闭AD Polling功能，在AD-Polling配置模式下，使用以下命令：
no enable
指定认证服务器
指定域内认证AD服务器，在AD-Polling配置模式下，使用以下命令：
host ip-address
l
ip-address - 指定域内认证AD服务器的IP地址。此处仅支持AD服务器。指定认证AD服务器后，当域
用户从该AD服务器登录时，AD服务器会产生登录日志。
在AD-Polling配置模式下，使用该命令no的形式删除域内认证服务器:
no host
指定AAA服务器
指定系统引用的AAA服务器，在AD-Polling配置模式下，使用以下命令：
aaa-server server-name
l
server-name - 指定引用的AAA服务器的名称。AAA服务器支持选择Local、AD或者LDAP类型的服务
器，建议用户直接选择配置的认证AD服务器。选择AAA服务器后，系统可以在引用的AAA服务器上查询
在线用户的用户名对应的用户组和角色信息，从而实现基于用户组和角色的策略控制。
在AD-Polling配置模式下，使用该命令no的形式删除AAA服务器：
no aaa-server
指定账户
指定一个域用户的用户名，用于登录AD服务器。在AD-Polling配置模式下，使用以下命令：
account username
l
username – 指定域用户的用户名。格式为domain\username，范围是1到63个字符。要求该用户具
有读取AD服务器上的安全日志的权限，例如AD服务器上权限是Domain Admins的默认用户
Administrator。
在AD-Polling配置模式下，使用该命令no的形式删除账户：
no account

<!-- 来源页 1317 -->
指定密码
指定与域用户名对应的密码，在AD-Polling配置模式下，使用以下命令：
password password
l
password - 指定与域用户名对应的密码。范围是1到31个字符。
在AD-Polling配置模式下，使用该命令no的形式删除密码：
no password
指定AD Polling间隔
指定AD Polling定时探测的时间间隔，在AD-Polling配置模式下，使用以下命令：
ad-polling-interval interval
l
interval - 指定AD Polling定时探测的时间间隔。系统每隔时间间隔去AD服务器查询上线用户信息。
取值范围为1到3600秒，默认为2秒。为保证获取的用户上线信息的实时性，建议配置2到5秒。
在AD-Polling配置模式下，使用该命令no的形式恢复AD Polling定时探测的时间间隔默认值：
no ad-polling-interval
指定客户端探测间隔
指定客户端定时探测的间隔，在AD-Polling配置模式下，使用以下命令：
client-probing-interval time
l
time – 指定客户端定时探测的时间间隔。系统每隔时间间隔会通过WMI探测已上线用户是否在线，如果
探测不到，则踢出用户。取值范围为0到1440分钟，默认为0分钟，即关闭该功能。如果对用户下线要求
不高，建议配置较大探测间隔，节省系统性能。
在AD Polling配置模式下，使用该命令no的形式恢复客户端探测时间间隔的默认值：
no client-probing-interval
指定强制超时时间
指定强制下线时间，在AD-Polling配置模式下，使用以下命令：
force-timeout time
l
time - 指定强制下线时间。当用户在线时长超过配置的强制超时时间后，系统会提出用户，强制用户下
线。取值范围是0到144000分钟，默认为600分钟。如果设置为0分钟，则关闭该功能。
在AD-Polling配置模式下，使用该命令no的形式恢复强制超时时间的默认值：

<!-- 来源页 1318 -->
no force-timeout
查看AD Polling配置
查看系统所有或者指定名称的AD Polling配置，包括名称、状态、AAA服务器，客户端探测间隔等。在任意
模式下，使用以下命令：
show user-sso client ad-polling [profile-name]
l
profile-name – 指定AD Polling profile的名称。此时显示指定AD Polling的配置信息。
查看用户映射信息
查看指定名称的AD Polling的用户名/IP绑定信息。在任意模式下，使用以下命令：
show user-mapping user-sso ad-polling profile-name
查看认证用户表
设备生成的用户认证信息保存在用户认证表。在任意模式下，使用以下命令：
show auth-user ad-polling
踢出用户映射信息
踢出某指定IP的用户和IP的映射信息。在任意模式下，使用以下命令：
exec user-mappping user-sso ad-polling kickout ip ip-address vrouter vrouter-name
Radius Snooping单点登录
RADIUS为远程认证拨入用户服务，是用于NAS和AAA服务器间通信的一种协议。RADIUS报文监控通过解
析镜像到设备上的RADIUS报文，系统将自动获取认证用户的用户名和IP地址（可以为IPv4地址或者IPv6地
址）对应关系，生成对应的用户认证信息并加入认证用户表，用于用户流量的控制和审计。
进入Radius Snooping配置模式
进入Radius Snooping配置模式，在全局配置模式下，使用以下命令：
user-sso server radius-snooping default
开启/关闭Radius Snooping功能
默认情况下，系统的Radius Snooping功能是关闭的。开启活关闭Radius Snooping功能，在Radius
Snooping配置模式下，使用以下命令：

<!-- 来源页 1319 -->
l
开启：enable
l
关闭：no enable
指定AAA服务器
指定用户所属的AAA服务器，在Radius Snooping配置模式下，使用以下命令：
aaa-server aaa-server-name
l
aaa-server-name – 指定AAA服务器的名称。AAA服务器支持选择Local、AD或者LDAP类型的服务
器。选择AAA服务器后，系统可以在引用的AAA服务器上查询在线用户的用户名对应的用户组和角色信
息，从而实现基于用户组和角色的策略控制。
在Radius Snooping配置模式下使用该命令no的形式取消对AAA服务器的指定：
no aaa-server
配置空闲超时时间
空闲超时时间指认证用户在无流量状态下保持认证状态的最长时间，超出空闲超时时间后，设备仍未收到镜
像RADIUS报文设备，则会删除设备记录的用户名和IP地址对应关系。配置空闲超时时间，在Radius
Snooping配置模式下，使用以下命令：
idle-timeout timeout
l
timeout – 指定空闲超时时间，单位为分钟。取值范围是1到1440分钟。
默认情况下，在无流量状态下认证用户永不超时。在Radius Snooping配置模式下使用该命令no的形式恢
复空闲超时时间的默认值：
no idle-timeout
指定强制超时时间
指定强制下线时间，在Radius Snooping配置模式下，使用以下命令：
force-timeout time
l
time - 指定强制下线时间。当用户在线时长超过配置的强制超时时间后，系统会踢出用户，强制用户下
线。取值范围是0到1440分钟，默认为600分钟。
在Radius Snooping配置模式下，使用该命令no的形式恢复强制超时时间的默认值：
no force-timeout

<!-- 来源页 1320 -->
配置心跳超时时间
认证成功后，系统会在心跳超时时间结束前重新确认登录信息。如果同时配置了空闲超时时间和心跳超时时
间，用户会在两者中的最小时间点下线。配置心跳超时时间，在Radius Snooping配置模式下，使用以下
命令：
heartbeat-timeout {interval | disable}
l
interval – 指定超时时间，单位为分钟。取值范围是3到1440分钟。默认为5分钟。
l
disable – 关闭心跳超时时间功能。
在Radius Snooping配置模式下，使用该命令no的形式恢复默认心跳超时时间：
no heartbeat-timeout
配置认证用户过滤
通过配置认证用户过滤，系统在生成认证用户时，会过滤掉指定的用户名，只对未被过滤掉的用户名生成认
证用户信息。
配置认证用户过滤，在Radius Snooping配置模式下，使用以下命令：
username-filter not-end-with filter-string
l
not-end-with filter-string - 表示过滤掉用户名以指定字符串结尾的用户，对于被过滤掉的用户名，
不会生成认证用户信息。filter-string的取值范围是1到15个字符。
显示Radius Snooping配置信息
在任意模式下，使用以下命令查看Radius Snooping配置信息：
show user-sso server radius-snooping default
Agile Controller单点登录
启用Agile Controller功能后，系统可接收Agile Controller服务器发送的用户上下线报文和用户信息更新
报文，根据报文内容获取用户认证信息，并进行在线用户上下线及在线用户信息更新操作，实现单点登录。
进入Agile Controller配置模式
进入Agile Controller配置模式，在全局配置模式下，使用以下命令：
user-sso server agile-controller default

<!-- 来源页 1321 -->
开启/关闭Agile Controller功能
默认情况下，系统的Agile Controller功能是关闭的。开启或者关闭Agile Controller功能，在Agile
Controller配置模式下，使用以下命令：
l
启用：enable
l
关闭：no enable
指定设备接收Agile Controller报文的端口号
指定设备接收Agile Controller服务器报文的端口号（不可在非根VSYS中配置端口），在Agile
Controller配置模式下，使用如下命令：
local-port port
l
port – 指定端口号。取值范围为1024到65535，默认端口号为8001。
在Agile Controller配置模式下，使用no local-port命令恢复默认端口号。
指定AAA服务器
指定用户所属的AAA服务器。指定AAA服务器，在Agile Controller配置模式下，使用以下命令：
aaa-server aaa-server-name
l
aaa-server-name – 指定AAA服务器的名称。AAA服务器支持选择Local、AD或者LDAP类型的服务
器。选择AAA服务器后，系统可以在引用的AAA服务器上查询在线用户的用户名对应的用户组和角色信
息，从而实现基于用户组和角色的策略控制。
在Agile Controller配置模式下使用no aaa-server命令取消对AAA服务器的指定。
指定查询地址范围
指定系统主动向Agile Controller服务器查询源IP对应的在线用户信息时，需要查询的源IP的地址范围，在
Agile Controller配置模式下，使用以下命令：
sync-address address-entry
l
address-entry - 指定需要查询的源IP地址范围，为系统中已创建的地址簿条目。
在Agile Controller配置模式下，使用no sync-address命令取消对查询的源IP地址范围的指定。
指定查询速率
指定系统主动向Agile Controller服务器查询源IP对应的在线用户信息时，发送查询报文的速率，在Agile
Controller配置模式下，使用以下命令：

<!-- 来源页 1322 -->
sync-rate number
l
number - 指定发送查询报文的速率。取值范围为5到40次/秒，默认值为20次/秒。
在Agile Controller配置模式下，使用no sync-rate命令恢复默认查询报文速率。
指定查询时间间隔
指定系统主动向Agile Controller服务器查询源IP对应的在线用户信息时，每个源IP地址的查询时间间隔，
在Agile Controller配置模式下，使用以下命令：
ip-sync-interval time
l
time - 指定每个源IP地址的查询时间间隔。取值范围为1到100秒，默认为20秒。
在Agile Controller配置模式下，使用no ip-sync-interval命令恢复默认查询时间间隔。
指定每次最多查询IP数
指定系统主动向Agile Controller服务器查询在线用户信息时，每个查询报文中最多包含的源IP地址数量，
在Agile Controller配置模式下，使用以下命令：
max-ip-per-packet number
l
number - 指定每个查询报文中最多包含的源IP地址数量。取值范围是1到50个，默认为50个。
在Agile Controller配置模式下，使用no max-ip-per-packet命令恢复默认值。
指定强制超时时间
当用户在线时长超过配置的强制超时时间后，系统会强制用户下线。指定强制超时时间，在Agile
Controller配置模式下，使用以下命令：
force-timeout time
l
time– 指定强制超时时间。取值范围是5到1440分钟，默认为600分钟。
在Agile Controller配置模式下，使用no force-timeout命令恢复强制超时时间的默认值。
配置Agile Controller客户端
配置Agile Controller客户端，需要在Agile Controller客户端配置模式下进行。进入Agile Controller客
户端配置模式，在Agile Controller配置模式下，使用如下命令：
access-agile-controller name
l
name– 指定Agile Controller服务器的名称。

<!-- 来源页 1323 -->
在Agile Controller配置模式下，使用no access-agile-controller name命令删除指定的Agile
Controller客户端。
指定Agile Controller服务器IP地址
指定Agile Controller服务器的IP地址，在Agile Controller客户端配置模式下，使用如下命令：
host ip-address [vrouter vr-name]
l
ip-address - 指定Agile Controller服务器的IP地址。
l
vrouter vr-name - 指定Agile Controller服务器所属的VRouter，如不指定，默认为trust-vr。
在Agile Controller客户端配置模式下，使用no host命令删除指定的Agile Controller服务器IP地址。
配置共享密钥
设备使用共享密钥校验与Agile Controller服务器之间的加密通信报文，校验成功后，才会对报文进行解
析，否则丢弃报文。Agile Controller客户端需要配置与Agile Controller服务器相同的共享密钥，报文才
能通过校验。配置共享密钥，在Agile Controller客户端配置模式下，使用如下命令：
shared-secret key-value
l
key-value – 指定共享密钥。长度1-31个字符。
清除共享秘钥，在Agile Controller客户端配置模式下使用no shared-secret命令。
配置加密算法
指定系统与Agile Controller服务器通信时使用的加密算法，在Agile Controller客户端配置模式下，使用
如下命令：
encryption [3des | aes128]
l
3des | aes128 - 指定系统与Agile Controller服务器通信时使用的加密算法。如不指定，默认采用
AES128加密算法。
在Agile Controller客户端配置模式下，使用no encryption命令恢复加密算法的默认值。
开启/关闭主动查询功能
启用主动查询功能后，系统将主动向Agile Controller服务器查询用户在线信息。默认情况下，系统的主动
查询功能是关闭的。开启/关闭主动查询功能，在Agile Controller客户端配置模式下，使用如下命令：
l
开启：sync enable
l
关闭：no sync enable

<!-- 来源页 1324 -->
显示Agile Controller配置信息
显示Agile Controller配置信息，在任意模式下，使用如下命令：
show user-sso server agile-controller default
TS Agent单点登录
在Windows服务器上安装并运行Hillstone Terminal Service Agent软件。启用TS Agent功能后，当用
户通过远程桌面服务登录Windows服务器时，Hillstone Terminal Service Agent为用户分配端口段，并
将端口段和用户信息发送给设备，设备创建基于流量IP、端口段和用户的映射信息，实现用户的“免登
录”。
使用TS Agent实现单点登录，包含以下两个步骤：
l TS Agent服务器端配置，即在Windows服务器上安装并运行Hillstone Terminal Service Agent。
l TS Agent客户端配置，即在StoneOS上配置TS Agent功能。
注意: 本节主要对如何在StoneOS上进行TS Agent功能配置及查看的命令进行介绍。在Windows
服务器上安装并运行Hillstone Terminal Service Agent软件的方法，请参考TS Agent单点登
录配置举例。
创建TS Agent Profile
创建TS Agent profile并进入TS-Agent配置模式，在全局配置模式下，输入以下命令：
user-sso client ts-agent profile-name
l
profile-name - 指定所创建的TS Agent profile的名称。执行该命令后，系统将创建指定名称的TS
Agent profile，并进入TS-Agent配置模式；如果指定的TS Agent profile名称已存在，则直接进入
TS-Agent配置模式。
在全局配置模式下使用该命令的no形式删除指定的TS Agent profile：
no user-sso client ts-agent profile-name
开启/关闭TS Agent功能
启用TS Agent功能后，系统与Hillstone Terminal Service Agent建立SSL连接并获取用户及端口段信
息，并实时更新在线用户的流量IP、端口段和用户名的映射信息。
开启TS Agent功能，在TS-Agent配置模式下，使用以下命令：
enable

<!-- 来源页 1325 -->
关闭TS Agent功能，在TS-Agent配置模式下，使用以下命令：
no enable
指定TS Agent服务器
指定TS Agent服务器，在TS-Agent配置模式下，使用以下命令：
host {domain-name | ip-address} [vrouter vrouter-name]
l
domain-name | ip-address- 指定TS Agent服务器的管理地址，支持域名、IPv4及IPv6地址。
l
vrouter vrouter-name - 指定TS Agent服务器所属的虚拟路由器。
在TS-Agent配置模式下，使用该命令no的形式删除TS Agent服务器:
no host
指定TS Agent服务器端口
指定TS Agent服务器端口号，在TS-Agent配置模式下，使用以下命令：
port port-number
l
port-number - 指定TS Agent服务器的端口号。取值范围为1025到65534，默认值为5019。该端口
号必须和Hillstone Terminal Service Agent中设置的监听端口一致，否则无法通信。
在TS-Agent配置模式下，使用该命令no的形式恢复默认端口号:
no port
指定AAA服务器
指定系统引用的AAA服务器，在TS-Agent配置模式下，使用以下命令：
aaa-server server-name
l
server-name - 指定引用的AAA服务器的名称。AAA服务器支持选择Local、AD或者LDAP类型的服务
器。选择AAA服务器后，系统可以在引用的AAA服务器上查询在线用户的用户名对应的用户组和角色信
息，从而实现基于用户组和角色的策略控制。
在TS-Agent配置模式下，使用该命令no的形式删除AAA服务器：
no aaa-server
指定断开超时时间
指定断开超时时间，在TS-Agent配置模式下，使用以下命令：
disconnection-timeout timeout

<!-- 来源页 1326 -->
l
timeout - 设置断开超时时间。当StoneOS和Hillstone Terminal Service Agent的连接断开时，如
果在指定的断开超时时间内仍然连接失败，则删除在线用户信息。范围是0到1800秒，默认值为300。0
表示立即删除在线用户信息。
在TS-Agent配置模式下，使用该命令no的形式恢复断开超时时间为默认值：
no disconnection-timeout
指定流量IP
指定流量IP，在TS-Agent配置模式下，使用以下命令：
traffic-ip ip-address
l
ip-address - 指定流量IP地址，即TS Agent服务器网络接口（网卡）的IP地址。支持IPv4地址和IPv6
地址，最多可以指定4个IP地址。
在TS-Agent配置模式下，使用该命令no的形式删除指定的流量IP地址:
no traffic-ip ip-address
查看TS Agent配置
查看系统所有或者指定名称的TS Agent配置，包括名称、启用状态、TS Agent服务器、AAA服务器、断开
超时时间、流量IP等。在任意模式下，使用以下命令：
show user-sso client ts-agent [profile-name]
l
profile-name – 指定TS Agent profile的名称。此时显示指定TS Agent的配置信息。
查看TS Agent状态信息
查看TS Agent的状态信息，包括连接状态、用户分配端口范围，用户端口段大小，每用户最多端口段，心跳
时间间隔、心跳超时时间等。在任意模式下，使用以下命令：
show user-sso client ts-agent profile-name status
查看TS Agent用户映射信息
查看TS Agent的用户映射关系。在任意模式下，使用以下命令：
show user-mapping user-sso ts-agent profile-name
查看认证用户表
设备生成的用户认证信息保存在认证用户表。在任意模式下，使用以下命令查看认证用户表：
show auth-user ts-agent [port-range range | vrouter vrouter-name]

<!-- 来源页 1327 -->
踢出TS Agent用户
踢出TS Agent用户并删除映射关系，支持踢出指定IP和端口范围映射的用户映射信息，以及踢出指定用户名
的用户映射信息。在任意模式下，使用以下命令：
exec user-mappping user-sso ts-agent kickout {ip ip-address vrouter vrouter-name portrange range | username user-name auth-server server-name}
SAML单点登录
启用并配置SAML单点登录方案后，用户可以在防火墙登录界面使用SAML方式进行登录。
开启/关闭单点登录功能
开启/关闭允许第三方平台进行单点登录，在全局配置模式下，使用以下命令：
开启：admin sso-login enable
关闭：admin sso-login disable
配置SAML单点登录方案
指定单点登录方案为SAML单点登录，在全局配置模式下，使用以下命令：
admin sso-login type saml
指定单点登录方案为SAML单点登录后，需继续指定单点登录时所使用的SAML服务器。
指定SAML服务器，在SAML单点登录配置模式下，使用以下命令：
server server-name
l
server-name - 指定通过SAML单点登录时所使用的SAML服务器，该服务器需为系统中已创建的SAML
服务器。
取消指定SAML服务器，在SAML单点登录配置模式下，使用以下命令：
no server
查看管理员单点登录配置信息
查看管理员单点登录配置信息，在任意模式下，使用以下命令：
show http
云·界单点登录方案
仅虚拟化产品云·界支持该功能。该功能默认为关闭状态。开启该功能并配置第三方平台对应的单点登录方案
后，用户可在登录第三方平台后，直接访问云·界而无需输入用户名和密码。系统支持以下单点登录方案：

<!-- 来源页 1328 -->
l 启明CAS服务器（CAS_QIMING）：通过配置启明CAS服务器单点登录方案，用户可在启明星辰云安全资源池平
台单点登录云·界。
l 天翼云单点登录（CTYUN）：通过配置天翼云单点登录方案，用户可在天翼云平台单点登录云·界。
l 360云阵单点登录（360_YUNZHEN）：通过配置360云阵单点登录方案，用户可在360云阵云安全管理平台单点
登录云·界。
l 联通云CAS服务器（CAS_UNICOMCLOUD）：通过配置联动云CAS服务器单点登录方案，用户可在联通云安全管
理平台单点登录云·界。
开启/关闭单点登录功能
开启/关闭允许第三方平台进行单点登录，在全局配置模式下，使用命令：
开启：admin sso-login enable
关闭：admin sso-login disable
注意:
l
进行单点登录时，第三方平台的系统时间需与云·界保持一致。两者系统时间差不能超过10分
钟，否则单点登录将失败。
l
进行单点登录时，可能会因为CAS服务器的内存影响导致首次单点登录超时，此时需连续第二
次登录才可以单点登录成功。
开启单点登录功能后，需继续指定具体的第三方平台单点登录方案：启明CAS服务器单点登录(CAS_
QIMING)、天翼云单点登录(CTYUN)、360云阵单点登录(360_YUNZHEN)或联通云CAS服务器单点登录
（CAS_UNICOMCLOUD）。
配置启明CAS服务器单点登录方案
指定单点登录方案为启明CAS服务器单点登录(CAS_QIMING)，在全局配置模式下，使用命令：
admin sso-login type cas-qiming
指定单点登录方案为启明CAS服务器单点登录后，需继续指定Service Ticket校验地址及单点登录时所绑定
的虚拟路由器。
l
指定CAS服务器校验Service Ticket的URL地址，在启明CAS服务器单点登录模式下，使用命令：
ticket-check-url url
l
指定CAS服务器所在的虚拟路由器，在启明CAS服务器单点登录模式下，使用命令：
vrouter vrouter-name

<!-- 来源页 1329 -->
配置天翼云单点登录方案
指定单点登录方案为天翼云单点登录(CTYUN)，在全局配置模式下，使用命令：
admin sso-login type ctyun
查看/删除天翼云单点登录的Token信息
该功能需在天翼云单点登录场景下使用。系统支持查看或删除管理员的Token信息。Token信息用于天翼云
平台单点登录到云·界的过程中的身份验证。
查看管理员的Token信息，在全局配置模式下，使用命令：
show admin sso-token type ctyun
删除管理员的Token信息，在全局配置模式下，使用命令：
exec admin sso-token-del type ctyun owner username
l
username– 指定需删除Token信息的管理员用户名。
配置360云阵单点登录方案
指定第三方单点登录方案为360云阵单点登录(360_YUNZHEN)，在全局配置模式下，使用命令：
admin sso-login type 360-yunzhen
查看360云阵单点登录的Token信息
该功能需在360云阵单点登录场景下使用。系统支持查看360云阵单点登录的Token信息。Token信息用于
360云阵云平台单点登录到云·界的过程中的身份验证。
查看360云阵单点登录的签名信息，在任意模式下，使用命令：
show admin sso-info type 360-yunzhen
配置联通云CAS服务器单点登录方案
指定单点登录方案为联通云CAS服务器单点登录（CAS_UNICOMCLOUD），在全局配置模式下，使用命
令：
admin sso-login type cas-unicomcloud
指定单点登录方案为联通云CAS服务器单点登录后，需继续指定Service Ticket校验地址以及单点登录时所
绑定的虚拟路由器。
l
指定CAS服务器校验Service Ticket的URL地址，在联通云CAS服务器单点登录模式下，使用命令：
ticket-check-url url
l
指定CAS服务器所在的虚拟路由器，在联通云CAS服务器单点登录模式下，使用命令：
vrouter vrouter-name

<!-- 来源页 1330 -->
l
指定单点登录失败时的重定向地址（可选配置），在联通云CAS服务器单点登录模式下，使用命令：
failure-redirect-url url
查看管理员单点登录配置信息
查看管理员单点登录配置信息，在任意模式下，使用以下命令：
show http

<!-- 来源页 1331 -->
Portal认证
Portal认证功能用来对通过设备访问Internet的用户进行身份认证。配置Portal认证功能后，HTTP请求会
被重定向到Portal服务器的特定认证页面，用户可以访问其中的免费网络资源。当用户需要继续访问
Internet其他信息时，需要在该页面提供正确的用户名和密码进行认证。Portal认证成功后，将通过SSO
（Single Sign-On单点登录）在系统中生成认证用户，系统会按照策略配置给IP地址分配角色，从而实现
设备对不同用户的访问控制。
Portal服务器由第三方提供，用来接收Portal认证请求、进行用户身份认证以及与设备交互用户认证信息。
配置Portal认证相关功能，用户需要在以下模块进行配置：
l 配置接口、安全域以及角色映射规则。
l 配置服务器监控功能与Portal服务器交互认证信息。
l 创建策略规则，用来定义做Portal认证的流量以及触发Portal认证功能。
注意:
l
Portal认证功能仅支持通过命令行（CLI）配置。详细步骤请参阅《StoneOS命令行手册》。
l
系统同时支持通过二层接口和三层接口连接到Portal认证服务器。
l
Portal认证功能的配置通过策略规则与服务器监控功能相结合的方式实现，请参考策略配置。
l
关于如何配置服务器监控功能，请参考AAA服务器。
l
关于如何配置第三方Portal认证服务器，请参考第三方的用户手册。
配置触发Portal认证功能的策略规则
Portal认证功能的配置通过策略规则与服务器监控功能相结合的方式实现，此外还有特有的命令行。本节仅
介绍Portal认证特有命令行。
触发Portal认证功能，需要配置相应的策略规则。该策略规则可以在两种配置模式下配置：全局配置模式和
策略规则配置模式。
在全局配置模式下，需使用以下命令配置策略规则相关参数：
rule [role {UNKNOWN | role-name} | user aaa-server-name user-name | user-group aaaserver-name user-group-name] from src-addr to dst-addr service service-name application
app-name {permit | deny | tunnel tunnel-name | fromtunnel tunnel-name | webauth | portalserver portal-server-url}

<!-- 来源页 1332 -->
l
permit | deny | tunnel tunnel-name | fromtunnel tunnel-name | webauth | portal-server
portal-server-url – 指定策略规则的行为。具体描述如下：
l
portal-server – 对符合条件的流量进行Portal认证。
在策略规则配置模式下，需使用以下命令配置策略规则相关参数：
指定角色为unknown，用来匹配未经过认证的流量：
role unknown
指定Portal认证行为和第三方Portal认证服务器地址：
action portal-server portal-server-url
l
portal-server-url – 指定Portal认证服务器地址，范围为1到63个字符。URL地址格式为
“www.abc.com”或“https://www.abc.com”。

<!-- 来源页 1333 -->
802.1X认证
802.1X简介
802.1X是IEEE为解决基于端口的接入控制（Port-Based Network Access Control）而定义的一个标
准。它采用基于二层的认证方式，对局域网用户的接入的合法性进行认证。认证所使用的协议是EAPOL
（Extensible Authentication Protocol over LAN），该协议不基于网络层，而是基于二层的认证方
式，也就是说，防火墙可以对基于二层安全域或VLAN端口启用802.1x认证，只要指定的MAC地址或端口通
过认证，通过该接口的所有数据均可以通过。
支持802.1x的认证服务器是本地认证服务器（Local）和Radius认证服务器，其他认证服务器（AD或
LDAP）不支持。
802.1X体系结构
802.1X的体系结构包括了三个元素：认证请求者、认证系统和认证服务器。下图为802.1X体系结构关系
图。
只有当具备了这三个元素时，才能够完成基于端口的访问控制的用户认证和授权。
l 认证请求者：即客户端。用户启动客户端程序并输入用户名和口令，客户端程序向认证系统发出802.1X认证请
求。客户端需要支持EAP协议，且必须运行802.1X客户端软件。客户端和认证系统之间使用EAPOL格式封装EAP
协议传送认证信息。
l 认证服务器：该服务器可以存储用户的相关信息，如用户名称、用户口令等。它通过检验认证系统上传的用户信
息和口令判断用户是否有权使用网络资源，并向认证系统返回认证结果。目前版本可使用本地认证服务器或
RADIUS服务器来实现认证服务器的认证和授权功能。
l 认证系统（Hillstone设备）：它为客户端提供接入局域网的端口，支持物理端口。它将客户端的用户信息和口令
上传到认证服务器或下达到客户端，并根据认证的结果打开或关闭端口。认证系统在客户端和认证服务器之间充
当代理角色。
802.1X认证流程
802.1X认证方式有EAP-MD5、EAP-TLS和EAP-PEAP。不同的认证方式有不同的认证流程。

<!-- 来源页 1334 -->
提示:
l
目前Hillstone设备不支持使用本地认证服务器进行EAP-TLS认证。
l
使用EAP-TLS认证时，客户端软件需要兼容802.1X标准协议。
EAP-MD5认证流程
以下以EAP-MD5方式为例，介绍802.1X的基本认证流程：
1. 当用户需要访问网络资源时，启动802.1X客户端程序，并输入已经申请、登记过的用户名和口令，发起连接请
求，开启一次认证过程。
2. 认证系统收到来自客户端的请求后，发出一个请求帧要求客户端将用户名送上来。
3. 客户端响应认证系统的请求，将用户名信息送给认证系统。
4. 认证系统将客户端送上来的数据帧经过封包处理后送给认证服务器。
5. 认证服务器将收到的用户名信息与自己数据库中的用户信息相比对，找到该用户名对应的用户口令，用随机生成
的加密字对口令进行加密，并发送给认证系统。
6. 客户端收到由认证系统传来的加密字后，将口令进行加密处理，传给认证服务器。
7. 认证服务器将加密后的口令信息和自己经过加密后的口令信息进行对比。如果相同，则该用户为合法用户，可以
通过该端口访问网络。如果不同，则该用户未通过认证，继续保持认证系统端口的非认证状态。
EAP-TLS认证流程
EAP-TLS是一种客户端和服务器对数字证书进行相互验证的802.1X认证方式。首先服务器提供自己的数字
证书给客户端，客户端在验证服务器证书通过后，提交自己的数字证书给服务器，服务器验证通过后则允许
该客户端访问网络资源。如果组网环境中已经部署了PKI系统，Hillstone推荐您使用EAP-TLS认证方式。
使用EAP-TLS认证方式，请在客户端安装支持证书认证的802.1X客户端软件，并导入客户端数字证书和CA
证书；在服务器端设置认证方式为EAP-TLS，并部署服务器的数字证书和CA证书。
配置802.1X 认证
802.1X认证的配置包括：
l 创建并配置802.1X Profile。802.1X Profile包含802.1X认证属性，包括认证请求帧的最大可重复发送次数、客
户端重认证时间间隔、认证系统静默时间、客户端超时时间以及认证服务器应答超时时间。
l 指定802.1X认证服务器。支持本地认证服务器和外部认证服务器（RADIUS）。

<!-- 来源页 1335 -->
l 配置端口的802.1X属性。
l 配置802.1X认证的全局参数，比如允许接入客户端数量最大值、同名用户登录功能等。
创建802.1X Profile
创建802.1X Profile，在全局配置模式下，输入以下命令：
dot1x profile profile-name
l
profile-name - 指定所创建的802.1X Profile的名称。执行该命令后，系统将创建指定名称的802.1X
Profile，并进入dot1x配置模式；如果指定的名称已存在，则直接进入dot1x配置模式。
在全局配置模式下使用该命令的no形式删除指定的802.1X Profile：
no dot1x profile profile-name
认证请求帧的最大可重复发送次数
认证系统向客户端发送认证请求帧并收到客户端响应的数据后，会将数据发送给认证服务器并等待认证服务
器应答。如果未收到应答，则再次向客户端发送认证请求帧，直到收到认证服务器应答或达到允许的重复发
送次数后放弃尝试。在dot1x配置模式下，使用以下命令配置认证请求帧的最大可重复发送次数：
retransmission-count value
l
value – 指定认证请求帧的最大可重复发送次数。范围为1至10次，默认值为2次。
在dot1x配置模式下，使用no retransmission-count命令恢复默认值。
客户端重认证时间间隔
当客户端认证成功并接入网络后，认证系统可以对客户端进行重认证。在dot1x配置模式下，输入以下命令
配置认证系统的重认证时间间隔：
reauth-period value
l
value – 指定认证系统对客户端的重认证时间间隔。范围为0至65535秒，默认值为3600秒。如果取值
为0，则关闭重认证功能。
在dot1x配置模式下，使用no reauth-period命令恢复默认值。
认证系统静默时间
如果认证失败，认证系统需要静默一段时间后再重新处理同一客户端的请求。在dot1x配置模式下，使用以
下命令指定认证系统的静默时间：
quiet-period value

<!-- 来源页 1336 -->
l
value – 指定认证系统在认证失败之后处于静默状态的秒数。范围为0至65535秒，默认值为60秒。如
果取值为0，认证系统将一直处理同一客户端的请求。
在dot1x配置模式下，使用no quiet-period命令恢复静默时间默认值。
客户端超时时间
当认证系统向客户端发送请求报文，请求客户端上传用户名后，客户端需要在指定时间内向认证系统发送应
答报文。如果未在指定的客户端超时时间内完成发送，则认证系统将重发认证请求报文到客户端。在dot1x
配置模式下，使用以下命令指定客户端超时时间：
tx-period value
l
value – 指定客户端传送应答报文的超时时间。范围为1至65535秒，默认值为30秒。
在dot1x配置模式下，使用no tx-period命令恢复超时时间的默认值。
认证服务器应答超时时间
认证系统向客户端发送认证请求帧并收到客户端响应的数据后，会将数据发送给认证服务器并等待认证服务
器应答。如果在指定的认证服务器应答超时时间结束时，认证系统仍未收到认证服务器的应答，则会重新发
送请求帧到客户端。在dot1x配置模式下，使用以下命令指定认证服务器应答超时时间：
server-timeout value
l
value – 指定认证服务器应答超时时间。范围为1至65535秒，默认值为30秒。
在dot1x配置模式下，使用no server-timeout命令恢复超时时间的默认值。
指定802.1X认证服务器
用户可以将已配置好的AAA服务器指定为802.1X的认证服务器。在dot1x配置模式下，输入以下命令：
aaa-server server-name
l
server-name - 指定已配置的AAA认证服务器名称。目前版本支持AAA本地认证服务器和RADIUS服务
器。
在dot1x配置模式下，使用以下命令删除指定的802.1X认证服务器：
no aaa-server server-name
注意: 关于如何配置本地认证服务器和RADIUS服务器，请参阅"配置本地服务器认证参数" 在第
1197页、"配置RADIUS服务器认证参数" 在第1205页。

<!-- 来源页 1337 -->
配置端口的802.1X属性
认证系统为客户端提供接入局域网的端口，该端口需要绑定到二层域或VLAN。用户可以开启端口的802.1X
认证特性，并对其属性进行配置。
开启/关闭802.1X认证
在接口配置模式下，输入以下命令开启或关闭端口的802.1X认证：
l
开启802.1X认证：dot1x enable
l
关闭802.1X认证：no dot1x enable
当802.1X认证开启后，用户可以对端口的802.1X特性进行配置。
绑定802.1X Profile到端口
将已创建的802.1X Profile绑定到端口上，在接口配置模式下，输入以下命令：
dot1x profile profile-name
l
profile-name – 指定已创建的802.1X Profile名称。
使用该命令no的形式解除绑定：
no dot1x profile profile-name
端口接入控制模式
配置802.1X在指定端口上进行接入控制的模式，在接口配置模式下，使用以下命令：
dot1x port-control {auto | force-unauthorized}
l
auto - 自动模式，它是默认设置。在此模式下，认证系统依据802.1X协议认证的结果决定客户端是否
可以接入网络。
l
force-unauthorized - 强制未授权模式。在此模式下，端口始终为未授权模式，任何客户端都无法与
之建立连接。
在接口配置模式下，使用该命令的no形式恢复端口接入控制模式的默认设置：
no dot1x port-control
端口接入控制方式
配置802.1X端口接入控制的方式，在接口配置模式下，使用以下命令：
dot1x control-mode {mac | port}

<!-- 来源页 1338 -->
l
mac - 基于MAC地址进行认证。一个端口下连接的所有客户端都必须通过认证，才能访问网络资源。
l
port - 基于端口进行认证，它是默认设置。对一个端口下连接的所有客户端，只要有一个客户端通过认
证，其他客户端不必通过认证，即可访问网络资源。
在接口配置模式下，使用该命令的no形式恢复端口接入控制方式的默认设置：
no dot1x control-mode
配置802.1X全局参数
以下为802.1X的全局参数的配置。
端口允许同时接入客户端数量最大值
配置认证系统端口允许同时接入客户端数量最大值，在全局配置模式下，使用以下命令：
dot1x max-user user-number
l
user-number – 指定允许同时接入的客户端数量最大值。范围是1至1000。端口允许同时接入的客户
端数量的默认值根据平台的不同而不同。
使用no dot1x max-user命令恢复端口允许接入的最大客户端数量默认值。
已认证客户端超时时间
注意: 为保证该功能配置可以生效，建议用户先使用show dot1x profile profile-name命令确
认“keep-alive”功能为开启状态。如果为关闭状态，请先在dot1x配置模式下，使用keepalive enable命令开启心跳报文发送功能。
对于已通过802.1X认证的客户端，用户可以配置它的认证超时时间。客户端在此时间内没有回应认证系统，
则需要再次申请认证。在全局配置模式下，输入以下命令：
dot1x timeout timeout-value
l
timeout-value – 指定已认证的客户端超时时间，单位为秒。范围是180至3600*24秒，默认值是300
秒。
使用no dot1x timeout命令恢复默认值。
802.1X用户同名登录功能
用户同名登录功能指允许同一个用户在多个客户端同时登录。系统默认状态不开启此功能。开启802.1X用户
同名登录功能，允许同一用户在不同的客户端上登录，在全局配置模式下，输入以下命令：
dot1x allow-multi-logon

<!-- 来源页 1339 -->
执行该命令后，用户同名登录功能开启，用户可以对同一用户名的登录个数做限制。在全局配置模式下通过
使用以下命令指定用户同名登录次数：
dot1x allow-multi-logon number
l
number – 指定用户同名登录次数。范围是2到1000。
在全局配置模式下使用该命令no的形式关闭用户同名登录功能：
no dot1x allow-multi-logon
拒绝同名用户登录
802.1X用户同名登录功能为关闭状态时，如果开启拒绝同名用户登录功能，同一用户再次登录的信息会替换
掉已登录的信息，系统自动断开已登录的连接。如果关闭拒绝同名用户登录功能，则系统禁止同一用户再次
登录。在全局配置模式下，输入以下命令开启或关闭此功能：
l
开启拒绝同名用户登录（默认设置）：dot1x auto-kickout
l
关闭拒绝同名用户登录：no dot1x auto-kickout
强制断开客户端连接
认证系统可以通过命令强制断开某个客户端与认证系统的连接。强制断开客户端连接，在任何模式下，使用
以下命令：
exec dot1x kickout port-name authenticated-user-mac
l
port-name – 指定客户端连接的端口名称。
l
authenticated-user-mac – 指定被强制断开连接的已认证客户端的MAC地址。
开启/关闭心跳报文发送功能
客户端802.1X认证成功后，防火墙设备默认会定期向客户端发送心跳报文，用于监测用户的在线情况。如果
用户在认证时使用的客户端是Windows系统自带的802.1X客户端，即使认证成功，客户端在收到心跳报文
后仍会弹出“输入凭据”的对话框，提示用户再次输入用户名和密码。为避免上述问题，系统支持手动关闭
心跳报文的发送功能，关闭后，防火墙设备将无法监测用户的在线情况。
开启/关闭心跳报文发送功能，在dot1x配置模式下，使用以下命令：
l
开启（默认状态）：keep-alive enable
l
关闭：keep-alive disable

<!-- 来源页 1340 -->
注意:
l
关闭心跳报文发送功能后，dot1x timeout timeout-value命令配置无法生效。如需使其生
效，请先开启心跳报文发送开关。
l
关闭心跳报文发送功能后，防火墙设备将无法监测到异常掉线的用户，需要手动踢出掉线的用
户。具体操作，请参阅“用户认证> 802.1X认证> 查看在线用户”章节。
显示802.1X配置
用户可以通过show命令随时查看802.1X的配置情况。在任意模式下，输入以下命令：
show dot1x [profile profile-name | port port-name | statistics [port-name]]
l
show dot1x - 显示802.1X全局参数。
l
profile profile-name – 显示指定的802.1X Profile配置信息。
l
port port-name – 显示指定的认证系统端口的配置信息以及其绑定的Profile信息。
l
statistics [port-name] – 显示指定的认证系统端口的统计信息。

<!-- 来源页 1341 -->
PKI
PKI介绍
PKI（Public Key Infrastructure）即公钥基础设施，是提供公钥加密和数字签名服务的系统，目的是为了
自动管理密钥和证书，保证网上数据信息传输的机密性、真实性、完整性和不可否认性。PKI采用证书进行
公钥管理，通过第三方的可信任机构，把用户的公钥和用户的其它标识信息捆绑在一起，从而在网上验证用
户的身份。一个PKI系统由公钥密码技术（Public Key Cryptography）、证书认证机构（CA）、注册机
构（RA）、数字证书（Digital Certificate）和相应的PKI存储库组成。
以下介绍几个PKI相关的术语：
l 公钥密码技术：用户使用公钥密码技术产生密钥对，分别为公钥（public key）和私钥（private key），公钥向
外界公开，私钥则自己保留。公钥与私钥互为补充，被一个密钥加密的数据，只可以用相匹配的另外一个密钥解
密。
l 认证机构（CA）：是一个向个人、计算机或任何其它实体颁发证书的可信实体。CA受理证书服务申请，根据证
书管理策略验证申请方的信息，然后用其私钥对证书进行签名，并颁发该证书给申请方。
l 注册机构（RA）：RA是CA的延伸，RA向CA转发证书服务申请，也向目录服务器转发CA颁发的数字证书和证书
撤消列表，以提供目录浏览和查询服务。
l 证书撤销列表（CRL）：证书具有一定的使用期限，但是由于密钥被泄露、业务终止等原因，CA可通过撤销证书
缩短证书的使用期限。一个证书一旦被撤销，证书中心就要公布CRL来声明该证书是无效的，并列出不能再使用
的证书的序列号。
系统在以下功能模块中可以使用PKI认证方式：
l IKE VPN：建立IKE VPN时，支持PKI认证。
l HTTPS/SSH：使用HTTPS或者SSH方式访问Hillstone设备时，支持PKI认证。
l 沙箱防护：支持对PE文件进行可信证书验证。
配置PKI
StoneOS的PKI配置包括：
l 创建和删除PKI密钥对
l 配置PKI信任域
l 配置在线证书状态协议

<!-- 来源页 1342 -->
l 导入CA证书
l 导入密钥
l 导入加密密钥对
l 生成证书服务请求
l 安装本地证书
l 下载证书撤销列表
l 导出和导入PKI信任域
l 导出和导入本地证书
l 配置证书链
l 配置证书有效期检查
创建和删除PKI密钥对
系统有一个默认PKI密钥对，名为“Default-Key”。创建PKI密钥对，在全局配置模式下，使用以下命令：
pki key generate {rsa | dsa | sm2 | ecc} [label key-name] [modulus size] [ ec-group { 
prime256 | prime384 | prime521 }] [noconfirm]
l
rsa | dsa | sm2 | ecc– 指定密钥对的类型，RSA、DSA、SM2或者ECC。
l
label key-name – 指定密钥对的名称。该名称在系统中必须是唯一的。如没有指定该参数，系统将选
择默认的密钥对Default-Key。
l
modulus size – 指定密钥对的模长，单位为比特。RSA的模长可选项为1024、2048（系统默认值）、
512、768和4096，DSA的模长可选项为1024（系统默认值）、2048、512和768，SM2的模长为
256。
l
ec-group { prime256 | prime384 | prime521 }– 指定椭圆曲线组，包含P-256、P-384、P-521椭
圆曲线。若没有指定该参数，系统将选择默认的椭圆曲线组P-256。
l
noconfirm – 禁止关于该密钥对的提示信息。例如，创建的密钥对如果在系统中存在同名密钥对，如果
不配置该参数，系统将提示是否覆盖已有同名密钥对，如果配置该参数，系统将直接拒绝创建同名密钥
对。另外，用户可以使用命令pki key zeroize noconfirm禁止所有密钥对的提示信息。
删除已有的PKI密钥，在全局配置模式下，使用以下命令：
pki key zeroize {default | label key-name} [noconfirm]

<!-- 来源页 1343 -->
l
default | label key-name – 指定被删除密钥。default为删除系统默认密钥（Default-Key），
label key-name为删除指定名称的密钥。
l
noconfirm – 禁止该密钥对的提示信息。
配置PKI信任域
PKI信任域包含申请PKI本地证书所需的配置信息，例如密钥对、证书申请方式以及证书主题内容等。配置
PKI信任域，首先需要进入PKI信任域配置模式。进入PKI信任域配置模式，在全局配置模式下使用以下命
令：
pki trust-domain trust-domain-name
l
trust-domain-name – 指定PKI信任域的名称。执行该命令后，系统生成指定名称的PKI信任域并且进
入PKI信任域配置模式；如果指定的名称已存在，则直接进入PKI信任域配置模式。
在全局配置模式下，使用no pki trust-domain trust-domain-name命令删除指定的PKI信任域。
进入PKI信任域后，用户可以做以下配置：
l 指定证书获得方法
l 指定密钥对
l 配置主题内容
l 添加使用者可选名称
l 配置证书撤销列表
指定证书获得方法
为PKI信任域指定证书获得方法，在PKI信任域配置模式，使用以下命令：
enrollment {self | terminal}
l
self – 使用自签名的获得方法。
l
terminal – 使用终端（剪切和粘贴）的获得方法。
在PKI信任域配置模式下使用no enrollment命令取消证书获得方法的配置。

<!-- 来源页 1344 -->
注意:
l
该命令没有默认值，因此，用户必须使用该命令指定一种证书获得方法。
l
当证书获得方法为self，在生成自签名证书时，证书默认带有“SSL客户端身份验证”或者
“SSL服务端身份验证”属性。
指定密钥对
为PKI信任域指定密钥对，在PKI信任域配置模式，使用以下命令：
keypair key-name
l
key-name – 指定密钥对的名称。
在PKI信任域配置模式使用no keypair命令取消密钥对的指定。
配置主题内容
为PKI信任域配置主题内容，在PKI信任域配置模式，使用以下命令：
l
配置普通名称：subject commonName string
l
配置国家名称（可选）：subject country string
注意: 国家名称只能包含两个字符。
l
配置所在位置（可选）：subject localityName string
l
配置州或省名称（可选）：subject stateOrProvinceName string
l
配置机构名称（可选）：subject organization string
l
配置机构单元（可选）：subject organizationUnit string
使用以上命令no的形式取消相关配置：
l
no subject commonName
l
no subject country
l
no subject localityName
l
no subject stateOrProvinceName
l
no subject organization
l
no subject organizationUnit

<!-- 来源页 1345 -->
添加使用者可选名称
系统支持添加IP和域名形式的使用者可选名称。
添加IP形式的使用者可选名称
将指定的IP地址添加到使用者可选名称列表，在PKI信任域配置模式下，使用以下命令：
subject-alt-name ip ip-address
l
ip-address - 指定需要添加到使用者可选名称列表里的IP地址，支持IPv4和IPv6地址。
将指定的IP地址从使用者可选名称列表删除，在PKI信任域配置模式下，使用以下命令：
no subject-alt-name ip ip-address
添加域名形式的使用者可选名称
将指定的域名添加到使用者可选名称列表，在PKI信任域配置模式下，使用以下命令：
subject-alt-name dns domain-name
l
domain-name - 指定需要添加到使用者可选名称列表里的域名，取值范围是1到255个字符。
将指定的域名从使用者可选名称列表删除，在PKI信任域配置模式下，使用以下命令：
no subject-alt-name dns domain-name
配置证书撤销列表
证书撤销列表帮助用户检查一个有效期内证书是否被它的CA撤销。
配置CRL的检查方式
配置CRL的检查方式，在PKI信任域配置模式，使用以下命令：
crl {nocheck | optional | required}
l
nocheck – 安全设备不检查CRL。该选项为默认选项。
l
optional – 即使CRL不可用，Hillstone设备仍然可以接受对端的认证。
l
required – 只有CRL可用时，才可以接收对端认证。
配置获得CRL信息的URL
另外，用户可以配置获得CRL信息的URL。该配置需要在CRL配置模式下进行。进入CRL配置模式，在PKI信
任域配置模式，使用以下命令：

<!-- 来源页 1346 -->
crl configure
在CRL配置模式下，使用以下命令配置获得CRL信息的URL：
url index {url-http | url-ldap [username user-name password password auth-method authmethod]} [vrouter vrouter-name]
l
index – 为URL指定排序指数。系统最多支持3个URL，并且最先使用指数为1的URL。
l
url-http – 指定通过HTTP方式获得CRL信息，并指明获得CRL信息的URL。输入的URL必须以
“http://”开头，为1到255个字符的字符串。
l
url-ldap – 指定通过LDAP方式获得CRL信息，并指明获得CRL信息的URL。输入的URL必须以
“ldap://”开头，为1到255个字符的字符串。
l
username user-name password password auth-method auth-method – 指定通过LDAP方
式获得CRL信息时的用户名（username user-name）、密码（password password）和认证方式
（auth-method auth-method）。如不配置，系统默认通过匿名方式获得CRL信息。
l
username user-name - 用户名为LDAP服务器的登录DN（通常为LDAP服务器预设的具有查
询权限的用户账号）。
l
password password – 密码为登录DN所对应的密码。
l
auth-method auth-method -指定LDAP服务器的认证方式，支持明文认证（plain）。
l
vrouter vrouter-name – 指定获取CRL信息的VRouter。默认为系统缺省VR即trust-vr。
配置在线证书状态协议
在线证书状态协议（Online Certificate Status Protocol，简称为OCSP），其作用与CRL相同，即获得
数字证书的撤销状态。与CRL相比，OCSP可实现证书状态的在线查询，具有更强的时效性。CRL和OCSP可
以共同配置使用，其中任何一种方法验证证书失败，系统都会判断证书为不可用。
在PKI信任域配置模式下，使用以下命令启用/关闭OCSP证书状态检查功能：
l
启用：ocsp required
l
关闭：ocsp nocheck
OCSP相关参数配置需要在OCSP配置模式下进行。进入OCSP配置模式，在PKI信任域配置模式下，执行
ocsp configure命令。OCSP相关配置参数包括：
l
指定OCSP响应器
l
配置OCSP请求随机数
l
指定OCSP响应信息失效时间

<!-- 来源页 1347 -->
指定OCSP响应器
指定OCSP响应器，在OCSP配置模式下，使用以下命令：
url url
l
url – 指定OCSP相应器的URL，以“http://”开头。
使用该命令no的形式取消URL的指定，即no url。
配置OCSP请求随机数
设备发送OCSP请求时，用户可指定在请求中增加随机数，以此来增强设备与OCSP响应器之间通信的安全
性。配置OCSP请求随机数，在OCSP配置模式下，使用以下命令：
l
使用随机数（默认状态）：nonce enable
l
不使用随机数：nonce disable
指定OCSP响应信息失效时间
系统提供OCSP响应信息缓存功能，用来提高证书认证效率。用户可根据需要指定缓存在设备中的OCSP响应
信息的失效时间（失效的响应信息将会被从缓存中清除）。指定失效时间，在OCSP配置模式下，使用以下
命令：
response-cache-refresh-interval time
l
time - 指定缓存的OCSP响应信息的失效时间，单位为分钟，取值范围为0到1440。0表示不缓存，即每
次获得证书认证请求时，系统都会向OCSP响应器发出请求，询问证书状态；当取值为1到1440之间的任
意数值时，缓存的响应信息的失效时间由“当前系统时间+time”的时间与响应信息本身的next
update时间相比较而得出，哪个时间近，哪个时间即为失效时间。
在OCSP配置模式下，使用no response-cache-refresh-interval命令取消失效时间的配置。此时OCSP
响应信息的失效时间即为OCSP响应信息自身的next update时间（系统默认状态）。
导入CA证书
导入CA证书，在全局配置模式下，使用以下命令：
pki authenticate trust-domain-name
l
trust-domain-name – 指定PKI信任域的名称。
执行该命令后，系统提示用户将证书内容拷贝到指定的位置，回车后输入句点（.），之后再次敲回车。系统
将开始导入CA证书。

<!-- 来源页 1348 -->
注意: 系统会对导入证书做有效性检查，导入的CA证书中的“Basic Constraints”字段必须包含
“Subject Type=CA”。
导入密钥
导入密钥到PKI信任域，请在全局配置模式下使用以下命令：
pki key import {rsa | dsa | sm2 | ecc} [label label-name]
l
rsa – 指定导入RSA类型的密钥到PKI。
l
dsa – 指定导入DSA类型的密钥到PKI。
l
sm2 – 指定导入SM2类型的密钥到PKI。
l
ecc - 指定导入ECC类型的密钥到PKI。
l
label-name – 指定密钥对的名称。该名称在系统中必须是唯一的。如没有指定该参数，系统将选择默
认的密钥对Default-Key。
导入加密密钥对
用户需在导入时指定签名密钥对用于解密。被导入的加密密钥对是指将签名密钥对用数字信封的方式进行保
护。导入国密标准的加密密钥对到PKI信任域，请在执行模式下使用以下命令：
import pki key key-name enc-key sig-key-name from {ftp server ip-address [vrouter VRname] [user user-name password password] file-name | tftp server ip-address [vrouter VRname] file-name}
l
key-name – 指定导入后的加密密钥对的名字。
l
enc-key – 指定密钥的类型为国密标准定义的加密密钥类型的。
l
sig-key-name – 指定用于解密的签名密钥对。
l
ftp | tftp – 指定上传的方式，通过FTP上传或TFTP上传。
l
server ip-address – 指定FTP服务器或TFTP服务器的IP地址。
l
vrouter VR-name - 指定所属VRouter的名称。
l
user user-name password password – 指定服务器的用户名和密码。
l
file-name – 指定导入的本地加密密钥对文件名称。

<!-- 来源页 1349 -->
生成证书服务请求
PKI信任域配置完成后，用户需要根据PKI信任域的内容，生成证书服务请求，然后将生成的服务请求发送到
CA服务器，申请得到相应的本地证书。生成证书服务请求，在全局配置模式下，使用以下命令：
pki enroll trust-domain-name
l
trust-domain-name – 指定PKI信任域的名称，生成相应的证书服务请求。
安装本地证书
从CA服务器获得本地证书后，用户需要将本地证书安装到Hillstone设备上。安装本地证书，在全局配置模
式下，使用以下命令：
pki import trust-domain-name certificate
l
trust-domain-name – 指定PKI信任域的名称，安装相应的本地证书。
执行该命令后，系统提示用户将证书内容拷贝到指定的位置，然后输入句点（.）并敲回车。系统将开始安装
证书。
下载证书撤销列表
为PKI信任域下载证书撤销列表（CRL），在全局配置模式下，使用以下命令：
pki crl request trust-domain-name
l
trust-domain-name – 指定PKI信任域的名称。系统将根据PKI信任域中的CRL配置地址下载当前的证
书撤销列表。
导出和导入PKI信任域信息
为简化配置，用户可以将PKI信任域的证书（CA证书和本地证书）以及本地证书对应的私钥信息以PKSC12
格式一并从一台设备上导出，然后再一并导入到另外一台设备。
导出PKI信任域信息
导出PKI信任域信息，在全局配置模式下，使用以下命令：
pki export trust-domain-name pkcs12 pass-phrase
l
trust-domain-name – 指定PKI信任域的名称。
l
pass-phrase – 指定用于解密PKCS12数据的密码。
用户还可以通过命令行导出文件类型的PKI信任域信息到FTP服务器、TFTP服务器或者U盘。

<!-- 来源页 1350 -->
导出PKI信任域信息到FTP服务器
导出PKI信任域信息到FTP服务器，在执行模式下使用以下命令：
export pki trust-domain-name pkcs12 password to ftp server ip-address [user user-name
password password [file-name] | file-name]
l
trust-domain-name – 指定PKI信任域的名称。
l
pkcs12 password – 指定私钥保护口令，用于解密私钥。
l
ip-address – 指定FTP服务器的IP地址。
l
user user-name password password – 指定FTP服务器的用户名和密码。
l
file-name – 指定导出的PKI信任域信息的文件名称。
导出PKI信任域信息到TFTP服务器
导出PKI信任域信息到TFTP服务器，在执行模式下使用以下命令：
export pki trust-domain-name pkcs12 password to tftp server ip-address [file-name]
导出PKI信任域信息到U盘
导出PKI信任域信息到U盘，在执行模式下使用以下命令：
export pki trust-domain-name pkcs12 password to {usb0 | usb1} [file-name]
导入PKI信任域信息
导入PKI信任域信息，在全局配置模式下，使用以下命令：
pki import trust-domain-name pkcs12 pass-phrase
l
trust-domain-name – 指定PKI信任域的名称。
l
pass-phrase – 指定用于解密PKCS12数据的密码。
执行该命令后，系统提示用户将PKI信任域信息内容拷贝到指定的位置，回车后输入句点（.），之后再次敲
回车。系统将开始导入PKI信任域信息。
用户还可以通过命令行，导入文件类型的PKI信任域信息。导入的方式包括通过FTP和TFTP服务器或者通过
设备的USB口导入。
从FTP服务器导入PKI信任域信息
从FTP服务器导入PKI信任域信息，在执行模式下使用以下命令：

<!-- 来源页 1351 -->
import pki trust-domain trust-domain-name pkcs12 password from ftp server ip-address
{user user-name password password file-name | file-name}
l
trust-domain-name – 指定PKI信任域的名称。
l
pkcs12 password – 指定私钥保护口令，用于解密私钥。
l
ip-address – 指定FTP服务器的IP地址。
l
user user-name password password file-name – 指定FTP服务器的用户名和密码，以及导出
的PKI信任域信息的文件名称。
l
file-name – 指定导入的PKI信任域信息的文件名称。
从TFTP服务器导入PKI信任域信息
从TFTP服务器导入PKI信任域信息，在执行模式下使用以下命令：
import pki trust-domain trust-domain-name pkcs12 password from tftp server ip-address
file-name
从U盘导入PKI信任域信息
从U盘导入PKI信任域信息，在执行模式下使用以下命令：
import pki trust-domain trust-domain-name pkcs12 password from {usb0 | usb1} file-name
导入可信根证书
系统支持对PE文件进行可信证书验证，即如文件的签名证书是可信的，系统将不对其进行检测。导入可信根
证书，在全局配置模式下，使用以下命令：
import pki trusted-ca {package | single} from {ftp server ip-address [vrouter VR-name] [user
user-name password password] file-name | tftp server ip-address [vrouter VR-name] filename}
l
package – 指定导入证书包。
l
single – 指定导入单个证书。
l
ftp | tftp – 指定上传的方式，通过FTP上传或TFTP上传。
l
server ip-address – 指定FTP服务器或TFTP服务器的IP地址。
l
vrouter VR-name - 指定所属VRouter的名称。
l
user user-name password password – 指定服务器的用户名和密码。
l
file-name – 指定导入的本地证书文件名称。

<!-- 来源页 1352 -->
导出和导入本地证书
为简化配置，用户可以将PKI信任域的本地证书从一台设备上导出，然后再导入到另外一台设备。
导出本地证书
导出本地证书，在全局配置模式下，使用以下命令：
pki export trust-domain-name certificate
l
trust-domain-name – 指定PKI信任域的名称。
执行该命令后，系统提示用户将证书内容拷贝到指定的位置，回车后输入句点（.），之后再次敲回车。系统
将开始导出本地证书。
用户还可以通过命令行，导出文件类型的本地证书到FTP服务器、TFTP服务器或者U盘。
导出本地证书到FTP服务器
导出本地证书到FTP服务器，在执行模式下使用以下命令：
export pki trust-domain-name cert to ftp server ip-address [user user-name password
password [file-name] | file-name]
l
trust-domain-name – 指定PKI信任域的名称。
l
ip-address – 指定FTP服务器的IP地址。
l
user user-name password password – 指定FTP服务器的用户名和密码。
l
file-name – 指定导出的本地证书文件名称。
导出本地证书到TFTP服务器
导出本地证书到TFTP服务器，在执行模式下使用以下命令：
export pki trust-domain-name cert to tftp server ip-address [file-name]
导出本地证书到U盘
导出本地证书到U盘，在执行模式下使用以下命令：
export pki trust-domain-name cert to {usb0 | usb1} [file-name]
导入本地证书
导入本地证书，在全局配置模式下，使用以下命令：
pki import trust-domain-name certificate

<!-- 来源页 1353 -->
l
trust-domain-name – 指定PKI信任域的名称。
执行该命令后，系统提示用户将证书内容拷贝到指定的位置，回车后输入句点（.），之后再次敲回车。系统
将开始导入本地证书。
用户还可以通过命令行，导入文件类型的本地证书。导入的方式包括通过FTP和TFTP服务器或者通过设备的
USB口导入。
从FTP服务器导入本地证书
从FTP服务器导入本地证书，在执行模式下使用以下命令：
import pki trust-domain trust-domain-name cert from ftp server ip-address {user username password password file-name | file-name}
l
trust-domain-name – 指定PKI信任域的名称。
l
ip-address – 指定FTP服务器的IP地址。
l
user user-name password password file-name – 指定FTP服务器的用户名和密码，以及导入的
本地证书的文件名称。
l
file-name – 指定导入的本地证书文件名称。
从TFTP服务器导入本地证书
从TFTP服务器导入本地证书，在执行模式下使用以下命令：
import pki trust-domain trust-domain-name cert from tftp server ip-address file-name
从U盘导入本地证书
从U盘导入本地证书，在执行模式下使用以下命令：
import pki trust-domain trust-domain-name cert from {usb0 | usb1} file-name
HTTPS认证支持导入定制证书
导入定制证书
开启Web认证功能后，如果选择HTTPS认证模式进行认证，用户的浏览器会出现安全证书不受信任的情况，
此时用户需要点击继续才可以进行认证。为了避免出现此情况，用户可以从国际CA认证中心购买由CA签名
的本地证书，并将此证书导入到新创建的PKI信任域中，然后通过导入定制证书功能实现对可信任证书的引
用。配置此功能后，用户进行HTTPS认证时，浏览器证书列表中的CA证书的公钥将会对导入的由CA私钥签
名的本地证书进行认证，不会出现安全证书不受信任的情况。

<!-- 来源页 1354 -->
配置导入定制证书功能，在Web认证配置模式下，使用以下命令：
https-trust-domain trust-domain-name
l
trust-domain-name – 指定HTTPS信任域的名称。执行该命令前，系统必须先创建此PKI信任域，且
该PKI信任域已导入从国际CA认证中心购买的证书。缺省情况下，PKI信任域为trust_domain_
default，用户在进行HTTPS认证时仍会遇到安全证书不受信任的情况。
注意: PC端需要确保在浏览器证书列表中有可信的CA证书，否则浏览器仍会提示证书不受信。
在Web认证配置模式下，使用no https-trust-domain命令取消对非默认PKI信任域的引用。
查看HTTPS信任域配置信息
用户可以在任何模式下，随时使用show命令查看HTTPS信任域配置信息。命令如下：
show webauth
证书有效期相关配置
为保证用户使用的证书有效，防止由于证书过期而产生一系列问题，系统会针对证书有效期做以下处理：对
于即将过期的证书或者CA证书，系统会在证书过期前一个星期开始生成警告（Warning）级别日志信息，
进行提醒；对于已经过期的证书或者CA证书，系统将会每天生成一条严重（Critical）级别日志信息，进行
提醒；并且对于自签名证书，系统将提供一个刷新方法，使用户可以重新自签名。
系统规定自签名证书的有效期为10年，用户可以在全局配置模式下使用以下命令刷新自签名证书，重新自签
名：
pki refresh trust-domain-name
l
trust-domain-name – 指定PKI信任域的名称。
显示PKI配置信息
用户可以随时使用show命令显示PKI的配置信息。显示密钥对的配置信息，在任何模式下，使用以下命令：
show pki key [label key-name [ssh-pubkey]]
l
label key-name – 显示指定名称的密钥对配置信息。如果不指定该参数值，则显示系统中所以密钥对
的配置信息。
l
ssh-pubkey - 显示指定密钥对的SSH格式公钥。仅支持显示RSA类型密钥对的SSH格式公钥。
显示PKI信任域的配置信息，在任何模式下，使用以下命令：
show pki trust-domain [trust-domain-name]

<!-- 来源页 1355 -->
l
trust-domain-name – 显示指定名称的PKI信任域的配置信息。如果不指定该参数，则显示系统中所
有PKI信任域的配置信息。
配置证书链
证书链是一个由根CA证书、中间证书和用户证书组成的一条完整证书信任链。只有当整个证书信任链上的各
个证书都有效时，浏览器才会认定当前用户的证书是有效和受信任的。根CA证书是信任链的起点，是受信
CA证书机构颁发给自己的证书。中间证书是根CA证书机构颁发给中间CA证书机构的证书，作用是保护根证
书不被泄露，可以有多级。
创建证书链
创建证书链，在全局配置模式下，使用以下命令：
pki cert-chain cert-chain-name
l
cert-chain-name - 指定证书链名称，取值范围是1到31个字符。执行该命令后，系统生成指定名称的
证书链并且进入证书链配置模式；如果指定的名称已存在，则直接进入证书链配置模式。
删除指定的证书链，在全局配置模式下，使用以下命令：
no pki cert-chain cert-chain
导入证书链
系统支持从服务器导入证书链文件或通过粘贴证书链内容的方式导入。证书链中支持包含最多6个证书，链
式必须连续，但不限制排列顺序。
从FTP、FTPS或SFTP服务器导入证书链文件
从FTP、FTPS或SFTP服务器导入证书链文件，在执行模式下，使用以下命令：
import pki cert-chain cert-chain-name {pkcs7 | pkcs12-der password | cert-bundle} from
{ftp | ftps | sftp server} ip-address vrouter vrouter-name user user-name password
password file-name
l
cert-chain-name - 指定证书链名称。
l
pkcs7 | pkcs12-der password | cert-bundle - 指定证书链文件的格式，即PKCS#7、PKCS#12或
CERT-BUNDLE格式。CERT-BUNDLE是PEM编码的证书链文件。对于PKCS#12格式的证书链，需要指
定证书链文件的密码。
l
ip-address - 指定FTP、FTPS或SFTP服务器地址。
l
vrouter vrouter-name - 指定虚拟路由器名称。

<!-- 来源页 1356 -->
l
user user-name password password- 指定用于服务器的用户名和密码。
l
file-name - 指定证书链文件名称。
从TFTP服务器导入证书链文件
从TFTP服务器导入证书链文件，在执行模式下，使用以下命令：
import pki cert-chain cert-chain-name {pkcs7 | pkcs12-der password | cert-bundle} from
tftp server ip-address vrouter vrouter-name file-name
通过粘贴证书内容的方式导入证书链
通过粘贴证书内容的方式导入证书链，在全局配置模式下，使用以下命令：
pki import cert-chain cert-chain-name {pkcs7 | cert-bundle}
执行该命令后，根据提示粘贴证书链文件内容，并在新的一行以点号“.”结束输入。
导出证书链
系统支持导出证书链文件到指定的服务器或将证书链内容显示在终端上。
导出证书链文件到服务器
导出证书链文件到服务器，在执行模式下，使用以下命令：
export pki cert-chain cert-chain-name {pkcs7 | pkcs12-der password } to {ftp | ftps | sftp
server} ip-address vrouter vrouter-name user user-name password password file-name
导出证书链文件并显示在终端上
导出证书链文件并显示在终端上，在全局配置模式下，使用以下命令：
pki export cert-chain cert-chain-name
查看证书链信息
查看指定证书链配置信息，在任意模式下，使用以下命令：
show pki cert-chain cert-chain-name
查看所有证书链配置信息，在任意模式下，使用以下命令：
show pki cert-chain
查看指定证书链内的证书信息，在任意模式下，使用以下命令：
show pki cert-chain cert-chain-name cert subject-name

<!-- 来源页 1357 -->
l
cert-chain-name - 指定证书链名称。
l
subject-name - 指定证书主题名称。
配置证书有效性检查
开启/关闭证书有效性检查
证书有效性检查对证书链中的所有证书以及信任域中的证书都有效，默认为开启状态。关闭证书有效性检
查，在全局配置模式下，使用以下命令：
pki cert-validity-check disable
开启证书有效性检查，在全局配置模式下，使用以下命令：
pki cert-validity-check enable
配置证书有效性检查
默认情况下，在证书到期前一周开始，系统会每天告警一次。当证书过期时，系统会记录Critical级别的事
件日志。
配置证书有效性的检查间隔和提前告警时间，在全局配置模式下，使用以下命令：
pki cert-validity-check {interval value | pre-warning-time time}
l
interval value - 指定证书有效性的检查间隔，取值范围是1到100小时，默认为24。
l
pre-warning-time time - 指定提前告警时间，取值范围是1到1000小时，默认值为168。
查看证书有效性检查配置和检查结果
查看证书有效性检查的配置信息，在任意模式下，使用以下命令：
show pki cert-validity-check
命令输出中会显示上一次的检查结果：
l
not checked yet：表示还没开始检查。
l
valid：表示证书在有效期内。
l
expired：表示证书已过期。
l
null cert：表示证书不存在，信任域或证书链里未导入证书。

<!-- 来源页 1358 -->
用户认证配置举例
用户认证配置举例包括以下：
l "例：认证与授权配置举例" 在第1356页
l "例：Web认证配置举例" 在第1358页
l "HTTP Web认证配置举例" 在第1358页
l "NTLM认证配置举例" 在第1360页
l "例：单点登录配置举例" 在第1363页
l "AD Polling单点登录配置举例" 在第1363页
l "AD Scripting单点登录配置举例" 在第1364页
l "SSO Monitor单点登录配置举例" 在第1367页
l "SSO Radius登录配置举例" 在第1370页
l "例：通过SSO Web实现基于用户的网络访问控制" 在第1371页
l "TS Agent单点登录配置举例" 在第1376页
l "Agile Controller单点登录配置举例" 在第1375页
l "例：Portal认证配置举例" 在第1378页
l "例：802.1X配置举例" 在第1380页
l "例：PKI配置举例" 在第1382页
例：认证与授权配置举例
本例对Telnet用户进行外部RADIUS验证。具体要求及配置如下所述。
组网需求
对Telnet用户用RADIUS服务器进行认证。认证服务器的IP地址为202.10.1.2，且无备用服务器；RADIUS
服务器的重传次数采用默认值3次；RADIUS服务器的应答超时时间采用默认值3秒；在RADIUS服务器的
1812端口上启动验证服务。下图为该需求组网图。

<!-- 来源页 1359 -->
配置步骤
第一步：将Hillstone设备的接口接入安全域并配置接口的IP地址。
hostname# configure
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# manage telnet
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 10.1.1.1/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 202.10.1.1/24
第二步：进入AAA服务器配置模式。
hostname(config-aaa-server)# aaa-server rad type radius
第三步：配置认证方案。
hostname(config-aaa-server)# host 202.10.1.2
hostname(config-aaa-server)# port 1645
hostname(config-aaa-server)# secret testing123
hostname(config-aaa-server)# exit
第四步：为系统指定认证服务器。
hostname(config)# admin auth-server rad
第五步：检验配置结果。

<!-- 来源页 1360 -->
hostname(config)# show aaa-server rad
==============================================================
aaa-server: radius
type: radius
role-mapping-rule :
backup-aaa-server :
server address: 202.10.1.2(trust-vr)
first backup :
second backup :
radius setting:
port: 1812 secret: a3UfKjOGP80IGeggG9kuvDJ7I8Ye
retries 3 time(s), timeout 3 second(s).
accounting: enable (optional)
accounting setting:
port: 2000 secret: hq8DNiGMUL4Pq2A9tf1422uLRWcF
server address: 202.10.1.2(trust-vr)
first backup :
second backup :
==============================================================
例：Web认证配置举例
Web认证配置举例包含：
l "HTTP Web认证配置举例" 在第1358页
l "NTLM认证配置举例" 在第1360页
HTTP Web认证配置举例
该实例对通过设备上网的用户进行控制：仅允许user1通过Web认证后上网，其它流量全部拒绝。认证服务
器为本地服务器local。
第一步：配置用户、角色以及角色映射规则：

<!-- 来源页 1361 -->
hostname(config)# aaa-server local
hostname(config-aaa-server)# user-group usergroup1
hostname(config-user-group)# exit
hostname(config-aaa-server)# user user1
hostname(config-user)# password hillstone1
hostname(config-user)# group usergroup1
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)# role role1
hostname(config)# role-mapping-rule role-mapping1
hostname(config-role-mapping)# match user-group usergroup1 role role1
hostname(config-role-mapping)# exit
hostname(config)#
第二步：配置本地认证服务器的角色映射规则：
hostname(config)# aaa-server local
hostname(config-aaa-server)# role-mapping-rule role-mapping1
hostname(config-aaa-server)# exit
hostname(config)#
第三步：配置接口与安全域：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 192.168.1.1/16
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/10
hostname(config-if-eth0/10)# zone untrust
hostname(config-if-eth0/10)# ip address 66.1.200.1/16
hostname(config-if-eth0/10)# exit
hostname(config)#

<!-- 来源页 1362 -->
第四步：开启设备的HTTP Web认证功能并且通过策略规则触发Web认证功能：
hostname(config)# webauth
hostname(config-webauth)# enable
hostname(config-webauth)# protocal http
hostname(config-webauth)# exit
hostname(config)# policy-global
hostname(config-policy)# rule from any to any from-zone trust to-zone untrust
service dns permit
hostname(config-policy)# rule role UNKNOWN from 192.168.1.1/16 to any service any
webauth local
Rule id 4 is created
hostname(config-policy)# exit
hostname(config)#
第五步：配置允许访问的策略规则：
hostname(config)# policy-global
hostname(config-policy)# rule role role1 from 192.168.1.1/16 to any from-zone trust
to-zone untrust service any permit
hostname(config-policy)# exit
hostname(config)#
以上配置完成后，系统会对所有来自192.168.1.1/16网段的HTTP请求（有可达路由的外部地址）进行Web
认证，只有在认证页面输入用户名和密码分别为user1和hillstone1，才可以访问网络。
NTLM认证配置举例
以下为NTLM认证配置举例。完成配置后，用户只需通过Active Directory服务器的认证便可以正常访问网
络资源。
实现NTLM认证功能，按照以下步骤进行配置：
第一步：配置Active-Directory类型的AAA服务器：
hostname(config)# aaa-server ad type active-directroy
hostname(config-aaa-server)# host 1.1.1.1
hostname(config-aaa-server)# base-dn dc=hillstonenet

<!-- 来源页 1363 -->
hostname(config-aaa-server)# login-dn cn=user,dc=hillstonenet
hostname(config-aaa-server)# login-password admin
hostname(config-aaa-server)# exit
hostname(config)#
第二步：指定Web认证服务器：
hostname(config)# policy-global
hostname(config-policy)# rule from any to any service any webauth ad
hostname(config-policy)# exit
hostname(config)#
第三步：启用NTLM功能：
hostname(config)# webauth
hostname(config-webauth)# mode ntlm
第四步：配置浏览器自动使用当前用户名和密码登录（以Chrome浏览器为例）：

<!-- 来源页 1364 -->
1. 在浏览器工具栏右侧，点击
按钮，选择设置：
2. 在<设置>页面，选择自动填充> 密码管理器：

<!-- 来源页 1365 -->
3. 在<密码管理器>页面，将“自动登录”功能设置为开启状态：
4. 注销当前用户，重新登录后，用户无需在浏览器中完成Web认证便可正常访问网络资源。
例：单点登录配置举例
单点登录配置举例包含：
l "AD Polling单点登录配置举例" 在第1363页
l "AD Scripting单点登录配置举例" 在第1364页
l "SSO Monitor单点登录配置举例" 在第1367页
l "SSO Radius登录配置举例" 在第1370页
l "例：通过SSO Web实现基于用户的网络访问控制" 在第1371页
l "Agile Controller单点登录配置举例" 在第1375页
l "TS Agent单点登录配置举例" 在第1376页
AD Polling单点登录配置举例
以下为使用AD Polling实现单点登录配置举例。完成配置后，当域用户通过Active-Directory服务器登录
时，AD服务器上会产生登录日志。开启AD Polling功能后，系统会定时查询并获取AD服务器上的用户登录
信息，并定时探测在线用户是否下线，获取正确的认证用户信息，从而实现单点登录。
使用AD Polling实现单点登录，按照以下步骤进行配置:
第一步：配置AD Polling引用的AAA服务器。可以选择配置的Local、AD或者LDAP类型的服务器。此处以
AD服务器为例。
hostname(config)# aaa-server ad type active-directroy
hostname(config-aaa-server)# host 192.168.2.2

<!-- 来源页 1366 -->
hostname(config-aaa-server)# base-dn dc=hillstonenet
hostname(config-aaa-server)# login-dn cn=user,dc=hillstonenet
hostname(config-aaa-server)# login-password admin
hostname(config-aaa-server)# exit
hostname(config)#
第二步：启用并配置AD Polling功能。指定认证服务器、引用的AAA服务器、账户和密码等。
hostname(config)# user-sso client ad-polling test
hostname(config-ad-polling)# enable
hostname(config-ad-polling)# host 10.180.201.8
hostname(config-ad-polling)# account adpoll\administrator
hostname(config-ad-polling)# password hillstone
hostname(config-ad-polling)# aaa-server ad
hostname(config-ad-polling)# exit
hostname(config)#
AD Scripting单点登录配置举例
以下为AD Scripting功能配置举例。完成配置后，当用户通过Active-Directory服务器认证的同时，即可
自动通过设备认证。
实现AD Scripting单点登录，按照以下步骤进行配置:
第一步：配置Active-Directory类型的AAA服务器：
hostname(config)# aaa-server ad type active-directroy
hostname(config-aaa-server)# host 1.1.1.1
hostname(config-aaa-server)# base-dn dc=hillstonenet
hostname(config-aaa-server)# login-dn cn=user,dc=hillstonenet
hostname(config-aaa-server)# login-password admin
hostname(config-aaa-server)# exit
hostname(config)#
第二步：启用AD Scripting功能：
hostname(config)# user-sso server ad-scripting default

<!-- 来源页 1367 -->
hostname(config-ad-scripting)# enable
hostname(config-ad-scripting)# aaa-server ad
hostname(config-ad-scripting)# exit
hostname(config)#
第三步：在Active Directory服务器导入登录/注销脚本：
1. 在AD Agent软件中，打开<AD Scripting>标签页，点击“获取AD Scripting”获取脚本程序（名称为
“Logonscript.exe”、“adscripting-startup.bat”和“adscripting-dispatch.bat”），然后将三个脚本程
序存放在域服务器的Logon目录下。
2. 在AD服务器上，进入“开始”菜单，选择“管理工具>Active Directory用户与计算机”，弹出<Active
Directory 用户与计算机>对话框。
3. 右键点击要应用单点登录的域，选择“属性”，然后点击<组策略>标签页。

<!-- 来源页 1368 -->
4. 在策略列表中，双击要应用单点登录的组策略，然后在弹出的<组策略编辑器>窗口中，点击“用户配置
>Windows设置>脚本（登录/注销）”。
5. 双击右侧窗口的“登录”，在弹出的<登录属性>对话框中，点击“添加”。
6. 在弹出的<添加脚本>对话框中，点击“浏览”选择脚本程序：
l 当选择“Logonscript.exe”时，在“脚本参数”处输入ip-adddress logon。ip-adddress参数用于指
定StoneOS系统的认证接口地址IP，可以向多个设备发送上线请求，支持配置1-20个IP地址，用“,”隔

<!-- 来源页 1369 -->
开。
l 当选择“Logonscript.exe”时，在“脚本参数”处输入ip-adddress logon daemon [cycle cycletimes]。daemon表示可以对用户IP变化进行监测。cycle cycle-times 参数用于指定监测用户IP变化的周
期，取值范围是1-300秒，默认值为5秒。
l 当选择“adscripting-dispatch.bat”时，在“adscripting-startup.bat”中修改参数ip-adddress
logon daemon [cycle cycle-times]。
提示: 当客户端数量较多时，推荐使用“adscripting-dispatch.bat”程序；客户端数量较少
时，推荐使用“Logonscript.exe”程序。
7. 点击“确定”。
8. 同样的，设置注销时启动的脚本程序。在<添加脚本>对话框中，点击“浏览”选择脚本程序
（Logonscript.exe），在“脚本参数”处输入ip-adddress logoff，支持配置1-20个IP地址，用“,”隔开。
注意: 存储脚本程序的目录必须保证所有域用户均具有访问权限，否则脚本程序不能被触发。
SSO Monitor单点登录配置举例
AD Agent软件能够将AD域内的用户在线状态通过SSO Monitor协议报文发送到防火墙，因此可以作为SSO
Monitor单点登录功能对接的外部服务器。此处以AD Agent软件为例说明如何通过SSO Monitor与AD
Agent对接实现单点登录。
在Active-Directory服务器或域内任一PC上安装AD Agent软件，当域用户从Active-Directory服务器登
录时，AD Agent会记录该用户的用户名、IP地址、上线时间等信息，并将用户名和IP地址对应关系信息发
送到StoneOS，使得用户可以免于二次登录，在防火墙上生成认证用户。利用所获取的用户名和IP地址对应
关系信息，系统还可以实现基于用户的安全统计、日志记录、上网行为审计等。
使用SSO Monitor对接AD Agent实现单点登录，按照以下步骤进行配置:

<!-- 来源页 1370 -->
第一步：安装AD Agent并配置相关参数。AD Agent可以安装在AD服务器或者域内任一PC上，支持
Windows和Windows Server环境。推荐在Windows Server 2008 /2012/2016/2019、Windows
7/10中安装。
在PC或服务器上安装和运行AD Agent，按照以下步骤操作：
1. 点击链接https://images.hillstonenet.com/dist/#/StoneOS/id/1782，进入山石网科固件下载中心的
StoneOS目录。
2. 点击“ADAgent”文件夹，获取并下载AD Agent安装程序。下载完成后，将其拷贝到域内的一台PC机或服务器
上。
3. 双击AD Agent安装程序ADAgentSetup.exe，按照安装向导提示逐步安装直至完成。
4. 使用以下两种方法启动AD Agent软件：
a. 双击桌面的AD Agent Configuration Tool 快捷方式，系统弹出<AD Agent设置工具>对话框。
b. 点击“开始菜单”中的“所有程序> Hillstone AD Agent >AD Agent Configuration Tool”，系统弹出
<AD Agent设置工具>对话框。
5. 第四步：点击<设置>标签页。
在<设置>标签页，配置基础选项。

<!-- 来源页 1371 -->
选项
说明
端口号
输入监听端口号。AD Agent通过该端口与StoneOS建立通信连接。取值范围为1025到
65535。系统默认为6666。该端口号需和SSO Monitor单点登录中配置的端口号一致，
否则无法通信。
域用户名
输入一个域用户的用户名，用于登录AD服务器。如果AD Agent运行在域内其他PC上，
要求该用户具有较高的权限，能够远程访问AD服务器上的事件日志，例如AD服务器上
权限是Domain Admins的Administrator用户。
密码
与域用户名对应的密码。若AD Agent运行在AD服务器所在设备上，则可以不填写域用
户名和密码。
服务器查询
启用事件日志查询
选择该选项，开启日志查询功能，能够查看AD服务器的事件日志。默认每隔5秒查询一
次。要实现AD Agent查询用户的功能，必须开启此开关。
查询间隔
设定轮询查找不同AD服务器的事件日志的间隔时间。取值范围为1到99秒，默认值为5
秒。每当查找完成一个AD服务器，AD Agent会将更新的用户信息发送给系统。
用户在线时长
设置用户单点登录成功后的在线时长，到期后用户将被下线。取值范围是1到99小时，
默认是8小时。
客户端探测
启用WMI探测
选中复选框，开启WMI协议查询。
l 要使WMI能够对终端PC进行探测查询，终端PC必须开启RPC服务以及远程管理。
开启RPC服务，进入“控制面板>管理工具>服务”，开启Remote Procedure
Call和Remote Procedure Call Locator；开启远程管理，以管理员身份运行命
令提示符窗口（cmd），输入命令netsh firewall set service RemoteAdmin。
l WMI协议辅助事件日志查询，定期查找用户列表中的所有IP。当发现终端PC的域
用户名与已存储名称不符时，将更新为探测到的域用户名。
探测间隔
设定主动发起WMI探测的间隔时间。取值范围为1到99分钟，默认值是20分钟。
慢速上线模式
选中复选框，开启慢速上线模式。防火墙中配置了角色映射规则后，该模式可以避免因
为客户端用户上线速度过快导致的角色映射失败。
6. 在<查询到的服务器>标签页，点击“自动获取”按钮，自动搜索域内的认证AD服务器。也可以点击“添加”按
钮，手动输入服务器IP地址，将其添加到服务器列表中。
7. 在<过滤的用户>标签页，在“过滤的用户名”文本框中输入用户名，点击“添加”按钮，该用户会显示在“过滤
的用户”列表中。最多可以配置100个过滤用户，且不区分大小写。
8. 在<查询到的用户>标签页，查看已经探测到的域用户名称和用户地址的对应关系。已经添加到“过滤的用户”列
表中的用户不会显示在该列表中。

<!-- 来源页 1372 -->
9. 点击页面右上角“提交”按钮，提交所有设置并启动AD Agent服务。
注意: 提交后，AD Agent的服务将一直在后台运行。如果需要修改设置，仅需要在<AD Agent设
置工具>对话框中编辑后点击“提交”，AD Agent服务立刻采用新的配置。
第二步：配置Active-Directory类型的AAA服务器。
hostname(config)# aaa-server ad type active-directroy
hostname(config-aaa-server)# host 192.168.2.2
hostname(config-aaa-server)# base-dn dc=hillstonenet
hostname(config-aaa-server)# login-dn cn=user,dc=hillstonenet
hostname(config-aaa-server)# login-password admin
hostname(config-aaa-server)# exit
hostname(config)#
第三步：启用并配置SSO Monitor功能，指定AD Agent服务的地址、端口、关联的AAA服务器（第二步中
配置的Active-Directory服务器）以及组织同步模式（需设置为“aaa-server”）。
hostname(config)#user-sso client sso-monitor test
hostname(config-aaa-server)# enable
hostname(config-aaa-server)# host1 10.180.201.8 vrouter trust-vr
hostname(config-aaa-server)# aaa-server ad
hostname(config-aaa-server)# org-source aaa-server
hostname(config-aaa-server)# port 6666
hostname(config-aaa-server)# exit
hostname(config)#
SSO Radius登录配置举例
以下为SSO Radius功能配置举例。启用SSO Radius功能后，系统可接收符合Radius标准协议的计费报
文，并根据报文内容获取用户认证信息、更新在线用户信息以及对用户进行上下线操作。
实现SSO Radius单点登录，按照以下步骤进行配置:
第一步：配置SSO Radius引用的AAA服务器。可以选择配置的Local、AD或者LDAP类型的服务器。此处
以AD服务器为例。

<!-- 来源页 1373 -->
hostname(config)# aaa-server ad type active-directroy
hostname(config-aaa-server)# host 1.1.1.1
hostname(config-aaa-server)# base-dn dc=hillstonenet
hostname(config-aaa-server)# login-dn cn=user,dc=hillstonenet
hostname(config-aaa-server)# login-password admin
hostname(config-aaa-server)# exit
hostname(config)#
第二步：启用SSO Radius功能，指定引用的AAA服务器和客户端IP地址等。
hostname(config)# user-sso server sso-radius default
hostname(config-sso-radius)# enable
hostname(config-sso-radius)# aaa-server ad
hostname(config-sso-radius)# client 2.2.2.2
hostname(config-sso-radius-client)# exit
hostname(config-sso-radius)# exit
hostname(config)#
例：通过SSO Web实现基于用户的网络访问控制
组网环境如下图所示，某企业在网络边界处部署了一台Hillstone防火墙作为出口网关，连接内部网络与
Internet。该企业将用户组织架构信息存储在AD服务器上，且通过第三方认证系统对用户进行认证。要求完
成SSO Web配置后，防火墙可以获取正确的用户认证信息，实现基于用户的用户组或者角色的网络访问控
制。

<!-- 来源页 1374 -->
SSO Web单点登录流程
1. 用户通过第三方认证系统进行身份认证。
2. 第三方认证系统通过HTTP(S) RESTful API请求将用户认证信息发送给防火墙。
根据发送的用户认证消息以及防火墙中AD服务器配置的不同，防火墙获取用户的用户组或者角色信息的方法不
同，分为以下四种情况：
l 如果发送给防火墙的用户认证信息中包含用户的用户组或者角色信息，防火墙直接获取到用户的用户组或
者角色信息；
l 如果发送给防火墙的用户认证信息中不包含用户组信息，且防火墙中AD服务器的同步对象配置为用户和
用户组，防火墙可以从AD服务器同步的数据中查找用户所属的用户组；
l 如果发送给防火墙的用户认证信息中不包含用户组信息，且防火墙中AD服务器的同步对象配置为仅同步
用户、仅同步用户组或者用户和用户组均不同步时，防火墙可以通过AD服务器查询用户所属的用户组；
l 如果发送给防火墙的用户认证信息中不包含角色信息，且防火墙中AD服务器配置了角色映射规则，防火
墙可以根据角色映射规则为用户映射角色。
3. 防火墙基于用户组或者角色对用户进行网络访问控制，且用户进行网络访问时，无需再次进行认证。
配置步骤
第一步：配置SSO Web引用的AAA服务器。可以选择配置Local、AD或者LDAP类型的服务器。本例中以
AD服务器为例。
hostname(config)# aaa-server adserver type active-directroy
hostname(config-aaa-server)# exit
hostname(config)#
（此处省略AD服务器的其它基础配置）
第二步：启用SSO Web功能，并指定AAA服务器。
hostname(config)# user-sso server sso-web default
hostname(config-sso-web)# enable
hostname(config-sso-web)# aaa-server adserver
hostname(config-sso-web)# exit
hostname(config)#
第三步：第三方认证系统的运维人员使用开发工具在第三方认证系统代码中构建HTTP(S) RESTful API请
求。第三方认证系统对用户认证成功后，调用防火墙API接口，将用户认证信息同步给防火墙。

<!-- 来源页 1375 -->
注意:
l
与第三方认证系统通信的防火墙接口需要开启HTTP或HTTPS服务。
l
第三方认证系统IP地址需要在防火墙可信主机范围内。
该示例中UserIP=120.1.1.163，UserName=qa_user1，Group=QA_Group，
Role=RnD-Group，防火墙接口IP地址为10.182.12.34，第三方认证系统的运维人员使
用开发工具在第三方认证系统中代码中构建以下HTTP(S) RESTful API请求：
构建HTTP(S) RESTful API请求的详细方法说明，请参阅在第三方认证系统中构建HTTP(S)
RESTful API请求。
l 用户上线请求：
http(s)://10.182.12.34/rest/api/sso-webuser?opr=login&info=MTIwLjEuMS4xNjMvcWFfdXNlcjEvL1FBX0dyb3VwLy9yb2xlP
VJuRC1Hcm91cA==
l 用户下线请求：
http(s)://10.182.12.34/rest/api/sso-webuser?opr=logout&info=MTIwLjEuMS4xNjMvcWFfdXNlcjEvL1FBX0dyb3VwLy9yb2xl
PVJuRC1Hcm91cA==
RESTful API请求返回结果说明如下：
GET：上线sso-web类型用户
上线成功：
HTTP/1.1 200 OK
ContentType:: application/json
Content-Length: 128
Success Example:
{
"success": true,
}
上线失败：

<!-- 来源页 1376 -->
HTTP/1.1 200 OK
Content-Type: application/json; charset="UTF-8"
Content-Length: 128
{
"success": false,
"exception": {
"code":"400000000",
"message":"Error: Request resolution failed",
"stack":""
}
}
GET：下线sso-web类型用户
下线成功：
HTTP/1.1 200 OK
ContentType:: application/json
Content-Length: 128
Success Example:
{
"success": true,
}
下线失败：
HTTP/1.1 200 OK
Content-Type: application/json; charset="UTF-8"
Content-Length: 128
{
"success": false,
"exception": {
"code":"400000000",

<!-- 来源页 1377 -->
"message":"Error: Request resolution failed",
"stack":""
}
}
第四步：结果验证。
用户成功上线后，防火墙获取用户的用户组或者角色信息，匹配策略规则中的Group和Role，实现
网络访问控制。
hostname(config)# show auth-user
Username: qa_user1
AAA Server: adserver
Authentication: User got from sso-web, online 5s
Reference Session: 0
Virtual Router: trust-vr
IP/MAC: 120.1.1.163
Auth user id: 1
Group: QA_Group
Role: RnD-Group
Authorization:
Agile Controller单点登录配置举例
以下为使用Agile Controller实现单点登录配置举例。完成配置后，系统可通过以下两种方式获取正确的用
户认证信息，从而实现单点登录：
l 接收Agile Controller服务器发送的用户上下线报文和用户信息更新报文；
l 当流经设备的流量匹配上已配置的查询地址范围，且本地没有对应的认证用户时，系统会主动查询Agile
Controller服务器上的用户信息，并进行本地用户信息更新。
使用Agile Controller实现单点登录，按照以下步骤进行配置:
第一步：配置Agile Controller引用的AAA服务器。可以选择配置的Local、AD或者LDAP类型的服务器。
此处以AD服务器为例。
hostname(config)# aaa-server ad type active-directroy

<!-- 来源页 1378 -->
hostname(config-aaa-server)# host 192.168.2.2
hostname(config-aaa-server)# base-dn dc=hillstonenet
hostname(config-aaa-server)# login-dn cn=user,dc=hillstonenet
hostname(config-aaa-server)# login-password admin
hostname(config-aaa-server)# exit
hostname(config)#
第二步：启用并配置Agile Controller功能。指定引用的AAA服务器、主动查询的源IP地址范围、Agile
Controller服务器的IP地址、共享密钥。
hostname(config)# user-sso server agile-controller default
hostname(config-agile-controller)# enable
hostname(config-agile-controller)# aaa-server ad
hostname(config-agile-controller)# sync-address address_book1
hostname(config-agile-controller)# access-agile-controller test
hostname(config-agile-controller-client)# host 1.1.1.1 vrouter trust-vr
hostname(config-agile-controller-client)# shared-secret Agilecon@123
hostname(config-agile-controller-client)# sync enable
hostname(config-agile-controller-client)# exit
hostname(config-agile-controller)# exit
hostname(config)#
TS Agent单点登录配置举例
以下为使用TS Agent实现单点登录配置举例。在Windows服务器上安装并运行Hillstone Terminal
Service Agent。启用TS Agent功能后，当用户通过远程桌面服务登录Windows服务器时，Hillstone
Terminal Service Agent为用户分配端口段，并将端口段和用户信息发送给设备，设备创建基于流量IP、
端口段和用户的映射信息，实现用户的“免登录”。
使用TS Agent实现单点登录，包含以下两个步骤：
l TS Agent服务器端配置，即在Windows服务器上安装并运行Hillstone Terminal Service Agent。
l TS Agent客户端配置，即在StoneOS上配置TS Agent功能。
第一步：在Windows服务器上安装并运行Hillstone Terminal Service Agent。

<!-- 来源页 1379 -->
1. 点击链接http://swupdate.hillstonenet.com:1337/sslvpn/download?os=windows-tsagent下载Hillstone
Terminal Service Agent安装程序。下载完成后，将其拷贝到Windows Server服务器上。
注意:
l
目前支持Windows Server 2008 R2，Windows Server 2016和Windows Server
2019。Windows Server 2008 R2必须装有Windows Server 2008 R2 Service
Pack 1以及KB3033929。
l
建议先关闭杀毒软件，再进行Hillstone Terminal Service Agent的安装。
2. 双击Hillstone Terminal Service Agent安装程序HSTSAgent.exe，按照安装向导提示逐步安装直至完成。
3. 双击Hillstone Terminal Service Agent快捷方式，弹出Hillstone Terminal Service Agent对话框。
4. 点击<监听配置>标签页，进行如下配置：
l 监听地址IPv4：0.0.0.0
l 监听端口（1025-65534）：5019
l 心跳时间间隔（1-30秒）：5
l 心跳超时时间（10-300秒）：60
点击“保存”按钮，保存配置。
5. 点击<端口配置>标签页，进行如下配置：
l 用户分配端口范围（1025-65534）：20000-39999
l 用户端口段大小（20-2000）：200
l 每用户最多端口段（1-256）：1
l 用户端口耗尽时允许系统分配端口：勾选
点击“保存”按钮，保存配置。
第二步：在StoneOS上配置TS Agent功能。
host-name(config)# user-sso client ts-agent tsagent1
host-name(config-ts-agent)# host 10.1.1.1
host-name(config-ts-agent)# aaa-server local
host-name(config-ts-agent)# traffic-ip 10.1.1.1
host-name(config-ts-agent)# enable
host-name(config-ts-agent)# exit

<!-- 来源页 1380 -->
hostname(config)#
例：Portal认证配置举例
该实例对通过设备上网的用户进行控制：仅允许user1通过Portal认证后上网，其它用户流量全部拒绝。认
证服务器为Portal认证服务器，IP地址为192.168.2.2。
第一步：配置角色以及角色映射规则：
hostname(config)# role role1
hostname(config)# role-mapping-rule role-mapping1
hostname(config-role-mapping)# match user-group usergroup1 role role1
hostname(config-role-mapping)# exit
hostname(config)#
第二步：配置接口与安全域：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 192.168.1.1/16
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 66.1.200.1/16
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# zone dmz
hostname(config-if-eth0/2)# ip address 192.168.2.1/16
hostname(config-if-eth0/2)# exit
hostname(config)#
第三步：配置认证服务器的角色映射规则以及开启服务器监控功能：
hostname(config)# aaa-server AD type active-directory
hostname(config-aaa-server)# role-mapping-rule role-mapping1

<!-- 来源页 1381 -->
hostname(config-aaa-server)# host 192.168.2.2
hostname(config-aaa-server)# base-dn “dc=hillstone”
hostname(config-aaa-server)# login-dn “user=administrators”
hostname(config-aaa-server)# login-password password1
hostname(config-aaa-server)# agent
hostname(config-aaa-server)# exit
hostname(config)#
第四步：通过策略规则触发Portal认证功能：
hostname(config)# rule id 1
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-ip 192.168.2.2/16
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# exit
hostname(config)# rule id 2
hostname(config-policy-rule)# role UNKNOWN
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# action portal-server http://192.168.2.2/
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# exit
hostname(config)# rule id 3 from any to any service any permit
第五步：配置允许访问的策略规则：
hostname(config)# policy-global
hostname(config-policy)# rule role role1 from 192.168.1.1/16 to any service any
permit
hostname(config-policy)# exit
hostname(config)#

<!-- 来源页 1382 -->
以上配置完成后，所有HTTP请求都会进行Portal认证，只有在认证页面输入用户名和密码分别为user1和
hillstone1，才可以访问网络。
例：802.1X配置举例
本节列举一个802.1X认证的典型配置示例。
组网需求
对通过Hillstone设备上网的用户进行控制，控制方式为基于MAC的802.1X认证，认证服务器为本地服务器
local。认证通过，允许用户通过端口ethernet0/0访问网络，否则禁止其访问。组网图如下：
配置步骤
第一步：创建用户和角色。
hostname(config)# aaa-server local
hostname(config-aaa-server)# user user1
hostname(config-user)# password password1
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)# role role1
第二步：配置角色映射规则。
hostname(config)# role-mapping-rule test
hostname(config-role-mapping)# match user user1 role role1

<!-- 来源页 1383 -->
hostname(config-role-mapping)# exit
hostname(config)# aaa-server local
hostname(config-aaa-server)# role-mapping-rule test
hostname(config-aaa-server)# exit
hostname(config)#
第三步：将接口绑定到安全域并配置接口的IP地址。
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone l2-trust
hostname(config-if-eth0/0)# exit
hostname(config)# interface vswitchif1
hostname(config-if-vsw1)# zone trust
hostname(config-if-vsw1)# ip address 192.168.1.1 255.255.255.0
hostname(config-if-vsw1)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 201.10.1.1 255.255.255.0
hostname(config-if-eth0/1)# exit
hostname(config)#
第四步：创建并配置802.1X profile。
hostname(config)# dot1x profile profile1
hostname(config-dot1x)# aaa-server local
hostname(config-dot1x)# exit
hostname(config)#
第五步：配置802.1X认证端口。
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# dot1x enable
hostname(config-if-eth0/0)# dot1x profile profile1
hostname(config-if-eth0/0)# dot1x control-mode mac

<!-- 来源页 1384 -->
hostname(config-if-eth0/0)# exit
hostname(config)#
第六步：配置允许访问的策略规则。
hostname(config)# address src-address
hostname(config-addr)# address 192.168.1.1/24
hostname(config-addr)# exit
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# role role1
hostname(config-policy-rule)# src-addr src-address
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
例：PKI配置举例
本节介绍通过IKE方式创建安全联盟的实例。IKE认证策略采用PKI证书体系进行身份认证。
组网需求
在Hillstone设备A和Hillstone设备B之间建立一个安全隧道，PC1作为Hillstone设备A端的主机，IP地址
为10.1.1.1，网关为10.1.1.2；Server1作为Hillstone设备B端的服务器，IP地址为192.168.1.1，网关是
192.168.1.2。要求对PC1代表的子网（10.1.1.0/24）与server1代表的子网（192.168.1.0/24）之间的
数据流进行安全保护。认证策略采用PKI证书体系，安全协议采用ESP协议，加密算法采用3DES，验证算法
采用SHA1。组网图如下图所示：

<!-- 来源页 1385 -->
配置步骤
第一步：配置Hillstone设备接口。
Hillstone设备A
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 10.1.1.2/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if)# zone untrust
hostname(config-if-eth0/1)# ip address 1.1.1.1/24
hostname(config-if-eth0/1)# exit
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone trust
hostname(config-if-tun1)# exit
Hillstone设备B
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 192.168.1.2/24

<!-- 来源页 1386 -->
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 1.1.1.2/24
hostname(config-if-eth0/1)# exit
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone trust
hostname(config-if-tun1)# exit
第二步：配置Hillstone设备策略规则。
Hillstone设备A
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit

<!-- 来源页 1387 -->
hostname(config)#
Hillstone设备B
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
第三步：配置P1提议，使用PKI身份认证方式。
Hillstone设备A
hostname(config)# isakmp proposal p1
hostname(config-isakmp-proposal)# authentication rsa-sig
hostname(config-isakmp-proposal)# group 2
hostname(config-isakmp-proposal)# hash sha
hostname(config-isakmp-proposal)# encryption 3des

<!-- 来源页 1388 -->
hostname(config-isakmp-proposal)# exit
Hillstone设备B
hostname(config)# isakmp proposal p1
hostname(config-isakmp-proposal)# authentication rsa-sig
hostname(config-isakmp-proposal)# group 2
hostname(config-isakmp-proposal)# hash sha
hostname(config-isakmp-proposal)# encryption 3des
hostname(config-isakmp-proposal)# exit
第四步：PKI配置。
Hillstone设备A
配置密钥对
hostname(config)# pki key generate rsa label 111 modulus 1024
配置PKI信任域
hostname(config)# pki trust-domain td1
hostname(config-trust-domain)# keypair 111
hostname(config-trust-domain)# enrollment terminal
hostname(config-trust-domain)# subject commonName aa
hostname(config-trust-domain)# subject country cn
hostname(config-trust-domain)# subject stateOrProvinceName bj
hostname(config-trust-domain)# subject localityName hd
hostname(config-trust-domain)# subject organization hillstone
hostname(config-trust-domain)# subject organizationunit rd
hostname(config-trust-domain)# exit
生成证书服务请求，并将请求发送到CA服务器，申请本地证书。
hostname(config)# pki enroll td1
认证CA证书
hostname(config)# pki authenticate td1
安装本地证书

<!-- 来源页 1389 -->
hostname(config)# pki import td1 certificate
Hillstone设备B
配置密钥对
hostname(config)# pki key generate rsa label 222 modulus 1024
配置PKI信任域
hostname(config)# pki trust-domain td2
hostname(config-trust-domain)# keypair 222
hostname(config-trust-domain)# enrollment terminal
hostname(config-trust-domain)# subject commonName aa
hostname(config-trust-domain)# subject country cn
hostname(config-trust-domain)# subject stateOrProvinceName bj
hostname(config-trust-domain)# subject localityName hd
hostname(config-trust-domain)# subject organization hillstone
hostname(config-trust-domain)# subject organizationunit rd
hostname(config-trust-domain)# exit
生成证书服务请求，并将请求发送到CA服务器，申请本地证书。
hostname(config)# pki enroll td2
认证CA证书
hostname(config)# pki authenticate td2
安装本地证书
hostname(config)# pki import td2 certificate
第五步：配置ISAKMP网关。
Hillstone设备A
hostname(config)# isakmp peer east
hostname(config-isakmp-peer)# interface ethernet0/1
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# peer 1.1.1.2
hostname(config-isakmp-peer)# local-id asn1dn

<!-- 来源页 1390 -->
hostname(config-isakmp-peer)# peer-id asn1dn
CN=bb,OU=rd,O=hillstone,L=hd,ST=bj,C=cn
hostname(config-isakmp-peer)# trust-domain td1
hostname(config-isakmp-peer)# exit
Hillstone设备B
hostname(config)# isakmp peer east
hostname(config-isakmp-peer)# interface ethernet0/1
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# peer 1.1.1.1
hostname(config-isakmp-peer)# local-id asn1dn
hostname(config-isakmp-peer)# peer-id asn1dn
CN=aa,OU=rd,O=hillstone,L=hd,ST=bj,C=cn
hostname(config-isakmp-peer)# trust-domain td2
hostname(config-isakmp-peer)# exit
第六步：配置P2提议
Hillstone设备A
hostname(config)# ipsec proposal p2
hostname(config-ipsec-proposal)# protocol esp
hostname(config-ipsec-proposal)# hash sha
hostname(config-ipsec-proposal)# encryption 3des
hostname(config-ipsec-proposal)# exit
Hillstone设备B
hostname(config)# ipsec proposal p2
hostname(config-ipsec-proposal)# protocol esp
hostname(config-ipsec-proposal)# hash sha
hostname(config-ipsec-proposal)# encryption 3des
hostname(config-ipsec-proposal)# exit
第七步：配置名为VPN的隧道。

<!-- 来源页 1391 -->
Hillstone设备A
hostname(config)# tunnel ipsec vpn auto
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# isakmp-peer east
hostname(config-tunnel-ipsec-auto)# id local 10.1.1.0/24 remote 192.168.1.0/24
service any
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)# interface tunnel1
hostname(config-if-tun1)# tunnel ipsec vpn
hostname(config-if-tun1)# exit
Hillstone设备B
hostname(config)# tunnel ipsec vpn auto
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# isakmp-peer east
hostname(config-tunnel-ipsec-auto)# id local 192.168.1.0/24 remote 10.1.1.0/24
service any
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)# interface tunnel1
hostname(config-if-tun1)# tunnel ipsec vpn
hostname(config-if-tun1)# exit
第八步：配置路由。
Hillstone设备A
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 192.168.1.0/24 tunnel1
hostname(config-vrouter)# exit
Hillstone设备B
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 10.1.1.0/24 tunnel1

<!-- 来源页 1392 -->
hostname(config-vrouter)# exit
