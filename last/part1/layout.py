#!/usr/bin/env python3
from nicegui import ui
from part.templat import temp

@ui.page('/')
def homepage():
    temp()
    with ui.card().classes('w-[500px]'):
        with ui.column().classes('border border-red-400 w-full h-full'):
            ui.input(label='account').classes('w-full')
            ui.input(label='password').classes('w-full')
            ui.input(label='e-mail').classes('w-full')
            ui.input(label='address').classes('w-full')
        with ui.row().classes('border border-blue-400 w-full h-full'):
            ui.button('add').on_click(lambda: ui.info('Form submitted!'))
            ui.button('edit').on_click(lambda: ui.info('Form edit!'))
            ui.space().classes('flex-grow')
            ui.button('clear').on_click(lambda: ui.info('Form clear!'))
        with ui.grid(columns='100px 100px auto auto').classes('border border-green-400 w-full h-full'):
            ui.label('account')
            ui.label('password')
            ui.label('e-mail')
            ui.label('address')
        
@ui.page('/page-1')
def page1():
    temp()
    ui.label('This is page 1')
    with ui.grid(columns=2):
        ui.button('Button 1')
        ui.button('Button 2')
        ui.button('Button 3')
        ui.button('Button 4')
    
@ui.page('/page-2')
def page2():
    temp()
    ui.label('This is page 2')

ui.run()