Part of the [KnitDB project](http://db.knit.zone) at the [Carnegie Mellon Textiles Lab](https://textiles-lab.github.io/).
For bugs, file a github issue.
For other inquires, please contact [Jim McCann](http://www.cs.cmu.edu/~jmccann/).

# KnitDB

This repository contains the results of machine knitting and measuring a group of patterns.
This collection first appeared as part of the KnitPick paper at UIST 2019 ([project page](https://textiles-lab.github.io/publications/2019-knitpick/)).

If you use data from this project, please cite the KnitDB project page as well as the KnitPick paper.

These patterns were collected from the [Essential Stitch Collection](https://lccn.loc.gov/2009047907) book and the [Stitch Maps](https://stitch-maps.com/) web page; the [KnitPick paper](https://textiles-lab.github.io/publications/2019-knitpick/) describes how they were converted into 60x60 charts.
All patterns were machine-knit on a 15-gauge Shima Seiki SWG091N2 using Tamm Petit 2/30 acrylic yarn (Color T4221 - Medium Camel).

## Measurements
Measurements and notes for each swatch are available in the [swatches.csv](swatches.csv) file.
This is a simplified version of an (internal) google sheet available here:

https://docs.google.com/spreadsheets/d/1IMrSV6Ko_APNaBrBPPJ-oIy15S53_X-9U_buCmDyZfA

(requires a Carnegie-Mellon-affiliated Google account.)

## Charts
Cart files are provided for reference but are in an undocumented and ideosyncratic format.
If you believe these would be useful for you, please get in touch with the authors -- see [project page](https://textiles-lab.github.io/projects/knitdb/).

Location: ```charts/$(simpleName).chart``` (simpleName from the swatches.csv file)

Format: JSON-based stitch graph, as described in the [KnitPick](https://textiles-lab.github.io/publications/2019-knitpick/) paper

## Machine Knitting Instructions
We originally converted charts to knitting instructions using an old pipeline; we've retroactively modified this pipeline to also produce ```.knitout``` files to describe the instructions, and included the files here.
To the best of our knowledge, these files exactly match what was knit. Please let us know if you find any discrepencies.

Location: ```knitouts/$(simpleName).knitout``` (simpleName from the swatches.csv file)

Format: [knitout](https://github.com/textiles-lab/knitout)

## Stitch Meshes and Yarn Paths
These can be created from the knitout files by using the [smobj](https://github.com/textiles-lab/smobj) utilities.
```
#for example:
	mkdir -p yarns smobjs
	../smobj/utilities/knitout-to-smobj knitouts/5_2_014TuckedRib.knitout  smobjs/5_2_014TuckedRib.smobj
	../smobj/utilities/smobj-to-yarns smobjs/5_2_014TuckedRib.smobj ../smobj/faces/knitout.sf yarns/5_2_014TuckedRib.yarns
```

Scripts are also provided to make all the knitout files into smobj and yarns files:
```
#use as follows:
	#NOTE: path to smobj utilities is hard-coded in these scripts; if you put them elsewhere you will need to edit
	cd scripts
	mkdir -p ../smobjs
	rm -f ../smobjs/*.smobj
	python3 make-smobjs-par.py
	mkdir -p ../yarns
	rm -f ../yarns/*.yarns
	python3 make-yarns-par.py
#or just:
	cd scripts
	make make-smobjs
	make make-yarns
```

Word of forwarning: even though the ```make-*-par.py``` scripts do spawn a bunch of parallel worker threads, the process of generating these files still takes a few minutes (2.5 minutes on my relatively recent desktop).

Currently, the smobj utilties are under development so pre-computed yarns or smobj files are not available.

## Photos
The swatches were photographed three times each as part of measurement.
Relaxed photos were taken by gently sticking the swatch to a piece of sandpaper.
Stretched photos were taken by stretching the swatch between metal bars attached to weights (TOOD g).
In the stretched configuration, photos with both light and dark backgrounds were taken.

In some cases, swatches were photographed multiple times to correct errors, in which case a ```.2``` or ```.3``` is appended.
In other cases, swatches were mistakenly measured twice, in which case a ```.A``` or ```.B``` is used to differentiate and a note appears in ```swatches.csv```.
(In one instance, a swatch was photographed with the wrong side up, and this is also noted.)

Note that the photos were taken in several sessions with different lighting and white balance settings (sessions can be recovered from EXIF data in the NEF files.)
This is especially noticiable in the first set of relaxed photos, where the white balance stored with the file is significantly flawed.
We have included a variety of miscellaneous calibration images (```DSC_*.NEF```) which may partially help with white balancing.

### Relaxed

To save repository space, these photos are stored on google drive:
https://drive.google.com/drive/folders/1FMwaVcfr_RN8J2lZSaw9dL3aTdHTbRpU

If you have the [gdrive](https://github.com/gdrive-org/gdrive) utility, you can download them from the command line as follows:
```
	cd photos
	#this will create a directory 'relaxed' with ~7.4G of photos:
	gdrive download --recursive 1FMwaVcfr_RN8J2lZSaw9dL3aTdHTbRpU
```

Note that the photo ```101_1_212Three plus.NEF``` is missing.

Location: ```photos/relaxed/$(simpleName).NEF```

Format: Nikon raw file.

### Stretched

To save repository space, these photos are stored on google drive:
https://drive.google.com/drive/folders/1R8VuEuiK3v9HLXmnBzYGdHSUFcR5wTZK

If you have the [gdrive](https://github.com/gdrive-org/gdrive) utility, you can download them from the command line as follows:
```
	cd photos
	#this will create a directory 'stretched' with ~15G of photos:
	gdrive download --recursive 1R8VuEuiK3v9HLXmnBzYGdHSUFcR5wTZK
```

Note that the photos ```10_2_034BrokenRibBacketWeave_*.NEF``` and ```10_3_037SubtleTwist_*.NEF``` are missing.

Location: ```photos/stretched/$(simpleName)_light.NEF``` (light background) and ```photos/stretched/$(simpleName)_dark.NEF``` (dark background)

Format: Nikon raw file.
