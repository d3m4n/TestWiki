from ..wiki_analyzer import WikiAnalyzer


DEST = 'http://wikipedia.org/wiki/Philosophy'


def test_basic():
    """ Straightforward test """
    src = 'https://en.wikipedia.org/wiki/Art'
    w = WikiAnalyzer(src, DEST)
    assert (['Art', 'Human_behavior', 'Motion_(physics)',
            'Physics', 'Natural_science', 'Science',
            'Knowledge', 'Awareness',
            'Conscious', 'Quality_(philosophy)'] == w.path)


def test_dest():
    """ Test with src == dest """
    src = 'https://en.wikipedia.org/wiki/Philosophy'
    w = WikiAnalyzer(src, DEST)
    assert [] == w.path


def test_stress():
    """ Test a page with a large number of links and a strange structure """
    src = 'https://en.wikipedia.org/wiki/Star_Wars'
    w = WikiAnalyzer(src, DEST)
    assert (['Star_Wars', 'Epic_film', 'Genre',
             'Literature', 'Culture',
             'Edward_Burnett_Tylor',
             'Anthropologist',
             'Knowledge',
             'Awareness',
             'Conscious',
             'Quality_(philosophy)'] == w.path)


def test_parenthesis():
    """ Test a page with nested parenthesis """
    src = 'https://en.wikipedia.org/wiki/Genre'
    w = WikiAnalyzer(src, DEST)
    assert 'Literature' == w.path[1]
