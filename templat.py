from nicegui import ui

def temp():
    with ui.header().classes(replace='row items-center') as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')

    with ui.left_drawer().classes('bg-blue-100') as left_drawer:
        ui.label('Side menu')
        ui.button('Home', on_click=lambda: ui.navigate.to('/'))
        ui.button('Page 1', on_click=lambda: ui.navigate.to('/page-1'))
        ui.button('Page 2', on_click=lambda: ui.navigate.to('/page-2'))