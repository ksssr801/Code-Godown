import time
import re
import os
import stat
import logging
import logging.handlers as handlers
import zipfile
import glob


class SizedTimedRotatingFileHandler(handlers.TimedRotatingFileHandler):
    """
    Handler for logging to a set of files, which switches from one file
    to the new zip file when the current file reaches a certain size, or at certain
    timed intervals.
    """

    def __init__(self, filename, maxBytes=0, backupCount=0, encoding=None,
                 delay=0, when='h', interval=1, utc=False):
        handlers.TimedRotatingFileHandler.__init__(
            self, filename, when, interval, backupCount, encoding, delay, utc)
        self.maxBytes = maxBytes
        self.filename = filename

    def shouldRollover(self, record):
        """
        Determine if rollover should occur.

        Basically, see if the supplied record would cause the file to exceed
        the size limit we have.
        """
        if self.stream is None: # delay was set...
            self.stream = self._open()

        if self.backupCount > 0:
            # It will find the oldest log file and delete it.
            s = glob.glob(self.filename + ".20*")
            if len(s) > self.backupCount:
                s.sort()
                os.remove(s[0])

        if self.maxBytes > 0: # are we rolling over?
            msg = "%s\n" % self.format(record)
            
            # due to non-posix-compliant Windows feature
            self.stream.seek(0, 2)
            if self.stream.tell() + len(msg) >= self.maxBytes:
                ts = self.rolloverAt - self.interval
                zip_file_name = self.filename + "." + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(ts))
                if os.path.exists(zip_file_name + ".zip"):
                    os.remove(zip_file_name + ".zip")
                file = zipfile.ZipFile(zip_file_name + ".zip", "w")
                file.write(self.filename, os.path.basename(zip_file_name), zipfile.ZIP_DEFLATED)
                file.close()
                os.remove(self.filename)
                return 1

        # Time based rollover
        # t = int(time.time())
        # if t >= self.rolloverAt:
        #     return 1
        return 0

def create_log_handler(file_name='debug.log', log_msg='', log_size_limit=0, back_up_count=0, log_interval_type='s', log_interval=0):
    logger = logging.getLogger('MyLogger')
    logger.setLevel(logging.DEBUG)
    handler = SizedTimedRotatingFileHandler(file_name, maxBytes=log_size_limit, when=log_interval_type, backupCount=back_up_count, interval=log_interval)
    logger.addHandler(handler)
    logger.debug(log_msg)

# create_log_handler()