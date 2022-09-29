# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest
import utilatest

import chapter.path
import chapter.serialize
import tests.chapter


def detect_intro(source, td, mp):
    source = power.link(source)
    tests.chapter.run(f'-i {source} --intro', mp=mp)
    # load data
    path = chapter.path.chapter_intro(td.tmpdir)
    loaded = chapter.serialize.load_chapter_introinfo(path)
    return loaded


@pytest.mark.parametrize('source', [
    pytest.param(power.MASTER078_PDF, id='master78'),
])
def test_chapter_intro_x_complete(source, testdir, monkeypatch):
    utilatest.fixture_requires(source)
    loaded = detect_intro(source, testdir, monkeypatch)
    # verify
    assert loaded.goal
    assert loaded.limit
    assert loaded.method
    assert loaded.start
    assert loaded.structure


@pytest.mark.parametrize('source', [
    pytest.param(power.MASTER075_PDF, id='master75', marks=pytest.mark.xfail),
])
def test_chapter_intro_x_missing(source, td, mp):
    loaded = detect_intro(source, td, mp)
    # verify
    assert loaded.goal
    assert loaded.method
    assert loaded.start
    assert not loaded.limit
    assert not loaded.structure
