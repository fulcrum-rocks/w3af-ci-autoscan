import sys
import subprocess
import os

if len(sys.argv) < 2:
    print('Error! URL is not specified!')
    exit(1)

url = sys.argv[1]
print('URL:', url)
print('Creating script...')

template = """
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
audit cors_origin, response_splitting, xpath, xss, xst, sqli
##Customize behavior of each audit plugin when needed
audit config file_upload
set extensions jsp,php,php2,php3,php4,php5,asp,aspx,pl,cfm,rb,py,sh,ksh,csh,bat,ps,exe
back

##Specify list of GREP plugins type to use (grep plugin is a type of
#plugin
#that can find also vulnerabilities or informations disclosure)
grep analyze_cookies, click_jacking, code_disclosure, cross_domain_js, csp, directory_indexing, dom_xss, error_500, error_pages, html_comments, objects, path_disclosure, private_ip, strange_headers, strange_http_codes, strange_parameters, strange_reason, url_session, xss_protection_header


#Specify list of INFRASTRUCTURE plugins type to use (infrastructure
#plugins
#is a type of plugin that can find informations disclosure)
#infrastructure server_header, server_status, domain_dot, dot_net_errors
#back

#Configure reporting in order to generate an HTML report
output console, xml_file
output config xml_file
set output_file /tmp/results/W3afReport.xml
set verbose False
back
output config console
set verbose True
back

back
#Set target informations, do a cleanup and run the scan
target
set target {0}
back

cleanup
start

exit
""".format(url)

with open("script.w3af", "w") as text_file:
    text_file.write(template)
print('Run scanner...')

p = subprocess.run(["./w3af_console", "-s", "script.w3af"], stdout=subprocess.PIPE,
    input='y\n', encoding='ascii')
subprocess.call(["cat", "/tmp/results/W3afReport.xml"])
