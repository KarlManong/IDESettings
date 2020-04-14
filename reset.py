# coding=utf-8
import os
import sys
import shutil

products = ["DataGrip", "IntelliJIdea", "PyCharm"]
eval_dir = "eval"
options = ["options.xml", "other.xml"]


def reset_windows():
    try:
        old_type_dir = os.getenv("USERPROFILE")
        do_reset(old_type_dir, "config")
        new_type_dir = os.path.join(os.getenv("APPDATA"), "JetBrains")
        do_reset(new_type_dir)

        import winreg

        delete_sub_key(winreg.HKEY_CURRENT_USER, r"Software\JavaSoft\Prefs\jetbrains")
        delete_sub_key(winreg.HKEY_CURRENT_USER, r"Software\Jetbrains")
    except:
        import traceback
        traceback.print_exc()


def delete_sub_key(key0, current_key, sub_key="", arch_key=0):
    import winreg
    if sub_key:
        current_key = current_key + "\\" + sub_key

    try:
        open_key = winreg.OpenKey(key0, current_key, 0, winreg.KEY_ALL_ACCESS | arch_key)
        info_key = winreg.QueryInfoKey(open_key)
        for x in range(0, info_key[0]):
            # NOTE:: This code is to delete the key and all sub_keys.
            # If you just want to walk through them, then
            # you should pass x to EnumKey. sub_key = winreg.EnumKey(open_key, x)
            # Deleting the sub_key will change the sub_key count used by EnumKey.
            # We must always pass 0 to EnumKey so we
            # always get back the new first sub_key.
            sub_key = winreg.EnumKey(open_key, 0)
            try:
                winreg.DeleteKey(open_key, sub_key)
                print("Removed key %s\\%s " % (current_key, sub_key))
            except OSError:
                delete_sub_key(key0, current_key, sub_key)
                # No extra delete here since each call
                # to delete_sub_key will try to delete itself when its empty.

        winreg.DeleteKey(open_key, "")
        open_key.Close()
        print("Removed key %s" % current_key)
    except FileNotFoundError:
        pass


def do_reset(base_dir, sub_dir=""):
    for dir_ in os.listdir(base_dir):
        for p in products:
            if p in dir_:
                current_dir = os.path.join(base_dir, dir_)
                if sub_dir:
                    current_dir = os.path.join(current_dir, sub_dir)
                try:
                    eval_dir_ = os.path.join(current_dir, eval_dir)
                    print("Deleted directory " + eval_dir_)
                    shutil.rmtree(eval_dir_)
                except FileNotFoundError:
                    pass
                options_dir = os.path.join(current_dir, "options")
                for opt in options:
                    try:
                        option_file = os.path.join(options_dir, opt)
                        print("Deleted file " + option_file)
                        os.remove(option_file)
                    except FileNotFoundError:
                        pass


def reset_linux():
    do_reset(os.getenv("HOME"), "config")
    new_type_dir = os.path.join(os.getenv("HOME"), ".config", "JetBrains")
    do_reset(new_type_dir)
    os.remove(os.path.join(os.getenv("HOME"), ".java", ".userPrefs", "prefs.xml"))
    shutil.rmtree(os.path.join(os.getenv("HOME"), ".java", ".userPrefs", "jetbrains"))


def reset():
    if sys.version_info > (3,):
        if sys.platform.startswith("win"):
            reset_windows()
        elif sys.platform.startswith("linux"):
            reset_linux()
        else:
            pass
    else:
        print(u"请用python3运行")


if __name__ == "__main__":
    reset()
