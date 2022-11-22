import sys
sys.dont_write_bytecode = True

from code_runner import CodeRunner
from queue.queue import Queue
from pepper_connection import PepperConnection
from blockly_connection import server
from queue.program_object import Program