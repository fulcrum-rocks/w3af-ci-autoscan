import sys

url = sys.argv[1]

template = """
# -----------------------------------------------------------------------------------------------------------
#                                              W3AF AUDIT SCRIPT FOR WEB APPLICATION
# -----------------------------------------------------------------------------------------------------------
#Configure HTTP settings
http-settings
set timeout 30
back
#Configure scanner global behaviors
misc-settings
set max_discovery_time 20
set fuzz_cookies True
set fuzz_form_files True
set fuzz_url_parts True
set fuzz_url_filenames True
back
plugins
#Configure entry point (CRAWLING) scanner
crawl web_spider
crawl config web_spider
set only_forward False
set ignore_regex (?i)(logout|disconnect|signout|exit)+
back
#Configure vulnerability scanners
##Specify list of AUDIT plugins type to use
audit blind_sqli, buffer_overflow, cors_origin, csrf, eval, file_upload, ldapi, lfi, os_commanding, phishing_vector, redos, response_splitting, sqli, xpath, xss, xst
##Customize behavior of each audit plugin when needed
audit config file_upload
set extensions jsp,php,php2,php3,php4,php5,asp,aspx,pl,cfm,rb,py,sh,ksh,csh,bat,ps,exe
back
##Specify list of GREP plugins type to use (grep plugin is a type of plugin that can find also vulnerabilities or informations disclosure)
grep analyze_cookies, click_jacking, code_disclosure, cross_domain_js, csp, directory_indexing, dom_xss, error_500, error_pages, 
html_comments, objects, path_disclosure, private_ip, strange_headers, strange_http_codes, strange_parameters, strange_reason, url_session, xss_protection_header
#Configure reporting in order to generate an HTML report
output console, html_file
output config html_file
set output_file /tmp/W3afReport.html
set verbose True
back
output config console
set verbose True
back
back
#Set target informations, do a cleanup and run the scan
target 
set target {0}
set target_os windows
set target_framework php
back
cleanup
start""".format(url)

with open("script.w3af", "w") as text_file:
    text_file.write(template)