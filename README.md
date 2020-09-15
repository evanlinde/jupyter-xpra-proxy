# jupyter-xpra-proxy

**jupyter-xpra-proxy** provides Jupyter server and notebook extensions to proxy [xpra](https://xpra.org/). This will allow you to run X11 applications -- even a full desktop session.

If you have a JupyterHub deployment, jupyter-xpra-proxy can take advantage of JupyterHub's existing authenticator and spawner to launch xpra in users' Jupyter environments. You can also run this from within Jupyter.

This is a convenience package built from the template in [jupyter-server-proxy](https://github.com/jupyterhub/jupyter-server-proxy).


## Installation

### Pre-reqs

#### GUI desktop

(jupyter-xpra-proxy is configured for xfce4, but you can change this in `jupyter_xpra_proxy/__init__.py`)
```
sudo apt-get install xorg xfce4 xfce4-panel xfce4-session xfce4-settings xubuntu-icon-theme 
```

#### xpra and websockify

```
sudo apt-get install xpra websockify
```


### Install jupyter-xpra-proxy

Install the library:
```
pip install git+https://github.com/evanlinde/jupyter-xpra-proxy
```


### Multiuser Considerations

This extension launches an xpra process from the jupyter notebook server that listens on a tcp socket and accepts all connections. This is fine in JupyterHub deployments where user servers are containerized since other users cannot connect to the xpra port. In non-containerized JupyterHub deployments, for example on multiuser systems running LocalSpawner or BatchSpawner, this not secure. Any user may connect to xpra and run arbitrary code.

