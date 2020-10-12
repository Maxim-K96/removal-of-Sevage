#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import sys
import re
from datetime import datetime
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


PATHLOG = 'C:/LogPath/'
if os.path.exists(PATHLOG) == False:
	os.makedirs(PATHLOG)

class RemovalOfSewage:
	def __init__(self, parent):
		"""VARIABLE"""
		#COLORS
		self._BACKGROUND = '#2C3A47'
		self._FOREGROUND = '#fff'
		self._FOREGROUND_ACTIVE = '#EAB543'

		#FONTS
		self._FONTS_BUTTON = {'fonts':'Colus', 'size': 12}
		self._FONTS_LABEL ={'fonts':'Calibri', 'size':12}

		#SIZE WINDOW
		self.width = 560
		self.height = 250

		# GENERAL VARIABLES
		self.__X = 10
		self.__WIDTH__ENTRY = 5
		self.__Y = 15
		self.__STEP = 40
		self.__LOCATION_ENTRY_X = self.width/1.2

		# PARAMETRS BUTTON
		self._WIDTH_BUTTON = round(self.width/40)
		self._PADDING_BUTTON = 2
		self._LOCATION_BUTTON_X = self.width/1.5
		self._LOCATION_BUTTON_Y = self.height/1.3
		self._TEXT_BUTTON = 'рассчитать'

		# PARAMETRS LABLE (cars zil) and ENTRY
		self._LOCATION_LABEL_ZIL_X = self.__X
		self._LOCATION_LABEL_ZIL_Y = self.__Y
		self._WIDTH_NUMBER_OF_FLIGHTS_ZIL_ENTRY = self.__WIDTH__ENTRY
		self._LOCATION_NUMBER_OF_FLIGHTS_ZIL_ENTRY_X = self.__LOCATION_ENTRY_X
		self._LOCATION_NUMBER_OF_FLIGHTS_ZIL_ENTRY_Y = self.__Y

		# PARAMETRS LABLE (cars KaMaz) and ENTRY
		self._LOCATION_LABEL_KAMAZ_X = self.__X
		self._LOCATION_LABEL_KAMAZ_Y = int(self.__Y + self.__STEP)
		self._WIDTH_NUMBER_OF_FLIGHTS_KAMAZ_ENTRY = self.__WIDTH__ENTRY
		self._LOCATION_NUMBER_OF_FLIGHTS_KAMAZ_ENTRY_X = self.__LOCATION_ENTRY_X
		self._LOCATION_NUMBER_OF_FLIGHTS_KAMAZ_ENTRY_Y = int(self.__Y + self.__STEP)

		# PARAMETRS LABLE (cars gaz) and ENTRY
		self._LOCATION_LABEL_GAZ_X = self.__X
		self._LOCATION_LABEL_GAZ_Y = int(self.__Y + self.__STEP * 2)
		self._WIDTH_NUMBER_OF_FLIGHTS_GAZ_ENTRY = self.__WIDTH__ENTRY
		self._LOCATION_NUMBER_OF_FLIGHTS_GAZ_ENTRY_X = self.__LOCATION_ENTRY_X
		self._LOCATION_NUMBER_OF_FLIGHTS_GAZ_ENTRY_Y = int(self.__Y + self.__STEP * 2)

		# PARAMETRS LABLE OUTPUT
		self._LOCATION_LABEL_OUTPUT_X = self.__X
		self._LOCATION_LABEL_OUTPUT_Y = int(self.__Y + self.__STEP * 3)
		self._WIDTH_LABEL_OUTPUT = round(self.width/8.5)

		# PARAMETRS WINDOW
		self.parent = parent
		self.parent.configure(background=self._BACKGROUND)
		self.parent.minsize(self.width, self.height)
		self.parent.maxsize(self.width, self.height)
		self.parent.title('Количество вывезенных отходов')

		# Установка значка в левом верхнем углу
		icon = PhotoImage(file=os.path.join('icon.gif'))
		self.parent.tk.call('wm', 'iconphoto', self.parent._w, icon)
		#self.parent.iconbitmap(icon)

		self.style = ttk.Style()

		# STYLE LABEL
		self.style.configure(
			"BW.TLabel", 
			foreground=self._FOREGROUND, 
			background=self._BACKGROUND, 
			font=(self._FONTS_LABEL['fonts'], self._FONTS_LABEL['size']))

		# STYLE BUTTON
		self.style.configure(
			"TButton", 
			font = (self._FONTS_BUTTON['fonts'], self._FONTS_BUTTON['size']), 
			width = self._WIDTH_BUTTON,
			padding = self._PADDING_BUTTON
		)
		self.style.map(
			"TButton",
			foreground=[('pressed', self._FOREGROUND), ('active', self._FOREGROUND_ACTIVE)],
			background=[('pressed', '!disabled', self._FOREGROUND), ('active', self._FOREGROUND_ACTIVE)]
			)
		
		self.inputData()

	def removal(self, Zil, KaMaz, Gaz):
		"""METHOD SUM VOLUME AND NUMBER_OF_FLIGHTS_CARS"""
		volume_Zil = 5.5
		volume_KaMaZ = 8
		volume_Gaz = 4
		self.amountExported = Zil*volume_Zil + KaMaz*volume_KaMaZ + Gaz*volume_Gaz

		self.lbl_Output['text'] = 'Количество вывезенных отходов {} составляет: {} кубометров'.format(datetime.today().strftime("%d.%m.%Y"), float(self.amountExported))

		self.clear()
		self.logging()

	def inputData(self):
		"""METHOD FOR ARRANGING WIDGETS IN A WINDOW"""
		lbl_Zil = ttk.Label(self.parent, text = "Введите количество рейсов, совершенных машиной ЗИЛ:", style="BW.TLabel")
		lbl_Zil.place(x=self._LOCATION_LABEL_ZIL_X, y=self._LOCATION_LABEL_ZIL_Y)

		self.Number_of_flights_Zil = Entry(self.parent, width=self._WIDTH_NUMBER_OF_FLIGHTS_ZIL_ENTRY)
		self.Number_of_flights_Zil.place(x=self._LOCATION_NUMBER_OF_FLIGHTS_ZIL_ENTRY_X, y=self._LOCATION_NUMBER_OF_FLIGHTS_ZIL_ENTRY_Y)
		self.Number_of_flights_Zil.focus()

		lbl_KaMaZ = ttk.Label(self.parent, text = "Введите количество рейсов, совершенных машиной КАМАЗ:", style="BW.TLabel")
		lbl_KaMaZ.place(x=self._LOCATION_LABEL_KAMAZ_X, y=self._LOCATION_LABEL_KAMAZ_Y)

		self.Number_of_flights_KaMaZ = Entry(self.parent, width=self._WIDTH_NUMBER_OF_FLIGHTS_KAMAZ_ENTRY)
		self.Number_of_flights_KaMaZ.place(x=self._LOCATION_NUMBER_OF_FLIGHTS_KAMAZ_ENTRY_X, y=self._LOCATION_NUMBER_OF_FLIGHTS_KAMAZ_ENTRY_Y)

		lbl_Gaz = ttk.Label(self.parent, text = "Введите количество рейсов, совершенных машиной ГАЗ:", style="BW.TLabel")
		lbl_Gaz.place(x=self._LOCATION_LABEL_GAZ_X, y=self._LOCATION_LABEL_GAZ_Y)

		self.lbl_Output = Label(
			self.parent, 
			text = '', 
			style="BW.TLabel",
			background=self._BACKGROUND,
			width=self._WIDTH_LABEL_OUTPUT
		)
		self.lbl_Output.place(x=self._LOCATION_LABEL_OUTPUT_X, y=self._LOCATION_LABEL_OUTPUT_Y)

		self.Number_of_flights_Gaz = Entry(self.parent, width=self._WIDTH_NUMBER_OF_FLIGHTS_GAZ_ENTRY)
		self.Number_of_flights_Gaz.place(x=self._LOCATION_NUMBER_OF_FLIGHTS_GAZ_ENTRY_X, y=self._LOCATION_NUMBER_OF_FLIGHTS_GAZ_ENTRY_Y)

		btn = ttk.Button(
			self.parent, 
			text = self._TEXT_BUTTON, 
			command=lambda: self.validationCheck())
		btn.place(x=self._LOCATION_BUTTON_X, y=self._LOCATION_BUTTON_Y)

	def validationCheck(self):
		"""CHECK VALIDATION"""
		try:
			self.removal(
				int(self.Number_of_flights_Zil.get()), 
				int(self.Number_of_flights_KaMaZ.get()),
				int(self.Number_of_flights_Gaz.get()) 
			)
		except ValueError:
			messagebox.showerror('Error', 'Вы ввели некорректные данные, повторите ввод')
			self.clear()

	def clear(self):
		"""METHOD CLEAR ENTRY"""
		self.Number_of_flights_Zil.delete(0, END)
		self.Number_of_flights_KaMaZ.delete(0, END)
		self.Number_of_flights_Gaz.delete(0, END)

		self.Number_of_flights_Zil.focus()

	def logging(self):
		"""LOGGING"""
		filename = '%s.log'%datetime.today().strftime("%d.%m.%Y-%H-%M-%S")
		logfile = open(PATHLOG + filename, 'w')
		logfile.write('Количество вывезенных отходов {} составляет: {} кубометров'.format(datetime.today().strftime("%d.%m.%Y"), float(self.amountExported)))
		logfile.close()
		

if __name__ == '__main__':
	root = Tk()
	app = RemovalOfSewage(root)
	sys.exit(root.mainloop())
