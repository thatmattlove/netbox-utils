# netbox-utils
Collection of random python scripts written to automate things I do regularly in [Netbox](https://github.com/digitalocean/netbox). Mostly written using [`pynetbox`](https://github.com/digitalocean/pynetbox).

## Index

|Script              |Purpose                                                                                    |Status    |
|--------------------|-------------------------------------------------------------------------------------------|----------|
|`tenant_create.py`  |Asks for input, creates tenant based on input                                              |Functional|
|`tenant_prefixes.py`|Pulls a list of prefixes assigned to a particular tenant and belonging to a particular role|Functional|

## Configuration

Clone example configuration:
```console
# cp ./netbox_config_example.py ./netbox_config.py
```

And add your Netbox URL & API Token:
```
netbox_url = "example.domain.tld"
netbox_token = "0123456789"
```

### `tenant_prefixes.py`
#### Usage
```console
# python3 ./tenant_prefixes.py <tenant slug> <prefix role>
```
# License
<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png"
       width="80" height="15" alt="WTFPL" /></a>
