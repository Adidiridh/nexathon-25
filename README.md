Topic name - Ai agents - Ai agents in finance , 🤖 What is AI? AI (Artificial Intelligence) is a branch of computer science that enables machines to:-

.Think, learn, and solve problems like humans.

.Use data to predict, analyze, or generate content.

Examples of AI:

. ChatGPT answering your questions

. Google Maps predicting traffic

. Netflix recommending shows

🧠 What are AI Agents? . An AI agent is an autonomous software entity that:-

. Perceives its environment

. Makes decisions

. Acts independently to achieve goals

. It can communicate, learn, reason, and collaborate with other agents or humans. In AI systems, agents can be:-

Simple rule-based bots

Intelligent systems using LLMs like GPT-4

Think of them as smart assistants that talk to each other to get things done.

💸 AI Agents in Finance — What They Do . In the financial world, AI agents are revolutionizing how we analyze, predict, and automate. Here's what they can do:

🔍 1. Market Analysis Agent - Reads financial news and stock updates

. Determines if the sentiment is positive or negative

Example: FinSentimentAgent

🧠 2. Q&A Finance Agent- Answers finance-related questions using an LLM (like GPT-4)

Example: "Should I invest in gold during inflation?"

Example: FinGPTAgent

💼 3. Portfolio Manager Agent- Suggests how to diversify investments

Monitors risks based on user profile

Rebalances portfolios automatically

💳 4. Transaction Agent- Manages wallet transfers or payments

Tracks spending and sends alerts

Example: TransactAI

📈 5. Trading Bot Agent- Uses AI to predict stock/crypto price changes

Places trades based on rules or real-time AI insights

🔗 6. RAG-based Research Agent- Fetches latest financial data from trusted websites

Uses Retrieval-Augmented Generation (RAG) to give grounded answers

Example: QueryFinanceAgent

🧾 Real-World Applications AI Agent Type Real Example Chatbot Bank customer support Robo-advisor Zerodha's smallcase recommendations Fraud Detection Agent Monitors unusual transaction patterns News Sentiment Analyzer Bloomberg AI filters news for traders.

The ai agents which i use are - . RAG ai agent , FinGPTAgent , QueryFinanceAgent , Bob Agent , Eth processor agent , Transact AI agent , FinSentiment Agent , Finsight Agent . Now let me give u each ai agent working . RAG ai agent - The RAG Agent processes user queries with a given website URL, retrieves relevant content, and generates responses using OpenAI's model. Key Concepts of RAG ai agent - Handling incoming questions with on_message Uses GPT-4o-mini for contextual responses Returns structured answers Usage of RAg ai agent - Start the agent to begin receiving and answering questions. Feel free to modify and experiment with different models or response formats! Link of RAG ai agent (url) - https://agentverse.ai/agents/details/agent1qvpy4s2vxvjjh4zrqeznppd6pq0s4gm0z3sepjunpy8yy0lx5uepvf263s6/profile

. FinGPT Agent - The FinGPT ai Agent receives questions from another agent, queries OpenAI's chat model, and responds with an answer.

Key Concepts of FinGPT Agent - (i) Handling incoming questions with on_message (ii) Querying an external LLM (GPT-4o-mini) (iii)Sending structured responses Usage of FinGPT Agent - Start the agent to begin receiving and answering questions. Feel free to modify and experiment with different models or response formats! You will need to provide your own OPENAI api key. Link for FinGPT Agent (url) - https://agentverse.ai/agents/details/agent1q2jz799u38llhjkzrftuqfyxaxpr8klfrpt45vkrtu5hj7lhwnkcxyyzsq7/profile

. QueryFinanceAgent - The QueryFinanceAgent periodically sends a list of questions and website url to a RAG agent and logs the received answers.

Key Concepts of QueryFinance Agent :- .Communicating with another agent .Sending message on startup .Handling incoming responses with on_message

Usage of QueryFinance Agent :- Start the RAG agent first to ensure it is ready to receive messages. Feel free to modify and experiment with different questions or interactions! Link for QueryFinance Agent (url) - https://agentverse.ai/agents/details/agent1qdk3sqzgdy7gl5r4wcqc5syqj900gfc309d7vk7f6ddc09g8m8zkusna6qn/profile

. Bob Agent :- The Bob Agent on startup sends a question to an AI agent and logs the received answer.

Key Concepts .Communicating with another agent .Sending messages at startup .cybersecurity regarded like some cybersecurity basic tools work such as - Google chronicle , Microsoft defender ATP ,Cylance(Blackberry) , IBM QRadar . . Handling incoming responses with on_message Usage Start the AI agent first to ensure it is ready to receive messages. Feel free to modify and experiment with different questions or interactions! Link for bob agent (url) - https://agentverse.ai/agents/details/agent1qfr043md4nvjx484vx6q98fjlqtc0x8zfrwsupgp97rd924n7ryh6yuttm6/profile

. Eth processor agent - ETH Processor Agent handles ETH transfer requests and processes transactions.

Features of Eth processor agent :- .Receives ETH transaction requests .Sends ETH transactions using Web3 .Replies with transaction hash upon success Setup - Before running the agent, update the following secrets in AgentVerse:-

WEB3_PROVIDER_URL = <YOUR_WEB3_PROVIDER_URL> like https://sepolia.infura.io/v3/{YOU_INFURA_API_KEY}, SENDER_ADDRESS = <SENDER_ADDRESS>, RECEIVER_ADDRESS = <RECEIVER_ADDRESS>, SENDER_PRIVATE_KEY = <SENDER_PRIVATE_KEY>, AMOUNT = <SENDER_PRIVATE_KEY>,

Usage of Eth processor agent :- Ensure Web3 provider details and wallet credentials are configured. Modify as needed for different interactions! Link - https://agentverse.ai/agents/details/agent1qg6adhxjsukczp644v93chkyt67wz5uzgskzts9jc6h23wtyu7xm6guqvhl/profile

. TransactAI Agent - TransAct AI Sender Agent sends a transaction request and processes the response. Link (url) - https://agentverse.ai/agents/details/agent1qguklcj4melfnvykr0nqsr0j7q0zhkhksaf9paz0ys9lylglra0w7y43r8c/profile

. FinSentimentAgent - The FinSentimentAgent is designed to analyze the sentiment of financial news, reports, or market updates by interacting with an external AI (e.g. a GPT-4o-powered agent). Link (url) - https://agentverse.ai/agents/details/agent1qfnup0v2xnwum6cz30f7z6tsy69754t6v4k3ag2p5ug9sfcars2xsqg2ljk/profile

. FinSight Agent - This ai agent is for budget planning , news summary , Risk analysis , Investment Advice . Link(url) - https://agentverse.ai/agents/details/agent1qw036ejkjurt535q3mu8pg7sgmddmv2mvcwjfqff7jmhc7paapafg8wx5jg/profile

