[app]

# (str) Title of your application
title = Anti Theft Test

# (str) Package name
package.name = antithefttest

# (str) Package domain (needed for android packaging)
package.domain = org.antitheft

# (list) Source files to include (let it include all)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
