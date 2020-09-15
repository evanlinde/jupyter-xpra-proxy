"""
Return config on servers to start for xpra

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os

def setup_xpra():
    return {
        'command': [ 'xpra', 'start-desktop', '--start=xfce4-session', '--bind-tcp=0.0.0.0:' + str(port), '--html=on', '--auth=allow' ],
        'environment': {},
        'launcher_entry': {
            'title': 'xpra',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'xpra.svg')
        }
    }
