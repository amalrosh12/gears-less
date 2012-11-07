import os
from gears.compilers import ExecCompiler


class LESSCompiler(ExecCompiler):

    result_mimetype = 'text/css'
    executable = 'node'
    params = [os.path.join(os.path.dirname(__file__), 'compiler.js')]

    def __call__(self, asset):
        self.asset = asset
        super(LESSCompiler, self).__call__(asset)

    def get_args(self):
        args = super(LESSCompiler, self).get_args()
        args.append(self.asset.absolute_path)
        return args
