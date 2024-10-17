from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.tools.file import FileTools

from pkg.shared import OUTPUT_DIR

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True), FileTools(base_dir=OUTPUT_DIR)],
    instructions=["Always use tables to display data. Append the file created by the Web Agent with the latest financial data and market analysis."],
    show_tool_calls=True,
)

def transfer_to_finance_agent():
    return finance_agent

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo(), FileTools(base_dir=OUTPUT_DIR), transfer_to_finance_agent],
    instructions=["Always save response to a file named osint-report-<question>.md. Always use transfer_to_finance_agent() to get financial data and do the market analysis."],
    markdown=True,
    show_tool_calls=True,
)


swarm = Agent(
    team=[web_agent, finance_agent],
    show_tool_calls=True,
    markdown=True
)







