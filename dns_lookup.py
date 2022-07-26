import os
try:
    import dns.resolver
except ModuleNotFoundError:
    print('dnspython not found')
    print('Install with pip "pip install dnspython"')
    quit()


if os.stat('domains.txt').st_size == 0:
    print('"domains.txt" does not contain any domains')

with open('domains.txt', 'r') as f:
    for d in f.read().splitlines():
        print(f'Looking up DNS records for {d}')

        arec=None
        mxrec=None
        nsrec=None
        txtrec=None
        dmarcrec=None
        soarec=None

        try:
            a_rec = dns.resolver.resolve(d, 'A')
            arec=True
        except dns.resolver.NoAnswer:
            arec=False
        try:
            mx_rec = dns.resolver.resolve(d, 'MX')
            mxrec=True
        except dns.resolver.NoAnswer:
            mxrec=False
        try:
            ns_rec = dns.resolver.resolve(d, 'NS')
            nsrec=True
        except dns.resolver.NoAnswer:
            nsrec=False
        try:
            txt_rec = dns.resolver.resolve(d, 'TXT')
            txtrec=True
        except dns.resolver.NoAnswer:
            txtrec=False
        try:
            soa_rec = dns.resolver.resolve(d, 'SOA')
            soarec=True
        except dns.resolver.NoAnswer:
            soarec=False
        dmarc_domain = f'_dmarc.{d}'
        try:
            dmarc_rec = dns.resolver.resolve(dmarc_domain, 'TXT')
            dmarcrec=True
        except dns.resolver.NXDOMAIN:
            dmarcrec=False

        
        if arec==True:
            for val in a_rec:
                print(f'A record: {val}')
        else:
            print('No A record found')

        if mxrec==True:
            for val in mx_rec:
                print(f'MX record: {val}')
        else:
            print('No MX record found')

        if nsrec==True:
            for val in ns_rec:
                print(f'NS record: {val}')
        else:
            print('No NS record found')

        if txtrec==True:
            for val in txt_rec:
                print(f'TXT record: {val}')
        else:
            print('No TXT record found')
        
        if soarec==True:
            for val in soa_rec:
                print(f'SOA record: {val}')
        else:
            print('No TXT record found')

        if dmarcrec==True:
            for val in dmarc_rec:
                print(f'DMARC TXT record: {val}')
        else:
            print('No dmarc record found')

        print('#################################')
        print()
