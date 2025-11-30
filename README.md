## Description
🛒 This is a personal shopping assistant built with the Google Agent Development Kit (ADK). This assistant helps user research the best item to buy, provides recommendations, then stores the product list in user's Notion workspace.

## Demo
[Watch the video demo](./video-demo.mp4)

Chat with your assistant:

<img width="80%" alt="adk ui" src="https://github.com/user-attachments/assets/43c188a3-9512-498a-a62c-6e0a1ddd54e3" />
<br><br>

Store in your Notion:

<img width="80%" alt="notion page" src="https://github.com/user-attachments/assets/a6c9596e-b8ad-4bf2-9fb3-7a990e21023e" />


## Setup

1. Clone the repository.
   ```
   git clone https://github.com/lia-weng/google-adk-notion-mcp.git
   ```
1. Create and activate a virtual environment.
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
1. Install dependencies.
   ```
   pip install -r requirements.txt
   ```
1. Create a `.env` file in the `./notion-agent` with the following variables.
   ```
   GOOGLE_GENAI_USE_VERTEXAI=0
   GOOGLE_API_KEY= # your Google API Key, create one from: https://aistudio.google.com/api-keys
   NOTION_API_KEY= # your Notion API Key, create one from: https://www.notion.so/profile/integrations
   ```
1. Run the app in the root folder, then go to `http://127.0.0.1:8000/` to start chatting with your personal shopping assistant!
   ```
   adk web
   ```
1. (Optional) In `./notion_agent/agent.py` update `USER_INFO` with your own information.
   ```
   USER_INFO = {
     "name": "Lia",
     "gender": "female",
     "age": 25,
   }
   ```
