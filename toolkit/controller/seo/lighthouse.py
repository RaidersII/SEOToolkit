from toolkit.lib.http_tools import request_page

def audit_google_lighthouse_full(url):
    pagespeed = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="
    result = request_page(pagespeed + url, timeout=30)
    return result.content

def audit_google_lighthouse_seo(url):
    pagespeed = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="
    result = request_page(pagespeed + url + "&category=seo", timeout=30)
    content = result.json()
    result_seo = {}
    result_seo["summary"] = {}
    result_seo["summary"]["requestedUrl"] = content["lighthouseResult"]["requestedUrl"]
    result_seo["summary"]["finalUrl"] = content["lighthouseResult"]["finalUrl"]
    result_seo["summary"]["timing"] = content["lighthouseResult"]["timing"]["total"]
    result_seo["summary"]["date"] = content["lighthouseResult"]["fetchTime"]
    result_seo["results"] = {}
    for key in content["lighthouseResult"]["audits"]:
        result_seo["results"][key] = {}
        result_seo["results"][key]["short_desc"] = content["lighthouseResult"]["audits"][key]["title"]
        result_seo["results"][key]["long_desc"] = content["lighthouseResult"]["audits"][key]["description"]
        result_seo["results"][key]["score"] = content["lighthouseResult"]["audits"][key]["score"]


    return result_seo

    