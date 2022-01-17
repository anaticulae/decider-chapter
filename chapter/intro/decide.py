# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german

import chapter.intro.data
import chapter.serialize

FIELDS = 'start goal method limit structure'.split()


def judge(lines, ranges) -> chapter.serialize.ChapterIntroInfo:
    result = chapter.serialize.ChapterIntroInfo(
        pagestart=ranges[0],
        pageend=ranges[1],
    )
    for index, line in enumerate(lines):
        if not line:
            continue
        for ind, name in enumerate(FIELDS):
            if not line[ind]:
                continue
            getattr(result, name).append((index, line[ind]))
    return result


def run(sentences: list) -> list:
    result = []
    for sentence in sentences:
        if not isinstance(sentence, str):
            # headline
            sentence = sentence.title
            if sentence is None:
                # TODO: SHOULD NOT HAPPEN
                result.append(None)
                continue
        detected = analyse(sentence)
        if not any(detected):
            result.append(None)
            continue
        result.append(detected)
    return result


def analyse(sentence: str) -> tuple:
    result = []
    for _, tokens in chapter.intro.data.TODO:
        found = german.searches(
            tokens,
            sentence=sentence,
        )
        result.append(len(found))
    return result
