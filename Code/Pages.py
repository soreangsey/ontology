# -*- coding: utf-8 -*- 

import wx
import wx.xrc
from owlready2 import *
from sklearn.externals import joblib


###########################################################################
## Class First page
###########################################################################

class InputPage(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Input page", pos=wx.DefaultPosition, size=(800, 600),
                          style=wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.MINIMIZE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)

        # self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))
        bSizer0 = wx.BoxSizer(wx.VERTICAL)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, -1),
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText4 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY,
                                           u"Please select the situation of your team", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))
        self.m_staticText4.Wrap(-1)
        bSizer7.Add(self.m_staticText4, 0, wx.ALL, 5)

        lblList = [u"Unknown", u"Situation:Big organization: more than 500 people",
                   u"Situation:Medium organization: between 100 to 500 people",
                   u"Situation:Small organization:less than 100 people"]
        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"1. Organization size",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)
        # self.rbox1 = wx.RadioBox(self.m_scrolledWindow1, label = '1. Organization size', pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox1 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[1], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox1, 0, wx.ALL, 5)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"2. Team size", wx.DefaultPosition,
                                          wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Situation:Big team more than 10", u"Situation:Medium team between 5 and 10",
                   u"Situation:Small team less than 5"]
        # self.rbox2 = wx.RadioBox(self.m_scrolledWindow1, label = '2. Team size', pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox2 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[1], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox2, 0, wx.ALL, 5)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"3. Team distribution",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Situation:Distributed Team", u"Situation:Same site"]
        # self.rbox3 = wx.RadioBox(self.m_scrolledWindow1, label = '3. Team distribution', pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox3 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[1], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox3, 0, wx.ALL, 5)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"4. Agile maturity level",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Situation:No agile experience", u"Situation:1 years agile experience",
                   u"Situation:2 years agile experience", u"Situation:3 years agile experience",
                   u"Situation:4 years agile experience", u"Situation:5 years agile experience",
                   u"Situation:Some experience in agile"]
        # self.rbox4 = wx.RadioBox(self.m_scrolledWindow1, label = u"4. Agile maturity level", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox4 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[1], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox4, 0, wx.ALL, 5)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"5. Type of communication",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)

        lblList = [u"Unknown", u"Situation:Face to face communication", u"Situation:Virtual communication"]
        # self.rbox5 = wx.RadioBox(self.m_scrolledWindow1, label = u"5. Type of communication", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox5 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[1], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox5, 0, wx.ALL, 5)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"6. Domain of knowledge maturity level",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer7.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Situation:No domain knowledge", u"Situation:Experience in domain knowledge",
                   u"Situation:Expert in domain knowledge"]
        # self.rbox6 = wx.RadioBox(self.m_scrolledWindow1, label = u"6. Domain of knowledge maturity level", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox6 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, lblList[1], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer7.Add(self.rbox6, 0, wx.ALL, 5)

        self.m_scrolledWindow1.SetSizer(bSizer7)
        self.m_scrolledWindow1.Layout()
        bSizer5.Add(self.m_scrolledWindow1, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 0)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow2 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow2.SetScrollRate(5, 5)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"7.  Management support level",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer8.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Situation:Poor management support", u"Situation:Average management support",
                   u"Situation:High management support"]
        # self.rbox7 = wx.RadioBox(self.m_scrolledWindow2, label = u"7.  Management support level", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox7 = wx.ComboBox(self.m_scrolledWindow2, wx.ID_ANY, lblList[1], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer8.Add(self.rbox7, 0, wx.ALL, 5)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY,
                                          u"8. Project management in previous project", wx.DefaultPosition,
                                          wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer8.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Waterfall", u"eXtreme Programming"]
        # self.rbox8 = wx.RadioBox(self.m_scrolledWindow2, label = u"8. Project management in previous project", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox8 = wx.ComboBox(self.m_scrolledWindow2, wx.ID_ANY, lblList[1], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer8.Add(self.rbox8, 0, wx.ALL, 5)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"9. Project size", wx.DefaultPosition,
                                          wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer8.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Situation:Small project less than 2 years",
                   u"Situation:Medium project between 2 to 5 years", u"Situation:Big project more than 5 years"]
        # self.rbox9 = wx.RadioBox(self.m_scrolledWindow2, label = u"9. Project size", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox9 = wx.ComboBox(self.m_scrolledWindow2, wx.ID_ANY, lblList[1], wx.DefaultPosition, wx.Size(700, -1),
                                 style=wx.CB_READONLY, choices=lblList)
        bSizer8.Add(self.rbox9, 0, wx.ALL, 5)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"10. Requirements  stability",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer8.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Situation:Unstable Requirement", u"Situation:Stable Requirement"]
        # self.rbox10 = wx.RadioBox(self.m_scrolledWindow2, label = u"10. Requirements  stability", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox10 = wx.ComboBox(self.m_scrolledWindow2, wx.ID_ANY, lblList[1], wx.DefaultPosition, wx.Size(700, -1),
                                  style=wx.CB_READONLY, choices=lblList)
        bSizer8.Add(self.rbox10, 0, wx.ALL, 5)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"11. Technology knowledge level",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer8.Add(self.m_staticText, 0, wx.ALL, 5)
        lblList = [u"Unknown", u"Situation:Novice in techonology knowledge",
                   u"Situation:Experience in techonology knowledge", u"Situation:Expert in techonology knowledge",
                   u"Situation:Cross compentence in technology knowledge"]
        # self.rbox11 = wx.RadioBox(self.m_scrolledWindow2, label = u"11. Technology knowledge level", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox11 = wx.ComboBox(self.m_scrolledWindow2, wx.ID_ANY, lblList[1], wx.DefaultPosition, wx.Size(700, -1),
                                  style=wx.CB_READONLY, choices=lblList)
        bSizer8.Add(self.rbox11, 0, wx.ALL, 5)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"12. User availability level",
                                          wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText.Wrap(-1)
        bSizer8.Add(self.m_staticText, 0, wx.ALL, 5)

        lblList = [u"Unknown", u"Situation:User hardly available", u"Situation:User availlable time to time",
                   u"Situation:User highly available"]
        # self.rbox12 = wx.RadioBox(self.m_scrolledWindow2, label = u"12. User availability level", pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.rbox12 = wx.ComboBox(self.m_scrolledWindow2, wx.ID_ANY, lblList[1], wx.DefaultPosition, wx.Size(700, -1),
                                  style=wx.CB_READONLY, choices=lblList)
        bSizer8.Add(self.rbox12, 0, wx.ALL, 5)

        self.m_scrolledWindow2.SetSizer(bSizer8)
        self.m_scrolledWindow2.Layout()
        bSizer8.Fit(self.m_scrolledWindow2)
        bSizer6.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer6, 1, wx.EXPAND, 0)
        bSizer0.Add(bSizer1, 1, wx.EXPAND, 0)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Next", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer0.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        self.SetSizer(bSizer0)
        self.Layout()

        self.Centre(wx.BOTH)
        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.ShowNextFrame)

    def __del__(self):
        pass

    def ShowNextFrame(self, event):
        self.situationList = []
        self.situationList.append(self.rbox1.GetStringSelection().replace(' ', '_'))
        self.situationList.append(self.rbox2.GetStringSelection().replace(' ', '_'))
        self.situationList.append(self.rbox3.GetStringSelection().replace(' ', '_'))
        self.situationList.append(self.rbox4.GetStringSelection().replace(' ', '_'))
        self.situationList.append(self.rbox5.GetStringSelection().replace(' ', '_'))
        self.situationList.append(self.rbox6.GetStringSelection().replace(' ', '_'))
        self.situationList.append(self.rbox7.GetStringSelection().replace(' ', '_'))
        self.situationList.append(self.rbox8.GetStringSelection().replace(' ', '_'))
        self.situationList.append(self.rbox9.GetStringSelection().replace(' ', '_'))
        self.situationList.append(self.rbox10.GetStringSelection().replace(' ', '_'))
        self.situationList.append(self.rbox11.GetStringSelection().replace(' ', '_'))
        self.situationList.append(self.rbox12.GetStringSelection().replace(' ', '_'))

        print(self.situationList)
        self.Hide()  # hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult(inputList) #calculate all the result
        new_frame = InputPage2(self)  # open the page to the input page 2
        new_frame.Show()


