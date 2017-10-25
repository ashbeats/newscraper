y = ('left-center', 'fakenews', 'propaganda', 'extremeright', 'high', 'left', 'center', 'mixed',
     'conspiracy', 'hate', 'right-center', 'right', 'veryhigh', 'bias', 'satire', 'low', 'unreliable',
     'pro-science')


def label_cleaner():
    key = {
        'fakenews': 'fake news',
        'extremeright': 'extreme right',
        'veryhigh': 'very high credibility',
        'low': 'low credibility',
        'pro-science': 'pro science',
        'mixed': 'mixed credibility'
    }
    for label in y:
        for k, v in key.items():
            label = label.replace(k, v)
        yield label.title().replace('high', 'high credibility')


# print(list(label_cleaner()))

from sys import argv

print(argv)