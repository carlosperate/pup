"""
PUP Plugin implementing the 'python-runtime' step.
"""

import logging


_log = logging.getLogger(__name__)



class Step:

    """
    Downloads and extracts a relocatable Python runtime for the target platform
    into the directory specified by the context.
    """

    @staticmethod
    def usable_in(ctx):
        return (
            (ctx.pkg_platform == 'darwin') or
            (ctx.pkg_platform == 'win32')
        ) and (
            (ctx.pkg_platform == ctx.tgt_platform)
        )

    def __call__(self, ctx, _dsp):
        _log.warning(
            'TODO: Extract relocatable Python runtime for %r into %r.',
            ctx.tgt_platform,
            ctx.python_runtime_dir,
        )
