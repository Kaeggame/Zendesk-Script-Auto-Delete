#Here is the credentials, in "email" you should put your email, in "Token" you should put a valid API token and the "Subdomain" is the subdomain of our Zendesk.
creds = {
'email' : '',
'token' : '',
'subdomain': ''
}

#library from Zendesk in order to be use Python on Zendesk.
from zenpy import Zenpy

#Zenpy authentification to Zendesk and rate limite of the script (Remplace X to the limit of your Zendesk API Call).
zenpy_client = Zenpy(proactive_ratelimit=X, **creds)
zenpy = Zenpy(**creds)

