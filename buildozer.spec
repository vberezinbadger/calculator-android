[app]
title = Calculator
package.name = calculator
package.domain = org.tecspo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET
android.arch = armeabi-v7a
android.presplash.filename = %(source.dir)s/data/presplash.png
android.icon.filename = %(source.dir)s/data/icon.png
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
