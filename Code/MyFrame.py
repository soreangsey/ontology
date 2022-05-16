import wx
import wx.aui
from wx.lib.embeddedimage import PyEmbeddedImage

import CreatePage

# --------------------------------------------------- #
# Some bitmaps for ribbon buttons

align_center = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAABHNCSVQICAgIfAhkiAAAADpJ"
    "REFUKJFjZGRiZqAEMFGkm4GBgQWZ8//f3//EaGJkYmaEsyn1Ags2QVwuQbaZNi4YDYMRGwYU"
    "ZyYAopsYTgbXQz4AAAAASUVORK5CYII=")

# ----------------------------------------------------------------------
align_left = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAABHNCSVQICAgIfAhkiAAAADxJ"
    "REFUKJFjZGRiZqAEMFGkm4GBgYWBgYHh/7+//4lRzMjEzIghRqkX8LoAm430dQExLhoNg2ER"
    "BhRnJgDCqhhOM7rMkQAAAABJRU5ErkJggg==")

# ----------------------------------------------------------------------
align_right = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAABHNCSVQICAgIfAhkiAAAADdJ"
    "REFUKJFjZGRiZqAEMFGkm4GBgQWb4P9/f/8To5mRiZmRkVIvYHUBsS6inQtGw2DEhQHFmQkA"
    "gowYTpdfxvkAAAAASUVORK5CYII=")

# ----------------------------------------------------------------------
aui_style = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAMFJ"
    "REFUWIXtlrENgzAUBQ/beAQWYAcGYYIkgyWZxz2lF0CiRwJBCmKJIlGq+DV+lS1ZutO39eSq"
    "MpaU5+O+kyGX661Ka3eG932fgw+wJwmTi/gtRcCdN9u2aQWWZdEKzPOsFVjXVSsguYJz++Wc"
    "QOI6gLZtAZimKQs88WKMh0CMMQv4UxxA0zQS+DiOh4D3XiIA7wkYo2tkB2Ct/XXuvwJ1XWsF"
    "5BOQv4FhGLQCXddJ4CEE/Y+oCBSBIlAEHByNpMoLu1w1qHGIod8AAAAASUVORK5CYII=")

# ----------------------------------------------------------------------
auto_crop_selection = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAi5J"
    "REFUWIXFlz1r20AYx/+ns4PjR7jG1IgG2tIO/QAdkyyZOvcrlECnQujWT9AtFDIF+h06dcjU"
    "KaFTxg4dWwiIBNU1d8Y0Ol0H+8TpxUKKpOgPB7Is7vfoebtHjDkcXcrplA4AzOFYe0ED0Pd9"
    "zUwIdKQ0czhr/Y3XMjxWlAP3YVScAzpSOg0/9g8z95uS2Tc3CQ0cAE5vjuKH2zAmNsC42oYT"
    "d0Gc8OXvR+hI6TNx0pgRhpebhDpS+vTmCMQJ5LgAgOHamP3tN2giLwwvNwTM4eztw08ZOHG3"
    "LjejTAjs368ffEjAyaHGwIZXWAVn4qQVeIJnd0Jzne6O9ko/Q/vfM/fKLKQ7YVXRwaWeTAZw"
    "iUNIhSBYQn57WTk579SK6eBSP3lM2PG2MB71MJuHuPL/4ddvWdoIw+tVtRgAJpMBdrwtPH86"
    "gDftw7++BQAIqSAr7rWxCjZpuHuuXeIYj3rwpn28eLYNb9rHeNSDSxzD3fNSjcrwYg+UDcHi"
    "Yo+JRz/0bB7Gb+5f32I2DyGkwuJir/0QBMESV7TKneBPGOdAECwr79V5FRT2gTIrrw+gRP9A"
    "ug80NXzoSOmf4VcAgIwkpBKQSuKV+y6R6JnDqOnJpwhu8zaeBU3BF0rE84T9TOFEVNsAC74y"
    "SCQmK1uthMC43cClWnnEnjELJ6K6MnuZyUquPfHe+5wY/ZjDWe0yLHPsHvuHmVJE3eP4Lh7J"
    "+6+VKkgrD547EaHLb8Ou9B/kXYasrB2oNQAAAABJRU5ErkJggg==")

