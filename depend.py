#!/usr/bin/python
import sys

dependencies = {}
installedpackages = []
key = ''
elements = []
f = open('pdf_input.dat')
lines = f.readlines()
for line in lines:
		print line
		elements = line.split()
		if len(elements) == 1:
				if 'LIST' in elements[0]:
					#iterates through the installed package list
					for installed in installedpackages:
						print "   {installed}".format(installed=installed)
				if 'END' in element[0]:
					#does a graceful exit when END is on a line
					sys.exit(0)
		if 'INSTALL' in elements[0] and len(elements) == 2:
				elements.remove('INSTALL')
				#check if package is installed
				if elements in installedpackages:
					print "   {package}already installed".format(package=elements[-1])
				elif elements not in installedpackages:
					key = elements[-1]
					for element in elements:
						for key, value in dependencies.items():
							if key == element:
								for each in value:
									if value not in installedpackages:
										print "   Installing {package}".format(package=each)
										installedpackages.append(each)
						print "   Installing {package}".format(package=element)				
						installedpackages.append(element)
		elif 'INSTALL' in elements[0] and len(elements) > 2:
				print "You can only install one item at a time.  Please correct {line}".format(line=line)
		if 'DEPEND' in elements[0] and len(elements) >= 2:
				#adds depenedencies
				key = elements[-1]
				elements.remove('DEPEND')
				elements.remove(key)
				dependencies.setdefault(key, [])
				for element in elements:
						dependencies[key].append(element)
		if 'REMOVE' in elements[0] and len(elements) == 2:
				elements.remove('REMOVE')
				try:
					dependencies.remove(elements)
					print "   Removing {elements{".format(element=elements)
				except:
					#put an exception here
					print "   {elements} is not installed.".format(elements=elements)
		elif 'REMOVE' in elements[0] and len(elements) > 2:
				print "You can only remove one item at a time.  Please correct {line}".format(line=line)
