# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import chapter.intro.data
import chapter.intro.decide
import chapter.utils


def test_intro_decide(master72):
    sentences, firstchapter = chapter.utils.content(*master72)
    decided = chapter.intro.decide.run(sentences)
    assert len(decided) == 44
    result = chapter.intro.decide.judge(decided, firstchapter)
    assert result.pagestart == 3
    assert result.pageend == 6
    assert len(result.structure) == 14  # NOT VALIDATED
