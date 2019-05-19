#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import sys
from workflow import Workflow3

__author__ = 'hua.xiao'


# Workflow3 supports Alfred 3's new features. The `Workflow` class
# is also compatible with Alfred 2.


def main(wf):
    # The Workflow3 instance will be passed to the function
    # you call from `Workflow3.run`.
    # Not super useful, as the `wf` object created in
    # the `if __name__ ...` clause below is global...
    #
    # Your imports go here if you want to catch import errors, which
    # is not a bad idea, or if the modules/packages are in a directory
    # added via `Workflow3(libraries=...)`

    # Get args from Workflow3, already in normalized Unicode.
    # This is also necessary for "magic" arguments to work.
    args = wf.args

    # Do stuff here ...
    import time

    # Add an item to Alfred feedback
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    current_time_stamp = int(time.time())
    wf.add_item(current_time, current_time_stamp)

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but subsequent calls
    # are ignored (otherwise the JSON sent to Alfred would be invalid).
    wf.send_feedback()


if __name__ == '__main__':
    # Create a global `Workflow3` object
    wf = Workflow3()
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))
