# OrgModeDisplay
Convert Org mode files to html.

# The tools
* [Flask](http://flask.pocoo.org/) to serve the html document.
* [orgparse](https://github.com/tkf/orgparse) to read the org mode files.
* [watchdog](https://pythonhosted.org/watchdog/) to monitor any changes made to the org mode files.
  * may be required or not, we will see.

# Installation

Step 1, install [Python 3](http://python.org).

```
  pip install flask
  pip install orgparse
  pip install watchdog
```
