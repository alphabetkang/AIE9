

## # Session 17: Model Context Protocol (MCP) & Agent-to-Agent (A2A) Protocol


| Session Sheet                                                         | Recording                                                                                                                                             | Slides                                                                                                                                                                             | Repo          | Homework                                                                                   | Feedback                                             |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| [MCP Servers & A2A](../00_Docs/Session_Sheets/17_MCP_Servers_and_A2A) | [Recording!](https://us02web.zoom.us/rec/share/_iJT-kZiYacyz23fjU3N7w7mZIUFJqGXV48RDqCkCY3avsmngKtzK0SNs0I7k74.xICq6NSv6l6GqAFU) passcode: `fJ9tx4h.` | [Session 17 Slides](https://www.canva.com/design/DAG-ELapG4g/6vDMm63RBwKVsSZvheorVA/edit?utm_content=DAG-ELapG4g&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [(Optional) Session 17 Assignment: MCP Servers & A2A](https://forms.gle/qtjQFfoEF8aykTWy5) | [Feedback 3/12](https://forms.gle/sJwD1a6LLn9NU9s48) |


---

## 📚 Useful Resources

**MCP (Model Context Protocol)**

- [MCP Official Docs](https://modelcontextprotocol.io/) — Spec, tutorials, and guides
- [MCP-UI](https://mcpui.dev/) — Official standard for interactive UI in MCP
- [MCP Auth Guide (Auth0)](https://auth0.com/blog/mcp-specs-update-all-about-auth/) — Deep dive into MCP auth spec updates

**A2A (Agent-to-Agent Protocol)**

- [A2A Official Docs](https://a2a-protocol.org/latest/) — Spec and guides
- [A2A GitHub Repo](https://github.com/a2aproject/A2A) — Protocol spec and implementations
- [Announcing A2A (Google Blog)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) — Protocol vision and motivation

**MCP vs A2A**

- [A2A and MCP (Official)](https://a2a-protocol.org/latest/topics/a2a-and-mcp/) — How they complement each other

---

# Running the MCP Server

### 1. Install dependencies

```bash
uv sync
```

### 2. Set up environment variables

Copy the example env file and fill in your OpenAI API key:

```bash
cp .env.example .env
```

### 3. Run the MCP server locally

```bash
uv run server.py
```

The server will start on `http://localhost:8000`.

### 4. Expose the server with ngrok (for remote/Claude Desktop access)

In a separate terminal, start an ngrok tunnel:

```bash
ngrok http 8000
```

Copy the ngrok forwarding URL (e.g. `https://xxxx-xx-xx-xx-xx.ngrok-free.app`) and restart the server with it:

```bash
ISSUER_URL=https://xxxx-xx-xx-xx-xx.ngrok-free.app uv run server.py
```

> **Note:** The `ISSUER_URL` must match the public URL clients use to reach the server, otherwise OAuth authentication will fail.

---

# Build 🏗️

In today's assignment, we'll be building an MCP server with OAuth authentication — a cat shop application that exposes tools for browsing products, managing a cart, and checking out.

- 🤝 Breakout Room #1
  - Set up the MCP server with OAuth and the product database
  - Explore the MCP tools: `list_products`, `get_product`, `add_to_cart`, `view_cart`, `remove_from_cart`, `checkout`
- 🤝 Breakout Room #2
  - Connect an MCP client to the server
  - Build an end-to-end interaction flow using the MCP tools

# Ship 🚢

The completed MCP server and client integration!

### Deliverables

- A short Loom of either:
  - the MCP server you built and a demo of the client interacting with it; or
  - the notebook you created for the Advanced Build

# Share 🚀

Make a social media post about your final application!

### Deliverables

- Make a post on any social media platform about what you built!

Here's a template to get you started:

```
🚀 Exciting News! 🚀

I am thrilled to announce that I have just built and shipped an MCP server with OAuth authentication! 🎉🤖

🔍 Three Key Takeaways:
1️⃣
2️⃣
3️⃣

Let's continue pushing the boundaries of what's possible in the world of AI and tool integration. Here's to many more innovations! 🚀
Shout out to @AIMakerspace !

#MCP #ModelContextProtocol #OAuth #Innovation #AI #TechMilestone

Feel free to reach out if you're curious or would like to collaborate on similar projects! 🤝🔥
```

# Submitting Your Homework [OPTIONAL]

## Main Homework Assignment

Follow these steps to prepare and submit your homework assignment:

1. Review the MCP server code in `server.py` and the `app/` directory
2. Run the MCP server locally using `uv run server.py`
3. Connect to the server using an MCP client (e.g., Claude Desktop, or a custom client)
4. Test all available tools: browsing products, adding to cart, viewing cart, removing items, and checkout
5. Record a Loom video reviewing what you have learned from this session

## Questions

### ❓ Question #1:

Why is OAuth important for MCP servers, and what security considerations should you keep in mind when exposing tools to AI clients?

#### ✅ Answer:

OAuth is important for MCP servers just like it is for any other software application in that it provides a way for applications to implement authorization and authentication as security measures. For example, in the old days, people could use a simple username and password combination to log into an application. The problem was that access to this one combination of username and password would grant immediate access to the application to any number of hackers who had the credentials. With OAuth in MCP, a token meant to be used by one service cannot be misues by another. MCP clients now implement Resource Indicators which state the intended recipient of the access token, meaning that even if the access token is stolen, the metada associated with that token would flag the access token as 'mis-redeemed' by a fradulent recipient. 

Overall, AI clients create a new class of security concerns because LLMs are capable of reading, writing and manipulating text files and code dynamically and unpredictably. It is imperative that AI applications and MCP servers enforce security flows that take into account these dynamic capabilities. Leveraging metadata is a powerful way to guide application and security flow behavior as metadata sits on top of business logic code that LLMs typically run. 

### ❓ Question #2:

What is the Agent-to-Agent (A2A) protocol, and how does it differ from MCP in terms of purpose and architecture? When would you choose A2A over MCP?

#### ✅ Answer:

A2A is an open standard (like REST and MCP) that defines how agents can interact with other agents! In an era where all sorts of people are developing their own agents for all sorts of purposes, it is usefl to have an agreed-upon way for agents to communicate with one another. A2A facilitates this communication while focusing on the following: Interoperability: communication standards that allow cross-platform functionality; Complex Workflows: ability for multiple agents to work together to achieve a larger task; and Security and Opactiy: Agent-to-agent communication that doesn't require sharing of internal memroy, tools or proprietary logic. 

A2A focuses on agent-to-agent communication, while MCP focuses on agent-to-tool communication. This means that architecturally, developers would implement A2A for their agents to communicate with agents from other organizations and implement MCP to connect tools to their agents within their own organizations. In other words, A2A can be thought of more as an 'external' interface to outside agents while MCP is a standard for 'internal' interfaces to tools necessary for the agent to do its job. 

## Activity 1: Extend the MCP Server

Add at least one new tool to the cat shop MCP server (e.g., `search_products`, `update_cart_quantity`, or `get_order_history`). Ensure the new tool integrates properly with the existing database and OAuth authentication. Demo the new tool through an MCP client and include it in your Loom video.

## Advanced Activity: Build a Custom MCP Client

Build a custom MCP client that connects to the cat shop server over Streamable HTTP, authenticates via OAuth, and orchestrates a multi-step shopping flow (browse → add to cart → checkout). Compare the developer experience of MCP-based tool integration vs. traditional REST API calls.

Include your findings and a demo in your Loom video.