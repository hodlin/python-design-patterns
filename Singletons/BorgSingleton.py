class Borg(object):
    """
    Borg singleton implementation

    Ex.:
    >>> borg = Borg()
    >>> another_borg = Borg()
    >>> borg is another_borg
    False
    """
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class Child(Borg):
    """
     Child of classic Borg

    Ex.:
    >>> borg = Borg()
    >>> child = Child()
    >>> borg.only_one_var = "I'm the only one var"
    >>> child.only_one_var
    I'm the only one var
    """
    pass
