# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import chapter
import tests.chapter


def test_chapter_cli_help(monkeypatch):
    tests.chapter.run('--help', monkeypatch=monkeypatch)


def test_chapter_nomonkey_cli_help():
    utila.run(f'{chapter.PROCESS} --help')
