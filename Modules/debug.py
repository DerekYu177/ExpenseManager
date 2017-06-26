import shared

def show_sys_path():
    import sys
    for path in sys.path:
        print path
