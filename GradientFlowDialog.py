"""!
Created on Jan 07, 2025
@author: Chetan Kumar Jain

This module contains the implementation of the GradientPanel class, which displays a gradient progress bar.
"""

import wx


class GradientPanel(wx.Panel):

    def __init__(self, parent, size=(25, 300)):
        """
        Initializes the GradientPanel with a specified parent and size.

        This panel displays a gradient progress bar with a specified size and
        initializes the necessary brushes for drawing the progress and remaining areas.

        Parameters:
        parent (wx.Window): The parent window for this panel.
        size (tuple): A tuple specifying the height and width of the panel. Default is (25, 300).

        Returns:
        None
        """
        wx.Panel.__init__(self, parent, size=size)
        self.height = size[0]
        self.width = size[1]
        self.progress = 0
        self.progressWidth = 0
        # Create gradient brushes for progress and remaining areas
        self.progressBrush = wx.GraphicsContext.Create().CreateLinearGradientBrush(0, -9, 0, 9,
                                                                                   wx.GraphicsGradientStops(wx.BLACK,
                                                                                                            wx.GREEN))
        self.remainingBrush = wx.GraphicsContext.Create().CreateLinearGradientBrush(0, -9, 0, 9,
                                                                                    wx.GraphicsGradientStops(wx.BLACK,
                                                                                                             wx.WHITE))
        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.SetProgress(self.progress)
        self.SetSize((self.width, self.height))

    def SetProgress(self, progress):
        """
        Sets the progress value for the gradient panel and updates the width of the progress bar.

        Ensures that the progress value is clamped between 0 and 100, and calculates the width
        of the progress bar based on the current progress.

        Parameters:
        progress (int): The progress value to set, expected to be between 0 and 100.

        Returns:
        None
        """
        # Ensure progress is within 0-100 range
        if progress < 0:
            progress = 0
        if progress > 100:
            progress = 100
        width = self.width * progress / 100
        if width < 1:
            width = 1
        self.progressWidth = width
        self.progress = progress

    def OnPaint(self, evt):
        """
        Handles the paint event for the panel, drawing the progress and remaining areas.

        This method is called whenever the panel needs to be repainted. It draws the
        remaining area and the progress area using the pre-defined gradient brushes,
        and displays the current progress percentage as text.

        Parameters:
        evt (wx.PaintEvent): The paint event object.

        Returns:
        None
        """
        dc = wx.PaintDC(self)
        gc = wx.GraphicsContext.Create(dc)

        # Draw remaining area
        gc.SetBrush(self.remainingBrush)
        gc.SetPen(wx.Pen('red', 0, wx.PENSTYLE_SOLID))
        gc.DrawRectangle(-1, -1, self.width, self.height)

        # Draw progress area
        gc.SetBrush(self.progressBrush)
        gc.SetPen(wx.Pen('red', 1, wx.PENSTYLE_SOLID))
        w, h = gc.GetSize()
        gc.DrawRectangle(-1, -1, self.progressWidth, h)

        # Draw progress text
        dc.SetFont(wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        dc.DrawText(str(self.progress) + "%", 150, 3)


class GradientFlowDialog(wx.Dialog):
    backgroundColor = "LTGRAY"

    def __init__(self, message):
        """
        Initializes the GradientFlowDialog window with a specified message.

        This constructor sets up the dialog window, including a gradient progress bar,
        a label displaying the provided message, and a cancel button. It also initializes
        the necessary attributes for tracking the progress and handling user cancellation.

        Parameters:
        message (str): The message to display in the dialog, typically informing the user
                       about the ongoing process.

        Returns:
        None
        """
        super(GradientFlowDialog, self).__init__(None, title="Progress", style=wx.CAPTION | wx.STAY_ON_TOP,
                                                 size=(320, 124))
        self.keepCalculating = True
        pnl = wx.Panel(self)
        hbox1 = wx.BoxSizer(wx.VERTICAL)
        self.gaugePanel = wx.Panel(pnl, size=(300, 25), style=wx.BORDER)
        self.gauge = GradientPanel(self.gaugePanel, size=(25, 300))
        self.label = wx.StaticText(pnl, label=message)
        self.buttonCancel = wx.Button(pnl, label="Cancel")
        self.SetBackgroundColour(self.backgroundColor)
        hbox1.Add(self.label, flag=wx.ALIGN_LEFT | wx.ALL, border=5)
        hbox1.Add(self.gaugePanel, flag=wx.ALIGN_LEFT | wx.ALL, border=5)
        hbox1.Add(wx.StaticLine(pnl, size=(300, 2), style=wx.LI_HORIZONTAL), flag=wx.ALIGN_CENTRE)
        hbox1.Add(self.buttonCancel, flag=wx.ALIGN_LEFT | wx.RIGHT, border=5)
        self.Bind(wx.EVT_BUTTON, self.OnCancel, self.buttonCancel)
        pnl.SetSizer(hbox1)

    def UpdateValue(self, progress):
        """
        Updates the progress value displayed on the gradient panel and refreshes the panel.

        This method sets the progress value for the gradient panel and triggers a refresh
        to visually update the progress bar.

        Parameters:
        progress (int): The progress value to set, expected to be between 0 and 100.

        Returns:
        None
        """
        self.gauge.SetProgress(progress)
        self.gaugePanel.Refresh()

    def OnCancel(self, event):
        """
        Handles the cancel button event, showing a confirmation dialog to the user.

        When the cancel button is clicked, this method displays a confirmation dialog
        asking the user if they are sure they want to cancel the operation. If the user
        confirms, the calculation process is stopped.

        Parameters:
        event (wx.CommandEvent): The event object associated with the button click.

        Returns:
        None
        """
        dlg = wx.MessageDialog(self, " Are you sure you want to cancel ? ",
                               "Confirm Cancel", wx.OK | wx.CANCEL | wx.ICON_INFORMATION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.keepCalculating = False
