import vertexai
import pprint
from vertexai.preview.extensions import Extension

PROJECT_ID = "your project id"
# REGION = "us-central1"
vertexai.init(project=PROJECT_ID)

extension_code_interpreter = Extension.from_hub("code_interpreter")
CODE_QUERY = """Write a python method to invert a binary tree in O(n) time."""
response = extension_code_interpreter.execute(
 operation_id = "generate_and_execute",
 operation_params = {"query": CODE_QUERY}
 )
print("Generated Code:")
pprint.pprint({response['generated_code']})