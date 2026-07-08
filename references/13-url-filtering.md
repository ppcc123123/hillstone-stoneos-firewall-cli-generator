# 数据安全与URL过滤

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 16  数据安全&URL过滤
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 2403 -->
16 数据安全&URL过滤
本章节包含以下内容：
l "数据安全" 在第2402页：介绍了系统包含的主要数据安全功能，包括内容过滤、文件过滤、上网行为审计以及
日志管理。
l "对象配置" 在第2442页：介绍了如何配置数据安全功能中的公用配置项，包括：预定义URL库、自定义URL库、
URL查询、关键字类别、页面提示、Bypass域名以及免监控用户。
l "URL过滤" 在第2458页：介绍了如何配置URL过滤功能实现控制用户对某些网站的访问。
l "SSL代理" 在第2465页：介绍了如何在两种典型的场景（当设备作为Web客户端一侧的网关时、当设备作为
Web服务器一侧的网关时）中配置SSL代理功能，从而解密HTTPS流量。

<!-- 来源页 2404 -->
数据安全
仅有部分平台支持该功能，请以实际页面为准。
系统提供数据安全功能，可以根据需要针对不同用户、不同上网行为、不同时间进行灵活的控制，对用户的
上网行为进行全面的行为控制和行为审计（记录行为日志）。通过对用户的网络访问行为、敏感数据进行控
制和审计，有效解决因接入互联网而可能引发的各种问题，防止数据信息泄露，优化对互联网资源的应用。
数据安全功能主要包括以下几个方面：
功能
说明
文件过滤
对使用HTTP(S)、FTP、SMTP(S)、IMAP(S)、POP3(S)以及SMB协议传输的文件进行检测，
对符合过滤条件的文件进行控制。
内容过滤
l 文件内容过滤：对指定协议类型、文件类型的文件内容中携带的敏感关键字进行检测，
并且可以对其进行日志记录或者阻断。
l 网页关键字：对用户访问含有某关键字的网页进行行为控制和行为审计。
l Web外发信息：对用户在某网站发布含有某关键字信息进行行为控制和行为审计。
l 邮件过滤：对用户使用SMTP(S)协议、POP3(S)协议、IMAP(S)协议外发邮件进行控
制。
l 应用行为控制：对FTP、HTTP(S)、TELNET应用程序行为进行控制和审计。
上网行为审计
对IM应用程序行为进行审计，并能对上网行为进行日志记录

<!-- 来源页 2405 -->
内容过滤
仅有部分平台支持该功能，请以实际页面为准。
内容过滤功能主要包括以下几个方面：
l "文件内容过滤" 在第2404页：对指定传输协议类型、文件类型的文件内容中携带的敏感关键字进行检测以及行
为控制。
l "网页关键字" 在第2407页：对用户访问含有某关键字的网页进行行为控制和行为审计：比如，禁止访问含“赌
博”词汇的网页，并记录访问行为日志。
l "Web外发信息" 在第2410页：对用户在某网站发布信息或者发布含有某关键字信息进行行为控制和行为审计：
比如，禁止在社区论坛上发布含“色情”词汇的信息，并记录发布行为日志。
l "邮件过滤" 在第2413页：对用户使用SMTP(S)/POP3(S)/IMAP(S)协议及Webmail外发邮件进行控制：
l 对所有邮件外发行为进行行为控制和行为审计。
l 对发送包含特定收件人、发件人、关键字内容的行为进行行为控制和行为审计。
l "应用行为控制" 在第2418页：对FTP、HTTP(S)和TELNET应用程序行为进行控制和审计：
l 对FTP的Login、Get、Put行为进行行为控制和行为审计。
l 对HTTP(S)的Connect、Get、Put、Head、Options、Post、Trace、Delete行为进行行为控制和行为审
计。
l 对TELNET客户端向服务器发起的请求内容进行行为控制和行为审计。

<!-- 来源页 2406 -->
文件内容过滤
文件内容过滤功能可以对指定协议类型、文件类型的文件内容中携带的敏感关键字进行检测，并且可以对其
进行日志记录或者阻断。比如，通过HTTP(S)协议下载的doc类型的文件内容进行检测，对于包含手机号关
键字内容的文件，进行记录日志信息。
网络管理员可以针对不同协议传输的不同类型文件制定适合的文件内容过滤规则，系统将会对与规则相匹配
的网络流量根据配置进行处理。
配置文件内容过滤功能
文件内容过滤功能可以对指定协议类型、文件类型的文件内容中携带的敏感关键字进行检测，并且可以对其
进行日志记录或者阻断。比如，通过HTTP协议下载的doc类型的文件内容进行识别，对于包含手机号关键字
内容的文件，进行记录日志信息。
配置文件内容过滤功能
文件内容过滤功能的CLI配置主要通过策略规则或安全域与Profile相结合的方式实现。将文件内容过滤
Profile绑定到策略规则或安全域后，系统将会对与策略规则或安全域相匹配的网络流量根据Profile配置进
行处理。系统还支持绑定文件内容过滤Profile到ZTNA策略，对与ZTNA策略相匹配的流量进行文件检测和
处理。相关配置请参阅配置ZTNA策略。
通过CLI配置文件内容过滤功能，请按照以下步骤进行操作：
1. 定义文件内容过滤Profile，在Profile中指定需要进行过滤的文件类型、协议类型、检测方向、关键字类别以及采
取的控制动作。
2. 将文件内容过滤Profile绑定到适当的策略规则或安全域。
创建文件内容过滤Profile
文件内容过滤Profile中主要指定需要进行过滤的文件类型、协议类型、检测方向、关键字类别以及采取的控
制动作。创建文件内容过滤Profile，在全局配置模式下使用以下命令：
file-contentfilter-profile profile-name
l
profile-name - 指定所创建的文件内容过滤Profile的名称，并且进入该文件内容过滤Profile的配置模
式。如果指定名称已存在，则直接进入文件内容过滤Profile配置模式。
使用no file-contentfilter-profile profile-name删除指定的文件内容过滤Profile。
指定文件类型
指定需要进行文件内容过滤的文件类型，在文件内容过滤Profile配置模式下使用以下命令：

<!-- 来源页 2407 -->
file-type {txt | doc | docx | ppt | pptx | xls | xlsx}
l
txt | doc | docx | ppt | pptx | xls | xlsx - 指定需要进行文件内容过滤的文件类型，目前仅支持txt，
doc，docx，ppt，pptx，xls，xlsx类型文件。
重复使用以上命令可指定多个文件类型。
在文件内容过滤Profile配置模式下，使用no file-type {txt | doc | docx | ppt | pptx | xls | xlsx}取消文
件类型的指定。
指定关键字类别及控制动作
指定需要进行控制的关键字类别及控制动作，在文件内容过滤Profile配置模式下使用以下命令：
keyword-category keyword-category-name action {block | log-only}
l
keyword-category-name - 指定需要进行控制的关键字类别名称。可以为自定义关键字类别或预定义
关键字类别。
l
block – 指定阻止传输含有相应关键字内容的文件并进行日志记录。
l
log-only – 指定对传输含有相应关键字内容的文件的行为进行日志记录。
重复使用以上命令可指定多个关键字类别及相应的控制动作。
在文件内容过滤Profile配置模式下，使用no keyword-category keyword-category-name命令取消
关键字类别及控制动作的指定。
指定协议类型及检测方向
指定需要进行控制的协议类型及检测方向，在文件内容过滤Profile配置模式下使用以下命令：
protocol-type {ftp | http | imap4 | pop3 | smb | smtp } direction {both | download | upload}
l
ftp | http | imap4 | pop3 | smb | smtp - 指定协议类型。
l
direction {both | download | upload}- 指定检测方向，包含双向both、下载download、上传
upload。HTTP、FTP、SMB协议支持指定的方向为下载、上传、双向；SMTP协议仅支持指定为上
传；POP3、IMAP协议仅支持指定为下载。
在文件内容过滤Profile配置模式下，使用no protocol-type命令取消协议类型及检测方向的指定。
绑定文件内容过滤Profile到策略规则
将文件内容过滤Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据Profile配置进行处
理。绑定文件内容过滤Profile到策略规则，需要在策略规则配置模式下进行。

<!-- 来源页 2408 -->
进入策略规则配置模式需要进行两步配置。首先，在全局配置模式下，输入以下命令进入策略配置模式：
policy-global
然后，在策略配置模式下，输入以下命令进入策略规则配置模式：
rule [id id-number]
进入策略规则配置模式后，输入以下命令将文件内容过滤Profile绑定到策略规则：
file-contentfilter profile-name
l
profile-name - 指定所需要绑定的文件内容过滤Profile名称。
绑定文件内容过滤Profile到安全域
将文件内容过滤Profile绑定到安全域后，系统将会对以该安全域为目的安全域的流量按照Profile配置进行
处理。当策略规则已经绑定了文件内容过滤Profile，同时策略规则的目的安全域也绑定了文件内容过滤
Profile，策略规则绑定的文件内容过滤Profile将会生效，而目的安全域绑定的文件内容过滤Profile无效。
绑定文件内容过滤Profile到安全域，在安全域配置模式下，使用以下命令：
file-contentfilter enable profile-name
l
profile-name – 指定绑定到安全域的文件内容过滤Profile的名称。一个安全域只能绑定一个文件内容
过滤Profile。
在安全域配置模式下，使用该命令no的形式取消文件内容过滤Profile的绑定：
no file-contentfilter enable
显示文件内容过滤Profile信息
在任何模式下，输入以下命令显示文件内容过滤Profile信息：
show file-contentfilter-profile [profile-name]
l
profile-name – 显示指定文件内容过滤Profile的信息。若不指定Profile名称，显示系统中所有文件内
容过滤Profile的信息。

<!-- 来源页 2409 -->
网页关键字
网页关键字功能可以对用户访问含有特定关键字内容的网站的行为进行控制，并能对访问行为进行日志记
录。比如，阻止用户访问含“赌博”词汇的网站，并记录访问行为日志。网络管理员可以针对不同上网行为
制定适合的网页关键字规则，系统将会对与规则相匹配的网络流量根据配置进行处理。
配置网页关键字功能
网页关键字功能的CLI配置主要通过策略规则或安全域与Profile相结合的方式实现。将网页关键字Profile绑
定到策略规则或安全域后，系统将会对与策略规则或安全域相匹配的网络流量根据Profile配置进行处理。
通过CLI配置网页关键字功能，请按照以下步骤进行操作：
1. 定义网页关键字Profile，在Profile中指定需要进行控制的关键字类别、采取的控制动作以及关键字控制范围，另
外还能配置仅过滤网页内容功能。
2. 将网页关键字Profile绑定到适当的策略规则或安全域。
创建网页关键字Profile
网页关键字Profile中主要指定需要进行控制的关键字类别、采取的控制动作以及关键字控制范围。创建网页
关键字Profile，在全局配置模式下使用以下命令：
contentfilter-profile profile-name
l
profile-name - 指定所创建的网页关键字Profile的名称，并且进入该网页关键字Profile的配置模式。
如果指定名称已存在，则直接进入网页关键字Profile配置模式。使用no contentfilter-profile
profile-name删除指定的网页关键字Profile。
指定关键字类别及控制动作
指定需要进行控制的关键字类别及控制动作，在网页关键字Profile配置模式下使用以下命令：
keyword-category keyword-category-name { [block] [log] }
l
keyword-category-name - 指定需要进行控制的关键字类别名称。可以为自定义关键字类别或预定义
关键字类别。
l
block – 指定阻止访问内容中含有相应关键字的网站。
l
log – 指定对访问含有相应关键字内容的网站的行为进行日志记录。
使用多条该命令可指定多个关键字类别及相应的控制动作。

<!-- 来源页 2410 -->
在网页关键字Profile配置模式下，使用no keyword-category keyword-category-name命令取消关键
字类别及控制动作的指定。
指定关键字控制范围
系统会对指定的网站做关键字控制。指定关键字控制范围，在网页关键字Profile配置模式下使用以下命令：
url-category {all | url-category-name}
l
all | url-category-name – 指定需要进行关键字控制的URL类别名称，可以为所有的URL类别（all）
或者特定URL类别（url-category-name）。
使用多条该命令可指定多个URL类别。
在网页关键字Profile配置模式下，使用no url-category {all | url-category-name}命令取消URL类别的
指定。
仅过滤网页内容
默认情况下，配置网页关键字功能对HTML网页进行关键字过滤时，系统不但对网页中显示的内容进行过
滤，也对HTML标签中的代码进行过滤。如果用户仅想使用关键字过滤HTML网页中显示的内容，在网页关键
字Profile配置模式下，使用以下命令：
exclude-html-tag
在网页关键字Profile配置模式下，使用该命令no的形式恢复默认值：
no exclude-html-tag
注意: 仅当HTML的content类型为“text/html”，即content="text/html"时，该功能生效。
绑定网页关键字Profile到策略规则
将网页关键字Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据Profile配置进行处理。
绑定网页关键字Profile到策略规则，需要在策略规则配置模式下进行。
进入策略规则配置模式需要进行两步配置。首先，在全局配置模式下，输入以下命令进入策略配置模式：
policy-global
然后，在策略配置模式下，输入以下命令进入策略规则配置模式：
rule [id id-number]
进入策略规则配置模式后，输入以下命令将网页关键字Profile绑定到策略规则
contentfilter profile-name

<!-- 来源页 2411 -->
l
profile-name - 指定所需要绑定的网页关键字Profile名称。
绑定网页关键字Profile到安全域
将网页关键字Profile绑定到安全域后，系统将会对以该安全域为目的安全域的流量按照Profile配置进行处
理。当策略规则已经绑定了网页关键字Profile，同时策略规则的目的安全域也绑定了网页关键字Profile，
策略规则绑定的网页关键字Profile将会生效，而目的安全域绑定的网页关键字Profile无效。
绑定网页关键字Profile到安全域，在安全域配置模式下，使用以下命令：
contentfilter enable profile-name
l
profile-name – 指定绑定到安全域的网页关键字Profile的名称。一个安全域只能绑定一个网页关键字
Profile。
在安全域配置模式下，使用该命令no的形式取消网页关键字Profile的绑定：
no contentfilter enable
显示网页关键字Profile信息
在任何模式下，输入以下命令显示网页关键字Profile信息：
show contentfilter-profile [profile-name]
l
profile-name – 显示指定网页关键字Profile的信息。若不指定Profile名称，显示系统中所有网页关键
字Profile的信息。

<!-- 来源页 2412 -->
Web外发信息
Web外发信息功能可以对用户在某网站发布信息或者发布含有特定关键字信息的行为进行控制，并能对发布
行为进行日志记录。例如，阻止用户在社区论坛类网站发布含有关键字“舆论”的信息，并记录发布行为日
志。网络管理员可以针对不同信息发布行为制定适合的Web外发信息规则，系统将会对与规则相匹配的网络
流量根据配置进行处理。
配置Web外发信息功能
Web外发信息功能的CLI配置主要通过策略规则或安全域与Profile相结合的方式实现。将Web外发信息
Profile绑定到策略规则或安全域后，系统将会对与策略规则或安全域相匹配的网络流量根据Profile配置进
行处理。
通过CLI配置Web外发信息功能，请按照以下步骤进行操作：
1. 定义Web外发信息Profile，在Profile中指定需要进行控制的Web外发信息类型、采取的控制动作以及网站控制
范围。
2. 将Web外发信息Profile绑定到适当的策略规则或安全域。
创建Web外发信息Profile
Web外发信息Profile中主要指定需要进行控制的Web外发信息类型、采取的控制动作以及网站控制范围。
创建Web外发信息Profile，在全局配置模式下使用以下命令：
webpost-profile profile-name
l
profile-name - 指定所创建的Web外发信息Profile的名称，并且进入该Web外发信息Profile的配置
模式。如果指定名称已存在，则直接进入Web外发信息Profile配置模式。使用no webpost-profile
profile-name删除指定的Web外发信息Profile。
指定Web外发信息类型及控制动作
用户可以指定控制所有Web外发信息或者控制含有特定关键字的Web外发信息。
指定控制所有Web外发信息和控制动作，在Web外发信息Profile配置模式下使用以下命令：
webpost all [block] [log]
l
block – 指定阻止所有信息发布行为。
l
log – 指定对所有信息发布行为进行日志记录。
在Web外发信息Profile配置模式下，使用no webpost all命令取消控制所有Web外发信息的指定。

<!-- 来源页 2413 -->
指定控制含有特定关键字的Web外发信息和控制动作，在Web外发信息Profile配置模式下使用以下命令：
keyword-category keyword-category-name { [block] [log] }
l
keyword-category-name - 指定需要进行控制的关键字类别名称。可以为自定义关键字类别或预定义
关键字类别。
l
block – 指定阻止发布含有相应关键字的信息。
l
log – 指定对发布含有相应关键字信息的行为进行日志记录。
使用多条该命令可指定多个关键字类别及相应的控制动作。
在Web外发信息Profile配置模式下，使用no keyword-category keyword-category-name命令取消
关键字类别及控制动作的指定。
指定网站控制范围
系统会对指定的网站做外发信息控制。指定需要进行外发信息控制的网站，在Web外发信息Profile配置模
式下使用以下命令：
url-category {all | url-category-name}
l
all | url-category-name – 指定需要进行外发信息控制的URL类别名称，可以为所有的URL类别
（all）或者特定URL类别（url-category-name）。
使用多条该命令可指定多个URL类别。
在Web外发信息Profile配置模式下，使用no url-category {all | url-category-name}命令取消URL类
别的指定。
绑定Web外发信息Profile到策略规则
将Web外发信息Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据Profile配置进行处
理。绑定Web外发信息Profile到策略规则，需要在策略规则配置模式下进行。
进入策略规则配置模式需要进行两步配置。首先，在全局配置模式下，输入以下命令进入策略配置模式：
policy-global
然后，在策略配置模式下，输入以下命令进入策略规则配置模式：
rule [id id-number]
进入策略规则配置模式后，输入以下命令将Web外发信息Profile绑定到策略规则
webpost profile-name
l
profile-name - 指定所需要绑定的Web外发信息Profile名称。

