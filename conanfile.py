from conans import ConanFile, tools

import os

class LcovConanFile(ConanFile):
    name = "lcov"
    version = "1.15"
    license = "GPLv2"
    exports = "LICENSE"
    requires = "perl/5.32.0@fickle/testing"

    def source(self):
        git = tools.Git(folder="lcov")
        git.clone("https://github.com/linux-test-project/lcov.git", "v1.15")

    def build(self):
        for file in os.listdir(os.path.join("lcov", "bin")):
            if file.startswith("gen") or file == "lcov":
                tools.replace_in_file(
                    os.path.join("lcov", "bin", file),
                    "`$tool_dir/get_version.sh --full`",
                    '"v1.15"')

    def package(self):
        self.copy("Copying", dst="licenses", src="lcov")
        self.copy("gen*", dst="bin", src="lcov/bin")
        self.copy("lcov", dst="bin", src="lcov/bin")

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
