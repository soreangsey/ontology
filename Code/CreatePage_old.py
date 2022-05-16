# -*- coding: utf8 -*-

import joblib
import owlready2
import wx
import wx.xrc
from owlready2 import *


from listctrl import MyListCtrl, ColumnInfo

owlready2.JAVA_EXE = "C:\Program Files (x86)\Common Files\Oracle\Java\javapath\java.exe"


###########################################################################
## Class Panel
###########################################################################

class welcomePage(wx.Panel):

    def __init__(self, parent, frame_):
        self.frame_ = frame_
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, style=wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Welcome", wx.DefaultPosition, wx.Size(-1, -1),
                                           wx.ALIGN_CENTRE)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        self.m_staticText4 = wx.StaticText(self.m_panel3, wx.ID_ANY,
                                           u'''This tool is made to facilitate agile methods adopting by answering to most common concerns you may have when adopting a practice. 
                           
                                               - The information to all the concerns are generated frome the previous experiences reported in literature.
                           
                                               - The page "All the information related to practice" allows you to get all knowledge that we have extracted related to the practices. 
                                               
                                               - The page "Input page 1" allows you to insert the input describing the goal your team wants to achieve. This allows the tool suggesting the suitable practice(s) to adopt answering to your needs.
                           
                                               - The page "Input page 2" allows you to insert the input describing your team situation and the practice you adopt. This allows filtering the information to the concerns which are only related to your case.
                           
                                               - The information generated specifically based on your input can be found in the page "Information related to practice based on input".
                           
                                               
                                               * Hover your mouse on the phrase for the tooltip''', wx.DefaultPosition, wx.Size(-1, -1),
                                           wx.ALIGN_LEFT)
        self.m_staticText4.Wrap(-1)
        self.m_staticText4.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))

        bSizer20.Add(self.m_staticText2, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer20.Add(self.m_staticText4, 3, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button1 = wx.Button(self.m_panel3, wx.ID_ANY, u"Continue", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer20.Add(self.m_button1, 0, wx.ALL, 5)

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
        # self.frame.Hide() #hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult() #calculate all the result
        # new_frame = InputPage(self) #open the page to display result
        # new_frame.Show()
        self.frame_.m_auinotebook1.AdvanceSelection(True)


###########################################################################
## Class First page
###########################################################################

class InputPage1(wx.Panel):

    def __init__(self, parent, frame_):
        # wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input page", pos = wx.DefaultPosition, size =(800, 600), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.MINIMIZE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
        self.frame_ = frame_
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, style=wx.TAB_TRAVERSAL)
        # self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        bSizer0 = wx.BoxSizer(wx.VERTICAL)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, -1),
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText4 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY,
                                           u"Please select the situation of your team", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.situationTip = wx.ToolTip(
            "Situation effect adoption of a practice, selecting the value(s) which describe best your team situation allows you to get the answers best related to your team")
        self.m_staticText4.SetToolTip(self.situationTip)
        self.m_staticText4.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))
        self.m_staticText4.Wrap(-1)
        bSizer7.Add(self.m_staticText4, 0, wx.ALL, 5)

        lblList = [u"Unknown", u"Big organization: more than 500 people",
                   u"Medium organization: between 100 to 500 people", u"Small organization:less than 100 people"]
        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"1. Organization size",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)
        # self.rbox1 = wx.RadioBox(self.m_scrolledWindow1, label = '1. Organization size', pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox1 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[0], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox1, 0, wx.ALL, 5)
        self.rbox1.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"2. Team size", wx.DefaultPosition,
                                          wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Big team more than 10", u"Medium team between 5 and 10", u"Small team less than 5"]
        # self.rbox2 = wx.RadioBox(self.m_scrolledWindow1, label = '2. Team size', pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox2 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[0], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox2, 0, wx.ALL, 5)
        self.rbox2.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"3. Team distribution",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Distributed Team", u"Same site"]
        # self.rbox3 = wx.RadioBox(self.m_scrolledWindow1, label = '3. Team distribution', pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox3 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[0], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox3, 0, wx.ALL, 5)
        self.rbox3.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"4. Agile maturity level",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"No agile experience", u"1 years agile experience", u"2 years agile experience",
                   u"3 years agile experience",
                   u"4 years agile experience", u"5 years agile experience", u"Some experience in agile"]
        # self.rbox4 = wx.RadioBox(self.m_scrolledWindow1, label = u"4. Agile maturity level", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox4 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[0], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox4, 0, wx.ALL, 5)
        self.rbox4.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"5. Type of communication",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)

        lblList = [u"Unknown", u"Face to face communication", u"Virtual communication"]
        # self.rbox5 = wx.RadioBox(self.m_scrolledWindow1, label = u"5. Type of communication", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox5 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[0], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox5, 0, wx.ALL, 5)
        self.rbox5.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"6. Domain of knowledge maturity level",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"No domain knowledge", u"Experience in domain knowledge", u"Expert in domain knowledge"]
        # self.rbox6 = wx.RadioBox(self.m_scrolledWindow1, label = u"6. Domain of knowledge maturity level", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox6 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[0], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox6, 0, wx.ALL, 5)
        self.rbox6.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_scrolledWindow1.SetSizer(bSizer7)
        self.m_scrolledWindow1.Layout()
        bSizer5.Add(self.m_scrolledWindow1, 1, wx.EXPAND, 5)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"7.  Management support level",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Poor management support", u"Average management support", u"High management support"]
        # self.rbox7 = wx.RadioBox(self.m_scrolledWindow2, label = u"7.  Management support level", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox7 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[0], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox7, 0, wx.ALL, 5)
        self.rbox7.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY,
                                          u"8. Project management in previous project", wx.DefaultPosition,
                                          wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)

        lblList = [u"Unknown", u"Waterfall", u"eXtreme Programming"]
        # self.rbox8 = wx.RadioBox(self.m_scrolledWindow2, label = u"8. Project management in previous project", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox8 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[0], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox8, 0, wx.ALL, 5)
        self.rbox8.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 0)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow2 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow2.SetScrollRate(5, 5)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"9. Project size", wx.DefaultPosition,
                                          wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer8.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Small project less than 2 years", u"Medium project between 2 to 5 years",
                   u"Big project more than 5 years"]
        # self.rbox9 = wx.RadioBox(self.m_scrolledWindow2, label = u"9. Project size", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox9 = wx.ComboBox(self.m_scrolledWindow2, wx.ID_ANY, lblList[0], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer8.Add(self.rbox9, 0, wx.ALL, 5)
        self.rbox9.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"10. Requirements  stability",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer8.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Unstable Requirement", u"Stable Requirement"]
        # self.rbox10 = wx.RadioBox(self.m_scrolledWindow2, label = u"10. Requirements  stability", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox10 = wx.ComboBox(self.m_scrolledWindow2, wx.ID_ANY, lblList[0], wx.DefaultPosition, wx.Size(700, -1),
                                  style=wx.CB_READONLY, choices=lblList)
        bSizer8.Add(self.rbox10, 0, wx.ALL, 5)
        self.rbox10.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"11. Technology knowledge level",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer8.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Novice in techonology knowledge", u"Experience in techonology knowledge",
                   u"Expert in techonology knowledge", u"Cross compentence in technology knowledge"]
        # self.rbox11 = wx.RadioBox(self.m_scrolledWindow2, label = u"11. Technology knowledge level", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox11 = wx.ComboBox(self.m_scrolledWindow2, wx.ID_ANY, lblList[0], wx.DefaultPosition, wx.Size(700, -1),
                                  style=wx.CB_READONLY, choices=lblList)
        bSizer8.Add(self.rbox11, 0, wx.ALL, 5)
        self.rbox11.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"12. User availability level",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer8.Add(self.m_staticText, 0, wx.ALL, 5)

        lblList = [u"Unknown", u"User hardly available", u"User availlable time to time", u"User highly available"]
        # self.rbox12 = wx.RadioBox(self.m_scrolledWindow2, label = u"12. User availability level", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox12 = wx.ComboBox(self.m_scrolledWindow2, wx.ID_ANY, lblList[0], wx.DefaultPosition, wx.Size(700, -1),
                                  style=wx.CB_READONLY, choices=lblList)
        bSizer8.Add(self.rbox12, 0, wx.ALL, 5)
        self.rbox12.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_staticText4 = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText4.Wrap(-1)
        bSizer8.Add(self.m_staticText4, 0, wx.ALL, 5)
        self.m_staticText4.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))

        self.m_staticText4 = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY,
                                           u"Please select agile practice(s) you adopted or want  to adopt",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.practiceTip = wx.ToolTip(
            "Selecting agile practice(s) allows you to filter for only the information related to the practice(s) you interest")
        self.m_staticText4.SetToolTip(self.practiceTip)
        self.m_staticText4.Wrap(-1)
        bSizer8.Add(self.m_staticText4, 0, wx.ALL, 5)
        self.m_staticText4.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))

        self.m_checkBox1 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY, u"Daily Meeting", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox1, 0, wx.ALL, 5)
        self.m_checkBox1.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox2 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY, u"Short Iteration", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox2, 0, wx.ALL, 5)
        self.m_checkBox2.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox3 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY, u"Sprint Planning", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox3, 0, wx.ALL, 5)
        self.m_checkBox3.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox4 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY, u"Sprint Review", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox4, 0, wx.ALL, 5)
        self.m_checkBox4.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox5 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY, u"Sprint Retrospective", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox5, 0, wx.ALL, 5)
        self.m_checkBox5.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_scrolledWindow2.SetSizer(bSizer8)
        self.m_scrolledWindow2.Layout()
        bSizer8.Fit(self.m_scrolledWindow2)
        bSizer6.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer6, 1, wx.EXPAND, 0)
        bSizer0.Add(bSizer1, 13, wx.EXPAND, 0)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Go to Input Page 1", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer2.Add(self.m_button1, 0, wx.ALL, 5)
        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Calculate result", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer2.Add(self.m_button2, 0, wx.ALL, 5)
        bSizer0.Add(bSizer2, 1, wx.ALL, 5)
        self.SetSizer(bSizer0)
        self.Layout()

        self.Centre(wx.BOTH)
        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.secondInputPage)
        self.m_button2.Bind(wx.EVT_BUTTON, self.ShowResult)

    def __del__(self):
        pass

    def ShowPopup(self, event):
        popmenu = wx.Menu()
        popmenu.Append(1, "Copy this text to clipboard")
        popmenu.Bind(wx.EVT_MENU, self.Copy(event))
        self.m_scrolledWindow2.PopupMenu(popmenu)
        popmenu.Destroy()

    def Copy(self, event):
        clipdata = wx.TextDataObject()
        objectEvent = event.GetEventObject()
        text = objectEvent.GetLabel()
        if (text == ""):
            text = objectEvent.GetValue()
        clipdata.SetText(text)
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()

    def secondInputPage(self, event):

        self.frame_.m_auinotebook1.AdvanceSelection(True)

    def gatherData(self):
        self.frame_.situationList = []
        self.frame_.situationList.append(u"Situation:" + self.rbox1.GetStringSelection().replace(' ', '_'))
        self.frame_.situationList.append(u"Situation:" + self.rbox2.GetStringSelection().replace(' ', '_'))
        self.frame_.situationList.append(u"Situation:" + self.rbox3.GetStringSelection().replace(' ', '_'))
        self.frame_.situationList.append(u"Situation:" + self.rbox4.GetStringSelection().replace(' ', '_'))
        self.frame_.situationList.append(u"Situation:" + self.rbox5.GetStringSelection().replace(' ', '_'))
        self.frame_.situationList.append(u"Situation:" + self.rbox6.GetStringSelection().replace(' ', '_'))
        self.frame_.situationList.append(u"Situation:" + self.rbox7.GetStringSelection().replace(' ', '_'))
        self.frame_.situationList.append(u"Situation:" + self.rbox8.GetStringSelection().replace(' ', '_'))
        self.frame_.situationList.append(u"Situation:" + self.rbox9.GetStringSelection().replace(' ', '_'))
        self.frame_.situationList.append(u"Situation:" + self.rbox10.GetStringSelection().replace(' ', '_'))
        self.frame_.situationList.append(u"Situation:" + self.rbox11.GetStringSelection().replace(' ', '_'))
        self.frame_.situationList.append(u"Situation:" + self.rbox12.GetStringSelection().replace(' ', '_'))

        self.frame_.practiceList = []
        practiceName = [u"Practice:Daily_meeting", u"Practice:Short_iteration", u"Practice:Sprint_planning",
                        u"Practice:Sprint_review", u"Practice:Sprint_retrospective"]
        practiceCheckBox = [self.m_checkBox1, self.m_checkBox2, self.m_checkBox3, self.m_checkBox4, self.m_checkBox5]

        for i, item in enumerate(practiceCheckBox):
            if item.GetValue():
                self.frame_.practiceList.append(practiceName[i])

        # self.Hide() #hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult(inputList) #calculate all the result
        # new_frame = InputPage2(self) #open the page to the input page 2
        # new_frame.Show()
        # print(self.frame_.practiceList)
        # print(self.frame_.situationList)

    def ShowResult(self, event):

        self.frame_.result = []
        self.gatherData()
        self.frame_.input_page2.gatherData()

        self.frame_.runQuery.createNewInstance()  # create new instance and run the query based on team

        if self.frame_.resultpage2 == None:
            self.frame_.resultpage2 = ResultPage2(self.frame_.m_auinotebook1, self.frame_)
            self.frame_.m_auinotebook1.AddPage(self.frame_.resultpage2, "Questions and answers based on input")
        else:
            self.frame_.resultpage2.list.ClearAll()
        self.frame_.resultpage2.LoadResult(event=None, questionIndex=0)

        self.frame_.m_auinotebook1.SetSelection(4)


