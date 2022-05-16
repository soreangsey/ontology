# -*- coding: utf-8 -*- 

import wx
import wx.xrc


###########################################################################
## Class First page
###########################################################################

class ResultPage(wx.Frame):

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Home", pos=wx.DefaultPosition, size=wx.Size(1050, 676),
                          style=wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.MINIMIZE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, -1),
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)
        runQuery = SparqlQueries()

        m_listBox1Choices = runQuery.search()
        self.m_listBox1 = wx.ListBox(self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, -1),
                                     m_listBox1Choices, wx.LB_SINGLE)
        bSizer7.Add(self.m_listBox1, 0, wx.ALL, 5)

        self.m_scrolledWindow1.SetSizer(bSizer7)
        self.m_scrolledWindow1.Layout()
        bSizer5.Add(self.m_scrolledWindow1, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 0)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow2 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow2.SetScrollRate(5, 5)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        bSizer8.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.m_scrolledWindow2.SetSizer(bSizer8)
        self.m_scrolledWindow2.Layout()
        bSizer8.Fit(self.m_scrolledWindow2)
        bSizer6.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer6, 1, wx.EXPAND, 0)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_listBox1.Bind(wx.EVT_LISTBOX_DCLICK, self.LoadResult)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def LoadResult(self, event):
        event.Skip()


###########################################################################
## Class Panel
###########################################################################

class MainPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Welcome", wx.DefaultPosition, wx.Size(-1, -1),
                                           wx.ALIGN_CENTRE)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        bSizer20.Add(self.m_staticText2, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_button1 = wx.Button(self.m_panel3, wx.ID_ANY, u"Continue", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer20.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_panel3.SetSizer(bSizer20)
        self.m_panel3.Layout()
        bSizer20.Fit(self.m_panel3)
        bSizer1.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.ShowNextFrame)

    def __del__(self):
        pass

    def ShowNextFrame(self, event):
        self.frame.Hide()
        new_frame = ResultPage()
        new_frame.Show()


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=u"Home", pos=wx.DefaultPosition, size=wx.Size(1050, 676),
                          style=wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.MINIMIZE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)
        panel = MainPanel(self)


class MainApp(wx.App):
    def OnInit(self):
        mainFrame = MainFrame()
        mainFrame.Show(True)
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
