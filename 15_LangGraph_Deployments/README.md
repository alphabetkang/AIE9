## # Session 15: Build & Serve Agentic Graphs with LangGraph


| 📰 Session Sheet                                                                                          | ⏺️ Recording                                                                                                                                          | 🖼️ Slides                                                                                                                                                                         | 👨‍💻 Repo    | 📝 Homework                                                                 | 📁 Feedback                                         |
| --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------- | --------------------------------------------------- |
| [Agent Servers](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Session_Sheets/15_Agent_Servers) | [Recording!](https://us02web.zoom.us/rec/share/lORjByDju6fv4TdE3r93dorY3aNgmSKL_Qk_cX_AMcCQ6cNfSW77unaA1LMVV60.OcI8uEnfVmRAgjSn) passcode: `Dc@&pv1T` | [Session 15 Slides](https://www.canva.com/design/DAG-EJqkRaM/FR3WG_yMA5_BqbWpQlHR9g/edit?utm_content=DAG-EJqkRaM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 15 Assignment: Agent Servers](https://forms.gle/Vb3HNDsyVPQ1jqKX7) | [Feedback 3/3](https://forms.gle/kYmhbVUEMog16mKv8) |


### Prerequisites

Before starting, ensure you have the following:

- **Python 3.11+** installed
- An **OpenAI API Key**
- A **Tavily API Key**
- (Optional) **LangSmith** credentials for tracing

Create a `.env` file in this directory with your API keys:

1. Run `uv sync` to install dependencies.

# Build 🏗️

Run the repository and complete the following:

- 🤝 Breakout Room Part #1 — Building and serving your LangGraph Agent Graph
  - Task 1: Getting Dependencies & Environment
    - Configure `.env` (OpenAI, Tavily, optional LangSmith)
  - Task 2: Serve the Graph Locally
    - `uv run langgraph dev` (API on [http://localhost:2024](http://localhost:2024))
  - Task 3: Call the API from a different terminal
    - `uv run test_served_graph.py` (sync SDK example)
  - Task 4: Explore assistants (from `langgraph.json`)
    - `agent` → `simple_agent` (tool-using agent)
    - `agent_helpful` → `agent_with_helpfulness` (separate helpfulness node)
- 🤝 Breakout Room Part #2 — Using LangSmith Studio to visualize the graph
  - Task 1: Open Studio while the server is running
    - [https://smith.langchain.com/studio?baseUrl=http://localhost:2024](https://smith.langchain.com/studio?baseUrl=http://localhost:2024)
  - Task 2: Visualize & Stream
    - Start a run and observe node-by-node updates
  - Task 3: Compare Flows
    - Contrast `agent` vs `agent_helpful` (tool calls vs helpfulness decision)

🚧 Advanced Build 🚧 (OPTIONAL - *open this section for the requirements*)

> NOTE: This can be done in place of the Main Assignment

- Create and deploy a locally hosted MCP server with FastMCP.
- Extend your tools in `tools.py` to allow your LangGraph to consume the MCP Server.

When submitting, provide:

- Your Loom video link demonstrating the MCP server integration
- The GitHub URL to your completed Advanced Build

Have fun!

### Questions & Activities

#### Question 1:

What is the key architectural difference between the `simple_agent` and `agent_with_helpfulness` graphs? Specifically, explain how the helpfulness evaluation loop works and what mechanisms are in place to prevent it from running indefinitely.

##### Answer: 

The key architectural difference between `simple_agent` and `agent_with_helpfulness` graphs is that the latter includes two addition nodes in the graph:`route_to_action_or_helpfulness` and `helpfulness_decision`. After the agent has been called, the `route_to_action_or_helpfulness` node evaluates whether a tool call is loaded for the agent. If it is, the router passes the computation to the `tool_node`; if not, the `helpfulness_decision` node is called. Here, the agent evaluates whether the answer it has produced is 'helpful' or not and gives a yes-or-no answer. If the answer has been evaluated as helpful, the loop ends. If not, the computation enters the loop again and the agent is called once more. 

Overall, these two nodes transform the `simple_agent` to an agent that evaluates the helpfulness of its output to the user. By adding this extra check on helpfulness, it increases the quality of the output to the user and improves the user's experience with the app. It is a simple use of the `LLM-as-judge` paradigm, which leverages agentic reasoning for the purpose of improving the output provided by the agentic app. 

#### Question 2:

What is the role of `langgraph.json` in the LangGraph Deployments? Describe each of its key fields and how the platform uses this file to discover and serve your graphs.

##### Answer:

The `langgraph.json` file is a configuration file used by the LangSmith framework to define and instantiate agentic graphs for the application and define other application-level variables such as dependencies on packages and environmental variables. It is necessary to include this file for deploying an application with LangSmith Deployment. The following are descriptions of the keys in the `langgraph.json` file included in this application: 

`version`: The version number of this LangGraph application configuration
`dependencies`: Dependencies on other Python packages
`env`: The filepath of the file containing environmental variables
`python_version`: Python version required to run this app
`graphs`: Filepaths of the code that defines the graphs used by this app
`simple_agent` / `agent_with_helpfulness`: Specified filepaths and variable name for different graphs
`assistants`: Contains filepaths for assistants 
`agent`: Contains fields for one assistant
`graph_id`: The id of the assistant
`name`: The name of the assistant 
`description`: The description of the assistant

#### Activity #1:

Create your own agent graph! Build a new graph in `app/graphs/` with a custom evaluation node (e.g., a vibe checker, a fact verifier, a summarizer — get creative!). Register it in `langgraph.json`, serve it with `uv run langgraph dev`

##### Answer:

# Ship 🚢

- The completed notebook.
- 5min. Loom Video

# Share 🚀

- Walk through your notebook and explain what you've completed in the Loom video
- Make a social media post about your final application and tag @AIMakerspace
- Share 3 lessons learned
- Share 3 lessons not learned

# Submitting Your Homework

### Main Homework Assignment

Follow these steps to prepare and submit your homework:

1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
  - *(You should have completed this process already.)* For your initial repo setup, see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `15_LangGraph_Platform` folder (you can also use the *File -> Open Folder* menu option of an existing Cursor window)
3. Answer Questions 1 - 2 using the `##### Answer:` markdown cell below them in the README
4. Complete Activity #1 in the README
5. Add, commit and push your modified files to your GitHub repository.

When submitting your homework, provide:

- Your Loom video link
- The GitHub URL to the `15_LangGraph_Platform` folder on your assignment branch

