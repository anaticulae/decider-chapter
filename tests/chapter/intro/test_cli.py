# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest

import chapter.path
import chapter.serialize
import tests.chapter


def detect_intro(source, testdir, monkeypatch):
    source = power.link(source)
    tests.chapter.run(f'-i {source} --intro', monkeypatch=monkeypatch)
    # load data
    path = chapter.path.chapter_intro(testdir.tmpdir)
    loaded = chapter.serialize.load_chapter_introinfo(path)
    return loaded


@pytest.mark.parametrize('source', [
    pytest.param(power.MASTER078_PDF, id='master78'),
])
def test_chapter_intro_x_complete(source, testdir, monkeypatch):
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
def test_chapter_intro_x_missing(source, testdir, monkeypatch):
    loaded = detect_intro(source, testdir, monkeypatch)
    # verify
    assert loaded.goal
    assert loaded.method
    assert loaded.start
    assert not loaded.limit
    assert not loaded.structure
