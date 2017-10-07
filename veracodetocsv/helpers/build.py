# Purpose:  Build utilities

import json
import errno
import logging
import pytz
from datetime import datetime

from helpers.exceptions import VeracodeError


class BuildTools:
    def __init__(self):
        self.processed_builds = self._get_processed_builds()

    def _get_processed_builds(self):
        try:
            with open("processed_builds.txt", "r") as f:
                processed_builds = json.loads(f.read())
        except IOError as e:
            if e.errno is errno.ENOENT:
                processed_builds = {}
            else:
                logging.exception("Error opening processed builds file")
                raise VeracodeError(e)
        return processed_builds

    def build_should_be_processed(self, app_id, build_id, build_policy_updated_date):
        if app_id not in self.processed_builds or build_id not in self.processed_builds[app_id]:
            return True
        else:
            try:
                last_build_policy_updated_string = self.processed_builds[app_id][build_id]["policy_updated_date"][:22]\
                                                   + self.processed_builds[app_id][build_id]["policy_updated_date"][23:]
                last_build_policy_updated_date = datetime.strptime(last_build_policy_updated_string, "%Y-%m-%d %H:%M:%S%z").astimezone(pytz.utc)
            except ValueError as e:
                logging.exception("Error parsing date")
                raise VeracodeError(e)
            else:
                return build_policy_updated_date.astimezone(pytz.utc) > last_build_policy_updated_date

    def update_and_save_processed_builds_file(self, app_id, build_id, build_policy_updated_date):
        build_data = {"policy_updated_date": str(build_policy_updated_date)}
        if app_id not in self.processed_builds:
            self.processed_builds[app_id] = {build_id: build_data}
        else:
            self.processed_builds[app_id][build_id] = build_data
        try:
            with open("processed_builds.txt", "w") as f:
                json.dump(self.processed_builds, f)
        except IOError as e:
            logging.exception("Error saving processed builds file")
            raise VeracodeError(e)
