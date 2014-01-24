from zope import interface
from dateable.chronos import interfaces
from OFS.SimpleItem import SimpleItem
import warnings 

class CalendarSupport(SimpleItem):
    """
    """

    interface.implements(interfaces.ICalendarSupport)

    @property
    def support_enabled(self):
        warnings.warn('CalendarSupport is no longer available', DeprecationWarning)
        return False