<!-- 来源页 2414 -->
绑定Web外发信息Profile到安全域
将Web外发信息Profile绑定到安全域后，系统将会对以该安全域为目的安全域的流量按照Profile配置进行
处理。当策略规则已经绑定了Web外发信息Profile，同时策略规则的目的安全域也绑定了Web外发信息
Profile，策略规则绑定的Web外发信息Profile将会生效，而目的安全域绑定的Web外发信息Profile无
效。
绑定Web外发信息Profile到安全域，在安全域配置模式下，使用以下命令：
webpost enable profile-name
l
profile-name – 指定绑定到安全域的Web外发信息Profile的名称。一个安全域只能绑定一个Web外发
信息Profile。
在安全域配置模式下，使用该命令no的形式取消Web外发信息Profile的绑定：
no webpost enable
显示Web外发信息Profile信息
在任何模式下，输入以下命令显示Web外发信息Profile信息：
show webpost-profile [profile-name]
l
profile-name – 显示指定Web外发信息Profile的信息。若不指定Profile名称，显示系统中所有Web
外发信息Profile的信息。

<!-- 来源页 2415 -->
邮件过滤
邮件过滤功能主要用于当用户通过SMTP邮箱发送邮件时，根据邮件的发件人、收件人、内容，对邮件进行
控制并记录日志；当用户通过POP3、IMAP邮箱接收邮件时，根据邮件内容，对邮件进行控制并记录日志。
外部动态列表可以应用于企业管理多台防火墙的场景中。通过将外部动态列表应用于防火墙的邮件过滤，企
业可以实现高效、统一的策略管理。管理员仅需在服务器上更新外部动态列表文件，所有关联的防火墙便会
按预设周期，自动同步文件内容。这种机制极大地简化了运维管理流程，避免了对每台防火墙逐一进行配置
更新，有效降低运维人员的工作负担。
配置邮件过滤功能
型号说明：
SG-6000 SDW 系列不支持邮件过滤功能。
邮件过滤功能的CLI配置主要通过策略规则或安全域与Profile相结合的方式实现。将邮件过滤Profile绑定到
策略规则或安全域后，系统将会对与策略规则或安全域相匹配的网络流量根据Profile配置进行处理。
通过CLI配置邮件过滤功能，请按照以下步骤进行操作：
1. 定义邮件过滤Profile，在Profile中指定需要进行控制的邮件类型、采取的控制动作、受控邮箱以及例外帐号。
2. 将邮件过滤Profile绑定到适当的策略规则或安全域。
创建邮件过滤Profile
邮件过滤Profile中主要指定需要进行控制的邮件类型、采取的控制动作、受控邮箱以及例外帐号。创建邮件
过滤Profile，在全局配置模式下使用以下命令：
mail-profile profile-name
l
profile-name - 指定所创建的邮件过滤Profile的名称，并且进入该邮件过滤Profile的配置模式。如果
指定名称已存在，则直接进入邮件过滤Profile配置模式。使用no mail-profile profile-name删除指
定的邮件过滤Profile。
指定受控邮箱
默认情况下，邮件过滤规则对系统支持的所有邮箱类型进行控制。指定受控制的邮箱类型，在邮件过滤
Profile配置模式下使用以下命令：
mail control {smtp | pop3 | imap}

<!-- 来源页 2416 -->
l
smtp - 指定需要进行控制的邮箱类型为SMTP邮件。
l
pop3- 指定需要进行控制的邮箱类型为POP3邮件。
l
imap- 指定需要进行控制的邮箱类型为IMAP邮件。
在邮件过滤Profile配置模式下，使用no mail control {smtp | pop3 | imap}命令取消邮箱类型的指定。
指定所有邮件及控制动作
指定控制所有外发邮件及控制动作，在邮件过滤Profile配置模式下使用以下命令：
mail any [log] – 指定对所有的外发邮件行为进行日志记录。
在邮件过滤Profile配置模式下，使用no mail any命令取消对所有邮件进行控制的指定。
指定发件人和收件人及控制动作
指定需要进行控制的发件人或者收件人及控制动作，在邮件过滤Profile配置模式下使用以下命令：
mail {sender email-address | sender-external-dynamic-list external-dynamic-list-name |
recipient email-address | recipient-external-dynamic-list external-dynamic-list-name}
[block | log]
l
sender | recipient – 指定对外发邮件的发件人（sender）或者收件人（recipient）进行控制。
l
sender-external-dynamic-list | recipient-external-dynamic-list – 指定对外发邮件的发件人
（sender）或者收件人（recipient）的外部动态列表进行控制。
l
email-address – 指定发件人或者收件人邮箱帐号。支持两种输入格式：一种为用户名精确匹配，以
126邮箱为例，用户需输入"user-name@126.com"；另一种为用户通配符匹配，同样以126邮箱为
例，用户需输入"*@126.com"。
l
external-dynamic-list-name – 指定发件人或者收件人的外部动态列表。仅支持指定邮箱类型的外部
动态列表。external-dynamic-list-name非自定义项，为系统中已配置的邮箱类型的外部动态列表名
称。
l
block – 指定阻止发送含特定发件人或者收件人的邮件。
l
log – 指定对发送含有特定发件人或者收件人邮件的行为进行日志记录。
使用多条该命令可指定多个发件人或者收件人及相应的控制动作。
在邮件过滤Profile配置模式下，使用no mail {sender email-address | sender-external-dynamiclist external-dynamic-list-name | recipient email-address | recipient-external-dynamic-list
external-dynamic-list-name}命令取消发件人或者收件人及控制动作的指定。

<!-- 来源页 2417 -->
指定内容关键字及控制动作
指定控制含有特定关键字内容的外发邮件及控制动作，在邮件过滤Profile配置模式下使用以下命令：
keyword-category keyword-category-name { [block] [log] }
l
keyword-category-name - 指定需要进行控制的关键字类别名称。可以为自定义关键字类别或预定义
关键字类别。
l
block – 指定阻止发送含有相应关键字的邮件。
l
log – 指定对发送含有相应关键字邮件的行为进行日志记录。
使用多条该命令可指定多个关键字类别及相应的控制动作。
在邮件Profile配置模式下，使用no keyword-category keyword-category-name命令取消关键字类别
及控制动作的指定。
启用/禁用指定邮件控制内容
启用指定邮件控制内容，在邮件过滤Profile配置模式下使用以下命令：
mail enable {sender | recipient | attach | keyword-category}
l
sender | recipient | attach | keyword-category – 指定启用对邮件发件人（sender）、收件人
（recipient）、附件（attach）和内容关键字（keyword-category）的控制。默认情况下，都为启
用状态。
在邮件Profile配置模式下，使用no mail enable {sender | recipient | attach | keyword-category}
命令关闭指定邮件控制内容。
指定其它邮件及控制动作
其它邮件为系统中已配置的指定邮件控制内容（包含特定发件人、收件人、内容关键字或附件的邮件）以外
的邮件。指定其它邮件及控制动作，在邮件过滤Profile配置模式下使用以下命令：
mail others [block] [log]
l
block – 指定阻止发送特定邮件控制内容以外的邮件。
l
log – 指定对发送特定邮件控制内容以外邮件的行为进行日志记录。
在邮件过滤Profile配置模式下，使用no mail others命令取消对其它邮件进行控制的指定。

<!-- 来源页 2418 -->
指定例外帐号
例外帐号为不受邮件过滤规则控制的邮箱帐号，可以为发件人帐号、收件人帐号或外部动态列表。指定例外
帐号，在邮件过滤Profile配置模式下使用以下命令：
mail {allowlist mail-address | allowlist-external-dynamic-list external-dynamic-list-name}
l
mail-address – 指定不受邮件过滤策略规则控制的邮箱帐号。支持两种输入格式：一种为用户名精确
匹配，以126邮箱为例，用户需输入"user-name@126.com"；另一种为用户通配符匹配，同样以126
邮箱为例，用户需输入"*@126.com"。
l
external-dynamic-list-name – 指定不受邮件过滤策略规则控制的外部动态列表。仅支持指定邮箱类
型的外部动态列表。external-dynamic-list-name非自定义项，为系统中已配置的邮箱类型的外部动
态列表名称。
使用多条该命令可指定多个例外帐号。
在邮件过滤Profile配置模式下，使用no mail {allowlist mail-address | allowlist-externaldynamic-list external-dynamic-list-name}命令取消例外帐号的指定。
绑定邮件过滤Profile到策略规则
将邮件过滤Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据Profile配置进行处理。绑
定邮件过滤Profile到策略规则，需要在策略规则配置模式下进行。
进入策略规则配置模式需要进行两步配置。首先，在全局配置模式下，输入以下命令进入策略配置模式：
policy-global
然后，在策略配置模式下，输入以下命令进入策略规则配置模式：
rule [id id-number]
进入策略规则配置模式后，输入以下命令将邮件过滤Profile绑定到策略规则
mail profile-name
l
profile-name - 指定所需要绑定的邮件过滤Profile名称。
绑定邮件过滤Profile到安全域
将邮件过滤Profile绑定到安全域后，系统将会对以该安全域为目的安全域的流量按照Profile配置进行处
理。当策略规则已经绑定了邮件过滤Profile，同时策略规则的目的安全域也绑定了邮件过滤Profile，策略
规则绑定的邮件过滤Profile将会生效，而目的安全域绑定的邮件过滤Profile无效。
绑定邮件过滤Profile到安全域，在安全域配置模式下，使用以下命令：

<!-- 来源页 2419 -->
mail enable profile-name
l
profile-name – 指定绑定到安全域的邮件过滤Profile的名称。一个安全域只能绑定一个邮件过滤
Profile。
在安全域配置模式下，使用该命令no的形式取消邮件过滤Profile的绑定：
no mail enable
显示邮件过滤Profile信息
在任何模式下，输入以下命令显示邮件过滤Profile信息：
show mail-profile [profile-name]
l
profile-name – 显示指定邮件过滤Profile的信息。若不指定Profile名称，显示系统中所有邮件过滤
Profile的信息。
在任何模式下，输入以下命令显示指定邮件控制内容信息：
show mail-object [mail-profile profile-name]
l
mail-profile profile-name – 显示指定邮件过滤Profile中的指定邮件控制内容信息。若不指定，显
示系统中所有指定邮件控制内容信息。

<!-- 来源页 2420 -->
应用行为控制
应用行为控制功能可以对FTP、HTTP和TELNET应用行为进行控制和审计（记录日志），包括：
l 对FTP协议传输的内容，以及FTP的Login、Get、Put行为进行行为控制和行为审计；
l 对HTTP的Connect、Get、Put、Head、Options、Post、Trace、Delete行为进行行为控制和行为审计；
l 对TELNET客户端向服务器发起的请求内容进行控制和审计。
网络管理员可以针对不同用户、不同时间、不同应用程序行为制定适合的应用行为控制规则，系统将会对与
规则相匹配的网络流量根据配置进行处理。
配置应用行为控制功能
应用行为控制功能的CLI配置主要通过策略规则或安全域与Profile相结合的方式实现。将行为Profile绑定到
策略规则或安全域后，系统将会对与策略规则或安全域相匹配的网络流量根据Profile配置进行处理。
通过CLI配置应用行为控制功能，请按照以下步骤进行操作：
1. 定义行为Profile，在Profile中指定需要进行控制的FTP行为、HTTP行为、TELNET行为以及采取的控制动作。
2. 将行为Profile绑定到适当的策略规则或安全域。
创建行为Profile
行为Profile中主要指定需要进行控制的FTP行为、HTTP行为、TELNET行为以及采取的控制动作。创建行为
Profile，在全局配置模式下使用以下命令：
behavior-profile profile-name
l
profile-name - 指定所创建的行为Profile的名称，并且进入该行为Profile的配置模式。如果指定名称
已存在，则直接进入行为Profile配置模式。使用no behavior-profile profile-name删除指定的行为
Profile。
FTP控制
在行为Profile配置模式下，用户可以使用以下命令对FTP应用程序行为配置控制操作：
ftp {login [user-name] | get [file-name] | put [file-name]} {block | permit} [log]
l
login [user-name] – 对FTP的登录行为进行控制。如果使用user-name参数指定用户名，可对指定用
户的登录行为进行控制。

<!-- 来源页 2421 -->
l
get [file-name] – 对FTP的Get行为进行控制。如果使用file-name参数指定文件名，可对指定文件的
Get行为进行控制。
l
put [file-name] – 对FTP的Put行为进行控制。如果使用file-name参数指定文件名，可对指定文件的
Put行为进行控制。
l
block | permit – 指定控制动作，可以是阻止（block），或者允许（permit）。
l
log – 指定对FTP应用程序行为进行日志记录。
在行为Profile配置模式下，使用以上命令no的形式取消相应的FTP行为控制：
no ftp {login [user-name] | get [file-name] | put [file-name]}
HTTP控制
在行为Profile配置模式下，用户可以使用以下命令对HTTP应用程序行为配置控制操作：
http {connect | delete [host] | get [host] | head [host] | options [host] | post [host] | put [host] |
trace [host]} {block | permit} [log]
l
connect | delete [host] | get [host] | head [host] | options [host] | post [host] | put [host] |
trace [host] – 指定对HTTP应用程序的请求方法进行控制。如果使用host参数指定主机名称，可对指定
主机的行为进行控制。
l
block | permit – 指定控制动作，可以是阻止（block），或者允许（permit）。
l
log – 指定对HTTP应用程序行为进行日志记录。
在行为Profile配置模式下，使上命令no的形式取消相应的HTTP行为控制：
no http {connect | delete [host] | get [host] | head [host] | options [host] | post [host] | put
[host] | trace [host]}
TELNET控制
在行为Profile配置模式下，用户可以使用以下命令对TELNET客户端发起的请求内容进行控制：
telnet keyword-category keyword-category-name{ [block] [log] }
l
keyword-category-name - 指定需要进行控制的关键字类别名称。可以为自定义关键字类别或预定义
关键字类别。
l
block – 对请求内容中包含相应关键字类别的行为进行阻断。
l
log – 对请求内容中包含相应关键字类别的行为记录日志。

<!-- 来源页 2422 -->
在行为Profile配置模式下，使用no telnet keyword-category keyword-category-name命令取
消对TELNET行为的控制。
绑定行为Profile到策略规则
将行为Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据Profile配置进行处理。绑定行
为Profile到策略规则，需要在策略规则配置模式下进行。
进入策略规则配置模式需要进行两步配置。首先，在全局配置模式下，输入以下命令进入策略配置模式：
policy-global
然后，在策略配置模式下，输入以下命令进入策略规则配置模式：
rule [id id-number]
进入策略规则配置模式后，输入以下命令将行为Profile绑定到策略规则
behavior profile-name
l
profile-name - 指定所需要绑定的行为Profile名称。
绑定行为Profile到安全域
将行为Profile绑定到安全域后，系统将会对以该安全域为目的安全域的流量按照Profile配置进行处理。当
策略规则已经绑定了行为Profile，同时策略规则的目的安全域也绑定了行为Profile，策略规则绑定的行为
Profile将会生效，而目的安全域绑定的行为Profile无效。
绑定行为Profile到安全域，在安全域配置模式下，使用以下命令：
behavior enable profile-name
l
profile-name – 指定绑定到安全域的行为Profile的名称。一个安全域只能绑定一个行为Profile。
在安全域配置模式下，使用该命令no的形式取消行为Profile的绑定：
no behavior enable
显示行为Profile信息
在任何模式下，输入以下命令显示行为Profile信息：
show behavior-profile [profile-name]
l
profile-name – 显示指定行为Profile的信息。若不指定Profile名称，显示系统中所有行为Profile的
信息。
在任何模式下，输入以下命令显示行为Profile的对象信息：

<!-- 来源页 2423 -->
show behavior-object [behavior-profile profile-name]
l
behavior-profile profile-name – 显示指定行为Profile的对象信息。若不指定，显示系统中所有行
为Profile的对象信息。

