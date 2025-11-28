from dotenv import load_dotenv

from google.adk.agents import Agent
from google.genai import types
from google.adk.tools import google_search, AgentTool
from google.adk.models.google_llm import Gemini

from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

load_dotenv()

retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

USER_INFO = {
    "name": "Lia",
    "gender": "female",
    "age": 25,
}

RESEARCH_AGENT_INSTRUCTION = """
   A helpful assistant for researching the best products to buy based on the user's requirement
"""

research_agent = Agent(
    model=Gemini(model="gemini-2.5-flash", retry_options=retry_config),
    name="research_agent",
    description="A helpful assistant for researching the best products to buy based on the user's requirement.",
    instruction=RESEARCH_AGENT_INSTRUCTION,
    tools=[google_search],
)

mcp_notion_server = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=["-y", "mcp-remote", "https://mcp.notion.com/mcp"],
            tool_filter=["notion-search", "notion-create-pages"],
        ),
        timeout=30,
    )
)

ROOT_AGENT_INSTRUCTION = f"""
    You are a personal shopping assistant that helps user find the best products and store them in their Notion workspace. Personalize your messages and product recommendations based on the user's information: {USER_INFO}.

    First, ask the user what they want to buy. If user's description is too vague, ask for more details or clarifying questions to help you refine the search.
    
    Then, research online and find the top 3 options. Output the name, price, and briefly explain why you chose the time.

    Then, ask if user is happy with the options. If yes, store the product information in the user's Notion workspace. If not, ask user for more details and research again.

    If there already exists a page called "Shopping List", add the items you found to that page. Format them items as follows:
    - Product Type: (header 3)
        - Product 1: (bullet)
            - Product 1 info (sub-bullet)
        - Product 2: (bullet)
            - Product 2 info (sub-bullet)
        - Product 3: (bullet)
            - Product 3 info (sub-bullet)

    If there is no such page, create one first, and then add the items to that database.
"""

root_agent = Agent(
    model=Gemini(model="gemini-2.5-flash", retry_options=retry_config),
    name="root_agent",
    description="A personal shopping assistant.",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=[AgentTool(agent=research_agent), mcp_notion_server],
)
