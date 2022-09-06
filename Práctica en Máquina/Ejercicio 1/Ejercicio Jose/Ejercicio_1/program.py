import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

def readBytes(filename):
    header = []
    with open(filename,'rb') as file:
        
        bytes = []
        for offset in range(0,4): bytes.append(int.from_bytes(file.read(1), byteorder='big'))
        header.append(['big','0','4','ChunkID',''.join(map(chr,bytes))])
        
        header.append(['little','4','4','ChunkSize', int.from_bytes(file.read(4), byteorder='little')])

        bytes = []
        for offset in range(0,4): bytes.append(int.from_bytes(file.read(1), byteorder='big'))
        header.append(['big','8','4','Format',''.join(map(chr,bytes))])
    
        bytes = []
        for offset in range(0,4): bytes.append(int.from_bytes(file.read(1), byteorder='big'))
        header.append(['big','12','4','Subchunk1ID',''.join(map(chr,bytes))])

        header.append(['little','16','4','Subchunk1Size', str(int.from_bytes(file.read(4), byteorder='little'))])

        header.append(['little','20','2','AudioFormat', str(int.from_bytes(file.read(2), byteorder='little'))])

        header.append(['little','22','2','NumChannels', str(int.from_bytes(file.read(2), byteorder='little'))])

        header.append(['little','24','4','SampleRate', str(int.from_bytes(file.read(4), byteorder='little'))])

        header.append(['little','28','4','ByteRate', str(int.from_bytes(file.read(4), byteorder='little'))])

        header.append(['little','32','2','BlockAlign', str(int.from_bytes(file.read(2), byteorder='little'))])

        header.append(['little','34','2','BitsPerSample', str(int.from_bytes(file.read(2), byteorder='little'))])
    
    return header

def abrirArchivo(tv:ttk.Treeview, tipo_wav:Label):
    archivo = filedialog.askopenfilename(title='abrir', initialdir=os.getcwd(), filetypes=[("Archivos WAV","*.wav"),("Todos los Archivos", "*.*")])
    header = readBytes(archivo)

    #-- Vacio la tabla
    for c in tv.get_children():tv.delete(c)

    if(header[0][4]=="RIFF"):
        print(' ** El archivo es de tipo wav **')
        tipo_wav.config(text='** El archivo es tipo wav **', fg='green')
        print(' >> Wav header <<')
        for h in header:
            print(f'> {h[3]} : {str(h[4])}')
            tv.insert("",END,text=h[0], values=(h[1],h[2],h[3],h[4]))
    else:
        tipo_wav.config(text='** El archivo no es tipo wav **', fg='red')
        print('El archivo no es de tipo wav')
    
#-- Defino la ventana raiz de la Interfaz Grafica de Usuario (GUI)
root = Tk()
root.title('UNSJ-FCEFyN ~ Teoria de la informacion ~ Ejercicio-1')
root.resizable(False,False)
root.iconbitmap('logo_unsj.ico')
root.geometry('1024x768')

#-- Defino el backgraound de la ventana principal
bgImage = PhotoImage(file='background.png')
background_label = Label(root,image=bgImage)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

#-- Defino el cartel principal
intro_text = Label(root, text='INGRESAR UN ARCHIVO PARA VALIDAR SI ES TIPO WAV', font=('Helvetica', 25), fg='white', bg='#010001')

#-- Defino la tabla
tv = ttk.Treeview(root, columns=('col1','col2','col3','col4'))

tv.column('#0', width=50, anchor=CENTER)
tv.column('col1', width=100, anchor=CENTER)
tv.column('col2', width=100, anchor=CENTER)
tv.column('col3', width=125, anchor=CENTER)
tv.column('col4', width=125, anchor=CENTER)

tv.heading('#0', text='Endian', anchor=CENTER)
tv.heading('col1', text='File offset (bytes)', anchor=CENTER)
tv.heading('col2', text='Field size (bytes)', anchor=CENTER)
tv.heading('col3', text='Field name', anchor=CENTER)
tv.heading('col4', text='Value', anchor=CENTER)

#-- Defino el cartel "es tipo wav"
tipo_wav = Label(root, font=('Helvetica', 25), bg='#010001')

#-- Defino el boton abrir
btnAbrir = Button(root, text='Abrir archivo', command=lambda:abrirArchivo(tv,tipo_wav))

intro_text.pack(pady=(20,0))
btnAbrir.pack(pady=(20,0))
tv.pack(pady=(370,0))
tipo_wav.pack(pady=(10,0))

root.mainloop()
