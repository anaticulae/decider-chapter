# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import chapter.utils


def content(words, sections):
    firstchapter = chapter.utils.select_chapter(sections, chapternumber=0)
    if firstchapter is None:
        return None
    start, end = firstchapter
    selected = [
        utila.select_page(words, page)
        for page in utila.ranged_tuple(start, end)
    ]
    result = []
    for page in selected:
        for section in page.content:
            result.append(section.headline)
            result.extend(section.content)
    return result, firstchapter
