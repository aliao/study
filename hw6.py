"""Submission for CS61A Homework 6.

Name:
Login:
Collaborators:
"""

# Q1 (and part of Q2).

class Bank:
    """A Bank capable of creating accounts."""

    def __init__(self):
        self.accounts = []

    def make_account(self, balance):
        account = Account(self, balance)
        self.accounts.append(account)
        return account

    def make_secure_account(self, balance, password):
        account = SecureAccount(self, balance, password)
        self.accounts.append(account)
        return account

    def total_deposits(self):
        total = 0
        for i in self.accounts:
            total += i.balance()
        return total

class Account:
    """ An account in a particular bank.

    >>> third_national = Bank()
    >>> second_federal = Bank()
    >>> acct0 = third_national.make_account(1000)
    >>> acct0.withdraw(100)
    >>> acct1 = third_national.make_account(2000)
    >>> third_national.total_deposits()
    2900
    >>> second_federal.total_deposits()
    0
    >>> acct1.total_deposits()
    Traceback (most recent call last):
       ...
    AttributeError: 'Account' object has no attribute 'total_deposits'
    >>> acct1.bank().total_deposits()
    2900
    """


    def __init__(self, bank, balance):
        self._bank = bank
        self._balance = balance

    def balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            return 'Insufficient funds'
        else:
            self._balance -= amount

    def deposit(self, amount):
        self._balance += amount

    def bank(self):
        return self._bank


# Q2

class SecurityError(BaseException):
    """Exception to raise if there is an attempted security violation."""
    pass

class SecureAccount(Account):
    """An account that provides password security.
    >>> third_national = Bank()
    >>> acct3 = third_national.make_secure_account(1000, "The magic woid")
    >>> acct3.deposit(1000, 'The magic woid')
    >>> acct3.balance('The magic woid')
    2000
    >>> acct3.balance('Foobar')
    Traceback (most recent call last):
       ...
    hw6.SecurityError: wrong passphrase or account
    >>> acct3.balance()
    Traceback (most recent call last):
       ...
    hw6.SecurityError: passphrase missing
    """

    def __init__(self, bank, balance, password):
        self._bank = bank
        self._balance = balance
        self._password = password

    def password_ok(self, password):
        if password == self._password:
            return True
        elif password == '':
            raise SecurityError('passphrase missing')
        else:
            raise SecurityError('wrong passphrase or account')

    def balance(self, password=''):
        if self.password_ok(password):
            return self._balance

    def withdraw(self, amount, password=''):
        if self.password_ok(password):
            super().withdraw(amount)

    def deposit(self, amount, password=''):
        if self.password_ok(password):
            super().deposit(amount)


# Q3 and Q4

"*** YOUR CODE HERE ***"
    

class rlist:
    """A recursive list consisting of a first element and the rest.
    
    >>> s = rlist(1, rlist(2, rlist(3)))
    >>> len(s)
    3
    >>> s[0]
    1
    >>> s[1]
    2
    >>> s[2]
    3
    >>> for x in s:
    ...     print(x)
    1
    2
    3
    """
    class Empty_rlist:
        def __init__(self):
            pass

        def __len__(self):
            return 0

        def __repr__(self):
            return 'rlist.empty()'


    empty_rlist = Empty_rlist()

    @classmethod
    def empty(cls):
        return cls.empty_rlist

    def __init__(self, x, L=empty_rlist):
        self.__first = x
        self.__rest = L

    def first(self):
        return self.__first

    def rest(self):
        return self.__rest

    def __len__(self):
        return 1 + self.rest().__len__()

    def __getitem__(self, k):
        if k == 0:
            return self.first()
        else:
            return self.rest().__getitem__(k - 1)

    def __iter__(self):
        class Iterator:
            def __init__(self, arlist):
                self.__arlist = arlist
                self.i = 0

            def __next__(self):
                if self.i < len(self.__arlist):
                    item = self.__arlist.__getitem__(self.i)
                    self.i += 1
                    return item
                else:
                    raise StopIteration()
        return Iterator(self)

    def __repr__(self):
        """A printed representation of self that resembles a Python
        expression that reproduces the same list.  The builtin function
        repr(x) calls x.__repr__().  The Python interpreter uses __repr__
        to print the values of non-null expressions it evaluates."""
        f = repr(self.first())
        if self.rest() is rlist.empty():
            return 'rlist({0})'.format(f)
        else:
            return 'rlist({0}, {1})'.format(f, repr(self.rest()))


# Q5.

