import shared

def show_sys_path():
    if shared.global_variables.DEBUG:
        import sys
        for path in sys.path:
            print path
