import genpy
from time import time


class Time(genpy.Time):
    """
    Time represents the ROS 'time' primitive type, which consists of two
    integers: seconds since epoch and nanoseconds since seconds. Time
    instances are mutable.
    The L{Time.now()} factory method can initialize Time to the
    current ROS time and L{from_sec()} can be used to create a
    Time instance from the Python's time.time() float seconds
    representation.
    The Time class allows you to subtract Time instances to compute
    Durations, as well as add Durations to Time to create new Time
    instances.
    Usage::
      now = rospy.Time.now()
      zero_time = rospy.Time()
      print 'Fields are', now.secs, now.nsecs
      # Time arithmetic
      five_secs_ago = now - rospy.Duration(5) # Time minus Duration is a Time
      five_seconds  = now - five_secs_ago  # Time minus Time is a Duration
      true_val = now > five_secs_ago
      # NOTE: in general, you will want to avoid using time.time() in ROS code
      import time
      py_time = rospy.Time.from_sec(time.time())
    """
    __slots__ = []

    def __init__(self, secs=0, nsecs=0):
        """
        Constructor: secs and nsecs are integers and correspond to the
        ROS 'time' primitive type. You may prefer to use the static
        L{from_sec()} and L{now()} factory methods instead.

        @param secs: seconds since epoch
        @type  secs: int
        @param nsecs: nanoseconds since seconds (since epoch)
        @type  nsecs: int
        """
        super(Time, self).__init__(secs, nsecs)

    def __repr__(self):
        return 'rospy.Time[%d]' % self.to_nsec()

    @staticmethod
    def now():
        """
        Create new L{Time} instance representing current time. This
        can either be wall-clock time or a simulated clock. It is
        strongly recommended that you use the now() factory to create
        current time representations instead of reading wall-clock
        time and create Time instances from it.

        @return: L{Time} instance for current time
        @rtype: L{Time}
        """
        return get_rostime()

    @classmethod
    def from_seconds(cls, float_secs):
        """
        Use Time.from_sec() instead. Retained for backwards compatibility.

        @param float_secs: time value in time.time() format
        @type  float_secs: float
        @return: Time instance for specified time
        @rtype: L{Time}
        """
        return cls.from_sec(float_secs)


def get_rostime():
    """
    Get the current time as a L{Time} object
    @return: current time as a L{rospy.Time} object
    @rtype: L{Time}
    """
    float_secs = time()
    secs = int(float_secs)
    nsecs = int((float_secs - secs) * 1000000000)
    return Time(secs, nsecs)
