from tools.travily_tool import travily_search
from tools.flight_tool import flight_search
from backend import run_travel_agent 
user_input = input("Enter your travel query: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
    )



#res= flight_search("plan a 7 days japan trip from india")
print("\nFinal Response:\n")
print(response["answer"])