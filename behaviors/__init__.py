import sys
sys.dont_write_bytecode = True

from expressions import PepperExpression
from movement import ArmGesture, HeadGesture, HipGesture, PepperMove
from speech import PepperSpeech
from composite_handler import CompositeHandler