<!-- 来源页 2424 -->
文件过滤
文件过滤功能是对通过HTTP(S）、FTP、SMTP(S)、IMAP(S)、POP3(S)以及SMB协议传输的文件进行检
测，对符合过滤条件的文件进行控制。
l 支持通过HTTP(S) GET/POST方法、FTP、SMTP(S)、IMAP(S)、POP3(S)、SMB传输的文件进行检测和控制。对
于SMB协议，系统还支持断点续传场景下的文件检测和控制。
l 支持对文件类型设置过滤条件。
l 可对符合过滤条件的文件进行阻断传输、记录日志、允许访问等控制动作。
如设备开启了IPv6，文件过滤功能支持基于IPv6的文件检测和行为控制。
文件过滤功能需要通过策略规则与文件过滤规则相结合的方式实现。将文件过滤规则绑定到策略规则后，系
统将会对与策略规则相匹配的网络流量根据文件过滤规则配置进行处理。系统还支持绑定文件过滤规则到
ZTNA策略，对与ZTNA策略相匹配的流量进行文件检测和处理。相关配置请参阅配置ZTNA策略。
各协议支持的过滤条件如下表所述：
HTTP
FTP
SMTP
POP3
SMB
GET
POST
文件大小
√
√
√
√
√
√
文件类型
√
√
√
√
√
√
文件名称
√
√
√
√
√
√
配置文件过滤功能
文件过滤功能的CLI配置主要通过策略规则与文件过滤Profile相结合的方式实现。将文件过滤Profile绑定到
策略规则后，系统将会对与策略规则相匹配的网络流量根据文件过滤Profile配置进行处理。系统还支持绑定
文件过滤Profile到ZTNA策略，对与ZTNA策略相匹配的流量进行文件检测和处理。相关配置请参阅配置
ZTNA策略。
通过CLI配置文件过滤功能，请按照以下步骤进行操作：
1. 定义文件过滤Profile，在Profile中创建过滤规则。
2. 在过滤规则中指定需要进行检测的协议、过滤条件以及控制动作。
3. 将文件过滤Profile绑定到适当的策略规则。
创建文件过滤Profile
创建文件过滤Profile，在全局配置模式下使用以下命令：

<!-- 来源页 2425 -->
dlp-profile profile-name
l
profile-name - 指定所创建的文件过滤Profile的名称，并且进入该文件过滤Profile的配置模式。如果
指定名称已存在，则直接进入文件过滤Profile配置模式。
使用no dlp-profile profile-name删除指定的文件过滤Profile。
创建过滤规则
过滤规则用来指定需要进行检测的协议、过滤条件、以及控制动作。创建过滤规则，在文件过滤Profile配置
模式下，使用以下命令：
filter id id-number
l
id id-number – 指定所创建的过滤规则的ID，并且进入该过滤规则的配置模式。如果指定ID已存在，
则直接进入过滤规则配置模式。ID取值范围为1至8，即系统最多允许配置8个过滤规则。
如果任一一个过滤规则的控制动作为阻断(block)且文件符合此过滤规则，则系统直接阻断当前上传或下
载；如果文件符合的一个或多个过滤规则中没有设置阻断(block)控制动作，则放行文件并记录日志；
使用no filter id id-number删除指定的过滤条件。
指定文件大小
当传输的文件大小达到指定的值时，将触发控制动作。指定文件大小，在过滤规则配置模式下，使用如下命
令：
file-size-threshold size-value
l
size-value – 指定文件大小。取值范围为1到512000，单位KB。
使用no file-size-threshold命令取消文件大小的指定。
指定文件名称
当传输的文件名称符合指定的名称时，将触发控制动作。指定文件名称，在过滤规则配置模式下，使用如下
命令：
file-name name
l
name – 指定文件名称。长度为1到255个字符。一个过滤规则中可最多指定32个文件名称。如果指定的
文件名称当中没有通配符，则只有传输的文件名与指定的文件名称完全匹配时，才会触发控制动作；如
果指定的文件名称中有通配符*，则传输的文件名只要包含*后面的字符串，就会触发控制动作。
使用no file-name name命令取消文件名称的指定。

<!-- 来源页 2426 -->
指定协议类型
系统将对指定的协议进行检测。指定协议类型，在过滤规则配置模式下，使用如下命令：
protocol-type { all | http-get | http-post | ftp | smtp | pop3 | imap | smb-upload | smbdownload}
l
all | http-get | http-post | ftp | smtp | pop3 | imap| smb-upload | smb-download – 指定检
测的协议：all表示对HTTP协议的GET请求和POST请求、FTP协议、SMTP协议、POP3协议以及SMB协
议进行检测；http-get表示对HTTP协议的GET请求进行检测；http-post表示对HTTP协议的POST请求
进行检测；ftp表示对FTP协议进行检测；smtp表示对SMTP协议进行检测；pop3表示对POP3协议进行
检测；imap表示对IMAP协议进行检测;smb-upload表示对SMB协议的上传请求进行检测；smbdownload 表示对SMB协议的下载请求进行检测。
取消协议类型的指定，使用no protocol-type命令。
指定文件类型
当系统检测到传输的文件类型是指定的类型时，将触发控制动作。文件过滤功能支持对如下文件类型进行识
别：
7Z, AI, APK, ASF, AVI, BAT, BMP, CAB, CATPART, CDR, CIN, CLASS, CMD, CPL, DLL, DOC, DOCX,
DPX, DSN, DWF, DWG, DXF, EDIT, EMF, EPS, EPUB, EXE, EXR, FLA, FLV, GDS, GIF, GZ, HLP,
HTA, HTML, IFF, ISO, JAR, JPG, KEY, LNK, LZH, MA, MB, MDB, MDI, MIF, MKV, MOV, MP3, MP4,
MPEG, MPKG, MSI, NUMBERS, OCX, PAGES, PBM, PCL, PDF, PGP, PIF, PL, PNG, PPT, PPTX, PSD,
RAR, REG, RLA, RMVB, RPF, RTF, SGI, SH, SHK, STP, SVG, SWF, TAR, TDB, TIF, TORRENT, TXT,
VBE, WAV, WEBM, WMA, WMF, WMV, WRI, WSF, XLS, XLSX, XML, XPM, ZIP, BZIP2,UNKNOWN
指定文件类型，在过滤规则配置模式下，使用如下命令：
file-type type
l
type - 指定文件类型。每次可指定一个类型。类型名称如上所述。重复此命令指定多个文件类型。对系
统无法识别的文件进行控制，可指定UNKNOWN文件类型。
使用no file-type type命令取消文件类型的指定。
指定控制动作
对符合过滤规则的文件进行处理。指定控制动作，在过滤规则配置模式下，使用如下命令：
action { log | block }

<!-- 来源页 2427 -->
l
block – 使用block参数对符合过滤规则的文件进行阻断，阻断此次上传或下载。
l
log – 对符合过滤规则的文件放行并记录日志。
使用no action命令取消控制动作的指定。
添加/删除文件过滤Profile描述信息
在文件过滤Profile配置模式下，用户可以通过使用以下命令为文件过滤Profile添加描述信息。
description description
l
description – 指定文件过滤Profile的描述信息。范围是1到255字节。
在文件过滤Profile配置模式下，使用以下命令删除文件过滤Profile的描述信息。
no description
绑定文件过滤Profile到策略规则
将文件过滤Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据文件过滤Profile配置进行
处理。绑定文件过滤Profile到策略规则，需要在策略规则配置模式下进行。
进入策略规则配置模式需要进行两步配置。首先，在全局配置模式下，输入以下命令进入策略配置模式：
policy-global
然后，在策略配置模式下，输入以下命令进入策略规则配置模式：
rule [id id-number]
进入策略规则配置模式后，输入以下命令将URL过滤Profile绑定到策略规则
dlp-profile profile-name
l
profile-name - 指定所需要绑定的文件过滤Profile名称。
使用no dlp-profile命令取消文件过滤Profile的绑定。
显示文件过滤Profile信息
在任何模式下，输入以下命令显示文件过滤Profile信息：
show dlp-profile profile-name
l
profile-name – 显示指定文件过滤Profile的信息。
配置应用层压缩控制功能
配置应用层压缩控制功能后，系统会对传输的压缩文件进行解压，并能对超出最大压缩层数的文件以及加密
压缩文件按照指定的动作进行处理。支持解压缩的文件格式包括RAR、ZIP、TAR、GZIP、BZIP2以及7-

<!-- 来源页 2428 -->
ZIP。
注意:
l
应用层压缩控制功能对病毒过滤功能和数据安全功能均生效。关于病毒过滤功能的详细信息，
请参阅"配置病毒过滤" 在第2138页。
l
A2200、A1800、A1600、X9180不支持对7-ZIP类型的文件进行解压。
l
不支持对使用PPMD方式压缩的7-ZIP文件进行解压。
l
对于7-ZIP压缩文件，每次解压缩检测仅支持检测其中的10个文件，超过10个文件将不再进行
检测。如果检测的10个文件中包含压缩文件，会继续进行解压缩检测。
开启/关闭解压缩功能
系统会对传输的压缩文件进行解压。默认情况下，系统的解压缩功能是开启的。开启或者关闭解压缩功能，
在全局配置模式下，使用以下命令：
decompression {enable | disable}
l
enable | disable - 开启（enable）/关闭（disable）解压缩功能。
指定最大压缩层数
用户可以配置最大压缩层数，并且指定对超出该层数限制的压缩嵌套文件的处理动作。
decompression max-recursion number exceed-action {log-only | reset-conn}
l
number – 指定最大压缩层数。取值范围为1-100层，默认为1层。
l
log-only | reset-conn – 指定对超出限制的压缩文件的处理动作，可以是产生日志信息（log-only）
和断开连接（reset-conn）。默认动作为log-only。
使用以上命令no的形式恢复默认值：
no decompression max-recursion
注意:
l
对于包含docx、pptx，xlsx、jar、apk格式的压缩文件，当处理动作被指定为断开连接
（reset-conn）时，用户需要将压缩嵌套层数增加1层，以避免无法下载该压缩文件的问题。

<!-- 来源页 2429 -->
l
启用应用层压缩控制功能会增加设备的性能消耗，最大压缩层数越高消耗越大，进而导致数据
转发延时随之增大，请谨慎配置。
指定加密压缩文件控制动作
默认情况下，系统不对加密压缩文件特殊处理。如需要对加密压缩文件进行处理，可指定控制动作，在全局
配置模式下，使用如下命令：
decompression encryption-file action {log-only | reset-conn}
l
log-only | reset-conn – 指定对加密压缩文件的处理动作，可以是产生日志信息（log-only）和断开
连接（reset-conn）。
使用以上命令no的形式恢复到默认控制动作，不对加密压缩文件进行处理：
no decompression encryption-file action
显示应用层压缩控制配置信息
在任何模式下，输入以下命令显示应用层压缩控制配置信息：
show decompression configuration
开启/关闭7-ZIP解压调试功能
开启7-ZIP解压调试功能，在任意模式下，使用以下命令：
debug strmengine decoder 7z [basic | error]
l
debug strmengine decoder 7z - 输出7-ZIP解压缩的基本调试信息和错误调试信息。
l
basic - 输出7-ZIP解压缩的基本调试信息。
l
error - 输出7-ZIP解压缩的错误调试信息。
关闭7-ZIP解压调试功能，在任意模式下，使用以下命令：
undebug strmengine decoder 7z

<!-- 来源页 2430 -->
上网行为审计
上网行为审计功能可以对IM应用程序行为进行审计，并能对访问行为进行日志记录，包括：
l 对QQ、微信和微博的行为审计；
l 指定上网日志记录控制动作。
配置上网行为审计功能
上网行为审计功能的CLI配置主要通过策略规则/安全域与Profile相结合的方式实现。将上网行为审计
Profile绑定到策略规则/安全域后，系统将会对与策略规则/安全域相匹配的网络流量根据Profile配置进行
处理。
通过CLI配置上网行为审计功能，请按照以下步骤进行操作：
1. 定义上网行为审计Profile，在Profile中指定需要进行审计的IM应用程序、配置超时时间以及指定上网日志记录
控制动作。
2. 将网络聊天Profile绑定到适当的策略规则/安全域。
创建上网行为审计Profile
上网行为审计Profile中主要指定需要进行进行审计的IM应用程序、配置超时时间以及指定上网日志记录控
制动作。创建上网行为审计Profile，在全局配置模式下使用以下命令：
nbr-profile profile-name
l
profile-name - 指定所创建的上网行为审计Profile的名称，并且进入该上网行为审计Profile的配置模
式。如果指定名称已存在，则直接进入上网行为审计Profile配置模式。使用no nbr-profile profilename删除指定的上网行为审计Profile。
IM审计
IM审计即对指定的IM应用程序流量行为进行审计，识别微信流量中的UID（唯一标识）及对应的IP，
MAC，时间，并记录到日志中。开启IM审计功能，在上网行为审计Profile配置模式下，使用如下命令：
im {qq | wechat | sinaweibo} log enable
l
qq - 指定对QQ进行审计。
l
wechat - 指定对微信进行审计。
l
sinaweibo - 指定对新浪微博进行审计。

<!-- 来源页 2431 -->
在上网行为审计Profile配置模式下，执行no im {qq | wechat | sinaweibo} log enable命令取消IM审计
的配置。
注意: 配置IM审计功能，需要在安全域配置模式下，使用application-identify命令开启规则所绑
定安全域的应用识别功能。
配置超时时间
在超时时间内，相同IM用户的流量不会触发新的日志。超过超时时间后，IM用户的流量会触发新的日志。配
置超时时间，在上网行为审计Profile配置模式下，使用如下命令：
im {qq | wechat | sinaweibo} timeout value
l
qq | wechat | sinaweibo – 指定审计的IM用户类型。
l
value – 指定超时时间。单位为分钟，范围是5-20分钟。默认20分钟。
使用no im {qq | wechat | sinaweibo} timeout命令恢复默认时间。
指定上网日志记录控制动作
在上网行为审计Profile配置模式下，用户可以使用以下命令开启系统的上网日志记录功能：
web-surfing-record method [get | get-post [post-content] | post [post-content]]
l
get - 记录GET方式的上网日志信息。
l
get-post - 记录GET和POST方式的上网日志信息。
l
post - 记录POST方式的上网日志信息。
l
post-content – 记录POST内容。
在上网行为审计Profile配置模式下，使用该命令no的形式关闭上网日志记录功能：
no web-surfing-record
绑定上网行为审计Profile到策略规则
将上网行为审计Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据Profile配置进行处
理。绑定上网行为审计Profile到策略规则，需要在策略规则配置模式下进行。
进入策略规则配置模式需要进行两步配置。首先，在全局配置模式下，输入以下命令进入策略配置模式：
policy-global
然后，在策略配置模式下，输入以下命令进入策略规则配置模式：
rule [id id-number]

<!-- 来源页 2432 -->
进入策略规则配置模式后，输入以下命令将上网行为审计Profile绑定到策略规则
nbr profile-name
l
profile-name - 指定所需要绑定的上网行为审计Profile名称。
绑定配置完成后，需要修改策略规则的优先级，确保流量优先匹配此策略规则，然后可以继续指定策略规则
的用户、目的安全域和时间表参数，并能禁用或者启用该条策略规则。具体配置命令请参阅安全策略。
绑定上网行为审计Profile到安全域
将上网行为审计Profile绑定到安全域后，系统将会对以该安全域为目的安全域的流量按照Profile配置进行
处理。当策略规则已经绑定了上网行为审计Profile，同时策略规则的目的安全域也绑定了上网行为审计
Profile，策略规则绑定的上网行为审计Profile将会生效，而目的安全域绑定的上网行为审计Profile无效。
绑定上网行为审计Profile到安全域，在安全域配置模式下，使用以下命令：
nbr enable profile-name
l
profile-name – 指定绑定到安全域的上网行为审计Profile的名称。一个安全域只能绑定一个上网行为
审计Profile。
在安全域配置模式下，使用该命令no的形式取消上网行为审计Profile的绑定：
no nbr enable
显示上网行为审计Profile信息
在任何模式下，输入以下命令显示上网行为审计Profile信息：
show nbr-profile [profile-name]
l
profile-name – 显示指定上网行为审计Profile的信息。若不指定Profile名称，显示系统中所有上网行
为审计Profile的信息。

<!-- 来源页 2433 -->
日志管理
系统数据安全日志信息（文件过滤日志、内容过滤日志、上网行为审计日志）可以对用户的上网行为进行全
面记录，包括网页访问记录、外发邮件行为、内容及附件记录、论坛发帖记录、IM行为和聊天内容记录以及
FTP/HTTP使用记录等等，这些记录为HSM（Hillstone Security Management，山石网科安全管理平
台）的数据安全日志查询统计与审计分析提供完整的数据信息。关于数据安全日志查询统计与审计分析的详
细信息，请参阅《山石网科安全管理平台WebUI手册》。
日志信息级别及输出格式
按照日志信息的严重程度区分，数据安全日志属于信息（Information）级别。
为方便用户查阅和分析系统日志信息，系统按照固定的格式输出数据安全日志信息。该格式为：时间，级别
@模块：日志描述。请参阅以下示例：
2017-06-17 11:34:27, WEBPOST: IP 100.100.10.55 (-) vrouter trust-vr, url, content_type
content_type, action action, reason reason, rule rule, character set character-set, content
日志信息输出目的地
数据安全日志信息（文件过滤日志、内容过滤日志、上网行为审计日志）可以输出到下列3种目的地，用户
可以根据自己的需要指定：
l Console – Console端口终端。
l 缓存（Buffer）- 内存缓存。
l 日志服务器（Syslog Server）- 系统可以将日志信息发往UNIX或Windows Syslog Server。
配置日志功能
配置数据安全日志功能，包括开启/关闭日志功能、指定日志信息输出目的地、导出系统日志信息、清除系统
日志信息。数据安全功能配置，参见下表：
配置
CLI
开启和关闭日志功能
全局配置模式下使用以下命令：
l 开启：logging data-security [dlp | cf | nbr] on
l 关闭：no logging data-security[dlp | cf | nbr] on
指定记录上网行为审计日志信息
上网行为审计Profile配置模式下使用以下命令：
l 记录QQ、微信以及新浪微博上网行为审计日志信息：im {qq | wechat |
sinaweibo} log enable

<!-- 来源页 2434 -->
配置
CLI
l 关闭QQ、微信以及新浪微博上网行为审计日志信息记录功能：no im {qq |
wechat | sinaweibo} log enable
指定数据安全日志信息（文件过
滤日志、内容过滤日志、上网行
为审计日志）输出目的地
全局配置模式下使用以下命令：
l 输出到Console、Syslog服务器：logging data-security [dlp | cf | nbr]
to {console | syslog [binary-format [distributed [src-ip-hash | roundrobin]] | custom-format] }
l 输出到内存缓存：logging data-security [dlp | cf | nbr] to buffer [size
buffer-size]
显示数据安全日志信息
show logging data-security [dlp | cf | nbr]
清除数据安全日志信息
clear logging data-security [dlp | cf | nbr]

<!-- 来源页 2435 -->
数据安全配置举例
本节介绍5个数据安全配置举例，包括：
l 例：URL过滤
l 例：网页关键字
l 例：Web外发信息
l 例：邮件过滤
l 例：上网行为审计
数据安全配置组网
组网图如下图所示，某企业通过设备接入Internet，接口ethernet0/0属于untrust安全域，接入
Internet；ethernet0/1属于trust安全域，连接内网的研发部门；ethernet0/3属于trust1安全域，连接
内网的市场部门。
l
强烈建议用户使用单一方式配置数据安全功能，即不要CLI和WebUI混用配置。
l
实例中接口、安全域及日志输出等部分配置请参考相关章节，本节重点介绍数据安全相关配置。

<!-- 来源页 2436 -->
例：URL过滤配置举例
在设备上配置URL过滤规则，禁止公司研发部员工（IP网段为10.100.0.0/16）在上班时间（周一至周五，
每天09：00到18：00）访问新闻媒体类网站（网站www.abc.com除外）和某娱乐网站www.bcd.com，
并禁止搜索关键字“ef”，对试图访问及搜索的行为进行记录。
准备工作
进行下列实例配置前，请完成以下准备工作：
1. 安装URL许可证，然后重启设备。
2. 升级预定义URL库。
配置步骤
第一步：配置时间表:
hostname(config)# schedule workday
hostname(config-schedule)# periodic weekdays 09:00 to 18:00
hostname(config-schedule)# exit
hostname(config)#
第二步：自定义包含娱乐网站“www.bcd.com”的URL类别“bcd”:
hostname(config)# url-category bcd
hostname(config)# url www.bcd.com url-category bcd
第三步：配置关键字类别“url-keyword”：
hostname(config)# category url-keyword
hostname(config)# keyword ef simple category url-keyword
第四步：配置URL过滤Profile“urlcontrol”：
hostname(config)# url-profile urlcontrol
hostname(config-url-profile)# url-category News block log
hostname(config-url-profile)# keyword-category url-keyword block log
hostname(config-url-profile)# exit
hostname(config)#
第五步：绑定URL过滤Profile到策略规则：

<!-- 来源页 2437 -->
hostname(config)# policy-global
hostname(config-policy)# rule id 1
hostname(config-policy-rule)# url urlcontrol
hostname(config-policy-rule)# src-ip 10.100.0.0/16
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# schedule workday
hostname(config-policy-rule)# exit
hostname(config)#
第六步：进行Bypass域名设置，不对网站“www.abc.com”进行控制：
hostname(config)# address abc
hostname(config-addr)# host www.abc.com
hostname(config-addr)# exit
hostname(config)# policy-global
hostname(config-policy)# rule from any to abc service any permit
hostname(config-policy)# exit
hostname(config)#
配置完成后，请修改策略规则的优先级，确保流量优先匹配此策略规则。生效后，研发部员工在上班时间上
网时，将不能访问新闻媒体类网站（网站www.abc.com除外）和网站www.bcd.com，并且不能搜索关键
字“ef”。如有访问和搜索，行为将被阻断，并且系统会对该行为进行日志记录。
例：网页关键字配置举例
在设备上配置网页关键字规则，禁止公司研发部员工（员工“a”除外，研发部IP网段为10.100.0.0/16）
访问含“X”和“Y”两个词汇的网页，并对试图访问的行为进行记录。
准备工作
进行下列实例配置前，请完成以下准备工作：
1. 安装URL许可证，然后重启设备。
2. 升级预定义URL库。
配置步骤
第一步：自定义关键字类别“web-keyword”：

<!-- 来源页 2438 -->
hostname(config)# contentfilter
hostname(config-contentfilter)# category web-keyword
hostname(config-contentfilter)# keyword X simple category stock-keyword
hostname(config-contentfilter)# keyword Y simple category stock-keyword
hostname(config-contentfilter)# exit
hostname(config)#
第二步：配置网页关键字Profile“webkeyword-control”：
hostname(config)# contentfilter-profile webkeyword-control
hostname(config-contentfilter-profile)# keyword-category web-keyword block log
hostname(config-contentfilter-profile)# exit
hostname(config)#
第三步：绑定网页关键字Profile到策略规则：
hostname(config)# policy-global
hostname(config-policy)# rule id 2
hostname(config-policy-rule)# contentfilter webkeyword-control
hostname(config-policy-rule)# src-ip 10.100.0.0/16
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# exit
hostname(config)#
第四步：进行免监控用户设置，不对员工“a”进行控制：
hostname(config)# aaa-server local
hostname(config-aaa-server)# user a
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)# policy-global
hostname(config-policy)# rule from any to any from-zone trust to-zone untrust
service any permit

