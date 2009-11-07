#!/usr/bin/env python
import sys
from time import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from optparse import OptionParser

"""
The Webkit Html Manipulator. 
See README for instructions.
Author: Rune Kaagaard <rumi.kg@gmail.com>.
"""
class WebkitHtmlManipulator():
  # Set class properties and runs methods.
  def __init__(self, options):
    self.app = QApplication([])
    self.view = QWebView()
    self.page = self.view.page()
    self.frame = self.page.mainFrame()
    self.options = options
    self.connectSignals()
    self.loadPage()
  
  # Signal when the view has finished loading.
  def connectSignals(self):
    QObject.connect(self.view, SIGNAL("loadFinished(bool)"), self.parsePage)
  
  # Loads the page, and takes care of not exiting too soon.
  def loadPage(self):
    self.view.load(QUrl(self.options.url));
    self.view.show()
    sys.exit(self.app.exec_())
  
  # Returns the html for the page or the string set by the javascript file.
  def parsePage(self):
    if self.options.jsFile==False: 
      print unicode(self.frame.toHtml())
    else:
      result = QObject()
      result.setObjectName("WebkitHtmlManipulator")
      result.setProperty("result",QVariant(""))
      self.frame.addToJavaScriptWindowObject("WebkitHtmlManipulator", result) 
      self.frame.evaluateJavaScript(self.getFileContent(self.options.jsFile))
      print unicode(result.property("result").toString())
    # Close the app when we are done.
    self.app.quit()
  
  # Returns all content of a file
  def getFileContent(self, filepath):
      f = open(filepath, 'r')
      m,v = f.read(),f.close()
      return m

# Parse options.
parser = OptionParser()
parser.add_option("-u", "--url", dest="url",
                  help="The url to parse.", default='http://example.com')
parser.add_option("-j", "--js-file",
                  dest="jsFile", help="The javascript file to manipulate the html. Must set the WebkitHtmlManipulator.result variable in the global scope.",
                  default=False
                  )
(options, args) = parser.parse_args()

# Run.
WebkitHtmlManipulator(options)
