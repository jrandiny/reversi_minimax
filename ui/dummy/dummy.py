from ui_base import UIBase, UIMessageType


class DummyUI(UIBase):
    def threadWorker(self):
        while True:
            io = self.inputQueue.get()

            if (io["type"] == UIMessageType.QUIT):
                break

            self.inputQueue.task_done()