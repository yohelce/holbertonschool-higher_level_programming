#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as exc:
        sys.stderr.write("Exception: " + str(exc) + "\n")
        return None
