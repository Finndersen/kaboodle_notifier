# kabuto

Kaboodle ticket resale watcher (updated)

## Context

**Kaboodle** is a service that sells tickets to events, mainly electronic music at Printworks in London. For some events where the tickets have sold out, a "Resale queue" is made active. If one would like to attend a sold out event with the resale queue active, they would need to keep entering the Resale queue link and hoping some tickets were made available since there is no notification option. 

**Twilio** is an API platform company which provides a tool to programmatically send text messages. One can sign up for a free trial which provides £15 free credit.

## Functionality

`kabuto` is a python script that checks the resale queue for available tickets to a particular event and sends a text message when at least 1 ticket becomes available.

## Usage
- Find the event page on kaboodle.co.uk, Click Resale Tickets link to open a page which should have URL in format like: 
> https://bookings.printworkslondon.co.uk/book/<event_id>/ticket
- Update script with event name and ID (taken from above URL)
- Use something like [this](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc) to get cookies while on the ticket resale page, and fill out data in the script
- For text message notification, create a free [Twilio](twilio.com) account and add details to script (could alternatively use SNS or something on AWS to send an email if deploying there)

