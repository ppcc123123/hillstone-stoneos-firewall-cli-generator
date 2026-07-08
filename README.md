# StoneOS Firewall CLI Generator

> 基于官方《StoneOS 命令行手册 全系列 V5.5R12F2》生成的防火墙配置 CLI 知识库，适用于各类 AI Agent。

[![Version](https://img.shields.io/badge/Version-V5.5R12F2-green)](https://www.hillstonenet.com)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

📖 English version: [README_EN.md](README_EN.md)

## 项目简介

本仓库将 StoneOS（Hillstone 山石网科）防火墙官方命令行手册转化为结构化的配置 CLI 知识库。
任何 AI Agent 加载后，即可根据用户需求（自然语言或参数化）输出可直接粘贴执行的防火墙配置 CLI，
并附带中文注释说明。

## 核心特性

- **权威来源**：所有 CLI 命令提取自官方命令行手册，非编造
- **双格式输出**：纯净可复制 CLI + 带中文注释的 CLI 详解
- **多模块组合**：自动识别跨主题需求（如安全策略 + NAT + VPN + 威胁防护）并按依赖顺序合并输出
- **自然语言 + 参数化**：既支持"帮我配置一条允许内网访问外网的安全策略"，也支持具体参数输入
- **全系列覆盖**：覆盖 StoneOS V5.5R12F2 全系列能力

## 配置主题覆盖

| 文件 | 主题 | 内容 |
|---|---|---|
| `01-cli-basics.md` | CLI基础与防火墙基础配置 | 命令行接口、模式切换、接口、安全域(Zone) |
| `02-security-policy.md` | 安全策略 | 策略规则、ACL、Web重定向 |
| `03-routing.md` | 高级路由功能 | 静态/OSPF/BGP/RIP/策略路由 |
| `04-system-management.md` | 系统管理 | SNMP/NTP/日志/用户角色/License |
| `05-virtual-system.md` | 虚拟系统 | VSYS 配置与资源分配 |
| `06-ha.md` | 高可靠性 | HA 双机热备、会话同步 |
| `07-ipv6.md` | IPv6 | IPv6 地址/邻居发现/路由 |
| `08-auth.md` | 用户认证 | 本地用户/Radius/TACACS/LDAP |
| `09-vpn.md` | VPN | IPsec/IKE/GRE/L2TP/SSL VPN |
| `10-ztna.md` | 零信任网络访问 | ZTNA/SDP/访问策略 |
| `11-qos.md` | 流量管理 | 带宽管理/限速/优先级队列 |
| `12-threat-protection.md` | 威胁防护 | IPS/防病毒/反DDoS/Botnet |
| `13-url-filtering.md` | 数据安全与URL过滤 | URL过滤/数据过滤/DLP |
| `14-monitoring.md` | 监控 | 会话/流量监控、告警 |
| `15-diagnostics.md` | 分析诊断 | Ping/抓包/Debug/诊断 |
| `16-show-commands.md` | 常用Show命令 | 查看配置与运行状态的命令汇总 |

## 目录结构

```
hillstone-stoneos-firewall-cli-generator/
├── SKILL.md              # Skill 入口（路由表 + 工作流 + 输出模板）
├── README.md             # 中文文档
├── README_EN.md          # English documentation
├── scripts/
│   ├── extract_pdf.py    # PDF 文本提取脚本（来源唯一真相）
│   └── map.json          # 主题分组映射配置
└── references/           # 16 个主题参考文件 + index.md
    ├── index.md
    ├── 01-cli-basics.md
    └── ... (其余主题)
```

## 工作原理

1. `scripts/extract_pdf.py` 读取官方 PDF 与 `map.json`，按主题分页提取文本生成 `references/*.md`
2. 运行时根据用户问题中的关键词路由到对应参考文件
3. 在参考文件中匹配最贴近的配置模板，替换用户参数
4. 输出双格式配置：纯净 CLI + 带注释详解

## 快速开始（Agent 使用示例）

```
配置一条安全策略：允许 trust 安全域的 192.168.1.0/24 访问 untrust 安全域的任意地址，
服务为 http/https，动作为 permit，并记录日志
```

Agent 加载本仓库后，会输出：

```
hostname# configure
hostname(config)# policy from trust to untrust
hostname(config-policy)# rule from 192.168.1.0/24 to any service http https permit log
```

以及对应的命令注释说明。

## 重新生成参考文件

如需基于新版手册重新提取：

```bash
pip install PyMuPDF
python3 scripts/extract_pdf.py <新版手册.pdf> --map scripts/map.json --output references/
```

## 免责声明

- 本仓库内容提取自官方公开手册，仅供学习与研究使用，如有侵权，请主动与我联系，随时删除，工作邮箱：jeffchenchen@foxmail.com。
- 实际设备配置前请在测试环境验证命令正确性与版本兼容性。
- 不同固件版本 CLI 可能存在差异。
