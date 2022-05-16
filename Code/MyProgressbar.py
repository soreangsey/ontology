import time

import wx


class MyProgressbar(wx.Frame):

    def __init__(self, parent=None, frame):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='Agile Practices Selection', pos=wx.DefaultPosition,
                          size=wx.Size(740, 479), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL | wx.WANTS_CHARS)
        locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        self.frame_ = frame
        self.count = 0
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        self.gauge = wx.Gauge(pnl, range=20, size=(450, 25), style=wx.GA_HORIZONTAL)
        # self.btn1 = wx.Button(pnl, label = "Start")
        # self.Bind(wx.EVT_BUTTON, self.OnStart, self.btn1)

        hbox1.Add(self.gauge, proportion=1, flag=wx.ALIGN_CENTRE)
        # hbox2.Add(self.btn1, proportion = 1, flag = wx.RIGHT, border = 10)

        vbox.Add((0, 30))
        vbox.Add(hbox1, flag=wx.ALIGN_CENTRE)
        vbox.Add((0, 20))
        # vbox.Add(hbox2, proportion = 1, flag = wx.ALIGN_CENTRE)
        pnl.SetSizer(vbox)

        self.SetSize((500, 150))
        self.Centre()
        self.Show(True)

    def OnStart(self):

        while True:
            time.sleep(1);
            self.count = self.count + 1
            self.gauge.SetValue(self.count)

            if self.count >= 50:
                self.Destroy()
                return