class InputPage2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Input page", pos=wx.DefaultPosition,
                          size=wx.Size(1050, 676),
                          style=wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.MINIMIZE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)
        self.situationList = parent.situationList
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))
        bSizer0 = wx.BoxSizer(wx.VERTICAL)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, -1),
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText4 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY,
                                           u"Please select agile practice(s) you adopted or want  to adopt",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer7.Add(self.m_staticText4, 0, wx.ALL, 5)
        self.m_staticText4.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))

        self.m_checkBox1 = wx.CheckBox(self.m_scrolledWindow1, wx.ID_ANY, u"Daily Meeting", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer7.Add(self.m_checkBox1, 0, wx.ALL, 5)

        self.m_checkBox2 = wx.CheckBox(self.m_scrolledWindow1, wx.ID_ANY, u"Short Iteration", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer7.Add(self.m_checkBox2, 0, wx.ALL, 5)

        self.m_checkBox3 = wx.CheckBox(self.m_scrolledWindow1, wx.ID_ANY, u"Sprint Planning", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer7.Add(self.m_checkBox3, 0, wx.ALL, 5)

        self.m_checkBox4 = wx.CheckBox(self.m_scrolledWindow1, wx.ID_ANY, u"Sprint Review", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer7.Add(self.m_checkBox4, 0, wx.ALL, 5)

        self.m_checkBox5 = wx.CheckBox(self.m_scrolledWindow1, wx.ID_ANY, u"Sprint Retrospective", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer7.Add(self.m_checkBox5, 0, wx.ALL, 5)

        self.m_scrolledWindow1.SetSizer(bSizer7)
        self.m_scrolledWindow1.Layout()
        bSizer5.Add(self.m_scrolledWindow1, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 2, wx.EXPAND, 0)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow2 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow2.SetScrollRate(5, 5)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY,
                                           u"Please select agile principle(s) you want to achieve", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer8.Add(self.m_staticText5, 0, wx.ALL, 5)
        self.m_staticText5.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))

        self.m_checkBox6 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                       u"Our highest priority is to satisfy the customer through early and continuous delivery of valuable software",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox6, 0, wx.ALL, 5)

        self.m_checkBox7 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                       u"Welcome changing requirements, even late in development. Agile processes harness change for the customer's competitive advantage",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox7, 0, wx.ALL, 5)

        self.m_checkBox8 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                       u"Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox8, 0, wx.ALL, 5)

        self.m_checkBox9 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                       u"Business people and developers must work together daily throughout the project",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox9, 0, wx.ALL, 5)

        self.m_checkBox10 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"Build projects around motivated individuals. Give them the environment and support they need, and trust them to get the job done",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox10, 0, wx.ALL, 5)

        self.m_checkBox11 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"The most efficient and effective method of conveying information to and within a development team is face-to-face conversation",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox11, 0, wx.ALL, 5)

        self.m_checkBox12 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"Working software is the primary measure of progress", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox12, 0, wx.ALL, 5)

        self.m_checkBox13 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"Agile processes promote sustainable development. The sponsors, developers, and users should be able to maintain a constant pace indefinitely",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox13, 0, wx.ALL, 5)

        self.m_checkBox14 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"Continuous attention to technical excellence and good design enhances agility",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox14, 0, wx.ALL, 5)

        self.m_checkBox15 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"Simplicity--the art of maximizing the amount of work not done--is essential",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox15, 0, wx.ALL, 5)

        self.m_checkBox16 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"The best architectures, requirements, and designs emerge from self-organizing teams",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox16, 0, wx.ALL, 5)

        self.m_checkBox17 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"At regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox17, 0, wx.ALL, 5)

        self.m_staticText = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText.Wrap(-1)
        bSizer8.Add(self.m_staticText, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY,
                                           u"\n Please select agile value(s) you want to achieve", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer8.Add(self.m_staticText6, 0, wx.ALL, 5)
        self.m_staticText6.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))

        self.m_checkBox18 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"Individuals and interactions over processes and tools", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox18, 0, wx.ALL, 5)

        self.m_checkBox19 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"Working software over comprehensive documentation", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox19, 0, wx.ALL, 5)

        self.m_checkBox20 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"Customer collaboration over contract negotiation", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox20, 0, wx.ALL, 5)

        self.m_checkBox21 = wx.CheckBox(self.m_scrolledWindow2, wx.ID_ANY,
                                        u"Responding to change over following a plan", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer8.Add(self.m_checkBox21, 0, wx.ALL, 5)

        self.m_scrolledWindow2.SetSizer(bSizer8)
        self.m_scrolledWindow2.Layout()
        bSizer8.Fit(self.m_scrolledWindow2)
        bSizer6.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer6, 3, wx.EXPAND, 0)

        self.m_button0 = wx.Button(self, wx.ID_ANY, u"Back to first input page", wx.Point(-1, -1), wx.DefaultSize, 0)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Calculate result", wx.Point(-1, -1), wx.DefaultSize, 0)

        bSizer2.Add(self.m_button0, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        bSizer2.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        bSizer0.Add(bSizer1, 12, wx.EXPAND, 0)
        bSizer0.Add(bSizer2, 1, wx.ALL | wx.ALIGN_RIGHT, 0)

        self.SetSizer(bSizer0)
        self.Layout()

        self.Centre(wx.BOTH)
        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.ShowNextFrame)
        self.m_button0.Bind(wx.EVT_BUTTON, self.ShowFirstInputFrame)

    def __del__(self):
        pass

    def ShowFirstInputFrame(self, event):
        self.Hide()  # hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult(inputList) #calculate all the result
        new_frame = InputPage(self)  # open the page to the input page 2
        new_frame.Show()

    def ShowNextFrame(self, event):
        self.practiceList = []
        practiceName = [u"Practice:Daily_meeting", u"Practice:Short_iteration", u"Practice:Sprint_planning",
                        u"Practice:Sprint_review", u"Practice:Sprint_retrospective"]
        practiceCheckBox = [self.m_checkBox1, self.m_checkBox2, self.m_checkBox3, self.m_checkBox4, self.m_checkBox5]

        for i, item in enumerate(practiceCheckBox):
            if item.GetValue():
                self.practiceList.append(practiceName[i])

        self.principleList = []
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
                self.principleList.append(principleName[i])

        self.valueList = []

        valueCheckBox = [self.m_checkBox18, self.m_checkBox19, self.m_checkBox20, self.m_checkBox21]

        valueName = [u"Value:Individuals_and_interactions_over_processes_and_tools",
                     u"Value:Working_software_over_comprehensive_documentation",
                     u"Value:Customer_collaboration_over_contract_negotiation",
                     u"Value:Responding_to_change_over_following_a_plan"]

        for i, item in enumerate(valueCheckBox):
            if item.GetValue():
                self.valueList.append(valueName[i])

        print(self.situationList)
        print(self.practiceList)
        print(self.principleList)
        print(self.valueList)
        self.Hide()  # hide the welcome window
        runQuery = SparqlQueries(self)
        self.result = runQuery.queryAllResult()  # calculate all the result
        new_frame = ResultPage1(self)  # open the page to display result
        new_frame.Show()


