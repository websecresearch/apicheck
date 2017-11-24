# Copyright 2017 BBVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest

from os.path import exists, join

from apitest.actions.unittest.unittest.api import build_unittest
from apitest.actions.unittest.unittest.model import ApitestGenerateUnitTestModel


def test_build_unittest_runs_ok(apitest_file, tmpdir, apitest_obj):
    in_file = apitest_file
    out_dir = str(tmpdir) + "/outdir/"

    config = ApitestGenerateUnitTestModel(**dict(file_path=in_file, output_dir=out_dir))

    build_unittest(config, apitest_obj)

    # Check that output dir has "conftest.py" file
    assert exists(join(out_dir, "conftest.py")) is True


def test_build_unittest_runs_config_none(apitest_obj):

    with pytest.raises(AssertionError):
        build_unittest(None, apitest_obj)


def test_build_unittest_runs_data_none(apitest_file, tmpdir):
    in_file = apitest_file
    out_dir = str(tmpdir) + "/outdir/"

    config = ApitestGenerateUnitTestModel(**dict(file_path=in_file, output_dir=out_dir))

    with pytest.raises(AssertionError):
        build_unittest(config, None)
