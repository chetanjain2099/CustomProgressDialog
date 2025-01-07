import threading, time
import wx

from GradientFlowDialog import GradientFlowDialog


class MainFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        """
        Initializes the MainFrame window and starts a worker thread to perform tasks.

        This constructor sets up the main frame of the application, initializes a
        GradientFlowDialog to display progress, and starts a separate thread to handle
        time-consuming tasks.

        Parameters:
        parent (wx.Window): The parent window for this frame.
        ID (int): The identifier for the frame.
        title (str): The title of the frame.

        Returns:
        None
        """
        wx.Frame.__init__(self, parent, ID, title)
        self.gFr = GradientFlowDialog(message="Processing can take a few minutes. Please wait...")
        self.gFr.Center()
        # Start the worker thread
        workThread = threading.Thread(target=self.doWork)
        workThread.start()
        self.gFr.ShowModal()

    def doWork(self):
        """
        Performs time-consuming tasks and updates the progress dialog.

        This method runs in a separate thread, simulating a long-running process by
        sleeping for a short duration in a loop. It updates the progress dialog with
        the current progress and checks if the user has requested to cancel the operation.

        Parameters:
        None

        Returns:
        None
        """
        for i in range(0, 100):
            time.sleep(0.05)
            if not self.gFr.keepCalculating:
                break
            wx.CallAfter(self.gFr.UpdateValue, i+1)
        wx.CallAfter(self.gFr.Destroy)
        wx.CallAfter(self.Destroy)


# Initialize the application
app = wx.App(False)
fr = MainFrame(None, -1, "Title")
app.MainLoop()
