from PySide6.QtWidgets import QApplication

from ...views.components.shareProfileDialog import ShareProfileDialog
from ...src.structs import ShareProfile, Profile
from ...src.consts import SHARE_TYPE_EDIT

def shareProfileDialog():
    app = QApplication()
    dialog = ShareProfileDialog()

    currentProfile = Profile('1', None, 'Loja B', None, None, None, None, None, None)
    profiles = [
        Profile('0', None, 'Loja A', None, None, None, None, None, None),
        currentProfile,
        Profile('2', None, 'Loja C', None, None, None, None, None, None),
    ]

    dialog.setProfiles(profiles)
    dialog.setData(ShareProfile(
        'marcelo@email.com', currentProfile, SHARE_TYPE_EDIT
    ))

    dialog.exec()

    print(dialog.getData())
    app.quit()