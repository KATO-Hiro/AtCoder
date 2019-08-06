#! /usr/bin/env python3
import os
import sys
import shutil
import time
import urllib.request, urllib.parse
import http
import http.cookiejar
import json
from datetime import datetime, timedelta
from zipfile import ZipFile, ZIP_STORED
from subprocess import Popen, PIPE

class Option:
    def __init__(self):
        p = os.path.dirname(__file__).replace('\\', '/') + '/'
        self.crdir = '' if p == '/' else p
        self.cmdc = {}
        self.cmdi = {}
        self.op = ''
        self.cls = ''
        self.browser = ''
        self.getch = None
        self.win = False
        self.unix = False
        sp = ';'
        if len(sys.argv) > 1 : self.op = sys.argv[1].replace('\\', '/')
        if 'win' in sys.platform and 'darwin' != sys.platform:
            self.cls = 'cls'
            self.getch = self.getch_win
            self.win = True
        else:
            self.cls = 'clear'
            self.getch = self.getch_unix
            self.unix = True
            sp = ':'
        with open(self.crdir + 'setting.ini', encoding='UTF-8') as f:
            mode = ''
            for i in f.readlines():
                s = i.strip()
                if len(i) > 1 and i[:2] != '//':
                    if s[0] == '[':
                        mode = s
                    else:
                        s = s.replace('\\', '/')
                        if mode == '[path]':
                            os.environ['PATH'] = os.environ['PATH'] + sp + s
                        if mode == '[browser]':
                            self.browser = s
                        if mode == '[tle]':
                            self.timeout = int(s)
                        if mode == '[compile]':
                            lang, cmd = map(lambda x : x.strip(), s.split(':', 1))
                            self.cmdc[lang] = cmd.split()
                        if mode == '[interpreter]':
                            lang, cmd = map(lambda x : x.strip(), s.split(':', 1))
                            self.cmdi[lang] = cmd.split()
        self.browser_text = '   problempage:[P]' if self.browser else ''
    def getch_unix(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch
    def getch_win(self):
        import msvcrt
        try:
            return msvcrt.getch().decode('utf8')
        except:
            return ''
    def is_unix(self) : return self.unix
    def is_win(self) : return self.win

class PatCoderVirtualDir:
    def __init__(self):
        self.op = Option()
        s = ''
        if self.op.op:
            s = self.op.op
        else:
            s = input('VirtualContestURL = ')
        if 'http' not in s : return
        vurl = s
        vname = self._vurl_to_vname(vurl)

        for i, u, p in self._i_urls_problems(vurl):
            if self._template_copy(vname, i, u, p):
                print(i, 'ok')
            else:
                print(i, 'no')

    def _vurl_to_vname(self, vurl) : return vurl.split('not-522.appspot.com/contest/')[1]

    def _url_to_problem(self, url):
        ret = url.split('_')[1]
        if 'abc' in url and 'arc' in url:
            if ret == 'a' : return 'c'
            if ret == 'b' : return 'd'
        if ret in '1234':
            return '0abcd'[int(ret)]

        return ret

    def _line_to_url_problem(self, line):
        for i in line.split('"'):
            if 'atcoder.jp' in i:
                url = i.split('tasks')[0]
                problem = self._url_to_problem(i)
                return (url, problem)
    def _i_urls_problems(self, vurl):
        ret = []
        ht = urllib.request.urlopen(vurl).read().decode("utf-8").split('\n')
        cnt = 0
        for i in ht:
            if 'atcoder.jp' in i:
                cnt += 1
                url, problem = self._line_to_url_problem(i)
                ret += [(str(cnt), url, problem)]
        return ret
    def _template_copy(self, vname, index, url, s):
        vdir = self.op.crdir + vname
        idir = self.op.crdir + vname + '/' + index
        dir = self.op.crdir + vname + '/' + index + '/' + self._url_to_contest_name(url) + '/'
        try:
            try_mkdir(vdir)
            try_mkdir(idir)
            try_mkdir(dir)
            print('Create >>> ' + dir)
            temp = self.op.crdir + 'template' + '/'
            exts = [os.path.splitext(x)[1] for x in os.listdir(temp)]
            for i in exts : shutil.copyfile(temp + 'template' + i, dir + s + i)
            return 1
        except:
            return 0
    def _url_to_contest_name(self, url):
        # if 'beta.atcoder.jp' in url:
        if 'atcoder.jp' in url:
            return url.split('contests/')[1].split('/')[0]
        else:
            return url.split('//')[1].split('.')[0]


def try_mkdir(dir):
    try:
        if not os.path.exists(dir) : os.mkdir(dir)
    except:
        pass
def try_rmdir(dir):
    try:
        if os.path.exists(dir) : os.remove(dir)
    except:
        pass
def to_list(s, w, h):
    mlen = lambda x : sum(2 if ord(y) > 255 else 1 for y in x)
    r = []
    for i in s.split('\n'):
        if mlen(i) > w:
            b = ''
            bw = 0
            for j in i:
                c = mlen(j)
                if bw + c > w:
                    r += [b]
                    b = ''
                    bw = 0
                b += j
                bw += c
            r += [b]
        else:
            r += [i]
    if len(r) < h : r += [''] * (h-len(r))
    if len(r) > h : r = r[:h]
    for i in range(h):
        r[i] = r[i] + ' ' * (w-mlen(r[i]))
    return r
def strlim(s, n):
    if n <= 3:
        s = s[:n]
    elif len(s) > n:
        s = s[:n-3] + '...'
    return s.ljust(n, ' ')

if __name__ == '__main__':
    PatCoderVirtualDir()