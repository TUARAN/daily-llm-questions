#!/usr/bin/env python3
"""
简单的 LLM 提问工具
用法: python ask.py "你的问题"
"""

import sys
import os
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("用法: python ask.py '你的问题'")
        sys.exit(1)
    
    question = " ".join(sys.argv[1:])
    
    print(f"\n问题: {question}\n")
    print("=" * 50)
    print("注意：这个工具目前是一个框架。")
    print("你需要集成具体的 LLM API（OpenAI、Anthropic 等）")
    print("=" * 50)
    
    # TODO: 集成 LLM API
    # - OpenAI API
    # - Anthropic API
    # - 本地模型
    
    answer = "[在这里集成 LLM 响应]"
    
    # 记录到文件
    save_to_file(question, answer)
    
    print(f"\n答案: {answer}\n")
    print(f"已保存到 questions/{datetime.now().strftime('%Y-%m')}.md")

def save_to_file(question, answer):
    """将问答记录到对应月份的文件"""
    now = datetime.now()
    month_file = f"../questions/{now.strftime('%Y-%m')}.md"
    
    # 确保目录存在
    os.makedirs(os.path.dirname(month_file), exist_ok=True)
    
    # 如果文件不存在，创建头部
    if not os.path.exists(month_file):
        with open(month_file, 'w', encoding='utf-8') as f:
            f.write(f"# {now.strftime('%Y年%m月')}问题记录\n\n")
    
    # 追加问答
    with open(month_file, 'a', encoding='utf-8') as f:
        f.write(f"## {now.strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"**问题：** {question}\n\n")
        f.write(f"**回答：**\n{answer}\n\n")
        f.write("---\n\n")

if __name__ == "__main__":
    main()
