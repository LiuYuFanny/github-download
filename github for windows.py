import os
import urllib

path = "D:\\github\\"
version = "GitHub_3_0_17_0"

urls = [
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/de/Microsoft.Expression.Interactions.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/en/Microsoft.Expression.Interactions.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/es/Microsoft.Expression.Effects.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/es/Microsoft.Expression.Interactions.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/fr/Microsoft.Expression.Effects.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/fr/Microsoft.Expression.Interactions.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/Images/App.ico.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/it/Microsoft.Expression.Effects.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/it/Microsoft.Expression.Interactions.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/ja/Microsoft.Expression.Effects.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/ja/Microsoft.Expression.Interactions.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/ko/Microsoft.Expression.Effects.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/ko/Microsoft.Expression.Interactions.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/ru/Microsoft.Expression.Effects.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/ru/Microsoft.Expression.Interactions.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/zh-Hans/Microsoft.Expression.Effects.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/zh-Hans/Microsoft.Expression.Effects.resources.dll_2.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/zh-Hans/Microsoft.Expression.Interactions.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/zh-Hans/Microsoft.Expression.Interactions.resources.dll_2.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/zh-Hant/Microsoft.Expression.Effects.resources.dll.deploy",
"http://github-windows.s3.amazonaws.com/Application Files/" + version + "/zh-Hant/Microsoft.Expression.Interactions.resources.dll.deploy",
]

def download(url):
	urlList = url.split('/')
	if urlList[-2].find('GitHub') == -1:
		if not os.path.isdir(path + urlList[-2]):
			os.mkdir(path + urlList[-2])
	fileName  = path + urlList[-2] + "\\" + urlList[-1]
	print "download " + fileName
	urllib.urlretrieve(url, fileName)

def rename():
	walkList = os.walk(path)
	for group in walkList:
		filePath = group[0]
		files = group[-1]
		for file in files:
			if file.find('.deploy'):
				fileName = file.replace('.deploy', '')
				os.rename(filePath + "\\" + file, filePath + "\\" + fileName)

for i in urls:
	download(i)

rename()