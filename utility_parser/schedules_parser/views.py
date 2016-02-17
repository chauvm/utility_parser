from django.shortcuts import render
from django.http import HttpResponse

import re
import urllib2
from datetime import date
from bs4 import BeautifulSoup

# Create your views here.
	
"""
Example:
<tr class="">
        <td nowrap>
                Tuesday February 16, 2016
        </td>
        <td nowrap>
                12:00 PM
                -
                2:00 PM
        </td>
        <td>
                Veterans Memorial Skating Rink&nbsp;
        </td>
</tr>

"""
def index(request):
	header = "Schedules Parser App"
	context = {"header" : header}
	return render(request, "schedules_parser/index.html", context)
	
def ice_rink(request):
	header = "Ice Rinks Schedule"
	data = get_veteran_schedule()
	context = {"header" : header, "veteran_data" : data}
	return render(request, "schedules_parser/ice_rink.html", context)

def get_element(node):
        return node.next_element.next_element.next_element
def get_content(node):
        return node.text.strip()

def get_veteran_schedule():
        # Parse Sommervile recreation page
	veteran_memorial_url = "https://www.somervillerec.com/info/popups/activity_dates.aspx?ProgramID=29752&EventID=0&ActivityID=143909"
	content = urllib2.urlopen(veteran_memorial_url).read()
	#content = content.replace(re.compile('\t+'), '')
	
	tree = BeautifulSoup(content, 'html.parser')
	schedule_table = tree.find_all('table')[2]
	today = "{:%A %B %d, %Y}".format(date.today())

	# get today's data
	found = schedule_table.find('td', string=re.compile(today))
	slot = found.next_element.next_element.next_element
	place = slot.next_element.next_element.next_element

        # get next day's data
	found_2 = get_element(place)
	next_day = get_element(found_2)
	next_slot = get_element(next_day)
	next_place = get_element(next_slot)
	next_day = get_content(next_day)
	
        result = {today : {"Time": get_content(slot),
                          "Location": get_content(place)},
                  next_day : {"Time": get_content(next_slot),
                              "Location": get_content(next_place)}
                  }
	return result
