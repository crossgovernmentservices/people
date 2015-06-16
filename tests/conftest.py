# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest
import os


@pytest.fixture(scope='session')
def client():
    os.environ['TESTING'] = 'true'

    from application.settings import TestConfig
    from application.app import create_app
    return create_app(TestConfig).test_client()


@pytest.fixture(scope='session')
def email():
    return 'test@example.org'
