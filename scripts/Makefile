GDRIVE=gdrive

all : 


create-swatches-csv :
	rm -f 'Swatch Log - Reorganized.csv'
	#creates 'Swatch Log - Reorganized.csv':
	gdrive export --mime text/csv 1IMrSV6Ko_APNaBrBPPJ-oIy15S53_X-9U_buCmDyZfA
	#filters to create 'swatches.csv':
	python3 make-swatches-csv.py
	mv swatches.csv ../swatches.csv


check-photo-names :
	rm -f stretched.list relaxed.list
	$(GDRIVE) list --no-header -m 1000 --query "'1R8VuEuiK3v9HLXmnBzYGdHSUFcR5wTZK' in parents" > stretched.list
	$(GDRIVE) list --no-header -m 1000 --query "'1FMwaVcfr_RN8J2lZSaw9dL3aTdHTbRpU' in parents" > relaxed.list
	python3 check-photo-names.py

download-stretched.list :
	rm -f stretched.list
	$(GDRIVE) list --no-header -m 1000 --query "'1R8VuEuiK3v9HLXmnBzYGdHSUFcR5wTZK' in parents" > stretched.list

download-relaxed.list :
	rm -f relaxed.list
	$(GDRIVE) list --no-header -m 1000 --query "'1FMwaVcfr_RN8J2lZSaw9dL3aTdHTbRpU' in parents" > relaxed.list
