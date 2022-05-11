# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib

import iamraw
import utila


def mainpart(sections):
    for item in sections.content:
        if not isinstance(item, iamraw.MainPart):
            continue
        return item
    return None


def select_chapter(sections, chapternumber: int = 0):
    assert chapternumber >= 0, f'invalid chapter number: {chapternumber}'
    main = mainpart(sections)
    if not main:
        return None
    chapters = []
    for item in main.content:
        if isinstance(item, iamraw.sections.Chapter):
            chapters.append(item.start)
            continue
    if len(main.content) > 1:
        chapters.append(main.content[-1].end)
    # select chapter by chapternumber
    with contextlib.suppress(IndexError):
        return chapters[chapternumber], chapters[chapternumber + 1]
    return None


def firstchapter(words, sections):
    first = select_chapter(
        sections,
        chapternumber=0,
    )
    if first is None:
        return None
    start, end = first
    selected = [
        utila.select_page(words, page)
        for page in utila.ranged_tuple(start, end)
    ]
    result = []
    for page in selected:
        if not page:
            # empty page?
            continue
        for section in page.content:
            result.append(section.headline)
            result.extend(section.content)
    return result, first