# ----------------------------------------------------------------------
auto_crop_selection_small = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAASRJ"
    "REFUOI2lkzFLw1AUhb+XdOvQiiAqgqAgLeJSWo0RG+iiOBRcXV3t6OIPEHfnQPUPFERxExRK"
    "i7gLXUSoo4hDxuQ62AsSQxPaAw8u7753OOdwrwGECWEs2+S0AJAoFK3TIFEoAJZerDhz0uo0"
    "kSgUbWZBTtkOTmtseRvM3y0y6A65vrjPRGCphcvDG957n3iNTfJ2PquAXwWKQXfIR/+Ll6dX"
    "AAqOL9/949RMxFg28VN02+KcvEnRbSf29Z+VxFhwfClVPPYbM5QqHgXHHxvqVArMqEj0qRnU"
    "dtelWi8ThAFX57cYyzY6M4kWFBpgtV7m6GyPtZ2lf2/GEiiCMODx4Znl7Vl02FIziPsFpNVp"
    "yqq7IJkziOPvrmhtmHIbzUjOxPgBMl93hZvH4+AAAAAASUVORK5CYII=")

# ----------------------------------------------------------------------
circle = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAANtJ"
    "REFUWIXNV8sSxCAIA/z/T67d0864PiBQ2ZpbHQkxlGKZpVAEtV53+yxSOMLDqIA+oQVUkCnA"
    "m9grRDKTIxxLAUhykcKI1RrXtARagJXQGzsIWBF433KU50fALCjaXiinoBujmHG0udQu+AeE"
    "KO/0Gtc35xkODIsbT29xvu/Ajs9tFLVe9+BAhv0a9/sl6BcySzJv90TLLYgUPq8ERDllWE7H"
    "3Ym8ECJ7Yj2FNmvOcIAozwVr0p51JbOCESGPL6UIUU/o2QsLQIkRaK6pXZB1KW1x/s8pKijq"
    "1gcd75B9JbWfpAAAAABJRU5ErkJggg==")

# ----------------------------------------------------------------------
circle_small = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAHxJ"
    "REFUOI2lU0EOwCAIg/r/J6u7TKMVgWXcDG2paFVRxKrWal/PQFELpyzARC4WQjSVCYyZDtbG"
    "za6FQZbMvcHBDZARERFBtDSvWqt9OshMt7DwgCmx1U6WtC/9g/VjOoq6HymaLvJewXrfiDw4"
    "WxZuAfKC9TtMh0DkhusBDWJQP2fEFKMAAAAASUVORK5CYII=")

# ----------------------------------------------------------------------
colours = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAAOklE"
    "QVQokWNgIBEwMjAwXJJiwpTQefgPU5CJlQGLUvxgRGpgYWBgiNiHReJu3H9s6hkHoR8GoQaS"
    "AQBoQQZvRwyakAAAAABJRU5ErkJggg==")

# ----------------------------------------------------------------------
cross = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAO9J"
    "REFUWIXNl9sOAyEIRIHu/39xU/epiXVRhltSX3ZNZOZoDCCzvGge4/MeLBdTw9C0ZV0wf6vN"
    "NW1ZF+zmFebaXE5mFRCWNhMN0yR6J5ANCCIeOQkkhuVi+f5UQqDmRNMlrILwmP8AVEB4zR8A"
    "GYiIuQoQgYiaExHxmop3Jplx2pB6AkhghbkJkIVAYk2AKAQaAwF4ITxrYYCuAQNUp2IXQFcx"
    "ggAyuQAqx13mqMYWAE2v2QKmAnhzewbiARAtLFEItS33mmcgtm151MALcWzLvcIRiP9vyzvL"
    "sdmWdzYkZlte+UI+aattecfzfKd9AzzryGWicE3pAAAAAElFTkSuQmCC")

