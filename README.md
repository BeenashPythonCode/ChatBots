# RAG Real-Time Answering Chatbot

A real-time AI chatbot powered by **Retrieval-Augmented Generation (RAG)** that combines local LLM inference with live web search to provide accurate, up-to-date answers.

## Features

- 🤖 **Local LLM**: Uses Ollama with LLaMA 3.2 for privacy-preserving inference
- 🔍 **Real-Time Search**: Fetches current information from the web via DuckDuckGo
- ⚡ **RAG Architecture**: Augments LLM responses with relevant search results
- 💬 **Interactive CLI**: Simple command-line interface for real-time conversations
- 🔐 **No API Keys**: Runs locally without relying on external API keys

## Architecture

The chatbot implements a Retrieval-Augmented Generation (RAG) pipeline:

1. **User Question** → Sent to the RAG chain
2. **Web Search** → DuckDuckGo fetches real-time search results
3. **Context Augmentation** → Search results are embedded into the prompt
4. **LLM Response** → Local LLaMA 3.2 model generates answers based on context
5. **Output** → User receives grounded, current answer

## Prerequisites

### System Requirements
- Python 3.8+
- 8GB+ RAM (for running Ollama locally)
- Ollama installed and running ([Download Ollama](https://ollama.ai))

### Ollama Setup
1. Download and install Ollama from [ollama.ai](https://ollama.ai)
2. Pull the LLaMA 3.2 model:
   ```bash
   ollama pull llama3.2:latest
   ```
3. Start the Ollama server:
   ```bash
   ollama serve
   ```
   (Ollama typically runs on `http://localhost:11434`)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/RAG_real_time_answering_chat_bot.git
   cd RAG_real_time_answering_chat_bot
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Ensure Ollama is running**
   ```bash
   ollama serve
   ```
   (Keep this running in a separate terminal)

2. **Run the chatbot**
   ```bash
   python chat_assistance.py
   ```

3. **Interact with the bot**
   ```
   Hello! I am a real_time AI assistant. What's new?
   You: What are the latest AI developments in 2024?
   Thinking...
   [Bot responds with current information from search results]
   ```

4. **Exit the chatbot**
   - Type `exit` or `quit` to end the conversation

## Dependencies

- **langchain** - LLM orchestration framework
- **langchain_community** - Community integrations (DuckDuckGo search)
- **langchain_ollama** - Ollama integration for LangChain
- **duckduckgo-search** - Real-time web search engine

See `requirements.txt` for specific versions.

## How It Works

### RAG Chain Flow
```
User Input (Question)
        ↓
  [RunnablePassthrough]
        ↓
    [Search Tool] → DuckDuckGo Results
        ↓
  [Prompt Template] → Inject context
        ↓
  [LLM Model] → LLaMA 3.2 Inference
        ↓
    Output (Answer)
```

### Prompt Strategy
The bot uses a grounded prompt that:
- Explicitly instructs the LLM to answer based only on search results
- Prevents hallucination by returning "I could not find any information on that." when needed
- Maintains context across multiple conversation turns

## Configuration

You can modify the following in `chat_assistance.py`:

- **LLM Model**: Change `"llama3.2:latest"` to other Ollama models
- **Prompt Template**: Edit the system prompt to customize bot behavior
- **Search Tool**: Replace `DuckDuckGoSearchRun()` with other search providers

## Examples

### Example 1: Current Events
```
You: What happened in the latest tech news?
Thinking...
[Bot searches and returns latest tech news]
```

### Example 2: Factual Questions
```
You: What is the capital of France?
Thinking...
[Bot provides accurate answer with sources]
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Connection refused error** | Ensure Ollama is running (`ollama serve`) in another terminal |
| **Model not found** | Run `ollama pull llama3.2:latest` |
| **High latency** | Reduce model complexity or increase system resources |
| **No search results** | Check internet connection and DuckDuckGo availability |

## Limitations

- Requires Ollama server running locally
- Search quality depends on DuckDuckGo's results
- Longer responses may take time on lower-end hardware
- Works best with factual, recent queries

## Future Enhancements

- [ ] Support for multiple LLM models
- [ ] Persistent conversation history
- [ ] Web UI interface
- [ ] Custom knowledge base integration
- [ ] Response caching
- [ ] Source attribution in responses

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Built with ❤️ using LangChain, Ollama, and DuckDuckGo**