<!-- 来源页 2439 -->
Rule id 3 is created
hostname(config-policy)# rule id 3
hostname(config-policy-rule)# user local a
hostname(config-policy-rule)# exit
hostname(config)#
配置完成后，请修改策略规则的优先级，确保流量优先匹配此策略规则。生效后，研发部员工将不能访问含
有关键字“X”和“Y”的网页。如有访问，访问将被阻断，并且系统会对该访问行为进行日志记录。
例：Web外发信息配置举例
在设备上配置Web外发信息规则，对公司员工在网站www.abc.com发布包含“X”词汇信息的行为进行记
录。
准备工作
进行下列实例配置前，请完成以下准备工作：
1. 安装URL许可证，然后重启设备。
2. 升级预定义URL库。
配置步骤
第一步：自定义关键字类别“reactionary-keyword”：
hostname(config)# contentfilter
hostname(config-contentfilter)# category reactionary-keyword
hostname(config-contentfilter)# keyword X simple categoryreactionary-keyword
hostname(config-contentfilter)# exit
hostname(config)#
第二步：自定义包含门户网站“www.abc.com”的URL类别“abc”：
hostname(config)# url-category abc
hostname(config)# url www.abc.com url-category abc
第三步：配置Web外发信息Profile“webpost-control”：
hostname(config)# webpost-profile webpost-control
hostname(config-webpost-profile)# keyword-category reactionary-keyword log

<!-- 来源页 2440 -->
hostname(config-webpost-profile)# url-category abc
hostname(config-webpost-profile)# exit
hostname(config)#
第四步：绑定Web外发信息Profile到策略规则：
hostname(config)# policy-global
hostname(config-policy)# rule id 3
hostname(config-policy-rule)# webpost webpost-control
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# exit
hostname(config)#
配置完成后，请修改策略规则的优先级，确保流量优先匹配此策略规则。生效后，系统会对员工在网站
www.abc.com发布包含“X”词汇信息的行为进行日志记录。
例：邮件过滤配置举例
在设备上配置邮件过滤规则，阻止公司员工通过QQ邮箱发送邮件，并对通过其它邮箱发送邮件的行为进行日
志记录。
配置步骤
第一步：配置邮件过滤Profile“mailfilter”：
hostname(config)# mail-profile mailfilter
hostname(config-mail-profile)# mail sender *@qq.com block
hostname(config-mail-profile)# mail others log
hostname(config-mail-profile)# mail control all
hostname(config-mail-profile)# exit
hostname(config)#
第二步：绑定邮件过滤Profile到策略规则：
hostname(config)# policy-global
hostname(config-policy)# rule id 4
hostname(config-policy-rule)# mail mailfilter
hostname(config-policy-rule)# dst-zone untrust

<!-- 来源页 2441 -->
hostname(config-policy-rule)# exit
hostname(config)#
配置完成后，请修改策略规则的优先级，确保流量优先匹配此策略规则。生效后，系统会阻止员工通过QQ邮
箱发送邮件，并对通过其它邮箱发送邮件的行为进行日志记录。
例：上网行为审计配置举例
在设备上配置上网行为审计规则，对市场部员工（对应角色marketing）使用微信进行行为审计，即记录员
工的上网行为审计日志。
配置步骤
第一步：配置用户、角色以及角色映射规则（以该部门员工user1为例）：
hostname(config)# aaa-server local
hostname(config-aaa-server)# user-group usergroup1
hostname(config-user-group)# exit
hostname(config-aaa-server)# user user1
hostname(config-user)# password 123456
hostname(config-user)# group usergroup1
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)# role marketing
hostname(config)# role-mapping-rule role-mapping1
hostname(config-role-mapping)# match user-group usergroup1 role marketing
hostname(config-role-mapping)# exit
hostname(config)#
第二步：配置本地认证服务器的角色映射规则：
hostname(config)# aaa-server local
hostname(config-aaa-server)# role-mapping-rule role-mapping1
hostname(config-aaa-server)# exit
hostname(config)#
第三步：配置接口与安全域：

<!-- 来源页 2442 -->
hostname(config)# internet ethernet0/3
hostname(config-if-eth0/3)# zone trust1
hostname(config-if-eth0/3)# ip address 192.168.1.1/16
hostname(config-if-eth0/3)# exit
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone untrust
hostname(config-if-eth0/0)# ip address 66.1.200.1/16
hostname(config-if-eth0/0)# exit
hostname(config)#
第四步：通过策略规则触发Web认证功能并配置DNS策略：
hostname(config)# webauth
hostname(config-webauth)# enable
hostname(config-webauth)# protocal http
hostname(config-webauth)# exit
hostname(config)# policy-global
hostname(config-policy)# rule from any to any service any webauth local
Rule id 1 is created
hostname(config-policy)# rule id 1
hostname(config-policy-rule)# src-ip 192.168.1.1/16
hostname(config-policy-rule)# src-zone trust1
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# role unknown
hostname(config-policy-rule)# exit
hostname(config-policy)# rule from any to any service dns permit
Rule id 2 is created
hostname(config-policy)# rule id 2
hostname(config-policy-rule)# src-zone trust1
hostname(config-policy-rule)# dst-zone untrust

<!-- 来源页 2443 -->
hostname(config-policy-rule)# exit
hostname(config)#
第五步：配置允许访问网络的策略规则：
hostname(config-policy)# rule from any to any service any permit
Rule id 3 is created
hostname(config-policy)# rule id 3
hostname(config-policy-rule)# src-zone trust1
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# role marketing
hostname(config-policy-rule)# exit
hostname(config)#
第六步：配置上网行为审计Profile“marketim”：
hostname(config)# nbr-profile marketim
hostname(config-nbr-profile)# im wechat log enable
hostname(config-nbr-profile)# exit
hostname(config)#
第七步：绑定上网行为审计Profile“marketim”到策略规则：
hostname(config)# policy-global
hostname(config-policy)# rule id 4
hostname(config-policy-rule)# im marketim
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# role marketing
hostname(config-policy-rule)# exit
hostname(config)#
配置完成后，请修改策略规则的优先级，确保流量优先匹配此策略规则。生效后，系统会对市场部员工微信
进行日志记录。

<!-- 来源页 2444 -->
对象配置
对象是指用户在配置内容过滤规则和URL过滤规则时，需要引用的一些配置项。包括：
对象
说明
预定义URL库
包含数十个类别，多达上千万条URL，用于“网页关键字/Web外发信息”中URL类别及控
制范围的指定。
自定义URL库
自定义的URL库。用于“网页关键字/Web外发信息”中URL类别及控制范围的指定。
URL查询
通过URL查询功能查看特定URL的具体信息，包括该URL所属的URL类别以及所属URL库的
类型。
关键字类别
用户可以根据需要使用预定义关键字类别或者自定义关键字类别。用于“文件内容过滤/网
页关键字/Web外发信息/邮件过滤/应用行为控制”中关键字的指定。
页面提示
用户可以根据需要启用或禁用告警页面提示功能。
l 用户被阻断警告：当用户的上网行为被阻断时，在用户的Web浏览器中显示访问被拒绝
的警告信息提示页面。
l 用户被监控警告：当用户的上网行为被监控时，在用户的Web浏览器中显示行为被监控
的警告信息提示页面。
Bypass域名
设置不受上网行为控制规则控制的特殊域名。
免监控用户
设置不受上网行为控制规则控制的特殊用户。
未分类URL首次访问
指定首次访问的未分类URL查询等待时间并启用等待超时阻断动作，超过查询等待时间后，
系统将会对该未分类URL的访问进行阻断。用于URL过滤功能。
预定义URL库
系统内置预定义URL库。使用预定义URL库，需安装URL许可证后。
注意: 预定义URL库受许可证控制，安装许可证后，预定义URL库才可使用。
预定义URL库能够为网页关键字过滤功能和Web外发信息控制功能提供URL类别。预定义URL库中的URL按
照中国的文化背景、伦理道德、法律法规、应用领域、上网习惯等进行分类。目前，系统预定义URL库共提
供数十个类别，包含多达上千万条的URL。
对于URL类别的匹配顺序，优先匹配自定义URL库，其次匹配预定义URL库。
预定义URL库更新
默认情况下，系统会每日自动更新预定义URL库，用户可以根据需要更改数据库更新配置。Hillstone山石网
科提供两个默认数据库更新服务器，分别是update1.hillstonenet.com和update2.hillstonenet.com。

<!-- 来源页 2445 -->
StoneOS支持在线更新和本地更新两种方式供用户进行选择。预定义URL库更新配置，请参阅下表：
配置
CLI
配置更新模式，默认为自动更
新
全局配置模式下使用以下命令：
url-db update mode {auto | manual}
配置更新传输协议，默认为
HTTPS
在全局配置模式下，使用以下命令：
url-ub update protocol HTTP
在全局配置模式下使用该命令no的形式恢复默认HTTPS模式：
no url-ub update protocol HTTP
配置更新服务器
全局配置模式下使用以下命令：
url-db update {server1 | server2 | server3} {ip-address |
domain-name} [vrouter vrouter-name] [src-interface srcinterface-name]
指定自动更新时间
全局配置配置模式下使用以下命令：
url-db update schedule {daily | weekly {mon | tue | wed | thu |
fri | sat | sun} | monthly date} [HH:MM]
立即更新
执行模式下使用以下命令：
exec url-db update
本地更新
执行模式下使用以下命令：
import url-db from {ftp server ip-address [vrouter vroutername] [user user-name password password] | tftp server ipaddress | usb0 | usb1} file-name
说明：非根VSYS不支持此命令。
显示URL库信息
show url-db info
显示URL库更新配置信息
show url-db update
查看URL访问统计信息
show statistics-set name [{current | history | history-max}
[sort-by {up | down | item}] ]
手动刷新本地缓存URL信息
exec url-db refresh {all | url url-string}
l
all- 刷新本地缓存中的所有URL信息。
l
url url-string- 刷新本地缓存中的指定URL。
查看URL统计计数信息
show url-db statistics
清除URL统计计数信息
clear url-db statistics

<!-- 来源页 2446 -->
指定HTTP代理服务器
当设备需要通过HTTP代理服务器访问互联网时，为确保特征库能够正常升级，需要在设备上指定代理服务器
的IP地址和端口号。
为预定义URL特征库升级指定代理服务器，在全局配置模式下，使用如下命令：
url-db update proxy-server {main | backup} ip-address port-number
l
main | backup – 使用main参数指定主代理服务器，使用backup指定备份代理服务器。
l
ip-address port-number – 指定代理服务器的IP地址和端口号。
取消指定的代理服务器，使用no url-db update proxy-server {main | backup}命令。
自定义URL库
用户可以根据需要自定义URL类别。与预定义URL类别相同，自定义URL库能够为URL过滤功能提供URL类
别。对于URL类别的匹配顺序，优先匹配自定义URL库，其次匹配预定义URL库。
系统提供3个预定义的URL类别，分别是custom1，custom2，custom3；用户可将自定义的URL列表导入
其中。
注意: 非根VSYS不支持将自定义的URL列表导入3个预定义的URL类别。
配置自定义URL库
自定义URL类别，请参阅下表：
配置
CLI
创建URL类别
创建URL类别，全局配置模式下使用以下命令：
url-category category-name
删除URL类别，在全局配置模式下使用以下命令：
no url-category category-name
添加URL条目
同一条URL可以被添加到多个不同的URL类别中。支持配置的URL格式如
下：
l
域名：www.example.com；带通配符的域名：*.example.com
l
IPv4地址：192.168.1.1；带通配符的IPv4地址：192.168.1.*
l
IPv6地址：2001:db8::1
l
URL路径：www.example.com/path/index.html
将URL添加进URL类别，全局配置模式下，使用以下命令：
url url url-category category-name

<!-- 来源页 2447 -->
配置
CLI
将URL从URL类别中删除，在全局配置模式下，使用以下命令：
no url url url-category category-name
注意：
l
URL路径不支持配置通配符，且不支持携带资源查询参数。例
如：www.test.com/test1?test2=xxx
l
若URL路径中需配置IPv6地址，则IPv6地址需要用“[]”括起来。例
如：[2001:db8::1]/test
l
当自定义URL类别被SSL代理功能引用时，该类别中URL路径格式的条
目将对SSL代理功能不生效。
启用/禁用自定义URL库支持
HTTPS协议域名功能
启用，在全局配置模式下，使用以下命令：
url-db-https-enable
禁用，在全局配置模式下，使用以下命令：
no url-db-https-enable
显示自定义URL库支持HTTPS
协议域名的功能启用状态
显示自定义URL库支持HTTPS协议域名的功能启用状态，在任意模式下，
使用以下命令：
show url-db-https
导入自定义的URL列表
导入自定义的URL列表，在执行模式下，使用以下命令：
import url-file {custom1 | custom2 | custom3} from {ftp | ftps |
sftp} server IP [vrouter vrouter-name] [user username
password password] file-name
import url-file {custom1 | custom2 | custom3} from tftp server
IP [vrouter vrouter-name] file-name
注意：导入文件路径为/flash/urldb/url_file。URL文件大小应不超过
1M，且最多仅支持1000条URL。文件中支持使用通配符，但仅支持一个
通配符且必须在URL的起始位置。非根VSYS不支持导入自定义的URL列
表。
清除URL列表
清除URL列表，在任意模式下，使用以下命令：
exec url-file {custom1 | custom2 | custom3} clear
显示URL类别
显示URL类别，在任意模式下，使用以下命令：
show url-category
显示所有自定义URL信息
显示所有自定义URL信息，在任意模式下，使用以下命令：
show url

<!-- 来源页 2448 -->
URL查询
用户可以通过URL查询功能查看特定URL的具体信息，包括该URL所属的URL类别以及所属URL库的类型。
查看URL信息，请参阅下表：
配置
CLI
查询URL信息
show url url-string
URL查询服务器配置
URL查询服务器可以将网站访问过程中出现的未分类URL地址（预定义及自定义URL库中不包含的URL地
址）进行分类，并在以后的URL数据库升级中更新到数据库。Hillstone山石网科提供两个默认URL查询服务
器，分别是url1.hillstonenet.com和url2.hillstonenet.com。默认情况下，URL查询服务器处于启用状
态。配置查询服务器，请参阅下表：
配置
CLI
启用/关闭URL查询服务器
启用，在全局配置模式下使用以下命令：
url-db-query {server1 | server2} enable
关闭，在全局配置模式下使用以下命令：
no url-db-query {server1 | server2} enable
配置URL查询服务器
全局配置模式下使用以下命令：
url-db-query {server1 | server2} {ip-address | domain-name}
[vrouter vrouter-name] [port port] [encrypt-type BCAP]
显示URL查询服务器信息
show url-db-query [server1 | server2]
关键字类别
关键字类别包括预定义关键字类别和自定义关键字类别，用于“URL过滤/文件内容过滤/网页关键字/Web
外发信息/邮件过滤/应用行为控制”中关键字的指定。用户可以根据需要使用预定义关键字类别或者自定义
关键字类别。系统默认提供四种预定义关键字类别，分别是predef_bank_card（银行卡号关键字）、
predef_email_address（邮箱账号关键字）、predef_cellphone_number（手机号关键字）和
predef_mainland_id_card（身份证号关键字），不可被编辑和删除。
关键字匹配规则
配置关键字相关的上网行为控制规则后，系统会按照关键字对流量进行扫描，并将扫描到的关键字按照关键
字类别进行信任值的统计计算，计算方法为：将扫描到的所有属于该类别的关键字按照“次数* 关键字信任
值”进行累加计算，然后用此计算值与关键字类别的警戒值进行比较（关键字类别的警戒值为100）。根据
比较结果进行如下处理：