class InputPage2(wx.Panel):

    # def __init__( self, parent ):
    # wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input page", pos = wx.DefaultPosition, size = wx.Size( 1050,676 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.MINIMIZE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

    def __init__(self, parent, frame_):
        # wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input page", pos = wx.DefaultPosition, size =(800, 600), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.MINIMIZE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
        self.frame_ = frame_
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, style=wx.TAB_TRAVERSAL)
        self.situationList = self.frame_.situationList
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        bSizer0 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow2 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow2.SetScrollRate(5, 5)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY,
                                           u"Please select agile principle(s) as the goal you want to achieve",
                                           wx.DefaultPosition, wx.DefaultSize, 0)

        self.principleTip = wx.ToolTip(
            "Agile Principle are known to be the sub goals of agile values but also the top goals we believe we can achieve by adopting agile methods. 12 principles were defined during the creation of agile methods. Selecting agile principle(s) allows you to know query suitable practice(s) to adopt in order to achieve them")
        self.m_staticText5.SetToolTip(self.principleTip)

        self.m_staticText5.Wrap(-1)
        bSizer8.Add(self.m_staticText5, 0, wx.ALL, 5)
        self.m_staticText5.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))

        self.m_checkBox6 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                       u"To satisfy the customer through early and continuous delivery of valuable software",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox6, 0, wx.ALL, 5)

        self.m_checkBox6.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox7 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                       u"To welcome changing requirements, even late in development. To harness change for the customer's competitive advantage",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox7, 0, wx.ALL, 5)
        self.m_checkBox7.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox8 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                       u"To deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox8, 0, wx.ALL, 5)
        self.m_checkBox8.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox9 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                       u"To make business people and developers must work together daily throughout the project",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox9, 0, wx.ALL, 5)
        self.m_checkBox9.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox10 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"To build projects around motivated individuals. Give them the environment and support they need, and trust them to get the job done",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox10, 0, wx.ALL, 5)
        self.m_checkBox10.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox11 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"To have the most efficient and effective method of conveying information to and within a development team which is face-to-face conversation",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox11, 0, wx.ALL, 5)
        self.m_checkBox11.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox12 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"To make working software as the primary measure of progress",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox12, 0, wx.ALL, 5)
        self.m_checkBox12.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox13 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"To promote sustainable development. The sponsors, developers, and users should be able to maintain a constant pace indefinitely",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox13, 0, wx.ALL, 5)
        self.m_checkBox13.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox14 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"To have continuous attention to technical excellence and good design enhances agility",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox14, 0, wx.ALL, 5)
        self.m_checkBox14.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox15 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"To make simplicity--the art of maximizing the amount of work not done-- essential",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox15, 0, wx.ALL, 5)
        self.m_checkBox15.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox16 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"To have the best architectures, requirements, and designs emerge from self-organizing teams",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox16, 0, wx.ALL, 5)
        self.m_checkBox16.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox17 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"To make the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly at regular intervals, ",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox17, 0, wx.ALL, 5)
        self.m_checkBox17.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText.Wrap(-1)
        bSizer8.Add(self.m_staticText, 0, wx.ALL, 5)
        self.m_staticText6 = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY,
                                           u"Please select agile value(s) as the goal you want to achieve",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.valueTip = wx.ToolTip(
            "Agile Value are known to be the top goals we believe we can achieve by adopting agile methods. 4 values were defined during the creation of agile methods. Selecting agile value(s) allows you to know query suitable practice(s) to adopt in order to achieve them")
        self.m_staticText6.SetToolTip(self.valueTip)
        self.m_staticText6.Wrap(-1)
        bSizer8.Add(self.m_staticText6, 0, wx.ALL, 5)
        self.m_staticText6.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))
        ##
        ##        self.m_staticText6 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"\n Please select agile value(s) you want to achieve", wx.DefaultPosition, wx.DefaultSize, 0 )

        ##        self.m_staticText6.SetFont( wx.Font( 12, 70, 90, wx.BOLD, False, wx.EmptyString )  )

        self.m_checkBox18 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"To make individuals and interactions more important than processes and tools",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox18, 0, wx.ALL, 5)
        self.m_checkBox18.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox19 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"To make working software more important than comprehensive documentation",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox19, 0, wx.ALL, 5)
        self.m_checkBox19.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox20 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"To make customer collaboration more important than contract negotiation",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox20, 0, wx.ALL, 5)
        self.m_checkBox20.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_checkBox21 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"To make responding to change more important than following a plan",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox21, 0, wx.ALL, 5)
        self.m_checkBox21.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_scrolledWindow2.SetSizer(bSizer8)
        self.m_scrolledWindow2.Layout()
        bSizer8.Fit(self.m_scrolledWindow2)
        bSizer6.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        bSizer0.Add(bSizer6, 13, wx.EXPAND, 0)

        self.m_button0 = wx.Button(self, wx.ID_ANY, u"Go to Input Page 2", wx.Point(-1, -1), wx.DefaultSize, 0)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Calculate result", wx.Point(-1, -1), wx.DefaultSize, 0)

        bSizer2.Add(self.m_button0, 0, wx.ALL, 5)
        bSizer2.Add(self.m_button1, 0, wx.ALL, 5)
        bSizer0.Add(bSizer2, 1, wx.ALL, 0)

        self.SetSizer(bSizer0)
        self.Layout()

        self.Centre(wx.BOTH)
        # Connect Events
        self.m_button0.Bind(wx.EVT_BUTTON, self.firstInputPage)
        self.m_button1.Bind(wx.EVT_BUTTON, self.ShowResult)

    def __del__(self):
        pass

    def ShowPopup(self, event):
        popmenu = wx.Menu()
        popmenu.Append(1, "Copy this text to clipboard")
        popmenu.Bind(wx.EVT_MENU, self.Copy(event))
        self.m_scrolledWindow2.PopupMenu(popmenu)
        popmenu.Destroy()

    def Copy(self, event):
        clipdata = wx.TextDataObject()
        objectEvent = event.GetEventObject()
        text = objectEvent.GetLabel()
        clipdata.SetText(text)
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()

    def firstInputPage(self, event):
        # self.Hide() #hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult(inputList) #calculate all the result
        # new_frame = InputPage(self) #open the page to the input page 2
        # new_frame.Show()
        self.frame_.m_auinotebook1.SetSelection(2)

    def gatherData(self):
        self.frame_.m_auinotebook1.AdvanceSelection(forward=True)

        self.frame_.principleList = []
        principleName = [
            u"Principle:Our_highest_priority_is_to_satisfy_the_customer_through_early_and_continuous_delivery_of_valuable_software",
            u"Principle:Welcome_changing_requirements_even_late_in__development._Agile_processes_harness_change_for__the_customer_s_competitive_advantage",
            u"Principle:Deliver_working_software_frequently_from_a__couple_of_weeks_to_a_couple_of_months_with_a__preference_to_the_shorter_timescale",
            u"Principle:Business_people_and_developers_must_work__together_daily_throughout_the_project",
            u"Principle:Build_projects_around_motivated_individuals.__Give_them_the_environment_and_support_they_need__and_trust_them_to_get_the_job_done",
            u"Principle:The_most_efficient_and_effective_method_of__conveying_information_to_and_within_a_development__team_is_face-to-face_conversation",
            u"Principle:Working_software_is_the_primary_measure_of_progress",
            u"Principle:Agile_processes_promote_sustainable_development.__The_sponsors_developers_and_users_should_be_able__to_maintain_a_constant_pace_indefinitely",
            u"Principle:Continuous_attention_to_technical_excellence__and_good_design_enhances_agility",
            u"Principle:Simplicity--the_art_of_maximizing_the_amount__of_work_not_done--is_essential",
            u"Principle:The_best_architectures_requirements_and_designs__emerge_from_self-organizing_teams",
            u"Principle:At_regular_intervals_the_team_reflects_on_how__to_become_more_effective_then_tunes_and_adjusts__its_behavior_accordingly"]

        principleCheckbox = [self.m_checkBox6, self.m_checkBox7, self.m_checkBox8, self.m_checkBox9, self.m_checkBox10,
                             self.m_checkBox11, self.m_checkBox12, self.m_checkBox13, self.m_checkBox14,
                             self.m_checkBox15, self.m_checkBox16, self.m_checkBox17]

        for i, item in enumerate(principleCheckbox):
            if item.GetValue():
                self.frame_.principleList.append(principleName[i])

        self.frame_.valueList = []

        valueCheckBox = [self.m_checkBox18, self.m_checkBox19, self.m_checkBox20, self.m_checkBox21]

        valueName = [u"Value:Individuals_and_interactions_over_processes_and_tools",
                     u"Value:Working_software_over_comprehensive_documentation",
                     u"Value:Customer_collaboration_over_contract_negotiation",
                     u"Value:Responding_to_change_over_following_a_plan"]

        for i, item in enumerate(valueCheckBox):
            if item.GetValue():
                self.frame_.valueList.append(valueName[i])

    def ShowResult(self, event):
        self.frame_.result = []
        self.frame_.input_page1.gatherData()
        self.gatherData()

        self.frame_.runQuery.createNewInstance()  # create new instance and run the query for that object

        if self.frame_.resultpage2 == None:
            self.frame_.resultpage2 = ResultPage2(self.frame_.m_auinotebook1, self.frame_)
            self.frame_.m_auinotebook1.AddPage(self.frame_.resultpage2, "Questions and answered based on input")
        else:
            self.frame_.resultpage2.list.ClearAll()

        self.frame_.resultpage2.LoadResult(event=None, questionIndex=0)

        self.frame_.m_auinotebook1.SetSelection(4)


