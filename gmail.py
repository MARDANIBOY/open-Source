import requests

def get_temp_email_address():
    try:
        response = requests.get('https://api.tempmail.io/request/domains')
        domains = response.json()

        if response.status_code == 200 and domains:
            domain = domains[0]
            response = requests.post(f'https://api.tempmail.io/request/mailbox/{domain}')

            if response.status_code == 201:
                mailbox = response.json()
                email_address = f'{mailbox["email"]}@{domain}'
                return email_address

        raise Exception('Failed to create temporary email address')

    except Exception as e:
        print(f'Error: {str(e)}')
        return None

# Example usage
temp_email = get_temp_email_address()
print(f'Temporary Email Address: {temp_email}')
