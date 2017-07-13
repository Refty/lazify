class LazyProxy(object):
    """Class for proxy objects that delegate to a specified function to evaluate
    the actual object.

    >>> def greeting(name='world'):
    ...     return 'Hello, %s!' % name
    >>> lazy_greeting = LazyProxy(greeting, name='Joe')
    >>> print(lazy_greeting)
    Hello, Joe!
    >>> u'  ' + lazy_greeting
    u'  Hello, Joe!'
    >>> u'(%s)' % lazy_greeting
    u'(Hello, Joe!)'

    This can be used, for example, to implement lazy translation functions that
    delay the actual translation until the string is actually used. The
    rationale for such behavior is that the locale of the user may not always
    be available. In web applications, you only know the locale when processing
    a request.

    The proxy implementation attempts to be as complete as possible, so that
    the lazy objects should mostly work as expected, for example for sorting:

    >>> greetings = [
    ...     LazyProxy(greeting, 'world'),
    ...     LazyProxy(greeting, 'Joe'),
    ...     LazyProxy(greeting, 'universe'),
    ... ]
    >>> greetings.sort()
    >>> for greeting in greetings:
    ...     print(greeting)
    Hello, Joe!
    Hello, universe!
    Hello, world!
    """
    __slots__ = ['_func', '_args', '_kwargs', '_value', '_is_cache_enabled']

    def __init__(self, func, *args, **kwargs):
        is_cache_enabled = kwargs.pop('enable_cache', True)
        # Avoid triggering our own __setattr__ implementation
        object.__setattr__(self, '_func', func)
        object.__setattr__(self, '_args', args)
        object.__setattr__(self, '_kwargs', kwargs)
        object.__setattr__(self, '_is_cache_enabled', is_cache_enabled)
        object.__setattr__(self, '_value', None)

    @property
    def value(self):
        if self._value is None:
            value = self._func(*self._args, **self._kwargs)
            if not self._is_cache_enabled:
                return value
            object.__setattr__(self, '_value', value)
        return self._value

    def __contains__(self, key):
        return key in self.value

    def __nonzero__(self):
        return bool(self.value)

    def __dir__(self):
        return dir(self.value)

    def __iter__(self):
        return iter(self.value)

    def __len__(self):
        return len(self.value)

    def __str__(self):
        return str(self.value)

    def __unicode__(self):
        return unicode(self.value)

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return other + self.value

    def __mod__(self, other):
        return self.value % other

    def __rmod__(self, other):
        return other % self.value

    def __mul__(self, other):
        return self.value * other

    def __rmul__(self, other):
        return other * self.value

    def __call__(self, *args, **kwargs):
        return self.value(*args, **kwargs)

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def __delattr__(self, name):
        delattr(self.value, name)

    def __getattr__(self, name):
        return getattr(self.value, name)

    def __setattr__(self, name, value):
        setattr(self.value, name, value)

    def __delitem__(self, key):
        del self.value[key]

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __copy__(self):
        return LazyProxy(
            self._func,
            enable_cache=self._is_cache_enabled,
            *self._args,
            **self._kwargs
        )

    def __deepcopy__(self, memo):
        from copy import deepcopy
        return LazyProxy(
            deepcopy(self._func, memo),
            enable_cache=deepcopy(self._is_cache_enabled, memo),
            *deepcopy(self._args, memo),
            **deepcopy(self._kwargs, memo)
        )


__all__ = ["LazyProxy"]
