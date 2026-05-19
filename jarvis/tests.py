import json
import os
assert os.path.exists("data.json"), "ERROR: data.json file does not exist!"
print("Test 1 passed: data.json exists")
with open("data.json", "r") as file:
    data = json.load(file)
print("Test 2 passed: data.json can be opened and read")
assert "open" in data, "ERROR: section 'open' not found in data.json!"
print("Test 3 passed: section 'open' exists")
assert "calculate" in data, "ERROR: section 'calculate' not found in data.json!"
print("Test 4 passed: section 'calculate' exists")
assert "app" in data, "ERROR: section 'app' not found in data.json!"
print("Test 5 passed: section 'app' exists")
assert "plus" in data["calculate"], "ERROR: 'plus' not found in calculate!"
assert "minus" in data["calculate"], "ERROR: 'minus' not found in calculate!"
assert "multiply" in data["calculate"], "ERROR: 'multiply' not found in calculate!"
assert "divide" in data["calculate"], "ERROR: 'divide' not found in calculate!"
print("Test 6 passed: all required commands exist in 'calculate'")
for site_name in data["open"]:
    assert isinstance(data["open"][site_name], str), f"ERROR: link for '{site_name}' is not a string!"
print("Test 7 passed: all links in 'open' are strings")
for app_name in data["app"]:
    assert isinstance(data["app"][app_name], str), f"ERROR: path for '{app_name}' is not a string!"
print("Test 8 passed: all paths in 'app' are strings")
print("\nAll tests passed successfully!")