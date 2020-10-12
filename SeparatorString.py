#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

try:
    import sys
    import os
    import time
    import pyperclip
    import asyncio
    from datetime import datetime
    from progress.bar import IncrementalBar
except:
    dependencies = open('./_requirements.txt', 'w')
    dependencies.write('pyperclip==1.8.0\nprogress==1.5\nasyncio==3.4.3\n')
    dependencies.close()
    print('Для корректной работы, введите: pip3 install -r _requirements.txt')
    sys.exit()

if os.path.exists('_requirements.txt') == True:
    os.remove('_requirements.txt')


def timeit(func):
    async def wrapper(coro):
        start = datetime.now()
        result = func
        print('time {}: {}'.format(func.__name__, datetime.now() - start))
        await asyncio.sleep(.5)
        return result
        return loop.run_until_complete(coro)
    return wrapper


class SeparatorString():
    def __init__(self, test=False):
        self.text = ''
        self.test = test
        self.separator = ''

    """ Программа для разбиения текста """

    def ReadString(self):
        """
        Функция читающая подаваемые строки и
        разбивающая их по разделителю
        """
        print('Подождите, программа работает с буфером обмена...')
        self.Loop()
        while True:
            try:
                self.separator = str(input('Введите символ разделитель: '))
                break
            except:
                print('Введенный символ отсутствует в исходним тексте, повторите ввод')
                continue
        if self.separator == 'exit':
            sys.exit()
        elif self.separator == '}':
            lines = self.CssSplit()
        textWriten = ''.join(lines)
        return textWriten

    def CssSplit(self):
        onelines = self.text.split('{')
        for i in range(len(onelines)):
            onelines[i] = onelines[i].strip() + ' {' + '\n' + '  '
        onelines = ''.join(onelines)
        lines = onelines.split(self.separator)
        for j in range(len(lines)):
            lines[j] = lines[j].strip() + '\n' + str(self.separator) + '\n'
        return lines

    #@timeit
    async def Countdown(self):
        """ Прогресс-бар  """
        bar = IncrementalBar('Countdown', max=100)
        for i in range(100):
            bar.next()
            time.sleep(.03)
        bar.finish()

    #@timeit
    async def PasteText(self):
        """ Получение текста из буфера обмена """
        pasteText = pyperclip.paste()
        self.text = pasteText
        print('First 40 strings in paste text: {}'.format(self.text[:40]))
        await asyncio.sleep(.5)

    def Loop(self):
        """ Ассинхронное выполнение получения текста из буфера обмена и прогресс-бара """
        loop = asyncio.get_event_loop()
        tasks = [
            loop.create_task(self.Countdown()),
            loop.create_task(self.PasteText()),
        ]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()

    def EnterFile(self):
        """ Запись в файл """
        while True:  # Проверка существования директории
            if os.path.exists('/mnt/c/temp') == True:
                string = self.ReadString()
                filename = str(
                    input('Введите название файла, куда будут записаны данные: '))
                if os.path.exists(os.path.join('/', 'mnt', 'c', 'temp', filename)) == False:
                    writeString = open(os.path.join(
                        '/', 'mnt', 'c', 'temp', filename), "w")
                    writeString.write(string)
                    writeString.close()
                    print('Данные записаны в ' +
                          os.path.join('/', 'mnt', 'c', 'temp', filename))
                    return False
                else:
                    writeString = open(os.path.join(
                        '/', 'mnt', 'c', 'temp', filename), "a")
                    writeString.write(string)
                    writeString.close()
                    print('Данные добавлены в файл', os.path.join(
                        '/', 'mnt', 'c', 'temp', filename))
                    return False
            else:
                path = '/mnt/c/temp'
                os.makedirs(path)
                bar = IncrementalBar('Makedir ', max=1)
                for i in range(1):
                    print(os.path.dirname(path))
                    bar.next()
                    time.sleep(0.01)
                bar.finish()
                continue


def main():
    enterText = SeparatorString(test=True)
    enterText.EnterFile()


if __name__ == "__main__":
    main()
