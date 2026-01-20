# 日常与大模型的问题 / Daily LLM Questions

这个仓库用于记录、沉淀和演进我在**日常工作、思考与创作中**与大模型产生的所有问题、Prompt、实验和工作流。

目标不是"聊天记录"，而是：
- 可复用
- 可版本控制
- 可结构化演进

## 为什么不用浏览器？

浏览器里的对话：
- 不可复用
- 不可对比
- 不可沉淀为系统能力

编辑器里的交互：
- 是工程资产
- 是思考过程
- 是长期复利

## 目录说明

- `questions/`  
  日常真实问题，按时间沉淀，不追求"好看"，追求"真实"。

- `prompts/`  
  经过验证、可重复使用的 Prompt 模板。

- `experiments/`  
  所有失败、尝试、对比实验，都值得被记录。

- `workflows/`  
  我如何在写作、研究、编码中系统性使用大模型。

- `tools/`  
  用脚本把"提问"变成流程。

- `writings/`  
  使用 LLM 辅助创作的文档和深度内容。

## 使用方式

主要通过 VS Code / Cursor 进行：
- 直接编辑 Markdown
- 结合内置 LLM 或外部 API
- 将 AI 视为"协作对象"，而不是"问答工具"

## 目录结构

```
daily-llm-questions/
├─ README.md                # 项目说明
├─ questions/               # 日常问题沉淀
│  ├─ 2026-01.md
│  ├─ 2026-02.md
│  └─ index.md
├─ prompts/                 # 可复用 Prompt
│  ├─ thinking.md
│  ├─ writing.md
│  └─ coding.md
├─ experiments/             # 实验 / 尝试
│  ├─ rag.md
│  ├─ agent.md
│  └─ failures.md
├─ workflows/               # 你自己的 LLM 使用流程
│  ├─ daily.md
│  ├─ research.md
│  └─ writing.md
├─ writings/                # LLM 辅助创作的文档
│  ├─ 李飞飞与人工智能发展史.md
│  └─ README.md
├─ tools/                   # 脚本 & 工具
│  ├─ ask.py
│  └─ README.md
└─ .cursor/ or .vscode/     # 编辑器级交互（可选）
```

---

> This repo treats LLM interaction as **infrastructure**, not conversation.
