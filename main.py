import json
import requests
import wrapt


def wrapper(wrapped, instance, args, kwargs):
    metadata = {}

    try:
        if args[1] == 'https://ora4d07er6.execute-api.us-east-1.amazonaws.com/dev':
            return wrapped(*args, **kwargs)

        metadata['operation name'] = wrapped.__name__
        metadata['module'] = wrapped.__module__
        metadata['operation type'] = args[0]
        metadata['url'] = args[1]
        metadata['arguments'] = kwargs
        metadata['exception'] = ''

    except Exception as e:
        metadata['exception'] = e.args
        return e

    print(json.dumps(metadata))

    requests.post('https://ora4d07er6.execute-api.us-east-1.amazonaws.com/dev', json.dumps(metadata))


wrapt.wrap_function_wrapper(requests.api, 'request', wrapper)


def test():
    requests.post('http://www.sport5.co.il', data={'test': 'wowow'})
    requests.get('http://www.sport5.co.il', headers={'test': 'wow'})


if __name__ == '__main__':
    test()

"""""
to do:
get the data from the trace
store it into rds
"""
