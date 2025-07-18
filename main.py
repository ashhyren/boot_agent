import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types
from system_prompt import system_prompt
from call_function import available_functions, function_dictionary

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

    verbose_status=False

    if sys.argv[-1] == "--verbose":
        verbose_status = True
        print(f"\nUser prompt: \n{question}")
    print("\nRESPONSE:")

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages, config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt)
    )

    if response.function_calls:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose_status)
            if not function_call_result.parts[0].function_response.response:
                raise Exception("ERROR: No response generated. Check code.")
            if verbose_status == True:
                print(f"-> {function_call_result.parts[0].function_response.response}")


    else:    
        print(response.text)

    if verbose_status:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

#

def call_function(function_call_part, verbose=False):
    if verbose == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else: 
        print(f" - Calling function: {function_call_part.name}")
    function_call_part.args["working_directory"] = "./calculator"
    if function_call_part.name not in function_dictionary:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
        )
    ],
)
    function_result = function_dictionary[function_call_part.name](**function_call_part.args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": function_result},
        )
    ],
)
    
#

if __name__ == "__main__":
    main()
