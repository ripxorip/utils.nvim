# ============================================================================
# FILE: utils.py
# AUTHOR: Philip Karlsson <philipkarlsson at me.com>
# License: MIT license
# ============================================================================

import neovim
import os

def python_input(nvim, message = 'input'):
    nvim.command('call inputsave()')
    nvim.command("let user_input = input('" + message + ": ')")
    nvim.command('call inputrestore()')
    return nvim.eval('user_input')


@neovim.plugin
class UtilsPlug(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.logstr = []
        self.logstr.append('== utils debug ==')

    def log(self, s):
        self.logstr.append(s)

    def doRg(self, pattern, word):
        if len(word) == 0:
            rgs = 'Rg <cword> ' + pattern
        else:
            rgs = 'Rg ' + word[0] + ' ' + pattern
        self.nvim.command(rgs)

    @neovim.command("Ytc", range='', nargs='*', sync=True)
    def ytc(self, args, range):
        """ Yanks the entire buffer to clipboard """
        self.nvim.command('normal! mm')
        self.nvim.command('normal! gg')
        self.nvim.command('normal! v')
        self.nvim.command('normal! G')
        self.nvim.command('normal! $')
        self.nvim.command('normal! "*y')
        self.nvim.command('normal! \'m')

    @neovim.command("Rgc", range='', nargs='*', sync=True)
    def rgc(self, args, range):
        pattern = '--no-ignore --type c'
        self.doRg(pattern, args)

    @neovim.command("Rgh", range='', nargs='*', sync=True)
    def rgh(self, args, range):
        pattern = " --no-ignore -g '*.hpp' -g '*.h'"
        self.doRg(pattern, args)

    @neovim.command("Rgcpp", range='', nargs='*', sync=True)
    def rgcpp(self, args, range):
        pattern = '--no-ignore --type cpp'
        self.doRg(pattern, args)

    @neovim.command("UtilsShowLog", range='', nargs='*', sync=True)
    def usl(self, args, range):
        self.nvim.command('e utils_log')
        self.nvim.command('setlocal buftype=nofile')
        self.nvim.command('setlocal filetype=utils_log')
        self.nvim.current.buffer.append(self.logstr)

    @neovim.command("UtilsFindReplace", range='', nargs='*', sync=True)
    # TODO respect .gitignore etc.
    def frc(self, args, range):
        currentSymbol = self.nvim.eval("expand('<cword>')")
        # Prompt what to replace this symbol with
        resp = python_input(self.nvim, message="Replace " + currentSymbol + " with in cwd?")
        if resp == "":
            return
        cmd = "find . -type f ! -name \"*.o\" ! -name \"*.git\" -print0 | xargs -0 sed -i '' -e 's/%s/%s/g'" % (currentSymbol, resp)
        self.log(resp)
        os.system(cmd)
        self.nvim.command('set noconfirm')
        self.nvim.command('bufdo e')
        self.nvim.command('set confirm')

