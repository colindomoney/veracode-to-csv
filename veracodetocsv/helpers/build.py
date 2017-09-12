import json
import errno
import logging
from datetime import datetime

from .exceptions import VeracodeError


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
        if app_id not in self.processed_builds:
            return True
        else:
            if build_id not in self.processed_builds[app_id]:
                return True
            else:
                # Check if build policy update has occurred
                xml_date_format = "%Y-%m-%dT%H:%M:%S"
                try:
                    current_build_policy_updated = datetime.strptime(build_policy_updated_date, xml_date_format)
                    last_build_policy_updated = datetime.strptime(self.processed_builds[app_id][build_id]["policy_updated_date"], xml_date_format)
                except ValueError as e:
                    logging.exception("Error parsing date")
                    raise VeracodeError(e)
                else:
                    return current_build_policy_updated > last_build_policy_updated

    def update_and_save_processed_builds_file(self, app_id, build_id, build_policy_updated_date):
        build_data = {"policy_updated_date": build_policy_updated_date}
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
