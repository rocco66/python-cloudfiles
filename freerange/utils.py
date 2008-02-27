
import re
from urlparse  import urlparse
from errors    import InvalidUrl

def parse_url(url):
    """
    Given a URL, returns a 4-tuple containing the hostname, port,
    a path relative to root (if any), and a boolean representing 
    whether the connection should use SSL or not.
    """
    (scheme, netloc, path, params, query, frag) = urlparse(url)

    # We only support web services
    if not scheme in ('http', 'https'):
        raise InvalidUrl('Scheme must be one of http or https')

    is_ssl = scheme == 'https' and True or False

    # Verify hostnames are valid and parse a port spec (if any)
    match = re.match('([a-zA-Z0-9\-\.]+):?([0-9]{2,5})?', netloc)

    if match:
        (host, port) = match.groups()
        if not port:
            port = is_ssl and '443' or '80'
    else:
        raise InvalidUrl('Invalid host and/or port: %s' % netloc)

    return (host, port, path.strip('/'), is_ssl)
