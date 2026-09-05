# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum

import utilo


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


START = utilo.splitlines("""\
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
spielt im
ziehen sie gegenwärtig weite Kreise
""")

GOAL = utilo.splitlines("""\
Arbeit leiten wird
Der Schwerpunkt
Forschungsfragen
Fragestellung und Zielsetzung
Welche
Welche Aspekte
Wie gestaltet
Wie oft
Zentraler Bestandteil
Ziel
Ziel der folgenden Ausführungen
Ziel dieser Arbeit
folgende Forschungsfragen
wenig erforschtes Gebiet
zentrale Fragestellung
zu entwerfen
zu identifizieren
zu implementieren
""")

METHOD = utilo.splitlines("""\
Auswahlkriterium zur Stichprobenkonstruktion
Bearbeitung dieser Leitfrage
Hierfür wurde abgefragt
Im Zuge
Quotenauswahl
Stichprobe
Stichprobenart
Stichprobenumfang
Untersuchungsgebiete
demographischen Merkmalen
den Ansätzen
funktionalen Zugang
modular und leicht erweiterbar
repräsentative, standardisierte Kundenbefragung
soll anhand
sozioökonomische Daten
standardisierten Fragebogens
theoretische Strömungen
theoretischen Ansätze werden
verschiedenen Gruppen
zueinander in Beziehung gesetzt
""")

LIMIT = utilo.splitlines("""\
Arbeit nicht durchgeführt werden
Literatur bisher kaum verfolgt
Selten wird
Zeitrahmen
bewusst keinen Beitrag
festgestellt werden
kaum Ansätze zu finden
nicht möglich sein wird
sondern legt den Fokus
""")

STRUCTURE = utilo.splitlines("""\
Aufbau der Arbeit
Kapitel 1
Kapitel 2
Kapitel 3
Kapitel 4
Kapitel 5
beschreibt den
des vierten Teils
dritten Kapitel
erste Kapitel
fünfte Kapitel
gibt eine Einführung
gliedert sich in
in fünf Teile
stellt die wichtigsten
vierte Kapitel
werden Begriffe und Überlegungen
zweite Kapitel
zweiten Teil
""")

TODO = [
    (IntroType.START, START),
    (IntroType.GOAL, GOAL),
    (IntroType.METHOD, METHOD),
    (IntroType.LIMIT, LIMIT),
    (IntroType.STRUCTURE, STRUCTURE),
]
