# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import gennex
import hoverpower
import pytest
from utilotest import mp  # pylint:disable=W0611
from utilotest import td  # pylint:disable=W0611

import chapter

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = chapter.PROCESS
hoverpower.setup(chapter.ROOT)

RESOURCES = [
    (hoverpower.MASTER072_PDF, '0:20'),
    (hoverpower.MASTER075_PDF, '0:15'),
    (hoverpower.MASTER078_PDF, '0:15'),
]

WORKER = 6


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    hoverpower.run()


def extract(resources):
    gennex.extract(
        files=resources,
        footnote=True,
        groupme=True,
        headlines=True,
        headnote=True,
        lists=True,
        pagenumber=True,
        sections=True,
        words=True,
        worker=WORKER,
        pages=':',
    )
