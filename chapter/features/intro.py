# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import serializeraw

import chapter.intro.decide
import chapter.serialize


def work(words: str, headlines: str, sections: str, pages: tuple = None) -> str:
    # load data
    headlines = serializeraw.load_headlines(headlines, pages=pages)
    words = serializeraw.load_text(words, headlines=headlines, pages=pages)
    sections = serializeraw.load_sections(sections, pages=pages)
    # run algo
    detected = chapter.utils.content(words, sections)
    if not detected:
        # could not detect firstchapter, content
        intro = chapter.serialize.ChapterIntroInfo()
    else:
        content, firstchapter = detected
        found = chapter.intro.decide.run(content)
        intro = chapter.intro.decide.judge(found, firstchapter)
    # dump
    dumped = chapter.serialize.dump_chapter_introinfo(intro)
    return dumped
