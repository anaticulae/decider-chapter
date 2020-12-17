# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import utila

import chapter
import tests.chapter


def test_chapter_cli_help(monkeypatch):
    tests.chapter.run('--help', monkeypatch=monkeypatch)


def test_chapter_nomonkey_cli_help():
    utila.run(f'{chapter.PROCESS} --help')


def test_chapter_master72(testdir, monkeypatch):
    source = power.link(power.MASTER072_PDF)
    tests.chapter.run(f'-i {source}', monkeypatch=monkeypatch)


def test_chapter_serialize(testdir, monkeypatch):
    source = power.link(power.MASTER072_PDF)
    tests.chapter.run(f'-i {source}', monkeypatch=monkeypatch)

    intro = chapter.path.chapter_intro(testdir.tmpdir)
    loaded = chapter.serialize.load_chapter_introinfo(intro)
    dumped = chapter.serialize.dump_chapter_introinfo(loaded)
    raw = utila.file_read(intro)
    assert dumped == raw
