import vertexai
from typing import Optional
from vertexai.generative_models import GenerativeModel, Tool, FunctionDeclaration

def display_cities(cities: list[str], preferences: Optional[str] = None):
    """Provides a list of cities based on the user's search query and preferences.
    Args:
        preferences (str): The user's preferences for the search, like skiing,
            beach, restaurants, bbq, etc.
        cities (list[str]): The list of cities being recommended to the user.
    Returns:
        list[str]: The list of cities being recommended to the user.
    """
    return cities

model = GenerativeModel("gemini-2.0-flash-001")
display_cities_function = FunctionDeclaration.from_func(display_cities)
display_tool = Tool(function_declarations=[display_cities_function])
message = "I’d like to take a ski trip with my family but I’m not sure where to go."
res = model.generate_content(message, tools=[display_tool])

print(f"Function Name: {res}")
# print(f"Function Args: {res.candidates[0].content.parts[0].function_call.args}")
# current problem: function_call is none - -

# debug logs:
# gemini-1.5-flash-001` was not found or your project does not have access to it. 
# Please ensure you are using a valid model version. For more information, 
# see: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions", grpc_status:5
# gemini-1.5-flash-001 is outdated, should switch to newer versions