<!-- 来源页 2449 -->
l 如果计算值大于或者等于该类别的警戒值，则触发该类别所对应的控制动作；
l 如果多个关键字类别的计算值大于或者等于警戒值，且对应控制动作有阻止的，则按照阻止进行处理；
l 如果多个关键字类别的计算值大于或者等于警戒值，且对应控制动作都为允许，则按照允许进行处理。
例如：某网页关键字规则配有两个关键字类别C1和C2，C1对应控制动作为阻止，C2对应控制动作为允许。
类别C1中包含两个关键字K1和K2，K1的信任值为20，K2的信任值为40。类别C2中包含两个关键字K1和
K2，K1的信任值为30，K2的信任值为80。
假设扫描某网页，发现K1和K2各出现一次。对C1信任值计算：20*1+40*1=60<100；对C2信任值计
算：30*1+80*1=110>100。所以触发C2对应的控制动作，即允许访问该网页。
假设扫描某网页，发现K1出现三次，K2出现一次。对C1信任值计算：20*3+40*1=100；对C2信任值计
算：30*3+80*1=170>100。C1和C2都满足触发条件，所以触发C1对应的阻止控制动作，即禁止访问该网
页。
建议通过关键字组合的方式实现关键字相关的上网行为控制功能。例如，配置网页关键字功能阻止用户访问
网游相关网站，如果只指定过滤关键字“网游”，则可能阻止很多无关网站；但如果指定过滤关键字“网
游”、“经验值”、“装备”和“外挂”，并恰当设置每个关键字的信任值，这样就能大大提高控制的准确
性。更为高级的使用方式是将网游相关的术语都收集起来，按照可能性给每个关键字分配信任值，这样可以
较为全面和准确的达到控制目的。
自定义关键字类别
自定义关键字类别，请参阅下表：
配置
CLI
创建关键字类别
全局配置模式下使用以下命令：
category category-name
添加关键字条目
全局配置模式下使用以下命令：
keyword keyword {regexp | simple} category category-name
[confidence value]
当系统所定义的关键字增加、
减少或者改变时，更新关键字
应用
执行模式下使用以下命令：
exec contentfilter apply
显示关键字类别
任何模式下使用以下命令：
show category category-name
显示关键字条目
任何模式下使用以下命令：
keyword keyword {regexp | simple} category category-name

<!-- 来源页 2450 -->
配置
CLI
[confidence value]
页面提示
页面提示功能指通过告警页面提示用户被阻断警告信息或提示用户被监控警告信息，用户可以根据需要启用
或禁用告警页面提示功能。
告警页面包括预定义告警页面和自定义告警页面。
l 预定义告警页面：显示系统预定义的警告信息内容，包括提示信息以及警告原因。
l 自定义告警页面：用户可以通过自定义警告信息和插入自定义图片，来自定义符合自己实际需求的告警页面。
用户被阻断警告
开启用户被阻断警告功能后，如果用户上网流量匹配病毒过滤、URL过滤、内容过滤、应用策略控制等阻断
类型安全策略时，防火墙会立即中断该访问连接，并根据不同管控类型，向客户端Web浏览器推送对应类型
的阻断提示页面，告知用户访问被拦截的原因。系统为以下5类阻断场景预置了默认提示页面（预定义告警
页面）：
l
URL过滤阻断用户通知：当流量命中URL过滤规则时（如URL黑名单、URL分类等），系统会拦截访问并
推送预定义的URL过滤阻断告警页面。页面默认提示内容如下图所示。
l
病毒过滤发现恶意软件：当病毒过滤功能扫描出携带恶意软件的访问流量时，系统会拦截访问并推送预
定义的病毒过滤发现恶意软件告警页面。页面默认提示内容如下图所示。

<!-- 来源页 2451 -->
l
病毒过滤发现恶意站点：当病毒过滤功能扫描出访问恶意站点的流量时，系统会拦截访问并推送预定义
的病毒过滤发现恶意站点告警页面。页面默认提示内容如下图所示。
l
内容过滤阻断用户通知：当流量命中网页关键字、Web外发信息、邮件等内容过滤规则时，系统会拦截
访问并推送预定义的内容过滤阻断告警页面。页面默认提示内容如下图所示。
l
应用阻断用户通知：当流量命中应用策略控制规则时，系统会拦截访问并推送预定义的应用阻断告警页
面。页面默认提示内容如下图所示。
用户被监控警告
开启用户被监控警告功能后，如果用户的上网行为与系统中已配置的上网行为控制功能（网页关键字过滤、
Web外发信息控制、邮件过滤和应用行为控制）相匹配，则该用户的HTTP网页访问请求会被重定向到用户

<!-- 来源页 2452 -->
被监控警告提示页面，提示其上网行为将受到监控，注意保护个人隐私并遵守相关法律法规。例如，如果创
建网页关键字规则对用户浏览某网页的行为进行监控，并且用户被监控警告提示功能是启用的，当用户浏览
该网页时，用户PC的Web浏览器将显示用户被监控警告提示页面。预定义告警页面如下图所示：
配置页面提示
配置用户被阻断警告
配置用户被阻断警告功能，请参阅下表：
配置
CLI
开启/关闭URL过滤阻断用户通
知功能
该功能默认开启。
开启，在全局配置模式下使用以下命令：
url-block-notification
关闭，在全局配置模式下使用以下命令：
no url-block-notification
说明：如果已配置并启用自定义告警页面，显示自定义告警页面。如果
未启用自定义告警页面，显示默认预定义告警页面。
开启/关闭内容过滤阻断用户
通知功能
该功能默认开启。
开启，在全局配置模式下使用以下命令：
contentfilter-block-notification
关闭，在全局配置模式下使用以下命令：
no contentfilter-block-notification
说明：如果已配置并启用自定义告警页面，显示自定义告警页面。如果未
启用自定义告警页面，显示默认预定义告警页面。
开启/关闭病毒过滤发现恶意
软件用户通知功能
该功能默认开启。详细配置请参阅配置病毒过滤的“指定协议类型”章
节。
开启/关闭病毒过滤发现恶意
站点用户通知功能
该功能默认开启。详细配置请参阅配置病毒过滤的“防恶意网站功能”章
节。
开启/关闭应用阻断用户通知
功能
该功能默认关闭。
开启，在全局配置模式下使用以下命令：
app block-notification enable

<!-- 来源页 2453 -->
配置
CLI
关闭，在全局配置模式下使用以下命令：
app block-notification disable
说明：如果已配置并启用自定义告警页面，显示自定义告警页面。如果未
启用自定义告警页面，显示默认预定义告警页面。
注意:
l
该功能依赖应用特征库，使用前请确保应用特征库已升级至
260529或更高版本。如需更新应用特征库，可参阅“防火
墙> 服务和应用> 应用> 更新应用特征库”章节。
l
使用该功能前，建议先在安全域中启用应用识别功能，以免
因应用识别失败导致系统无法阻断应用。
l
仅当HTTP流量或解密后的HTTPS流量被策略拒绝时，系统
才会向用户浏览器返回应用阻断告警页面进行提示。如需对
HTTPS流量开启该通知，请在使用前配置SSL代理功能。
查看应用阻断用户通知功能的
启用状态
show app block-notification status
返回示例：
hostname# show app block-notification status
Application block-notification status: Disable
查看URL过滤阻断和内容过滤
阻断用户通知功能的启用状态
show block-notification
返回示例：
hostname# show block-notification
URL block notification: enable（URL过滤阻断用户通知功能：开
启）
Contentfilter block notification: disable（内容过滤阻断用户通知功
能：关闭）
配置用户被监控警告
默认情况下，用户被监控警告功能是关闭的。配置用户被监控警告功能，请参阅下表：
配置
CLI
开启/关闭URL过滤用户被监控
警告功能
开启，在全局配置模式下使用以下命令：
url-user-notification
关闭，在全局配置模式下使用以下命令：
no url-user-notification
说明：如果已配置并启用自定义告警页面，显示自定义告警页面。如果
未启用自定义告警页面，显示默认预定义告警页面。

<!-- 来源页 2454 -->
配置
CLI
开启/关闭内容过滤用户被监
控警告功能
开启，在全局配置模式下使用以下命令：
contentfilter-user-notification
关闭，在全局配置模式下使用以下命令：
no contentfilter-user-notification
说明：如果已配置并启用自定义告警页面，显示自定义告警页面。如果
未启用自定义告警页面，显示默认预定义告警页面。
如果开启用户被监控警告功能，对于同一个源IP，若用户的网络行为与系统中已配置的数据安全规则相匹
配，则用户在浏览网页时会每隔24小时收到一次警告提示。
配置自定义告警页面
用户可以通过自定义警告信息和图片，来自定义符合自己实际需求告警页面。自定义告警页面包含以下配
置：
l 进入告警页面配置模式
l 开启自定义告警页面功能
l 创建图片对象
l 上传自定义图片
l 上传自定义告警页面
l 查看自定义告警页面信息
l 查看自定义图片信息
l 清除自定义告警页面内容
进入告警页面配置模式
进入告警页面配置模式，在全局配置模式下使用以下命令：
warning-page
开启自定义告警页面功能
系统支持以下7种类型的自定义告警页面。
l
URL过滤监控用户通知：通知URL过滤功能将扫描用户流量。
l
URL过滤阻断用户通知：通知用户流量被URL过滤阻断。
l
病毒过滤发现恶意软件：病毒过滤扫描网络流量，发现恶意软件后显示告警页面。
l
病毒过滤发现恶意站点：病毒过滤扫描网络流量，发现恶意软件后显示告警页面。

<!-- 来源页 2455 -->
l
内容过滤监控用户通知：通知内容过滤功能将扫描用户流量。
l
内容过滤阻断用户通知：通知用户流量被内容过滤阻断。
l
应用阻断用户通知：通知用户流量被应用策略阻断。
提示:
l
自定义告警页面大小不得超过10KB。
l
自定义告警页面的中英文HTML文件相互独立，修改中文内容不会同步到英文文件。设备会根
据自身系统语言，自动推送对应语种的通知页面（例如：系统语言为中文时推送中文页面，为
英文时推送英文页面）。
请根据设备当前语言，在告警页面配置模式下，选择对应的命令，开启指定类型的自定义告警页面：
系统语言为英文时执行以下命令：
{av-malicious-website | av-malware | contentfilter-audit-notification | contentfilter-block |
url-audit-notification | url-block | application-block} customized
系统语言为中文时执行以下命令：
{av-malicious-website-cn | av-malware-cn | contentfilter-audit-notification-cn |
contentfilter-block-cn | url-audit-notification-cn | url-block-cn | application-block-cn}
customized
l
av-malicious-website - 开启“病毒过滤发现恶意站点”的自定义告警页面。
l
av-malware- 开启“病毒过滤发现恶意软件”的自定义告警页面。
l
contentfilter-audit-notification - 开启“内容过滤监控用户通知”的自定义告警页面。
l
contentfilter-block- 开启“内容过滤阻断用户通知”的自定义告警页面。
l
url-audit-notification - 开启“URL过滤监控用户通知”的自定义告警页面。
l
url-block - 开启“URL过滤阻断用户通知”的自定义告警页面。
l
application-block - 开启“应用阻断用户通知”的自定义告警页面。
请根据设备当前语言，在告警页面配置模式下，选择对应的no命令关闭指定类型的自定义告警页面功能：
系统语言为英文时执行以下命令：
no {av-malicious-website | av-malware | contentfilter-audit-notification | contentfilter block
| url-audit-notification | url-block | application-block} customized
系统语言为中文时执行以下命令：

<!-- 来源页 2456 -->
no {av-malicious-website-cn | av-malware-cn | contentfilter-audit-notification-cn |
contentfilter-block-cn | url-audit-notification-cn | url-block-cn | application-block-cn}
customized
创建图片对象
创建图片对象，在告警页面配置模式下，使用以下命令：
image image-name
l
image-name- 指定图片对象的名称。范围是1到31个字符。
在告警页面配置模式下使用该命令no的形式删除图片对象：
no image image-name
上传自定义图片
上传自定义图片并绑定到已创建的图片对象，在执行模式下，使用以下命令：
import warning-page image image-name from {{ftp | ftps | sftp} server ip-address [vrouter
vrouter-name] [user user-name password password] | tftp server ip-address [vrouter
vrouter-name]} file-name
l
image-name - 指定需要绑定的图片对象的名称。
l
ip-address – 指定FTP、FTPS、SFTP或者TFTP服务器的IP地址。
l
user user-name password password – 指定FTP、FTPS或者SFTP服务器的用户名和密码。
l
vrouter vrouter-name - 指定FTP、FTPS、SFTP或者TFTP服务器所属的VRouter。
l
file-name – 指定需要上传的自定义图片文件的名称。
自定义图片上传完毕后，用户可以通过WebUI方式查看已上传的图片，选择“系统> 告警页面管理> 图片
管理”进行查看。
上传自定义告警页面
用户在本地将自定义告警页面编辑完成之后，通过上传该页面到指定的FTP、FTPS、SFTP或者TFTP服务器
使其生效。
在执行模式下，使用以下命令，上传本地已编辑完成的中英文自定义告警页面：
上传英文自定义告警页面
import warning-page html {av-malicious-website | av-malware | contentfilter-auditnotification | contentfilter-block | url-audit-notification | url-block | application-block} from

<!-- 来源页 2457 -->
{{ftp | ftps | sftp} server ip-address [vrouter vrouter-name] [user user-name password
password] | tftp server ip-address [vrouter vrouter-name]} file-name
上传中文自定义告警页面
import warning-page html {av-malicious-website-cn | av-malware-cn | contentfilter-auditnotification-cn | contentfilter-block-cn | url-audit-notification-cn | url-block-cn |
application-block-cn} from {{ftp | ftps | sftp} server ip-address [vrouter vrouter-name] [user
user-name password password] | tftp server ip-address [vrouter vrouter-name]} file-name
l
av-malicious-website | av-malware | contentfilter-audit-notification | contentfilter-block
| url-audit-notification | url-block | application-block - 指定上传的自定义告警页面类型。
l
ip-address – 指定FTP、FTPS、SFTP或者TFTP服务器的IP地址。
l
user user-name password password – 指定FTP、FTPS或者SFTP服务器的用户名和密码。
l
vrouter vrouter-name - 指定FTP、FTPS、SFTP或者TFTP服务器所属的VRouter。
l
file-name – 指定需要上传的自定义告警页面文件的名称。
自定义告警页面上传完毕后，用户可以通过WebUI方式查看已上传的页面，选择“系统> 告警页面管理>
页面管理”查看对应类别的预览页面。
查看自定义告警页面信息
用户可以在任何模式下使用以下命令，查看中英文界面的自定义告警页面启用状态、大小等信息：
l
查看英文界面的自定义告警页面信息：show warning-page html [av-malicious-website | avmalware | contentfilter-audit-notification | contentfilter-block | url-audit-notification |
url-block | application-block]
l
查看中文界面的自定义告警页面信息：show warning-page html [av-malicious-website-cn |
av-malware-cn | contentfilter-audit-notification-cn | contentfilter-block-cn | url-auditnotification-cn | url-block-cn | application-block-cn]
查看自定义图片信息
用户可以在任何模式下使用以下命令查看自定义图片信息，包括图片类型、图片大小等：
show warning-page image [image-name]

<!-- 来源页 2458 -->
清除自定义告警页面内容
各类型的自定义告警页面包含默认显示的警告信息内容，用户可以清除页面的自定义内容并恢复默认，在执
行模式下，使用以下命令：
exec warning-page {image image-name | html {av-malicious-website | av-malware |
contentfilter-audit-notification | contentfilter-block | url-audit-notification | url-block |
application-block | av-malicious-website-cn | av-malware-cn | contentfilter-auditnotification-cn | contentfilter-block-cn | url-audit-notification-cn | url-block-cn |
application-block-cn}} clear
l
image image-name - 指定清除的图片对象名称。
l
html {av-malicious-website | av-malware | contentfilter-audit-notification |
contentfilter-block | url-audit-notification | url-block | application-block | av-maliciouswebsite-cn | av-malware-cn | contentfilter-audit-notification-cn | contentfilter-block-cn |
url-audit-notification-cn | url-block-cn | application-block-cn} - 指定需要清除自定义内容的
告警页面类型。
提示:
l
当系统语言为中文时，需指定带-cn后缀的类型。例如：contentfilter-block-cn。
l
当系统语言为英文时，需指定不带-cn后缀的类型。例如：contentfilter-block。
清除完成后，告警提示页面将会恢复到自定义告警页面默认内容。用户可以通过WebUI方式查看自定义告警
页面的默认内容，选择“系统> 告警页面管理> 页面管理”查看对应类别的预览页面。
未分类URL首次访问
对于用户首次访问的未分类URL，即该URL并未包含在系统的预定义URL库或自定义URL库中，系统将会在
云端继续查询该URL的类别，由于查询结果返回可能会出现时延，在查询结果返回之前，对于该未分类的
URL系统不能及时执行类别相对应的处理动作。
为解决上述问题，针对首次访问的未分类URL，用户可以指定其查询等待时间并启用等待超时阻断动作，超
过查询等待时间后，系统将会对该未分类URL的访问进行阻断。
配置未分类URL首次访问
指定查询等待时间
指定查询等待时间，在全局配置模式下，使用以下命令：

<!-- 来源页 2459 -->
url-match-pending hold-time time
l
time - 指定查询结果等待时间，范围是0到5000毫秒，默认值是0毫秒。
使用no url-match-pending hold-time time命令恢复查询等待时间默认值0毫秒，表示没有等待时间限
制。
启用/禁用等待超时阻断动作
启用等待超时阻断动作，在全局配置模式下，使用以下命令：
url-match-pending timeout-action block
使用no url-match-pending timeout-action block命令禁用等待超时阻断动作，在超过查询等待时间
后，将会继续按照URL过滤Profile配置进行URL过滤。
显示未分类URL首次访问配置信息
用户可以在任何模式下使用以下命令查看未分类URL的首次访问的配置信息以及被阻断的次数：
show url-match-pending