class Monitor:
    """A general-purpose wrapper class that counts the number of times each
    attribute of a monitored object is accessed.

    >>> B = Bank()
    >>> acct = B.make_account(1000)
    >>> mon_acct = Monitor(acct)
    >>> mon_acct.balance()
    1000
    >>> for i in range(10): mon_acct.deposit(100)
    >>> mon_acct.withdraw(20)
    >>> mon_acct.balance()
    1980
    >>> mon_acct.access_count('balance')
    2
    >>> mon_acct.access_count('deposit')
    10
    >>> mon_acct.access_count('withdraw')
    1
    >>> mon_acct.access_count('clear')
    0
    >>> L = list(mon_acct.attributes_accessed())
    >>> L.sort()
    >>> L
    ['balance', 'deposit', 'withdraw']
    """

    def __init__(self, obj):
        self.__obj = obj
        self.__attributes_counts = {}

    def __getattr__(self, attr):
        self.__attributes_counts.setdefault(attr, 0)
        self.__attributes_counts[attr] += 1
        return self.__obj.__getattribute__(attr)

    def access_count(self, attr):
        return self.__attributes_counts.get(attr, 0)

    def attributes_accessed(self):
        return self.__attributes_counts.keys()




# Q6.

class Abbrev:
    """An abbreviation map."""

    def __init__(self, full_names):
        """Initialize self to handle abbreviations for the words
        in the sequence of strings full_names.  It is an error if
        a name appears twice in full_names."""
        if len(full_names) != len(set(full_names)):
            raise ValueError('A name appears twice in full_names')
        else:
            self.__full_names = full_names.copy()

    def complete(self, cmnd):
        """The member of my word list that the string cmnd
        abbreviates, if it exists and is unique.  cmnd abbreviates
        a string S in my word list if cmnd == S, or cmnd is a
        prefix of S and of no other command in my word list.
        Raises ValueError if there is no such S.
        >>> a = Abbrev(['continue', 'catch', 'next', 
        ...             'st', 'step', 'command'])
        >>> a.complete('ne')
        'next'
        >>> a.complete('co')
        Traceback (most recent call last):
           ...
        ValueError: not unique: 'co'
        >>> a.complete('st')
        'st'
        >>> a.complete('foo')
        Traceback (most recent call last):
           ...
        ValueError: unknown command: 'foo'
        """
        if cmnd in self.__full_names:
            return cmnd
        else:
            match = 0
            commands = []
            for i in self.__full_names:
                if i.startswith(cmnd):
                    match += 1
                    commands.append(i)
            if match == 0:
                raise ValueError("unknown command: '{}'".format(cmnd))
            elif match > 1:
                raise ValueError("not unique: '{}'".format(cmnd))
            else:
                return commands[0]

    def minimal_abbreviation(self, cmnd):
        """The string, S, of shortest length such that
        self.complete(S) == cmnd.  
        >>> a = Abbrev(['continue', 'catch', 'next', 
        ...             'st', 'step', 'command'])
        >>> a.minimal_abbreviation('continue')
        'con'
        >>> a.minimal_abbreviation('next')
        'n'
        >>> a.minimal_abbreviation('step')
        'ste'
        >>> a.minimal_abbreviation('ste')
        Traceback (most recent call last):
           ...
        ValueError: unknown command: 'ste'
        """
        if cmnd in self.__full_names:
            for i in range(1, len(cmnd)):
                match = 0
                result = []
                cmnd_start = cmnd[0:i]
                for j in self.__full_names:
                    if j.startswith(cmnd_start):
                        match += 1
                        result.append(cmnd_start)
                if match == 1:
                    return result[0]
        else:
            raise ValueError("unknown command: '{}'".format(cmnd))

# Q7 Extra for Experts.

class ArgumentMonitor:
    """A general-purpose wrapper class that counts the number of times each
    method of a monitored object is called with each unique argument list.

    >>> B = Bank()
    >>> acct = B.make_account(1000)
    >>> mon_acct = ArgumentMonitor(acct, ['balance', 'withdraw', 'deposit'])
    >>> mon_acct.balance()
    1000
    >>> for i in range(10): mon_acct.deposit(100)
    >>> mon_acct.withdraw(20)
    >>> mon_acct.withdraw(10)
    >>> mon_acct.balance()
    1970
    >>> d = mon_acct.argument_counts('balance')
    >>> d[()]
    2
    >>> d = mon_acct.argument_counts('deposit')
    >>> list(d.items())
    [((100,), 10)]
    >>> d = mon_acct.argument_counts('withdraw')
    >>> d[(10,)]
    1
    >>> d[(20,)]
    1
    """

    def __init__(self, obj, operations):
        """An ArgumentMonitor that monitors the methods named in
        operations for obj."""
        self.__operations = operations.copy()
        self.__obj = obj
        self.__argument_counts = {}
        for i in operations:
            self.__argument_counts[i] = {}

    def __getattr__(self, attr):
        def wrapper(*args):
            self.__argument_counts[attr].setdefault(tuple(args), 0)
            self.__argument_counts[attr][tuple(args)] += 1
            return self.__obj.__getattribute__(attr)(*args)
        if attr in self.__operations:
            return wrapper

    def argument_counts(self, attr):
        return self.__argument_counts[attr]





