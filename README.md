# KnitDB

This repository contains the results of machine knitting and measuring a group of patterns.
This collection first appeared as part of the KnitPick paper at UIST 2019 ([project page](https://textiles-lab.github.io/publications/2019-knitpick/)).

These patterns were collected from the [Essential Stitch Collection](https://lccn.loc.gov/2009047907) book and the [Stitch Maps](https://stitch-maps.com/) web page; the [KnitPick paper](https://textiles-lab.github.io/publications/2019-knitpick/) describes how they were converted into 60x60 charts.
All patterns were machine-knit on a Shima Seiki SWG 091N2 using Tamm Petit 2/30 acrylic yarn (Color T4221 - Medium Camel).

## Measurements
Measurements and notes for each swatch are available in the ```swatches.csv``` file.

## Charts
Cart files are provided for reference but are in an undocumented and ideosyncratic format.
If you believe these would be useful for you, please get in touch with the authors -- see [project page](https://textiles-lab.github.io/projects/knitdb/).

Location: ```charts/```

Naming: ```patternName``` from the swatches.csv file

Format: ???

## Machine Knitting Instructions
We originally converted charts to knitting instructions using an old pipeline; we've retroactively modified this pipeline to also produce ```.knitout``` files to describe the instructions, and included the files here.
To the best of our knowledge, these files exactly match what was knit. Please let us know if you find any discrepencies.

Location: ```knitouts/```

Naming: Same as chart, with ```.knitout``` extension instead of ```.chart```

Format: [knitout](https://github.com/textiles-lab/knitout)

## Stitch Meshes and Yarn Paths
TODO: These can be created from ...


## Photos
The swatches were photographed three times each as part of measurement.
Relaxed photos were taken by gently sticking the swatch to a piece of sandpaper.
Stretched photos were taken by stretching the swatch between metal bars attached to weights (TOOD g).
In the stretched configuration, photos with both light and dark backgrounds were taken.

In some cases, swatches were photographed multiple times to correct errors, in which case a ```.2``` or ```.3``` is appended.
In other cases, swatches were mistakenly measured twice, in which case a ```.A``` or ```.B``` is used to differentiate and a note appears in ```swatches.csv```.
(In one instance, a swatch was photographed with the wrong side up, and this is also noted.)

Photos are named by the ```DAT_POS_simplePatternName``` where ```DAT``` is the dat id, ```POS``` is the dat position and ```simplePatternName``` is the ```patternName``` from swatches.csv with everything after the first underscore removed (that is, the string ```_out.chart``` or ```_{40 hex digits}_out.chart``` has been removed).

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

Location: ```photos/relaxed/```

Naming: ```simplePatternName.NEF```

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


To save repository space, these photos are stored on google drive:

Note that the photos ```10_2_034BrokenRibBacketWeave_*.NEF``` and ```10_3_037SubtleTwist_*.NEF``` are missing.

Location: ```photos/stretched/```

Naming: ```simplePatternName_light.NEF``` (light background), ```simplePatternName_dark.NEF``` (dark background)

Format: Nikon raw file.
