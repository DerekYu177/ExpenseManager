def prompt_user_for_location():
    import Tkinter as tk
    from tkFileDialog import askdirectory

    tk_prompt = tk.Tk()
    tk_prompt.withdraw()
    return askdirectory()
