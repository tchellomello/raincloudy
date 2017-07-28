# -*- coding: utf-8 -*-
"""Raincloudy helpers."""
import re
from bs4 import BeautifulSoup


def serial_finder(data):
    """
    Find controller serial and faucet_serial from the initial page.

    :param str data: text to be parsed
    :return: a dict with controller_serial and faucet_serial
    :rtype: dict
    :raises IndexError: if controller_serial was not found on the data

    Many thanks to Pablo Hess <pablo@hess.net.br> for the regex filter
    """
    try:
        soup = BeautifulSoup(data, 'html.parser')
        child = soup.find_all('script',
                              text=re.compile('controller_serial'))[0]

        # pylint: disable=line-too-long
        regex = re.compile(r"controller_serial':\s*'(?P<controller_serial>\w*)',\s*'faucet_serial':\s*'(?P<faucet_serial>\w*)'") # noqa
        return regex.search(child.string).groupdict()

    except IndexError:
        raise "Could not find expression."

# vim:sw=4:ts=4:et:
