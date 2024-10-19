from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.tools.file import FileTools

from pkg.shared import OUTPUT_DIR
from pkg.models import IntelligenceReport

aggregator_agent = Agent(
    name="Aggregator Agent",
    role="You are responsible for aggregating and and summarizing the information from the web and financial data to create a comprehensive intelligence report merging the results from the web and financial agents. Use FileTools to read the files and output the results in a file named intelligence-report-<question>.md",
    model=OpenAIChat(id="gpt-4o"),
    tools=[FileTools(base_dir=OUTPUT_DIR)],
    instructions=["Always save response to a file named intelligence-report-<question>.json"],
    show_tool_calls=True
)

def transfer_to_aggregator_agent():
    return aggregator_agent

finance_agent = Agent(
    name="Finance Agent",
    role="Do market analysis and financial intelligence analysis of the target topic and pass to the aggregator agent. Include companies and strategies for investment exposure to the target topic.",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True), transfer_to_aggregator_agent],
    instructions=["Always use tables to display data. Provide strategic guidance and commentary, always use the first principle of information economics and central bank, government debt, and geo-political analysis."],
    show_tool_calls=True
)

def transfer_to_finance_agent():
    return finance_agent

web_agent = Agent(
    name="Web Agent",
    role="You are an expert in osint and you are tasked with searching the web for information about the desired topic to support producing a comprehensive intelligence report. Ensure the aggregator agent has all the information it needs to produce the report.",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo(), transfer_to_finance_agent, transfer_to_aggregator_agent],
    instructions=["Aggregate the latest information from the web and transfer the results to the finance agent for market analysis. With the following format: topic, date, bottom line up front, analysis, recommendations, and sources."],
    show_tool_calls=True
)

swarm = Agent(
    team=[web_agent, finance_agent, aggregator_agent],
    instructions=["Work together to create a comprehensive intelligence report about the target topic. Always end with the aggregator_agent to output the report in the intelligence-report-<question>.md file."],
    show_tool_calls=True,
    markdown=True
)







