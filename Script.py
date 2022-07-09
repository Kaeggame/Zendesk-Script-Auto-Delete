#Import the authentification to Zendesk and rate limite of the script from Log.py
from Auth import zenpy_client

#Import the variable "five_years" from Time.py
from Time import five_years

#Search for all tickets that are solved or closed and has no activity since 5 years and put is on the "ticket" variable.
for ticket in zenpy_client.search(type='ticket', updated_before=five_years, status_greater_than='solved'):
    print(ticket)

#Delete the tickets in the "ticket" variable
#   zenpy.tickets.delete(ticket)