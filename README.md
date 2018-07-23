# Introduction

This ansible demonstrates an ansible strategy plugin used to check if the repository in which ansible is running is out of date or has uncommited changes.

We need to use the strategy plugin because this is the only type of plugin that allows to raise Exceptions that will actually stop the execution of a playbook.

# Usage

To use the plugin, you just have to create the ```strategy_plugins``` folder and add the plugin there, and update ansible.cfg accordingly.

To ignore a dirty repo, you can use the extra var ```IGNORE_DIRTY_REPO```.
