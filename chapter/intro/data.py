# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum

import chapter.utils


class IntroType(enum.IntEnum):
    # Hinführung zum Thema
    START = enum.auto()
    # Gegenstand, Problemstellung und Ziele der Arbeit
    GOAL = enum.auto()
    # Gang der Untersuchung
    METHOD = enum.auto()
    # Abgrenzung der Arbeit
    LIMIT = enum.auto()
    # Aufbau der Arbeit
    STRUCTURE = enum.auto()


START = """\
Circa
Ein Beispiel dafür
Einleitung
Kritisch beurteilt wird
deuten an
erfreuen sich großer Beliebtheit
gegenwärtig weite Kreise
haben gut
kaum noch wegzudenken
sondern deuten auch an
ziehen sie gegenwärtig weite Kreise
"""
START = chapter.utils.init(START)

GOAL = """\
Arbeit leiten wird
Der Schwerpunkt
Fragestellung und Zielsetzung
Zentraler Bestandteil
Ziel der folgenden Ausführungen
wenig erforschtes Gebiet
zentrale Fragestellung
"""
GOAL = chapter.utils.init(GOAL)

METHOD = """\
Bearbeitung dieser Leitfrage
den Ansätzen
funktionalen Zugang
theoretische Strömungen
theoretischen Ansätze werden
zueinander in Beziehung gesetzt
"""
METHOD = chapter.utils.init(METHOD)

LIMIT = """\
Arbeit nicht durchgeführt werden
Literatur bisher kaum verfolgt
Selten wird
bewusst keinen Beitrag
kaum Ansätze zu finden
sondern legt den Fokus
"""
LIMIT = chapter.utils.init(LIMIT)

STRUCTURE = """\
Aufbau der Arbeit
des vierten Teils
dritten Kapitel
erste Kapitel
fünfte Kapitel
gliedert sich in
in fünf Teile
vierte Kapitel
werden Begriffe und Überlegungen
zweite Kapitel
zweiten Teil
"""
STRUCTURE = chapter.utils.init(STRUCTURE)

TODO = [
    (IntroType.START, START),
    (IntroType.GOAL, GOAL),
    (IntroType.METHOD, METHOD),
    (IntroType.LIMIT, LIMIT),
    (IntroType.STRUCTURE, STRUCTURE),
]
