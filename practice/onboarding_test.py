#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""CodinGame: Onboarding Test"""

from attest import Tests
import onboarding

TESTS = Tests()


@TESTS.test
def detect():
    """Test the functionality of the detect method."""
    dictionary_default = {
        'name': '',
        'distance': -1
    }
    assert onboarding.detect() == dictionary_default
    dictionary_defined = {
        'name': 'defined',
        'distance': 42
    }
    assert (onboarding.detect(dictionary_defined['name'],
                              dictionary_defined['distance']) ==
            dictionary_defined)

if __name__ == '__main__':
    TESTS.run()
