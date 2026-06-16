AI Personal Assistant:
基于 Agent 的私人 AI 助理，支持知识库问答和多种工具调用。

功能:
知识库管理：创建/删除知识库，上传文档（txt, pdf, docx, md, py, json, csv），自动分块、向量化（bge-large-zh + FAISS），支持混合检索（BM25 + FAISS）
对话 Agent：集成天气查询、网络搜索（百度）、代码解释器、时间获取、知识库检索，基于 LangChain ReAct 模式
代码解释器：执行 Python 代码，支持 matplotlib 等库的绘图，自动返回图片
双库存储：FAISS 向量库管理文档嵌入与检索，SQLite 关系库管理知识库元信息（名称、描述等）
Web 界面：Gradio 聊天界面，支持文件上传和流式对话
大模型：Qwen/Qwen2.5-72B-Instruct（通过 SiliconFlow API 调用）

安装:
pip install -r requirements.txt

配置:
需要设置以下环境变量（创建 .env 文件）：

SILICONFLOW_API_KEY：用于调用 Qwen 大模型
SENIVERSE_API_KEY：用于心知天气
SERPAPI_API_KEY：用于百度搜索

运行:
启动后端 API：
python app_server.py
启动 Web 界面（另一个终端）：
python webui.py
依赖:
见 requirements.txt
