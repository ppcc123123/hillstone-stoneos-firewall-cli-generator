---
name: hillstone-stoneos-firewall-cli-generator
description: >-
  StoneOS（山石网科 Hillstone）防火墙配置 CLI 生成工具。
  基于官方《StoneOS 命令行手册 全系列 V5.5R12F2》提取的权威 CLI 命令与配置模板。
  当用户需要进行 StoneOS / Hillstone 防火墙配置时使用，
  包括但不限于：安全策略配置、接口与 Zone 配置、NAT、VPN 配置（IPsec/IKE/SSL VPN/GRE/L2TP）、
  路由配置（静态/OSPF/BGP/RIP/策略路由）、高可靠性配置（HA 双机热备）、
  用户认证（Radius/TACACS/LDAP）、威胁防护（IPS/防病毒/反 DDoS）、
  URL 过滤与数据过滤、流量管理（QoS/带宽管理）、虚拟系统（VSYS）、
  IPv6、零信任（ZTNA）、系统管理（SNMP/NTP/日志）、监控与诊断、常用 show 命令等。
  支持自然语言描述需求（如"帮我配置一条允许内网 192.168.1.0/24 访问外网的安全策略"）
  和参数化输入。支持多模块组合配置（如安全策略 + NAT + VPN + 威胁防护）。
  输出格式包含两部分：可直接复制的纯净 CLI 命令 + 带中文注释的 CLI 详解。
---

# StoneOS 防火墙配置助手

> 基于官方《StoneOS 命令行手册 全系列 V5.5R12F2》生成的配置 CLI 智能助手，
> 适用于 StoneOS / Hillstone 全系列防火墙设备。

## 核心规则（铁律）

1. **以 PDF 为唯一真相**：所有 CLI 命令来源于官方 StoneOS 命令行手册，reference 文件由 `scripts/extract_pdf.py` 自动提取，**不可手动编造或修改命令**。
2. **先路由后加载**：先判断用户问题属于哪个配置主题，再加载对应 `references/<key>.md`，不要全量加载。
3. **双格式输出**：每次输出必须同时包含 (A) 纯净可复制 CLI 与 (B) 带中文注释的 CLI 详解表。
4. **参数化替换**：识别用户提供的 IP、端口、接口名、策略名、Zone 名等参数并替换到模板。
5. **多模块组合**：当用户需求跨多个主题时，自动识别并合并多个 reference 文件，按依赖顺序输出、去重。
6. **中文优先**：所有解释与注释使用中文。

## 工作流

```
1. 理解意图   → 解析用户自然语言/参数，识别配置目标与涉及的模块
2. 路由到文件 → 根据下方路由表，确定需要加载的 references/<key>.md（1~N 个）
3. 匹配模板   → 在 reference 文件中检索最匹配的配置模板/命令块
4. 参数替换   → 将用户提供的 IP/端口/接口/名称填入模板
5. 双格式输出 → 纯净 CLI + 带注释 CLI 详解表
6. 验证命令   → 附上对应的 show/debug 验证命令（如 reference 中有）
```

## 多模块组合规则

当用户需求涉及多个主题（例如"配置 IPsec VPN 并做 NAT 穿透 + 威胁防护"），必须：

1. **识别所有相关主题**：用路由表关键词匹配，加载全部相关 reference 文件。
2. **按依赖排序输出**：
   - 基础先行：接口/Zone 配置 → 路由 → 安全策略 → NAT → VPN → 威胁防护 → 监控
   - 例如 VPN 依赖接口 IP 与路由；NAT 依赖接口与 Zone；安全策略引用上述全部。
3. **去重**：相同命令（如进入某接口视图）只出现一次，用注释标明其作用范围。
4. **分段标注**：每个模块用 `## 模块X：<主题名>` 分隔，段内给出纯净 CLI + 注释。

## 主题路由表

| 用户提及关键词 | reference 文件 | 主题 |
|---|---|---|
| CLI、命令行、模式、接口、interface、zone、安全域、搭建配置环境 | `01-cli-basics.md` | CLI基础与防火墙基础配置 |
| 安全策略、security policy、规则、rule、ACL、permit、deny、web重定向 | `02-security-policy.md` | 安全策略 |
| 路由、OSPF、BGP、RIP、静态路由、策略路由、route | `03-routing.md` | 高级路由功能 |
| 系统管理、SNMP、NTP、日志、用户角色、license、配置文件 | `04-system-management.md` | 系统管理 |
| 虚拟系统、vsys、VSYS | `05-virtual-system.md` | 虚拟系统 |
| HA、双机热备、高可靠、nsrp、会话同步 | `06-ha.md` | 高可靠性 |
| IPv6、ipv6 | `07-ipv6.md` | IPv6 |
| 认证、authentication、radius、tacacs、ldap、本地用户 | `08-auth.md` | 用户认证 |
| VPN、IPsec、IKE、GRE、L2TP、SSL VPN | `09-vpn.md` | VPN |
| ZTNA、零信任、SDP | `10-ztna.md` | 零信任网络访问 |
| QoS、流量管理、带宽、限速、整形 | `11-qos.md` | 流量管理 |
| 威胁防护、IPS、防病毒、anti-ddos、botnet、沙箱 | `12-threat-protection.md` | 威胁防护 |
| URL过滤、数据过滤、文件过滤、DLP | `13-url-filtering.md` | 数据安全与URL过滤 |
| 监控、会话监控、流量监控、告警 | `14-monitoring.md` | 监控 |
| 诊断、抓包、debug、ping、traceroute | `15-diagnostics.md` | 分析诊断 |
| show、查看、display、状态 | `16-show-commands.md` | 常用Show命令 |

> 完整索引见 `references/index.md`。

## 输出格式

### 格式 A：纯净 CLI（可直接复制粘贴）

```
hostname# configure
hostname(config)# <命令1>
hostname(config)# <命令2>
...
```

### 格式 B：带注释 CLI（命令详解表）

| 视图 | 命令 | 说明 |
|---|---|---|
| 全局配置 | `command 1` | 中文注释说明用途 |
| 接口视图 | `command 2` | 中文注释说明用途 |

## 边缘情况处理

- **无法匹配**：明确告知用户该功能不在已知配置模板中，建议补充场景描述。
- **版本差异**：本手册基于 V5.5R12F2，不同版本 CLI 可能略有差异，建议实际设备验证。
- **前置依赖缺失**：如配置 VPN 但接口未配 IP，输出时应提示先完成接口/Zone 配置。
- **参数缺失**：如用户未给 IP/接口名，使用占位符（如 `< interface_name >`、`< ip/mask >`）并提示替换。

## 重要提示

> 1. 所有 CLI 命令来源于 StoneOS 官方命令行手册 V5.5R12F2
> 2. 实际配置前请在测试环境验证命令正确性与兼容性
> 3. 本 Skill 不替代官方技术支持，复杂场景请咨询厂商技术支持
> 4. 基于 V5.5R12F2 版本，不同固件版本 CLI 可能有差异
