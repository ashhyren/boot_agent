import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types
from system_prompt import system_prompt
from functions.get_files_info import schema_get_files_info, available_functions



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    print("Hello from boot-agent!")

    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if len(sys.argv) == 1:
        print("ERROR: No prompt given")
        sys.exit(1)
    else:
        question = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=question)]),
    ]

    if sys.argv[-1] == "--verbose":
        print(f"\nUser prompt: \n{question}")
    print("\nRESPONSE:")

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages, config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt)
    )

    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:    
        print(response.text)

    if sys.argv[-1] == "--verbose":
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
