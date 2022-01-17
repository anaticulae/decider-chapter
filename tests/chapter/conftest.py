# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import power
import pytest
import serializeraw
import words.path


@pytest.fixture
def master72():
    source = power.link(power.MASTER072_PDF)
    # determine path
    headlines = words.path.headlines(source)
    text = words.path.word(source)
    sections = iamraw.path.sections_(source)
    # load data
    headlines = serializeraw.load_headlines(headlines)
    text = serializeraw.load_text(text, headlines=headlines)
    sections = serializeraw.load_sections(sections)
    return text, sections
