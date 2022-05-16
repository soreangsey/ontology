# -*- coding: utf8 -*-
'''


@author: Soreangsey Kiv
'''

import wx

from MySplashScreen import MySplashScreen

if __name__ == '__main__':
    app = wx.App(False)

    MySplash = MySplashScreen(None)
    # frame = MyFrame(None)
    MySplash.Show()

    # app.SetTopWindow(frame)
    # frame.Show()

    app.MainLoop()
