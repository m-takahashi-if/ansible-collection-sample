#!/usr/bin/env python3
from urllib.parse import parse_qs
from urllib.parse import urlparse
from urllib.parse import urlencode
from ansible.module_utils.basic import *

module = AnsibleModule(
    argument_spec = dict(
        command=dict(required=True),
        base_url = dict(required=False, default='http://localhost:8080/')
    )
)

query_string = urlencode({'':module.params['command']})

module.exit_json(changed=True)
