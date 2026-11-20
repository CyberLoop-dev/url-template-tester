<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=145&section=header&text=URL%20Template%20Tester&fontColor=ffffff&fontSize=34" alt="Animated header"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=900&center=true&vCenter=true&width=620&lines=URL%20Template%20Tester;Expand%20URI%20templates%20safely" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/url-template-tester?label=MIT)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/url-template-tester)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/url-template-tester?style=social)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/url-template-tester)

<img src="./assets/mark.svg" width="145" alt="Custom SVG illustration"/>

**Expand practical URI templates with safe percent-encoding and local JSON variables.**

</div>

## ✨ Overview

A small local RFC 6570-inspired workbench for simple, reserved, and query expansion. It never fetches the expanded URL.

## 🚀 Features

- 🔗 Supports simple, reserved, query, and query-continuation operators.
- 🔐 Percent-encodes variable values with operator-specific rules.
- 🧩 Accepts JSON variables from the command line.
- ⚠️ Rejects unsupported expressions and non-scalar values.

## 🧪 Demo

```bash
python main.py '/users/{name}{?page}' --vars '{"name":"Ada Lovelace","page":2}'
```

## ⚡ Quick Start

```bash
git clone https://github.com/CyberLoop-dev/url-template-tester.git
cd url-template-tester
python main.py '/search{?q,page}' --vars '{"q":"hello world","page":2}'
```

## 🧰 Tech Stack

Python 3.10+ · urllib.parse · Standard library only.

## 🗂️ Folder Structure

```text
url-template-tester/
├── main.py
├── tests/test_main.py
├── requirements.txt
├── .github/workflows/tests.yml
└── assets/mark.svg
```

## 🗺️ Roadmap

- [x] Simple, reserved, and query expansion
- [x] Unit tests and CI
- [ ] Prefix modifiers and exploded lists
- [ ] Interactive browser playground

## 🤝 Contributing

Add RFC examples with expected expansions. Keep unsupported syntax explicit rather than approximating it.

## 📄 License

MIT — see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated footer"/></div>
