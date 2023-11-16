#### Python venv

```
sudo apt install python3.10-venv

pip install virtualenv

# create venv
python3 -m venv pythonenv_pelican

# activate venv
source pythonenv_pelican/bin/activate

# check if activated
pip list

# install packages
pip install yourpackage

# create requirements.txt
pip freeze > requirements.txt

# install from requirements.txt
pip install -r requirements.txt

# deactivate venv
deactivate


```

#### Build

```bash
pelican content

```

#### start local server

```bash
pelican -l
```

---

#### GitHub Pages Pelican Build Action

https://github.com/marketplace/actions/github-pages-pelican-build-action
https://github.com/nelsonjchen/gh-pages-pelican-action


```yaml
- name: GitHub Pages Pelican Build Action
  uses: nelsonjchen/gh-pages-pelican-action@0.1.10
```