class SparqlQueries:
    def __init__(self, parent):
        self.situationList = parent.situationList
        self.practiceList = parent.practiceList
        self.principleList = parent.principleList
        self.valueList = parent.valueList
        # owlready2.JAVA_EXE = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Java\java.exe"
        my_world = World()
        myOnto = my_world.get_ontology("AgileOntology9_4_19.owl").load()  # path to the owl file is given here
        ##        situationList = ["Situation:Experience_in_techonology_knowledge", "Situation:no_agile_experience","Situation:2_years_agile_experience","Situation:Distributed_Team","Situation:User_hardly_available",
        ##                         "Situation:Virtual_communication","Situation:No_domain_knowledge"]
        ##        goalList = ["Goal:Gradual_transfer_of_responsibilities_from_project_manager_to_development_team", "Goal:Enhanced_Project_Visibility"]
        ##        practiceList = ["Practice:Daily_meeting", "Practice:Short_iteration"]

        tmpTeam = myOnto.Team("Tmp_team")
        for i in range(len(self.situationList)):
            if self.situationList[i] != u"Unknown":
                situation = myOnto.Situation(self.situationList[i])
                tmpTeam.Have.append(situation)
        ##        for i in range(len(goalList)):
        ##            goal = myOnto.Goal(goalList[i])
        ##            tmpTeam.Have.append(goal)
        for i in range(len(self.practiceList)):
            practice = myOnto.Practice(self.practiceList[i])
            tmpTeam.Adopt.append(practice)
        print(tmpTeam)
        sync_reasoner(my_world, debug=1, infer_property_values=True,
                      keep_tmp_file=True)  # reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()

    def search(self, practice):
        queryPrefix = u'''PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX agile: <http://www.semanticweb.org/skiv/ontologies/2016/9/untitled-ontology-6#>

            '''
        if practice != None:
            queryList = ['''SELECT DISTINCT ?practice ?instance_x
            WHERE { 
            ?practice rdf:type agile:Practice.
            ?practice agile:Achieve ?instance_x.
            ?instance_x rdf:type agile:Goal.
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
                         ?practice agile:Composed_of ?instance_x.
                         ?instance_x rdf:type agile:Activity.
                         FILTER( regex(str(?practice), "''' + practice + '''"))}
            ''',
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
                                 {?practice rdf:type agile:Practice.
                                 ?practice agile:Harmed_by ?instance_x.
                                 ?instance_x rdf:type agile:Situation.}
                                 UNION
                                 {?practice rdf:type agile:Practice.
                                 ?practice agile:Harmed_by ?instance_x.
                                 ?instance_x rdf:type agile:Activity.}
                                FILTER( regex(str(?practice), "''' + practice + '''"))}
            ''',
                         '''SELECT DISTINCT ?practice ?instance_x
                             WHERE { 
                                 {?practice rdf:type agile:Practice.
                                 ?practice agile:Helped_by ?instance_x.
                                 ?instance_x rdf:type agile:Situation.}
                                 UNION
                                 {?practice rdf:type agile:Practice.
                                 ?practice agile:Helped_by ?instance_x.
                                 ?instance_x rdf:type agile:Activity.}
                                FILTER( regex(str(?practice), "''' + practice + '''"))}
            ''',
                         '''SELECT DISTINCT ?practice ?instance_x
                            WHERE { 
                                 ?practice rdf:type agile:Practice.
                                 ?practice agile:Encounter ?instance_x.
                                 ?instance_x rdf:type agile:Problem.
                                 FILTER( regex(str(?practice), "''' + practice + '''"))}
            ''',
                         '''SELECT DISTINCT ?practice ?instance_x
                            WHERE { 
                                 ?practice rdf:type agile:Practice.
                                 ?practice agile:Require ?instance_x.
                                 ?instance_x rdf:type agile:Artifact.
                                FILTER( regex(str(?practice), "''' + practice + '''"))}
            ''']
        else:
            # questionList = ['What objectives/goals team may achieve by the adopting agile practice?',
            # 'What agile values team may achieve by adopting agile practice?',
            # 'What agile principles team may achieve by adopting agile practice?',
            # 'What are  the harm full part the team?',
            # 'What are the helpful part of the team?',
            # 'What are the problem may be faced by the team?'

            queryList = ['''SELECT DISTINCT ?team ?instance_x
            WHERE { 
            ?team rdf:type agile:Team.
            ?team agile:Achieve ?instance_x.
            ?instance_x rdf:type agile:Goal.
            FILTER( regex(str(?team), "Tmp"))}
            ''',
                         '''SELECT DISTINCT ?team ?instance_x
                         WHERE { 
                         ?team rdf:type agile:Team.
                         ?team agile:Achieve ?instance_x.
                         ?instance_x rdf:type agile:Value.
                         FILTER( regex(str(?team), "Tmp"))}
                         ''',
                         '''SELECT DISTINCT ?team ?instance_x
                         WHERE { 
                         ?team rdf:type agile:Team.
                         ?team agile:Achieve ?instance_x.
                         ?instance_x rdf:type agile:Principle.
                         FILTER( regex(str(?team), "Tmp"))}
                         ''',
                         '''
                         SELECT DISTINCT ?instance_x ?requisite
                                  WHERE {
                                         {?team rdf:type agile:Team.
                                         ?requisite rdf:type agile:Requisite.
                      
                                         ?instance_x agile:Harm ?requisite.
                                         ?team agile:Have ?instance_x.}
             
                                         UNION
                                         {?team rdf:type agile:Team.
                                         ?requisite rdf:type agile:Requisite.
                      
                                         ?instance_x agile:Harm ?requisite.
                                         ?team agile:Perform ?instance_x.}
             
                                         FILTER (regex(str(?team),"Tmp"))
                                         FILTER (regex(str(?requisite),"Requisite"))}
                         ''',
                         '''SELECT DISTINCT ?instance_x ?requisite
                                  WHERE {
                                         {?team rdf:type agile:Team.
                                         ?requisite rdf:type agile:Requisite.
                      
                                         ?instance_x agile:Help ?requisite.
                                         ?team agile:Have ?instance_x.}
             
                                         UNION
                                         {?team rdf:type agile:Team.
                                         ?requisite rdf:type agile:Requisite.
                      
                                         ?instance_x agile:Help ?requisite.
                                         ?team agile:Perform ?instance_x.}
             
                                         FILTER (regex(str(?team),"Tmp"))
                                         FILTER (regex(str(?requisite),"Requisite"))}
                         ''',
                         '''SELECT DISTINCT ?team ?instance_x
                         WHERE { 
                         ?team rdf:type agile:Team.
                         ?team agile:Encounter ?instance_x.
                         ?instance_x rdf:type agile:Problem.
                         FILTER( regex(str(?team), "Tmp"))}
                         ''']

        resultList = []  # list of result for all the queries
        for index in range(len(queryList)):
            wholeQuery = queryPrefix + queryList[index]
            # print(wholeQuery)
            result = self.graph.query(wholeQuery)  # list of result for each query
            # creating json object
            response = []
            for item in result:
                s = str(item['instance_x'].toPython())
                s = re.sub(r'.*#', "", s)
                if s not in response:
                    response.append(s)  # list of result for each query in the text format
            resultList.append(response)  # add list of result for each query to the list

        return resultList

    def queryAllResult(self):
        siutationList = []
        practiceList = ["Daily", "Short", "planning", "retrospective", "review"]
        goalList = []
        allResult = []
        tmp_result = []
        if os.path.exists(u'queryByPractice.pkl'):
            allResult = joblib.load(u'queryByPractice.pkl')
            print("load")
        else:
            for i in range(len(practiceList)):
                tmp_result.append(self.search(practiceList[i]))
            joblib.dump(tmp_result, u'queryByPractice.pkl')
            print("dump")

            allResult = tmp_result
        print(allResult)
        allResult.append(self.search(practice=None))

        return allResult


class ResultPage1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Result", pos=wx.DefaultPosition, size=wx.Size(1050, 676),
                          style=wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.MINIMIZE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)

        self.result = parent.result
        self.situationList = parent.situationList
        self.practiceList = parent.practiceList
        self.principleList = parent.principleList
        self.valueList = parent.valueList

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))
        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, -1),
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)
        practice = "Daily meeting"
        self.preAnswerByPractice = [' Objectives/goals can be achieved by ' + practice + ' are:\n\n',
                                    ' Agile values can be achieved by adopting ' + practice + ' are:\n\n',
                                    ' Agile principles can be achieved by adopting a  ' + practice + ' are:\n\n',
                                    ' Activities part  of  a ' + practice + ' and  need  to  be  performed  by  the team are:\n\n',
                                    ' Requisites to successfully adopt a  ' + practice + ' are\n\n',
                                    ' What can be harmful when adopting a  ' + practice + ' are:\n\n',
                                    ' What can be useful when adopting a  ' + practice + ' are:\n\n',
                                    ' What are the problem faced by ' + practice + ' are:\n\n',
                                    ' What are the artifacts required for a  ' + practice + ' are:\n\n']

        self.questionList = ['What objectives/goals can be achieved by an agile practice?',
                             'What agile values can be achieved by adopting a practice?',
                             'What agile principles can be achieved by adopting a practice?',
                             'What  activities  are  part  of  a  practice  and  need  to  be  performed  by  the team?',
                             'What are the requisites to successfully adopt a practice?',
                             'What can be harmful when adopting a practice?',
                             'What can be useful when adopting a practice?',
                             'What are the problem faced by a practice?',
                             'What are the artifacts required for a practice?']
        self.m_staticText3 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY,
                                           u"This section will answer to the question related to practice",
                                           wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText3.Wrap(-1)
        bSizer7.Add(self.m_staticText3, 0, wx.ALL, 5)
        self.m_staticText3.SetFont(wx.Font(13, 70, 90, wx.BOLD, False, wx.EmptyString))

        self.m_staticText4 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"1. Please select a question",
                                           wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText4.Wrap(-1)
        bSizer7.Add(self.m_staticText4, 0, wx.ALL, 5)
        self.m_staticText4.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))

        self.m_bcomboBox1 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, self.questionList[0], wx.DefaultPosition,
                                        wx.Size(700, -1), style=wx.CB_READONLY, choices=self.questionList)
        bSizer7.Add(self.m_bcomboBox1, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"2. Please  select a practice",
                                           wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText5.Wrap(-1)
        bSizer7.Add(self.m_staticText5, 0, wx.ALL, 5)
        self.m_staticText5.SetFont(wx.Font(12, 70, 90, wx.BOLD, False, wx.EmptyString))

        practiceList = ["Daily meeting", "Short iteration", "Sprint planning", "Sprint retrospective", "Sprint review"]
        self.m_bcomboBox2 = wx.ComboBox(self.m_scrolledWindow1, wx.ID_ANY, practiceList[0], wx.DefaultPosition,
                                        wx.Size(700, -1), choices=practiceList, style=wx.CB_READONLY)
        bSizer7.Add(self.m_bcomboBox2, 0, wx.ALL, 5)

        # self.m_listBox1 = wx.ListBox( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,-1 ), m_listBox1Choices, wx.LB_SINGLE )
        # bSizer7.Add( self.m_listBox1, 0, wx.ALL, 5 )

        self.m_scrolledWindow1.SetSizer(bSizer7)
        self.m_scrolledWindow1.Layout()
        bSizer5.Add(self.m_scrolledWindow1, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 0)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow2 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow2.SetScrollRate(5, 5)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(self.m_scrolledWindow2, 1, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        bSizer8.Add(self.m_staticText9, 0, wx.ALL, 5)

        response = (self.result[0][0])
        s = '\n - '
        s = s.join(response)
        s = s.replace('_', ' ')
        self.m_staticText9.SetLabel(self.preAnswerByPractice[0] + '\n - ' + s)
        self.m_scrolledWindow2.SetSizer(bSizer8)
        self.m_scrolledWindow2.Layout()
        bSizer8.Fit(self.m_scrolledWindow2)
        bSizer6.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer6, 1, wx.EXPAND, 0)

        bSizer20.Add(bSizer1, 12, wx.EXPAND, 0)

        self.m_button0 = wx.Button(self, wx.ID_ANY, u"Back to first input page", wx.Point(-1, -1), wx.DefaultSize, 0)
        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Next result", wx.Point(-1, -1), wx.DefaultSize, 0)

        bSizer2.Add(self.m_button0, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        bSizer2.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        bSizer20.Add(bSizer2, 1, wx.ALL | wx.ALIGN_RIGHT, 0)

        self.SetSizer(bSizer20)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_bcomboBox1.Bind(wx.EVT_COMBOBOX, self.LoadResult)
        self.m_bcomboBox1.Bind(wx.EVT_TEXT, self.LoadResult)
        self.m_bcomboBox2.Bind(wx.EVT_COMBOBOX, self.LoadResult)
        self.m_bcomboBox2.Bind(wx.EVT_TEXT, self.LoadResult)
        self.m_button1.Bind(wx.EVT_BUTTON, self.ShowNextFrame)
        self.m_button0.Bind(wx.EVT_BUTTON, self.ShowFirstInputFrame)

    def __del__(self):
        pass

    def ShowFirstInputFrame(self, event):
        self.Hide()  # hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult(inputList) #calculate all the result
        new_frame = InputPage(self)  # open the page to the input page 2
        new_frame.Show()
        # Virtual event handlers, overide them in your derived class

    def LoadResult(self, event):
        # print("Index of question" + str(self.m_bcomboBox1.GetSelection()))
        # print("Index of practice" + str(self.m_bcomboBox2.GetSelection()))

        practice = self.m_bcomboBox2.GetStringSelection()

        questionIndex = self.m_bcomboBox1.GetSelection()
        practiceIndex = self.m_bcomboBox2.GetSelection()

        self.preAnswerByPractice = [' Objectives/goals can be achieved by ' + practice + ' are:\n\n',
                                    ' Agile values can be achieved by adopting ' + practice + ' are:\n\n',
                                    ' Agile principles can be achieved by adopting a  ' + practice + ' are:\n\n',
                                    ' Activities part  of  a ' + practice + ' and  need  to  be  performed  by  the team are:\n\n',
                                    ' Requisites to successfully adopt a  ' + practice + ' are\n\n',
                                    ' What can be harmful when adopting a  ' + practice + ' are:\n\n',
                                    ' What can be useful when adopting a  ' + practice + ' are:\n\n',
                                    ' What are the problem faced by ' + practice + ' are:\n\n',
                                    ' What are the artifacts required for a  ' + practice + ' are:\n\n']

        if questionIndex < 9:
            response = (self.result[self.m_bcomboBox2.GetSelection()][self.m_bcomboBox1.GetSelection()])
            s = '\n - '
            s = s.join(response)
            s = s.replace('_', ' ')
            self.m_staticText9.SetLabel(self.preAnswerByPractice[questionIndex] + '\n - ' + s)

    def ShowNextFrame(self, event):
        self.Hide()  # hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult() #calculate all the result
        new_frame = ResultPage2(self)  # open the page to display result
        new_frame.Show()


###########################################################################
## Class Resultpage2 for the question related to Team
###########################################################################
class ResultPage2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Result", pos=wx.DefaultPosition, size=wx.Size(1050, 676),
                          style=wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.MINIMIZE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)

        self.result = parent.result
        self.situationList = parent.situationList
        self.practiceList = parent.practiceList
        self.principleList = parent.principleList
        self.valueList = parent.valueList

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))
        bSizer20 = wx.BoxSizer(wx.VERTICAL)
        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, -1),
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.questionList = ['What objectives/goals team may achieve by the adopting agile practice?',
                             'What agile values team may achieve by adopting agile practice?',
                             'What agile principles team may achieve by adopting agile practice?',
                             'What are  the harm full part the team?',
                             'What are the helpful part of the team?',
                             'What are the problem may be faced by the team?']
        self.prepreAnswerByTeam = [
            ' Objectives/goals team may achieve are: \n\n',
            ' Agile values team may achieve are: \n\n',
            ' Agile principles team may achieve are: \n',
            ' The harmful part of the team when adopting agile practice are:\n\n',
            ' The useful part of the team when adopting agile practice are:\n\n',
            ' The problem the team may encounter are:\n\n', ]

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

        ##                self.m_staticText5 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"2. Please  select a practice", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )
        ##                self.m_staticText5.Wrap( -1 )
        ##                bSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )
        ##
        ##                practiceList = ["Daily meeting", "Short iteration","Sprint planning",  "Sprint retrospective", "Sprint review"]
        ##                self.m_bcomboBox2 = wx.ComboBox( self.m_scrolledWindow1, wx.ID_ANY, practiceList[0], wx.DefaultPosition, wx.Size( 700,-1 ), choices=practiceList,style = wx.CB_READONLY  )
        ##                bSizer7.Add( self.m_bcomboBox2, 0, wx.ALL, 5 )

        # self.m_listBox1 = wx.ListBox( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,-1 ), m_listBox1Choices, wx.LB_SINGLE )
        # bSizer7.Add( self.m_listBox1, 0, wx.ALL, 5 )

        self.m_scrolledWindow1.SetSizer(bSizer7)
        self.m_scrolledWindow1.Layout()
        bSizer5.Add(self.m_scrolledWindow1, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 0)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow2 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow2.SetScrollRate(5, 5)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(self.m_scrolledWindow2, 1, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        bSizer8.Add(self.m_staticText9, 0, wx.ALL, 5)
        response = self.result[5][0]
        s = '\n - '
        s = s.join(response)
        s = s.replace('_', ' ')
        self.m_staticText9.SetLabel(self.prepreAnswerByTeam[0] + '\n - ' + s)

        self.m_scrolledWindow2.SetSizer(bSizer8)
        self.m_scrolledWindow2.Layout()
        bSizer8.Fit(self.m_scrolledWindow2)
        bSizer6.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer6, 1, wx.EXPAND, 0)
        bSizer20.Add(bSizer1, 12, wx.EXPAND, 0)

        self.m_button0 = wx.Button(self, wx.ID_ANY, u"Back to first input page", wx.Point(-1, -1), wx.DefaultSize, 0)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Previous result", wx.Point(-1, -1), wx.DefaultSize, 0)
        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Next result", wx.Point(-1, -1), wx.DefaultSize, 0)

        bSizer2.Add(self.m_button0, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        bSizer2.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        bSizer2.Add(self.m_button2, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        bSizer20.Add(bSizer2, 1, wx.ALL | wx.ALIGN_RIGHT, 0)

        self.SetSizer(bSizer20)

        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_bcomboBox1.Bind(wx.EVT_COMBOBOX, self.LoadResult)
        self.m_bcomboBox1.Bind(wx.EVT_TEXT, self.LoadResult)
        self.m_button1.Bind(wx.EVT_BUTTON, self.BackToFirstResult)
        self.m_button0.Bind(wx.EVT_BUTTON, self.ShowFirstInputFrame)
        self.m_button2.Bind(wx.EVT_BUTTON, self.ShowNextFrame)
        # self.m_bcomboBox2.Bind( wx.EVT_COMBOBOX, self.LoadResult )
        # self.m_bcomboBox2.Bind( wx.EVT_TEXT, self.LoadResult )

    def __del__(self):
        pass

    def ShowNextFrame(self, event):
        self.Hide()  # hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult() #calculate all the result
        new_frame = ResultPage3(self)  # open the page to display result
        new_frame.Show()

    def ShowFirstInputFrame(self, event):
        self.Hide()  # hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult(inputList) #calculate all the result
        new_frame = InputPage(self)  # open the page to the input page 2
        new_frame.Show()

    # Virtual event handlers, overide them in your derived class
    def LoadResult(self, event):
        # print("Index of question" + str(self.m_bcomboBox1.GetSelection()))
        # print("Index of practice" + str(self.m_bcomboBox2.GetSelection()))

        # practice = self.m_bcomboBox2.GetStringSelection()

        questionIndex = self.m_bcomboBox1.GetSelection()

        response = self.result[5][questionIndex]
        s = '\n - '
        s = s.join(response)
        s = s.replace('_', ' ')
        self.m_staticText9.SetLabel(self.prepreAnswerByTeam[questionIndex] + '\n - ' + s)

    def BackToFirstResult(self, event):
        self.Hide()  # hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult() #calculate all the result
        new_frame = ResultPage1(self)  # open the page to display result
        new_frame.Show()


###########################################################################
## Class Resultpage3 for the answers of the question in the list control format
###########################################################################
class ResultPage3(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Result", pos=wx.DefaultPosition, size=wx.Size(1050, 676),
                          style=wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.MINIMIZE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)

        self.result = parent.result
        self.situationList = parent.situationList
        self.practiceList = parent.practiceList
        self.principleList = parent.principleList
        self.valueList = parent.valueList

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))
        bSizer20 = wx.BoxSizer(wx.VERTICAL)
        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, -1),
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.questionList = ['What objectives/goals team may achieve by the adopting agile practice?',
                             'What agile values team may achieve by adopting agile practice?',
                             'What agile principles team may achieve by adopting agile practice?',
                             'What are  the harm full part the team?',
                             'What are the helpful part of the team?',
                             'What are the problem may be faced by the team?']
        self.prepreAnswerByTeam = [
            ' Objectives/goals team may achieve are: \n\n',
            ' Agile values team may achieve are: \n\n',
            ' Agile principles team may achieve are: \n',
            ' The harmful part of the team when adopting agile practice are:\n\n',
            ' The useful part of the team when adopting agile practice are:\n\n',
            ' The problem the team may encounter are:\n\n', ]

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
                                        wx.Size(500, -1), style=wx.CB_READONLY, choices=self.questionList)
        bSizer7.Add(self.m_bcomboBox1, 0, wx.ALL, 5)

        ##                self.m_staticText5 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"2. Please  select a practice", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )
        ##                self.m_staticText5.Wrap( -1 )
        ##                bSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )
        ##
        ##                practiceList = ["Daily meeting", "Short iteration","Sprint planning",  "Sprint retrospective", "Sprint review"]
        ##                self.m_bcomboBox2 = wx.ComboBox( self.m_scrolledWindow1, wx.ID_ANY, practiceList[0], wx.DefaultPosition, wx.Size( 700,-1 ), choices=practiceList,style = wx.CB_READONLY  )
        ##                bSizer7.Add( self.m_bcomboBox2, 0, wx.ALL, 5 )

        # self.m_listBox1 = wx.ListBox( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,-1 ), m_listBox1Choices, wx.LB_SINGLE )
        # bSizer7.Add( self.m_listBox1, 0, wx.ALL, 5 )

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

        self.list = wx.ListCtrl(self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size(900, 600),
                                style=wx.LC_REPORT | wx.LC_ALIGN_LEFT)

        bSizer8.Add(self.list, 0, wx.ALL, 5)

        self.m_scrolledWindow2.SetSizer(bSizer8)
        self.m_scrolledWindow2.Layout()
        bSizer8.Fit(self.m_scrolledWindow2)
        bSizer6.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer6, 3, wx.EXPAND, 0)
        bSizer20.Add(bSizer1, 13, wx.EXPAND, 0)

        self.m_button0 = wx.Button(self, wx.ID_ANY, u"Back to first input page", wx.Point(-1, -1), wx.DefaultSize, 0)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Previous result", wx.Point(-1, -1), wx.DefaultSize, 0)

        bSizer2.Add(self.m_button0, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        bSizer2.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        bSizer20.Add(bSizer2, 1, wx.ALL | wx.ALIGN_RIGHT, 0)

        self.SetSizer(bSizer20)

        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_bcomboBox1.Bind(wx.EVT_COMBOBOX, self.LoadResult)
        # self.m_bcomboBox1.Bind( wx.EVT_TEXT, self.LoadResult )
        self.m_button1.Bind(wx.EVT_BUTTON, self.BackToFirstResult)
        self.m_button0.Bind(wx.EVT_BUTTON, self.ShowFirstInputFrame)
        # self.m_bcomboBox2.Bind( wx.EVT_COMBOBOX, self.LoadResult )
        # self.m_bcomboBox2.Bind( wx.EVT_TEXT, self.LoadResult )

    def __del__(self):
        pass

    def ShowFirstInputFrame(self, event):
        self.Hide()  # hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult(inputList) #calculate all the result
        new_frame = InputPage(self)  # open the page to the input page 2
        new_frame.Show()

    # Virtual event handlers, overide them in your derived class
    def LoadResult(self, event):
        self.list.ClearAll()
        questionIndex = self.m_bcomboBox1.GetSelection()
        self.questionList = ['What objectives/goals team may achieve by the adopting agile practice?',
                             'What agile values team may achieve by adopting agile practice?',
                             'What agile principles team may achieve by adopting agile practice?',
                             'What are  the harm full part the team?',
                             'What are the helpful part of the team?',
                             'What are the problem may be faced by the team?']

        column0 = ['Practice', 'Practice', 'Practice', 'Situation', 'Situation', 'Practice']
        column1 = ['Goal', 'Value', 'Principle', 'Practice', 'Practice', 'Problem']
        self.list.InsertColumn(0, column0[questionIndex], wx.LIST_FORMAT_LEFT, width=300)
        self.list.InsertColumn(1, column1[questionIndex], wx.LIST_FORMAT_LEFT, width=600)

        if questionIndex == 0 or questionIndex == 1 or questionIndex == 2 or questionIndex == 5:

            practiceName = [u"Practice:Daily_meeting", u"Practice:Short_iteration", u"Practice:Sprint_planning",
                            u"Practice:Sprint_review", u"Practice:Sprint_retrospective"]
            itemIndex = 0
            for index, practice in enumerate(practiceName):
                if practice in self.practiceList:

                    practice = practice.replace("_", " ")
                    practice = practice.replace("Practice:", "")

                    itemIndex = self.list.InsertItem(itemIndex, practice)
                    print(itemIndex, practice)
                    self.list.SetItem(itemIndex, 1, self.result[index][questionIndex][0].replace("_", " ")[
                                                    len(column1[questionIndex]) + 1:])
                    for i in range(len(self.result[index][questionIndex]) - 1):
                        itemIndex += i + 1
                        itemIndex = self.list.InsertItem(itemIndex, "")
                        print(itemIndex, self.result[index][questionIndex][i + 1])
                        self.list.SetItem(itemIndex, 1, self.result[index][questionIndex][i + 1].replace("_", " ")[
                                                        len(column1[questionIndex]) + 1:])
                    itemIndex += 1
                    itemIndex = self.list.InsertItem(itemIndex, "")
                    self.list.SetItem(itemIndex, 1, "")
                    itemIndex += 1

    ##            response = self.result[5][questionIndex]
    ##            s = '\n - '
    ##            s = s.join(response)
    ##            s = s.replace('_', ' ')
    ##            self.m_staticText9.SetLabel(self.prepreAnswerByTeam[questionIndex] + '\n - '+ s)
    def BackToFirstResult(self, event):
        self.Hide()  # hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult() #calculate all the result
        new_frame = ResultPage1(self)  # open the page to display result
        new_frame.Show()


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
        self.frame.Hide()  # hide the welcome window
        # runQuery = SparqlQueries()
        # self.result =  runQuery.queryAllResult() #calculate all the result
        new_frame = InputPage(self)  # open the page to display result
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
