# Gazellesync
GazelleSync is a cross-platform program coded in Python, originally created by “Creator” on Orpheus.
It is able to clone very quickly a torrent and all the associated information from one tracker to another.
It has a GUI, but it can also be used by command line.

# Requirements

python 3.6 or above.

 (use pip install MUDULENAME)
 ``mechanize``
 
 `requests`
 
 `pysimplegui`

# current bugs/issues

OPS -> RED doesn't work if the OPS torrent is set to "Original Release".
Any .log that's not a rip log is a problem. (0% log on destination tracker)
Currently incompatible with RED's 2FA.

# Command line usage

Obligatory arguments:

`to: tracker the torrent will be moved to (Possible values: ops or red or dic or nwcd )`

`from: tracker the torrent comes from (Possible values: ops or red or dic or nwcd )`

IF I want to point to the exact folder of the album

 ` album: the folder of the album (examples : “C:\Albums\Roger Molls - Melography – 2019 [FLAC]”, “/Albums/Roger Molls - Melography – 2019 [FLAC]”`
ELSE

 ` folder: the folder that contains all albums. The album folder(s) will be extracted from the site metadata (ex: “C:\Albums\”, “~/Albums/”)`
 
 END


In order to get the metadata from the Source Tracker :
IF I want to use the torrent ID from the site

  `tid: the torrent ID. Example: 2167548`
  
ELSEIF I want to get the torrent ID from the permalink

`  link: the whole permalink. Example: “https://redacted.ch/torrents.php?id=1006866&torrentid=2167548#torrent2167548”`

ELSEIF I want to point to a .torrent file

 ` tpath: the path that points towards the .torrent file. The infohash will be computed in order to retrieve the torrent ID on the source private tracker.`
 
ELSEIF I want to point to a directory full of .torrent files (each of these will be processed)

 ` tfolder: the folder containing all the .torrent files`
 
END