# ----------------------------------------------------------------------
empty = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAANElE"
    "QVQokWNgIBEwMjAw/P//H84/efIkHtUWFhZMpNpAew0sDKjuNjc3H2gnjWqgiQaSAQBRvgke"
    "qvN6jAAAAABJRU5ErkJggg==")

# ----------------------------------------------------------------------
expand_selection_h = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAVFJ"
    "REFUWIXtVjFuwzAMJCmjQGrv/UH27vlB9j4gyAvykC5eCz+gewbv3rvnB93lGihCsUNqQ1Ys"
    "x0nUJgZ8AGFapOgTKVFGJAW3BN306xOBURIQwyKGpU//UwIAAEgK66etXxRrdMewL83/VoKQ"
    "uL8SnNrN19i67OQ65Tr1070SuU6PSDYExLAUVdYiY0s93nfcbJtvflFlLRKIpEAMy8f3O5Ss"
    "oeQSvlhDaQ56yRo2T29NcDEsPhK2TQzL6+caYpVArGKIKYHHWlcJPD+8AJJCEsOy228HJjEc"
    "dvstiGE5+xgOLcFQEJLCebQcPCFUI5pHywNhJAW/vUCKKpNcpwIAR2L71borrp8ruU6lqLJW"
    "vKYESAoXsxXY77bY475VuX5d8xezVdvP7YR1Gofs9HNtXXGjvlWEhC/u/d0FpzBdx6ExzhL4"
    "/ooviTW+EkwEQuMHDB37+4Mc8HwAAAAASUVORK5CYII=")

# ----------------------------------------------------------------------
expand_selection_v = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAATtJ"
    "REFUWIXtlzGOwjAQRb8dhISCRMkN6OnpKaho9gArWho6TkBHQ4v2ADRbpaCnp88NtlyJCAnF"
    "HqqAozhoPfEmIPElS04cj59mbE9GCBmAK9KKAEDIQHBtyCqLx2mEOI1uIBwJjgdIKzpedrl3"
    "w/YHyxPOAKQVHc5f1rFR59MZwgmAtKL9afPwm3F37gThDJD1v39XubFpb3k36gDQ+vPqhmHS"
    "ihJ9Kh13kROAqUQl3Km+AIoe4Ih9DK3G6jiGvsW+Cb1JyKDQABAA+q9+rtlCQFpRlQRTJpvd"
    "59wDVbLbI9nsNr4J3yEoDUH2MWlFvvq2dZ4zBHWKlQ19JiN2Ol7/zHLPi/6WZYcNEAZd7lRf"
    "AGH9AGbsQ1n0AKdSeq3f8gyiscLEhGisNDMh4jQCAAxaE3aFXOkq9lGeXwGxGs15gJjjygAA"
    "AABJRU5ErkJggg==")

# ----------------------------------------------------------------------
eye = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAJNJ"
    "REFUOI3NkjEOwjAQBOdsoE7pwj+gyCP4f0HBD67gDUHJUkRGhkRIlgtYyZJ13h3pzmcWIj0K"
    "Xem/ABw+C1pmfQtYiLYLKEF3ByDnDGlaH++nuq4aZBYiWmYVQx0ez0cArrfHG6R4CkTu/jqA"
    "SJPGiwSDYFjvadKet3uI3S1Y2cSGIbIZYq3Wb9wAWvX7Ve4GPAEieGRem+OF/wAAAABJRU5E"
    "rkJggg==")

# ----------------------------------------------------------------------
hexagon = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAALNJ"
    "REFUWIXt180NgCAMBlALG7ILU7gLGxo9aWL4a/uV6KE9Q/sAxUoU4vZlBGRyjuXMsZxIDtLs"
    "QK/ofiRaCuCuVgJhAWYrRnZkCJAm1kCaAPSMJfNfAMuHi5vvAbQGawtzIHduohCrAVaFZ5D9"
    "SFRdRKuK93JDN6FFOMABDnCAAyoA2mSOopX7H5/j0UAEImpIpBPRwkOAFmLWlEoTL2vLuRBN"
    "YRVgBln+a9aDIK8rBLCICxjaeOXhD450AAAAAElFTkSuQmCC")

