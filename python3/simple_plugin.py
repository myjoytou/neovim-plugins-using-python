import neovim

@neovim.plugin
class SimplePlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.function("SimpleFunction", sync= true)
    def simple_function(self, args):
        print "the self is: ", self
        print "the args are: ", args

    @neovim.command("SimpleCommand", range='', nargs='*')
    def def simple_command(self, args, range):
        self.nvim.current.line = ('Command with args: {}, range: {}'
                .format(args, range))

    @neovim.autocmd('BufEnter', pattern='*.py', eval='expand("<afile>")', sync= true)
    def on_bufenter(self, filename):
        self.nvim.out_write("testplugin is in " + filename + "\n")
