email_id="fazil@gmail.com"

at_index_position=email_id.index("@")


user=email_id[:at_index_position]

print(user)



domain=email_id[at_index_position:]

print(domain)