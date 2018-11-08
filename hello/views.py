# django cas ng (integrate with CAS??) <-- don't want to do this
# want different groups, need different account for each one
# have different login methods
# investigate making user accounts with django (also groups)
# probably want a user account with several groups instead of several groups with several user account
# rank shifts? (allow TAs t0) and then have merit system for in-demand?
# avoid 3-0 problem (not checkboxes, rank)
# two part problem: do you provide good availabilites?
# have a public page showing who is working which shift + subs
# PROBLEM: create an algorithm to check if students are behaving correctly
# leaderboard: time elapsed between shift announce and sub accept
# "I can do this if nobody else can"
# show shifts that you didn't say you were available
# make sure that every shift is covered by subs

# poll lab TAs and also list servs
# mock up steps to process
# nail down the terminology

# try keepasking.io: how it's self-sustained
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, loader
from django.conf import settings
import requests
import os
import calendar
from collections import defaultdict
import yaml

from .models import Greeting

import django
django.setup()



# settings.configure() # We have to do this to use django templates standalone - see
# http://stackoverflow.com/questions/98135/how-do-i-use-django-templates-without-the-rest-of-django

# Our template. Could just as easily be stored in a separate file
month_mapping = {1: "January", 2: "February", 3: "March", 4: "April",
                5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
                10: "October", 11: "November", 12: "December"}
# inv_month_mapping = {v: k for k, v in month_mapping.items()}
month = 11 # placeholder
year = 2018 # placeholder
shifts = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
# shifts[2018][11][2].append((19, 2))
shifts[2018][11][2].append("19:00-21:00")
# shifts[2018][11][2].append((21, 2))
shifts[2018][11][2].append("21:00-23:00")
pick_shifts = yaml.load("""
- {day: Monday, start_time: '19:00', end_time: '21:00'}
- {day: Monday, start_time: '21:00', end_time: '23:00'}
- {day: Tuesday, start_time: '19:00', end_time: '21:00'}
- {day: Tuesday, start_time: '21:00', end_time: '23:00'}
- {day: Wednesday, start_time: '19:00', end_time: '21:00'}
- {day: Wednesday, start_time: '21:00', end_time: '23:00'}
- {day: Thursday, start_time: '19:00', end_time: '21:00'}
- {day: Thursday, start_time: '21:00', end_time: '23:00'}
- {day: Friday, start_time: '19:00', end_time: '21:00'}
- {day: Friday, start_time: '21:00', end_time: '23:00'}
- {day: Saturday, start_time: '15:00', end_time: '17:00'}
- {day: Saturday, start_time: '16:00', end_time: '18:00'}
- {day: Saturday, start_time: '17:00', end_time: '19:00'}
- {day: Sunday, start_time: '17:00', end_time: '19:00'}
- {day: Sunday, start_time: '18:00', end_time: '20:00'}
- {day: Sunday, start_time: '19:00', end_time: '21:00'}
- {day: Sunday, start_time: '20:00', end_time: '22:00'}
- {day: Sunday, start_time: '21:00', end_time: '23:00'}
""")

shifts_by_day = defaultdict(list)
indexed_shifts = []
i = 0
for s in pick_shifts:
    shifts_by_day[s["day"]].append((i, "{:s}-{:s}".format(s["start_time"], s["end_time"])))
    indexed_shifts.append(s)
    i += 1



# shifts = {"2018":
#             {"11":
#                 {"2": [(19, 2), (21, 2)]}
#             }
#         }

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    template = loader.get_template('calendar.html')
    calMatrix = calendar.monthcalendar(year, month)
    shifts_this_month = shifts[year][month]
    context = {"title": "{:s} {:d}".format(month_mapping[month], year),
                "monthCal": calMatrix,
                "shifts": shifts_this_month
              }
    return HttpResponse(template.render(context, request))
    # return render(request, 'index.html')

def select_shifts(request):
    if request.method == "GET":
        params = request.GET
    else:
        params = request.POST
    template = loader.get_template('shift-selection.html')
    context = { "shifts_by_day": shifts_by_day,
                "weekdays": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                "params": params
              }
    return HttpResponse(template.render(context, request))

def set_shifts(request):
    myshifts = defaultdict(list)
    i = 0
    template = loader.get_template('set-shifts.html')
    context = { "shifts_by_day": myshifts,
                "weekdays": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
              }
    for s in indexed_shifts:
        checked = request.POST.get(i)
        context["testing"] = checked
        return HttpResponse(template.render(context, request))
        if checked:
            myshifts[s["day"]].append((s["start_time"], s["end_time"]))
            return HttpResponse(template.render(context, request))
            # TODO: Add to user's shifts here
    return HttpResponseRedirect('/')

def select(request):

    return HttpResponse('Nothing here yet')


# def index(request):
#     r = requests.get('http://httpbin.org/status/418')
#     print(r.text)
#     return HttpResponse('<pre>' + r.text + '</pre>')

# def index(request):
#     times = int(os.environ.get('TIMES',3))
#     return HttpResponse('Hello! ' * times)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
