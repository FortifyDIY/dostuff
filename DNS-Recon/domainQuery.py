#!/usr/bin/env python

import dns.resolver
import os.path
from pprint import pprint

name = "tesla"
prefix = ['',
        'www.',
        'mail.',
        'remote.',
        'blog.',
        'webmail.',
        'server.',
        'ns1.',
        'ns2.',
        'smtp.',
        'secure.',
        'vpn.',
        'm.',
        'shop.',
        'ftp.',
        'mail2.',
        'test.',
        'portal.',
        'ns.',
        'ww1.',
        'host.',
        'support.',
        'dev.',
        'web.',
        'bbs.',
        'ww42.',
        'mx.',
        'email.',
        'cloud.',
        '1.',
        'mail1.',
        '2.',
        'forum.',
        'owa.',
        'www2.',
        'gw.',
        'admin.',
        'store.',
        'mx1.',
        'cdn.',
        'api.',
        'exchange.',
        'app.',
        'gov.',
        '2tty.',
        'vps.',
        'govyty.',
        'hgfgdf.',
        'news.',
        '1rer.',
        'lkjkui.']
suffix = ['.life',
        '.com',
        '.net',
        '.org',
        '.de',
        '.icu',
        '.uk',
        '.ru',
        '.info',
        '.top',
        '.xyz',
        '.tk',
        '.cn',
        '.ga',
        '.cf',
        '.nl',
        '.live',
        '.buzz',
        '.fit',
        '.ml',
        '.gq',
        '.wang',
        '.ryukyu',
        '.okinawa',
        '.pw',
        '.br',
        '.in',
        '.us',
        '.it',
        '.online',
        '.pl',
        '.ca']

domains = []

for x, y in [(x,y) for x in prefix for y in suffix]:
    domain = x + name  + y
    domains.append(domain)
    #creates file if one doesn't already exist for results file
    if os.path.isfile(name):
        #need to make sure this line doesn't show up in the results file
        pass
    else:
        f = open(name, "w+")
        f.close()

    with open(name, "r+") as file:
        for line in file:
            if domain in line:
                break
        else:  # not found, we are at the eof
            file.write(domain)  # append missing data
            file.write("\n")



    # domainFile = open(name, "a")
    #
    # domainFile.write(domain)
    # domainFile.write("\n")
    # domainFile.close()



def get_records(domain):
    """
    Get all the records associated to domain parameter.
    :param domain:
    :return:
    """
    ids = [
        'NONE',
        'A',
        'NS',
        'MD',
        'MF',
        'CNAME',
        'SOA',
        'MB',
        'MG',
        'MR',
        'NULL',
        'WKS',
        'PTR',
        'HINFO',
        'MINFO',
        'MX',
        'TXT',
        'RP',
        'AFSDB',
        'X25',
        'ISDN',
        'RT',
        'NSAP',
        'NSAP-PTR',
        'SIG',
        'KEY',
        'PX',
        'GPOS',
        'AAAA',
        'LOC',
        'NXT',
        'SRV',
        'NAPTR',
        'KX',
        'CERT',
        'A6',
        'DNAME',
        'OPT',
        'APL',
        'DS',
        'SSHFP',
        'IPSECKEY',
        'RRSIG',
        'NSEC',
        'DNSKEY',
        'DHCID',
        'NSEC3',
        'NSEC3PARAM',
        'TLSA',
        'HIP',
        'CDS',
        'CDNSKEY',
        'CSYNC',
        'SPF',
        'UNSPEC',
        'EUI48',
        'EUI64',
        'TKEY',
        'TSIG',
        'IXFR',
        'AXFR',
        'MAILB',
        'MAILA',
        'ANY',
        'URI',
        'CAA',
        'TA',
        'DLV',
    ]

    for a in ids:
        try:
            answers = dns.resolver.query(domain, a)
            # for rdata in answers:
            #     print(domain + ':', a, ':', rdata.to_text())
        except Exception as e:
             pass #print(e)  # or pass
    return(domains)
#length = len(domains)
#print(length)
#pprint(domains)

for i in domains:
    def fileWrite():
        f = open(name, "a+")
        f.write(i)
        f.close()
    def fWrite():
        if not os.path.exists(name) != True:
            os.remove(name)
            print(os.path.exists(name))
            print("Removing "+name+" before continuing")
            fileWrite()
        else:
            print("The file does not exist")
            fileWrite()

fWrite()


# for i in domains:
#     #print(i, end = ' ')
#
#
#         fWrite(i)
for i in domains:
    get_records(i)
