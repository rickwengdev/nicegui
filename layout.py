#!/usr/bin/env python3
from nicegui import ui
from templat import temp

@ui.page('/')
def homepage():
    temp()
    ui.label('Welcome to the homepage')
    with ui.column().classes('null'):
        ui.button('Page 1')
        ui.button('Page 2')

@ui.page('/page-1')
def page1():
    temp()
    ui.label('This is page 1')
    
@ui.page('/page-2')
def page2():
    temp()
    ui.label('This is page 2')

ui.run()