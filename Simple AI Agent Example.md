# Simple AI Agent Example

This project demonstrates a basic AI agent implemented in Python. The agent can interact with the user and utilize predefined tools to answer questions or perform simple tasks.

## Features

- **Current Time Tool**: Provides the current time.
- **Calculator Tool**: Performs basic arithmetic operations (addition, subtraction, multiplication, division).
- **Weather Tool**: Provides mock weather information.
- **Interactive Command Line Interface**: Allows users to interact with the agent through text commands.

## How to Run

1.  **Save the Agent Script**: Save the provided `simple_agent.py` file to your local machine.

2.  **Make it Executable**: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the following command to make the script executable:

    ```bash
    chmod +x simple_agent.py
    ```

3.  **Run the Agent**: Execute the agent using the following command:

    ```bash
    ./simple_agent.py
    ```

    The agent will start, and you will see a prompt where you can type your queries.

## Usage Examples

Once the agent is running, you can type commands like:

-   `What time is it?`
-   `calculate 10 add 5`
-   `calculate 20 minus 7`
-   `calculate 4 multiply 6`
-   `calculate 100 divide 4`
-   `What's the weather like?`
-   `help` (to see available tools)
-   `quit` (to exit the agent)

## Code Structure

-   `SimpleTool` Class: A generic class to define tools with a name, description, and a function to execute.
-   `SimpleAgent` Class: The core agent class that manages tools, processes user queries, and maintains conversation history.
-   Tool Functions: `get_current_time`, `simple_calculator`, and `mock_weather` are example functions that serve as tools for the agent.

This example is designed to be straightforward and easy to understand, illustrating the fundamental concepts of an AI agent interacting with tools.


