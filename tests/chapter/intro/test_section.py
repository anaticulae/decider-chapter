# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import chapter.utils


def test_intro_content(master72):
    text, sections = master72
    sentences, _ = chapter.utils.content(text, sections)
    assert len(sentences) == 39  # TODO: NOT VALIDATED YET
