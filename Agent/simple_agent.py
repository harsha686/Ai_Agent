#!/usr/bin/env python3
"""
Simple AI Agent Example
A basic AI agent that can perform simple tasks using tools.
"""

import json
from datetime import datetime
from typing import Dict, Any, List

class SimpleTool:
    """Base class for simple tools."""
    
    def __init__(self, name: str, description: str, func):
        self.name = name
        self.description = description
        self.func = func
    
    def run(self, input_text: str = "") -> str:
        """Execute the tool."""
        return self.func(input_text)

class SimpleAgent:
    """A simple AI agent that can use tools to answer questions."""
    
    def __init__(self, tools: List[SimpleTool]):
        self.tools = {tool.name: tool for tool in tools}
        self.conversation_history = []
    
    def get_available_tools(self) -> str:
        """Get a description of available tools."""
        tool_descriptions = []
        for tool in self.tools.values():
            tool_descriptions.append(f"- {tool.name}: {tool.description}")
        return "\n".join(tool_descriptions)
    
    def process_query(self, query: str) -> str:
        """Process a user query and return a response."""
        query_lower = query.lower()
        
        # Simple keyword-based tool selection
        if "time" in query_lower:
            if "current_time" in self.tools:
                result = self.tools["current_time"].run()
                response = f"The current time is {result}."
            else:
                response = "I don't have access to time information."
        
        elif "weather" in query_lower:
            if "weather" in self.tools:
                result = self.tools["weather"].run(query)
                response = f"Weather information: {result}"
            else:
                response = "I don't have access to weather information."
        
        elif "calculate" in query_lower or "math" in query_lower:
            if "calculator" in self.tools:
                # Extract numbers and operation from query
                result = self.tools["calculator"].run(query)
                response = f"Calculation result: {result}"
            else:
                response = "I don't have access to calculation tools."
        
        elif "help" in query_lower or "tools" in query_lower:
            response = f"I have access to the following tools:\n{self.get_available_tools()}"
        
        else:
            response = f"I understand you're asking: '{query}'. However, I can only help with specific tasks using my available tools. Type 'help' to see what I can do."
        
        # Store conversation
        self.conversation_history.append({"query": query, "response": response})
        
        return response

# Define some simple tools
def get_current_time(input_text: str = "") -> str:
    """Get the current time."""
    return datetime.now().strftime("%H:%M:%S")

def simple_calculator(input_text: str) -> str:
    """Perform simple calculations."""
    try:
        # Extract numbers from the input
        import re
        numbers = re.findall(r'\d+', input_text)
        if len(numbers) >= 2:
            a, b = int(numbers[0]), int(numbers[1])
            if "add" in input_text.lower() or "+" in input_text:
                return str(a + b)
            elif "subtract" in input_text.lower() or "-" in input_text:
                return str(a - b)
            elif "multiply" in input_text.lower() or "*" in input_text:
                return str(a * b)
            elif "divide" in input_text.lower() or "/" in input_text:
                return str(a / b) if b != 0 else "Cannot divide by zero"
        return "Please provide two numbers and an operation (add, subtract, multiply, divide)"
    except Exception as e:
        return f"Calculation error: {str(e)}"

def mock_weather(input_text: str) -> str:
    """Get mock weather information."""
    return "Sunny, 22°C (This is mock data)"

# Create tools
tools = [
    SimpleTool("current_time", "Get the current time", get_current_time),
    SimpleTool("calculator", "Perform simple math calculations", simple_calculator),
    SimpleTool("weather", "Get weather information", mock_weather)
]

# Create and run the agent
def main():
    agent = SimpleAgent(tools)
    
    print("🤖 Simple AI Agent")
    print("=" * 50)
    print("Hello! I'm a simple AI agent. I can help you with:")
    print(agent.get_available_tools())
    print("\nType 'quit' to exit, 'help' to see available tools.")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("🤖 Agent: Goodbye!")
                break
            
            if not user_input:
                continue
            
            response = agent.process_query(user_input)
            print(f"🤖 Agent: {response}")
            
        except KeyboardInterrupt:
            print("\n🤖 Agent: Goodbye!")
            break
        except Exception as e:
            print(f"🤖 Agent: Sorry, I encountered an error: {str(e)}")

if __name__ == "__main__":
    main()

