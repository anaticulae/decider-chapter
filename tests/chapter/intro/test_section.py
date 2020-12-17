# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import chapter.intro.section


def test_intro_content(master72):
    text, sections = master72
    sentences, _ = chapter.intro.section.content(text, sections)
    assert len(sentences) == 44  # TODO: NOT VALIDATED YET
