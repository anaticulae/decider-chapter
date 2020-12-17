# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import chapter.intro.data
import chapter.intro.decide
import chapter.intro.section


def test_intro_decide(master72):
    sentences, _ = chapter.intro.section.content(*master72)
    decided = chapter.intro.decide.run(sentences)
    assert len(decided) == 44
    decided = sorted(utila.notnone(utila.make_unique(decided)))
    expected = [
        chapter.intro.data.IntroType.START,
        chapter.intro.data.IntroType.GOAL,
        chapter.intro.data.IntroType.METHOD,
        chapter.intro.data.IntroType.LIMIT,
        chapter.intro.data.IntroType.STRUCTURE,
    ]
    assert decided == expected
