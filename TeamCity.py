from Connection import Connection

class NoConnection(Exception):
    pass

class NoBuild(Exception):
    pass

class TeamCity:
    def __init__(self, url, build_type_id):
        self.connection = Connection(url)

        try:
            root = self.connection.get_href("/guestAuth/app/rest", {})
        except Exception:
            raise NoConnection

        if not 'TeamCity REST API' in root:
            raise NoConnection

        try:
            self.build_type = self.get_build_type(build_type_id)
        except Exception:
            raise NoBuild

    def get_projects(self):
        projects = self.connection.get_href_json("/guestAuth/app/rest/projects")["project"]
        return [project["name"] for project in projects]

    def get_project_details(self, name):
        self.projects = self.connection.get_href_json("/guestAuth/app/rest/projects")["project"]
        self.buildType = self.get_buildType(project, config.buildType)
        for project in self.projects:
            if project["name"] == name:
                return self.connection.get_href_json(project["href"])
        return None

    def get_build_types(self):
        return self.connection.get_href_json("/guestAuth/app/rest/buildTypes")["buildType"]
    
    def get_build_type(self, build_type_id):
        for build_type in self.get_build_types():
            if build_type["id"] == build_type_id:
                return self.connection.get_href_json(build_type["href"])
        return None

    def get_builds(self, build_type):
        href = build_type["builds"]["href"]
        return self.connection.get_href_json(href)["build"]

    def get_latest_build(self):
        builds = self.get_builds(self.build_type)
        if builds == None or len(builds) == 0:
            return None
        return self.get_build_details(builds[0])

    def build_finished(self, build):
        return build["state"] == "finished"

    def build_failed(self, build):
        return build["status"] == "FAILURE"
    
    def get_build_details(self, build):
        href = build["href"]
        return self.connection.get_href_json(href)

    def get_failed_builds(self):
        failed = []
        for build_item in self.get_builds(self.buildType):
            if self.build_finished(build_item):
                if self.build_failed(build_item):
                    failed.append(self.get_build_details(build_item))
                else:
                    break
        failed.reverse()
        return failed

    def get_failed_tests(self, build):
        failed = []
        id = build["id"]
        url = "/guestAuth/app/rest/testOccurrences?locator=build:{0}".format(id)
        tests = self.connection.get_href_json(url)
        if tests["count"] > 0:
            for test in tests["testOccurrence"]:
                if not test["status"] == "SUCCESS":
                    failed.append(test)

        return failed

    def get_checkins(self, build):
        checkins = []
        for checkin in build["lastChanges"]["change"]:
            checkins.append(checkin["username"])
        return checkins

    def close(self):
        self.connection.connection.close()

if __name__ == "__main__":
    url = raw_input("Enter TeamCity server url:")
    teamcity = TeamCity(url)
    print teamcity.get_projects()
