# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2

form = """
<!DOCTYPE html>
<form method="post">
    <label>
        One
        <input type="radio" name="q" value="one">
    </label>
    <labe>
        Two
        <input type="radio" name="q" value="two">
    </labe>
    <label>
        Three
        <input type="radio" name="q" value="three">
    </label>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)

    def post(self):
        q = self.request.get("q")
        self.redirect("/thanks?q=%s" % q)

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("Thanks for your time %s" % self.request.get("q"))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ("/thanks", ThanksHandler)
], debug=True)
