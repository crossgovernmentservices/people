# -*- coding: utf-8 -*-
import pytest
import base64
import json


class TestProfile:
    def test_create_profiles(self, client, email):
        payload = {'email': email}
        headers = {'Content-Type': 'application/json'}
        # create a session first
        res = client.post("/session",
                          data=json.dumps(payload),
                          headers=headers)
        assert res.status_code == 201

    def test_read_profile(self, client, email):
        # update headers with Authorization
        authstr = '%s:%s' % (email, 'hunter2')
        token = base64.b64encode(authstr.encode('ascii'))

        headers = {'Content-Type': 'application/json'}
        headers.update({'Authorization': 'Basic %s' % token.decode('ascii')})

        # GET all profiles
        res = client.get("/profile", headers=headers)
        assert res.status_code == 200
