# -*- coding: utf-8 -*-
"""Test raincloudy.faucet post."""
import requests_mock
from tests.test_base import UnitTestBase
from raincloudy.const import (
    DAJAXICE_ENDPOINT, HOME_ENDPOINT, SETUP_ENDPOINT)
from tests.extras import load_fixture


class TestRainCloudyFaucet(UnitTestBase):
    """Unit tests for faucet attributes."""

    @requests_mock.Mocker()
    def test_post_actions(self, mock):
        """Test post actions."""
        mock.post(DAJAXICE_ENDPOINT,
                  text=load_fixture('get_cu_and_fu_status.json'))
        mock.get(HOME_ENDPOINT,
                 text=load_fixture('home.html'))
        mock.post(SETUP_ENDPOINT)

        faucet = self.rdy.controller.faucet
        self.assertIsNone(setattr(faucet, 'name', 'test'))
        faucet.update()

# vim:sw=4:ts=4:et:
