from zope.interface import Interface
import warnings


class ISubtyped(Interface): 
    warnings.warn('Subtyper is no longer available', DeprecationWarning)
