from pprint import pprint
from ipwhois import IPWhois
import socket
import json
import os.path
from varname import varname

name = 'escapefromtarkov'

##### array of domain names to do lookups on, can be pulled from ansible inventory if needed
DNames = open(name, "r+")
domainNames = DNames.read().splitlines()
#pprint(domainNames)

##### empty array to be filled later
IPaddrs = []

##### for loop to perform actions on each domain name (dn) in the array (domainNames)
for dn in domainNames:
    ##### basically an nslookup using socket, converts FQDN to IP
    #print(dn)
    try:
        ip = str(socket.gethostbyname(dn))
        ##### append translated IPs into our empty array (IPaddrs)
        IPaddrs.append(ip)
    except Exception:
        pass

    #pprint(dn + " == " + ip)

    ##### for loop to run IPWhois on each IP in IPaddrs array
    for IPaddr in IPaddrs:
        ##### run IPWhois
        obj = IPWhois(IPaddr)
        ##### create results variable
        results = obj.lookup_whois()
        ##### convert json output (results) to string
        j = json.dumps(results)
        #pprint(results)
        ##### decode the json string to parse
        a = json.loads(j)
        ##### example(s) of pulling top-level values to var
        asn = a['asn']
        queryIP = a['query']
        ##### example of pulling nested values to var, or several layers deep
        cidr = a['nets'][0]['cidr']
        email = a['nets'][0]['emails']
        addr = a['nets'][0]['address']
        #pprint(results)
        # if type(email) is list:
        #     print
        #     'a list'
        # elif type(email) is tuple:
        #     print
        #     'a tuple'
        # else:
        #     print
        #     'neither a tuple or a list'
        #pprint(email)
        fnames = ['all', 'asn', 'queryIP', 'cidr', 'email', 'addr']

        def rectype(i):
            switcher={
                'all':results,
                'asn':asn,
                'queryIP':queryIP,
                'cidr':cidr,
                'email':email,
                'addr':addr
            }
            return switcher.get(i)

        # Function to convert
        def listToString(t):
            # initialize an empty string
            str1 = ""
            # traverse in the string
            for ele in t:
                str1 += ele
                # return string
            return str1

        def convertTuple(tup):
            str = ''.join(tup)
            return str

        def vname():
            return varname(fn)

            #pprint(types)
        for fn in fnames:
            if os.path.isfile(name+'.'+fn):
                # need to make sure this line doesn't show up in the results file
                pass
            else:
                f = open(name+'.'+fn, "w+")
                f.close()

            with open(name+'.'+fn, "r+") as file:
                t = rectype(fn)
                print(t)
                for line in file:
                    if t in line:
                        break
                    else:
                        file.write(t)
                        file.write("\n")
                    # print(t)
                    # if t is list:
                    #     t = listToString(t)
                    #     if t in line:
                    #         print('strTexists')
                    #         break
                    #     else:
                    #         file.write(t)  # append missing data
                    #         file.write("\n")
                    #         print('tISstring')
                    # elif t is tuple:
                    #     t = convertTuple(t)
                    #     if t in line:
                    #         print('tupleTexists')
                    #         break
                    #     else:
                    #         file.write(t)  # append missing data
                    #         file.write("\n")
                    #         print('tIStuple')
                    # else:
                    #     if t in line:
                    #         print('Texists')
                    #         break
                    #     else:
                    #         file.write(t)  # append missing data
                    #         file.write("\n")
                    #         print('Twritten')






                    # if t in line:
                    #     break
                    # elif t is list:  # not found, we are at the eof
                    #     file.write(listToString(t))  # append missing data
                    #     file.write("\n")
                    # else:
                    #     file.write(t)  # append missing data
                    #     file.write("\n")



# ##### contained within the same 'for loop' to use variables form each for printing, added value headers for readability
# ##### can also be passed to new variables, or to other scripts
#     pprint('Domain: ' + dn)
#     pprint('ASN: ' + asn)
#     pprint('Query: ' + query)
#     pprint('CIDR: ' + nets)
#     ##### blank line for readability
#     print()
#
#     ##### alternatively, in a one-liner
#     print('ALTERNATIVE', 'Domain: ' + dn, 'ASN: ' + asn, 'Query: ' + query, 'CIDR: ' + nets, sep="\n")
#     print()
#     print('##################')
#     print()
