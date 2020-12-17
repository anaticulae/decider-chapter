# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german

import chapter.intro.data


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
        if max(detected) == 0:
            result.append(None)
            continue
        maxindex = detected.index(max(detected))
        maxed = chapter.intro.data.TODO[maxindex][0]
        result.append(maxed)
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
