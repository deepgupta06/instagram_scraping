from pymailtm import Account, MailTm

"""mt = MailTm()
domain =mt._get_domains_list()[0]
print(domain)
password = "qwerty123!"
username = "qwertyuiop9191"
address = f"{username}@{domain}"
response = mt._make_account_request("accounts", address, password)
print(response)"""
mt = MailTm()
domain =mt._get_domains_list()[0]
print(domain)
password = "qwerty123!"
username = "qwertyuiop9191"
address = f"{username}@{domain}"
token = "/accounts/6400b8aabbfe3825ed2e0204"
account = Account(token, address, password)
#print(account.get_messages())
print(account.wait_for_message())