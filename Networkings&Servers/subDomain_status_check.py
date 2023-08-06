import requests # this lib is used to check the status of the HTTPS requests
import time  # we have many advantages of time library, in this case we use to measure time intervals
from prettytable import PrettyTable  # it will put the data in a tabular format

# subdomains list to check the status, we can put multiple subdomains to check the status
subdomains = [
    "chat.openai.com",
    "www.gmail.com",
    "www.herovired.com",
    "vlearnv.herovired.com",
    "subdomain1.example.com"
]

# to display the status of the subdomain in tabular format
table = PrettyTable()
table.field_names = ["Subdomain", "Status"]

def status_check(subdomain):
    try:
        response = requests.get(f"http://{subdomain}")
        if response.status_code == 200:
            return "Up"
        else:
            return "Down"
    except requests.ConnectionError:
        return "Down"

def store_data_in_table():
    table.clear_rows()
    for subdomain in subdomains:
        status = status_check(subdomain)
        table.add_row([subdomain, status])

def main():
    try:
        while True:
            store_data_in_table()
            print(table)
            time.sleep(60)  # We are checking for  minute. We can modify as per our requirement. We need to enter in seconds format
    except KeyboardInterrupt:
        print("Status check interrupted by the user.")

if __name__ == "__main__":
    main()