<!-- 来源页 2460 -->
URL过滤
URL过滤功能可以控制用户对某些网站的访问，并能对访问行为进行日志记录。URL过滤支持配置IPv4和
IPv6地址的URL和关键字（keyword）。
通过配置URL过滤功能，可以实现：
l 控制用户对某类网站的访问。比如，阻止用户访问赌博、色情类网站。
l 控制用户对某个网站的访问。比如，对用户访问某网站的行为进行日志记录。
l 分时段控制用户对某类网站的访问。比如，阻止用户在上班时间访问在线聊天类网站，下班后则允许访问。
l 控制用户对网址中含有特定关键字的网站的访问。比如，阻止用户访问网址中含有关键字“游戏”的网站。
配置URL过滤功能
系统支持基于安全域和基于策略的URL过滤配置方式。URL过滤支持配置IPv4和IPv6地址的URL和关键字
（keyword）。
通过CLI配置URL过滤功能，请按照以下步骤进行操作：
1. 定义URL过滤Profile，在Profile中指定需要进行控制的URL类别、URL关键字类别以及采取的控制动作。
2. 将URL过滤Profile绑定到安全域/策略规则。
创建URL过滤Profile
URL过滤Profile中主要指定URL过滤功能的控制类型及相应的控制动作。控制类型包括URL类别、URL单条
配置及URL关键字。控制动作包括阻断访问以及记录日志。URL类别指定需要进行控制的URL类别以及相应
的控制动作；URL单条配置指定需要进行控制的URL以及相应的控制动作；URL关键字指定需要进行控制的
URL关键字类别以及相应的控制动作；上网日志记录记录用户的GET，POST请求，以及POST请求的内容。
每一个URL过滤Profile只可以配置一种控制类型。系统有一个缺省的URL过滤Profile，名称为no-url，不
可编辑和删除，该Profile不对任何URL进行过滤。创建URL过滤Profile，在全局配置模式下使用以下命
令：
url-profile profile-name
l
profile-name - 指定所创建的URL过滤Profile的名称，并且进入该URL过滤Profile的配置模式。如果
指定名称已存在，则直接进入URL过滤Profile配置模式。不同的VSYS中可以配置相同名称的URL过滤
Profile。使用no url-profile profile-name删除指定的URL过滤Profile。
指定URL类别及控制动作
指定需要进行控制的URL类别及控制动作，在URL过滤Profile配置模式下使用以下命令：

<!-- 来源页 2461 -->
url-category {all | url-category-name} [block] [log]
l
all | url-category-name – 指定需要进行控制的URL类别名称，可以为所有的URL类别（all）或者特
定URL类别（url-category-name）。系统不支持指定非本VSYS中自定义的URL类别名称。
l
block – 指定阻止访问相应的URL类别。
l
log – 指定对用户的URL访问行为进行日志记录。
使用多条该命令可指定多个URL类别及相应的控制动作。
在URL过滤Profile配置模式下，使用no url-category {all | url-category-name}命令取消URL类别及控
制动作的指定。
指定URL单条配置及控制动作
指定需要进行控制的URL及控制动作，在URL过滤Profile配置模式下使用以下命令：
url url-name [block] [log]
l
url-name – 指定需要进行控制的URL，长度取值范围为1-255个字符。支持配置的URL格式如下：
l
域名：www.example.com；带通配符的域名：*.example.com
l
IPv4地址：192.168.1.1；带通配符的IPv4地址：192.168.1.*
l
IPv6地址：2001:db8::1
l
URL路径：www.example.com/path/index.html
l
block – 指定阻止访问相应的URL。
l
log – 指定对用户的URL访问行为进行日志记录。
使用多条该命令可指定多个URL及相应的控制动作。每个URL过滤Profile中最多指定64条URL。
在URL过滤Profile配置模式下，使用no url url-name命令取消URL及控制动作的指定。
注意:
l
URL路径不支持配置通配符，且不支持携带资源查询参数。例
如：www.test.com/test1?test2=xxx
l
若URL路径中需配置IPv6地址，则IPv6地址需要用“[]”括起来。例如：[2001:db8::1]/test
指定URL关键字类别及控制动作
指定需要进行控制的URL关键字类别及控制动作，在URL过滤Profile配置模式下使用以下命令：

<!-- 来源页 2462 -->
keyword-category {keyword-category-name | other} [block] [log]
l
keyword-category-name | other – 指定需要进行控制的URL关键字类别名称，可以为特定URL关键
字类别（keyword-category-name）或除此之外的所有URL关键字类别（other）。
l
block – 指定阻止访问网址中含有相应关键字的网站。
l
log – 指定对访问网址中含有相应关键字的网站的行为进行日志记录。
使用多条该命令可指定多个URL关键字类别及相应的控制动作。
在URL过滤Profile配置模式下，使用no keyword-category {keyword-category-name | other}命令
取消URL关键字类别及控制动作的指定。
开启安全搜索功能
许多搜索引擎，如Google、Bing、Yahoo!、Yandex、Youtube，都包含“安全搜索”设置项，该设置
用来过滤搜索结果中的成人内容，搜索引擎会根据该设置项的设置返回不同级别的搜索结果。系统支持通过
在URL过滤Profile中开启安全搜索功能，来检测搜索引擎“安全搜索”的设置以及执行相应的控制动作。
开启安全搜索功能并指定控制动作，在URL过滤Profile配置模式下，使用以下命令：
safe-search {block | enforce}
l
block – 指定动作为阻断，即当检测出搜索引擎“安全搜索”未设置时，阻止用户访问搜索页面并显示
警告提示页面，提供“安全搜索”设置链接提示用户前往设置。
l
enforce – 指定动作为执行，即当检测出搜索引擎“安全搜索”未设置时，系统强制将搜索引擎的“安
全搜索”设置为最严格级别。
在URL过滤Profile配置模式下，使用no safe-search关闭安全搜索功能。
注意:
l
安全搜索功能目前仅支持以下搜索引擎：Google、Bing、Yahoo!、Yandex、Youtube。
l
由于搜索引擎使用HTTPS协议，因此安全搜索功能与SSL代理功能结合才可使用，需要为URL
过滤Profile（已开启安全搜索功能）绑定的策略规则启用SSL代理功能。
l
为了保证Google搜索引擎安全搜索功能的有效性，需要配置策略规则阻断UDP 80和UDP 443
端口号。
绑定URL过滤Profile到安全域
将URL过滤Profile绑定到安全域后，系统将会对以该安全域为目的安全域的流量按照Profile配置进行URL
过滤检查。当策略规则已经绑定了URL过滤Profile，同时策略规则的目的安全域也绑定了URL过滤

<!-- 来源页 2463 -->
Profile，策略规则绑定的URL过滤Profile将会生效，而目的安全域绑定的URL过滤Profile无效。
绑定URL过滤Profile到安全域，在安全域配置模式下，使用以下命令：
url enable url-profile-name
l
url-profile-name – 指定绑定到安全域的URL过滤Profile的名称。一个安全域只能绑定一个URL过滤
Profile。
在安全域配置模式下，使用该命令no的形式取消URL过滤Profile的绑定：
no url enable
绑定URL过滤Profile到策略规则
将URL过滤Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据Profile配置进行处理。绑
定URL过滤Profile到策略规则，需要在策略规则配置模式下进行。
进入策略规则配置模式需要进行两步配置。首先，在全局配置模式下，输入以下命令进入策略配置模式：
policy-global
然后，在策略配置模式下，输入以下命令进入策略规则配置模式：
rule [id id-number]
进入策略规则配置模式后，输入以下命令将URL过滤Profile绑定到策略规则
url profile-name
l
profile-name - 指定所需要绑定的URL过滤Profile名称。
注意: 被绑定的URL过滤Profile只有在解除绑定后，才可以进行删除。
绑定配置完成后，需要修改策略规则的优先级，确保流量优先匹配此策略规则，然后可以继续指定策略规则
的用户、目的安全域和时间表参数，并能禁用或者启用该条策略规则。
如果需要对HTTPS流量执行URL过滤功能，需要为上述策略规则启用SSL代理功能。系统将根据SSL代理
Profile解密HTTPS流量，对解密后的数据根据URL过滤Profile进行检测。
根据安全策略规则的配置不同，系统将进行如下操作：
安全策略规则配置
操作
启用SSL代理
不启用URL过滤
根据SSL代理Profile解密HTTPS流量，对解密后的数据不进行URL过滤。
启用SSL代理
启用URL过滤
根据SSL代理Profile解密HTTPS流量，对解密后的数据根据URL过滤Profile进行
URL过滤。

<!-- 来源页 2464 -->
安全策略规则配置
操作
不启用SSL代理
启用URL过滤
对HTTP流量根据URL过滤Profile进行URL过滤。对HTTPS流量不进行解密，如
果URL过滤Profile没有配置SSL检测，则不进行URL过滤，只进行转发；如果
URL过滤Profile配置了SSL检测，则根据URL过滤Profile进行URL过滤。
如果此条策略启用了SSL代理，但是URL过滤Profile对应的URL过滤规则中的控制类型为“上网日志记
录”，系统将不会对HTTPS流量中的GET和POST方法及内容进行记录。
当安全策略规则所关联的安全域也启用URL过滤时，系统将进行如下操作：
安全策略规则配置
安全域配置
操作
启用SSL代理
不启用URL过滤
启用URL过滤
根据SSL代理Profile解密HTTPS流量，对解密后的数据
根据安全域配置的URL过滤Profile进行URL过滤。
启用SSL代理
启用URL过滤
启用URL过滤
根据SSL代理Profile解密HTTPS流量，对解密后的数据
根据安全策略规则中配置的URL过滤Profile进行URL过
滤。
不启用SSL代理
启用URL过滤
启用URL过滤
对HTTP流量根据安全策略规则中配置的URL过滤Profile
进行URL过滤。对HTTPS流量不进行解密，如果URL过滤
Profile没有配置SSL检测，则不进行URL过滤，只进行转
发；如果URL过滤Profile配置了SSL检测，则根据URL过
滤Profile进行URL过滤。
显示URL过滤Profile信息
在任何模式下，输入以下命令显示URL过滤Profile信息：
show url-profile [profile-name]
l
profile-name – 显示指定URL过滤Profile的信息。若不指定Profile名称，显示系统中所有URL过滤
Profile的信息。
URL黑白名单
用户可以通过配置URL黑白名单来进一步控制对某些指定网站的访问。
l
在配置URL黑名单后，当用户向黑名单中指定的URL发出访问请求时，系统将对该请求进行阻断。
l
在配置URL白名单后，当用户向白名单中指定的URL发出访问请求时，系统将不对该访问请求进行URL过
滤，并且对该访问请求放行处理。
l
若URL黑名单、URL白名单、URL过滤Profile中均配置了URL类别，系统对URL类别过滤的匹配优先级
为：URL白名单>URL黑名单>URL过滤Profile。

<!-- 来源页 2465 -->
注意:
l
同一个URL类别只能被一个对象（URL黑名单、URL白名单或URL过滤规则）引用，例如：当
URL类别“广告”已被添加到URL黑名单中，那么该URL类别将不能被添加到URL白名单，同
时在URL过滤Profile中将不能被引用。
l
非根VSYS不支持URL黑白名单功能。
配置URL黑名单
URL黑名单用来过滤不被允许的URL访问请求，将URL类别添加到URL黑名单中后，对于命中URL黑名单的
HTTP/HTTPS流量进行阻断。
配置URL黑名单，需要在URL黑名单配置模式下进行。进入URL黑名单配置模式，在全局配置模式下，使用
以下命令：
url-blocklist
添加URL类别到URL黑名单中，在URL黑名单配置模式下，使用以下命令：
url-category url-category-name
l
url-category-name - 指定添加到URL黑名单中的URL类别。
在URL黑名单配置模式下，使用该命令no的形式将指定的URL类别从URL黑名单中删除：
no url-category url-category-name
配置URL白名单
URL白名单用来过滤允许的URL访问请求，将URL类别添加到URL白名单中后，对于命中URL白名单的
HTTP/HTTPS流量进行放行处理，且不会被URL过滤Profile控制。
配置URL白名单，需要在URL白名单配置模式下进行。进入URL白名单配置模式，在全局配置模式下，使用
以下命令：
url-allowlist
添加URL类别到URL白名单中，在URL白名单配置模式下，使用以下命令：
url-category url-category-name
l
url-category-name - 指定添加到URL白名单中的URL类别。
在URL白名单配置模式下，使用该命令no的形式将指定的URL类别从URL白名单中删除：
no url-category url-category-name

<!-- 来源页 2466 -->
显示URL黑名单信息
在任何模式下，输入以下命令显示URL黑名单信息：
show url-blocklist
显示URL白名单信息
在任何模式下，输入以下命令显示URL白名单信息：
show url-allowlist

<!-- 来源页 2467 -->
SSL代理
仅有部分平台支持该功能，请以实际页面为准。
为了保护敏感数据在互联网传送中的安全性，越来越多的网站都采用SSL加密形式发布。设备提供SSL代理功
能，能够解密HTTPS、POP3S、SMTPS、IMAPS、RDPS和FTPS流量。SSL代理功能可工作在如下两种场
景：
第一种场景，当设备作为Web客户端一侧的网关时，SSL代理功能利用SSL代理证书替换加密Web网站的数
字证书，并将SSL代理证书发送到客户端的Web浏览器，在此过程中，设备分别作为SSL客户端和SSL服务器
与Web服务器和Web浏览器建立SSL连接，从而获得加密通信的明文内容。SSL代理证书是使用设备本身的
证书对Web服务器证书重新签发而成的证书。过程如下图所示：
第二种场景，当设备作为Web服务器一侧的网关时，开启SSL代理功能的设备可充当SSL服务器，使用Web
服务器的证书与客户端建立SSL连接，并将解密后的流量以明文的方式发送到内网的Web服务器。
工作模式
根据如上两种使用场景，SSL代理可工作在两种模式下。对于第一种场景，可工作在“客户端流量检查-代理
模式”下；对于第二种场景，可工作在“服务器流量检查-卸载模式”和“服务器流量检查-代理模式”下。
l 工作在“客户端流量检查-代理模式”时，可对指定的网站进行SSL代理。对于不需要进行SSL代理的网站，设备
将网站IP地址和端口号动态添加到放行名单，其流量被放行；对于需要进行SSL代理的网站，设备将会对SSL协商
过程中的参数进行检查。对于符合检查条件的SSL协商参数，用户可对其
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行阻断或者放行。
l 设置为阻断行为的HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量，设备将会对其进行阻断；
l 设置为放行行为的HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量，设备不会对其进行解密。同时，设
备将此网站IP地址和端口号动态地添加到放行名单，则其HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流
量被放行。

<!-- 来源页 2468 -->
l 对于既没有被阻断，也没有被放行的HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量，设备将会对其解
密。
l 工作在“服务器流量检查-卸载模式”时，设备将对来自Web客户端发起的SSL连接进行代理，解密数据，并将数
据以明文的方式发送给Web服务器。
l 工作在“服务器流量检查-代理模式”时，设备将对来自Web客户端发起的SSL连接进行代理，解密数据，并将数
据重新加密后发送给Web服务器。
SSL代理功能可与如下功能模块结合使用：
l 与应用识别结合使用，设备能够对使用SSL加密通讯的应用所产生的HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS
流量进行解密与识别。识别应用后，可针对应用进行策略控制、流量控制、会话限制、配置策略路由等。
l 与Web认证结合使用，支持单边SSL代理。在客户端进行认证时启动SSL连接，认证通过后，SSL代理不再工作，
客户端与服务器之间直接交互。
l 与AV、IPS、URL、文件过滤、内容过滤与沙箱结合使用，设备能够对
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行AV防护、IPS防护、文件过滤、URL过滤、文件内容过滤以
及沙箱防护；对HTTPS流量进行网页关键字过滤、Web外发信息过滤以及应用行为控制；对
POP3S/SMTPS/IMAPS流量进行邮件过滤。

<!-- 来源页 2469 -->
当设备作为Web客户端一侧的网关时
通过策略规则与SSL代理Profile相结合的方式可实现SSL代理。将SSL代理Profile绑定到策略规则后，系统
将会对与策略规则相匹配的网络流量根据SSL代理Profile配置进行处理。请按照以下步骤进行操作：
1. 配置SSL代理相关参数，包括指定设备证书的PKI信任域、获取网站证书Subject字段的CN值以及导入设备证书到
客户端Web浏览器。
2. 定义SSL代理Profile，在Profile中设置工作模式，对符合检查条件的SSL协商设置行为、启用警告提示功能等。
3. 将SSL代理Profile绑定到适当的策略规则，对符合策略规则且没有被阻断与放行的
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行解密。
配置SSL代理相关参数
SSL代理相关参数的配置包括：
l 指定PKI信任域
l 获取网站证书的CN值
l 导入设备证书到客户端Web浏览器
指定PKI信任域
默认情况下，设备会使用缺省PKI信任域trust_domain_ssl_proxy_2048的配置对Web服务器证书重新签
发，生成SSL代理证书。
指定设备证书信任域，在全局配置模式下，使用以下命令：
sslproxy trust-domain trust-domain-name
l
trust-domain-name – 指定系统中已创建的PKI信任域名称。
在全局配置模式下，使用no sslproxy trust-domain命令取消指定的信任域。
获取网站证书的CN值
获取网站证书Subject字段的CN值，按照以下步骤进行操作（以需要获得https://mail.qq.com/网站证书
Subject字段的CN值为例）：
1. 打开Web浏览器（以Chrome版本121.0.6167.185为例），访问https://mail.qq.com。
2. 在浏览器地址栏单击
图标。
3. 在弹出菜单中选择“链接是安全的”。

<!-- 来源页 2470 -->
4. 点击“证书有效”，打开证书详情页。
5. 在“基本信息”页签的“公用名（CN）”字段查看对应的CN值。
导入设备证书到客户端Web浏览器
进行SSL代理时，设备会用SSL代理证书替换SSL Web站点的证书，并发送到客户端Web浏览器。由于客户
端浏览器不拥有SSL代理证书的根证书，从而导致用户不能正常访问代理站点。为了解决这个问题，需要在
客户端浏览器中导入SSL代理证书的根证书，也即设备证书。导入设备证书到客户端PC浏览器，请按照以下
步骤进行操作：
1.
导出设备证书，使用以下命令完成此配置：
命令行：
export pki trust-domain-name {cacert | cert | pkcs12 password | pkcs12-der password}
to {ftp server ip-address [user user-name password password] | tftp server ip-address |
usb0 | usb1} [file-name]
示例：
hostname# export pki trust_domain_ssl_proxy cacert to tftp server 10.10.10.1
Export ok,target filename 1252639478
hostname#
2.
导入证书到客户端PC浏览器（导入证书前，请将证书文件扩展名修改为“.crt”）。在客户端Web浏览
器（以Internet Explorer为例）选择“工具> Internet选项> 内容> 证书> 受信任的根证书颁发机
构”。点击列表下方的“导入”按钮，如下图所示，弹出<证书导入向导>，按照向导提示将设备证书导
入到浏览器。

