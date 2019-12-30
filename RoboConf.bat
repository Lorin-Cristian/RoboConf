
@echo off

SET /p Input=Tasteaza nume calculatorului EX PROFIXXXXServer sau PROFIXXXXReceptie:
wmic computersystem where caption='PROFIXXXTIPPC' rename "%Input%"

SET /p Input=: Tasteaza nume workgrup EX PROFIXXXX:
wmic computersystem where name="%computername%" call joindomainorworkgroup name="%Input%"

exit
