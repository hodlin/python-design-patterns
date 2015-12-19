class Singleton(object):
    """
    Classic Singleton implementation

    Ex.:
    >>> singleton = Singleton()
    >>> another_singleton = Singleton()
    >>> singleton is another_singleton
    True
    >>> singleton.only_one_var = "I'm only one var"
    >>> another_singleton.only_one_var
    I'm only one var
    """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class Child(Singleton):
    """
    Child of classic Singleton

    Ex.:
    >>> singleton = Singleton()
    >>> child = Child()
    >>> child is singleton
    False
    """
    pass
