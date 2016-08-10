"""A module for demonstrating Exceptions"""

def convert(s):
    '''Convert to an integer.'''
    try:
         return int(s)
    except (ValueError, TypeError) as e:
        print("Coversion error: {}"\
        .format(str(e)),
        file=sys.stderr)
        return - 1
