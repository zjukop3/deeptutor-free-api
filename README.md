# DeepTutor-Free-API

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-green)
[![DeepTutor](https://img.shields.io/badge/Based%20on-DeepTutor-red)](https://github.com/HKUDS/DeepTutor)

## 📖 项目简介

**DeepTutor-Free-API** 是一个非官方的开源项目，旨在将 [DeepTutor](https://github.com/HKUDS/DeepTutor) 的强大辅导能力封装为 OpenAI 兼容的 API 接口。通过本项目，你可以使用任何支持 OpenAI API 格式的第三方客户端（如 ChatGPT-Next-Web, LobeChat 等）无缝接入 DeepTutor，享受终身个性化辅导服务。

### 🤔 为什么有这个项目？

[DeepTutor](https://github.com/HKUDS/DeepTutor) 是一个极优秀的终身个性化辅导系统。然而，原生项目主要面向命令行或独立部署，尚未直接提供标准的 OpenAI 兼容 API。为了让更多用户能够通过熟悉的客户端工具使用 DeepTutor，我们开发了此桥接项目。

### ✨ 特性

- 🚀 **OpenAI 兼容**：完全兼容 `/v1/chat/completions` 和 `/v1/models` 接口。
- 🔄 **流式响应**：支持 SSE 流式输出，打字机效果体验更佳。
- 🛠️ **简单易用**：几行命令即可启动服务，快速接入。
- 🧩 **解耦设计**：不修改 DeepTutor 原有逻辑，仅作为 API 层桥接。

### 📦 安装

```bash
git clone https://github.com/zjukop3/DeepTutor-Free-API.git
cd DeepTutor-Free-API
pip install -e .
```

### 🚀 快速上手

启动 API 服务：
```bash
uvicorn deeptutor_free_api.main:app --host 0.0.0.0 --port 8000
```

使用 `curl` 测试：
```bash
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deeptutor",
    "messages": [{"role": "user", "content": "解释一下量子纠缠"}],
    "stream": false
  }'
```

### 🔗 与主项目的关系

本项目是 [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) 的**生态补充**，并非官方项目。我们仅提供 API 封装层，核心辅导能力完全依赖于 DeepTutor。如果需要更深度的定制或了解底层原理，请访问主项目仓库。

### 🗺️ Roadmap

- [x] 基础 OpenAI 兼容接口
- [x] 流式响应支持
- [ ] 鉴权中间件
- [ ] 上下文持久化
- [ ] DeepTutor 后端真实调用逻辑完善

### 📄 License

本项目基于 [MIT License](LICENSE) 开源。

---

## 📖 Introduction

**DeepTutor-Free-API** is an unofficial open-source project designed to wrap the powerful tutoring capabilities of [DeepTutor](https://github.com/HKUDS/DeepTutor) into an OpenAI-compatible API. With this project, you can seamlessly connect to DeepTutor using any third-party client that supports the OpenAI API format (like ChatGPT-Next-Web, LobeChat, etc.) and enjoy lifelong personalized tutoring.

### 🤔 Why this project?

[DeepTutor](https://github.com/HKUDS/DeepTutor) is an excellent lifelong personalized tutoring system. However, the original project is primarily oriented towards CLI or standalone deployment and does not directly provide a standard OpenAI-compatible API. To allow more users to use DeepTutor through familiar client tools, we developed this bridge project.

### ✨ Features

- 🚀 **OpenAI Compatible**: Fully compatible with `/v1/chat/completions` and `/v1/models` endpoints.
- 🔄 **Streaming Response**: Supports SSE streaming output for a better typewriter experience.
- 🛠️ **Easy to Use**: Start the service with a few commands and integrate quickly.
- 🧩 **Decoupled Design**: Does not modify DeepTutor's original logic, acting only as an API bridge layer.

### 📦 Installation

```bash
git clone https://github.com/zjukop3/DeepTutor-Free-API.git
cd DeepTutor-Free-API
pip install -e .
```

### 🚀 Quick Start

Start the API server:
```bash
uvicorn deeptutor_free_api.main:app --host 0.0.0.0 --port 8000
```

Test with `curl`:
```bash
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deeptutor",
    "messages": [{"role": "user", "content": "Explain quantum entanglement"}],
    "stream": false
  }'
```

### 🔗 Relationship with the main project

This project is an **ecosystem supplement** to [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) and is not an official project. We only provide the API wrapper layer; the core tutoring capabilities rely entirely on DeepTutor. For deeper customization or to understand the underlying principles, please visit the main project repository.

### 🗺️ Roadmap

- [x] Basic OpenAI compatible interface
- [x] Streaming response support
- [ ] Authentication middleware
- [ ] Context persistence
- [ ] DeepTutor backend actual call logic implementation

### 📄 License

This project is licensed under the [MIT License](LICENSE).