import pytest
import stanza

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
    reocognized_lemmas = [
        'if', 'you', 'want', 'to', 'see', 'g', 'rpc', 'in', 'action', 'first',
        ',', 'visit', 'the', 'python', 'Quickstart', '.'
    ]
    a_record = {
        'deprel': 'mark',
        'head': 3,
        'id': '1',
        'lemma': 'if',
        'misc': 'start_char=0|end_char=2',
        'text': 'If',
        'upos': 'SCONJ',
        'xpos': 'IN'
    }
    res = usecase.recognize(sent)
    assert isinstance(res, list)

    assert len(res) == 1
    assert len(res[0]) == len(reocognized_lemmas)
    # assert res[0][0] == a_record
    # assert [r.get('lemma') for r in res[0]] == reocognized_lemmas
    """case
    If multiple sentence was input, this function return 
    """
    sent = """If you want to see gRPC in action first, visit the Python Quickstart. 
            Or, if you would like dive in with more extensive usage of gRPC Python, check gRPC Basics - Python out.
            """

    # recognized =
    res = usecase.recognize(sent)
    assert isinstance(res, list)
    # assert
    """case
    If sentence is empty, this function return 
    """
