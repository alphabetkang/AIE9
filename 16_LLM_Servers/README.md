

## # Session 16: LLM Servers


| 📰 Session Sheet                                        | ⏺️ Recording                                                                                                                                           | 🖼️ Slides                                                                                                                                                                         | 👨‍💻 Repo    | 📝 Homework                                                                                                                                 | 📁 Feedback                                         |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [LLM Servers](../00_Docs/Session_Sheets/16_LLM_Servers) | [Recording!](https://us02web.zoom.us/rec/share/HDunij9p7eCXeP_OgsRDRjTdWUqiEhDBGWrFJEn1bwWR1wz1jKX6EHXSOM45d0sC.rHiyo_znZ-R8Jh6S) passcode: `D80X^YjL` | [Session 16 Slides](https://www.canva.com/design/DAG-EBu7B5A/POcowC5rDLENSPcSVpbf8g/edit?utm_content=DAG-EBu7B5A&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 16 Assignment: LLM Servers](https://forms.gle/Riqvwf6KrZcCRKV86) [Demo Day Submission (3/12)](https://forms.gle/7xyuBUn69GX4v6K98) | [Feedback 3/5](https://forms.gle/W28QFWJXpSS4ZAR6A) |


**⚠️!!! PLEASE BE SURE TO SHUTDOWN YOUR DEDICATED ENDPOINT ON FIREWORKS AI WHEN YOU'RE FINISHED YOUR ASSIGNMENT !!!⚠️**

# Build 🏗️

In today's assignment, we'll be creating Fireworks AI endpoints, and then building a RAG application.

- 🤝 Breakout Room #1
  - Set-up Open Source Endpoint (Instructions [here](./ENDPOINT_SETUP.md)) ((This process may take 15-20min.))
  - Test Endpoint and Embeddings with the `endpoint_slammer.ipynb` notebook.
- 🤝 Breakout Room #2
  - Use the Open Source Endpoints to build a RAG LangGraph application

# Ship 🚢

The completed notebook and your RAG app/notebook!

### Deliverables

- A short Loom of either:
  - the notebook and the RAG application you built for the Main Homework Assignment; or
  - the notebook you created for the Advanced Build

# Share 🚀

Make a social media post about your final application!

### Deliverables

- Make a post on any social media platform about what you built!

Here's a template to get you started:

```
🚀 Exciting News! 🚀

I am thrilled to announce that I have just built and shipped a RAG application powered by open-source endpoints! 🎉🤖

🔍 Three Key Takeaways:
1️⃣
2️⃣
3️⃣

Let's continue pushing the boundaries of what's possible in the world of AI and question-answering. Here's to many more innovations! 🚀
Shout out to @AIMakerspace !

#LangChain #QuestionAnswering #RetrievalAugmented #Innovation #AI #TechMilestone

Feel free to reach out if you're curious or would like to collaborate on similar projects! 🤝🔥
```

# Submitting You Homework [OPTIONAL]

## Main Homework Assignment

Follow these steps to prepare and submit your homework assignment:

1. Follow the instructions in `ENDPOINT_SETUP.md`
2. Replace both `model` values in `endpoint_slammer.ipynb` with the `gpt-oss` endpoint you created in Step 1
3. Run the code cells in `endpoint_slammer.ipynb`
4. Respond to the questions in the section below
5. Build a sample RAG
6. Record a Loom video reviewing what you have learned from this session

**⚠️!!! PLEASE BE SURE TO SHUTDOWN YOUR DEDICATED ENDPOINT ON FIREWORKS AI WHEN YOU HAVE FINISHED YOUR ASSIGNMENT !!!⚠️**

## Questions

### ❓ Question #1:

What is the difference between serverless and dedicated endpoints?

#### ✅ Answer:

Serverless endpoints  typically mean that the underlying resources driving that endpoint are shared with other serverless endpoints. This means that a set amount of compute isn't necessarily set apart at all times for this enpoint. Rather, a certain amount of compute and resources is carved out for the endpoint at runtime when the resources are requested. This is useful if the client doesn't want to be paying for resources that they aren't using and don't need around the clock. 

On the other hand, dedicated endpoints carve out a specific amount of compute and resources on a guaranteed basis. This is useful if the client is building an application that they know will require a certain amount of dedicated compute at all times. 

### ❓ Question #2:

Why is it important to consider token throughput and latency when choosing an LLM for user-facing applications?

#### ✅ Answer:

Token throughput and latency are important when choosing an LLM for user-facing applications because they directly affect the user experience when interacting with the application. Slow responses from the LLM degrade the experience and make it feel more clunky, whereas tight response-times from the LLM make the user feel that the application is alive and ready to handle their requests. LLM applications are distnct from regular software applications in that they provide natural language as an interface for requesting and receiving services from the application. This means that just as humans expect responsiveness from other humans when requesting services, they also expect the same from human-like LLM service apps. Responsiveness is directly impacted by token throughput and latency, so these metrics are important to consider when choosing LLMs to serve the applications.

## Activity 1: RAGAS Evaluation with Cost Analysis

Use RAGAS to evaluate your open-source Fireworks AI powered RAG app against an OpenAI `gpt-4.1-mini` powered equivalent. Compare retrieval quality, answer faithfulness, and end-to-end accuracy across both providers.

Additionally, instrument both pipelines with **LangSmith** to capture token usage and cost per query. Use LangSmith's tracing and cost dashboards to compare the total cost of running each provider at scale. Include your evaluation results, cost breakdown, and analysis in your Loom video.

## Advanced Activity: Local Models

Swap out the Fireworks AI endpoints for **locally-running open-source models** using [Ollama](https://ollama.com/) or another local inference server of your choice. Run both your embedding model and your chat model locally, and rebuild the RAG pipeline on top of them.

- Compare quality and latency between the local setup and your Fireworks AI hosted endpoint.
- Reflect: what are the trade-offs of local models vs. managed endpoints in a production setting?

Include your findings and a demo in your Loom video.