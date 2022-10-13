from widgets.AgreementDialog import AgreementDialog
from .UI import PasswordDialogUi

from utils import Strings
from .util import centralizate


class PasswordDialog(AgreementDialog, PasswordDialogUi):
    def __init__(self, parent=None, text=Strings.MainUi.agreement_use_pass):
        super().__init__(parent, text)

        self.setFixedSize(self.label.sizeHint().width() + 40,
                          111)
        self.password_input.setGeometry(20, 35, self.label.sizeHint().width(), 30)
        self.buttonBox.setGeometry(centralizate(self.width(), self.buttonBox.width()), 75, self.buttonBox.width(), 30)