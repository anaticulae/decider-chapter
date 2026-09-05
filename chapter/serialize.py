# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses

import utilo


@dataclasses.dataclass
class ChapterIntroInfo:
    pagestart: int = None
    pageend: int = None
    start: list = dataclasses.field(default_factory=list)
    goal: list = dataclasses.field(default_factory=list)
    method: list = dataclasses.field(default_factory=list)
    limit: list = dataclasses.field(default_factory=list)
    structure: list = dataclasses.field(default_factory=list)


def dump_chapter_introinfo(intro: ChapterIntroInfo) -> str:
    raw = dataclasses.asdict(intro)
    dumped = utilo.yaml_dump(raw)
    return dumped


def load_chapter_introinfo(path: str) -> ChapterIntroInfo:
    loaded = utilo.yaml_load(path)
    result = ChapterIntroInfo(**loaded)
    return result
