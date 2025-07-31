import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool()
async def search_web(query: str, run_context: RunContext) -> str:
    """
    Search the web using DuckDuckGo and return the first result.
    """
    try:
        results = DuckDuckGoSearchRun().run(tool_input=query)
        logging.info(f"Web search results for '{query}': {results}")
        return results if results else "No results found."
    except Exception as e:
        logging.error(f"Error during web search: {e}")
        return "An error occurred while searching the web."

# @function_tool()
# async def send_email(context: RunContext, to_email: str, subject: str, message: str) -> str:
#     """
#     Send an email through Gmail SMTP.

#     Args:
#         context (RunContext): The run context for logging.
#         to_email (str): The recipient's email address.
#         subject (str): The subject of the email.
#         message (str): The body of the email.
#     """
#     try:
#         import smtplib
#         from email.mime.text import MIMEText

#         msg = MIMEText(body)
#         msg['Subject'] = subject
#         msg['From'] = '


calendar_store = {}

@function_tool()
async def add_calendar_event(title: str, date: str, details: str, run_context: RunContext) -> str:
    """
    Add a new event to the calendar.
    """
    try:
        if title in calendar_store:
            return f"An event with the title '{title}' already exists."
        calendar_store[title] = {"date": date, "details": details}
        logging.info(f"Added event: {title} on {date} with details '{details}'")
        return f"Event '{title}' added for {date}."
    except Exception as e:
        logging.error(f"Error adding event: {e}")
        return "An error occurred while adding the event."

@function_tool()
async def update_calendar_event(title: str, date: str = None, details: str = None, run_context: RunContext = None) -> str:
    """
    Update an existing event's date or details.
    """
    try:
        if title not in calendar_store:
            return f"No event found with the title '{title}'."
        if date:
            calendar_store[title]["date"] = date
        if details:
            calendar_store[title]["details"] = details
        logging.info(f"Updated event: {title} to {calendar_store[title]}")
        return f"Event '{title}' updated."
    except Exception as e:
        logging.error(f"Error updating event: {e}")
        return "An error occurred while updating the event."

@function_tool()
async def remove_calendar_event(title: str, run_context: RunContext) -> str:
    """
    Remove an event from the calendar.
    """
    try:
        if title not in calendar_store:
            return f"No event found with the title '{title}'."
        del calendar_store[title]
        logging.info(f"Removed event: {title}")
        return f"Event '{title}' removed."
    except Exception as e:
        logging.error(f"Error removing event: {e}")
        return "An error occurred while removing the event."

@function_tool()
async def list_calendar_events(run_context: RunContext) -> str:
    """
    List all events in the calendar.
    """
    try:
        if not calendar_store:
            return "No events found in the calendar."
        events = "\n".join(
            f"- {title}: {data['date']} — {data['details']}" for title, data in calendar_store.items()
        )
        logging.info("Listing calendar events.")
        return f"Calendar Events:\n{events}"
    except Exception as e:
        logging.error(f"Error listing events: {e}")
        return "An error occurred while listing the events."

@function_tool()
async def search_youtube(topic: str, run_context: RunContext) -> str:
    """
    If the user asks for a video explanation, search for a YouTube video on the given topic and return the first video link.
    """
    try:
        query = f"{topic} site:youtube.com"
        results = DuckDuckGoSearchRun().run(tool_input=query)
        logging.info(f"YouTube search results for '{topic}': {results}")
        return results if results else "No YouTube videos found for this topic."
    except Exception as e:
        logging.error(f"Error searching YouTube: {e}")
        return "An error occurred while searching for YouTube videos."