# ----------------------------------------------------------------------
msw_style = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAOhJ"
    "REFUWIVjZGRiZkAGU3c8+c9AQ5DtIcOIzGdBtzzaSoCW9jMw7HjyH9kRjLAQmLrjyf8oS37a"
    "Wg4Fy45/hIcESgj8+UcX+1EAigN+/x1gB/yjafIbdQARDvg/AA5gZGRiZpi648l/D31+BkZG"
    "whqoAf7/Z2DYcRGSFRl7Nj36H2QuQh+b0cC6k28YmAbEZiTAwsDAwPD0xfMBsp4V4gAJUfGB"
    "sf/hO4gD/vwdgDIYCgaHA778+DOwDvg7EEUgsgPoVgLhcgDjiHfAaBQMuANGo2DAQ+De6+8D"
    "5oABb5CMOgDaJBu4NAAAvuND/BvGPIIAAAAASUVORK5CYII=")

# ----------------------------------------------------------------------
position_left = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAABHNCSVQICAgIfAhkiAAAAExJ"
    "REFUKJHtkzEKwDAMA0/yx/z/P7XqVOiQDmmHLDEIBEKCGyy5yHmEDyeXACIX3YlcPP2dvQkI"
    "QEblqYFRuTuZGtgIG2EpguR/33gBsoRzDlCsBR0AAAAASUVORK5CYII=")

# ----------------------------------------------------------------------
position_top = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAABHNCSVQICAgIfAhkiAAAAFJJ"
    "REFUKJHtkzEKwDAMA092H5b//ylRppRCpzhToTd50RljJEXi0U0BRQrAiqQ1W5HszIABXAkr"
    "kltQCb8E3z1By1Llev5zF4/uONkO8AtAp22caOhgKT6Nla4AAAAASUVORK5CYII=")

# ----------------------------------------------------------------------
ribbon = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAYxJ"
    "REFUOI19krtKA0EUhr8xMcYbRIJgk87KBSsRBK0UROMi6y3Wig+wpLQTLMUHsLNSBEVCIoKd"
    "gpAyEBBMISKIiDeSmLhqxiLuZrPjeqrhXH6+c/4RoiWAX2iGKQHyR9vCryf43+D4zBLWtwTw"
    "FRJeAs0wpbEQ5+4Jql8BIl1tTu385EARCXqHB0bihIKwuxH+zdZY2xQIIRibWgSQbpEWL1Jf"
    "j+S5VH/ryQp6ssLOuvS5gItAM0w5ObtMb1eRd6ueS221O0JVq41wKKhQOAT5o21xerzHQ7GV"
    "SGeDwI630ge1mlTuoKzQHQ5RsRppPVkhtdVOTcJb+UNZ4U8XVlfmuX385LX0xUu5UStkM4oL"
    "ioAtAqDP6Vzff3N1mXHW9PYqH0kzTDk0bhDpCJE63AdgQk/wWr+s/JdAM0zZPzzt4E7oCQDO"
    "Uvu4826RJhsHR+O8Ww3Pbx6KynqDo/EmkiYbcxdpYlFBIZtRBgvZDLGoIHeR/pvAFrHVNcOU"
    "sWi9r+Cp+d7AHbYTHnElfgAFJbH0Sf7mkQAAAABJRU5ErkJggg==")

# ----------------------------------------------------------------------
selection_panel = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAHlJ"
    "REFUOI3tk8EOwzAIQx+w307Dtu9u3UsS9bamuc4Ski8GjIyZByvwJTVA20CAnvBXb5SZAHp/"
    "vla3ol9cx666FWEemAeZqc7vVmbKzAMdu8zDZqx3zThiW28KdSvydsip6VfN30LYUhJHDrof"
    "gEvibvHR4CmWv/EExjdqKKO2QxEAAAAASUVORK5CYII=")

