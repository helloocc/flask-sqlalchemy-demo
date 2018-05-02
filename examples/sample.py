#!/usr/bin/env python
#-*- coding=utf8 -*-
from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
app = Flask(__name__)
Bootstrap(app)
nav=Nav()
nav.register_element('top',Navbar(u'411-check-in',
                                    View(u'openstack','home'),
                                    View(u'cps','about'),
                                    Subgroup(u'项目',
                                             View(u'项目一','about'),
                                             Separator(),
                                             View(u'项目二', 'cps'),
                                    ),
))

nav.init_app(app)
@app.route('/')
def home():
    return render_template('home.html',title_name = 'welcome')

@app.route('/cps')
def cps():
    #  return 'cps'
    return render_template('cps.html',title_name = 'welcome')

@app.route('/about')
def about():
    return 'about'

@app.template_test('current_link')
def is_current_link(link):
    return link == request.path

if __name__ == '__main__':
    app.run(debug=True)
