# -*- coding: utf-8 -*-

import wx
import wx.wizard as wiz


class Page(wiz.WizardPageSimple):
    """This is the class for a page inside the Wizard.
        It needs a title in order to work"""
    def __init__(self, parent, title):
        wiz.WizardPageSimple.__init__(self, parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        title = wx.StaticText(self, -1, title)
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(title, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND|wx.ALL, 5)


def main():
    wizard = wx.wizard.Wizard(None, -1, "Wizard Example")
    page1 = Page(wizard, "Hola")
    page2 = Page(wizard, "Que tal?")
    page3 = Page(wizard, "Adios!")

    wx.wizard.WizardPageSimple.Chain(page1, page2)
    wx.wizard.WizardPageSimple.Chain(page2, page3)


    wizard.FitToPage(page1)
    wizard.RunWizard(page1)

    wizard.Destroy()

if __name__ == "__main__":
    app = wx.App()
    main()
    app.MainLoop()
