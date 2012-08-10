#!/usr/bin/env python

import sys

from PySide import QtCore, QtGui

from word_count import count_words_in_file

class WordTableModel(QtCore.QAbstractTableModel):
    def setWords(self, word_count_dict):
        self.word_count = word_count_dict.items()
    def rowCount(self, index):
        return len(self.word_count)
    def columnCount(self, index):
        return len(self.word_count[0])
    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.word_count[index.row()][index.column()]
        return None

def main(args=None):
    if args is None:
        args = sys.argv
    app = QtGui.QApplication(args)
    win = QtGui.QWidget()
    layout = QtGui.QVBoxLayout(win)
    file_tuple = QtGui.QFileDialog.getOpenFileName(
        parent=win,
        caption='Open file for which to count words')
    file_name = file_tuple[0]
    word_count = count_words_in_file(file_name)
    model = WordTableModel()
    model.setWords(word_count)
    table_view = QtGui.QTableView(win)
    table_view.setModel(model)
    layout.addWidget(table_view)
    win.setLayout(layout)
    win.showMaximized()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
