from typing import Sequence
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMessageBox

from .dialog import Dialog
from ...src.tools import generateInputForm, generateComboBox
from ...src.consts import MSG_SHARE_PROFILE, SHARE_TYPE_EDIT, SHARE_TYPE_PROPERTY, SHARE_TYPE_VIEW
from ...src.structs import ShareProfile, Profile

class ShareProfileDialog(Dialog):

    def __init__(self, parent:QWidget=None, profiles:Sequence[Profile]=None, currentProfile:Profile=None):
        super().__init__('Compartilhar Perfil', self.BtnCancel | self.BtnSave, parent=parent)
        wid = QWidget(self.getParent())
        font = self.getFont()
        widPerfil, self.__comboPerfil, _ = generateComboBox('Perfil', wid, font)
        label = QLabel(MSG_SHARE_PROFILE, wid, wordWrap=True)

        widUsuario, self.__leUsuario, _ = generateInputForm('Usuário (login de acesso)', wid, font)
        if profiles: self.setProfiles(profiles)
        if currentProfile: self.setData(ShareProfile(None, currentProfile, None))

        widShareType, self.__comboShareType, _ = generateComboBox('Tipo de Compartilhamento', wid, font)
        self.__comboShareType.addItems(['Edição', 'Visualização', 'Transferência de Propriedade'])

        layout = QVBoxLayout(wid)
        layout.addWidget(widUsuario)
        layout.addWidget(widPerfil)
        layout.addWidget(widShareType)
        layout.addWidget(label)

        self.setWidget(wid)

    def isValid(self):
        return self.__leUsuario.text() and self.__comboPerfil.currentText()
    
    def alertNotValid(self):
        QMessageBox(QMessageBox.Warning, 'Validação de Parâmetros', 'Preencha todos os campos!').exec()
    
    def getData(self) -> ShareProfile:
        profileIndex = self.__comboPerfil.currentIndex()

        return ShareProfile(
            self.__leUsuario.text(),
            self.__profileByIndex[profileIndex] if profileIndex != -1 else None,
            self.__shareTypeIdFromText(self.__comboShareType.currentText())
        )

    def setData(self, d:ShareProfile):
        if d.profile not in self.__profileByIndex:
            raise ValueError('the profile is not a valid option')
        
        if d.username is not None : self.__leUsuario.setText(d.username)
        if d.shareType is not None: self.__comboShareType.setCurrentText(self.__shareTypeTextFromId(d.shareType))
        self.__comboPerfil.setCurrentIndex(self.__profileByIndex.index(d.profile))

    def setProfiles(self, options:Sequence[Profile]):
        self.__comboPerfil.clear()
        self.__comboPerfil.addItems([ p.name for p in options ])
        self.__profileByIndex = list(options)

    def __shareTypeTextFromId(self, shareType:int) -> str:
        if shareType == SHARE_TYPE_EDIT: return 'Edição'
        elif shareType == SHARE_TYPE_VIEW: return 'Visualização'
        elif shareType == SHARE_TYPE_PROPERTY: return 'Transferência de Propriedade'
        
        raise ValueError(f'the shareType {shareType} is not valid')

    def __shareTypeIdFromText(self, shareType:str) -> int:
        match shareType:
            case 'Edição': return SHARE_TYPE_EDIT
            case 'Visualização': return SHARE_TYPE_VIEW
            case 'Transferência de Propriedade': return SHARE_TYPE_PROPERTY

        raise ValueError(f'the shareType {shareType} is not valid')
