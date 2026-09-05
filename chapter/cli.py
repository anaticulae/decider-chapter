# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import chapter

DESCRIPTION = ''

WORKPLAN = [
    utilo.create_step(
        'intro',
        inputs=[
            utilo.ResultFile('words', 'sentences_sentences'),
            utilo.ResultFile('headlines', 'result_result'),
            utilo.ResultFile('sections', 'section_result'),
        ],
        output=('intro',),
    ),
]


def main():
    utilo.featurepack(
        workplan=WORKPLAN,
        root=chapter.ROOT,
        featurepackage='chapter.features',
        config=utilo.FeaturePackConfig(
            description=DESCRIPTION,
            multiprocessed=True,
            name=chapter.PROCESS,
            pages=True,
            version=chapter.__version__,
        ),
    )