<!-- 来源页 2471 -->
如果在第一步导出设备证书中指定的加密标准为“pkcs12”或者“pkcs12-der”，则在导入证书到客
户端PC浏览器时，用户需要在弹出的证书密码框中输入证书密码（第一步导出设备证书中通过“pkcs12
password | pkcs12-der password”指定的密码）。
配置SSL代理Profile
SSL代理Profile中可以配置会话复用功能，设置SSL代理工作模式，设置需要进行SSL代理的网站名单(通过
网站证书的Subject字段的CN值进行指定)，对符合检查条件的SSL协商设置相应的行为，配置设备根证书下
载提示，以及配置描述信息等。创建SSL代理Profile，在全局配置模式下使用以下命令：
sslproxy-profile profile-name
l
profile-name - 指定所创建的SSL代理Profile的名称，并且进入该SSL代理Profile的配置模式。如果
指定名称已存在，则直接进入SSL代理Profile配置模式。使用no sslproxy-profile profile-name删
除指定的SSL代理Profile。
配置会话复用功能
SSL代理支持会话复用功能。配置该功能后，当客户端向服务器端发起SSL连接请求时，服务器端会判断该请
求连接是否已经创建过，如果是，则恢复之前的SSL连接，无需再进行完整的TLS握手协商过程，从而减少了
TLS握手过程中的时间耗费。
系统支持以下两种会话复用方式：

<!-- 来源页 2472 -->
l Session Ticket会话复用：客户端与Web服务器端完成第一次SSL连接后，服务器端将本次TLS握手中生成的对称
密钥及其他状态信息加密并生成Session Ticket，然后将Session Ticket发送给客户端，由客户端保存。当客户
端再次向服务器端发起SSL连接请求（或者断开连接后再次发起连接请求）时，会将Session Ticket同时发送给
服务器端，如果服务器端解密校验成功，则恢复第一次的SSL连接，进行会话复用。
l Session ID会话复用：客户端与Web服务器端完成第一次SSL连接后，客户端和服务器端将本次TLS握手中生成
的Session ID、对称密钥及其他状态信息缓存在本端。当客户端再次向服务器端发起SSL连接请求（或者断开连
接后再次发起连接请求）时，服务器将新请求中的Session ID与已缓存的Session ID进行对比，如果一致，则恢
复第一次的SSL连接，进行会话复用。
注意:
l
当设备作为Web客户端一侧的网关时，需要Web服务器端同时支持会话复用功能；
l
如果同时配置了Session Ticket会话复用方式和Session ID会话复用方式，系统优会先使用
Session Ticket会话复用方式。
配置会话复用方式
开启/关闭Session ID会话复用方式或者Session Ticket会话复用方式，在SSL代理Profile配置模式下使用
以下命令：
session reuse {id | ticket} {enable | disable}
l
id | ticket - 指定开启（enable）或者关闭（disable）Session ID （id）会话复用方式或者Session
Ticket（ticket）会话复用方式。
配置会话缓存数量
配置系统保存Session ID会话复用方式下的会话缓存数量或者Session Ticket会话复用方式下的会话缓存数
量，在SSL代理Profile配置模式下使用以下命令：
session reuse cache-size value
l
value - 指定系统保存Session ID会话复用方式下的会话缓存数量或者Session Ticket会话复用方式下
的会话缓存数量。
该选项的取值范围和默认值因设备型号而异，分为以下三类，请以实际界面为准。

<!-- 来源页 2473 -->
o
取值范围：0-32（单位：条）；默认值：32。
o
取值范围：0-128（单位：条）；默认值：128。
o
取值范围：0-256（单位：条）；默认值：256。
说明：0表示不保存会话缓存信息。
在SSL代理Profile配置模式下，使用no session reuse cache-size命令取消会话缓存数量配置。
配置会话超时时间
配置系统保存Session ID会话复用方式下的会话缓存或者Session Ticket会话复用方式下的会话缓存的时
间，在SSL代理Profile配置模式下使用以下命令：
session reuse timeout value
l
value - 指定系统保存Session ID会话复用方式下的会话缓存或者Session Ticket会话复用方式下的会
话缓存的时间，超过该指定时间后，系统将删除会话缓存，当客户端与服务器端建立SSL连接时，需要重
新进行完整的TLS握手协商过程。取值范围为1800秒至72000秒，默认取值为3600秒。
在SSL代理Profile配置模式下，使用no session reuse timeout命令取消会话超时时间配置。
清除会话缓存
清除系统中保存的Session ID会话复用方式下的会话缓存或者Session Ticket会话复用方式下的会话缓存，
在任意模式下，使用以下命令：
clear sslproxy {session-ticket | session-id} cache
l
session-ticket | session-id - 指定清除系统中保存的Session ID会话复用方式下的会话缓存
（session-id）或者Session Ticket会话复用方式下的会话缓存（session-ticket）。
查看会话缓存信息
查看系统中保存的Session ID会话复用方式下的会话缓存信息或者Session Ticket会话复用方式下的会话缓
存信息，在任意模式下，使用以下命令：
show sslproxy {session-ticket | session-id} cache
l
session-ticket | session-id - 查看系统中保存的Session ID会话复用方式下的会话缓存信息
（session-id）或者Session Ticket会话复用方式下的会话缓存信息（session-ticket）。
设置SSL代理工作模式
当设备作为Web客户端一侧的网关时，SSL代理可工作在客户端流量检查-代理模式。

<!-- 来源页 2474 -->
l
工作在客户端流量检查模式下时，可对指定的网站进行SSL代理。对于不需要进行SSL代理的网站，设备
将网站IP地址和端口号动态添加到放行名单，且HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量被放
行；对于需要进行SSL代理的网站，设备将会对SSL协商过程中的参数进行检查。对于符合检查条件的
SSL协商参数，用户可对其HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行阻断或者放行。
指定SSL代理的工作模式，在SSL代理Profile配置模式下使用以下命令：
mode client-inspection proxy
设置SSL代理的应用类型
当SSL代理工作在客户端流量检查-代理模式时，用户可指定SSL代理检查的应用类型。默认情况下，系统仅
对默认端口的HTTPS流量进行SSL代理。用户可根据需要添加其他应用进行SSL代理，如IMAPS、POP3S、
SMTPS、RDPS和FTPS。系统支持对SSL代理检查的应用配置自定义端口，具体配置可参考“防火墙>服务
与应用>用户自定义应用”中的“在自定义应用特征配置模式配置自定义应用特征规则”内容。
指定SSL代理检查的应用类型，在SSL代理Profile配置模式下使用以下命令：
inspect-app {https | imaps | pop3s | smtps | rdps | ftps}
l
https - 指定对HTTPS流量进行SSL代理。
l
imaps - 指定对IMAPS流量进行SSL代理。
l
pop3s- 指定对POP3S流量进行SSL代理。
l
smtps - 指定对SMTPS流量进行SSL代理。
l
rdps- 指定对RDPS流量进行SSL代理。
l
ftps- 指定对FTPS流量进行SSL代理。
设置URL白名单
当工作在“客户端流量检查-代理模式”下，用户可以根据需要指定URL类别（预定义URL类别或自定义URL
类别），添加到URL白名单中，设备将会对URL白名单中的网站不进行SSL代理。默认情况下，预定义URL类
别“医疗健康”和“财经”已添加到URL白名单中。
设置URL白名单，在SSL代理Profile配置模式下，使用以下命令：
url-category category-name
l
category-name - 指定需要添加到URL白名单中的URL类别名称。最多可以添加8个URL类别。
使用no url-category category-name删除添加到URL白名单中的URL类别。
注意: 为确保URL白名单能够正常生效，请在配置该功能前先升级预定义URL库。

<!-- 来源页 2475 -->
配置设备根证书下载提示
当用户的HTTPS访问行为被SSL代理功能监控，即，HTTPS流量被解密时，该用户的HTTPS网页访问请求会
被重定向到设备根证书下载的提示页面，提示其HTTPS访问行为将受到监控，注意保护个人隐私并遵守相关
法律法规。设备根证书下载提示页面如下图所示：
在SSL代理Profile配置模式下，使用如下命令开启或关闭设备根证书下载的提示：
开启设备根证书下载提示：no ca-cert-push disable
关闭设备根证书下载提示：ca-cert-push disable
如果用户开启设备根证书下载的提示功能，对于同一个源IP，若用户的HTTPS访问行为与策略规则相匹配，
则用户在浏览该HTTPS网站时会每隔12小时收到一次设备根证书下载的提示。
用户可以清除SSL代理的设备根证书下载提示记录，清除记录后，无论用户之前何时收到过下载提示，当用
户再次访问HTTPS页面并且该访问行为匹配策略规则时，系统会立即推送设备根证书下载页面。清除设备根
证书下载提示历史记录，在任意模式下，使用以下命令：
clear sslproxy ca-cert-push
对符合检查条件的SSL协商设置行为
在SSL代理过程中，系统将会对SSL协商过程中的参数进行检查。对于符合检查条件的SSL协商参数，用户可
对其HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行阻断或者放行。
l 设置为阻断行为的HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量将无法显示在浏览器中；
l 设置为放行行为的HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量，设备不会对其进行解密。同时，设备将此
网站证书的Subject字段的CN值动态地添加到放行名单。对于动态地添加到放行名单的网站，第一次连接会断
开，用户需要重新发起HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS访问才能正常显示网站内容。
对于既没有被阻断，也没有被放行的HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量，设备将会对其解
密。
在配置过程中，注意如下事项：

<!-- 来源页 2476 -->
l 当SSL协商的参数符合多个检查条件且用户对不同的检查条件设置不同的行为，即，阻断行为和放行行为，则阻
断行为生效。相关的HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量将会被阻断。
l 系统完成对SSL协商的检查后，对于既没有被阻断，也没有被放行的SSL协商，系统将完成SSL代理功能，其
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量将会被解密。
检查服务器使用的SSL协议版本
检查服务器使用的SSL协议版本。当SSL服务器使用指定范围内版本的SSL协议时，系统将代理其
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量。配置系统支持的SSL协议版本，在SSL代理Profile配置
模式下，使用如下命令：
l
max-support-ssl-version {tlsv1.0 | tlsv1.1 | tlsv1.2 | tlsv1.3}–配置系统支持的最高的SSL协议版
本，默认为tlsv1.3。
l
min-support-ssl-version {tlsv1.0 | tlsv1.1 | tlsv1.2 | tlsv1.3}–配置系统支持的最低的SSL协议版
本，默认为tlsv1.0。
恢复系统默认设置，使用no {max-support-ssl-version |  min-support-ssl-version}命令。
当SSL服务器端使用了系统不支持的SSL协议时，配置系统对HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS
流量采取的动作，在SSL代理Profile配置模式下，使用如下命令：
unsupported-ssl-version bypass | block}
l
bypass | block–使用bypass参数放行HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量且不对
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行解密。使用block参数阻断
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量。当SSL服务器端使用了系统不支持的SSL协议时，
系统默认放行HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量且不对
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行解密。
恢复系统默认设置，使用no unsupported-ssl-version命令。
检查未知错误
当SSL握手失败而又无法确认失败的原因时，配置系统对HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量
采取的动作，在SSL代理Profile配置模式下，使用如下命令：
unknown-ssl-failure {bypass | block}
l
bypass | block–使用bypass参数放行HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量且不对
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行解密。使用block参数阻断

<!-- 来源页 2477 -->
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量。系统默认放行
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量且不对
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行解密。
恢复系统默认值，使用no unknown-ssl-failure命令。
检查加密算法
当SSL服务器端使用了系统不支持的加密算法时，配置系统对HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS
流量采取的动作，在SSL代理Profile配置模式下，使用如下命令：
unsupported-cipher {bypass | block}
l
bypass | block–使用bypass参数放行HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量且不对
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行解密。使用block参数阻断
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量。系统默认放行
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量且不对
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行解密。
恢复系统默认值，使用no unsupported-cipher命令。
检查服务器证书是否过期
检查SSL服务器证书是否过期。当SSL服务器的证书过期时，系统可解密、阻断或者放行
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量。在SSL代理Profile配置模式下，使用如下命令设置行
为：
expired-cert {decrypt | block | bypass}
l
decrypt |block | bypass – 使用decrypt参数对HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进
行解密。使用block参数阻断HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量。使用bypass参数放行
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量且不对
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行解密。系统默认对SSL服务器过期证书的HTTPS
流量进行解密。
恢复系统默认设置，使用no expired-cert命令。
检查服务器是否需要验证客户端证书
检查服务器是否需要验证客户端证书。当服务器需要验证客户端证书时，系统可阻断或者放行
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量。当服务器需要验证客户端证书时，配置系统对
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量采取的动作，在SSL代理Profile配置模式下，使用如下

<!-- 来源页 2478 -->
命令：
verify-client {bypass | block}
l
bypass | block–使用bypass参数放行HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量且不对
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行解密。使用block参数阻断
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量。系统默认放行
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量且不对
HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量进行解密。
恢复系统默认设置，使用no verify-client命令。
服务器证书验证失败时系统的防护动作
当系统验证服务器证书失败时，用户可根据需要配置系统对HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流
量的防护动作。在SSL代理Profile配置模式下，使用以下命令：
verify-server-cert-failed {block | bypass | decrypt}
l
block - 系统将阻断验证失败的HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量。
l
bypass - 系统将放行验证失败的HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量。
l
decrypt - 系统将继续解密验证失败的HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量。对服务器证
书验证失败的HTTPS/POP3S/SMTPS/IMAPS/RDPS/FTPS流量解密时，系统默认使用设备自签名证书
与客户端Web浏览器进行SSL协商。用户还可选择使用可信证书“SG6000”与客户端Web浏览器进行
SSL协商，在SSL代理Profile配置模式下，使用use-self-sign-cert disable 命令。恢复系统默认
值，使用no use-self-sign-cert disable命令。
配置描述信息
为SSL代理Profile添加描述信息，在SSL代理Profile配置模式下，使用如下命令：
description description
l
description – 输入描述信息。
使用no description删除描述信息。
指定优先使用低强度加密算法
在设备作为Web客户端一侧的网关时，当收到SSL客户端发送的加密套件后，将会默认使用高强度的加密算
法，以保证SSL代理功能的性能。如果用户需要降低SSL代理功能的加密强度，可以指定SSL服务器端优先使
用低强度的加密算法，在SSL代理Profile配置模式下，使用如下命令：

<!-- 来源页 2479 -->
downstream-cipher-mode low-intensity-first
恢复默认使用高强度的加密算法，使用no downstream-cipher-mode low-intensity-first命令。
可信根证书库升级
为减少验证服务器证书时出现问题，系统需保证本地可信根证书库足够全，且及时更新可信根证书库。用户
可以根据需要更改可信根证书库的升级更新配置信息。可信根证书库升级更新配置包括：
l 配置可信根证书库升级信息
l 立即更新
l 导入可信根证书库文件
l 查看可信根证书库升级信息
l 查看可信根证书库信息
配置可信根证书库升级信息
配置可信根证书库的升级信息，在全局配置模式下，使用以下命令：
trusted-root-ca-store update {mode {auto | manual} | proxy-server {main | backup} proxy-ip
proxy-port | schedule {daily | weekly {sun | mon | tue | wed | thu | fri | sat} | monthly date} |
server1 {domain | ip} [vrouter vrouter-name] [src-interface src-interface-name] | server2
{domain | ip} [vrouter vrouter-name] [src-interface src-interface-name] | server3 {domain |
ip} [vrouter vrouter-name] [src-interface src-interface-name] | protocol HTTP}
l
mode {auto | manual} – 指定升级可信根证书库的方式，分为自动升级和手动升级。不配置默认为自
动升级。
l
proxy-server {main | backup} proxy-ip proxy-port – 指定升级可信根证书库的代理服务器。
l
schedule {daily | weekly {sun | mon | tue | wed | thu | fri | sat} | monthly date} – 指定自动升
级可信根证书库的升级周期。
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

<!-- 来源页 2480 -->
l
src-interface src-interface-name – 指定源接口名称，该源接口需为虚拟路由器下的接口。指定
后，可信根证书库更新时将通过该源接口对升级服务器发起访问。若不指定，则默认使用管理口作为源
接口。
立即更新
用户可以立即升级可信根证书库。在执行模式下，使用以下命令：
exec trusted-root-ca-store update
导入可信根证书库文件
在某些情况下，用户设备可能无法连接到更新服务器对可信根证书库进行更新，针对这一问题，StoneOS提
供可信根证书库文件导入功能。用户可以通过FTP或者TFTP方式导入可信根证书库，从而更新设备的可信根
证书库。导入可信根证书库文件，在执行模式下，使用以下命令：
import trusted-root-ca-store from {ftp server { A.B.C.D | X:X:X:X::X } [vrouter vrouter-name]
[user username password string] | tftp server { A.B.C.D | X:X:X:X::X }[vrouter vrouter-name]}
file-name
l
ftp server { A.B.C.D | X:X:X:X::X } [vrouter vrouter-name] [user user-name password
password] – 指定从FTP服务器获取可信根证书库文件，并指定FTP服务器的IP地址、FTP服务器所属的
VRouter以及访问服务器使用的用户名和密码。当不输入用户名和密码时表示采用匿名登录方式。
l
tftp server { A.B.C.D | X:X:X:X::X } [vrouter vrouter-name] – 指定从TFTP服务器获取可信根证书
库文件，并指定TFTP服务器的IP地址以及所属的VRouter。
l
file-name – 指定导入的可信根证书库文件的名称。
查看可信根证书库升级信息
用户可以在任何模式下使用以下命令查看可信根证书库升级信息：
show trusted-root-ca-store update
查看可信根证书库信息
用户可以在任何模式下使用以下命令查看可信根证书库信息：
show trusted-root-ca-store info
绑定SSL代理Profile到策略规则
将SSL代理Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据Profile配置进行处理。绑定
SSL代理Profile到策略规则，需要在策略规则配置模式下进行。
进入策略规则配置模式需要进行两步配置。首先，在全局配置模式下，输入以下命令进入策略配置模式：

