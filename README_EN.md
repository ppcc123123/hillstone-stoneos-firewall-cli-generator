# StoneOS Firewall CLI Generator

> A firewall configuration CLI knowledge base generated from the official *StoneOS Command Line Interface Manual (Full Series, V5.5R12F2)*, suitable for use by any AI Agent.

[![Version](https://img.shields.io/badge/Version-V5.5R12F2-green)](https://www.hillstonenet.com)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

📖 中文版： [README.md](README.md)

## Introduction

This repository turns the official StoneOS (Hillstone Networks) firewall command-line manual into a structured configuration CLI knowledge base. Once loaded by any AI Agent, it can produce copy-pasteable firewall configuration CLI from user requests (natural language or parameterized), together with Chinese explanatory annotations.

## Key Features

- **Authoritative source**: All CLI commands are extracted from the official command-line manual — nothing is fabricated.
- **Dual-format output**: Clean copy-pasteable CLI + CLI with Chinese annotations.
- **Multi-module composition**: Automatically detects cross-topic requirements (e.g. security policy + NAT + VPN + threat protection) and merges them in dependency order.
- **Natural language + parameterized**: Supports both "configure a policy that allows the internal network to access the Internet" and explicit parameter input.
- **Full-series coverage**: Covers all StoneOS V5.5R12F2 capabilities.

## Configuration Topics Covered

| File | Topic | Content |
|---|---|---|
| `01-cli-basics.md` | CLI Basics & Firewall Basics | CLI interface, mode switching, physical interfaces, security zones (Zone) |
| `02-security-policy.md` | Security Policy | Policy rules, ACL, Web redirect |
| `03-routing.md` | Advanced Routing | Static / OSPF / BGP / RIP / Policy Routing |
| `04-system-management.md` | System Management | SNMP / NTP / Logging / User roles / License |
| `05-virtual-system.md` | Virtual System | VSYS configuration & resource allocation |
| `06-ha.md` | High Availability | HA active-standby, session synchronization |
| `07-ipv6.md` | IPv6 | IPv6 addressing / neighbor discovery / routing |
| `08-auth.md` | User Authentication | Local users / Radius / TACACS / LDAP |
| `09-vpn.md` | VPN | IPsec / IKE / GRE / L2TP / SSL VPN |
| `10-ztna.md` | Zero Trust Network Access (ZTNA) | ZTNA / SDP / access policy |
| `11-qos.md` | Traffic Management (QoS) | Bandwidth management / rate limiting / priority queues |
| `12-threat-protection.md` | Threat Protection | IPS / Anti-virus / Anti-DDoS / Botnet |
| `13-url-filtering.md` | Data Security & URL Filtering | URL filtering / data filtering / DLP |
| `14-monitoring.md` | Monitoring | Session / traffic monitoring, alerts |
| `15-diagnostics.md` | Analysis & Diagnostics | Ping / packet capture / Debug / diagnostics |
| `16-show-commands.md` | Common Show Commands | Commands for viewing configuration & runtime state |

## Directory Structure

```
hillstone-stoneos-firewall-cli-generator/
├── SKILL.md              # Skill entry (routing table + workflow + output template)
├── README.md             # Chinese documentation
├── README_EN.md          # English documentation
├── scripts/
│   ├── extract_pdf.py    # PDF text extraction script (single source of truth)
│   └── map.json          # Topic grouping mapping configuration
└── references/           # 16 topic reference files + index.md
    ├── index.md
    ├── 01-cli-basics.md
    └── ... (remaining topics)
```

## How It Works

1. `scripts/extract_pdf.py` reads the official PDF and `map.json`, extracts text per topic into `references/*.md`.
2. At runtime, the user's question keywords route to the corresponding reference file.
3. The closest configuration template is matched within the reference file and the user's parameters are substituted.
4. Dual-format configuration is produced: clean CLI + annotated explanation.

## Quick Start (Agent Usage Example)

```
Configure a security policy: allow traffic from the trust zone 192.168.1.0/24
to any address in the untrust zone, services http/https, action permit, with logging.
```

After loading this repository, the Agent outputs:

```
hostname# configure
hostname(config)# policy from trust to untrust
hostname(config-policy)# rule from 192.168.1.0/24 to any service http https permit log
```

along with the corresponding command annotations.

## Regenerating Reference Files

To re-extract from a newer manual version:

```bash
pip install PyMuPDF
python3 scripts/extract_pdf.py <newer_manual.pdf> --map scripts/map.json --output references/
```

## Disclaimer

- The content of this repository is extracted from the official public manual, for learning and research purposes only. If any content infringes copyright, please contact me and it will be removed promptly. Work email: jeffchenchen@foxmail.com.
- Verify command correctness and version compatibility in a test environment before applying to a live device.
- CLI may differ across firmware versions.
