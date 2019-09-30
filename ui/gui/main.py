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
from ui_base import UIBase, UICommandType, UIMessageType
from queue import Queue


class Handler(QObject):
    def __init__(self, moveQueue):
        super().__init__()
        self.moveQueue = moveQueue

    @Slot(int)
    def tileClicked(self, index):
        self.moveQueue.put({"x": index % 8, "y": index // 8})


class QTUI(UIBase):
    def ioThread(self, inputQueue):
        while True:
            io = inputQueue.get()

            if (io["type"] == UIMessageType.BOARD):
                print(io["data"])
            elif (io["type"] == UIMessageType.SCORE):
                print(io["data"])
            elif (io["type"] == UIMessageType.TURN):
                turn = io["data"]
                print(f"Sekarang giliran {turn}")
            elif (io["type"] == UIMessageType.FORFEIT):
                print("Tidak ada langkah mungkin, skip")
            elif (io["type"] == UIMessageType.DOTURN):
                print('do turn')
            elif (io["type"] == UIMessageType.QUIT):
                break

            self.inputQueue.task_done()

    def threadWorker(self):
        self.app = QGuiApplication(sys.argv)
        self.view = QQuickView()
        self.view.setResizeMode(QQuickView.SizeRootObjectToView)

        #Load the QML file
        qml_file = os.path.join(os.path.dirname(__file__), "view.qml")
        self.view.setSource(QUrl.fromLocalFile(os.path.abspath(qml_file)))

        root = self.view.rootObject()
        self.board = root.findChild(QObject, "boardGame")

        handler = Handler(self.moveQueue)
        context = self.view.rootContext()
        context.setContextProperty("handler", handler)

        print(self.board.getCell(3).spawn())
        # self.cell.spawn()

        #Show the window
        if self.view.status() == QQuickView.Error:
            sys.exit(-1)

        threading.Thread(target=self.ioThread,
                         args=(self.inputQueue, )).start()

        self.view.show()
        self.app.exec_()
        del self.view