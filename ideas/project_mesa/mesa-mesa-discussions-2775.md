# Discussion #2775

**Parent:** Project Mesa — Project Ideas
**Source:** https://github.com/mesa/mesa/discussions/2775
**Scraped:** 2026-02-22T23:28:47.627163

---

-

|
Hello! After submitting my GSoC proposal I updated it slightly to include some other ideas I had, here is the link to the ## Mesa LLM Proposal Overview## Using the Mesa LLM Extension to Build LLM-Based Models in MesaLLM-based models in Mesa can broadly be envisioned under two categories: -
Where the agents converse with each other in natural language using LLMs
*Example: Modeling the spread of misinformation.* -
Where the LLMs sever purely as reasoning engines and are used just to generate logic and carry out the necessary tasks.
*Example: Modeling the spread of a disease in a city.*
There could, of course, be cases where we require a mix of these two categories, and that too can be accounted for under the proposed framework. ## Proposed Architecture
## Key Highlights- Abstractions for popular reasoning engines like ReAct, CoT, ToT, ReWoo, etc.
- Natural language communication between agents
- In-house memory unit for agents
- Facilitates interaction and communication between LLMAgents and the environment
(This is done primarily through the self.execute() method under LLMAgnet via tools that enable interaction between the agent and the environment. E.g. Tools that move the agent in the grid, or tools that change the value of the property layer of a cell that the agent is on.)
## The Reasoning Engine- Gives the user an option to define their own instance of the Reasoning Engine class
- Allows the user to import the logic for the Reasoning engine from another file
- Provides the user with pre-coded frameworks (CoT, ReAct, ReWoo etc)
There are three possible ways to pre-code the framework for in-context learning: - Utilize existing renditions from libraries like LangChain for popular frameworks like ReAct
- Implement complex architectures like ToT using tools such as LangGraph
- Employ prompt engineering for simpler architectures
The method of pre-coding will likely be determined through trial and error. Additionally, we could consider creating a Python registry to keep track of the different reasoning engines. ## ToolsLike in the reasoning engine, I would propose to maintain a registry for tools as well. We could create some built-in tools such as: -
For models that are dependent on the environment and get data from property layers, we could create a tool that converts the property layer into matrix form and passes it to the reasoning engine. *(Refer to the proposal extension for more clarity)* -
For agents falling under the conversational model, we could provide tools that retrieve particular conversations (or all conversations) and pass them into the reasoning engine if it needs context before taking action. (For instance, in relation to the sales model I had mentioned in my proposal, the prompt could be as follows: ”Decide if you want to buy product A or product B” For this, the agent might use this tool to go through all the conversations it had with the salespeople and then come to a decision.)
## ConversationFor conversational models where LLM agents communicate in natural language: -
In case we are working with conversational models, where the LLM agents will be communicating in natural language to each other, we must toggle the conversation attribute of the model to on. This will create a pandas data frame (or polars, but I don’t think that would be necessary). -
Now each time, an agent wants to converse with another agent, they can do so using a method resembling the following line:
`A.converse([B, C], my_hugging_face_mistral_generator, "start a sales pitch for...")` Here I am giving flexibility to the user in terms of the reasoning engine they want to use to generate the conversation. If they don’t mention anything, we will use the default engine (which is the engine mentioned in the self.reasoning_engine). This method will automatically log the conversation into the database and also, If A B C are engaging in a to and fro communication, it will add those dialogues into the prompt so that there is a proper flow in the conversation.(look into proposal extension for more details about this class method) ## Implementing the Disaster Response SimulationProblem statement: There are 10 fire fighters, all initially located in their headquarters. A fire of different intensities breaks out in their city. The property layer depicts the intensity of the fire. Observe how the agents might put out the fire in the best possible way. This is a matrix representation of the property layer. 0→ No danger 1→ Small fire [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, $, 0, 2, 0], [0, 1, 1, 1, 0, 0, 0, 0, 2, 2], [0, 0, 0, 0, 0, 0, 0, 2, 2, 2], [0, 0, 0, 0, 0, 0, 0, 2, 2, 2], [0, 0, 0, 0, 0, 0, 0, 2, 2, 0], [0, 0, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ] Step 1: Create an instance of the tool class that allows the agent to move around the grid |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

## Replies: 2 comments 2 replies

-

|
Posting in both discussions and this may be too late... but is there any thought to 1 project integrating LLMs into models and another building a custom Mesa LLM (available via the docs?) that addresses the Mesa 2 issue? Or maybe even an agent AI that integrates the chatbot with tests so at some interval it checks and improves its responses or users have the option to have it run tests when they want more detailed responses? |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I'm Selcuk Senturk, MSc Computer Science student and an AI/ML Engineer at IBM Expert Labs. I came across this discussion while researching Mesa-LLM for GSoC 2026 and wanted to introduce myself. The architecture from both proposals resonates directly with work I do: at IBM I build production multi-agent systems using PydanticAI and LangGraph for LLM agent application development, and also at Kastas I built multi-agent pipelines with PydanticAI and LangGraph covering tool integration, memory management, prompt engineering, and async execution across agents. I've worked with OpenAI, Anthropic, and HuggingFace APIs as well as local inference setups. For GSoC 2026 I'm interested in the stabilization track, improving tool modularization, test coverage, memory handling reliability, and Ollama/local inference support, while contributing example models from real multi-agent use cases. I would like to discuss further if I'm a good candidate for GSoC 2026 and how I plan to implement these above. Resume: |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)
