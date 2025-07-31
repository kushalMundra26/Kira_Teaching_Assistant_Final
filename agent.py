import asyncio
import logging
from dotenv import load_dotenv

from livekit import rtc
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.voice import Agent, AgentSession
from livekit.agents import stt, ModelSettings
from livekit.plugins import deepgram, cartesia, silero, anthropic, google, resemble
from livekit.agents.llm import StopResponse
from prompts import AGENT_INSTRUCTIONS
from tools import search_web, add_calendar_event, update_calendar_event, remove_calendar_event, list_calendar_events

load_dotenv()

logger = logging.getLogger("wake-word-agent")
logger.setLevel(logging.INFO)


class WakeWordAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions=AGENT_INSTRUCTIONS,
            stt=deepgram.STT(),
            llm=anthropic.LLM(
                model="claude-3-5-sonnet-20241022"),
            tts=resemble.TTS(
                voice_uuid="55592656",
            ),
            vad=silero.VAD.load(),
            tools=[search_web, add_calendar_event, update_calendar_event, remove_calendar_event, list_calendar_events],
        )

    async def on_user_turn_completed(self, turn_ctx, new_message):
        wake_words = ["kira", "quira", "keira", "kia", "kiara", "khira", "keera"]
        if any(wake_word in new_message.text_content.lower() for wake_word in wake_words):
            logger.info(f"Responding with: {new_message.text_content}")
            try:
                with open('meeting_log.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    m_logs = ' '.join(line.strip() for line in lines)
                    m_log = ' '.join(m_logs.split())
                new_message.content = [
                    f"Here is the entire meeting log: {m_log} Now just answer this question: {new_message.text_content}"
                ]
            except Exception as e:
                logger.error(f"Failed to read meeting_log.txt: {e}")
        else:
            
            logger.info("No wake word — logging and ignoring user input.")
            try:
                with open("meeting_log.txt", mode="a", encoding="utf-8") as f:
                    f.write(f"[USER]: {new_message.text_content}\n")
            except Exception as e:
                logger.error(f"Failed to write to meeting_log.txt: {e}")
            raise StopResponse()



async def entrypoint(ctx: JobContext):
    await ctx.connect()
    session = AgentSession()
    await session.start(agent=WakeWordAgent(), room=ctx.room)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
