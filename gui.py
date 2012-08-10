#!/usr/bin/env python

import sys

from PySide import QtGui

from word_count import count_words_in_file

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
    for word, count in word_count.iteritems():
        label = QtGui.QLabel('{0}: {1}'.format(word, count))
        layout.addWidget(label)
    win.setLayout(layout)
    win.show()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
