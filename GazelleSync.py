 #!/usr/bin/env Python3
import PySimpleGUI as sg
import os
sg.ChangeLookAndFeel('Dark')

layout = [

    [sg.Text('GazelleSync 5.0.2', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('(Note: You should edit constants.py first, to include usernames and passwords of all relevant trackers)', font=("Helvetica", 8))],
    [sg.Text('(Note: This .py should be in the same directory as the other .py files)', font=("Helvetica", 8))],
    [sg.Text('From: ', font=("Helvetica", 15)), sg.InputCombo(('OPS', 'RED', 'SOWS', 'DIC'),key='_from_', default_value='none', background_color="#004F00"), sg.Text('To :', font=("Helvetica", 15)), sg.InputCombo(('OPS', 'RED', 'SOWS', 'DIC'),key='_to_', default_value='none', background_color="#004F00")],
	[sg.Text('1) Fetch the torrent info from source tracker :', font=("Helvetica", 20))],
	[sg.Text('Method A - using Source Tracker permalink', font=("Helvetica", 15))],
    [sg.InputText(key='_permalink_')],
    [sg.Text('The Source Tracker Permalink can be either of these two forms:', font=("Helvetica", 8))],
    [sg.Text('https://source.tracker/torrents.php?id=1&torrentid=1#torrent1', font=("Helvetica", 8))],
    [sg.Text('https://source.tracker/torrents.php?id=1&torrentid=1', font=("Helvetica", 8))],
	[sg.Text('Method B - using Source Tracker .torrent file', font=("Helvetica", 15))],
    [sg.Text('Choose a .torrent file', size=(15, 1), auto_size_text=False, justification='right'),
     sg.InputText(key='_torrentFile_'), sg.FileBrowse(file_types=(("ALL Files", ".torrent"),))],
	[sg.Text('Method C - using a folder of torrents', font=("Helvetica", 15))],
    [sg.Text('Choose a folder', size=(15, 1), auto_size_text=False, justification='right'),
     sg.InputText(key='_torrentFolder_'), sg.FolderBrowse()],
	[sg.Text('2) Select the Music Folder(s)', font=("Helvetica", 20))],
    [sg.InputCombo(('Single Mode', 'Bash Mode'), size=(20, 1), key='_singleOrBash_', background_color="#004F00"),
	sg.InputText(key='_musicFolder_'), sg.FolderBrowse()],
    [sg.Text('Single Mode : Please browse to the directory that contains the actual music files', font=("Helvetica", 8))],
    [sg.Text('Bash Mode : Please browse to the directory ABOVE your music directory (or directories)!', font=("Helvetica", 8))],
    [sg.Text('_'  * 80)],
    [sg.Submit(button_text='Go! Go! Go! (Let\'s rip)', key='_goGo_'), sg.Exit(button_text='Exit')]
]


window = sg.Window('Gazelle -> Gazelle (5.0)', layout, default_element_size=(40, 1), grab_anywhere=False, icon="favicon.ico")

event, values = window.Read()

while True:
    event, values = window.Read()
    callMovePy = ''
    if event == '_goGo_':
        callMovePy = 'python move.py from=' + values['_from_'] + ' to=' + values['_to_']
        if len(values['_permalink_']) > 0 :
            callMovePy += ' link="' + values['_permalink_'] + '"'
        elif len(values['_torrentFile_']) > 0:
            callMovePy += ' tpath="' + values['_torrentFile_'] + '"'
        elif len(values['_torrentFolder_']) >0:
            callMovePy += ' tfolder="' + values['_torrentFolder_'] + '"'

        if values['_singleOrBash_'] == 'Single Mode' :
            callMovePy += ' album="' + values['_musicFolder_'] + '"'
        elif values['_singleOrBash_'] == 'Bash Mode' :
            callMovePy += ' folder="' + values['_musicFolder_'] + '"'
        os.system(callMovePy)
    elif event is None or event == 'Exit':
        break
window.Close()


'''
    if event == '_goGo_':
        callMovePy = 'python move.py from=%(from) to=%(to)'
        if len(values['_permalink_']) > 0 :
            callMovePy += ' link="%(permalink)"'
        elif len(values['_torrentFile_']) > 0:
            callMovePy += ' tpath="%(torrentFile)"'
        elif len(values['_torrentFolder_']) >0:
            callMovePy += ' tpath="%(torrentFolder)"'


        callMovePy = callMovePy + ' album="' + values['_musicFolder_'] + "\""
        os.system(callMovePy % {'from' : values['_from_'],
                                'to': values['_to_'],
                                'permalink': values['_permalink_'],
                                'torrentFile': values['_torrentFile_'],
                                'torrentFolder': values['_torrentFolder_']})
'''

'''
    if event == '_goGo_':
        callMovePy = 'python move.py from=' + values['_from_'] + ' to=' + values['_to_']
        if len(values['_permalink_']) > 0 :
            callMovePy += ' link="' + values['_permalink_'] + '"'
        elif len(values['_torrentFile_']) > 0:
            callMovePy += ' tpath="' + values['_torrentFile_'] + '"'
        elif len(values['_torrentFolder_']) >0:
            callMovePy += ' tfolder="' + values['_torrentFolder_'] + '"'

        callMovePy = callMovePy + ' album="' + values['_musicFolder_'] + '"'
        os.system(callMovePy)
'''
