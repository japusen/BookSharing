import sys
import re

from login.models import Course, Department


for line in file('ARTHI.txt', 'r'):
	courseCode = line.split(".", 1)[0].strip()
	courseTitle = line.split(".", 1)[1].strip()
	dept = Department.objects.get(pk=courseCode.split(" ")[0].strip())
	temp = courseCode.split(" ", 1)[1].strip()
	match = re.match(r'^([0-9]{1,3})([A-Z]{1,5})$', temp)
	if match:
		courseNo =  int(match.group(1))
		courseLetter = match.group(2)
	else:
		courseNo = int(temp)
		courseLetter = ''
	new = Course(dept=dept, courseCode=courseCode, courseTitle=courseTitle, courseNo=courseNo, courseLetter=courseLetter)
	new.save()
	print '%s %s' % (courseCode, courseTitle)
