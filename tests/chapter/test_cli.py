# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import utila
import utilatest

import chapter
import tests.chapter


def test_chapter_cli_help(mp):
    tests.chapter.run('--help', mp=mp)


def test_chapter_nomonkey_cli_help():
    utila.run(f'{chapter.PROCESS} --help')


@utilatest.requires(power.MASTER072_PDF)
def test_chapter_master72(td, mp):  # pylint:disable=W0613
    source = power.link(power.MASTER072_PDF)
    tests.chapter.run(f'-i {source}', mp=mp)


@utilatest.requires(power.MASTER072_PDF)
def test_chapter_serialize(td, mp):
    source = power.link(power.MASTER072_PDF)
    tests.chapter.run(f'-i {source}', mp=mp)

    intro = chapter.path.chapter_intro(td.tmpdir)
    loaded = chapter.serialize.load_chapter_introinfo(intro)
    dumped = chapter.serialize.dump_chapter_introinfo(loaded)
    raw = utila.file_read(intro)
    assert dumped == raw
