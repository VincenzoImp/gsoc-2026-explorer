# Discussion #2773

**Parent:** Project Mesa — Project Ideas
**Source:** https://github.com/mesa/mesa/discussions/2773
**Scraped:** 2026-02-22T23:28:47.627104

---

# Mesa-LLM developpement (Colin's version) #2773

[colinfrisch](https://github.com/colinfrisch)started this conversation in

[Ideas](https://github.com/mesa/mesa/discussions/categories/ideas)

-

|
Hello everyone ! We can discuss here about the Mesa-LLM project that I'll be developing with My proposal, some more detailed code examples for the project as well as some refining that I did on the subject are available in my public The general idea to it is to build a derived LLMAgent(Agent) class, with three main attributes :
If you have a new topic of discussion on Mesa-LLM that you would want to explore, please feel free to create a new discussion in the |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

## Replies: 3 comments 8 replies

-

|
Hey, after a few discussions with |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

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
