from ldap3 import Server, Connection, ALL, NTLM, BASE

server = Server('10.10.10.161', get_info=ALL)

# get ROOT DSE
conn = Connection(server, auto_bind=True)
print(server.info)
conn.unbind()

"""
# get defaultNamingContext
conn = Connection(server, auto_bind=True)
print(server.info.other['dnsHostName'][0])
conn.unbind() 

# let's bind do a search to get all users and then unbind
entries = []
with Connection('htb.local', 'svc-alfresco', 's3rvice') as conn:
        conn.search('dc=htb,dc=local', '(&(objectclass=person))')
        entries = conn.entries

for entry in entries:   
    print(entry)


entries = []
with Connection('htb.local', 'svc-alfresco', 's3rvice') as conn:
    conn.search('dc=htb,dc=local', '(&(objectclass=person)(adminCount=1))', attributes=['userPrincipalName'])
    entries = conn.entries
for entry in entries:
    print(entry)
    
# get groups
entries = []
with Connection('htb.local', 'svc-alfresco', 's3rvice') as conn:
    conn.search('dc=htb,dc=local', '(&(objectclass=group))', attributes=['member'])
    entries = conn.entries
for entry in entries:
    print(entry) 


# get nested groups 
entries = []
with Connection('htb.local', 'svc-alfresco', 's3rvice') as conn:
    conn.search('dc=htb,dc=local', '(&(objectclass=group))', attributes=['member'])
    entries = conn.response

for entry in entries:
    try:
        if len(entry['attributes']['member']) > 0:
            print(entry['dn'])
            print(entry['attributes']['member'])
        try:
            nested = []
            with Connection('htb.local', 'svc-alfresco', 's3rvice') as conn:
                conn.search('dc=htb,dc=local', '(&(objectClass=user)(memberof:1.2.840.113556.1.4.1941:=%s)))' % entry['dn'], attributes=['member'])
                nested.append(conn.response)
            for nestedentry in nested:
                try:
                    print("\t" + nestedentry['dn'])
                    if len(nestedentry['attributes']['member']) > 0:
                        print("\t\t" + nestedentry['attributes']['member'])
                except:
                    pass
        except:
            pass
    except:
        pass

"""
