# api/mock_functions.py
def mock_hubspot_api_call(action: str, *args):
    print(f"Simulating HubSpot API call: Action={action}, Args={args}")

def mock_upso_api_call(action: str, *args):
    print(f"Simulating Upso API call: Action={action}, Args={args}")
