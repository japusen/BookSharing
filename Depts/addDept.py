from login.models import Department

for line in file('departments', 'r'):
	split = line.split('-')
	deptCode = split[1].strip()
	deptName = split[0].strip()
	new = Department(dept=deptCode, deptName=deptName)
	new.save()
