# VPN

> 来源: StoneOS-命令行手册-全系列-V5.5R12F2.pdf
> 覆盖章节: 12  VPN
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 1393 -->
12 VPN
系统支持如下VPN功能：
l "IPSec VPN" 在第1392页：IPSec是IETF制定的三层隧道加密协议，它为互联网上传输的数据提供了高质量的、
基于密码学的安全保证，是一种传统的实现三层VPN的安全技术。IPSec通过在特定通信方之间（例如两个安全
设备之间）建立“通道”，来保护通信方之间传输的用户数据，该通道通常称为IPSec隧道。
l "SSL VPN" 在第1490页：SSL VPN是以HTTPS为基础的VPN技术，充分利用了SSL协议提供的基于证书的身份认
证、数据加密和消息完整性验证机制，可以为通信建立安全连接。
l "L2TP VPN" 在第1703页：L2TP是VPDN（Virtual Private Dial-up Network，虚拟私有拨号网）隧道协议的一
种。VPDN是指利用公共网络的拨号功能接入公共网络，实现虚拟专用网，从而为企业、小型ISP、移动办公人员
等提供接入服务。即，VPDN为远端用户与私有企业网之间提供了一种经济而有效的点到点连接方式。
l "GRE VPN" 在第1693页：GRE（Generic Routing Encapsulation）是通用封装路由，是定义了在任意一种网络
层协议上封装任意一个其它网络层协议的协议。系统支持GRE over IPSec功能，实现路由协议信息的安全传输。
l "拨号VPN配置" 在第1653页：拨号VPN指在中心设备上仅配置一个VPN隧道，之后允许多个远程拨号端通过
VPN隧道访问中心设备。远程拨号端需配置与中心设备VPN隧道对应的IKE VPN，进行数据保护。同时，中心设
备通过预共享密钥或者证书认证方式，认证拨号端的身份，从而建立与拨号端的VPN隧道。（仅支持CLI方式配
置）
l "PnPVPN" 在第1677页：提供了一种简单易用的VPN技术——PnPVPN，即插即用VPN。
l "VXLAN" 在第1737页：VXLAN是采用MAC in UDP（User Datagram Protocol）封装方式，是NVO3
（Network Virtualization over Layer3）中的一种大二层虚拟网络扩展的隧道封装技术。VXLAN引入了类似
VLAN ID的用户标识，称为VXLAN网络标识VNI（VXLAN Network ID），由24比特组成，可划分多达16M的
VXLAN段，从而满足了大量的用户标识。通过VXLAN构建大二层网络，保证了在虚拟迁移时虚拟机的IP地址、
MAC地址等参数保持不变。

<!-- 来源页 1394 -->
IPSec VPN
本章节包含以下内容：
l "IPSec协议介绍" 在第1392页
l "IPSec VPN基础概念" 在第1393页
l "IPSec VPN的使用场景" 在第1397页
l "IPSec VPN的应用" 在第1400页
在CLI配置中包含以下内容：
l "配置IPSec VPN功能" 在第1400页
l "配置IKEv1 VPN" 在第1407页
l "配置IKEv2 VPN" 在第1430页
l "手工密钥VPN" 在第1404页
l "配置XAUTH" 在第1447页
l "配置非根VSYS隧道配额" 在第1452页
l "显示IPSec配置信息" 在第1454页
l "IPSec VPN配置举例" 在第1457页
l "例：HA Peer模式支持IPsec VPN配置举例" 在第1481页
l "例：IKE VPN配置举例" 在第1461页
l "例：手工密钥VPN配置举例" 在第1457页
l "例：基于策略的VPN监控及冗余备份功能配置举例" 在第1474页
l "例：基于路由的VPN监控及冗余备份功能配置举例" 在第1467页
l "例：XAUTH配置举例" 在第1486页
IPSec协议介绍
IPSec是为实现VPN功能而最普遍使用的协议。IPSec不是一个单独的协议，它给出了应用于IP层上网络数据
安全的一整套体系结构。该体系结构包括认证头协议（Authentication Header，简称为AH）、封装安全
负载协议（Encapsulating Security Payload，简称为ESP）、密钥管理协议（Internet Key
Exchange，简称为IKE）和用于网络认证及加密的一些算法等。IPSec规定了如何在对等体之间选择安全协
议、确定安全算法和密钥交换，向上提供了访问控制、数据源认证、数据加密等网络安全服务。

<!-- 来源页 1395 -->
l 认证头协议（AH）：IPsec体系结构中的一种主要协议，它为IP数据包提供无连接完整性的保护与数据源认证，
并提供保护以避免重播情况。AH尽可能为IP头和上层协议数据提供足够多的认证。
l IPsec封装安全负载（ESP）：IPsec 体系结构中的一种主要协议。ESP加密需要保护的数据并且在IPsec ESP的数
据部分进行数据的完整性校验，以此来保证机密性和完整性。ESP 提供了与AH相同的安全服务并提供了一种保
密性（加密）服务，ESP与AH各自提供的认证根本区别在于它们的覆盖范围。
l 密钥管理协议（IKE）：用于协商AH和ESP所使用的密码算法，并将算法所需的必备密钥放到恰当位置。
注意: IPSec VPN支持使用国家商用密码算法配置。详细的国密算法标准，请参阅国家密码管理局
颁发的《IPSec VPN技术规范》。
IPSec VPN基础概念
l 安全联盟
l 封装方式
l 协商方式
l 验证算法
l 加密算法
l 压缩算法
l 相关资料
安全联盟（Security Association）
IPSec在两个端点之间提供安全通信，两个端点被称为IPSec ISAKMP网关。安全联盟（Security
Association, 简称为SA）是IPSec的基础，也是IPSec的本质。SA是通信对等体间对某些要素的约定，例
如使用哪种协议、协议的操作模式、加密算法（DES、3DES、AES-128、AES-192和AES-256）、特定流
中保护数据的共享密钥以及SA的生存周期等。
安全联盟是单向的，在两个对等体之间的双向通信，最少需要两个安全联盟来分别对两个方向的数据流进行
安全保护。
SA建立方式
建立安全联盟的方式有两种，一种是手工方式（Manual），一种是IKE自动协商（ISAKMP）方式。
手工方式配置比较复杂，创建安全联盟所需的全部信息都必须手工配置，而且IPSec的一些高级特性（例如
定时更新密钥）不能被支持，但优点是可以不依赖IKE而单独实现IPSec功能。该方式适用于当与之进行通信
的对等体设备数量较少的情况，或是IP地址相对固定的环境中。

<!-- 来源页 1396 -->
IKE自动协商方式相对比较简单，只需要配置好IKE协商安全策略的信息，由IKE自动协商来创建和维护安全
联盟。该方式适用于中、大型的动态网络环境中。该方式建立SA的过程分两个阶段。第一阶段，协商创建一
个通信信道（ISAKMP SA），并对该信道进行认证，为双方进一步的IKE通信提供机密性、数据完整性以及
数据源认证服务；第二阶段，使用已建立的ISAKMP SA建立IPsec SA。分两个阶段来完成这些服务有助于
提高密钥交换的速度。
第一阶段SA
第一阶段SA为建立信道而进行的安全联盟。第一阶段协商的步骤是：
1. 参数配置。包括：
l 认证方法：选择预共享密钥或数字证书认证
l Diffie-Hellman组的选择
2. 策略协商。包括：
l 加密算法：选择DES、3DES、AES-128、AES-192或AES-256
l hash算法：选择MD5、SHA-1或SHA-2
3. DH交换。虽然名为“密钥交换”，但事实上在任何时候，两台通信主机之间都不会交换真正的密钥，它们之间
交换的只是一些DH算法生成共享密钥所需要的基本材料信息。DH交换，可以是公开的，也可以受保护。在彼此
交换过密钥生成“材料”后，两端主机可以各自生成出完全一样的共享“主密钥”，保护紧接其后的认证过程。
4. 认证。DH交换需要得到进一步认证，如果认证不成功，通信将无法继续下去。“主密钥”结合在第一步中确定
的协商算法，对通信实体和通信信道进行认证。在这一步中，整个待认证的实体载荷，包括实体类型、端口号和
协议，均由前一步生成的“主密钥”提供机密性和完整性保证。
第二阶段SA
第二阶段SA为快速SA，为数据传输而建立的安全联盟。这一阶段协商建立IPsec SA，为数据交换提供
IPSec服务。第二阶段协商消息受第一阶段SA保护，任何没有第一阶段SA保护的消息将被拒收。第二阶段协
商（快速模式协商）步骤是：
1. 策略协商，双方交换保护需求：
l 使用哪种IPSec协议：AH或ESP
l 是否使用hash算法：MD5、SHA-1、SHA-2或NULL
l 是否要求加密，若是，选择加密算法：DES或3DES、AES-128、NULL、AES-192或AES-256
l 是否使用压缩算法：DEFLATE
l 在上述四方面达成一致后，将建立起两个SA，分别用于入站和出站通信。

<!-- 来源页 1397 -->
2. 会话密钥“材料”刷新或交换。
在这一步中，将通过DH交换生成加密IP数据包的“会话密钥”。
3. 将SA递交给IPSec驱动程序。
在第二阶段协商过程中，如果响应超时，则自动尝试重新进行第二阶段SA协商。
封装方式
IPSec有如下两种工作模式：
l 隧道（tunnel）模式：用户的整个IP数据包被用来计算AH或ESP头，AH或ESP头以及ESP加密的用户数据被封装
在一个新的IP数据包中。通常，隧道模式应用在两台设备之间的通讯。
l 传输（transport）模式：只是传输层数据被用来计算AH或ESP头，AH或ESP头以及ESP加密的用户数据被放置
在原IP包头后面。通常，传输模式应用在两台主机之间的通讯，或一台主机和一台设备之间的通讯。
协商方式
手工方式配置比较复杂，创建安全联盟所需的全部信息都必须手工配置，而且IPSec的一些高级特性（例如
定时更新密钥）不能被支持，但优点是可以不依赖IKE而单独实现IPSec功能。该方式适用于当与之进行通信
的对等体设备数量较少的情况，或是IP地址相对固定的环境中。
IKE自动协商方式相对比较简单，只需要配置好IKE协商安全策略的信息，由IKE自动协商来创建和维护安全
联盟。该方式适用于中、大型的动态网络环境中。该方式建立SA的过程分两个阶段。第一阶段，协商创建一
个通信信道（ISAKMP SA），并对该信道进行认证，为双方进一步的IKE通信提供机密性、数据完整性以及
数据源认证服务；第二阶段，使用已建立的ISAKMP SA建立IPSec SA。分两个阶段来完成这些服务有助于
提高密钥交换的速度。
验证算法
AH和ESP都能够对IP报文的完整性进行验证，以判别报文在传输过程中是否被篡改。验证算法的实现主要是
通过杂凑函数。杂凑函数是一种能够接受任意长的消息输入，并产生固定长度输出的算法，该输出称为消息
摘要。IPSec对等体计算摘要，如果两个摘要是相同的，则表示报文是完整未经篡改的。一般来说IPSec使用
下列验证算法：
l MD5：MD5输入任意长度的消息，产生128bit的消息摘要。
l SHA-1：SHA-1输入长度小于2的64次方比特的消息，产生160bit的消息摘要。SHA-1的摘要长于MD5，因而是
更安全的。
l SHA-2：SHA-2一般包含SHA-256、SHA-384和SHA-512三种杂凑函数，能将输入消息对应到更长的消息摘
要。SHA-256输入长度小于2的64次方比特的消息，产生256bit的消息摘要；SHA-384输入长度小于2的128次

<!-- 来源页 1398 -->
方比特的消息，产生384bit的消息摘要；SHA-512输入长度小于2的128次方比特的消息，产生512bit的消息摘
要。
l SM3：SM3输入长度小于2的64次方比特的消息，产生256bit的消息摘要。
加密算法
ESP能够对IP报文内容进行加密保护，防止报文内容在传输过程中被窥探。加密算法实现主要通过对称密钥
系统，它使用相同的密钥对数据进行加密和解密。StoneOS实现了五种加密算法：
l DES（Data Encryption Standard）：使用56bit的密钥对每个64bit的明文块进行加密。
l 3DES（Triple DES）：使用三个56bit的DES密钥（共168bit密钥）对明文进行加密。
l AES（Advanced Encryption Standard）：StoneOS实现了128bit、192bit和256bit密钥长度的AES算法，其
加密算法安全级别由高到低的顺序为AES-256 > AES-192 > AES-128。
l SM1: 国家密码管理局编制的一种商用密码分组标准对称算法。分组长度和密钥长度都为128bit。仅国密设备支
持该算法。
l SM4: 国家密码管理局编制的一种商用密码分组标准对称算法。分组长度和密钥长度都为128bit。
在上述五种加密算法中，用户可根据业务场景，使用对应的加密算法。
l 高安全性和高性能的通用场景（如IPSec VPN、SSL VPN等）：推荐使用AES算法，其广泛应用于网络通信加
密、数据存储加密、金融交易安全等领域。AES算法具有安全性高、效率高、灵活性好的特点，支持多种密钥长
度，能够根据实际需求选择合适的密钥长度以平衡安全性和性能。
l 国内商用密码场景：推荐使用SM1或SM4算法，如政府机构、金融机构等对数据安全有高要求且需要符合国内密
码标准的场景。
提示: 由于DES和3DES算法安全性和性能不足，不推荐使用。
压缩算法
IPComp（IP Payload Compression，IP有效载荷压缩）是一个减少IP数据报长度的协议，该协议通过支
持不同的压缩算法对IP数据报的有效负载进行压缩处理，从而实现通信数据在低带宽条件下的高负载传输。
应用IPComp的关键在于通信的两个端点之间必须首先建立一个IPComp关联（IPCA），此关联中包含了
IPComp操作要求的所有信息，例如所使用的压缩算法以及所选择的压缩算法要求的参数等。使用IPComp
对IPSec处理的网络数据流进行压缩时，用户可以手工配置创建IPCA，也可以通过动态协商创建IPCA。当使
用动态协商方式时，ISAKMP网关提供建立IPCA必须的机制。Hillstone设备的IPSec功能提供以下IPComp
压缩算法：

<!-- 来源页 1399 -->
l DEFLATE：使用LZ77算法和Huffman译码，是一种可以在IPComp中实现的自由可用的无损耗压缩算法。
相关资料
StoneOS的IPSec功能遵循RFC中IPSec协议的规定。关于IPSec协议的更多详细信息，请参阅以下RFC文档
的相关章节：
l Security Architecture for the Internet Protocol: RFC2401/RFC4301
l ESP：RFC2406/RFC4303
l AH：RFC2402/RFC4302
l 加密算法参考：RFC2410（Null Encryption），RFC2405（DES-CBC），RFC2451（3DES-CBC）以及
RFC3602（AES-CBC）
l 验证算法参考：：FIPS180-2（SHA），RFC2404（SHA-1），RFC4868（SHA-2）以及RFC2403（MD5）
l 压缩算法参考：RFC2393（IPComp）以及RFC2394（DEFLATE）
IPSec VPN的使用场景
局域网之间的安全互联场景
在企业拥有多个分支机构的情况下，为了确保各分支与总部以及分支间的安全、高效数据传输和资源共享，
可以通过在各自的IPSec网关之间建立IPSec隧道，实现局域网的安全互联。
如下图所示，局域网之间的安全互联包含以下三种组网应用：
l 点到点VPN（IPSec Tunnel）：在企业分支机构与总部的两个IPSec网关之间建立IPSec隧道，确保局域网之间能
够安全地互相访问。

<!-- 来源页 1400 -->
l 点到点VPN（GRE over IPSec Tunnel）：GRE over IPSec Tunnel结合了GRE和IPSec的优势，利用GRE（通用
封装路由）将组播、广播和非IP报文封装成IP报文，再通过IPsec提供安全通信。当需要在IPSec VPN上传输组
播、广播和非IP报文时，如在总部与分支之间开视频会议等组播业务，可以在各自的IPSec网关之间建立GRE
over IPSec隧道，以此实现局域网之间的安全互联。
远程用户安全接入场景
远程接入是指出差员工或合作伙伴在非固定办公场所下，通过公共网络接入企业核心网络并访问内部资源的
需求场景。远程用户虽可通过L2TP协议实现对企业总部资源的远程接入，但由于L2TP协议本身不具备加密
机制，存在数据泄露风险。基于此，可部署L2TP over IPSec VPN，在远程用户终端（PC）与企业IPSec网
关之间建立L2TP over IPSec隧道，利用IPSec的加密与认证机制，保障通信数据的安全性。
分支机构两条IPSec VPN互为主备场景
如下图所示，该场景采用冗余VPN组网结构，以增强网络的可靠性和稳定性。在总部部署两台防火墙，通过
高可用性（HA）配置实现冗余，同时连接两条运营商线路，与各分店建立IPSEC VPN连接。各分店则配置
一台带有4G模块的防火墙，通过一条PPPOE线路和一条4G移动线路与总部建立主备两条IPSEC VPN，确保
业务连续性。
此外，在总部还部署了一台安全管理平台HSM，实现对总部及分店防火墙的统一管理。该平台支持统一配置
下发、版本升级、设备信息监控、整网VPN隧道状态监控以及流量统计等功能，简化了运维管理流程。
此方案的优势在于VPN网络可靠性高，分店通过4G链路作为备份，不仅降低了投入成本，还提高了网络的稳
定性。同时，集中管理和监控机制便于运维，有效节省了维护成本。
对于规模较小、人员不多的分店，也可采用SSLVPN方式接入总部，以降低成本并提高接入的灵活性。

<!-- 来源页 1401 -->
多种VPN技术综合场景
企业总部与各分公司部署VPN设备进行IPSEC VPN互联，实现分公司与总部之间的安全互联，并使分公司能
够安全访问总部的CRM、OA、邮件、ERP、财务等关键业务系统。同时，在企业总部部署SSL VPN设备，
为远程办公人员、移动办公人员和远程运维人员提供安全的内网接入，确保他们能够安全访问办公系统及各
种IT系统的远程运维。该场景有效解决了总部与分公司的互联互通问题，保障了远程办公人员的安全访问需
求，并为远程IT运维提供了安全的访问方式。

<!-- 来源页 1402 -->
IPSec VPN的应用
设备通过“基于策略的VPN”和“基于路由的VPN”两种方式把配置好的VPN隧道调用到设备上，实现流量
的加密解密安全传输。
l 基于策略的VPN：将配置成功的VPN隧道名称引用到策略规则中，使符合条件的流量通过指定的VPN隧道进行传
输。
l 基于路由的VPN：将配置成功的VPN隧道与隧道接口绑定；配置静态路由时，将隧道接口指定为下一跳路由。
配置IPSec VPN功能
StoneOS支持两种配置IPSec VPN的方法，分别是：
l 手工密钥VPN
l IKE VPN，支持IKEv1和IKEv2两个版本。
提升IPSec VPN解密性能
该功能仅支持虚拟化产品云•界。当云•界使用的CPU数大于2个vCPU以上时，用户可以根据需要开启IPSec
VPN解密性能提升功能。开启后，系统将采用多核解密技术对数据包进行解密，IPSec VPN解密性能将提
升，同时设备的吞吐量也将增大。开启IPSec VPN解密性能提升功能，在全局配置模式下使用以下命令：
tunnel-core-unbind
在全局配置模式下，使用no tunnel-core-unbind恢复默认配置。

<!-- 来源页 1403 -->
提升IPSec VPN新建性能
用户可以根据需要配置IPSec VPN新建性能提升功能。配置该功能后，系统将采用多核多进程技术进行VPN
协商，IPSec VPN新建性能将提升。
指定系统数据层面占用CPU核的数量
型号说明：
l
不支持：SG-6000-K2680-A/K2680-A-GM/K2580-A/K2560-A/K2380-A/K2380-AGM/K1280-A
l
不支持：SG-6000-A2200-A/A1800-A
提升IPSec VPN新建性能，用户需要首先指定系统数据层面占用CPU核的数量，指定后，VPN进程数量为系
统CPU核总数减去系统数据层面占用CPU核的数量。指定系统数据层面占用CPU核的数量，在全局配置模式
下，使用以下命令：
flow-core-num number
l
number – 指定系统数据层面占用CPU核的数量。取值范围为max_core_number/2到max_core_
number，max_core_number为系统的CPU核总数。指定后，VPN进程数量的计算公式为：新增加的
VPN进程数量=max_core_number（系统CPU核总数）- flow-core-number （系统数据层面占用
CPU核的数量）。
在全局配置模式下，使用no flow-core-num取消系统数据层面占用CPU核数量的配置。
开启/关闭VPN多进程功能
默认情况下，VPN多进程功能是关闭状态，在全局配置模式下，使用以下命令开启或关闭此功能：
l
开启：cp-multi-cores vpnd
l
关闭：no cp-multi-cores vpnd
注意:
l
指定或者取消指定系统数据层面占用CPU核的数量后，需要重启设备使配置生效。
l
开启/关闭VPN多进程功能后，需要重启设备使配置生效。

<!-- 来源页 1404 -->
l
用户需要同时配置“指定系统数据层面占用CPU核的数量”和“开启VPN多进程功能”，并且
在重启设备之后，VPN多进程功能才能够被完全开启。
l
IPSec VPN新建性能提升功能适用于IKEv1 VPN、拨号VPN、PnPVPN以及XAUTH。
l
SG-6000-X8180/A1600-A/A200-A/A200G4-A/A200W-A/A200WG4-A设备及CPU核数
≤2 的设备不支持该功能。
使用两个CPU核处理SM1加密算法的IPSec VPN流量
该功能仅支持E、A系列平台的国密设备。
系统支持使用两个CPU核处理SM1加密算法的IPSec VPN流量，该功能通过优化IPSec VPN SM1流量的处
理流程提高设备的业务处理性能。系统将IPSec VPN SM1流量加入VPN隧道队列（queue），其中加密报
文会被送入加密队列，解密报文被送入解密队列，系统CPU核在获得队列访问权限后才能够进行IPSec VPN
SM1报文加解密处理。这样，同一时间下系统只需要两个CPU核进行IPSec VPN SM1加解密业务的处理，
一个用于处理加密报文，一个用于处理解密报文，其他CPU核则可以处理其他业务，从而提高系统的业务处
理性能。
用户可以在任意模式下，使用以下命令查看VPN隧道队列的统计信息：
show dp-tunnel statistics [clear]
l
show dp-tunnel statistics - 显示VPN隧道队列的统计信息。
l
clear - 清除VPN隧道队列的统计信息。
以下是显示VPN隧道队列的统计信息的命令示例：
hostname(config)# show dp-tunnel statistics
IPSec SM1 queue statistics:
Queue0:
pkts_in: 1151160（入队报文数目）
pkts_out: 1151160（出队报文数目）
pkts_drop_for_queue_full: 0（因队列满丢弃报文数目）
pkts_drop_for_session_invalid: 0（因会话无效丢弃报文数目）
max_encap_time(ms): 2（最大报文加密时间）
max_decap_time(ms): 0（最大报文解密时间）
Queue1:

<!-- 来源页 1405 -->
pkts_in: 1151160
pkts_out: 1151160
pkts_drop_for_queue_full: 0
pkts_drop_for_session_invalid: 0
max_encap_time(ms): 0
max_decap_time(ms): 2
Queue0用于处理加密流量，Queue1用于处理解密流量。
IPSec异步模式
型号说明：
l
支持：除ASIC防火墙型号外的所有SG-6000-A系列平台。
l
支持：SG-6000-X8180。
IPSec异步模式应用于集成了硬件加速卡的平台。IPSec加解密支持异步模式，通过硬件加速卡加速数据加解
密，提升IPSec吞吐性能。
启用/禁用IPSec异步模式
默认情况下，IPSec异步模式为启用状态。在全局配置模式下，使用以下命令启用或禁用该功能：
l
启用IPSec异步模式：no ipsec-async-crypto-disable
l
禁用IPSec异步模式：ipsec-async-crypto-disable
查询硬件加速卡信息
查询硬件加速卡信息及算法集，在任意模式下，使用以下命令：
show dp-dpdk-crypto-device
注意: 当硬件加速卡被其他功能（如SSL Proxy）占用时，"device status"显示为"device
status: disable(crypto is used by other module)"
查询加解密队列统计数据
查询加解密队列统计数据，在任意模式下，使用以下命令：
show ipsec-async-crypto statistic [ tunnel_id ] [clear]

<!-- 来源页 1406 -->
l
show ipsec-async-crypto statistic: 显示异步模式下，整机IPSec加解密队列的统计数据。
l
tunnel_id：指定隧道ID号。指定后，系统将显示指定隧道的IPSec加解密队列统计数据。
l
clear：回显整机或指定隧道的IPSec加解密队列统计数据，然后清除统计数据。
手工密钥VPN
手工密钥VPN的配置包括指定IPSec协议的封装模式、安全参数索引、协议类型、加密算法/验证算法和压缩
算法等。
创建手工密钥VPN
创建手工密钥VPN，在全局配置模式下，使用以下命令：
tunnel ipsec name manual
l
name – 指定所创建的手工密钥VPN隧道的名称。
执行该命令后，CLI进入到手工密钥VPN配置模式。对手工密钥VPN的所有参数配置都需要在该模式下进
行。在全局配置模式下使用以下命令删除指定的手工密钥VPN隧道：
no tunnel ipsec name manual
启用/禁用手工密钥VPN隧道的硬件快转功能
型号说明：
l
支持：SG-6000-A系列ASIC防火墙。
l
支持：SG-6000-K系列ASIC防火墙。
开启后将由专门的硬件芯片进行IPSec数据包的加密/解密，从而降低CPU负载，提升大流量场景下的转发性
能。该功能默认为开启状态。
启用/禁用手工密钥VPN隧道的硬件快转功能，在手工密钥VPN配置模式下，使用以下命令：
l
启用：hardware-fast-forward enable
l
禁用：hardware-fast-forward disable
注意: 若未开启全局硬件快转功能，则手工密钥VPN隧道的硬件快转功能将不生效。配置全局硬件
快转功能参见“防火墙> 硬件快转”章节。

<!-- 来源页 1407 -->
指定IPSec协议的封装模式
指定IPSec协议的封装模式，可以是隧道模式或者传输模式，在手工密钥VPN配置模式下使用以下命令：
mode {transport | tunnel}
l
transport – 指定IPSec协议的封装模式为传输模式。
l
tunnel – 指定IPSec协议的封装模式为隧道模式。该模式为系统默认模式。
使用no mode命令恢复默认模式。
指定安全参数索引
安全参数索引（Security Parameter Index，简称为SPI）是为唯一标识SA而生成的一个32比特的数值，
它在AH和ESP头中传输。SPI的作用是查找对应的VPN隧道进行解密。指定手工密钥VPN隧道的SPI，在手工
密钥VPN配置模式下使用以下命令：
spi spi-number out-spi-number
l
spi-number – 指定本端的SPI参数。
l
out-spi-number – 指定对端的SPI参数。
使用no spi命令取消对SPI参数的配置。
在为系统配置安全联盟时，必须分别设置进方向（inbound）和出方向（outbound）两个方向的安全联盟
的参数。并且在隧道的两端设置的安全联盟参数必须是完全匹配的。本端的入方向安全联盟的SPI必须和对
端的出方向安全联盟的SPI一样；本端的出方向安全联盟的SPI必须和对端的入方向安全联盟的SPI一样。
指定协议类型
IPSec协议的类型为ESP和AH两种。为手工密钥VPN隧道指定协议类型，在手工密钥VPN配置模式下使用以
下命令：
protocol {esp | ah}
l
esp – 指定使用ESP协议。该协议为系统默认协议。
l
ah – 指定使用AH协议。
使用no protocol恢复默认协议配置。
指定加密算法
为手工密钥VPN隧道指定加密算法，请在手工密钥VPN配置模式下使用以下命令：
encryption {3des | des | aes | aes-192 | aes-256 | null}

<!-- 来源页 1408 -->
l
3des – 指定使用3DES加密方法。密钥长度为192比特。该方法为系统默认方法。
l
des – 指定使用DES加密方法。密钥长度为64比特。
l
aes – 指定使用AES加密方法。密钥长度为128比特。
l
aes-192 – 指定使用192bit AES加密方法。密钥长度为192比特。
l
aes-256 – 指定使用256bit AES加密方法。密钥长度为256比特。
l
null – 不使用加密功能。
使用no encryption命令恢复默认加密算法。
指定验证算法
为手工密钥VPN隧道指定验证算法，请在手工密钥VPN配置模式下使用以下命令：
hash {md5 | sha | sha256 | sha384 | sha512 | null}
l
md5 – 指定使用MD5验证算法。摘要为128比特。
l
sha – 指定使用SHA-1验证算法。摘要为160比特。该算法为StoneOS的默认算法。
l
sha256 – 指定使用SHA-256验证算法。摘要为256比特。
l
sha384 – 指定使用SHA-384验证算法。摘要为384比特。
l
sha512 –指定使用SHA-512验证算法。摘要为512比特。
l
null – 不使用验证功能。
使用no hash命令恢复默认验证算法。
指定压缩算法
默认情况下，手工密钥VPN不使用任何压缩算法。为手工密钥VPN隧道指定压缩算法（DEFLATE算法），请
在手工密钥VPN配置模式下使用以下命令：
compression deflate
使用no compression命令取消对压缩算法的指定。
指定对端IP地址
配置对端的IP地址，请在手工密钥VPN配置模式下使用以下命令：
peer ip-address
l
ip-address – 指定对端的IP地址。
使用no peer命令取消对端IP地址的配置。

<!-- 来源页 1409 -->
配置协议的验证密钥
用户需要为安全隧道两端均配置协议的验证密钥，且本端入方向验证密钥必须与对端出方向的验证密钥相
同，而本端出方向的验证密钥必须与对端入方向的验证密钥相同。配置协议验证密钥，请在手工密钥VPN配
置模式下使用以下命令：
hash-key inbound hex-number-string outbound hex-number-string
l
inbound hex-number-string – 配置本端进方向的验证密钥。
l
outbound hex-number-string – 配置本端出方向的验证密钥。
使用no hash-key命令取消对验证密钥的配置。
配置协议的加密密钥
用户需要为安全隧道两端均配置协议的加密密钥，且本端入方向加密密钥必须与对端出方向的加密密钥相
同，而本端出方向的加密密钥必须与对端入方向的加密密钥相同。配置协议加密密钥，请在手工密钥VPN配
置模式下使用以下命令：
encryption-key inbound hex-number-string outbound hex-number-string
l
inbound hex-number-string – 配置本端进方向的加密密钥。
l
outbound hex-number-string – 配置本端出方向的加密密钥。
使用no encryption-key命令取消对加密密钥的配置。
指定出接口
为手工密钥VPN隧道指定出接口，请在手工密钥VPN配置模式下使用以下命令：
l
interface interface-name
l
interface-name – 指定出接口名称。
使用no interface命令取消对出接口的指定。
注意: 非根VSYS中的出接口不可以为VSYS共享接口。
配置IKEv1 VPN
IKEv1 VPN的配置包括：
l 配置P1提议
l 配置ISAKMP网关

<!-- 来源页 1410 -->
l 配置P2提议
l 配置智能选路
l 配置隧道
配置P1提议
P1提议是IKE安全提议，可应用到ISAKMP网关上，在SA第一阶段使用。对IKE安全提议的配置包括指定认证
方式、加密算法、验证算法、DH组和安全联盟的生命周期。
创建P1提议
创建一个P1提议，即IKE安全提议，请在全局配置模式下使用以下命令：
isakmp proposal p1-name
l
p1-name – 指定所创建的P1提议的名称。执行该命令后，CLI进入到P1提议配置模式。用户可以在该模
式下对P1提议进行参数配置。
使用no isakmp proposal p1-name命令删除指定的P1提议。
指定认证方式
此处指定的是IKE身份认证的方式。身份认证用来确认通信双方的身份。方式有预共享密钥认证、数字证书
认证和国密数据信封认证。对于预共享密钥认证方式，认证字用来作为一个输入产生密钥，认证字不同是不
可能在双方产生相同的密钥的。指定IKE安全提议的身份认证方式，在P1提议配置模式下使用以下命令：
authentication {pre-share | rsa-sig | dsa-sig |ecdsa-sig | gm-de }
l
pre-share – 指定使用预共享密钥认证方式。该方式为默认认证方式。
l
rsa-sig – 指定使用RSA数字证书认证方式。
l
dsa-sig – 指定使用DSA数字证书认证方式。此方式对应的验证算法只能为SHA-1。
l
ecdsa-sig – 指定使用ECDSA数字证书认证方式。此方式对应的验证算法只能为SHA-256、SHA-384
和SHA-512，加密算法不支持SM1和SM4。
l
gm-de – 指定使用国密数字信封认证方式。当认证方式为此选项时，加密算法仅支持使用SM1和SM4，
验证算法仅支持使用SHA或SM3。
使用no authentication命令恢复默认认证方式。
指定加密算法
指定IKE安全提议的加密算法，在P1提议配置模式下使用以下命令：

<!-- 来源页 1411 -->
encryption {3des | des | aes | aes-192 | aes-256 | sm1 | sm4}
l
3des – 指定使用3DES加密方法。密钥长度为192比特。该方法为StoneOS系统默认方法。
l
des – 指定使用DES加密方法。密钥长度为64比特。
l
aes – 指定使用AES加密方法。密钥长度为128比特。
l
aes-192 – 指定使用192bit AES加密方法。密钥长度为192比特。
l
aes-256 – 指定使用256bit AES加密方法。密钥长度为256比特。
l
sm1 – 指定使用国家商用密码SM1分组密码算法。密钥长度为128比特。
l
sm4 – 指定使用国家商用密码SM4分组密码算法。密钥长度为128比特。
使用no encryption命令恢复默认加密算法。
指定验证算法
指定IKE安全提议的验证算法，在P1提议模式下使用以下命令：
hash {md5 | sha | sha256 | sha384 | sha512 | sm3}
l
md5 – 指定使用MD5验证算法。摘要为128比特。
l
sha – 指定使用SHA-1验证算法。摘要为160比特。该算法为StoneOS的默认算法。
l
sha256 – 指定使用SHA-256验证算法。摘要为256比特。
l
sha384 – 指定使用SHA-384验证算法。摘要为384比特。
l
sha512 – 指定使用SHA-512验证算法。摘要为512比特。
l
sm3 – 指定使用国密SM3验证算法。摘要为256比特。该算法用于密码应用中的数字签名和验证、消息
认证码的生成与验证，可满足多种密码应用的安全需求。
使用no hash命令恢复默认认证方式。
选择DH组
Diffie-Hellman（DH）是一种建立密钥的方法。DH组决定DH交换中密钥生成“材料”的长度。密钥的牢
固性部分决定于DH组的强度。密钥“材料”长度越长，所生成的密钥安全度也就越高，越难被破译。DH组
的选择很重要，因为DH组只在第一阶段的SA协商中确定，第二阶段的协商不再重新选择DH组，两个阶段使
用的是同一个DH组，因此该DH组的选择将影响所有会话密钥的生成。在协商过程中，两个ISAKMP网关间
应选择同一个DH组，即密钥“材料”长度应该相等。若DH组不匹配，将协商失败。
在P1提议选择DH组，在P1提议配置模式下使用以下命令：
group {1 | 2 | 5 | 14 | 15 |16 | 18 | 19 | 20 | 21 | 24}

<!-- 来源页 1412 -->
l
1 – 选择DH组1。密钥的长度为768比特（MODP Group）。
l
2 – 选择DH组2。密钥的长度为1024比特（MODP Group）。2为系统默认值。
l
5 – 选择DH组5。密钥的长度为1536比特（MODP Group）。
l
14 – 选择DH组14。密钥的长度为2048比特（MODP Group）。
l
15 – 选择DH组15。密钥的长度为3072比特（MODP Group）。
l
16 – 选择DH组16。密钥的长度为4096比特（MODP Group）。
l
18 – 选择DH组18。密钥的长度为8192比特（MODP Group）。
l
19 – 选择DH组19。密钥的长度为256比特（ECP Group）。
l
20 – 选择DH组20。密钥的长度为384比特（ECP Group）。
l
21 – 选择DH组21。密钥的长度为521比特（ECP Group）。
l
24 – 选择DH组24。密钥的长度为2048比特（MODP Group with 256-bit Prime Order
Subgroup）。
使用no group命令取消恢复默认DH组。
在P2提议中配置PFS时，也可选用如上DH组。
指定安全联盟的生命周期
第一阶段SA有一个默认的生命周期，如果ISAKMP SA生命期时间到，要向对方发送第一阶段SA删除消息，
通知对方第一阶段SA已经过期。之后需要重新进行SA协商。指定安全联盟的生命周期，在P1提议配置模式
下使用以下命令：
lifetime time-value
l
time-value – 指定SA第一阶段的生命周期长度，单位为秒。默认86400秒。范围是300到86400秒。
使用no lifetime命令恢复默认生命周期长度。
配置ISAKMP网关
创建一个ISAKMP网关后，用户可以配置ISAKMP网关的IKE协商模式、ISAKMP网关IP地址及类型、IKE安全
提议、预共享密钥、PKI信任域、本地ID、ISAKMP网关ID 、ISAKMP网关连接方式以及是否开启ISAKMP网
关的NAT穿越功能等。
创建ISAKMP网关
创建ISAKMP网关，在全局配置模式下，使用以下命令:
isakmp peer peer-name

<!-- 来源页 1413 -->
l
peer-name – 指定ISAKMP网关的名称。
执行该命令后，CLI进入到ISAKMP网关配置模式。用户可以在该模式下对ISAKMP网关进行参数配置。
在全局配置模式下使用no isakmp peer peer-name命令删除指定的ISAKMP网关。
绑定接口到ISAKMP网关
用户可以绑定某个接口到ISAKMP网关。将接口绑定到ISAKMP网关，在ISAKMP网关配置模式下使用以下命
令：
interface interface-name
l
interface-name – 指定被绑定接口的名称。
使用no interface interface-name命令取消接口绑定。
配置IKE协商模式
IKE的协商模式有两种：主模式（main mode）和野蛮模式（aggressive mode）。IKE野蛮模式不提供
身份保护，以下情况只能用野蛮模式：中心设备的IP地址为固定分配的地址，而客户端设备的IP地址为动态
获取的地址。配置IKE协商模式，在ISAKMP网关配置模式下使用以下命令：
mode {main | aggressive}
l
main – 指定使用主模式，可提供ID保护功能。该模式为系统的默认模式。
l
aggressive – 指定使用野蛮模式。
使用no mode命令恢复默认协商模式。
配置IKE协商协议
默认情况下，IPSec VPN使用UDP协议进行IKE协商，当遇到运营商封堵UDP协议时，会造成IPsec隧道建立
失败，导致用户无法通过IPSec VPN来进行资源访问。因此，系统支持使用TCP协议进行IKE协商，并且能够
根据协商状态自动切换协议，从而缓解由运营商封堵端口和协议带来的VPN网络问题。
注意:
l
协商协议不适用于传输模式、AH协议、IPv6、VSYS、IKEv2 VPN。
l
IKE协商采用的协议类型是由发起端控制的。系统作为响应端时，本端配置的协商协议将不会生
效。
配置IKE协商协议，在ISAKMP网关配置模式下，使用以下命令：

<!-- 来源页 1414 -->
negotiate-transport-protocol {udp | tcp | auto}
l
udp - 指定使用UDP协议进行IKE协商。默认为UDP协议。
l
tcp - 指定使用TCP协议进行IKE协商。
l
auto - 指定自动切换协商协议，系统将按照以下顺序进行轮询协商：
l
当发起端指定auto，并且VPN两端配置了UDP和TCP自定义端口时，系统将按照“TCP协议+TCP
自定义端口”、“TCP协议+TCP500端口”、“UDP协议+UDP自定义端口”、“UDP协议
+UDP500端口”的顺序轮流进行协商。如果“TCP协议+TCP自定义端口”协商失败，则自动切换
到“TCP协议+TCP500端口”进行协商，以此类推进行轮询协商。配置自定义端口参见配置自定
义IKE协商端口章节。
l
当发起端指定auto，并且VPN两端没有配置UDP和TCP自定义端口时，系统将按照“TCP协议
+TCP500端口”、“UDP协议+UDP500端口”的顺序进行轮询协商。
取消配置IKE协商协议后，系统将默认使用UDP协议进行IKE协商。取消配置IKE协商协议，在ISAKMP网关
配置模式下，使用以下命令：
no negotiate-transport-protocol
配置自定义IKE协商端口
用户可以自定义UDP端口和TCP端口进行IKE协商，并且建立IPSec连接。
配置UDP自定义协商端口，在ISAKMP网关配置模式下使用以下命令：
ipsec-over-udp port port-number
l
port-number – 指定UDP端口号。取值范围是1到65535，建议使用1024到65535之间的端口号。
使用no ipsec-over-udp命令取消自定义的UDP端口配置。
配置TCP自定义协商端口，在ISAKMP网关配置模式下使用以下命令：
ipsec-over-tcp port port-number
l
port-number – 指定TCP端口号。取值范围是1到65535。
使用no ipsec-over-tcp命令取消自定义的TCP端口配置。

<!-- 来源页 1415 -->
注意:
l
当使用TCP协议并且使用TCP自定义端口进行协商时，VPN两端必须配置相同的TCP端口才能协
商成功。
l
系统最多支持配置16个TCP自定义端口。
配置自定义IKE协商端口池
用户可以置自定义IKE协商端口池，当VPN通过端口500或者4500协商，首包协商超时失败时，系统可以使
用自定义端口池中的端口进行IKE协商，并建立IPSec连接。
配置自定义IKE协商端口池，需要在IKE端口池配置模式下进行。在全局配置模式下，使用以下命令进入IKE
端口池配置模式：
ike-port-pool
在全局配置模式下，使用no ike-port-pool删除自定义IKE协商端口池。
在IKE端口池配置模式下，使用以下命令配置自定义IKE协商端口池中的端口范围：
port-range min min_port max max_port
l
min min_port max max_port– 指定端口范围的最小值端口号和最大端口号，取值范围均为1024
到65535。
多次执行以上命令配置多个端口范围。系统最多允许配置120个端口范围。
在IKE端口池配置模式下，使用no port-range min min_port max max_port删除端口范围。
注意:
l
自定义IKE协商端口池配置完成后，需要绑定到ISAKMP网关，VPN才可以使用端口池中的端口
进行IKE协商。关于如何绑定自定义IKE协商端口池，请参阅绑定自定义IKE协商端口池。
l
配置自定义IKE协商端口池功能后，建议同时配置DPD功能或者VPN监控功能，如果发现500或
者4500端口被禁用，系统会断开原VPN连接，继续使用500或者4500端口发起协商，首包协
商超时失败时，会从自定义IKE协商端口池获取端口进行IKE协商。
l
如果已经协商成功的VPN端口被禁用，从断开原VPN连接到更换自定义端口重新协商之间，
VPN连接至少会有1分钟的时间处于断开状态。
l
建议单独配置使用自定义IKE协商端口功能和自定义IKE协商端口池功能。

<!-- 来源页 1416 -->
绑定自定义IKE协商端口池
自定义IKE协商端口池绑定到ISAKMP网关后，VPN才可以使用端口池中的端口进行IKE协商。
绑定自定义IKE协商端口池，在ISAKMP网关配置模式下使用以下命令：
bind ike-port-pool
在ISAKMP网关配置模式下，使用no bind ike-port-pool解除自定义IKE协商端口池绑定。
指定对端的IP地址及类型
用户可以为所创建的ISAKMP网关指定对端的IP地址和IP地址的类型（静态或者动态）。指定对端的IP地
址，请在ISAKMP网关配置模式下使用以下命令：
type {dynamic | static}
l
dynamic – 指定对端的IP地址为动态IP地址。
l
static – 指定对端的IP地址为静态IP地址。该选项为系统的默认选项。
使用no type命令恢复对端IP地址的默认类型。
peer ip-address
l
ip-address - 指定对端的IP地址或主机名称。该IP地址只有当对端的IP地址类型是静态的时候才有效。
使用no peer命令取消对端IP地址或主机名称的指定。
接受对端ID
使所创建的ISAKMP网关接受任意的对端ID，不对对端进行ID检查，在ISAKMP网关配置模式下使用以下命
令：
accept-all-peer-id
使用no accept-all-peer-id关闭该功能。
指定P1提议
为ISAKMP网关指定P1提议，在ISAKMP网关配置模式下使用以下命令：
isakmp-proposal p1-proposal1 [p1-proposal2] [p1-proposal3] [p1-proposal4]
l
p1-proposal1 – 指定P1提议的名称。用户最多可以为ISAKMP网关指定4个P1提议供对端选择使用。
使用no isakmp-proposal取消对P1提议的指定。

<!-- 来源页 1417 -->
配置预共享密钥
如果使用预共享密钥认证方式，用户就需要指定预共享密钥。为ISAKMP网关指定预共享密钥，在ISAKMP网
关配置模式下使用以下命令：
pre-share string
l
string – 指定预共享密钥的内容。
使用no pre-share取消对预共享密钥的指定。
配置PKI信任域
如果使用数字证书认证方式，用户就需要指定数字证书的PKI信任域。为ISAKMP网关指定PKI信任域，在
ISAKMP网关配置模式下使用以下命令：
trust-domain string
l
string – 指定PKI信任域。
使用no trust-domain取消对PKI信任域的指定。
关于如何配置PKI信任域，请参阅《用户认证》的“PKI配置”部分。
配置对端证书的信任域
对端证书一般用于协商中数据加密以及认证，需由发起VPN连接的一端先导入对端证书。该命令仅适用于国
密1.0版本。配置对端证书所在的信任域，请在ISAKMP网关配置模式下使用以下命令：
remote-trust-domain string
l
string – 指定对端证书所在的信任域。
使用no remote-trust-domain命令删除对端证书的信任域配置。
配置加密证书的信任域
加密证书一般用于协商中数据加密。该命令仅适用于国密1.1版本，需为系统指定双证书。配置加密证书所
在的信任域，请在ISAKMP网关配置模式下使用以下命令：
trust-domain-enc string
l
string – 指定加密证书所在的信任域。
使用no trust-domain-enc命令删除加密证书的信任域配置。

<!-- 来源页 1418 -->
配置协商协议标准
协商协议标准分为国际标准IKEv1、国际标准IKEv2和国密标准。默认情况下，系统使用国际标准IKEv1为协
商协议标准。指定协商协议的标准为iIKEv1或国密标准，请在ISAKMP网关配置模式下使用以下命令：
protocol-standard {ikev1 | guomi[v1.0 | v1.1]}
l
ikev1 – 指定使用国际标准IKEv1为协商协议标准。
l
guomi[v1.0 | v1.1] – 指定使用国密标准为协商协议标准。v1.0为国密1.0版本；v1.1为国密1.1版本。
如指定版本号v1.0或v1.1，进行协商的两端设备必须是相同的版本号才能协商成功，否则协商失败。如
不指定版本号，那么发起端国密协议版本号为国密v1.0或v1.1都可协商。
使用no protocol-standard命令取消协商协议标准的配置。
配置本端ID
配置本端的ID，请在ISAKMP网关配置模式下使用以下命令：
local-id {fqdn string | asn1dn [string] | u-fqdn string | key-id string |ip ip-address }
l
fqdn string – 指定使用FQDN类型的ID。string为ID的具体内容。
l
asn1dn [string] – 指定使用Asn1dn类型的ID，该类型只可应用于使用证书的情况。string为ID的具
体内容。用户可以不指定ID的具体内容，在此种情况下，系统将从证书中获取ID。
l
u-fqdn string – 指定使用U-FQDN类型的ID，即电子邮件地址类型，例如
user1@hillstonenet.com。
l
key-id string - 指定使用Key ID类型的ID。该类型仅应用于XAUTH功能。
l
ip ip-address - 指定使用IP地址类型的ID。ip-address为ID的具体内容。
使用no local-id命令取消对本地ID的配置。
配置对端ID
配置对端ID，请在ISAKMP网关配置模式下使用以下命令：
peer-id {fqdn | asn1dn | u-fqdn | key-id | ip } string
l
fqdn – 指定使用FQDN类型的ID。string为ID的具体内容。
l
asn1dn – 指定使用Asn1dn类型的ID，该类型只可应用于使用证书的情况。string为ID的具体内容。
l
u-fqdn string – 指定使用U-FQDN类型的ID，即电子邮件地址类型，例如
user1@hillstonenet.com。

<!-- 来源页 1419 -->
l
key-id - 指定使用Key ID类型的ID。该类型仅应用于XAUTH功能。
l
ip - 指定使用IP地址类型的ID。
使用no peer-id命令取消对对端ID的配置。
指定连接类型
创建的ISAKMP网关可以是发起端、响应端或者既是发起端也是响应端。指定ISAKMP网关的连接类型，在
ISAKMP网关配置模式下使用以下命令：
connection-type {bidirectional | initiator-only | responder-only}
l
bidirectional – 指定该ISAKMP网关既是发起端也是响应端。该选项为系统的默认选项。
l
initiator-only – 指定该ISAKMP网关仅是发起端。
l
responder-only – 指定该ISAKMP网关仅是响应端。
使用no connection-type命令恢复默认连接方式。
开启NAT穿越功能
在IPSec或者IKE组建的VPN隧道中，若存在NAT网关设备，且NAT网关设备对VPN数据进行了NAT转换，则
必须开启IPSec或者IKE的NAT穿越功能。默认情况下，NAT穿越功能是关闭的。开启NAT穿越功能，在
ISAKMP网关配置模式下，使用以下命令：
nat-traversal
使用no nat-traversal命令关闭NAT穿越功能。
配置自动生成路由功能
对于IKEv1 VPN，当指定对端的IP地址类型为static或dynamic时，配置自动生成路由功能后，每创建一个
IPSec SA，设备会将目的地址为对端的local ID、下一跳为隧道接口的路由条目添加到自己的路由表。删除
一个IPSec SA后，相应的路由条目也会被删除。
默认情况下，设备的自动生成路由功能是关闭的。开启此功能，请在ISAKMP配置模式下，使用以下命令：
generate-route
使用no generate-route命令关闭自动生成路由功能。
配置DPD功能
DPD（Dead Peer Detection）为安全隧道对端状态探测功能。该功能开启后，系统将按照指定的时间间
隔，周期性的向对端发送请求报文，对ISAKMP网关是否存在进行检测。默认情况下，DPD功能是关闭的。

<!-- 来源页 1420 -->
开启DPD功能，在ISAKMP网关配置模式下使用以下命令：
dpd
配置DPD功能，在ISAKMP网关配置模式下使用以下命令：
dpd interval seconds retry times [on-demand | periodic]
l
interval seconds– 指定向对端发送查询请求的时间间隔。间隔范围是1到10秒。默认值是10。
l
retry times – 指定向对端发送查询请求的次数。向对端发送查询请求后，如果本端在指定的时间间隔内
收不到对端的报文，系统会在再次发送查询请求，如此反复，直到完成该参数指定的次数。在指定次数
查询完成后如果仍然收不到对端的报文，则判断对端ISAKMP网关已经死掉。查询请求的次数范围是1到
20次，默认是3次。
l
on-demand –指定DPD探测为on-demand模式。在该模式下，系统将根据设备是否收到IPSec流量
来判断是否向对端发送DPD探测报文。若设备未收到IPSec流量，不发送DPD探测报文；若设备收到
IPSec流量，需转发IPSec流量时，系统查询当前距离上一次收到对端IPSec报文的时间间隔，并与DPD
探测周期进行比较：①当前距离上一次收到对端IPSec报文的时间间隔小于DPD探测周期，说明在DPD
探测周期内收到了对端报文，表明对端ISAKMP网关存在，设备不发送DPD探测报文；②当前距离上一
次收到对端IPSec报文的时间间隔超过DPD探测周期，则表明不确定对端ISAKMP网关是否存在，设备发
送DPD探测报文对对端ISAKMP进行检测。若在一个DPD探测周期内均未收到对端报文，则判定对端
ISAKMP网关已经失效。系统将老化第一阶段和第二阶段的SA信息，重新发起新的IPSec协商。
l
periodic–指定DPD探测为periodic模式。在该模式下，系统将按照指定的时间间隔，持续向对端发送
DPD探测报文。若在一个DPD探测周期内，未收到对端响应报文，则判定对端失活。计算方式：DPD探
测周期=DPD时间间隔*DPD重试次数。默认为periodic模式。
使用no dpd命令恢复默认的DPD配置。
配置ISAKMP SA与IPSec SA关联/分离模式
在对端支持发起ISAKMP SA重协商的应用场景里，建议在防火墙上配置ISAKMP SA与IPSec SA分离模式。
默认情况下，ISAKMP SA与IPSec SA为关联模式。在关联模式下，对端在ISAKMP SA超时后，如果只发起
ISAKMP SA协商，不协商IPSec SA，ISAKMP SA会在一段时间后超时并断开，导致IPsec VPN断开。
配置ISAKMP SA与IPSec SA分离模式后，系统允许对端在ISAKMP SA超时后，只协商ISAKMP SA，继续
使用原有的IPSec SA，ISAKMP SA不会因为未协商新的IPsec SA而超时。
配置ISAKMP SA与IPSec SA分离模式，在ISAKMP网关配置模式下使用以下命令：
phase1-phase2-sa unbind
配置ISAKMP SA与IPSec SA关联模式，在ISAKMP网关配置模式下使用以下命令：
phase1-phase2-sa bind

<!-- 来源页 1421 -->
指定描述信息
为所配置的ISAKMP网关指定描述信息，请在ISAKMP网关配置模式下使用以下命令：
description string
l
string – ISAKMP网关的描述信息。
使用no description命令删除ISAKMP网关的描述信息。
开启/关闭ISAKMP SA与IPSec SA分离协商模式
ISAKMP SA与IPSec SA分离协商模式默认为关闭状态，即在ISAKMP SA超时后，如果只协商ISAKMP
SA，不协商IPSec SA，ISAKMP SA会在一段时间后超时并断开，导致IPsec VPN断开。开启ISAKMP SA与
IPSec SA分离协商模式时，系统允许在ISAKMP SA超时后，只协商ISAKMP SA，原有的IPSec SA会继续使
用，ISAKMP SA不会因为未协商新的IPsec SA而超时。
开启ISAKMP SA与IPSEC SA分离协商模式，在ISAKMP网关配置模式下使用以下命令：
phase1-phase2-sa unbind
关闭ISAKMP SA与IPSEC SA分离协商模式，在ISAKMP网关配置模式下使用以下命令：
phase1-phase2-sa bind
开启/关闭SN准入功能
IPSec VPN响应端设备开启SN准入功能后，将会在IPSec VPN的第一阶段协商过程中校验发起端设备的设
备序列号（SN号），若发起端设备的SN号不在SN准入名单中，则IPSec VPN将建立失败。该功能默认为关
闭状态。
注意:
l
用户需要先在响应端配置SN准入名单，再开启对应的SN准入功能。
l
若IPSec VPN响应端开启SN准入功能，则发起端必须是山石网科设备且版本为StoneOS
5.5R12P1及之后版本，否则IPSec VPN将建立失败。
l
SN准入功能仅支持IKEv1协议标准，不支持IKEv2和国密协议标准。
l
SN准入功能不支持非根VSYS。
开启SN准入功能，在ISAKMP网关配置模式下，使用以下命令：
verify-sn
关闭SN准入功能，在ISAKMP网关配置模式下，使用以下命令：

<!-- 来源页 1422 -->
no verify-sn
配置P2提议
P2提议使用在SA第二阶段。对P2提议的配置包括指定协议类型、加密算法、验证算法、压缩算法和生命周
期。
创建P2提议
创建P2提议，即IPSec安全提议，请在全局配置模式下使用以下命令：
ipsec proposal p2-name
l
p2-name – 指定所创建的P2提议的名称。执行该命令后，CLI进入到P2提议配置模式。对P2提议各项
参数的配置都要在该模式下进行。
使用no ipsec proposal p2-name命令删除指定的IPSec proposal。
指定协议类型
P2提议可使用的协议类型有AH以及ESP。为P2提议指定协议类型，在P2提议配置模式下使用以下命令：
protocol {esp | ah}
l
esp – 指定使用ESP协议。该协议为系统默认协议。
l
ah – 指定使用AH协议。
使用no protocol命令恢复默认协议配置。
指定加密算法
用户可以为P2提议指定至少一种最多四种加密算法。为P2提议指定加密算法，在P2提议配置模式下使用以
下命令：
encryption {3des | des | aes | aes-192 | aes-256 | aes-gcm-128 | aes-gcm-192 | aes-gcm-256 |
sm1 | sm4 | null} [3des | des | aes | aes-192 | aes-256 | aes-gcm-128 | aes-gcm-192 | aesgcm-256 | sm1 | sm4 | null] [3des | des | aes | aes-192 | aes-256 | aes-gcm-128 | aes-gcm-192
| aes-gcm-256 | sm1 | sm4 | null]……
l
3des – 指定使用3DES加密方法。密钥长度为192比特。该方法为StoneOS系统默认方法。
l
des – 指定使用DES加密方法。密钥长度为64比特。
l
aes – 指定使用AES加密方法。密钥长度为128比特。
l
aes-192 – 指定使用192bit AES加密方法。密钥长度为192比特。

<!-- 来源页 1423 -->
l
aes-256 – 指定使用256bit AES加密方法。密钥长度为256比特。
l
aes-gcm-128– 指定使用128bit AES-GCM加密方法。密钥长度为128比特。
l
aes-gcm-192– 指定使用192bit AES-GCM加密方法。密钥长度为192比特。
l
aes-gcm-256– 指定使用256bit AES-GCM加密方法。密钥长度为256比特。
l
sm1 – 指定使用国家商用密码SM1分组密码算法。密钥长度为128比特。
l
sm4 – 指定使用国家商用密码SM4分组密码算法。密钥长度为128比特。
l
null – 不使用加密功能。
使用no encryption命令恢复默认加密算法。
指定验证算法
用户可以为P2提议指定至少一种最多三种验证算法。为P2提议指定验证算法，在P2提议配置模式下使用以
下命令：
hash {md5 | sha | sha256 | sha384 | sha512 | sm3 | null} [md5 | sha | sha256 | sha384 | sha512
| sm3 | null] [md5 | sha | sha256 | sha384 | sha512 | sm3 | null]
l
md5 – 指定使用MD5验证算法。摘要为128比特。
l
sha – 指定使用SHA-1验证算法。摘要为160比特。该算法为StoneOS的默认算法。
l
sha256 – 指定使用SHA-256验证算法。摘要为256比特。
l
sha384 – 指定使用SHA-384验证算法。摘要为384比特。
l
sha512 –指定使用SHA-512验证算法。摘要为512比特。
l
sm3 – 指定使用国密SM3验证算法。摘要为256比特。
l
null – 不使用验证功能。
使用no hash命令恢复默认验证算法。
指定压缩算法
默认情况下，P2提议不使用任何压缩算法。为P2提议指定压缩算法（DEFLATE算法），请在P2提议配置模
式下使用以下命令：
compression deflate
使用no compression命令取消对压缩算法的指定。

<!-- 来源页 1424 -->
配置PFS功能
PFS（Perfect Forward Security）功能决定新密钥的生成方式，而不是新密钥的生成时间。PFS保证无论
在哪一阶段，一个密钥只能使用一次，而且，生成密钥的“材料”也只能使用一次。某个“材料”在生成了
一个密钥后就被弃，绝不用来再生成任何其它密钥。这样可以确保一旦单个密钥泄密，最多只可能影响用该
密钥加密的数据，而不会危及整个通信。PFS功能是由DH算法做保障的。配置P2提议的PFS功能，在P2提
议配置模式下使用以下命令：
group {nopfs | 1 | 2 | 5 | 14 | 15 |16| 18 | 19 | 20 | 21 | 24}
l
nopfs – 不使用PFS功能。该选项为系统的默认选项。
l
1 – 选择DH组1。密钥的长度为768比特（MODP Group）。
l
2 – 选择DH组2。密钥的长度为1024比特（MODP Group）。
l
5 – 选择DH组5。密钥的长度为1536比特（MODP Group）。
l
14 – 选择DH组14。密钥的长度为2048比特（MODP Group）。
l
15 – 选择DH组15。密钥的长度为3072比特（MODP Group）。
l
16 – 选择DH组16。密钥的长度为4096比特（MODP Group）。
l
18 – 选择DH组18。密钥的长度为8192比特（MODP Group）。
l
19 – 选择DH组19。密钥的长度为256比特（ECP Group）。
l
20 – 选择DH组20。密钥的长度为384比特（ECP Group）。
l
21 – 选择DH组21。密钥的长度为521比特（ECP Group）。
l
24 – 选择DH组24。密钥的长度为2048比特（MODP Group with 256-bit Prime Order
Subgroup）。
使用no group命令恢复默配置。
指定生命周期
Hillstone设备有两种衡量生命周期的方法，分别是按时间和按流量。当SA的流量或者时间达到特定值时，
SA就会过期，需要重新进行协商。指定P2提议的生命周期，在P2提议配置模式，使用以下命令：
lifetime seconds
l
seconds – 指定时间类型生命周期的时间长度，单位为秒。默认值是28800秒。
lifesize kilobytes
l
kilobytes – 指定流量类型周期的流量值，单位为字节。默认值是0，意义为没有周期流量限制。

<!-- 来源页 1425 -->
使用以上两个命令no的形式恢复默认配置。即
no lifetime
no lifesize
配置隧道
通过IKE配置IPSec隧道，用户需要配置的选项有指定协议类型、ISAKMP网关、IKE安全提议、ID号、是否
分片以及防重放等。
创建IKE隧道
创建IKE隧道，在全局配置模式下，使用以下命令：
tunnel ipsec tunnel-name auto
l
tunnel-name - 指定所创建的IKE隧道的名称。
执行该命令后，CLI进入到IKE隧道配置模式。对IKE隧道的所有参数配置都需要在该模式下进行。
在全局配置模式下使用no tunnel ipsec tunnel-name auto删除指定的IKE隧道。
启用/禁用IPSec VPN隧道
默认情况下，IPSec VPN 隧道为启用状态。启用/禁用IPSec VPN隧道，在IKE隧道配置模式下，使用以下
命令：
l
启用IPSec VPN隧道：enable
l
禁用IPSec VPN隧道：disable
启用/禁用IPSec VPN隧道硬件快转功能
型号说明：
l
支持：SG-6000-A系列ASIC防火墙。
l
支持：SG-6000-K系列ASIC防火墙。
开启后将由专门的硬件芯片进行IPSec数据包的加密/解密，从而降低CPU负载，提升大流量场景下的转发性
能。该功能默认为开启状态。
启用/禁用IPSec VPN隧道的硬件快转功能，在IKE隧道配置模式下，使用以下命令：

<!-- 来源页 1426 -->
l
启用：hardware-fast-forward enable
l
禁用：hardware-fast-forward disable
注意:
l
若未开启全局硬件快转功能，则IPSec VPN隧道的硬件快转功能将不生效。配置全局硬件快转
功能参见“防火墙> 硬件快转”章节。
l
若IPSec VPN隧道已关闭硬件快转功能，重新开启后需要手动执行clear isakmp sa命令进行
隧道重协商，使硬件快转功能生效。
指定IPSec协议的封装模式
为IKE隧道指定封装模式，可以是隧道模式或者传输模式，在IKE隧道配置模式下使用以下命令：
mode {transport | tunnel}
l
transport – 指定IPSec协议的封装模式为传输模式。
l
tunnel – 指定IPSec协议的封装模式为隧道模式。该模式为系统默认模式。
使用no mode命令恢复默认模式。
指定ISAKMP网关
为IKE隧道指定ISAKMP网关，请在IKE隧道配置模式下使用以下命令：
isakmp-peer peer-name
l
peer-name – 指定ISAKMP网关的名称。
使用no isakmp-peer取消对ISAKMP网关的指定。
指定P2提议
为IKE隧道指定P2提议，请在IKE隧道配置模式下使用以下命令：
ipsec-proposal p2-name
l
p2-name – 指定P2提议的名称。可以指定三个
使用no ipsec-proposal取消对P2提议的指定。

<!-- 来源页 1427 -->
指定第二阶段ID
当用户需对IPSec VPN流量进行分流与限流时，需指定IKE第二阶段ID。第二阶段ID由本地网段、远程网段
和服务类型组成。配置时，需在本端和对端设备上对应配置，然后本端和对端将进行协商，最终创建一条
IKE IPSec隧道。用户可指定1个或多个第二阶段ID，即创建1条或多条IKE IPSec隧道。系统将根据每个隧道
的第二阶段ID对隧道中的流量进行分流、限流。
若不需对IPSec VPN流量分流与限流，可不配置。关于如何开启分流或限流功能，请查阅“配置IPSec VPN
流量分流与限流”章节。
为IKE IPSec隧道指定第二阶段ID，请在IKE隧道配置模式下使用以下命令：
id {auto | local ip-address/mask remote ip-address/mask service service-name}
l
auto – 自动指定第二阶段ID。此参数为系统默认配置。
l
local ip-address/mask – 指定第二阶段的本地网段的IP/掩码。
l
remote ip-address/mask – 指定第二阶段的远程网段的IP/掩码。
l
service service-name – 指定第二阶段IKE IPSec隧道可传输的流量的服务或协议名称。
用户可配置最多256个第二阶段ID用于协商建立多个IKE隧道。
使用no id {auto | local ip-address/mask remote ip-address/mask service service-name}命令
恢复系统默认配置。
注意:
l
默认情况下，IKE IPSec 隧道本端与对端的第二阶段ID需对应配置，若没有对应配置，将导致
协商失败。
l
若响应方设备开启接受对端任意ID时，也可实现协商成功。关于该功能，请查阅“启用接受对
端ID功能”章节。
配置IPSec VPN流量分流与限流
默认情况下，IPSec VPN流量分流与限流功能为禁用状态。开启该功能后，设备将根据第二阶段ID的配置，
对进出IKE隧道的流量进行过滤，然后分流、限流；未匹配到第二阶段ID的流量将被丢弃。具体如下：
l
流量分流：设备根据第二阶段ID的配置，在IKE隧道入口对进入IKE隧道的流量进行分流。如果流量的源
IP地址、目的IP地址、以及流量的类型(service)匹配某一个第二阶段ID的配置，则该流量进入相应的
IKE隧道进行封装发送。如果没有匹配的第二阶段ID，则该流量被丢弃。

<!-- 来源页 1428 -->
l
流量限流：设备根据第二阶段ID的配置，在IKE隧道出口对解封装后的流量进行限流。如果解封装后流量
的源IP地址、目的IP地址、以及流量的类型(service)匹配某一个第二阶段ID的配置，则该流量被接收设
备继续处理；如果流量无法匹配任何一个第二阶段ID的配置，则该流量被丢弃。
注意: 配置该功能前需确保已配置第二阶段ID且IKE隧道第二阶段协商成功。
开启流量分流与限流功能，在IKE隧道配置模式，使用如下命令：
check-id
使用no check-id关闭流量分流与限流功能。
启用接受对端ID功能
该功能需在IKE隧道协商的响应方设备上进行配置。开启后，响应方设备将接受对端（协商发起方）配置的
第二阶段ID，同时设置自身的第二阶段ID与对端保持对应，从而使IKE隧道两端能协商成功。常用于响应方
设备对发起方的第二阶段ID无法感知或者不感兴趣的场景。在IKE隧道配置模式下，使用以下命令开启接受
对端ID的功能：
accept-all-proxy-id
在IKE隧道配置模式下，使用该命令no的形式关闭接受对端ID功能：
no accept-all-proxy-id
注意: 当响应方设备上配置了多个第二阶段ID时，将无法开启该功能。
配置自动连接功能
设备提供了两种触发建立SA的方式：自动方式和流量触发方式。
l
自动方式是指设备每60秒检查一次SA的状态，如果SA未建立则自动发起协商请求；
l
流量触发方式是指当有数据流量需要通过隧道进行传输时，该隧道才发起协商请求。
默认情况下，使用流量触发方式。若需要使用自动方式，请在IKE隧道配置模式下使用以下命令：
auto-connect
使用no auto-connect命令恢复系统的默认设置。
注意: 自动连接功能仅在对端IP地址为静态类型且本端可以作为发起端时有效。

<!-- 来源页 1429 -->
配置分片功能
用户可以指定是否允许转发设备将包进行分片处理。为IKE隧道配置分片功能，请在IKE隧道配置模式下使用
以下命令：
df-bit {copy | clear | set}
l
copy – 直接从发包端拷贝IP包的DF选项。该选项为系统默认选项。
l
clear – 允许转发设备对包做分片处理。
l
set – 不允许转发设备对包做分片处理。
使用no df-bit恢复系统的默认设置。
配置防重放功能
防重放（anti-replay）指防止恶意用户通过重复发送捕获到的数据包所进行的攻击，即接收方会拒绝旧的
或重复的数据包。默认情况下，防重放功能是关闭的。为IKE IPSec隧道配置防重放功能，请在IKE IPSec隧
道配置模式下使用以下命令：
anti-replay {32 | 64 | 128 | 256 | 512 | 1024 | 2048 | 4096}
l
32 – 指定防重放的窗口为32。
l
64 – 指定防重放的窗口为64。
l
128 – 指定防重放的窗口为128。
l
256 – 指定防重放的窗口为256。
l
512 – 指定防重放的窗口为512。
l
1024 – 指定防重放的窗口为1024。
l
2048 – 指定防重放的窗口为2048。
l
4096 – 指定防重放的窗口为4096。
在网络状况较差时，例如存在严重乱序现象等，请选择较大的窗口。
使用no anti-replay命令关闭防重放功能。
开启/关闭扩展序列号功能
ESN（Extended Sequence Number，扩展序列号）功能用于扩展防重放序列号的范围，能够将防重放序
列号由原有的32位扩展至64位。在大量数据流通过IPSec SA高速传输的场景下，可避免由于序列号被快速
用尽导致IPSec SA频繁地重协商。开启防重放功能后，才能够开启ESN功能。该功能默认为关闭状态。
开启扩展序列号功能，在IKE IPSec隧道配置模式下，使用以下命令：

<!-- 来源页 1430 -->
esn
关闭扩展序列号功能，在IKE IPSec隧道配置模式下，使用以下命令：
no esn
配置VPN监控及冗余备份功能
Hillstone设备能够监测指定的VPN隧道是否连通，并且能够实现两条或者多条VPN隧道的备份或者分流。
该功能对基于路由的VPN以及基于策略的VPN均有效。具体实现包括以下两种环境：
l
为同一个远程对端配置备份VPN隧道，并且在任意时刻只有一个隧道处于活动状态。最初，主VPN隧道
处于活动状态，如果监测到该主隧道中断，Hillstone设备会通过备份隧道重新传输信息流；
l
为同一个远程对端配置了两个或者多个VPN隧道，所有隧道都同时处于活动状态，并且通过等价多径路
由（ECMP）实现负载均衡。如果监测到隧道中断，Hillstone设备会通过其它隧道重新传输信息流。
VPN监控功能支持通过Ping报文对目标隧道进行监测。默认情况下，该功能是关闭的。配置VPN监控功能，
请在IKE IPSec隧道配置模式下使用以下命令：
vpn-track [A.B.C.D] [src-ip A.B.C.D] [interval time-value] [threshold value]
l
A.B.C.D – 指定监测目标的IP地址。当对端设备为Hillstone设备时，如果不指定该参数，系统默认为对
端IP地址。此IP地址不能为“0.0.0.0”和“255.255.255.255”。
l
src-ip A.B.C.D – 指定发送Ping监测报文的源IP地址。当对端设备为Hillstone设备时，如果不指定该
参数，系统默认为出接口IP地址。此IP地址不能为“0.0.0.0”和“255.255.255.255”。
l
interval time-value – 指定发送Ping监测报文的时间间隔，单位为秒。范围是1到255秒。默认值是
10秒。
l
threshold value – 指定判断监测失败的警戒值。如果系统连续未收到该参数指定个数的响应报文，就
判断为监测失败，即目标隧道中断。取值范围是1到255。默认值是10。
使用no vpn-track命令取消VPN监控功能的配置。
VPN监控功能包括active和dead两种状态。用户可以使用相应的show命令在CLI的任何模式下查看VPN监
控功能的状态以及配置信息：
l
查看VPN监控功能的状态：show ipsec sa {id}
l
查看VPN监控功能的配置情况：show tunnel ipsec {manual | auto} {tunnel-name}
例如：
查看VPN监控功能状态

<!-- 来源页 1431 -->
hostname(config)# show ipsec sa 5
ID: 1
scpu: 0
VPN Name: vpn1
L2tp port: 1
Duration(S): 1375459
Last setup time: 2022-03-08 22:09:53
Last teardown time: 2022-03-09 06:09:54
Tear down reason: a lifetime timeout occurred
Teardowns today: 0
Outbound
Gateway: 1.1.1.2
......
Sending rate(KB/s): 0
Status: Active
Inbound
Gateway: 1.1.1.2
......
Receiving rate(KB/s): 0
Status: Active
查看VPN监控功能配置
hostname(config)# show tunnel ipsec auto vpn1
Name: vpn1
mode: tunnel
......
vpn-track: enable
tracknotify: enable
vpntrack destination 1.1.1.1
vpntrack source ip: 2.2.2.2

<!-- 来源页 1432 -->
vpntrack interval: 3
vpntrack threshold: 3
注意: 关于VPN监控及冗余备份的具体实例，请参阅VPN监控及冗余备份的具体实例一节。
开启/关闭VPN隧道状态通知功能
默认情况下，VPN隧道状态通知功能为关闭状态。在开启VPN隧道状态通知功能后，如果是基于路由的
VPN，系统一旦监测到中断的VPN隧道，会立即通知路由模块中断的VPN隧道信息并进行隧道路由的更新处
理；如果是基于策略的VPN，系统一旦监测到中断的VPN隧道，会立即通知策略模块中断的VPN隧道信息并
进行隧道策略的更新处理。用户可以通过命令开启/关闭VPN隧道状态通知功能，对中断状态下的VPN隧道
信息进行通知。开启/关闭VPN隧道状态通知功能，在IKE IPSec隧道配置模式下，使用以下命令：
l
开启：tunnel-state-notify
l
关闭：no tunnel-state-notify
设置Commit位
用户可以配置使响应方设置Commit位，从而防止出现丢包和时间差现象。但是，设置Commit位可能导致
响应速度变慢。设置Commit位，请在IKE IPSec隧道配置模式下使用以下命令：
响应方设置Commit位：responder-set-commit
响应方不设置Commit位：no responder-set-commit
指定描述信息
为所配置的IKE隧道指定描述信息，请在IKE IPSec隧道配置模式下使用以下命令：
description string
l
string – IKE隧道的描述信息。
使用no description命令删除IKE隧道的描述信息。
配置IKEv2 VPN
IKEv2 VPN的配置包括：
l 配置P1提议
l 配置ISAKMP网关

<!-- 来源页 1433 -->
l 配置P2提议
l 配置隧道
配置P1提议
P1提议是IKE安全提议，可应用到ISAKMP网关上，在SA第一阶段使用。对IKE安全提议的配置包括指定认证
方式、加密算法、验证算法、PRF 算法、DH组和安全联盟的生命周期。
创建P1提议
创建一个P1提议，即IKE安全提议，请在全局配置模式下使用以下命令：
isakmp proposal p1-name
l
p1-name – 指定所创建的P1提议的名称。执行该命令后，CLI进入到P1提议配置模式。用户可以在该模
式下对P1提议进行参数配置。
使用no isakmp proposal p1-name命令删除指定的P1提议。
指定认证方式
此处指定的是IKE身份认证的方式。身份认证用来确认通信双方的身份。方式有预共享密钥认证、数字证书
认证和国密数据信封认证。对于预共享密钥认证方式，认证字用来作为一个输入产生密钥，认证字不同是不
可能在双方产生相同的密钥的。指定IKE安全提议的身份认证方式，在P1提议配置模式下使用以下命令：
authentication {pre-share | rsa-sig | ecdsa-sig }
l
pre-share – 指定使用预共享密钥认证方式。该方式为默认认证方式。
l
rsa-sig – 指定使用RSA数字证书认证方式。
l
ecdsa-sig – 指定使用ECDSA数字证书认证方式。此方式对应的验证算法只能为SHA-256、SHA-384
和SHA-512。
使用no authentication命令恢复默认认证方式。
指定加密算法
指定IKEv2安全提议的加密算法，在P1提议配置模式下使用以下命令：
encryption {3des | des | aes | aes-192 | aes-256 }
l
3des – 指定使用3DES加密方法。密钥长度为192比特。该方法为StoneOS系统默认方法。
l
des – 指定使用DES加密方法。密钥长度为64比特。

<!-- 来源页 1434 -->
l
aes – 指定使用AES加密方法。密钥长度为128比特。
l
aes-192 – 指定使用192bit AES加密方法。密钥长度为192比特。
l
aes-256 – 指定使用256bit AES加密方法。密钥长度为256比特。
使用no encryption命令恢复默认加密算法。
指定验证算法
指定IKEv2安全提议的验证算法，在P1提议模式下使用以下命令：
hash {md5 | sha | sha256 | sha384 | sha512 }
l
md5 – 指定使用MD5验证算法。摘要为128比特。
l
sha – 指定使用SHA-1验证算法。摘要为160比特。该算法为StoneOS的默认算法。
l
sha256 – 指定使用SHA-256验证算法。摘要为256比特。
l
sha384 – 指定使用SHA-384验证算法。摘要为384比特。
l
sha512 – 指定使用SHA-512验证算法。摘要为512比特。
使用no hash命令恢复默认认证方式。
指定PRF算法
StoneOS支持以下PRF算法：MD5、SHA-1以及SHA-2（包括SHA-256、SHA-384和SHA-512）。用户
可指定至少一种最多四种PRF算法。指定IKEv2安全提议的PRF算法，在P1提议模式下使用以下命令：
prf {md5 | sha | sha256 | sha384 | sha512}
l
md5 – 指定使用MD5算法。摘要为128比特。
l
sha – 指定使用SHA-1算法。摘要为160比特。该算法为StoneOS的默认算法。
l
sha256 – 指定使用SHA-256算法。摘要为256比特。
l
sha384 – 指定使用SHA-384算法。摘要为384比特。
l
sha512 – 指定使用SHA-512算法。摘要为512比特。
使用no prf命令恢复默认认证方式。
选择DH组
Diffie-Hellman（DH）是一种建立密钥的方法。DH组决定DH交换中密钥生成“材料”的长度。密钥的牢
固性部分决定于DH组的强度。密钥“材料”长度越长，所生成的密钥安全度也就越高，越难被破译。DH组
的选择很重要，因为DH组只在第一阶段的SA协商中确定，第二阶段的协商不再重新选择DH组，两个阶段使

<!-- 来源页 1435 -->
用的是同一个DH组，因此该DH组的选择将影响所有会话密钥的生成。在协商过程中，两个ISAKMP网关间
应选择同一个DH组，即密钥“材料”长度应该相等。若DH组不匹配，将协商失败。
在P1提议选择DH组，在P1提议配置模式下使用以下命令：
group {1 | 2 | 5 | 14 | 15 |16 | 18 | 19 | 20 | 21 | 24}
l
1 – 选择DH组1。密钥的长度为768比特（MODP Group）。
l
2 – 选择DH组2。密钥的长度为1024比特（MODP Group）。2为系统默认值。
l
5 – 选择DH组5。密钥的长度为1536比特（MODP Group）。
l
14 – 选择DH组14。密钥的长度为2048比特（MODP Group）。
l
15 – 选择DH组15。密钥的长度为3072比特（MODP Group）。
l
16 – 选择DH组16。密钥的长度为4096比特（MODP Group）。
l
18 – 选择DH组18。密钥的长度为8192比特（MODP Group）。
l
19 – 选择DH组19。密钥的长度为256比特（ECP Group）。
l
20 – 选择DH组20。密钥的长度为384比特（ECP Group）。
l
21 – 选择DH组21。密钥的长度为521比特（ECP Group）。
l
24 – 选择DH组24。密钥的长度为2048比特（MODP Group with 256-bit Prime Order
Subgroup）。
使用no group命令取消恢复默认DH组。
在P2提议中配置PFS时，也可选用如上DH组。
指定安全联盟的生命周期
第一阶段SA有一个默认的生命周期，如果ISAKMP SA生命期时间到，要向对方发送第一阶段SA删除消息，
通知对方第一阶段SA已经过期。之后需要重新进行SA协商。指定安全联盟的生命周期，在P1提议配置模式
下使用以下命令：
lifetime time-value
l
time-value – 指定SA第一阶段的生命周期长度，单位为秒。默认86400秒。范围是300到86400秒。
使用no lifetime命令恢复默认生命周期长度。
配置ISAKMP网关
创建一个ISAKMP网关后，用户可以配置ISAKMP网关的IKE协商模式、ISAKMP网关IP地址及类型、IKE安全
提议、预共享密钥、PKI信任域、本地ID、ISAKMP网关ID 、ISAKMP网关连接方式以及是否开启ISAKMP网

<!-- 来源页 1436 -->
关的NAT穿越功能等。
创建ISAKMP网关
创建ISAKMP网关，在全局配置模式下，使用以下命令:
isakmp peer peer-name
l
peer-name – 指定ISAKMP网关的名称。
执行该命令后，CLI进入到ISAKMP网关配置模式。用户可以在该模式下对ISAKMP网关进行参数配置。
在全局配置模式下使用no isakmp peer peer-name命令删除指定的ISAKMP网关。
绑定接口到ISAKMP网关
用户可以绑定某个接口到ISAKMP网关。将接口绑定到ISAKMP网关，在ISAKMP网关配置模式下使用以下命
令：
interface interface-name
l
interface-name – 指定被绑定接口的名称。
使用no interface interface-name命令取消接口绑定。
配置协商协议标准
协商协议标准分为国际标准IKEv1、国际标准IKEv2和国密标准。默认情况下，系统使用国际标准IKEv1为协
商协议标准。指定协商协议的标准为IKEv2，请在ISAKMP网关配置模式下使用以下命令：
protocol-standard ikev2
l
ikev2 – 指定使用国际标准IKEv2为协商协议标准。
使用no protocol-standard命令取消协商协议标准的配置。
配置自定义IKE协商端口
用户可以自定义UDP端口进行IKE协商，并且建立IPSec连接。配置自定义IKE协商端口，在ISAKMP网关配
置模式下使用以下命令：
ipsec-over-udp port port-number
l
port-number – 指定UDP端口号。取值范围是1到65535，建议使用1024到65535之间的端口号。
使用no ipsec-over-udp命令取消自定义的UDP端口配置。

<!-- 来源页 1437 -->
指定对端的IP地址及类型
用户可以为所创建的ISAKMP网关指定对端的IP地址。指定对端的IP地址，请在ISAKMP网关配置模式下使用
以下命令：
peer ip-address
l
ip-address - 指定对端的IP地址或主机名称。
使用no peer命令取消对端IP地址或主机名称的指定。
指定P1提议
为ISAKMP网关指定P1提议，在ISAKMP网关配置模式下使用以下命令：
isakmp-proposal p1-proposal1 [p1-proposal2] [p1-proposal3] [p1-proposal4]
l
p1-proposal1 – 指定P1提议的名称。用户最多可以为ISAKMP网关指定4个P1提议供对端选择使用。
使用no isakmp-proposal取消对P1提议的指定。
配置预共享密钥
如果使用预共享密钥认证方式，用户就需要指定预共享密钥。为ISAKMP网关指定预共享密钥，在ISAKMP网
关配置模式下使用以下命令：
pre-share string
l
string – 指定预共享密钥的内容。
使用no pre-share取消对预共享密钥的指定。
配置PKI信任域
如果使用数字证书认证方式，用户就需要指定数字证书的PKI信任域。为ISAKMP网关指定PKI信任域，在
ISAKMP网关配置模式下使用以下命令：
trust-domain string
l
string – 指定PKI信任域。
使用no trust-domain取消对PKI信任域的指定。
关于如何配置PKI信任域，请参阅《用户认证》的“PKI配置”部分。

<!-- 来源页 1438 -->
配置对端证书的信任域
对端证书一般用于协商中数据加密以及认证，需由发起VPN连接的一端先导入对端证书。该命令仅适用于国
密1.0版本。配置对端证书所在的信任域，请在ISAKMP网关配置模式下使用以下命令：
remote-trust-domain string
l
string – 指定对端证书所在的信任域。
使用no remote-trust-domain命令删除对端证书的信任域配置。
配置本端ID
配置本端的ID，请在ISAKMP网关配置模式下使用以下命令：
local-id {fqdn string | asn1dn [string] | u-fqdn string | key-id string |ip ip-address }
l
fqdn string – 指定使用FQDN类型的ID。string为ID的具体内容。
l
asn1dn [string] – 指定使用Asn1dn类型的ID，该类型只可应用于使用证书的情况。string为ID的具
体内容。用户可以不指定ID的具体内容，在此种情况下，系统将从证书中获取ID。
l
u-fqdn string – 指定使用U-FQDN类型的ID，即电子邮件地址类型，例如
user1@hillstonenet.com。
l
key-id string - 指定使用Key ID类型的ID。该类型仅应用于XAUTH功能。
l
ip ip-address - 指定使用IP地址类型的ID。ip-address为ID的具体内容。
使用no local-id命令取消对本地ID的配置。
配置对端ID
配置对端ID，请在ISAKMP网关配置模式下使用以下命令：
peer-id {fqdn | asn1dn | ip } string
l
fqdn – 指定使用FQDN类型的ID。string为ID的具体内容。
l
asn1dn – 指定使用Asn1dn类型的ID，该类型只可应用于使用证书的情况。string为ID的具体内容。
l
ip - 指定使用IP地址类型的ID。
使用no peer-id命令取消对对端ID的配置。

<!-- 来源页 1439 -->
指定连接类型
创建的ISAKMP网关可以是发起端、响应端或者既是发起端也是响应端。指定ISAKMP网关的连接类型，在
ISAKMP网关配置模式下使用以下命令：
connection-type {bidirectional | initiator-only | responder-only}
l
bidirectional – 指定该ISAKMP网关既是发起端也是响应端。该选项为系统的默认选项。
l
initiator-only – 指定该ISAKMP网关仅是发起端。
l
responder-only – 指定该ISAKMP网关仅是响应端。
使用no connection-type命令恢复默认连接方式。
配置自动生成路由功能
对于IKEv1 VPN，当指定对端的IP地址类型为static或dynamic时，配置自动生成路由功能后，每创建一个
IPSec SA，设备会将目的地址为对端的local ID、下一跳为隧道接口的路由条目添加到自己的路由表。删除
一个IPSec SA后，相应的路由条目也会被删除。
默认情况下，设备的自动生成路由功能是关闭的。开启此功能，请在ISAKMP配置模式下，使用以下命令：
generate-route
使用no generate-route命令关闭自动生成路由功能。
配置DPD功能
DPD（Dead Peer Detection）为安全隧道对端状态探测功能。该功能开启后，系统将按照指定的时间间
隔，周期性的向对端发送请求报文，对ISAKMP网关是否存在进行检测。默认情况下，DPD功能是关闭的。
开启DPD功能，在ISAKMP网关配置模式下使用以下命令：
dpd
配置DPD功能，在ISAKMP网关配置模式下使用以下命令：
dpd interval seconds retry times [on-demand | periodic]
l
interval seconds – 指定向对端发送查询请求的时间间隔。间隔范围是1到10秒。默认值是10。
l
retry times – 指定向对端发送查询请求的次数。向对端发送查询请求后，如果本端在指定的时间间隔内
收不到对端的报文，系统会在再次发送查询请求，如此反复，直到完成该参数指定的次数。在指定次数
查询完成后如果仍然收不到对端的报文，则判断对端ISAKMP网关已经死掉。查询请求的次数范围是1到
20次，默认是3次。

<!-- 来源页 1440 -->
l
on-demand – 指定DPD探测为on-demand模式。在该模式下，系统将根据设备是否收到IPSec流量
来判断是否向对端发送DPD探测报文。若设备未收到IPSec流量，不发送DPD探测报文；若设备收到
IPSec流量，需转发IPSec流量时，系统查询当前距离上一次收到对端IPSec报文的时间间隔，并与DPD
探测周期进行比较：①当前距离上一次收到对端IPSec报文的时间间隔小于DPD探测周期，说明在DPD
探测周期内收到了对端报文，表明对端ISAKMP网关存在，设备不发送DPD探测报文；②当前距离上一
次收到对端IPSec报文的时间间隔超过DPD探测周期，则表明不确定对端ISAKMP网关是否存在，设备发
送DPD探测报文对对端ISAKMP进行检测。若在一个DPD探测周期内均未收到对端报文，则判定对端
ISAKMP网关已经失效。系统将老化第一阶段和第二阶段的SA信息，重新发起新的IPSec协商。
l
periodic – 指定DPD探测为periodic模式。在该模式下，系统将按照指定的时间间隔，持续向对端发送
DPD探测报文。若在一个DPD探测周期内，未收到对端响应报文，则判定对端失活。计算方式：DPD探
测周期=DPD时间间隔*DPD重试次数。默认为periodic模式。
使用no dpd命令恢复默认的DPD配置。
指定描述信息
为所配置的ISAKMP网关指定描述信息，请在ISAKMP网关配置模式下使用以下命令：
description string
l
string – ISAKMP网关的描述信息。
使用no description命令删除ISAKMP网关的描述信息。
配置P2提议
P2提议使用在SA第二阶段。对P2提议的配置包括指定协议类型、加密算法、验证算法、压缩算法和生命周
期。
创建P2提议
创建P2提议，即IPSec安全提议，请在全局配置模式下使用以下命令：
ipsec proposal p2-name
l
p2-name – 指定所创建的P2提议的名称。执行该命令后，CLI进入到P2提议配置模式。对P2提议各项
参数的配置都要在该模式下进行。
使用no ipsec proposal p2-name命令删除指定的IPSec proposal。

<!-- 来源页 1441 -->
指定协议类型
P2提议可使用的协议类型有ESP。为P2提议指定协议类型，在P2提议配置模式下使用以下命令：
protocol esp
l
esp – 指定使用ESP协议。该协议为系统默认协议。
使用no protocol命令恢复默认协议配置。
指定加密算法
用户可以为P2提议指定至少一种最多四种加密算法。为P2提议指定加密算法，在P2提议配置模式下使用以
下命令：
encryption {3des | des | aes-192 | aes-256 } [3des | des | aes | aes-192 | aes-256 ] [3des | des |
aes | aes-192 | aes-256 ]……
l
3des – 指定使用3DES加密方法。密钥长度为192比特。该方法为StoneOS系统默认方法。
l
des – 指定使用DES加密方法。密钥长度为64比特。
l
aes-192 – 指定使用192bit AES加密方法。密钥长度为192比特。
l
aes-256 – 指定使用256bit AES加密方法。密钥长度为256比特。
使用no encryption命令恢复默认加密算法。
指定验证算法
用户可以为P2提议指定至少一种最多四种验证算法。为P2提议指定验证算法，在P2提议配置模式下使用以
下命令：
hash {md5 | sha | sha256 | sha384 | sha512 }
l
md5 – 指定使用MD5验证算法。摘要为128比特。
l
sha – 指定使用SHA-1验证算法。摘要为160比特。该算法为StoneOS的默认算法。
l
sha256 – 指定使用SHA-256验证算法。摘要为256比特。
l
sha384 – 指定使用SHA-384验证算法。摘要为384比特。
l
sha512 –指定使用SHA-512验证算法。摘要为512比特。
使用no hash命令恢复默认验证算法。

<!-- 来源页 1442 -->
指定压缩算法
默认情况下，P2提议不使用任何压缩算法。为P2提议指定压缩算法（DEFLATE算法），请在P2提议配置模
式下使用以下命令：
compression deflate
使用no compression命令取消对压缩算法的指定。
配置PFS功能
PFS（Perfect Forward Security）功能决定新密钥的生成方式，而不是新密钥的生成时间。PFS保证无论
在哪一阶段，一个密钥只能使用一次，而且，生成密钥的“材料”也只能使用一次。某个“材料”在生成了
一个密钥后就被弃，绝不用来再生成任何其它密钥。这样可以确保一旦单个密钥泄密，最多只可能影响用该
密钥加密的数据，而不会危及整个通信。PFS功能是由DH算法做保障的。配置P2提议的PFS功能，在P2提
议配置模式下使用以下命令：
group {nopfs | 1 | 2 | 5 | 14 | 15 |16| 18 | 19 | 20 | 21 | 24}
l
nopfs – 不使用PFS功能。该选项为系统的默认选项。
l
1 – 选择DH组1。密钥的长度为768比特（MODP Group）。
l
2 – 选择DH组2。密钥的长度为1024比特（MODP Group）。
l
5 – 选择DH组5。密钥的长度为1536比特（MODP Group）。
l
14 – 选择DH组14。密钥的长度为2048比特（MODP Group）。
l
15 – 选择DH组15。密钥的长度为3072比特（MODP Group）。
l
16 – 选择DH组16。密钥的长度为4096比特（MODP Group）。
l
18 – 选择DH组18。密钥的长度为8192比特（MODP Group）。
l
19 – 选择DH组19。密钥的长度为256比特（ECP Group）。
l
20 – 选择DH组20。密钥的长度为384比特（ECP Group）。
l
21 – 选择DH组21。密钥的长度为521比特（ECP Group）。
l
24 – 选择DH组24。密钥的长度为2048比特（MODP Group with 256-bit Prime Order
Subgroup）。
使用no group命令恢复默配置。

<!-- 来源页 1443 -->
指定生命周期
Hillstone设备有两种衡量生命周期的方法，分别是按时间和按流量。当SA的流量或者时间达到特定值时，
SA就会过期，需要重新进行协商。指定P2提议的生命周期，在P2提议配置模式，使用以下命令：
lifetime seconds
l
seconds – 指定时间类型生命周期的时间长度，单位为秒。默认值是28800秒。
lifesize kilobytes
l
kilobytes – 指定流量类型周期的流量值，单位为字节。默认值是0，意义为没有周期流量限制。
使用以上两个命令no的形式恢复默认配置。即
no lifetime
no lifesize
配置隧道
通过IKE配置IPSec隧道，用户需要配置的选项有指定协议类型、ISAKMP网关、IKE安全提议、ID号、是否
分片以及防重放等。
创建IKE隧道
创建IKE隧道，在全局配置模式下，使用以下命令：
tunnel ipsec tunnel-name auto
l
tunnel-name - 指定所创建的IKE隧道的名称。
执行该命令后，CLI进入到IKE隧道配置模式。对IKE隧道的所有参数配置都需要在该模式下进行。
在全局配置模式下使用no tunnel ipsec tunnel-name auto删除指定的IKE隧道。
启用/禁用IPSec VPN隧道
默认情况下，IPSec VPN 隧道为启用状态。启用/禁用IPSec VPN隧道，在IKE隧道配置模式下，使用以下
命令：
l
启用IPSec VPN隧道：enable
l
禁用IPSec VPN隧道：disable

<!-- 来源页 1444 -->
启用/禁用IPSec VPN隧道的硬件快转功能
型号说明：
l
支持：SG-6000-A系列ASIC防火墙。
l
支持：SG-6000-K系列ASIC防火墙。
开启后将由专门的硬件芯片进行IPSec数据包的加密/解密，从而降低CPU负载，提升大流量场景下的转发性
能。该功能默认为开启状态。
启用/禁用IPSec VPN隧道的硬件快转功能，在IKE隧道配置模式下，使用以下命令：
l
启用：hardware-fast-forward enable
l
禁用：hardware-fast-forward disable
注意:
l
若未开启全局硬件快转功能，则IPSec VPN隧道的硬件快转功能将不生效。配置全局硬件快转
功能参见“防火墙> 硬件快转”章节。
l
若IPSec VPN隧道已关闭硬件快转功能，重新开启后需要手动执行clear isakmp sa命令进行
隧道重协商，使硬件快转功能生效。
指定IPSec协议的封装模式
为IKE隧道指定封装模式，可以是隧道模式或者传输模式，在IKE隧道配置模式下使用以下命令：
mode {transport | tunnel}
l
transport – 指定IPSec协议的封装模式为传输模式。
l
tunnel – 指定IPSec协议的封装模式为隧道模式。该模式为系统默认模式。
使用no mode命令恢复默认模式。
指定ISAKMP网关
为IKE隧道指定ISAKMP网关，请在IKE隧道配置模式下使用以下命令：
isakmp-peer peer-name
l
peer-name – 指定ISAKMP网关的名称。

<!-- 来源页 1445 -->
使用no isakmp-peer取消对ISAKMP网关的指定。
指定P2提议
为IKE隧道指定P2提议，请在IKE隧道配置模式下使用以下命令：
ipsec-proposal p2-name
l
p2-name – 指定P2提议的名称。用户最多可以为IKEv2隧道指定3个P2提议供对端选择使用。
使用no ipsec-proposal取消对P2提议的指定。
指定第二阶段ID
当用户需对IPSec VPN流量进行分流与限流时，需指定IKE第二阶段ID。第二阶段ID由本地网段、远程网段
和服务类型组成。配置时，需在本端和对端设备上对应配置，然后本端和对端将进行协商，最终创建一条
IKE IPSec隧道。用户可指定1个或多个第二阶段ID，即创建1条或多条IKE IPSec隧道。系统将根据每个隧道
的第二阶段ID对隧道中的流量进行分流、限流。
若不需对IPSec VPN流量分流与限流，可不配置。关于如何开启分流或限流功能，请查阅“配置IPSec VPN
流量分流与限流”章节。
为IKE IPSec隧道指定第二阶段ID，请在IKE隧道配置模式下使用以下命令：
id local ip-address/mask remote ip-address/mask service service-name
l
local ip-address/mask – 指定第二阶段的本地网段的IP/掩码。
l
remote ip-address/mask – 指定第二阶段的远程网段的IP/掩码。
l
service service-name – 指定第二阶段IKE IPSec隧道可传输的流量的服务或协议名称。
用户可配置最多256个第二阶段ID用于协商建立多个IKE隧道。
使用no id local ip-address/mask remote ip-address/mask service service-name命令恢复系统
默认配置。
注意:
l
默认情况下，IKE IPSec 隧道本端与对端的第二阶段ID需对应配置，若没有对应配置，将导致
协商失败。
配置IPSec VPN流量分流与限流
默认情况下，IPSec VPN流量分流与限流功能为启用状态，选择协议为IKEv2时需要先开启该功能。开启该
功能后，设备将根据第二阶段ID的配置，对进出IKE隧道的流量进行过滤，然后分流、限流；未匹配到第二

<!-- 来源页 1446 -->
阶段ID的流量将被丢弃。具体如下：
l
流量分流：设备根据第二阶段ID的配置，在IKE隧道入口对进入IKE隧道的流量进行分流。如果流量的源
IP地址、目的IP地址、以及流量的类型(service)匹配某一个第二阶段ID的配置，则该流量进入相应的
IKE隧道进行封装发送。如果没有匹配的第二阶段ID，则该流量被丢弃。
l
流量限流：设备根据第二阶段ID的配置，在IKE隧道出口对解封装后的流量进行限流。如果解封装后流量
的源IP地址、目的IP地址、以及流量的类型(service)匹配某一个第二阶段ID的配置，则该流量被接收设
备继续处理；如果流量无法匹配任何一个第二阶段ID的配置，则该流量被丢弃。
注意: 配置该功能前需确保已配置第二阶段ID且IKE隧道第二阶段协商成功。
开启流量分流与限流功能，在IKE隧道配置模式，使用如下命令：
check-id
使用no check-id关闭流量分流与限流功能。
配置自动连接功能
设备提供了两种触发建立SA的方式：自动方式和流量触发方式。
l
自动方式是指设备每60秒检查一次SA的状态，如果SA未建立则自动发起协商请求；
l
流量触发方式是指当有数据流量需要通过隧道进行传输时，该隧道才发起协商请求。
默认情况下，使用流量触发方式。若需要使用自动方式，请在IKE隧道配置模式下使用以下命令：
auto-connect
使用no auto-connect命令恢复系统的默认设置。
注意: 自动连接功能仅在对端IP地址为静态类型且本端可以作为发起端时有效。
配置分片功能
用户可以指定是否允许转发设备将包进行分片处理。为IKE隧道配置分片功能，请在IKE隧道配置模式下使用
以下命令：
df-bit {copy | clear | set}

<!-- 来源页 1447 -->
l
copy – 直接从发包端拷贝IP包的DF选项。该选项为系统默认选项。
l
clear – 允许转发设备对包做分片处理。
l
set – 不允许转发设备对包做分片处理。
使用no df-bit恢复系统的默认设置。
配置VPN监控及冗余备份功能
Hillstone设备能够监测指定的VPN隧道是否连通，并且能够实现两条或者多条VPN隧道的备份或者分流。
该功能对基于路由的VPN以及基于策略的VPN均有效。具体实现包括以下两种环境：
l
为同一个远程对端配置备份VPN隧道，并且在任意时刻只有一个隧道处于活动状态。最初，主VPN隧道
处于活动状态，如果监测到该主隧道中断，Hillstone设备会通过备份隧道重新传输信息流；
l
为同一个远程对端配置了两个或者多个VPN隧道，所有隧道都同时处于活动状态，并且通过等价多径路
由（ECMP）实现负载均衡。如果监测到隧道中断，Hillstone设备会通过其它隧道重新传输信息流。
VPN监控功能支持通过Ping报文对目标隧道进行监测。默认情况下，该功能是关闭的。配置VPN监控功能，
请在IKE IPSec隧道配置模式下使用以下命令：
vpn-track [A.B.C.D] [src-ip A.B.C.D] [interval time-value] [threshold value]
l
A.B.C.D – 指定监测目标的IP地址。当对端设备为Hillstone设备时，如果不指定该参数，系统默认为对
端IP地址。此IP地址不能为“0.0.0.0”和“255.255.255.255”。
l
src-ip A.B.C.D – 指定发送Ping监测报文的源IP地址。当对端设备为Hillstone设备时，如果不指定该
参数，系统默认为出接口IP地址。此IP地址不能为“0.0.0.0”和“255.255.255.255”。
l
interval time-value – 指定发送Ping监测报文的时间间隔，单位为秒。范围是1到255秒。默认值是
10秒。
l
threshold value – 指定判断监测失败的警戒值。如果系统连续未收到该参数指定个数的响应报文，就
判断为监测失败，即目标隧道中断。取值范围是1到255。默认值是10。
使用no vpn-track命令取消VPN监控功能的配置。
VPN监控功能包括active和dead两种状态。用户可以使用相应的show命令在CLI的任何模式下查看VPN监
控功能的状态以及配置信息：
l
查看VPN监控功能的状态：show ipsec sa {id}
l
查看VPN监控功能的配置情况：show tunnel ipsec {manual | auto} {tunnel-name}
例如：

<!-- 来源页 1448 -->
查看VPN监控功能状态
hostname(config)# show ipsec sa 5
ID: 1
scpu: 0
VPN Name: vpn1
L2tp port: 1
Duration(S): 1375459
Last setup time: 2022-03-08 22:09:53
Last teardown time: 2022-03-09 06:09:54
Tear down reason: a lifetime timeout occurred
Teardowns today: 0
Outbound
Gateway: 1.1.1.2
......
Sending rate(KB/s): 0
Status: Active
Inbound
Gateway: 1.1.1.2
......
Receiving rate(KB/s): 0
Status: Active
查看VPN监控功能配置
hostname(config)# show tunnel ipsec auto vpn1
Name: vpn1
mode: tunnel
......
vpn-track: enable
tracknotify: enable
vpntrack destination 1.1.1.1

<!-- 来源页 1449 -->
vpntrack source ip: 2.2.2.2
vpntrack interval: 3
vpntrack threshold: 3
注意: 关于VPN监控及冗余备份的具体实例，请参阅VPN监控及冗余备份的具体实例一节。
开启/关闭VPN隧道状态通知功能
默认情况下，VPN隧道状态通知功能为关闭状态。在开启VPN隧道状态通知功能后，如果是基于路由的
VPN，系统一旦监测到中断的VPN隧道，会立即通知路由模块中断的VPN隧道信息并进行隧道路由的更新处
理；如果是基于策略的VPN，系统一旦监测到中断的VPN隧道，会立即通知策略模块中断的VPN隧道信息并
进行隧道策略的更新处理。用户可以通过命令开启/关闭VPN隧道状态通知功能，对中断状态下的VPN隧道
信息进行通知。开启/关闭VPN隧道状态通知功能，在IKE IPSec隧道配置模式下，使用以下命令：
l
开启：tunnel-state-notify
l
关闭：no tunnel-state-notify
指定描述信息
为所配置的IKE隧道指定描述信息，请在IKE IPSec隧道配置模式下使用以下命令：
description string
l
string – IKE隧道的描述信息。
使用no description命令删除IKE隧道的描述信息。
配置XAUTH
XAUTH是对IKE协议的扩展和增强，允许设备结合已配置的认证服务器（RADIUS和本地AAA服务器）对试
图访问IPSec VPN网络的用户进行身份认证，目前大量应用在移动终端上。远程用户发起VPN连接请求后，
设备上的XAUTH服务器会中断VPN协商过程并要求用户输入有效的用户名和密码进行认证，认证成功后会继
续VPN协商过程并为合法的客户端分配IP地址，否则会中断VPN连接。
如果已配置XAUTH地址池，用户认证成功后，设备会继续VPN协商过程并为合法的客户端分配IP地址。如果
未配置XAUTH地址池，在开启自动生成路由功能后，设备会根据已配置的IKE VPN隧道第二阶段ID自动生成
VPN路由条目。有关自动生成路由功能的更多信息，请参考“VPN > IPSec协议> 配置IPSec VPN功能>
IKEv1 VPN > 配置隧道> 配置自动生成路由功能”。有关第二阶段ID的更多信息，请参考“VPN > IPSec
协议> 配置IPSec VPN功能> IKEv1 VPN > 配置隧道> 指定第二阶段ID”。
有关认证服务器配置的更多信息，请参考《用户认证》的“"配置AAA" 在第1196页”部分。

<!-- 来源页 1450 -->
XAUTH的配置包括：
l 启用XAUTH服务器
l 配置XAUTH地址池
l 绑定地址池到XAUTH服务器
l 配置IP用户绑定和IP角色绑定规则
l 配置推送到客户端的WINS服务器或DNS服务器
启用XAUTH服务器
XAUTH服务器在设备上默认是禁用的。启用XAUTH服务器，在ISAKMP网关配置模式下，使用以下命令：
xauth server
在ISAKMP网关配置模式下，使用该命令no的形式禁用XAUTH服务器：
no xauth server
配置XAUTH地址池
该参数为可选配置。XAUTH通过地址池为客户端分配IP地址。当客户端连接XAUTH服务端成功后，设备端
会从地址池里取出一个IP地址与其它相关参数（如DNS服务器地址、WINS服务器地址等）一起分配给客户
端，支持IPv4和IPv6地址。
配置XAUTH IPv4地址池
创建XAUTH IPv4地址池，在全局配置模式下，使用以下命令：
xauth pool pool-name
l
pool-name - 指定XAUTH IPv4地址池名称并进入XAUTH IPv4地址池配置模式。如果指定的名称已存
在，系统会直接进入XAUTH IPv4地址池配置模式。
在XAUTH IPv4地址池配置模式下，使用该命令no的形式删除指定的XAUTH IPv4地址池：
no xauth pool pool-name
配置XAUTH IPv6地址池
创建XAUTH IPv6地址池，在全局配置模式下，使用以下命令：
xauth pool-ipv6 pool-name
l
pool-name - 指定XAUTH IPv6地址池名称并进入XAUTH IPv6地址池配置模式，最多支持配置16个
IPv6地址池。如果指定的名称已存在，系统会直接进入XAUTH IPv6地址池配置模式。

<!-- 来源页 1451 -->
在XAUTH IPv6地址池配置模式下，使用该命令no的形式删除指定的XAUTH IPv6地址池：
no xauth pool-ipv6 pool-name
指定XAUTH地址池中允许分配的IP地址范围
该参数为可选配置。指定XAUTH地址池中允许分配的IP地址范围，在XAUTH IPv4或IPv6地址池配置模式
下，使用以下命令：
address start-ip end-ip {netmask mask | prefix-len prefix}
l
start-ip - 指定XAUTH地址池的起始IP地址。
l
end-ip - 指定XAUTH地址池的结束IP地址。
l
mask - 指定IPv4地址的网络掩码。
l
prefix - 指定IPv6地址的前缀长度。
在XAUTH IPv4或IPv6地址池配置模式下，使用该命令no的形式删除指定的IP地址范围：
no address
指定XAUTH保留地址池
该参数为可选配置。保留地址池中的IP地址为XAUTH地址池中的部分IP地址，当XAUTH服务器从地址池里
取出IP地址分配给客户端时，可以保留已经被占用的部分IP地址，不进行分配。
指定XAUTH保留地址池，在XAUTH IPv4或IPv6地址池配置模式下，使用以下命令：
exclude-address start-ip end-ip
l
start-ip - 指定XAUTH保留地址池的起始IP地址。
l
end-ip - 指定XAUTH保留地址池的结束IP地址。
在XAUTH IPv4或IPv6地址池配置模式下，使用该命令no的形式删除指定的保留地址池IP范围：
no exclude-address
绑定地址池到XAUTH服务器
该参数为可选配置。XAUTH地址池只有在绑定到XAUTH服务器后才会生效。将指定的XAUTH地址池绑定到
XAUTH服务器，在ISAKMP网关配置模式下，使用以下命令：
xauth pool-name pool-name
l
pool-name - 指定绑定的IPv4地址池名称。
xauth pool6-name pool-name

<!-- 来源页 1452 -->
l
pool-name - 指定绑定的IPv6地址池名称。
在ISAKMP网关配置模式下，使用该命令no的形式取消地址池绑定：
no xauth pool-name
no xauth pool6-name
配置IP用户绑定和IP角色绑定规则
该参数为可选配置。XAUTH服务器通过创建和执行IP地址绑定规则来满足客户端的固定IP地址需求。IP地址
绑定规则包括IP用户绑定规则和IP角色绑定规则。IP用户绑定规则将客户端用户与已配置地址池中的某个固
定IP地址绑定，当客户端连接成功后，设备端会将绑定的IP地址分配给客户端；IP角色绑定规则是将角色与
已配置地址池中的某一IP地址范围绑定，当此客户端连接成功后，设备端会从绑定的地址范围中取出一个IP
地址分配给客户端。
当XAUTH通过地址池给客户端分配IP地址时，系统会按照一定的顺序对客户端的IP地址绑定规则进行检查，
决定如何为客户端分配IP地址：
1. 检查是否已为客户端用户配置IP用户绑定规则，如果是，则将绑定的IP地址分配给客户端；否则，需要进一步检
查。注意，如果此IP用户绑定规则中的IP地址已被占用，则该用户无法登录。
2. 检查是否已为客户端用户配置IP角色绑定规则，如果是，则从绑定的地址范围中取出一个IP地址分配给客户端；
否则，在未绑定的IP地址范围中取出一个IP地址分配给客户端。注意，如果绑定的地址范围中的地址都已经被分
配，则该用户无法登录。
注意: IP用户绑定规则中的IP地址和IP角色绑定规则中的IP地址不能重叠。
配置IP用户绑定规则
配置IP用户绑定规则，在XAUTH IPv4或IPv6地址池配置模式下使用以下命令：
ip-binding user user-name ip ip-address
l
user user-name - 指定客户端用户名。
l
ip ip-address - 指定绑定的IP地址。此地址必须为地址池中可以分配的地址。
在XAUTH IPv4或IPv6地址池配置模式下，使用该命令no的形式取消对特定用户IP用户绑定规则的配置：
no ip-binding user user-name
配置IP角色绑定规则
配置IP角色绑定规则，在XAUTH IPv4或IPv6地址池配置模式下使用以下命令：

<!-- 来源页 1453 -->
ip-binding role role-name ip-range start-ip end-ip
l
role role-name - 指定角色名称。
l
ip-range start-ip end-ip - 指定绑定的IP范围的起始IP地址start-ip和结束IP地址end-ip。此地址
范围必须为地址池中可以分配的地址范围。
在XAUTH IPv4或IPv6地址池配置模式下使用该命令no的形式取消对特定角色的IP角色绑定规则的配置：
no ip-binding role role-name
修改IP角色绑定规则排列顺序
该参数为可选配置。一个用户可以绑定到一个或者多个角色，不同角色可以配置不同的IP角色绑定规则。对
于绑定到多个角色且多个角色有相应的IP角色绑定规则的用户，设备会对IP角色绑定规则进行顺序查找，然
后按照查找到的相匹配的第一条规则为用户分配地址。默认情况下，系统会将新创建的规则放到所有规则的
末尾，管理员可以移动已有的IP角色绑定规则从而改变规则的排列顺序。改变规则的排列顺序，在XAUTH
IPv4或IPv6地址池配置模式下使用以下命令：
move role-name1 {before role-name2 | after role-name2| top | bottom}
l
role –name1 – 指定被移动的IP角色绑定规则的角色名称。
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
配置推送到客户端的WINS/DNS服务器
该参数为可选配置。配置DNS服务器，在XAUTH IPv4或IPv6地址池配置模式下使用以下命令：
dns address1 [address2]
l
address1 - 指定DNS服务器IP地址。用户最多可配置2个DNS服务器。
在XAUTH IPv4或IPv6地址池配置模式下，使用该命令no的形式取消对DNS服务器的指定：
no dns
该参数为可选配置。配置WINS服务器，在XAUTH IPv4地址池配置模式下使用以下命令：
wins address1 [address2]

<!-- 来源页 1454 -->
l
address1 - 指定WINS服务器IP地址。用户最多可配置2个WINS服务器。
在XAUTH IPv4地址池配置模式下，使用该命令no的形式取消对WINS服务器的指定：
no wins
强制断开客户端XAUTH连接
XAUTH服务端可以通过命令强制断开某个客户端与设备端的连接。强制断开客户端XAUTH连接，在执行模
式使用以下命令：
exec xauth isakmp-peer-name kickout user-name
l
isakmp-peer-name - 指定ISAKMP对端的名称。
l
user-name - 指定被强制断开连接的用户名称。
配置非根VSYS隧道配额
配置非根VSYS的IPSec隧道资源配额，在VSYS Profile配置模式下使用以下命令：
tunnel-ipsec max max-num reserve reserve-num
l
max max-num reserve reserve-num– 指定非根VSYS中IPSec隧道数的最大配额（max-num
reserve）和预留配额（reserve reserve-num）。最大配额和预留配额根据不同平台取值范围不同。
预留配额不能超过最大配额。最大配额取值范围为0至max，默认值为max；预留配额的最小值为0。
注意: max为设备支持配置IPSec VPN的最大值，可在全局配置模式下，使用show capacity all
命令查看。
在VSYS Profile配置模式下使用该命令no的形式删除配额：
no tunnel-ipsec max max-num reserve reserve-num
SN准入名单
系统支持将IPSec VPN建立权限绑定到特定物理设备，通过SN准入名单来管控允许与中心端建立IPSec
VPN的分支端设备，实现对网络的严格管控。由于每个物理设备的设备序列号（SN号）具有唯一性，通过验
证SN号，可有效规避以下风险场景：当管理员离职等情况导致VPN密钥意外泄露时，未授权设备通过冒用合
法身份发起IPsec VPN连接请求，进而非法入侵公司网络。
注意: 系统最多支持创建2万条SN准入条目。

<!-- 来源页 1455 -->
进入SN准入配置模式
进入SN准入配置模式，在全局配置模式下，使用以下命令：
vpn-trusted-sn
配置SN准入条目
配置SN准入条目，在SN准入配置模式下，使用以下命令：
sn serial-number [description SN-description]
l
serial-number - 指定需要加入SN准入名单的设备SN号。SN号的长度应为16个字符。
l
SN-description - 指定准入条目的描述信息。取值范围为1-128个字符。
删除SN准入条目，在SN准入配置模式下，使用以下命令：
no sn serial-number
查看SN准入条目
查看已创建的SN准入条目信息，在任意模式下，使用以下命令：
show vpn-trusted-sn
以下是返回结果示例：
hostname(config)# show vpn-trusted-sn
Total count: 6
=================================================================
SN Description
------------------------------------------------------------------
A12B456C789D0EFG 设备A
XYZ1234567890ABC 设备B
1234567891234567
abcdefghijklmnop
===================================================================
在IPSec VPN隧道中绑定前向纠错（FEC）模板
开始之前
l 阅读"前向纠错（FEC）介绍" 在第165页。
l 阅读"前向纠错（FEC）技术应用场景" 在第165页介绍。
l 阅读"前向纠错（FEC）技术实现原理" 在第166页介绍。

<!-- 来源页 1456 -->
l 阅读"前向纠错（FEC）使用限制和注意事项" 在第167页。
l 阅读"IPSec VPN隧道前向纠错（FEC）配置流程" 在第167页。
在IPSec VPN隧道中绑定前向纠错（FEC）模板，需先进入IKE隧道配置模式或手工密钥VPN配置模式。
绑定前向纠错（FEC）模板
用户需根据业务规划需求，将前向纠错（FEC）模板绑定至对应的IPSec VPN隧道中。为确保前向纠错
（FEC）功能正常运行，IPSec VPN隧道两端的设备，均需绑定前向纠错（FEC）模板。
注意: 仅当IPSec VPN隧道的“封装模式”为“隧道模式”时，前向纠错（FEC）功能才生效。
绑定前向纠错（FEC）模板，在IKE隧道配置模式或手工密钥VPN配置模式下，使用以下命令：
fec-profile profile-name
l
profile-name - 指定需要绑定的前向纠错模板名称。
在IKE隧道配置模式或手工密钥VPN配置模式下，使用以下命令，解除前向纠错（FEC）模板的绑定：
no fec-profile
示例：
hostname(config)# tunnel ipsec vpn1 auto
hostname(config-tunnel-ipsec-auto)# fec-profile profile1
hostname(config-tunnel-ipsec-auto)# exit
下一步
为IPSec VPN隧道绑定前向纠错（FEC）模板后，请根据"IPSec VPN隧道前向纠错（FEC）配置流程" 在第
167页，执行相应的操作：
l 基于策略的IPSec VPN实现FEC功能：配置相应的策略规则，并确保该策略规则绑定了此IPSec VPN隧道，以及启
用了前向纠错（FEC）功能。
l 基于路由的IPSec VPN实现FEC功能：创建隧道接口，并绑定该IPSec VPN隧道。
显示IPSec配置信息
用户可以使用相应的show命令在CLI的任何模式下查看IPSec功能的配置信息。
查看P1提议的配置信息：show isakmp proposal [p1-name]
查看ISAKMP网关的配置信息：show isakmp peer [peer-name]

<!-- 来源页 1457 -->
查看P2提议的配置信息：show ipsec proposal [proposal-name]
查看手工密钥VPN隧道的配置信息：show tunnel ipsec manual [tunnel-name]
查看智能链路配置与切换信息：show ipsec smart-link-profile [profile-name]
查看IPSec隧道的配置信息：show tunnel ipsec auto [tunnel-name]
查看第一阶段安全联盟信息：show isakmp sa [v1 | v2] [peer_ip] [worker worker-id]
l
v1 | v2 - 指定查看IKEv1或IKEv2的第一阶段安全联盟信息。
l
peer_ip - 显示指定对端IP地址的第一阶段安全联盟信息。
l
worker-id - 显示指定VPN进程的第一阶段安全联盟信息。
清除第一阶段安全联盟信息：clear isakmp sa [v1 | v2] [peer_ip | cookie ] [worker worker-id]
l
v1 | v2 - 指定清除IKEv1或IKEv2的第一阶段安全联盟信息。
l
peer_ip - 清除指定对端IP地址的第一阶段安全联盟信息。
l
cookie - 清除指定Cookie值的第一阶段安全联盟信息。
l
worker-id - 清除指定VPN进程的第一阶段安全联盟信息。
查看第二阶段安全联盟信息：show ipsec sa [v1 | v2] [id | active | inactive] [worker worker-id]
l
v1 | v2 - 指定查看IKEv1或IKEv2的第二阶段安全联盟信息。
l
id | active | inactive - 显示指定的第二阶段安全联盟信息（id ）；显示活跃的第二阶段安全联盟信息
（active）；或者显示非活跃的第二阶段安全联盟信息（inactive）。
l
worker worker-id - 显示指定VPN进程的第二阶段安全联盟信息。
清除第二阶段安全联盟信息：clear ipsec sa [v1 | v2] [id ] [workerworker-id]
l
v1 | v2 - 指定清除IKEv1或IKEv2的第二阶段安全联盟信息。
l
id - 清除指定ID的第二阶段安全联盟信息。
l
workerworker-id - 清除指定VPN进程的第二阶段安全联盟信息。
查看XAUTH地址池信息：show xauth pool [pool-name]
查看接入的XAUTH用户信息：show xauth client isakmp-peer-name [user user-name]
查看VPN进程相关统计信息：show vpnd [isakmp-peer-name] statistics [clear]
l
isakmp-peer-name - 显示指定ISAKMP网关名称的VPN进程统计信息。
l
clear - 清除VPN进程统计信息。

<!-- 来源页 1458 -->
查看开启多进程功能相关信息：show cp-multi-cores
查看自定义IKE协商端口池范围：show ike-port-pool
查看TCP连接哈希表
TCP连接哈希表用于记录IPSec VPN在使用TCP协议协商过程中的TCP连接状态。用户可以查看每条连接的
本端IP地址、对端IP地址以及TCP连接状态等信息。
查看TCP连接哈希表，在任意模式下，使用以下命令：
show vpnd tcp-conn-hash-table [remote-ip ip-address [local-ip ip-address [worker id] |
worker id] | local-ip ip-address [worker id] | worker id]
l
remote-ip ip-address - 查询指定对端IP地址的TCP连接哈希表。
l
local-ip ip-address - 查询指定本端IP地址的TCP连接哈希表。
l
worker id - 查询指定进程id的TCP连接哈希表，若不配置默认为0。worker id为开启VPN多进程功能
后的进程id。
返回结果示例：
hostname# show vpnd tcp-conn-hash-tableworker2
ipsec tcp conn table:
total number:70, workerid 2
Flag: 0x01 - The tcp conn bind with phase1 isakmp sa
0x02 - The tcp conn bind with phase2 ipsec sa
==============================================================================
==================== remote/对端IP | local/对端IP | status/连接状态| flag | sequence/序列
号| ack_sequence/确认序列号
------------------------------------------------------------------------------------------------
--
17.0.83.1:41338 27.1.83.1:500 ESTABLISHED 0x01 535657718 2154957042
17.0.101.1:500 27.1.101.1:41849 ESTABLISHED 0x01 1226094502 169391233
17.0.14.1:41545 27.1.14.1:500 ESTABLISHED 0x01 3337334006 3940635278
17.0.25.1:65023 27.1.25.1:500 ESTABLISHED 0x02 1026908445 2615852491
17.0.0.1:500 27.1.0.1:42114 ESTABLISHED 0x01 1555689654 2689408712
==============================================================================
==================

<!-- 来源页 1459 -->
IPSec VPN配置举例
本节介绍通过手工密钥VPN和IKE VPN两种方式建立安全联盟的具体举例、VPN监控及冗余备份的具体举例
以及XAUTH的配置举例。
l "例：手工密钥VPN配置举例" 在第1457页
l "例：IKE VPN配置举例" 在第1461页
l "例：基于路由的VPN监控及冗余备份功能配置举例" 在第1467页
l "例：基于策略的VPN监控及冗余备份功能配置举例" 在第1474页
l "例：HA Peer模式支持IPsec VPN配置举例" 在第1481页
l "例：XAUTH配置举例" 在第1486页
例：手工密钥VPN配置举例
手工密钥VPN隧道要求安全联盟的所有相关配置都由用户手动一一指定。请看以下实例。
组网需求
在Hillstone设备A和Hillstone设备B之间建立一个安全隧道，PC1作Hillstone设备A端的主机，IP地址为
188.1.1.2，网关为188.1.1.1；server1作为Hillstone设备B端的服务器，IP地址为10.110.88.210，网
关是10.110.88.220。要求对PC1代表的子网（188.1.1.0/24）与Server1代表的子网
（10.110.88.0/24）之间的数据流进行安全保护（通过基于策略的VPN方式实现VPN的应用）。安全协议
采用ESP协议，加密算法采用3DES，验证算法采用SHA1，压缩算法采用DEFLATE。下图为该需求的组网
图。
配置步骤
第一步：配置Hillstone设备接口。
Hillstone设备A
hostname(config)# interface ethernet0/0

<!-- 来源页 1460 -->
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 188.1.1.1/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 192.168.1.2/24
hostname(config-if-eth0/1)# exit
Hillstone设备B
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 10.110.88.220/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/0
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 192.168.1.3/24
hostname(config-if-eth0/1)# exit
第二步：配置路由。
Hillstone设备A
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 10.110.88.0/24 192.168.1.3
hostname(config-vrouter)# exit
Hillstone设备B
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 188.1.1.0/24 192.168.1.2
hostname(config-vrouter)# exit
第三步：手动配置名为VPN1的隧道。
Hillstone设备A
hostname(config)# tunnel ipsec vpn1 manual
hostname(config-tunnel-ipsec-manual)# interface ethernet0/1

<!-- 来源页 1461 -->
hostname(config-tunnel-ipsec-manual)# protocol esp
hostname(config-tunnel-ipsec-manual)# peer 192.168.1.3
hostname(config-tunnel-ipsec-manual)# hash sha
hostname(config-tunnel-ipsec-manual)# hash-key inbound 1234 outbound 5678
hostname(config-tunnel-ipsec-manual)# encryption 3des
hostname(config-tunnel-ipsec-manual)# encryption-key inbound 00ff outbound 123a
hostname(config-tunnel-ipsec-manual)# compression deflate
hostname(config-tunnel-ipsec-manual)# spi 6001 6002
hostname(config-tunnel-ipsec-manual)# exit
Hillstone设备B
hostname(config)# tunnel ipsec vpn1 manual
hostname(config-tunnel-ipsec-manual)# interface ethernet0/1
hostname(config-tunnel-ipsec-manual)# protocol esp
hostname(config-tunnel-ipsec-manual)# peer 192.168.1.2
hostname(config-tunnel-ipsec-manual)# hash sha
hostname(config-tunnel-ipsec-manual)# hash-key inbound 5678 outbound 1234
hostname(config-tunnel-ipsec-manual)# encryption 3des
hostname(config-tunnel-ipsec-manual)# encryption-key inbound 123a outbound 00ff
hostname(config-tunnel-ipsec-manual)# compression deflate
hostname(config-tunnel-ipsec-manual)# spi 6002 6001
hostname(config-tunnel-ipsec-manual)# exit
第四步：配置Hillstone设备策略规则。
Hillstone设备A
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# src-addr any

<!-- 来源页 1462 -->
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action from tunnel vpn1
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
Hillstone设备B
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action tunnel vpn1
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action from tunnel vpn1
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
完成以上配置后，Hillstone设备A和Hillstone设备B之间的安全隧道便建立成功了。子网
（188.1.1.0/24）与server1代表的子网（10.110.88.0/24）之间的数据流将会被加密传输。

<!-- 来源页 1463 -->
例：IKE VPN配置举例
本节介绍通过IKE方式创建安全联盟的实例。
组网需求
在Hillstone设备A和Hillstone设备B之间建立一个安全隧道，PC1作为Hillstone设备A端的主机，IP地址
为10.1.1.1，网关为10.1.1.2；Server1作为Hillstone设备B端的服务器，IP地址为192.168.1.1，网关是
192.168.1.2。要求对PC1代表的子网（10.1.1.0/24）与server1代表的子网（192.168.1.0/24）之间的
数据流进行安全保护（通过基于路由的VPN方式实现VPN的应用）。安全协议采用ESP协议，加密算法采用
3DES，验证算法采用SHA1，压缩算法采用DEFLATE。组网图请参考下图：
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

<!-- 来源页 1464 -->
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 192.168.1.2/24
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
hostname(config-policy-rule)# dst-zone untrust
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

<!-- 来源页 1465 -->
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
Hillstone设备B
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
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

<!-- 来源页 1466 -->
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
第三步：配置路由。
Hillstone设备A
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 192.168.1.0/24 tunnel1
hostname(config-vrouter)# exit
Hillstone设备B
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 10.1.1.0/24 tunnel1
hostname(config-vrouter)# exit
第四步：配置P1提议。
Hillstone设备A
hostname(config)# isakmp proposal p1
hostname(config-isakmp-proposal)# authentication pre-share
hostname(config-isakmp-proposal)# group 2
hostname(config-isakmp-proposal)# hash sha
hostname(config-isakmp-proposal)# encryption 3des
hostname(config-isakmp-proposal)# exit

<!-- 来源页 1467 -->
Hillstone设备B
hostname(config)# isakmp proposal p1
hostname(config-isakmp-proposal)# authentication pre-share
hostname(config-isakmp-proposal)# group 2
hostname(config-isakmp-proposal)# hash sha
hostname(config-isakmp-proposal)# encryption 3des
hostname(config-isakmp-proposal)# exit
第五步：配置ISAKMP网关。
Hillstone设备A
hostname(config)# isakmp peer east
hostname(config-isakmp-peer)# interface ethernet0/1
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# peer 1.1.1.2
hostname(config-isakmp-peer)# pre-share hello1
hostname(config-isakmp-peer)# exit
Hillstone设备B
hostname(config)# isakmp peer west
hostname(config-isakmp-peer)# interface ethernet0/1
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# peer 1.1.1.1
hostname(config-isakmp-peer)# pre-share hello1
hostname(config-isakmp-peer)# exit
第六步：配置P2提议。
Hillstone设备A
hostname(config)# ipsec proposal p2
hostname(config-ipsec-proposal)# protocol esp
hostname(config-ipsec-proposal)# hash sha
hostname(config-ipsec-proposal)# encryption 3des

<!-- 来源页 1468 -->
hostname(config-ipsec-proposal)# compression deflate
hostname(config-ipsec-proposal)# exit
Hillstone设备B
hostname(config)# ipsec proposal p2
hostname(config-ipsec-proposal)# protocol esp
hostname(config-ipsec-proposal)# hash sha
hostname(config-ipsec-proposal)# encryption 3des
hostname(config-ipsec-proposal)# compression deflate
hostname(config-ipsec-proposal)# exit
第七步：配置名为VPN的隧道。
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

<!-- 来源页 1469 -->
hostname(config-if-tun1)# exit
完成以上配置后，Hillstone设备A和Hillstone设备B之间的安全隧道便建立成功了。子网（10.1.1.0/24）
与Server1代表的子网（192.168.1.0/24）之间的数据流将会被加密传输。
例：基于路由的VPN监控及冗余备份功能配置举例
该节介绍基于路由的VPN监控及冗余备份功能配置实例。
组网需求
在Hillstone设备A和Hillstone设备B之间配置IKE VPN隧道VPN1 tunnel和VPN2 tunnel，server作为
Hillstone设备A端的服务器，IP地址为192.168.100.8，网关是192.168.100.1；PC作为Hillstone设备B
端的主机，IP地址为172.16.10.8，网关为172.16.10.1。要求实现VPN1 tunnel和VPN2 tunnel的VPN
监控，并当主隧道（VPN1 tunnel）链路发生故障时，流量转向备份隧道（VPN2 tunnel）；主隧道恢复
正常时，流量切换回主隧道。组网图参见下图：
配置步骤
第一步：配置Hillstone设备A：
配置接口：

<!-- 来源页 1470 -->
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 192.168.100.1/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 10.10.10.1/24
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/4
hostname(config-if-eth0/4)# zone untrust
hostname(config-if-eth0/4)# ip address 20.20.20.1/24
hostname(config-if-eth0/4)# exit
配置P1提议
hostname(config)# isakmp proposal p1
hostname(config-isakmp-proposal)# authentication pre-share
hostname(config-isakmp-proposal)# group 2
hostname(config-isakmp-proposal)# hash md5
hostname(config-isakmp-proposal)# encryption des
hostname(config-isakmp-proposal)# exit
配置ISAKMP网关：
hostname(config)# isakmp peer gwa-peer-1
hostname(config-isakmp-peer)# interface ethernet0/1
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# peer 10.10.10.2
hostname(config-isakmp-peer)# pre-share U8FdHNEEBz6sNn5Mvqx3yWuLRWce
hostname(config-isakmp-peer)# exit
hostname(config)# isakmp peer gwa-peer-2
hostname(config-isakmp-peer)# interface ethernet0/4
hostname(config-isakmp-peer)# isakmp-proposal p1

<!-- 来源页 1471 -->
hostname(config-isakmp-peer)# peer 20.20.20.2
hostname(config-isakmp-peer)# pre-share i39jnnNiCSh9rXb77oGA7Fg7BNQy
hostname(config-isakmp-peer)# exit
配置P2提议：
hostname(config)# ipsec proposal p2
hostname(config-ipsec-proposal)# protocol esp
hostname(config-ipsec-proposal)# hash md5
hostname(config-ipsec-proposal)# encryption des
hostname(config-ipsec-proposal)# exit
配置VPN隧道：
hostname(config)# tunnel ipsec vpn1-tunnel auto
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# isakmp-peer gwa-peer-1
hostname(config-tunnel-ipsec-auto)# vpn-track interval 3 threshold 9
hostname(config-tunnel-ipsec-auto)# track-event-notify enable
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)# tunnel ipsec vpn2-tunnel auto
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# isakmp-peer gwa-peer-2
hostname(config-tunnel-ipsec-auto)# vpn-track interval 3 threshold 9
hostname(config-tunnel-ipsec-auto)# track-event-notify enable
hostname(config-tunnel-ipsec-auto)# auto-connect
hostname(config-tunnel-ipsec-auto)# exit
创建隧道接口并绑定VPN隧道：
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone untrust
hostname(config-if-tun1)#
hostname(config-if-tun1)# tunnel ipsec vpn1-tunnel
hostname(config-if-tun1)# exit

<!-- 来源页 1472 -->
hostname(config)# interface tunnel2
hostname(config-if-tun2)# zone untrust
hostname(config-if-tun2)# ip address 10.2.2.1/24
hostname(config-if-tun2)# tunnel ipsec vpn2-tunnel
hostname(config-if-tun2)# exit
配置路由：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)#
hostname(config-vrouter)# ip route 172.16.10.0/24 tunnel2 20
hostname(config-vrouter)# exit
配置策略：
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
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

<!-- 来源页 1473 -->
hostname(config)#
第二步：配置Hillstone设备B：
配置接口：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 172.16.10.1/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 10.10.10.2/24
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/4
hostname(config-if-eth0/4)# zone untrust
hostname(config-if-eth0/4)# ip address 20.20.20.2/24
hostname(config-if-eth0/4)# exit
配置P1提议
hostname(config)# isakmp proposal p1
hostname(config-isakmp-proposal)# authentication pre-share
hostname(config-isakmp-proposal)# group 2
hostname(config-isakmp-proposal)# hash md5
hostname(config-isakmp-proposal)# encryption des
hostname(config-isakmp-proposal)# exit
配置ISAKMP网关：
hostname(config)# isakmp peer gwb-peer-1
hostname(config-isakmp-peer)# interface ethernet0/1
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# peer 10.10.10.1
hostname(config-isakmp-peer)# pre-share U8FdHNEEBz6sNn5Mvqx3yWuLRWce

<!-- 来源页 1474 -->
hostname(config-isakmp-peer)# exit
hostname(config)# isakmp peer gwb-peer-2
hostname(config-isakmp-peer)# interface ethernet0/4
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# peer 20.20.20.1
hostname(config-isakmp-peer)# pre-share i39jnnNiCSh9rXb77oGA7Fg7BNQy
hostname(config-isakmp-peer)# exit
配置P2提议：
hostname(config)# ipsec proposal p2
hostname(config-ipsec-proposal)# protocol esp
hostname(config-ipsec-proposal)# hash md5
hostname(config-ipsec-proposal)# encryption des
hostname(config-ipsec-proposal)# exit
配置VPN隧道：
hostname(config)# tunnel ipsec vpn1-tunnel auto
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# isakmp-peer gwb-peer-1
hostname(config-tunnel-ipsec-auto)# vpn-track interval 3 threshold 9
hostname(config-tunnel-ipsec-auto)# track-event-notify enable
hostname(config-tunnel-ipsec-auto)# auto-connect
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)# tunnel ipsec vpn2-tunnel auto
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# isakmp-peer gwb-peer-2
hostname(config-tunnel-ipsec-auto)# vpn-track interval 3 threshold 9
hostname(config-tunnel-ipsec-auto)# track-event-notify enable
hostname(config-tunnel-ipsec-auto)# auto-connect
hostname(config-tunnel-ipsec-auto)# exit
创建隧道接口并绑定VPN隧道：

<!-- 来源页 1475 -->
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone untrust
hostname(config-if-tun1)# ip address 10.1.1.2/24
hostname(config-if-tun1)# tunnel ipsec vpn1-tunnel
hostname(config-if-tun1)# exit
hostname(config)# interface tunnel2
hostname(config-if-tun2)# zone untrust
hostname(config-if-tun2)# ip address 10.2.2.2/24
hostname(config-if-tun2)# tunnel ipsec vpn2-tunnel
hostname(config-if-tun2)# exit
配置路由：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 192.168.100.0/24 tunnel1 1
hostname(config-vrouter)# ip route 192.168.100.0/24 tunnel2 2
hostname(config-vrouter)# exit
配置策略：
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any

<!-- 来源页 1476 -->
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
由于本例中VPN终端设备都是Hillstone设备，因此可使用缺省源和目标地址进行VPN监控。
例：基于策略的VPN监控及冗余备份功能配置举例
该节介绍基于策略的VPN监控及冗余备份功能配置实例。
组网需求
在Hillstone设备A和Hillstone设备B之间配置IKE VPN隧道VPN1 tunnel和VPN2 tunnel，server作为
Hillstone设备A端的服务器，IP地址为192.168.100.8，网关是192.168.100.1；PC作为Hillstone设备B
端的主机，IP地址为172.16.10.8，网关为172.16.10.1。要求实现VPN1 tunnel和VPN2 tunnel的VPN
监控，并当主隧道（VPN1 tunnel）链路发生故障时，流量转向备份隧道（VPN2 tunnel）；主隧道恢复
正常时，流量切换回主隧道。组网图参见下图：

<!-- 来源页 1477 -->
配置步骤
第一步:配置Hillstone设备A：
配置接口：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 192.168.100.1/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 10.10.10.1/24
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/4
hostname(config-if-eth0/4)# zone untrust
hostname(config-if-eth0/4)# ip address 20.20.20.1/24
hostname(config-if-eth0/4)# exit
配置路由：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 172.16.10.0/24 20.20.20.2
hostname(config-vrouter)# exit
配置P1提议
hostname(config)# isakmp proposal p1
hostname(config-isakmp-proposal)# authentication pre-share
hostname(config-isakmp-proposal)# group 2
hostname(config-isakmp-proposal)# hash md5
hostname(config-isakmp-proposal)# encryption des
hostname(config-isakmp-proposal)# exit
配置ISAKMP网关：
hostname(config)# isakmp peer gwa-peer-1
hostname(config-isakmp-peer)# interface ethernet0/1

<!-- 来源页 1478 -->
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# peer 10.10.10.2
hostname(config-isakmp-peer)# pre-shareU8FdHNEEBz6sNn5Mvqx3yWuLRWce
hostname(config-isakmp-peer)# exit
hostname(config)# isakmp peer gwa-peer-2
hostname(config-isakmp-peer)# interface ethernet0/4
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# peer 20.20.20.2
hostname(config-isakmp-peer)# pre-share i39jnnNiCSh9rXb77oGA7Fg7BNQy
hostname(config-isakmp-peer)# exit
配置P2提议：
hostname(config)# ipsec proposal p2
hostname(config-ipsec-proposal)# protocol esp
hostname(config-ipsec-proposal)# hash md5
hostname(config-ipsec-proposal)# encryption des
hostname(config-ipsec-proposal)# exit
配置VPN隧道：
hostname(config)# tunnel ipsec vpn1-tunnel auto
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# isakmp-peer gwa-peer-1
hostname(config-tunnel-ipsec-auto)# vpn-track interval 1 threshold 5
hostname(config-tunnel-ipsec-auto)# track-event-notify enable
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)# tunnel ipsec vpn2-tunnel auto
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# isakmp-peer gwa-peer-2
hostname(config-tunnel-ipsec-auto)# vpn-track interval 1 threshold 5
hostname(config-tunnel-ipsec-auto)# track-event-notify enable
hostname(config-tunnel-ipsec-auto)#auto-connect

<!-- 来源页 1479 -->
hostname(config-tunnel-ipsec-auto)# exit
配置策略：
hostname(config)# policy-global
hostname(config-policy)# rule id 1
hostname(config-policy-rule)# src-ip 192.168.100.8/24
hostname(config-policy-rule)# dst-ip 172.16.10.8/24
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action tunnel vpn1-tunnel
hostname(config-policy-rule)# exit
hostname(config-policy)# rule id 2
hostname(config-policy-rule)# src-ip 172.16.10.8/24
hostname(config-policy-rule)# dst-ip 192.168.100.8/24
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action from tunnel vpn1-tunnel
hostname(config-policy-rule)# exit
hostname(config-policy)# rule id 3
hostname(config-policy-rule)# src-ip 192.168.100.8/24
hostname(config-policy-rule)# dst-ip 172.16.10.8/24
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action tunnel vpn2-tunnel
hostname(config-policy-rule)# exit
hostname(config-policy)# rule id 4
hostname(config-policy-rule)# src-ip 172.16.10.8/24
hostname(config-policy-rule)# dst-ip 192.168.100.8/24
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action from tunnel vpn2-tunnel
hostname(config-policy-rule)# exit
hostname(config-policy)# rule id 5
hostname(config-policy-rule)# src-addr any

<!-- 来源页 1480 -->
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
第二步：配置Hillstone设备B：
配置接口：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 172.16.10.1/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 10.10.10.2/24
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/4
hostname(config-if-eth0/4)# zone untrust
hostname(config-if-eth0/4)# ip address 20.20.20.2/24
hostname(config-if-eth0/4)# exit
配置路由：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 192.168.100.0/24 20.20.20.1
hostname(config-vrouter)# exit
配置P1提议
hostname(config)# isakmp proposal p1
hostname(config-isakmp-proposal)# authentication pre-share
hostname(config-isakmp-proposal)# group 2

<!-- 来源页 1481 -->
hostname(config-isakmp-proposal)# hash md5
hostname(config-isakmp-proposal)# encryption des
hostname(config-isakmp-proposal)# exit
配置ISAKMP网关：
hostname(config)# isakmp peer gwb-peer-1
hostname(config-isakmp-peer)# interface ethernet0/1
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# peer 10.10.10.1
hostname(config-isakmp-peer)# pre-shareU8FdHNEEBz6sNn5Mvqx3yWuLRWce
hostname(config-isakmp-peer)# exit
hostname(config)# isakmp peer gwb-peer-2
hostname(config-isakmp-peer)# interface ethernet0/4
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# peer 20.20.20.1
hostname(config-isakmp-peer)# pre-sharei39jnnNiCSh9rXb77oGA7Fg7BNQy
hostname(config-isakmp-peer)# exit
配置P2提议：
hostname(config)# ipsec proposal p2
hostname(config-ipsec-proposal)# protocol esp
hostname(config-ipsec-proposal)# hash md5
hostname(config-ipsec-proposal)# encryption des
hostname(config-ipsec-proposal)# exit
配置VPN隧道：
hostname(config)# tunnel ipsec vpn1-tunnel auto
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# isakmp-peer gwb-peer-1
hostname(config-tunnel-ipsec-auto)# vpn-track interval 1threshold 5
hostname(config-tunnel-ipsec-auto)# auto-connect
hostname(config-tunnel-ipsec-auto)# exit

<!-- 来源页 1482 -->
hostname(config)# tunnel ipsec vpn2-tunnel auto
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# isakmp-peer gwa-peer-2
hostname(config-tunnel-ipsec-auto)# vpn-track interval 1 threshold 5
hostname(config-tunnel-ipsec-auto)# track-event-notify enable
hostname(config-tunnel-ipsec-auto)#auto-connect
hostname(config-tunnel-ipsec-auto)# exit
配置策略：
hostname(config)# policy-global
hostname(config-policy)# rule id 1
hostname(config-policy-rule)# src-ip 172.16.10.8/24
hostname(config-policy-rule)# dst-ip 192.168.100.8/24
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action from tunnel vpn1-tunnel
hostname(config-policy-rule)# exit
hostname(config-policy)# rule id 2
hostname(config-policy-rule)# src-ip 192.168.100.8/24
hostname(config-policy-rule)# dst-ip 172.16.10.8/24
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action tunnel vpn1-tunnel
hostname(config-policy-rule)# exit
hostname(config-policy)# rule id 3
hostname(config-policy-rule)# src-ip 172.16.10.8/24
hostname(config-policy-rule)# dst-ip 192.168.100.8/24
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action from tunnel vpn2-tunnel
hostname(config-policy-rule)# exit
hostname(config-policy)# rule id 4
hostname(config-policy-rule)# src-ip 192.168.100.8/24

<!-- 来源页 1483 -->
hostname(config-policy-rule)# dst-ip 172.16.10.8/24
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action tunnel vpn2-tunnel
hostname(config-policy-rule)# exit
hostname(config-policy)# rule id 5
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
由于本例中VPN终端设备都是Hillstone设备，因此可使用缺省源和目标地址进行VPN监控。
例：HA Peer模式支持IPsec VPN配置举例
HA Peer模式支持IPsec VPN。具体使用请参考如下功能举例。
本节介绍如何在非对称路由环境中将Peer工作模式结合IPsec VPN功能。在配置之前，确认搭建成HA Peer
组网模式的两台Hillstone设备采用完全相同的硬件平台、固件版本和相同的许可证。
配置完成后，两台设备均会开启Peer工作模式以及IPsec VPN功能。PC访问Server的流量的流量经由设备A
并由设备A上配置的IPsec VPN功能进行安全保护，Server的回包流量经由设备B并由设备B的配置IPsec
VPN功能进行安全保护。其中一台设备或设备所在上下链路出现故障，将由另外一台设备接管相应的流量转
发功能及IPsec VPN功能。组网图请参见下图：

<!-- 来源页 1484 -->
配置步骤
第一步：配置HA Peer工作模式。
Hillstone设备A
hostname(config)# ha link interface eth0/4
hostname(config)# ha link ip 10.10.1.1/24
hostname(config)# ha group 0
hostname(config-ha-group)# priority 50
hostname(config-ha-group)# exit
hostname(config)# ha group 1
hostname(config-ha-group)# priority 100
hostname(config-ha-group)# exit
Hillstone设备B
hostname(config)# ha link interface eth0/4
hostname(config)# ha link ip 10.10.1.2/24
hostname(config)# ha group 0

<!-- 来源页 1485 -->
hostname(config-ha-group)# priority 100
hostname(config-ha-group)# exit
hostname(config)# ha group 1
hostname(config-ha-group)# priority 50
hostname(config-ha-group)# exit
第二步：配置VFI接口并添加相应路由及NAT规则。
Hillstone设备A
hostname(config)# interface eth0/1:1
hostname(con-if-eth0/1:1)# zone untrust
hostname(con-if-eth0/1:1)# ip address192.168.10.1/24
hostname(con-if-eth0/1:1)# exit
hostname(config)# interface eth0/0:1
hostname(con-if-eth0/2:1)# zone trust
hostname(con-if-eth0/2:1)# ip address192.168.20.1/24
hostname(con-if-eth0/2:1)# exit
第三步：配置IPsec VPN。
Hillstone设备A
hostname(M0D1)(config)# isakmp peer peer1
hostname(M0D1)(config-isakmp-peer)# interface ethernet0/1
hostname(M0D1)(config-isakmp-peer)# peer 192.168.1.2
hostname(M0D1)(config-isakmp-peer)# isakmp-proposal psk-md5-des-g2
hostname(M0D1)(config-isakmp-peer)# pre-share hillstone
hostname(M0D1)(config-isakmp-peer)# exit
hostname(M0D1)(config)# isakmp peer peer2
hostname(M0D1)(config-isakmp-peer)# interface ethernet0/1:1
hostname(M0D1)(config-isakmp-peer)# peer 192.168.10.2
hostname(M0D1)(config-isakmp-peer)# isakmp-proposal psk-md5-des-g2
hostname(M0D1)(config-isakmp-peer)# pre-share hillstone

<!-- 来源页 1486 -->
hostname(M0D1)(config-isakmp-peer)# exit
hostname(M0D1)(config)# tunnel ipsec vpn1 auto
hostname(M0D1)(config-tunnel-ipsec-auto)# isakmp-peer peer1
hostname(M0D1)(config-tunnel-ipsec-auto)# ipsec-proposal esp-md5-des-g2
hostname(M0D1)(config-tunnel-ipsec-auto)# exit
hostname(M0D1)(config)# tunnel ipsec vpn2 auto
hostname(M0D1)(config-tunnel-ipsec-auto)# isakmp-peer peer2
hostname(M0D1)(config-tunnel-ipsec-auto)# ipsec-proposal esp-md5-des-g2
hostname(M0D1)(config-tunnel-ipsec-auto)# exit
hostname(M0D1)(config)# int tunnel1
hostname(M0D1)(config-if-tun1)# zone vpn
hostname(M0D1)(config-if-tun1)# tunnel ipsec vpn1
hostname(M0D1)(config-if-tun1)# exit
hostname(M0D1)(config)# int tunnel1:1
hostname(M0D1)(config-if-tun1)# zone vpn
hostname(M0D1)(config-if-tun1)# tunnel ipsec vpn2
hostname(M0D1)(config-if-tun1)# exit
Hillstone设备C
hostname(config)# isakmp peer peer1
hostname(config-isakmp-peer)# interface ethernet0/1
hostname(config-isakmp-peer)# peer 192.168.1.1
hostname(config-isakmp-peer)# isakmp-proposal psk-md5-des-g2
hostname(config-isakmp-peer)# pre-share hillstone
hostname(config-isakmp-peer)# exit
hostname(config)# isakmp peer peer2
hostname(config-isakmp-peer)# interface ethernet0/2
hostname(config-isakmp-peer)# peer 192.168.10.1
hostname(config-isakmp-peer)# isakmp-proposal psk-md5-des-g2
hostname(config-isakmp-peer)# pre-share hillstone

<!-- 来源页 1487 -->
hostname(config-isakmp-peer)# exit
hostname(config)# tunnel ipsec vpn1 auto
hostname(config-tunnel-ipsec-auto)# isakmp-peer peer1
hostname(config-tunnel-ipsec-auto)# ipsec-proposal esp-md5-des-g2
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)# tunnel ipsec vpn2 auto
hostname(config-tunnel-ipsec-auto)# isakmp-peer peer2
hostname(config-tunnel-ipsec-auto)# ipsec-proposal esp-md5-des-g2
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)# int tunnel1
hostname(config-if-tun1)# zone vpn
hostname(config-if-tun1)# tunnel ipsecvpn1
hostname(config-if-tun1)# exit
hostname(config)# int tunnel2
hostname(config-if-tun1)# zone vpn
hostname(config-if-tun1)# tunnel ipsec vpn2
hostname(config-if-tun1)# exit
第四步：配置VPN相关的策略和路由。
Hillstone设备A
hostname(M0D1)(config)# ip vrouter trust-vr
hostname(M0D1)(config-vrouter)# ip route192.168.1.2/24 tunnel1
hostname(M0D1)(config-vrouter)# ip route 192.168.10.2/24 tunnel1:1
hostname(M0D1)(config-vrouter)# ip route 172.16.20.0/24 192.168.2.2
hostname(M0D1)(config-vrouter)# ip route 172.16.20.0/24 192.168.20.2
hostname(M0D1)(config-vrouter)# exit
hostname(M0D1)(config)# rule id 1 from any to any service any permit
Hillstone设备C
hostname(config)# ip vrouter trust-vr
hostname(config)# ip route 172.16.20.0/24 tunnel1 20

<!-- 来源页 1488 -->
hostname(config)# ip route 172.16.20.0/24 tunnel2 10
hostname(config)# exit
hostname(config)# rule id 1 from any to any service any permit
例：XAUTH配置举例
本节介绍典型的XAUTH配置实例。
组网需求
Hillstone设备上启用了XAUTH服务器，使用本地AAA服务器认证用户。要求当用户试图通过手机终端创建
VPN连接并访问内网的FTP服务器时，XAUTH服务器通过预共享秘钥方式对用户身份进行验证，并允许通过
验证的用户访问内网资源。组网图请参考下图。
配置步骤
第一步：配置接口、安全域和策略：
接口配置：
hostname(config)# interface ethernet0/6
hostname(config-if-eth0/7)# zone trust

<!-- 来源页 1489 -->
hostname(config-if-eth0/7)# ip address 6.6.6.6 255.255.255.0
hostname(config-if-eth0/7)# manage ping
hostname(config-if-eth0/7)# manage ssh
hostname(config-if-eth0/7)# manage http
hostname(config-if-eth0/7)# exit
hostname(config)# interface ethernet0/7
hostname(config-if-eth0/6)# zone untrust
hostname(config-if-eth0/6)# ip address 7.7.7.7 255.255.255.0
hostname(config-if-eth0/6)# exit
hostname(config)# rule top
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config)#
第二步：配置AAA服务器：
hostname(config)# aaa-server local type local
hostname(config-aaa-server)# user xauth
hostname(config-user)# password test
hostname(config-user)# ike-id key-id xauth
hostname(config-user)# end
hostname(config)#
第三步：配置XAUTH地址池
hostname(config)# xauth pool pool
hostname(config-xauth-pool)# address 9.9.9.9 9.9.9.99 netmask 255.255.255.0
hostname(config-xauth-pool)# exit
hostname(config)#

<!-- 来源页 1490 -->
第四步：配置ISAKMP网关：
hostname(config)# isakmp peer xauth
hostname(config-isakmp-peer)# mode aggresive
hostname(config-isakmp-peer)# type usergroup
hostname(config-isakmp-peer)# psk-sha-aes128-g2
hostname(config-isakmp-peer)# pre-share XhF44BilJO3b/2HFl5lVqXniqeMByq
hostname(config-isakmp-peer)# aaa-server local
hostname(config-isakmp-peer)# local-id key-id xauth
hostname(config-isakmp-peer)# xauth pool-name pool
hostname(config-isakmp-peer)# xauth server
hostname(config-isakmp-peer)# interfaceethernet0/7
hostname(config-isakmp-peer)# exit
hostname(config)#
第五步：创建IKE隧道和隧道接口：
hostname(config)# tunnel ipsec xauth auto
hostname(config-tunnel-ipsec-auto)# isakmp-peer xauth
hostname(config-tunnel-ipsec-auto)# esp-sha-aes128-g0
hostname(config-tunnel-ipsec-auto)# accept-all-proxy-id
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)# interface tunnel22
hostname(config-if-tun22)# zone trust
hostname(config-if-tun22)# ip address 9.9.9.1 255.255.255.0
hostname(config-if-tun22)# manage telnet
hostname(config-if-tun22)# manage ssh
hostname(config-if-tun22)# manage ping
hostname(config-if-tun22)# manage http
hostname(config-if-tun22)# manage https
hostname(config-if-tun22)# manage snmp

<!-- 来源页 1491 -->
hostname(config-if-tun22)# tunnel ipsec xauth
hostname(config-if-tun22)# exit
hostname(config)#
完成上述配置后，手机用户可以利用安卓或iOS系统中自带的VPN客户端完成认证（用户名xauth，密码
test，IPSec标示符/群组名称xauth）并访问内网资源。

<!-- 来源页 1492 -->
SSL VPN
SSL VPN介绍
为解决远程用户安全访问私网数据的问题，设备提供基于SSL的远程登录解决方案。SSL VPN功能可以通过
简单易用的方法实现信息的远程连通。
设备的SSL VPN功能包含服务端和客户端两部分。配置了SSL VPN功能的设备作为服务端，具有以下功能：
l 接受客户端连接；
l 为客户端分配IP地址、DNS服务器地址和WINS服务器地址；
l 进行客户端用户的认证与授权；
l 进行客户端主机的安全检测；
l 解密来自客户端的加密报文并转发。
不同型号的设备默认情况下支持的同时在线最大VPN客户端数不同，如果想增加支持的客户端数，请向代理
商购买相应的许可证。
SSL VPN客户端成功连接服务端后，用户就可以通过SSL VPN功能安全的传输数据信息。SSL VPN客户端分
为以下版本：
l "Hillstone Secure Connect客户端for Windows" 在第1921页
l "Hillstone Secure Connect客户端for Android" 在第1933页
l "Hillstone Secure Connect客户端for iOS" 在第1938页
l "Hillstone Secure Connect客户端for macOS" 在第1944页
l "Hillstone Secure Connect客户端for Linux" 在第1953页
l "Hillstone Secure Connect客户端for ChineseOS" 在第1964页
SSL VPN服务端配置介绍
山石网科设备的SSL VPN功能配置包括以下各部分：
l 接入地址池
l 资源列表
l 配置传输协议

<!-- 来源页 1493 -->
l SSL VPN实例配置
l 配置客户端USB Key证书认证
l 配置二次认证功能
l 配置主机绑定功能
l 配置主机检测功能
l 配置最优路径检测功能
l Secure Connect客户端管理配置
l 显示SSL VPN信息
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

<!-- 来源页 1494 -->
access-address-pool pool-name
l
pool-name – 指定地址池的名称，取值范围是1到31个字符。
执行该命令后，系统创建指定名称的地址池，并且进入接入地址池配置模式；如果指定的名称已存在，则直
接进入接入地址池配置模式。
在全局配置模式下，使用该命令no的形式删除指定的地址池：
no access-address-pool pool-name
在接入地址池配置模式下可进行如下配置：
l
配置地址池地址范围和网络掩码
l
配置保留地址池
l
配置IP地址绑定规则
l
配置DNS服务器
l
配置WINS服务器
配置地址池地址范围
为地址池配置地址范围和网络掩码，在接入地址池配置模式下使用以下命令：
address start-ip end-ip netmask A.B.C.D
l
start-ip – 指定IP范围的起始IP地址。
l
end-ip – 指定IP范围的结束IP地址。
l
netmask A.B.C.D – 指定地址池IP范围的网络掩码。
在接入地址池配置模式下使用该命令no的形式删除配置的IP地址范围：
no address
配置保留地址池
保留地址池中的IP地址为地址池中的部分IP地址，当服务端从地址池里取出IP地址分配给客户端时，需要保
留已经被占用的部分IP地址（如网关、FTP服务器等），不进行分配。配置保留地址池，在接入地址池配置
模式下使用以下命令：
exclude address start-ip end-ip
l
start-ip – 指定保留地址池的起始IP地址。
l
end-ip – 指定保留地址池的结束IP地址。

<!-- 来源页 1495 -->
在接入地址池配置模式下使用该命令no的形式取消保留地址池的配置：
no exclude
配置IP地址绑定规则
Hillstone设备通过创建和执行IP地址绑定规则来满足客户端的固定IP地址需求。IP地址绑定规则包括IP用户
绑定规则和IP角色绑定规则。IP用户绑定规则将客户端用户与已配置地址池中的某个固定IP地址绑定，当客
户端连接成功后，服务端会将绑定的IP地址分配给客户端；IP角色绑定规则是将角色与已配置地址池中的某
一IP地址范围绑定，当此客户端连接成功后，服务端会从绑定的地址范围中取出一个IP地址分配给客户端。
当服务端通过地址池给客户端分配IP地址时，系统会按照一定的顺序对客户端的IP地址绑定规则进行检查，
决定如何为客户端分配IP地址：
1.
检查是否已为客户端用户配置IP用户绑定规则，如果是，则将绑定的IP地址分配给客户端；否则，需要
进一步检查。注意，如果此IP用户绑定规则中的IP地址已被占用，则该用户无法登录。
2.
检查是否已为客户端用户配置IP角色绑定规则，如果是，则从绑定的地址范围中取出一个IP地址分配给
客户端；否则，在未绑定的IP地址范围中取出一个IP地址分配给客户端。注意，如果绑定的地址范围中
的地址都已经被分配，则该用户无法登录。
注意: IP用户绑定规则中的IP地址和IP角色绑定规则中的IP地址不能重叠。
配置IP用户绑定规则
配置IP用户绑定规则，在接入地址池配置模式下使用以下命令：
ip-binding user user-name ip ip-address
l
user user-name – 指定客户端用户名。
l
ip ip-address – 指定绑定的IP地址。此地址必须为地址池中可以分配的地址。
在接入地址池配置模式下使用该命令no的形式取消对特定用户IP用户绑定规则的配置：
no ip-binding user user-name
配置IP角色绑定规则
配置IP角色绑定规则，在接入地址池配置模式下使用以下命令：
ip-binding role role-name ip_range start-ip end-ip

<!-- 来源页 1496 -->
l
role role-name – 指定角色名称。
l
ip_range start-ip end-ip – 指定绑定的IP范围的起始IP地址start-ip和结束IP地址end-ip。此地址
范围必须为地址池中可以分配的地址范围。
在接入地址池配置模式下使用该命令no的形式取消对特定角色的IP角色绑定规则的配置：
no ip-binding role role-name
修改IP角色绑定规则排列顺序
一个用户可以绑定到一个或者多个角色，不同角色可以配置不同的IP角色绑定规则。对于绑定到多个角色且
多个角色有相应的IP角色绑定规则的用户，Hillstone设备会对IP角色绑定规则进行顺序查找，然后按照查找
到的相匹配的第一条规则为用户分配地址。默认情况下，系统会将新创建的规则放到所有规则的末尾，管理
员可以移动已有的IP角色绑定规则从而改变规则的排列顺序。改变规则的排列顺序，在接入地址池配置模式
下使用以下命令：
move role-name1 {before role-name2 | after role-name2| top | bottom}
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
配置DNS服务器，在接入地址池配置模式下使用以下命令：
dns address1 [address2] [address3] [address4]
l
address1 – 指定DNS服务器IP地址。用户最多可配置4个DNS服务器。
在接入地址池配置模式下使用该命令no的形式取消对DNS服务器的指定：
no dns
配置WINS服务器
配置WINS服务器，在接入地址池配置模式下使用以下命令：
wins address1[ address2]

<!-- 来源页 1497 -->
l
address1 – 指定WINS服务器IP地址。用户最多可配置两个WINS服务器。
在接入地址池配置模式下使用该命令no的形式取消对WINS服务器的指定：
no wins
显示IPv4地址池信息
显示地址池信息，在任何模式下使用以下命令：
show access-address-pool [pool-name]
l
pool-name – 指定地址池名称以显示指定的地址池信息。如果不指定该参数值，系统将显示所有已配置
的地址池信息。
以下是显示地址池具体信息的命令示例：
hostname(config)# show access-address-pool pool_test1
Name: pool_test1
Address range: 3.3.3.1 - 3.3.3.10 ( 地址池IP地址范围)
Exclude range: 3.3.3.1 - 3.3.3.2 ( 保留地址池地址范围)
Netmask: 255.255.255.0 ( 地址池网络掩码)
Wins server: ( WINS服务器信息)
wins1: 10.1.1.1
Dns server:
( DNS服务器信息)
dns1: 10.10.209.1
IP Binding User: ( IP用户绑定信息)
test 3.3.3.8
IP Binding Role: ( IP角色绑定信息)
role1 3.3.3.3 3.3.3.7
显示地址池统计信息，在任何模式下使用以下命令：
show access-address-pool pool-name statistics
l
pool-name – 指定地址池名称以显示指定的地址池统计信息。
以下是显示地址池统计信息的命令示例：
hostname(config)# show access-address-pool pool_test1 statistics

<!-- 来源页 1498 -->
Total Ip Num 10 ( 地址池中IP地址总数)
Exclude Ip Num 2 ( 保留IP地址个数)
Fixed Ip Num 6 ( 绑定IP地址个数)
Used Ip Num 2 ( 已分配IP地址个数)
Fixed Used Ip Num 0 ( 已分配绑定IP地址个数)
Free Ip Num 6 ( 可用地址个数)
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
l
配置地址池地址范围和前缀长度
l
配置保留地址池
l
配置IP地址绑定规则
l
配置DNS服务器
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

<!-- 来源页 1499 -->
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
配置IP地址绑定规则
设备通过创建和执行IP地址绑定规则来满足客户端的固定IPv6地址需求。IP地址绑定规则包括IP用户绑定规
则和IP角色绑定规则。IP用户绑定规则将客户端用户与已配置地址池中的某个固定IPv6地址绑定，当客户端
连接成功后，服务端会将绑定的IPv6地址分配给客户端；IP角色绑定规则是将角色与已配置地址池中的某一
IPv6地址范围绑定，当此客户端连接成功后，服务端会从绑定的地址范围中取出一个IPv6地址分配给客户
端。
当IPv6服务端通过地址池给客户端分配IP地址时，系统会按照一定的顺序对客户端的IPv6地址绑定规则进行
检查，决定如何为客户端分配IPv6地址：
1.
检查是否已为客户端用户配置IP用户绑定规则，如果是，则将绑定的IPv6地址分配给客户端；否则，需
要进一步检查。注意，如果此IP用户绑定规则中的IPv6地址已被占用，则该用户无法登录。
2.
检查是否已为客户端用户配置IP角色绑定规则，如果是，则从绑定的地址范围中取出一个IPv6地址分配
给客户端；否则，在未绑定的IPv6地址范围中取出一个IPv6地址分配给客户端。注意，如果绑定的地址
范围中的地址都已经被分配，则该用户无法登录。
注意: IP用户绑定规则中的IPv6地址和IP角色绑定规则中的IPv6地址不能重叠。
配置IP用户绑定规则
配置IP用户绑定规则，在IPv6接入地址池配置模式下使用以下命令：
ip-binding user user-name ip ipv6-address

<!-- 来源页 1500 -->
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
before role-name2 – 将IP角色绑定规则移动到某个IP角色绑定规则(角色名称为role-name2的规则)
之前。
l
after role-name2 – 将IP角色绑定规则移动到某个IP角色绑定规则(角色名称为role-name2的规则)之
后。
l
top – 将IP角色绑定规则移动到所有IP角色绑定规则之首。
l
bottom – 将IP角色绑定规则移动到所有IP角色绑定规则的末尾。

<!-- 来源页 1501 -->
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
Name Address range Prefix length
---------------------------------------------------------------------
--
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
1001:5678:2222:3333:5555:ABCD:EFAB:3000 ( IPv6地址池IPv6地址范围)

<!-- 来源页 1502 -->
Exclude range: 1001:5678:2222:3333:5555:ABCD:EFAB:1000 -
1001:5678:2222:3333:5555:ABCD:EFAB:2000 ( 保留IPv6池地范围)
prefix length: 112( 地址池前缀长度)
Dns server:
( DNS服务器信息)
IP Binding User:
IP Binding Role:
显示IPv6地址池池统计信息，在任何模式下使用以下命令：
show access-address-pool pool-name statistics
l
pool-name – 指定IPv6地址池名称以显示指定的地址池统计信息。
以下是显示地址池统计信息的命令示例：
hostname(config)# show access-address-pool 2-ipv6-pool statistics
Total Ip Num 10 ( 地址池中IPv6地址总数)
Exclude Ip Num 2 ( 保留IPv6地址个数)
Fixed Ip Num 6 ( 绑定IPv6地址个数)
Used Ip Num 2 ( 已分配IPv6地址个数)
Fixed Used Ip Num 0 ( 已分配绑定IPv6地址个数)
Free Ip Num 6 ( 可用IPv6地址个数)
资源列表
资源列表是指系统中配置的用户可便捷访问的资源，其中每个资源又包含多个资源条目。资源条目的展现形
式为“条目名称+对应的URL”。SSL VPN用户登录认证通过后，认证服务器将该用户所属的用户组信息或
者该用户映射的角色信息发送给SSL VPN服务器，然后服务器会根据配置的SSL VPN实例中用户组或者角色
和资源的绑定关系，把该用户可访问的内网资源列表发送给SSL VPN客户端，客户端对接收到的资源列表信
息进行分析并展示在用户系统默认浏览器弹出的页面中，用户可以通过点击“资源条目”名称访问内网资
源。需要注意的是，该资源列表页面只在认证通过后显示一次。如果登录的用户不属于任何用户组或者未映
射任何角色，认证成功后浏览器不会弹出资源列表页面。
配置资源列表
配置SSL VPN资源
配置SSL VPN资源，在全局配置模式下，使用以下命令：

<!-- 来源页 1503 -->
scvpn resource-list list-name
l
list-name –指定资源的名称。取值范围是1到63个字符。
执行该命令后，系统进入SSL VPN资源列表配置模式，用户可以继续为该新建资源配置资源条目。在全局配
置模式下，使用该命令no的形式删除指定的资源：
no resource-list list-name
注意:
l
系统最多允许配置256个资源列表。
l
支持资源列表功能的SSL VPN客户端版本：SSL VPN Windows客户端v1.4.6.1238及之后版
本、iOS v2.0.6及之后版本、Android v4.6及之后版本。
添加资源条目
在SSL VPN资源列表配置模式下，新建资源添加资源条目：
name name url url-string
l
name –指定资源条目的名称。取值范围是1到95个字符。
l
url-string –指定资源条目所对应的URL。取值范围是1到255个字符。
在SSL VPN资源列表配置模式下，使用以下命令删除指定的资源条目：
no name name
注意: 可配置的资源条目数目最大值根据平台不同可分为200、500、1000三类，请以实际情况为
准。
查看资源列表
用户可以在任何模式下，使用以下命令查看资源列表的配置信息：
show scvpn resource-list [list-name]
l
list-name –指定要查看的资源的名称。取值范围是1到63个字符。如果不指定该参数，则显示所有资源
的配置信息。
配置传输协议
系统支持通过TCP或UDP协议进行数据传输，默认使用UDP协议，端口为4433。配置传输协议及端口，在
SCVPN隧道配置模式下，使用以下命令：

<!-- 来源页 1504 -->
配置传输协议及端口
配置传输协议及端口，在SCVPN隧道配置模式下，使用以下命令：
transport-service{tcp | udp} port port-number
l
tcp | udp - 指定使用TCP或UDP协议进行数据传输。
l
port-number –指定数据通道使用的端口号。取值范围是1到65535。
显示TCP socket相关信息
显示TCP socket相关信息，在任何模式下，使用以下命令：
show dp tcp-socket [vrouter vrouter-name ] [ip ip] [port port] [statistics]
l
vrouter vrouter-name –显示指定Vrouter的TCP socket信息。
l
ip ip–显示指定IP地址的TCP socket信息。
l
port port –显示指定端口的TCP socket信息。
l
statistics –显示TCP socket的统计信息。
显示SCVPN使用的UDP端口信息
显示SCVPN使用的UDP端口信息，在任何模式下，使用以下命令：
show dp-scvpn-udp-socket
全局UDP端口号配置
配置SSL VPN连接采用的UDP端口号，在全局配置模式下，使用以下命令：
scvpn-udp-portport-number
l
port-number –指定UDP端口号。默认值是4433。取值范围是1到65535。
执行该命令后，所有配置的SSL VPN实例均采用此UDP端口号进行数据连接。
在全局配置模式下使用该命令no的形式恢复默认UDP端口号：
no scvpn-udp-port
SSL VPN实例配置
创建SSL VPN实例，在全局配置模式下，使用以下命令：
tunnel scvpn instance-name
l
instance-name – 指定SSL VPN实例的名称。

<!-- 来源页 1505 -->
执行该命令后，系统创建指定名称的SSL VPN实例，并且进入SSL VPN实例配置模式；如果指定的名称已存
在，则直接进入SSL VPN实例配置模式。在全局配置模式下，使用该命令no的形式删除指定的SSL VPN实
例：
no tunnel scvpn instance-name
在SSL VPN实例配置模式下，用户可以进行如下配置：
l 启用/禁用SSL VPN实例
l 指定服务类型
l 指定接入地址池
l 指定服务端接口
l 指定SSL协议
l 指定PKI信任域
l 指定加密信任域
l 指定隧道密码套件
l 指定AAA服务器
l 指定HTTPS端口号
l 配置传输协议
l 显示TCP socket相关信息
l 显示SCVPN使用的UDP端口信息
l 配置SSL VPN隧道路由
l 配置防重放功能
l 配置分片功能
l 配置空闲时间
l 配置强制下线时间表
l 配置用户同名登录功能
l 配置URL重定向功能
l 启用/禁用清除SSL VPN桌面版客户端缓存数据功能
l 在HA Peer模式中使用SSL VPN
l 绑定L2TP VPN实例

<!-- 来源页 1506 -->
l 绑定资源
l 开启/关闭允许浏览器下载客户端功能
启用/禁用SSL VPN实例
SSL VPN实例处于启用状态且配置完整的情况下，客户端可以正常接入。若客户端已接入到SSL VPN，禁用
SSL VPN实例，已连接的客户端用户将会被下线。启用或禁用SSL VPN实例，在SSL VPN实例配置模式下，
使用以下命令：
启用：enable
禁用：disable
指定服务类型
指定SSL VPN实例的服务类型，包括IPv4、IPv6或双栈。IPv6和双栈类型仅当系统版本为IPv6版本时可
配，默认情况下SSL VPN实例的服务类型为IPv4。在SSL VPN实例配置模式下，使用以下命令：
service-type {ipv4 | ipv6 | dual-stack}
l
ipv4 | ipv6 | dual-stack–指定SSL VPN实例的服务类型，包括IPv4、IPv6或双栈。
相关概念：
双栈是一种网络技术，它允许在一个网络设备上同时运行IPv4和IPv6两种网络协议栈，使得网络设备能
够在IPv4和IPv6网络间进行无缝切换和通信。
指定地址池
指定IPv4-地址池
VPN实例指定IPv4-地址池，在SSL VPN实例配置模式下，使用以下命令：
access-address-pool pool-name
l
pool-name – 指定已配置的IPv4地址池名称。
在SSL VPN实例配置模式下使用该命令no的形式取消IPv4地址池的指定：
no access-address-pool
指定IPv6地址池
为SSL VPN实例指定IPv6地址池，在SSL VPN实例配置模式下，使用以下命令：
access-address-pool-ipv6 pool-name
l
pool-name – 指定已配置的IPv6地址池名称。

<!-- 来源页 1507 -->
在SSL VPN实例配置模式下使用该命令no的形式取消IPv6地址池的指定：
no access-address-pool-ipv6
注意:
l
仅可以为IPv4服务类型的SSL VPN实例指定IPv4地址池。
l
仅可以为IPv6服务类型的SSL VPN实例指定IPv6地址池。
指定服务端接口
客户端通过HTTPS协议访问服务端接口。指定SSL VPN服务端接口，在SSL VPN实例配置模式下，使用以下
命令：
interface interface-name
l
interface-name – 指定服务端接口的名称。
在SSL VPN实例配置模式下使用该命令no的形式取消服务端接口的配置：
no interface interface-name
指定SSL协议
为SSL VPN指定SSL协议，在SSL VPN实例配置模式下，使用以下命令：
ssl-protocol { tlsv1 | tlsv1.2 | tlsv1.3 | gmssl | any}
l
tlsv1 – 指定使用TLSv1协议。
l
tlsv1.2 – 指定使用TLSv1.2协议。此为系统默认配置。
l
tlsv1.3 – 指定使用TLSv1.3协议。
l
gmssl – 指定使用国密GMSSLv1.0协议。当协议为此选项时，PKI信任域和加密信任域必须选择配置含
有SM2类型密钥的信任域，加密算法建议优先选择SM4，Hash算法建议优先选择SM3.
l
any – 指定使用TLSv1、TLSv1.1、TLSv1.2或者TLSv1.3任何一种协议。
在SSL VPN实例配置模式下使用该命令no的形式恢复SSL协议的默认值：
no ssl-protocol
如果服务端指定的SSL协议类型为tlsv1.2或者any，在SSL VPN客户端进行数字证书认证前，需要用户将要
导入到浏览器中的软证书或者USB Key中的.pfx格式证书进行处理，使得证书能够支持tlsv1.2协议，以便用
户在使用“用户名/密码+数字证书”或者“数字证书”认证方式进行认证时，能够连接成功。处理证书前，

<!-- 来源页 1508 -->
请先准备一台安装了OpenSSL1.0.1版本及以上的PC（Windows或Linux系统均可）。以文件名称为
oldcert.pfx的证书为例，处理步骤如下：
1.
在OpenSSL软件界面中，输入以下命令将.pfx格式的证书转换为.pem格式的证书。openssl pkcs12 –
in oldcert.pfx –out cert.pem
2.
继续输入下面的命令将.pem格式的证书转换为支持tlsv1.2的.pfx格式证书。openssl pkcs12 –
export –in cert.pem –out newcert.pfx –CSP “Microsoft Enhanced RSA and AES
Cryptographic Provider”
3.
将新生成的.pfx格式证书导入到浏览器或者USB Key。
上述操作完成后，请使用1.4.6.1239及以上版本的SSL VPN客户端进行登录。当配置使用国密标准的SSL
VPN功能时，PC端需安装支持国密标准的SSL VPN客户端（当前支持国密标准的Windows客户端版本为
1.4.7.1252），并且使用“国密SSL”相关登录模式进行登录。
指定PKI信任域
此处指定的PKI信任域用于HTTPS访问认证。为SSL VPN指定PKI信任域，在SSL VPN实例配置模式下，使
用以下命令：
trust-domain trust-domain-name
l
trust-domain-name – 指定系统中已配置的PKI信任域的名称。默认信任域为trust_domain_
default。
在SSL VPN实例配置模式下使用该命令no的形式恢复信任域的默认配置：
no trust-domain
关于如何创建PKI信任域，请参阅《用户认证》的“PKI配置”部分。
指定加密信任域
此处为SSL VPN指定加密信任域，加密信任域用于国密SSL协商。在SSL VPN实例配置模式下，使用以下命
令：
trust-domain-enc enc-cert
l
enc-cert – 指定系统预定义的用于国密SSL协商的加密信任域的名称。
在SSL VPN实例配置模式下使用该命令no的形式删除加密信任域的配置：
no trust-domain-enc

<!-- 来源页 1509 -->
指定隧道密码套件
隧道密码套件包括加密算法、验证算法和压缩算法。为SSL VPN指定隧道密码套件，在SSL VPN实例配置模
式下，使用以下命令：
tunnel-cipher encryption {null | des | 3des | aes | aes192 | aes256 | sm4} hash {null | md5 |
sha | sha256 | sha384 | sha512 | sm3} [compression defl]
l
null | des | 3des | aes | aes192 | aes256 | sm4 – 指定加密算法。默认加密算法为AES。null表示不
使用加密功能。关于加密算法的详细描述，请参阅“加密算法”。
l
null | md5 | sha | sha256 | sha384 | sha512| sm3 – 指定验证算法。默认验证算法为MD5。null表
示不使用验证功能。关于验证算法的详细描述，请参阅“验证算法”。
l
compression defl – 指定DEFLATE压缩算法。默认无压缩算法。关于压缩算法的详细描述，请参阅
“压缩算法”。
在SSL VPN实例配置模式下使用该命令no的形式恢复加密算法和验证算法的默认值并取消压缩算法的配置：
no tunnel-cipher
指定AAA服务器
此处指定的AAA服务器为进行客户端用户身份认证的AAA服务器。指定AAA服务器，在SSL VPN实例配置模
式下，使用以下命令：
aaa-serveraaa-server-name [domain domain-name] [keep-domain-name]
l
aaa-server-name – 指定AAA服务器的名称。
l
domain domain-name – 为AAA服务器指定域名以区分不同的AAA服务器。
l
keep-domain-name – 指定该参数后，用于身份认证的用户名将验证域名。
注意: 仅Windows/macOS/Linux/国产操作系统的Hillstone Secure Connect客户端支持
OAuth2认证方式。OAuth2服务器不支持用户域名验证功能（keep-domain-name）。
在SSL VPN实例配置模式下使用该命令no的形式取消对AAA服务器的指定：
no aaa-server aaa-server-name [domain domain-name]
指定HTTPS端口号
HTTPS端口号用于客户端访问服务端时使用。指定HTTPS端口号，在SSL VPN实例配置模式下，使用以下命
令：
https-port port-number

<!-- 来源页 1510 -->
l
port-number – 指定HTTPS端口号。默认值是4433。取值范围是1到65535。为避免与WebUI使用的
HTTPS端口号相冲突，建议用户不要把HTTPS端口号设置为443。绑定到同一个接口的SSL VPN实例需
配置不同的HTTPS端口号。
在SSL VPN实例配置模式下使用该命令no的形式恢复默认HTTPS端口号：
no https-port
配置传输协议
系统支持通过TCP或UDP协议进行数据传输，默认使用UDP协议，端口为4433。
配置传输协议及端口
配置传输协议及端口，在SCVPN隧道配置模式下，使用以下命令：
transport-service{tcp | udp} port port-number
l
tcp | udp - 指定使用TCP或UDP协议进行数据传输。
l
port-number –指定数据通道使用的端口号。取值范围是1到65535。
显示TCP socket相关信息
显示TCP socket相关信息，在任何模式下，使用以下命令：
show dp tcp-socket [vrouter vrouter-name ] [ip ip] [port port] [statistics]
l
vroutervrouter-name –显示指定Vrouter的TCP socket信息。
l
ip ip –显示指定IP地址的TCP socket信息。
l
port port –显示指定端口的TCP socket信息。
l
statistics –显示TCP socket的统计信息。
显示SCVPN使用的UDP端口信息
显示SCVPN使用的UDP端口信息，在任何模式下，使用以下命令：
show dp-scvpn-udp-socket
配置SSL VPN隧道路由
IPv4/IPv6 SSL VPN隧道路由是指通过IPv4/IPv6类型的SSL VPN隧道到指定网段/域名的路由。SSL VPN
客户端接收到指定网段后，生成到达指定网段的路由条目；接收到指定域名后，根据域名解析结果，生成到
达域名所在地址的路由条目。

<!-- 来源页 1511 -->
注意: 当配置双栈类型的SSL VPN时，需指定IPv4和IPv6 SSL VPN隧道路由。
配置到指定IPv4网段的SSL VPN隧道路由
仅可以为IPv4或双栈服务类型的SSL VPN实例配置IPv4 SSL VPN隧道路由。使用网段方式配置SSL VPN隧
道路由，在SSL VPN实例配置模式下，使用以下命令：
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
l
role role_name] – 指定角色名称。指定后，仅该角色对应的用户可以访问隧道路由中的指定网段。说
明：指定该参数前请先创建角色，具体方法请参阅“角色配置”（系统管理> 系统用户管理> 角色配
置）。
用户可以配置多条该命令添加多条路由。
在SSL VPN实例配置模式下使用该命令no的形式删除指定的路由：
no split-tunnel-route ip-address/netmask [metric metric-number] [user-group aaa-server_
name group_name | role role_name]
配置到指定IPv6网段的SSL VPN隧道路由
仅可以为IPv6或双栈服务类型的SSL VPN实例配置IPv6 SSL VPN隧道路由。使用网段方式配置IPv6 SSL
VPN 隧道路由，在SSL VPN实例配置模式下，使用以下命令：
split-tunnel-route-ipv6 ipv6-address/prefix [metric metric-number] [user-group aaaserver_name group_name | role role_name]
l
ipv6-address/prefix – 指定IPv6类型的目的地址和前缀长度。
l
metric metric-number – 指定路由的度量值。默认值是35。取值范围是1到9999。
l
user-group aaa-server_name group_name – 指定用户组所属的认证服务器名称和用户组名称。
指定后，仅该用户组里的用户可以访问隧道路由中的指定网段。说明：指定该参数前请先创建用户组，
具体方法请参阅“用户组配置”（系统管理> 系统用户管理> 用户组配置）。

<!-- 来源页 1512 -->
l
role role_name] – 指定角色名称。指定后，仅该角色对应的用户可以访问隧道路由中的指定网段。说
明：指定该参数前请先创建角色，具体方法请参阅“角色配置”（系统管理> 系统用户管理> 角色配
置）。
用户可以配置多条该命令添加多条IPv6路由。
在SSL VPN实例配置模式下使用该命令no的形式删除指定的路由：
no split-tunnel-route-ipv6 ipv6-address/prefix [metric metric-number] [user-group aaaserver_name group_name | role role_name]
配置域名下发功能
系统将指定域名下发给客户端后，客户端根据域名解析结果，生成到达域名所在地址的路由条目。指定下发
给客户端的域名，在SSL VPN实例配置模式下，使用以下命令：
domain-route {disable | enable | max-entries value | url]
l
disable – 不下发域名到客户端。此为系统默认设置。
l
enable – 下发域名到客户端。
l
max-entries value – 指定客户端可以根据域名解析后地址所生成的最大路由条目数。默认值是
1000，取值范围是1到10000。
l
url – 指定域名。每次可添加一个，支持最多64个域名。每个域名的字符串长度不得超过63个字符。域
名末尾不能为“.”，不支持通配符，且不支持过于宽泛的URL，比如：“.com”、“com”。
在SSL VPN实例配置模式下使用该命令no的形式删除指定的域名：
no domain-route url
注意: 域名下发功能和SSL VPN专线功能互斥，不能同时使用。关于如何配置SSL VPN专线功能，
请参阅启用SSL VPN专线。
启用SSL VPN专线
系统支持SSL VPN专线功能，该功能默认关闭。启用该功能后，用户在成功登录SSL VPN后仅能访问隧道路
由中指定网段的内网资源，不能访问互联网资源。

<!-- 来源页 1513 -->
注意:
l
支持SSL VPN专线功能的客户端版本包括：Windows系统SSL VPN客户端最新版本、macOS
系统SSL VPN客户端最新版本、Linux系统SSL VPN客户端最新版本。
l
SSL VPN专线功能和域名下发功能互斥，不能同时使用。关于如何配置域名下发功能，请参阅
配置到指定域名的隧道路由。
l
启用SSL VPN专线功能后，建议不要在隧道路由中配置默认路由。
启用或者禁用SSL VPN专线功能，在SSL VPN实例配置模式下，使用以下命令：
dedicated-tunnel {enable | disable}
l
enable - 启用SSL VPN专线功能。
l
disable -禁用SSL VPN专线功能。
配置防重放功能
防重放（anti-replay）指防止恶意用户通过重复发送捕获到的数据包所进行的攻击，即接收方会拒绝旧的
或重复的数据包。配置防重放功能，在SSL VPN实例配置模式下，使用以下命令：
anti-replay {32 | 64 | 128 | 256 | 512}
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
在SSL VPN实例配置模式下使用该命令no的形式恢复默认防重放窗口：
no anti-replay
配置分片功能
用户可以指定是否允许转发设备将包进行分片处理。配置分片功能，在SSL VPN实例配置模式下，使用以下
命令：
df-bit {copy | clear | set}

<!-- 来源页 1514 -->
l
copy – 直接从发包端拷贝IP包的DF选项。该选项为系统默认选项。
l
clear – 允许转发设备对包做分片处理。
l
set – 不允许转发设备对包做分片处理。
在SSL VPN实例配置模式下使用该命令no的形式恢复系统的默认设置：
no df-bit
配置空闲时间
空闲时间指客户端与服务端在无流量状态下能够保持连接状态的最长时间，超出空闲时间后，服务端将断开
与客户端的连接。配置空闲时间，在SSL VPN实例配置模式下，使用以下命令：
idle-time time-value
l
time-value – 指定空闲时间，单位为分钟。默认值是30分钟。取值范围是15到1500分钟。
在SSL VPN实例配置模式下使用该命令no的形式恢复空闲时间的默认值：
no idle-time
配置强制下线时间表
为SSL VPN实例指定强制下线时间表，时间表生效后，系统将按照时间表周期计划或绝对计划的起始时间强
制在线用户下线。配置强制下线时间表，在SSL VPN实例配置模式下，使用以下命令：
kickout-all-user schedule schedule-name
l
schedule-name - 指定时间表名称。系统将在时间表的起始时间强制用户在线。
注意:
l
起始时间与结束时间不能相同，否则时间表无法生效。
l
时间表生效后再上线的用户会在时间表下一次生效时被强制下线。
配置用户同名登录功能
用户同名登录功能指允许同一个用户在多个地点同时登录认证。开启用户同名登录功能，在SSL VPN实例配
置模式下，使用以下命令：
allow-multi-logon
执行该命令后，开启用户同名登录功能，并且不对同一用户名的同时登录个数做限制。用户可以在SSL VPN
实例配置模式下通过使用以下命令指定用户同名登录的个数：
allow-multi-logon number number

<!-- 来源页 1515 -->
l
number – 指定用户同名登录个数。范围是1到99999999。
在SSL VPN实例配置模式下使用以下命令no的形式关闭用户同名登录功能：
no allow-multi-logon
配置URL重定向功能
URL重定向功能是指在SSL VPN服务端配置重定向的URL，客户端认证成功后将自动跳转到指定URL的页
面。默认情况下，URL重定向功能是关闭的。配置URL重定向功能，在SSL VPN实例配置模式下，使用以下
命令：
redirect-url url title name
l
url – 指定认证成功后，客户端自动跳转页面的URL，取值范围为1到255字符。系统支持HTTP
（http://）和HTTPS（https://）两种类型的URL。
l
title name – 指定重定向URL的描述信息，范围为1到31字符。
在SSL VPN实例配置模式下使用该命令no的形式取消URL重定向功能：
no redirect-url
URL内容格式
根据重定向页面类型的不同，StoneOS支持内容符合下列格式的URL输入，以HTTP类型URL为例：
l
UTF-8编码格式的页面：输入“URL”+“username=$USER&password=$PWD”。比如，
“http://www.abc.com/oa/login.do?username=$USER&password=$PWD”
l
GB2312编码格式的页面：输入“URL”+“username=$GBUSER&password=$PWD”。比如，
“http://www.abc.com/oa/login.do?username=$GBUSER&password=$PWD”
l
其它页面：直接输入URL。比如，http://www.abc.com
注意: 关于URL重定向功能的具体实例，请参阅“URL重定向配置举例”。
启用/禁用清除SSL VPN桌面版客户端主机缓存数据功能
为了保证用户SSL VPN桌面版客户端主机的隐私数据安全性，用户可以在SSL VPN桌面版客户端断开后，启
用清除桌面版客户端主机缓存数据功能，清除浏览器缓存、临时文件等隐私数据。启用/禁用清除桌面版客户
端主机缓存数据功能，在SSL VPN实例配置模式下，使用以下命令：
l
启用：host-cache-clear enable
l
禁用：host-cache-clear disable

<!-- 来源页 1516 -->
在HA Peer模式中使用SSL VPN
在HA Peer模式的网络环境中，分别在两台设备上配置正确有效的SSL VPN。当一台主设备或者其上下链路
出现故障时，SSL VPN客户端可以重新连接到另外一台主设备。用户需要指定重连地址列表。SSL VPN客户
端将根据重连地址列表中地址的优先级进行重连。若重连失败，将会循环尝试列表中的地址，直到连接成
功。用户可最多指定四个重连地址。四个重连地址按配置的列表顺序（Server1~Server4）进行优先级排
列。
配置重连地址列表，在SSL VPN实例配置模式下，使用如下命令：
cluster {server1 |server2 | server3 | server4} address [port port-number]
l
{server1 |server2 | server3 | server4} address – 指定用于SSL VPN连接的服务器IPv4地址、IPv6
地址或者域名。
l
port port-number – 指定用于SSL VPN连接的端口号。默认值是4433。
删除重连地址列表，在SSL VPN实例配置模式下，使用如下命令：
no cluster [server1 | server2 | server3 | server4]
l
no cluster - 删除所有重连地址配置。
l
server1 | server2 | server3 | server4 - 删除指定重连地址配置。
在使用此功能时，需要注意以下事项：
l
当SSL VPN客户端选择<自动重连>选项且用户通过client-auto-connect count命令在服务器端设置自
动重连次数为unlimited时，SSL VPN客户端将连接之前指定的连接地址，不会连接重连地址列表中的
地址；当用户通过命令设置自动重连次数为X次时，SSL VPN客户端将在X次连续重连失败后，使用重连
地址列表中的地址进行重连。
l
当SSL VPN客户端不选择<自动重连>选项时，无论服务器端的配置如何，SSL VPN客户端将直接使用地
址重连列表中的地址进行重连。
l
当使用支持此功能的系统固件时，如果服务器端没有配置重连地址列表，低于1.4.4.1207版本的SSL
VPN客户端可正常连接SSL VPN服务器端。StoneOS会提示用户存在新版本的SSL VPN客户端。如果服
务器端配置重连地址列表，当低于1.4.4.1207版本的SSL VPN客户端连接SSL VPN服务器端时，
StoneOS会提示用户进行升级。用户需要手动卸载旧版本的SSL VPN客户端，然后登陆SSL VPN的Web
登陆界面进行SSL VPN客户端的下载与安装。新版本的SSL VPN客户端可与不支持此功能的系统固件兼
容。

<!-- 来源页 1517 -->
绑定L2TP VPN实例
在使用iOS的老版本SSL VPN客户端Hillstone BYOD Client(HBC)与SSL VPN服务器进行连接时，需要为
SSL VPN实例绑定L2TP VPN实例且此实例需引用IPSec隧道。进行绑定配置，在SSL VPN实例配置模式
下，使用以下命令：
client-bind-lns tunnel-name
l
tunnel-name – 指定系统中已配置的L2TP VPN实例。此实例需要引用IPSec隧道。使用该命令no的形
式取消绑定配置：no client-bind-lns
l
对于绑定的L2TP VPN实例和引用的IPSec隧道，需要满足如下条件：
l
IPSec隧道的认证方式需要使用预共享密钥认证。
l
L2TP实例的隧道密码（通过secret secret-string指定）需要与IPSec隧道的预共享密钥一致。
l
L2TP实例与SSL VPN实例指定的AAA服务器需要一致。
l
L2TP实例的地址池需要正确配置，设备根据L2TP实例的地址池为iOS的SSL VPN客户端下发相关
地址。
绑定资源
配置资源和用户组/角色的绑定关系后，SSL VPN客户端才能在用户认证成功后将其可访问的资源列表显示
在系统默认浏览器的页面中。一个用户组/角色可以绑定多个资源，一个资源也可以绑定多个用户组/角色。
一个SSL VPN实例中最多可以配置256个绑定条目。
配置资源和用户组的绑定条目，在SSL VPN实例配置模式下，使用以下命令：
bind resource-list list-name {user-group aaa-server-name group-name | role role-name}
l
list-name –指定资源的名称。取值范围是1到63个字符。
l
aaa-server-name –指定用户组所属的认证服务器的名称。目前仅支持本地认证服务器和RADIUS认证
服务器。
l
group-name –指定用户组的名称。
l
role rolename–指定角色名称。
在SSL VPN实例配置模式下，使用以下命令可以取消指定的资源和用户组的绑定关系：
no bind resource-list list-name {user-group aaa-server-name group-name |role rolename}

<!-- 来源页 1518 -->
开启/关闭允许浏览器下载客户端功能
浏览器下载功能指通过浏览器Web页面的方式下载SSL VPN客户端，默认情况下，该功能为开启状态。当关
闭该功能后，用户可通过山石网科官网下载SSL VPN客户端。
开启允许浏览器下载客户端功能，在SSL VPN实例配置模式下，使用以下命令：
client-download-page enable
关闭允许浏览器下载客户端功能，在SSL VPN实例配置模式下，使用以下命令：
client-download-page disable
绑定SSL VPN实例到隧道接口
配置好的SSL VPN实例需要绑定到隧道接口，才能够生效。绑定SSL VPN实例到隧道接口，在隧道接口配置
模式下，使用以下命令：
tunnel scvpn instance-name
l
instance-name – 指定系统中已配置的SSL VPN实例的名称。
在隧道接口配置模式下使用该命令no的形式取消隧道接口与SSL VPN实例的绑定：
no tunnel scvpn instance-name
配置客户端USB Key证书认证
设备支持客户端USB Key证书认证。只要用户持有的USB Key支持标准的Windows SDK （Certificate
Store Functions），并且存储合法的证书，就能通过认证进而实现网络连通的目的。
USB Key证书认证功能支持以下两种认证方式：
l
用户名/密码+ USB Key：SSL VPN用户需要持有存储正确数字证书的USB Key，并且在登录时输入正
确的用户名、密码和USB Key用户口令，才能通过认证；
l
只用USB Key：SSL VPN用户需要持有存储正确数字证书的USB Key，并且在登录时输入正确的USB
Key用户口令，即可通过认证，无需输入用户名和密码。
注意: 当认证方式为“只用USB Key”时，
l
系统可以根据USB Key数字证书中的证书名称（证书CN字段）或者组织机构（证书OU字段）
为认证成功的用户映射相应的角色。
l
系统不支持允许本地用户修改密码。

<!-- 来源页 1519 -->
l
系统不支持配置短信口令认证功能。
l
如果移除USB Key，客户端不会自动重连。
实现USB Key证书认证功能，用户需在服务端配置以下功能：
l 开启USB Key证书认证功能
l 导入USB Key证书相应CA证书到信任域
l 配置USB Key证书相应CA证书的信任域
开启USB Key证书认证功能
默认情况下，服务端的USB Key证书认证功能为关闭状态，用户可以在SSL VPN实例配置模式下使用以下命
令开启USB Key证书认证功能：
client-cert-authentication [usbkey-only]
l
usbkey-only – 指定USB Key证书认证方式为“只用USB Key”。如不指定该参数，认证方式为“用户
名/密码+ USB Key”。
在SSL VPN实例配置模式下使用该命令no的形式关闭USB Key证书认证功能：
no client-cert-authentication [usbkey-only]
导入USB Key证书相应CA证书到信任域
用户可以通过多种方式（FTP、TFTP和USB）实现CA证书到信任域的导入。在执行模式下使用以下命令：
import pki trust-domain-name cacert from {ftp server ip-address [user user-name password
password] | tftp server ip-address | usb0 | usb1} file-name
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
的信任域。客户端所提交的证书匹配到其中任意一个信任域的CA证书，都会认证成功。

<!-- 来源页 1520 -->
注意: 客户端证书的签发CA及其所属的所有上级CA直至根CA均需要添加信任域，一个CA对应一个
信任域。
在SSL VPN实例配置模式下，使用以下命令：
client-auth-trust-domain trust-domain
l
trust-domain – 指定CA证书所在的PKI信任域，该信任域需已经创建。
如果需要配置多个信任域，需重复使用本命令。系统最多可以支持10个信任域。
在SSL VPN实例配置模式下使用该命令no的形式取消对PKI信任域的指定：
no client-auth-trust-domain trust-domain
提示: 关于如何创建PKI信任域，请参阅《用户认证》的“PKI配置”部分。
配置二次认证功能
二次认证功能是指SSL VPN用户使用用户名/密码或用户名/密码+数字证书方式登录时，收到登录请求的山
石网科设备通过短信口令、令牌口令、邮件口令的方式进行二次认证，用户输入收到的认证码后，才可以通
过认证，进而访问内网资源。
l "配置令牌口令认证" 在第1519页
l "配置短信口令认证" 在第1519页
l "配置邮件口令认证" 在第1542页
开启/关闭二次认证功能
默认情况下，系统的二次认证功能为关闭状态。开启/关闭二次认证功能，在SSL VPN实例配置模式下，使
用以下命令：
开启：two-step verification enable
关闭：two-step verification disable
指定认证类型
指定二次认证的类型，在SSL VPN实例配置模式下，使用以下命令：
two-step verification type {token | sms modem | sms service-provider | email }

<!-- 来源页 1521 -->
l
token- 指定通过令牌口令对用户进行二次认证。
l
sms modem - 指定通过短信猫发送短信口令对用户进行二次认证。
l
sms service-provider - 指定通过短信网关发送短信口令对用户进行二次认证。
l
email - 指定通过邮件口令对用户进行二次认证。
配置令牌口令认证
当用户登录时，通过绑定的令牌口令进行认证，并支持用户自定义令牌口令认证的提示信息。
配置提示信息
配置令牌口令认证的提示信息，在SSL VPN实例配置模式下，使用以下命令：
token-auth prompt-message message
l
prompt-message message- 指定提示信息，为1到255个字符长度的字符串。
配置短信口令认证
短信口令认证功能是指SSL VPN用户使用用户名和密码登录时，收到登录请求的山石网科设备通过短信猫或
短信网关自动向该用户的手机号码发送一条包含随机认证码的短信，用户输入收到的认证码后，才可以通过
认证，进而访问内网资源。
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

<!-- 来源页 1522 -->
短信猫认证配置
短信口令认证功能的服务端配置包括：
l 设置短信认证手机号码
l 配置短信认证码有效时间
l 配置短信认证码长度
l 配置短信验证内容
l 配置短信最大发送数量
l 发送测试短信
设置短信认证手机号码
SSL VPN本地用户和AD用户均可使用短信口令认证功能。管理员可以为每个本地用户和AD用户设置一个手
机号码。开启短信口令认证功能后，系统会向已指定的登录用户手机号码发送认证码短信。
为本地用户设置手机号码，在用户配置模式下，使用以下命令：
phone phone-number
l
phone-number – 指定本地用户手机号码。
在用户配置模式下使用该命令no的形式取消用户手机号码的指定：
no phone
为AD用户设置手机号码，需要在AD服务器的“mobile”属性中配置手机号码。
配置短信认证码有效时间
每条短信认证码都有一个有效时间，如果用户在有效时间内没有输入短信认证码也没有重新申请认证码，
SSL VPN服务端将自动断开连接。配置短信认证码有效时间，在SSL VPN实例配置模式下，使用以下命令：
sms-auth expiration expiration
l
expiration – 指定短信认证码有效时间。默认为10分钟，范围为1-10分钟。
在SSL VPN实例配置模式下使用该命令no的形式恢复系统默认有效时间：
no sms-auth expiration
配置短信认证码长度
配置短信认证码长度，在SSL VPN实例配置模式下，使用以下命令：
sms-auth verification-code-length length

<!-- 来源页 1523 -->
l
length – 指定短信认证码长度。取值范围为4至8个字符。默认为8个字符。
在SSL VPN实例配置模式下，使用该命令no的形式恢复默认短信认证码长度。
no sms-auth verification-code-length
配置短信验证内容
配置认证码短信的验证内容，在SSL VPN实例配置模式下，使用以下命令：
sms-auth message-content content
l
content – 指定认证码短信的验证内容，内容必须包含“＄VRFYCODE”（用于获取认证码），可以包
含“＄USERNAME”和“＄EXPIRATION”（“＄USERNAME”用于获取用户
名；“＄EXPIRATION”用于获取认证码有效期）。短信验证内容长度的取值范围为9至500个字符。若
未配置短信验证内容，将使用默认短信验证内容，默认短信验证内容为“Your num sms authing
message is vrfycode”(num为认证次数，vrfycode为认证码。)
在SSL VPN实例配置模式下，使用该命令no的形式恢复默认验证内容。
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

<!-- 来源页 1524 -->
exec sms sp sp-name tunnel-name sendtest-message to phone-number [test-msgcontentcontent ]
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
短信网关认证配置
山石网科安全设备可通过运营商的短信网关或者其代理服务器向用户发送短消息。配置该功能前，用户需先
向运营商索要短信网关的地址、发送短消息的设备ID等相关信息。
短信网关认证的配置包括：
1. 创建Service Provider（SP）实例，并根据需要，配置SP实例。
2. 绑定SP实例到已创建的SSL VPN隧道，开启短信网关认证功能。
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

<!-- 来源页 1525 -->
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

<!-- 来源页 1526 -->
no sms service-provider sp-name
配置SP实例介绍
在SP实例配置模式下，可以进行以下配置：
l 指定VRouter
l 指定发送方式
l 指定HTTP（S）报文的内容类型
l 指定编码格式
l 指定UMS/ACC/BEIKE/ALIYUNSMS/BEIKE协议
l 配置URL地址
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

<!-- 来源页 1527 -->
l 指定请求类型
l 指定机构子码
l 指定短信业务类型
l 指定交易码
l 指定渠道码
l 配置HTTP(S)-Plus类型短信网关
l 发送测试短信
l 指定短信网关实例
l 指定发送方名称或者签名
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

<!-- 来源页 1528 -->
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

<!-- 来源页 1529 -->
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

<!-- 来源页 1530 -->
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

<!-- 来源页 1531 -->
配置属性
当SP实例使用HTTP(S)协议类型时，不同短信网关的属性不同，系统通过配置的属性参数和短信网关进行交
互。常用的属性包括手机号码字段的参数名称、短信内容字段的参数名称、用户密码以及用户名等，最多可
以配置32条。其中手机号码字段的参数名称、短信内容字段的参数名称为默认属性，必须配置，密码字段和
其他自定义的用户字段均为可选属性。
注意:
l
仅当“发送方式”为“POST”、“内容类型”为“JSON”、参数类型默认为“HTTP DATA”
时，才支持配置节点名称和数组对象。
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

<!-- 来源页 1532 -->
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

<!-- 来源页 1533 -->
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

<!-- 来源页 1534 -->
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

<!-- 来源页 1535 -->
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

<!-- 来源页 1536 -->
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

<!-- 来源页 1537 -->
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

<!-- 来源页 1538 -->
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

<!-- 来源页 1539 -->
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

<!-- 来源页 1540 -->
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

<!-- 来源页 1541 -->
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

<!-- 来源页 1542 -->
命令行
解释
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

<!-- 来源页 1543 -->
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
指定短信网关实例
配置好的SP实例需要绑定到SSL VPN隧道才能生效。在SSL VPN实例配置模式下，使用以下命令指定短信网
关实例：
sms-auth enable servicer-provider sp-name
l
sp-name – 指定SP实例的名称，该名称须是已创建的SP实例名称。取值范围为1至31个字符。
指定发送方名称或者签名
当绑定到SSL VPN隧道的SP实例的协议类型为SGIP、USM或者ACC时，用户可以指定短信发送方名称以显
示在短信内容中；当绑定到SSL VPN隧道的SP实例的协议类型为ALIYUNSMS时, 用户需要输入在阿里云短
信服务中申请的短信签名，以显示在短信内容中。指定发送方名称或者短信签名，在SSL VPN实例配置模式
下，使用以下命令：
sms-auth sms-sender-name sender-name [without-auto-bracket]
l
sender-name – 指定发送方名称或者签名。取值范围是1到63字符。该签名需要与在阿里云短信服务
中申请的签名保持一致。
l
without-auto-bracket– 关闭发送方名称自动添加尖括号功能。例如，当短信网关名称指定为SGIP或
UMS服务商名称，且用户配置了发送方名称时，如果不配置该参数，验证短信中的发送方名称将会自动
添加尖括号。如果配置该参数，验证短信中的发送方名称不会自动添加尖括号。
在SSL VPN实例配置模式下，使用该命令no的形式取消发送方名称或者签名的指定：
no sms-auth sms-sender-name

<!-- 来源页 1544 -->
注意:
l
由于UMS企业信息平台限制，当使用短信网关认证时，发送方名称将会显示在UMS企业信息平
台注册的名称。
l
发送方名称自动添加尖括号功能对针对默认短信验证内容有效，若用户自定义配置了短信验证
内容，发送方名称自动添加尖括号功能将失效。如需要，用户可以在配置短信验证内容时，直
接在短信模板内容末尾处手动添加带尖括号的发送方名称。配置短信验证内容，请参阅配置短
信验证内容。
指定模板CODE
当绑定到SSL VPN隧道的SP实例的协议类型为ALIYUNSMS时，用户需要指定在阿里云短信服务中申请的短
信内容模板对应的CODE（代码）。指定模板CODE，在SSL VPN实例配置模式下，使用以下命令：
sms-auth sms-msg-templatecode word
l
word - 指定模板CODE，取值范围为1至30个字符。该参数需与在阿里云短信服务中申请的模板CODE
保持一致。
在SSL VPN实例配置模式下，使用no sms-auth sms-msg-templatecode命令取消模板CODE的指定。
显示短信网关配置信息
在任意模式下，使用以下命令查看短信网关的配置信息：
show sms service-provider [sp-name]
l
sp-name – 指定已创建的SP实例。如不指定，则默认显示所有已创建的SP实例的配置信息。
显示短信统计信息
在任意模式下，使用以下命令查看短信网关发送短信成功或失败的计数信息：
show tunnel scvpn scvpn-name smsp-statistice [clear]
l
scvpn-name – 指定已创建的SSL VPN实例名称。
l
clear – 清除所有的计数信息。
配置邮件口令认证
邮件口令认证功能是指SSL VPN用户使用用户名/密码或用户名/密码+数字证书方式登录时，收到登录请求
的山石网科设备通过邮件服务器自动向该用户的邮箱发送一条包含随机认证码的邮件，用户输入收到的认证

<!-- 来源页 1545 -->
码后，才可以通过认证，进而访问内网资源。
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
“etc/freeradius/users”中添加Hillstone-user-email属性值)

<!-- 来源页 1546 -->
指定邮件服务器
指定邮件服务器，该服务器上配有用于发送认证码的邮箱地址，在SSL VPN实例配置模式下，使用以下命
令：
email-auth smtp-server smtp-server-name
l
smtp-server--name – 指定邮件服务器，该服务器为系统中已配置的邮件服务器。取值范围为1至31
个字符。
在SSL VPN实例配置模式下，使用no email-auth smtp-server命令取消邮件服务器的指定。
配置认证码长度
配置邮件认证码长度，在SSL VPN实例配置模式下，使用以下命令：
email-auth verification-code-length length
l
length – 指定邮件认证码长度。取值范围为4至8个字符。默认为8个字符。
在SSL VPN实例配置模式下，使用no email-auth verification-code-length恢复默认认证码长度。
配置认证码有效时间
每个邮件认证码都有一个有效时间，如果用户在有效时间内没有输入认证码也没有重新申请认证码，SSL
VPN服务端将自动断开连接。配置邮件认证码的有效时间，在SSL VPN实例配置模式下，使用以下命令：
email-auth expiration value
l
value – 指定邮件认证码的有效时间。取值范围为1至10分钟。默认为10分钟。
在SSL VPN实例配置模式下，使用no email-auth expiration恢复默认有效时间。
配置发送方名称
配置认证码的发送方名称以显示在邮件内容中，在SSL VPN实例配置模式下，使用以下命令：
email-auth sender-name name
l
name – 指定认证码的发送方名称。取值范围为1至63个字符。为防止认证码邮件被认定为垃圾邮件，
建议用户进行认证码邮件发送方名称的配置。
在SSL VPN实例配置模式下，使用no email-auth sender-name恢复默认发送方名称。
配置邮件验证内容
配置认证码邮件的验证内容，在SSL VPN实例配置模式下，使用以下命令：
email-auth message-content content

<!-- 来源页 1547 -->
l
content – 指定认证码邮件的验证内容，内容必须包含“＄USERNAME”和“＄VRFYCODE”
（“＄USERNAME”用于获取用名；“＄VRFYCODE”用于获取认证码）。取值范围为18至128个字
符。默认内容为“ZTNA user <＄USERNAME> email verification code: ＄VRFYCODE. Do not
reveal to anyone! If you did not request this, please ignore it.”。
在SSL VPN实例配置模式下，使用no email-auth message-content恢复默认验证内容。
主机绑定
主机绑定功能是指SSL VPN对运行SSL VPN客户端的主机进行验证。用户在PC上通过SSL VPN客户端登录
时，客户端先收集主机的主板序列号、硬盘序列号、CPU ID和BIOS序列号，然后客户端对这些信息进行
MD5运算，生成一个32位的字符串，即主机ID。之后，客户端将主机ID以及用户名密码信息发送到SSL
VPN服务端进行验证。SSL VPN服务端根据未绑定主机列表和已绑定主机列表中记录表项以及主机验证配置
进行验证。未绑定主机列表和已绑定主机列表描述如下：
l 未绑定主机列表：客户端首次登录时，SSL VPN服务端会记录用户名与主机ID的对应关系，并加入未绑定主机列
表中。
l 已绑定主机列表：已绑定主机列表中包含允许验证通过的主机ID与用户名对应关系的表项。用户可以通过手工操
作或首次登录自动批准方式把候选表中的表项移入已绑定主机列表中。客户端登录时，SSL VPN服务端会先检查
已绑定主机列表中是否有该主机ID与用户名的对应关系表项，如果有，则通过主机验证，继续进行用户名密码验
证；如果没有，则直接中断SSL通讯过程。
注意: 对于虚拟化平台上部署的主机，由于主机ID无法保证唯一性，不同的虚拟机可能显示相同的
主机ID。
配置主机绑定功能
开启主机绑定功能
默认情况下，服务端的主机绑定功能处于关闭状态。在SSL VPN实例配置模式下，使用以下命令开启主机绑
定功能：
user-host-verify [allow-multi-host] [allow-shared-host] [auto-approved-first-bind]
l
user-host-verify – 开启主机绑定功能。默认情况下，仅允许一个用户通过一台主机登录，即用户名和
主机一一对应。
l
allow-multi-host – 允许一个用户通过多台主机登录。

<!-- 来源页 1548 -->
l
allow-shared-host – 允许多个用户通过一台主机登录。
l
auto-approved-first-bind – 用户首次登录时自动把用户名和主机ID的对应关系加入绑定表。
在SSL VPN实例配置模式下使用该命令no的形式关闭主机绑定功能：
no user-host-verify
批准候选表项
批准候选表项是把候选表中的主机ID与用户名的对应关系表项移到绑定表中。在任意模式下，使用以下命令
批准指定的候选表项：
exec scvpn instance-name approve-binding user user-name host host-id
l
scvpn instance-name – 指定SSL VPN实例的名称。
l
user user-name – 指定候选表项对应的用户名称。
l
host host-id – 指定候选表项对应的主机ID。
配置超级用户
超级用户不受主机验证功能限制，可以通过任意主机登录。在任意模式下使用以下命令配置候选表或者绑定
表中的用户为超级用户：
exec scvpn instance-name no-host-binding-check user user-name
l
scvpn instance-name – 指定SSL VPN实例的名称。
l
user user-name – 指定超级用户的用户名称，取值范围是1到95个字符。
使用以下命令取消超级用户配置：
exec scvpn instance-name host-binding-check user user-name
配置共享主机
通过共享主机登录的用户不受主机验证功能限制。在任意模式下使用以下命令配置候选表或者绑定表中的主
机为共享主机：
exec scvpn instance-name no-user-binding-check host host-id
l
scvpn instance-name – 指定SSL VPN实例的名称。
l
host
host-id – 指定共享主机的主机ID。该主机ID需要为候选表或者绑定表中的主机ID。
使用以下命令取消共享主机配置：
exec scvpn instance-name user-binding-check host host-id

<!-- 来源页 1549 -->
增加/减少预批准主机数
当允许一个用户通过多台主机登录且设置了用户首次登录自动批准用户名和主机ID的绑定关系时，默认情况
下，仅自动批准用户和首次登录主机ID的绑定关系表项，即仅批准一个主机ID，以后登录的主机ID进入候选
表。在任意模式下，使用以下命令增加/减少预批准主机数：
增加预批准主机数
exec scvpn instance-name increase-host-binding user user-name number
l
scvpn instance-name – 指定SSL VPN实例的名称。
l
user user-name – 指定用户名称。
l
number – 指定增加的预批准主机数。取值范围为1到32。系统将在原预批准主机数的基础上进行增
加。单个用户的预批准主机数的总数范围为0到100。
减少预批准主机数
exec scvpn instance-name decrease-host-binding user user-name number
l
scvpn instance-name – 指定SSL VPN实例的名称。
l
user user-name – 指定用户名称。
l
number – 指定减少的预批准主机数。取值范围为1到32。系统将在原预批准主机数的基础上进行减
少。单个用户的预批准主机数的总数范围为0到100。
清除绑定表
在任意模式下，使用以下命令清除绑定表或指定的绑定表项：
exec scvpn instance-name clear-binding [{user user-name [host host-id] | host host-id }]
l
scvpn instance-name – 指定SSL VPN实例的名称。
l
user user-name – 指定用户名称。如果不指定Host ID，则删除指定用户的所有绑定表项。
l
host host-id – 指定主机ID。
导出/导入绑定表
用户可以通过FTP、TFTP或USB方式实现绑定表的导出或导入。
导出绑定表
在执行模式下，使用以下命令导出绑定表：

<!-- 来源页 1550 -->
export scvpn user-host-binding to {ftp server ip-address [user user-name password
password] | tftp server ip-address | usb0 | usb1} [file-name]
l
ftp server ip-address [user user-name password password] – 指定通过FTP方式导出绑定表。
user user-name password password指定FTP服务器的IP地址以及访问服务器使用的用户名和密
码，当不指定用户名和密码时表示采用匿名登录方式。
l
tftp server ip-address – 指定通过TFTP方式导出绑定表。ip-address 指定TFTP服务器的IP地址。
l
usb0 | usb1 – 指定将绑定表导出到U盘根目录。
l
file-name– 指定导出的绑定表的文件名称。默认名称为scvpn_bind_file。
导入绑定表
在执行模式下，使用以下命令导入绑定表：
import scvpn user-host-binding from {ftp server ip-address [user user-name password
password] | tftp server ip-address | usb0 | usb1} [file-name]
l
ftp server ip-address [user user-name password password] – 指定通过FTP方式导入绑定
表。user user-name password password指定FTP服务器的IP地址以及访问服务器使用的用户名
和密码，不指定用户名和密码时表示采用匿名登录方式。
l
tftp server ip-address – 指定通过TFTP方式导入绑定表。ip-address 指定TFTP服务器的IP地址。
l
usb0 | usb1 – 指定从U盘根目录导入绑定表。
l
file-name – 指定要导入的文件名。
主机检测
主机检测功能是指SSL VPN服务端对运行SSL VPN客户端主机的安全状况进行检测，通过检查客户端主机的
操作系统、IE版本以及特定软件的安装情况等因素来评估客户端主机的安全级别，并根据不同安全级别为客
户端分配不同的资源访问权限，保证SSL VPN接入的安全性。
主机检测功能对客户端主机的详细检查内容，请参阅下表：
检查项目
详细描述
操作系统配置
l 操作系统版本（如Windows 2000、Windows 2003、Windows XP、Windows
Vista、Windows 7、Windows 8等）
l 操作系统补丁包版本（如Service Pack 1等）
l Windows特定补丁包是否安装（如KB958215等）

<!-- 来源页 1551 -->
检查项目
详细描述
l Windows安全中心和自动升级是否打开
l 防病毒软件是否必须安装，实时监控和病毒库在线升级是否打开
l 防间谍软件是否必须安装，实时监控和特征库在线升级是否打开
l 个人防火墙是否必须安装和实时保护是否打开
IE版本和安全级别是否达到指定标准
其他配置
指定进程是否正在运行
指定服务是否已经安装
指定服务是否正在运行
指定注册表键值是否存在
指定文件是否存在于操作系统中
基于角色的访问控制和主机检测流程
基于角色的访问控制是指用户的权限不是由用户名而是由用户在系统中的角色决定的，一个登录于某系统的
用户，可以通过它所对应角色的权限来决定其可以访问的系统资源。在权限管理中，角色作为中间桥梁把用
户和权限联系起来。
SSL VPN在主机检测流程中实现了基于角色的访问控制，在主机检测策略规则中引入初级角色和次级角色的
概念。初级角色主要用于用户从服务端获取对应的主机检测规则信息（包含主机检测的内容以及安全级
别）；次级角色决定检测失败用户的实际访问权限。
主机检测流程如下：
1. 客户端发起连接请求并成功认证。
2. 服务端下发主机检测规则到客户端。
3. 客户端根据主机检测规则对主机系统进行相应的安全检测。如果检测失败，则弹出检测结果进行提示。
4. 客户端将最终检测结果返回给服务端。
5. 服务端根据配置的主机检测策略规则断开检测失败客户端的连接或者根据其相应的次级角色授予实际访问权限。
另外，主机检测功能还支持动态的访问权限控制。一方面，当服务端的安全状况发生变化时，服务端会主动
下发主机检测规则给客户端，并要求客户端重新进行安全检测；另一方面，客户端可以周期性地进行安全检
查，比如可以定时地检查客户端主机的防病毒软件是否开启，如果用户在使用过程中关闭了防病毒软件，系
统可能会因此在用户的访问过程中改变该用户所属的角色，重新为该用户分配相应的权限。

<!-- 来源页 1552 -->
配置主机检测功能
配置主机检测Profile
主机检测Profile指定主机安全检查的内容以及安全级别。用户可以通过WebUI和CLI指定主机检测Profile
名称，但是Profile的内容需要通过WebUI进行配置。可参阅WebUI手册“主机检测”内容。
指定主机检测Profile，在全局配置模式下使用以下命令：
scvpn host-check-profile hostcheck-profile-name
l
hostcheck-profile-name – 指定主机检测Profile的名称。执行该命令后，系统创建指定名称的主机
检测Profile。
在全局配置模式下，使用no scvpn host-check-profile hostcheck-profile-name删除指定的主机检测
Profile。
配置主机检测策略规则
主机检测Profile配置完成后，只有把它引用到主机检测策略规则中，配置的安全检测功能才能对用户生效。
配置主机检测策略规则，请在SSL VPN实例配置模式下使用以下命令：
host-check [role role-name] profile profile-name [guest-role guestrole-name] | redirect-url
url [periodic-check period-time]
l
role role-name – 指定用户的初级角色，该初级角色为AAA服务器中已配置的用户角色。如果配置该
参数，该主机检测Profile对该指定角色有效；如果不配置此参数，该主机检测Profile将作为缺省
Profile并对所有未指定Profile的用户生效。
注意：如果配置了角色，则需要在对应的AAA服务器中配置角色映射规则，否则角色配置将不生效。
l
profile profile-name – 指定绑定的主机检测Profile名称。
l
guest-role guestrole-name – 指定用户的次级角色。当客户端的主机检测失败时，如果配置该参
数，用户将获得该次级角色拥有的访问权限；如果不配置该参数，系统将断开该客户端连接。
l
guest-role guestrole-name | redirect-url url- 指定主机检测异常处理方法。
l
guest-role guestrole-name – 指定用户的次级角色。当客户端的主机检测失败时，如果配置
该参数，用户将获得该次级角色拥有的访问权限；如果不配置该参数，系统将断开该客户端连接。
l
redirect-url url-指定重定向URL。当客户端的主机检测失败时，如果配置该参数，将会自动打
开浏览器并跳转到指定的URL，引导用户下载主机检测需要安装的软件并断开客户端连接；如果不
配置该参数，系统将断开该客户端连接。

<!-- 来源页 1553 -->
l
periodic-check period-time – 指定该用户的自动检测周期。单位为分钟，取值范围为5到1440分
钟，默认值为30分钟。
可以配置多条该命令添加多个安全检测策略规则。当一个用户可匹配多个安全检测策略规则时，服务端会按
照查找到的第一条相匹配的规则进行处理；另外，一个用户可以绑定到一个或者多个角色，当一个用户绑定
到多个角色且多个角色均配置安全检测策略规则时，服务端会按照查找到的第一条相匹配的规则进行处理。
在SSL VPN实例配置模式下，使用no host-check [role role-name] profile profile-name [guestrole guestrole-name | redirect-url url] [periodic-check period-time]取消主机检测策略规则的配
置。
根据上述主机检测策略规则CLI描述，表20-3列出主机检测策略规则配置情况、检测结果和权限授予之间的
详细对应关系：
策略规则配置
检测结果
通过检测
未通过检测
初级角色：配置
profile：配置
次级角色：配置
重定向URL：未配置
获得初级角色对应访问权限
获得次级角色对应访
问权限
初级角色：配置
profile：配置
次级角色：未配置
重定向URL：配置
获得初级角色对应访问权限
打开重定向URL下载
需要的软件并且断开
连接
初级角色：配置
profile：配置
次级角色：未配置
重定向URL：未配置
获得初级角色对应访问权限
断开连接并给出提示
初级角色：未配置
profile：配置
次级角色：配置
重定向URL：未配置
正常连接
获得次级角色对应访
问权限
初级角色：未配置
profile：配置
次级角色：未配置
重定向URL：配置
正常连接
打开重定向URL下载
需要的软件并且断开
连接
初级角色：未配置
profile：配置
次级角色：未配置
重定向URL：未配置
正常连接
断开连接并给出提示

<!-- 来源页 1554 -->
最优路径检测
目前，大规模VPN网络往往都是跨ISP（Internet Service Provider，互联网服务提供商）的，但是不同
ISP间通信时带宽小、延迟大，严重影响了VPN的应用效果。针对此问题，Hillstone设备SSL VPN支持最优
路径检测功能，该功能能够使不同ISP线路接入的客户端自动选择最快线路连接到SSL VPN服务端，从而提
高访问总部资源时的速度。
Hillstone设备SSL VPN最优路径检测功能的网络环境实现包括以下两种：
如上图所示，SSL VPN客户端直接访问服务端出接口地址。SSL VPN服务端首先需要申请多条不同的ISP上
网线路连接到Internet，并启用相应数目的服务端接口作为SSL VPN通道出接口。当客户端使用不同的ISP
上网线路访问总部资源时，如果开启了服务端检测最优通道功能，服务端Hillstone设备会通过客户端的源
接入地址判断其ISP类型，根据判断，将所有的SSL VPN出接口IP地址按照优先级重新排序并下发给客户
端，由客户端选择连接的最优通道；如果开启由客户端检测最优通道的功能，客户端会通过发送UDP探测包
自动判断最优链路，并选择连接的最优通道。

<!-- 来源页 1555 -->
如上图所示，SSL VPN客户端通过DNAT设备访问SSL VPN服务端，该DNAT设备会将客户端的访问地址映
射到SSL VPN服务端的出接口地址。这种方式下，DNAT设备外网端口通过多条不同的ISP上网线路连接到
Internet，用户需要将DNAT设备的外网接口地址配置为服务端地址簿中的地址条目，当客户端使用不同的
ISP上网线路访问DNAT设备外网接口地址时，如果开启了服务端检测最优通道功能，服务端Hillstone设备
会通过客户端的源接入地址判断其ISP类型，根据判断，将所有的DNAT外网接口IP地址按照优先级重新排序
并下发给客户端，由客户端选择连接的最优通道；如果开启由客户端检测最优通道的功能，客户端会通过发
送UDP探测包自动判断最优链路，并选择连接的最优通道。
配置最优路径检测功能
启用服务端接口作为SSL VPN通道出接口
启用服务端接口作为SSL VPN通道出接口，在SSL VPN实例配置模式下，使用以下命令：
interface interface-name
l
interface-name – 指定服务端接口的名称。
多次执行该命令启用多个接口，系统允许最多开启两个接口。在SSL VPN实例配置模式下使用该命令no的形
式取消指定服务端接口的配置：
no interface interface-name

<!-- 来源页 1556 -->
配置最优路径检测功能
配置最优路径检测功能，在SSL VPN实例配置模式下，使用以下命令：
link-select { mode {client-detect | server-detect} | {addr1 | addr2 | addr3 | addr4} address
[port port-number]}
l
mode {client-detect | server-detect} - 指定最优通道检测的模式，client-detect表示由客户端检
测最优通道，server-detect表示由服务端检测最优通道。默认情况下由客户端检测最优通道。
l
{addr1 | addr2 | addr3 | addr4} address - 指定DNAT设备外网接口IP。系统允许最多配置四个IP地
址，可以为IPv4或者IPv6地址。
l
port port-number –指定DNAT设备外网接口HTTPS端口号。默认值是4433。取值范围是1到
65535。为避免与WebUI使用的HTTPS端口号相冲突，建议用户不要把HTTPS端口号设置为443。
删除最优路径检测功能的配置，在SSL VPN实例配置模式下，使用以下命令：
no link-select [addr1 | addr2 | addr3 | addr4]
l
no link-select - 删除最优路径检测功能的所有配置信息。
l
addr1 | addr2 | addr3 | addr4 - 删除指定DNAT设备外网接口IP。
另外，SSL VPN最优路径检测的应用还提供多链路冗余的功能，当任意一条链路不通时，数据均会自动切换
到另外的链路，从而保证客户端连接的稳定性（切换过程中流量可能会中断）。
通过Radius认证服务器限定用户的访问范围
当用户使用Radius认证方式时，系统可限定已认证用户的访问范围。对于已认证的用户，系统从Radius服
务器上获取此用户的授权区域信息（即可访问的目的地址范围）。根据该授权区域，系统为此用户动态创建
从其源地址到授权区域的安全策略；对于未通过认证的用户，系统拒绝将其接入网络。当用户注销登录、登
陆超时、或被系统管理员强制登出后，对应的安全策略将被自动删除。
在任何模式下，使用以下命令查看用户的授权区域信息：
show auth-user username user-name
l
user-name – 指定要查看的用户的用户名。
配置Radius服务器
用户需要在Radius服务器的字典文件中增如下自定义属性：
属性名称
属性类型
描述
Hillstone-user-policy-dstipaddr
授权区域的起始IP地址。请输入IPv4地址。

<!-- 来源页 1557 -->
属性名称
属性类型
描述
ip-begin
Hillstone-user-policy-dstip-end
ipaddr
授权区域的终止IP地址。请输入IPv4地址。
添加自定义属性后，为Radius服务器中的用户赋予相应的属性值。完成赋值后，重启Radius服务。当用户
使用SSL VPN客户端成功认证后，系统将根据此用户在Radius服务器中配置的属性值限定其可访问的网络
资源。如果没有为此用户设定授权区域，用户将不受访问限制。
显示SSL VPN信息
用户可以通过show命令查看系统SSL VPN信息。
l
显示SSL VPN实例信息：
show tunnel scvpn [scvpn-instance-name]
l
显示指定SSL VPN实例当前在线的客户端信息：
show scvpn client scvpn-instance-name [user user-name]
l
显示所有SSL VPN实例当前在线的客户端信息：
show auth-user scvpn [interface interface-name | vrouter vrouter-name | slot slot-no]
l
显示主机验证绑定表：
show scvpn user-host-binding scvpn-instance-name {host [host-id] | user [user-name]}
l
显示SSL VPN授权用户数量：
show secure-connect user capacity
l
显示客户端升级URL：
show secure-connect update-url
l
显示客户端下载页面的定制标题：
show secure-connect download-web-page-title
l
显示客户端信息：
show secure-connect client-info

<!-- 来源页 1558 -->
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

<!-- 来源页 1559 -->
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

<!-- 来源页 1560 -->
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

<!-- 来源页 1561 -->
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

<!-- 来源页 1562 -->
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

<!-- 来源页 1563 -->
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

<!-- 来源页 1564 -->
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

<!-- 来源页 1565 -->
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

<!-- 来源页 1566 -->
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

<!-- 来源页 1567 -->
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

<!-- 来源页 1568 -->
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

<!-- 来源页 1569 -->
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

<!-- 来源页 1570 -->
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

<!-- 来源页 1571 -->
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

<!-- 来源页 1572 -->
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

<!-- 来源页 1573 -->
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

<!-- 来源页 1574 -->
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

<!-- 来源页 1575 -->
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

<!-- 来源页 1576 -->
3. 双击SelectUSBKey.exe，系统弹出<Select Default Certificate>对话框。如下图所示：
Export：将USB Key的CSP Name以注册表文件（.reg）格式导出到本地目录。
Update：刷新证书列表。
Close：关闭对话框。
4. 在<Certificate List>中选中所需证书，点击『Export』按钮，将USB Key的CSP Name信息以注册表文件
（.reg）格式导出到本地目录。如下图所示:
导出USB Key的CSP Name信息后，用户将信息文件存放在客户端PC目录中并双击该文件，将文件中的信
息添加进客户端PC注册表。添加完成后，当用户通过该USB Key进行SSL VPN客户端认证时，客户端会自
动选择USB Key中的数字证书传送至服务端，不需要用户手动选择证书。

<!-- 来源页 1577 -->
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

<!-- 来源页 1578 -->
“导入”按钮，导入对服务器进行认证的证书。点击“删除”按钮，删除列表中的可信证书。
l 状态通知：当客户端连接成功或失败时，出现相应的状态弹窗通知。
客户端的卸载
从PC上卸载Secure Connect Windows客户端，从“开始菜单”点击“所有程序> Hillstone Secure
Connect > Hillstone Secure Connect”，右键点击“Hillstone Secure Connect”，在菜单中选择
“卸载”。
Hillstone Secure Connect客户端for Linux
型号说明：v5.4.0及以上版本的Secure Connect Linux客户端支持接入双栈类型的SSL
VPN/ZTNA实例。
支持Linux系统的SSL VPN/ZTNA客户端工具为Hillstone Secure Connect，建议在以下操作系统中运
行：
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

<!-- 来源页 1579 -->
下面以CentOS 7.6为例介绍客户端的下载与安装、启动与连接、升级与卸载、客户端GUI和菜单，其他系统
配置方法类似。
下载与安装
下载和安装Secure Connect Linux客户端，按照以下步骤进行操作：
1. 访问Hillstone官网客户端下载页面https://www.hillstonenet.com.cn/support-and-training/hillstonesecure-connect/；或者访问服务端的客户端下载地址https://IP-Address:Port-Number。其中“IPAddress”和“Port-Number”分别为服务端SSL VPN或ZTNA实例中指定的接口的IP地址和HTTPS端口号。
2. 下载完成后，使用鼠标右击图标并选择“属性”，进入属性页面。
3. 在属性页面，点击“权限”标签页，勾选“允许作为程序执行文件”，点击“关闭”。

<!-- 来源页 1580 -->
4. 双击安装程序，并按照设置向导完成安装。
启动与连接
客户端安装成功后，按照以下步骤启动和登录客户端：
1. 双击Linux系统桌面上的客户端图标，系统进入超级用户身份认证页面，输入超级用户密码，并点击“授权”，
进入客户端主界面。
2. 在主界面，点击“添加连接”按钮，系统弹出下图所示对话框。
输入连接信息。

<!-- 来源页 1581 -->
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

<!-- 来源页 1582 -->
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

<!-- 来源页 1583 -->
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
l
客户端连接支持OAuth2认证的服务端（R10F4及以后F版本，R11及以后版本）时，客户端页
面返回服务端配置的认证方式。例如服务端配置用户名/密码和OAuth2认证，则客户端的<连
接>页面，显示用户名/密码和第三方应用登录方式。
l
客户端连接不支持OAuth2认证的服务端（R10F4之前版本）时，客户端的连接页面默认显示3
种认证方式，需要选择服务端配置的认证方式才能连接成功。例如服务端配置了仅证书的认证
方式，则在客户端页面需要选择数字证书的方式才能连接成功。如下图所示：

<!-- 来源页 1584 -->
编辑和删除登录信息条目
当连接为断开状态时，将光标指向登录信息条目，点击
图标编辑登录信息条目；点击
图标删除登录
信息条目。
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

<!-- 来源页 1585 -->
地址信息:显示IP地址信息。
发送
显示通过压缩算法处理后的发送数据长度百分比。
接收
显示通过压缩算法处理后的接收数据长度百分比。
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

<!-- 来源页 1586 -->
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

<!-- 来源页 1587 -->
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

<!-- 来源页 1588 -->
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
6. 阅读权限需求。
7. 点击“安装”按钮。
安装成功后会在Android系统中出现程序图标，如下图所示：

<!-- 来源页 1589 -->
启动与连接
客户端安装成功后，按照以下步骤启动和登录客户端：
1. 点击Android系统桌面上的Hillstone Secure Connect图标，进入客户端界面。
2. 在“首页”页签，点击“+”，进入“添加连接”页面。
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

<!-- 来源页 1590 -->
选项
说明
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
SPA功能，并通过默认端口敲门。该选项为默认设置。
通信稳定性优化
设置是否使用TCP协议传输数据，默认为关闭。启用该功能时需要服务端配置
TCP端口。
3. 连接信息填写完成后，点击“确定”按钮，系统将添加一条登录信息条目。如需要，可重复以上步骤添加多个登
录信息条目。

<!-- 来源页 1591 -->
4. 返回客户端主界面，选择刚刚添加的登录信息条目，打开“连接状态”开关。
5. 如果服务端开启短信口令、令牌口令或邮件口令认证功能，需输入相应的认证码完成认证。
6. 连接成功后，此时就可以实现客户端与服务端之间的加密通信。
编辑和删除登录信息条目
点击需要编辑的登录信息条目，点击
图标，可以编辑登录信息条目。
按住需要删除的登录信息条目，向右拖拽，可以删除登录信息条目。

<!-- 来源页 1592 -->
查看连接信息
点击客户端界面下方的“连接信息”页签，可查看连接统计、接口和路由信息。
连接统计信息：

<!-- 来源页 1593 -->
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

<!-- 来源页 1594 -->
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

<!-- 来源页 1595 -->
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

<!-- 来源页 1596 -->
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

<!-- 来源页 1597 -->
编辑和删除登录信息条目
点击需要编辑的登录信息条目，点击
图标，可以编辑登录信息条目。
按住需要删除的登录信息条目，向右拖拽，可以删除登录信息条目。

<!-- 来源页 1598 -->
查看连接信息
点击客户端界面下方的“连接信息”页签，可查看连接统计、接口和路由信息。
连接统计信息：

<!-- 来源页 1599 -->
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

<!-- 来源页 1600 -->
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

<!-- 来源页 1601 -->
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

<!-- 来源页 1602 -->
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

<!-- 来源页 1603 -->
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

<!-- 来源页 1604 -->
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

<!-- 来源页 1605 -->
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

<!-- 来源页 1606 -->
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

<!-- 来源页 1607 -->
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

<!-- 来源页 1608 -->
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
Hillstone Secure Connect客户端for ChineseOS
型号说明：v5.4.0及以上版本的Secure Connect ChineseOS客户端支持接入双栈类型的SSL
VPN/ZTNA实例。
支持国产操作系统的SSL VPN/ZTNA客户端工具为Hillstone Secure Connect，建议在以下操作系统中运
行：

<!-- 来源页 1609 -->
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
2. 点击“安装”按钮，安装Hillstone Secure Connect客户端。安装完成后显示为“打开”按钮。点击“打开”按
钮可直接启动客户端。

<!-- 来源页 1610 -->
启动与连接
客户端安装成功后，按照以下步骤启动和登录客户端：
1. 在“开始”菜单栏中找到“Hillstone Secure Connect”，点击客户端，进入客户端主界面。也可以右键点击
“Hillstone Secure Connect”，在菜单中选择桌面添加快捷方式或固定到任务栏。
2. 在主界面，点击“添加连接”按钮，系统弹出下图所示对话框。

<!-- 来源页 1611 -->
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

<!-- 来源页 1612 -->
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

<!-- 来源页 1613 -->
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

<!-- 来源页 1614 -->
编辑和删除登录信息条目
当连接为断开状态时，将光标指向登录信息条目，点击
图标编辑登录信息条目；点击
图标删除登录
信息条目。
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

<!-- 来源页 1615 -->
地址信息:显示IP地址信息。
压缩率
发送
显示通过压缩算法处理后的发送数据长度百分比。
接收
显示通过压缩算法处理后的接收数据长度百分比。
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

<!-- 来源页 1616 -->
点击
，选择“日志级别”，设置需要显示的日志的级别。
配置检查更新
客户端支持自动更新检测和手动更新检测。手动更新检测操作是在客户端页面，点击
，选择“检查更
新”。当有可用更新时，在弹出的提示框中，进行如下操作：
l 选择“确认”，用户可前往国产操作系统自带的软件应用商店下载安装最新的客户端。
l 选择“不再提醒”，下次启动客户端时，将不再出现自动更新提示。
通用设置
在客户端页面，点击“设置”。
l 自动重连：开启后，客户端将在连接中断时进行自动重连。
l 自动登录：开启后，客户端将在启动时使用上一次登录成功的连接信息进行自动登录。
l 连接最小化：开启后，客户端将在连接成功后自动缩小到托盘。
l 可信服务器证书管理：在建立连接时开启“验证服务器证书”功能后，点击
按钮，在<可信证书>页面点击
“导入”按钮，导入对服务器进行认证的证书。点击“删除”按钮，删除列表中的可信证书。

<!-- 来源页 1617 -->
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
后，可以获得访问权限。禁止访问的应用资源不在Portal页面上展示，如果用户被禁止访问任何应用资源，
Portal页面将展示“无可用的Web服务资源”。
l 显示主页面：当客户端界面处于最小化状态时，点击此项可以显示客户端主页面。
l 退出：退出Secure Connect ChineseOS客户端程序。
客户端的卸载
从PC上卸载Secure Connect ChineseOS客户端，从“开始”菜单栏中找到“Hillstone Secure
Connect”，右键点击“Hillstone Secure Connect”，在菜单中选择“卸载”。
SSL VPN配置举例
本节介绍SSL VPN相关的配置举例。
l "例：SSL VPN-用户名密码/USB Key认证配置举例" 在第1616页
l "例：SSL VPN-URL重定向配置举例" 在第1620页
l "例：SSL VPN-主机安全检测配置举例" 在第1622页
l "例：SSL VPN-最优路径检测配置举例" 在第1629页

<!-- 来源页 1618 -->
l " 例：通过SSL VPN实现远程终端访问内网业务" 在第1636页
l "例：使用iOS/Android设备远程访问内网服务" 在第1647页
例：SSL VPN-用户名密码/USB Key认证配置举例
该节介绍SSL VPN配置实例。分别针对用户名密码方式认证和USB Key认证方式进行进行举例。
组网需求
外网PC1（IP：6.6.6.5/24）通过Hillstone设备设备访问内网服务器Server1
（IP：10.160.65.52/21），要求使用SSL VPN对数据进行加密。组网图参见下图：
l 需求一：使用用户名密码方式对用户进行认证。
l 需求二：使用USB Key方式对用户进行认证。
需求一配置步骤
第一步：创建本地用户：
hostname(config)# aaa-server local
hostname(config-aaa-server)# user user1
hostname(config-user)# password 123456
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)#exit
第二步：配置地址池：
hostname(config)# access-address-pool pool1
hostname(config-address-pool)# address 20.1.1.1 20.1.1.100 netmask 255.255.255.0
hostname(config-address-pool)# dns 20.1.1.1

<!-- 来源页 1619 -->
hostname(config-address-pool)# wins 20.1.1.2
hostname(config-address-pool)# exit
hostname(config)#
第三步：配置SSL VPN实例。系统默认添加split-tunnel-route 0.0.0.0/0的路由条目，如需限定远程用户
访问范围，请使用no split-tunnel-route 0.0.0.0/0命令。
hostname(config)# tunnel scvpn ssl1
hostname(config-tunnel-scvpn)# access-address-pool pool1
hostname(config-tunnel-scvpn)# aaa-server local
hostname(config-tunnel-scvpn)# interface ethernet0/5
hostname(config-tunnel-scvpn)# https-port 4433
hostname(config-tunnel-scvpn)# split-tunnel-route 10.160.64.0/21
hostname(config-tunnel-scvpn)# exit
hostname(config)#
第四步：创建隧道接口并把SSL VPN实例绑定到此接口（隧道接口的IP地址必须与SSL VPN地址池的IP地址
在同一网段）：
hostname(config)# zone VPN
hostname(config-zone-VPN)#
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone VPN
hostname(config-if-tun1)# ip address 20.1.1.101/24
hostname(config-if-tun1)# tunnel scvpn ssl1
hostname(config-if-tun1)# exit
hostname(config)#
第五步：配置从VPN安全域到trust安全域的策略：
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone VPN
hostname(config-policy-rule)# dst-zone trust

<!-- 来源页 1620 -->
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
第六步:在PC1的浏览器中输入https://6.6.6.1:4433，在弹出的登录页面输入用户名密码，分别是
“user1”和“123456”。认证通过后下载并安装Hillstone Secure Connect。
第七步:通过Web方式或客户端方式登录SSL VPN服务端成功后，PC1便可通过SSL VPN安全地访问trust安
全域中的资源。
需求二配置步骤
为了增加安全性，在需求一的基础上开启USB Key证书认证功能：只有当用户的USB Key支持标准的
Windows SDK （Certificate Store Functions），并且存储的证书合法时，用户才可以登录设备。本例
以用户持有Hillstone UKey为例。
准备工作
使用USB Key认证，用户需要做以下准备工作：
l 准备数字证书和相应的CA证书。
l 准备Hillstone UKey和配套光盘。
l 使用Hillstone UKey管理员软件导入数字证书到USB Key。
配置步骤
第一步：配置服务端：
#创建PKI信任域stone，并指定该信任域的证书获得方式为terminal
hostname(config)# pki trust-domain stone
hostname(config-trust-domain)# enrollment terminal
hostname(config-trust-domain)# exit
hostname(config)#

<!-- 来源页 1621 -->
#开启SSL VPN实例SSL1的USB Key证书认证功能，并指定CA证书的信任域
hostname(config)# tunnel scvpn ssl1
hostname(config-tunnel-scvpn)# client-cert-auth
hostname(config-tunnel-scvpn)# client-auth-trust-domain stone
hostname(config-tunnel-scvpn)# exit
hostname(config)#
#导入CA证书文件到CA证书的信任域
hostname(config)# exit
hostname# import pki stone cacert from tftp server 192.168.1.2 certnew.cer
第二步：客户端操作，步骤如下：
1. 在客户端PC安装Hillstone UKey驱动程序。
2. 插入USB Key。
3. 打开SSL VPN客户端，按下图所示依次填写登录信息（密码为“123456”；PIN码为USB Key的用户口令，默认
为1111）。填写完毕，点击『登录』按钮，进行连接。

<!-- 来源页 1622 -->
例：SSL VPN-URL重定向配置举例
某公司总部有一套OA系统，并且选用一台Hillstone设备作为SSL VPN服务端。现要求通过配置，实现客户
端在登录SSL VPN的同时成功登录OA系统。
该实例通过配置URL重定向功能实现上述需求。组网图参见下图。
配置步骤
第一步：创建本地用户：
hostname(config)# aaa-server local
hostname(config-aaa-server)# user test
hostname(config-user)# password test
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)#
第二步：配置地址池：
hostname(config)# access-address-pool pool1
hostname(config-address-pool)# address 20.1.1.1 20.1.1.255 netmask 255.255.255.0
hostname(config-address-pool)# dns 20.1.1.1
hostname(config-address-pool)# wins 20.1.1.2

<!-- 来源页 1623 -->
hostname(config-address-pool)# exit
hostname(config)#
第三步：配置SSL VPN实例，并在实例中配置URL重定向功能。系统默认添加split-tunnel-route
0.0.0.0/0的路由条目，如需限定远程用户访问范围，请使用no split-tunnel-route 0.0.0.0/0命令。
hostname(config)# tunnel scvpn ssl1
hostname(config-tunnel-scvpn)# access-address-pool pool1
hostname(config-tunnel-scvpn)# aaa-server local
hostname(config-tunnel-scvpn)# interface ethernet0/5
hostname(config-tunnel-scvpn)# https-port 4433
hostname(config-tunnel-scvpn)# redirect-url
http://192.10.5.201/oa/login.do?username=$USER&password=$PWD title-en OA titlezh 中文OA系统
hostname(config-tunnel-scvpn)# split-tunnel-route 10.160.64.0/21
hostname(config-tunnel-scvpn)# split-tunnel-route 192.10.5.0/24
hostname(config-tunnel-scvpn)# exit
hostname(config)#
第四步：创建隧道接口并把SSL VPN实例绑定到此接口（隧道接口的IP地址必须与SSL VPN地址池的IP地址
在同一网段）：
hostname(config)# zone VPN
hostname(config-zone-VPN)# exit
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone VPN
hostname(config-if-tun1)# ip address 20.1.1.1/24
hostname(config-if-tun1)# tunnel scvpn ssl1
hostname(config-if-tun1)# exit
hostname(config)#
第五步：配置从VPN安全域到trust安全域的策略：
hostname(config)# policy-global
hostname(config-policy)# rule

<!-- 来源页 1624 -->
hostname(config-policy-rule)# src-zone VPN
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
第六步：在PC1的浏览器中输入https://6.6.6.1:4433，在弹出的登录页面输入用户名密码，分别是
“test”和“test”。认证通过后下载并安装Hillstone Secure Connect。
第七步：通过Web方式或客户端方式登录SSL VPN服务端成功后，客户端自动跳转到OA系统认证页面并成
功登录；同时，客户端菜单中增加“中文OA系统”菜单项。
当OA系统认证页面关闭后，用户可以点击“中文OA系统”菜单项，再次打开OA系统认证页面。
例：SSL VPN-主机安全检测配置举例
该节介绍SSL VPN主机安全检测配置实例。
组网需求
外网PC通过Hillstone设备设备访问公司总部资源，需要组建SSL VPN网络并配置主机安全检测功能，以达
到以下目的：
l 客户端PC通过SSL VPN访问公司总部资源；
l 公司总部的软件私有网络网段（IP：10.1.1.0/24）的资源只允许属于角色“sw”的用户访问；总部下载网络网
段（IP：10.1.2.0/24）的资源只允许属于角色“dl”的用户访问；总部公开网络网段（IP：10.1.3.0/24）的资
源允许所有的用户访问；
l 对访问总部资源的客户端PC进行主机安全检测，并根据检测结果授予相应的资源访问权限。

<!-- 来源页 1625 -->
组网图参见下图：
配置步骤
第一步：创建本地用户：
hostname(config)# aaa-server local type local
hostname(config-aaa-server)# user pc1
hostname(config-user)# password xxxfcvg236
hostname(config-user)# exit
hostname(config-aaa-server)# user pc2
hostname(config-user)# password xcabuv112
hostname(config-user)# exit

<!-- 来源页 1626 -->
hostname(config-aaa-server)# user pc3
hostname(config-user)# password xacfomg763
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)#
第二步：配置角色映射规则：
hostname(config)# role sw
hostname(config)# role dl
hostname(config)# role-mapping-rule rule1
hostname(config-role-mapping)# match user pc1 role sw
hostname(config-role-mapping)# match user pc1 role dl
hostname(config-role-mapping)# match user pc2 role dl
hostname(config-role-mapping)# exit
hostname(config)# aaa-server local type local
hostname(config-aaa-server)# role-mapping-rule rule1
hostname(config)#
第三步：配置服务端接口：
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 1.1.1.1/24
hostname(config-if-eth0/1)# exit
hostname(config)#
第四步：配置主机安全检测Profile（请通过WebUI配置相应的Profile文件）：
hostname(config)# scvpn host-check-profile dl-security-check
hostname(config-profile_scvpn)# exit
hostname(config)# scvpn host-check-profile sw-security-check
hostname(config-profile_scvpn)# exit
hostname(config)#

<!-- 来源页 1627 -->
通过WebUI配置主机安全检测Profile，指定主机安全检测内容如下：
1. 从页面左侧导航树选择并点击“配置h网络hSSL VPN”，进入SSL VPN页面。
2. 从页面右侧辅助栏的<任务>区选择『主机检测』链接，进入SSL VPN的主机检测页面。
3. 点击主机检测规则列表左上角的『新建』按钮，弹出<主机检测配置>对话框。在『基本配置』标签页，进行如下
配置：
l 名称：dl-security-check
l OS版本：依次从下拉菜单中选择“至少”、“Win2003”、“无”
l 补丁包1：KB958215
l 最低IE版本：IE6.0
l 最低IE安全级别：高
4. 在『高级配置』标签页，进行如下配置：
l 安全中心：勾选“必须启用”
l 防病毒软件：依次勾选“安装软件”、“实时监控”、“病毒库更新”
l 防间谍软件：依次勾选“安装软件”、“实时监控”、“特征库更新”
l 防火墙：依次勾选“安装软件”、“实时监控”
5. 点击『确定』按钮，保存所做配置并返回上一级对话框/页面。
6. 点击主机检测规则列表左上角的『新建』按钮，弹出<主机检测配置>对话框。在『基本配置』标签页，进行如下
配置：
l 名称：sw-security-check
l OS版本：依次从下拉菜单中选择“必须匹配”、“WinXP”、“SP3”
l 补丁包1：KB921883
l 最低IE版本：IE7.0
l 最低IE安全级别：高
7. 在『高级配置』标签页，进行如下配置：
l 安全中心：勾选“必须启用”
l 自动更新：勾选“必须启用”
l 防病毒软件：依次勾选“安装软件”、“实时监控”、“病毒库更新”
l 防间谍软件：依次勾选“安装软件”、“实时监控”、“特征库更新”

<!-- 来源页 1628 -->
l 防火墙：依次勾选“安装软件”、“实时监控”
l 文件路径名称：在<文件1>下拉菜单中选择“存在”并在文本框中输入“C:\Program
Files\McAfee\VirusScan\Enterprise.exe”
8. 点击『确定』按钮，保存所做配置并返回上一级对话框/页面。
第五步：配置地址池：
hostname(config)# access-address-pool pool1
hostname(config-address-pool)# address11.1.1.10 11.1.1.100 netmask 255.255.255.0
hostname(config-address-pool)# dns 10.1.1.1
hostname(config-address-pool)# wins wins
hostname(config-address-pool)# exit
hostname(config)#
第六步：配置SSL VPN实例。系统默认添加split-tunnel-route 0.0.0.0/0的路由条目，如需限定远程用户
访问范围，请使用no split-tunnel-route 0.0.0.0/0命令。
hostname(config)# tunnel scvpn ssl1
hostname(config-tunnel-scvpn)# access-address-pool pool1
hostname(config-tunnel-scvpn)# aaa-server local
hostname(config-tunnel-scvpn)# interface ethernet0/1
hostname(config-tunnel-scvpn)# https-port 4433
hostname(config-tunnel-scvpn)# split-tunnel-route 10.1.1.0/24 metric 10
hostname(config-tunnel-scvpn)# split-tunnel-route 10.1.2.0/24 metric 5
hostname(config-tunnel-scvpn)# split-tunnel-route 10.1.3.0/24 metric 3
hostname(config-tunnel-scvpn)# host-check role sw profile sw-security-check guestrole dl
hostname(config-tunnel-scvpn)# host-check profile dl-security-check periodic-check
50
hostname(config-tunnel-scvpn)# exit
hostname(config)#
第七步：创建隧道接口并把SSL VPN实例绑定到此接口（隧道接口的IP地址必须与SSL VPN地址池的IP地址
在同一网段）：

<!-- 来源页 1629 -->
hostname(config)# zone VPN
hostname(config-zone-VPN)# exit
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone VPN
hostname(config-if-tun1)# ip address11.1.1.1/24
hostname(config-if-tun1)# tunnel scvpn ssl1
hostname(config-if-tun1)# exit
hostname(config)#
第八步：配置策略规则：
hostname(config)# address sw
hostname(config-addr)# ip 10.1.1.0/24
hostname(config-addr)# exit
hostname(config)# address dl
hostname(config-addr)# ip 10.1.2.0/24
hostname(config-addr)# exit
hostname(config)# address public
hostname(config-addr)# ip 10.1.3.0/24
hostname(config-addr)# exit
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone VPN
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr sw
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# role sw
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit

<!-- 来源页 1630 -->
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone VPN
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr dl
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# role dl
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone VPN
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr public
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
客户端PC发起SSL VPN连接请求并通过认证后，服务端会根据配置的安全检测策略规则对客户端进行安全检
测，并根据检测结果授予客户端用户相应的资源访问权限。本示例的主机安全检测策略规则配置以及资源访
问权限授予之间的对应关系，请参见下表：
用户
策略规则配置
检测结果
未通过检测
通过检测
初级角色：sw profile：sw-security-check 次级角
色：dl 自动检测周期：默认30分钟CLI：host-check
role sw profile sw-security-check guest-role dl
可以访问软件私有网
络并且每隔30分钟自
动进行安全检测
可以访问下载
网络并且每隔30分
钟自动进行安全检
测
PC1
PC2
初级角色：未配置（根据default角色“dl”授予权限）
profile：dl-security-check 次级角色：未配置自动检
可以访问下载网络并
且每隔50分钟自动进
断开连接

<!-- 来源页 1631 -->
用户
策略规则配置
检测结果
未通过检测
通过检测
测周期：50分钟CLI：host-check profile dl-securitycheck periodic-check 50
行安全检测
PC3
初级角色：未配置profile：dl-security-check 次级角
色：未配置自动检测周期：50分钟CLI：host-check
profile dl-security-check periodic-check 50
可以访问公开网络并
且每隔50分钟自动进
行安全检测
断开连接
例：SSL VPN-最优路径检测配置举例
该节介绍SSL VPN最优路径检测配置实例。
组网需求一
某公司总部选用一台Hillstone设备作为SSL VPN服务端，并通过两条不同的上网线路ISP1（接口
ethernet0/1，IP：202.2.3.1/24）和ISP2（接口ethernet0/3，IP：196.1.2.3/24）接入Internet。现
要求通过配置，实现客户端PC（IP：64.2.3.1）通过最优路径检测功能访问公司总部Server
（IP：10.1.1.2）。组网图参见下图：
该需求有两种配置方式，分别是：

<!-- 来源页 1632 -->
l 服务端作最优通道判断
l 客户端判断最优通道
服务端作最优通道判断
第一步：创建本地用户：
hostname(config)# aaa-server local type local
hostname(config-aaa-server)# user user1
hostname(config-user)# password drgrhrgerg231
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)#
第二步：配置服务端接口：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 10.1.1.0/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 202.2.3.1/24
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/3
hostname(config-if-eth0/3)# zone untrust
hostname(config-if-eth0/3)# ip address 196.1.2.3/24
hostname(config-if-eth0/3)# exit
hostname(config)#
第三步：配置地址池：
hostname(config)# access-address-pool pool1
hostname(config-address-pool)# address 11.1.1.10 11.1.1.100 netmask
255.255.255.0

<!-- 来源页 1633 -->
hostname(config-address-pool)# dns 10.1.1.1
hostname(config-address-pool)# wins 10.1.1.2
hostname(config-address-pool)# exit
hostname(config)#
第四步：配置SSL VPN实例（在SSL VPN实例中配置最优路径检测功能）。系统默认添加split-tunnelroute 0.0.0.0/0的路由条目，如需限定远程用户访问范围，请使用no split-tunnel-route 0.0.0.0/0命
令。
hostname(config)# tunnel scvpn ssl1
hostname(config-tunnel-scvpn)# access-address-pool pool1
hostname(config-tunnel-scvpn)# aaa-server local
hostname(config-tunnel-scvpn)# interface ethernet0/1
hostname(config-tunnel-scvpn)# interface ethernet0/3
hostname(config-tunnel-scvpn)# https-port 4433
hostname(config-tunnel-scvpn)# split-tunnel-route 10.1.1.0/24 metric 10
hostname(config-tunnel-scvpn)# link-select server-detect
hostname(config-tunnel-scvpn)# exit
hostname(config)#
第五步：创建隧道接口并把SSL VPN实例绑定到此接口（隧道接口的IP地址必须与SSL VPN地址池的IP地址
在同一网段）：
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone untrust
hostname(config-if-tun1)# ip address 11.1.1.1/24
hostname(config-if-tun1)# tunnel scvpn ssl1
hostname(config-if-tun1)# exit
hostname(config)#
第六步：配置策略规则：
hostname(config)# address dst
hostname(config-addr)# ip 10.1.1.0/24
hostname(config-addr)# exit

<!-- 来源页 1634 -->
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr dst
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
第七步：配置ISP信息：
hostname(config)# isp-network isp1
hostname(config-isp)# subnet 202.2.3.0/24
hostname(config-isp)# subnet 64.2.3.0/24
hostname(config-isp)# exit
hostname(config)#
当客户端PC通过ISP2向服务端发起连接请求时，服务端判断客户端PC的IP地址与SSL VPN出接口
ethernet0/1的IP地址同属于ISP1，根据判断，将带有优先级的出接口IP地址下发给客户端，最终，客户端
PC将选择通过ISP1访问公司总部Server。
客户端判断最优通道
此种情况下的配置与服务端作最优通道判断中的配置基本相似，不同在于：
第四步：配置SSL VPN实例（在SSL VPN实例中配置最优路径检测功能）：
hostname(config)# tunnel scvpn ssl1
……
hostname(config-tunnel-scvpn)# link-select
……
第七步：无（不需配置）

<!-- 来源页 1635 -->
当客户端PC通过ISP2向公司总部发起连接请求时，服务端会将SSL VPN出接口ethernet0/1和
ethernet0/3的IP地址下发给客户端，客户端通过发送UDP探测包自动判断最优通道。
组网需求二
某公司总部选用一台Hillstone设备作为SSL VPN服务端，并通过一台DNAT设备经由两条不同的上网线路
ISP1（IP：202.2.3.1/24）和ISP2（IP：196.1.2.3/24）接入Internet。现要求通过配置，实现客户端
PC（IP：64.2.3.1）通过最优路径检测功能访问公司总部Server（IP：10.1.1.2）。组网图参见下图：
该需求有两种配置方式，分别是：
l 服务端作最优通道判断
l 客户端判断最优通道
服务端作最优通道判断
第一步：创建本地用户：
hostname(config)# aaa-server local type local

<!-- 来源页 1636 -->
hostname(config-aaa-server)# user user1
hostname(config-user)# password drgrhrgerg231
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)#
第二步：配置服务端接口：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone trust
hostname(config-if-eth0/0)# ip address 10.1.1.0/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone dmz
hostname(config-if-eth0/1)# ip address 192.168.1.2/24
hostname(config-if-eth0/1)# exit
hostname(config)#
第三步：配置地址池：
hostname(config)# access-address-pool pool1
hostname(config-address-pool)# address 11.1.1.10 11.1.1.100 netmask
255.255.255.0
hostname(config-address-pool)# dns 10.1.1.1
hostname(config-address-pool)#wins 10.1.1.2
hostname(config-address-pool)# exit
hostname(config)#
第四步：配置SSL VPN实例（在SSL VPN实例中配置最优路径检测功能）。系统默认添加split-tunnelroute 0.0.0.0/0的路由条目，如需限定远程用户访问范围，请使用no split-tunnel-route 0.0.0.0/0命
令。
hostname(config)# tunnel scvpn ssl1
hostname(config-tunnel-scvpn)# access-address-pool pool1
hostname(config-tunnel-scvpn)# aaa-server local

<!-- 来源页 1637 -->
hostname(config-tunnel-scvpn)# interface ethernet0/1
hostname(config-tunnel-scvpn)# https-port 4433
hostname(config-tunnel-scvpn)# split-tunnel-route10.1.1.0/24 metric 10
hostname(config-tunnel-scvpn)# link-select server-detect 202.2.3.1 https-port 2234
196.1.2.3 https-port 3367
hostname(config-tunnel-scvpn)# exit
hostname(config)#
第五步：创建隧道接口并把SSL VPN实例绑定到此接口（隧道接口的IP地址必须与SSL VPN地址池的IP地址
在同一网段）：
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone untrust
hostname(config-if-tun1)# ip address 11.1.1.1/24
hostname(config-if-tun1)# tunnel scvpn ssl1
hostname(config-if-tun1)# exit
hostname(config)#
第六步：配置策略规则（从dmz到trust安全域的策略）：
hostname(config)# address dst
hostname(config-addr)# ip 10.1.1.0/24
hostname(config-addr)# exit
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone dmz
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr dst
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit

<!-- 来源页 1638 -->
hostname(config)#
第七步：配置ISP信息：
hostname(config)# isp-network isp1
hostname(config-isp)# subnet 202.2.3.0/24
hostname(config-isp)# subnet 64.2.3.0/24
hostname(config-isp)# exit
hostname(config)#
当客户端PC通过ISP2向DNAT设备发起连接请求时，DNAT设备会将客户端的访问地址196.1.2.3:3367映
射到SSL VPN服务端的出接口地址192.168.1.2:4433。此时，服务端判断客户端PC的IP地址与DNAT外网
接口IP地址202.2.3.1/24同属于ISP1，根据判断，将带有优先级的DNAT外网接口IP地址下发给客户端，最
终，客户端PC将选择通过ISP1访问公司总部Server。
客户端判断最优通道
此种情况下的配置与服务端作最优通道判断中的配置基本相似，不同在于：
第四步：配置SSL VPN实例（在SSL VPN实例中配置最优路径检测功能）：
hostname(config)# tunnel scvpn ssl1
……
hostname(config-tunnel-scvpn)# link-select 202.2.3.1 https-port 2234 196.1.2.3
https-port 3367
……
第九步:无（不需配置）
当客户端PC通过ISP2向公司总部发起连接请求时，DNAT设备会将客户端的访问地址196.1.2.3:3367映射
到SSL VPN服务端的出接口地址192.168.1.2:4433。服务端会将DNAT外网接口IP地址下发给客户端，客
户端通过发送UDP探测包自动判断最优通道。
例：通过SSL VPN实现远程终端访问内网业务
本示例介绍如何通过配置SSL VPN实现远程终端用户访问企业内部服务器资源。

<!-- 来源页 1639 -->
提示: 本示例所展示的操作步骤，基于StoneOS 5.5R9版本进行配置。若有变动，请以实际页面为
准。
组网场景
组网环境如下图所示，远程用户A和B位于互联网。这两个用户使用SSL VPN的方法访问其公司内网服务器
Server，认证方式为用户名密码方式。同时，使用短信验证码的二次认证方式，增强用户登录的安全性；用
户A属于用户组group1，用户B属于角色role1，属于用户组group1的用户允许访问Bug系统，对应角色
role1的用户允许访问OA系统；使用TCP协议进行数据传输，加强通信稳定性。
配置步骤
步骤一：创建本地用户。
选择“对象> 用户> 本地用户”，选
择本地服务器“local”并点击“新建>
用户”。
l 名称：test1
l 密码：123456
l 重新输入密码：123456
l 手机号码：根据实际情况配置。当用
户登录SSL VPN客户端时，若已开启短
信认证功能，短信网关或短信猫会将
验证码发送到该手机号码上。
重复该步骤，创建名称为test2的用
户。

<!-- 来源页 1640 -->
步骤二：将用户test1绑定至用户组。
选择“对象> 用户> 本地用户”，选
择本地服务器“local”并点击“新建>
用户组”。
l 名称：group1
l 用户：test1
步骤三：将用户test2绑定至角色。
选择“对象> 角色> 角色”，点击
“新建”。
l 角色名称：role1
选择“对象> 角色> 角色映射”，点
击“新建”。
l 映射名称：mapping-role1
l 角色映射规则：角色“role1”；类型
“用户”；映射源“test2”
选择“对象> AAA服务器”，选择本地
服务器“local”并点击“编辑”。
l 角色映射规则：mapping-role1
注意：将用户绑定至角色时，任意服务
器类型的用户，都需要配置本地服务器
的“角色映射规则”。否则用户登录客
户端时，无法下发相应角色的隧道路
由。

<!-- 来源页 1641 -->
步骤四：配置短信网关。
选择“系统> 短信发送参数> 短信网
关”，点击“新建”。短信网关请按照
实际情况配置。
l 协议类型：SGIP
l 服务商名称：hillstone
l 虚拟路由器：trust-vr
l 网关主机：IP；43.240.X.X
l 短信网关端口：8801
l 设备编码：27484X
l 来源号码：10690333
l 用户名与密码：根据实际情况，输入
登录短信网关的用户名和密码
步骤五：配置SSL VPN地址池。
选择“对象> 接入地址池”，选择IPv4
标签页点击“新建”创建一个地址池条
目。
l 地址池名称：scpool
l 起始IP：192.168.1.2（请使用私
网地址，避免与公网IP冲突）
l 终止IP：192.168.1.100（请使用
私网地址，避免与公网IP冲突）
l 子网掩码：255.255.255.0
l DNS1：10.160.65.60

<!-- 来源页 1642 -->
步骤六：创建隧道接口。
选择“网络> 安全域”，并点击“新
建”。
l 安全域名称：VPN
l 类型：三层安全域
l 虚拟路由器：trust-vr
选择“网络> 接口”，并点击“新建>
隧道接口”。
l 接口名称：tunnel1
l 绑定安全域：三层安全域
l 安全域：VPN
l 类型：静态IP
l IP地址：192.168.1.1
l 网络掩码：255.255.255.0
隧道接口的IP地址必须与SSL VPN地址
池的IP地址在同一网段。
步骤七：配置资源。
选择“网络> VPN > SSL VPN”，并点
击页面右上方“相关配置> 资源列表”。
在<资源列表>页面，点击“新建”。
l 资源名称：Bug管理系统
l 资源条目：条目名称“Bug管理系
统”；URL“https://bug123.com”
重复该步骤，创建资源名称为OA系统、
条目名称为OA系统、URL为
https://oa123.com的资源。
步骤八：配置SSL VPN服务端。

<!-- 来源页 1643 -->
步骤八：配置SSL VPN服务端。
选择“网络> VPN > SSL VPN”，并点击“新建”。
在<名称/接入用户>标签页做如下配置：
l SSL VPN名称：ssl vpn
l 接入用户：点击“新建”，在“AAA服务器”的下拉菜单中选择“local”
在<接入接口/隧道接口>标签页做如下配置：
l 出接口：ethernet0/3 （ethernet0/3 的IP地址已配置为10.196.4.136/24）
l 服务端口：4433
l 隧道接口：tunnel1
l 地址池：scpool
在<隧道路由配置>标签页，点击“新建”配置两条隧道路由。
用户组group1对应的隧道路由：
l IP：10.160.65.0
l 子网掩码：255.255.255.0
l 类型：用户组
l 用户组/角色：group1
l AAA服务器：local

<!-- 来源页 1644 -->
步骤八：配置SSL VPN服务端。
角色role1对应的隧道路由：
l IP：172.16.12.0
l 子网掩码：255.255.255.0
l 类型：角色
l 用户组/角色：role1
隧道路由IP地址须与内网服务器（Server）的IP地址在同一网段。
在<绑定资源>标签页，点击“新建”绑定两条资源。
用户组group1对应的资源：
l 条目名称：Bug管理系统
l 类型：用户组
l 用户组/角色：group1
l AAA服务器：local
角色role1对应的资源：
l 条目名称：OA系统
l 类型：角色
l 用户组/角色：role1

<!-- 来源页 1645 -->
步骤八：配置SSL VPN服务端。
点击<高级配置>标签，在<参数配置>标
签页做如下配置：
l 高级参数
l 数据端口（TCP）：10000
服务端配置完成后，需同时开启客户端的
“通信稳定性优化”功能，PC端的客户端
才可通过TCP协议与服务端通信。
点击<高级配置>标签，在<二次认证>标
签页做如下配置：
l 二次认证：点击“启用”按钮
l 类型：短信口令验证
l 短信认证类型：短信网关
l 短信网关名称：hillstone
l 短信认证码有效时间：10
l 发送方名称：FWvisitAPP
l 认证码长度：8
步骤九：创建从VPN到内网服务器的策略规则。
选择“对象> 地址簿”，点击“新建”
配置安全策略policy1和policy2的源地
址。
l 名称：address1-src
l 类型：IPv4
l 地址成员：IP范围；192.168.1.2-
192.168.1.100
建议地址成员的配置与SSL VPN接入地
址池的IP地址范围保持一致。

<!-- 来源页 1646 -->
步骤九：创建从VPN到内网服务器的策略规则。
选择“对象> 地址簿”，点击“新建”
配置内网服务器资源的地址簿。
配置Bug系统的地址簿：
l 名称：bug-address
l 类型：IPv4
l 地址成员：IP/掩
码；10.160.65.52/32
重复该步骤，配置OA系统的地址簿。
l 名称：oa-address
l 类型：IPv4
l 地址成员：IP/掩
码；172.16.12.12/32
选择“策略> 安全策略”，并点击“新
建”配置用户test1的安全策略。
l 名称：policy1
l 地址类型：IPv4
l 源安全域：VPN
l 源地址：address1-src
l 目的安全域：trust
l 目的地址：bug-address
l 用户：group1
l 服务：Any  
l 动作：允许
重复该步骤，配置用户test2的安全策
略。
l 名称：policy2

<!-- 来源页 1647 -->
步骤九：创建从VPN到内网服务器的策略规则。
l 地址类型：IPv4
l 源安全域：VPN
l 源地址：address1-src
l 目的安全域：trust
l 目的地址：oa-address
l 用户：role1
l 服务：Any  
l 动作：允许
步骤十：验证结果
配置完成后，在用户test1的PC端的浏览器中输入
https://10.196.4.136:4433，在弹出的页面中选
择“Windows”标签，并点击“立即下载”。根
据系统提示安装Hillstone Secure Connect。
在Hillstone Secure Connect客户端输入如
下信息：
l 服务器：10.196.4.136
l 端口：4433
l 用户名：test1
l 密码：123456
输入上述信息后，客户端将弹出<短信口令认
证>对话框，进行VPN登录的二次认证。

<!-- 来源页 1648 -->
步骤十：验证结果
打开客户端后，右上角点击“添加连接”按
钮，弹出<添加连接>页面，输入如下信息：
l 连接名称：test1
l 服务器：10.196.4.136
l 端口：4433
l 通信稳定性优化：开（用户成功登录SSL VPN
客户端后，将使用TCP协议安全地访问trust安
全域中服务器Sever的资源）
然后点击“确定”按钮，生成一条登录信息条
目。
点击登录信息条目中的“连接”按钮，客户端
弹出连接页面。
l 用户名：test1
l 密码：123456
输入上述信息后，客户端将弹出<短信口令认
证>对话框，进行VPN登录的二次认证。
查看用户test1手机端收到的8位数字的验证
码，填入<短信口令认证>的文本框，并点击
“验证”。
客户端显示连接成功后，用户test1的PC便可通过SSL VPN安全地访问内网服务器中的Bug管理系统。同时，点击
客户端的“路由”标签页，可查看到服务端给属于用户组group1的用户test1下发的隧道路由。

<!-- 来源页 1649 -->
步骤十：验证结果
用户test2的PC端重复以上步骤。
客户端显示连接成功后，用户test2的PC便可通过SSL VPN安全地访问内网服务器中的OA系统。同时，点击客户
端的“路由”标签页，可查看到服务端给对应角色role1的用户test2下发的隧道路由。
例：使用iOS/Android设备远程访问内网服务
本示例介绍如何通过iOS/Android设备使远程用户访问企业内部服务器资源。
提示: 本示例所展示的操作步骤，基于StoneOS 5.5R2版本进行配置。若有变动，请以实际页面为
准。
组网环境如下图所示，远程用户位于互联网。该用户使用iOS或Android设备访问其公司内网服务器
Server1。认证方式为用户名密码方式，连接基于SSL VPN，请参阅" 例：通过SSL VPN实现远程终端访问
内网业务" 在第1636页的步骤一到步骤五创建SSL VPN实例。

<!-- 来源页 1650 -->
配置步骤
使用iOS设备远程访问内网服务
以下以2.0.8版本的VPN客户端为例。
步骤一：下载安装Hillstone Access Client。
在APP Store中搜索Hillstone Access
Client，点击“获取”下载并安装此应
用。

<!-- 来源页 1651 -->
步骤二：建立与服务端连接。
点击iOS系统桌面上的HSAccess图
标，进入登录界面。
l 连接名：connection1
l 服务器：153.34.29.1
l 端口：4433
l 用户名：user1
l 密码：123456
点击“登录”。登录成功后，客户端与
服务端成功建立连接。
步骤三：安装VPN配置文件。
连接建立后，弹出“添加VPN配置”提
示框。点击“允许”，安装VPN配置文
件。

<!-- 来源页 1652 -->
步骤三：安装VPN配置文件。
在随后弹出的“输入密码”提示框中，
输入iOS锁屏密码。
密码输入正确后，iOS开始执行安装。
安装完成后，点击“完成”。
步骤四：建立VPN连接。
在iOS中，选择“设置> 通用> VPN与
设备管理”。
在列表中，选中connection1。
打开VPN开关。iOS进行VPN连接。

<!-- 来源页 1653 -->
步骤五：验证连接状态。
当iOS显示VPN状态为“已连接”且客
户端在“连接”界面显示“当前已经连
接”，表明客户端与服务端成功建立
VPN连接。
步骤六：访问内网服务。
通过iOS设备访问Server1。

<!-- 来源页 1654 -->
使用Android设备远程访问内网服务
步骤一：下载安装Hillstone Secure Connect。
访问客户端下载页
面，在页面右下侧
“VPN移动客户端下
载”扫描Android客
户端二维码。
https://www.hillstonenet.com.cn/product/technology/VPN.html
打开下载链接并下载安
装文件。下载完成后，
安装此应用。
步骤二：建立与服务端连接。
点击Android系统桌面上的Hillstone
Secure Connect图标，进入登录界
面。
l 服务器：153.34.29.1
l 端口：4433
l 用户名：user1
l 密码：123456
点击“登入”。
登入成功后，系统通知栏显示钥匙形图
标，此时就可以实现客户端与服务端之
间的加密通信。
步骤三：访问内网服务。
通过Android设备访问Server1。

<!-- 来源页 1655 -->
拨号VPN
拨号VPN介绍
拨号VPN指，在中心设备上仅配置一个VPN隧道，之后允许多个远程拨号端通过VPN隧道访问中心设备。远
程拨号端需配置与中心设备VPN隧道对应的IKE VPN，进行数据保护。同时，中心设备通过预共享密钥或者
证书认证方式，认证拨号端的身份，从而建立与拨号端的VPN隧道。
拨号VPN的应用
StoneOS通过“基于策略的VPN”和“基于路由的VPN”两种方式把配置好的VPN隧道应用到Hillstone设
备上，实现流量的加密解密安全传输。
l 基于策略的VPN：将配置成功的VPN隧道名称引用到策略规则中，使符合条件的流量通过指定的VPN隧道进行传
输。此方式只支持分支机构访问中心，不支持中心访问分支机构以及Hub-and-spoke。
l 基于路由的VPN：将配置成功的VPN隧道与隧道接口绑定；配置静态路由时，将隧道接口指定为下一跳路由。
拨号VPN配置
l 中心设备配置
l 拨号端配置
中心设备配置
拨号VPN的中心设备配置包括：
l 配置P1提议
l 配置ISAKMP网关
l 配置P2提议
l 配置隧道
l 配置拨号端用户信息
配置P1提议
P1提议是IKE安全提议，可应用到ISAKMP网关上，在SA第一阶段使用。对IKE安全提议的配置包括指定认证
方式、加密算法、验证算法、DH组和安全联盟的生命周期。

<!-- 来源页 1656 -->
创建P1提议
创建一个P1提议，即IKE安全提议，请在全局配置模式下使用以下命令：
isakmp proposal p1-name
l
p1-name – 指定所创建的P1提议的名称。执行该命令后，CLI进入到P1提议配置模式。用户可以在该模
式下对P1提议进行参数配置。
使用no isakmp proposal p1-name命令删除指定的P1提议。
指定认证方式
此处指定的是IKE身份认证的方式。身份认证用来确认通信双方的身份。方式有两种：预共享密钥认证和数
字证书认证。对于预共享密钥认证方式，认证字用来作为一个输入产生密钥，认证字不同是不可能在双方产
生相同的密钥的。指定IKE安全提议的身份认证方式，在P1提议配置模式下使用以下命令：
authentication {pre-share | rsa-sig | dsa-sig | gm-de }
l
pre-share – 指定使用预共享密钥认证方式。该方式为默认认证方式。
l
rsa-sig – 指定使用RSA数字证书认证方式。
l
dsa-sig – 指定使用DSA数字证书认证方式。此方式对应的验证算法只能为SHA-1。
l
gm-de– 指定使用国密数字信封认证方式。当认证方式为此选项时，加密算法仅支持使用SM1和SM4，
验证算法仅支持使用SHA或SM3。
使用no authentication命令恢复默认认证方式。
指定加密算法
StoneOS提供以下五种加密算法：3DES、DES、128bit AES、192bit AES以及256bit AES。指定IKE安
全提议的加密算法，在P1提议配置模式下使用以下命令：
encryption {3des | des | aes | aes-192 | aes-256}
l
3des – 指定使用3DES加密方法。密钥长度为192比特。该方法为StoneOS系统默认方法。
l
des – 指定使用DES加密方法。密钥长度为64比特。
l
aes – 指定使用AES加密方法。密钥长度为128比特。
l
aes-192 – 指定使用192bit AES加密方法。密钥长度为192比特。
l
aes-256 – 指定使用256bit AES加密方法。密钥长度为256比特。
使用no encryption命令恢复默认加密算法。

<!-- 来源页 1657 -->
指定验证算法
StoneOS支持以下验证算法：MD5、SHA-1和SHA-2（包括SHA-256、SHA-384和SHA-512）。指定IKE
安全提议的验证算法，在P1提议模式下使用以下命令：
hash {md5 | sha | sha256 | sha384 | sha512}
l
md5 – 指定使用MD5验证算法。摘要为128比特。
l
sha – 指定使用SHA-1验证算法。摘要为160比特。该算法为StoneOS的默认算法。
l
sha256 – 指定使用SHA-256验证算法。摘要为256比特。
l
sha384 – 指定使用SHA-384验证算法。摘要为384比特。
l
sha512 – 指定使用SHA-512验证算法。摘要为512比特。
使用no hash命令恢复默认认证方式。
选择DH组
Diffie-Hellman（DH）是一种建立密钥的方法。DH组决定DH交换中密钥生成“材料”的长度。密钥的牢
固性部分决定于DH组的强度。密钥“材料”长度越长，所生成的密钥安全度也就越高，越难被破译。DH组
的选择很重要，因为DH组只在第一阶段的SA协商中确定，第二阶段的协商不再重新选择DH组，两个阶段使
用的是同一个DH组，因此该DH组的选择将影响所有会话密钥的生成。在协商过程中，两个ISAKMP网关间
应选择同一个DH组，即密钥“材料”长度应该相等。若DH组不匹配，将协商失败。
选择DH组，在P1提议配置模式下使用以下命令：
group {1 | 2 | 5 | 14 | 15 |16 | 19 | 20 | 21 | 24 }
l
1 – 选择DH组1。密钥的长度为768比特（MODP Group）。
l
2 – 选择DH组2。密钥的长度为1024比特（MODP Group）。2为系统默认值。
l
5 – 选择DH组5。密钥的长度为1536比特（MODP Group）。
l
14 – 选择DH组14。密钥的长度为2048比特（MODP Group）。
l
15 – 选择DH组15。密钥的长度为3072比特（MODP Group）。
l
16 – 选择DH组16。密钥的长度为4096比特（MODP Group）。
l
19– 选择DH组16。密钥的长度为256比特（ECP Group）。
l
20– 选择DH组16。密钥的长度为384比特（ECP Group）。
l
21– 选择DH组16。密钥的长度为521比特（ECP Group）。

<!-- 来源页 1658 -->
l
24– 选择DH组16。密钥的长度为2048比特（MODP Group with 256-bit Prime Order
Subgroup）。
使用no group命令恢复默认DH组。
指定安全联盟的生命周期
第一阶段SA有一个默认的生命周期，如果ISAKMP SA生命期时间到，要向对方发送第一阶段SA删除消息，
通知对方第一阶段SA已经过期。之后需要重新进行SA协商。指定安全联盟的生命周期，在P1提议配置模式
下使用以下命令：
lifetime time-value
l
time-value – 指定SA第一阶段的生命周期长度，单位为秒。默认86400秒。范围是300到86400秒。
使用no lifetime命令恢复默认生命周期长度。
配置ISAKMP网关
创建一个ISAKMP网关后，用户可以指定ISAKMP网关的认证服务器、IKE协商模式、ISAKMP网关IP地址及
类型、IKE安全提议、预共享密钥、PKI信任域、本地ID、ISAKMP网关ID 、ISAKMP网关连接方式以及是否
开启ISAKMP网关的NAT穿越功能等。
创建ISAKMP网关
创建ISAKMP网关，在全局配置模式下，使用以下命令:
isakmp peer peer-name
l
peer-name – 指定ISAKMP网关的名称。
执行该命令后，CLI进入到ISAKMP网关配置模式。用户可以在该模式下对ISAKMP网关进行参数配置。
在全局配置模式下使用no isakmp peer peer-name命令删除指定的ISAKMP网关。
指定ISAKMP网关的认证服务器
此处指定的认证服务器用来对拨号端的设备进行身份认证。指定ISAKMP网关的认证服务器，在ISAKMP网关
配置模式下，使用以下命令：
aaa-server server-name
l
server-name – 指定认证服务器的名称。支持“local”、Radius、AD、LDAP和TACACS+认证服务
器。
在ISAKMP网关配置模式下使用该命令no的形式取消认证服务器的指定：

<!-- 来源页 1659 -->
no aaa-server
绑定接口到ISAKMP网关
用户可以绑定某个接口到ISAKMP网关。将接口绑定到ISAKMP网关，在ISAKMP网关配置模式下使用以下命
令：
interface interface-name
l
interface-name – 指定被绑定接口的名称。
使用no interface命令取消接口绑定。
配置IKE协商模式
IKE的协商模式有两种：主模式（main mode）和野蛮模式（aggressive mode）。IKE野蛮模式不提供
身份保护，以下情况推荐使用野蛮模式：中心设备的IP地址为固定分配的地址，而客户端设备的IP地址为动
态获取的地址。配置IKE协商模式，在ISAKMP网关配置模式下使用以下命令：
mode {main | aggressive}
l
main – 指定使用主模式，可提供ID保护功能。该模式为系统的默认模式。
l
aggressive – 指定使用野蛮模式。
使用no mode命令恢复默认协商模式。
指定对端类型
用户可以为所创建的ISAKMP网关指定对端的类型。指定对端的类型，请在ISAKMP网关配置模式下使用以下
命令：
type usergroup
在ISAKMP网关配置模式下使用该命令no的形式恢复默认配置：
no type
指定P1提议
为ISAKMP网关指定P1提议，在ISAKMP网关配置模式下使用以下命令：
isakmp-proposal p1-proposal1 [p1-proposal2] [p1-proposal3] [p1-proposal4]
l
p1-proposal1 – 指定P1提议的名称。用户最多可以为ISAKMP网关指定4个P1提议供对端选择使用。
使用no isakmp-proposal取消对P1提议的指定。

<!-- 来源页 1660 -->
配置预共享密钥
如果使用预共享密钥认证方式，用户就需要指定预共享密钥。为ISAKMP网关指定预共享密钥，在ISAKMP网
关配置模式下使用以下命令：
pre-share string
l
string – 指定预共享密钥的内容。
使用no pre-share取消对预共享密钥的指定。
开启/关闭衍生用户密钥功能
在“野蛮模式下”，中心设备默认开启“衍生用户密钥”功能。此时，在配置完中心设备的预共享密钥后，
用户需要一个一个生成不同的用户密钥作为拨号端的预共享密钥。这样的方式更安全但并不方便，因此用户
也可以关闭该功能，将中心设备的预共享密钥作为拨号端的预共享密钥。生成用户密钥配置参阅“VPN > 拨
号VPN > 拨号VPN配置> 生成拨号端用户预共享密钥”章节。
若开启该功能，拨号端的预共享密钥需要填写对应生成的用户密钥；若关闭该功能，则拨号端的预共享密钥
只需填写中心设备的预共享密钥。该功能默认为开启状态。
开启/关闭衍生用户密钥功能，在ISAKMP网关配置模式下，使用以下命令：
l
开启：derived-user-key
l
关闭：noderived-user-key
配置PKI信任域
如果使用数字证书认证方式，用户就需要指定数字证书的PKI信任域。为ISAKMP网关指定PKI信任域，在
ISAKMP网关配置模式下使用以下命令：
trust-domain string
l
string – 指定PKI信任域。
使用no trust-domain取消对PKI信任域的指定。
关于如何配置PKI信任域，请参阅《用户认证》的“PKI配置”部分。
配置本端ID
配置本端的ID，请在ISAKMP网关配置模式下使用以下命令：
local-id {fqdn string | asn1dn [string] | u-fqdnstring }

<!-- 来源页 1661 -->
l
fqdn string – 指定使用FQDN类型的ID。string为ID的具体内容。
l
asn1dn [string] – 指定使用Asn1dn类型的ID，该类型只可应用于使用证书的情况。string为ID的具
体内容。用户可以不指定ID的具体内容，在此种情况下，系统将从证书中获取ID。
l
u-fqdn string – 指定使用U-FQDN类型的ID，即电子邮件地址类型，例如
user1@hillstonenet.com。
使用no local-id命令取消对本端ID的配置。
指定连接类型
创建的ISAKMP网关可以是发起端、响应端或者既是发起端也是响应端。指定ISAKMP网关的连接类型，在
ISAKMP网关配置模式下使用以下命令：
connection-type {bidirectional | initiator-only | responder-only}
l
bidirectional – 指定该ISAKMP网关既是发起端也是响应端。该选项为系统的默认选项。
l
initiator-only – 指定该ISAKMP网关仅是发起端。
l
responder-only – 指定该ISAKMP网关仅是响应端。
由于拨号VPN只能做响应端，因此此处只能配置bidirectional或者responder-only。
使用no connection-type命令恢复默认连接方式。
开启NAT穿越功能
在IPSec或者IKE组建的VPN隧道中，若存在NAT网关设备，且NAT网关设备对VPN数据进行了NAT转换，则
必须开启IPSec或者IKE的NAT穿越功能。默认情况下，NAT穿越功能是关闭的。开启NAT穿越功能，在
ISAKMP网关配置模式下，使用以下命令：
nat-traversal
使用no nat-traversal命令关闭NAT穿越功能。
配置DPD功能
DPD（Dead Peer Detection）为安全隧道对端状态探测功能。该功能开启后，如果接收端长时间收不到
对端的报文，便触发DPD查询，主动向对端发送请求报文，对ISAKMP网关是否存在进行检测。默认情况
下，DPD功能是关闭的。
开启DPD功能，在ISAKMP网关配置模式下使用以下命令：
dpd

<!-- 来源页 1662 -->
配置DPD功能，在ISAKMP网关配置模式下使用以下命令：
dpd interval seconds retry times [on-demand | periodic]
l
interval seconds – 指定向对端发送查询请求的时间间隔。间隔范围是1到10秒。默认值是10。
l
retry times – 指定向对端发送查询请求的次数。向对端发送查询请求后，如果本端在指定的时间间隔内
收不到对端的报文，系统会在再次发送查询请求，如此反复，直到完成该参数指定的次数。在指定次数
查询完成后如果仍然收不到对端的报文，则判断对端ISAKMP网关已经死掉。查询请求的次数范围是1到
20次，默认是3次。
l
on-demand –指定DPD探测为on-demand模式。在该模式下，系统将根据设备是否收到IPSec流量来
判断是否向对端发送DPD探测报文。若设备未收到IPSec流量，不发送DPD探测报文；若设备收到IPSec
流量，需转发IPSec流量时，系统查询当前距离上一次收到对端IPSec报文的时间间隔，并与DPD探测周
期进行比较：①当前距离上一次收到对端IPSec报文的时间间隔小于DPD探测周期，说明在DPD探测周
期内收到了对端报文，表明对端ISAKMP网关存在，设备不发送DPD探测报文；②当前距离上一次收到
对端IPSec报文的时间间隔超过DPD探测周期，则表明不确定对端ISAKMP网关是否存在，设备发送DPD
探测报文对对端ISAKMP进行检测。若在一个DPD探测周期内均未收到对端报文，则判定对端ISAKMP网
关已经失效。系统将老化第一阶段和第二阶段的SA信息，重新发起新的IPSec协商。
l
periodic–指定DPD探测为periodic模式。在该模式下，系统将按照指定的时间间隔，持续向对端发送
DPD探测报文。若在一个DPD探测周期内，未收到对端响应报文，则判定对端失活。计算方式：DPD探
测周期=DPD时间间隔*DPD重试次数。默认为periodic模式。
使用no dpd命令恢复默认的DPD配置。
指定描述信息
为所配置的ISAKMP网关指定描述信息，请在ISAKMP网关配置模式下使用以下命令：
description string
l
string – ISAKMP网关的描述信息。
使用no description命令删除ISAKMP网关的描述信息。
配置P2提议
P2提议使用在SA第二阶段。对P2提议的配置包括指定协议类型、加密算法、验证算法、压缩算法和生命周
期。
创建P2提议
创建P2提议，即IPSec安全提议，请在全局配置模式下使用以下命令：

<!-- 来源页 1663 -->
ipsec proposal p2-name
l
p2-name – 指定所创建的P2提议的名称。执行该命令后，CLI进入到P2提议配置模式。对P2提议各项
参数的配置都要在该模式下进行。
使用no ipsec proposal p2-name命令删除指定的IPSec proposal。
指定协议类型
P2提议可使用的协议类型有AH以及ESP。为P2提议指定协议类型，在P2提议配置模式下使用以下命令：
protocol {esp | ah}
l
esp – 指定使用ESP协议。该协议为系统默认协议。
l
ah – 指定使用AH协议。
使用no protocol命令恢复默认协议配置。
指定加密算法
用户可以为P2提议指定至少一种最多四种加密算法。为P2提议指定加密算法，在P2提议配置模式下使用以
下命令：
encryption {3des | des | aes | aes-192 | aes-256 | null} [3des | des | aes | aes-192 | aes-256 |
null] [3des | des | aes | aes-192 | aes-256 | null]……
l
3des – 指定使用3DES加密方法。密钥长度为192比特。该方法为StoneOS系统默认方法。
l
des – 指定使用DES加密方法。密钥长度为64比特。
l
aes – 指定使用AES加密方法。密钥长度为128比特。
l
aes-192 – 指定使用192bit AES加密方法。密钥长度为192比特。
l
aes-256 – 指定使用256bit AES加密方法。密钥长度为256比特。
l
null – 不使用加密功能。
使用no encryption命令恢复默认加密算法。
指定验证算法
用户可以为P2提议指定至少一种最多三种验证算法。为P2提议指定验证算法，在P2提议配置模式下使用以
下命令：
hash {md5 | sha | sha256 | sha384 | sha512 | sm3 | null} [md5 | sha | sha256 | sha384 | sha512
| null] [md5 | sha | sha256 | sha384 | sha512 |null]

<!-- 来源页 1664 -->
l
md5 – 指定使用MD5验证算法。摘要为128比特。
l
sha – 指定使用SHA-1验证算法。摘要为160比特。该算法为StoneOS的默认算法。
l
sha256 – 指定使用SHA-256验证算法。摘要为256比特。
l
sha384 – 指定使用SHA-384验证算法。摘要为384比特。
l
sha512 –指定使用SHA-512验证算法。摘要为512比特。
l
null – 不使用验证功能。
使用no hash命令恢复默认验证算法。
配置PFS功能
PFS（Perfect Forward Security）功能决定新密钥的生成方式，而不是新密钥的生成时间。PFS保证无论
在哪一阶段，一个密钥只能使用一次，而且，生成密钥的“材料”也只能使用一次。某个“材料”在生成了
一个密钥后就被弃，绝不用来再生成任何其它密钥。这样可以确保一旦单个密钥泄密，最多只可能影响用该
密钥加密的数据，而不会危及整个通信。PFS功能是由DH算法做保障的。配置P2提议的PFS功能，在P2提
议配置模式下使用以下命令：
group {nopfs | 1 | 2 | 5 | 14 | 15 |16 | 19 | 20 | 21 | 24 | }
l
nopfs – 不使用PFS功能。该选项为系统的默认选项。
l
1 – 选择DH组1。密钥的长度为768比特（MODP Group）。
l
2 – 选择DH组2。密钥的长度为1024比特（MODP Group）。
l
5 – 选择DH组5。密钥的长度为1536比特（MODP Group）。
l
14 – 选择DH组14。密钥的长度为2048比特（MODP Group）。
l
15 – 选择DH组15。密钥的长度为3072比特（MODP Group）。
l
16 – 选择DH组16。密钥的长度为4096比特（MODP Group）。
l
19– 选择DH组16。密钥的长度为256比特（ECP Group）。
l
20– 选择DH组16。密钥的长度为384比特（ECP Group）。
l
21– 选择DH组16。密钥的长度为521比特（ECP Group）。
l
24– 选择DH组16。密钥的长度为2048比特（MODP Group with 256-bit Prime Order
Subgroup）。
使用no group命令恢复默配置。

<!-- 来源页 1665 -->
指定生命周期
Hillstone设备有两种衡量生命周期的方法，分别是按时间和按流量。当SA的流量或者时间达到特定值时，
SA就会过期，需要重新进行协商。指定P2提议的生命周期，在P2提议配置模式，使用以下命令：
lifetime seconds
l
seconds – 指定时间类型生命周期的时间长度，单位为秒。默认值是28800秒。
lifesize kilobytes
l
kilobytes – 指定流量类型周期的流量值，单位为字节。默认值是0，意义为没有周期流量限制。
使用以上两个命令no的形式恢复默认配置。即
no lifetime
no lifesize
配置隧道
通过IKE配置IPSec隧道，用户需要配置的选项有指定协议类型、ISAKMP网关、IKE安全提议、ID号、是否
分片以及防重放等。
创建IKE隧道
创建IKE隧道，在全局配置模式下，使用以下命令：
tunnel ipsec tunnel-name auto
l
tunnel-name - 指定所创建的IKE隧道的名称。
执行该命令后，CLI进入到IKE隧道配置模式。对IKE隧道的所有参数配置都需要在该模式下进行。
在全局配置模式下使用no tunnel ipsec tunnel-name auto删除指定的IKE隧道。
指定IPSec协议的操作模式
为IKE隧道指定操作模式（隧道模式），在IKE隧道配置模式下使用以下命令：
mode tunnel
使用no mode命令恢复默认模式。
指定ISAKMP网关
为IKE隧道指定ISAKMP网关，请在IKE隧道配置模式下使用以下命令：

<!-- 来源页 1666 -->
isakmp-peer peer-name
• peer-name – 指定ISAKMP网关的名称。
使用no isakmp-peer取消对ISAKMP网关的指定。
指定P2提议
为IKE隧道指定P2提议，请在IKE隧道配置模式下使用以下命令：
ipsec-proposal p2-name
l
p2-name – 指定P2提议的名称。
使用no ipsec-proposal取消对P2提议的指定。
指定第二阶段ID
为IKE IPSec隧道指定第二阶段ID，请在IKE隧道配置模式下使用以下命令：
id {auto | local ip-address/mask remote ip-address/mask service service-name}
l
auto – 自动指定第二阶段ID。此参数为系统默认配置。
l
local ip-address/mask – 指定本端第二阶段local ID。
l
remote ip-address/mask – 指定本端第二阶段remote ID。
l
service service-name – 指定服务名称。
用户可配置最多256个第二阶段ID用于协商建立多个IKE隧道。当中心设备端配置了多个第二阶段ID时，中心
设备能够与拨号端协商并创建多个IPSec SA，即创建多个IKE隧道。配置了自动生成路由功能后（参见配置
自动生成路由功能），每创建一个IPSec SA，中心设备会将目的地址为拨号端的local ID、下一跳为拨号端
网关接口（出接口）的IP地址的路由条目添加到自己的路由表。删除一个IPSec SA后，相应的路由条目也会
被删除。
使用no id {auto | local ip-address/mask remote ip-address/mask service service-name}命令
恢复系统默认配置。
配置ID为包含关系时生成IPSec SA
当中心设备配置的第二阶段的remote ID包含拨号端的第二阶段的local ID时，配置该功能后，中心设备和
远程拨号端之间可成功协商生成IPSec SA。配置ID为包含关系时生成IPSec SA，请在IKE隧道配置模式下使
用以下命令：
dialup-control-id
使用no dialup-control-id恢复默认配置。

<!-- 来源页 1667 -->
配置IPSec分流限流功能
中心设备可以和一个远程拨号端协商生成多个IPSec SA，并在IKE隧道出接口对封装的数据包进行限流，在
IKE隧道入接口对封装的数据包进行分流。如果数据包的源IP地址、目的IP地址和服务类型匹配某个第二阶段
ID的配置，那么该数据包会被中心设备接收并继续处理，否则该数据包会被丢弃。配置IPSec分流限流功
能，请在IKE隧道配置模式下使用以下命令：
check-id
使用no check-id恢复默认配置。
配置自动连接功能
设备提供两种触发建立SA的方式：自动方式和流量触发方式。
l
自动方式：设备每60秒检查一次SA的状态，如果SA未建立则自动发起协商请求；
l
流量触发方式：当有数据流量需要通过隧道进行传输时，该隧道才发起协商请求。
默认情况下，系统使用流量触发方式。使用自动方式，在IKE隧道配置模式下使用以下命令：
auto-connect
使用no auto-connect命令恢复系统的默认设置。
注意: 自动连接功能仅在对端IP地址为静态类型且本端可以作为发起端时有效。
配置分片功能
用户可以指定是否允许转发设备将包进行分片处理。为IKE隧道配置分片功能，请在IKE隧道配置模式下使用
以下命令：
df-bit {copy | clear | set}
l
copy – 直接从发包端拷贝IP包的DF选项。该选项为系统默认选项。
l
clear – 允许转发设备对包做分片处理。
l
set – 不允许转发设备对包做分片处理。
使用no df-bit恢复系统的默认设置。

<!-- 来源页 1668 -->
配置防重放功能
防重放（anti-replay）指防止恶意用户通过重复发送捕获到的数据包所进行的攻击，即接收方会拒绝旧的
或重复的数据包。默认情况下，防重放功能是关闭的。为IKE IPSec隧道配置防重放功能，请在IKE IPSec隧
道配置模式下使用以下命令：
anti-replay {32 | 64 | 128 | 256 | 512}
l
32 – 指定防重放的窗口为32。
l
64 – 指定防重放的窗口为64。
l
128 – 指定防重放的窗口为128。
l
256 – 指定防重放的窗口为256。
l
512 – 指定防重放的窗口为512。
在网络状况较差时，例如存在严重乱序现象等，请选择较大的窗口。
使用no anti-replay命令关闭防重放功能。
设置Commit位
用户可以配置使响应方设置Commit位，从而防止出现丢包和时间差现象。但是，设置Commit位可能导致
响应速度变慢。设置Commit位，请在IKE IPSec隧道配置模式下使用以下命令：
响应方设置Commit位：responder-set-commit
响应方不设置Commit位：no responder-set-commit
配置空闲时间
空闲时间指隧道在无流量状态下能够保持连接状态的最长时间，超出空闲时间后，SA将会被清除。配置空闲
时间，在IKE IPSec隧道配置模式下，使用以下命令：
idle-time time-value
l
time-value – 指定空闲时间，单位为秒。取值范围是120到3000秒。
在IKE IPSec隧道配置模式下使用该命令no的形式关闭空闲时间功能：
no idle-time
指定描述信息
为所配置的IKE隧道指定描述信息，请在IKE IPSec隧道配置模式下使用以下命令：

<!-- 来源页 1669 -->
description string
l
string – IKE隧道的描述信息。
使用no description命令删除IKE隧道的描述信息。
配置路由优先级
开始之前：
l
配置路由优先级前，需要先开启自动生成路由功能，否则路由优先级的配置不会生效。自动生成路由功
能参阅“VPN > 拨号VPN > 拨号VPN配置> 配置自动生成路由功能”章节。
注意:
l
该功能只对IKE1协议标准的VPN生效。
l
若本端为响应方，则路由优先级优先由发起方决定。
l
发起方配置路由优先级后，若响应方不支持路由优先级功能，会导致VPN连接失败。（仅
StoneOS R10P9及以上版本、R11P3及以上版本、R12及以上版本、R10P9M5及以上版本、
R11F3及以上版本支持路由优先级功能。）
用户可以指定路由的优先级，更灵活地管理VPN。例如，对于到达相同目的地址的VPN，如果需要设置VPN
主备，则可以指定不同的路由优先级来实现；如果需要实现负载均衡，则可以指定相同的路由优先级。指定
的路由优先级数字越大，则优先级越低，取值范围为1-255。若不指定路由优先级，则默认为1。
配置路由优先级，在IKE隧道配置模式下，使用以下命令：
route-prioritynumber
number - 指定路由的优先级，取值范围为1-255，默认为1。
在IKE隧道配置模式下，使用noroute-priority命令恢复默认的路由优先级。
配置自动生成路由功能
对于基于路由的拨号VPN或者PnPVPN，其中心设备通常会连接多个分支机构（拨号VPN的拨号端或者
PnPVPN的客户端），并且这些分支机构的IP地址会经常发生变动，因此，当中心设备访问分支机构时，手
工配置路由会给管理员带来很多不便。Hillstone设备支持自动生成路由功能，该功能允许设备自动添加从
中心设备到分支机构的路由条目，从而避免了手工配置路由所带来的问题。
默认情况下，设备的自动生成路由功能是关闭的。开启此功能，请在ISAKMP配置模式下，使用以下命令：
generate-route

<!-- 来源页 1670 -->
对于拨号VPN，执行此命令后，自动生成路由条目的目的地址为拨号端的第二阶段local ID，下一跳IP地址
为对端的IP地址。关于如何配置第二阶段ID，请参阅“指定第二阶段ID”。
对于PnPVPN，执行此命令后，自动生成路由条目的目的地址为客户端DHCP地址池的起始IP地址和客户端
DHCP地址池的网络掩码的逻辑“与”运算结果（dhcp-pool-addr-start & dhcp-pool-netmask）。下
一跳IP地址为对端的IP地址。关于如何配置客户端DHCP地址池及其网络掩码，请参阅“通过CLI配置
PnPVPN服务器端”。
使用no generate-route命令关闭自动生成路由功能。
注意:
l
对于拨号VPN，当拨号端的第二阶段local ID指定为0.0.0.0/0时，强烈建议用户在中心设备
上不要开启自动生成路由功能。
l
当分支机构访问中心设备时，用户可以在中心设备上使用no reverse-route命令取消隧道接
口的逆向路由功能，使所有反向数据原路返回。
配置拨号端用户信息
中心设备需要创建拨号端的用户信息，包括用户帐号以及生成拨号端用户预共享密钥。
创建拨号端用户帐号
在全局配置模式下，使用以下命令：
user user-name aaa-server local
l
user-name – 指定用户名称。
执行该命令后，系统进入用户配置模式，在该模式下，指定用户的IKE ID，命令如下：
ike-id {fqdn string | asn1dn string}
l
fqdn string – 指定使用FQDN类型的IKE ID。string为ID的具体内容。
l
asn1dn string – 指定使用Asn1dn类型的ID，该类型只可应用于使用证书的情况。string为ID的具体
内容。
在用户配置模式下使用该命令no的形式取消IKE ID的配置：
no ike-id
生成拨号端用户预共享密钥
根据拨号端用户的用户名以及IKE ID，中心设备可生成相应的预共享密钥。在执行模式下，使用以下命令：

<!-- 来源页 1671 -->
exec generate-user-key rootkey pre-share-key userid string
l
pre-share-key – 指定设备端的预共享密钥。
l
string – 指定用户名称相对应的IKE ID。
配置拨号端用户IKE ID
对于拨号端用户，需要为其指定IKE ID。指定IKE ID，在用户配置模式下，使用以下命令：
ike_id {fqdnstring | asn1dnstring | key-idstring }
l
fqdnstring – 指定使用FQDN（Fully Qualified Domain Name）类型的IKE ID。string为ID的具体
内容。
l
asn1dnstring – 指定使用Asn1dn类型的ID，该类型只可应用于使用证书的情况。string为ID的具体
内容。
l
key-idstring – 指定使用Key ID类型的ID。该类型仅应用于XAUTH功能。
在用户配置模式下使用该命令no的形式取消IKE ID的配置：
no ike_id
拨号端配置
拨号端需要配置与中心设备相对应的P1提议、P2提议、ISAKMP网关以及隧道。配置过程与中心设备的配置
基本相同。
提示: 在配置拨号端的ISAKMP网关时，如果中心设备使用的是预共享密钥并且开启了衍生用户密
钥功能，则拨号端指定的预共享密钥为中心设备生成的相应的用户密钥；如果未开启衍生用户密钥
功能，则拨号端指定的预共享密钥为中心设备的预共享密钥。
例：拨号VPN配置举例
该节介绍一个拨号VPN的实例。
组网需求
两个拨号端设备（User1和User2）与中心设备（2.2.2.1/24）组成拨号VPN，实现与拨号端设备相连的PC
（PC1和PC2）能够安全访问被中心设备保护的服务器（Server1）资源。组网图参见下图：

<!-- 来源页 1672 -->
中心设备配置
第一步：接口配置：
hostname(config)# zone vpnzone
hostname(config-zone-vpnzone)# exit
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/0)# zone vpnzone
hostname(config-if-eth0/0)# ip address 2.2.2.1/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/5
hostname(config-if-eth0/5)# zone trust
hostname(config-if-eth0/5)# ip address 192.168.1.1/24
hostname(config-if-eth0/5)# exit
第二步：配置拨号端用户帐号及预共享密钥信息：
hostname(config)# aaa-server local
hostname(config-aaa-server)# user user1
hostname(config-user)# ike_id fqdn hillstone1
hostname(config-user)# exit

<!-- 来源页 1673 -->
hostname(config-aaa-server)# user user2
hostname(config-user)# ike_id fqdn hillstone2
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)# exit
hostname# exec generate-user-key rootkey 123456 userid hillstone1
userkey: 3zPNDY6MmI8Wejk5fa3jhPU39p8=
hostname# exec generate-user-key rootkey 123456 userid hillstone2
userkey: tAFW+48HcAr15+NcISm6TZJZzGU=
hostname# configure
hostname(config)#
第三步：配置IKE VPN：
hostname(config)# isakmp proposal p1
hostname(config-isakmp-proposal)# exit
hostname(config)# ipsec proposal p2
hostname(config-ipsec-proposal)# exit
hostname(config)# isakmp peer test
hostname(config-isakmp-peer)# aaa-server local
hostname(config-isakmp-peer)# interface ethernet0/0
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# mode aggressive
hostname(config-isakmp-peer)# pre-share 123456
hostname(config-isakmp-peer)# type usergroup
hostname(config-isakmp-peer)# exit
hostname(config)# tunnel ipsec vpn auto
hostname(config-tunnel-ipsec-auto)# isakmp-peer test
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# id local 192.168.1.2/24 remote 0.0.0.0/0
service any

<!-- 来源页 1674 -->
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)#
第四步：配置策略：
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone vpnzone
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action tunnel vpn
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone vpnzone
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action fromtunnel vpn
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
拨号端1配置
第一步：接口配置：
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/0)# zone untrust
hostname(config-if-eth0/0)# ip address 3.3.3.2/24
hostname(config-if-eth0/0)# exit

<!-- 来源页 1675 -->
hostname(config)# interface ethernet0/4
hostname(config-if-eth0/5)# zone trust
hostname(config-if-eth0/5)# ip address 192.168.2.1/24
hostname(config-if-eth0/5)# exit
hostname(config)#
第二步：配置IKE VPN：
hostname(config)# isakmp proposal p1
hostname(config-isakmp-proposal)# exit
hostname(config)# ipsec proposal p2
hostname(config-ipsec-proposal)# exit
hostname(config)# isakmp peer test
hostname(config-isakmp-peer)# interface ethernet0/1
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# mode aggressive
hostname(config-isakmp-peer)# peer 2.2.2.1
hostname(config-isakmp-peer)# pre-share 3zPNDY6MmI8Wejk5fa3jhPU39p8=
hostname(config-isakmp-peer)# local-id fqdn hillstone1
hostname(config-isakmp-peer)# exit
hostname(config)# tunnel ipsec vpn auto
hostname(config-tunnel-ipsec-auto)# isakmp-peer test
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# id local 192.168.2.2/24 remote 192.168.1.2/24
service any
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)#
第三步：配置策略：
hostname(config)# policy-global
hostname(config-policy)# rule

<!-- 来源页 1676 -->
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action tunnel vpn
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action fromtunnel vpn
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
拨号端2配置
第一步：接口配置：
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/0)# zone untrust
hostname(config-if-eth0/0)# ip address 4.4.4.2/24
hostname(config-if-eth0/0)# exit
hostname(config)# interface ethernet0/4
hostname(config-if-eth0/5)# zone trust
hostname(config-if-eth0/5)# ip address 192.168.3.1/24
hostname(config-if-eth0/5)# exit
hostname(config)#

<!-- 来源页 1677 -->
第二步：配置IKE VPN：
hostname(config)# isakmp proposal p1
hostname(config-isakmp-proposal)# exit
hostname(config)# ipsec proposal p2
hostname(config-ipsec-proposal)#
hostname(config)# isakmp peer test
hostname(config-isakmp-peer)# interface ethernet0/1
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# mode aggressive
hostname(config-isakmp-peer)# peer 2.2.2.1
hostname(config-isakmp-peer)# pre-share tAFW+48HcAr15+NcISm6TZJZzGU=
hostname(config-isakmp-peer)#
hostname(config-isakmp-peer)# exit
hostname(config)# tunnel ipsec vpn auto
hostname(config-tunnel-ipsec-auto)# isakmp-peer test
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# id local 192.168.3.2/24 remote 192.168.1.2/24
service any
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)#
第三步：配置策略：
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone untrust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action tunnel vpn

<!-- 来源页 1678 -->
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone untrust
hostname(config-policy-rule)# dst-zonetrust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action fromtunnel vpn
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#

<!-- 来源页 1679 -->
PnPVPN
IPSec VPN配置复杂，维护成本高，对网管人员技术要求高，针对该问题，为企业用户提供了一种简单易用
的VPN技术——PnPVPN，即即插即用VPN。PnPVPN由两部分组成，分别是PnPVPN Server和PnPVPN
Client，各自功能描述如下：
l PnPVPN Server：通常放置于企业总部，由总部IT工程师负责维护，客户端的大多数配置由服务器下发。
PnPVPN Server通常由设备充当，一台设备可充当多个PnPVPN Server。
l PnPVPN Client：通常放置于企业分支机构（如办事处），可由总部工程师远程维护，只需要做简单配置（如客
户端ID、密码和服务器端IP地址），和Server端协商成功后即可从Server端获取配置信息（如DNS、WINS、
DHCP地址池等）。
提示: 设备既可以充当PnPVPN Server，又可以充当PnPVPN Client。当充当Server时，不同平
台支持的VPN实例数和每个实例所支持的客户端数有所不同。
PnPVPN工作流程
PnPVPN的工作流程如下：
1. 客户端发起连接请求，并传送自己的ID以及密码到服务器端。
2. 服务器端收到请求后，验证客户端传送的ID和密码，验证通过即下发预配置的DHCP地址池、DHCP掩码、DHCP
网关、WINS、DNS和隧道路由等信息到客户端。
3. 客户端把收到的信息下发到相应的功能模块。
4. 客户端PC自动获取IP地址、IP地址掩码和网关地址等网络参数，并正常接入VPN网络。
PnPVPN链路冗余
PnPVPN服务器端支持一个PnPVPN客户端拨入两条VPN链路并自动生成到客户端的路由、为客户端配置
VPN监控。服务器端需要配置两个ISAKMP网关和两个隧道接口，两个VPN隧道分别引用不同的ISAKMP网
关，并绑定到两个不同的隧道接口。
客户端支持通过VPN双链路拨入服务器端、VPN监控和冗余选路。PnP客户端的两个VPN隧道在和服务器端
协商时，会根据服务器端的隧道路由配置分别生成不同优先级的路由，优先级高的隧道作为主链路，优先级
低的隧道作为备份链路，从而实现冗余选路。主VPN隧道会首先处于active状态，如果客户端监测到该主隧
道中断，客户端设备会通过备份隧道重新传输数据；当监测到主隧道恢复正常后，客户端设备会重新启用主
隧道传输数据。

<!-- 来源页 1680 -->
相关链接：
l 配置PnPVPN
配置PnPVPN
PnPVPN的配置包含：
l 配置PnPVPN服务器端
l 配置PnPVPN客户端
配置PnPVPN服务器端
PnPVPN配置包括服务器端配置和客户端配置。服务器端可通过CLI和WebUI两种方式进行配置。
l 通过CLI配置PnPVPN服务器端
l 通过WebUI配置PnPVPN服务器端
通过CLI配置PnPVPN服务器端
PnPVPN服务器端配置基于IPSec VPN命令行，此外，还有特有的命令行，本节仅介绍PnPVPN特有命令
行。使用以下特有命令并不能完成服务器端的配置，完整配置请参见PnPVPN配置举例部分。
配置用户网络参数
客户端与服务器端VPN协商成功后，服务器端需要下发给用户端网络参数信息，包括DNS服务器地址、
WINS服务器地址、隧道路由、DHCP地址池及其掩码和网关地址。这些网络参数需要在相应的用户配置模式
下进行配置。DNS、WINS和隧道路由也可以在IKE隧道配置模式下配置，但用户配置模式下的配置优先级高
于IKE隧道配置模式，即当用户配置模式和IKE隧道配置模式同时配置了DNS、WINS或隧道路由，服务器使
用用户配置模式下的配置下发给客户端。
进入本地用户配置模式，使用以下命令：
aaa-server aaa-server-name type local （进入本地AAA认证服务器配置模式）
user user-name
l
user-name – 指定用户名称。
通过以下命令完成用户网络参数的配置，其中DHCP地址池、DHCP网络掩码和网关为必配网络参数。
dns A.B.C.D [A.B.C.D] [A.B.C.D] [A.B.C.D]

<!-- 来源页 1681 -->
l
A.B.C.D – 配置DNS服务器的IP地址，可同时指定1个主DNS服务器和最多3个备份服务器。使用no
dns命令取消配置。
wins A.B.C.D [A.B.C.D]
l
A.B.C.D – 配置WINS服务器的IP地址，可同时指定一个主WINS服务器和一个备份WINS服务器。使用
no wins命令取消配置。
split-tunnel-route A.B.C.D/Mask
l
A.B.C.D/Mask – 配置隧道路由。A.B.C.D为IP地址前缀，Mask为子网掩码的位数。最多可设置128条
隧道路由。使用no split-tunnel-route A.B.C.D/Mask命令取消配置。
dhcp-pool-address start-ipaddr end-ipaddr
l
start-ipaddr end-ipaddr – 配置DHCP地址池的起始IP地址和终止IP地址。使用no dhcp-pooladdress命令取消配置。
dhcp-pool-netmask A.B.C.D
l
A.B.C.D – 配置DHCP地址池的网络掩码。使用no dhcp-pool-netmask命令取消配置。
dhcp-pool-gateway A.B.C.D
l
A.B.C.D – 配置DHCP地址池的网关地址。该地址用来作为PnPVPN客户端内网接口的IP地址，并被设置
为PC的网关地址，PC的IP地址由以上设置的DHCP地址池的网段以及网络掩码确定，所以网关地址应该
和DHCP地址池在同一个网段。使用no dhcp-pool-gateway命令取消配置。
配置隧道网络参数
当所有或大部分客户端使用统一的DNS、WINS或隧道路由时，可以在IKE隧道配置模式下配置DNS、WINS
或隧道路由以减少用户配置模式下的工作量。使用以下命令进入IKE隧道配置模式：
tunnel ipsec tunnel-name auto
l
tunnel-name – 指定IKE隧道名称。
通过以下命令完成DNS、WINS或隧道路由的配置：
dns A.B.C.D [A.B.C.D] [A.B.C.D] [A.B.C.D]
l
A.B.C.D – 配置DNS服务器的IP地址，可同时指定1个主DNS服务器和最多3个备份服务器。使用no
dns命令取消配置。

<!-- 来源页 1682 -->
wins A.B.C.D [A.B.C.D]
l
A.B.C.D – 配置WINS服务器的IP地址，可同时指定一个主WINS服务器和一个备份WINS服务器。使用
no wins命令取消配置。
split-tunnel-route A.B.C.D/Mask
l
A.B.C.D/Mask – 配置隧道路由。A.B.C.D为IP地址前缀，Mask为子网掩码的位数。最多可设置128条
隧道路由。使用no split-tunnel-route A.B.C.D/Mask命令取消配置。
配置ISAKMP网关对端通配符
当PnPVPN Server通过Radius服务器进行认证时，需要配置ISAKMP网关对端的通配符。Hillstone设备在
收到客户端的VPN连接建立请求时，根据客户端的用户名与ISAKMP网关对端通配符的匹配结果，确定与客
户端接入的PnPVPN Server（一台Hillstone设备可同时充当多个PnPVPN的Server），进而确定对用户进
行认证的Radius服务器。
在ISAKMP网关配置模式下使用以下命令配置ISAKMP网关对端通配符：
peer-id fqdn wildcard string
l
fqdn – 指定使用FQDN类型的通配符。
l
wildcard string – 指定通配符ID，通常为客户端的域名。如abc.com。
使用no peer-id命令取消通配符配置。
配置PnPVPN客户端的隧道接口
为了使分支机构的多个子网网段可以访问服务器端，StoneOS支持在PnPVPN服务器端为客户端的隧道接口
指定IP地址，并启用SNAT规则。如果PnPVPN客户端是由Hillstone SR系列安全路由器充当，那么需要SR
系列产品的版本支持该功能。
注意: 该功能工作时，PnPVPN服务器端将无法访问客户端。
进入本地用户配置模式
进入本地用户配置模式，使用以下命令：
aaa-server aaa-server-name type local （进入本地AAA认证服务器配置模式）
user user-name
l
user-name – 指定用户名称。
配置PnPVPN客户端的隧道接口

<!-- 来源页 1683 -->
在本地用户配置模式下，使用以下命令配置PnPVPN客户端的隧道接口：
tunnel-ip-address A.B.C.D [snat]
l
A.B.C.D – 指定客户端隧道接口的IP地址，该地址不能与客户端已存在的IP地址冲突。
l
snat – 启用SNAT规则。默认情况下，系统不开启隧道接口的SNAT规则。
在本地用户配置模式下，使用该命令no的形式取消配置PnPVPN客户端的隧道接口：
no tunnel-ip-address
通过WebUI配置服务器端
通过WebUI配置服务器端，用户需要在以下模块进行配置：
l 用户配置
l IKE VPN配置
l 隧道接口配置
l 路由配置
l 策略配置
注意: 注意：PnPVPN支持两种认证服务器：Local和Radius。以下配置列出使用本地服务器进行
认证的情况，关于Radius服务器认证配置请参阅相应的Radius服务器使用手册。
用户配置
请按照以下步骤进行用户配置：
1. 选择“对象> 用户> 本地用户”。
2. 在“本地服务器”下拉菜单中选择需要的本地服务器名称，然后点击对话框左上角的“新建”下拉菜单，选择
“用户”，打开<用户配置>页面。
3. 在“名称”文本框中输入用户名称。
4. 设置用户密码。在“密码”文本框输入密码，并在“重新输入密码”文本框再次输入密码进行确认。
5. 配置用户的手机号码。在“手机号码”文本框中输入手机号码。如果启用了短信认证功能，短信认证码将发送到
用户设置的电话号码。
6. 配置用户的邮箱。在“邮箱”文本框中输入邮箱地址。如果启用了邮件认证功能，邮件认证码将发送到用户设置
的邮箱。

<!-- 来源页 1684 -->
7. 在“描述”文本框中输入用户描述信息。
8. 点击“组”文本框，在弹出的“用户组”页面中选择用户所归属的用户组。
9. 选择账户到期日。选中“启用”复选框，开启用户的有效期限制功能，并选择日期和时间。
10. 点击“VPN配置”右侧的下拉菜单，展开VPN配置项。
11. 在“拨号VPN”下，指定用户IKE ID。从“IKEID”部分选中“FQDN”单选按钮，并在“IKEID”文本框中输入
ID。PnPVPN Client将使用该ID进行登录认证。
12. 填写“PnPVPN”下面的文本框，包括DHCP相关选项、DNS、WINS以及隧道路由。当该用户不使用隧道下已经
配置的DNS、WINS和隧道路由选项或者新建隧道页面未配置这些选项时，这些选项必须在本页面完成配置。
13. 根据需要对该页面的其它选项进行配置。
14. 配置完成，点击“确定”按钮保存所做配置。
IKE VPN配置
IKE VPN配置包括P1提议配置、P2提议配置、对端配置以及隧道配置。
按照以下步骤配置P1提议：
1. 从页面左侧导航树选择并点击“配置> 网络> IPSec VPN”，进入IPSec VPN页面。点击『P1提议』标签，进入
P1提议标签页。
2. 点击P1提议列表左上方的『新建』按钮，弹出<阶段1提议配置>对话框。
3. 指定P1提议名称。在<提议名称>文本框输入P1提议名称。
4. 指定认证方式。选中“pre-share”单选按钮。
5. 指定DH组。选中“Group2”单选按钮。
6. 根据需要对该页面的其它选项进行配置或保持其默认值。
7. 配置完成，点击『确定』按钮保存所做配置。
按照以下步骤配置P2提议：
1. 从页面左侧导航树选择并点击“配置h网络hIPSec VPN”，进入IPSec VPN页面。点击『P2提议』标签，进入P2
提议标签页。
2. 点击P2提议列表左上方的『新建』按钮，弹出<阶段2提议配置>对话框。
3. 指定P2提议名称。在<提议名称>文本框输入P2提议名称。
4. 选择使用的协议、验证算法、加密算法和PFS组。

<!-- 来源页 1685 -->
5. 根据需要对该页面的其它选项进行配置或保持其默认值。
6. 配置完成，点击『确定』按钮保存所做配置。
按照以下步骤配置对端：
1. 从页面左侧导航树选择并点击“配置h网络hIPSec VPN”，进入IPSec VPN页面。点击『VPN对端列表』标签，
进入VPN对端列表标签页。
2. 点击列表左上方的『新建』按钮，弹出<VPN对端配置>对话框。
3. 指定对端名称。在<对端名称>文本框输入对端名称。
4. 指定外网接口。从<接口>下拉菜单中选择需要的接口。
5. 指定模式和类型。选中<野蛮模式>和<用户组>单选按钮。
6. 指定认证服务器。从<AAA服务器>下拉菜单选择使用的认证服务器。
7. 指定P1提议。从<提议1>下拉菜单中选择需要的P1提议。
8. 指定预共享密钥。在<预共享密钥>文本框输入相应的预共享密钥。
9. 根据需要对该页面的其它选项进行配置或保持其默认值。
10. 点击『生成』按钮，弹出<生成用户密钥>对话框。输入用户ID和预共享密钥，点击『生成』按钮，生成的密钥将
显示在<创建结果>文本框中。PnPVPN Client将使用该密钥作为密码进行登录认证。点击『关闭』按钮返回对端
配置页面。
11. 点击『确定』按钮保存所做配置。
注意: 当选用Radius服务器进行认证时，必须配置对端通配符。
按照以下步骤配置隧道：
1. 从页面左侧导航树选择并点击“配置h网络hIPSec VPN”，进入IPSec VPN页面。点击『IPSec VPN』标签，进
入IPSec VPN标签页。
2. 点击IKE VPN列表左上方的『新建』按钮，弹出<IKE VPN配置>对话框。
3. 在<步骤1：对端>部分，点击<对端名称>的『导入』按钮，然后从下拉菜单中选择需要的对端。用户也可以直接
在该页面新建对端（ISAKMP网关）。
4. 点击<步骤2：隧道>，展开隧道具体配置选项。
5. 指定隧道名称。在<名称>文本框输入隧道名称。
6. 指定模式。选中<tunnel>单选按钮。

<!-- 来源页 1686 -->
7. 指定提议。从<p2提议>下拉菜单选择需要的提议。
8. 点击『高级配置』标签进行高级选项配置。
9. 配置DNS和WINS服务器。通过该隧道接入的用户将使用此处指定的DNS和WINS。
10. 设置隧道路由。
11. 根据需要对该页面的其它选项进行配置或保持其默认值。
12. 点击『确定』按钮保存所做配置。
dns A.B.C.D [A.B.C.D] [A.B.C.D] [A.B.C.D] A.B.C.D – 配置DNS服务器的IP地址，可同时指定1个主DNS服务器
和最多3个备份服务器。使用no dns命令取消配置。wins A.B.C.D [A.B.C.D] A.B.C.D – 配置WINS服务器的IP地
址，可同时指定一个主WINS服务器和一个备份WINS服务器。使用no wins命令取消配置。split-tunnel-route
A.B.C.D/Mask A.B.C.D/Mask – 配置隧道路由。A.B.C.D为IP地址前缀，Mask为子网掩码的位数。最多可设置
128条隧道路由。使用no split-tunnel-route A.B.C.D/Mask命令取消配置。
注意: 用户配置部分指定的DNS、WINS和隧道路由优先级高于此处配置。
隧道接口配置
请按照以下步骤进行隧道接口配置：
1. 点击“配置> 网络> 网络连接”，进入网络连接页面。
2. 点击接口列表左上方的『新建』下拉菜单，选择并点击<隧道接口>，弹出<接口配置>对话框。
3. 指定隧道接口名称。在<名称>部分的<tunnel>文本框输入编号。
4. 指定隧道接口所属安全域类型。在<安全域类型>部分选中<三层安全域>单选按钮。
5. 指定隧道接口所属安全域。从<安全域>下拉菜单选择需要的安全域。
6. 绑定隧道。在<隧道绑定配置>部分选中<IPSec VPN>单选按钮，然后从<VPN名称>下拉菜单选择VPN隧道名称。
无需配置网关地址。
7. 点击『确定』按钮保存所做配置。
路由配置
为实现服务器端网络的主机能够访问客户端网络，用户需要添加静态路由条目。按照以下步骤配置路由：
1. 访问“配置h网络h路由”，进入目的路由页面。
2. 点击目的路由列表左上方的『新建』按钮，弹出<目的路由配置>对话框。

<!-- 来源页 1687 -->
3. 配置目的IP。在<目的地>和<子网掩码>文本框中分别输入客户端网络内网IP前缀和子网掩码。
4. 配置下一跳。在<下一跳>部分选中<接口>单选按钮，然后从<接口>下拉菜单中选择VPN隧道绑定的隧道接口，并
在<网关>文本框中填写设备端外网接口的IP地址。
5. 根据需要对该页面的其它选项进行配置或保持其默认值。
6. 点击『确定』按钮保存所做配置。
策略配置
根据网络拓扑情况，配置相应的访问策略（点击“配置> 安全>策略”，进入策略页面）。
配置PnPVPN客户端
PnPVPN客户端仅支持WebUI方式配置。按照以下步骤通过WebUI配置PnPVPN客户端：
1. 从页面左侧导航树选择并点击“配置h网络hIPSec VPN”，进入IPSec VPN页面。
2. 从页面右侧辅助栏的<任务>区选择『PnPVPN客户端』链接，弹出<PnPVPN配置>对话框。
3. 依次填写或者选择各项。配置选项具体描述如下：
l 服务器地址1：指定服务器端IP地址。该选项为必选项。
l 服务器地址2：指定服务器端IP地址。服务器地址1和服务器地址2可以相同，也可以不同。该选项为可选
项。
l ID：指定服务器端分配给用户端的IKE ID。
l 密码：指定服务器端分配给用户端的密码。
l 重新输入密码：再次输入密码以确认。
l 自动保存：选中<启用>复选框，系统自动保存连接建立后PnPVPN服务器端下发给客户端的DHCP和WINS
信息。
l VPN出接口1：VPN出接口1是接入Internet的接口，从下拉菜单中选择需要的接口名称。该选项为必选
项。
l VPN出接口2：VPN出接口2是接入Internet的接口，从下拉菜单中选择需要的接口名称。出接口1和出接
口2可以相同，也可以不同。该选项为可选项。
l VPN入接口：VPN入接口是内部PC或者各种应用服务器在PnPVPN客户端上的接入口。选中所需接口类型
的单选按钮。当选择<接口>时需要在后面的<接口>下拉菜单中选择接口名称；当客户端有多个内网口连接
PnPVPN的时候，选择<bgroup接口>，并需要在后面的<bgroup接口>部分指定该bgroup接口包含的可

<!-- 来源页 1688 -->
用接口成员。指定接口成员，在左侧的<可用成员>列表中选中需要指定的接口名称，点击右箭头按钮将其
添加到右侧<服务成员>列表中；删除已指定的接口，在右侧的<服务成员>列表中选中需要删除的接口名
称，点击左箭头按钮将其删除。
4. 配置完成，点击『确定』按钮保存所做配置并返回IPSec VPN页面。
例：PnPVPN配置举例
该节介绍PnPVPN配置举例。
组网需求
某公司总部位于北京，在上海和广州设有办事处，三地均可成功接入Internet。由于业务需求，需要组建
VPN网络，达到以下目的：
l 广州和上海办事处的员工通过VPN访问总部数据库；
l 公司员工（包括总部和两办事处三地）之间可以通过VPN共享资源。
通过配置PnPVPN可实现以上需求，并且简单实用。组网图如图所示。配置方式如下：
l 公司总部选用一台Hillstone设备作为PnPVPN Server，采用本地认证方式；
l 上海和广州办事处各部署一台Hillstone设备，作为PnPVPN Client，接入总部VPN网络。

<!-- 来源页 1689 -->
l 通过策略和路由配置实现允许公司员工之间的资源共享。
根据上图，具体网络环境描述如下：
l 总部局域网网段为192.168.1.0/24，通过接口ethernet0/0接入网络，属于trust安全域；
l 总部服务器群网段为192.168.200.0/24，通过接口ethernet0/2接入网络，属于trust安全域；
l 总部Hillstone设备通过接口ethernet0/1（IP地址为202.106.6.208）接入Internet，属于untrust安全域。
l 上海办事处设备接入Internet的接口IP地址为61.170.6.208，广州办事处设备接入Internet的IP地址为
59.42.6.208。
l PnPVPN Server将分配192.168.2.0/24网段到上海办事处，192.168.3.0/24网段到广州办事处。

<!-- 来源页 1690 -->
配置步骤
配置步骤分服务器端配置和客户端配置。
服务器端配置
第一步：配置本地AAA认证服务器：
hostname(config)# aaa-server test type local
hostname(config-aaa-server)# exit
hostname(config)#
第二步：为上海办事处配置网络参数：
hostname(config)# aaa-server test type local
hostname(config-aaa-server)# user shanghai
hostname(config-user)# ike-id fqdn shanghai
hostname(config-user)# dhcp-pool-address 192.168.2.1 192.168.2.100
hostname(config-user)# dhcp-pool-netmask 255.255.255.0
hostname(config-user)# dhcp-pool-gateway 192.168.2.101
hostname(config-user)# split-tunnel-route 192.168.200.0/24
hostname(config-user)# split-tunnel-route 192.168.1.0/24
hostname(config-user)# split-tunnel-route 192.168.3.0/24
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)#
第三步：为广州办事处配置网络参数：
hostname(config)# aaa-server test type local
hostname(config-aaa-server)# user guangzhou
hostname(config-user)# ike-id fqdn guangzhou
hostname(config-user)# dhcp-pool-address 192.168.3.1 192.168.3.100
hostname(config-user)# dhcp-pool-netmask 255.255.255.0
hostname(config-user)# dhcp-pool-gateway 192.168.3.101
hostname(config-user)# split-tunnel-route 192.168.200.0/24

<!-- 来源页 1691 -->
hostname(config-user)# split-tunnel-route 192.168.1.0/24
hostname(config-user)# split-tunnel-route 192.168.2.0/24
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)#
第四步：配置PnPVPN Server：
hostname(config)# isakmp proposal test1
hostname(config-isakmp-proposal)# group 2
hostname(config-isakmp-proposal)# exit
hostname(config)# ipsec proposal test2
hostname(config-ipsec-proposal)# group 2
hostname(config-ipsec-proposal)# exit
hostname(config)# isakmp peer test1
hostname(config-isakmp-peer)# type usergroup
hostname(config-isakmp-peer)# mode aggressive
hostname(config-isakmp-peer)# interface ethernet0/1
hostname(config-isakmp-peer)# aaa-server test
hostname(config-isakmp-peer)# isakmp-proposal test1
hostname(config-isakmp-peer)# pre-share 123456
hostname(config-isakmp-peer)#generate-route
hostname(config-isakmp-peer)# exit
hostname(config)# tunnel ipsec test auto
hostname(config-tunnel-ipsec-auto)# ipsec-proposal test2
hostname(config-tunnel-ipsec-auto)# isakmp-peer test1
hostname(config-tunnel-ipsec-auto)# mode tunnel
hostname(config-tunnel-ipsec-auto)# id auto
hostname(config-tunnel-ipsec-auto)# dns 192.168.200.1 192.168.200.11
hostname(config-tunnel-ipsec-auto)# wins 192.168.200.2 192.168.200.12

<!-- 来源页 1692 -->
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)#
第五步：生成客户端密钥：
hostname(config)# exec generate-user-key rootkey 123456 userid shanghai
userkey: kyZAKmLWCc5Nz75fseDiM2r+4Vg=
hostname(config)# exec generate-user-key rootkey 123456 userid guangzhou
userkey: SdqhY4+dPThTtpipW2hs2OMB5Ps=
第六步：配置隧道接口和策略规则：
hostname(config)# zone VPN
hostname(config-zone-VPN)# exit
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone VPN
hostname(config-if-tun1)# tunnel ipsec test
hostname(config-if-tun1)# exit
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone VPN
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone VPN
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any

<!-- 来源页 1693 -->
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone VPN
hostname(config-policy-rule)# dst-zone VPN
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
客户端配置
上海办事处设备配置如下：
1. 登录设备WebUI，从页面左侧导航树选择并点击“配置h网络hIPSec VPN”，进入IPSec VPN页面。
2. 从页面右侧辅助栏的<任务>区选择『PnPVPN客户端』链接，弹出<PnPVPN配置>对话框。在该对话框做以下配
置：
l 服务器地址：202.106.6.208
l ID：shanghai
l 密码：kyZAKmLWCc5Nz75fseDiM2r+4Vg=
l 重新输入密码：kyZAKmLWCc5Nz75fseDiM2r+4Vg=
l 自动保存：选中复选框
l VPN出接口：ethernet0/0
l VPN入接口：ethernet0/3
3. 点击『确定』按钮保存所做配置并发起链接。
广州办事处设备配置如下：

<!-- 来源页 1694 -->
1. 登录设备WebUI，从页面左侧导航树选择并点击“配置h网络hIPSec VPN”，进入IPSec VPN页面。
2. 从页面右侧辅助栏的<任务>区选择『PnPVPN客户端』链接，弹出<PnPVPN配置>对话框。在该对话框做以下配
置：
l 服务器地址：202.106.6.208
l ID：guangzhou
l 密码：SdqhY4+dPThTtpipW2hs2OMB5Ps=
l 重新输入密码：SdqhY4+dPThTtpipW2hs2OMB5Ps=
l 自动保存：选中复选框
l VPN出接口：ethernet0/0
l VPN入接口：ethernet0/3
3. 点击『确定』按钮保存所做配置并发起链接

<!-- 来源页 1695 -->
GRE VPN
GRE协议介绍
GRE（Generic Routing Encapsulation）是通用封装路由，是定义了在任意一种网络层协议上封装任意
一个其它网络层协议的协议。系统支持GRE over IPSec功能，实现路由协议信息的安全传输。
GRE配置
系统的GRE配置包括：
l 配置GRE隧道
l 绑定GRE隧道到隧道接口
l 配置GRE隧道保活报文（Keepalive）
l 显示GRE隧道配置信息
配置GRE隧道
GRE隧道配置需要在GRE隧道配置模式下进行。进入GRE隧道配置模式，在全局配置模式下，使用以下命
令：
tunnel gre gre-tunnel-name
l
gre-tunnel-name – 指定将要创建的GRE隧道的名称。执行该命令后，系统创建指定名称的GRE隧
道，并且进入GRE隧道配置模式；如果指定的名称已存在，则直接进入GRE隧道配置模式。
使用以上命令no的形式删除指定的GRE隧道：
no tunnel gre gre-tunnel-name
进入GRE隧道配置模式后，用户需要为GRE隧道配置以下参数：
l 指定源接口/地址
l 指定目的地址
l 指定出接口
l 指定IPSec VPN隧道（可选）
l 指定验证密钥（可选）
l 开启/关闭ERSPAN解封装功能

<!-- 来源页 1696 -->
指定源地址
为GRE隧道指定源地址，在GRE隧道配置模式下，使用以下命令：
source {interface interface-name [ipv6] | {ipv4-address | ipv6-address }}
l
interface interface-name [ipv6]– 指定接口的IP地址为GRE隧道的源地址，也可指定IPv6地址为
GRE隧道的源地址。通过interface-name参数指定接口名称。
l
ipv4-address | ipv6-address– 为GRE隧道指定源地址（IPv4或IPv6地址）。
在GRE隧道配置模式下使用该命令no的形式取消源地址的配置：
no source
指定目的地址
为GRE隧道指定目的地址，在GRE隧道配置模式下，使用以下命令：
destination {ipv4-address | ipv6-address }
l
ipv4-address | ipv6-address – 为GRE隧道指定目的地址（IPv4或IPv6地址）。
在GRE隧道配置模式下，使用下命令no的形式取消目的地址的配置：
no destination
指定出接口
为GRE隧道指定出接口，在GRE隧道配置模式下，使用以下命令：
interface interface-name
l
interface-name – 指定出接口的名称。
在GRE隧道配置模式下使用该命令no的形式取消出接口配置：
no interface
指定IPSec VPN隧道
使用GRE over IPSec功能时，用户需要通过该命令指定IPSec VPN隧道对数据进行IPSec封装。指定IPSec
VPN隧道，在GRE隧道配置模式下，使用以下命令：
next-tunnel ipsec tunnel-name
l
tunnel-name – 指定IPSec VPN隧道的名称。
在GRE隧道配置模式下使用该命令no的形式取消IPSec VPN隧道的指定：
no next-tunnel

<!-- 来源页 1697 -->
指定验证密钥
通过指定验证密钥，对进入GRE隧道的数据包进行封装与验证。当数据包携带的密钥与接收端配置的验证密
钥相同时，数据包将会被解密。如果不相同，数据包将会被丢弃。指定验证密钥，在GRE隧道配置模式下，
使用以下命令：
key key-value
l
key-value – 指定验证密钥。取值范围为0到4294967295。
在GRE隧道配置模式下使用该命令no的形式取消验证密钥的指定：
no key
开启/关闭ERSPAN解封装功能
ERSPAN（Encapsulated Remote Switched Port Analyzer，封装式远程端口交换分析器）是一种远程
端口镜像技术，它通过GRE隧道将源设备（如交换机、路由器）上的镜像流量封装后，传输到远端的分析设
备（如防火墙），从而实现跨网络边界的流量监控和安全分析。
为解决DHCP流量以及旁路部署环境中IoT设备流量不经过防火墙而无法被识别和分析的问题，系统支持开启
ERSPAN解封装功能。启用后，系统可对GRE隧道中的ERSPAN封装流量进行解封装并还原镜像流量，使防
火墙能够正常处理这类流量，并上送至上层应用进行IoT设备识别、资产管理、威胁检测等深度分析，有效提
升网络安全可见性与防护能力。该功能默认为关闭状态。
注意:
l
为确保防火墙能够对解封装后的ERSPAN流量进行深度分析，请确保防火墙已安装对应的功能
授权许可证（License），如IoT管控许可证、入侵防御许可证等。
l
非根VSYS不支持该功能。
开启/关闭ERSPAN解封装功能，在GRE隧道配置模式下，使用以下命令：
l
开启：erspan enable
l
关闭：erspan disable
绑定GRE隧道到隧道接口
配置完成的GRE隧道需要绑定到隧道接口上才能够生效。绑定GRE隧道到隧道接口，在隧道接口配置模式
下，使用以下命令：
tunnel gre gre-tunnel-name [gw {ipv4-address | ipv6-address | ipv4-address ipv6-address}]

<!-- 来源页 1698 -->
l
gre-tunnel-name – 指定将要绑定的GRE隧道的名称。该隧道为系统中已创建的GRE隧道。
l
gw {ipv4-address | ipv6-address | ipv4-addressipv6-address} – 当配置多个隧道到隧道接口
时，需要配置该参数。该参数指定GRE隧道的下一跳IP地址，为对端隧道接口的IP地址。可以同时配置
IPv4和IPv6类型的地址或仅配置其中一个。
在隧道接口配置模式下，使用该命令no的形式取消GRE隧道的绑定：
no tunnel gre gre-tunnel-name
关于隧道接口的静态路由配置，请参阅《路由》的“配置静态路由”部分。
配置GRE隧道保活报文（Keepalive）
GRE保活功能用于对GRE隧道的连通性进行实时检测，通过双向交互保活报文实现隧道状态监控。配置该功
能后，隧道发起端会定期发送保活请求报文，响应端收到请求后自动返回保活响应报文，由此可进一步提升
GRE 隧道通信的可靠性。
该功能默认为关闭状态。在GRE隧道配置模式下，使用以下命令配置GRE隧道保活报文：
keepalive interval interval-value retry times
l
interval-value - 指定保活请求报文的发送间隔，取值范围1至32767秒。
l
times - 指定发送保活请求后未收到响应时的最大重试次数，取值范围1至255次。
注意:
l
不支持在GRE over IPSec的场景下使用该功能。
l
基于IPv6 接口建立的GRE 隧道，不支持使用该功能。
显示GRE隧道配置信息
用户可以在任何模式下使用以下命令查看GRE隧道配置信息：
show tunnel gre [gre-tunnel-name]
l
gre-tunnel-name – 显示指定名称的GRE隧道配置信息。
例：GRE配置举例
本节介绍通过Hillstone设备实现GRE over IPSec with OSPF的配置举例。

<!-- 来源页 1699 -->
需求描述
中心（Center）与分支（Branch1）跨越Internet互联，且中心与分支之间使用OSPF动态路由协议。通过
配置GRE over IPSec功能实现中心与分支之间信息的安全传输。下图为该需求组网图：
配置步骤
以下分别介绍中心设备Center和分支设备Branch1的配置。
中心配置
对于IPSec VPN和OSPF配置，该文档仅列出必要配置。
第一步：接口配置：
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 202.106.1.1/24
hostname(config-if-eth0/1)# exit
hostname(config)#
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone trust

<!-- 来源页 1700 -->
hostname(config-if-eth0/1)# ip address 192.168.1.1/24
hostname(config-if-eth0/1)# exit
hostname(config)#exit
第二步：IPSec VPN配置：
hostname(config)# isakmp proposal branch1
hostname(config-isakmp-proposal)# exit
hostname(config)# ipsec proposal branch1
hostname(config-ipsec-proposal)# exit
hostname(config)# isakmp peer branch1
hostname(config-isakmp-peer)# interface ethernet0/0
hostname(config-isakmp-peer)# peer 202.106.2.1
hostname(config-isakmp-peer)# pre-share 111111
hostname(config-isakmp-peer)# isakmp branch1
hostname(config-isakmp-peer)# exit
hostname(config)# tunnel ipsec branch1 auto
hostname(config-tunnel-ipsec-auto)# isakmp-peer branch1
hostname(config-tunnel-ipsec-auto)# ipsec-proposal branch1
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)#
第三步：GRE隧道配置：
hostname(config)# tunnel gre center-branch1
hostname(config-tunnel-gre)# source 202.106.1.1
hostname(config-tunnel-gre)# destination 202.106.2.1
hostname(config-tunnel-gre)# interface ethernet0/0
hostname(config-tunnel-gre)# next-tunnel ipsec branch1
hostname(config-tunnel-gre)# exit
hostname(config)#
第四步：绑定GRE隧道到隧道接口：

<!-- 来源页 1701 -->
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone trust
hostname(config-if-tun1)# ip address 172.16.1.1/24
hostname(config-if-tun1)# tunnel gre center-branch1 gw 172.16.1.2
hostname(config-if-tun1)# exit
hostname(config)#
第五步：OSPF配置：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# router ospf
hostname(config-router)# router-id 172.16.1.1
hostname(config-router)# network 172.16.1.1/24 area 0
hostname(config-router)# network 192.168.1.1/24 area 0
hostname(config-router)# exit
hostname(config-vrouter)# exit
hostname(config)#
第六步：策略配置：
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

<!-- 来源页 1702 -->
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
分支配置
第一步：接口配置：
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 202.106.2.1/24
hostname(config-if-eth0/1)# exit
hostname(config)#
hostname(config)# interface ethernet0/0
hostname(config-if-eth0/1)# zone trust
hostname(config-if-eth0/1)# ip address 192.168.2.1/24
hostname(config-if-eth0/1)# exit
hostname(config)#
第二步：IPSec VPN配置：
hostname(config)# isakmp proposal center
hostname(config-isakmp-proposal)# exit
hostname(config)# ipsec proposal center
hostname(config-ipsec-proposal)# exit
hostname(config)# isakmp peer center
hostname(config-isakmp-peer)# interface ethernet0/0
hostname(config-isakmp-peer)# peer 202.106.1.1
hostname(config-isakmp-peer)# pre-share 111111

<!-- 来源页 1703 -->
hostname(config-isakmp-peer)# isakmp center
hostname(config-isakmp-peer)# exit
hostname(config)# tunnel ipsec center auto
hostname(config-tunnel-ipsec-auto)# isakmp-peer center
hostname(config-tunnel-ipsec-auto)# ipsec-proposal center
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)#
第三步：GRE隧道配置：
hostname(config)# tunnel gre branch1
hostname(config-tunnel-gre)# source 202.106.2.1
hostname(config-tunnel-gre)# destination 202.106.1.1
hostname(config-tunnel-gre)# interface ethernet0/0
hostname(config-tunnel-gre)# next-tunnel ipsec center
hostname(config-tunnel-gre)# exit
hostname(config)#
第四步：绑定GRE隧道到隧道接口：
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone trust
hostname(config-if-tun1)# ip address 172.16.1.2/24
hostname(config-if-tun1)# tunnel gre branch1 gw 172.16.1.1
hostname(config-if-tun1)# exit
hostname(config)#
第五步：OSPF配置：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# router ospf
hostname(config-router)# router-id 172.16.1.2
hostname(config-router)# network 172.16.1.2/24 area 0
hostname(config-router)# network 192.168.2.1/24 area 0

<!-- 来源页 1704 -->
hostname(config-router)# exit
hostname(config-vrouter)# exit
hostname(config)#
第六步：策略配置：
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone trust
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)#
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

<!-- 来源页 1705 -->
L2TP VPN
介绍
L2TP（Layer Two Tunneling Protocol，第二层隧道协议）是虚拟专用拨号网络（VPDN）技术的一种。
L2TP可以让拨号用户从L2TP客户端或者L2TP访问集中器端（LAC）发起VPN连接，通过点对点协议
（PPP）连接到L2TP 网络服务器（LNS）。连接成功后，LNS会向合法用户分配IP地址，并允许其访问私
网。
设备在L2TP协议隧道组网中可以充当LNS的角色，也可以充当L2TP客户端的角色。当作为LNS的角色时，
它接受来自L2TP客户端或LAC的连接，进行用户认证与授权，为合法用户分配IP地址、DNS服务器地址和
WINS服务器地址。当作为L2TP客户端的角色时，它主动发起PPP协商和认证，隧道建立完成过后，流量通
过L2TP VPN隧道传输到对端。
L2TP协议不对隧道传输中的数据进行加密，因此在传输过程中无法保证数据的安全。用户可以将L2TP协议
和IPSec协议结合使用，利用IPSec协议对数据进行加密的优势，保证L2TP隧道传输中的数据安全。
说明：关于L2TP协议的更多详细信息，请参阅RFC2661。
本章包含以下内容：
l "典型的L2TP隧道组网" 在第1703页
l "L2TP over IPSec" 在第1704页
l 配置L2TP VPN
典型的L2TP隧道组网
以下为两种典型的L2TP隧道组网模式：
上图为L2TP客户端直接向LNS发出连接请求并建立隧道的组网模式。任何一台装有Windows
2000/2003/XP/Vista或Linux操作系统的计算机都可以充当L2TP客户端。

<!-- 来源页 1706 -->
上图为远程拨号用户通过PSTN/ISDN拨入LAC后，由LAC向LNS发起VPN连接并建立隧道的组网模式。LAC
是为远程拨号用户提供接入服务的设备。它位于远程拨号用户和LNS之间，负责它们之间的数据转发。LAC
与远程拨号用户的连接使用PPP协议或采用本地连接，与LNS端的连接需要利用L2TP协议在它们之间建立隧
道。
L2TP over IPSec
L2TP协议不对隧道传输中的数据进行加密，因此在传输过程中无法保证数据的安全。用户可以将L2TP协议
和IPSec协议结合使用，利用IPsec协议对数据进行加密的优势，保证L2TP隧道传输中的数据安全。
配置L2TP over IPSec，请按照以下步骤进行：
1. 配置L2TP 客户端，并确保客户端启用IPSec数据加密。客户端的配置方法，请参阅相应操作系统的使用手册。
Windows XP操作系统的L2TP客户端配置，可参阅“L2TP over IPSec配置举例”。
2. 配置IPSec VPN。具体操作，请参阅“IPSec协议”。
3. 配置L2TP实例，并引用已创建的IPSec隧道。
4. 配置策略规则。
使用Windows操作系统的L2TP客户端时，应注意以下事项：
l Windows操作系统的L2TP客户端仅支持主模式的IKE协商。因此用户需要将LNS端的IKE协商模式配置为主模
式，同时需要配置accept-all-peer-id命令使ISAKMP网关接受任意的对端ID。配置后，LNS端将不对其IPSec
VPN对端的IP地址进行认证。其他操作系统的L2TP客户端是否支持野蛮模式，请参阅其使用手册。
l Windows操作系统的IPSec协议操作模式仅支持传输模式（transport），因此用户需要将LNS端的IPSec协议操
作模式配置为传输模式。

<!-- 来源页 1707 -->
配置L2TP VPN
设备作为LNS端配置
注意: 设备作为LNS时，L2TP地址池需与隧道接口的IP地址处于同一网段，且隧道接口的IP地址不
能位于地址池的地址范围内。
LNS端的配置包括：
l 地址池配置
l L2TP实例配置
l 绑定已配置的L2TP 实例到隧道接口
l 强制断开L2TP连接
l 隧道重启
地址池配置
LNS通过地址池给用户分配IP地址。当用户连接LNS成功后，LNS会从地址池里取出一个IP地址与其它相关
参数（如DNS服务器地址与WINS服务器地址等）一起分配给用户。在全局配置模式，使用以下命令创建
L2TP地址池：
l2tp pool pool-name
l
pool-name – 指定地址池的名称。
执行该命令后，系统创建指定名称的地址池，并且进入L2TP地址池配置模式；如果指定的名称已存在，则直
接进入L2TP地址池配置模式。在全局配置模式下，使用该命令no的形式删除指定的L2TP地址池：
no l2tp pool pool-name
在L2TP地址池配置模式下可进行如下配置：
l 配置地址池地址范围
l 配置保留地址池
l 配置IP地址绑定规则
配置地址池地址范围
为地址池配置地址范围，在L2TP地址池配置模式下使用以下命令：
address start-ip end-ip

<!-- 来源页 1708 -->
l
start-ip – 指定IP范围的起始IP地址。
l
end-ip – 指定IP范围的结束IP地址。
用户可以为一个地址池最多指定60000个IP地址。
在L2TP地址池配置模式下，使用该命令no的形式删除配置的IP地址范围：
no address
配置保留地址池
保留地址池中的IP地址为地址池中的部分IP地址，当LNS从地址池里取出IP地址分配给用户时，需要保留已
经被占用的部分IP地址（如网关、FTP服务器等），不进行分配。配置保留地址池，在L2TP地址池配置模式
下使用以下命令：
exclude-address start-ip end-ip
l
start-ip – 指定保留地址池的起始IP地址。
l
end-ip – 指定保留地址池的终止IP地址。
在L2TP地址池配置模式下，使用该命令no的形式取消保留地址池的配置：
no exclude address
配置IP地址绑定规则
L2TP通过创建和执行IP地址绑定规则来满足客户端的固定IP地址需求。IP地址绑定规则包括静态IP地址绑定
规则和角色-IP地址绑定规则。静态IP地址绑定规则将客户端用户与已配置地址池中的某个固定IP地址绑定，
当客户端连接成功后，系统会将绑定的IP地址分配给客户端；角色-IP地址绑定规则是将角色与已配置地址池
中的某一IP地址范围绑定，当此客户端连接成功后，系统会从绑定的地址范围中取出一个IP地址分配给客户
端。
当LNS通过地址池给客户端分配IP地址时，系统会按照一定的顺序对客户端的IP地址绑定规则进行检查，决
定如何为客户端分配IP地址：
1. 检查是否已为客户端用户配置静态IP地址绑定规则，如果是，则将绑定的IP地址分配给客户端；否则，需要进一
步检查。注意，如果此静态IP地址绑定规则中的IP地址已被占用，则该用户无法登录。
2. 检查是否已为客户端用户配置角色-IP地址绑定规则，如果是，则从绑定的地址范围中取出一个IP地址分配给客户
端；否则，该用户无法登录。
注意: 静态IP地址绑定规则中的IP地址和角色-IP地址绑定规则中的IP地址不能重叠。

<!-- 来源页 1709 -->
配置静态IP地址绑定规则
配置静态IP地址绑定规则，在L2TP地址池配置模式下使用以下命令：
ip-binding user user-name ip-address
l
user user-name – 指定客户端用户名。
l
ip-address – 指定绑定的IP地址。此地址必须为地址池中可以分配的地址。
在L2TP地址池配置模式下，使用该命令no的形式取消对特定用户静态IP地址绑定规则的配置：
no ip-binding user user-name
配置角色-IP地址绑定规则
配置角色-IP地址绑定规则，在L2TP地址池配置模式下使用以下命令：
ip-binding role role-name ip-range start-ip end-ip
l
role role-name – 指定角色名称。
l
ip-range start-ip end-ip – 指定绑定的IP范围的起始IP地址start-ip和结束IP地址end-ip。此地址范
围必须为地址池中可以分配的地址范围。
在L2TP地址池配置模式下，使用该命令no的形式取消对特定角色的角色-IP地址绑定规则的配置：
no ip-binding role role-name
修改角色-IP地址绑定规则排列顺序
一个用户可以绑定到一个或者多个角色，不同角色可以配置不同的角色-IP地址绑定规则。对于绑定到多个角
色且多个角色有相应的角色-IP地址绑定规则的用户，Hillstone设备会对角色-IP地址绑定规则进行顺序查
找，然后按照查找到的相匹配的第一条规则为用户分配地址。默认情况下，系统会将新创建的规则放到所有
规则的末尾，管理员可以移动已有的角色-IP地址绑定规则从而改变规则的排列顺序。改变规则的排列顺序，
在L2TP地址池配置模式下使用以下命令：
move role-name1 {before role-name2 | after role-name2| top | bottom}
l
role –name1 – 指定被移动的角色-IP地址绑定规则的角色名称。
l
before role-name2 – 将角色-IP地址绑定规则移动到某个角色-IP地址绑定规则(角色名称为rolename2的规则)之前。
l
after role-name2 – 将角色-IP地址绑定规则移动到某个角色-IP地址绑定规则(角色名称为rolename2的规则)之后。

<!-- 来源页 1710 -->
l
top – 将角色-IP地址绑定规则移动到所有角色-IP地址绑定规则之首。
l
bottom – 将角色-IP地址绑定规则移动到所有角色-IP地址绑定规则的末尾。
L2TP 实例配置
创建L2TP实例，在全局配置模式下，使用以下命令：
tunnel l2tp tunnel-name
l
tunnel-name – 指定L2TP实例的名称。
执行该命令后，系统创建指定名称的L2TP实例，并且进入L2TP实例配置模式；如果指定的名称已存在，则
直接进入L2TP实例配置模式。在全局配置模式下，使用该命令no的形式删除指定的L2TP实例：
no tunnel l2tp tunnel-name
在L2TP实例配置模式下，用户可以进行如下配置：
l 指定分配IP方式
l 指定地址池
l 配置DNS服务器
l 配置WINS服务器
l 指定隧道出接口
l 指定AAA服务器
l 指定PPP认证的协议
l 指定Hello报文间隔
l 启用隧道认证
l 指定隧道密码
l 指定LNS本端名称
l 启用AVP数据隐含
l 指定隧道接受窗口大小
l 配置用户同名登录功能
l 允许或禁止用户指定IP地址
l 指定控制报文重传次数
l 引用IPSec隧道
l 配置LCP强制协商

<!-- 来源页 1711 -->
l 开启/关闭UDP报文校验和功能
l 引用用户下线告警模板
指定分配IP方式
LNS通过地址池或本地AAA认证服务器给用户分配IP地址和DNS服务器地址。默认情况下，LNS通过地址池
分配IP地址。
为L2TP实例指定分配IP地址方式，在L2TP实例配置模式下，使用以下命令：
assign-client-ip from { pool | aaa-server }
l
pool – 指定地址池为用户分配IP地址和DNS服务器地址。
l
aaa-server – 指定本地AAA认证服务器为用户分配IP地址和DNS服务器地址。
注意: 所指定的本地AAA认证服务器类型必须是Radius类型。
指定地址池
为L2TP实例指定L2TP地址池，在L2TP实例配置模式下，使用以下命令：
pool pool-name
l
pool-name – 指定已配置的L2TP地址池名称。
在L2TP实例配置模式下，使用该命令no的形式取消地址池的指定：
no pool
配置DNS服务器
指定DNS服务器的地址，在L2TP地址池配置模式下使用以下命令：
dns address1 [address2]
l
address1 – 指定DNS服务器IP地址。用户最多可配置2个DNS服务器。
在L2TP地址池配置模式下，使用该命令no的形式取消对DNS服务器的指定：
no dns
配置WINS服务器
指定WINS服务器的地址，在L2TP地址池配置模式下使用以下命令：
wins address1 [address2]

<!-- 来源页 1712 -->
l
address1 – 指定WINS服务器IP地址。用户最多可配置2个WINS服务器。
在L2TP地址池配置模式下，使用该命令no的形式取消对WINS服务器的指定：
no wins
指定隧道出接口
指定隧道出接口，在L2TP实例配置模式下，使用以下命令：
interface interface-name
l
interface-name – 指定出接口的名称。
在L2TP实例配置模式下，使用该命令no的形式取消出接口的配置：
no interface
指定AAA服务器
此处指定的AAA服务器为LNS进行L2TP用户身份认证的AAA服务器。指定AAA服务器，在L2TP实例配置模
式下，使用以下命令：
aaa-server aaa-server-name [domain domain-name [keep-domain-name]]
l
aaa-server-name – 指定AAA服务器的名称。
l
domain domain-name – 为AAA服务器指定域名以区分不同的AAA服务器。
l
keep-domain-name – 指定该参数后，用于身份认证的用户名将验证域名。
在L2TP实例配置模式下，使用该命令no的形式取消对AAA服务器的指定：
no aaa-server aaa-server-name [domain domain-name]
指定PPP认证的协议
LNS与客户端或LAC建立连接时，在PPP协商的过程中可以对用户使用PAP和CHAP协议进行身份验证。指定
PPP认证的协议，在L2TP实例配置模式下，使用以下命令：
ppp-auth {pap | chap | any}
l
pap – 指定PPP认证方式为密码认证协议PAP。
l
chap – 指定PPP认证方式为质询握手认证协议CHAP。此选项为默认选项。
l
any – 指定该参数后，系统首选认证方式为CHAP，如果认证不支持CHAP协议时，则使用PAP协议进行
认证。

<!-- 来源页 1713 -->
在L2TP实例配置模式下，使用该命令no的形式恢复默认配置：
no ppp-auth
指定LCP Echo报文发送间隔
在PPP协商过程中LNS会定期发送LCP Echo报文判断链路的连通性。指定LCP Echo报文发送的时间间隔，
在L2TP实例配置模式下，使用以下命令：
ppp-lcp-echo interval time
l
time – 指定LCP Echo报文发送的时间间隔。单位为秒。范围是0到1000秒，0秒表示不发送LCP Echo
报文。默认值是30秒。
在L2TP实例配置模式下，使用该命令no的形式恢复时间间隔的默认值：
no ppp-lcp-echo interval
指定Hello报文间隔
L2TP 使用Hello 报文来检测隧道是否连通。LNS定时向L2TP客户端或LAC发送Hello 报文，若在一段时间
内未收到应答，该隧道连接将被断开。指定Hello报文发送的时间间隔，在L2TP实例配置模式下，使用以下
命令：
keepalive time
l
time – 指定Hello报文发送的时间间隔。单位为秒。范围是60到1800秒。默认值是60秒。
在L2TP实例配置模式下，使用该命令no的形式恢复时间间隔的默认值：
no keepalive
启用隧道认证
在隧道建立连接前，用户可启用隧道认证功能以保证连接的安全。隧道认证可由LNS或LAC任何一端发起，
只有两端均通过隧道认证，即隧道密码一致时，方可建立隧道。默认情况下，隧道验证功能是关闭状态。在
L2TP实例配置模式下，使用以下命令启用该功能：
tunnel-authentication
在L2TP实例配置模式下，使用该命令no的形式禁用隧道认证：
no tunnel-authentication
指定隧道密码
指定LNS端隧道认证的密码，在L2TP实例配置模式下，使用以下命令：

<!-- 来源页 1714 -->
secret secret-string [peer-name name]
l
secret-string – 指定隧道密码。范围为1至31个字符。
l
peer-name name – 指定LAC端设备的主机名称。如果多个LAC与LNS建立连接，用户可通过配置该项
参数为不同的LAC端设备指定不同的隧道密码。如果没有指定该参数，系统对多个LAC端均使用相同的隧
道密码。
在L2TP实例配置模式下，使用该命令no的形式取消指定隧道密码：no secret secret-string [peername name]
指定LNS本端名称
用户可以在LNS端指定本端隧道的名称，在L2TP实例配置模式下，使用以下命令：
local-name name
l
name – 指定LNS端隧道的名称。范围为1至31个字符。默认值为“LNS”。
在L2TP实例配置模式下，使用该命令no的形式恢复默认值：
no local-name
启用AVP数据隐含
L2TP协议使用AVP（attribute value pair，属性值对）来传递和协商L2TP 的一些参数、属性等。在默认
情况下，AVP 是采用明文形式传输的。为了保证数据安全，用户可以通过隧道密码加解密这些数据，将这些
AVP 隐藏起来传输。在L2TP实例配置模式下，使用以下命令启用或禁用AVP数据隐含功能：
l
启用AVP数据隐含：avp-hidden
l
禁用AVP数据隐含（默认配置）：no avp-hidden
注意: 启用AVP数据隐含功能需要配置隧道密码。
指定隧道接受窗口大小
传送数据时，用户可以指定隧道传输数据的窗口大小。在L2TP实例配置模式下，使用以下命令：
tunnel-receive-window window-size
l
window-size – 指定窗口大小。单位为包，默认值为8包，取值范围为4至800包。
在L2TP实例配置模式下，使用该命令no的形式恢复默认值：
no tunnel-receive-window

<!-- 来源页 1715 -->
配置用户同名登录功能
用户同名登录功能指允许同一个用户在多个地点同时登录认证。默认情况下，此功能为开启状态。在L2TP实
例配置模式下，使用以下命令启用或禁用用户同名登录功能：
l
启用用户同名登录：allow-multi-logon
l
禁用用户同名登录：no allow-multi-logon
允许或禁止客户端指定IP地址
默认情况下，客户端的IP地址由LNS从地址池中取出并自动分配。启用该功能后，用户可以指定IP地址，但
该IP地址必须属于已指定的地址池范围之内且与用户的用户名和角色一致。如果指定的IP地址已被占用，则
系统禁止该用户登录。在L2TP实例配置模式下，使用以下命令允许或禁止指定IP地址：
l
允许客户端指定IP地址（默认配置）：accept-client-ip
l
禁止客户端指定IP地址：no accept-client-ip
指定控制报文重传次数
L2TP协议使用两种类型的报文：控制报文和数据报文。控制报文负责创建、维护及清除L2TP隧道，数据报
文负责传输数据。数据报文的传输是不可靠传输，若数据丢失，则不进行数据重传。控制报文的传输是可靠
传输，如果在指定的重传次数内未收到对端的响应，则系统认为隧道连接已经断开。控制报文重传间隔从1
秒开始，按照2的倍数增长，如1秒、2秒、4秒、8秒、16秒等。指定控制报文重传次数，在L2TP实例配置
模式下，使用以下命令：
transmit-retry times
l
times – 指定控制报文重传次数。范围是1至10次。默认值为5次。
在L2TP实例配置模式下，使用该命令no的形式恢复控制报文重传次数的默认值：
no transmit-retry
引用IPSec隧道
用户在配置L2TP over IPSec时，需要将IPSec隧道与L2TP隧道结合用来加密数据。在L2TP实例配置模式
下，使用以下命令在L2TP实例中引用IPSec隧道：
next-tunnel ipsec tunnel-name
l
tunnel-name – 指定已创建的IPSec VPN的隧道名称。
在L2TP实例配置模式下，使用该命令no的形式取消引用IPSec隧道：

<!-- 来源页 1716 -->
no next-tunnel ipsec
配置LCP强制协商
远程拨号用户拨入LAC后，由LAC向LNS发起L2TP VPN连接并建立隧道。当LNS再次对用户进行验证时，可
配置LNS是否与L2TP客户端进行LCP（Link Control Protocol，链路控制协议）强制协商。
默认情况下，LNS不与L2TP客户端进行LCP强制协商，而是根据ICCN（Incoming-Call-Connected）报
文中Proxy Authen Type AVP所指定的认证方式对L2TP客户端进行认证。系统支持PAP与CHAP认证两种
类型。
用户可配置LNS与L2TP客户端进行LCP强制协商，在L2TP实例配置模式下，使用如下命令：
ppp-lcp-force
关闭强制协商，使用no ppp-lcp-force命令。
在远程用户直接向LNS发起L2TP VPN连接并建立隧道的场景下，ICCN（Incoming-Call-Connected）报
文中不会携带Proxy Authen Type AVP，无论用户是否开启和关闭LCP强制协商，LNS都将于L2TP客户端
进行LCP强制协商。
开启/关闭UDP报文校验和功能
UDP报文校验和功能默认情况下是关闭的，即UDP报文头部经过更改后设备会重新计算UDP校验和。用户如
果希望提高设备的性能，可以关闭UDP报文校验和功能，设备将不再进行UDP校验和的计算。开启/关闭
UDP报文校验和功能，请在L2TP实例配置模式下使用以下命令：
l
开启UDP报文校验和功能：l2tp-udp-checksum enable
l
关闭UDP报文校验和功能：l2tp-udp-checksum disable
引用用户下线告警模板
系统支持用户下线告警功能，用户在配置L2TP VPN实例时，可以引用已配置的用户下线告警模板，实现对
用户下线情况的监控。当在指定时间内，下线用户数达到指定阈值则进行相应告警。
引用用户下线告警模板，在L2TP实例配置模式下，使用以下命令：
user-logout-alarmprofile_name
l
profile_name – 指定系统中已配置的用户下线告警模板名称。
在L2TP实例配置模式下，使用no user-logout-alarm命令取消用户下线告警模板的引用。

<!-- 来源页 1717 -->
注意:
l
引用用户下线告警模板前，请先配置用户下线告警模板。关于用户下线告警模板的配置方法，
请参阅新建用户下线告警模板。
l
目前仅L2TP VPN功能支持引用用户下线告警模板，且系统中所有的用户下线告警模板被引用
次数总和不能超过8次。
l
用户下线告警模板被引用时，不支持修改告警阈值。
绑定L2TP实例到隧道接口
配置好的L2TP实例需要绑定到隧道接口，才能够生效。每一个隧道接口只能绑定一个L2TP实例。当一个
L2TP实例只绑定一个隧道接口并且没有为此L2TP隧道（绑定L2TP实例的隧道）指定域名时，所有拨入此
LNS的客户端将被划分到此隧道对应的VR中。
用户也可将多个隧道接口绑定到一个L2TP实例并为每一个L2TP隧道指定不同的域名。当客户端发起L2TP
VPN连接并完成用户认证后，系统将根据客户端用户的域名，将客户端接入到指定了相同域名的隧道中。当
隧道接口属于不同的VR时，LNS可通过认证服务器将内网资源地址重复分配给每个L2TP隧道中的客户端。
绑定L2TP实例到隧道接口，在隧道接口配置模式下，使用以下命令：
tunnel l2tp tunnel-name [bind-to-domain domain-name]
l
tunnel-name – 指定系统中已配置的L2TP实例的名称。
l
bind-to-domain domain-name – 为L2TP隧道绑定域名（即domain name）。绑定域名后，如果
登陆用户的用户名不存在域名，拨号将失败。如果没有为L2TP实例绑定域名，LNS进行认证时将忽略登
录用户的域名。
在隧道接口配置模式下使用该命令no的形式取消隧道接口与L2TP实例的绑定以及指定的域名：
no tunnel l2tp tunnel-name
在隧道接口配置模式下使用如下命令取消指定的域名：
no tunnel l2tp tunnel-name bind-to-domain domain-name
指定PPP数据包含ACF信息
LNS与客户端或LAC建立连接时，用户可以通过命令指定LNS在发送的PPP数据报文在封装时是否包含ACF字
段信息（Address Control Field），即地址和控制字段，在全局配置模式下，使用以下命令：
l2tp-include-ppp-acf
在全局配置模式下使用如下命令取消PPP数据包含ACF信息：
no l2tp-include-ppp-acf

<!-- 来源页 1718 -->
强制断开L2TP连接
用户可以通过命令强制断开某个用户与LNS的连接。强制断开连接，在执行模式下使用以下命令：
exec l2tp tunnel-name kickout user user-name
l
tunnel-name – 指定L2TP实例的名称。
l
user-name – 指定被强制断开连接的用户名。
隧道重启
隧道重启后，所有与该隧道的连接将被清除。在任何模式下，使用以下命令重启隧道：
clear l2tp tunnel-name
l
tunnel-name – 指定L2TP实例的名称。
显示L2TP信息
用户可以通过show命令查看系统L2TP信息。
l
显示L2TP实例信息：
show tunnel l2tp [l2tp-tunnel-name]
l
显示已创建的L2TP隧道的状态信息：
show l2tp tunnel l2tp-tunnel-name
l
显示L2TP实例当前在线的客户端信息：
show l2tp client {tunnel-name l2tp-tunnel-name [user user-name] [public-ipip_address]|
tunnel-id ID}
l
显示L2TP地址池的配置信息：
show l2tp pool [pool-name]
l
显示L2TP地址池的统计信息：
show l2tp pool pool-name statistics
l
显示所有L2TP实例当前在线的客户端信息：
show auth-user l2tp [interface interface-name | vrouter vrouter-name | slot slot-no]
L2TP客户端配置
如果采用L2TP客户端和Hillstone设备（LNS）之间建立L2TP隧道的组网模式，用户需要对L2TP客户端进
行配置。关于Windows 2000/2003/XP/Vista操作系统的L2TP信息，请参阅Windows
2000/2003/XP/Vista操作系统相关文档。

<!-- 来源页 1719 -->
注意: 使用Windows操作系统的L2TP客户端拨号连接LNS时，请确保系统中未安装Hillstone
Secure Defender。
设备作为L2TP客户端配置
L2TP客户端的配置包括：
l L2TP客户端实例配置
l 清除L2TP客户端连接
l 显示L2TP客户端实例信息
L2TP 客户端实例配置
创建L2TP客户端实例，在全局配置模式下，使用以下命令：
tunnel l2tp-client tunnel-name
l
tunnel-name – 指定L2TP客户端实例的名称。
执行该命令后，系统创建指定名称的L2TP客户端实例，并且进入L2TP客户端实例配置模式；如果指定的名
称已存在，则直接进入L2TP客户端实例配置模式。在全局配置模式下，使用该命令no的形式删除指定的
L2TP客户端实例：
no tunnel l2tp-client tunnel-name
在L2TP客户端实例配置模式下，用户可以进行如下配置：
l 指定隧道出接口
l 指定LNS服务器
l 指定隧道保活时间
l 配置自动连接
l 指定隧道认证方式
l 指定PPP报文的发送间隔和重传次数
l 指定L2TP客户端用户名及密码
l 配置控制报文重传次数
l 配置协商超时时间

<!-- 来源页 1720 -->
指定隧道出接口
指定绑定L2TP VPN隧道的隧道接口，流量通过隧道接口进出L2TP VPN通道。在L2TP客户端实例配置模式
下，使用以下命令：
interface interface-name
l
interface-name – 指定出接口的名称。
在L2TP客户端实例配置模式下，使用该命令no的形式取消出接口的配置：
no interface
指定LNS服务器
配置LNS服务器的IP地址或域名，在L2TP客户端实例配置模式下，使用以下命令：
lns-ip ip-address/hostname
l
ip-address/hostname - 指定LNS服务器的IP地址或域名。取值范围为1-255个字符。
在L2TP客户端实例配置模式下，使用该命令no的形式取消对LNS服务器的指定：
no lns-ip
指定隧道保活时间
LNS和L2TP客户端之间的隧道建立后，为保证双方的正常通信，L2TP客户端会定期发送Hello报文确认LNS
是否可以正常连接。“保活时间”即连续两次发送hello报文之间的时间间隔，取值越小则设备对于可能存
在的网络故障感知越快，取值越大则hello报文占用网络带宽越小。指定隧道保活时间间隔，在L2TP客户端
实例配置模式下，使用以下命令：
keepalive time
time – 指定Hello报文发送的时间间隔。单位为秒。范围是60到1800秒。默认值是60秒。
在L2TP客户端实例配置模式下，使用该命令no的形式恢复时间间隔的默认值：
no keepalive
配置自动连接
开启L2TP客户端自动拨号功能。开启此功能后，L2TP客户端与LNS之间可以自主建立隧道，用户不用PPP拨
号即可访问LNS内网。在L2TP客户端实例配置模式下，使用以下命令：
l2tp-auto-client
在L2TP客户端实例配置模式下，使用以下命令关闭自动连接功能：

<!-- 来源页 1721 -->
no l2tp-auto-client
指定隧道认证方式
L2TP客户端与LNS端建立连接时，在PPP协商的过程中可以对用户使用PAP和CHAP协议进行身份验证。指
定PPP认证的协议，在L2TP客户端实例配置模式下，使用以下命令：
ppp-auth {pap | chap | any}
l
pap – 指定PPP认证方式为密码认证协议PAP。
l
chap – 指定PPP认证方式为质询握手认证协议CHAP。此选项为默认选项。
l
any – 指定该参数后，系统首选认证方式为CHAP，如果认证不支持CHAP协议时，则使用PAP协议进行
认证。
在L2TP客户端实例配置模式下，使用该命令no的形式恢复默认配置：
no ppp-auth
指定PPP报文的发送间隔和重传次数
在PPP协商过程中L2TP客户端会定期发送LCP Echo报文判断链路的连通性。指定LCP Echo报文发送的时间
间隔和重传次数，在L2TP客户端实例配置模式下，使用以下命令：
ppp-lcp-echo interval time retry times
l
interval time – 指定LCP Echo报文发送的时间间隔。单位为秒。范围是0到1000秒，0秒表示不发送
LCP Echo报文。默认值是30秒。
l
retry times -指定发送LCP Echo报文的重传次数。如果L2TP客户端在发送次数达到设置的重传次数后
未收到响应，会判断连接已经断开。配置范围是1-30次，默认值是4次。
在L2TP客户端实例配置模式下，使用该命令no的形式恢复默认值：
no ppp-lcp-echo interval time retry times
指定L2TP客户端用户名及密码
L2TP客户端使用指定的用户名向LNS端发起L2TP VPN隧道建立请求，LNS端对拨入用户认证通过后，建立
L2TP隧道和会话。
指定L2TP客户端用户名和密码，在L2TP客户端实例配置模式下，使用以下命令：
user user-name password password

<!-- 来源页 1722 -->
l
user-name - 指定L2TP客户端使用的用户名，配置范围是1-31个字符。
l
password -指定L2TP客户端用户名密码，配置范围是4-63字符。
配置控制报文重传次数
指定L2TP控制报文重传次数，在L2TP客户端实例配置模式下，使用以下命令：
transmit-retry times
times – 指定控制报文重传次数。范围是1至10次。默认值为5次。
在L2TP客户端实例配置模式下，使用该命令no的形式恢复控制报文重传次数的默认值：
no transmit-retry
配置协商超时时间
系统支持配置协商超时时间，若在指定时间内未协商成功，则自动重新发起协商。默认情况下，系统不自动
重新协商。在L2TP客户端实例配置模式下，使用以下命令：
negotiation-timeout timeout-value
l
timeout-value – 指定协商超时时间，单位为秒。范围为30到300秒。
在L2TP客户端实例配置模式下，使用该命令no的形式取消协商超时时间的配置（不自动重新协商）：
no negotiation-timeout
清除L2TP客户端连接
清除L2TP客户端连接，在任何模式下，使用以下命令：
clear l2tp-client [tunnel-name]
l
tunnel-name - 清除指定名称的客户端连接。
显示L2TP客户端信息
用户可以通过show命令查看L2TP客户端信息。
显示L2TP客户端实例信息
show tunnel l2tp-client [tunnel-name]
显示L2TP客户端拨号情况信息
show l2tp-client [tunnel-name]

<!-- 来源页 1723 -->
L2TPv3隧道配置
L2TPv3是Layer Two Tunneling Protocol - Version 3的简称，提供高性能基于IP的隧道技术，是二层
VPN传输技术的一种实现方式。
配置L2TPv3隧道
配置L2TPv3隧道，在全局配置模式下，使用以下命令：
tunnel l2tpv3 tunnel-name
l
tunnel-name - 指定L2TPv3隧道的名称。
在全局模式下，使用命令no tunnel l2tpv3 tunnel-name取消配置L2TPv3隧道。
配置隧道出接口
配置隧道出接口，在L2TPv3隧道模式下，使用以下命令：
interface interface-name
l
interface-name - 指定隧道出接口名称。
在L2TPv3隧道模式下使用命令no interface取消配置隧道出接口。
配置L2TPv3隧道的本地和远端的session-id
创建隧道后，配置L2TPv3隧道的本地和远端的session-id，用于设备对接，在L2TPv3隧道模式下，使用以
下命令：
id local-session-id remote-session-id
l
local-session-id - 指定L2TPv3隧道的本地session-id。
l
remote-session-id - 指定L2TPv3隧道的远端session-id。
配置L2TPv3隧道的本端cookie密钥和远端cookie密钥
配置L2TPv3隧道的本端cookie密钥和远端cookie密钥，设备根据报文的cookie字段跟预先配置做比较，
不等则丢弃报文，用来在隧道的终端做安全检查。远端cookie密钥必须与对端设备的cookie一致，否则会
导致报文丢失，业务中断。
配置本端cookie密钥
配置本端cookie密钥，在L2TPv3隧道模式下，使用以下命令：
cookie local {4 lower-value | 8 lower-value high-value}

<!-- 来源页 1724 -->
l
4 lower-value - 指定本端密钥的明文低4字节。
l
8 lower-value high-value - 指定本端密钥的明文8字节的低4位和高4位。
在L2TPv3隧道模式下，使用命令no cookie local取消配置本端cookie密钥。
配置远端cookie密钥
配置远端cookie密钥，在L2TPv3隧道模式下，使用以下命令：
cookie remote {4 lower-value | 8 lower-value high-value}
l
4 lower-value - 指定本端密钥的明文低4字节。
l
8 lower-value high-value - 指定本端密钥的明文8字节的低4位和高4位。
在L2TPv3隧道模式下，使用命令no cookie remote取消配置远端cookie密钥。
配置L2TPv3隧道的目的IP地址
配置L2TPv3隧道的目的IP地址，在L2TPv3隧道模式下，使用以下命令：
destination ip-address
l
ip-address - 指定L2TPv3隧道的目的IP地址。
在L2TPv3隧道模式下，使用命令no destination 取消配置隧道目的IP地址。
配置L2TPv3隧道接口的安全域
配置L2TPv3隧道接口的安全域，在L2TPv3隧道接口模式下，使用以下命令：
zone zone
l
zone - 指定L2TPv3隧道接口的安全域。
在L2TPv3隧道接口模式下，使用命令no zone取消配置L2TPv3隧道接口的安全域。
将L2TPv3隧道绑定到隧道接口
将L2TPv3隧道绑定到隧道接口，在隧道接口模式下，使用以下命令：
tunnel l2tpv3 tunnel-name [filter ipv6]
l
tunnel-name - 指定绑定隧道的名称。
l
filter ipv6 - 配置L2TPv3隧道进行IPv6数据包过滤。
在隧道接口模式下，使用命令no tunnel l2tpv3 tunnel-name取消配置L2TPv3隧道绑定到隧道接口。

<!-- 来源页 1725 -->
显示L2TPv3隧道配置信息
显示L2TPv3隧道配置信息，在L2TPv3隧道模式下，使用以下命令：
show tunnel l2tpv3 tunnel-name

<!-- 来源页 1726 -->
例：L2TP配置举例
本节介绍L2TP的配置举例。
组网需求
某员工需要通过L2TP VPN 远程访问公司总部的内网资源，组网图如下：
配置步骤
该组网的配置分为LNS配置和L2TP客户端配置。
LNS配置
第一步：配置Hillstone设备的接口：
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone untrust
hostname(config-if-eth0/1)# ip address 58.31.46.207/24
hostname(config-if-eth0/1)# exit
hostname(config)# interface ethernet0/2

<!-- 来源页 1727 -->
hostname(config-if-eth0/2)# zone trust
hostname(config-if-eth0/2)# ip address 10.110.0.190/24
hostname(config-if-eth0/2)# exit
hostname(config)#
第二步：配置本地AAA认证服务器：
hostname(config)# aaa-server local
hostname(config-aaa-server)# user shanghai
hostname(config-user)# password 123456
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)#
第三步：配置LNS地址池，并指定地址池IP范围：
hostname(config)# l2tp pool pool1
hostname(config-l2tp-pool)# address 10.232.241.2 10.232.244.254
hostname(config-l2tp-pool)#dns 202.106.0.20 10.188.7.10
hostname(config-l2tp-pool)# exit
hostname(config)#
第四步：配置L2TP实例：
hostname(config)# tunnel l2tp test
hostname(config-tunnel-l2tp)# pool pool1
hostname(config-tunnel-l2tp)# interface ethernet0/1
hostname(config-tunnel-l2tp)# ppp-auth any
hostname(config-tunnel-l2tp)# keepalive 1800
hostname(config-tunnel-l2tp)# aaa-server local
hostname(config-tunnel-l2tp)# exit
hostname(config)#
第五步：创建隧道接口并绑定L2TP实例“test”到该接口：
hostname(config)# interface tunnel1

<!-- 来源页 1728 -->
hostname(config-if-tun1)# zone untrust
hostname(config-if-tun1)# ip address 10.232.241.1 255.255.248.0
hostname(config-if-tun1)# manage ping
hostname(config-if-tun1)# tunnel l2tp test
hostname(config-if-tun1)# exit
hostname(config)#
第六步：配置策略规则：
hostname(config)# policy-global
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
客户端配置
本部分以配置Windows XP操作系统的L2TP客户端程序为例，说明配置步骤：
1. 创建L2TP拨号连接。
2. 配置已创建的拨号连接，修改相关属性。
3. 修改注册表禁用IPSec加密。
创建L2TP拨号连接
按照以下步骤创建Windows XP操作系统的L2TP拨号连接：
1. 点击“开始菜单à控制面板à网络和Internet 连接”。
2. 选择“创建一个到您的工作位置的网络连接”，系统弹出新建连接向导对话框。

<!-- 来源页 1729 -->
3. 选择“虚拟专用网络连接”的单选按钮，并点击“下一步”。
4. 在“公司名”文本框中指定此连接的名称“L2TP”；并点击“下一步”。
5. 选择“不拨此初始连接”的单选按钮，并点击“下一步”。
6. 在“主机名或IP地址”文本框中输入LNS的IP 地址“58.31.46.207”，点击“下一步”。
7. 根据连接向导，完成L2TP客户端其它配置。
配置L2TP拨号连接
按照以下步骤修改已创建的拨号连接的属性：
1. 打开“网上邻居”，双击网络连接中已创建的拨号连接名称“L2TP”，打开连接L2TP对话框。如下图所示：
2. 点击“属性”，打开L2TP属性对话框。
3. 点击L2TP属性的“安全”标签，选择“高级（自定义设置）”单选按钮，并点击其后的“设置”，弹出高级安全
设置对话框。
4. 在“数据加密”下拉菜单中选择“可选加密（没有加密也可以连接）”，在“登录安全措施”框内选择“允许这
些协议”的单选按钮，并勾选“不加密的密码（PAP）”和“质询握手身份验证协议（CHAP）”前的复选框。
点击“确定”。如下图所示：

<!-- 来源页 1730 -->
5. 点击L2TP属性对话框的“网络”标签，在“VPN类型”下拉菜单中选择“L2TP IPSec VPN”，勾选“此连接使
用下列项目”栏内的“Internet 协议（TCP/IP）”。如下图所示：

<!-- 来源页 1731 -->
6. 点击“确定”，保存所做的修改。
修改注册表
默认情况下，Windows XP操作系统对L2TP连接启用IPSec加密。用户可以通过修改Windows XP 的注册
表来禁用这种默认行为。如果没有禁用IPSec加密，L2TP客户端在拨号过程中会被自动断开连接。
按照以下步骤修改注册表：
1. 点击“开始菜单à运行”，在运行对话框中输入“Regedt32”，弹出注册表编辑器窗口。
2. 在左侧注册表项目中逐级点击HKEY_LOCAL_
MACHINE\System\CurrentControlSet\Services\RasMan\Parameters。
3. 为Parameters参数添加DWORD值。单击Parameters项，然后在注册表编辑器右侧空白处单击鼠标右键，弹出
右键菜单。选择“新建àDWORD值”，如下图所示。指定该值名称为“ProhibitIPSec”、数据类型为“REG_

<!-- 来源页 1732 -->
DWORD”、值为“1”。点击“确定”，保存所做的修改。
4. 退出注册表编辑器，重新启动计算机以使改动生效。
使用客户端连接LNS
完成LNS和客户端的配置后，用户可以使用已配置的客户端对LNS发起VPN连接并建立隧道。
使用客户端连接LNS，用户需要打开“网上邻居”，双击网络连接中已创建的拨号连接“L2TP”，在弹出的
连接对话框中输入用户名“shanghai”和密码“123456”，然后点击“连接”。如下图所示：
拨号连接成功后，该名在上海的员工就可以通过L2TP协议安全地访问公司的Web服务器和FTP服务器。

<!-- 来源页 1733 -->
在MS-DOS方式下输入“ipconfig”，系统返回一个LNS地址池中的地址“10.232.241.2 15”，即LNS分
配给他的PC的IP地址。
例：L2TP over IPSec配置举例
本节介绍L2TP over IPSec的配置举例。
组网需求
某员工需要通过L2TP VPN访问公司的Web资源，PC与LNS之间的数据通过IPSec协议加密后传输。组网图
如下：
配置步骤
该组网的配置分为LNS配置和L2TP客户端配置。
LNS配置
第一步：配置Hillstone设备的接口：
hostname(config)# interface ethernet0/2
hostname(config-if-eth0/2)# zone trust
hostname(config-if-eth0/2)# ip address 10.110.0.190/24
hostname(config-if-eth0/2)# exit
hostname(config)# interface ethernet0/3
hostname(config-if-eth0/3)# zone untrust
hostname(config-if-eth0/3)# ip address 192.168.1.1/24
hostname(config-if-eth0/3)# exit

<!-- 来源页 1734 -->
hostname(config)#
第二步：配置IPSec VPN：
hostname(config)# isakmp proposal p1
hostname(config-isakmp-proposal)# authentication pre-share
hostname(config-isakmp-proposal)# hash sha
hostname(config-isakmp-proposal)# exit
hostname(config)# ipsec proposal p2
hostname(config-ipsec-proposal)# protocol esp
hostname(config-ipsec-proposal)# hash sha
hostname(config-ipsec-proposal)# encryption 3des
hostname(config-ipsec-proposal)# exit
hostname(config)# isakmp peer east
hostname(config-isakmp-peer)# interface ethernet0/3
hostname(config-isakmp-peer)# type usergroup
hostname(config-isakmp-peer)# accept-all-peer-id
hostname(config-isakmp-peer)# mode main
hostname(config-isakmp-peer)# isakmp-proposal p1
hostname(config-isakmp-peer)# pre-share hello1
hostname(config-isakmp-peer)# aaa-server local
hostname(config)# tunnel ipsec vpn1 auto
hostname(config-tunnel-ipsec-auto)# mode transport
hostname(config-tunnel-ipsec-auto)# isakmp-peer east
hostname(config-tunnel-ipsec-auto)# ipsec-proposal p2
hostname(config-tunnel-ipsec-auto)# accept-all-proxy-id
hostname(config-tunnel-ipsec-auto)# exit
hostname(config)#
第三步：配置本地AAA认证服务器：
hostname(config)# aaa-server test type local

<!-- 来源页 1735 -->
hostname(config-aaa-server)# user shanghai
hostname(config-user)# password 123456
hostname(config-user)# exit
hostname(config-aaa-server)# exit
hostname(config)#
第四步：配置LNS地址池，并指定地址池IP范围：
hostname(config)# l2tp pool pool2
hostname(config-l2tp-pool)# address 10.10.10.2 10.10.10.100
hostname(config-l2tp-pool)#dns 202.106.0.20
hostname(config-l2tp-pool)# exit
hostname(config)#
第五步：配置L2TP实例，并引用IPSec隧道：
hostname(config)# tunnel l2tp l2tp1
hostname(config-tunnel-l2tp)# pool pool2
hostname(config-tunnel-l2tp)# interface ethernet0/3
hostname(config-tunnel-l2tp)# next-tunnel ipsec vpn1
hostname(config-tunnel-l2tp)# ppp-auth chap
hostname(config-tunnel-l2tp)# keepalive 1800
hostname(config-tunnel-l2tp)# aaa-server test
hostname(config-tunnel-l2tp)# exit
hostname(config)#
第六步：创建隧道接口并绑定L2TP实例“l2tp1”到该接口：
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone dmz
hostname(config-if-tun1)# ip address 10.10.10.1/24
hostname(config-if-tun1)# manage ping
hostname(config-if-tun1)# tunnel l2tp l2tp1
hostname(config-if-tun1)# exit

<!-- 来源页 1736 -->
hostname(config)#
第七步：配置策略规则：
hostname(config)# policy-global
hostname(config-policy)# rule
hostname(config-policy-rule)# src-zone dmz
hostname(config-policy-rule)# dst-zone trust
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config-policy)# exit
hostname(config)#
客户端配置
本部分以配置Windows XP操作系统的L2TP客户端程序为例，说明配置步骤：
1. 创建L2TP拨号连接。
2. 配置已创建的拨号连接，修改相关属性。
3. 启用IPSec加密。
创建L2TP拨号连接
按照以下步骤创建Windows XP操作系统的L2TP拨号连接：
1. 点击“开始菜单à控制面板à网络和Internet 连接”。
2. 选择“创建一个到您的工作位置的网络连接”，系统弹出新建连接向导对话框。
3. 选择“虚拟专用网络连接”的单选按钮，并点击“下一步”。
4. 在“公司名”文本框中指定此连接的名称“L2TP over IPSec”；并点击“下一步”。
5. 选择“不拨此初始连接”的单选按钮，并点击“下一步”。
6. 在“主机名或IP地址”文本框中输入LNS的IP 地址“192.168.1.1”，点击“下一步”。
7. 根据连接向导，完成L2TP客户端其它配置。

<!-- 来源页 1737 -->
配置L2TP拨号连接
按照以下步骤修改已创建的拨号连接的属性：
1. 打开“网上邻居”，双击网络连接中已创建的拨号连接名称“L2TP over IPSec”，打开连接L2TP over IPSec对
话框。
2. 点击“属性”，打开属性对话框。
3. 点击标签页，进行属性的详细配置，配置如下：
l “安全”标签页的配置：
l 选择“高级（自定义设置）”单选按钮，并点击其后的“设置”，弹出高级安全设置对话框。在“数据加
密”下拉菜单中选择“可选加密（没有加密也可以连接）”，在“登录安全措施”框内选择“允许这些协
议”的单选按钮，并勾选“不加密的密码（PAP）”和“质询握手身份验证协议（CHAP）”前的复选
框。点击“确定”。
l 选择“IPSec设置”，在弹出的对话框中勾选“使用预共享的密钥作身份验证”并输入密钥“hello1”。
点击“确定”。
l “网络”标签页的配置：在“VPN类型”下拉菜单中选择“L2TP IPSec VPN”，并勾选“此连接使用下列
项目”栏内的“Internet 协议（TCP/IP）”。
4. 点击“确定”按钮，保存配置并关闭属性对话框。
启用IPSec加密
默认情况下，Windows XP操作系统对L2TP连接启用IPSec加密。如果禁用了IPSec加密，用户也可以通过
修改注册表来重新启用这种默认行为。
按照以下步骤修改注册表：
1. 点击“开始菜单à运行”，在运行对话框中输入“Regedt32”，弹出注册表编辑器窗口。
2. 在左侧注册表项目中逐级点击HKEY_LOCAL_
MACHINE\System\CurrentControlSet\Services\RasMan\Parameters。
3. 为Parameters参数添加DWORD值。单击Parameters项，然后在注册表编辑器右侧空白处单击鼠标右键，弹出
右键菜单。选择“新建àDWORD值”。指定该值名称为“ProhibitIPSec”、数据类型为“REG_DWORD”、值
为“0”。点击“确定”，保存所做的修改。
4. 退出注册表编辑器，重新启动计算机以使改动生效。

<!-- 来源页 1738 -->
使用客户端连接LNS
完成LNS和客户端的配置后，用户可以使用已配置的客户端对LNS发起VPN连接并建立隧道。使用客户端连
接LNS，用户需要打开“网上邻居”，双击网络连接中已创建的拨号连接“L2TP over IPSec”，在弹出的
连接对话框中输入用户名“shanghai”和密码“123456”，然后点击“连接”。拨号连接成功后，该员工
就可以通过L2TP协议安全地访问公司的Web资源。

<!-- 来源页 1739 -->
VXLAN
介绍
VXLAN是采用MAC in UDP（User Datagram Protocol）封装方式，是NVO3（Network
Virtualization over Layer3）中的一种大二层虚拟网络扩展的隧道封装技术。VXLAN引入了类似VLAN
ID的用户标识，称为VXLAN网络标识VNI（VXLAN Network ID），由24比特组成，可划分多达16M的
VXLAN段，从而满足了大量的用户标识。通过VXLAN构建大二层网络，保证了在虚拟迁移时虚拟机的IP地
址、MAC地址等参数保持不变。
VXLAN使用VTEP（VXLAN Tunnel Endpoint，VXLAN隧道端点）设备对VXLAN 报文进行封装与解封
装，包括ARP请求报文和正常的VXLAN数据报文。VETP将原始以太网帧通过VXLAN封装后发送至对端VTEP
设备，对端VETP设备接收到VXLAN报文后解封装，然后根据原始MAC进行转发，VTEP可以是物理交换机、
物理服务器或者其他支持VXLAN的硬件设备或软件来实现。
型号说明：
l
不支持：K系列K20803、K9180、K7680、K7280、K6680、K6580。
l
不支持：X系列平台。
配置VXLAN静态隧道
配置VXLAN静态隧道并进入VXLAN隧道配置模式
配置VXLAN静态隧道并进入VXLAN隧道配置模式，在全局配置模式下，使用命令：
tunnel vxlan name
l
name - 指定VXLAN静态隧道的名称。
在全局配置模式下，使用命令no tunnel vxlan name取消配置VXLAN静态隧道。
配置VXLAN静态隧道的目的VTEP的IP地址
配置VXLAN静态隧道的目的VTEP的IP地址，在VXLAN隧道配置模式下，使用命令：
destination ipv4-address
l
ipv4-address - 指定VXLAN静态隧道的目的VTEP的IP地址。
在VXLAN隧道配置模式下，使用命令no destination 取消配置VXLAN静态隧道的目的VTEP的IP地址。

<!-- 来源页 1740 -->
配置VXLAN静态隧道的VNI
配置VXLAN静态隧道的VNI ，即VXLAN网络标识，在VXLAN隧道配置模式下，使用命令：
vni id
l
id - 指定VXLAN静态隧道的网络标识，取值范围是1-16777215。
在VXLAN隧道配置模式下，使用命令no vni 取消配置VXLAN静态隧道的网络标识。
配置VXLAN静态隧道出接口
配置VXLAN静态隧道出接口，在VXLAN隧道配置模式下，使用命令：
interface interface-name
l
interface-name - 指定VXLAN静态隧道的出接口。
在VXLAN隧道配置模式下，使用命令no interface取消配置VXLAN静态隧道的出接口。
配置VXLAN动态源端口范围
默认情况下，设备在发送VXLAN数据包时，会使用固定端口4789作为VXLAN的源端口进行通信。然而，在
某些VXLAN应用场景中，设备使用固定端口进行通信，可能会出现会话混淆、资源分配失衡及负载均衡失效
等问题；为此，系统提供配置VXLAN动态源端口范围功能。用户通过配置VXLAN动态源端口的范围，可使
设备从指定的端口范围中动态选取一个端口作为VXLAN的源端口，确保每个会话使用独立端口进行数据传
输，从而实现端口资源的均衡利用，避免因单一端口拥塞导致的性能瓶颈，同时配合负载均衡设备优化流量
分发，提升网络资源利用率和系统健壮性，尤其适用于多租户云环境等高并发场景。
在VXLAN隧道配置模式下，使用以下命令，配置VXLAN动态源端口范围：
source-port range minimum maximum
l
minimum maximum - 指定设备在发送VXLAN数据包时，可动态选取的源端口范围，取值范围是1到
65535。默认为固定端口4789（即端口范围为4789~4789）。
在VXLAN隧道配置模式下，使用以下命令，恢复默认值：
no source-port range
配置VXLAN静态隧道目的端口
配置对端VTEP上接收VXLAN数据的UDP端口，本端设备发送的VXLAN数据将被封装并发送至该端口。为确
保VXLAN隧道正常通信，本端配置的目的端口需与对端VTEP实际监听的UDP端口一致（该监听端口即为对
端VXLAN Tunnel中所配置的目的端口），且通信两端的设备均需为山石网科防火墙设备。
配置VXLAN静态隧道目的端口，在VXLAN隧道配置模式下，使用命令：

<!-- 来源页 1741 -->
destination-port port-number
l
port-number - 指定VXLAN静态隧道的目的端口号。默认使用的UDP端口号为4789，可根据实际需求
进行自定义配置，取值范围为1到65535。
在VXLAN隧道配置模式下，使用命令no destination-port删除配置的目的端口。
指定引用的IPSec隧道
系统支持将VXLAN报文加密封装在IPSec报文中，保证VXLAN隧道传输中的数据安全。指定引用的IPSec隧
道，在VXLAN隧道配置模式下，使用命令：
next-tunnel ipsectunnel-name
l
tunnel-name - 指定VXLAN静态隧道引用的IPSec隧道名称。
在VXLAN隧道配置模式下，使用命令no next-tunnel 取消VXLAN静态隧道引用的IPSec隧道。
注意:
l
不支持引用对端类型为“用户组”的IPSec隧道。
l
仅支持HA Active-Passive（A/P）模式。
开启/关闭克隆源端口功能
型号说明：仅云·界支持该功能。
系统支持开启/关闭克隆源端口功能。默认情况下，该功能为关闭状态。启用后，当数据包进入VXLAN隧道
时，系统会复制原始流量的源端口信息，并将这些流量通过多个物理或逻辑端口同时发送出去，从而实现流
量负载均衡分配、链路冗余备份等目的，保障网络的高可用性与吞吐效率。该功能主要用于流量复制与负载
均衡（SLB）。
在VXLAN隧道配置模式下，使用以下命令，开启/关闭克隆源端口功能：
l
开启：source-port clone
l
关闭：no source-port clone
注意: source-port rangeminimummaximum和source-port clone命令不能同时配置。若两
者都不进行配置，设备会使用固定端口4789作为源端口发送VXLAN数据包。

<!-- 来源页 1742 -->
开启/关闭传递VXLAN扩展字段功能
型号说明：仅云·界支持该功能。
VXLAN的扩展字段是在VXLAN隧道中用于携带额外信息的字段，它允许在VXLAN封装的UDP报文中包含更
多的元数据。这些元数据可以用于支持多租户环境、提供网络隔离、以及实现更细粒度的流量管理和路由策
略。
系统支持开启/关闭传递VXLAN扩展字段功能。默认情况下，该功能为关闭状态。启用后，系统在数据包进
入VXLAN隧道时，会保留其扩展字段信息，并根据该扩展字段将流量精确传输到对应的目的地，从而提升网
络流量管理的精确度和效率。例如：在华为云部署场景中，服务器负载均衡（SLB）通常需要通过三层网关
（L3GW）实现流量分发，而单个SLB节点可能与多个L3GW相连接，为确保SLB能够正确地将流量传输到对
应的L3GW，需在VXLAN的扩展字段中添加相应的L3GW虚拟隧道端点（VTEP）地址信息，以此作为流量路
由判定的依据。
在VXLAN隧道配置模式下，使用以下命令，开启/关闭传递VXLAN扩展字段功能：
l
开启：copy-extension
l
关闭：no copy-extension
为VXLAN隧道接口绑定安全域
为VXLAN隧道接口绑定安全域，在隧道接口配置模式下，使用命令：
zone { l2-zone | l3-zone}
l
l2-zone - 为VXLAN隧道指定绑定的二层安全域名称。
l
l3-zone - 为VXLAN隧道指定绑定的三层安全域名称，仅云·界支持该功能。
在隧道接口配置模式下，使用命令no zone { l2-zone | l3-zone}取消绑定安全域。
绑定VXLAN隧道到隧道接口
配置完成的VXLAN隧道需要绑定到隧道接口上才能够生效。
注意：如果要使VXLAN隧道能够正常使用，隧道接口需要绑定二层安全域。
绑定VXLAN隧道到隧道接口，在隧道接口配置模式下，使用以下命令：
tunnel vxlan vxlan-tunnel-name
l
vxlan-tunnel-name – 指定将要绑定的VXLAN隧道的名称。该隧道为系统中已创建的VXLAN隧道。

<!-- 来源页 1743 -->
在隧道接口配置模式下，使用该命令no的形式取消VXLAN隧道的绑定：
no tunnel vxlan vxlan-tunnel-name
显示VXLAN隧道配置信息
在任何模式下，使用以下命令，显示VXLAN隧道配置信息：
show tunnel vxlan name
例如：
hostname# show tunnel vxlan test
===================================
Name vni Interface Peer Next-tunnel Source-Port
（隧道名称网络标识出接口目的VETP的IP地址引用的IPSec隧道动态源端口范围）
-----------------------------------
test 3001 ethernet0/0 1.1.1.1 IPSec1 20~50
===================================
VXLAN配置举例
本节介绍VXLAN相关的配置举例。
l 例：配置VXLAN静态单播隧道
l 例：配置VXLAN静态隧道，实现不同网段网络之间的三层互通
例：配置VXLAN静态单播隧道
本示例介绍配置VXLAN静态单播隧道，采用MAC in UDP封装来延伸二层网络，通过VXLAN，虚拟网络可
接入大量租户。
组网环境如下图所示，PC1和PC2通过VXLAN隧道（VNI100）进行通信。
说明：同一隧道中，不同VNI之间不能互相通信。

<!-- 来源页 1744 -->
提示: 本示例所展示的操作步骤，基于StoneOS 5.5R8版本进行配置。若有变动，请以实际页面为
准。
配置步骤
VTEP1 配置
第一步：配置接口。
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone l2-trust
hostname(config-if-eth0/1)# exit
第二步：配置VXLAN隧道。
hostname(config)# tunnel vxlan tunnel 1
hostname(config-tunnel-vxlan)# interface ethernet0/7
hostname(config-tunnel-vxlan)# destination 7.1.1.2
hostname(config-tunnel-vxlan)# vni 100
hostname(config-tunnel-vxlan)# exit
hostname(config)#
第三步：配置隧道接口，绑定二层安全域。
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone l2-trust
hostname(config-if-tun1)#tunnel vxlan tunnel1
hostname(config-if-tun1)# exit
hostname(config)#
第四步：配置策略。
hostname(config)# policy-global
hostname(config-policy)# rule id 1
Rule id 1 is created
hostname(config-policy-rule)# src-addr any

<!-- 来源页 1745 -->
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config)#
VTEP2 配置
第一步：配置接口。
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone l2-trust
hostname(config-if-eth0/1)# exit
第二步：配置VXLAN隧道。
hostname(config)# tunnel vxlan tunnel 1
hostname(config-tunnel-vxlan)# interface ethernet0/7
hostname(config-tunnel-vxlan)# destination 7.1.1.1
hostname(config-tunnel-vxlan)# vni 100
hostname(config-tunnel-vxlan)# exit
hostname(config)#
第三步：配置隧道接口，绑定二层安全域。
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone l2-trust
hostname(config-if-tun1)#tunnel vxlan tunnel1
hostname(config-if-tun1)# exit
hostname(config)#
第四步：配置策略。
hostname(config)# policy-global
hostname(config-policy)# rule id 1

<!-- 来源页 1746 -->
Rule id 1 is created
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit
hostname(config)#
第五步：验证结果。
以上配置完成后，PC1和PC2可以通过VXLAN隧道互相通信。
例：配置VXLAN静态隧道，实现不同网段网络之间的三层互通
该节介绍VXLAN静态隧道的配置实例。
组网需求
某企业在两个不同的部门分别有服务器Server1（IP：192.168.1.2/24）和服务器Server2
（IP：192.168.2.2/24），且没有专门的网络使散落在不同位置的两个服务器相互通信，现需通过部署
Hillstone设备并建立VXLAN静态隧道实现不同网段网络之间的三层互通。
组网图参见下图：
l 需求一：VTEP1的VXLAN静态隧道配置在三层安全域，并绑定tunnel1隧道接口。
l 需求二：VTEP2的VXLAN静态隧道配置在三层安全域，并绑定tunnel2隧道接口。
注意: 仅云·界支持配置VXLAN隧道在三层安全域。
需求一配置步骤
第一步：配置接口：
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone trust

<!-- 来源页 1747 -->
hostname(config-if-eth0/1)# ip address 192.168.1.1/24
hostname(config-if-eth0/1)# exit
第二步：配置VXLAN隧道：
hostname(config)# tunnel vxlan test1
hostname(config-tunnel-vxlan)# destination 10.1.1.1
hostname(config-tunnel-vxlan)# interface ethernet0/2
hostname(config-tunnel-vxlan)# vni 3001
hostname(config-tunnel-vxlan)# exit
第三步：配置隧道接口，绑定三层安全域：
hostname(config)# interface tunnel1
hostname(config-if-tun1)# zone trust
hostname(config-if-tun1)# ip address 4.1.1.2/24
hostname(config-if-tun1)# tunnel vxlan test1
hostname(config-if-tun1)# exit
第四步：配置路由：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 192.168.2.0/24 4.1.1.3
hostname(config-vrouter)# exit
第五步：配置策略：
hostname(config)# policy-global
hostname(config-policy)# rule id 1
Rule id 1 is created
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit

<!-- 来源页 1748 -->
需求二配置步骤
第一步：配置接口：
hostname(config)# interface ethernet0/1
hostname(config-if-eth0/1)# zone trust
hostname(config-if-eth0/1)# ip address 192.168.2.1/24
hostname(config-if-eth0/1)# exit
第二步：配置VXLAN隧道：
hostname(config)# tunnel vxlan test2
hostname(config-tunnel-vxlan)# destination 10.1.1.2
hostname(config-tunnel-vxlan)# interface ethernet0/2
hostname(config-tunnel-vxlan)# vni 3001
hostname(config-tunnel-vxlan)# exit
第三步：配置隧道接口，绑定三层安全域：
hostname(config)# interface tunnel2
hostname(config-if-tun2)# zone trust
hostname(config-if-tun2)# ip address 4.1.1.3/24
hostname(config-if-tun2)# tunnel vxlan test2
hostname(config-if-tun2)# exit
第四步：配置路由：
hostname(config)# ip vrouter trust-vr
hostname(config-vrouter)# ip route 192.168.1.0/24 4.1.1.2
hostname(config-vrouter)# exit
第五步：配置策略：
hostname(config)# policy-global
hostname(config-policy)# rule id 1
Rule id 1 is created
hostname(config-policy-rule)# src-addr any
hostname(config-policy-rule)# dst-addr any

<!-- 来源页 1749 -->
hostname(config-policy-rule)# service any
hostname(config-policy-rule)# action permit
hostname(config-policy-rule)# exit

<!-- 来源页 1750 -->
VPN集群
当中心端存在多个节点，并且分支端与各个中心端节点均有多条隧道链路时，用户可以在分支端上创建并配
置VPN集群。VPN集群能够提升服务的连续性、可用性与灵活性。当某条隧道链路出现故障时，流量能够迅
速切换到其他可用的链路上；或当某个中心端节点故障时，其余中心端节点也能够承担起工作负载，保证业
务不受影响。
注意:
l
加入集群隧道组中的IPSec VPN隧道，需开启以下功能：
l
分支端：在<VPN对端配置>中需要将连接类型配置为“发起者”并开启产生路由功能；
在<IPSec VPN配置>中需要手动配置代理ID并开启自动连接功能；需要将隧道绑定至隧
道接口上。
l
中心端：在<VPN对端配置>中需要将连接类型配置为“响应者”并开启产生路由功能；
在<IPSec VPN配置>中需要手动配置代理ID（若VPN对端类型为用户组且VPN开启了接
受对端任意代理ID功能，则不需要配置代理ID）并开启VPN隧道监测功能；需要将隧道
绑定至隧道接口上。
l
相关配置参见“VPN > IPSec VPN > 配置IPSec > 配置IKEv1 VPN”章节。
l
X系列设备、K20803、K9180、K7680、K7280、K6680、K6580作为分支端时不支持配置
VPN集群，作为中心端时支持监控VPN集群信息。
l
VPN集群功能不支持IKEv2和国密协议标准的隧道。
l
VPN集群功能不支持VSYS。
l
不能同时使用VPN集群功能和VPN多进程功能。
l
分支端不支持HA。在HA环境下将隧道加入VPN集群隧道组后，隧道将无法使用。
该章节包含以下内容：
l 创建VPN集群
l 配置VPN集群描述
l 配置隧道组
l 配置链路保持时间
l 配置链路回切时间

<!-- 来源页 1751 -->
l 配置隧道质量探测
l 配置业务探测
l 手动指定主隧道组
l 查看隧道组信息
l 查看VPN集群信息
创建VPN集群
注意: 每个分支端最多支持配置2个VPN集群。
对VPN集群的各项配置需要在VPN集群配置模式下进行。创建VPN集群，在全局配置模式下，使用以下命
令：
vpn cluster name [id cluster-id] site-id site-id
l
name - 指定VPN集群的名称。取值范围为1-31个字符。
l
id cluster-id - 指定VPN集群的ID。取值范围为1-2。
l
site-id site-id - 指定分支端的分支标识，便于在中心端区分各分支端。取值范围为1-63个字符。
执行该命令后，系统将创建指定名称的VPN集群，并进入VPN集群配置模式。如果指定的名称已存在，可使
用vpn cluster name命令直接进入对应的VPN集群配置模式。
删除VPN集群，在全局配置模式下，使用以下命令：
no vpn cluster name
注意: 删除VPN集群前需要先将集群中已添加的隧道组删除。
配置VPN集群描述
配置VPN集群描述信息，在VPN集群配置模式下，使用以下命令：
description string
l
string - 指定VPN集群的描述信息。取值范围为1-255个字符。
删除VPN集群描述信息，在VPN集群配置模式下，使用以下命令：
no description

<!-- 来源页 1752 -->
配置隧道组
配置隧道组，用于管理IPSec VPN隧道，每个VPN集群最多配置4个隧道组。
注意:
l
同一VPN集群中各隧道组的优先级不能相同。
l
当高优先级的隧道组中隧道链路质量均不满足要求时，系统将切换使用次优先级的隧道组，依
次往下。
l
隧道组有主、备、从、连接中四种状态，只有主隧道组中的隧道会下发路由。
配置隧道组，在VPN集群配置模式下，使用以下命令：
tunnel-group group-name priority value
l
group-name - 指定隧道组的名称。取值范围为1-31个字符。
l
priority value - 指定隧道组的优先级，系统将按照优先级选用隧道组，优先级数值越小优先级越高。
取值范围为1-4。
执行该命令后，系统将创建指定名称的隧道组，并进入隧道组配置模式。如果指定的名称已存在，可使用
tunnel-group group-name命令直接进入对应的隧道组配置模式。
删除隧道组，在VPN集群配置模式下，使用以下命令：
no tunnel-group group-name
绑定IPSec VPN隧道
注意:
l
每个隧道组最多绑定8条IPSec VPN隧道。
l
隧道组中最高优先级的隧道为实际使用的隧道，若优先级高的隧道链路质量不满足要求，则切
换使用次优先级的隧道，依次往下。
将IPSec VPN隧道绑定至隧道组，在隧道组配置模式下，使用以下命令：
tunnel ipsec ipsec-name [priority value]

<!-- 来源页 1753 -->
l
ipsec ipsec-name - 指定需要加入隧道组的隧道名称，必须为系统中已创建的隧道。
l
priority value - 指定隧道的优先级，系统将按照优先级选用隧道。优先级数值越小优先级越高。取值
范围为1-4。若不指定，默认为1，表示为最高优先级。
删除IPSec VPN隧道，在隧道组配置模式下，使用以下命令：
no tunnel ipsec ipsec-name
配置链路保持时间
配置隧道组切换的链路保持时间，即最短切换时间，避免因网络波动造成隧道组频繁切换。该功能仅针对主
隧道组，链路保持时间从隧道组变为主状态时开始计算。例如：指定隧道组的链路保持时间为5分钟，则主
隧道组中的所有隧道链路质量均不满足要求并且主隧道组存在时间已经超过5分钟时，才会触发隧道组切
换。
配置链路保持时间，在VPN集群配置模式下，使用以下命令：
link-hold-time value
l
value - 指定链路保持时间。取值范围为0-30分钟，默认为5分钟。若配置为0，表示关闭该功能。
恢复默认的链路保持时间，在VPN集群配置模式下，使用以下命令：
no link-hold-time
配置链路回切时间
配置隧道组的链路回切时间。若备隧道组的优先级高于主隧道组，当达到链路回切时间时，将进行主备切
换。链路回切时间从隧道组变为主状态时开始计算。
配置链路回切时间，在VPN集群配置模式下，使用以下命令：
switch-back-time value
l
value - 指定链路回切时间。取值范围为0-600分钟，默认为300分钟。若配置为0，表示关闭该功能。
恢复默认的链路回切时间，在VPN集群配置模式下，使用以下命令：
no switch-back-time
配置隧道质量探测
系统会对隧道组中的隧道链路进行隧道质量探测，当探测到的链路抖动、延迟、丢包率均小于阈值时，表示
隧道质量满足要求。该功能是针对单条隧道链路质量进行探测，而非针对整体隧道质量。
隧道质量探测包含：

<!-- 来源页 1754 -->
l 配置抖动阈值
l 配置延迟阈值
l 配置丢包率阈值
l 配置劣化持续时间
配置抖动阈值
配置抖动阈值，在VPN集群配置模式下，使用以下命令：
tunnel-sla jitter threshold value
l
value - 指定抖动阈值。取值范围为0-1000毫秒，默认为100毫秒。若配置为0，表示不对链路抖动进
行限制。
恢复默认的抖动阈值，在VPN集群配置模式下，使用以下命令：
no tunnel-sla jitter threshold
配置延迟阈值
配置延迟阈值，在VPN集群配置模式下，使用以下命令：
tunnel-sla latency threshold value
l
value - 指定延迟阈值。取值范围为0-1000毫秒，默认为100毫秒。若配置为0，表示不对链路延迟进
行限制。
恢复默认的延迟阈值，在VPN集群配置模式下，使用以下命令：
no tunnel-sla latency threshold
配置丢包率阈值
配置丢包率阈值，在VPN集群配置模式下，使用以下命令：
tunnel-sla loss-rate threshold value
l
value - 指定丢包率阈值。取值范围为0-100%，默认为5%。若配置为0，表示不对链路丢包率进行限
制。
恢复默认的丢包率阈值，在VPN集群配置模式下，使用以下命令：
no tunnel-sla loss-rate threshold

<!-- 来源页 1755 -->
配置劣化持续时间
配置劣化持续时间，当链路探测结果超出阈值持续指定时间后，系统将判定该隧道链路的质量不满足要求。
配置劣化持续时间，在VPN集群配置模式下，使用以下命令：
tunnel-sla degradation-duration-time value
l
value - 指定劣化持续时间。取值范围为0-30秒，默认为15秒。若配置为0，表示关闭该功能，当链路
探测结果达到阈值时，系统就会判定该隧道链路的质量不满足要求。
恢复默认的劣化持续时间，在VPN集群配置模式下，使用以下命令：
no tunnel-sla degradation-duration-time value
配置业务探测
业务探测是向指定的内网IP发送探测报文，探测链路是否可达。若探测失败，说明通过主隧道组中的隧道链
路访问内网失败，链路不可达，将触发隧道组切换。
业务探测包含：
l 配置源接口
l 配置检测间隔时间
l 配置连续失败次数
l 配置对端业务IP
配置源接口
配置源接口，在VPN集群配置模式下，使用以下命令：
service-track src-if interface
l
interface - 指定业务探测的源接口，该源接口需要为分支端连接本地内网的接口。
配置检测间隔时间
配置检测间隔时间，在VPN集群配置模式下，使用以下命令：
service-track interval value
l
value - 指定检测间隔时间。取值范围为1-255秒，默认为10秒。
恢复默认的检测间隔时间，在VPN集群配置模式下，使用以下命令：
no service-track interval

<!-- 来源页 1756 -->
配置连续失败次数
配置连续失败次数，在VPN集群配置模式下，使用以下命令：
service-track threshold value
l
value - 指定连续失败次数，当连续探测失败次数达到指定次数时，表示业务探测失败，链路不可达。
取值范围为1-255次，默认为10次。
恢复默认的连续失败次数，在VPN集群配置模式下，使用以下命令：
no service-track threshold
配置对端业务IP
配置对端业务IP，即所需探测的内网业务IP。最多配置2个对端业务IP。
配置对端业务IP，在VPN集群配置模式下，使用以下命令：
service-track dst-ip {A.B.C.D | X:X:X:X::X}
l
A.B.C.D - 指定IPv4类型的对端业务IP。
l
X:X:X:X::X - 指定IPv6类型的对端业务IP。
取消配置对端业务IP，在VPN集群配置模式下，使用以下命令：
no service-track dst-ip {A.B.C.D | X:X:X:X::X}
手动指定主隧道组
用户可以手动指定主隧道组，当所指定的隧道组状态为主时，保持不变；当所指定的隧道组状态为备时，该
隧道组将切换为主隧道组；当所指定的隧道组状态为从时，系统会尝试连接该隧道组中的隧道，若连接成功
且隧道质量满足要求，则该隧道组切换为主隧道组，否则保持不变。
手动指定主隧道组，在任意模式下，使用以下命令：
exec vpn cluster cluster-name tunnel-group tunnel-group-name master
l
cluster-name - 指定需要切换的VPN集群名称。
l
tunnel-group-name - 指定需要切换的隧道组名称。
查看隧道组信息
查看隧道组信息和链路探测结果，在任意模式下，使用以下命令：
show vpn cluster cluster-name tunnel-group-name

<!-- 来源页 1757 -->
l
cluster-name - 指定所需查看的VPN集群名称。
l
tunnel-group-name - 指定所需查看的隧道组名称。
以下是返回结果示例，其中“status”列带“*”的表示正在使用的隧道：
hostname(config)# show vpn cluster cluster-testHUB1
=========================================================================
==============================
tunnel-group: HUB1
priority: 1
status: MASTER
flag: * - Used tunnel
=========================================================================
==============================
Name priority status latency(ms) jitter(ms) loss-rate(%) upstream(Bps)
downstream(Bps)
-------------------------------------------------------------------------
------------------------------
HUB1-tun~ 1 connected* 1 0 0 248 248
=========================================================================
==============================
查看VPN集群信息
查看VPN集群信息和隧道组状态，在任意模式下，使用以下命令：
show vpn cluster cluster-name
l
cluster-name - 指定所需查看的VPN集群名称。
以下是返回结果示例：
hostname(config)# show vpn cluster cluster-test
================================================================
VPN cluster cluster-test info:
ID:1

<!-- 来源页 1758 -->
site-id: Branch1
switch-back time: 300(min)
link-hold time: 5(min)
description:
service-track:
interval: 10(second)
threshold: 10
src-if: vswitchif1
tunnel-SLA:
latency threshold: 100ms
jitter threshold: 100ms
loss-rate threshold: 5%
degradation-duration time: 15(second)
tunnel-group:
================================================================
Name state priority tunnel-num
----------------------------------------------------------------
HUB1 MASTER 1 1
HUB2 BACKUP 2 1
================================================================

<!-- 来源页 1759 -->
Geneve
在各类云环境中（如亚马逊云AWS、阿里云等）运行着关键应用程序，云·界虚拟防火墙对进出云环境的流
量进行安全检查，单个虚拟实例或主备冗余虚拟实例处理能力有限，容易成为网络性能瓶颈。
阿里云、亚马逊云等云厂商提供的网关型负载均衡（GWLB，Gateway Load Balancer）服务，能在多台
设备间对流量类安全网元的流量进行高性能负载分配。它通过IP监听，可将所有端口的流量分发给后端服务
器组中的网络虚拟设备（NVA，Network Virtual Appliance），这样一来，既能有效解决单设备的性能
瓶颈问题，满足大规模、高并发的云网络流量管理需求，实现对流量灵活的分发与处理，又能助力轻松完成
各类网络虚拟设备的高可用部署。
而云・界虚拟防火墙在GWLB应用场景中，作为网络虚拟设备集成至后端服务器组中，以实现访问流量的检
测和过滤。云・界提供Geneve功能，用于适配各类云厂商的GWLB方案。
Geneve（通用网络虚拟化封装）是一种网络虚拟化隧道协议，它通过将原始数据帧封装在UDP 数据包中，
在底层IP网络（Underlay网络）之上构建虚拟网络（Overlay网络），该协议具备出色的可扩展性，能通
过添加Type - Length - Value（TLV）字段来支持丰富多样的功能，为网络虚拟化场景下的数据传输与封
装提供了有力的技术支撑。当云・界虚拟防火墙接收到GWLB封装的Geneve报文后，会先执行解封装操
作，提取出原始流量并对其执行安全策略；之后，按照云厂商GWLB的要求，对流量重新进行Geneve封
装，再将封装后的流量发回GWLB。通过这一过程，在GWLB的流量负载架构中，嵌入了云・界虚拟防火墙
的安全防护能力，实现了负载均衡与安全防护的协同工作，保障了云网络中流量的高效且安全传输。
注意:
l
Geneve功能当前仅适用于亚马逊云AWS、阿里云和天翼云的GWLB方案。
l
仅支持对Geneve封装格式的报文进行处理；若接收的报文非Geneve封装格式（例如明文数据
报文），在报文封装（encap）过程中，系统由于无法匹配到所需的扩展数据（ex_data），
将会直接执行丢弃操作。
型号说明：仅云·界支持该功能。
GWLB工作原理
如下图所示，以阿里云GWLB工作流程为例，说明GWLB结合云·界虚拟防火墙Geneve的完整工作流程。

<!-- 来源页 1760 -->
相关概念说明：
l VPC：Virtual Private Cloud，虚拟私有云，是针对公有云的基础网络来定义的一种概念。各个云服务商推出的
VPC服务一般是指，用户在云服务商申请的隔离的、私密的网络环境。用户可以自由配置VPC内的IP地址段、子
网、安全组等服务。
l GWLB：Gateway Load Balancer，网关型负载均衡，通过将流量透明地分发到不同的后端服务器来提高应用系
统的安全性和可用性。
l GWLBe：Gateway Load Balancer Endpoint，网关型负载均衡终端节点，是一种特殊类型的VPC终端节点，可
以通过GWLBe在业务VPC与安全VPC之间建立私网连接。
l Geneve：Geneve（通用网络虚拟化封装）隧道，GWLB和后端网络虚拟设备（山石云・界虚拟防火墙）使用
Geneve协议进行通信。
工作流程说明如下：
l ①：客户端访问服务端的流量被路由至网关型负载均衡终端节点GWLBe。
l ②：GWLBe通过私网连接（PrivateLink）服务将访问流量路由至安全VPC中的GWLB。
l ③：GWLB将原始报文通过Geneve隧道封装，然后根据流量调度算法将流量转发至后端网络虚拟设备（山石
云・界虚拟防火墙）。云・界会根据Geneve隧道携带的64位GWLBe ID等信息来识别流量的不同来源。
l ④：云・界收到做完相应处理之后，再次使用Geneve隧道将报文转发到GWLB。云・界接收到GWLB封装的
Geneve报文后，会先执行解封装操作，提取出原始流量并对其执行安全策略；再按照云厂商GWLB的要求，对
流量重新进行Geneve封装，再将封装后的流量发回GWLB。
l ⑤：GWLB会通过私网连接（PrivateLink）将流量转发至相应的GWLBe。
l ⑥：GWLBe会根据目的地址查找路由，将流量转发至服务端相应的目的服务器。

<!-- 来源页 1761 -->
配置Geneve
开始之前
l 阅读"Geneve" 在第1757页功能介绍。
l 阅读"GWLB工作原理" 在第1757页。
前置条件
l 已在云环境（亚马逊云AWS、阿里云和天翼云）中完成网关型负载均衡（GWLB）组网的部署与搭建，确保
GWLB基础网络架构可正常运行。
l 已在云环境（亚马逊云AWS、阿里云和天翼云）中完成云・界虚拟防火墙的部署，且已在GWLB组网内创建后端
服务器组，并将云・界添加至该服务器组中，用于接收GWLB转发的客户端请求。
注意:
l
当报文经GWLB封装后送到云·界处理完成后返回的报文需保持为单个报文（即不能产生分片报
文），因此，需将VPN隧道报文的分片方式指定为“先分片后封装”（即可使用no vpnfragment-post-frag命令恢复系统默认的分片方式“先分片后封装”）。
配置Geneve隧道并进入Geneve隧道配置模式
配置Geneve隧道并进入Geneve隧道配置模式，在全局配置模式下，使用命令：
tunnel geneve name
l
name - 指定Geneve隧道的名称。
在全局配置模式下，使用命令no tunnel geneve name删除配置Geneve隧道。
配置Geneve隧道的目的IP地址
配置Geneve隧道的目的IP地址，指定流量经Geneve封装后流向的目的IP地址，通常为网关型负载均衡
（GWLB）的IP地址。在流量传输流程中，经Geneve封装后的流量会以该目的IP地址，发送到GWLB，从而
进入后续由GWLB进行流量转发等操作的环节。在Geneve隧道配置模式下，使用命令：
destination ipv4-address
l
ipv4-address - 指定Geneve隧道的目的IP地址。
在Geneve隧道配置模式下，使用命令no destination删除配置Geneve隧道的目的IP地址。

<!-- 来源页 1762 -->
注意: Geneve隧道目前仅支持IPv4地址类型，暂不支持IPv6地址类型。
配置Geneve隧道出接口
配置定云・界虚拟防火墙发送经Geneve封装后流量时所使用的接口，即与GWLB连接的接口，Geneve封装
流量通过该接口流出云・界，进而传输到GWLB。在Geneve隧道配置模式下，使用命令：
interface interface-name
l
interface-name - 指定Geneve隧道的出接口。
在Geneve隧道配置模式下，使用命令no interface删除配置Geneve隧道的出接口。
绑定Geneve隧道到隧道接口
配置完成的Geneve隧道需要绑定到隧道接口上才能够生效。
注意:
l
在配置隧道接口绑定Geneve隧道时，需将隧道接口绑定在三层安全域。
l
Geneve隧道接口和出接口的MTU值需配置为1582及以上。
绑定Geneve隧道到隧道接口，在隧道接口配置模式下，使用以下命令：
tunnel geneve geneve-tunnel-name
l
geneve-tunnel-name – 指定将要绑定的Geneve隧道的名称。该隧道为系统中已创建的Geneve隧
道。
在隧道接口配置模式下，使用该命令no的形式取消Geneve隧道的绑定：
no tunnel geneve geneve-tunnel-name
显示Geneve隧道配置信息
在任何模式下，使用以下命令，显示Geneve隧道配置信息：
show tunnel geneve geneve-tunnel-name
例如：
hostname# show tunnel geneve geneve1
======================================================
Name   
Interface   
Peer   
Tunnel-if

<!-- 来源页 1763 -->
（隧道名称
出接口
目的IP地址
绑定的隧道接口）
-------------------------------------------------------------------
geneve1   
ethernet0/0   
192.168.1.197   
tunnel1
======================================================
后续操作
完成Geneve隧道配置后，需添加源接口路由条目，确保解封装后的明文流量能匹配路由并进入用于解封装
的Geneve隧道。
注意: 需确保配置路由时，所设置的下一跳地址，与绑定Geneve隧道的隧道接口处于同一网段，
否则明文流量无法正常匹配路由并进入Geneve隧道。