# ----------------------------------------------------------------------
square = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAEdJ"
    "REFUWIXt1zEOACAIQ9FC9P4HNinOuhsGPyNLXxoWouRS42RnOABJGvcic8bLQHsdN9feAAAA"
    "AAAAAAAAAAAAAILf8HvABvIMCjlFTCZ2AAAAAElFTkSuQmCC")

# ----------------------------------------------------------------------
triangle = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAALFJ"
    "REFUWIXVl0EOgCAMBFvq/39s8ERCyCKwIJY9EYG2M9GDqsGETbzvKCKiZsrWCHT3RaEHSPTl"
    "etsAq0INgIhZC+cZyEnVTPMvgLFwloGSHq1HLZxjoEaPno1YOMNAix7t9Vrwb6CXHp3pseDb"
    "wCg9Otuy4NcAS4/uvFnwaWCWHt2tWfBnYBU9qoEs+DKwmh7VKi34MfAVPaqZ9/JhYObPhk3q"
    "eb1t7ohKlO30eX5/Bx4qMXoN5ex1NgAAAABJRU5ErkJggg==")


# --------------------------------------------------- #

class ColourClientData(object):

    def __init__(self, name, colour):
        self._name = name
        self._colour = colour

    def GetName(self):
        return self._name

    def GetColour(self):
        return self._colour


# --------------------------------------------------- #

def CreateBitmap(xpm):
    bmp = eval(xpm).Bitmap

    return bmp


# --------------------------------------------------- #

class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='OBAMA - Ontology Based for Agile Methods Adoption',
                          pos=wx.DefaultPosition, size=wx.Size(740, 479),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL | wx.WANTS_CHARS)
        locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        self.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))
        ####declaration of variable
        self.generalResult = []
        self.result = []
        self.resultByTeam = []
        self.situationList = []
        self.practiceList = []
        self.principleList = []
        self.valueList = []
        self.runQuery = None

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow(self)
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT | wx.aui.AUI_BUTTON_MINIMIZE)
        # self.scale = languageConversion.Conversion(self.lstr)

        self.SetIcon(wx.Icon('agile.ico', wx.BITMAP_TYPE_ICO, 16, 16))

        # self._ribbon = MyRibbonBar(self)

        # self.m_mgr.AddPane( self._ribbon, wx.aui.AuiPaneInfo() .Top() .CaptionVisible( False ).CloseButton( False ).Dock().Resizable().DockFixed(True) )

        self.m_auinotebook1 = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                 wx.aui.AUI_NB_DEFAULT_STYLE | wx.aui.AUI_NB_BOTTOM | wx.aui.AUI_NB_CLOSE_ON_ACTIVE_TAB)
        self.m_mgr.AddPane(self.m_auinotebook1, wx.aui.AuiPaneInfo().Center().CaptionVisible(False).CloseButton(
            False).Dock().Resizable().FloatingSize(wx.DefaultSize).DockFixed(False))
        self.m_auinotebook1.SetBackgroundColour(wx.Colour(240, 248, 255))
        self.m_auinotebook1.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        ##
        ##
        ##        # ADD CONTRLS
        self.welcomePage = CreatePage.welcomePage(self.m_auinotebook1, self)
        self.m_auinotebook1.AddPage(self.welcomePage, "Welcome page")

        self.resultpage1 = CreatePage.ResultPage1(self.m_auinotebook1, self)
        self.m_auinotebook1.AddPage(self.resultpage1, "All the information related to practice")

        self.input_page1 = CreatePage.InputPage1(self.m_auinotebook1, self)
        self.m_auinotebook1.AddPage(self.input_page1, "Input page 1")

        self.input_page2 = CreatePage.InputPage2(self.m_auinotebook1, self)
        self.m_auinotebook1.AddPage(self.input_page2, "Input page 2")

        self.resultpage2 = CreatePage.ResultPage2(self.m_auinotebook1, self)
        self.m_auinotebook1.AddPage(self.resultpage2, "Information related to practice based on input")

        print("Done")

### our normal wxApp-derived class, as usual
##app = wx.PySimpleApp()
##
##frame = MyFrame(None)
##app.SetTopWindow(frame)
##frame.Show()
##
##app.MainLoop()
