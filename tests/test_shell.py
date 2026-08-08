"""Nested execution: a cell driving `fastcore.nbio.run_cell` against a shell, in a loopless
process (the nbdev-test environment, entered through `asyncio.run` at the boundary). Pins that
inner-run assignments persist in the right namespace and errors stay structural."""
import asyncio
from IPython.core.interactiveshell import InteractiveShell
from execnb.shell import CaptureShell


def test_nested_run_separate_shell():
    "Inner runs against a second shell: assignments persist in the inner ns, visible during and after the outer cell"
    k = CaptureShell(mpl_format=None)
    k.user_ns['psh'] = InteractiveShell()
    outs = asyncio.run(k.run(
        "from fastcore.nbio import run_cell\n"
        "r1 = await run_cell(psh, 'zz = 5', silent=True)\n"
        "r2 = await run_cell(psh, 'zz2 = zz+1', store_history=True)\n"
        "ok = psh.user_ns.get('zz')==5 and psh.user_ns.get('zz2')==6"))
    assert not k.exc, outs
    psh = k.user_ns['psh']
    assert k.user_ns['ok'], 'inner assignments not visible inside the outer cell'
    assert psh.user_ns.get('zz')==5 and psh.user_ns.get('zz2')==6, 'inner assignments lost after the outer cell'


def test_nested_run_self_shell():
    "Inner runs against the outer shell itself via get_ipython(): assignments persist in its ns"
    k = CaptureShell(mpl_format=None)
    outs = asyncio.run(k.run(
        "from fastcore.nbio import run_cell\n"
        "await run_cell(get_ipython(), 'qq = 7', silent=True)\n"
        "await run_cell(get_ipython(), 'qq2 = qq+1', store_history=True)\n"
        "inner_saw = get_ipython().user_ns.get('qq2')"))
    assert not k.exc, outs
    assert k.user_ns.get('inner_saw')==8, 'inner runs did not see their own writes'
    assert k.user_ns.get('qq')==7 and k.user_ns.get('qq2')==8, \
        f"assignments lost after outer cell: qq={k.user_ns.get('qq')} qq2={k.user_ns.get('qq2')}"
