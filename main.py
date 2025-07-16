import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types



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
        model='gemini-2.0-flash-001', contents=messages
    )
    print(response.text)
    if sys.argv[-1] == "--verbose":
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
