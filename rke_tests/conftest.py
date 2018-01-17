import os
import pytest
import random

from lib.aws import AmazonWebServices
from lib.rke_client import RKEClient
from lib.kubectl_client import KubectlClient


CLOUD_PROVIDER = os.environ.get("CLOUD_PROVIDER", 'AWS')


@pytest.fixture(scope='session')
def cloud_provider():
    if CLOUD_PROVIDER == 'AWS':
        return AmazonWebServices()


@pytest.fixture(scope='function')
def rke_client():
    return RKEClient()


@pytest.fixture(scope='function')
def kubectl():
    return KubectlClient()


@pytest.fixture(scope='function')
def test_name(request):
    name = request.function.__name__.replace('test_', '').replace('_', '-')
    # limit name length
    name = name[0:20] if len(name) > 20 else name
    return '{0}-{1}'.format(name, random.randint(100000, 1000000))
