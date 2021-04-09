 #!/usr/bin/env Python3      
import PySimpleGUI as sg      
import os
sg.ChangeLookAndFeel('DarkBlue')      

   

      

layout = [      
          
    [sg.Text('GazelleSync 5.0.2 - DIC Variant', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],         
    [sg.Text('(注意：首先，你需要编辑 constants.py，在其中添加所有相关站点的用户名和密码。)', font=("Microsoft YaHei", 10))],
    [sg.Text('(注意：本 .py 文件应与其他 .py 文件处于同一目录下。)', font=("Microsoft YaHei", 10))],
    [sg.Text('从：', font=("Microsoft YaHei", 13)), sg.InputCombo(('OPS', 'RED', 'NWCD', 'DIC'),key='_from_', default_value='none'), sg.Text('到：', font=("Microsoft YaHei", 13)), sg.InputCombo(('OPS', 'RED', 'NWCD', 'DIC'),key='_to_', default_value='none')],
	[sg.Text('1) 从来源站点获取种子信息：', font=("Microsoft YaHei", 16))],
	[sg.Text('方法一：使用来源站点的种子永久链接（PL）', font=("Microsoft YaHei", 13))],
    [sg.InputText(key='_permalink_')],
    [sg.Text('来源站点的种子永久链接可能存在以下两种形式：', font=("Microsoft YaHei", 10))], 
    [sg.Text('https://source.tracker/torrents.php?id=1&torrentid=1#torrent1', font=("Helvetica", 10))], 
    [sg.Text('https://source.tracker/torrents.php?id=1&torrentid=1', font=("Helvetica", 10))],
	[sg.Text('方法二：使用来源站点的种子文件', font=("Microsoft YaHei", 13))],     
    [sg.Text('指定种子文件目录：', size=(15, 1), auto_size_text=False, justification='right', font=("Microsoft YaHei", 10)),      
     sg.InputText(key='_torrentFile_'), sg.FileBrowse(file_types=(("ALL Files", ".torrent"),))],
	[sg.Text('方法三：使用一个包含种子文件的文件夹', font=("Microsoft YaHei", 13))], 
    [sg.Text('指定文件夹目录：', size=(15, 1), auto_size_text=False, justification='right', font=("Microsoft YaHei", 10)),      
     sg.InputText(key='_torrentFolder_'), sg.FolderBrowse()],
	[sg.Text('2) 指定音乐文件夹', font=("Microsoft YaHei", 16))],
    [sg.InputCombo(('单种模式', '批量模式'), size=(20, 1), key='_singleOrBash_', font=("Microsoft YaHei", 10)),
	sg.InputText(key='_musicFolder_'), sg.FolderBrowse()],
    [sg.Text('单种模式：请指定直接包含音乐文件的目录。', font=("Microsoft YaHei", 10))], 
    [sg.Text('批量模式：请指定直接包含音乐文件目录的上层目录。', font=("Microsoft YaHei", 10))], 
    [sg.Text('_'  * 80)],        
    [sg.Submit(button_text='运行', key='_goGo_'), sg.Exit(button_text='退出', key='_exit_')]
]      


window = sg.Window('Gazelle -> Gazelle (5.0)', layout, default_element_size=(40, 1), grab_anywhere=False, icon="favicon2.ico")      

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

        if values['_singleOrBash_'] == '单种模式' :
            callMovePy += ' album="' + values['_musicFolder_'] + '"'
        elif values['_singleOrBash_'] == '批量模式' :
            callMovePy += ' folder="' + values['_musicFolder_'] + '"'
        os.system(callMovePy)
    elif event is None or event == '_exit_':
        break
window.Close()