import os
import requests
import wrapt
import epsagon
import wrappingLib

epsagon.init(
    token='3b6fb738-df8a-4de2-9de2-afbadc80718e',
    app_name='Epsagon Exce',
    metadata_only=False,
)


wrapt.wrap_function_wrapper(requests.api, 'request', wrappingLib.wrapper)


@epsagon.python_wrapper
def test():
    requests.post('http://www.pi.com', data={'test': 'wowow'})
    requests.get('http://www.pi.com', headers={'test': 'wow'})


if __name__ == '__main__':
    test()