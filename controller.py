import user_interface as ui
import module_import as mi
import module_export as me

def click():
    ui.welcome()
    if ui.choose() == 1:
        mi.write()
    else:
        me.read()