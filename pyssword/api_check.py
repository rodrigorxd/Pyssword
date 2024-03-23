import requests

def connection():
    response = requests.get('https://api.pwnedpasswords.com/range/21BD1')
    return response.status_code

#check first 5 digits
def first_content(first_search):
    response = requests.get(f'https://api.pwnedpasswords.com/range/{first_search}').text
    return response

#check password
def second_content(second_search, first_report):
    if second_search.upper() in first_report:
        return True