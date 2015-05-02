This python script allows you to render a webpage on your server and manipulate and
extract the rendered html. The manipulation is done with
javascript in the browser using the pyQt Webkit Api.

The difference from a normal html scraper is that javascript and css also is
rendered.

This allows you to:
  * Render a webpage on a server with the very high quality Webkit engine.
  * Manipulate the page using client-type javascript (jQuery, etc.).
  * Extract the information/HTML you need from the page using javascript.

The script is very short so it is good platform for creating your own variant.

### Browse the source ###
http://code.google.com/p/py-webkit-html-manipulator/source/browse/#svn/trunk

### Read the README ###
http://code.google.com/p/py-webkit-html-manipulator/source/browse/trunk/README

### Get the files ###
```
svn checkout http://py-webkit-html-manipulator.googlecode.com/svn/trunk/ py-webkit-html-manipulator-read-only
```

### Requirements ###
  * Python
  * PyQT
  * xvfb for running it headless under linux.

### Questions? ###
Contact me at rumi.kg@gmail.com.

### Want to contribute code? ###
Cool! Write me.

### Acknowledgments ###
  * Thx to unlotto for helping me hook up the signals from pyQt.
  * Found good ideas here: http://www.holovaty.com/writing/headless-html-rendering-engine/
  * I found the headless penguin logo at http://www.flickr.com/photos/chadica/2069750969/ where its released under the Creative Commons license.