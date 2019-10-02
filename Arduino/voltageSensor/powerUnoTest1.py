from pyfirmata import Arduino, util
board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)
it.start()
board.analog[1].enable_reporting()
board.analog[1].read()
it.start()

'''
pinA1 = board.get_pin('a:1:i')`
pinA1.read()
'''
