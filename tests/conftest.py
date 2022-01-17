# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import genex
import power
import pytest

import chapter

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = chapter.PROCESS
power.setup(chapter.ROOT)

RESOURCES = [
    (power.MASTER072_PDF, '0:10'),
    (power.MASTER075_PDF, '0:15'),
    (power.MASTER078_PDF, '0:15'),
]

WORKER = 6


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    power.run()


def extract(resources):
    genex.extract(
        files=resources,
        destination=power.generated(),
        base=power.REPOSITORY,
        groupme=True,
        sections=True,
        words=True,
        magic=True,
        worker=WORKER,
        pages=':',
    )
