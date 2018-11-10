# ============================================================================
# FILE: utils.py
# AUTHOR: Philip Karlsson <philipkarlsson at me.com>
# License: MIT license
# ============================================================================

import neovim


@neovim.plugin
class UtilsPlug(object):
    def __init__(self, nvim):
        self.nvim = nvim

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
