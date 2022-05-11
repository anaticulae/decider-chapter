# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import chapter

DESCRIPTION = ''

WORKPLAN = [
    utila.create_step(
        'intro',
        inputs=[
            utila.ResultFile('words', 'sentences_sentences'),
            utila.ResultFile('headlines', 'result_result'),
            utila.ResultFile('sections', 'section_result'),
        ],
        output=('intro',),
    ),
]


def main():
    utila.featurepack(
        workplan=WORKPLAN,
        root=chapter.ROOT,
        featurepackage='chapter.features',
        config=utila.FeaturePackConfig(
            description=DESCRIPTION,
            multiprocessed=True,
            name=chapter.PROCESS,
            pages=True,
            version=chapter.__version__,
        ),
    )
