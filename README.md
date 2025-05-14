[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/tolios-connect4-mcp-badge.png)](https://mseep.ai/app/tolios-connect4-mcp)

# MCP CONNECT 4

While people use MCP to build powerful connections with various tools like db's or the web
one can imagine a great and perhaps more advanced interaction between user and assistant,
would be to play a game. So I say why not. Let's play games!

This is the premise behind this repo. Also its fun!

MCP Connect 4 offers structure to the state of the game. The assistant plays the move it believes
and also plays your move. (this might be a criticism)

## How to use

Simply clone the repo and add the following to the json config of claude (or massage similarly for other clients) this:

```json
{
    "connect4": {
      "command": "absolute path to uv",
      "args": [
        "--directory",
        "absolute path to this repo",
        "run",
        "main.py"
      ]
    }
}
```

Currently one can view the board by seeing the tool call from the chat of the LLM provider (should do better)...
