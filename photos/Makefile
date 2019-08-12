
GDRIVE=gdrive

all :

#Download all the images:

download-all : download-stretched download-relaxed

download-stretched :
	$(GDRIVE) download --recursive 1FMwaVcfr_RN8J2lZSaw9dL3aTdHTbRpU

download-relaxed :
	$(GDRIVE) download --recursive 1R8VuEuiK3v9HLXmnBzYGdHSUFcR5wTZK

#Just list the files, don't download them (handy if you want file IDs of just a few photos):

download-stretched.list :
	$(GDRIVE) list --no-header -m 1000 --query "'1R8VuEuiK3v9HLXmnBzYGdHSUFcR5wTZK' in parents" > stretched.list

download-relaxed.list :
	$(GDRIVE) list --no-header -m 1000 --query "'1FMwaVcfr_RN8J2lZSaw9dL3aTdHTbRpU' in parents" > relaxed.list
