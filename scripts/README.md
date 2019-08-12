# Scripts

These scripts in this folder were used in *making* the database; you shouldn't need to run them if you are just *using* the db.

Basic DB tasks:

```
#Create a 'swatches.csv' by filtering source document from google drive:
	rm -f 'Swatch Log - Reorganized.csv'
	#creates 'Swatch Log - Reorganized.csv':
	gdrive export --mime text/csv 1IMrSV6Ko_APNaBrBPPJ-oIy15S53_X-9U_buCmDyZfA
	#filters to create 'swatches.csv':
	python3 make-swatches-csv.py
#or just:
	make create-swatches-csv
```


```
#Check photo names (and for missing photos):
	rm -f stretched.list relaxed.list
	$(GDRIVE) list --no-header -m 1000 --query "'1R8VuEuiK3v9HLXmnBzYGdHSUFcR5wTZK' in parents" > stretched.list
	$(GDRIVE) list --no-header -m 1000 --query "'1FMwaVcfr_RN8J2lZSaw9dL3aTdHTbRpU' in parents" > relaxed.list
	python3 check-photo-names.py
#or just:
	make check-photo-names
```

```
#sort older/newer charts to extract the ones for actually knitted swatches (also simplifies names):
	#place older charts in 'src-older/'
	#place newer charts in 'src-newer/'
	rm -f ../charts/*.chart
	python3 sort-charts.py
#or just:
	#place older charts in 'src-older/'
	#place newer charts in 'src-newer/'
	make sort-charts
```
