import subprocess

from ansible.plugins.strategy.linear import StrategyModule as LinearStrategyModule
from ansible.errors import AnsibleError


class StrategyModule(LinearStrategyModule):
    def _check_dirty_repo(self):
        check_remote_cmd = ["git", "remote", "show", "origin"]
        check_remote = subprocess.Popen(check_remote_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (check_remote_output, _) = check_remote.communicate()

        if check_remote.returncode != 0 or "out of date" in check_remote_output:
            raise AnsibleError(
                "Repository is out of date, use git pull or use"
                "extra var IGNORE_DIRTY_REPO"
            )

        diff_cmd = ["git", "diff", "--stat"]

        diff = subprocess.Popen(diff_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        (diff_output, _) = diff.communicate()

        if diff.returncode != 0 or len(diff_output) > 0:
            raise AnsibleError(
                "There are uncommited changes in the repo. "
                "Please commit or use extra var IGNORE_DIRTY_REPO"
            )

    def run(self, iterator, play_context):
        ignore_dirty_repo = self._variable_manager.extra_vars.get("IGNORE_DIRTY_REPO")

        if not ignore_dirty_repo:
            self._check_dirty_repo()

        return super(StrategyModule, self).run(iterator, play_context)

