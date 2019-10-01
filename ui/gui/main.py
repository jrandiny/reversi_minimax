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
from constant import *


class Handler(QObject):
    def __init__(self, moveQueue):
        super().__init__()
        self.moveQueue = moveQueue

    @Slot(int)
    def tileClicked(self, index):
        self.moveQueue.put({"x": index % 8, "y": index // 8})


class ioObject(QObject):
    interactCell = Signal(int, bool)
    setScore = Signal(int, int)
    setMark = Signal(bool)

    def __init__(self, root):
        super().__init__()
        board = root.findChild(QObject, "boardGame")
        self.interactCell.connect(board.interactCell)
        self.setScore.connect(root.setScore)
        self.setMark.connect(root.setMark)

    def send(self, index, isBlack):
        self.interactCell.emit(index, isBlack)

    def sendScore(self, whiteScore, blackScore):
        self.setScore.emit(whiteScore, blackScore)

    def sendMark(self, isBlackTurn):
        self.setMark.emit(isBlackTurn)


class QTUI(UIBase):
    def xyToIndex(self, x, y):
        return y * 8 + x

    def indexToXY(self, index):
        return (index % 8, index // 8)

    def ioThread(self, inputQueue, emitter):
        while True:
            io = inputQueue.get()

            if (io["type"] == UIMessageType.BOARD):
                for index in range(0, 64):
                    col, row = self.indexToXY(index)
                    item = io["data"][row][col]
                    if (item == BLACK):
                        emitter.send(index, True)
                    elif (item == WHITE):
                        emitter.send(index, False)
                time.sleep(0.2)

            elif (io["type"] == UIMessageType.SCORE):
                emitter.sendScore(io["data"]["o"], io["data"]["x"])
            elif (io["type"] == UIMessageType.TURN):
                turn = io["data"]
                if turn == "x":
                    emitter.sendMark(True)
                else:
                    emitter.sendMark(False)
            elif (io["type"] == UIMessageType.FORFEIT):
                print("Tidak ada langkah mungkin, skip")
            elif (io["type"] == UIMessageType.DOTURN):
                pass
            elif (io["type"] == UIMessageType.QUIT):
                break

            self.inputQueue.task_done()

    def threadWorker(self):
        self.app = QGuiApplication()
        self.view = QQuickView()
        self.view.setResizeMode(QQuickView.SizeRootObjectToView)

        #Load the QML file
        qml_file = os.path.join(os.path.dirname(__file__), "view.qml")
        self.view.setSource(QUrl.fromLocalFile(os.path.abspath(qml_file)))

        root = self.view.rootObject()

        ioHandler = Handler(self.moveQueue)
        context = self.view.rootContext()
        context.setContextProperty("handler", ioHandler)

        #Show the window
        if self.view.status() == QQuickView.Error:
            sys.exit(-1)

        ioSignaler = ioObject(root)

        input_thread = threading.Thread(target=self.ioThread,
                                        args=(self.inputQueue, ioSignaler))
        input_thread.start()

        self.view.show()
        self.app.exec_()

        self.inputQueue.put({"type": UIMessageType.QUIT})
        input_thread.join()
        self.outputQueue.put({"type": UICommandType.QUIT})
        self.moveQueue.put({"x": -1, "y": -1})
