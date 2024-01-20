from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
import os
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.label import Label
import socket
from kivymd.toast import toast
toast("By KareKaren\nSpecial thanks to liuviy\nUSR -  UDP SENDER RECIEVER\nДля копирования нажмите на текст.\nТекст можно скролить вниз/вверх.\nКаждые ваши действия можно посмотреть в логах.\nПуть к логам: /0/USRDATA/USR.txt")
from kivy.core.clipboard import Clipboard

try:
	new_dir =r'USRDATA'
	parent_dir = '/storage/emulated/0'
	path = os.path.join(parent_dir, new_dir)
	os.mkdir(path)
except FileExistsError:
	pass
	
class CopyLabel(Label):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            Clipboard.copy(self.text.replace("[b]", "").replace("[color=FF0905]", "").replace("[color=0511FF]", "").replace("[color=FFFFFF]", "").replace("[color=00FF00]", "").replace("[color=0F00FF]", ""))
            toast("Скопировано в буфер обмена.")

kv = '''<MainWidget>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'USR.png'
    boxl: box
    BoxLayout:
        orientation: 'vertical'
        id: box
        box: box1
        box0: box2
        BoxLayout:
            id: box1
            reci: reci
            size_hint_y: None
            height: 50
            
            TextInput:
                id: name
                multiline: True
                size_hint: (.9, None)
                height: 50
                font_size: 40
                hint_text: "                    Айпи "
            
            TextInput:
                id: namee
                multiline: True
                size_hint: (.9, None)
                height: 50
                font_size: 40
                hint_text: "                    Порт "
                
            
                
        BoxLayout:
            orientation: 'vertical'
            id: box2
            namee: namee
            name: name
            nameee: nameee
            
            TextInput:
                id: nameee
                multiline: True
                size_hint: (.9, None)
                height: 50
                font_size: 40
                pos_hint:{"center_x":0.5}
                hint_text: "                                         Запрос "
            
            ScrollView:
                do_scroll_x: True
                do_scroll_y: True
                
                CopyLabel:
                    size_hint: (1, None)
                    #size_hint_y: None
                    height: self.texture_size[1]
                    #text_size: self.width, None
                    text_size: self.width, None
                    width: self.texture_size[0] + 20  # Добавляем отступы по ширине текста
                    halign: 'center'  # Центрирование текста по горизонтали
                    #padding: 10  # Отступы по ширине текста
    
                    id: reci
                    markup: True
                    font_size: 37
                    text: '[b][color=0F00FF]Recieved[color=FFFFFF]:[b]'
                    #size_hint_x: None
                    #width: 100
                    #pos_hint:{"center_x": 1,"center_y":1}
                
            Button:
                markup: True
                font_size: 70
                text: '[b][color=FF0905]SEND[b]'
                size_hint: (.9, None)
                pos_hint:{"center_x":0.5}
                on_press: root.say_reci()
                
            Button:
                markup: True
                font_size: 70
                text: '[b][color=0FFF01]Очистить логи[b]'
                size_hint: (.9, None)
                pos_hint:{"center_x":0.5}
                on_press: root.log_clr()
                '''
class MainWidget(BoxLayout):
    data_output = ObjectProperty()
    data_input = ObjectProperty()
    boxl = ObjectProperty()
    namee = ObjectProperty()
    name = ObjectProperty()
    def client(self, data): pass
    
    def say_reci(self):
          if self.boxl.box0.namee.text == '':
              self.boxl.box0.namee.text = '19132'
          if self.boxl.box0.name.text == '':
              self.boxl.box0.name.text = '0.0.0.0'
          if self.boxl.box0.nameee.text == '':
              self.boxl.box0.nameee.text = 'ls'
          if self.boxl.box0.name.text == 'latecraft.ru':
              toast("latecraft самый крутой сервер")
          if self.boxl.box0.name.text == 'play.24mine.ru':
             toast("я думаю не стоит отправлять запросы на эту парашу")
          udp_nigger = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          udp_nigger.settimeout(1.5)
          myfilee = open("/storage/emulated/0/USRDATA/USR.txt", "a+")
          myfilee.write("[CONNECT] Подключение к " + self.boxl.box0.name.text + ":" + self.boxl.box0.namee.text +", запрос: " + self.boxl.box0.nameee.text + "\n-")
          myfilee.close()
          try:
              udp_nigger.connect((self.boxl.box0.name.text,int(self.boxl.box0.namee.text)))
              udp_nigger.send((self.boxl.box0.nameee.text).encode())
              data = udp_nigger.recv(9999).decode("utf-8",errors="ignore")
              
              self.boxl.box.reci.text = '[b][color=0511FF]\n\nRecieved[color=FFFFFF]:[color=00FF00] \n\n' + data + "[b]"
              myfileee = open("/storage/emulated/0/USRDATA/USR.txt", "a+")
              
              
              myfileee.write("[RESPONSE] Ответ:\n--------\n" + data + "\n")
              myfileee.close()
          except:
              self.boxl.box.reci.text = '[b][color=FF0905]Ошибка подключения![b]\n'
              myfile = open("/storage/emulated/0/USRDATA/USR.txt", "a+")
              myfile.write("[ERR] Ошибка подключения к " + self.boxl.box0.name.text + ":" + self.boxl.box0.namee.text + ", отправляемый запрос: " + self.boxl.box0.nameee.text + "\n\n")
              myfile.close()
              
    def log_clr(self):
    	              toast("Логи успешно сброшены!")
    	              clr = open("/storage/emulated/0/USRDATA/USR.txt", "w+")
    	              clr.write("Логи успешно сброшены!\n\n")
    	              clr.close()
    	              
class MainApp(MDApp):
    def build(self):
        Builder.load_string(kv)
        
        return MainWidget()


if __name__ == '__main__':
    app = MainApp()
    app.run()