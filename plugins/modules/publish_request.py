#!/usr/bin/env python3

from urllib.error import URLError
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import parse_qs
from urllib.parse import urlencode
from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import ParseResult
from ansible.module_utils.basic import AnsibleModule

# Ansibleモジュールの定義
module = AnsibleModule(
    argument_spec=dict(
        base_url=dict(required=False, type='str', default='http://localhost:8080/'),
        value=dict(required=False, type='int', default=None),
        command=dict(required=False, type='str', default=None)
    )
)

# 接続先のURIに埋め込むパラメータの収集
params = dict()
for key in ['command', 'value']:
    if module.params[key] is not None:
        params[key] = module.params[key]

# 接続先のURIの構築
parsed = urlparse(module.params['base_url'])
url = urlunparse(
    ParseResult(
        scheme=parsed.scheme,
        netloc=parsed.netloc,
        path=parsed.path,
        params='',
        query=urlencode(params),
        fragment=''
    )
)

# HTTPリクエスト発行
request = Request(url)
try:
    with urlopen(request) as response:
        body = response.read()
        module.exit_json(
            changed=True,
            msg=body.decode('utf-8'),
            ansible_facts={'url':url}
        )
except URLError as err:
    module.fail_json(
        msg=str(err.reason),
        ansible_facts={'url':url}
    )
