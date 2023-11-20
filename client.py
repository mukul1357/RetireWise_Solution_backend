import requests

url = 'http://127.0.0.1:5000/TIAA/prediction1'
url2 = 'http://127.0.0.1:5000/TIAA/prediction2'

# Define the data to be sent in the request body
data = {
    'age': 30,
    'retirement_age': 60,
    'goals': "to plan a Europe trip from India and to get 8000 per month after retirement for 20 years"
}

# Make a POST request with the data
response = requests.post(url, json=data)


data2 = {
    'age' : data['age'],
    'savings_per_annum' : 30000,
    'expected_savings_growth' : 0.07,
    'risk_tolerance' : 1,
    'age_of_retirement' : data['retirement_age'],
    'employment' : 'Doctor',
    'region' : 'Tier3',
    'retirement_goals_cost' : response.json()['cost_value'],
    'current_amount' : 100000,
    'dependents' : 1
}
print(response.json())
print(data2)

response2 = requests.post(url2, json=data2)
print(response2.json())