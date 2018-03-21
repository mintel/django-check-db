import contextlib
import math
import signal
import time

from django.core.management.base import BaseCommand
from django.db import connections


class Command(BaseCommand):
    help = "Test that connections can be established to all databases."

    def add_arguments(self, parser):
        parser.add_argument(
            '-t', '--timeout',
            type=int,
            default=1,
            help="Max number of seconds to wait for each connection. "
                 "If 0, will wait indefinitely.",
        )

    def handle(self, *args, **options):
        timeout = options['timeout']
        for db_name in connections.databases:
            connection = connections[db_name]
            start_time = time.time()
            end_time = start_time + timeout
            remaining_time = timeout
            while (not timeout  # timeout == 0: wait forever
                   or remaining_time > 0):
                try:
                    with alarm_timeout(remaining_time):
                        cursor = connection.cursor()
                        cursor.execute("SELECT 1")
                        cursor.fetchone()
                        break
                except Exception:
                    pass
                remaining_time = math.ceil(end_time - time.time())  # round up to nearest second
            else:
                raise Exception(db_name + 'timed out')
            self.stderr.write(self.style.SUCCESS(db_name + ' OK'))


@contextlib.contextmanager
def alarm_timeout(timeout):
    """Exit on timeout, even during blocking IO calls."""
    if timeout != 0:
        signal.alarm(int(timeout))  # must be an int
        yield
        signal.alarm(0)  # disable alarm
    else:
        # timeout == 0: wait forever
        yield
