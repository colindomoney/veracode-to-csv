from __future__ import absolute_import

from veracodetocsv.helpers import models


def test_app_model():
    app = models.App("1", "test-app", "finance")

    assert app.id == "1"
    assert app.name == "test-app"
    assert app.business_unit == "finance"
    assert app.to_headers() == ["id", "name", "business_unit"]
    assert app.to_list() == ["1", "test-app", "finance"]


def test_sandbox_model():
    sandbox = models.Sandbox("1", "test-sandbox")

    assert sandbox.id == "1"
    assert sandbox.name == "test-sandbox"
    assert sandbox.to_headers() == ["id", "name"]
    assert sandbox.to_list() == ["1", "test-sandbox"]


def test_dynamic_build_model():
    build = models.DynamicBuild("1", "test-build", "2017-01-01T00:00:00")

    assert build.id == "1"
    assert build.name == "test-build"
    assert build.policy_updated_date == "2017-01-01T00:00:00"
    assert build.type == "dynamic"
    assert build.to_headers() == ["id", "name", "type", "policy_updated_date", "published_date"]
    assert build.to_list() == ["1", "test-build", "dynamic", "2017-01-01T00:00:00", None]


def test_static_build_model():
    build = models.StaticBuild("1", "test-build", "2017-01-01T00:00:00")

    assert build.id == "1"
    assert build.name == "test-build"
    assert build.policy_updated_date == "2017-01-01T00:00:00"
    assert build.type == "static"
    assert build.to_headers() == ["id", "name", "type", "policy_updated_date", "published_date", "analysis_size_bytes"]
    assert build.to_list() == ["1", "test-build", "static", "2017-01-01T00:00:00", None, None]


def test_dynamic_flaw_model():
    flaw = models.DynamicFlaw("1", "2017-01-01T00:00:00", "5", "78", "Command Injection",
                              "true", "3", "New", "Not Mitigated", "http://example.com/test")

    assert flaw.id == "1"
    assert flaw.date_first_occurrence == "2017-01-01T00:00:00"
    assert flaw.severity == "5"
    assert flaw.cweid == "78"
    assert flaw.remediationeffort == "3"
    assert flaw.affects_policy_compliance == "true"
    assert flaw.categoryname == "Command Injection"
    assert flaw.url == "http://example.com/test"
    assert flaw.remediation_status == "New"
    assert flaw.mitigation_status_desc == "Not Mitigated"
    assert flaw.to_headers() == ["id", "date_first_occurrence", "severity", "cweid",
                                 "categoryname", "affects_policy_compliance", "remediationeffort",
                                 "remediation_status", "mitigation_status_desc", "url"]
    assert flaw.to_list() == ["1", "2017-01-01T00:00:00", "5", "78",
                              "Command Injection", "true", "3",
                              "New", "Not Mitigated", "http://example.com/test"]


def test_static_flaw_model():
    flaw = models.StaticFlaw("1", "2017-01-01T00:00:00", "5", "78", "Command Injection",
                             "true", "3", "New", "Not Mitigated", "2", "test.war", "test.java", "69")

    assert flaw.id == "1"
    assert flaw.date_first_occurrence == "2017-01-01T00:00:00"
    assert flaw.severity == "5"
    assert flaw.cweid == "78"
    assert flaw.remediationeffort == "3"
    assert flaw.affects_policy_compliance == "true"
    assert flaw.categoryname == "Command Injection"
    assert flaw.exploitLevel == "2"
    assert flaw.module == "test.war"
    assert flaw.sourcefile == "test.java"
    assert flaw.line == "69"
    assert flaw.remediation_status == "New"
    assert flaw.mitigation_status_desc == "Not Mitigated"
    assert flaw.to_headers() == ["id", "date_first_occurrence", "severity", "cweid",
                                 "categoryname", "affects_policy_compliance", "remediationeffort",
                                 "remediation_status", "mitigation_status_desc", "exploitLevel",
                                 "module", "sourcefile", "line"]
    assert flaw.to_list() == ["1", "2017-01-01T00:00:00", "5", "78",
                              "Command Injection", "true", "3",
                              "New", "Not Mitigated", "2",
                              "test.war", "test.java", "69"]
