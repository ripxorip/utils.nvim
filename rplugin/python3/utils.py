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

