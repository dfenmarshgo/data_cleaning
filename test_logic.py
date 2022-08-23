from mylib.logic import wiki


def test_wiki():
    assert (
        "god" in wiki()
    )  # The reason for this is to try to test the specific application
