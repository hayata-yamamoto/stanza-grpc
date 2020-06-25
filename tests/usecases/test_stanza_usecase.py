import pytest
import stanza
import json

from src.usecases.stanza_usecase import StanzaUsecase


@pytest.fixture(scope='module')
def stanza_pipeline():
    return stanza.Pipeline('en')


def test_init(stanza_pipeline):
    usecase = StanzaUsecase(stanza_pipeline)
    assert isinstance(usecase, StanzaUsecase)


def test_recognize(stanza_pipeline):
    usecase = StanzaUsecase(stanza_pipeline)
    """case
    If a single sentence was input, this function return 
    """
    sent = "If you want to see gRPC in action first, visit the Python Quickstart."

    # TOOD: This may raise error because of pretrained model update.
    correct = '[[{"id": "1", "text": "If", "lemma": "if", "upos": "SCONJ", "xpos": "IN", "head": 3, "deprel": "mark", "misc": "start_char=0|end_char=2"}, {"id": "2", "text": "you", "lemma": "you", "upos": "PRON", "xpos": "PRP", "feats": "Case=Nom|Person=2|PronType=Prs", "head": 3, "deprel": "nsubj", "misc": "start_char=3|end_char=6"}, {"id": "3", "text": "want", "lemma": "want", "upos": "VERB", "xpos": "VBP", "feats": "Mood=Ind|Tense=Pres|VerbForm=Fin", "head": 12, "deprel": "advcl", "misc": "start_char=7|end_char=11"}, {"id": "4", "text": "to", "lemma": "to", "upos": "PART", "xpos": "TO", "head": 5, "deprel": "mark", "misc": "start_char=12|end_char=14"}, {"id": "5", "text": "see", "lemma": "see", "upos": "VERB", "xpos": "VB", "feats": "VerbForm=Inf", "head": 3, "deprel": "xcomp", "misc": "start_char=15|end_char=18"}, {"id": "6", "text": "g", "lemma": "g", "upos": "NOUN", "xpos": "NN", "feats": "Number=Sing", "head": 7, "deprel": "compound", "misc": "start_char=19|end_char=20"}, {"id": "7", "text": "RPC", "lemma": "rpc", "upos": "NOUN", "xpos": "NN", "feats": "Number=Sing", "head": 5, "deprel": "obj", "misc": "start_char=20|end_char=23"}, {"id": "8", "text": "in", "lemma": "in", "upos": "ADP", "xpos": "IN", "head": 9, "deprel": "case", "misc": "start_char=24|end_char=26"}, {"id": "9", "text": "action", "lemma": "action", "upos": "NOUN", "xpos": "NN", "feats": "Number=Sing", "head": 7, "deprel": "nmod", "misc": "start_char=27|end_char=33"}, {"id": "10", "text": "first", "lemma": "first", "upos": "ADV", "xpos": "RB", "head": 5, "deprel": "advmod", "misc": "start_char=34|end_char=39"}, {"id": "11", "text": ",", "lemma": ",", "upos": "PUNCT", "xpos": ",", "head": 12, "deprel": "punct", "misc": "start_char=39|end_char=40"}, {"id": "12", "text": "visit", "lemma": "visit", "upos": "VERB", "xpos": "VB", "feats": "Mood=Imp|VerbForm=Fin", "head": 0, "deprel": "root", "misc": "start_char=41|end_char=46"}, {"id": "13", "text": "the", "lemma": "the", "upos": "DET", "xpos": "DT", "feats": "Definite=Def|PronType=Art", "head": 15, "deprel": "det", "misc": "start_char=47|end_char=50"}, {"id": "14", "text": "Python", "lemma": "python", "upos": "PROPN", "xpos": "NNP", "feats": "Number=Sing", "head": 15, "deprel": "compound", "misc": "start_char=51|end_char=57"}, {"id": "15", "text": "Quickstart", "lemma": "Quickstart", "upos": "PROPN", "xpos": "NNP", "feats": "Number=Sing", "head": 12, "deprel": "obj", "misc": "start_char=58|end_char=68"}, {"id": "16", "text": ".", "lemma": ".", "upos": "PUNCT", "xpos": ".", "head": 12, "deprel": "punct", "misc": "start_char=68|end_char=69"}]]'
    res = usecase.recognize(sent)
    assert isinstance(res, str)
    assert res == correct
    """case
    If sentence is empty, this function return 
    """
    sent = ""
    res = usecase.recognize(sent)
    assert isinstance(res, str)
    assert "" == res
