from contextlib import contextmanager
# Создание своего  именованного окружения изоляторов WITH


@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")


with tag('h1'):
    print("Hello!")

# <h1>
# Hello!
# </h1>
