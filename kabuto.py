import requests
import time
import os
from twilio.rest import Client
from datetime import datetime

# Twilio Details (need to fill in)
account_sid = ''
auth_token = ''
twilio_number = ''
my_number = ''

# Cookie data (need to fill in)
cookies = {
    '__stripe_mid': '',
    '__stripe_sid': '',
    'kabFLOW': ''
}

events = [
    ['Event Name', 1234],
]

api_url = "https://bookings.kaboodle.co.uk/api/package/ticketavailability"
event_url_template = 'https://bookings.kaboodle.co.uk/book/{}/ticket'

def check_tickets():
    
    for event_name, event_id in events:
        print('Checking event: {}'.format(event_name))
        event_url = event_url_template.format(event_id)

        api_headers = {'package-id': str(event_id),
            'referer': event_url,
            'accept': 'application/json',
            # 'cookie': cookies
            }
        response = requests.get(api_url, allow_redirects=True, headers=api_headers, cookies=cookies)
        print("\n" + str(datetime.now()) + "\n")
        print(str(response.json()) + "\n")
        if response.status_code < 300:
            for item in response.json()['tickets']:
                tickets_available = item['available']
                if tickets_available and not item['sold_out']:
                    print("There are " + str(tickets_available) + " tickets available for {}!".format(event_name))
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                        body = "{} tickets available for {}! {}".format(
                            tickets_available,
                            event_name,
                            event_url
                        ),
                        from_= twilio_number,
                        to = my_number
                    )
                    break
        else:
            print('REQUEST ERROR')
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body = "Error with API request: {}".format(
                    response.json()
                ),
                from_= twilio_number,
                to = my_number
            )
            break

check_tickets() 