class ResultPage1(wx.Panel):

    # def __init__(self, parent):
    #       wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Result", pos = wx.DefaultPosition, size = wx.Size( 1050,676 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.MINIMIZE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
    def __init__(self, parent, frame_):
        # wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input page", pos = wx.DefaultPosition, size =(800, 600), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.MINIMIZE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
        self.frame_ = frame_
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, style=wx.TAB_TRAVERSAL)
        self.frame_.runQuery = SparqlQueries(self, self.frame_)
        self.result = self.frame_.runQuery.queryAllResult()
        self.frame_.result = self.result
        self.frame_.SolutionProblemList = []
        self.frame_.ProblemWithSolution = []

        for i, each in enumerate(self.result[5][7]):
            self.frame_.SolutionProblemList.append([each[0], each[1]])  # add problem and solution to list
            if not each[0] in self.frame_.ProblemWithSolution:
                self.frame_.ProblemWithSolution.append(each[0])

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, -1),
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)
        practice = "Daily meeting"
        self.questionList = ['The goal a team can achieve by adopting an agile practice',
                             'The agile value a team can achieve by adopting a practice',
                             'The agile principle a team can achieve by adopting a practice',
                             'The activity a team should perform as part of a practice',
                             'The problem a team may encounter while adopting a practice',

                             'The situation of the team or the activity that they perform which is bad for adopting a practice',
                             'The situation of the team or the activity that they perform which is good for adopting a practice',

                             'The artifact required for adopting a practice',
                             'The roles or responsibility distribution needed for a practice',

                             'The requisites a team should prepare in order to successfully adopt a practice',

                             'The cause of the problem team may encounter',
                             'The solution a team may use to solve the problem',

                             'The general knowledge based on experiences related to agile practice a team should learn']

        ##                self.questionList = ['What objectives/goals can be achieved by an agile practice?',
        ##                                'What agile values can be achieved by adopting a practice?',
        ##                                'What agile principles can be achieved by adopting a practice?',
        ##                                'What  activities  are  part  of  a  practice  and  need  to  be  performed  by  the team?',
        ##                                'What are the problem faced by a practice?',
        ##
        ##
        ##                                'What can be harmful when adopting a practice?',
        ##                                'What can be useful when adopting a practice?',
        ##
        ##                                'What are the artifacts required for a practice?',
        ##
        ##                                'What are the roles required for a practice?',
        ##                                'What are the requisites to successfully adopt a practice?',
        ##                                'What are the cause of the problem team may encounter?',
        ##                                'What are the solutions to the problem?'
        ##
        ##                                ]
        self.m_staticText3 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY,
                                           u"This section will provide the answers to the concerns related to practice",
                                           wx.DefaultPosition, wx.Size(800, -1), 0)
        self.m_staticText3.Wrap(-1)
        bSizer7.Add(self.m_staticText3, 0, wx.ALL, 5)
        self.m_staticText3.SetFont(wx.Font(13, 70, 90, wx.BOLD, False, wx.EmptyString))

        self.m_staticText4 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY,
                                           u"1. Please select a concern you want to know", wx.DefaultPosition,
                                           wx.Size(700, -1), 0)
        self.m_staticText4.Wrap(-1)
        bSizer7.Add(self.m_staticText4, 0, wx.ALL, 5)
        self.m_staticText4.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))

        self.m_bcomboBox1 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, self.questionList[0], wx.DefaultPosition,
                                        wx.Size(700, -1), style=wx.CB_READONLY, choices=self.questionList)
        bSizer7.Add(self.m_bcomboBox1, 0, wx.ALL, 5)

        ##                self.m_staticText5 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"2. Please  select a practice", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )
        ##                self.m_staticText5.Wrap( -1 )
        ##                bSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )
        ##                self.m_staticText5.SetFont( wx.Font( 12, 70, 90, wx.BOLD, False, wx.EmptyString )  )

        ##                practiceList = ["Daily meeting", "Short iteration","Sprintplanning",  "Sprint retrospective", "Sprint review"]
        ##                self.m_bcomboBox2 = wx.ComboBox( self.m_scrolledWindow1, wx.ID_ANY, practiceList[0], wx.DefaultPosition, wx.Size( 700,-1 ), choices=,style = wx.CB_READONLY  )
        ##                bSizer7.Add( self.m_bcomboBox2, 0, wx.ALL, 5 )

        # self.m_listBox1 = wx.ListBox( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,-1 ), m_listBox1Choices, wx.LB_SINGLE )
        # bSizer7.Add( self.m_listBox1, 0, wx.ALL, 5 )

        self.m_scrolledWindow1.SetSizer(bSizer7)
        self.m_scrolledWindow1.Layout()
        bSizer5.Add(self.m_scrolledWindow1, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 2, wx.EXPAND, 0)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow2 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_scrolledWindow2.SetScrollRate(5, 5)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(self.m_scrolledWindow2, 1, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        bSizer8.Add(self.m_staticText9, 0, wx.ALL, 5)

        #                self.list = wx.ListCtrl(self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition,  wx.Size( 900, 650),  style = wx.LC_REPORT|wx.LC_ALIGN_LEFT)

        columns = [
            ColumnInfo(
                "column0",
                lambda person: person.name,
                wx.LIST_FORMAT_LEFT),
            ColumnInfo(
                "column1",
                lambda person: person.erdos_number,
                wx.LIST_FORMAT_RIGHT),

            ColumnInfo(
                "column2",
                lambda person: person.erdos_number,
                wx.LIST_FORMAT_RIGHT)
        ]

        self.list = MyListCtrl(self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size(1800, 830),
                               wx.LC_REPORT | wx.LC_ALIGN_LEFT, columns)
        bSizer8.Add(self.list, 0, wx.ALL, 5)
        self.list.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_scrolledWindow2.SetSizer(bSizer8)
        self.m_scrolledWindow2.Layout()
        bSizer8.Fit(self.m_scrolledWindow2)
        bSizer6.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer6, 10, wx.EXPAND, 0)

        bSizer20.Add(bSizer1, 12, wx.EXPAND, 0)

        self.m_button0 = wx.Button(self, wx.ID_ANY, u"Go to input page", wx.Point(-1, -1), wx.DefaultSize, 0)
        # self.m_button1 = wx.Button( self, wx.ID_ANY, u"Next result", wx.Point( -1,-1 ), wx.DefaultSize, 0 )

        bSizer2.Add(self.m_button0, 0, wx.ALL, 5)
        # bSizer2.Add( self.m_button1, 0, wx.ALL, 5 )
        bSizer20.Add(bSizer2, 1, wx.ALL, 0)

        self.SetSizer(bSizer20)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_bcomboBox1.Bind(wx.EVT_COMBOBOX, self.LoadResult)
        self.m_bcomboBox1.Bind(wx.EVT_TEXT, self.LoadResult)
        # self.m_bcomboBox2.Bind( wx.EVT_COMBOBOX, self.LoadResult )
        # self.m_bcomboBox2.Bind( wx.EVT_TEXT, self.LoadResult )
        # self.m_button1.Bind( wx.EVT_BUTTON, self.ShowNextFrame )
        self.m_button0.Bind(wx.EVT_BUTTON, self.firstInputPage)
        self.LoadResult(event=None, questionIndex=0)

    def __del__(self):
        pass

    def ShowPopup(self, event):
        popmenu = wx.Menu()
        popmenu.Append(1, "Copy this text to clipboard")
        popmenu.Bind(wx.EVT_MENU, self.Copy(event))
        self.m_scrolledWindow2.PopupMenu(popmenu)
        popmenu.Destroy()

    def Copy(self, event):
        questionIndex = self.m_bcomboBox1.GetSelection()
        clipdata = wx.TextDataObject()
        objectEvent = event.GetEventObject()

        if questionIndex == 0 or questionIndex == 3 or questionIndex == 4 or questionIndex == 9 or questionIndex == 10 or questionIndex == 11 or questionIndex == 12:
            # print ("self.list.GetColumWidth(0)", self.list.GetColumnWidth(0))
            if event.GetX() < self.list.GetColumnWidth(0):
                text = objectEvent.GetItemText(objectEvent.GetFocusedItem(), col=0)

            else:
                text = objectEvent.GetItemText(objectEvent.GetFocusedItem(), col=1)

        else:
            print(event.GetX(), self.list.GetColumnWidth(0), self.list.GetColumnWidth(1))
            if event.GetX() < self.list.GetColumnWidth(0):
                text = objectEvent.GetItemText(objectEvent.GetFocusedItem(), col=0)
            elif event.GetX() < self.list.GetColumnWidth(0) + self.list.GetColumnWidth(1):
                text = objectEvent.GetItemText(objectEvent.GetFocusedItem(), col=1)

            else:
                text = objectEvent.GetItemText(objectEvent.GetFocusedItem(), col=2)
        # print("event.GetX())", event.GetX())
        clipdata.SetText(text)
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()

    def firstInputPage(self, event):
        self.frame_.m_auinotebook1.AdvanceSelection(forward=True)
        # self.Hide() #hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult(inputList) #calculate all the result
        # new_frame = InputPage(self) #open the page to the input page 2
        # new_frame.Show()
        # Virtual event handlers, overide them in your derived class

    def LoadResult(self, event, questionIndex=None):
        if questionIndex == None:
            questionIndex = self.m_bcomboBox1.GetSelection()
        self.list.ClearAll()
        # print (self.result[0][1])
        tmpitem = ""

        column0 = ['Practice', 'Practice', 'Practice', 'Practice', 'Practice', 'Practice', 'Practice', 'Practice',
                   'Practice', 'Practice', 'Cause', 'Problem', 'Practice']
        column1 = ['Achieves Goal', 'Achieves Value', 'Achieves Principle', 'Composed of Activity',
                   'Encounters Problem', 'With Activity/Situation', 'With Activity/Situation', 'Requires Artifact',
                   'Role', 'Requires Requisite', 'Problem', 'Solution', 'Lesson Learned']
        column2 = ['', 'Contributed by Principle', 'Has Sub-goal', '', '', 'Harms Requisite', 'Helps Requisite',
                   'For Activity', 'In responsible of Activity', '', '', '', '']

        prefix1 = ['Goal', 'Value', 'Principle', 'Activity', 'Problem', '', '', 'Artifact', 'Role', 'Requisite',
                   'Cause', 'Problem', 'Lesson']
        prefix2 = ['', 'Principle', 'Goal', '', '', 'Requisite', 'Requisite', 'Activity', 'Activity', '', 'Problem',
                   'Solution', '']
        practiceName = [u"Practice:Daily_meeting", u"Practice:Short_iteration", u"Practice:Sprint_planning",
                        u"Practice:Sprint_review", u"Practice:Sprint_retrospective"]

        if questionIndex == 1 or questionIndex == 2 or questionIndex == 5 or questionIndex == 6 or questionIndex == 7 or questionIndex == 8:

            previous1 = ""
            previous2 = ""
            self.list.InsertColumn(0, column0[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(1, column1[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(2, column2[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
            itemIndex = 0
            for index, practice in enumerate(practiceName):
                previous1 = ""
                if len(self.result[index][questionIndex]) > 0:
                    practice = practice.replace("_", " ")
                    practice = practice.replace("Practice:", "")
                # print(self.result[index][questionIndex])
                for i, each in enumerate(self.result[index][questionIndex]):

                    if previous1 == "":
                        itemIndex = self.list.InsertItem(itemIndex, practice)
                        previous1 = practice
                    else:
                        itemIndex = self.list.InsertItem(itemIndex, "")

                    if previous2 == each[0]:
                        self.list.SetItem(itemIndex, 1, '')

                    else:
                        if questionIndex == 1 or questionIndex == 2 or questionIndex == 7 or questionIndex == 8:
                            tmpitem = each[0].replace("_", " ")[len(prefix1[questionIndex]) + 1:]
                            tmpitem = tmpitem.replace("1rst:", "")
                            tmpitem = tmpitem.replace("2nd:", "")
                            tmpitem = tmpitem.replace("3rd:", "")
                            tmpitem = tmpitem.replace("4th:", "")
                            tmpitem = tmpitem.replace("5th:", "")
                            tmpitem = tmpitem.replace("6th:", "")
                            self.list.SetItem(itemIndex, 1, tmpitem)
                        else:
                            self.list.SetItem(itemIndex, 1, each[0].replace("_", " "))
                        previous2 = each[0]
                    if questionIndex == 1 or questionIndex == 2 or questionIndex == 7 or questionIndex == 8:
                        tmpitem = each[1].replace("_", " ")[len(prefix2[questionIndex]) + 1:]
                        tmpitem = tmpitem.replace("1rst:", "")
                        tmpitem = tmpitem.replace("2nd:", "")
                        tmpitem = tmpitem.replace("3rd:", "")
                        tmpitem = tmpitem.replace("4th:", "")
                        tmpitem = tmpitem.replace("5th:", "")
                        tmpitem = tmpitem.replace("6th:", "")
                        self.list.SetItem(itemIndex, 2, tmpitem)
                    else:
                        self.list.SetItem(itemIndex, 2, each[1].replace("_", " ")[len(prefix2[questionIndex]) + 1:])
                    # self.list.SetItem(itemIndex , 2, each[2].replace("_"," "))
                    itemIndex += 1


        elif questionIndex < 10 or questionIndex == 12:  # filter by team and agile practice
            self.list.InsertColumn(0, column0[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(1, column1[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(2, column2[questionIndex], wx.LIST_FORMAT_LEFT, width=300)

            itemIndex = 0
            for index, practice in enumerate(practiceName):
                if len(self.result[index][questionIndex]) > 0:
                    practice = practice.replace("_", " ")
                    practice = practice.replace("Practice:", "")

                    itemIndex = self.list.InsertItem(itemIndex, practice)
                    # print (itemIndex, practice)
                    tmpitem = self.result[index][questionIndex][0].replace("_", " ")[len(prefix1[questionIndex]) + 1:]
                    tmpitem = tmpitem.replace("1rst:", "")
                    tmpitem = tmpitem.replace("2nd:", "")
                    tmpitem = tmpitem.replace("3rd:", "")
                    tmpitem = tmpitem.replace("4th:", "")
                    tmpitem = tmpitem.replace("5th:", "")
                    tmpitem = tmpitem.replace("6th:", "")

                    self.list.SetItem(itemIndex, 1, tmpitem)
                    for i in range(len(self.result[index][questionIndex]) - 1):
                        itemIndex += i + 1
                        itemIndex = self.list.InsertItem(itemIndex, "")
                        # print (itemIndex,self.result[index][questionIndex][i+1])

                        tmpitem = self.result[index][questionIndex][i + 1].replace("_", " ")[
                                  len(prefix1[questionIndex]) + 1:]
                        tmpitem = tmpitem.replace("1rst:", "")
                        tmpitem = tmpitem.replace("2nd:", "")
                        tmpitem = tmpitem.replace("3rd:", "")
                        tmpitem = tmpitem.replace("4th:", "")
                        tmpitem = tmpitem.replace("5th:", "")
                        tmpitem = tmpitem.replace("6th:", "")

                        self.list.SetItem(itemIndex, 1, tmpitem)

                    itemIndex += 1
                    itemIndex = self.list.InsertItem(itemIndex, "")
                    self.list.SetItem(itemIndex, 1, "")
                    itemIndex += 1
        else:
            previous = ""
            itemIndex = 0
            self.list.InsertColumn(0, column0[questionIndex], wx.LIST_FORMAT_LEFT, width=450)
            self.list.InsertColumn(1, column1[questionIndex], wx.LIST_FORMAT_LEFT, width=450)
            for i, each in enumerate(self.result[5][questionIndex - 4]):
                if each[0].replace("_", " ") == previous:
                    itemIndex = self.list.InsertItem(itemIndex, '')
                else:
                    if questionIndex == 11:
                        itemIndex = self.list.InsertItem(itemIndex,
                                                         each[0].replace("_", " ")[len(prefix1[questionIndex]) + 1:])
                    else:
                        itemIndex = self.list.InsertItem(itemIndex, each[0].replace("_", " "))
                self.list.SetItem(itemIndex, 1, each[1].replace("_", " ")[len(prefix2[questionIndex]) + 1:])
                itemIndex += 1
                previous = each[0].replace("_", " ")


##            practice = self.m_bcomboBox2.GetStringSelection()
##        
##            questionIndex =self.m_bcomboBox1.GetSelection()
##            practiceIndex = self.m_bcomboBox2.GetSelection()
##            
##            self.preAnswerByPractice = [' Objectives/goals can be achieved by '+practice+' are:\n\n',
##                      ' Agile values can be achieved by adopting '+practice+' are:\n\n',
##                      ' Agile principles can be achieved by adopting a  '+practice+' are:\n\n',
##                      ' Activities part  of  a '+practice+' and  need  to  be  performed  by  the team are:\n\n',
##                      ' What are the problem faced by '+practice+' are:\n\n',
##                     
##                      ' What can be harmful when adopting a  '+practice+' are:\n\n',
##                      ' What can be useful when adopting a  '+practice+' are:\n\n',
##                      
##                      ' What are the artifacts required for a  '+practice+' are:\n\n',
##                      ' Requisites to successfully adopt a  '+practice+' are\n\n']
##            
##
##            if questionIndex < 9:
##                response = ( self.result[self.m_bcomboBox2.GetSelection()][self.m_bcomboBox1.GetSelection()])
##                s = '\n - '
##                s = s.join(response)
##                s = s.replace('_', ' ')
##                self.m_staticText9.SetLabel(self.preAnswerByPractice[questionIndex] + '\n - '+ s)


###########################################################################
## Class Resultpage2 for the answers of the question in the list control format
###########################################################################
class ResultPage2(wx.Panel):

    # def __init__(self, parent):
    #       wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Result", pos = wx.DefaultPosition, size = wx.Size( 1050,676 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.MINIMIZE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
    def __init__(self, parent, frame_):
        # wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input page", pos = wx.DefaultPosition, size =(800, 600), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.MINIMIZE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
        self.frame_ = frame_
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, style=wx.TAB_TRAVERSAL)
        self.result = self.frame_.runQuery.queryAllResult()
        self.frame_.result = self.result
        self.teamActivity = []

        self.situationList = self.frame_.situationList
        self.practiceList = self.frame_.practiceList
        self.principleList = self.frame_.principleList
        self.valueList = self.frame_.valueList

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        bSizer20 = wx.BoxSizer(wx.VERTICAL)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, -1), 0)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.questionList = ['The goal a team can achieve by adopting an agile practice',
                             'The agile value a team can achieve by adopting a practice',
                             'The agile principle a team can achieve by adopting a practice',
                             'The activity a team should perform as part of a practice',
                             'The problem a team may encounter while adopting a practice',
                             'The solution a team may use to solve the problem',

                             'The situation of the team which is bad for adopting a practice',
                             'The situation of the team which is good for adopting a practice',
                             'The practice that a team should adopt to achieve the principle they need',
                             'The practice that a team should adopt to achieve value they need',
                             'The subgoal of the principle that team need to achieve',
                             'The subgoal of the value that team need ',
                             'The artifact required for adopting a practice',
                             'The roles or responsibility distribution needed for a practice',
                             'The requisites a team should prepare in order to successfully adopt a practice',

                             'The general knowledge based on experiences related to agile practice a team should learn'

                             ]

        self.m_staticText3 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY,
                                           u"This section will answer to the question related to the team",
                                           wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText3.Wrap(-1)
        bSizer7.Add(self.m_staticText3, 0, wx.ALL, 5)
        self.m_staticText3.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))

        self.m_staticText4 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"1. Please select a question",
                                           wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText4.Wrap(-1)
        bSizer7.Add(self.m_staticText4, 0, wx.ALL, 5)
        self.m_staticText4.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))

        self.m_bcomboBox1 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, self.questionList[0], wx.DefaultPosition,
                                        wx.Size(700, -1), style=wx.CB_READONLY, choices=self.questionList)
        bSizer7.Add(self.m_bcomboBox1, 0, wx.ALL, 5)

        self.m_scrolledWindow1.SetSizer(bSizer7)
        self.m_scrolledWindow1.Layout()
        bSizer5.Add(self.m_scrolledWindow1, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 2, wx.EXPAND, 0)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow2 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow2.SetScrollRate(5, 5)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(self.m_scrolledWindow2, 1, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        bSizer8.Add(self.m_staticText9, 0, wx.ALL, 5)

        columns = [
            ColumnInfo(
                "column0",
                lambda person: person.name,
                wx.LIST_FORMAT_LEFT),
            ColumnInfo(
                "column1",
                lambda person: person.erdos_number,
                wx.LIST_FORMAT_RIGHT),

            ColumnInfo(
                "column2",
                lambda person: person.erdos_number,
                wx.LIST_FORMAT_RIGHT)
        ]

        self.list = MyListCtrl(self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size(1800, 830),
                               wx.LC_REPORT | wx.LC_ALIGN_LEFT, columns)

        bSizer8.Add(self.list, 0, wx.ALL, 5)
        self.list.Bind(wx.EVT_RIGHT_DOWN, self.ShowPopup)

        self.m_scrolledWindow2.SetSizer(bSizer8)
        self.m_scrolledWindow2.Layout()
        bSizer8.Fit(self.m_scrolledWindow2)
        bSizer6.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer6, 10, wx.EXPAND, 0)
        bSizer20.Add(bSizer1, 13, wx.EXPAND, 0)

        self.m_button0 = wx.Button(self, wx.ID_ANY, u"Back to first input page", wx.Point(-1, -1), wx.DefaultSize, 0)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Back to general questions and answers", wx.Point(-1, -1),
                                   wx.DefaultSize, 0)

        bSizer2.Add(self.m_button0, 0, wx.ALL, 5)
        bSizer2.Add(self.m_button1, 0, wx.ALL, 5)
        bSizer20.Add(bSizer2, 1, wx.ALL, 0)

        self.SetSizer(bSizer20)

        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_bcomboBox1.Bind(wx.EVT_COMBOBOX, self.LoadResult)
        # self.m_bcomboBox1.Bind( wx.EVT_TEXT, self.LoadResult )
        self.m_button1.Bind(wx.EVT_BUTTON, self.resultPage1)
        self.m_button0.Bind(wx.EVT_BUTTON, self.firstInputPage)
        # self.m_bcomboBox2.Bind( wx.EVT_COMBOBOX, self.LoadResult )
        # self.m_bcomboBox2.Bind( wx.EVT_TEXT, self.LoadResult )
        self.LoadResult(event=None, questionIndex=None)

    def __del__(self):
        pass

    def ShowPopup(self, event):
        popmenu = wx.Menu()
        popmenu.Append(1, "Copy this text to clipboard")
        popmenu.Bind(wx.EVT_MENU, self.Copy(event))
        self.m_scrolledWindow2.PopupMenu(popmenu)
        popmenu.Destroy()

    def Copy(self, event):
        questionIndex = self.m_bcomboBox1.GetSelection()
        clipdata = wx.TextDataObject()
        objectEvent = event.GetEventObject()

        if questionIndex == 0 or questionIndex == 3 or questionIndex == 8 or questionIndex == 9 or questionIndex == 10 or questionIndex == 11 or questionIndex == 14 or questionIndex == 15:
            if event.GetX() < self.list.GetColumnWidth(0):
                text = objectEvent.GetItemText(objectEvent.GetFocusedItem(), col=0)

            else:
                text = objectEvent.GetItemText(objectEvent.GetFocusedItem(), col=1)

        else:
            # print(event.GetX(),self.list.GetColumnWidth(0), self.list.GetColumnWidth(1))
            if event.GetX() < self.list.GetColumnWidth(0):
                text = objectEvent.GetItemText(objectEvent.GetFocusedItem(), col=0)
            elif event.GetX() < self.list.GetColumnWidth(0) + self.list.GetColumnWidth(1):
                text = objectEvent.GetItemText(objectEvent.GetFocusedItem(), col=1)

            else:
                text = objectEvent.GetItemText(objectEvent.GetFocusedItem(), col=2)

        clipdata.SetText(text)
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()

    def firstInputPage(self, event):
        self.frame_.m_auinotebook1.SetSelection(2)
        # self.Hide() #hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult(inputList) #calculate all the result
        # new_frame = InputPage(self) #open the page to the input page 2
        # new_frame.Show()

    # Virtual event handlers, overide them in your derived class
    def LoadResult(self, event, questionIndex=None):
        practiceName = [u"Practice:Daily_meeting", u"Practice:Short_iteration", u"Practice:Sprint_planning",
                        u"Practice:Sprint_review", u"Practice:Sprint_retrospective"]
        self.list.ClearAll()
        if questionIndex == None:
            questionIndex = self.m_bcomboBox1.GetSelection()

        column0 = ['Practice', 'Agile Value', 'Agile Principle', 'Practice', '', '', 'Situation', 'Situation',
                   'Principle', 'Value', 'Principle', 'Value', 'Practice', 'Practice', 'Practice', 'Practice']
        column1 = ['Achieves Goal', 'Contributed by Principle', 'Has Sub-goal', 'Composed of Activity',
                   'Encounters Problem', '', 'Harms Requisite', 'Helps Requisite', 'Achieved by Practice',
                   'Achieved by Practice', 'Has Sub-Goal', 'Has Sub-Goal', 'Requires Artifact', 'Requires Role',
                   'Requires Requisite', 'Has Lesson learned']
        column2 = ['', 'Achieved By Practice', 'Achieved by Practice', '', '', 'Required by Practice',
                   'Required by Practice', 'Required by Practice', '', '', '', '', 'For Activity',
                   'In responsible of Activity', 'In responsible of Activity']
        itemIndex = 0
        prefix0 = ['Practice:', 'Value:', 'Principle:', 'Practice:', '', '', 'Situation:', 'Situation:', 'Principle:',
                   'Value:', 'Principle:', 'Value:', 'Practice:', 'Practice:', 'Practice:', 'Practice:']
        prefix1 = ['Goal:', 'Principle:', 'Goal:', 'Activity:', '', '', 'Requisite:', 'Requisite:', 'Practice:',
                   'Practice:', 'Goal:', 'Goal:', 'Artifact:', 'Role:', 'Requisite:', 'Lesson:']
        prefix2 = ['', 'Practice:', 'Goal:', '', '', '', 'Practice:', 'Practice:', '', '', '', '', 'Activity:',
                   'Activity:']

        practiceName = [u"Practice:Daily_meeting", u"Practice:Short_iteration", u"Practice:Sprint_planning",
                        u"Practice:Sprint_review", u"Practice:Sprint_retrospective"]

        if questionIndex == 1 or questionIndex == 2:
            previous1 = ""
            previous2 = ""
            self.list.InsertColumn(0, column0[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(1, column1[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(2, column2[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
            itemIndex = 0

            for index, practice in enumerate(practiceName):

                if practice in self.frame_.practiceList:
                    previous1 = ""
                    if len(self.result[index][questionIndex]) > 0:
                        practice = practice.replace("_", " ")
                        practice = practice.replace("Practice:", "")
                    # print(self.result[index][questionIndex])
                    for i, each in enumerate(self.result[index][questionIndex]):

                        if previous1 == "":
                            itemIndex = self.list.InsertItem(itemIndex, practice)
                            previous1 = practice
                        else:
                            itemIndex = self.list.InsertItem(itemIndex, "")

                        if previous2 == each[0]:
                            self.list.SetItem(itemIndex, 1, '')

                        else:
                            tmpitem = each[0].replace("_", " ")[len(prefix1[questionIndex]):]
                            self.list.SetItem(itemIndex, 1, tmpitem)
                            previous2 = each[0]

                        tmpitem = each[1].replace("_", " ")[len(prefix2[questionIndex]):]
                        self.list.SetItem(itemIndex, 2, tmpitem)

                        itemIndex += 1

        elif questionIndex == 0:  # filter by team and agile practice
            self.list.InsertColumn(0, column0[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(1, column1[questionIndex], wx.LIST_FORMAT_LEFT, width=600)

            itemIndex = 0
            for index, practice in enumerate(practiceName):
                if practice in self.frame_.practiceList:
                    practice = practice.replace("_", " ")
                    practice = practice.replace("Practice:", "")

                    itemIndex = self.list.InsertItem(itemIndex, practice)
                    # print (itemIndex, practice)
                    tmpitem = self.result[index][questionIndex][0].replace("_", " ")[len(prefix1[questionIndex]):]

                    self.list.SetItem(itemIndex, 1, tmpitem)
                    for i in range(len(self.result[index][questionIndex]) - 1):
                        itemIndex += i + 1
                        itemIndex = self.list.InsertItem(itemIndex, "")
                        # print (itemIndex,self.result[index][questionIndex][i+1])
                        tmpitem = self.result[index][questionIndex][i + 1].replace("_", " ")[
                                  len(prefix1[questionIndex]):]

                        self.list.SetItem(itemIndex, 1, tmpitem)
                    itemIndex += 1
                    itemIndex = self.list.InsertItem(itemIndex, "")
                    self.list.SetItem(itemIndex, 1, "")
                    itemIndex += 1

        elif questionIndex == 3:

            # print (self.frame_.resultByTeam)

            self.list.InsertColumn(0, "Practice", wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(1, "Activity", wx.LIST_FORMAT_LEFT, width=300)

            # print (self.frame_.resultByTeam)
            allTeamActivity = []

            for index, practice in enumerate(practiceName):

                if practice in self.frame_.practiceList:
                    practice = practice.replace("_", " ")
                    practice = practice.replace("Practice:", "")

                    activityByPractice = []
                    for i, eachActivity in enumerate(self.result[index][3]):
                        activityWithCause = False
                        causeByTeam = False

                        for j, eachActivitywithCause in enumerate(self.result[5][8]):
                            if eachActivity == eachActivitywithCause[1]:
                                activityWithCause = True
                                if eachActivitywithCause[0] in self.frame_.situationList:
                                    causeByTeam = True
                                    # cause = eachProblemwithCause[0]
                        if (activityWithCause == False) or (activityWithCause == True and causeByTeam == True):
                            self.teamActivity.append(
                                eachActivity.replace("Activity:", "").replace("1rst:", "").replace("2nd:", "").replace(
                                    "3rd:", "").replace("4th:", "").replace("5th:", "").replace("6th:", "").replace("_",
                                                                                                                    " "))
                            activityByPractice.append([practice, eachActivity.replace("Activity:", "").replace("1rst:",
                                                                                                               "").replace(
                                "2nd:", "").replace("3rd:", "").replace("4th:", "").replace("5th:", "").replace("6th:",
                                                                                                                "").replace(
                                "_", " ")])
                    activityByPractice = sorted(activityByPractice, key=lambda x: x[1])
                    allTeamActivity.append(activityByPractice)

            for index, eachActivityList in enumerate(allTeamActivity):
                previous1 = ''
                for index2, item in enumerate(eachActivityList):
                    if item[0] == previous1:
                        itemIndex = self.list.InsertItem(itemIndex, '')
                    else:
                        itemIndex = self.list.InsertItem(itemIndex, item[0])

                    self.list.SetItem(itemIndex, 1, item[1])
                    itemIndex += 1
                    previous1 = item[0]


        elif questionIndex == 4:

            # print (self.frame_.resultByTeam)
            previous1 = ""
            previous2 = ""
            self.list.InsertColumn(0, "Practice", wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(1, "Cause", wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(2, "Problem", wx.LIST_FORMAT_LEFT, width=300)
            # print (self.frame_.resultByTeam)
            allTeamProblem = []

            for index, practice in enumerate(practiceName):

                if practice in self.frame_.practiceList:
                    practice = practice.replace("_", " ")
                    practice = practice.replace("Practice:", "")

                    problemByPractice = []
                    for i, eachProblem in enumerate(self.result[index][4]):
                        problemWithCause = False
                        causeByTeam = False

                        cause = "Undefined cause"
                        for j, eachProblemwithCause in enumerate(self.result[5][6]):
                            if eachProblem == eachProblemwithCause[1]:
                                problemWithCause = True
                                if eachProblemwithCause[0] in self.frame_.situationList:
                                    causeByTeam = True
                                    cause = eachProblemwithCause[0]
                        if (problemWithCause == False) or (problemWithCause == True and causeByTeam == True):
                            problemByPractice.append([practice, cause.replace("Situation:", "").replace("_", " "),
                                                      eachProblem.replace("Problem:", "").replace("_", " ")])
                    problemByPractice = sorted(problemByPractice, key=lambda x: x[1])
                    allTeamProblem.append(problemByPractice)

            for index, eachProblemList in enumerate(allTeamProblem):
                previous1 = ''
                previous2 = ''
                for index2, item in enumerate(eachProblemList):
                    if item[0] == previous1:
                        itemIndex = self.list.InsertItem(itemIndex, '')
                    else:
                        itemIndex = self.list.InsertItem(itemIndex, item[0])

                    if item[1] == previous2:
                        self.list.SetItem(itemIndex, 1, '')
                    else:
                        self.list.SetItem(itemIndex, 1, item[1])

                    self.list.SetItem(itemIndex, 2, item[2])
                    itemIndex += 1
                    previous1 = item[0]
                    previous2 = item[1]
        elif questionIndex == 5:
            previous1 = ""
            previous2 = ""
            self.list.InsertColumn(0, "Practice", wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(1, "Problem", wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(2, "Solution", wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(3, "In reponsible of", wx.LIST_FORMAT_LEFT, width=300)

            allTeamProblem = []

            for index, practice in enumerate(practiceName):

                if practice in self.frame_.practiceList:
                    practice = practice.replace("_", " ")
                    practice = practice.replace("Practice:", "")

                    problemByPractice = []
                    for i, eachProblem in enumerate(self.result[index][4]):
                        problemWithCause = False
                        causeByTeam = False

                        cause = "Undefined cause"
                        for j, eachProblemwithCause in enumerate(self.result[5][6]):
                            if eachProblem == eachProblemwithCause[1]:
                                problemWithCause = True
                                if eachProblemwithCause[0] in self.frame_.situationList:
                                    causeByTeam = True
                                    cause = eachProblemwithCause[0]
                        if (problemWithCause == False) or (problemWithCause == True and causeByTeam == True):

                            if eachProblem in self.frame_.ProblemWithSolution:
                                for j, eachProblemSolution in enumerate(self.frame_.SolutionProblemList):

                                    if eachProblem == eachProblemSolution[0]:
                                        for k, eachSolutionRole in enumerate(self.result[5][9]):
                                            if (eachSolutionRole[0] == eachProblemSolution[1]):
                                                problemByPractice.append(
                                                    [practice, eachProblem.replace("Problem:", "").replace("_", " "),
                                                     eachProblemSolution[1].replace("Solution:", "").replace("_", " "),
                                                     eachSolutionRole[1].replace("Role:", "").replace("_", " ")])

                            else:
                                problemByPractice.append(
                                    [practice, eachProblem.replace("Problem:", "").replace("_", " "), "", ""])

                    problemByPractice = sorted(problemByPractice, key=lambda x: x[1])
                    allTeamProblem.append(problemByPractice)

            # print ("allTeamProblem:",allTeamProblem)
            for index, eachProblemList in enumerate(allTeamProblem):
                previous1 = ''
                previous2 = ''
                for index2, item in enumerate(eachProblemList):
                    if item[0] == previous1:
                        itemIndex = self.list.InsertItem(itemIndex, '')
                    else:
                        itemIndex = self.list.InsertItem(itemIndex, item[0])

                    if item[1] == previous2:
                        self.list.SetItem(itemIndex, 1, '')
                    else:
                        self.list.SetItem(itemIndex, 1, item[1])

                    self.list.SetItem(itemIndex, 2, item[2])
                    self.list.SetItem(itemIndex, 3, item[3])
                    itemIndex += 1
                    previous1 = item[0]
                    previous2 = item[1]


        elif questionIndex == 6 or questionIndex == 7:
            previous = ""
            previous2 = ""

            self.list.InsertColumn(0, column0[questionIndex], wx.LIST_FORMAT_LEFT, width=350)
            self.list.InsertColumn(1, column1[questionIndex], wx.LIST_FORMAT_LEFT, width=350)
            self.list.InsertColumn(2, column2[questionIndex], wx.LIST_FORMAT_LEFT, width=200)
            for i, each in enumerate(self.result[5][questionIndex - 6]):
                if (each[0] in self.frame_.situationList):

                    for index, practice in enumerate(practiceName):
                        if practice in self.frame_.practiceList:
                            for j, eachRequisite in enumerate(self.result[index][9]):
                                if (each[1] == eachRequisite):
                                    if each[0].replace("_", " ")[len(prefix0[questionIndex]):] == previous:
                                        itemIndex = self.list.InsertItem(itemIndex, '')
                                    else:
                                        itemIndex = self.list.InsertItem(itemIndex, each[0].replace("_", " ")[
                                                                                    len(prefix0[questionIndex]):])

                                    if each[1].replace("_", " ")[len(prefix1[questionIndex]):] == previous2:
                                        itemIndex = self.list.InsertItem(itemIndex, '')

                                    else:
                                        self.list.SetItem(itemIndex, 1,
                                                          each[1].replace("_", " ")[len(prefix1[questionIndex]):])

                                    self.list.SetItem(itemIndex, 2, practice.replace("Practice:", "").replace("_", " "))

                                    itemIndex += 1
                                    previous = each[0].replace("_", " ")[len(prefix0[questionIndex]):]
                                    previous2 = each[1].replace("_", " ")[len(prefix1[questionIndex]):]

        elif questionIndex == 8 or questionIndex == 9:

            previous = ""
            self.list.InsertColumn(0, column0[questionIndex], wx.LIST_FORMAT_LEFT, width=450)
            self.list.InsertColumn(1, column1[questionIndex], wx.LIST_FORMAT_LEFT, width=450)
            for i, each in enumerate(self.result[5][questionIndex - 6]):

                if each[0] in self.frame_.principleList or each[0] in self.frame_.valueList:
                    if each[0].replace("_", " ") == previous:
                        itemIndex = self.list.InsertItem(itemIndex, '')
                    else:
                        itemIndex = self.list.InsertItem(itemIndex,
                                                         each[0].replace("_", " ")[len(prefix0[questionIndex]):])
                    self.list.SetItem(itemIndex, 1, each[1].replace("_", " ")[len(prefix1[questionIndex]):])
                    itemIndex += 1
                    previous = each[0].replace("_", " ")

        elif questionIndex == 10 or questionIndex == 11:
            previous = ""
            self.list.InsertColumn(0, column0[questionIndex], wx.LIST_FORMAT_LEFT, width=450)
            self.list.InsertColumn(1, column1[questionIndex], wx.LIST_FORMAT_LEFT, width=450)
            for i, each in enumerate(self.result[5][questionIndex - 6]):

                if each[0] in self.frame_.principleList or each[0] in self.frame_.valueList:
                    if each[0].replace("_", " ") == previous:
                        itemIndex = self.list.InsertItem(itemIndex, '')
                    else:
                        itemIndex = self.list.InsertItem(itemIndex,
                                                         each[0].replace("_", " ")[len(prefix0[questionIndex]):])
                    self.list.SetItem(itemIndex, 1, each[1].replace("_", " ")[len(prefix1[questionIndex]):])
                    itemIndex += 1
                    previous = each[0].replace("_", " ")

        elif questionIndex == 12 or questionIndex == 13:
            teamActivity = []

            for index, practice in enumerate(practiceName):
                if practice in self.frame_.practiceList:
                    practice = practice.replace("_", " ")
                    practice = practice.replace("Practice:", "")

                    activityByPractice = []
                    for i, eachActivity in enumerate(self.result[index][3]):
                        activityWithCause = False
                        causeByTeam = False

                        for j, eachActivitywithCause in enumerate(self.result[5][8]):
                            if eachActivity == eachActivitywithCause[1]:
                                activityWithCause = True
                                if eachActivitywithCause[0] in self.frame_.situationList:
                                    causeByTeam = True

                        if (activityWithCause == False) or (activityWithCause == True and causeByTeam == True):
                            teamActivity.append(
                                eachActivity.replace("Activity:", "").replace("1rst:", "").replace("2nd:", "").replace(
                                    "3rd:", "").replace("4th:", "").replace("5th:", "").replace("6th:", "").replace("_",
                                                                                                                    " "))

            previous1 = ""
            previous2 = ""
            self.list.InsertColumn(0, column0[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(1, column1[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
            self.list.InsertColumn(2, column2[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
            itemIndex = 0

            for index, practice in enumerate(practiceName):
                if practice in self.frame_.practiceList:

                    if len(self.result[index][questionIndex - 5]) > 0:
                        practice = practice.replace("_", " ")
                        practice = practice.replace("Practice:", "")
                    # print(self.result[index][questionIndex])
                    for i, each in enumerate(self.result[index][questionIndex - 5]):
                        tmpitem = each[1].replace("_", " ").replace(prefix2[questionIndex], "").replace("1rst:",
                                                                                                        "").replace(
                            "2nd:", "").replace("3rd:", "").replace("4th:", "").replace("5th:", "").replace("6th:", "")

                        if (tmpitem in teamActivity):
                            if previous1 == practice:
                                itemIndex = self.list.InsertItem(itemIndex, "")

                            else:
                                itemIndex = self.list.InsertItem(itemIndex, practice)
                                previous1 = practice
                            if previous2 == each[0]:
                                self.list.SetItem(itemIndex, 1, '')
                            else:
                                self.list.SetItem(itemIndex, 1,
                                                  each[0].replace("_", " ").replace(prefix1[questionIndex], ""))
                                previous2 = each[0]
                            self.list.SetItem(itemIndex, 2, tmpitem)
                            itemIndex += 1
        elif questionIndex == 14:
            previous = ""
            itemIndex = 0
            self.list.InsertColumn(0, column0[questionIndex], wx.LIST_FORMAT_LEFT, width=450)
            self.list.InsertColumn(1, column1[questionIndex], wx.LIST_FORMAT_LEFT, width=450)

            for index, practice in enumerate(practiceName):
                if practice in self.frame_.practiceList:
                    for i, each in enumerate(
                            self.result[index][9]):  # 9 is the index of query for requisite of each practice

                        if practice == previous:
                            itemIndex = self.list.InsertItem(itemIndex, '')
                        else:
                            itemIndex = self.list.InsertItem(itemIndex,
                                                             practice.replace("_", " ").replace("Practice:", ""))
                            previous = practice
                        self.list.SetItem(itemIndex, 1, each.replace("_", " ")[len(prefix1[questionIndex]):])
                        itemIndex += 1

        else:  # questionIndex == 15
            previous = ""
            itemIndex = 0
            self.list.InsertColumn(0, column0[questionIndex], wx.LIST_FORMAT_LEFT, width=450)
            self.list.InsertColumn(1, column1[questionIndex], wx.LIST_FORMAT_LEFT, width=450)
            for index, practice in enumerate(practiceName):
                if practice in self.frame_.practiceList:
                    for i, each in enumerate(
                            self.result[index][12]):  # 12 is the index of query for lesson learn of each practice
                        if practice == previous:
                            itemIndex = self.list.InsertItem(itemIndex, '')
                        else:
                            itemIndex = self.list.InsertItem(itemIndex,
                                                             practice.replace("_", " ").replace("Practice:", ""))
                            previous = practice

                        self.list.SetItem(itemIndex, 1, each.replace("_", " ")[len(prefix1[questionIndex]):])
                        itemIndex += 1

    def resultPage1(self, event):
        # self.Hide() #hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult() #calculate all the result
        # new_frame = ResultPage1(self) #open the page to display result
        # new_frame.Show()
        self.frame_.m_auinotebook1.SetSelection(1)


class SparqlQueries:
    def __init__(self, parent, frame_):
        self.frame_ = frame_

        #        owlready2.JAVA_EXE = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Java\java.exe"
        self.my_world = World()
        self.myOnto = self.my_world.get_ontology(
            "./AgileOntology02_10_19.owl").load()  # path to the owl file is given here
        # print("Ontology load")
        sync_reasoner(self.my_world, debug=1, infer_property_values=True,
                      keep_tmp_file=True)  # reasoner is started and synchronized here
        self.graph = self.my_world.as_rdflib_graph()

    def createNewInstance(self):
        # self.my_world = World()
        # self.myOnto =self.my_world.get_ontology("AgileOntology9_4_19.owl").load()
        self.situationList = self.frame_.situationList
        self.practiceList = self.frame_.practiceList
        self.principleList = self.frame_.principleList
        self.valueList = self.frame_.valueList
        self.tmpTeam = self.myOnto.Team("Team:Tmp_team")
        for i in range(len(self.situationList)):
            if self.situationList[i] != u"Unknown":
                situation = self.myOnto.Situation(self.situationList[i])
                self.tmpTeam.Have.append(situation)

        for i in range(len(self.practiceList)):
            practice = self.myOnto.Practice(self.practiceList[i])
            self.tmpTeam.Adopt.append(practice)
        # print (self.tmpTeam)

    ##        sync_reasoner(self.my_world, debug=1, infer_property_values=True, keep_tmp_file=True)  # reasoner is started and synchronized here
    ##        self.graph = self.my_world.as_rdflib_graph()
    ##        query = u'''
    ##            PREFIX owl: <http://www.w3.org/2002/07/owl#>
    ##            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    ##            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    ##            PREFIX agile: <http://www.semanticweb.org/skiv/ontologies/2016/9/untitled-ontology-6#>
    ##
    ##            SELECT DISTINCT  ?instance_y ?instance_x  ?solution
    ##                    WHERE {
    ##                    ?team rdf:type agile:Team.
    ##                    ?team agile:Encounter ?instance_x.
    ##                    ?instance_x rdf:type agile:Problem.
    ##                    ?instance_x agile:Caused_by ?instance_y.
    ##                    ?solution agile:Solve ?instance_x.
    ##                    FILTER( regex(str(?team), "Test"))
    ##                    }
    ##
    ##            Order by ?instance_y'''
    ##        resultsList = self.graph.query(query)
    ##        #print (len(resultsList))
    ##        # creating json object
    ##        response = []
    ##        for item in resultsList:
    ##            s = str(item['instance_y'].toPython())
    ##            s = re.sub(r'.*#', "", s)
    ##            p = str(item['instance_x'].toPython())
    ##            p = re.sub(r'.*#', "", p)
    ##            q = str(item['solution'].toPython())
    ##            q = re.sub(r'.*#', "", q)
    ##
    ##            response.append([s,p,q])
    ##
    ##        self.frame_.resultByTeam = response
    ##        #print(response)  # just to show the output
    ##        #return response

    def search(self, practice):
        queryPrefix = u'''PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX agile: <http://www.semanticweb.org/skiv/ontologies/2016/9/untitled-ontology-6#>

            '''
        if practice in ["Daily", "Short", "planning", "review", "retrospective"]:
            queryList = ['''SELECT DISTINCT ?practice ?instance_x
            WHERE { 
            ?practice rdf:type agile:Practice.
            ?practice agile:Achieve ?instance_x.
            ?instance_x rdf:type agile:Goal.
            FILTER( regex(str(?practice), "''' + practice + '''"))}
            ''',
                         '''SELECT DISTINCT ?practice ?instance_x ?instance_y
                         WHERE { 
                         ?practice rdf:type agile:Practice.
                         ?practice agile:Achieve ?instance_x.
                         ?instance_x rdf:type agile:Value.
                         
                         ?instance_y rdf:type agile:Principle.
                         ?practice agile:Achieve ?instance_y.
                         
                         ?instance_y agile:Contribute_to ?instance_x.
                         FILTER( regex(str(?practice), "''' + practice + '''"))}

            ''',
                         '''SELECT DISTINCT ?practice ?instance_x ?instance_y
                         WHERE { 
                         ?practice rdf:type agile:Practice.
                         ?practice agile:Achieve ?instance_x.
                         ?instance_x rdf:type agile:Principle.
                         
                         ?instance_y rdf:type agile:Goal.
                         ?practice agile:Achieve ?instance_y.
                         
                         ?instance_y agile:Contribute_to ?instance_x.
                         FILTER( regex(str(?practice), "''' + practice + '''"))}
            ''',
                         '''SELECT DISTINCT ?practice ?instance_x 
                         WHERE { 
                         ?practice rdf:type agile:Practice.
                         ?practice agile:Composed_of ?instance_x.
                         ?instance_x rdf:type agile:Activity.
                         ?instance_y rdf:type agile:Team.
                         ?instance_x agile:Performed_by ?instance_y.
                         FILTER( regex(str(?practice),  "''' + practice + '''"))}
            ORDER By  ?instance_y ?instance_x

            ''',
                         '''SELECT DISTINCT ?practice ?instance_x
                            WHERE { 
                                 ?practice rdf:type agile:Practice.
                                 ?practice agile:Encounter ?instance_x.
                                 ?instance_x rdf:type agile:Problem.
                                 FILTER( regex(str(?practice), "''' + practice + '''"))}
            ''',
                         '''SELECT DISTINCT ?practice ?instance_x ?instance_y
                             WHERE
                                 {?practice rdf:type agile:Practice.
                                 ?practice agile:Require ?instance_y.
                                 ?instance_y rdf:type agile:Requisite.
                                 ?instance_y agile:Harmed_by ?instance_x.
                                 FILTER( regex(str(?practice),"''' + practice + '''") &&( regex(str(?instance_x),"Activity:") || (regex(str(?instance_x),"Situation:"))))
          		
                        }
          		order by ?instance_x
            ''',
                         '''SELECT DISTINCT ?practice ?instance_x ?instance_y
                            WHERE
                                {?practice rdf:type agile:Practice.
                                ?practice agile:Require ?instance_y.
                                ?instance_y rdf:type agile:Requisite.
                                ?instance_y agile:Helped_by ?instance_x.
                                FILTER( regex(str(?practice),"''' + practice + '''") &&( regex(str(?instance_x),"Activity:") || (regex(str(?instance_x),"Situation:"))))
          		
                        }
          		order by ?instance_x
            ''',

                         '''SELECT DISTINCT ?practice ?instance_x ?instance_y
                            WHERE { 
                                 ?practice rdf:type agile:Practice.
                                 ?practice agile:Require ?instance_x.
                                 ?instance_x rdf:type agile:Artifact.
                                 ?instance_y rdf:type agile:Activity.
                                 ?instance_y agile:Part_of ?practice.
                                 ?instance_y agile:Require ?instance_x.
                      FILTER( regex(str(?practice), "''' + practice + '''"))}''',
                         '''SELECT DISTINCT ?practice ?instance_x ?instance_y
                               WHERE { 
                                    ?practice rdf:type agile:Practice.
                                    ?practice agile:Require ?instance_x.
                                    ?instance_x rdf:type agile:Role.
                                    ?instance_y rdf:type agile:Activity.
                                    ?instance_y agile:Part_of ?practice.
                                    ?instance_y agile:In_Responsible_of ?instance_x.
                                   FILTER( regex(str(?practice), "''' + practice + '''"))}''',
                         '''
                             SELECT DISTINCT ?practice ?instance_x
                             WHERE { 
                             ?practice rdf:type agile:Practice.
                             ?practice agile:Require ?instance_x.
                             ?instance_x rdf:type agile:Requisite.
                             FILTER( regex(str(?practice), "''' + practice + '''"))}
            ''',

                         '''SELECT DISTINCT ?practice ?instance_x
                           WHERE { 
                           ?practice rdf:type agile:Practice.
                           ?practice agile:Achieve ?instance_x.
                           ?instance_x rdf:type agile:Value.
                           FILTER( regex(str(?practice), "''' + practice + '''"))}

            ''',
                         '''SELECT DISTINCT ?practice ?instance_x
                         WHERE { 
                         ?practice rdf:type agile:Practice.
                         ?practice agile:Achieve ?instance_x.
                         ?instance_x rdf:type agile:Principle.
                         FILTER( regex(str(?practice), "''' + practice + '''"))}
            ''',
                         '''SELECT DISTINCT ?practice ?instance_x
                           WHERE { 
                           ?practice rdf:type agile:Practice.
                           ?practice agile:Have ?instance_x.
                           ?instance_x rdf:type agile:Lesson_Learn.
                           FILTER( regex(str(?practice), "''' + practice + '''"))}''']
        else:
            queryList = [
                '''SELECT DISTINCT  ?instance_x ?instance_y
           	 WHERE
            		{
           	 	?instance_x agile:Harm ?instance_y.
            		FILTER(  (regex(str(?instance_x),"Situation:"))&&(( regex(str(?instance_y),"Requisite:"))))
          		
                        }
          		order by ?instance_x ''',
                '''SELECT DISTINCT  ?instance_x ?instance_y
                         WHERE
                                {
                                ?instance_x agile:Help ?instance_y.
                                FILTER(  (regex(str(?instance_x),"Situation:"))&&(( regex(str(?instance_y),"Requisite:"))))
                                
                                }
                                order by ?instance_x''',
                '''SELECT DISTINCT  ?instance_x ?instance_y  
                   WHERE { 
                   
                   ?instance_y rdf:type agile:Practice.
                   ?instance_x rdf:type agile:Principle.
                   ?instance_y agile:Achieve ?instance_x.
                  }
                   
                   Order by ?instance_x
                   ''',
                '''SELECT DISTINCT  ?instance_x ?instance_y  
                WHERE { 
                
                ?instance_y rdf:type agile:Practice.
                ?instance_x rdf:type agile:Value.
                ?instance_y agile:Achieve ?instance_x.
               }
                
                Order by ?instance_x
                ''',
                '''SELECT DISTINCT  ?instance_x ?instance_y  
                WHERE { 
                
                ?instance_y rdf:type agile:Goal.
                ?instance_x rdf:type agile:Principle.
                ?instance_y agile:Contribute_to ?instance_x.
               }
                
                Order by ?instance_x''',
                '''SELECT DISTINCT  ?instance_x ?instance_y  
                WHERE { 
                
                ?instance_y rdf:type agile:Goal.
                ?instance_x rdf:type agile:Value.
                ?instance_y agile:Contribute_to ?instance_x.
               }
                
                Order by ?instance_x''',
                '''SELECT DISTINCT  ?instance_x ?instance_y
                         WHERE
                                {
                                ?instance_x agile:Cause ?instance_y.
                                ?instance_y rdf:type agile:Problem.
                                FILTER(  regex(str(?instance_x),"Activity:") || (regex(str(?instance_x),"Situation:"))|| (regex(str(?instance_x),"Problem:")))
                                
                                }
                                order by ?instance_x''',
                '''SELECT DISTINCT   ?instance_x ?instance_y
                         WHERE
                                {
                                ?instance_x agile:Solved_by ?instance_y.
                                ?instance_x rdf:type agile:Problem.
                                ?instance_y rdf:type agile:Solution.
                                
                                
                                }
                                order by ?instance_x''',
                '''SELECT DISTINCT  ?instance_x ?instance_y
                        WHERE
                               { 
                               ?instance_x agile:Lead_to ?instance_y.
                               ?instance_y rdf:type agile:Activity.
                               
                               }
                               order by ?instance_x''',

                '''SELECT DISTINCT ?instance_x ?instance_y
           	WHERE { 
            		
           	 	
            		?instance_x rdf:type agile:Solution.
            		?instance_y rdf:type agile:Role.
        
            		?instance_x agile:In_Responsible_of ?instance_y.
          		}''']

        resultList = []  # list of result for all the queries

        for index in range(len(queryList)):
            wholeQuery = queryPrefix + queryList[index]

            # print(wholeQuery)
            result = self.graph.query(wholeQuery)  # list of result for each query
            # creating json object
            response = []
            # print ("result:" , str(result))

            for item in result:
                s = str(item['instance_x'].toPython())
                s = re.sub(r'.*#', "", s)
                # print ("s", s)
                if index == 1 or index == 2 or index == 5 or index == 6 or index == 7 or index == 8 or practice == None:  # for the query with more than two variables.
                    p = str(item['instance_y'].toPython())
                    p = re.sub(r'.*#', "", p)

                    response.append([s, p])
                else:
                    if s not in response:
                        response.append(s)  # list of result for each query in the text format
            resultList.append(response)  # add list of result for each query to the list

        return resultList

    def queryAllResult(self):
        siutationList = []
        practiceList = ["Daily", "Short", "planning", "review", "retrospective"]
        goalList = []
        allResult = []
        tmp_result = []
        if self.frame_.generalResult == []:
            if os.path.exists(u'queryByPractice.pkl'):
                self.frame_.generalResult = joblib.load(u'queryByPractice.pkl')

            else:

                for i in range(len(practiceList)):
                    tmp_result.append(self.search(practiceList[i]))
                tmp_result.append(self.search(practice=None))
                # print(len(tmp_result),self.search(practice=None))

                joblib.dump(tmp_result, u'queryByPractice.pkl')
                # print("dump")
                self.frame_.generalResult = tmp_result

        return self.frame_.generalResult

    ###########################################################################


## Class Panel
###########################################################################

class MainPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Welcome", wx.DefaultPosition, wx.Size(-1, -1),
                                           wx.ALIGN_CENTRE)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        bSizer20.Add(self.m_staticText2, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button1 = wx.Button(self.m_panel3, wx.ID_ANY, u"Continue", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer20.Add(self.m_button1, 0, wx.ALL, 5)

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
        self.frame.Hide()  # hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult() #calculate all the result
        new_frame = InputPage(self)  # open the page to display result
        new_frame.Show()
