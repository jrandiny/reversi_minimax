#!/usr/bin/env python
# -*- conding: utf-8 -*-
import sys
import os
import time
import threading
import PySide2.QtQml
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QObject, Signal, Slot, QUrl
from PySide2.QtGui import QGuiApplication
from ui_base import UIBase, UICommandType
from queue import Queue


class Handler(QObject):
    def __init__(self, commandQueue):
        super().__init__()
        self.commandQueue = commandQueue

    @Slot(int)
    def tileClicked(self, index):
        print(index)
        self.commandQueue.put({
            "type": UICommandType.MOVE,
            "data": {
                "x": index % 8,
                "y": index // 8
            }
        })


class QTUI(UIBase):
    def threadWorker(self):
        app = QGuiApplication(sys.argv)
        view = QQuickView()
        view.setResizeMode(QQuickView.SizeRootObjectToView)

        #Load the QML file
        qml_file = os.path.join(os.path.dirname(__file__), "view.qml")
        view.setSource(QUrl.fromLocalFile(os.path.abspath(qml_file)))

        root = view.rootObject()
        self.board = root.findChild(QObject, "boardGame")

        handler = Handler(self.outputQueue)
        context = view.rootContext()
        context.setContextProperty("handler", handler)

        # self.board
        print(self.board.getCell(3).spawn())
        # self.cell.spawn()
        #Show the window
        if view.status() == QQuickView.Error:
            sys.exit(-1)
        view.show()

        # self.outputQueue.put({
        #     "type": UICommandType.MOVE,
        #     "data": {
        #         "x": 1,
        #         "y": 1
        #     }
        # })

        app.exec_()
        del view
