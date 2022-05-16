import wx
import wx.adv

from MyFrame import MyFrame


# ----------------------------------------------------------------------#

class MySplashScreen(wx.adv.SplashScreen):
    """
Create a splash screen widget.
    """

    def __init__(self, parent=None):
        # This is a recipe to a the screen.
        # Modify the following variables as necessary.
        locale = wx.Locale(wx.LANGUAGE_ENGLISH)

        aBitmap = wx.Image(name="./splash1.png").ConvertToBitmap()
        wx.adv.SplashScreen.__init__(self, aBitmap, wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT, 5000, None,
                                     -1, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER | wx.STAY_ON_TOP)
        self.g1 = wx.Gauge(self, -1, 130, (0, 165), (580, 20))
        #        self.Bind(wx.EVT_CLOSE, self.OnExit)

        wx.Yield()
        self.Bind(wx.EVT_TIMER, self.TimerHandler)
        self.timer = wx.Timer(self)
        self.timer.Start(100)
        self.count = 0
        self.frame = MyFrame(None)

    def TimerHandler(self, event):
        self.count = self.count + 1
        if self.count >= 50:
            self.frame.Show()

            self.Destroy()

            self.timer.Stop()
        ##            self.frame.login_dlg = CreatePage.LoginDialog(self.frame)
        ##            self.frame.login_dlg.SetSize((422,295))
        ##            self.frame.login_dlg.ShowModal()

        self.g1.SetValue(self.count)

    # ----------------------------------------------------------------------#

    def OnExit(self, evt):
        self.Hide()
        self.timer.Stop()
        self.Destroy()
        # The program will freeze without this line.
#        evt.Skip()  # Make sure the default handler runs too...
# ----------------------------------------------------------------------#