<!-- 来源页 2481 -->
policy-global
然后，在策略配置模式下，输入以下命令进入策略规则配置模式：
rule [id id-number]
进入策略规则配置模式后，输入以下命令将SSL代理Profile绑定到策略规则
sslproxy profile-name
l
profile-name - 指定所需要绑定的SSL代理Profile名称。
绑定配置完成后，需要修改策略规则的优先级，确保流量优先匹配此策略规则，然后可以继续指定策略规则
的用户、目的安全域和时间表参数，并能禁用或者启用该条策略规则。具体配置命令请参阅“安全策略”。

<!-- 来源页 2482 -->
当设备作为Web服务器一侧的网关时
通过策略规则与SSL代理Profile相结合的方式可实现SSL代理。将SSL代理Profile绑定到策略规则后，系统
将会对与策略规则相匹配的网络流量根据SSL代理Profile配置进行处理。请按照以下步骤进行操作：
1. 定义SSL代理Profile，在Profile中设置工作模式，指定Web服务器证书的信任域以及端口号。
2. 将SSL代理Profile绑定到适当的策略规则，对符合策略规则的HTTPS流量进行代理。
配置SSL代理Profile
SSL代理Profile中可以配置会话复用功能，设置SSL代理工作模式，指定Web服务器证书的信任域及端口
号。创建SSL代理Profile，在全局配置模式下使用以下命令：
sslproxy-profile profile-name
l
profile-name - 指定所创建的SSL代理Profile的名称，并且进入该SSL代理Profile的配置模式。如果
指定名称已存在，则直接进入SSL代理Profile配置模式。
使用no sslproxy-profile profile-name删除指定的SSL代理Profile。
配置会话复用功能
SSL代理支持会话复用功能。配置该功能后，当客户端向服务器端发起SSL连接请求时，服务器端会判断该请
求连接是否已经创建过，如果是，则恢复之前的SSL连接，无需再进行完整的TLS握手协商过程，从而减少了
TLS握手过程中的时间耗费。
系统支持以下两种会话复用方式：
l Session Ticket会话复用：客户端与Web服务器端完成第一次SSL连接后，服务器端将本次TLS握手中生成的对称
密钥及其他状态信息加密并生成Session Ticket，然后将Session Ticket发送给客户端，由客户端保存。当客户
端再次向服务器端发起SSL连接请求（或者断开连接后再次发起连接请求）时，会将Session Ticket同时发送给
服务器端，如果服务器端解密校验成功，则恢复第一次的SSL连接，进行会话复用。
l Session ID会话复用：客户端与Web服务器端完成第一次SSL连接后，客户端和服务器端将本次TLS握手中生成
的Session ID、对称密钥及其他状态信息缓存在本端。当客户端再次向服务器端发起SSL连接请求（或者断开连
接后再次发起连接请求）时，服务器将新请求中的Session ID与已缓存的Session ID进行对比，如果一致，则恢
复第一次的SSL连接，进行会话复用。

<!-- 来源页 2483 -->
注意:
l
当设备作为Web服务器一侧的网关时，需要Web客户端同时支持会话复用功能；
l
如果同时配置了Session Ticket会话复用方式和Session ID会话复用方式，系统优会先使用
Session Ticket会话复用方式。
配置会话复用
开启/关闭Session ID会话复用方式或者Session Ticket会话复用方式，在SSL代理Profile配置模式下使用
以下命令：
session reuse {id | ticket} {enable | disable}
l
id | ticket - 指定开启（enable）或者关闭（disable）Session ID （ticket）会话复用方式或者
Session Ticket（id）会话复用方式。
配置会话缓存数量
配置系统保存Session ID会话复用方式下的会话缓存数量或者Session Ticket会话复用方式下的会话缓存数
量，在SSL代理Profile配置模式下使用以下命令：
session reuse cache-size value
l
value - 指定系统保存Session ID会话复用方式下的会话缓存数量或者Session Ticket会话复用方式下
的会话缓存数量。
该选项的取值范围和默认值因设备型号而异，分为以下三类，请以实际界面为准。
o
取值范围：0-32（单位：条）；默认值：32。
o
取值范围：0-128（单位：条）；默认值：128。
o
取值范围：0-256（单位：条）；默认值：256。
说明：0表示不保存会话缓存信息。
在SSL代理Profile配置模式下，使用no session reuse cache-size命令取消会话缓存数量配置。
配置会话超时时间
配置系统保存Session ID会话复用方式下的会话缓存或者Session Ticket会话复用方式下的会话缓存的时
间，在SSL代理Profile配置模式下使用以下命令：
session reuse timeout value

<!-- 来源页 2484 -->
l
value - 指定系统保存Session ID会话复用方式下的会话缓存或者Session Ticket会话复用方式下的会
话缓存的时间，超过该指定时间后，系统将删除会话缓存，当客户端与服务器端建立SSL连接时，需要重
新进行完整的TLS握手协商过程。取值范围为1800秒至72000秒，默认取值为3600秒。
在SSL代理Profile配置模式下，使用no session reuse timeout命令取消会话超时时间配置。
清楚会话缓存
清除系统中保存的Session ID会话复用方式下的会话缓存或者Session Ticket会话复用方式下的会话缓存，
在任意模式下，使用以下命令：
clear sslproxy {session-ticket | session-id} cache
l
session-ticket | session-id - 指定清除系统中保存的Session ID会话复用方式下的会话缓存
（session-id）或者Session Ticket会话复用方式下的会话缓存（session-ticket）。
查看会话缓存信息
查看系统中保存的Session ID会话复用方式下的会话缓存信息或者Session Ticket会话复用方式下的会话缓
存信息，在任意模式下，使用以下命令：
show sslproxy {session-ticket | session-id} cache
l
session-ticket | session-id - 查看系统中保存的Session ID会话复用方式下的会话缓存信息
（session-id）或者Session Ticket会话复用方式下的会话缓存信息（session-ticket）。
设置SSL代理工作模式
当设备作为Web服务器一侧的网关时，SSL代理可工作在“服务端流量检查-卸载模式”或“服务端流量检查
-代理模式”。
l
“服务端流量检查-卸载模式”下，设备将对来自Web客户端发起的SSL连接进行代理，解密数据，并将
数据以明文的方式发送给Web服务器。
l
“服务端流量检查-代理模式”下，设备将对来自Web客户端发起的SSL连接进行代理，解密数据，并将
数据重新加密后发送给Web服务器。
指定SSL代理的工作模式，在SSL代理Profile配置模式下，使用以下命令：
mode server-inspection { offload | proxy}
l
offload - 指定SSL代理工作模式为服务端流量检查-卸载模式。
l
proxy - 指定SSL代理工作模式为服务端流量检查-代理模式。

<!-- 来源页 2485 -->
指定信任域
由于设备代理Web服务器与Web客户端建立SSL连接，所以，需要将Web服务器的证书和秘钥对导入到设备
中。如何导入证书和秘钥对，可参考《StoneOS命令行用户手册_用户认证》的PKI配置章节。导入证书后和
秘钥对后，需要在设备中指定此Offload模式对应的信任域，即，存储此证书和秘钥对的容器。在SSL代理
Profile配置模式下，使用如下命令，指定对应的信任域：
ssl-offload server-trust-domain trust-domain-name
l
trust-domain-name – 指定系统中对应的PKI信任域名称。
使用该命令no ssl-offload server-trust-domain命令取消指定的信任域。
指定Web服务器的HTTP端口
指定设备所代理得Web服务器的HTTP服务的端口号。在SSL代理Profile配置模式下，使用如下命令，指定
端口号：
server-port port
l
port – 指定Web服务器的HTTP服务的端口号。取值范围1-65535。“服务器流量检查-卸载模式”下，
默认端口号为80，“服务器流量检查-代理模式”下，默认端口号为443。
使用该命令no server-port命令取消指定的端口号。
配置描述信息
为SSL代理Profile添加描述信息，在SSL代理Profile配置模式下，使用如下命令：
description description
l
description – 输入描述信息。
使用no description删除描述信息。
绑定SSL代理Profile到策略规则
将SSL代理Profile绑定到策略规则后，系统将会对与策略规则相匹配的流量根据Profile配置进行处理。绑定
SSL代理Profile到策略规则，需要在策略规则配置模式下进行。
进入策略规则配置模式需要进行两步配置。首先，在全局配置模式下，输入以下命令进入策略配置模式：
policy-global
然后，在策略配置模式下，输入以下命令进入策略规则配置模式：
rule [id id-number]
进入策略规则配置模式后，输入以下命令将SSL代理Profile绑定到策略规则

<!-- 来源页 2486 -->
sslproxy profile-name
l
profile-name - 指定所需要绑定的SSL代理Profile名称。
绑定配置完成后，需要修改策略规则的优先级，确保流量优先匹配此策略规则，然后可以继续指定策略规则
的用户、目的安全域和时间表参数，并能禁用或者启用该条策略规则。具体配置命令请参阅“安全策略”。

<!-- 来源页 2487 -->
配置SSL代理过滤规则
在用户开启SSL代理功能后，如果代理的HTTPS流量出现异常问题，为了便于用户定位异常问题，系统支持
配置SSL代理过滤规则，过滤指定地址或指定网段内被代理的HTTPS流量信息。
添加SSL代理过滤规则
添加SSL代理过滤规则，在任意模式下，使用以下命令：
exec sslproxy-filter add {src-ip {ipv4-address|ipv4-address/Mask} [dst-ip ipv4-address] |
src-ipv6 {ipv6-address | ipv6-address/Mask} [dst-ipv6 ipv6-address] } [dst-port portnumber]
l
src-ip {ipv4-address | ipv4-address/Mask} [dst-ip ipv4-address] - 指定需要过滤代理HTTPS
流量的源IPv4地址和目的IPv4地址。
l
src-ipv6 {ipv6-address | ipv6-address/Mask} [ dst-ipv6 ipv6-address ] - 指定需要过滤代理
HTTPS流量的源IPv6地址和目的IPv6地址。
l
[dst-port port-number] - 指定需要过滤代理HTTPS流量的目的端口号。
删除SSL代理过滤规则
删除SSL代理过滤规则，在任意模式下，使用以下命令：
exec sslproxy-filter del
显示SSL代理过滤规则信息
在任何模式下，输入以下命令查看SSL代理过滤规则信息：
show sslproxy filter

<!-- 来源页 2488 -->
配置异步加速
型号说明：
l
支持：SG-6000-A系列（不含SG-6000-
A200/A200W/A200G4/A200WG4/A1600/A1800/A2200/A1800-A/A2200-A、
ASIC防火墙型号）。
l
支持：SG-6000-K系列（不含SG-6000-K2680-A/K2680-A-GM/K2580-A/K2560-
A/K2380-A/K2380-A-GM/K1280-A、ASIC防火墙型号）。
l
支持：SG-6000-X20803/X20812。
系统支持使用QAT引擎为SSL Proxy进行异步加速。配置当前加速引擎给IPSec或SSL Proxy使用，在全局
配置模式下使用以下命令：
crypto-engine {ipsec |sslproxy}
l
ipsec - 配置QAT引擎为IPSec进行异步加速。
l
sslproxy- 配置QAT引擎为SSL Proxy进行异步加速。
注意: 配置完成后，需重启才能生效。
查看QAT引擎当前状态，在任何模式下使用以下命令：
show sslproxy qat-engine status
查看当前使用QAT引擎的模块，在任何模式下使用以下命令：
show crypto-engine
查看QAT引擎当前请求/响应计数，在任何模式下使用以下命令：
show sslproxy qat-engine counter
查看SSL Proxy异步功能相关计数，在任何模式下使用以下命令：
show sslproxy async statistic

<!-- 来源页 2489 -->
配置域名白名单
对于不需要或无法进行SSL代理的网站，可以将其加入域名白名单。系统提供预定义域名白名单，用于保存
目前无法进行SSL代理的站点，例如需要进行客户端证书认证或网站证书固定的情况。用户也可以根据需要
将站点加入网站白名单。预定义的域名白名单条目不允许进行编辑和删除。
注意: 系统共用根VSYS下的域名白名单，且该白名单仅供SSL代理模块使用。
配置自定义域名白名单
用户出于业务、隐私或其他自愿原因选择不解密指定站点时，可以将该站点加入域名白名单，设备将不会对
白名单内的网站进行SSL代理。新建自定义域名白名单，在全局配置模式下，使用以下命令：
sslproxy exempt-domain domain-name description reason {enable | disable}
l
domain-name– 指定自定义域名白名单的域名。取值范围为1-63个字符。域名注意区分大小写。支持
含有通配符“*”的域名，但仅支持一个通配符且必须在域名的起始位置，如
“*.hillstonenet.com”。
l
reason–添加自定义域名白名单的描述信息。
l
enable–启用该自定义域名白名单条目。
l
disable–禁用该自定义域名白名单条目。
使用no sslproxy exempt-domain domain-name删除自定义域名白名单。

<!-- 来源页 2490 -->
配置IP白名单
配置IP白名单后，系统不会对IP白名单中的流量进行SSL代理，对于不需要或无法进行SSL代理的流量，可以
将其加入IP白名单。IP白名单列表中包括动态IP白名单和静态IP白名单。
注意: 系统共用根VSYS下的IP白名单，且该白名单仅供SSL代理模块使用。
配置静态IP白名单
系统不会对IP白名单中的流量进行SSL代理，用户可以根据需要自定义静态IP白名单，静态IP白名单永不过
期。新建静态IP白名单，在全局配置模式下，使用以下命令：
sslproxy exempt-ip {ipv4 | ipv6} address port port_id
l
ipv4 | ipv6–指定静态IP白名单条目的IP类型为IPv4或IPv6。
l
address–配置静态IP白名单条目的IP地址。
l
port port_id–配置静态IP白名单条目的TCP端口。
使用no sslproxy exempt-ip {ipv4 | ipv6} address port port_id删除静态IP白名单。
配置动态IP白名单的老化时间
当设备作为客户端一侧的网关时，出现系统无法对流量进行代理的情况且SSL Profile中配置了放行动作时，
系统会自动将该流量的IP地址加入动态IP白名单中，后续不会再对IP白名单列表中的流量进行SSL代理。详
细配置，请参阅配置SSL代理Profile。由于设备无法代理而被加入动态IP白名单的流量超过有效时长后会被
重新代理，配置动态IP白名单的有效时长可以自动删除当前存在的动态IP白名单。通过配置动态IP白名单的
老化时间，可以自动将这些动态IP白名单条目删除。配置老化时间，在全局配置模式下，使用以下命令：
sslproxy exempt-ip timeout num
l
num–配置动态IP白名单的老化时间，单位为天。取值范围为1至30天，默认为15天。
注意: 修改SSL Profile中的策略或修改动态IP的有效时长后，系统会删除当前列表中的动态IP白名
单条目。
清除IP白名单
清除全部IP白名单，在全局配置模式下，使用以下命令：
clear sslproxy exempt-ip

<!-- 来源页 2491 -->
注意: 不同平台支持IP白名单总数不同，当存在的IP白名单数目超过限制个数时，系统会生成事件
日志提醒用户清理。

<!-- 来源页 2492 -->
显示SSL代理信息
查看IP白名单信息
用户可以查看SSL代理的IP白名单信息，包括客户端IP地址、服务端IP地址、端口号、创建时间、老化时间
以及加入原因。
查看IP白名单信息，在任意模式下，使用以下命令：
show sslproxy [slot slot-number] exempt-ip [reason reason-name | server-ip {ipv4 | ipv6} ipaddress | server-port port-number]
l
slot slot-number - 查看指定槽位的IP白名单条目信息。（仅
K20803/K9180/K7680/K7280/K6680/K6580以及X系列设备支持slot参数）
l
reason-name - 查看指定加入原因的IP白名单条目信息。
l
ipv4 | ipv6 - 查看IPv4类型或IPv6类型的IP白名单条目信息。
l
ip-address - 查看指定服务端IP地址的IP白名单条目信息。
l
port-number - 查看指定端口号的IP白名单条目信息。
以下是返回结果示例：
hostname(config)# show sslproxy slot slot4 exempt-ip
Total: 1
=====================================================================
===========
CLIENT_IP : ------
SERVER_IP : 200.1.1.246
SERVRT_PORT : 443
INSERT_TIME : 2025-11-25 09:33:40
EXPIRED_TIME: never expire
REASON : Manual
=====================================================================
===========
查看域名白名单信息
用户可以查看SSL代理的域名白名单信息，包括域名白名单总数、域名、类型、描述以及启用状态。
查看域名白名单信息，在任意模式下，使用以下命令：
show sslproxy [slot slot-number] exempt-domain

<!-- 来源页 2493 -->
l
slot slot-number - 查看指定槽位的域名白名单条目信息。（仅
K20803/K9180/K7680/K7280/K6680/K6580以及X系列设备支持slot参数）
以下是返回结果示例：
hostname(config)# show sslproxy slot slot4 exempt-domain
Total: 175
=====================================================================
===========
host_name type reason enable
---------------------------------------------------------------------
-----------
abc manual test 0
*.acompli.net predefined outlook-web-online:pinned-cert 1
*.agent.datadog.com predefined datadog:client-cert-auth 1
查看SSL代理信息
用户可以查看SSL代理信息，包括代理模式、成功代理过证书的累积值、代理的Session的累计值、PKI信任
域信息、bypass的Session数、丢弃的新建Session数、实时代理的HTTPS流量值、证书验证失败的次数
等。
查看SSL代理信息，在任意模式下，使用以下命令：
show sslproxy [slot slot-number] state
l
slot slot-number - 查看指定槽位的SSL代理信息。（仅
K20803/K9180/K7680/K7280/K6680/K6580以及X系列设备支持slot参数）
查看SSL Profile信息
用户可以查看SSL Profile信息，包括工作模式，绑定的策略规则，检查条件的设置、警告提示开关、URL白
名单等。
查看SSL Profile信息，在任意模式下，使用以下命令：
show sslproxy-profile [profile-name]
l
profile-name - 指定需要查看的SSL Profile的名称。
查看TCP代理的会话信息
查看TCP代理的会话信息，在任意模式下，使用以下命令：
show tcpproxy [slot slot-number] session-id id

<!-- 来源页 2494 -->
l
slot slot-number - 查看指定槽位的会话信息。（仅K20803/K9180/K7680/K7280/K6680/K6580
以及X系列设备支持slot参数）
l
id - 查看指定ID的会话信息。
